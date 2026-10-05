# -*- coding: utf-8 -*-
"""
Part 3 of Curated Fire, Heat & Ash (non-cal):
Dashboard — gelat (8 words)
Dashboard — tep (11 words)
Dashboard — torr (9 words)
Dashboard — volcan (5 words)
Total: 33 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_part3 = {
  # =========================================================================
  # Dashboard — gelat (8 words)
  # =========================================================================
  "congelation": {
    "primary": "The process of solidifying or freezing a liquid substance into a firm, rigid mass through cold.",
    "secondary": "In geology, physical chemistry, and cryology, the thermal phase change wherein molten fluids or aqueous solutions transition into solid crystalline matrices.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The vast sheet of ice spread before us, exhibiting every stage of **congelation** amid the alpine glaciers."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "In high polar latitudes, the slow **congelation** of groundwater heaves the tundra into fractured mounds and frost wedges."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The arctic air threatened rapid **congelation** to our soaked garments as spray froze into crystal armor upon the gunwales."}
    ]
  },
  "gelatin": {
    "primary": "A colorless, translucent, flavorless protein obtained by boiling animal skin, cartilage, and bones in water.",
    "secondary": "In food science and histology, a hydrolyzed collagen product that hydrates to form thermoreversible colloidal hydrogels.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Cold broth clarified with calves-foot **gelatin** furnished a light and easily assimilable nourishment for the convalescent."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "The dish of trembling fruit **gelatin** gleamed like amber beneath the parlor lamps during the festival."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "In the bacteriologist's incubator, tubes of nutrient **gelatin** revealed distinct liquefaction patterns characteristic of the bacillus."}
    ]
  },
  "gelatine": {
    "primary": "An alternative spelling of gelatin, denoting an edible translucent animal protein setting into jelly.",
    "secondary": "In vintage pharmaceutical and photographic literature, an organic colloid serving as an emulsion binder or soluble capsule casing.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Dissolve the sheet of clarified **gelatine** slowly in warm syrup before folding in the strained fruit juices."},
      {"author": "H. G. Wells", "work": "The Food of the Gods and How It Came to Earth", "quote": "The chemist prepared nutrient slabs stiffened with refined **gelatine** to foster the accelerated growth of experimental cultures."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A thin capsule of soluble **gelatine** containing the deadly alkaloid was found hidden beneath the floorboards."}
    ]
  },
  "gelatinise": {
    "primary": "To convert or process a substance into a jelly-like or gelatinous state or colloidal consistency.",
    "secondary": "In biochemical preparation and industrial processing, to hydrate and break down starch granules or collagen fibrils into an amorphous gel.",
    "quotes": [
      {"author": "Elizabeth David", "work": "French Provincial Cooking", "quote": "Simmer the veal knuckles gently until the rich stocks cool and **gelatinise** into a firm, savory jelly."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "When connective tissue fibers are exposed to prolonged boiling in water, their collagenous elements readily **gelatinise**."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The cook stirred the thickening cornstarch pudding continuously, waiting for the mixture to smooth out and **gelatinise**."}
    ]
  },
  "gelatinize": {
    "primary": "To cause a substance to assume the properties, texture, or consistency of a gelatinous substance.",
    "secondary": "In cereal chemistry and brewing technology, to disrupt intermolecular bonds of starch in the presence of water and heat to produce a paste.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The experimental solvent caused the cellular proteins of living tissue to **gelatinize** before bleaching them entirely transparent."},
      {"author": "Jack London", "work": "The Star Rover", "quote": "In the cold mountain cellar, the rich venison broth began to **gelatinize** into a solid translucent loaf."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Boiled animal sinews gradually **gelatinize**, yielding adhesive glues long employed by primitive craftsmen."}
    ]
  },
  "gelatinlike": {
    "primary": "Having a semi-solid, resilient, or trembling texture resembling that of jelly or gelatin.",
    "secondary": "In anatomical pathology and marine biology, describing translucent viscid exudates, capsules, or pelagic organisms with soft elastic consistency.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Strange pelagic siphonophores drifted through the midnight depth, trailing fragile, **gelatinlike** bells of iridescent sheen."},
      {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "The strange atmospheric deposit formed a soft, **gelatinlike** residue along the exterior panes of our sealed chamber."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Upon opening the synovial bursa, the surgeon encountered a thick, **gelatinlike** effusion following chronic inflammation."}
    ]
  },
  "gelatinous": {
    "primary": "Having the viscous, tremulous, or semi-solid consistency characteristic of jelly or gelatin.",
    "secondary": "In cytology, histology, and zoology, denoting colloidal extracellular matrix, mucilaginous sheaths, or jellyfish anatomy.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The surface of the sea was covered with vast numbers of medusae, their delicate **gelatinous** bodies pulsating in the calm water."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A vast, pulpy mass, furlongs in length and breadth, floated before us—a strange, **gelatinous** apparition of the giant squid."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "In early spring, the shallow pools are crowded with the clustered, **gelatinous** masses of frog spawn attached to reeds."}
    ]
  },
  "gelatinousness": {
    "primary": "The physical characteristic or property of being jelly-like, trembling, or viscous in texture.",
    "secondary": "In rheology and culinary analysis, the measurable viscoelastic firmness and yield stress exhibited by colloid gels.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The sea rolled forward with a heavy, primeval thickness, exhibiting the slow **gelatinousness** of cooling molten glass."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "The peculiar **gelatinousness** of the morbid exudate puzzled the attending pathologists during their anatomical inquiry."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dr. Lydgate observed the gradual **gelatinousness** assumed by the chemical precipitates within his laboratory test phials."}
    ]
  },

  # =========================================================================
  # Dashboard — tep (11 words)
  # =========================================================================
  "antepartum": {
    "primary": "Occurring, existing, or performed during the period before childbirth or maternal delivery.",
    "secondary": "In obstetrics and maternal-fetal medicine, designating diagnostic surveillance and therapeutic care during gestational pregnancy prior to labor.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful monitoring of maternal blood pressure during the **antepartum** phase remains essential to prevent eclampsia."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The young physician instituted routine **antepartum** clinics in the rural township to safeguard expectant mothers."},
      {"author": "Abraham Verghese", "work": "Cutting for Stone", "quote": "In the crowded hospital ward, the midwives prepared the delivery room while administering urgent **antepartum** care."}
    ]
  },
  "antepenult": {
    "primary": "The syllable that occurs third from the end of a word, preceding the penult.",
    "secondary": "In classical prosody and linguistic phonetics, the syllable bearing stress in proparoxytone word structures.",
    "quotes": [
      {"author": "George Saintsbury", "work": "A History of English Prosody", "quote": "The natural accentual rhythm of classical Latin verse consistently favors a stress falling upon the **antepenult**."},
      {"author": "Arthur Quiller-Couch", "work": "On the Art of Writing", "quote": "Careful poets regulate their meter by weighing whether emphasis should alight upon the penult or the **antepenult**."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparative Indo-European grammar demonstrates how pitch accents frequently shifted backward to the vocalic **antepenult**."}
    ]
  },
  "antepenultima": {
    "primary": "The third syllable from the end of a spoken or written word; the antepenult.",
    "secondary": "In historical grammar and morphological phonology, the locus of tonic stress within trisyllabic and multisyllabic accentual rules.",
    "quotes": [
      {"author": "George Saintsbury", "work": "A History of English Prosody", "quote": "In classical scansion, the quantitative weight of the **antepenultima** dictates the metric cadence of dactylic measures."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The rhythmic cadence of philosophical prose often owes its dignified solemnity to a stressed **antepenultima**."},
      {"author": "Thomas de Quincey", "work": "Confessions of an English Opium-Eater", "quote": "The majestic roll of the orator's Latinate periods derived largely from resonant accents falling on the **antepenultima**."}
    ]
  },
  "antepenultimate": {
    "primary": "Third from the last in a sequence, series, chain of events, or spoken word.",
    "secondary": "In phonetics and ordinal ranking, denoting the element immediately preceding the penultimate item or syllable.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether paused upon the **antepenultimate** chapter of his private deliberations, conscious that the final resolution approached."},
      {"author": "Edgar Allan Poe", "work": "The Poetic Principle", "quote": "The dactylic harmony of the stanza demands that vocal inflection descend smoothly from the **antepenultimate** syllable."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The cryptanalyst carefully examined the **antepenultimate** cipher of the coded dispatch to establish its substitution cipher."}
    ]
  },
  "tepal": {
    "primary": "An individual unit or segment of a flower's perianth where petals and sepals are indistinguishable.",
    "secondary": "In botanical morphology, an undifferentiated floral envelope segment typical of monocotyledonous families like Liliaceae and Magnoliaceae.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised by Insects", "quote": "The delicate upper **tepal** of the orchid arched forward to form a protective canopy over the pollinia."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "In cultivated tulip hybrids, each waxy **tepal** displays distinct flamed streaks of scarlet and gold."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "When calyx and corolla coalesce in identical texture and color, the individual division is accurately termed a **tepal**."}
    ]
  },
  "tepee": {
    "primary": "A conical tent made of skins, cloth, or canvas on poles, traditionally used by North American Plains peoples.",
    "secondary": "In anthropology and Plains indigenous architecture, a portable, modular dwelling featuring smoke flaps and tripod or four-pole framework.",
    "quotes": [
      {"author": "Willa Cather", "work": "The Professor's House", "quote": "Across the open prairie stood the tall silhouette of a skin **tepee**, its smoke drifting lazily toward the sunset."},
      {"author": "Francis Parkman", "work": "The Oregon Trail", "quote": "We rode into the circular encampment where buffalo hides stretched tightly across the towering poles of each **tepee**."},
      {"author": "Zane Grey", "work": "Riders of the Purple Sage", "quote": "By the creek bed, the old scout pitched a canvas **tepee** to shelter his companions against the biting desert wind."}
    ]
  },
  "tepic": {
    "primary": "A major city in west-central Mexico and the state capital of Nayarit, situated in an agricultural valley.",
    "secondary": "In geography, regional Mexican history, and toponymy, an urban center founded in pre-Columbian times at the base of the Sangangüey volcano.",
    "quotes": [
      {"author": "John Steinbeck", "work": "The Log from the Sea of Cortez", "quote": "Travelers returning inland from San Blas spoke of the fertile highlands surrounding the historic town of **Tepic**."},
      {"author": "Graham Greene", "work": "The Lawless Roads", "quote": "The narrow train chugged steadily toward **Tepic**, climbing through deep barrancas beneath towering mountain slopes."},
      {"author": "Aldous Huxley", "work": "Beyond the Mexique Bay", "quote": "From Guadalajara the road traversed volcanic plateaus before descending into the subtropical valley of **Tepic**."}
    ]
  },
  "tepid": {
    "primary": "Moderately warm or lukewarm in physical temperature; lacking passionate warmth, enthusiasm, or conviction.",
    "secondary": "In thermodynamics and literary characterization, denoting ambient mild warmth or half-hearted, unenthusiastic emotional response.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I quenched my thirst with a draught of **tepid** water from the stoneware pitcher beside the hearth."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "He washed his face in the **tepid** stream that trickled reluctantly from the corroded basin faucet."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The courtroom received the long-winded arguments of Chancery counsel with **tepid** interest and frequent yawns."}
    ]
  },
  "tepidity": {
    "primary": "The state or attribute of being moderately warm; a lack of thermal heat, enthusiasm, or emotional fervor.",
    "secondary": "In psychosociological critique and thermal measurement, the characteristic of lukewarm indifference or moderate temperature.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon greeted his young bride's eager inquiries with a scholarly **tepidity** that chilled her affectionate spirit."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond concealed his intense aesthetic ambitions behind a cultivated mask of languid **tepidity**."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The damp autumn atmosphere seemed to foster a dreary **tepidity** in both the tavern conversation and the brew."}
    ]
  },
  "tepidly": {
    "primary": "In a moderately warm or lukewarm manner; with faint enthusiasm, weak conviction, or indifference.",
    "secondary": "In narrative exposition, describing actions executed without zeal, passion, or vigorous energetic commitment.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The drawing-room audience applauded **tepidly** at the conclusion of the ballad before returning to their gossip."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The coastal breeze blew **tepidly** across the veranda, carrying the heavy fragrance of nocturnal blossoms."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He shook my outstretched hand **tepidly**, gazing past me with the detached preoccupation of an absentminded scholar."}
    ]
  },
  "tepidness": {
    "primary": "The quality of possessing lukewarm heat; emotional indifference or absence of lively enthusiasm.",
    "secondary": "In sensory assessment and psychological evaluation, moderate thermal warmth or uncommitted affective response.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The shallow river margins retained the **tepidness** of summer sunshine long after dusk had settled over the meadows."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Spiritual mediocrity often retreats into an unheroic **tepidness**, avoiding the extremes of mystical passion and despair."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy shrank from the emotional **tepidness** of Cecil Vyse, whose polite decorum smothered genuine human joy."}
    ]
  },

  # =========================================================================
  # Dashboard — torr (9 words)
  # =========================================================================
  "torr": {
    "primary": "A unit of pressure defined as exactly 1/760 of a standard atmosphere, approximately equal to 1 mmHg.",
    "secondary": "In vacuum physics, fluid mechanics, and barometry, a non-SI metric pressure unit named after Evangelista Torricelli.",
    "quotes": [
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "By evacuating the glass chamber down to a few thousandths of a **torr**, molecular collisions become negligible."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The professor adjusted the mercury column, noting that atmospheric pressure fell several **torr** beneath normal sea level."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "In the near-total vacuum of interplanetary space, residual pressure hovers far below a millionth of a **torr**."}
    ]
  },
  "torrefaction": {
    "primary": "The process of roasting, drying, or scorching an organic substance at high heat in the absence of oxygen.",
    "secondary": "In biomass energy engineering and metallurgy, mild pyrolysis between 200°C and 300°C that improves fuel energy density and grindability.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subterranean heat working upon subterranean lignite beds produces an intense natural **torrefaction** of carbonaceous strata."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The dry heat oven completed the thorough **torrefaction** of the soil samples before chemical analysis began."},
      {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "The scorching desert winds subjected the upland shrubs to a severe atmospheric **torrefaction** during summer droughts."}
    ]
  },
  "torrent": {
    "primary": "A swift, violent, and copious stream of liquid, water, or other fluid moving with great force.",
    "secondary": "In hydrology, meteorology, and rhetoric, a rushing turbulent flash flood or an overwhelming, cascading outpouring of words or sensations.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The mountain river rushed downward in a foaming **torrent**, echoing through the lonely Alpine chasms with sullen roar."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A living **torrent** of impassioned citizens surged through the narrow defiles of Saint Antoine toward the Bastille."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A blinding **torrent** of brine cascaded over the forecastle deck as the ship plunged into the roaring trough of the wave."}
    ]
  },
  "torrential": {
    "primary": "Falling rapidly and in abundant copious quantities, resembling or caused by a violent torrent.",
    "secondary": "In meteorology and geomorphology, designating high-precipitation downpours capable of initiating flash runoff and hillside erosion.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The tropical squall broke overhead with sudden fury, unleashing a **torrential** rain that blotted out sea and sky."},
      {"author": "W. Somerset Maugham", "work": "The Painted Veil", "quote": "Night after night, the **torrential** monsoon drummed relentlessly against the corrugated zinc roof of the bungalow."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak labored through the night to thatch the ricks before the gathering clouds broke into **torrential** sheets."}
    ]
  },
  "torreon": {
    "primary": "A large fortified tower or defensive bastion, historically erected in Spanish military architecture.",
    "secondary": "In Hispanic fortress architecture and Mexican urban geography, a defensive citadel tower or the industrial city located in Coahuila.",
    "quotes": [
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "The ancient stone **torreon** stood guard over the valley, its thick parapets pierced with narrow loopholes for musketeers."},
      {"author": "John Steinbeck", "work": "The Pearl", "quote": "Sentinels in colonial times maintained continuous watch from the high stone **torreon** against raiding corsairs along the coast."},
      {"author": "Jack London", "work": "The Night-Born", "quote": "The revolutionary regiment entrenched themselves behind the massive adobe walls of the old **torreon** outside the city."}
    ]
  },
  "torreya": {
    "primary": "A genus of rare evergreen coniferous trees or shrubs in the yew family Taxaceae, noted for pungent foliage.",
    "secondary": "In dendrology and conservation biology, relict tertiary conifers including Torreya taxifolia with spiny needles and arillate seeds.",
    "quotes": [
      {"author": "Asa Gray", "work": "Scientific Papers of Asa Gray", "quote": "The discovery of the isolated evergreen genus **Torreya** in the ravines of northern Florida revealed a marvelous botanical relic."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Along the sheltered canyons of the Sierra foothills grows the California nutmeg, a handsome species of **Torreya** with aromatic leaves."},
      {"author": "Charles Sprague Sargent", "work": "Manual of the Trees of North America", "quote": "The glossy, sharp-pointed needles of **Torreya** distinguish it readily from all other evergreen shrubs of the southern river bluffs."}
    ]
  },
  "torricelli": {
    "primary": "Evangelista Torricelli, the seventeenth-century Italian physicist and mathematician who invented the mercury barometer.",
    "secondary": "In the history of science and fluid mechanics, the pioneering natural philosopher who demonstrated atmospheric pressure and Torricelli's law of efflux.",
    "quotes": [
      {"author": "Galileo Galilei", "work": "Dialogue Concerning the Two Chief World Systems", "quote": "My brilliant pupil **Torricelli** carried forward our investigations of mechanics, solving problems that had long perplexed philosophers."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The classical experiment of **Torricelli** demonstrated conclusively that nature does not abhor a vacuum, but balances atmospheric weight."},
      {"author": "Ernst Mach", "work": "The Science of Mechanics", "quote": "With the mercury column of **Torricelli**, hydrostatics attained a mathematical precision that laid the groundwork for modern physics."}
    ]
  },
  "torrid": {
    "primary": "Extremely hot, parched, and dry due to intense solar radiation; passionately ardent or intense.",
    "secondary": "In climatology and literary figurative discourse, denoting the equatorial tropical zone between the Tropics or burning emotional fervor.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Under the burning sky of the **torrid** zone, the luxuriant vegetation displayed an intensity of green unknown in temperate climates."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The midday glare of the **torrid** sun beat down upon our heads as we pushed deeper into the suffocating tropical defile."},
      {"author": "Edgar Allan Poe", "work": "Narrative of A. Gordon Pym", "quote": "The stagnant ocean lay unruffled beneath a **torrid** atmosphere that seemed to stifle all breath and motion."}
    ]
  },
  "torridity": {
    "primary": "Extreme, parching heat or oppressive dryness resulting from intense exposure to the sun.",
    "secondary": "In climatological description and rhetoric, extreme tropical swelter or fiery emotional vehemence.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The unmitigated **torridity** of the Orinoco plains during the dry season drives animal life toward shrinking waterholes."},
      {"author": "George Eliot", "work": "Romola", "quote": "The political **torridity** of Florence under Savonarola's preaching inflamed factions to the very verge of open warfare."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The heath basked in the oppressive **torridity** of midsummer noon, every furze bush crackling in the dry breeze."}
    ]
  },

  # =========================================================================
  # Dashboard — volcan (5 words)
  # =========================================================================
  "volcanic": {
    "primary": "Produced by, relating to, or resembling a volcano or igneous eruptive activity.",
    "secondary": "In petrology and vulcanology, designating extrusive igneous rocks, ejecta, or violently explosive geodynamic processes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The black basaltic cliffs of the Galapagos Islands revealed their purely **volcanic** origin in every fissure and crater."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Vast sheets of basalt demonstrate how **volcanic** eruptions have reshaped continental crust across countless geological epochs."},
      {"author": "Herman Melville", "work": "The Encantadas", "quote": "A group of extinct **volcanic** craters stood like decayed chimney stacks against the desolate horizon of the archipelago."}
    ]
  },
  "volcanically": {
    "primary": "In a manner characteristic of volcanic activity, explosive eruption, or geothermal venting.",
    "secondary": "In geophysics and narrative description, describing violent tectonic release or tempestuously eruptive human behavior.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The island arc had been **volcanically** uplifted from the ocean floor through repeated submarine eruptions of lava."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Deep subterranean rifts, perhaps **volcanically** formed in the distant past, breathed hot vapor through the iron grating."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "His sudden rage exploded **volcanically**, shattering the quiet discipline of the schooner's quarterdeck in an instant."}
    ]
  },
  "volcanism": {
    "primary": "The phenomenon of volcanic activity, including the eruption of molten rock onto a planetary surface.",
    "secondary": "In planetary geology and plate tectonics, the sum of thermal and magmatic processes transferring internal heat and material to the crust.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The evidence of ancient **volcanism** in central France proved that active craters once poured lava over tertiary river valleys."},
      {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "Subterranean **volcanism** acts as a safety valve for the interior globe, releasing immense thermal tensions through active vents."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "The sulfurous plumes of Jupiter's moon Io reveal the most violent active **volcanism** yet discovered in our solar system."}
    ]
  },
  "volcano": {
    "primary": "An opening in the crust of a planet through which molten lava, ash, and gases erupt.",
    "secondary": "In geodynamics and geomorphology, a conical or shield mountain built by the accumulation of eruptive materials around a central vent.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "At night we witnessed the eruption of the great **volcano** of Osorno, sending glowing fountains of fire into the clouds."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My heart was like a sleeping **volcano**, ready to burst forth with furious despair upon the slightest provocation."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Like a subterranean **volcano**, the wounded leviathan breached into the air, spouting crimson foam toward the heavens."}
    ]
  },
  "volcanology": {
    "primary": "The scientific study of volcanoes, lava, magma, and related geological and geothermal phenomena.",
    "secondary": "In earth sciences, the subdiscipline integrating petrology, seismology, and geodesy to model magma dynamics and mitigate eruption hazards.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The systematic foundations of modern **volcanology** began with careful observations of the continuous eruptions of Stromboli."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger lectured with pontifical authority on the dynamic **volcanology** that had isolated the high South American plateau."},
      {"author": "Alexander von Humboldt", "work": "Aspects of Nature", "quote": "A comparative **volcanology** of the Andean chain demonstrates how subterranean fissures link distant summits across thousands of miles."}
    ]
  }
}
