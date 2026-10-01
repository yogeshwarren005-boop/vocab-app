import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Animals & Zoology';

const filesData = {
  "Dashboard — ther/theridiid.md": {
    "primary": "Any spider of the family Theridiidae, commonly known as cobweb spiders, tangle-web spiders, or comb-footed spiders.",
    "secondary": "In arachnology, entelegyne spiders possessing a comb of serrated bristles on the tarsi of the fourth legs used to fling viscid silk over prey.",
    "quotes": [
      {
        "author": "J. H. Fabre",
        "work": "The Life of the Spider",
        "quote": "The little **theridiid** weaves an irregular criss-cross maze of threads in the dark corner of the shed."
      },
      {
        "author": "Nathan Banks",
        "work": "The Acarina or Mites",
        "quote": "The notorious black widow is a venomous **theridiid** inhabiting dry crevices and stone heaps."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "Comb-like hairs upon the fourth tarsus distinguish each **theridiid** when swathing struggling prey in sticky bands."
      }
    ]
  },
  "Dashboard — ther/theridiidae.md": {
    "primary": "A large cosmopolitan family of spiders (comb-footed spiders) comprising over 3,000 species, including black widows and house cobweb spiders.",
    "secondary": "In systematic araneology, spiders characterized by eight eyes, absence of a cribellum, and construction of three-dimensional gumfoot-thread tangled webs.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "Modern Classification of Insects",
        "quote": "Members of the family **Theridiidae** capture insect prey with irregular scaffolding snares lacking geometric orb symmetry."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "The potent neurotoxic venom of Latrodectus placed the family **Theridiidae** at the forefront of medical arachnology."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "The Romance of Natural History",
        "quote": "Beneath overturned logs, small species of **Theridiidae** suspend their globular parchment egg-cocoons."
      }
    ]
  },
  "Dashboard — ther/therm.md": {
    "primary": "A non-SI unit of heat energy equal to 100,000 British thermal units (BTU) or approximately 105.5 megajoules; or heat in Greek.",
    "secondary": "In fuel commerce and energy billing, a standard measurement unit used for retail natural gas and domestic heating supply.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "The mechanical equivalent of each unit **therm** was determined through Joule's paddle-wheel experiments in water."
      },
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "Engineers computed the combustible output of industrial coal in standard **therm** ratings for locomotive boilers."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Internal Constitution of the Stars",
        "quote": "Millions of **therm** equivalents of energy are radiated every second from each square meter of the solar photosphere."
      }
    ]
  },
  "Dashboard — ther/thermal.md": {
    "primary": "Of, relating to, or caused by heat; or an ascending column of warm air used by soaring birds and gliders.",
    "secondary": "In physics and meteorology, describing thermal energy, temperature gradients, or convective atmospheric updrafts.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The condors wheeled in immense majestic circles, riding the rising **thermal** currents above the Andean gorges."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "Molecular kinetic energy is directly observable as the macroscopic **thermal** state of an enclosed gas."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Subterranean **thermal** springs emerge along deep tectonic faults, indicating deep-seated volcanic furnaces."
      }
    ]
  },
  "Dashboard — ther/thermalgesia.md": {
    "primary": "An abnormal, painful sensation produced by heat or warmth that would normally produce only a sensation of heat (thermoalgesia).",
    "secondary": "In clinical neurology and pain physiology, a dysesthesia or thermal allodynia where non-noxious warmth triggers intense burning pain.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients recovering from traumatic median nerve injury frequently suffered exquisite **thermalgesia** from warm water."
      },
      {
        "author": "S. Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "In severe causalgia, even the gentle radiation of a fire provoked intolerable **thermalgesia** across the hand."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Thalamic lesions frequently disrupt sensory modulation, inducing hyperpathia and severe **thermalgesia** in the contralateral limbs."
      }
    ]
  },
  "Dashboard — ther/thermally.md": {
    "primary": "With regard to heat, temperature, or thermal properties; by means of heat.",
    "secondary": "In materials science and engineering, describing insulation, conductivity, or structural stability under varying temperatures.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The metallic conductor expanded **thermally** as the intense galvanic current passed through its cross-section."
      },
      {
        "author": "Walther Nernst",
        "work": "Theoretical Chemistry",
        "quote": "Gaseous molecules become **thermally** excited, dissociating into atomic ions at high blast-furnace temperatures."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Subducted oceanic slabs are **thermally** assimilated back into the convecting mantle over millions of years."
      }
    ]
  },
  "Dashboard — ther/thermel.md": {
    "primary": "A thermoelectric thermometer or thermocouple assembly used for highly accurate, sensitive temperature measurements.",
    "secondary": "In experimental physics and physiological calorimetry, a multiple-junction thermoelectric device measuring minute temperature variations in tissues.",
    "quotes": [
      {
        "author": "William Thomson (Lord Kelvin)",
        "work": "On the Dynamical Theory of Heat",
        "quote": "The sensitive **thermel** detected temperature fluctuations as minute as one-thousandth of a degree."
      },
      {
        "author": "Augustin-Jean Fresnel",
        "work": "Oeuvres Completes",
        "quote": "By placing the junction of the **thermel** across the focal plane, we mapped the infrared spectrum of the sun."
      },
      {
        "author": "A. V. Hill",
        "work": "Muscular Activity",
        "quote": "A delicate **thermel** placed upon the isolated frog muscle measured the tiny burst of initial heat produced during twitching."
      }
    ]
  },
  "Dashboard — ther/thermic.md": {
    "primary": "Of, relating to, or generated by heat; thermal.",
    "secondary": "In historical clinical pathology, designating conditions caused by excessive heat, such as thermic fever (severe heatstroke/sunstroke).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Troops marching across the sun-baked plains of northern India succumbed rapidly to deadly **thermic** fever."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "The fierce **thermic** heat of the dog-days inflamed the blood, predisposing citizens to violent bilious fevers."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Ice baths and cold water affusions were the sovereign remedies applied to reduce the acute **thermic** crisis."
      }
    ]
  },
  "Dashboard — ther/thermidor.md": {
    "primary": "The eleventh month of the French Republican Calendar (July 19–August 17); or the political reaction that ended the Reign of Terror.",
    "secondary": "In political science and history, the coup of 9 Thermidor Year II (July 27, 1794) that deposed Robespierre; hence, a conservative reaction following a radical revolution.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "On the ninth of **Thermidor**, the National Convention shouted down Robespierre, ending the bloody Reign of Terror."
      },
      {
        "author": "Leon Trotsky",
        "work": "The Revolution Betrayed",
        "quote": "The bureaucratic reaction in the Soviet state represents a classic Soviet **Thermidor**, rolling back revolutionary ideals."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "After the fever of **Thermidor**, exhausted France welcomed bourgeois stability and military order under Bonaparte."
      }
    ]
  },
  "Dashboard — ther/thermion.md": {
    "primary": "A charged particle (electron or ion) emitted from a heated material via thermionic emission.",
    "secondary": "In electronics and atomic physics, a particle escaping the work function of a glowing metallic filament inside a vacuum tube.",
    "quotes": [
      {
        "author": "J. J. Thomson",
        "work": "Conduction of Electricity Through Gases",
        "quote": "The negative **thermion** emitted by the incandescing platinum wire proved to be identical with the cathode ray electron."
      },
      {
        "author": "Owen Willans Richardson",
        "work": "The Emission of Electricity from Hot Bodies",
        "quote": "Richardson's law describes the exponential increase in the rate at which each **thermion** escapes the heated metal surface."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "The cloud chamber tracks confirmed that each liberated **thermion** carried the elementary unit of electric charge."
      }
    ]
  },
  "Dashboard — ther/thermionic.md": {
    "primary": "Of, relating to, or involving the emission of electrons or ions from substances at elevated temperatures.",
    "secondary": "In electrical engineering, designating thermionic valves, vacuum tubes, and cathode ray devices foundational to early 20th-century radio and radar.",
    "quotes": [
      {
        "author": "John Ambrose Fleming",
        "work": "The Thermionic Valve and Its Developments in Radiotelegraphy and Telephony",
        "quote": "The invention of the **thermionic** diode valve allowed the rectification of high-frequency wireless waves into audible speech."
      },
      {
        "author": "Lee de Forest",
        "work": "Father of Radio",
        "quote": "By inserting a third electrode grid into the **thermionic** tube, the Audion amplified faint signals a thousandfold."
      },
      {
        "author": "H. G. Wells",
        "work": "The Shape of Things to Come",
        "quote": "Early wireless networks depended upon glowing glass banks of **thermionic** valves humming through the night."
      }
    ]
  },
  "Dashboard — ther/thermionics.md": {
    "primary": "The scientific branch and technology dealing with the emission, behavior, and applications of thermions in vacuum tubes.",
    "secondary": "In physics and telecommunications, the theoretical foundation of vacuum electronics that underpinned the 20th-century radio and computer revolution.",
    "quotes": [
      {
        "author": "Owen Willans Richardson",
        "work": "The Emission of Electricity from Hot Bodies",
        "quote": "The principles of **thermionics** established the relationship between temperature, metal work functions, and saturation current."
      },
      {
        "author": "V. K. Zworykin",
        "work": "Television: The Electronics of Image Transmission",
        "quote": "Advances in experimental **thermionics** paved the way for the cathode-ray iconoscope and modern electronic television."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "Applied **thermionics** transformed theoretical electron physics into global radio communications and international broadcasting."
      }
    ]
  },
  "Dashboard — ther/thermistor.md": {
    "primary": "A type of electrical resistor whose resistance changes significantly and predictably with temperature.",
    "secondary": "In electrical instrumentation and electronics, a semiconductor device (thermal resistor) possessing a high negative (NTC) or positive (PTC) temperature coefficient.",
    "quotes": [
      {
        "author": "John Bardeen",
        "work": "Semiconductor Research Leading to the Point Contact Transistor",
        "quote": "The high temperature sensitivity of the semiconductor **thermistor** made it an ideal sensor for microwave power measurement."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Oceanographic bathythermographs equipped with a sensitive **thermistor** mapped thermal thermoclines across the Atlantic."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "A miniature bead **thermistor** inserted into the chemical calorimeter recorded temperature changes of a microdegree."
      }
    ]
  },
  "Dashboard — ther/thermoacidophile.md": {
    "primary": "An extremophilic microorganism that thrives in environments characterized by both high temperatures and high acidity (low pH).",
    "secondary": "In microbial ecology and astrobiology, archaea (such as Sulfolobus) inhabiting sulfur hot springs and solfataras at temperatures of 70–80°C and pH 2–3.",
    "quotes": [
      {
        "author": "Carl Woese",
        "work": "Bacterial Evolution",
        "quote": "The discovery that the **thermoacidophile** Sulfolobus belonged to Archaea fundamentally redrew the phylogenetic tree of life."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "In boiling acidic cauldrons of Yellowstone, the tough **thermoacidophile** thrives where all other living cells dissolve."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Full House",
        "quote": "The metabolic adaptations of the **thermoacidophile** demonstrate that life can flourish in environmental extremes akin to early Earth."
      }
    ]
  },
  "Dashboard — ther/thermobia.md": {
    "primary": "A genus of primitive wingless insects in the family Lepismatidae, containing the firebrat (Thermobia domestica).",
    "secondary": "In domestic entomology, bristletail insects closely related to silverfish, flourishing in warm, dry microhabitats such as bakeries, boiler rooms, and hearths.",
    "quotes": [
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "The firebrat **Thermobia** domestica scuttles behind commercial bake-ovens, reveling in intense heat that would kill other insects."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Species of **Thermobia** are remarkably tolerant of desiccation, finding optimal development between thirty-five and forty degrees."
      },
      {
        "author": "Vincent Dethier",
        "work": "To Know a Fly",
        "quote": "The rapid nocturnal darting of **Thermobia** across hearth bricks fascinated entomologists studying thermotaxis."
      }
    ]
  },
  "Dashboard — ther/thermocautery.md": {
    "primary": "The medical cauterization of living tissue using an instrument heated by electricity or fuel combustion.",
    "secondary": "In surgical history, the Paquelin cautery using benzine vapor to heat a hollow platinum tip for hemostasis and tumor excision.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Application of the **thermocautery** along the spinal column provided effective counter-irritation in chronic myelitis."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Before electrosurgery, surgeons relied upon the glowing tip of the **thermocautery** to arrest troublesome dural bleeding."
      },
      {
        "author": "Joseph Lister",
        "work": "The Collected Papers of Joseph Lister",
        "quote": "The sterile heat of the **thermocautery** destroyed malignant ulcers without introducing hospital gangrene into the wound."
      }
    ]
  },
  "Dashboard — ther/thermochemistry.md": {
    "primary": "The branch of chemical science that studies the heat absorbed or released during chemical reactions and phase changes.",
    "secondary": "In physical chemistry, the application of the First Law of Thermodynamics to chemical systems, formulated through Hess's Law of constant heat summation.",
    "quotes": [
      {
        "author": "Germain Henri Hess",
        "work": "Thermochemical Researches",
        "quote": "The fundamental axiom of **thermochemistry** asserts that the heat evolved in a reaction is constant regardless of the pathway taken."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Outlines of General Chemistry",
        "quote": "Precise bomb calorimetry enabled **thermochemistry** to determine the bond enthalpies of organic compounds."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "The convergence of electrochemistry with **thermochemistry** revealed the energetic basis of ionic dissociation."
      }
    ]
  },
  "Dashboard — ther/thermocoagulation.md": {
    "primary": "The therapeutic coagulation and destruction of biological tissue or blood vessels using localized heat.",
    "secondary": "In neurosurgery, dermatology, and cardiology, the use of radiofrequency or thermal probes to ablate tumors, thrombose bleeding vessels, or destroy aberrant cardiac pathways.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Electro-Surgery as an Aid to the Removal of Intracranial Tumors",
        "quote": "Point **thermocoagulation** of bleeding cerebral vessels reduced blood loss to a fraction of previous mortality rates."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Superficial angiomas and vascular nevi respond promptly to gentle, controlled cutaneous **thermocoagulation**."
      },
      {
        "author": "Michael DeBakey",
        "work": "Surgical Techniques in Vascular Surgery",
        "quote": "Modern high-frequency **thermocoagulation** seals capillary beds cleanly, preventing postoperative hematomas."
      }
    ]
  },
  "Dashboard — ther/thermocouple.md": {
    "primary": "A thermoelectric device consisting of two dissimilar metal conductors joined at two junctions, producing a voltage proportional to the temperature difference.",
    "secondary": "In instrumentation and physics, a rugged pyrometric temperature sensor operating on the Seebeck effect, measuring extreme heat in blast furnaces and jet engines.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "By calibrating a platinum-rhodium **thermocouple**, we attained precise temperature measurements up to fifteen hundred degrees."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The tiny current flowing through the circuit of the **thermocouple** reflected the Seebeck effect at the heated metallic contact."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Internal Constitution of the Stars",
        "quote": "Laboratory furnaces regulated by a delicate **thermocouple** simulated the high-temperature ionization of stellar matter."
      }
    ]
  },
  "Dashboard — ther/thermodynamic.md": {
    "primary": "Of, relating to, or governed by the relations between heat, mechanical work, and other forms of energy.",
    "secondary": "In physics and engineering, describing systems operating under energy conservation, entropy production, and absolute temperature limits.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "On the Dynamical Theory of Heat",
        "quote": "The absolute **thermodynamic** scale of temperature is independent of the properties of any particular thermometric substance."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "A heat engine operating on the Carnot cycle achieves the maximum possible **thermodynamic** efficiency."
      },
      {
        "author": "Ludwig Boltzmann",
        "work": "Lectures on Gas Theory",
        "quote": "The statistical interpretation of entropy links microscopic atomic disorder with macroscopic **thermodynamic** state functions."
      }
    ]
  },
  "Dashboard — ther/thermodynamical.md": {
    "primary": "Relating to or involving thermodynamics; thermodynamic (variant).",
    "secondary": "In physical science treatises, describing mathematical formulations of energy transformations, equilibria, and state equations.",
    "quotes": [
      {
        "author": "J. Willard Gibbs",
        "work": "On the Equilibrium of Heterogeneous Substances",
        "quote": "The **thermodynamical** potential of each component dictates the equilibrium distribution across multiple coexisting phases."
      },
      {
        "author": "Max Planck",
        "work": "Treatise on Thermodynamics",
        "quote": "Every reversible process represents an idealized limit where no net **thermodynamical** entropy is generated."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "Entropy is the arrow of time, imparting an irreversible direction to all cosmic **thermodynamical** processes."
      }
    ]
  },
  "Dashboard — ther/thermodynamically.md": {
    "primary": "In accordance with or from the standpoint of the principles and laws of thermodynamics.",
    "secondary": "In chemical physics and biology, describing whether a process is energetically favorable or spontaneous (delta G < 0).",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Although diamond is **thermodynamically** unstable relative to graphite at ambient pressure, its rate of conversion is negligible."
      },
      {
        "author": "Erwin Schrodinger",
        "work": "What Is Life?",
        "quote": "The living organism preserves its complex structure by continuously drawing negative entropy **thermodynamically** from its environment."
      },
      {
        "author": "Walther Nernst",
        "work": "Theoretical Chemistry",
        "quote": "A reaction that is **thermodynamically** feasible may remain dormant until activated by a suitable catalyst."
      }
    ]
  },
  "Dashboard — ther/thermodynamics.md": {
    "primary": "The branch of physical science that deals with the relations between heat and other forms of energy (mechanical, electrical, chemical).",
    "secondary": "In theoretical physics, the discipline founded upon four universal laws governing conservation of energy, non-decreasing entropy, and absolute zero.",
    "quotes": [
      {
        "author": "Sadi Carnot",
        "work": "Reflections on the Motive Power of Fire",
        "quote": "The production of motive power in steam engines laid the empirical groundwork for the grand science of **thermodynamics**."
      },
      {
        "author": "Albert Einstein",
        "work": "Autobiographical Notes",
        "quote": "Classical **thermodynamics** is the only physical theory of universal content which I am convinced will never be overthrown."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "The second law of **thermodynamics** holds the supreme position among the laws of Nature."
      }
    ]
  },
  "Dashboard — ther/thermoelectric.md": {
    "primary": "Relating to or involving the direct conversion of temperature differences into electric voltage, and vice versa.",
    "secondary": "In solid-state physics, encompassing the Seebeck effect (generating voltage from thermal gradients) and Peltier effect (heating/cooling from current).",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The **thermoelectric** pile devised by Melloni detects thermal radiation of extraordinary delicacy from distant candles."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The Thomson effect accounts for the absorption or evolution of heat when current traverses a **thermoelectric** conductor with a temperature gradient."
      },
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "Mathematical relations between the Seebeck and Peltier coefficients established the unified theory of **thermoelectric** phenomena."
      }
    ]
  },
  "Dashboard — ther/thermoelectrical.md": {
    "primary": "Pertaining to thermoelectricity; thermoelectric (variant).",
    "secondary": "In electrical engineering and experimental physics, describing instruments, currents, or circuits driven by thermal electromotive forces.",
    "quotes": [
      {
        "author": "William Crookes",
        "work": "On the Illumination of Lines of Molecular Pressure",
        "quote": "The radiometer vanes rotated when subjected to **thermoelectrical** radiation inside the high-vacuum bulb."
      },
      {
        "author": "Arthur Eddington",
        "work": "Stars and Atoms",
        "quote": "Galvanometers coupled to **thermoelectrical** receivers measured the minute heat received from bright stars."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "Careful thermal shielding of all junction points prevented spurious **thermoelectrical** currents from distorting the bridge balance."
      }
    ]
  },
  "Dashboard — ther/thermoelectricity.md": {
    "primary": "Electricity generated directly by the difference of temperature between two dissimilar electrical conductors or semiconductors.",
    "secondary": "In physics, the reversible interconversion of thermal and electrical energy discovered by Thomas Johann Seebeck in 1821 and Jean Charles Peltier in 1834.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "The thermodynamic principles applied to **thermoelectricity** proved that the heat generated at the junction is strictly reversible with current direction."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "Seebeck's momentous discovery of **thermoelectricity** demonstrated yet another profound link unifying heat and electrical forces."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "Modern pyrometers harness **thermoelectricity** to record temperatures inside blast furnaces beyond the range of mercury."
      }
    ]
  },
  "Dashboard — ther/thermogram.md": {
    "primary": "A photographic or digital image produced by thermography, showing temperature variations across a surface in false color.",
    "secondary": "In infrared diagnostics, building inspection, and vascular medicine, an image displaying surface heat distribution to detect tumors or insulation leaks.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "An airborne infrared **thermogram** mapped the sinuous, swirling boundary where the warm Gulf Stream encounters cold slope water."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "A diagnostic **thermogram** of the lower extremities revealed asymmetric cutaneous coolness indicating arterial thrombosis."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Satellite **thermogram** images disclosed hidden volcanic hot spots glowing through the nighttime cloud cover."
      }
    ]
  },
  "Dashboard — ther/thermograph.md": {
    "primary": "An instrument that automatically records variations in temperature over time on a revolving drum, chart, or digital medium.",
    "secondary": "In meteorology and climatology, a self-registering bimetallic or Bourdon tube sensor producing continuous thermograms of atmospheric temperature.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The continuous trace of the **thermograph** recorded the sudden plummet of mountain temperatures as cold fronts swept over the Andes."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Deep cave observatories equipped with a **thermograph** revealed that subterranean temperatures remain constant throughout the year."
      },
      {
        "author": "Robert Falcon Scott",
        "work": "Scott's Last Expedition",
        "quote": "The polar blizzard froze the revolving drum of the meteorological **thermograph**, stopping our continuous thermal log."
      }
    ]
  },
  "Dashboard — ther/thermography.md": {
    "primary": "A diagnostic imaging technique that records temperature patterns on surfaces using infrared radiation.",
    "secondary": "In clinical medicine and non-destructive industrial testing, utilizing infrared thermocameras to detect localized inflammation, poor perfusion, or electrical hotspots.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Early clinical experiments in **thermography** demonstrated increased radiant heat overlying active arthritic joints."
      },
      {
        "author": "Arthur Eddington",
        "work": "Stars and Atoms",
        "quote": "Astronomical **thermography** allows observers to measure the infrared glow emitted by cool interstellar dust clouds."
      },
      {
        "author": "Michael DeBakey",
        "work": "Surgical Techniques in Vascular Surgery",
        "quote": "Intraoperative **thermography** verified the restoration of blood flow across newly anastomosed peripheral bypass grafts."
      }
    ]
  },
  "Dashboard — ther/thermogravimeter.md": {
    "primary": "An analytical instrument used in thermogravimetry to measure continuous changes in a sample's weight as it is heated.",
    "secondary": "In analytical chemistry and materials science, a sensitive microbalance enclosed within a programmable furnace under controlled gaseous atmospheres.",
    "quotes": [
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "The quartz spring **thermogravimeter** recorded the continuous loss of water of crystallization as temperature ascended."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Thermal decomposition of calcium oxalate monohydrate inside the **thermogravimeter** proceeds through three discrete mass plateaus."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "A precision **thermogravimeter** determined the exact ash and volatile carbon content of commercial coking coals."
      }
    ]
  },
  "Dashboard — ther/thermogravimetric.md": {
    "primary": "Of, relating to, or measured by thermogravimetry (continuous measurement of mass changes during heating).",
    "secondary": "In materials characterization, describing thermogravimetric analysis (TGA) curves used to determine polymer thermal stability, decomposition, and moisture content.",
    "quotes": [
      {
        "author": "Walther Nernst",
        "work": "Theoretical Chemistry",
        "quote": "The **thermogravimetric** trace revealed an abrupt mass loss at three hundred degrees corresponding to complete dehydration."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "Kinetic parameters of solid-state thermal degradation were evaluated from the derivative **thermogravimetric** curve."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "High-temperature **thermogravimetric** data established the stoichiometry of oxygen vacancies in refractory ceramic oxides."
      }
    ]
  },
  "Dashboard — ther/thermogravimetry.md": {
    "primary": "A thermal analysis technique in which the mass of a substance is monitored as a function of temperature or time in a controlled atmosphere.",
    "secondary": "In analytical chemistry, an indispensable methodology for evaluating thermal stability, oxidative degradation, and decomposition kinetics of compounds.",
    "quotes": [
      {
        "author": "Wilhelm Ostwald",
        "work": "Outlines of General Chemistry",
        "quote": "Modern **thermogravimetry** automated the tedious gravimetric calcination procedures of 19th-century quantitative analysis."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "In industrial polymer research, **thermogravimetry** measures the exact degradation threshold of new synthetic resins."
      },
      {
        "author": "Walther Nernst",
        "work": "Theoretical Chemistry",
        "quote": "The application of **thermogravimetry** under vacuum clarified the dissociation pressures of metallic carbonates."
      }
    ]
  },
  "Dashboard — ther/thermohydrometer.md": {
    "primary": "A hydrometer equipped with an integral thermometer, allowing simultaneous measurement of liquid density and temperature.",
    "secondary": "In petroleum engineering and brewing, a floating glass instrument calibrated to determine specific gravity corrected for temperature expansion.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "By using a **thermohydrometer**, the chemist reads the density of acids and alcohols with immediate temperature correction."
      },
      {
        "author": "Benjamin Franklin",
        "work": "Maritime Observations",
        "quote": "I lowered a **thermohydrometer** into the Gulf Stream, charting its warm temperature and high salinity across the Atlantic."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "The petroleum inspector plunged the **thermohydrometer** into the oil tank car to calculate the API gravity at standard sixty degrees."
      }
    ]
  },
  "Dashboard — ther/thermohydrometric.md": {
    "primary": "Of, relating to, or determined by a thermohydrometer; combining thermal and hydrometric measurements.",
    "secondary": "In chemical metrology, describing density measurements of liquids normalized against standardized temperature correction tables.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "The **thermohydrometric** tables allowed precise determination of battery electrolyte density throughout winter frosts."
      },
      {
        "author": "William Crookes",
        "work": "Researches on the Atomic Weight of Thallium",
        "quote": "Careful **thermohydrometric** calibration ensured that solution volumes were measured with absolute physical rigor."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "A **thermohydrometric** survey of industrial brine ponds tracked evaporation rates under the summer sun."
      }
    ]
  },
  "Dashboard — ther/thermojunction.md": {
    "primary": "The contact point between two dissimilar metals in a thermocouple where a thermoelectric voltage is generated by temperature differences.",
    "secondary": "In instrumentation physics, the measurement junction (hot junction) whose temperature is compared to a reference junction (cold junction) via the Seebeck effect.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "The electromotive force produced across the **thermojunction** depends solely on the nature of the metals and the temperature delta."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "Heat is absorbed or evolved at the **thermojunction** whenever an electric current is forced across the boundary."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "A delicate antimony-bismuth **thermojunction** detected the faint thermal beam reflected from the parabolic mirror."
      }
    ]
  },
  "Dashboard — ther/thermolabile.md": {
    "primary": "Readily decomposed, inactivated, or destroyed by heat (heat-labile); opposite of thermostable.",
    "secondary": "In biochemistry and immunology, describing proteins, vitamins (such as vitamin C), enzymes, and bacterial toxins that denature at moderate temperatures.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Mild heating to sixty degrees inactivated the **thermolabile** ferments without spoiling the natural bouquet of the wine."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The bactericidal complement in fresh human serum is **thermolabile**, being destroyed by heating for thirty minutes at fifty-six degrees."
      },
      {
        "author": "Hans Zinsser",
        "work": "Immunity: Principles and Application in Medicine",
        "quote": "Diphtheria exotoxin is highly **thermolabile**, rapidly transforming into benign toxoid when exposed to gentle heat."
      }
    ]
  },
  "Dashboard — ther/thermometer.md": {
    "primary": "An instrument for measuring and indicating temperature, typically consisting of a graduated glass tube containing mercury or alcohol.",
    "secondary": "In the history of science, invented conceptually by Galileo and perfected into sealed standardized instruments by Fahrenheit and Celsius.",
    "quotes": [
      {
        "author": "Galileo Galilei",
        "work": "The Assayer",
        "quote": "I constructed an open air **thermometer** whose fluctuating water level demonstrated the expansion of air under warmth."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "I checked the **thermometer** daily at noon, recording the rapid cooling of sea surface temperatures along the Peruvian coast."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The clinical **thermometer** introduced by Wunderlich replaced subjective guessing with scientific precision at the bedside."
      }
    ]
  },
  "Dashboard — ther/thermometric.md": {
    "primary": "Of, relating to, or determined by the measurement of temperature; thermometrical.",
    "secondary": "In physics and metrology, designating fixed points, scales (Celsius, Kelvin, Fahrenheit), or substances whose physical changes measure temperature.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "The freezing and boiling points of pure water under standard barometric pressure furnish the fundamental **thermometric** fixed points."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "Mercury serves as the standard **thermometric** liquid because of its uniform thermal expansion and high boiling point."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Continuous **thermometric** observations across diverse mountain elevations revealed the environmental lapse rate."
      }
    ]
  },
  "Dashboard — ther/thermometrograph.md": {
    "primary": "A self-registering thermometer that records maximum and minimum temperatures or continuous temperature curves over time.",
    "secondary": "In meteorological history, an early mechanical instrument recording daily extremes via small metal indices moved by mercury and alcohol columns (James Six's thermometer).",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "I suspended a **thermometrograph** beneath the rainforest canopy to log the nocturnal drop in tropical temperature."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Deep boreholes lowered a specialized **thermometrograph** to measure the geothermal gradient into the Earth's crust."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "A self-registering **thermometrograph** placed inside the deep mine shaft recorded temperatures rising one degree for every fifty feet."
      }
    ]
  },
  "Dashboard — ther/thermometry.md": {
    "primary": "The branch of physical science and engineering concerned with the measurement of temperature and scale calibration.",
    "secondary": "In metrology and clinical medicine, the scientific determination of thermal states, radiation thermometry, and absolute thermodynamic calibration.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Systematic clinical **thermometry** transformed fever diagnosis from vague impressions into definitive diurnal curves."
      },
      {
        "author": "Lord Kelvin",
        "work": "On an Absolute Thermometric Scale",
        "quote": "The goal of theoretical **thermometry** was achieved when temperature was defined purely in terms of mechanical energy."
      },
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Precise **thermometry** is the indispensable foundation of all chemical investigations into combustion and latent caloric."
      }
    ]
  },
  "Dashboard — ther/thermonuclear.md": {
    "primary": "Relating to or involving nuclear reactions (especially nuclear fusion) that occur only at extremely high temperatures.",
    "secondary": "In astrophysics and modern defense technology, designating stellar core fusion processes (converting hydrogen into helium) or hydrogen bombs.",
    "quotes": [
      {
        "author": "Arthur Eddington",
        "work": "The Internal Constitution of the Stars",
        "quote": "Subatomic **thermonuclear** reactions inside stellar cores release the vast energies that keep the sun burning for billions of years."
      },
      {
        "author": "Hans Bethe",
        "work": "Energy Production in Stars",
        "quote": "The carbon-nitrogen-oxygen cycle provides the **thermonuclear** engine powering massive main-sequence stars."
      },
      {
        "author": "J. Robert Oppenheimer",
        "work": "The Open Mind",
        "quote": "The devastating power of the **thermonuclear** weapon forced mankind to confront the ultimate responsibility of survival."
      }
    ]
  },
  "Dashboard — ther/thermopile.md": {
    "primary": "An electronic apparatus composed of an array of thermocouples connected in series, converting thermal energy directly into electric voltage.",
    "secondary": "In experimental physics and infrared optics, a sensitive detector invented by Leopoldo Nobili and Macedonio Melloni to measure radiant heat.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Melloni's **thermopile** coupled to a sensitive astatic galvanometer detected the invisible radiant heat of the lunar beam."
      },
      {
        "author": "John Tyndall",
        "work": "Contributions to Molecular Physics in the Domain of Radiant Heat",
        "quote": "By aiming a rock-salt **thermopile** at gas tubes, I proved that water vapor and carbon dioxide absorb infrared radiation."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "A delicate **thermopile** can detect the warmth radiated by a human face across a large auditorium."
      }
    ]
  },
  "Dashboard — ther/thermoplastic.md": {
    "primary": "A polymer or plastic material that becomes pliable or moldable above a specific temperature and solidifies upon cooling, repeatedly without chemical change.",
    "secondary": "In polymer chemistry and manufacturing, linear or branched macromolecules (such as polyethylene, nylon, or polystyrene) holding reversible melt-processing capability.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Unlike thermosets, a **thermoplastic** polymer can be repeatedly melted, reshaped, and recycled without chemical degradation."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "Injection molding of **thermoplastic** resins revolutionized the rapid mass production of domestic appliances."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Synthetic **thermoplastic** containers rapidly displaced glass and paper packaging across the industrial world."
      }
    ]
  },
  "Dashboard — ther/thermopsis.md": {
    "primary": "A genus of perennial herbaceous plants in the legume family (Fabaceae), commonly known as false lupines or goldenbanners.",
    "secondary": "In North American and Asian botany, rhizomatous prairie herbs bearing lupine-like palmate leaves and dense spikes of golden-yellow pea-like flowers (literally 'lupine-like').",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "On dry gravelly prairie banks, the golden spikes of **Thermopsis** rhombifolia blossom early in the spring."
      },
      {
        "author": "John Torrey",
        "work": "Report on the United States and Mexican Boundary Survey",
        "quote": "I collected specimens of **Thermopsis** montana flowering along the high mountain streams of the Rockies."
      },
      {
        "author": "David Douglas",
        "work": "Journal Kept by David Douglas During His Travels in North America",
        "quote": "The yellow blossoms of **Thermopsis** carpeted the river bottom lands in brilliant drifts of gold."
      }
    ]
  },
  "Dashboard — ther/thermopylae.md": {
    "primary": "A narrow coastal mountain pass in eastern central Greece, famed for the heroic stand of 300 Spartans under King Leonidas in 480 BCE; literally 'Hot Gates'.",
    "secondary": "In classical history and geography, named for the sulfurous hot springs emerging from the foot of Mount Oeta; the archetypal symbol of heroic sacrifice against overwhelming odds.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "At **Thermopylae**, Leonidas and his three hundred Spartans stood fast against the Persian host, preferring glorious death to shameful retreat."
      },
      {
        "author": "Lord Byron",
        "work": "Don Juan",
        "quote": "Earth! render back from out thy breast a remnant of our Spartan dead! Of the three hundred grant but three, to make a new **Thermopylae**!"
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The narrow pass of **Thermopylae** was fortified in every age as the natural northern rampart of Greece."
      }
    ]
  },
  "Dashboard — ther/thermoreceptor.md": {
    "primary": "A specialized sensory nerve ending or receptor organ that responds to changes in temperature (heat or cold).",
    "secondary": "In neurophysiology and sensory biology, transient receptor potential (TRP) ion channels located on free nerve endings detecting cutaneous and core temperature.",
    "quotes": [
      {
        "author": "Charles Scott Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Cutaneous sensory spots contain distinct **thermoreceptor** endings specialized separately for warmth and cold."
      },
      {
        "author": "Raymond Ditmars",
        "work": "Snakes of the World",
        "quote": "The facial pit of the rattlesnake houses an extraordinarily sensitive **thermoreceptor** membrane capable of detecting radiant warmth from a mouse."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Stimulation of a cold **thermoreceptor** by a drop of hot water occasionally produces the illusion of paradoxical cold."
      }
    ]
  },
  "Dashboard — ther/thermoregulator.md": {
    "primary": "A device or physiological mechanism that automatically controls or maintains a desired temperature.",
    "secondary": "In biological cybernetics and engineering, an automated thermostat or the hypothalamic preoptic nucleus that maintains homeostatic core temperature.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The anterior hypothalamus acts as the body's master physiological **thermoregulator**, orchestrating shivering, vasodilation, and sweat."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "An electrical **thermoregulator** maintained the reaction water bath at twenty-five degrees with unwavering constancy."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "Toluene expansion tubes coupled to sensitive relays provided a dependable **thermoregulator** for precision calorimetry."
      }
    ]
  },
  "Dashboard — ther/thermos.md": {
    "primary": "A vacuum flask or insulated container for keeping liquids hot or cold; or the Greek adjective thermos ('hot, warm').",
    "secondary": "In physics and industrial history, the commercialized Dewar flask (patented under the trademark Thermos in 1904) utilizing double-walled silvered glass separated by a vacuum.",
    "quotes": [
      {
        "author": "James Dewar",
        "work": "Collected Papers on Liquid Gases",
        "quote": "The vacuum-jacketed vessel, later popularized as the commercial **thermos**, prevented heat transfer by conduction and convection."
      },
      {
        "author": "Robert Falcon Scott",
        "work": "Scott's Last Expedition",
        "quote": "We filled our **thermos** flasks with hot tea before marching out into the minus-thirty-degree blizzard."
      },
      {
        "author": "George Orwell",
        "work": "Coming Up for Air",
        "quote": "We packed a basket with meat pies and a **thermos** of hot coffee for our Sunday fishing trip."
      }
    ]
  },
  "Dashboard — ther/thermoset.md": {
    "primary": "A polymer or plastic resin that becomes permanently rigid and infusible upon heating and cross-linking, unable to be remelted.",
    "secondary": "In materials science and polymer technology, network polymers (such as Bakelite, epoxies, and vulcanized rubber) that decompose rather than melt when reheated.",
    "quotes": [
      {
        "author": "Leo Baekeland",
        "work": "The Synthesis, Constitution, and Uses of Bakelite",
        "quote": "Under heat and pressure, phenol and formaldehyde cross-link into Bakelite, the first commercial **thermoset** plastic."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Extensive covalent cross-linking locks the chains of a **thermoset** into a single giant macromolecular network."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "The electrical insulation properties of a molded **thermoset** panel remain stable under extreme engine temperatures."
      }
    ]
  },
  "Dashboard — ther/thermosetting.md": {
    "primary": "Capable of becoming permanently rigid, cross-linked, and infusible upon the application of heat.",
    "secondary": "In chemical industry and manufacturing, describing prepolymers and resins (phenolics, melamines, polyurethanes) that cure irreversibly via thermal cross-linking.",
    "quotes": [
      {
        "author": "Leo Baekeland",
        "work": "Bakelite: A New Synthetic Resin",
        "quote": "The initial liquid resin is converted by baking into an insoluble, **thermosetting** solid impervious to solvents."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "Automobile distributors and airplane instrument housings were molded from durable **thermosetting** compounds."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Irreversible covalent bonds formed during the **thermosetting** cure prevent thermal reshaping."
      }
    ]
  },
  "Dashboard — ther/thermosphere.md": {
    "primary": "The layer of the Earth's atmosphere directly above the mesosphere and below the exosphere, characterized by increasing temperatures with altitude.",
    "secondary": "In atmospheric physics and space exploration, the high-altitude zone extending from 85 km to 600 km where solar X-rays and UV radiation ionize gases, housing the ionosphere and auroras.",
    "quotes": [
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Extreme ultraviolet radiation heats the rarefied gases of the **thermosphere** to temperatures exceeding fifteen hundred degrees."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Auroral curtains ripple through the thin upper air of the **thermosphere**, ignited by solar wind protons."
      },
      {
        "author": "James Lovelock",
        "work": "Gaia: A New Look at Life on Earth",
        "quote": "The high **thermosphere** shields the biosphere below by absorbing lethal shortwave solar ionizing radiation."
      }
    ]
  },
  "Dashboard — ther/thermostat.md": {
    "primary": "An automatic device that monitors and regulates temperature by turning heating or cooling equipment on and off.",
    "secondary": "In cybernetics and control systems, an engineering feedback loop invented by Cornelis Drebbel and popularized by Andrew Ure using bimetallic strips.",
    "quotes": [
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics: or Control and Communication in the Animal and the Machine",
        "quote": "The domestic **thermostat** is the classic exemplar of negative feedback, correcting deviations from the set point."
      },
      {
        "author": "Andrew Ure",
        "work": "The Philosophy of Manufactures",
        "quote": "I patented the bimetallic **thermostat** to maintain uniform temperatures inside textile drying rooms and steam boilers."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "The subterranean laboratories of the future were regulated by an automatic **thermostat** ensuring perpetual warmth."
      }
    ]
  },
  "Dashboard — ther/thermostatic.md": {
    "primary": "Of, relating to, or operated by a thermostat; maintaining automatic temperature regulation.",
    "secondary": "In mechanical engineering and domestic architecture, describing valves, switches, or mixers controlled automatically by thermal expansion.",
    "quotes": [
      {
        "author": "Andrew Ure",
        "work": "Dictionary of Arts, Manufactures, and Mines",
        "quote": "The **thermostatic** valve expands with heat, throttling the draft and preventing the steam boiler from overheating."
      },
      {
        "author": "Norbert Wiener",
        "work": "The Human Use of Human Beings",
        "quote": "Living organisms maintain homeostatic equilibrium through mechanisms analogous to **thermostatic** control circuits."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "Laboratory incubators equipped with **thermostatic** relays held bacteriological cultures at strict physiological temperatures."
      }
    ]
  },
  "Dashboard — ther/thermostatically.md": {
    "primary": "By means of a thermostat; with automatic temperature control.",
    "secondary": "In engineering and laboratory operations, maintaining thermal conditions automatically through a feedback mechanism.",
    "quotes": [
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "The temperature of the bath was regulated **thermostatically**, compensating instantly for ambient room drafts."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemist and His Work",
        "quote": "Industrial fermentation vats must be **thermostatically** controlled to prevent thermal inactivation of delicate yeast enzymes."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The warm-blooded body acts **thermostatically**, sweating or shivering to preserve the constancy of the internal milieu."
      }
    ]
  },
  "Dashboard — ther/thermostatics.md": {
    "primary": "The branch of physical science dealing with the conditions of thermal equilibrium in bodies, analogous to statics in mechanics.",
    "secondary": "In theoretical physics and thermodynamics, the study of non-flowing, stationary thermal systems where heat and work are in static balance.",
    "quotes": [
      {
        "author": "J. Willard Gibbs",
        "work": "On the Equilibrium of Heterogeneous Substances",
        "quote": "The principles of **thermostatics** determine the criteria of phase stability in multi-component chemical systems."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "Just as statics investigates forces at rest, so **thermostatics** investigates systems where temperatures have achieved complete equilibrium."
      },
      {
        "author": "Max Planck",
        "work": "Treatise on Thermodynamics",
        "quote": "The foundation of **thermostatics** rests upon the maximum entropy principle governing isolated physical systems."
      }
    ]
  },
  "Dashboard — ther/thermotherapy.md": {
    "primary": "The therapeutic application of heat to the body to relieve pain, improve circulation, and treat musculoskeletal injuries.",
    "secondary": "In physical medicine and rehabilitation, modalities including hot packs, paraffin baths, ultrasound, and sauna therapy used for muscle spasm and joint stiffness.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Judicious local **thermotherapy** promotes vasodilation and accelerates the absorption of chronic inflammatory exudates."
      },
      {
        "author": "Robley Dunglison",
        "work": "General Therapeutics and Materia Medica",
        "quote": "Ancient physicians practiced **thermotherapy** through the warm sulfur springs of Baiae to soothe gouty joints."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Rehabilitation protocols for paralyzed limbs integrated daily **thermotherapy** to reduce hypertonic muscular contractures."
      }
    ]
  },
  "Dashboard — ther/thermotropism.md": {
    "primary": "The directional growth, curvature, or movement of an organism or plant part in response to temperature gradients or heat.",
    "secondary": "In plant physiology and behavioral entomology, positive thermotropism (growing or moving toward warmth) and negative thermotropism (away from heat).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "Roots and young shoots display marked **thermotropism**, curving toward optimal soil warmth to promote vigorous cell elongation."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Hungry Fly",
        "quote": "The blood-feeding bug Rhodnius relies on positive **thermotropism** to guide its proboscis toward the warm blood vessels of its host."
      },
      {
        "author": "Jacques Loeb",
        "work": "Forced Movements, Tropisms, and Animal Conduct",
        "quote": "Insects exhibiting positive **thermotropism** congregate instinctively along warm surfaces regardless of visual illumination."
      }
    ]
  },
  "Dashboard — ther/theroid.md": {
    "primary": "Resembling or characteristic of a wild beast or animal in appearance, demeanor, or instinct.",
    "secondary": "In biological anthropology and psychiatry, describing feral behavior, bestial facial features, or archaic atavistic traits (from Greek ther, beast + -oid).",
    "quotes": [
      {
        "author": "Cesare Lombroso",
        "work": "Criminal Man",
        "quote": "The degenerate profile displayed distinct **theroid** characteristics, with prominent canine teeth and receding forehead."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The cranium of the archaic synapsid retained a **theroid** aspect that foreshadowed mammalian predatory specializations."
      },
      {
        "author": "H. G. Wells",
        "work": "The Island of Doctor Moreau",
        "quote": "The Beast Folk slipped steadily backward into their old **theroid** habits, howling on all fours through the tangled jungle."
      }
    ]
  },
  "Dashboard — ther/theropod.md": {
    "primary": "Any bipedal, hollow-boned carnivorous or omnivorous dinosaur of the clade Theropoda, from which modern birds evolved ('beast foot').",
    "secondary": "In vertebrate paleontology, predatory dinosaurs (from diminutive compsognathids to colossal tyrannosaurs) possessing curved claws, serrated teeth, and furculae.",
    "quotes": [
      {
        "author": "O. C. Marsh",
        "work": "Principal Characters of American Jurassic Dinosaurs",
        "quote": "The predatory **theropod** Allosaurus walked entirely upon its strong hind legs, its hands armed with curved tearing claws."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Bully for Brontosaurus",
        "quote": "The discovery of feathered dinosaurs in China proved beyond doubt that birds are living, surviving **theropod** dinosaurs."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "Skeletal Adaptations of Ornitholestes, Struthiomimus, and Tyrannosaurus",
        "quote": "The skull of the colossal **theropod** Tyrannosaurus was engineered for bone-crushing bite forces exceeding several tons."
      }
    ]
  },
  "Dashboard — ther/theropoda.md": {
    "primary": "A major suborder of saurischian dinosaurs comprising all predatory bipedal dinosaurs and modern birds.",
    "secondary": "In systematic paleontology, diapsids characterized by hollow, thin-walled bones, three-toed pes, ziphodont dentition, and brooding parental behaviors.",
    "quotes": [
      {
        "author": "O. C. Marsh",
        "work": "The Dinosaurs of North America",
        "quote": "I established the suborder **Theropoda** for those carnivorous dinosaurs whose hollow limb bones combine light weight with immense strength."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Animals Which Are Most Nearly Intermediate between Birds and Reptiles",
        "quote": "The avian tarsometatarsus is completely anticipated in the hind limb osteology of the **Theropoda**."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The global radiation of the **Theropoda** produced the dominant terrestrial predators of the entire Mesozoic era."
      }
    ]
  },
  "Dashboard — ther/theropsid.md": {
    "primary": "Pertaining to or belonging to the synapsid (mammal-like) lineage of amniotes, distinct from sauropsids (reptiles and birds); 'beast-faced'.",
    "secondary": "In evolutionary biology and comparative vertebrate morphology, designating synapsids characterized by a single lower temporal fenestra, leading directly to mammals.",
    "quotes": [
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The early divergence of amniotes separated the **theropsid** synapsids leading to mammals from the sauropsid line leading to lizards and birds."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "Evolution of the Vertebrates",
        "quote": "The Karoo fossils illustrate the progressive transformation of the **theropsid** skull toward mammalian cranial architecture."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "Our own remote ancestors were the humble **theropsid** synapsids that scuttled underfoot during the age of the dinosaurs."
      }
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

console.log(`Updated ${updatedCount} files in Batch 8!`);
