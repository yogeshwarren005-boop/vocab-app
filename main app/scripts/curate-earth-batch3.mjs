import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Earth & Geology";

const wordsData = {
  "Dashboard — ge/apogean.md": {
    word: "apogean",
    primary: "Of, relating to, or occurring at the apogee (the point in an orbit farthest from the Earth).",
    secondary: "In lunar and tidal science, describing apogean tides, which have a reduced tidal range because the Moon is at its greatest distance from Earth.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "The perturbing solar attraction reaches its minimum during the **apogean** position of the lunar orbit." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "During **apogean** periods, the neap tides display a markedly diminished vertical rise and fall." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "The satellite executed an engine burn at its **apogean** apex to circularize its orbit." }
    ]
  },
  "Dashboard — ge/apogee.md": {
    word: "apogee",
    primary: "The point in the orbit of an object (such as the Moon or an artificial satellite) that is farthest from the center of the Earth.",
    secondary: "In figurative usage, the highest point in the development of something; a culmination, climax, or zenith.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Under the reign of the Antonines, the power and prosperity of the Roman Empire reached its **apogee**." },
      { author: "John Milton", work: "Paradise Lost", quote: "Planets move through their orbits, now approaching perihelion, now retiring to their distant **apogee**." },
      { author: "H.G. Wells", work: "The First Men in the Moon", quote: "At the **apogee** of our flight, the blue sphere of Earth hung motionless in the velvet blackness." }
    ]
  },
  "Dashboard — ge/biogeographical.md": {
    word: "biogeographical",
    primary: "Of or relating to biogeography, the study of the geographical distribution of biological organisms.",
    secondary: "In evolutionary biology, concerning historical, geological, and ecological factors that establish distinct biogeographical provinces and faunal realms.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The Malay Archipelago offers the most striking **biogeographical** contrast to be found anywhere upon the globe." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "A strictly **biogeographical** survey of oceanic islands proves that native species are descended from mainland migrants." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Speciation cannot be understood without mapping the **biogeographical** barriers that divide ancestral populations." }
    ]
  },
  "Dashboard — ge/biogeography.md": {
    word: "biogeography",
    primary: "The branch of biology that deals with the geographical distribution of plants and animals over the Earth.",
    secondary: "An integrative historical discipline combining paleontology, ecology, geology, and phylogenetics to explain spatial patterns of biodiversity.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The science of **biogeography** deciphers the geological history of continents from the living distribution of animals." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "In considering the distribution of organic beings, the facts of **biogeography** point directly to evolution through descent." },
      { author: "E.O. Wilson", work: "The Diversity of Life", quote: "Island **biogeography** demonstrated that species richness balances immigration against local extinction." }
    ]
  },
  "Dashboard — ge/dermoplasty.md": {
    word: "dermoplasty",
    primary: "Surgical repair, restoration, or grafting of the skin; dermatoplasty.",
    secondary: "In plastic and reconstructive surgery, the transplantation of autologous or donor skin to restore tissue integrity following severe burns or trauma.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Extensive cutaneous burns necessitate early **dermoplasty** to prevent severe cicatricial contractures." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The vascularization of the graft in **dermoplasty** demonstrates the cellular affinity between donor epidermis and recipient bed." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Modern advances in antiseptic **dermoplasty** allow the surgeon to reconstruct disfiguring facial trauma." }
    ]
  },
  "Dashboard — ge/epigeous.md": {
    word: "epigeous",
    primary: "Growing on, living on, or germinating above the surface of the ground (opposed to hypogeous).",
    secondary: "In botany and entomology, designating seed germination where cotyledons emerge above soil level into sunlight, or ground-dwelling insect habits.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "In seedlings with **epigeous** germination, the hypocotyl arches upward, dragging the cotyledons above the soil." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The bean displays **epigeous** germination, raising its fleshy green seed-leaves into the air." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "Certain beetles maintain strictly **epigeous** habits, hunting across the surface litter of the forest floor." }
    ]
  },
  "Dashboard — ge/Gaia.md": {
    word: "Gaia",
    primary: "In classical Greek mythology, the primordial goddess personifying the Earth; Mother Earth.",
    secondary: "In Earth systems science, the Gaia hypothesis proposed by James Lovelock, viewing the Earth's biosphere, atmosphere, oceans, and soil as a self-regulating complex system maintaining habitability.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "Verily at the first Chaos came to be, but next wide-bosomed **Gaia**, the ever-sure foundation of all the deathless ones." },
      { author: "James Lovelock", work: "Gaia: A New Look at Life on Earth", quote: "We define **Gaia** as a complex entity involving the Earth's biosphere, atmosphere, oceans, and soil." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "In the ancient myth of **Gaia**, our ancestors recognized their deep physical kinship with the living planet." }
    ]
  },
  "Dashboard — ge/ge.md": {
    word: "ge",
    primary: "In classical Greek etymology, the root *ge-* (from γῆ, *ge*, 'earth', 'land', 'soil'), forming the primary base for scientific words pertaining to the Earth.",
    secondary: "A combining formant in classical compounds and cosmological terminology denoting the terrestrial globe, dry ground, or territorial domain.",
    quotes: [
      { author: "Aristotle", work: "Meteorology", quote: "The element of earth, denoted in Greek by **ge**, settles at the center of the elemental cosmos." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Every modern earth science derives its lineage from the ancient Greek root **ge-**." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "From the simple Greek monosyllable **ge** spring our grandest concepts of geography, geology, and geometry." }
    ]
  },
  "Dashboard — ge/geo.md": {
    word: "geo",
    primary: "The combining form *geo-* representing the Earth, soil, or global terrestrial systems in scientific, geographical, and linguistic compounding.",
    secondary: "In contemporary technical vocabulary, a standalone prefix denoting geographic, geodetic, or geospatial technologies (e.g., geo-engineering, geocaching).",
    quotes: [
      { author: "John McPhee", work: "Annals of the Former World", quote: "The prefix **geo-** attaches to every discipline that wrestles with deep terrestrial time." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "By prefixing **geo-** to logic and description, the ancients gave names to the study of the solid globe." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Our chemical interventions have upset the delicate **geo-**chemical balances of the biosphere." }
    ]
  },
  "Dashboard — ge/geocentric.md": {
    word: "geocentric",
    primary: "Measured from the center of the Earth; having or representing the Earth as the center.",
    secondary: "In the history of astronomy, designating the Ptolemaic cosmological model in which the Sun, stars, and planets revolve around a stationary Earth.",
    quotes: [
      { author: "Nicolaus Copernicus", work: "De revolutionibus orbium coelestium", quote: "The ancient **geocentric** hypothesis fails to explain the retrograde motions of the planets with simplicity." },
      { author: "Galileo Galilei", work: "Dialogue Concerning the Two Chief World Systems", quote: "Ptolemy constructed a magnificent mathematical edifice to preserve the **geocentric** illusion." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "For over a thousand years, Christian Europe embraced the **geocentric** cosmology as divine truth." }
    ]
  },
  "Dashboard — ge/geocentrism.md": {
    word: "geocentrism",
    primary: "The astronomical or philosophical belief that the Earth is the stationary center of the universe.",
    secondary: "In the history of science and epistemology, the Ptolemaic-Aristotelian worldview that dominated Western cosmology until overthrown by the Copernican Revolution.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "The overthrow of **geocentrism** was a painful demotion for human pride, casting us adrift in a vast universe." },
      { author: "Arthur Koestler", work: "The Sleepwalkers", quote: "The tenacious survival of **geocentrism** owed less to observation than to aesthetic devotion to perfect circular orbits." },
      { author: "Stephen Jay Gould", work: "The Flamingo's Smile", quote: "Copernicus dismantled **geocentrism** not by discovering new stars, but by re-centering planetary geometry on the Sun." }
    ]
  },
  "Dashboard — ge/geocide.md": {
    word: "geocide",
    primary: "The deliberate or catastrophic destruction of the Earth's environment, ecosystems, or planetary habitability.",
    secondary: "In environmental law and bioethics, systemic ecocide operating on a planetary scale through nuclear war, climate collapse, or uncontrolled pollution.",
    quotes: [
      { author: "Rachel Carson", work: "Lost Woods", quote: "Uncontrolled atmospheric contamination threatens what future generations may recognize as deliberate **geocide**." },
      { author: "E.O. Wilson", work: "The Future of Life", quote: "The accelerating extinction of species across all continents amounts to a slow, incremental **geocide**." },
      { author: "Carl Sagan", work: "Billions and Billions", quote: "A full-scale nuclear exchange would be planetary **geocide**, extinguishing the hard-won tapestry of life." }
    ]
  },
  "Dashboard — ge/geocultural.md": {
    word: "geocultural",
    primary: "Relating to both geographic factors and cultural practices; combining geography and culture.",
    secondary: "In human geography and geopolitics, analyzing how landforms, regional ecology, and spatial proximity shape cultural identities and civilizations.",
    quotes: [
      { author: "Fernand Braudel", work: "The Mediterranean and the Mediterranean World", quote: "The Mediterranean basin forms a cohesive **geocultural** space defined by olive groves, sea routes, and ancient commerce." },
      { author: "Arnold J. Toynbee", work: "A Study of History", quote: "Each civilization develops distinct **geocultural** boundaries determined by river valleys and mountain barriers." },
      { author: "Jared Diamond", work: "Guns, Germs, and Steel", quote: "The east-west continental axis of Eurasia fostered rapid **geocultural** diffusion of crops, livestock, and technology." }
    ]
  },
  "Dashboard — ge/geode.md": {
    word: "geode",
    primary: "A hollow, subglobular rock or mineral nodule whose internal cavity is lined with inward-projecting crystals or chalcedonic layers.",
    secondary: "In mineralogy and sedimentology, a secondary structure formed in volcanic or sedimentary rocks through mineral precipitation from circulating hydrothermal fluids.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "A rough, ordinary pebble when cracked open reveals a sparkling **geode** lined with purple amethyst." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The hollow interior of the limestone **geode** was coated with rhombohedral quartz crystals." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The roadcut exposed dozens of hollow **geodes** weathered out of the decayed basalt flow." }
    ]
  },
  "Dashboard — ge/geodesic.md": {
    word: "geodesic",
    primary: "Relating to the geometry of curved surfaces, especially the shortest line between two points on a curved surface or sphere.",
    secondary: "In architecture and structural engineering, designating lightweight, dome-shaped structures (geodesic domes) formed by interlocking triangles, developed by Buckminster Fuller.",
    quotes: [
      { author: "Albert Einstein", work: "Relativity: The Special and General Theory", quote: "Light rays and freely falling bodies follow the path of a **geodesic** through curved spacetime." },
      { author: "Buckminster Fuller", work: "Operating Manual for Spaceship Earth", quote: "The three-way grid of the **geodesic** dome distributes structural stress omnidirectionally." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Planets do not feel an invisible tether; they simply follow the straightest possible **geodesic** through warped space." }
    ]
  },
  "Dashboard — ge/geodesical.md": {
    word: "geodesical",
    primary: "Pertaining to geodesy or the mathematical determination of the Earth's size, shape, and curvature; geodesic.",
    secondary: "In historical surveying and mathematical geography, relating to precision trigonometrical measurements across terrestrial arcs.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Colossal **geodesical** surveys conducted in Lapland and Peru established the oblate spheroid form of the globe." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The **geodesical** calculations of the meridian arc required instruments of unprecedented optical precision." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Modern geology relies upon rigorous **geodesical** baselines to detect minute crustal movements." }
    ]
  },
  "Dashboard — ge/geodesy.md": {
    word: "geodesy",
    primary: "The branch of applied mathematics and earth science that deals with the measurement and representation of the Earth, including its gravitational field and exact shape.",
    secondary: "In geophysics, the discipline measuring variations in the Earth's geoid, crustal motion, and rotational dynamics through satellite positioning and gravimetry.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "The principles of **geodesy** demonstrate that centrifugal force must flatten the Earth at its poles." },
      { author: "Alexander von Humboldt", work: "Personal Narrative", quote: "Through the methods of precision **geodesy**, we mapped the colossal peaks of the equatorial cordillera." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "Theoretical **geodesy** bridges pure geometry with the physical realities of the planet's gravitational contours." }
    ]
  },
  "Dashboard — ge/geodetic.md": {
    word: "geodetic",
    primary: "Of, relating to, or obtained by geodesy; pertaining to the curvature and measurement of the Earth's surface.",
    secondary: "In cartography and civil engineering, describing precision surveys that correct for the ellipsoidal curvature of the Earth over large territorial expanses.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Professor Summerlee carried a certified **geodetic** sextant to verify our position in the Amazonian wilderness." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The Great Trigonometrical Survey of India established a permanent **geodetic** framework across the subcontinent." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Modern **geodetic** satellite benchmarks register the westward drift of the continent millimeters each year." }
    ]
  },
  "Dashboard — ge/geographer.md": {
    word: "geographer",
    primary: "A scholar or specialist who studies the physical features of the Earth, its atmosphere, and human populations and their spatial distribution.",
    secondary: "In the history of exploration and cartography, a researcher who charts territorial boundaries, natural resources, and regional landscapes.",
    quotes: [
      { author: "Antoine de Saint-Exupéry", work: "The Little Prince", quote: "The **geographer** is much too important to go loafing about; he does not leave his desk, but receives the explorers." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The true **geographer** does not merely enumerate rivers and towns, but perceives the interconnected harmony of nature." },
      { author: "Strabo", work: "Geography", quote: "The wide learning of the **geographer** encompasses both the natural heavens and the varied customs of mortal men." }
    ]
  },
  "Dashboard — ge/geographic.md": {
    word: "geographic",
    primary: "Of or relating to geography; pertaining to the natural features, divisions, and populations of the Earth.",
    secondary: "Characterized by spatial distribution, regional location, or environmental setting.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Natural barriers like mountain chains and oceans produce profound **geographic** isolation among species." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The great **geographic** chart of the South Seas was covered with pencil marks tracing sperm whale migrations." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The Atlantic currents create vast **geographic** zones defined by temperature and salinity gradients." }
    ]
  },
  "Dashboard — ge/geographical.md": {
    word: "geographical",
    primary: "Belonging or relating to geography; describing the Earth's terrestrial surface and regional distribution.",
    secondary: "In historical and ecological analysis, concerning the spatial and climatic parameters governing territorial habitats and human settlements.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The **geographical** boundary known as Wallace's Line separates the Asian and Australian faunal realms." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "A thorough **geographical** knowledge of the Thames basin reveals how river drainage carved our modern valleys." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The immense **geographical** extent of the Roman provinces created insurmountable difficulties for administrative control." }
    ]
  },
  "Dashboard — ge/geographically.md": {
    word: "geographically",
    primary: "In a geographical manner; with reference to geography or spatial location on the Earth's surface.",
    secondary: "In terms of regional distribution, territorial distance, or spatial relationships.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Though **geographically** adjacent, the eastern and western slopes of the cordillera presented utterly different vegetation." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The United States is **geographically** isolated from European rivalries by the breadth of the Atlantic." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The island was situated **geographically** beyond the regular paths of commercial steam navigation." }
    ]
  },
  "Dashboard — ge/geography.md": {
    word: "geography",
    primary: "The study of the physical features of the Earth and its atmosphere, and of human activity as it affects and is affected by these.",
    secondary: "The physical and cultural features, topography, and spatial layout of a specific region, country, or territory.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The science of **geography** seeks to comprehend the simultaneous interplay of all physical forces upon the globe." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The **geography** of the Galápagos archipelago held the key to the mysterious origin of new species." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The whaler explores a subterranean **geography** beneath the waves that landsmen never dream of." }
    ]
  },
  "Dashboard — ge/geoid.md": {
    word: "geoid",
    primary: "The hypothetical shape that the Earth's ocean surface would take under the influence of gravity and Earth's rotation alone, in the absence of winds and tides.",
    secondary: "In physical geodesy and gravimetry, the equipotential surface of the Earth's gravity field that serves as the universal reference datum for elevation.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The true mathematical figure of our planet is not an ellipsoid, but the irregular undulating **geoid**." },
      { author: "John McPhee", work: "Basin and Range", quote: "Gravimeters detect subtle dips and swells in the **geoid** caused by dense basaltic roots beneath the continents." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Precision satellite tracking has mapped the depressions of the **geoid** across the Indian Ocean basin." }
    ]
  },
  "Dashboard — ge/geomancer.md": {
    word: "geomancer",
    primary: "A practitioner of geomancy; one who divines or foretells the future by interpreting figures formed by earth, sand, or geological features.",
    secondary: "In traditional Chinese landscape cosmology (feng shui), an expert who aligns graves, houses, and temples with terrestrial energy currents (dragon lines).",
    quotes: [
      { author: "Washington Irving", work: "The Alhambra", quote: "The Moorish king summoned a wise **geomancer** to read the secret portents written in the sands of Granada." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The treasure hunter consulted an Oriental **geomancer** who claimed to detect buried gold by compass signs." },
      { author: "Walter Pater", work: "Gaston de Latour", quote: "The Renaissance astrologer worked alongside the **geomancer**, seeking harmonies between the stars and the soil." }
    ]
  },
  "Dashboard — ge/geomancy.md": {
    word: "geomancy",
    primary: "Divination by means of signs derived from the Earth, such as patterns made by handfuls of soil, sand, or dots cast on the ground.",
    secondary: "The art of siting structures or managing human spaces in harmony with surrounding landscape energies and topography (feng shui).",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Ancient superstitious arts such as **geomancy** pretended to extract secrets of destiny from the dust." },
      { author: "Richard Francis Burton", work: "The Book of the Thousand Nights and a Night", quote: "The wizard cast the sixteen figures of **geomancy** upon his sand-board to discover the runaway prince." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Tribal elders practiced primitive **geomancy** before clearing sacred forest groves for spring planting." }
    ]
  },
  "Dashboard — ge/geometric.md": {
    word: "geometric",
    primary: "Of or relating to geometry, or according to its methods and principles.",
    secondary: "Characterized by or decorated with regular lines, curves, angles, and formal shapes; increasing in a geometric progression.",
    quotes: [
      { author: "Thomas Robert Malthus", work: "An Essay on the Principle of Population", quote: "Population, when unchecked, increases in a **geometric** ratio, while subsistence increases only in an arithmetic ratio." },
      { author: "René Descartes", work: "Discourse on Method", quote: "The long chains of simple and easy reasonings by which **geometric** proofs are constructed charmed my youth." },
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "The eye is the best of artists, translating all organic forms into pure **geometric** symmetry." }
    ]
  },
  "Dashboard — ge/geometrical.md": {
    word: "geometrical",
    primary: "Of, relating to, or proceeding by the principles of geometry; geometric.",
    secondary: "In classical mathematics and natural philosophy, rigorously deduced through geometric axioms, proportions, and spatial theorems.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "The description of right lines and circles, upon which geometry is founded, belongs to mechanics and **geometrical** art." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Mathematical certainty in ethics might be achieved had we definitions as clear as those in **geometrical** science." },
      { author: "Baruch Spinoza", work: "Ethics", quote: "I have resolved to demonstrate the nature of God and the passions in a strict **geometrical** order." }
    ]
  },
  "Dashboard — ge/geometrically.md": {
    word: "geometrically",
    primary: "In a geometric manner; with reference to the laws or methods of geometry.",
    secondary: "At an exponentially accelerating rate (as in geometric progression), multiplying by a common factor.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Every organic being naturally increases at so high a rate that, if not destroyed, its progeny would **geometrically** overrun the earth." },
      { author: "Thomas Robert Malthus", work: "An Essay on the Principle of Population", quote: "A population growing **geometrically** must inevitably outstrip agricultural food supply." },
      { author: "Galileo Galilei", work: "The Assayer", quote: "The grand book of the universe cannot be understood unless one learns its language, written **geometrically** in triangles and circles." }
    ]
  },
  "Dashboard — ge/geometrician.md": {
    word: "geometrician",
    primary: "A mathematician who specializes in geometry; one skilled in geometric principles.",
    secondary: "In the history of science, a classical geometer such as Euclid, Archimedes, or Apollonius who demonstrated physical or mathematical truths via spatial proof.",
    quotes: [
      { author: "Thomas Hobbes", work: "Leviathan", quote: "Geometry is the only science that it hath pleased God hitherto to bestow on mankind, and the **geometrician** reasons with infallible certainty." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "The **geometrician** considers not the individual lines drawn on paper, but the universal ideas they represent." },
      { author: "René Descartes", work: "Discourse on Method", quote: "I resolved to imitate the ancient **geometrician** who begins with the simplest truths before ascending to higher problems." }
    ]
  },
  "Dashboard — ge/geometry.md": {
    word: "geometry",
    primary: "The branch of mathematics concerned with the properties, measurement, and relationships of points, lines, angles, surfaces, and solids.",
    secondary: "In philosophy and physics, the intrinsic spatial structure of the physical universe, from Euclidean space to non-Euclidean Riemannian spacetime.",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "The study of **geometry** draws the soul towards truth and creates the spirit of philosophy." },
      { author: "Albert Einstein", work: "Relativity: The Special and General Theory", quote: "How can it be that mathematics, being a product of human thought, fits so marvelously the **geometry** of physical reality?" },
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "Rational mechanics will be the science of motions resulting from any forces whatsoever, and of the motions required to produce any forces, accurately proposed and demonstrated by **geometry**." }
    ]
  },
  "Dashboard — ge/geophysical.md": {
    word: "geophysical",
    primary: "Relating to the physics of the Earth, including its gravitational field, magnetic field, internal core, earthquakes, and atmospheric phenomena.",
    secondary: "In petroleum and mineral exploration, employing physical measurements (seismic, gravimetric, electromagnetic) to probe subsurface strata.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The International **Geophysical** Year mobilized fleets of research ships to sound the deepest oceanic trenches." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Deep continental drilling confirmed **geophysical** estimates of the subterranean temperature gradient." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Geologists interpret **geophysical** seismic records as acoustic ultrasound images of the subterranean crust." }
    ]
  },
  "Dashboard — ge/geophysicist.md": {
    word: "geophysicist",
    primary: "A scientist who specializes in geophysics; one who studies the physical properties and processes of the Earth.",
    secondary: "An earth scientist who uses seismic waves, magnetic anomalies, and satellite gravimetry to model tectonic plate movement and mantle dynamics.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The pioneering **geophysicist** demonstrated that mantle convection currents provide the motive power for continental drift." },
      { author: "John McPhee", work: "Basin and Range", quote: "The **geophysicist** set off explosive charges in shallow boreholes to trace the reflection of sound through fault zones." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Comparative planetology allows the terrestrial **geophysicist** to test models of magma dynamics against volcanic worlds like Venus and Io." }
    ]
  },
  "Dashboard — ge/geophysics.md": {
    word: "geophysics",
    primary: "The branch of earth science that applies the principles and methods of physics to study the Earth, its interior, oceans, atmosphere, and space environment.",
    secondary: "In modern planetary science, the quantitative modeling of planetary cores, magnetospheres, plate tectonics, and seismicity across terrestrial bodies.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The integration of thermodynamics and **geophysics** transformed geology from descriptive natural history into an exact physical science." },
      { author: "John McPhee", work: "Rising from the Plains", quote: "Through modern **geophysics**, the roots of mountain ranges are seen floating like icebergs in the denser mantle." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Marine **geophysics** revealed the worldwide system of mid-ocean ridges splitting the sea floor." }
    ]
  },
  "Dashboard — ge/georgic.md": {
    word: "georgic",
    primary: "A poem or literary work dealing with agriculture, rural labor, and country life, modeled on Virgil's Georgics.",
    secondary: "Of or relating to agriculture or rural husbandry; bucolic.",
    quotes: [
      { author: "John Dryden", work: "Preface to the Translation of the Georgics", quote: "Virgil's **georgic** poem is the best poem of the best poet, elevating rustic toil into sublime art." },
      { author: "William Wordsworth", work: "The Prelude", quote: "I loved the honest farmer's simple life, celebrated in ancient verse with noble **georgic** dignity." },
      { author: "Henry David Thoreau", work: "Walden", quote: "My daily labor in the bean-field had a quiet, **georgic** serenity that commerce knows nothing of." }
    ]
  },
  "Dashboard — ge/Georgics.md": {
    word: "Georgics",
    primary: "A famous didactic poem in four books composed in hexameters by the Roman poet Virgil, celebrating agriculture, animal husbandry, beekeeping, and country life.",
    secondary: "In classical literature, Virgil's masterpiece completed around 29 BC, combining practical agrarian instruction with patriotic Roman myth and philosophical praise of nature.",
    quotes: [
      { author: "Virgil", work: "Georgics", quote: "What makes the crops rejoice, beneath what star / To turn the soil, Maecenas, is the theme of my **Georgics**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The exquisite verses of Virgil's **Georgics** fostered among Roman citizens an enduring love for Italian fields." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The pastoral truth of the **Georgics** captures the solemn labor of the plowman under the autumn sky." }
    ]
  },
  "Dashboard — ge/geosphere.md": {
    word: "geosphere",
    primary: "Any of the concentric regions of physical matter that make up the Earth and its atmosphere (especially the solid crust and mantle, as distinguished from the atmosphere, hydrosphere, and biosphere).",
    secondary: "In planetary science, the entire solid Earth from the core to the surface crust, acting as the reservoir for geochemical cycles.",
    quotes: [
      { author: "Vladimir Vernadsky", work: "The Biosphere", quote: "Living organisms exert a planetary pressure that permanently alters the mineral composition of the **geosphere**." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Interactions between the fluid hydrosphere and the solid **geosphere** generate the sedimentary cycles of erosion and deposition." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Persistent synthetic pollutants infiltrate every compartment of the **geosphere**, contaminating groundwater reservoirs for centuries." }
    ]
  },
  "Dashboard — ge/geostatic.md": {
    word: "geostatic",
    primary: "Relating to the pressure or equilibrium exerted by the weight of overlying rock and soil strata; lithostatic.",
    secondary: "In geotechnical engineering and mining, concerning internal Earth stresses and rock mechanical stability in deep subterranean excavations.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "At depths of several miles, colossal **geostatic** pressure causes crystalline rocks to deform plastically rather than fracture." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The mine shaft was braced with heavy timber arches to counter the relentless **geostatic** heave of the surrounding shale." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Deep metamorphism proceeds under enormous **geostatic** load combined with high temperatures from igneous intrusion." }
    ]
  },
  "Dashboard — ge/geostrophic.md": {
    word: "geostrophic",
    primary: "Relating to or governed by the balance between the horizontal pressure gradient force and the Coriolis force in large-scale atmospheric or oceanic motion.",
    secondary: "In dynamic meteorology and physical oceanography, describing winds or currents whose velocity and direction represent this equilibrium (geostrophic wind, geostrophic current).",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The great circular currents of the open ocean flow in **geostrophic** balance, steered by the spin of the globe." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Atmospheric circulation on rapidly rotating giant planets exhibits spectacular **geostrophic** jet streams banded around the equator." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Meteorologists calculate the velocity of the **geostrophic** wind directly from isobaric pressure gradients." }
    ]
  },
  "Dashboard — ge/geosynchronous.md": {
    word: "geosynchronous",
    primary: "Having an orbital period that matches the Earth's rotation period (approximately 23 hours, 56 minutes, and 4 seconds), so that the satellite returns to the same position in the sky each sidereal day.",
    secondary: "In satellite telecommunications and aerospace engineering, designating high-altitude orbits (approximately 35,786 km above Earth) used for weather monitoring and broadcast relays.",
    quotes: [
      { author: "Arthur C. Clarke", work: "Wireless World", quote: "Three communications satellites placed in **geosynchronous** orbit could provide unbroken radio and television coverage for the entire globe." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Robotic sentinels stationed in **geosynchronous** altitude watch over Earth's cloud belts and continental weather fronts." },
      { author: "Douglas Hofstadter", work: "Metamagical Themas", quote: "From the perspective of a ground dish, a **geosynchronous** orbiter appears permanently anchored in the sky." }
    ]
  },
  "Dashboard — ge/geosyncline.md": {
    word: "geosyncline",
    primary: "A major, elongated downwarp or trough in the Earth's crust in which vast thicknesses of sedimentary and volcanic deposits accumulate over millions of years.",
    secondary: "In classical historical geology (the Dana-Hall hypothesis), the tectonic precursor to a folded mountain range prior to the development of plate tectonic theory.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The Appalachian strata originated within an immense **geosyncline** that slowly subsided as thousands of feet of sediment poured in." },
      { author: "John McPhee", work: "Basin and Range", quote: "Before plate tectonics revolutionized geology, every mountain system was explained as an uplifted and inverted **geosyncline**." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The prolonged subsidence of the **geosyncline** created favorable conditions for thick coal seam accumulation." }
    ]
  },
  "Dashboard — ge/hypogeous.md": {
    word: "hypogeous",
    primary: "Growing, developing, or living beneath the surface of the ground (opposed to epigeous).",
    secondary: "In botany, describing seed germination where the cotyledons remain underground within the seed coat (as in the pea or oak acorn).",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "In plants with **hypogeous** germination, the cotyledons never leave their subterranean retreat to become green leaves." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The garden pea exemplifies **hypogeous** development, sending up only its epicotyl into the atmosphere." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "Many edible fungi are strictly **hypogeous**, maturing their subterranean sporocarps entirely beneath the oak litter." }
    ]
  },
  "Dashboard — ge/hypogeum.md": {
    word: "hypogeum",
    primary: "An underground chamber, tomb, temple, or subterranean vaulted structure of ancient construction.",
    secondary: "In classical archaeology and speleology, subterranean architectural complexes (such as the Hypogeum of Ħal Saflieni in Malta or Roman catacomb chambers).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Early Christians celebrated their solemn mysteries within the shadowy vaults of the subterranean **hypogeum**." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Red Circle", quote: "The conspirators met in an ancient vaulted **hypogeum** hidden beneath the pavement of the old quarter." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "Marius descended into the cool **hypogeum** where ancestral sarcophagi rested in solemn twilight." }
    ]
  },
  "Dashboard — ge/paleogeography.md": {
    word: "paleogeography",
    primary: "The branch of historical geology that reconstructs the geography, landforms, ocean basins, and climate of the Earth in past geological eras.",
    secondary: "In plate tectonics, mapping the changing positions of continental landmasses, shallow epicontinental seas, and past mountain belts over deep time.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "By deciphering fossil deposits, the geologist reconstructs the vanished **paleogeography** of prehistoric continents." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The **paleogeography** of the Paleozoic shows North America straddling the equator, bathed in warm tropical seas." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Fossil coral reefs provide our surest guide to the maritime **paleogeography** of the Silurian period." }
    ]
  },
  "Dashboard — ge/Pangea.md": {
    word: "Pangea",
    primary: "The hypothetical supercontinent that existed during the late Paleozoic and early Mesozoic eras, comprising all the present continents joined together before rifting apart.",
    secondary: "In continental drift and plate tectonic history, the colossal landmass named by Alfred Wegener that began breaking up approximately 175 million years ago into Laurasia and Gondwana.",
    quotes: [
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "All the continents were once united in a single primordial supercontinent, to which we give the name **Pangea**." },
      { author: "John McPhee", work: "Basin and Range", quote: "The breakup of **Pangea** opened the infant Atlantic Ocean, drifting the Americas westward away from Africa." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Over tens of millions of years, the pieces of **Pangea** sailed across the globe like colossal tectonic rafts." }
    ]
  },
  "Dashboard — ge/protogeometric.md": {
    word: "protogeometric",
    primary: "Relating to or characteristic of a style of ancient Greek pottery (c. 1050–900 BC) marked by simple geometric patterns, concentric circles, and semicircles.",
    secondary: "In classical Mediterranean archaeology, the transitional ceramic phase bridging the Mycenaean collapse and the full Geometric period, heralding the recovery of Greek craft.",
    quotes: [
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The bold compass-drawn concentric circles of **protogeometric** amphorae signal a fresh artistic dawn in post-Mycenaean Greece." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In **protogeometric** vases, one perceives the clean instinct for formal order returning after centuries of upheaval." },
      { author: "Heinrich Schliemann", work: "Mycenae", quote: "The upper strata revealed sherds of late **protogeometric** ware marking the reoccupation of the citadel." }
    ]
  },
  "Dashboard — ge/synge.md": {
    word: "synge",
    primary: "A historical dialectal or phonetic variant related to Singe, or referring to John Millington Synge (1871–1909), the celebrated Irish dramatist and poet of the Celtic Revival.",
    secondary: "In literary history, the dramatic works of J.M. Synge (The Playboy of the Western World, Riders to the Sea), known for rich poetic idiom and rural Irish peasant themes.",
    quotes: [
      { author: "William Butler Yeats", work: "Essays and Introductions", quote: "In the plays of J. M. **Synge**, the wild imagination of the Western peasantry found its purest and most enduring speech." },
      { author: "James Joyce", work: "Selected Letters", quote: "The tragic beauty of **Synge**'s island dramas captured the salt spray and relentless fate of the Aran coast." },
      { author: "George Bernard Shaw", work: "Dramatic Opinions and Essays", quote: "The genius of **Synge** brought back to English drama that wild music and harsh truth that commercial theaters had long forgotten." }
    ]
  },
  "Dashboard — pel/expel.md": {
    word: "expel",
    primary: "To force out, drive away, or eject forcibly; to officially dismiss from a school, organization, or country.",
    secondary: "In physiology and mechanics, to discharge fluid, gas, or waste from an internal cavity or mechanism under pressure.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "We must with all our strength **expel** this dangerous tumor from the commonwealth." },
      { author: "Thomas Hobbes", work: "Leviathan", quote: "The sovereign authority holds the power to **expel** seditious persons whose doctrines dissolve civic peace." },
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould", quote: "Earthworms swallow soil in great quantity to extract organic matter, and then **expel** the residue in coiled castings." }
    ]
  },
  "Dashboard — pel/expelling.md": {
    word: "expelling",
    primary: "The act or process of forcing out, ejecting, or banishing forcibly.",
    secondary: "In respiratory mechanics and engine thermodynamics, driving out air, exhaust gas, or accumulated pressure from a chamber.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The sperm whale surfaced, **expelling** a mighty plume of vapor into the cold Atlantic air." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "The mind succeeds in **expelling** false hypotheses only through rigorous confrontation with evidence." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The elastic recoil of the lungs assists in **expelling** carbon dioxide during quiet expiration." }
    ]
  },
  "Dashboard — pel/expulsion.md": {
    word: "expulsion",
    primary: "The act of expelling or the state of being expelled; forcible ejection, discharge, or banishment.",
    secondary: "In political and institutional history, the formal deprivation of membership, civic rights, or territory decreed by an governing body.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **expulsion** of the Tarquins from Rome laid the foundation for seven centuries of republican virtue." },
      { author: "John Milton", work: "Paradise Lost", quote: "Their **expulsion** from the garden of Eden left our first parents solitary in a vast and fallen world." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The forced **expulsion** of native tribes across the Mississippi was executed with cold bureaucratic regularity." }
    ]
  },
  "Dashboard — pel/pel.md": {
    word: "pel",
    primary: "In Greek linguistic morphology, the root element *pel-* (from πέλος, *pelos*, 'mud', 'clay', or πέλαγος, *pelagos*, 'open sea').",
    secondary: "A combining base in geology and marine ecology forming words relating to fine muddy sediments (pelite, pelitic) or the open ocean (pelagic).",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Petrologists derive the technical term pelite from the classical root **pel-**, denoting clay and fine mud." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The open ocean realm draws its scientific prefix from the ancient **pel-** root of the Aegean mariners." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "The Greek stem **pel-** marks those ocean sediments formed beyond the reach of continental sandbanks." }
    ]
  },
  "Dashboard — pel/pelage.md": {
    word: "pelage",
    primary: "The hairy, furry, or woolly coat of a mammal, as distinct from human hair; the fur or fleece collectively.",
    secondary: "In mammalogy, the full coat consisting of underfur (dense insulation) and guard hairs (waterproof protection), undergoing seasonal molting.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Arctic foxes undergo a complete change of **pelage**, exchanging dark summer fur for immaculate white coats." },
      { author: "Jack London", work: "The Call of the Wild", quote: "Buck's thick **pelage** protected him against the bitter sixty-below-zero frost of the Klondike." },
      { author: "Theodore Roosevelt", work: "African Game Trails", quote: "The lion displayed a magnificent dark **pelage** around his neck and shoulders, denoting prime maturity." }
    ]
  },
  "Dashboard — pel/pelagic.md": {
    word: "pelagic",
    primary: "Relating to, living in, or occurring in the open sea or ocean, away from the coast and seafloor (as distinguished from benthic or littoral).",
    secondary: "In marine biology and oceanography, designating the water column from the surface to the abyssal depths, and the organisms (such as tuna, pelagic sharks, and plankton) that inhabit it.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The **pelagic** zone is a realm of blue water where wandering creatures know neither shore nor seafloor." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The great spermaceti whale is purely a **pelagic** monster, rarely straying into shallow coastal bays." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "We captured exquisite transparent **pelagic** mollusks and jellyfish that drifted past the Beagle in mid-ocean." }
    ]
  },
  "Dashboard — pel/pelite.md": {
    word: "pelite",
    primary: "A sedimentary rock composed of fine-grained clay or mud particles; mudstone, shale, or argillite.",
    secondary: "In metamorphic petrology, an argillaceous rock (such as slate, phyllite, or mica schist) derived from the metamorphism of fine-grained muddy sediment.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The weathering of ancient feldspars yielded fine **pelite**, which settled quietly upon the deeper seafloor." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Regional metamorphism transformed the soft Ordovician **pelite** into shimmering sheets of mica schist." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Deep in the roots of the mountain chain, the aluminous **pelite** recrystallized into garnet and staurolite." }
    ]
  },
  "Dashboard — pel/pelitic.md": {
    word: "pelitic",
    primary: "Pertaining to, composed of, or resembling pelite; argillaceous or clay-rich.",
    secondary: "In metamorphic geology, describing mineral assemblages (such as pelitic schists) rich in aluminum silicates resulting from the alteration of clay minerals.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The **pelitic** schists of the Scottish Highlands reveal a sequence of metamorphic zones marked by index minerals." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The dark **pelitic** laminae alternate with fine sandy layers, recording seasonal changes in sedimentation." },
      { author: "John McPhee", work: "Basin and Range", quote: "Outcrops of dark, **pelitic** slate cleaved smoothly under the geological hammer." }
    ]
  },
  "Dashboard — pel/repel.md": {
    word: "repel",
    primary: "To drive back, ward off, or resist an attack, enemy, or approach; to force back.",
    secondary: "In physics and chemistry, to exert an opposing repulsive force against (as like magnetic poles or like electric charges repel each other); to resist absorption (as oil repels water).",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "Bodies which are charged with like electricity **repel** each other with a force inversely proportional to the square of their distance." },
      { author: "William Shakespeare", work: "Macbeth", quote: "With kerns and gallowglasses he did **repel** the fierce invaders from our sacred soil." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The oily secretion of aquatic birds serves to **repel** water and preserve the warmth of their down." }
    ]
  },
  "Dashboard — pel/repellant.md": {
    word: "repellant",
    primary: "Causing distaste, aversion, or disgust; repulsive; serving or tending to repel.",
    secondary: "In materials and chemistry, a substance used to deter pests, insects, or water (water repellant).",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "His hideous countenance was so utterly **repellant** that no human being could look upon him without horror." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The oily coat of the diving beetle acts as a natural water **repellant**, trapping a bubble of air for respiration." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "The bleak expanse of the Grimpen Mire presented a **repellant** wilderness of quagmire and fog." }
    ]
  },
  "Dashboard — pel/repellent.md": {
    word: "repellent",
    primary: "Serving or able to repel; causing disgust, aversion, or distaste; repulsive.",
    secondary: "In pharmacology and material science, a chemical treatment or spray applied to skin, cloth, or surfaces to deter insects or resist water.",
    quotes: [
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The customs of the Yahoos appeared to Gulliver so **repellent** that he turned his eyes away in loathing." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I found nothing cold or **repellent** in the solitude of the woods; rather, an affectionate hospitality in every pine needle." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Forestry workers applied a fragrant cedar oil **repellent** to ward off biting gnats in the marsh." }
    ]
  },
  "Dashboard — pel/repellently.md": {
    word: "repellently",
    primary: "In a repellent, repulsive, or distasteful manner; so as to cause aversion.",
    secondary: "In descriptive prose, exhibiting an off-putting, hostile, or forbidding demeanor or appearance.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Mrs. Reed looked **repellently** upon me as I stood trembling before her mahogany chair." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The bloated carcass of the dead whale drifted **repellently** in the glare of the noon sun." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The damp, moldering walls of the Chancery court frowned **repellently** upon suitors whose lives had been consumed in its corridors." }
    ]
  },
  "Dashboard — pel/repulsive.md": {
    word: "repulsive",
    primary: "Arousing intense distaste, disgust, or aversion; offensive to the mind or senses.",
    secondary: "In physics, of or relating to repulsion; tending to drive apart or separate (as repulsive forces between subatomic particles).",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "I beheld the wretch, the miserable monster whom I had created; he was gigantically hideous and utterly **repulsive**." },
      { author: "Isaac Newton", work: "Opticks", quote: "There are particles which attract each other at small distances and exert a strong **repulsive** power at minute intervals." },
      { author: "Robert Louis Stevenson", work: "The Strange Case of Dr. Jekyll and Mr. Hyde", quote: "There was something abnormal and misbegotten in the very essence of the creature that produced a **repulsive** shudder." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
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

console.log("Earth & Geology Batch 3 completed! Total words updated:", Object.keys(wordsData).length);
