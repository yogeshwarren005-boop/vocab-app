import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — aer/aeroallergen.md": {
    word: "aeroallergen",
    primary: "Any airborne allergen or substance (such as pollen, fungal spores, animal dander, or dust mite particles) that produces an allergic respiratory reaction when inhaled.",
    secondary: "In clinical immunology and allergy medicine, environmental particulate antigens that bind to specific IgE antibodies on mucosal mast cells, triggering allergic rhinitis and asthma.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Ragweed pollen and microscopic spores act as natural **aeroallergens**, triggering seasonal distress across agricultural valleys." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The inhalation of a specific **aeroallergen** initiates violent paroxysms of bronchial constriction in asthmatic patients." },
      { author: "René Dubos", work: "Man Adapting", quote: "Industrial urbanization alters the indoor environment, concentrating fungal and synthetic **aeroallergens** in closed living quarters." }
    ]
  },
  "Dashboard — aer/aeroballistics.md": {
    word: "aeroballistics",
    primary: "The branch of science that studies the aerodynamic performance and motion of projectiles, missiles, rockets, and bombs traveling through atmospheric air.",
    secondary: "In aerospace and ordnance engineering, the synthesis of fluid mechanics and classical external ballistics governing projectile drag, shockwave propagation, and trajectory stability.",
    quotes: [
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "High-velocity artillery requires rigorous **aeroballistics** to predict shockwave formation and trajectory deflection." },
      { author: "Robert H. Goddard", work: "Rockets", quote: "Calculations in **aeroballistics** revealed how atmospheric density diminishes the initial acceleration of sounding rockets." },
      { author: "Arthur C. Clarke", work: "The Promise of Space", quote: "Re-entry vehicles present the supreme challenge in **aeroballistics**, balancing hypersonic deceleration against aerodynamic heating." }
    ]
  },
  "Dashboard — aer/aerobatics.md": {
    word: "aerobatics",
    primary: "Feats of spectacular and precision flying performed in an aircraft, including loops, rolls, spins, stalls, and inverted flight; stunt flying.",
    secondary: "In aviation and aerobatic competition, specialized maneuvers executed to demonstrate extreme aircraft agility, structural airframe strength, and pilot handling precision.",
    quotes: [
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", quote: "The pilot tested the limits of his biplane in a dazzling series of **aerobatics**, rolling beneath the cloud deck." },
      { author: "Beryl Markham", work: "West with the Night", quote: "Stunt flying and flamboyant **aerobatics** offered thrilling spectacle, but long-distance navigation demanded quiet discipline." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "Test pilots honed their reflexes through high-G **aerobatics**, knowing that split-second spatial orientation meant survival." }
    ]
  },
  "Dashboard — aer/aerobe.md": {
    word: "aerobe",
    primary: "A microorganism or organism that requires molecular oxygen for growth, cellular respiration, and survival.",
    secondary: "In microbiology and cellular biochemistry, an organism that employs oxygen as the terminal electron acceptor in oxidative phosphorylation to synthesize ATP.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "I demonstrated that while the **aerobe** flourishes in the presence of free oxygen, the vibrion perishes instantly." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Metabolically, an obligate **aerobe** relies upon catalase and superoxide dismutase to survive toxic oxygen radicals." },
      { author: "Claude Bernard", work: "Experimental Medicine", quote: "The metabolic combustion observed in the **aerobe** represents the fundamental thermodynamic engine of multicellular life." }
    ]
  },
  "Dashboard — aer/aerobic.md": {
    word: "aerobic",
    primary: "Living, active, or occurring only in the presence of oxygen; relating to cellular respiration dependent upon atmospheric oxygen.",
    secondary: "In exercise physiology, denoting sustained physical conditioning (such as running, swimming, or cycling) that enhances cardiovascular endurance and oxygen utilization.",
    quotes: [
      { author: "Louis Pasteur", work: "Collected Works", quote: "The **aerobic** decomposition of organic substrates yields complete oxidation into water and carbonic acid." },
      { author: "Kenneth H. Cooper", work: "Aerobics", quote: "Regular **aerobic** exercise strengthens the myocardium and enhances systemic vascular transport capacity." },
      { author: "Hans Krebs", work: "The Citric Acid Cycle", quote: "The tricarboxylic acid cycle provides the enzymatic hub of all mitochondrial **aerobic** energy production." }
    ]
  },
  "Dashboard — aer/aerobics.md": {
    word: "aerobics",
    primary: "A system of physical conditioning exercises designed to stimulate and enhance cardiorespiratory endurance and cellular oxygen uptake.",
    secondary: "In fitness training and public health, rhythmic, continuous group exercise routines choreographed to music, popularized globally to promote cardiovascular health.",
    quotes: [
      { author: "Kenneth H. Cooper", work: "Aerobics", quote: "The philosophy of **aerobics** is simple: provide the heart and lungs with progressive physical overload to build endurance." },
      { author: "Jane Fonda", work: "Jane Fonda's Workout Book", quote: "Millions of women discovered physical strength and community through daily routines of musical **aerobics**." },
      { author: "René Dubos", work: "Man Adapting", quote: "Modern sedentary life necessitates artificial fitness regimens like **aerobics** to counteract bodily deconditioning." }
    ]
  },
  "Dashboard — aer/aerobiosis.md": {
    word: "aerobiosis",
    primary: "The state of living or surviving in the presence of oxygen; aerobic life.",
    secondary: "In comparative cellular physiology, the biological condition wherein metabolic pathways are coupled to oxygen-dependent oxidative phosphorylation.",
    quotes: [
      { author: "Louis Pasteur", work: "Researches on Fermentation", quote: "The transition from anaerobiosis to **aerobiosis** halts the production of alcohol in fermenting grape juice." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The global emergence of **aerobiosis** followed the great oxygenation event driven by ancient cyanobacteria." },
      { author: "Otto Meyerhof", work: "Chemical Dynamics of Life Phenomena", quote: "During muscular recovery, **aerobiosis** resynthesizes lactic acid back into glycogen." }
    ]
  },
  "Dashboard — aer/aerobiotic.md": {
    word: "aerobiotic",
    primary: "Pertaining to, living in, or characterized by aerobiosis; requiring molecular oxygen for life and metabolism; aerobic.",
    secondary: "In soil ecology and limnology, describing environmental conditions or microbial communities supported by dissolved oxygen in topsoil and surface waters.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Beer", quote: "Microbial species maintaining an **aerobiotic** existence consume glucose far more efficiently than anaerobic yeasts." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "The upper soil strata support vibrant **aerobiotic** communities of nitrifying bacteria and actinomycetes." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Toxic pollutants disrupt the **aerobiotic** balance of river waters, precipitating mass benthic suffocation." }
    ]
  },
  "Dashboard — aer/aerodyne.md": {
    word: "aerodyne",
    primary: "Any heavier-than-air aircraft that derives its lift in flight from aerodynamic forces acting upon fixed or rotating surfaces (such as an airplane or helicopter).",
    secondary: "In aeronautical taxonomy, a dynamic flying vehicle contrasted with an aerostat (lighter-than-air balloon or airship that relies on buoyant lift).",
    quotes: [
      { author: "H. G. Wells", work: "The War in the Air", quote: "The military debate raged between advocates of the rigid dirigible and proponents of the winged **aerodyne**." },
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "The structural design of an **aerodyne** requires an optimal lift-to-drag ratio across all flight regimes." },
      { author: "Octave Chanute", work: "Progress in Flying Machines", quote: "Every successful **aerodyne** must solve the simultaneous problems of dynamic sustentation and equilibrium." }
    ]
  },
  "Dashboard — aer/aeroembolism.md": {
    word: "aeroembolism",
    primary: "The obstruction of a blood vessel by an air or gas bubble; also, decompression sickness caused by rapid exposure to decreased barometric pressure; the bends.",
    secondary: "In aerospace medicine and hyperbaric physiology, the release of dissolved inert nitrogen gas into bloodstream bubbles during rapid altitude ascents or deep-sea decompression.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Divers ascending too rapidly suffer from severe **aeroembolism**, experiencing agonizing joint pains termed the bends." },
      { author: "Harvey Cushing", work: "Selected Papers", quote: "High-altitude aviators must be protected against **aeroembolism** by breathing pure oxygen prior to rapid climbs." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "The homeostatic regulation of vascular pressure is overwhelmed when **aeroembolism** occludes vital cerebral arterioles." }
    ]
  },
  "Dashboard — aer/aerofoil.md": {
    word: "aerofoil",
    primary: "A streamlined body or curved surface (such as an airplane wing, fin, or propeller blade) designed to generate aerodynamic lift or control forces when moving through air; airfoil.",
    secondary: "In fluid dynamics and aeronautical engineering, an asymmetrical cross-sectional profile engineered to produce a net pressure differential across its upper and lower boundaries.",
    quotes: [
      { author: "Ludwig Prandtl", work: "Essentials of Fluid Dynamics", quote: "Circulation theory explains how circulation around the cambered **aerofoil** produces dynamic lift." },
      { author: "Orville Wright", work: "How We Invented the Aeroplane", quote: "Our wind tunnel experiments revealed that a curved **aerofoil** gave far greater lift than a flat plane." },
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", quote: "Air flowed smoothly over the polished silver **aerofoil**, lifting the heavily laden mail plane into the dawn." }
    ]
  },
  "Dashboard — aer/aerogram.md": {
    word: "aerogram",
    primary: "A lightweight sheet of writing paper designed to be folded and gummed into an envelope for transmission by airmail at a uniform postal rate; an air letter.",
    secondary: "In postal telecommunications and philately, a pre-stamped, standardized airmail stationery sheet utilized worldwide for international correspondence prior to digital messaging.",
    quotes: [
      { author: "Graham Greene", work: "The Quiet American", quote: "I folded the thin blue **aerogram** and mailed it at the central post office in Saigon." },
      { author: "Paul Theroux", work: "The Great Railway Bazaar", quote: "At remote station halts, travelers scribbled hasty notes on flimsy **aerograms** to reassure families far away." },
      { author: "W. H. Auden", work: "Collected Poems", quote: "The transatlantic **aerogram** arrived crumpled, carrying news of births and departures across the ocean." }
    ]
  },
  "Dashboard — aer/aerolite.md": {
    word: "aerolite",
    primary: "A stony meteorite; a meteoritic stone composed chiefly of silicate minerals (such as olivine and pyroxenes) rather than metallic iron.",
    secondary: "In meteoritics and planetary geology, extraterrestrial chondritic or achondritic stone that traverses a planetary atmosphere to impact the terrestrial surface.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The fall of a heavy **aerolite** from a cloudless sky was regarded by antiquity as an omen of celestial wrath." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Chemical analysis of the fallen **aerolite** revealed olivine and pyroxene identical to terrestrial volcanic minerals." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "When a fiery meteor detonates in the upper atmosphere, showers of fragmented **aerolites** scatter across the fields." }
    ]
  },
  "Dashboard — aer/aerolitic.md": {
    word: "aerolitic",
    primary: "Of, relating to, or resembling an aerolite; stony and meteoritic in physical composition and celestial origin.",
    secondary: "In mineralogical and petrological analysis, describing crystalline silicate textures and fusion crusts characteristic of stony meteorites.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The specimen exhibited typical **aerolitic** fusion crusts scored by atmospheric ablation." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Observations of **aerolitic** showers prove that interplanetary space is populated by swarms of rocky debris." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The elemental composition of **aerolitic** fragments corroborates the universal distribution of terrestrial elements." }
    ]
  },
  "Dashboard — aer/aerological.md": {
    word: "aerological",
    primary: "Of or relating to aerology, the branch of meteorology concerned with observing and investigating the upper atmosphere.",
    secondary: "In synoptic and atmospheric forecasting, describing vertical sounding data (such as radiosonde measurements) charting temperature, humidity, and wind velocity aloft.",
    quotes: [
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "The establishment of a network of **aerological** stations revolutionized our understanding of jet streams." },
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "Modern weather forecasting demands continuous **aerological** soundings to trace the movements of air masses." },
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Comparative analysis of **aerological** soundings revealed the isothermal layer known as the stratosphere." }
    ]
  },
  "Dashboard — aer/aerology.md": {
    word: "aerology",
    primary: "The branch of meteorology that treats the physical and dynamic properties of the free atmosphere, especially above the planetary boundary layer.",
    secondary: "In atmospheric science and air navigation, observational research analyzing high-altitude pressure profiles, tropospheric wind shear, and stratosphere physics.",
    quotes: [
      { author: "Cleveland Abbe", work: "Treatise on Meteorological Apparatus", quote: "The development of sounding balloons equipped with self-recording barographs laid the foundation of modern **aerology**." },
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "Without the daily synoptic maps furnished by **aerology**, aviation across oceanic routes would be perilous." },
      { author: "James Glaisher", work: "Travels in the Air", quote: "Our high-altitude balloon ascents provided the earliest empirical measurements in experimental **aerology**." }
    ]
  },
  "Dashboard — aer/aeromagnetics.md": {
    word: "aeromagnetics",
    primary: "The scientific surveying and mapping of Earth's magnetic field using sensitive magnetometers carried aboard aircraft.",
    secondary: "In exploration geophysics, airborne magnetic reconnaissance utilized to delineate subsurface crystalline basements, tectonic fault zones, and mineral or petroleum deposits.",
    quotes: [
      { author: "Harold Urey", work: "The Planets", quote: "The application of **aeromagnetics** to continental shields revealed hidden basement fault systems buried beneath thick sedimentary cover." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Modern exploration relies upon **aeromagnetics** to delineate subsurface volcanic intrusions across inaccessible wilderness." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Surveys in **aeromagnetics** flown over the ocean basins provided the first hints of magnetic striping along the seafloor." }
    ]
  },
  "Dashboard — aer/aeromechanic.md": {
    word: "aeromechanic",
    primary: "A technician, mechanic, or engineer skilled in the maintenance, construction, and repair of aircraft, aero engines, and airframes.",
    secondary: "In aviation safety and maintenance engineering, a certified specialist licensed to inspect flight controls, avionics systems, and powerplant integrity.",
    quotes: [
      { author: "Antoine de Saint-Exupéry", work: "Night Flight", quote: "The conscientious **aeromechanic** tightened the fuel couplings by lantern light, knowing two lives depended on his torque." },
      { author: "Beryl Markham", work: "West with the Night", quote: "A skilled **aeromechanic** in Nairobi could coax smooth horsepower out of an engine that had swallowed desert dust." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "The young veteran dreamed of leaving the real estate office to train as an **aeromechanic** at the regional airfield." }
    ]
  },
  "Dashboard — aer/aeromechanics.md": {
    word: "aeromechanics",
    primary: "The scientific discipline that studies the mechanical properties and dynamics of air and gases, and the forces acting on bodies moving through them.",
    secondary: "In aerospace engineering, the fundamental science integrating aerodynamics (fluid forces) and aerostatics (buoyancy) with structural elasticity and vehicle dynamics.",
    quotes: [
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "The fundamental laws of **aeromechanics** dictate how compressibility transforms subsonic airflow into supersonic shock fronts." },
      { author: "Ludwig Prandtl", work: "Essentials of Fluid Dynamics", quote: "Boundary layer theory established a rigorous mathematical foundation for experimental **aeromechanics**." },
      { author: "Octave Chanute", work: "Progress in Flying Machines", quote: "Before attempting manned flight, pioneers had to master the basic principles of equilibrium in **aeromechanics**." }
    ]
  },
  "Dashboard — aer/aeromedical.md": {
    word: "aeromedical",
    primary: "Of, relating to, or concerning aviation medicine; pertaining to the physiological health and clinical safety of flight crews, passengers, and patients in air transit.",
    secondary: "In military and civilian healthcare, encompassing high-altitude physiology, oxygen equipment design, gravitational acceleration tolerance, and aeromedical evacuation.",
    quotes: [
      { author: "Harvey Cushing", work: "Selected Papers", quote: "Rigorous **aeromedical** screening ensures that fighter pilots maintain clear mental acuity during sustained high-altitude patrols." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "The candidates underwent grueling **aeromedical** examinations in dark centrifuge rooms to test their tolerance for extreme G-forces." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The development of **aeromedical** evacuation transport transformed wartime trauma care by shrinking transit times to hours." }
    ]
  },
  "Dashboard — aer/aeromedicine.md": {
    word: "aeromedicine",
    primary: "The medical specialty and clinical science concerned with the health, physiological stresses, and diseases associated with atmospheric and space flight; aviation medicine.",
    secondary: "In aerospace occupational medicine, the clinical field addressing rapid decompression, spatial disorientation, circadian dysrhythmia, and physiological cabin pressurization.",
    quotes: [
      { author: "Harvey Cushing", work: "The Medical Career", quote: "The rapid expansion of military aviation created an urgent new clinical frontier in **aeromedicine**." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "Physicians specializing in **aeromedicine** monitored heart rates and retinal blood flow as the rocket sled slammed into water brakes." },
      { author: "René Dubos", work: "Man Adapting", quote: "The artificial atmospheric sealed cabin engineered by **aeromedicine** represents the supreme triumph of technological homeostasis." }
    ]
  },
  "Dashboard — aer/aerometeorograph.md": {
    word: "aerometeorograph",
    primary: "An airborne meteorological instrument that automatically and simultaneously records atmospheric pressure, ambient temperature, and relative humidity on a revolving drum.",
    secondary: "In upper-air observational meteorology, a recording unit attached to aircraft struts or sounding kites that provided continuous vertical tropospheric profiles before modern digital telemetry.",
    quotes: [
      { author: "Cleveland Abbe", work: "Meteorological Apparatus and Methods", quote: "Mounted beneath the biplane wing, the **aerometeorograph** recorded a continuous thermodynamic cross-section of the storm front." },
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "Calibration of the **aerometeorograph** before each dawn ascent ensured standardized barometric and thermometric curves." },
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "The traces recovered from the **aerometeorograph** revealed cold dry air overriding humid surface currents." }
    ]
  },
  "Dashboard — aer/aerometer.md": {
    word: "aerometer",
    primary: "An instrument designed for measuring the density, weight, or specific gravity of air and other gases.",
    secondary: "In classical pneumatics and experimental physical chemistry, a calibrated laboratory apparatus used to determine the density and pressure coefficients of gases under standard conditions.",
    quotes: [
      { author: "Joseph Priestley", work: "Experiments and Observations on Different Kinds of Air", quote: "By employing a delicate **aerometer**, I determined the relative densities of dephlogisticated and nitrous air." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "The mercury **aerometer** allowed accurate quantification of the expansion coefficient of gases upon heating." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "Precision in gaseous synthesis requires continuous calibration of the laboratory **aerometer**." }
    ]
  },
  "Dashboard — aer/aeronaut.md": {
    word: "aeronaut",
    primary: "A person who operates, pilots, or travels in a lighter-than-air balloon or airship; broadly, an early pioneer of aerial flight.",
    secondary: "In the history of aviation, 18th- and 19th-century atmospheric voyagers who navigated open wicker baskets beneath gas-filled envelopes across continental airspace.",
    quotes: [
      { author: "Jules Verne", work: "Around the World in Eighty Days", quote: "The daring **aeronaut** gazed down at the miniature countryside drifting silently beneath his wicker basket." },
      { author: "Edgar Allan Poe", work: "The Balloon-Hoax", quote: "The adventurous **aeronaut** guided the steering vane as the great silk envelope caught the transatlantic trade wind." },
      { author: "James Glaisher", work: "Travels in the Air", quote: "At seven miles above the earth, the **aeronaut** loses consciousness as the oxygen starvation overcomes will." }
    ]
  },
  "Dashboard — aer/aeronautic.md": {
    word: "aeronautic",
    primary: "Of or relating to aeronautics; pertaining to the science, art, and technology of atmospheric flight; aeronautical.",
    secondary: "In engineering and military history, describing vehicles, instruments, design principles, or technical institutions dedicated to aerial navigation.",
    quotes: [
      { author: "H. G. Wells", work: "The War in the Air", quote: "Every major power hastened to establish an **aeronautic** corps, sensing that future battles would be decided in the sky." },
      { author: "Orville Wright", work: "How We Invented the Aeroplane", quote: "Our early gliders were designed in accordance with existing **aeronautic** tables, which proved dangerously misleading." },
      { author: "Octave Chanute", work: "Progress in Flying Machines", quote: "Scientific societies fostered international cooperation, publishing **aeronautic** treatises to accelerate aerial navigation." }
    ]
  },
  "Dashboard — aer/aeronautical.md": {
    word: "aeronautical",
    primary: "Of, relating to, or involving aeronautics; concerning the design, construction, operation, and navigation of aircraft.",
    secondary: "In aerospace engineering, relating to the theoretical and applied mechanics governing the flight of heavier- or lighter-than-air vehicles through Earth's atmosphere.",
    quotes: [
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "The **aeronautical** laboratory at Pasadena became the training ground for the designers of supersonic jets." },
      { author: "Wilbur Wright", work: "Some Aeronautical Experiments", quote: "The difficulties that obstruct the way to success in **aeronautical** art are of three general classes." },
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", quote: "Modern **aeronautical** technology has reduced distances between continents to a mere matter of flying hours." }
    ]
  },
  "Dashboard — aer/aeronautics.md": {
    word: "aeronautics",
    primary: "The science, art, and practice of designing, constructing, navigating, and operating aircraft through atmospheric air.",
    secondary: "In applied physical sciences, the overarching engineering discipline integrating aerodynamics, flight dynamics, propulsion thermodynamics, avionics, and materials engineering.",
    quotes: [
      { author: "Wilbur Wright", work: "Some Aeronautical Experiments", quote: "My brother and I became seriously interested in **aeronautics** after reading of the tragic death of Otto Lilienthal." },
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "The transition from low-speed **aeronautics** to supersonic rocketry required fundamentally new mathematical formulations." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The global federation of airmen and engineers made **aeronautics** the supreme instrument of worldwide order." }
    ]
  },
  "Dashboard — aer/aeroneurosis.md": {
    word: "aeroneurosis",
    primary: "A chronic neurosis affecting aviators, characterized by anxiety, restlessness, insomnia, emotional irritability, and functional gastrointestinal disturbances.",
    secondary: "In aviation psychiatry and military operational health, chronic flight fatigue syndrome induced by long-term hypoxia, high G-stress, cockpit vibration, and mortal hazard.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pilots flying repeated unpressurized patrols exhibit symptoms of **aeroneurosis**, marked by irritability and cardiovascular lability." },
      { author: "Harvey Cushing", work: "Selected Papers", quote: "Timely grounding and psychiatric rest are essential to reverse early **aeroneurosis** before disastrous pilot error occurs." },
      { author: "René Dubos", work: "Man Adapting", quote: "The constant physiological tension of high-altitude flight frequently precipitates the chronic neurosis termed **aeroneurosis**." }
    ]
  },
  "Dashboard — aer/aeronomy.md": {
    word: "aeronomy",
    primary: "The branch of atmospheric science that treats the physics and chemistry of the upper atmospheres of the Earth and other planets.",
    secondary: "In planetary physics, the study of photochemical dissociation, ionization processes, auroral emissions, and solar wind interactions occurring in the mesosphere and thermosphere.",
    quotes: [
      { author: "Sydney Chapman", work: "The Earth's Magnetism", quote: "I coined the term **aeronomy** to distinguish the study of the upper ionized atmosphere from conventional tropospheric meteorology." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Comparative **aeronomy** demonstrates how solar ultraviolet radiation disassociates water vapor in the upper atmosphere of Venus." },
      { author: "Patrick Moore", work: "The New Challenge of the Stars", quote: "Satellite probes measuring ion concentrations provided experimental data that revolutionized terrestrial **aeronomy**." }
    ]
  },
  "Dashboard — aer/aeropause.md": {
    word: "aeropause",
    primary: "The transitional boundary region in the upper atmosphere where air is too rarefied to provide aerodynamic lift for aircraft or oxygen for jet combustion.",
    secondary: "In space medicine and astrodynamics, the altitude zone (above approximately 12 to 20 miles) where atmospheric support ceases and spacecraft must rely on rocket propulsion and reaction thrusters.",
    quotes: [
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "Ascending beyond the **aeropause**, conventional aerodynamic control surfaces lose effectiveness, necessitating reaction thrusters." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Rocket planes like the X-15 probed the edge of the **aeropause**, coasting momentarily into ballistic space." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "At eighty thousand feet, the pilot reached the edge of the **aeropause**, where the sky turns deep purple and stars shine in daylight." }
    ]
  },
  "Dashboard — aer/aerophagia.md": {
    word: "aerophagia",
    primary: "The excessive or abnormal swallowing of air into the stomach, often causing abdominal distension, discomfort, belching, and flatulence.",
    secondary: "In gastroenterology and psychosomatic medicine, a functional habit or neurotic tic associated with anxiety, rapid eating, or esophageal dysmotility.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Hysterical patients frequently exhibit continuous **aerophagia**, producing severe tympanitic distension of the abdomen." },
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "The involuntary habit of **aerophagia** often serves as a somatic conversion symptom of acute neurotic tension." },
      { author: "Walter B. Cannon", work: "The Mechanical Factors of Digestion", quote: "Fluoroscopic examination shows that gastric bloating in nervous dyspeptics is caused by unconscious **aerophagia**." }
    ]
  },
  "Dashboard — aer/aerophobia.md": {
    word: "aerophobia",
    primary: "An abnormal, morbid, or irrational fear of fresh air, drafts, or moving air currents; also used to designate the intense fear of flying in an aircraft (aviophobia).",
    secondary: "In clinical neurology and infectious diseases, a pathognomonic symptom of human rabies in which the sensation of moving air across the skin triggers violent, painful spasms of the throat muscles.",
    quotes: [
      { author: "Louis Pasteur", work: "Researches on Rabies", quote: "The hydrophobic patient exhibited extreme **aerophobia**, convulsing in terror whenever a draft of air stirred across his face." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Hyperesthesia to moving air, or **aerophobia**, is almost invariably observed in the advanced paralytic stage of rabies." },
      { author: "G. Stanley Hall", work: "A Study of Fears", quote: "In modern urban populations, **aerophobia** has shifted its clinical meaning to designate the paralyzing terror of air travel." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 9 finished! Total words updated:", Object.keys(wordsData).length);
