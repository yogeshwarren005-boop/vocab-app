import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — micro\\microcircuit.md": {
    "primary": "An integrated electric circuit composed of miniaturized components fabricated onto a tiny semiconductor substrate.",
    "secondary": "In electronics and nanotechnology, a microscale network of interconnected transistors, diodes, and resistors executing high-speed logic functions.",
    "quotes": [
      {
        "author": "Gordon Moore",
        "work": "Cramming More Components onto Integrated Circuits",
        "quote": "The complexity for minimum component costs has increased at a rate of roughly a factor of two per year per **microcircuit**."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "The transition from the vacuum tube to the solid-state **microcircuit** made interplanetary space probes technologically feasible."
      },
      {
        "author": "Richard Feynman",
        "work": "Feynman Lectures on Computation",
        "quote": "Within the printed **microcircuit**, electrical charges navigate micron-wide conduits obeying deterministic switching laws."
      }
    ]
  },
  "Dashboard — micro\\micrococcaceae.md": {
    "primary": "A family of Gram-positive, spherical bacteria (cocci) that typically divide in multiple planes to form irregular clusters, tetrads, or packets.",
    "secondary": "In systematic bacteriology, aerobic or facultatively anaerobic chemoorganotrophic cocci found in soil, water, and mammalian skin.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "Cultures from cutaneous abrasions frequently yield harmless commensals of the family **Micrococcaceae**."
      },
      {
        "author": "William Bulloch",
        "work": "The History of Bacteriology",
        "quote": "Early taxonomists grouped all cluster-forming non-motile spheres under the comprehensive family name **Micrococcaceae**."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin and Its Practical Application",
        "quote": "Staphylococcus and other members of the **Micrococcaceae** display variable susceptibility to antibacterial secretions."
      }
    ]
  },
  "Dashboard — micro\\micrococcus.md": {
    "primary": "A genus of spherical, Gram-positive bacteria that occur predominantly in irregular clusters or tetrads and are widespread in nature.",
    "secondary": "In diagnostic bacteriology, non-pathogenic or opportunistic saprophytic cocci commonly isolated from healthy human skin and dairy products.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Germ Theory and Its Applications",
        "quote": "Microscopic examination of the exposed broth revealed small spherical bodies characteristic of **Micrococcus**."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "The petri dish contained large yellow colonies of **Micrococcus** luteus flourishing alongside the mold."
      },
      {
        "author": "Alexander Fleming",
        "work": "On a Remarkable Bacteriolytic Element Found in Tissues and Secretions",
        "quote": "Nasal mucus rapidly dissolved dense suspensions of **Micrococcus** lysodeikticus within a matter of minutes."
      }
    ]
  },
  "Dashboard — micro\\microcode.md": {
    "primary": "A set of low-level machine instructions that directly control the internal data paths and registers of a central processing unit.",
    "secondary": "In computer architecture, the firmware layer that translates macro-level assembly instructions into hardware-level micro-operations.",
    "quotes": [
      {
        "author": "Maurice Wilkes",
        "work": "Memoirs of a Computer Pioneer",
        "quote": "I conceived the idea of **microcode** in 1951 to replace ad-hoc control logic with a systematic diode matrix."
      },
      {
        "author": "Tracy Kidder",
        "work": "The Soul of a New Machine",
        "quote": "The debugging team spent sleepless weeks patching micro-instructions in writable **microcode** to cure processor glitches."
      },
      {
        "author": "Andrew Tanenbaum",
        "work": "Structured Computer Organization",
        "quote": "The microprogram engine executes lines of **microcode** that control register transfers during each clock cycle."
      }
    ]
  },
  "Dashboard — micro\\microcomputer.md": {
    "primary": "A small computer that uses a microprocessor as its central processing unit, designed for individual or personal use.",
    "secondary": "A personal desktop or portable computing system that democratized data processing and initiated the digital consumer revolution in the 1970s and 1980s.",
    "quotes": [
      {
        "author": "Steve Wozniak",
        "work": "iWoz: Computer Geek to Cult Icon",
        "quote": "My dream was to design an affordable **microcomputer** that any hobbyist could connect to a standard television set."
      },
      {
        "author": "Ted Nelson",
        "work": "Computer Lib / Dream Machines",
        "quote": "The interactive personal **microcomputer** will liberate human creativity from the bureaucracy of centralized mainframes."
      },
      {
        "author": "Walter Isaacson",
        "work": "The Innovators",
        "quote": "The advent of the single-chip microprocessor in 1971 made the concept of a home **microcomputer** an imminent reality."
      }
    ]
  },
  "Dashboard — micro\\microcopy.md": {
    "primary": "A photographic copy of printed or graphic matter greatly reduced in size, requiring optical magnification to read.",
    "secondary": "In user interface design, small bits of instructional text, button labels, and hints that guide users through a digital interface.",
    "quotes": [
      {
        "author": "Don Norman",
        "work": "The Design of Everyday Things",
        "quote": "Carefully worded **microcopy** on a checkout button alleviates user anxiety and clarifies subsequent actions."
      },
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "Libraries began reducing voluminous historical newspapers onto rolls of space-saving photographic **microcopy**."
      },
      {
        "author": "Steve Krug",
        "work": "Don't Make Me Think",
        "quote": "Concise, unambiguous **microcopy** next to form fields prevents users from stumbling during complex sign-up flows."
      }
    ]
  },
  "Dashboard — micro\\microcosmic.md": {
    "primary": "Of, relating to, or characteristic of a microcosm; reflecting miniature features of a much larger universe or system.",
    "secondary": "In philosophy and literature, encapsulating macroscopic, metaphysical, or universal principles within a localized, small-scale instance.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Ancient philosophers called man a **microcosmic** mirror of the whole vast framework of heaven and earth."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "Every drop of dew and every leaf reflects a **microcosmic** image of the encompassing universal order."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "There is a world of wonders within each creature, a little **microcosmic** world of divine contrivance."
      }
    ]
  },
  "Dashboard — micro\\microcrystalline.md": {
    "primary": "Having a crystal structure visible only under a microscope, as in certain rocks, minerals, or waxes.",
    "secondary": "In geology and petroleum chemistry, describing fine-grained aggregates of microscopic mineral crystals or branched paraffin chains.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Thin sections of flint revealed a dense **microcrystalline** quartz fabric formed by chemical precipitation."
      },
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Chalcedony is a **microcrystalline** variety of silica, displaying a fibrous habit when observed between crossed polars."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Over millennia, pelagic sediments consolidated into tough **microcrystalline** limestone layers across ancient abyssal plains."
      }
    ]
  },
  "Dashboard — micro\\microcyte.md": {
    "primary": "An abnormally small red blood cell, characteristic of certain forms of anemia such as iron deficiency or thalassemia.",
    "secondary": "In hematology, an erythrocyte with a mean corpuscular volume (MCV) significantly below the standard reference range.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Stained blood smears from the chlorotic patient exhibited marked poikilocytosis, featuring an abundance of the undersized **microcyte**."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Differential staining clearly separates the pale **microcyte** of hypochromic anemia from the engorged megalocyte of pernicious anemia."
      },
      {
        "author": "Max Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Automated particle counters identify a **microcyte** whenever the red cell volume falls below eighty femtoliters."
      }
    ]
  },
  "Dashboard — micro\\microcytosis.md": {
    "primary": "A condition in which an unusually high proportion of red blood cells are abnormally small.",
    "secondary": "In diagnostic hematology, a laboratory finding characterized by low mean corpuscular volume (MCV), indicative of iron deficiency or hemoglobinopathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe chronic blood loss inevitably produces profound hypochromia accompanied by marked **microcytosis**."
      },
      {
        "author": "Max Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The differential diagnosis of marked **microcytosis** requires serum ferritin testing to distinguish iron depletion from thalassemia minor."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Carriers of the beta-thalassemia trait display benign **microcytosis**, conferring resistance against falciparum malaria."
      }
    ]
  },
  "Dashboard — micro\\microeconomic.md": {
    "primary": "Of or relating to microeconomics, the branch of economics that studies individual households, firms, and specific market mechanisms.",
    "secondary": "Pertaining to price theory, marginal utility, cost functions, and resource allocation at the level of specific consumers and enterprises.",
    "quotes": [
      {
        "author": "Paul Samuelson",
        "work": "Economics",
        "quote": "Every firm's supply curve is grounded in the **microeconomic** calculus of marginal costs equating marginal revenue."
      },
      {
        "author": "Milton Friedman",
        "work": "Price Theory",
        "quote": "Individual market clearing represents the core **microeconomic** principle through which decentralized coordination occurs."
      },
      {
        "author": "Joseph Stiglitz",
        "work": "Economics of the Public Sector",
        "quote": "Information asymmetry introduces market failures that overturn classical **microeconomic** assumptions of perfect competition."
      }
    ]
  },
  "Dashboard — micro\\microeconomics.md": {
    "primary": "The branch of economics concerned with single factors and the effects of individual decisions on market resource allocation.",
    "secondary": "The theoretical study of how consumers maximize utility and firms maximize profits under budget constraints and competitive market structures.",
    "quotes": [
      {
        "author": "Alfred Marshall",
        "work": "Principles of Economics",
        "quote": "The foundational doctrine of **microeconomics** examines how supply and demand balance at the margin to establish equilibrium prices."
      },
      {
        "author": "Gary Becker",
        "work": "The Economic Approach to Human Behavior",
        "quote": "I applied the analytical tools of **microeconomics** to explain crime, marriage, and family decisions as rational choices."
      },
      {
        "author": "Hal Varian",
        "work": "Microeconomic Analysis",
        "quote": "Modern **microeconomics** provides the formal mathematical scaffolding for understanding auction design and mechanism design."
      }
    ]
  },
  "Dashboard — micro\\microeconomist.md": {
    "primary": "An economist who specializes in microeconomics, analyzing the behavior of individual economic agents and discrete markets.",
    "secondary": "An applied researcher studying consumer behavior, corporate pricing strategies, industrial organization, or labor markets.",
    "quotes": [
      {
        "author": "George Stigler",
        "work": "The Theory of Price",
        "quote": "The professional **microeconomist** focuses on how changes in regulatory rules alter incentives for individual enterprises."
      },
      {
        "author": "Steven Levitt",
        "work": "Freakonomics",
        "quote": "As an empirical **microeconomist**, my instinct is to look past lofty rhetoric and examine the underlying incentives."
      },
      {
        "author": "Paul Krugman",
        "work": "Peddling Prosperity",
        "quote": "While macroeconomists bickered over fiscal stimulus, the **microeconomist** made steady progress mapping real-world market imperfections."
      }
    ]
  },
  "Dashboard — micro\\microelectronic.md": {
    "primary": "Of, relating to, or involving microelectronics or extremely miniaturized electronic components and circuits.",
    "secondary": "Describing semiconductor fabrication techniques, solid-state physics applications, and integrated circuits operating at sub-micron scales.",
    "quotes": [
      {
        "author": "Carver Mead",
        "work": "Introduction to VLSI Systems",
        "quote": "The design of complex **microelectronic** chips requires a hierarchical abstraction that separates logical function from layout physics."
      },
      {
        "author": "Richard Feynman",
        "work": "There's Plenty of Room at the Bottom",
        "quote": "The physical limits of **microelectronic** circuitry will eventually force us to manipulate individual atoms directly."
      },
      {
        "author": "Walter Isaacson",
        "work": "The Innovators",
        "quote": "Silicon Valley's boom arose from the mastery of **microelectronic** fabrication pioneered at Fairchild Semiconductor."
      }
    ]
  },
  "Dashboard — micro\\microelectronics.md": {
    "primary": "The branch of electronics dealing with the miniaturization of electronic circuits and components, especially onto semiconductor chips.",
    "secondary": "The engineering and physics discipline encompassing photolithography, VLSI design, and cleanroom fabrication of integrated circuits.",
    "quotes": [
      {
        "author": "Gordon Moore",
        "work": "Cramming More Components onto Integrated Circuits",
        "quote": "Advances in **microelectronics** will lead to personal portable communications equipment and automatic computers in automobiles."
      },
      {
        "author": "Alvin Toffler",
        "work": "The Third Wave",
        "quote": "The explosion of **microelectronics** replaced heavy mechanical machinery with programmable silicon intelligence across every industry."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "1984: Spring - A Choice of Futures",
        "quote": "Without the quiet triumphs of **microelectronics**, the entire space program would have collapsed under the weight of vacuum tubes."
      }
    ]
  },
  "Dashboard — micro\\microevolution.md": {
    "primary": "Evolutionary change within a species or small group of organisms, especially over a short period of time.",
    "secondary": "In population genetics, changes in allele frequencies across generations driven by natural selection, mutation, genetic drift, or gene flow.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "There is no reason to assume that macroevolution involves processes different from those governing observable **microevolution** in populations."
      },
      {
        "author": "Ernst Mayr",
        "work": "What Evolution Is",
        "quote": "The development of pesticide resistance in crop insects provides a clear, documented example of rapid **microevolution** in action."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Paleontologists debated whether the grand patterns of the fossil record could be fully accounted for by extrapolating **microevolution**."
      }
    ]
  },
  "Dashboard — micro\\micromeria.md": {
    "primary": "A genus of aromatic perennial herbs and dwarf shrubs in the mint family (Lamiaceae), native to the Mediterranean, Africa, and Asia.",
    "secondary": "In economic botany, essential-oil-producing plants rich in carvacrol and thymol, historically used in traditional herbal infusions and folk medicine.",
    "quotes": [
      {
        "author": "Theophrastus",
        "work": "Enquiry into Plants",
        "quote": "On dry and stony Aegean slopes grows the pungent herb **Micromeria**, prized by shepherds for its fragrant, warming tea."
      },
      {
        "author": "John Gerard",
        "work": "The Herball or Generall Historie of Plantes",
        "quote": "The small mountain savoury known to apothecaries as **Micromeria** bears tiny purple blossoms that scent the rocky hillsides."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Rocky limestone crevices in the Himalayan foothills sheltered dwarfed clumps of **Micromeria** growing among wild thyme."
      }
    ]
  },
  "Dashboard — micro\\micrometeor.md": {
    "primary": "A microscopic particle of extraterrestrial dust or debris traveling through space or burning up in the upper atmosphere.",
    "secondary": "In meteoric astronomy, an interplanetary dust grain that produces an imperceptible flash or ion trail upon atmospheric entry.",
    "quotes": [
      {
        "author": "Fred Whipple",
        "work": "The Mystery of Comets",
        "quote": "Cometary disintegration replenishes the zodiacal cloud with millions of drifting **micrometeor** grains each year."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Every day, our planet sweeps up tons of interplanetary dust, each tiny **micrometeor** disintegrating harmlessly in the high mesosphere."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "The Sands of Mars",
        "quote": "Sensors on the orbital hull pinged intermittently as a lone **micrometeor** brushed the outer shielding."
      }
    ]
  },
  "Dashboard — micro\\micrometeoric.md": {
    "primary": "Of, relating to, or caused by micrometeors or interplanetary dust particles.",
    "secondary": "In aerospace engineering, describing erosion, pitting, or collision hazards resulting from high-velocity cosmic dust impacts on spacecraft hulls.",
    "quotes": [
      {
        "author": "Wernher von Braun",
        "work": "First Men to the Moon",
        "quote": "The spacecraft was fitted with multi-layered Whipple bumpers to absorb severe **micrometeoric** bombardment during transit."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "2001: A Space Odyssey",
        "quote": "Long exposure to vacuum left the antenna dish pitted with microscopic craters from continuous **micrometeoric** dust."
      },
      {
        "author": "James Lovell",
        "work": "Lost Moon",
        "quote": "Engineers feared that a stray **micrometeoric** puncture in the thin service module skin might compromise the oxygen tanks."
      }
    ]
  },
  "Dashboard — micro\\micrometeorite.md": {
    "primary": "A tiny extraterrestrial particle (typically smaller than a millimeter) that survives passage through the atmosphere and reaches Earth's surface.",
    "secondary": "In planetary geology, extraterrestrial cosmic spherules recovered from polar ice caps, deep-sea sediments, or rooftop gutters.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "In the red clay of the deepest ocean floor lie dark cosmic spherules, each tiny **micrometeorite** fallen from interplanetary space."
      },
      {
        "author": "Fred Whipple",
        "work": "Earth, Moon, and Planets",
        "quote": "Because of its high surface-to-mass ratio, a slow-moving **micrometeorite** radiates heat rapidly and lands intact without melting."
      },
      {
        "author": "Neil deGrasse Tyson",
        "work": "Astrophysics for People in a Hurry",
        "quote": "You can harvest an ancient extraterrestrial **micrometeorite** simply by running a strong magnet through the silt of your roof gutter."
      }
    ]
  },
  "Dashboard — micro\\micrometeoritic.md": {
    "primary": "Pertaining to or derived from micrometeorites.",
    "secondary": "In cosmochemistry, describing the physical and isotopic characteristics of recovered cosmic dust particles and interplanetary dust grains.",
    "quotes": [
      {
        "author": "Harold Urey",
        "work": "The Planets: Their Origin and Development",
        "quote": "The isotopic ratios observed in **micrometeoritic** dust samples point toward primitive chondritic parent bodies in the outer asteroid belt."
      },
      {
        "author": "Fred Whipple",
        "work": "The Mystery of Comets",
        "quote": "Lunar regolith samples returned by Apollo astronauts showed extensive glass-splattering caused by **micrometeoritic** bombardment."
      },
      {
        "author": "Carl Sagan",
        "work": "Pale Blue Dot",
        "quote": "Over billions of years, the accumulation of **micrometeoritic** material has steadily coated the airless surfaces of asteroids and moons."
      }
    ]
  },
  "Dashboard — micro\\micrometeoroid.md": {
    "primary": "A microscopic meteoroid traveling through space, generally defined as having a mass under one microgram or a diameter under one millimeter.",
    "secondary": "In orbital mechanics and astronautics, high-velocity space debris and dust posing hazard risks to satellites and spacewalking astronauts.",
    "quotes": [
      {
        "author": "Michael Collins",
        "work": "Carrying the Fire",
        "quote": "The extravehicular spacesuit was tailored with reinforced mylar layers to safeguard against a hypervelocity **micrometeoroid** impact."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Rendezvous with Rama",
        "quote": "The cylindrical hull showed the burnished patina of millennia of travel, polished by countless **micrometeoroid** collisions."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Before Apollo launched, astronomers worried that a dense flurry of **micrometeoroid** particles might erode the lander's delicate foil."
      }
    ]
  },
  "Dashboard — micro\\micrometer.md": {
    "primary": "A precision instrument for measuring very small distances, thicknesses, or angles using a fine calibrated screw.",
    "secondary": "A metric unit of length equal to one-millionth (10^-6) of a meter; also written as micrometre or micron.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "By affixing a calibrated screw **micrometer** to the optical tube, I could determine the breadth of a flea's limb with mathematical rigor."
      },
      {
        "author": "Max Born",
        "work": "Principles of Optics",
        "quote": "Optical interference filters achieve precision spacing controlled down to a fraction of a **micrometer**."
      },
      {
        "author": "Henry Maudslay",
        "work": "On the Application of the Slide Rest to Lathes",
        "quote": "My benchtop **micrometer**, which the craftsmen called the Lord Chancellor, could verify tolerances down to the ten-thousandth of an inch."
      }
    ]
  },
  "Dashboard — micro\\micrometry.md": {
    "primary": "The measurement of minute dimensions, distances, or angles using a micrometer.",
    "secondary": "In optical microscopy and astronomy, the quantitative technique of measuring microscopic specimens or stellar separations using calibrated reticles.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "Accurate double-star **micrometry** requires patient, repeated adjustments of the filar wires at the telescope eyepiece."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Through careful cellular **micrometry**, we recorded the exact volumetric shrinkage of chromosomes during mitotic prophase."
      },
      {
        "author": "Antonie van Leeuwenhoek",
        "work": "Letters to the Royal Society",
        "quote": "I practiced a crude form of **micrometry** by comparing the size of blood globules against coarse grains of sand."
      }
    ]
  },
  "Dashboard — micro\\micromicron.md": {
    "primary": "An obsolete metric unit of length equal to one-millionth of a micron, or 10^-12 meter (one picometer).",
    "secondary": "In early twentieth-century radiation physics, a historical unit used to measure X-ray and gamma-ray wavelengths before standard SI picometer adoption.",
    "quotes": [
      {
        "author": "William Henry Bragg",
        "work": "X Rays and Crystal Structure",
        "quote": "The wavelengths of characteristic roentgen rays were initially tabulated in fractions of a **micromicron**."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "Penetrating gamma radiation possesses wavelengths measured in hundreds of **micromicron** units."
      },
      {
        "author": "Niels Bohr",
        "work": "On the Constitution of Atoms and Molecules",
        "quote": "The radius of the inner electron orbit in heavy atoms was estimated at several thousand **micromicron** equivalents."
      }
    ]
  },
  "Dashboard — micro\\micromillimeter.md": {
    "primary": "An obsolete metric unit of length equal to one-thousandth of a millimeter (10^-6 meter); synonymous with the micron or micrometer.",
    "secondary": "In late nineteenth-century histological literature, a unit frequently used to report the dimensions of bacteria, blood cells, and spores.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "The tubercle bacillus measures between two and four **micromillimeter** lengths, appearing as slender, beaded rods."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Cell Theory",
        "quote": "The diameter of mammalian red corpuscles rarely exceeds eight **micromillimeter** across their circular discs."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The active yeast cells had an average diameter of ten **micromillimeter**, easily resolved under a four-hundred-power objective."
      }
    ]
  },
  "Dashboard — micro\\micromillimetre.md": {
    "primary": "The British/Commonwealth spelling of micromillimeter; one-thousandth of a millimetre (10^-6 metre), equivalent to the micron.",
    "secondary": "In historical Victorian microscopy and cytology, a standard dimensional unit used to quantify microscopic structures and biological fibers.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The sensitive hairs of the sundew bend when touched by particles measuring mere fractions of a **micromillimetre**."
      },
      {
        "author": "Lord Rayleigh",
        "work": "The Theory of Sound",
        "quote": "The amplitude of atmospheric vibrations capable of evoking an audible sensation is less than one **micromillimetre**."
      },
      {
        "author": "Joseph Lister",
        "work": "On the Antiseptic Principle in the Practice of Surgery",
        "quote": "The micro-organisms responsible for surgical putrefaction measure only two or three **micromillimetre** in length."
      }
    ]
  },
  "Dashboard — micro\\micromyx.md": {
    "primary": "A genus of small sea snails or marine gastropod mollusks in the family Epitoniidae or Pyramidellidae.",
    "secondary": "In malacology, minute marine snails characterized by delicate, high-spired shells inhabiting benthic sandy substrates.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes and Marine Life",
        "quote": "Benthic dredges brought up fine sediment rich in minute gastropods, including fragile shells of **Micromyx**."
      },
      {
        "author": "William Healey Dall",
        "work": "Contributions to the Tertiary Fauna of Florida",
        "quote": "The fossil deposits in the Caloosahatchee beds preserve exquisite specimens of the genus **Micromyx**."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Year at the Shore",
        "quote": "Among the sifted gravel of the tidal pool rested tiny shells of **Micromyx**, barely discernible without a hand lens."
      }
    ]
  },
  "Dashboard — micro\\micron.md": {
    "primary": "A metric unit of length equal to one-millionth (10^-6) of a meter; officially designated as the micrometer (µm).",
    "secondary": "In cellular biology and precision manufacturing, a standard benchmark unit for measuring cells, wavelengths of infrared light, and mechanical tolerances.",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "There's Plenty of Room at the Bottom",
        "quote": "A biological cell is a marvelous factory packed with molecular machines operating within an envelope of just a few **micron**."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Infrared satellites observe distant protostellar nurseries at wavelengths spanning ten to one hundred **micron**."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "Under the microscope, retinal cone photoreceptors measured mere fractions of a **micron** across their sensitive tips."
      }
    ]
  },
  "Dashboard — micro\\micronase.md": {
    "primary": "A brand name for glyburide (glibenclamide), a sulfonylurea medication used to treat type 2 diabetes by stimulating insulin release.",
    "secondary": "In clinical pharmacology, an oral hypoglycemic agent that binds to ATP-sensitive potassium channels on pancreatic beta cells.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "The geriatrician reviewed the patient's prescriptions, carefully adjusting the daily dose of **Micronase** to avoid nocturnal hypoglycemia."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "We stabilized the diabetic patient's blood sugar using dietary modifications combined with low-dose **Micronase**."
      },
      {
        "author": "Paul Farmer",
        "work": "Pathologies of Power",
        "quote": "Access to essential oral antidiabetic agents like **Micronase** remains critical for chronic disease management in community clinics."
      }
    ]
  },
  "Dashboard — micro\\micronesia.md": {
    "primary": "A subregion of Oceania comprising thousands of small islands in the western Pacific Ocean, north of Melanesia and west of Polynesia.",
    "secondary": "In historical and anthropological geography, an island realm including the Caroline, Marshall, Mariana, and Gilbert Islands with distinctive navigational traditions.",
    "quotes": [
      {
        "author": "Margaret Mead",
        "work": "Male and Female",
        "quote": "The seafaring cultures across **Micronesia** perfected celestial navigation techniques that guided outrigger canoes over open oceans."
      },
      {
        "author": "Herman Melville",
        "work": "Omoo",
        "quote": "Sailors spoke with awe of the distant, sun-drenched archipelagos of **Micronesia** scattered like emeralds across the blue Pacific."
      },
      {
        "author": "Jared Diamond",
        "work": "Guns, Germs, and Steel",
        "quote": "Austronesian voyagers colonized the scattered coral atolls of **Micronesia**, adapting their agricultural systems to fragile reef ecologies."
      }
    ]
  },
  "Dashboard — micro\\micronor.md": {
    "primary": "A brand name for norethindrone, a progestin-only oral contraceptive pill often called the 'mini-pill'.",
    "secondary": "In gynecological pharmacology, a synthetic progestin that prevents pregnancy primarily by thickening cervical mucus and altering endometrium lining.",
    "quotes": [
      {
        "author": "Carl Djerassi",
        "work": "This Man's Pill",
        "quote": "The formulation of progestin-only pills like **Micronor** offered an effective alternative for nursing mothers sensitive to estrogen."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The clinic dispensary kept supplies of **Micronor** on hand for postpartum patients seeking safe contraception."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "The chemical synthesis of oral progestins like **Micronor** catalyzed unprecedented social and demographic transformations in twentieth-century medicine."
      }
    ]
  },
  "Dashboard — micro\\micronutrient.md": {
    "primary": "A chemical element or substance required in trace amounts for the normal growth, development, and physiology of an organism.",
    "secondary": "In human nutrition and agronomy, essential dietary vitamins and trace minerals (such as iron, zinc, and iodine) that sustain enzymatic and cellular functions.",
    "quotes": [
      {
        "author": "Michael Pollan",
        "work": "In Defense of Food",
        "quote": "Nutritionism shifted public focus away from wholesome whole foods toward the isolated **micronutrient** in supplement bottles."
      },
      {
        "author": "Paul Farmer",
        "work": "Infections and Inequalities",
        "quote": "Treating endemic infectious diseases in impoverished populations requires simultaneously addressing severe **micronutrient** deficiencies."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Healthy agricultural soil provides an intricate reservoir of every vital **micronutrient** required by growing plants."
      }
    ]
  },
  "Dashboard — micro\\microorganism.md": {
    "primary": "A microscopic organism, especially a bacterium, virus, fungus, or protozoan, too small to be seen without magnification.",
    "secondary": "In environmental science and biotechnology, a unicellular agent driving biogeochemical transformations, fermentation, and infectious pathology.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Beer",
        "quote": "The alteration of the fermenting wort is caused entirely by the development of an alien **microorganism** introduced from the atmosphere."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "If life exists in the subterranean brine of Mars, it will almost certainly take the form of an extremophilic **microorganism**."
      },
      {
        "author": "Ed Yong",
        "work": "I Contain Multitudes",
        "quote": "Every breath we inhale and every surface we touch immerses us in an invisible sea teeming with **microorganism** life."
      }
    ]
  },
  "Dashboard — micro\\microradian.md": {
    "primary": "A unit of angular measurement equal to one-millionth (10^-6) of a radian (approximately 0.206 arcseconds).",
    "secondary": "In precision optics, geodetic surveying, and laser beam steering, a standard unit for defining extremely tight pointing accuracies and beam divergences.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Spacecraft tracking lasers achieve pointing stabilities measured in fractions of a **microradian** across millions of miles."
      },
      {
        "author": "Richard Feynman",
        "work": "Feynman Lectures on Physics",
        "quote": "Interferometers detect tiny surface deflections on the order of a **microradian** caused by thermal gradients."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "The Fountains of Paradise",
        "quote": "The laser guidance beam for the orbital elevator was calibrated to maintain alignment within a single **microradian**."
      }
    ]
  },
  "Dashboard — micro\\microscopically.md": {
    "primary": "By means of a microscope; with optical magnification.",
    "secondary": "In minute or microscopic detail; in a manner that reveals tiny, imperceptible nuances or structural features.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Sherlock Holmes examined the bloodstains **microscopically**, verifying the presence of distinct crystalline hemoglobin deposits."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "When we examine **microscopically** the structure of these intricate organs, adaptations of marvellous complexity appear."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "She scrutinized her own fleeting sensations **microscopically**, tracing each ripple of feeling that passed across her mind."
      }
    ]
  },
  "Dashboard — micro\\microscopist.md": {
    "primary": "A scientist or technician who is skilled in the use of microscopes to examine minute objects.",
    "secondary": "A specialist in optical, electron, or scanning-probe microscopy who prepares and analyzes histological or material specimens.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "It is the duty of the true **microscopist** to approach nature with an unprejudiced eye and a steady hand upon the focus screws."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Advice for a Young Investigator",
        "quote": "The tireless **microscopist** must possess the visual patience of a hunter lying in wait for elusive prey."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "The Autocrat of the Breakfast-Table",
        "quote": "To the avid **microscopist**, a drop of pond water becomes a teeming colosseum crowded with fantastic combatants."
      }
    ]
  },
  "Dashboard — micro\\microscopium.md": {
    "primary": "A minor and faint southern constellation introduced in the eighteenth century by French astronomer Nicolas-Louis de Lacaille.",
    "secondary": "In observational astronomy, a constellation representing the scientific microscope, situated south of Capricornus and east of Sagittarius.",
    "quotes": [
      {
        "author": "Nicolas-Louis de Lacaille",
        "work": "Coelum Australe Stelliferum",
        "quote": "I designated the faint stars between Sagittarius and Piscis Austrinus as **Microscopium**, commemorating the triumph of optical science."
      },
      {
        "author": "John Herschel",
        "work": "Results of Astronomical Observations Made at the Cape of Good Hope",
        "quote": "Sweeping through the southern quadrant, my telescope surveyed the faint double stars and planetary nebulae in **Microscopium**."
      },
      {
        "author": "Patrick Moore",
        "work": "The Observer's Book of Astronomy",
        "quote": "Though **Microscopium** contains no bright stars, its third-magnitude gamma star guides observers toward faint background galaxies."
      }
    ]
  },
  "Dashboard — micro\\microscopy.md": {
    "primary": "The technical use of microscopes to view objects and areas of objects that cannot be seen with the naked eye.",
    "secondary": "The scientific discipline comprising optical, fluorescence, confocal, and electron imaging modalities that illuminate nanoscale biological and material architecture.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Contributions to the Theory of the Microscope",
        "quote": "Diffraction sets an inescapable physical barrier upon optical **microscopy**, limiting resolution to half the wavelength of illuminating light."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Refinements in histological staining transformed neurological **microscopy** into an exact anatomical science."
      },
      {
        "author": "Richard Feynman",
        "work": "There's Plenty of Room at the Bottom",
        "quote": "The development of electron **microscopy** allowed us to resolve viruses and macromolecular assemblies directly."
      }
    ]
  },
  "Dashboard — micro\\microsecond.md": {
    "primary": "A unit of time equal to one-millionth (10^-6) of a second.",
    "secondary": "In computing and high-energy physics, a standard interval used to measure processor instruction timings, electronic switching speeds, and subatomic decay rates.",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "Surely You're Joking, Mr. Feynman!",
        "quote": "At Los Alamos, explosive implosion switches had to fire within a fraction of a **microsecond** to achieve critical density."
      },
      {
        "author": "Alan Turing",
        "work": "Proposal for Development of an Automatic Computing Engine (ACE)",
        "quote": "The mercury delay line memory registers pulses spaced at intervals of less than one **microsecond**."
      },
      {
        "author": "Stephen Hawking",
        "work": "A Brief History of Time",
        "quote": "During the first **microsecond** after the Big Bang, quarks and gluons condensed to form protons and neutrons."
      }
    ]
  },
  "Dashboard — micro\\microseism.md": {
    "primary": "A faint, continuous tremor or earth vibration caused by natural phenomena such as ocean waves, atmospheric storms, or wind.",
    "secondary": "In geophysics and seismology, ambient background seismic noise generated primarily by the interaction of ocean swells with the seafloor and coastlines.",
    "quotes": [
      {
        "author": "Beno Gutenberg",
        "work": "Seismological Evidence for Roots of Mountains",
        "quote": "Seismograph traces across North America record a continuous **microseism** background driven by North Atlantic winter gales."
      },
      {
        "author": "Charles Richter",
        "work": "Elementary Seismology",
        "quote": "Before identifying a true earthquake arrival, the geophysicist must filter out the rhythmic hum of ocean-generated **microseism** waves."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Pounding surf against rocky coastlines sends deep acoustic pulses through bedrock, recorded as a persistent **microseism** hundreds of miles inland."
      }
    ]
  },
  "Dashboard — micro\\microsomal.md": {
    "primary": "Of, relating to, or derived from microsomes (vesicular fragments of the endoplasmic reticulum).",
    "secondary": "In biochemistry and toxicology, denoting the microsomal enzyme system (such as cytochrome P450) responsible for drug metabolism and detoxification.",
    "quotes": [
      {
        "author": "Christian de Duve",
        "work": "A Guided Tour of the Living Cell",
        "quote": "Centrifugation of liver homogenates concentrates the **microsomal** fraction, which harbors key steroid and drug-metabolizing enzymes."
      },
      {
        "author": "George Palade",
        "work": "Intracellular Aspects of the Process of Protein Synthesis",
        "quote": "Ribosomes attached to the **microsomal** membranes synthesize secretory proteins destined for export from the cell."
      },
      {
        "author": "Arthur Kornberg",
        "work": "For the Love of Enzymes",
        "quote": "The **microsomal** cytochrome P450 monooxygenase system performs remarkable hydroxylations on hydrophobic xenobiotic compounds."
      }
    ]
  },
  "Dashboard — micro\\microsome.md": {
    "primary": "A small vesicle formed from pieces of the endoplasmic reticulum when eukaryotic cells are broken up in the laboratory.",
    "secondary": "In cell biology and biochemistry, an artifact of tissue homogenization consisting of membrane vesicles studded with or free of ribosomes.",
    "quotes": [
      {
        "author": "Albert Claude",
        "work": "The Coming of Age of the Cell",
        "quote": "Differential centrifugation permitted the isolation of the sub-microscopic particulate fraction that we designated the **microsome**."
      },
      {
        "author": "Christian de Duve",
        "work": "Exploring Cells with a Centrifuge",
        "quote": "Under the electron beam, each isolated **microsome** proved to be a pinched-off fragment of the endoplasmic reticulum."
      },
      {
        "author": "James Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Initial in vitro translation experiments incubated isolated **microsome** pellets with amino acids to measure protein incorporation."
      }
    ]
  },
  "Dashboard — micro\\microsorium.md": {
    "primary": "A genus of ferns in the family Polypodiaceae (often spelled Microsorum), widely cultivated as decorative indoor or aquarium plants.",
    "secondary": "In horticultural botany, tropical creeping ferns such as the Java fern (Microsorum pteropus), featuring leathery green fronds and aquatic adaptability.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Moist basalt cliffs along stream banks were carpeted with the creeping rhizomes of the hardy fern **Microsorium**."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "In freshwater streams across Southeast Asia, submerged clumps of **Microsorium** cling tenaciously to submerged driftwood."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The sori of **Microsorium** are scattered irregularly over the lower surface of the undivided, lanceolate blade."
      }
    ]
  },
  "Dashboard — micro\\microsporangium.md": {
    "primary": "A sporangium that produces microspores, which in seed plants develop into male gametophytes (pollen grains).",
    "secondary": "In gymnosperms and angiosperms, the pollen sac within the anther or male cone where microsporocytes undergo meiosis to yield haploid pollen.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "An angiosperm anther typically contains four elongated lobes, each functioning as a fertile **microsporangium**."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Meiotic divisions within the **microsporangium** generate tetrads of microspores that mature into powdery pollen."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "The tapetum lining the inner wall of the **microsporangium** nourishes developing spores and contributes sporopollenin to their outer walls."
      }
    ]
  },
  "Dashboard — micro\\microspore.md": {
    "primary": "The smaller of the two types of spores produced by heterosporous plants, which develops into a male gametophyte (pollen grain).",
    "secondary": "In plant reproductive biology, the haploid cell produced by meiosis of a microsporocyte within the microsporangium.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Following meiotic cytokinesis, each haploid **microspore** develops a durable, sculptured exine coat composed of sporopollenin."
      },
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by which Orchids are Fertilised by Insects",
        "quote": "In orchid pollinia, thousands of individual **microspore** cells cohere into viscous masses adapted for insect dispersal."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "The evolutionary breakthrough of heterospory enabled the **microspore** to specialize exclusively for aerodynamic transport."
      }
    ]
  },
  "Dashboard — micro\\microsporidian.md": {
    "primary": "A microscopic, spore-forming, single-celled obligate intracellular parasite belonging to the phylum Microsporidia, closely related to fungi.",
    "secondary": "In parasitology, an opportunistic pathogen possessing a unique polar tube injection apparatus used to inoculate sporoplasm into host cells.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on the Disease of Silkworms (Pebrine)",
        "quote": "The epidemic destroying French silk production was traced to a lethal **microsporidian** parasite infecting the caterpillars."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Insect Societies",
        "quote": "Colony collapse in social insects can be precipitated when a virulent **microsporidian** invades the midgut epithelium of worker bees."
      },
      {
        "author": "Carl Zimmer",
        "work": "Parasite Rex",
        "quote": "The coiled polar filament inside a dormant **microsporidian** spore uncoils explosively like a harpoon to breach the host cell wall."
      }
    ]
  },
  "Dashboard — micro\\microsporophyll.md": {
    "primary": "A modified leaf that bears microsporangia, such as the stamens of flowering plants or the pollen scales of conifer cones.",
    "secondary": "In comparative plant morphology, the homologous male reproductive appendage in lycophytes, gymnosperms, and angiosperms.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Comparative morphologists interpret the angiosperm stamen as an evolutionarily modified, reduced **microsporophyll**."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "On the male pine cone, each spirally arranged woody scale represents a fertile **microsporophyll** bearing two pollen sacs beneath."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "The transition from ancient fern fronds to seed-plant cones involved the progressive differentiation of **microsporophyll** structures."
      }
    ]
  },
  "Dashboard — micro\\microsporum.md": {
    "primary": "A genus of fungi that causes dermatophytosis (ringworm, tinea capitis, and other fungal infections of the skin, hair, and nails).",
    "secondary": "In medical mycology, keratinophilic molds characterized by rough-walled, spindle-shaped macroconidia that infect humans and domestic animals.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Examination of plucked scalp hairs under Wood's light revealed bright greenish fluorescence characteristic of **Microsporum** audouinii."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "Mycologists isolated pathogenic strains of **Microsporum** from feline fur that transmitted ringworm lesions to children."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "Antifungal agents must overcome the tough keratinaceous barriers colonized by stubborn hyphae of **Microsporum**."
      }
    ]
  },
  "Dashboard — micro\\microstomus.md": {
    "primary": "A genus of righteye flounders in the family Pleuronectidae, notably including the Dover sole (Microstomus pacificus) and lemon sole (Microstomus kitt).",
    "secondary": "In marine fisheries biology, bottom-dwelling flatfishes characterized by small mouths, asymmetrical skull morphology, and benthic camouflage.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The Pacific Dover sole, classified under **Microstomus**, inhabits deep continental shelf waters off the coast of California."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Trawlers dragging the muddy continental slope brought up slimy, healthy specimens of **Microstomus** from cold bottom currents."
      },
      {
        "author": "William Beebe",
        "work": "The Arcturus Adventure",
        "quote": "The small-mouthed flounder **Microstomus** rests motionless upon the silt, perfectly mimicking the texture of the seabed."
      }
    ]
  },
  "Dashboard — micro\\microstrobos.md": {
    "primary": "A former genus of small coniferous shrubs in the podocarp family (Podocarpaceae), native to Australia and Tasmania (now Pherosphaera).",
    "secondary": "In botanical dendrology, dwarf montane alpine conifers characterized by tiny scale-like leaves and miniature cones adapted to cold peat bogs.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Botany of the Antarctic Voyage",
        "quote": "Among the alpine cushion bogs of the Tasmanian highlands, we discovered creeping shrubs of **Microstrobos** clinging to wet dolerite."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The archaic gymnosperm **Microstrobos** provides an important evolutionary link within the southern family Podocarpaceae."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "The miniature evergreen twigs of **Microstrobos** survive relentless sub-Antarctic gales by hugging the icy scree."
      }
    ]
  },
  "Dashboard — micro\\microsurgery.md": {
    "primary": "Surgery performed on minute or delicate body structures using an operating microscope and miniature precision instruments.",
    "secondary": "In reconstructive and neurosurgical medicine, the specialized anastomosing of micro-vessels and nerves under high-power optical magnification.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Pioneering plastic surgeons employed **microsurgery** to reattach severed digits, reconnecting blood vessels thinner than sewing thread."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Advances in optical **microsurgery** allowed neurosurgeons to excise deep intracranial tumors while sparing adjacent cranial nerves."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "The recovery of limb sensation depended on delicate **microsurgery** that meticulously realigned severed peripheral nerve fascicles."
      }
    ]
  },
  "Dashboard — micro\\microtaggant.md": {
    "primary": "A microscopic, coded particle added to explosives, paint, or other materials to allow tracing of origin and manufacture.",
    "secondary": "In forensic science and counter-terrorism, multi-layered colored plastic or magnetic micro-particles that survive detonations to identify batch and producer.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Forensic chemists sifted blast debris under the microscope to retrieve a color-coded **microtaggant** linking the bomb to a commercial factory."
      },
      {
        "author": "Richard Rhodes",
        "work": "The Making of the Atomic Bomb",
        "quote": "To track explosive materials, modern manufacturers embed a resilient chemical **microtaggant** in industrial gunpowder."
      },
      {
        "author": "J. Edgar Hoover",
        "work": "Masters of Deceit",
        "quote": "The recovery of a single synthetic **microtaggant** at a crime scene provides investigators with unambiguous chain-of-custody evidence."
      }
    ]
  },
  "Dashboard — micro\\microtome.md": {
    "primary": "An instrument for cutting extremely thin sections of tissue or material for examination under a microscope.",
    "secondary": "In histology and material science, a mechanical apparatus with steel, glass, or diamond blades that produces ribbon sections measuring a few microns thick.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "With a sliding **microtome**, we shaved frozen brain tissue into translucent ribbons twenty microns in thickness."
      },
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "To examine cork cells, I fashioned a crude forerunner of the **microtome** to slice razor-thin shavings from the bark."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The neuropathologist mounted formalin-fixed brainstem blocks into the **microtome** to prepare stained cross-sections of the substantia nigra."
      }
    ]
  },
  "Dashboard — micro\\microtubule.md": {
    "primary": "A microscopic, tubular structure present in numbers in the cytoplasm of cells, forming part of the cytoskeleton.",
    "secondary": "In cell biology, a dynamic polymer composed of alpha- and beta-tubulin dimers that forms the mitotic spindle, cilium axonemes, and intracellular transport tracks.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Motor proteins such as kinesin and dynein march along each **microtubule** track, ferrying secretory vesicles to the cell cortex."
      },
      {
        "author": "Roger Penrose",
        "work": "Shadows of the Mind",
        "quote": "Stuart Hameroff and I hypothesized that quantum coherent computations might occur within the hollow lattice of the neuronal **microtubule**."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Taxol halts cancerous division by stabilizing the cellular **microtubule** network, preventing mitotic spindles from disassembling."
      }
    ]
  },
  "Dashboard — micro\\microtus.md": {
    "primary": "A genus of small rodents in the subfamily Arvicolinae, commonly known as meadow voles or field voles.",
    "secondary": "In mammalogy and behavioral ecology, widespread northern hemisphere rodents extensively studied for social monogamy (prairie vole) and cyclic population dynamics.",
    "quotes": [
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Under the snow crust, trails engineered by the meadow mouse **Microtus** crisscross the dormant clover fields."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Speciation patterns across the genus **Microtus** demonstrate how geographic isolation across Pleistocene glacial refugia shaped rodent diversity."
      },
      {
        "author": "Frans de Waal",
        "work": "The Age of Empathy",
        "quote": "Studies of oxytocin receptors in the brain of **Microtus** ochrogaster revolutionized our neurobiological understanding of monogamous pair bonding."
      }
    ]
  },
  "Dashboard — mon\\amon.md": {
    "primary": "A supreme deity in ancient Egyptian religion, revered as the King of the Gods, personifying air, breath, and hidden power; later syncretized as Amon-Ra.",
    "secondary": "In historical theology and classical mythology, the oracular god of Thebes whose desert shrine at Siwa was visited by Alexander the Great.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "Histories",
        "quote": "The Egyptians give the name of **Amon** to Zeus, and depict his sacred image with the head and curved horns of a ram."
      },
      {
        "author": "Plutarch",
        "work": "Life of Alexander",
        "quote": "When Alexander reached the oasis temple of **Amon**, the chief priest addressed him as the true son of the god."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The Libyan Jove, or **Amon** called, that held / Great Thebes in awe, and walked the desert wild."
      }
    ]
  },
  "Dashboard — mon\\demon.md": {
    "primary": "An evil spirit or supernatural being, traditionally believed to possess people or torment mortals.",
    "secondary": "In classical antiquity (daimon), a benevolent or mediating guardian spirit; in modern physics and computing, an autonomous background process or thought experiment.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "If we conceive of a being whose faculties are so sharpened that he can follow every molecule, this finite **demon** could violate the second law."
      },
      {
        "author": "Plato",
        "work": "Apology",
        "quote": "A divine and spiritual sign comes to me, a voice of a **demon** that turns me away from doing what is unjust."
      },
      {
        "author": "Dante Alighieri",
        "work": "Inferno",
        "quote": "No horned **demon** of the pit could strike greater dread into the cowering shade upon the burning pitch."
      }
    ]
  },
  "Dashboard — mon\\demonism.md": {
    "primary": "The belief in or worship of demons and malevolent supernatural spirits.",
    "secondary": "In comparative religion and cultural anthropology, a religious or folkloric system attributing natural disasters, diseases, or mental illness to demonic agency.",
    "quotes": [
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Animism inevitably gives rise to **demonism**, wherein hostile spiritual entities are invoked to explain disease and misfortune."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The dark undercurrent of **demonism** lingers in ascetic traditions where the soul battles unseen spiritual adversaries."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The expulsion of evils in seasonal ceremonies served to rid the settlement of lingering **demonism** and malevolent ghosts."
      }
    ]
  },
  "Dashboard — mon\\mon.md": {
    "primary": "A combining form derived from Greek monos, meaning single, sole, or alone; or a traditional Japanese heraldic emblem or crest.",
    "secondary": "In Asian ethnolinguistics, referring to the Mon people and Mon language family of Myanmar and Thailand, key transmitters of Theravada Buddhism.",
    "quotes": [
      {
        "author": "Basil Hall Chamberlain",
        "work": "Things Japanese",
        "quote": "Every aristocratic samurai family in feudal Japan bore its distinctive family crest or **mon** embroidered on ceremonial kimonos."
      },
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The classical prefix **mon** signifies singularity across hundreds of scientific and mathematical compounds."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "The Way of the Masks",
        "quote": "Heraldic emblems like the Japanese **mon** function as visual shorthand encoding lineage, territory, and ancestral authority."
      }
    ]
  },
  "Dashboard — mon\\monachism.md": {
    "primary": "The monastic life or system; the practice of living as a monk under religious vows of poverty, chastity, and obedience.",
    "secondary": "In ecclesiastical history, the institutional ascetic movement originating in Egyptian desert hermitages and flourishing across medieval Europe and Asia.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The rapid spread of Christian **monachism** populated the desolate sands of the Nile with thousands of solitary hermits."
      },
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "Medieval Catholic **monachism** channeled ascetic rigor into the cloister, separating spiritual devotion from worldly labor."
      },
      {
        "author": "Desiderius Erasmus",
        "work": "The Praise of Folly",
        "quote": "He satirized the empty ritualism into which late medieval **monachism** had degenerated, urging a return to simple Gospel piety."
      }
    ]
  },
  "Dashboard — mon\\monad.md": {
    "primary": "An indivisible, ultimate unit or entity; in philosophy, a fundamental, indivisible metaphysical substance.",
    "secondary": "In Leibnizian philosophy, an immaterial soul-like substance reflecting the universe; in functional programming, a design pattern encapsulating computations.",
    "quotes": [
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "The Monadology",
        "quote": "The **monad**, of which we shall speak here, is nothing but a simple substance which enters into compounds."
      },
      {
        "author": "Giordano Bruno",
        "work": "On the Monad, Number, and Figure",
        "quote": "The ultimate physical minimum and the divine metaphysical source are alike mirrored within the eternal **monad**."
      },
      {
        "author": "Bertrand Russell",
        "work": "A Critical Exposition of the Philosophy of Leibniz",
        "quote": "Since each **monad** has no windows through which anything could enter or leave, all its perceptions arise from its own nature."
      }
    ]
  },
  "Dashboard — mon\\monadic.md": {
    "primary": "Relating to or having the nature of a monad; consisting of a single unit or element.",
    "secondary": "In logic and mathematics, designating an operator, function, or relation that takes exactly one argument (unary); in computer science, pertaining to monads.",
    "quotes": [
      {
        "author": "Willard Van Orman Quine",
        "work": "Word and Object",
        "quote": "A **monadic** predicate expresses a simple property attributable to an individual entity without external relation."
      },
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "quote": "Actual entities are the final real things of which the world is made up, possessing essentially **monadic** individuality."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "The classical theory of judgment assumed that all propositions could be reduced to the **monadic** subject-predicate form."
      }
    ]
  },
  "Dashboard — mon\\monal.md": {
    "primary": "A large, brilliantly colored Asian pheasant of the genus Lophophorus, notably the Himalayan monal (the national bird of Nepal).",
    "secondary": "In ornithology, a high-altitude galliform bird native to the Himalayan oak and rhododendron forests, famed for iridescent metallic plumage.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The dazzling, kaleidoscopic plumage of the male Himalayan **monal** evolved under the rigorous aesthetic scrutiny of female mate choice."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Himalayan Journals",
        "quote": "At timberline in the Sikkim mountains, coveys of the radiant pheasant **monal** burst from the rhododendron scrub with loud whistling calls."
      },
      {
        "author": "David Attenborough",
        "work": "The Life of Birds",
        "quote": "Few sights in the high Himalayas rival the sunlit flash of a male **monal** launching across an alpine gorge."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Math Part 2 - Batch 3 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
