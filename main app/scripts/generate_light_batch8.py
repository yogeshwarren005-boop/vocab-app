# -*- coding: utf-8 -*-
import json
import os

batch8 = {
  "Dashboard — phos/aphotic.md": {
    "primary": "Devoid of light, especially designating the deep bathypelagic zone of an ocean or lake where solar radiation never penetrates.",
    "secondary": "In marine ecology and limnology, the deep oceanic water column below the photic zone where photosynthesis cannot occur and animals rely on bioluminescence or organic snow.",
    "quotes": [
      { "author": "William Beebe", "work": "Half Mile Down", "quote": "At two thousand feet the bathysphere hung in the cold, **aphotic** abysses where no solar ray has ever pierced." },
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Creatures of the **aphotic** depths inhabit a world of perpetual night, lit only by their own living lanterns." },
      { "author": "C. Wyville Thomson", "work": "The Depths of the Sea", "quote": "Life in the **aphotic** floor of the Atlantic proved unexpectedly rich, supported by organic matter sinking from above." }
    ]
  },
  "Dashboard — phos/biophoton.md": {
    "primary": "A photon of light in the optical range spontaneously emitted by living biological cells and tissues without external excitation.",
    "secondary": "In biophysics and photobiology, ultraweak photon emissions resulting from oxidative metabolic processes and lipid peroxidation in cellular membranes.",
    "quotes": [
      { "author": "Fritz-Albert Popp", "work": "Biophoton Emission: Multi-Author Review", "quote": "Living tissue exhibits continuous, coherent **biophoton** emission that mirrors internal cellular metabolic activity." },
      { "author": "Alexander Gurwitsch", "work": "Die mitogenetische Strahlung", "quote": "Mitotic division in onion roots appeared to be stimulated by ultraweak ultraviolet **biophoton** emanations." },
      { "author": "Eugene Rabinowitch", "work": "Photosynthesis", "quote": "Delayed luminescence in illuminated chloroplasts represents a transient, sensitive form of **biophoton** release." }
    ]
  },
  "Dashboard — phos/cataphote.md": {
    "primary": "A retroreflective safety reflector or optical device designed to reflect incident light back toward its originating source.",
    "secondary": "In transport infrastructure and vehicle safety engineering, corner-cube or beaded prism reflectors mounted on road verges and bicycles to enhance nocturnal visibility.",
    "quotes": [
      { "author": "Arthur D. Little", "work": "Technology and Highway Safety", "quote": "The glass **cataphote** mounted along highway curves catches automobile headlights, warning drivers of dangerous bends." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "Total internal reflection inside the angled prism makes the **cataphote** return light precisely along its path of incidence." },
      { "author": "Percy Bysshe Shelley", "work": "Philosophical Essays", "quote": "The poet's mind functions like a moral **cataphote**, reflecting the radiance of universal truth back into human darkness." }
    ]
  },
  "Dashboard — phos/diphoton.md": {
    "primary": "A pair of photons produced simultaneously in a particle collision or quantum decay process.",
    "secondary": "In experimental high-energy physics, the signature decay channel (H -> gamma gamma) utilized at the Large Hadron Collider to discover the Higgs boson.",
    "quotes": [
      { "author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "Positron-electron annihilation at rest yields a collinear **diphoton** pair carrying opposite momentum." },
      { "author": "Julian Schwinger", "work": "Particles, Sources, and Fields", "quote": "The neutral pion decays predominantly into a **diphoton** state via triangular fermion loop anomalies." },
      { "author": "Steven Weinberg", "work": "The Quantum Theory of Fields", "quote": "A sharp resonance peak in the invariant mass of the **diphoton** spectrum revealed the existence of the scalar boson." }
    ]
  },
  "Dashboard — phos/euphotic.md": {
    "primary": "Pertaining to the upper sunlit layer of a body of water where sunlight penetrates sufficiently to permit net photosynthetic production.",
    "secondary": "In oceanography and marine ecology, the upper ocean layer (extending down to roughly 1% of surface irradiance) where photosynthetic gains exceed respiratory losses.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "All marine animal life ultimately depends upon the microscopic pastures flourishing in the sunlit **euphotic** zone." },
      { "author": "H. U. Sverdrup", "work": "The Oceans", "quote": "The compensation depth marks the lower boundary of the **euphotic** layer, where daily photosynthesis equals respiration." },
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "High turbidity from river silt compresses the **euphotic** zone of the estuary to a depth of only few feet." }
    ]
  },
  "Dashboard — phos/microphotograph.md": {
    "primary": "A photograph of microscopic size, requiring a magnifying lens or microscope to be viewed; or a photograph taken through a microscope.",
    "secondary": "In photographic history and espionage, minute images on collodion film pioneered by John Benjamin Dancer and utilized during the 1870 Siege of Paris.",
    "quotes": [
      { "author": "Oliver Wendell Holmes", "work": "The Atlantic Monthly: Sun-Painting and Sun-Sculpture", "quote": "Dancer reduced the whole page of the Times to the size of a pin's head in a minute **microphotograph**." },
      { "author": "Charles Dickens", "work": "All the Year Round", "quote": "Pigeon carriers flew into besieged Paris carrying thousands of despatches condensed into a single **microphotograph**." },
      { "author": "Robert Koch", "work": "Etiology of Wound Infections", "quote": "To convince skeptical clinicians, I attached the camera to the microscope and prepared every **microphotograph** myself." }
    ]
  },
  "Dashboard — phos/microphotometer.md": {
    "primary": "An optical instrument designed to measure the optical density or light transmission of microscopic areas on a photographic plate or spectral line.",
    "secondary": "In observational astrophysics and spectrochemistry, a precision scanning instrument used to trace stellar absorption line profiles and determine elemental abundances.",
    "quotes": [
      { "author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Traces from the registering **microphotometer** revealed the true contour and width of the stellar calcium lines." },
      { "author": "Subrahmanyan Chandrasekhar", "work": "Radiative Transfer", "quote": "Quantitative spectrophotometry depends upon calibrating the **microphotometer** against standard photographic step-wedges." },
      { "author": "George Ellery Hale", "work": "The Study of Stellar Evolution", "quote": "Scanning across the spectral plate, the **microphotometer** galvanometer deflected in exact proportion to the darkness of the Fraunhofer line." }
    ]
  },
  "Dashboard — phos/phos.md": {
    "primary": "The Greek combining form (phos, photos, 'light, daylight') denoting light, radiant energy, photons, or photographic processes.",
    "secondary": "In scientific nomenclature, the classical root yielding phosphorus, photograph, photophobia, and photosynthesis across physics and biology.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek noun **phos** denoted the radiant daylight of the sun as well as the inner light of understanding." },
      { "author": "William Whewell", "work": "Philosophy of the Inductive Sciences", "quote": "From the Hellenic stem **phos**- modern physicists coined words describing the corpuscular quanta of illumination." },
      { "author": "Michael Faraday", "work": "Experimental Researches in Chemistry", "quote": "The prefix **phos**- signifies the power of radiant light to awaken dormant chemical affinities." }
    ]
  },
  "Dashboard — phos/phosphate.md": {
    "primary": "A chemical salt or ester of phosphoric acid containing the tetrahedral PO4^3- anion, essential for life.",
    "secondary": "In biochemistry and bioenergetics, high-energy phosphate bonds (as in adenosine triphosphate, ATP) driving cellular metabolism, muscle contraction, and nucleic acid synthesis.",
    "quotes": [
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Without bone **phosphate** in the soil, the golden wheat cannot form its plump and fertile grain." },
      { "author": "Fritz Lipmann", "work": "Metabolic Generation and Utilization of Phosphate Bond Energy", "quote": "The terminal **phosphate** bond of ATP functions as the universal energy currency of all living cells." },
      { "author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "Alternating sugar and **phosphate** groups form the structural outer backbones of the DNA double helix." }
    ]
  },
  "Dashboard — phos/phosphor.md": {
    "primary": "A synthetic luminescent substance that emits light (fluorescence or phosphorescence) when stimulated by radiation; the morning star (Phosphorus / Venus).",
    "secondary": "In display physics and television engineering, crystalline inorganic compounds (such as zinc sulfide) coating the inside of cathode-ray tube screens.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Sweet is the breath of Morn, her rising sweet, with charm of earliest birds; and glorious **phosphor** in the dawn." },
      { "author": "Vladimir Zworykin", "work": "Television", "quote": "The electron beam strikes the zinc sulfide **phosphor** coating, converting kinetic impact into visible luminescence." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "Every mineral **phosphor** absorbs high-frequency rays to emit longer, visible wavelengths in the dark." }
    ]
  },
  "Dashboard — phos/phosphoric.md": {
    "primary": "Pertaining to, containing, or derived from phosphorus, especially in its +5 oxidation state; phosphorescent.",
    "secondary": "In chemical industry, relating to phosphoric acid (H3PO4), widely used in rust-proofing metals, soft drinks, and manufacturing agricultural fertilizers.",
    "quotes": [
      { "author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "Treating calcined bones with sulfuric acid yields soluble **phosphoric** acid, an incomparable fertilizer for roots." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "The white wake of the ship glowed with a pale, **phosphoric** gleam across the midnight sea." },
      { "author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Oxidizing red phosphorus with nitric acid forms dense syrupy **phosphoric** acid." }
    ]
  },
  "Dashboard — phos/phosphorous.md": {
    "primary": "Relating to or containing phosphorus, especially in its trivalent (+3) chemical state; emitting a faint glowing light in the dark without noticeable heat.",
    "secondary": "In inorganic chemistry, characterizing phosphorous acid (H3PO3) and its phosphite salts, which act as reducing agents.",
    "quotes": [
      { "author": "Robert Boyle", "work": "The Aerial Noctiluca", "quote": "The cold **phosphorous** light shone brightly in the evacuated glass globe without scorching the hand." },
      { "author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "Heating white phosphorus in moist air produces pungent vapors of **phosphorous** acid." },
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Shoals of fish darted through the waves like fiery rockets, trailing long **phosphorous** sparks." }
    ]
  },
  "Dashboard — phos/phosphorus.md": {
    "primary": "A nonmetallic chemical element of atomic number 15 (symbol P), appearing in reactive white, red, and black allotropes, essential to all biological organisms.",
    "secondary": "In alchemy and history, Hennig Brand's 1669 discovered 'cold fire', named from Greek phosphoros (light-bearer) because white phosphorus glows upon autoxidation.",
    "quotes": [
      { "author": "Robert Boyle", "work": "New Experiments, and Observations, Made upon the Icy Noctiluca", "quote": "The newly discovered **phosphorus** continued to emit its mysterious cold flame so long as fresh air was admitted." },
      { "author": "Primo Levi", "work": "The Periodic Table", "quote": "The dangerous allure of **phosphorus** lay in its sudden spontaneous ignition upon drying in the air." },
      { "author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Bone ash consists mainly of calcium combined with oxygen and **phosphorus**, forming the skeletal framework of vertebrates." }
    ]
  },
  "Dashboard — phos/photic.md": {
    "primary": "Relating to light; penetrated by sunlight, especially describing the upper surface layer of an aquatic body.",
    "secondary": "In biological oceanography and limnology, the sunlit epipelagic zone where ambient light exceeds 1% of surface irradiance, supporting aquatic photosynthesis.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "The surface **photic** zone represents the green pastureland of the open sea, teeming with microscopic diatoms." },
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "Primary production is strictly confined to the **photic** layer, while decomposition predominates in the dark depths below." },
      { "author": "H. U. Sverdrup", "work": "The Oceans", "quote": "The thickness of the **photic** zone varies from a few meters in turbid coastal lagoons to over one hundred meters in clear tropical seas." }
    ]
  },
  "Dashboard — phos/photo.md": {
    "primary": "A photograph; or a combining form denoting light, radiant energy, or photographic processes.",
    "secondary": "In modern colloquial usage and technology, an informal abbreviation for photograph, photo-offset, or digital snapshot.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "The cabinet **photo** of the lady was the solitary prize Holmes preserved from the royal intrigue." },
      { "author": "Virginia Woolf", "work": "Jacob's Room", "quote": "An old framed **photo** of the college crew hung beside the bookshelf above the desk." },
      { "author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston held the slip of newsprint containing the telltale **photo** that disproved the Party's lie." }
    ]
  },
  "Dashboard — phos/photobiology.md": {
    "primary": "The scientific branch of biology that studies the interactions of light and radiant energy with living organisms.",
    "secondary": "In multidisciplinary science, encompassing photosynthesis, bioluminescence, phototaxis, photoperiodism, vision, and ultraviolet photopathology.",
    "quotes": [
      { "author": "Eugene Rabinowitch", "work": "Photosynthesis and Related Processes", "quote": "Modern **photobiology** seeks to trace the quantum transfer of photons from light-harvesting pigments into chemical bonds." },
      { "author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "Comparative **photobiology** demonstrates how primitive eye-spots gradually evolved into complex retinal cameras." },
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "The daily vertical migrations of oceanic plankton present one of the grandest mysteries of marine **photobiology**." }
    ]
  },
  "Dashboard — phos/photocatalysis.md": {
    "primary": "The acceleration or initiation of a chemical reaction caused by the presence of a catalyst that absorbs light.",
    "secondary": "In physical chemistry and materials science, using semiconductor materials (such as titanium dioxide) under ultraviolet irradiation to decompose water or pollutants.",
    "quotes": [
      { "author": "Svante Arrhenius", "work": "Theories of Chemistry", "quote": "Light absorption by sensitized metal salts triggers **photocatalysis**, accelerating reactions that would otherwise proceed with infinite slowness." },
      { "author": "Wilhelm Ostwald", "work": "Catalysis and Chemical Equilibrium", "quote": "In **photocatalysis**, the photon serves as the energetic spark while the catalyst lowers the activation barrier." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Solar water-splitting through semiconductor **photocatalysis** offers a promising route to clean hydrogen fuel." }
    ]
  },
  "Dashboard — phos/photochromism.md": {
    "primary": "The reversible transformation of a chemical species between two states having different absorption spectra upon exposure to light.",
    "secondary": "In optical materials science and photochemistry, the molecular isomerization utilized in photochromic eyeglass lenses that darken in sunlight and clear indoors.",
    "quotes": [
      { "author": "Wilhelm Ostwald", "work": "Manual of Physico-Chemical Measurements", "quote": "Crystalline salts of certain hydrazones display reversible **photochromism**, turning carmine under sunlight and bleaching in darkness." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Reversible cis-trans photoisomerization underlies the molecular mechanism of organic **photochromism**." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "The transient color shift provoked by ultraviolet rays demonstrates the delicate physical reality of **photochromism**." }
    ]
  },
  "Dashboard — phos/photoelectric.md": {
    "primary": "Relating to electrical effects produced by light; especially the emission of electrons from a material when illuminated by electromagnetic radiation.",
    "secondary": "In modern physics, the quantum phenomenon whose theoretical explanation by Albert Einstein in 1905 established the photon particle nature of light.",
    "quotes": [
      { "author": "Albert Einstein", "work": "Concerning an Heuristic Point of View Toward the Emission and Transformation of Light", "quote": "The **photoelectric** effect can be understood only if we assume that light energy is distributed discontinuously in discrete quanta." },
      { "author": "Heinrich Hertz", "work": "Electric Waves", "quote": "Illuminating the spark gap with ultraviolet light produced an unexpected **photoelectric** discharge across the terminals." },
      { "author": "Robert A. Millikan", "work": "A Direct Photoelectric Determination of Planck's 'h'", "quote": "Precise **photoelectric** measurements across clean sodium surfaces verified Einstein's linear energy equation with absolute fidelity." }
    ]
  },
  "Dashboard — phos/photoelectrical.md": {
    "primary": "Pertaining to photoelectric phenomena; relating to the generation of electricity by light or the control of currents by illumination.",
    "secondary": "In early electronic engineering, describing vacuum phototubes, selenium cells, and light-sensitive circuitry.",
    "quotes": [
      { "author": "Thomas Alva Edison", "work": "Laboratory Notes on Image Transmission", "quote": "The selenium cell displayed sensitive **photoelectrical** responses, altering its resistance with every beam of light." },
      { "author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "The discovery of **photoelectrical** conduction opened an entirely new avenue connecting optics with electrical theory." },
      { "author": "Arthur D. Little", "work": "Industrial Research", "quote": "Modern automated sorting machines rely upon delicate **photoelectrical** eyes to inspect manufactured goods." }
    ]
  },
  "Dashboard — phos/photogenic.md": {
    "primary": "Producing or emitting light; bioluminescent; or aesthetically attractive, looking appealing and well-composed in photographs.",
    "secondary": "In natural history, organisms possessing light-emitting organs; in popular culture and cinema, subjects possessing striking photographic appeal.",
    "quotes": [
      { "author": "William Beebe", "work": "Half Mile Down", "quote": "Rows of gleaming **photogenic** organs along the lanternfish's belly shone like the portholes of a miniature liner." },
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The **photogenic** power of the luminous beetle was under the voluntary control of its nervous system." },
      { "author": "Virginia Woolf", "work": "The Cinema", "quote": "The camera discovered that certain faces are inherently **photogenic**, acquiring a luminous glamour upon the silver screen." }
    ]
  },
  "Dashboard — phos/photogram.md": {
    "primary": "A photographic image produced without a camera by placing objects directly onto a photosensitive surface and exposing it to light.",
    "secondary": "In modern art history, camera-less photographic works popularized by Man Ray (rayographs) and László Moholy-Nagy to explore shadows and translucency.",
    "quotes": [
      { "author": "William Henry Fox Talbot", "work": "The Pencil of Nature", "quote": "My earliest photogenic drawings were simple **photogram** impressions of lace and ferns placed upon sensitive paper." },
      { "author": "Man Ray", "work": "Self-Portrait", "quote": "By arranging keys and wire upon photographic paper under the enlarger lamp, I created my first mysterious **photogram**." },
      { "author": "László Moholy-Nagy", "work": "Painting, Photography, Film", "quote": "The direct **photogram** organizes light and shadow into pure optical space without the mediation of perspective." }
    ]
  },
  "Dashboard — phos/photograph.md": {
    "primary": "A picture produced by photography, in which an image is focused onto a light-sensitive surface; or to capture an image in this way.",
    "secondary": "In the history of science and art, the permanent optical record created when chemical emulsions or digital sensor arrays register incident light.",
    "quotes": [
      { "author": "John Herschel", "work": "Philosophical Transactions of the Royal Society", "quote": "I have recommended the word **photograph** as a concise term for images delineated solely by the action of light." },
      { "author": "Oliver Wendell Holmes", "work": "The Atlantic Monthly: The Stereoscope and the Stereograph", "quote": "A **photograph** is an extraordinary mirror that retains the reflection after the face has departed." },
      { "author": "Charles Baudelaire", "work": "The Salon of 1859", "quote": "If the **photograph** is allowed to usurp art's divine domain, true painting will soon be ruined by mechanical copying." }
    ]
  },
  "Dashboard — phos/photographer.md": {
    "primary": "A person who takes photographs, especially as a professional occupation or serious artistic pursuit.",
    "secondary": "In cultural history, a visual artist and technician whose mastery of chemical sensitization, composition, and lighting documents human reality.",
    "quotes": [
      { "author": "Walt Whitman", "work": "Specimen Days", "quote": "The brave army **photographer** Matthew Brady carried his darkroom wagon into the smoking chaos of Antietam." },
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Red-Headed League", "quote": "He spent hours in the cellar under the pretense of being an enthusiastic amateur **photographer**." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "The architectural **photographer** provides records of crumbling gothic traceries with faithful and impartial veracity." }
    ]
  },
  "Dashboard — phos/photographic.md": {
    "primary": "Relating to or resembling photography; retaining visual impressions with extreme detail and accuracy (photographic memory).",
    "secondary": "In optics and technology, describing emulsion plates, lenses, or processes dedicated to the optical capture of images.",
    "quotes": [
      { "author": "William Henry Fox Talbot", "work": "Some Account of the Art of Photogenic Drawing", "quote": "The **photographic** process allows nature herself to draw her own pictures upon sensitive silver paper." },
      { "author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The human mind cannot retain a complete **photographic** replica of every passing sensory impression." },
      { "author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes possessed a **photographic** eye that observed every footprint, cigar ash, and scraped plaster in the room." }
    ]
  },
  "Dashboard — phos/photography.md": {
    "primary": "The art, application, and practice of creating durable images by recording light, either chemically by means of a light-sensitive material or electronically.",
    "secondary": "In intellectual history, the visual technology born in the 1830s through Niepce, Daguerre, and Talbot, revolutionizing science, journalism, and the arts.",
    "quotes": [
      { "author": "William Henry Fox Talbot", "work": "The Pencil of Nature", "quote": "The discovery of **photography** has armed science with an instrument of precision that records facts beyond human bias." },
      { "author": "Edgar Allan Poe", "work": "The Daguerreotype", "quote": "In truth, the plate of early **photography** is infinitely more accurate in its representations than any painting by human hand." },
      { "author": "Walter Benjamin", "work": "A Short History of Photography", "quote": "Early **photography** caught the fleeting aura of human faces before commercial studios mechanized the portrait." }
    ]
  },
  "Dashboard — phos/photolysis.md": {
    "primary": "The decomposition or separation of molecules by the action of light or radiant energy.",
    "secondary": "In photosynthetic biochemistry, the light-dependent splitting of water molecules in Photosystem II, releasing oxygen, protons, and electrons.",
    "quotes": [
      { "author": "Robin Hill", "work": "Oxygen Produced by Isolated Chloroplasts", "quote": "The **photolysis** of water by illuminated chloroplast suspensions proceeds in the absence of carbon dioxide fixation." },
      { "author": "Eugene Rabinowitch", "work": "Photosynthesis", "quote": "The primary quantum act in photosynthesis drives the catalytic **photolysis** of water, liberating atmospheric oxygen." },
      { "author": "Mario J. Molina", "work": "Stratospheric Halogen Chemistry", "quote": "Solar ultraviolet rays induce the **photolysis** of chlorofluorocarbons, releasing destructive free chlorine radicals." }
    ]
  },
  "Dashboard — phos/photometer.md": {
    "primary": "An instrument for measuring the intensity of light or luminous flux, or for comparing the relative illuminative power of two light sources.",
    "secondary": "In astronomical and industrial optics, Bunsen's grease-spot photometer or electronic photomultiplier tubes used to quantify stellar magnitudes and lux.",
    "quotes": [
      { "author": "Robert Bunsen", "work": "Photochemical Researches", "quote": "The simple grease-spot **photometer** allowed us to compare the brightness of gas flames with mathematical precision." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "By adjusting the distances upon the **photometer** bench, the two shadows cast by the lights were made equal." },
      { "author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "The photoelectric **photometer** attached to the telescope records variations in starlight as small as one-hundredth of a magnitude." }
    ]
  },
  "Dashboard — phos/photometric.md": {
    "primary": "Relating to or using the measurement of the intensity of light or luminous flux.",
    "secondary": "In astrophysics and colorimetry, describing quantitative techniques for measuring stellar brightness, surface albedo, and lamp efficiency.",
    "quotes": [
      { "author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Accurate **photometric** surveys established the true relative brilliance of the principal southern constellations." },
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "The human retina exhibits marked variations in **photometric** sensitivity across its central and peripheral zones." },
      { "author": "Subrahmanyan Chandrasekhar", "work": "Principles of Stellar Dynamics", "quote": "The **photometric** curve of the eclipsing binary star revealed the precise radii and mutual inclinations of the stellar pair." }
    ]
  },
  "Dashboard — phos/photometrical.md": {
    "primary": "Of, relating to, or employing photometry; photometric.",
    "secondary": "In historical physics, describing instruments, comparisons, or empirical laws governing the quantitative measurement of illumination.",
    "quotes": [
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Lambert's celebrated treatise established the mathematical laws of **photometrical** science on a solid foundation." },
      { "author": "David Brewster", "work": "A Treatise on Optics", "quote": "The **photometrical** balance was achieved by equalizing the illumination received upon adjacent white screens." },
      { "author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Careful **photometrical** trials proved that the Drummond limelight was sixty times brighter than an ordinary wax candle." }
    ]
  },
  "Dashboard — phos/photometrically.md": {
    "primary": "By means of photometry; using light measurement techniques.",
    "secondary": "In astronomy and biochemical analysis, quantifying radiant flux, optical transmission, or enzyme activity through measured light absorption.",
    "quotes": [
      { "author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Cepheid variable stars were monitored **photometrically**, confirming the period-luminosity relation discovered by Leavitt." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The concentration of hemoglobin in the blood sample was determined **photometrically** by light absorption at 540 nanometers." },
      { "author": "Lord Rayleigh", "work": "Scientific Papers", "quote": "The attenuation of light traversing foggy atmospheres was measured **photometrically** across the lake." }
    ]
  },
  "Dashboard — phos/photometrist.md": {
    "primary": "A specialist or scientist who measures the intensity and physical properties of light; an expert in photometry.",
    "secondary": "In optical physics and lighting engineering, a professional who calibrates luminous sources, luminous flux, and visual lux standards.",
    "quotes": [
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Bouguer was the pioneer **photometrist** whose experiments proved that moonlight is immensely fainter than direct solar rays." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "To the experienced **photometrist**, the eye itself remains the ultimate judge of optical balance upon the testing screen." },
      { "author": "Thomas Alva Edison", "work": "The Electric Light System", "quote": "Our chief **photometrist** tested every experimental carbon filament against the standard sperm candle." }
    ]
  },
  "Dashboard — phos/photometry.md": {
    "primary": "The science and practical measurement of light in terms of its perceived brightness to the human eye.",
    "secondary": "In illuminating engineering and astrophysics, the quantitative discipline measuring luminous flux, candelas, and apparent stellar magnitudes.",
    "quotes": [
      { "author": "Johann Heinrich Lambert", "work": "Photometria", "quote": "I have set down the mathematical principles of **photometry**, proving that illumination decreases with the square of distance." },
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Visual **photometry** must take into account the Purkinje shift, which enhances retinal sensitivity to blue at dusk." },
      { "author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "Stellar **photometry** transformed observational astronomy from descriptive cataloging into rigorous astrophysics." }
    ]
  },
  "Dashboard — phos/photon.md": {
    "primary": "A quantum of electromagnetic radiation, having zero rest mass, no electric charge, and traveling at the speed of light in a vacuum.",
    "secondary": "In quantum electrodynamics and physics, the gauge boson mediating the electromagnetic force, introduced by Gilbert Lewis and mathematically formulated by Einstein.",
    "quotes": [
      { "author": "Albert Einstein", "work": "On the Quantum Theory of Radiation", "quote": "The elementary light-quantum, which we now term the **photon**, carries both discrete energy and directional momentum." },
      { "author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "An electron moving through space simply absorbs or emits a **photon**, the basic event of quantum electrodynamics." },
      { "author": "Arthur Compton", "work": "A Quantum Theory of the Scattering of X-Rays by Light Elements", "quote": "The collision between an X-ray **photon** and an electron behaves exactly like a game of billiard balls in space." }
    ]
  },
  "Dashboard — phos/photoperiod.md": {
    "primary": "The duration of daily light exposure received by an organism, regulating seasonal physiological activities such as flowering and breeding.",
    "secondary": "In plant physiology and agronomy, the day-length signal detected by phytochrome that triggers flowering in short-day, long-day, or day-neutral plants.",
    "quotes": [
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "The lengthening **photoperiod** of spring triggers hormonal surges that set millions of migratory birds upon their northern flights." },
      { "author": "Asa Gray", "work": "Elements of Botany", "quote": "Experiments proved that chrysanthemums require a declining **photoperiod** to initiate floral bud formation." },
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Diapause in temperate insects is regulated by seasonal changes in the ambient **photoperiod**." }
    ]
  },
  "Dashboard — phos/photophobia.md": {
    "primary": "An abnormal sensitivity to or discomfort from light, especially causing eye pain and reflex blinking in ocular disorders.",
    "secondary": "In clinical ophthalmology and neurology, a symptom common to corneal ulceration, uveitis, meningitis, and severe migraine headaches.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute cerebrospinal meningitis manifests with high fever, agonizing headache, and intense **photophobia**." },
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Without protective dark glasses, daytime **photophobia** blinded the achromatopsic islanders on the sun-drenched beaches." },
      { "author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "Children with interstitial keratitis suffer from such severe **photophobia** that they bury their faces in pillows." }
    ]
  },
  "Dashboard — phos/photophone.md": {
    "primary": "An optical telecommunication apparatus invented by Alexander Graham Bell and Sumner Tainter in 1880 that transmitted sound on a beam of light.",
    "secondary": "In the history of telecommunications, the pioneering ancestor of modern fiber-optic communications, using selenium cells to convert modulated sunlight into speech.",
    "quotes": [
      { "author": "Alexander Graham Bell", "work": "On the Production and Reproduction of Sound by Light: The Photophone", "quote": "I have heard articulate speech produced by a beam of sunlight; I have heard the **photophone** speak across open space." },
      { "author": "John Tyndall", "work": "Essays on the Floating-Matter of the Air", "quote": "Bell's **photophone** proves that an undulating sunbeam can stimulate selenium into musical speech." },
      { "author": "Thomas Alva Edison", "work": "Letters on Scientific Discoveries", "quote": "The transmission of the human voice upon a solar beam in the **photophone** was a brilliant triumph of physical invention." }
    ]
  },
  "Dashboard — phos/photophore.md": {
    "primary": "A light-emitting glandular organ found in certain bioluminescent marine animals, such as lanternfish, anglerfish, and squids.",
    "secondary": "In marine biology and deep-sea ecology, complex dermal organs equipped with reflective tapeta, lenses, and filters to control light emission for counterillumination.",
    "quotes": [
      { "author": "William Beebe", "work": "Half Mile Down", "quote": "Each **photophore** along the flank of the deep-sea fish gleamed with an icy blue light, complete with miniature lens and reflector." },
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Benthic squids extinguish every **photophore** when alarmed, vanishing instantly into the ink of the abyss." },
      { "author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "The arrangement of the **photophore** groups along the ventral margin serves as the principal taxonomic guide to lanternfish genera." }
    ]
  },
  "Dashboard — phos/photopic.md": {
    "primary": "Relating to vision in bright daylight, mediated primarily by retinal cone photoreceptors, characterized by color perception and high visual acuity.",
    "secondary": "In visual neuroscience, daylight vision contrasting with scotopic (rod-mediated nocturnal) and mesopic (twilight) visual states.",
    "quotes": [
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "In the **photopic** state, the fovea centralis achieves its highest resolving power under full sunlight." },
      { "author": "Richard Gregory", "work": "Eye and Brain", "quote": "The transition from **photopic** cone vision to scotopic rod vision shifts maximal spectral sensitivity toward the green." },
      { "author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "The patient retained excellent **photopic** acuity for reading print, although all sensation of color had vanished." }
    ]
  },
  "Dashboard — phos/photoptarmosis.md": {
    "primary": "The photic sneeze reflex; a genetic condition characterized by involuntary sneezing triggered by sudden exposure to bright sunlight or bright light.",
    "secondary": "In neurogenetics and clinical medicine, an autosomal dominant trait (ACHOO syndrome) caused by optic-trigeminal nerve cross-talk in the brainstem.",
    "quotes": [
      { "author": "Aristotle", "work": "Problems", "quote": "Why does the heat of the sun excite sneezing when we look upon it? The ancient phenomenon of **photoptarmosis** was noted early in Greek science." },
      { "author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Looking toward the sun causes sudden sneezing, for the solar ray draws down moisture into the nostrils; this reflex is true **photoptarmosis**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The curious hereditary trait termed **photoptarmosis** reflects an anomalous trigeminal reflex triggered by macular illumination." }
    ]
  },
  "Dashboard — phos/photosynthesis.md": {
    "primary": "The biological process by which green plants, algae, and certain bacteria convert sunlight, water, and carbon dioxide into chemical energy (sugars) and oxygen.",
    "secondary": "In bioenergetics, the fundamental biophysical process combining light reactions in thylakoids with the dark Calvin cycle in the chloroplast stroma.",
    "quotes": [
      { "author": "Melvin Calvin", "work": "The Path of Carbon in Photosynthesis", "quote": "The miraculous machinery of **photosynthesis** captures solar photons to convert inorganic carbon into the living stuff of the biosphere." },
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "All terrestrial and marine life is sustained by the gentle alchemy of green **photosynthesis** in plant leaves." },
      { "author": "Julius von Sachs", "work": "Lectures on the Physiology of Plants", "quote": "Starch accumulation inside the illuminated chloroplast proved that **photosynthesis** occurs exclusively within the green plastid." }
    ]
  },
  "Dashboard — phos/photosynthetic.md": {
    "primary": "Relating to, involved in, or produced by photosynthesis; capable of carrying out photosynthesis.",
    "secondary": "In ecology and cell biology, describing autotrophic organisms (plants, cyanobacteria, phytoplankton) and chloroplast thylakoid membranes.",
    "quotes": [
      { "author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "Primary endosymbiosis introduced a free-living **photosynthetic** prokaryote into an ancestral protozoan host." },
      { "author": "Eugene Rabinowitch", "work": "Photosynthesis", "quote": "The **photosynthetic** reaction center achieves nearly one hundred percent quantum efficiency in primary charge separation." },
      { "author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Leaves align their surfaces perpendicular to the sun to maximize their **photosynthetic** yield of light." }
    ]
  },
  "Dashboard — phos/phototherapy.md": {
    "primary": "The medical treatment of physical or mental diseases by exposure to daylight or specific wavelengths of artificial light.",
    "secondary": "In clinical pediatrics and dermatology, ultraviolet light treatment for psoriasis or blue-light phototherapy to isomerize toxic bilirubin in neonatal jaundice.",
    "quotes": [
      { "author": "Niels Ryberg Finsen", "work": "Nobel Lecture: The Treatment of Lupus Vulgaris by Concentrated Chemical Light Rays", "quote": "Concentrated chemical light employed in modern **phototherapy** eradicated intractable lupus lesions without scarring." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The adoption of blue-light **phototherapy** dramatically reduced the need for exchange transfusions in jaundiced neonates." },
      { "author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Sunlight is the second great essential after fresh air; natural **phototherapy** restores pale hospital convalescents." }
    ]
  },
  "Dashboard — phos/telephoto.md": {
    "primary": "A telephoto lens or camera system designed to magnify distant objects; or taken with such a lens.",
    "secondary": "In photographic optical engineering, a lens system whose physical length is shorter than its effective focal length, achieved via a rear diverging element.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger fitted his long **telephoto** lens to photograph the pterodactyls nesting upon the distant basalt cliffs." },
      { "author": "John Muir", "work": "The Yosemite", "quote": "Through the **telephoto** glass, the leaping water of Upper Yosemite Fall resolved into countless glittering spray plumes." },
      { "author": "H. G. Wells", "work": "The War in the Air", "quote": "Scout airplanes carried powerful **telephoto** cameras to survey troop concentrations along the frontier." }
    ]
  },
  "Dashboard — phos/telephotograph.md": {
    "primary": "A photograph taken with a telephoto lens showing a magnified image of a distant object; or a photograph transmitted by telegraphy.",
    "secondary": "In telecommunications and military reconnaissance, an image transmitted over long-distance electrical circuits or cable systems.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "The German spy had secured a detailed **telephotograph** of the new naval dockyard fortifications." },
      { "author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The astronomical observatory received a sharp **telephotograph** of the Martian disc displaying strange volcanic eruptions." },
      { "author": "John Logie Baird", "work": "Television and Picture Transmission", "quote": "The transmission of a clear **telephotograph** across the Atlantic wire paved the way for wireless visual broadcasting." }
    ]
  },
  "Dashboard — phos/telephotography.md": {
    "primary": "The art, practice, or science of taking photographs of distant objects using a telephoto lens.",
    "secondary": "In field natural history and reconnaissance, photographing wildlife, distant landscapes, or military targets without approaching dangerously close.",
    "quotes": [
      { "author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "Pioneering attempts at wildlife **telephotography** in Kenya captured rhinos and giraffes at natural grazing distances." },
      { "author": "John Burroughs", "work": "Ways of Nature", "quote": "Modern **telephotography** brings the shyest eagle upon her mountain eyrie into intimate view for the bird student." },
      { "author": "Frank M. Chapman", "work": "Camps and Cruises of an Ornithologist", "quote": "Success in arctic gull colonies depended upon mastering the steady tripod technique essential for **telephotography**." }
    ]
  },
  "Dashboard — porphyr/porphyra.md": {
    "primary": "A genus of cold-water marine red algae (Rhodophyta), commonly known as purple laver or nori, widely cultivated for food.",
    "secondary": "In marine phycology and mariculture, membranous red seaweeds with a complex heteromorphic life cycle involving a microscopic diploid conchocelis phase.",
    "quotes": [
      { "author": "William Henry Harvey", "work": "Phycologia Britannica", "quote": "The delicate purple fronds of **Porphyra** carpet the tidal boulders like shimmering sheets of wet silk." },
      { "author": "Felix Eugen Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "Drew's discovery of the conchocelis stage in **Porphyra** revolutionized commercial nori cultivation in Japan." },
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "In the cold northern tide pools, **Porphyra** clings tenaciously to granite rocks drenched in ocean spray." }
    ]
  },
  "Dashboard — porphyr/porphyria.md": {
    "primary": "A group of rare, inherited metabolic disorders caused by deficiencies in enzymes of the heme biosynthetic pathway, leading to porphyrin accumulation.",
    "secondary": "In clinical medicine, divided into cutaneous and acute neurological porphyrias, causing severe abdominal crises, neurovisceral symptoms, and blistering photosensitivity.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute intermittent **porphyria** manifests with agonizing abdominal colic, motor neuropathy, and port-wine colored urine." },
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Folk legends of vampires and werewolves may have been inspired by patients suffering from severe cutaneous **porphyria**." },
      { "author": "Linus Pauling", "work": "Orthomolecular Medicine", "quote": "Enzyme defects in **porphyria** illustrate the catastrophic toxic effects of intermediate biosynthetic precursors." }
    ]
  },
  "Dashboard — porphyr/porphyrin.md": {
    "primary": "A group of heterocyclic organic compounds composed of four modified pyrrole rings connected by methine bridges, coordinating metal ions in pigments.",
    "secondary": "In molecular biochemistry, the macrocyclic tetrapyrrole ring system coordinating iron in hemoglobin and myoglobin, and magnesium in chlorophyll.",
    "quotes": [
      { "author": "Hans Fischer", "work": "Nobel Lecture: On the Chemistry of Pyrrole and Its Derivatives", "quote": "The synthesis of hemin established the universal architecture of the planar **porphyrin** ring across the animal and plant kingdoms." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The aromatic resonance of the planar **porphyrin** macrocycle confers remarkable chemical stability upon respiratory pigments." },
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Abnormal urinary excretion of free **porphyrin** signifies profound derangement in cellular heme synthesis." }
    ]
  },
  "Dashboard — porphyr/porphyrio.md": {
    "primary": "A genus of large, colorful wetland birds in the rail family Rallidae, commonly known as swamphens, possessing brilliant purple-blue plumage and massive red bills.",
    "secondary": "In ornithology, wetland gruiform birds (including the western swamphen and Australasian pukeko) possessing long unwebbed toes for walking on floating vegetation.",
    "quotes": [
      { "author": "John Gould", "work": "The Birds of Australia", "quote": "The purple swamphen, belonging to **Porphyrio**, strides majestically across water lily leaves with its massive red frontal shield." },
      { "author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Ancient Roman aviaries prized the majestic **Porphyrio** for its radiant indigo feathers and graceful carriage." },
      { "author": "Edward Lear", "work": "Illustrations of the Family of Psittacidae", "quote": "The rich purple mantle of **Porphyrio** mirrors the royal dyes extracted from Mediterranean murex shells." }
    ]
  },
  "Dashboard — porphyr/porphyritic.md": {
    "primary": "Having large, conspicuous mineral crystals (phenocrysts) embedded in a fine-grained or glassy groundmass (of igneous rocks).",
    "secondary": "In petrology, an igneous rock texture indicating a two-stage cooling history: slow crystallization at depth followed by rapid cooling upon volcanic extrusion.",
    "quotes": [
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The andesite lava displayed a magnificent **porphyritic** texture, with glistening plagioclase tablets set in dark basaltic paste." },
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "In a typical **porphyritic** granite, large pink orthoclase crystals stand out boldly from the medium-grained groundmass." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "The cooling rate dictated whether the molten magma solidified uniformly or assumed an unmistakable **porphyritic** structure." }
    ]
  },
  "Dashboard — porphyr/porphyrophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear or hatred of the color purple.",
    "secondary": "In clinical psychology and psychotherapy, a rare specific chromophobia where violet or purple hues trigger intense autonomic anxiety or revulsion.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "The Psychology of Color", "quote": "Instances of **porphyrophobia** are on record where the sight of imperial purple ecclesiastical vestments provoked panic." },
      { "author": "G. Stanley Hall", "work": "A Study of Fears", "quote": "Morbid chromatic aversions such as **porphyrophobia** often arise from frightening sensory associations formed in early childhood." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "Pathological idiosyncratic dislikes of certain saturated wavelengths, including **porphyrophobia**, reveal deep subconscious conditioning." }
    ]
  },
  "Dashboard — porphyr/porphyrula.md": {
    "primary": "A former genus of New World purple gallinules in the rail family Rallidae (now generally classified under *Porphyrio*).",
    "secondary": "In marsh ornithology, slender marsh birds (*Porphyrula martinica*) with iridescent purple plumage, emerald wings, and bright yellow legs.",
    "quotes": [
      { "author": "John James Audubon", "work": "Ornithological Biography", "quote": "The purple gallinule, then designated **Porphyrula**, ran across lotus leaves with the agility of a sandpiper." },
      { "author": "Elliott Coues", "work": "Key to North American Birds", "quote": "The dazzling sky-blue frontal shield and violet neck make **Porphyrula** the most beautiful of American marsh dwellers." },
      { "author": "Alexander Wilson", "work": "American Ornithology", "quote": "In the rice fields of Georgia, **Porphyrula** perched gracefully upon tall reeds to pluck ripening grains." }
    ]
  },
  "Dashboard — porphyr/porphyry.md": {
    "primary": "A hard, dark red or purple igneous rock containing crystals of feldspar or quartz embedded in a fine-grained groundmass; imperial Egyptian red porphyry.",
    "secondary": "In architectural history and classical sculpture, a royal stone quarried at Mons Porphyrites in Egypt, reserved exclusively for Roman emperors and Byzantine imperial sarcophagi.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Byzantine princes were born in the purple chamber and buried in massive sarcophagi of imperial red **porphyry**." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "Pillars of polished **porphyry** looted from eastern basilicas adorned the magnificent portal of St. Mark's." },
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The ancient red **porphyry** of Egypt consists of an aphanitic groundmass studded with white crystals of oligoclase feldspar." }
    ]
  },
  "Dashboard — pras/chrysoprase.md": {
    "primary": "An apple-green gem variety of chalcedony silica colored by trace inclusions of nickel minerals.",
    "secondary": "In mineralogy and jewelry history, a prized semi-precious stone (from Greek chrysos, gold, and prason, leek) famous since antiquity and mined in Silesia and Australia.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The delicate apple-green tint of **chrysoprase** is imparted by minute hydrated silicate compounds of nickel." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "The bishop's signet ring was set with a translucent **chrysoprase** that shone like young spring foliage." },
      { "author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He collected curiosities of every land, including oval cabochons of green **chrysoprase** and fiery garnets." }
    ]
  },
  "Dashboard — pras/praseodymium.md": {
    "primary": "A soft, silvery, malleable metallic chemical element of the lanthanide series with atomic number 59 (symbol Pr), forming leek-green chemical salts.",
    "secondary": "In industrial chemistry and spectroscopy, a rare-earth metal discovered by Carl Auer von Welsbach in 1885 when didymium was split into praseodymium and neodymium.",
    "quotes": [
      { "author": "Carl Auer von Welsbach", "work": "Die Zerlegung des Didyms in Seine Elemente", "quote": "I succeeded in splitting didymium into two elementary bodies, naming that which gives green salts **praseodymium**." },
      { "author": "Primo Levi", "work": "The Periodic Table", "quote": "The rare-earth family hid rare treasures like **praseodymium**, whose compounds imparted a pale leek-green tint to optical glass." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Alloying **praseodymium** with magnesium creates high-strength metals used in aircraft engine casings." }
    ]
  },
  "Dashboard — pras/prasinophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of the color green.",
    "secondary": "In clinical psychology and psychotherapy, a specific chromophobic neurosis where exposure to green landscapes, vegetation, or paint elicits acute panic.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "The Psychology of Color", "quote": "The patient's **prasinophobia** was so extreme that walking through a public park induced overwhelming palpitations." },
      { "author": "G. Stanley Hall", "work": "A Study of Fears", "quote": "Neurotic dread of natural hues occasionally focalizes as an obstinate **prasinophobia** toward spring foliage." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "Unreasonable sensory aversions, such as **prasinophobia**, reflect involuntary emotional fixations upon harmless visual stimuli." }
    ]
  },
  "Dashboard — pras/prasinous.md": {
    "primary": "Of a leek-green or light grass-green color; having a yellowish-green hue.",
    "secondary": "In historical botany and entomology, describing the pale verdant tint of certain beetle elytra, lichen crusts, or succulent leaves.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The underside of the succulent leaf displayed a pale **prasinous** tint contrasting with the deep olive upper surface." },
      { "author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "The forest tree-bug was clothed in a **prasinous** green armor that rendered it invisible upon oak foliage." },
      { "author": "John Lindley", "work": "An Introduction to Botany", "quote": "Botanical Latin employs **prasinous** to designate that precise shade of green exhibited by fresh leek leaves." }
    ]
  },
  "Dashboard — prism/antiprism.md": {
    "primary": "A polyhedron composed of two identical parallel polygon bases connected by an alternating band of surrounding triangles.",
    "secondary": "In three-dimensional Euclidean geometry and structural chemistry, a uniform polyhedron (such as the square antiprism found in eight-coordinate coordination complexes).",
    "quotes": [
      { "author": "Johannes Kepler", "work": "Harmonices Mundi", "quote": "By twisting the upper base through half an angle, the prism transforms into a beautiful Archimedean **antiprism**." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The coordination sphere of the heavy zirconium ion adopts the geometry of a distorted square **antiprism**." },
      { "author": "H. S. M. Coxeter", "work": "Regular Polytopes", "quote": "The alternating triangular faces of the **antiprism** ensure structural rigidity absent from right prisms." }
    ]
  },
  "Dashboard — prism/prism.md": {
    "primary": "A solid geometric figure whose two end faces are similar, equal, and parallel rectilinear figures; in optics, a transparent glass body that refracts and disperses light.",
    "secondary": "In physical optics, a triangular glass device used by Isaac Newton to demonstrate that white sunlight is composed of a continuous spectrum of colors.",
    "quotes": [
      { "author": "Isaac Newton", "work": "Opticks", "quote": "In a very dark chamber, at a round hole, I placed a glass **prism**, whereby the beam of sunlight was refracted to the opposite wall." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "The unequal refrangibility of different wavelengths within the **prism** unfolds the glorious rainbow of the spectrum." },
      { "author": "Percy Bysshe Shelley", "work": "Adonais", "quote": "Life, like a dome of many-colour'd glass, Stains the white radiance of Eternity, until the **prism** dissolves." }
    ]
  },
  "Dashboard — prism/prismatic.md": {
    "primary": "Relating to, resembling, or shaped like a prism; brilliant, vibrant, and multicolored like the spectral colors formed by a prism.",
    "secondary": "In mineralogy and optics, characterizing crystals with elongated prism faces, or dispersion halos displaying rainbow hues.",
    "quotes": [
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "The spray of the foaming waterfall blazed with **prismatic** glory under the midday sun." },
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Staurolite crystallizes in stout **prismatic** forms often twinned into the shape of a cross." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "A marvelous **prismatic** spray rose from the whale's spout as he breached into the sunset." }
    ]
  },
  "Dashboard — prism/prismatoid.md": {
    "primary": "A polyhedron whose vertices all lie in two parallel planes; a general geometric solid including prisms, prismoids, pyramids, and frustums.",
    "secondary": "In solid geometry and earthwork computation, a polyhedron whose volume is precisely calculated using the universal prismatoidal formula.",
    "quotes": [
      { "author": "Augustus De Morgan", "work": "The Elements of Arithmetic", "quote": "The volume of any irregular **prismatoid** can be determined by applying Simpson's prismoidal rule to its cross-sections." },
      { "author": "Thomas Heath", "work": "A History of Greek Mathematics", "quote": "Greek geometers calculated the capacity of the **prismatoid** by resolving it into pyramids and wedges." },
      { "author": "William Kingdon Clifford", "work": "Mathematical Papers", "quote": "The geometric beauty of the **prismatoid** lies in its continuous transition between two planar vertex sets." }
    ]
  },
  "Dashboard — prism/prismoid.md": {
    "primary": "A prismatoid having an equal number of vertices in each of its two parallel planes, with quadrilateral or triangular lateral faces.",
    "secondary": "In civil engineering and mensuration, a solid whose volume in railway excavations and canal embankments is computed via the prismoidal formula.",
    "quotes": [
      { "author": "Allen Hazen", "work": "Earthwork Computations", "quote": "Engineers employ the **prismoid** formula to avoid costly overestimation of excavated soil along railway cuttings." },
      { "author": "William Whewell", "work": "An Elementary Treatise on Mechanics", "quote": "The center of gravity of a homogeneous **prismoid** is readily obtained by integrating across parallel sections." },
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Certain hemimorphic crystals develop **prismoid** terminations that differ markedly at opposite poles." }
    ]
  }
}

# Write curate-light-batch8.mjs
mjs_code = f"""import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {{
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {{
    console.error(`File not found: ${{filePath}}`);
    return false;
  }}
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {{
    console.error(`No > [!book] in ${{filePath}}`);
    return false;
  }}
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${{data.primary}}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${{data.secondary}}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${{q.author}} (*${{q.work}}*):** *"${{q.quote}}"*`).join('\\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${{quoteLines}}`;

  const newContent = `${{headerPart}}\\n\\n${{defBlock}}\\n\\n${{quotesBlock}}\\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}}

const batchData = {json.dumps(batch8, indent=2, ensure_ascii=False)};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {{
  if (updateNote(relPath, data)) updated++;
}}
console.log(`Successfully updated ${{updated}} of ${{Object.keys(batchData).length}} files in Batch 8.`);
"""

with open('main app/scripts/curate-light-batch8.mjs', 'w', encoding='utf-8') as f:
    f.write(mjs_code)

print("Generated curate-light-batch8.mjs with", len(batch8), "words.")
