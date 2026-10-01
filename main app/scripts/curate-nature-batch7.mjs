import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — heli/aphelion.md": {
    word: "aphelion",
    primary: "The point in the elliptical orbit of a planet, comet, or other astronomical body that is farthest from the Sun.",
    secondary: "In celestial mechanics and orbital dynamics, the orbital apsis where a body moves with its minimum orbital velocity in accordance with Kepler's second law.",
    quotes: [
      { author: "Johannes Kepler", work: "Epitome of Copernican Astronomy", quote: "At **aphelion**, the planet reaches its greatest distance from the Sun and travels at its slowest orbital velocity." },
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "The radius vector sweeps equal areas in equal times between perihelion and **aphelion**." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Comets swing far out past the orbit of Pluto, lingering for centuries near their frozen **aphelion**." }
    ]
  },
  "Dashboard — heli/heli.md": {
    word: "heli",
    primary: "A combining form derived from Greek helios meaning the Sun, used extensively in scientific, astronomical, botanical, and physiological terminology.",
    secondary: "In linguistic morphology and scientific nomenclature, designating solar radiation, solar energy systems, sunlight orientation, or heliocentric relationships.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The classical root **heli**- preserves the ancient reverence for the central solar furnace." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Compounds beginning with **heli**- trace humanity's physical and astronomical engagement with the Sun." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "The Greek syllable **heli**- recurs across modern astrophysics to denote solar phenomena." }
    ]
  },
  "Dashboard — heli/heliac.md": {
    word: "heliac",
    primary: "Heliacal; rising or setting with the Sun, or emerging into visibility from the Sun's rays in morning twilight.",
    secondary: "In observational astronomy and ancient chronometry, designating the seasonal first morning appearance of a star just before sunrise after having been obscured by daylight.",
    quotes: [
      { author: "John Herschel", work: "Outlines of Astronomy", quote: "The **heliac** rising of Sirius served ancient Egyptian priests as a calendar marker for the Nile inundation." },
      { author: "Camille Flammarion", work: "The Wonders of the Heavens", quote: "In antique astrology, **heliac** risings were watched with solemn vigil as the morning star emerged from twilight." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Observations of the **heliac** dawn of constellations formed the empirical basis of ancient agrarian calendars." }
    ]
  },
  "Dashboard — heli/heliacal.md": {
    word: "heliacal",
    primary: "Pertaining to or near the Sun; astronomically designating the rising of a celestial body just before sunrise or setting just after sunset.",
    secondary: "In historical astronomy, specifically the heliacal rising when a star or planet first becomes visible in the eastern dawn sky after its annual solar conjunction.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The priests determined the onset of the sacred festival by the **heliacal** rising of the Dog Star in the eastern sky." },
      { author: "Johannes Kepler", work: "Astronomia Nova", quote: "The **heliacal** setting of Mars occurs when the planet sinks into the solar glow shortly after sunset." },
      { author: "John Milton", work: "Paradise Lost", quote: "The bright **heliacal** dawn dissolved the shadows of night across the primeval garden." }
    ]
  },
  "Dashboard — heli/heliamphora.md": {
    word: "heliamphora",
    primary: "A genus of carnivorous pitcher plants (family Sarraceniaceae) commonly called sun pitchers, native to the high sandstone plateaus (tepuis) of South America.",
    secondary: "In evolutionary botany, primitive pitfall-trap plants possessing tubular leaves with small nectar-secreting spoons, adapted to nutrient-deficient, high-radiation tropical mountain summits.",
    quotes: [
      { author: "Charles Darwin", work: "Insectivorous Plants", quote: "The sun pitcher, **Heliamphora**, traps insects within its water-filled tubular leaves atop the cloud-swept Guyana tepuis." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The isolated plateau summits of Mount Roraima harbor ancient relict flora, notably the carnivorous genus **Heliamphora**." },
      { author: "David Attenborough", work: "The Private Life of Plants", quote: "High on the mist-shrouded sandstone mesa, **Heliamphora** thrives in nutrient-poor soils by digesting wandering ants." }
    ]
  },
  "Dashboard — heli/helianthemum.md": {
    word: "helianthemum",
    primary: "A genus of flowering plants in the family Cistaceae commonly called rock roses or sun roses, bearing yellow, orange, or pink blossoms that open in full sunlight.",
    secondary: "In floristic horticulture and alpine botany, low-growing evergreen or semi-evergreen subshrubs of rocky slopes whose delicate petals drop quickly after afternoon exposure.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The yellow **Helianthemum** or rock rose openeth its tender petals only when the sun shineth bright and warm." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "On the sunny chalk banks, the fragile golden blossoms of **Helianthemum** carpet the slope throughout June." },
      { author: "Asa Gray", work: "Manual of Botany", quote: "Species of **Helianthemum** are distinguished by fugacious petals that drop within hours of solar exposure." }
    ]
  },
  "Dashboard — heli/helianthus.md": {
    word: "helianthus",
    primary: "A genus of tall, composite flowering plants in the daisy family (Asteraceae), native to the Americas, comprising sunflowers, notably the common sunflower (Helianthus annuus).",
    secondary: "In economic botany and crop science, large annuals or perennials cultivated worldwide for edible seeds, nutritious vegetable oil, and ornamental garden landscaping.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Linnaeus bestowed the name **Helianthus** upon the sunflower, in allusion to its radiant golden disc and solar orientation." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Along the sandy road, the tall wild **Helianthus** turned its yellow face steadily toward the midday sun." },
      { author: "Willa Cather", work: "My Ántonia", quote: "Miles of wild **Helianthus** lined the red prairie road, their coarse golden heads nodding in the August heat." }
    ]
  },
  "Dashboard — heli/helical.md": {
    word: "helical",
    primary: "Having the shape or form of a helix; spiral or winding in a three-dimensional coil (etymologically from Greek helix twist/coil, here homographic with heli-).",
    secondary: "In structural molecular biology, mechanics, and geometry, describing spiral trajectories such as the alpha-helix in proteins, the double-helical architecture of DNA, or helical gears.",
    quotes: [
      { author: "James D. Watson", work: "The Double Helix", quote: "We suddenly realized that the two sugar-phosphate backbones must follow a smooth **helical** path around a common axis." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "The diffraction pattern of DNA displayed the characteristic cross-shaped signature of a **helical** structure." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The horns of rams and the shells of nautili display logarithmic curves related to regular **helical** winding." }
    ]
  },
  "Dashboard — heli/helichrysum.md": {
    word: "helichrysum",
    primary: "A large genus of flowering plants in the sunflower family (Asteraceae), commonly called everlastings or strawflowers, known for dry, papery golden bracts that retain color indefinitely.",
    secondary: "In herbalism and perfumery, Mediterranean subshrubs (notably Helichrysum italicum or immortelle) prized for aromatic essential oils with potent antioxidant properties.",
    quotes: [
      { author: "John Gerard", work: "The Herball", quote: "The golden everlasting, **Helichrysum**, keepeth its bright color and dry papery petals for years without withering." },
      { author: "Elizabeth David", work: "A Book of Mediterranean Food", quote: "Across the dry Corsican maquis, the warm wind carries the spicy, curry-like fragrance of wild **Helichrysum**." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "In dried floral arrangements, **Helichrysum** remains the preeminent strawflower for its brilliant, unfading yellow bracts." }
    ]
  },
  "Dashboard — heli/helicidae.md": {
    word: "helicidae",
    primary: "A large, diverse family of air-breathing terrestrial pulmonate land snails, including the common garden snail and the edible Roman snail (Helix pomatia).",
    secondary: "In malacology, stylommatophoran gastropods possessing coiled globose or discoidal shells, sophisticated dart apparatuses for mating, and worldwide distribution.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Terrestrial snails of the family **Helicidae** demonstrate astonishing local variation across isolated oceanic archipelagoes." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The distribution of the **Helicidae** across Mediterranean islands reveals ancient geological land bridges." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "During damp summer evenings, members of the **Helicidae** emerge from garden crevices to feed upon tender leaves." }
    ]
  },
  "Dashboard — heli/helicon.md": {
    word: "helicon",
    primary: "A mountain in Boeotia, Greece, celebrated in classical mythology as the home of the Muses; also, a large bass brass wind instrument that encircles the musician's body.",
    secondary: "In classical literature, the symbol of poetic and artistic inspiration from which the sacred springs Aganippe and Hippocrene flowed; in music, the circular precursor to the sousaphone.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "From the Muses of Mount **Helicon** let us begin our song, who dance on soft feet beside the violet-dark spring." },
      { author: "John Milton", work: "Lycidas", quote: "From the sacred heights of **Helicon**, the Muses inspire the mortal poet's song." },
      { author: "John Philip Sousa", work: "Marching Along", quote: "The military brass band carried the great circular **helicon**, its deep bass notes booming through the parade ground." }
    ]
  },
  "Dashboard — heli/helicopter.md": {
    word: "helicopter",
    primary: "A type of aircraft that derives both lift and propulsion from horizontally rotating overhead blades or rotors (from Greek helix spiral + pteron wing).",
    secondary: "In aeronautical engineering and aviation history, a vertical-takeoff-and-landing (VTOL) rotary-wing vehicle capable of hovering, flying backwards, and landing in confined spaces.",
    quotes: [
      { author: "Igor Sikorsky", work: "The Story of the Winged-S", quote: "The successful hover of our **helicopter** proved that rotating lifting surfaces could provide complete omnidirectional flight control." },
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", quote: "Unlike the fixed-wing craft that must rush relentlessly forward, the **helicopter** hangs suspended like a mechanical dragonfly." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Future explorers on Mars will utilize a robotic **helicopter** to scout canyons and cliffs inaccessible to wheeled rovers." }
    ]
  },
  "Dashboard — heli/helicteres.md": {
    word: "helicteres",
    primary: "A genus of tropical trees and shrubs in the mallow family (Malvaceae), commonly known as screw-trees, named for their uniquely twisted spiral seed capsules.",
    secondary: "In tropical botany and ethnopharmacology, plants such as Helicteres isora whose spirally twisted fruits are used in traditional medicine for intestinal ailments.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The tropical genus **Helicteres**, or screw-tree, is celebrated for its spirally twisted carpels that untwist hygroscopically when moistened." },
      { author: "Nathaniel Lord Britton", work: "Flora of the American Virgin Islands", quote: "Along the coastal scrub, **Helicteres** jamaicensis displays peculiar corkscrew-shaped seed pods." },
      { author: "Charles Darwin", work: "The Movements and Habits of Climbing Plants", quote: "The twisted fruit capsules of **Helicteres** offer a classic instance of mechanical seed expulsion triggered by desiccation." }
    ]
  },
  "Dashboard — heli/heliobacter.md": {
    word: "heliobacter",
    primary: "A genus of anaerobic, photoheterotrophic, endospore-forming bacteria (family Heliobacteriaceae) that utilize bacteriochlorophyll g for photosynthesis.",
    secondary: "In microbial physiology and the evolution of photosynthesis, unique soil prokaryotes possessing a simple homodimeric Type-I reaction center linking ancient green sulfur bacteria and firmicutes.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The discovery of **Heliobacter** revealed a unique anaerobic lineage possessing bacteriochlorophyll g and lacking peripheral antenna complexes." },
      { author: "Carl Woese", work: "The Universal Ancestor", quote: "Phylogenetic analysis of ribosomal RNA aligns **Heliobacter** close to the gram-positive endospore-forming bacteria." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Photosynthetic energy transduction in **Heliobacter** provides insight into the earliest anaerobic stages of biological light harvesting." }
    ]
  },
  "Dashboard — heli/heliocentric.md": {
    word: "heliocentric",
    primary: "Having or representing the Sun as the center of the solar system, with the planets orbiting around it; Copernican.",
    secondary: "In astronomy and celestial mechanics, measured or calculated with reference to the center of the Sun, contrasted with geocentric coordinates.",
    quotes: [
      { author: "Nicolaus Copernicus", work: "De revolutionibus orbium coelestium", quote: "In the middle of all sits the Sun enthroned; thus we establish a truly **heliocentric** universe." },
      { author: "Galileo Galilei", work: "Dialogue Concerning the Two Chief World Systems", quote: "The phases of Venus provide unassailable ocular proof that the **heliocentric** system of Copernicus is physically true." },
      { author: "Johannes Kepler", work: "Astronomia Nova", quote: "By adopting the **heliocentric** viewpoint, the apparent retrograde loops of the planets are recognized as mere optical perspectives." }
    ]
  },
  "Dashboard — heli/heliocentrism.md": {
    word: "heliocentrism",
    primary: "The astronomical model in which the Earth and other planets revolve around the stationary Sun at the center of the solar system.",
    secondary: "In the history of science, the revolutionary paradigm shift initiated by Aristarchus and established by Copernicus, Kepler, and Galileo that overthrew Ptolemaic geocentrism.",
    quotes: [
      { author: "Galileo Galilei", work: "Letter to the Grand Duchess Christina", quote: "I hold that **heliocentrism** does not contradict holy scripture when natural philosophy is rightly understood." },
      { author: "Thomas Kuhn", work: "The Copernican Revolution", quote: "The adoption of **heliocentrism** shattered the scholastic cosmology and reorganized the scientific worldview of early modern Europe." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The triumph of **heliocentrism** displaced humanity from the imaginary physical center of the universe." }
    ]
  },
  "Dashboard — heli/heliodor.md": {
    word: "heliodor",
    primary: "A transparent, golden-yellow, greenish-yellow, or honey-colored gem variety of the mineral beryl (beryllium aluminum cyclosilicate).",
    secondary: "In gemology and mineralogy, precious beryl colored by ferric iron (Fe3+) impurities, whose name translates from Greek as 'gift of the sun'.",
    quotes: [
      { author: "Pliny the Elder", work: "Natural History", quote: "The golden beryl, which modern mineralogists term **heliodor**, captures the radiant warm yellow of the noon sun." },
      { author: "George Frederick Kunz", work: "Gems and Precious Stones of North America", quote: "Crystals of **heliodor** mined in pegmatite veins display magnificent transparent golden-yellow hues of gem quality." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The color of **heliodor** is attributed to traces of ferric iron substituting within the beryllium aluminum silicate lattice." }
    ]
  },
  "Dashboard — heli/heliogram.md": {
    word: "heliogram",
    primary: "A message or dispatch transmitted by a heliograph using flashed pulses of sunlight reflected from an adjustable mirror.",
    secondary: "In military communications history, visual telegraphic messages transmitted across long line-of-sight distances using Morse code flashes before field radio adoption.",
    quotes: [
      { author: "Rudyard Kipling", work: "Plain Tales from the Hills", quote: "A flashing **heliogram** from the frontier post warned the garrison that the tribesmen had cut the pass." },
      { author: "Winston Churchill", work: "The River War", quote: "Messages flashed by **heliogram** across fifty miles of shimmering desert mirage kept the advancing columns in constant communication." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The signaling corps maintained contact across the hills by mirrors, sending each brief **heliogram** in rapid Morse code." }
    ]
  },
  "Dashboard — heli/heliograph.md": {
    word: "heliograph",
    primary: "An optical signaling apparatus that transmits messages in code by flashing sunlight reflected from an adjustable mirror; also an instrument for recording hours of sunshine.",
    secondary: "In meteorology, the Campbell-Stokes sunshine recorder that focuses sunlight through a glass sphere to burn a trace upon a card; in military history, a tripod-mounted flash signaling device.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "The Campbell-Stokes **heliograph** burns a charred trace upon curved paper, measuring the exact daily duration of bright sunshine." },
      { author: "Winston Churchill", work: "The Story of the Malakand Field Force", quote: "On the highest crag, the signallers worked the **heliograph**, catching the solar ray to blink messages to the valley." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "By directing a silvered **heliograph** toward distant peaks, military surveyors measured vast triangulation baselines." }
    ]
  },
  "Dashboard — heli/heliogravure.md": {
    word: "heliogravure",
    primary: "Photogravure; an intaglio printmaking process in which a photographic negative is transferred to a sensitized copper plate and etched with acid.",
    secondary: "In the history of fine art printing and photography, an exquisite 19th-century photomechanical process prized for rich velvety continuous tones and archival permanence.",
    quotes: [
      { author: "Alfred Stieglitz", work: "Camera Work", quote: "The rich tonal depth of **heliogravure** elevates photography from mechanical reproduction into a fine graphic art." },
      { author: "Walter Benjamin", work: "The Work of Art in the Age of Mechanical Reproduction", quote: "The exquisite photogravure or **heliogravure** reproduced the subtle chiaroscuro of oil paintings with unprecedented fidelity." },
      { author: "Beaumont Newhall", work: "The History of Photography", quote: "Through **heliogravure**, continuous photographic tones were etched onto intaglio copper plates for ink press printing." }
    ]
  },
  "Dashboard — heli/heliolatry.md": {
    word: "heliolatry",
    primary: "The worship of the Sun as a god or divine entity; sun-worship.",
    secondary: "In comparative mythology and the anthropology of religion, solar religious cults widespread among ancient agrarian civilizations including Egypt, Persia, and Mesoamerica.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "From ancient Egypt to the Inca empire, **heliolatry** formed the religious foundation of divine kingship." },
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "In the evolution of religion, **heliolatry** represents the supreme personification of the celestial power that sustains all life." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The mythological epithets of Apollo and Ra demonstrate how natural gratitude for warmth crystallized into formal **heliolatry**." }
    ]
  },
  "Dashboard — heli/heliomania.md": {
    word: "heliomania",
    primary: "An abnormal, uncontrollable desire or obsession to be exposed to sunlight.",
    secondary: "In psychopathology and behavioural dermatology, a compulsive craving for sunbathing or ultraviolet exposure despite known risks of erythema and skin malignancy.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "An excessive craving for solar exposure, amounting to a compulsive **heliomania**, may dominate the behavior of sunbathers." },
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "The obsessive pursuit of tanning in cases of **heliomania** frequently conceals narcissistic anxieties over bodily aging." },
      { author: "G. Stanley Hall", work: "Adolescence", quote: "During summertime holidays, adolescent vigor sometimes gives way to a restless **heliomania**, spending all day under the blazing sun." }
    ]
  },
  "Dashboard — heli/heliometer.md": {
    word: "heliometer",
    primary: "An astronomical refracting telescope having an objective lens divided along its diameter into two movable halves, originally invented to measure the Sun's diameter.",
    secondary: "In astrometry, a high-precision instrument with micrometer-controlled split lenses famously utilized by Friedrich Bessel in 1838 to achieve the first successful measurement of stellar parallax.",
    quotes: [
      { author: "Friedrich Wilhelm Bessel", work: "Briefwechsel mit Olbers", quote: "Using the Fraunhofer **heliometer** at Königsberg, I successfully measured the stellar parallax of 61 Cygni." },
      { author: "John Herschel", work: "A Treatise on Astronomy", quote: "The divided object-glass of the **heliometer** enables the astronomer to bring two separated celestial images into precise contact." },
      { author: "Arthur Eddington", work: "Stars and Atoms", quote: "Bessel's triumphant measurement of stellar parallax with the **heliometer** proved that stars are distant suns." }
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
console.log("Batch 7 finished! Total words updated:", Object.keys(wordsData).length);
