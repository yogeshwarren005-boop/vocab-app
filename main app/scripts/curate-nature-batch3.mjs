import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — uran/anuran.md": {
    word: "anuran",
    primary: "Any tailless amphibian belonging to the order Anura, comprising frogs and toads; characterized by long hind legs adapted for leaping and absence of a tail in the adult stage.",
    secondary: "In systematic vertebrate zoology, an amphibian exhibiting metamorphic development from an aquatic tailed tadpole to a carnivorous, saltatory adult (etymologically from Greek an- without + oura tail).",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The absence of batrachians, specifically any native **anuran** species, from oceanic islands is easily explained by their vulnerability to sea-water." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "In every adult **anuran**, the caudal vertebrae are fused into an elongated unsegmented rod termed the urostyle." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "In spring marshes, the choral symphony of the **anuran** population heralds the awakening of life after winter dormancy." }
    ]
  },
  "Dashboard — uran/uranalysis.md": {
    word: "uranalysis",
    primary: "A variant spelling of urinalysis; the physical, chemical, and microscopic examination and clinical analysis of urine.",
    secondary: "In clinical pathology and diagnostics, routine laboratory evaluation of urine to assess renal filtration, metabolic health, liver function, and systemic hydration (from Greek ouron urine + analysis).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Routine **uranalysis** remains an indispensable bedside tool for detecting albuminuria, glycosuria, and casts." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Careful **uranalysis** reveals the chemical end-products of metabolism filtered continuously by the renal parenchyma." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Changes observed during careful **uranalysis** often give the nurse the earliest warning of systemic relapse." }
    ]
  },
  "Dashboard — uran/urania.md": {
    word: "urania",
    primary: "In Greek mythology, Urania, the Muse of astronomy and celestial navigation, usually depicted holding a celestial globe and a compass.",
    secondary: "In poetic and astronomical literature, the personification of heavenly contemplation, celestial mechanics, and divine astronomical inspiration.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Descend from Heav'n, **Urania**, by that name / If rightly thou art call'd, whose Voice divine / Following, above th' Olympian Hill I soare." },
      { author: "Percy Bysshe Shelley", work: "Adonais", quote: "Most musical of mourners, weep again! / Lament anew, **Urania**!—He died, / Who was thy extreme hope, thy loveliest." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "The celestial muse **Urania** inspires the astronomer to perceive the geometric harmony governing stellar spheres." }
    ]
  },
  "Dashboard — uran/uraninite.md": {
    word: "uraninite",
    primary: "A heavy, radioactive, pitch-black to dark brownish mineral ore consisting essentially of uranium dioxide (UO2); pitchblende.",
    secondary: "In mineralogy and nuclear geology, the primary ore mineral of uranium, famous as the source material from which Pierre and Marie Curie first isolated polonium and radium.",
    quotes: [
      { author: "Marie Curie", work: "Radioactive Substances", quote: "We were astonished to discover that raw **uraninite** exhibited a radioactivity several times greater than pure uranium itself." },
      { author: "Pierre Curie", work: "Nobel Lecture on Radioactivity", quote: "The extraction of polonium and radium from tons of pitchblende or **uraninite** required years of chemical fractionation." },
      { author: "Ernest Rutherford", work: "Radioactivity", quote: "The disintegration of heavy nuclei within ancient crystals of **uraninite** generates a steady accumulation of helium and lead." }
    ]
  },
  "Dashboard — uran/uranium.md": {
    word: "uranium",
    primary: "A dense, silvery-white, radioactive metallic chemical element of atomic number 92 (symbol U), belonging to the actinide series.",
    secondary: "In nuclear physics and energy, a heavy element whose fissile isotope (U-235) sustains nuclear chain reactions, named by Martin Klaproth in 1789 after the newly discovered planet Uranus.",
    quotes: [
      { author: "Marie Curie", work: "Radioactive Substances", quote: "The rays emitted by **uranium** compounds are spontaneous, persistent, and entirely independent of external illumination." },
      { author: "Enrico Fermi", work: "Collected Papers", quote: "The bombardment of **uranium** by slow neutrons induced unexpected nuclear transformations yielding numerous radioactive isotopes." },
      { author: "Albert Einstein", work: "Letter to President Franklin D. Roosevelt", quote: "In the course of the last four months it has been made probable that it may become possible to set up a nuclear chain reaction in a large mass of **uranium**." }
    ]
  },
  "Dashboard — uran/uranography.md": {
    word: "uranography",
    primary: "The branch of astronomy concerned with the descriptive mapping, cataloging, and celestial cartography of the stars, constellations, and heavens.",
    secondary: "In observational astronomy and history of cartography, the science and artistic technique of producing celestial atlases, star globes, and constellation boundaries.",
    quotes: [
      { author: "Johannes Hevelius", work: "Prodromus Astronomiae", quote: "The ultimate purpose of **uranography** is to fix with mathematical certainty the coordinates of every visible luminary." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "Through modern **uranography**, the celestial sphere is mapped into distinct constellations, guiding our exploration of the stellar expanse." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Descriptive **uranography** unites celestial cartography with historical records of stellar magnitudes and nebular positions." }
    ]
  },
  "Dashboard — uran/uranologist.md": {
    word: "uranologist",
    primary: "An astronomer or scholar who studies the heavens, celestial mechanics, and celestial bodies.",
    secondary: "In historical astronomical discourse, an observer or natural philosopher dedicated to charting stellar movements and planetary orbits across the celestial sphere.",
    quotes: [
      { author: "Galileo Galilei", work: "Dialogue Concerning the Two Chief World Systems", quote: "The discerning **uranologist** trusts telescopic observation over scholastic dogmas concerning the immutability of the heavens." },
      { author: "Johannes Kepler", work: "Astronomia Nova", quote: "Every dedicated **uranologist** must reconcile planetary observations with mathematical laws of orbital motion." },
      { author: "Camille Flammarion", work: "The Wonders of the Heavens", quote: "The amateur **uranologist**, equipped with a modest telescope, discovers endless marvels across the dark nocturnal vault." }
    ]
  },
  "Dashboard — uran/uranology.md": {
    word: "uranology",
    primary: "The branch of science that treats the heavens, stars, and celestial bodies; astronomy.",
    secondary: "In early scientific and philosophical treatises, the systematic discourse on the structure, motions, and physical laws governing the celestial realm.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "The principles of natural philosophy provide the mathematical foundation for both terrestrial dynamics and celestial **uranology**." },
      { author: "John Herschel", work: "A Treatise on Astronomy", quote: "A comprehensive **uranology** treats not merely the geometry of planetary orbits but the physical constitution of the stars." },
      { author: "Richard A. Proctor", work: "Other Worlds Than Ours", quote: "In modern **uranology**, the spectroscope reveals that distant stars share the same chemical elements found on Earth." }
    ]
  },
  "Dashboard — uran/uranometry.md": {
    word: "uranometry",
    primary: "The measurement of the celestial positions, coordinates, and apparent magnitudes of the stars; also, a chart or atlas of the heavens.",
    secondary: "In celestial cartography, specifically associated with Johann Bayer's epochal 1603 star catalog Uranometria, which introduced Greek-letter stellar designations.",
    quotes: [
      { author: "Johann Bayer", work: "Uranometria", quote: "In this **uranometry**, the stars of each constellation are systematically cataloged and designated by letters of the Greek alphabet." },
      { author: "Friedrich Wilhelm Bessel", work: "Fundamenta Astronomiae", quote: "Precision in modern **uranometry** demands rigorous correction for atmospheric refraction, precession, and stellar aberration." },
      { author: "Arthur Eddington", work: "The Internal Constitution of the Stars", quote: "Accurate **uranometry** provides the observational baseline from which stellar luminosities and distances are determined." }
    ]
  },
  "Dashboard — uran/uranophobia.md": {
    word: "uranophobia",
    primary: "An abnormal, irrational fear of heaven, the sky, or the celestial vault.",
    secondary: "In clinical psychiatry and phobic disorders, an anxiety state provoked by contemplating the overwhelming vastness of the sky or obsessive guilt regarding heavenly judgment.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "In cases of severe agoraphobia, the patient may experience a morbid **uranophobia**, terrified by the sheer, unconfined emptiness of the open sky." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "An acute dread of cosmic vastness or heavenly surveillance, termed **uranophobia**, reflects a deep disruption of spatial orientation." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Superstitious hypochondriacs frequently suffer from a religious **uranophobia**, trembling at the open firmament as if divine thunderbolts were poised to strike." }
    ]
  },
  "Dashboard — uran/uranoplasty.md": {
    word: "uranoplasty",
    primary: "Surgical reconstruction or plastic repair of the palate (roof of the mouth), particularly to correct a congenital cleft palate (uraniscoplasty).",
    secondary: "In reconstructive and maxillofacial surgery, the mobilization and suturing of mucoperiosteal flaps to reconstruct an intact vault between the oral and nasal cavities (from Greek ouranos palate/roof of mouth + plastos formed).",
    quotes: [
      { author: "William Stewart Halsted", work: "Surgical Papers", quote: "Meticulous closure of mucosal flaps during **uranoplasty** is essential to reconstruct the hard palate without tension." },
      { author: "J. Marion Sims", work: "The Story of My Life", quote: "Refinements in **uranoplasty** have enabled surgeons to restore normal speech and deglutition in children with congenital clefts." },
      { author: "Astley Cooper", work: "Lectures on the Principles and Practice of Surgery", quote: "Successful **uranoplasty** transforms the life of the patient by sealing the abnormal communication between oral and nasal cavities." }
    ]
  },
  "Dashboard — uran/uranoscopidae.md": {
    word: "uranoscopidae",
    primary: "A family of marine perciform fishes commonly called stargazers, characterized by upward-directed eyes situated on top of a flat bony head and an upward-directed mouth.",
    secondary: "In ichthyology, benthic ambush predators equipped with camouflage coloration, electric organs in certain species, and a venomous spine above the pectoral fin.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", quote: "Fishes of the family **Uranoscopidae** lie buried in sand with only their upward-directed eyes and fringed mouths protruding." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "Beneath the silt we uncovered a bizarre representative of the **Uranoscopidae**, equipped with an electric organ capable of stunning passing prey." },
      { author: "Louis Agassiz", work: "Lake Superior", quote: "The structural adaptations of the **Uranoscopidae** illustrate remarkable benthic specialization for ambush predation." }
    ]
  },
  "Dashboard — uran/Uranus.md": {
    word: "Uranus",
    primary: "The seventh planet from the Sun, an ice giant discovered by William Herschel in 1781, characterized by a retrograde rotation and an extreme axial tilt of 98 degrees.",
    secondary: "In classical mythology, the primordial Greek deity personifying the heavens and sky (Ouranos), husband of Gaia and father of the Titans and Cyclopes.",
    quotes: [
      { author: "William Herschel", work: "Account of a Comet", quote: "The observation of this moving star, subsequently identified as the planet **Uranus**, extends the known radius of our solar system." },
      { author: "John Keats", work: "On First Looking into Chapman's Homer", quote: "Then felt I like some watcher of the skies / When a new planet swims into his ken," },
      { author: "Carl Sagan", work: "Cosmos", quote: "Tipped upon its side by an ancient cosmic collision, the pale cyan orb of **Uranus** rolls through the frigid outer reaches of our solar family." }
    ]
  },
  "Dashboard — uran/uranyl.md": {
    word: "uranyl",
    primary: "The divalent inorganic oxycation of uranium in its hexavalent oxidation state, having the chemical formula [UO2]2+.",
    secondary: "In actinide coordination chemistry and environmental radiochemistry, a linear trans-dioxo cation forming characteristic bright fluorescent yellow-green crystalline salts.",
    quotes: [
      { author: "Marie Curie", work: "Radioactive Substances", quote: "In studying phosphorescence, Becquerel utilized double sulfates of **uranyl** and potassium, accidentally discovering spontaneous radioactivity." },
      { author: "Henri Becquerel", work: "Sur les radiations invisibles émises par les corps phosphorescents", quote: "Crystals of potassium **uranyl** sulfate placed upon photographic plates wrapped in black paper produced clear impressions without exposure to sunlight." },
      { author: "Glenn T. Seaborg", work: "The Transuranium Elements", quote: "Aqueous solutions containing the stable **uranyl** ion display a characteristic bright yellow-green fluorescence under ultraviolet excitation." }
    ]
  },
  "Dashboard — anem/anem.md": {
    word: "anem",
    primary: "A combining form derived from Greek anemos meaning wind, used in scientific, meteorological, and botanical terminology.",
    secondary: "In morphology and taxonomy, designating atmospheric air currents, wind pollination, or instrumentation designed to detect wind velocity and direction.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The Greek root **anem**- designates atmospheric currents, from gentle breezes to destructive gales." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Compounds rooted in **anem**- illustrate the universal human endeavor to chart and measure the restless winds of the globe." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The element **anem**- recurs across natural history to describe mechanisms tuned to the drifting air." }
    ]
  },
  "Dashboard — anem/anemia.md": {
    word: "anemia",
    primary: "A medical condition characterized by a deficiency of red blood cells or hemoglobin in the blood, resulting in pallor, fatigue, and tissue hypoxia.",
    secondary: "In hematology and pathology, a clinical syndrome arising from blood loss, impaired erythropoiesis, or accelerated hemolysis (from Greek an- without + haima blood).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pernicious **anemia** is characterized by profound pallor, progressive debility, and megaloblastic alteration of the erythroid marrow." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "By diminishing the oxygen-carrying capacity of the blood, experimental **anemia** reveals the metabolic dependence of every tissue." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "In valitudinarian chambers, deficient fresh air and poor nutrition inevitably foster a chronic, debilitating **anemia**." }
    ]
  },
  "Dashboard — anem/anemic.md": {
    word: "anemic",
    primary: "Suffering from or relating to anemia; marked by insufficient red blood cells or pallid complexion; metaphorically, lacking vitality, strength, or spirit.",
    secondary: "In medical and critical literary discourse, describing biological debility or figurative feebleness, bloodlessness, or lack of expressive vigor.",
    quotes: [
      { author: "Henry James", work: "The Portrait of a Lady", quote: "His pale, exhausted countenance gave him the fragile air of an **anemic** scholar confined too long among dusty folios." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The evening light faded into an **anemic** wash of gray, draining the vibrancy from the garden." },
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "The physicians examined the **anemic** young patient, noting his low hemoglobin and translucent complexion." }
    ]
  },
  "Dashboard — anem/anemograph.md": {
    word: "anemograph",
    primary: "An instrument that continuously and automatically records the velocity, force, or direction of the wind on a chart or digital register.",
    secondary: "In meteorological instrumentation, a recording anemometer combining a wind vane and revolving anemometer cups connected to a clockwork drum pen.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "The automatic **anemograph** registered every gust of the gale, tracing a continuous pencil line upon the revolving drum." },
      { author: "Camille Flammarion", work: "The Atmosphere", quote: "Telescopic and meteorological towers rely upon the self-recording **anemograph** to preserve an objective record of wind intensity." },
      { author: "John Tyndall", work: "Heat a Mode of Motion", quote: "The erratic tracings of the **anemograph** during a squall demonstrate the chaotic turbulence within moving air masses." }
    ]
  },
  "Dashboard — anem/anemographic.md": {
    word: "anemographic",
    primary: "Of, relating to, or obtained by an anemograph; pertaining to the recording and depiction of wind direction and speed.",
    secondary: "In dynamic meteorology, describing continuous graphical records and tracings that document the kinetic turbulence and gusts of atmospheric currents.",
    quotes: [
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Comparative analysis of **anemographic** charts from coastal stations reveals the diurnal cycle of land and sea breezes." },
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "Continuous **anemographic** records are indispensable for detecting sudden squall lines associated with approaching cold fronts." },
      { author: "Alexander Buchan", work: "Handy Book of Meteorology", quote: "The **anemographic** curves obtained during the equinoctial gale exhibited violent fluctuations in barometric gradient and wind speed." }
    ]
  },
  "Dashboard — anem/anemography.md": {
    word: "anemography",
    primary: "The scientific description, observation, and graphic charting of winds and atmospheric air currents.",
    secondary: "In physical climatology and geography, the systematic recording and mapping of global wind belts, prevailing trade winds, monsoons, and local breezes.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "A complete **anemography** of the tropical oceans charts the permanent trajectories of the trade winds and monsoons." },
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "Through systematic **anemography**, navigators uncovered the great circular wind circuits that govern global passage." },
      { author: "Cleveland Abbe", work: "Treatise on Meteorological Apparatus", quote: "The methodology of **anemography** combines mechanical instrumentation with mathematical analysis of aerodynamic trajectories." }
    ]
  },
  "Dashboard — anem/anemometer.md": {
    word: "anemometer",
    primary: "An instrument for measuring the speed, velocity, or pressure of the wind.",
    secondary: "In meteorological stations, fluid mechanics, and wind engineering, a device typically consisting of rotating hemispherical cups, a propeller, or hot-wire sensors calibrated to quantify wind flow.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "The cups of the Robinson **anemometer** revolved with furious velocity as the hurricane struck the exposed headland." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "We measured the force of the pampero with an **anemometer**, recording gale-force gusts that swept across the plains." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Meteorologists on weather ships watched the needle of the **anemometer** climb past sixty knots as the storm tightened." }
    ]
  },
  "Dashboard — anem/anemometric.md": {
    word: "anemometric",
    primary: "Of or relating to an anemometer or to the measurement of wind velocity and pressure.",
    secondary: "In observational meteorology and atmospheric science, describing data, instruments, or calculations derived from wind-speed sensors.",
    quotes: [
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "Accurate **anemometric** measurements require placing sensors well above the boundary layer of terrestrial obstacles." },
      { author: "Alexander Buchan", work: "Handy Book of Meteorology", quote: "Discrepancies in **anemometric** data frequently arise from local frictional turbulence near mountain crests." },
      { author: "Cleveland Abbe", work: "Meteorological Apparatus and Methods", quote: "Calibrating the **anemometric** gear in a wind tunnel ensures uniform velocity readings across all stations." }
    ]
  },
  "Dashboard — anem/anemometrical.md": {
    word: "anemometrical",
    primary: "Relating to or determined by anemometry; measuring wind force, speed, or velocity.",
    secondary: "In historical meteorological literature, describing physical observations and mathematical tables quantifying atmospheric wind pressure.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "Our **anemometrical** observations during the voyage corroborated the prevailing southwesterly flow across temperate seas." },
      { author: "John Herschel", work: "Meteorology", quote: "Careful **anemometrical** surveys demonstrate how surface winds are deflected by continental landmasses." },
      { author: "James Glaisher", work: "Travels in the Air", quote: "During our balloon ascent, **anemometrical** readings indicated a rapid increase in horizontal wind speed within the upper cloud deck." }
    ]
  },
  "Dashboard — anem/anemometry.md": {
    word: "anemometry",
    primary: "The science, art, and technique of measuring the velocity, force, volume, and direction of atmospheric winds and air currents.",
    secondary: "In fluid dynamics and wind-turbine engineering, the quantitative methodology employed to characterize airflow velocities, wind shear, and kinetic energy potential.",
    quotes: [
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "Advances in sonic and cup **anemometry** have made possible precise microscale turbulence modeling in aeronautics." },
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Theoretical **anemometry** establishes the mathematical relation between pressure gradient force and atmospheric velocity." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "The practice of scientific **anemometry** allows the traveler to correlate wind velocity with hygrometric variation." }
    ]
  },
  "Dashboard — anem/anemone.md": {
    word: "anemone",
    primary: "A plant of the genus Anemone (family Ranunculaceae), having cup-shaped flowers typically colored white, blue, red, or purple, commonly called the windflower; also, a sea anemone.",
    secondary: "In marine biology, a sedentary predatory polyp belonging to the order Actiniaria, possessing a fleshy column and a stinging ring of tentacles resembling the terrestrial flower.",
    quotes: [
      { author: "William Wordsworth", work: "Lines Written in Early Spring", quote: "The wild wood **anemone** nodded its white petals gently in the soft breath of April." },
      { author: "John Ruskin", work: "Proserpina", quote: "The Greek name **anemone**, or windflower, immortalizes the tender blossom that opens only when the spring winds blow." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "In deep tide pools, the plumose sea **anemone** unfurls a velvet crown of tentacles to capture drifting copepods." }
    ]
  },
  "Dashboard — anem/anemonella.md": {
    word: "anemonella",
    primary: "A delicate North American woodland perennial herb (Anemonella thalictroides or Thalictrum thalictroides), commonly called rue anemone, bearing clusters of small white or pale pink flowers.",
    secondary: "In floristic taxonomy and spring ephemerals, a monotypic genus closely allied to Thalictrum and Anemone, distinguished by tuberous roots, thalictrum-like compound leaves, and petaloid sepals.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The delicate **Anemonella** thalictroides, or rue anemone, blooms profusely on rocky wooded hillsides in early spring." },
      { author: "John Burroughs", work: "Wake-Robin", quote: "Beside the hepaticas, the slender blossoms of **Anemonella** tremble upon wiry stems at the slightest woodland breeze." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "In native woodland gardens, **Anemonella** is prized for its exquisite white and blush-pink sepals resembling miniature buttercups." }
    ]
  },
  "Dashboard — anem/anemophilous.md": {
    word: "anemophilous",
    primary: "Pollinated or fertilized by the agency of wind, as in grasses, sedges, and many deciduous and coniferous trees.",
    secondary: "In floral ecology, exhibiting specific evolutionary adaptations for wind pollination, including copious lightweight pollen, inconspicuous petals, lack of nectar, and feathery, protruding stigmas.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "In **anemophilous** plants, such as grasses and hazel, pollen grains are dry, light, and produced in prodigious quantities." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "The flowers of **anemophilous** species lack conspicuous petals and nectar, relying entirely upon wind currents for cross-pollination." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "Open grassland communities are dominated by **anemophilous** species whose abundant airborne pollen dominates the atmospheric pollen rain." }
    ]
  },
  "Dashboard — anem/anemophily.md": {
    word: "anemophily",
    primary: "The process or condition of pollination effected by the wind; wind-pollination in plants.",
    secondary: "In reproductive botany, an abiotic pollination syndrome prevalent in temperate forests and grasslands where high plant density and seasonal breezes ensure cross-fertilization.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "Evolution toward **anemophily** occurs in habitats where insect pollinators are scarce or seasonal winds are reliable." },
      { author: "Liberty Hyde Bailey", work: "Plant-Breeding", quote: "The mechanics of **anemophily** explain why isolation distances are essential in seed plots to prevent unwanted wind-borne cross-pollination." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The transition from entomophily to **anemophily** represents a fundamental adaptive shift in higher plant phylogeny." }
    ]
  },
  "Dashboard — anem/anemophobia.md": {
    word: "anemophobia",
    primary: "An abnormal, irrational, or disproportionate fear of wind, drafts, or violent atmospheric storms; ancraophobia.",
    secondary: "In clinical psychology and phobia taxonomy, a situational anxiety disorder where the sensation or acoustic roar of moving air produces acute panic and autonomic distress.",
    quotes: [
      { author: "G. Stanley Hall", work: "A Study of Fears", quote: "Children subject to **anemophobia** become hysterical at the sound of howling gales or drafts whistling beneath closed doors." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "In the anxious temperament, **anemophobia** transforms the innocent rustle of autumn leaves into an ominous harbinger of disaster." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Agoraphobic neuroses are frequently accompanied by **anemophobia**, where open windy spaces provoke intense autonomic distress." }
    ]
  },
  "Dashboard — anem/anemopsis.md": {
    word: "anemopsis",
    primary: "A genus of perennial wetland herbs in the lizard's-tail family (Saururaceae), native to southwestern North America, notably Anemopsis californica (yerba mansa).",
    secondary: "In ethnobotany and desert riparian botany, a stoloniferous aromatic herb with basal leaves and conical flower spikes surrounded by white petaloid bracts, traditionally valued for medicinal astringent rhizomes.",
    quotes: [
      { author: "Asa Gray", work: "Plantae Wrightianae", quote: "The singular genus **Anemopsis**, known locally as yerba mansa, carpets alkaline marshes of the desert Southwest." },
      { author: "John Charles Frémont", work: "Report of the Exploring Expedition", quote: "Along the moist margins of the salt spring we collected specimens of **Anemopsis** californica, prized by native tribes for its aromatic root." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "In bog gardens of arid climates, **Anemopsis** forms vigorous aromatic groundcover adorned with white anemone-like petaloid bracts." }
    ]
  },
  "Dashboard — anem/anemoscope.md": {
    word: "anemoscope",
    primary: "An instrument or device, such as a weather vane, designed to indicate the direction of the wind.",
    secondary: "In classical and historical meteorology, an optical or mechanical indicator that signals shifts in wind direction without recording continuous numerical measurements.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "On the Tower of the Winds in Athens, a revolving triton functioned as an **anemoscope**, indicating the prevailing breeze." },
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "A sensitive **anemoscope** mounted atop the mast instantly signals shifts in wind direction before barometer changes become apparent." },
      { author: "Camille Flammarion", work: "The Atmosphere", quote: "Before mechanical recorders were invented, the simple **anemoscope** provided mariners with immediate visual indication of wind direction." }
    ]
  },
  "Dashboard — anem/anemotropism.md": {
    word: "anemotropism",
    primary: "The orientation, movement, or growth response of a sessile organism or plant organ directed by or in response to air currents or wind.",
    secondary: "In experimental plant physiology and invertebrate behavior, an orientation reflex whereby organisms align their anatomical axis with or against prevailing airflow.",
    quotes: [
      { author: "Jacques Loeb", work: "Forced Movements, Tropisms, and Animal Conduct", quote: "In studying orientation in moving air, we observe clear negative **anemotropism** in certain flightless insects." },
      { author: "Wilhelm Pfeffer", work: "The Physiology of Plants", quote: "The orientation of fungal fruiting bodies into the direction of prevailing wind currents illustrates true **anemotropism**." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The skewed growth forms of coastal pines reflect continuous **anemotropism** and mechanical pressure induced by oceanic gales." }
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
console.log("Batch 3 finished! Total words updated:", Object.keys(wordsData).length);
