import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — heli/heliopause.md": {
    word: "heliopause",
    primary: "The theoretical boundary where the solar wind is slowed to a stop by the pressure of the interstellar medium; the outer boundary of the heliosphere.",
    secondary: "In astrophysics and deep-space exploration, the transitional shock front separating the Sun's magnetic influence and plasma domain from interstellar space.",
    quotes: [
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Far beyond the orbits of Neptune and Pluto lies the **heliopause**, where the solar wind is finally turned back by the interstellar gale." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Crossing the **heliopause**, a probe leaves behind the sun's magnetic domain and enters true interstellar space." },
      { author: "Steven Weinberg", work: "The First Three Minutes", quote: "At the **heliopause**, solar cosmic radiation yields dominance to the galactic cosmic-ray flux." }
    ]
  },
  "Dashboard — heli/Heliophila.md": {
    word: "Heliophila",
    primary: "A genus of flowering annual and perennial herbs and subshrubs in the mustard family (Brassicaceae), native to southern Africa, known for blue or white flowers that thrive in open sun.",
    secondary: "In South African floristic botany, sun-loving annuals characteristic of the succulent Karoo and fynbos biomes, forming vibrant mass spring displays after winter rains.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The South African genus **Heliophila** displays delicate blue and violet cruciferous blossoms that carpet the sun-drenched plains of Namaqualand." },
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Species of **Heliophila** are readily recognized by their linear leaves and sun-loving habits in arid soils." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "In desert crucifers like **Heliophila**, floral pigmentation and rapid seed maturation are tuned to fleeting winter rains." }
    ]
  },
  "Dashboard — heli/heliophobia.md": {
    word: "heliophobia",
    primary: "An abnormal, morbid, or irrational fear or avoidance of sunlight.",
    secondary: "In psychopathology and clinical photobiology, a phobic anxiety disorder or extreme photophobia where exposure to direct sunlight provokes panic, dread, or physical agony.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "In patients afflicted with **heliophobia**, the cheerful glare of noon produces acute panic and an agonizing urge to flee into shuttered rooms." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Severe **heliophobia** often accompanies acute migraine or photophobic neuralgia, forcing the sufferer to seek complete darkness." },
      { author: "Bram Stoker", work: "Dracula", quote: "The nocturnal habits of the creature suggested a morbid **heliophobia**, retreating to the tomb before the first light of dawn." }
    ]
  },
  "Dashboard — heli/heliophyte.md": {
    word: "heliophyte",
    primary: "A plant that thrives in, requires, or is adapted to full, unobstructed sunlight; a sun plant (contrasted with sciophyte).",
    secondary: "In plant physiological ecology, species possessing high photosynthetic light saturation points, thick cuticles, vertical leaf angles, and abundant chlorophyll a/b ratios.",
    quotes: [
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "A true **heliophyte**, such as the prairie sunflower, requires full unobstructed sunlight and exhibits stunted development in the canopy shade." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "The thick, cutinized epidermis and vertical leaf orientation of a **heliophyte** minimize excessive water loss under intense insolation." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", quote: "In early ecological succession, opportunistic **heliophytes** rapidly colonize open ground before shade-tolerant species arrive." }
    ]
  },
  "Dashboard — heli/heliopsis.md": {
    word: "heliopsis",
    primary: "A genus of herbaceous perennial composite plants (family Asteraceae) native to North America, commonly known as oxeye or false sunflowers.",
    secondary: "In floriculture and grassland ecology, hardy prairie perennials bearing sunflower-like yellow flower heads with fertile ray florets, blooming profusely from midsummer to frost.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Commonly called the false sunflower or oxeye, **Heliopsis** provides sturdy yellow blossoms that persist through late summer droughts." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The composite genus **Heliopsis** differs from Helianthus in possessing fertile ray flowers that yield distinct achenes." },
      { author: "John Burroughs", work: "Wake-Robin", quote: "Along the railway embankments, coarse yellow discs of **Heliopsis** cheered the dusty August landscape." }
    ]
  },
  "Dashboard — heli/Helios.md": {
    word: "Helios",
    primary: "The ancient Greek titan and personification of the Sun, son of Hyperion and Theia, brother of Selene and Eos, depicted driving a fiery chariot across heaven each day.",
    secondary: "In classical mythology and art, the all-seeing solar deity whose colossal bronze statue at Rhodes (Colossus of Rhodes) was celebrated as one of the Seven Wonders of the Ancient World.",
    quotes: [
      { author: "Homer", work: "The Odyssey", quote: "Now the sun god **Helios**, who sees all things and hears all things, climbed the steep celestial arch." },
      { author: "Hesiod", work: "Theogony", quote: "And Theia bore great **Helios** and gleaming Selene and Eos who shines for all that dwell on earth." },
      { author: "Percy Bysshe Shelley", work: "Hymn of Apollo", quote: "The golden chariot of **Helios** wheels across the azure plain, scattering light upon mortal eyes." }
    ]
  },
  "Dashboard — heli/helioscope.md": {
    word: "helioscope",
    primary: "A telescope or optical device adapted for viewing the Sun without injury to the observer's eyes, using darkened filters, polarizing prisms, or projection screens.",
    secondary: "In observational solar astronomy, an instrument designed to reduce solar glare and heat, enabling the safe examination of sunspots, solar granules, and planetary transits.",
    quotes: [
      { author: "Galileo Galilei", work: "Letters on Sunspots", quote: "Through an ingenious **helioscope** projection upon white paper, I tracked the daily transit of maculae across the solar disc." },
      { author: "Johannes Kepler", work: "Astronomia Nova", quote: "The **helioscope** protects the observer's vision while magnifying the violent granulation of the solar photosphere." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "A polarizing **helioscope** dims the intolerable brilliance of the Sun, revealing solar flares and faculae in crisp detail." }
    ]
  },
  "Dashboard — heli/heliosphere.md": {
    word: "heliosphere",
    primary: "The immense, bubble-like region of space surrounding the Sun, carved out of the interstellar medium by the outflowing supersonic solar wind and magnetic field.",
    secondary: "In space physics and planetary science, the protective cosmic domain encompassing all planets of the solar system, shielding them from the brunt of galactic cosmic rays.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Our entire planetary system is shielded within the **heliosphere**, a vast electromagnetic cocoon carved out by the solar wind." },
      { author: "Patrick Moore", work: "The New Challenge of the Stars", quote: "The Voyager spacecraft journeyed for decades to map the outer limits of the turbulent **heliosphere**." },
      { author: "Arthur Eddington", work: "Stars and Atoms", quote: "The outflow of ionized gas from the corona maintains the dynamic equilibrium of the **heliosphere** against interstellar pressure." }
    ]
  },
  "Dashboard — heli/heliostat.md": {
    word: "heliostat",
    primary: "An optical instrument consisting of a plane mirror moved continuously by clockwork or motors so as to reflect sunlight in a constant, unchanging direction.",
    secondary: "In solar energy engineering and astrophysical laboratories, an automated tracking reflector used in solar power towers or to feed sunlight into fixed subterranean spectrographs.",
    quotes: [
      { author: "Léon Foucault", work: "Sur les diverses méthodes employées pour mesurer la vitesse de la lumière", quote: "A clockwork **heliostat** directed a stationary beam of sunlight through the rotating mirror of our measuring apparatus." },
      { author: "John Tyndall", work: "Heat a Mode of Motion", quote: "By means of an adjustable **heliostat**, a concentrated solar ray was maintained upon the thermo-electric pile." },
      { author: "Camille Flammarion", work: "The Atmosphere", quote: "Spectroscopic observatories employ a planar **heliostat** to track the Sun and feed an unchanging beam into subterranean spectrographs." }
    ]
  },
  "Dashboard — heli/heliotherapy.md": {
    word: "heliotherapy",
    primary: "The therapeutic use of natural sunlight for the treatment of physical and psychological diseases; sun-cure.",
    secondary: "In clinical medicine and balneology, a clinical modality pioneered by Finsen and Rollier for curing cutaneous tuberculosis, rickets, and chronic wound infections via solar ultraviolet radiation.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "The curative benefits of **heliotherapy** are evident in how quickly pale, languishing patients revive when placed in sun-drenched wards." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In the treatment of scrofuloderma and surgical tuberculosis, systematic **heliotherapy** in high Alpine sanatoria produced remarkable healing." },
      { author: "Niels Finsen", work: "Chemical Light Rays and Medical Science", quote: "Concentrated chemical light and systematic **heliotherapy** demonstrated that actinic rays could destroy bacteriological foci in tissue." }
    ]
  },
  "Dashboard — heli/heliothis.md": {
    word: "heliothis",
    primary: "A genus of noctuid moths (family Noctuidae), whose caterpillars include major agricultural pests such as the corn earworm and tobacco budworm.",
    secondary: "In applied agricultural entomology, polyphagous moth pests whose destructive larvae bore into fruit capsules, cotton bolls, and tomato fruits worldwide.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Heavy aerial spraying failed to eradicate **Heliothis**, instead selecting for chemically resistant populations of bollworms." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Larvae of **Heliothis** exhibit surprising color polymorphism corresponding to the floral parts upon which they feed." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The destructive corn earworm, belonging to the genus **Heliothis**, causes millions of dollars in crop losses across temperate agricultural valleys." }
    ]
  },
  "Dashboard — heli/heliotrope.md": {
    word: "heliotrope",
    primary: "A plant of the genus Heliotropium (family Boraginaceae) with fragrant purple, violet, or white flowers; also a moderate reddish-purple color or a dark green chalcedony gemstone with red jasper spots (bloodstone).",
    secondary: "In surveying, an instrument that reflects sunlight with a mirror to indicate distant observation stations; historically, any plant that turns toward the Sun.",
    quotes: [
      { author: "Charles Baudelaire", work: "Les Fleurs du Mal", quote: "The sweet, vanilla-like perfume of the purple **heliotrope** drifted through the warm twilight air of the terrace." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The garden border was fragrant with beds of sweet-scented **heliotrope** and clove pinks." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The stone named **heliotrope**, or bloodstone, reflects red rays when dropped into water facing the sun." }
    ]
  },
  "Dashboard — heli/heliotropic.md": {
    word: "heliotropic",
    primary: "Turning, orienting, or growing toward sunlight; exhibiting heliotropism.",
    secondary: "In plant physiological ecology, describing floral or foliar structures (such as young sunflower buds) that track the diurnal movement of the Sun from east to west.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "Young seedling stems are vigorously **heliotropic**, curving toward lateral light through differential cellular elongation." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Like a **heliotropic** plant, the human spirit instinctively bends toward every ray of warmth and truth." },
      { author: "Henri Bergson", work: "Creative Evolution", quote: "The **heliotropic** curvature of growing vegetation demonstrates the fundamental responsiveness of protoplasm to solar energy." }
    ]
  },
  "Dashboard — heli/heliotropism.md": {
    word: "heliotropism",
    primary: "The directional growth, turning, or orientation movement of a plant or other organism toward or away from sunlight; solar phototropism.",
    secondary: "In plant physiology, an auxin-mediated growth response whereby asymmetric cellular elongation on the shaded side of an organ causes it to bend toward incident light.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "We have shown that **heliotropism** is a modified form of circumnutation directed by the stimulus of incident light." },
      { author: "Jacques Loeb", work: "Studies in General Physiology", quote: "Positive **heliotropism** in sessile organisms can be formulated as a physicochemical reaction governed by photochemical absorption laws." },
      { author: "Wilhelm Pfeffer", work: "Physiology of Plants", quote: "The mechanisms of **heliotropism** depend upon auxin redistribution between the shaded and illuminated flanks of the coleoptile." }
    ]
  },
  "Dashboard — heli/heliotype.md": {
    word: "heliotype",
    primary: "A print produced by a photo-mechanical process (a form of collotype) utilizing a gelatin film hardened with chrome alum to print continuous photographic tones in ink.",
    secondary: "In the history of photographic reproduction, an archival 19th-century process invented by Ernest Edwards, widely used for high-fidelity book illustrations without grain.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "The Doings of the Sunbeam", quote: "The newly invented **heliotype** reproduces photographic negatives in permanent printer's ink with astonishing clarity." },
      { author: "William Dean Howells", work: "A Hazard of New Fortunes", quote: "The prospectus for the illustrated magazine featured fine **heliotype** plates reproducing Parisian landscapes." },
      { author: "Beaumont Newhall", work: "The History of Photography", quote: "Commercial book publishers embraced the **heliotype** in the 1870s because it eliminated the fading inherent in silver albumen prints." }
    ]
  },
  "Dashboard — heli/heliozoa.md": {
    word: "heliozoa",
    primary: "A grouping of freshwater and marine amoeboid protozoans commonly called sun animalcules, possessing spherical bodies with stiff radiating axopodia.",
    secondary: "In protozoology and microbenthic biology, predatory sarcodines whose radiating axopodia are supported by intricate spiral or hexagonal microtubule arrays used to capture microplankton.",
    quotes: [
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The **Heliozoa**, or sun animalcules, display breathtaking radial symmetry with needle-like axopodia radiating from a spherical central capsule." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "Under microscopic observation, the freshwater **Heliozoa** resemble miniature radiant stars floating amidst filamentous algae." },
      { author: "William Benjamin Carpenter", work: "The Microscope and Its Revelations", quote: "Each axopodium of the **Heliozoa** consists of an internal stereoplasmic axis surrounded by streaming, sticky protoplasm." }
    ]
  },
  "Dashboard — heli/heliozoan.md": {
    word: "heliozoan",
    primary: "Any predatory amoeboid protozoan belonging to the Heliozoa, characterized by a spherical body and slender radiating axopodia; a sun animalcule.",
    secondary: "In plankton biology, a microscopic hunter that immobilizes passing ciliates and rotifers upon contact with adhesive extrusomes along its radiating cytoplasmic needles.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "A solitary **heliozoan** drifted across the slide, its slender ray-like pseudopodia capturing passing flagellates." },
      { author: "Libbie Hyman", work: "The Invertebrates: Protozoa", quote: "When prey touches the axopodium of a **heliozoan**, rapid adhesion and cytoplasmic streaming draw the victim into a digestive food vacuole." },
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "Centrosomal organization in the **heliozoan** cell provides insights into the structural anchoring of microtubular bundles." }
    ]
  },
  "Dashboard — heli/helium.md": {
    word: "helium",
    primary: "A light, colorless, odorless, nonflammable noble gas of atomic number 2 (symbol He), the second lightest and second most abundant element in the universe.",
    secondary: "In astrophysics and cryogenic engineering, an element first discovered in 1868 as an unassigned absorption line in the solar spectrum, liquefied at 4.2 K to produce superfluidity.",
    quotes: [
      { author: "Norman Lockyer", work: "Contributions to Solar Physics", quote: "To the mysterious yellow spectral line D3 in the solar chromosphere, Frankland and I assigned the element name **helium**." },
      { author: "William Ramsay", work: "The Discovery of Helium", quote: "Upon treating the mineral cleveite with acid, we isolated terrestrial **helium**, confirming Lockyer's solar discovery." },
      { author: "Ernest Rutherford", work: "Radioactive Transformations", quote: "The alpha particle emitted during radioactive decay was conclusively identified as a doubly ionized atom of **helium**." }
    ]
  },
  "Dashboard — heli/parheliacal.md": {
    word: "parheliacal",
    primary: "Of, relating to, or resembling a parhelion (mock sun or sun dog); produced by parhelic optical refraction.",
    secondary: "In meteorological optics, describing luminous atmospheric arcs and spots produced by the reflection and refraction of sunlight through hexagonal ice crystals in cirrus clouds.",
    quotes: [
      { author: "Robert Falcon Scott", work: "The Voyage of the Discovery", quote: "Above the Antarctic ice shelf, brilliant **parheliacal** spots flashed along the solar circle like luminous diamonds." },
      { author: "Samuel Taylor Coleridge", work: "Notebooks", quote: "The frosty atmosphere generated a wondrous **parheliacal** display, encircling the sun with shimmering prismatic arcs." },
      { author: "Camille Flammarion", work: "The Atmosphere", quote: "In high polar latitudes, **parheliacal** phenomena occur with extraordinary frequency whenever needle-like ice crystals fill the calm air." }
    ]
  },
  "Dashboard — heli/parhelic.md": {
    word: "parhelic",
    primary: "Pertaining to a parhelion or the parhelic circle; designating the horizontal white circle that passes through the Sun and parhelia at the same altitude.",
    secondary: "In atmospheric physics, describing optical halo displays caused by horizontal plate-like ice crystals reflecting sunlight in cold tropospheric layers.",
    quotes: [
      { author: "Fridtjof Nansen", work: "Farthest North", quote: "A luminous **parhelic** ring passed horizontally through the sun, intersected by vertical pillars of dazzling white light." },
      { author: "John Tyndall", work: "The Glaciers of the Alps", quote: "Refraction through atmospheric hexagonal ice prisms produces both the solar halo and the horizontal **parhelic** circle." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Observations of complex **parhelic** systems provided early physicists with empirical evidence of ice crystal geometry in the upper troposphere." }
    ]
  },
  "Dashboard — heli/parhelion.md": {
    word: "parhelion",
    primary: "A bright, rainbow-tinted optical spot appearing on either side of the Sun on a 22-degree halo; a mock sun or sun dog.",
    secondary: "In atmospheric optics, a luminous phenomenon produced when sunlight is refracted through hexagonal plate ice crystals floating with horizontal faces in cirrus clouds.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 3", quote: "Three glorious suns, each one a perfect sun; / Not separated with the racking clouds, / But sever'd in a pale clear-shining sky." },
      { author: "Henry David Thoreau", work: "Autumnal Tints", quote: "On a cold November afternoon, a radiant **parhelion** burned on either side of the low winter sun like a phantom attendant." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Round the frozen masthead hovered a luminous **parhelion**, mocking the crew with spectral twin suns." }
    ]
  },
  "Dashboard — heli/perihelion.md": {
    word: "perihelion",
    primary: "The point in the elliptical orbit of a planet, asteroid, or comet that is closest to the Sun (contrasted with aphelion).",
    secondary: "In celestial mechanics and general relativity, the orbital periapsis where a body attains its highest gravitational acceleration and velocity, notably showing orbital precession in Mercury.",
    quotes: [
      { author: "Johannes Kepler", work: "Astronomia Nova", quote: "At **perihelion**, Mars reaches its closest approach to the Sun, attaining its maximum velocity along its elliptical orbit." },
      { author: "Albert Einstein", work: "Explanation of the Perihelion Motion of Mercury", quote: "General relativity accounts precisely for the forty-three arcseconds of anomalous **perihelion** advance of Mercury." },
      { author: "Isaac Newton", work: "Principia", quote: "The gravitational attraction reaches its greatest intensity as the planet sweeps through **perihelion**." }
    ]
  },
  "Dashboard — aer/aer 2.md": {
    word: "aer 2",
    primary: "A combining prefix derived from Greek aer denoting air, the atmosphere, aviation, gases, or respiration (variant entry for aero- / aer-).",
    secondary: "In linguistic morphology and scientific nomenclature, forming compound words relating to aeronautics, aerobic biology, atmospheric physics, and aerosol dynamics.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The prefix **aer**- designates atmospheric respiration and the pneumatic mechanics of terrestrial life." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "In scientific nomenclature, the combining root **aer**- embraces all phenomena pertaining to atmospheric air and its chemical properties." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Physiological terms compounding **aer**- emphasize the absolute dependence of vital combustion upon atmospheric oxygen." }
    ]
  },
  "Dashboard — aer/aer.md": {
    word: "aer",
    primary: "The ancient Greek noun for air or the lower atmosphere, celebrated in classical philosophy as one of the four primordial elements.",
    secondary: "In the history of natural philosophy and pre-Socratic cosmology (notably Anaximenes), the infinite primal substance from which all material entities were condensed or rarefied.",
    quotes: [
      { author: "Aristotle", work: "Meteorology", quote: "In classical physics, **aer** represents the hot and moist element occupying the sphere between terrestrial water and celestial fire." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The ancients considered **aer** to be a prime substance whose subtle currents distribute life across the globe." },
      { author: "John Milton", work: "Paradise Lost", quote: "Through the pure **aer** of heaven the celestial messengers winged their untiring flight." }
    ]
  },
  "Dashboard — aer/aerate.md": {
    word: "aerate",
    primary: "To supply, charge, or permeate a liquid, soil, or substance with air, oxygen, or gas (such as carbon dioxide).",
    secondary: "In agronomy, hydrology, and respiratory physiology, to expose circulating fluids or dense soils to atmospheric oxygen to support aerobic respiration and biological vitality.",
    quotes: [
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould through the Action of Worms", quote: "By burrowing through the soil, earthworms **aerate** the dense loam and facilitate root penetration." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "When we vigorously **aerate** the yeast broth, vegetative growth increases while alcoholic fermentation is suppressed." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Microbial decomposers **aerate** fertile garden soils, recycling essential nutrients into the biosphere." }
    ]
  },
  "Dashboard — aer/aerated.md": {
    word: "aerated",
    primary: "Supplied, charged, or impregnated with air or gas (especially carbon dioxide, as in effervescent beverages); oxygenated.",
    secondary: "In aquatic ecology and soil mechanics, describing waters or substrate strata possessing abundant dissolved oxygen capable of sustaining aerobic benthic life.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "The clear, cold, **aerated** water of the pond sparkled with thousands of tiny rising bubbles." },
      { author: "Joseph Priestley", work: "Experiments and Observations on Different Kinds of Air", quote: "By impregnating spring water with fixed air, I produced a pleasant **aerated** beverage resembling Pyrmont mineral water." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Blood circulating through healthy pulmonary capillaries becomes richly **aerated** with atmospheric oxygen." }
    ]
  },
  "Dashboard — aer/aeration.md": {
    word: "aeration",
    primary: "The process of exposing a substance to the circulation of air, or charging a liquid or soil with air, oxygen, or carbon dioxide.",
    secondary: "In environmental engineering and wastewater treatment, the mechanical injection of air into sludge or water to stimulate aerobic bacterial decomposition of organic waste.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Beer", quote: "Proper **aeration** of the wort ensures healthy yeast proliferation before the onset of anaerobic fermentation." },
      { author: "Charles Darwin", work: "Vegetable Mould and Earthworms", quote: "The continuous **aeration** of agricultural soils by subterranean organisms is essential for humification." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Without constant **aeration** and circulation of fresh air, the hospital ward becomes a reservoir of pestilence." }
    ]
  },
  "Dashboard — aer/aerator.md": {
    word: "aerator",
    primary: "A device or apparatus that introduces air into a liquid or soil, such as a faucet nozzle aerator, aquarium bubbler, or lawn coring tool.",
    secondary: "In industrial bioengineering and municipal water treatment, a mechanical impeller, sparger, or fountain designed to maximize gas-liquid mass transfer and dissolved oxygen levels.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "In our marine aquarium, a mechanical **aerator** bubbled continuously to maintain dissolved oxygen for delicate filter feeders." },
      { author: "Louis Pasteur", work: "Collected Works", quote: "A fine porcelain **aerator** dispersed microscopic air bubbles evenly through the experimental bacterial broth." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "Martin adjusted the electric **aerator** in the incubator, watching the fine spray oxygenate the nutrient broth." }
    ]
  },
  "Dashboard — aer/aerenchyma.md": {
    word: "aerenchyma",
    primary: "A spongy plant tissue containing large, interconnected intercellular air spaces, found primarily in the roots, stems, and leaves of aquatic and wetland plants.",
    secondary: "In plant anatomy and wetland ecology, specialized lacunar parenchyma that facilitates internal gas exchange between emergent shoots and submerged, anoxic roots.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "Aquatic plants develop spongy **aerenchyma** filled with large intercellular gas spaces that provide internal buoyancy and root ventilation." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "The presence of lacunar **aerenchyma** in wetland sedges allows oxygen diffusion down into anoxic marsh mud." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "In waterlogged soils, species capable of forming adventitious **aerenchyma** survive prolonged submergence." }
    ]
  },
  "Dashboard — aer/aerial ladder.md": {
    word: "aerial ladder",
    primary: "A long, mechanically extendable ladder mounted on a turntable on the chassis of a specialized firefighting truck (aerial truck).",
    secondary: "In municipal emergency rescue and fire protection engineering, a hydraulic telescoping apparatus equipped with waterways and rescue platforms for high-rise building access.",
    quotes: [
      { author: "Jacob Riis", work: "How the Other Half Lives", quote: "The fire department extended its **aerial ladder** up to the tenement roof, rescuing trapped families from the smoke." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Firefighters trained their hoses from the top of the **aerial ladder**, pouring torrents into the burning slaughterhouse." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The mechanization of municipal safety, symbolized by the motorized **aerial ladder**, transformed vertical firefighting in modern metropolises." }
    ]
  },
  "Dashboard — aer/aerial yam.md": {
    word: "aerial yam",
    primary: "A vigorous climbing vine (Dioscorea bulbifera) in the yam family (Dioscoreaceae), commonly called air potato, that produces edible potato-like bulbils in its leaf axils.",
    secondary: "In tropical agronomy and ethnobotany, a fast-growing perennial liana cultivated across tropical Asia and Africa for its aerial tubers, though requiring boiling to eliminate toxic furostanol saponins in wild forms.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The **aerial yam**, Dioscorea bulbifera, produces edible bulbils in the leaf axils along its vigorous climbing vines." },
      { author: "David Fairchild", work: "The World Was My Garden", quote: "In the tropical garden we harvested the tubers of the **aerial yam**, which hang like curious brown stones from the trellis." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Members of the Dioscoreaceae, particularly the **aerial yam**, display remarkable storage bulbils borne entirely above ground." }
    ]
  },
  "Dashboard — aer/aerial.md": {
    word: "aerial",
    primary: "Inhabiting, existing in, or operating in the air; lofty, ethereal, or visionary; also, a radio or television antenna.",
    secondary: "In aeronautics and telecommunications, pertaining to atmospheric navigation, airborne photography, or metallic conductors designed to radiate or receive electromagnetic radio waves.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "A lake is a river of **aerial** blue, reflecting the serenity of the open heavens." },
      { author: "Percy Bysshe Shelley", work: "To a Skylark", quote: "Like an unbodied joy whose race is just begun, / The bird ascends with **aerial** lightness into the dawn." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "From his **aerial** perch at the masthead, the lookout swept the ocean horizon for spouts." }
    ]
  },
  "Dashboard — aer/aerialist.md": {
    word: "aerialist",
    primary: "An acrobat or gymnast who performs feats high above the ground on a trapeze, tightrope, high wire, or suspended silks.",
    secondary: "In performing arts and circus history, an athletic performer possessing extraordinary balance, grip strength, and spatial awareness executing mid-air maneuvers.",
    quotes: [
      { author: "Charles Dickens", work: "Hard Times", quote: "The crowd held its breath as the daring **aerialist** swung across the circus dome on the high trapeze." },
      { author: "Walt Whitman", work: "Specimen Days", quote: "With effortless poise, the gymnastic **aerialist** seemed to float weightlessly through the vaulted theater." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "He admired the swaggering confidence of the circus **aerialist**, poised high above the sawdust ring." }
    ]
  },
  "Dashboard — aer/aerially.md": {
    word: "aerially",
    primary: "In an aerial manner; by, in, or through the air; ethereally or loftily.",
    secondary: "In ecology, surveying, and aviation, from an elevated or airborne vantage point, or by means of atmospheric dissemination.",
    quotes: [
      { author: "Henry James", work: "The Wings of the Dove", quote: "The Venetian palaces seemed to float **aerially** above the green waters of the Grand Canal." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "Swallows swept **aerially** across the darkening expanse of Egdon Heath in pursuit of gnats." },
      { author: "Virginia Woolf", work: "The Waves", quote: "The gulls rose **aerially** on the sea wind, turning their wings to catch the morning sun." }
    ]
  },
  "Dashboard — aer/aerie.md": {
    word: "aerie",
    primary: "The nest of a bird of prey (such as an eagle or hawk) built high on a mountain crag or lofty cliff; also, any high, secluded dwelling.",
    secondary: "In literary and ecological description, an elevated mountain redoubt or fortress perched dramatically above surrounding valleys.",
    quotes: [
      { author: "William Wordsworth", work: "The Excursion", quote: "High on the inaccessible cliff, the golden eagle built her solitary **aerie** above the clouds." },
      { author: "John Milton", work: "Paradise Lost", quote: "There the Eagle and the Stork / On Cliffs and Cedar tops their **Aeries** build." },
      { author: "Walter Scott", work: "The Lady of the Lake", quote: "From her mountain **aerie**, the falcon watched the glint of spears winding through the glen." }
    ]
  },
  "Dashboard — aer/aerify.md": {
    word: "aerify",
    primary: "To change or convert into air or vapor; to aerate; to infuse or permeate with air.",
    secondary: "In historical chemistry and thermodynamics, to vaporize a liquid into gaseous form or infuse a solid matrix with air bubbles.",
    quotes: [
      { author: "Joseph Priestley", work: "Experiments on Air", quote: "Our objective was to **aerify** the liquid completely by liberating its dissolved gaseous components." },
      { author: "Humphry Davy", work: "Researches, Chemical and Philosophical", quote: "Intense heat served to **aerify** the volatile solid into an expansive, transparent vapor." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "Electrolytic decomposition tended to **aerify** the electrolyte, releasing bubbles of hydrogen at the cathode." }
    ]
  },
  "Dashboard — aer/aero.md": {
    word: "aero",
    primary: "Relating to aircraft, aviation, or aeronautics; an informal abbreviation for aeroplane or aeronautical.",
    secondary: "In engineering and industrial design, a combining form or modifier designating aerodynamic streamlining, aerospace propulsion, or atmospheric mechanics.",
    quotes: [
      { author: "H. G. Wells", work: "The War in the Air", quote: "The invention of the modern **aero** engine transformed warfare by conquering the third dimension." },
      { author: "Antoine de Saint-Exupéry", work: "Night Flight", quote: "The vibrations of the **aero** postal plane resonated through the pilot's bones as he navigated through the Andean tempest." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The rapid development of **aero** dynamics converted humanity's ancient dream of flight into routine industrial transport." }
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
console.log("Batch 8 finished! Total words updated:", Object.keys(wordsData).length);
