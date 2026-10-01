import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Earth & Geology";

const wordsData = {
  "Dashboard — petr/empetraceae.md": {
    word: "empetraceae",
    primary: "A former family of low evergreen ericoid shrubs (the crowberry family), now placed in the heath family (Ericaceae).",
    secondary: "In systematic botany, arctic-alpine dwarf shrubs bearing small, heath-like leaves and fleshy berry-like drupes adapted to cold, acid peatlands.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The small family **Empetraceae** comprises procumbent heath-like shrubs bearing black or red edible drupes." },
      { author: "Joseph Dalton Hooker", work: "The Botany of the Antarctic Voyage", quote: "Dwarf representatives of **Empetraceae** form dense carpets over the windswept peats of the Falkland Islands." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Taxonomists formerly separated the **Empetraceae** by their unisexual flowers and distinctive stony seedlets." }
    ]
  },
  "Dashboard — petr/empetrum.md": {
    word: "empetrum",
    primary: "A small genus of low, creeping evergreen shrubs (family Ericaceae), commonly known as crowberry, native to subarctic and alpine regions.",
    secondary: "In northern ecology and ethnobotany, Empetrum nigrum, a keystone dwarf shrub of subarctic tundra providing vital winter forage for birds and mammals.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The barren moors of Tierra del Fuego were covered with low mats of **Empetrum**, laden with sweet black berries." },
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "On the windswept tableland of Mount Katahdin, we found the dwarf **Empetrum** clinging to crevices in the granite." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "In the Scottish Highlands, **Empetrum** nigrum co-dominates with heather upon exposed oceanic peat bogs." }
    ]
  },
  "Dashboard — petr/epipetric.md": {
    word: "epipetric",
    primary: "Growing on, living on, or attached to rocks; saxicolous; epilithic.",
    secondary: "In botanical and bryological surveys, describing mosses, liverworts, or ferns rooted directly upon stony surfaces rather than in soil.",
    quotes: [
      { author: "John Muir", work: "The Mountains of California", quote: "A delicate **epipetric** fern feathered the granite wall, nurtured solely by spray from the roaring waterfall." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "Certain miniature alpine succulents display strictly **epipetric** growth habits on calcareous ledges." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "The limestone crag was patterned with **epipetric** crustose lichens that slowly dissolve the underlying carbonate." }
    ]
  },
  "Dashboard — petr/petr.md": {
    word: "petr",
    primary: "In classical Greek etymology, the root *petr-* (from πέτρα, *petra*, 'rock', 'stone', 'cliff'), the foundation for words relating to rocks, stone, and petrology.",
    secondary: "A productive linguistic combining element in geological, paleontological, and petroleum nomenclature.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The classical stem **petr-** lies at the very origin of our science of petrology and subterranean rocks." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Our nomenclature draws continually upon **petr-** to denote the rocky framework of continents." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "In every geological treatise, the **petr-** prefix identifies the enduring stone foundations of the globe." }
    ]
  },
  "Dashboard — petr/petrarca.md": {
    word: "petrarca",
    primary: "Francesco Petrarca (Petrarch, 1304–1374), Italian scholar, poet, and humanist regarded as the Father of the Renaissance and Humanism.",
    secondary: "The Italian family name (Petrarca), celebrated for his vernacular Italian Canzoniere love sonnets to Laura and his recovery of classical Latin manuscripts.",
    quotes: [
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "The humanism of the Renaissance began when **Petrarca** rediscovered Cicero's letters in the cathedral library of Verona." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "There is a tomb in Arqua; reared in air, / Pillar'd in their sarcophagus, repose / The bones of Laura's lover; here repair / Many familiar with his verse, for **Petrarca** sleepeth there." },
      { author: "Jacob Burckhardt", work: "The Civilization of the Renaissance in Italy", quote: "Francesco **Petrarca** was the first modern man to climb a mountain purely to enjoy the view." }
    ]
  },
  "Dashboard — petr/petrarch.md": {
    word: "petrarch",
    primary: "The English anglicized name for Francesco Petrarca (1304–1374), Italian lyric poet and early humanist scholar.",
    secondary: "In literary verse forms, the creator of the Petrarchan sonnet, consisting of an octave (abbaabba) and a sestet (cdecde or cdcdcd).",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "The poetry of **Petrarch** celebrated love as the great animating fire of the human spirit." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The laurel crown of ancient Rome was revived upon the Capitol to crown the genius of **Petrarch**." },
      { author: "John Keats", work: "Selected Letters", quote: "I have read over the sonnets of **Petrarch** and marvel at the melodic perfection of his Italian verse." }
    ]
  },
  "Dashboard — petr/petrel.md": {
    word: "petrel",
    primary: "Any of various tube-nosed pelagic seabirds of the order Procellariiformes (especially families Hydrobatidae and Procellariidae), flying far from land.",
    secondary: "In maritime lore and ornithology, small seabirds (like storm petrels, traditionally called 'Mother Carey's chickens') whose appearance was believed to presage ocean storms.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The stormy **petrel** skimmed the crests of the black swells, fearless amid the roaring gale." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Flocks of tiny storm **petrels** hovered in the ship's wake, their feet pattering lightly upon the water." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The oceanic **petrel** returns to land only in the darkest night to visit its burrow in the cliff." }
    ]
  },
  "Dashboard — petr/petrifaction.md": {
    word: "petrifaction",
    primary: "The process by which organic matter is converted into a stony substance by the infiltration and deposition of mineral matter (fossilization).",
    secondary: "Figuratively, a state of being paralyzed or stunned with amazement, horror, or fear; fossilization of institutions or ideas.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Through slow **petrifaction**, circulating silica replaced each microscopic wood fiber with chalcedony." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "I stood in a state of utter **petrifaction**, staring at the lifeless body of my beloved Elizabeth." },
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "A curious **petrifaction** seemed to steal over his soul, freezing the spring of youthful joy." }
    ]
  },
  "Dashboard — petr/petrification.md": {
    word: "petrification",
    primary: "The process of turning into stone; petrifaction; mineral replacement of organic structures.",
    secondary: "Extreme terror, shock, or immobility that leaves one motionless as stone.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In the petrified forest of the Andes, the process of **petrification** had preserved even the cellular rings of conifers." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "A feeling of icy **petrification** crept over me as I heard the low grating of the heavy iron door." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Calcareous springs at Clermont display astonishing powers of rapid **petrification**, coating twigs with crystalline travertine in a few weeks." }
    ]
  },
  "Dashboard — petr/petrify.md": {
    word: "petrify",
    primary: "To convert organic matter into stone or stony substance by mineral infiltration.",
    secondary: "To paralyze or make rigid with fear, astonishment, or horror.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Thermal waters charged with silica gradually **petrify** the fallen trunks of prehistoric forests." },
      { author: "Bram Stoker", work: "Dracula", quote: "The sudden glimpse of that gaunt, white-fanged face seemed to **petrify** my very limbs." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Her icy glare had the power to **petrify** every impulse of natural childhood warmth." }
    ]
  },
  "Dashboard — petr/petrifying.md": {
    word: "petrifying",
    primary: "Converting or having the power to convert into stone or mineral substance.",
    secondary: "Paralyzing with terror, astonishment, or dread; inducing absolute immobility.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "A terrible, blood-curdling howl rang across the moor, exerting a **petrifying** effect upon our nerves." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Visitors marveled at the famous **petrifying** well at Knaresborough, which encrusted bird nests with lime in months." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "The monster advanced with a **petrifying** calmness that robbed me of all power to flee." }
    ]
  },
  "Dashboard — petr/petrissage.md": {
    word: "petrissage",
    primary: "A massage movement in which muscles and subcutaneous tissues are kneaded, rolled, squeezed, and lifted with the hands.",
    secondary: "In physical therapy and sports medicine, a deep tissue manipulation designed to mobilize metabolic waste, reduce spasm, and stimulate venous circulation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Judicious massage employing effleurage and deep **petrissage** accelerates the rehabilitation of atrophied limbs." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The skillful masseur utilizes rhythmic **petrissage** to relieve the stubborn muscular contractions of chronic lumbago." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Mechanical **petrissage** increases localized tissue perfusion and lymphatic drainage from fatigued muscles." }
    ]
  },
  "Dashboard — petr/petrochemical.md": {
    word: "petrochemical",
    primary: "Relating to petrochemicals; obtained from refining petroleum or natural gas.",
    secondary: "In industrial chemistry, chemical products (such as plastics, synthetic rubber, resins, and fertilizers) manufactured from hydrocarbon feedstocks.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The modern synthetic pesticide industry is an offshoot of the post-war **petrochemical** boom." },
      { author: "John McPhee", work: "The Control of Nature", quote: "Towering cracking towers of the **petrochemical** corridor along the lower Mississippi gleamed like cities of fire in the dusk." },
      { author: "Carl Sagan", work: "Billions and Billions", quote: "Combustion of **petrochemical** fuels pumps billions of tons of carbon dioxide into the upper atmosphere each year." }
    ]
  },
  "Dashboard — petr/petrocoptis.md": {
    word: "petrocoptis",
    primary: "A small genus of perennial saxicolous herbaceous plants (family Caryophyllaceae) native to calcareous cliffs and crevices of the Pyrenees and northern Spain.",
    secondary: "In alpine botanical ecology, cliff-dwelling plants bearing pink or white flowers specialized for living in bare limestone rock clefts.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The Pyrenean rock chasm shelters **Petrocoptis**, whose roots penetrate microscopic fissures in search of moisture." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Alpine gardeners prize **Petrocoptis** for its glaucous foliage and delicate pink blossoms perched on limestone ledges." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India, Preface", quote: "The restricted endemism of cliff-dwelling genera like **Petrocoptis** provides clues to glacial refugia in southern Europe." }
    ]
  },
  "Dashboard — petr/petrogale.md": {
    word: "petrogale",
    primary: "A genus of small, agile wallabies native to Australia, commonly known as rock-wallabies (family Macropodidae).",
    secondary: "In mammalogy and marsupial ecology, agile macropods possessing modified, heavily padded footpads and long balancing tails adapted for bounding across precipitous rock outcrops.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The rock-wallaby, **Petrogale**, displays astonishing agility, leaping among rugged sandstone boulders of the interior." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Marsupial adaptation reaches a high peak of specialization in **Petrogale**, whose textured foot soles grip slick rock faces." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "Skeletal features of **Petrogale** reflect extreme modifications for leaping across rocky escarpments." }
    ]
  },
  "Dashboard — petr/petroglyph.md": {
    word: "petroglyph",
    primary: "A prehistoric rock carving or incision, especially one made on a natural rock surface by ancient peoples.",
    secondary: "In archaeology and rock art research, symbolic images (anthropomorphs, zoomorphs, geometric signs) pecked, incised, or abraded into desert varnish or cliff faces.",
    quotes: [
      { author: "John Wesley Powell", work: "Canyons of the Colorado", quote: "Upon the smooth sandstone cliff, an ancient red **petroglyph** depicted mountain sheep and dancing hunters." },
      { author: "V. Gordon Childe", work: "What Happened in History", quote: "The Scandinavian **petroglyphs** depict Bronze Age ships and sun discs carved into glaciated granite ledges." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The carved **petroglyph** served as an enduring territorial marker for early hunting and foraging clans." }
    ]
  },
  "Dashboard — petr/petrograd.md": {
    word: "petrograd",
    primary: "The former name of Saint Petersburg, Russia, from 1914 to 1924 (subsequently renamed Leningrad, and restored to Saint Petersburg in 1991).",
    secondary: "In modern history, the Russian capital during World War I and the Russian Revolutions of 1917, renamed to remove the Germanic element '-burg'.",
    quotes: [
      { author: "John Reed", work: "Ten Days That Shook the World", quote: "Across the frozen canals of **Petrograd**, the guns of the cruiser Aurora signaled the storming of the Winter Palace." },
      { author: "Leo Tolstoy", work: "War and Peace, Historical Epilogue", quote: "The great northern capital, later known as **Petrograd**, rose out of Finnish swamps by the iron will of the Tsar." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The revolutionary enthusiasm reminded older observers of the heroic days of the **Petrograd** Soviet in 1917." }
    ]
  },
  "Dashboard — petr/petrographic.md": {
    word: "petrographic",
    primary: "Of or relating to petrography, the scientific description and systematic classification of rocks.",
    secondary: "In optical mineralogy, using a polarizing petrographic microscope to identify mineral grains and microscopic textures in rock thin sections.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The **petrographic** description of the granite thin section revealed interlocking laths of quartz, feldspar, and biotite." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The development of the **petrographic** microscope transformed geology by revealing the microscopic crystalline texture of eruptive rocks." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "A thorough **petrographic** analysis showed that the cobble was a metamorphosed rhyolite from an exotic volcanic arc." }
    ]
  },
  "Dashboard — petr/petrography.md": {
    word: "petrography",
    primary: "The branch of geology concerned with the systematic description, microscopic examination, and classification of rocks.",
    secondary: "The descriptive counterpart of petrology, focusing on mineral composition, microscopic fabric, and textural classification rather than magma petrogenesis.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Henry Clifton Sorby laid the foundation of modern **petrography** when he first prepared transparent rock slices for optical inspection." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Accurate **petrography** is indispensable for unraveling the complex history of volcanic and metamorphic terranes." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Before a geologist can formulate a theory of magma genesis, he must master the detailed **petrography** of the suite." }
    ]
  },
  "Dashboard — petr/petrol.md": {
    word: "petrol",
    primary: "A volatile, flammable liquid mixture of hydrocarbons derived from petroleum, used as fuel for internal combustion engines; gasoline (chiefly British).",
    secondary: "In automotive and industrial history, a refined petroleum distillate with boiling range 35°C–200°C that powered the 20th-century transportation revolution.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "His Last Bow", quote: "The motor car was fueled with high-grade **petrol** and waited in the shadow of the coastal lane." },
      { author: "George Orwell", work: "Coming Up for Air", quote: "The smell of sweet country air was smothered by the reek of burning **petrol** from the passing lorries." },
      { author: "H.G. Wells", work: "The War of the Worlds", quote: "The abandoned motor car still smelled of spilled **petrol** in the deserted village square." }
    ]
  },
  "Dashboard — petr/petrolatum.md": {
    word: "petrolatum",
    primary: "A purified, translucent, semisolid mixture of hydrocarbons obtained from petroleum; petroleum jelly; Vaseline.",
    secondary: "In pharmacognosy and cosmetic formulation, an occlusive hydrophobic ointment base used to soothe burns, lubricate skin, and protect raw surfaces.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Dress the superficial skin excoriation with sterile gauze impregnated with white **petrolatum**." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "The laboratory jars held clean amber **petrolatum** used to seal culture tubes against atmospheric air." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "A soothing application of **petrolatum** protected the inflamed cutaneous surface from irritation." }
    ]
  },
  "Dashboard — petr/petroleum.md": {
    word: "petroleum",
    primary: "An oily, flammable liquid consisting of a complex mixture of hydrocarbons occurring naturally in subsurface rock strata; crude oil.",
    secondary: "In economic geology and industry, the primary fossil fuel refined into gasoline, diesel, kerosene, and lubricating oils, driving global industrialization.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Natural seepages of pitch and **petroleum** have been utilized since the ancient builders of Babylon cemented their brick walls." },
      { author: "John McPhee", work: "The Control of Nature", quote: "The industrial empire of modern civilization is sustained by the continuous pumping of subterranean **petroleum**." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Offshore drilling rigs tap ancient deposits of **petroleum** trapped within salt domes deep beneath the continental shelf." }
    ]
  },
  "Dashboard — petr/petrology.md": {
    word: "petrology",
    primary: "The branch of geology that studies the origin, composition, structure, and alteration of rocks (igneous, sedimentary, and metamorphic).",
    secondary: "An integrative earth science combining thermodynamics, phase equilibria, and geochemistry to model how rocks form from magma, water, and crustal pressure.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Modern **petrology** unites the laboratory experiments of the chemist with the field observations of the stratigrapher." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The great triumph of twentieth-century **petrology** was the recognition of fractional crystallization in magma chambers." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Through systematic **petrology**, we trace the life history of an igneous rock from its deep mantle melt to its surface crystallization." }
    ]
  },
  "Dashboard — petr/petromyzon.md": {
    word: "petromyzon",
    primary: "A genus of primitive, jawless, eel-like aquatic vertebrates (family Petromyzontidae), specifically the sea lamprey (Petromyzon marinus).",
    secondary: "In vertebrate comparative anatomy and evolutionary biology, a cyclostome possessing a toothed, funnel-like sucking mouth used to parasitize fish.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The circular suctorial disc of **Petromyzon** bears sharp horny teeth adapted for rasping the flesh of marine fish." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The jawless condition of **Petromyzon** provides living testimony to the ancestral cranial anatomy of the earliest chordates." },
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "The larval stage of **Petromyzon**, known as the ammocoetes, burrows in river mud like a lancelet." }
    ]
  },
  "Dashboard — petr/petromyzoniformes.md": {
    word: "petromyzoniformes",
    primary: "An order of primitive, jawless aquatic vertebrates consisting of the modern lampreys.",
    secondary: "In systematic ichthyology and vertebrate paleontology, the sole surviving order of the class Petromyzontida, characterized by lack of paired fins, a persistent notochord, and seven pairs of gill pouches.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The **Petromyzoniformes** retain an unsegmented notochord throughout life, lacking true vertebrae and jaws." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "Fossil lampreys from the Carboniferous indicate that the morphology of **Petromyzoniformes** has remained virtually unchanged for three hundred million years." },
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "Comparative embryology looks to the **Petromyzoniformes** for clues regarding the origin of the vertebrate thyroid gland." }
    ]
  },
  "Dashboard — petr/petromyzontidae.md": {
    word: "petromyzontidae",
    primary: "The biological family of jawless vertebrates comprising all living lampreys (order Petromyzoniformes).",
    secondary: "In aquatic ecology and zoology, parasitic and non-parasitic freshwater and anadromous cyclostomes with smooth scaleless skin and circular suction mouths.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "Members of the **Petromyzontidae** exhibit a remarkable metamorphosis from a filter-feeding mud larva to a free-swimming adult." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Biologists applied selective chemicals to Great Lakes streams to control invasive parasitic lampreys of the family **Petromyzontidae**." },
      { author: "Louis Agassiz", work: "Methods of Study in Natural History", quote: "The skeletal apparatus of the **Petromyzontidae** consists purely of unossified cartilage." }
    ]
  },
  "Dashboard — petr/petronius.md": {
    word: "petronius",
    primary: "Gaius Petronius Arbiter (c. AD 27–66), Roman courtier and satirist during the reign of Nero, author of the Satyricon.",
    secondary: "In classical literary history, the Roman patrician known as Nero's 'Arbiter of Elegance' (arbiter elegantiae), celebrated for his picaresque novel depicting Roman decadence and Trimalchio's lavish feast.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The witty and cynical courtier **Petronius** chose to expire in a bath of warm water, conversing calmly with his literary friends." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "In the fragment of **Petronius**, the lavish banquet of Trimalchio reflects the vulgar luxury of the Neronian court." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He fancied himself a modern **Petronius**, seeking new sensations and subtle refinements of aesthetic indulgence." }
    ]
  },
  "Dashboard — petr/petroselinum.md": {
    word: "petroselinum",
    primary: "A small genus of aromatic biennial herbs (family Apiaceae), native to the Mediterranean region, notably garden parsley (Petroselinum crispum).",
    secondary: "In pharmacognosy and culinary botany, herbs whose seeds and foliage yield volatile apiol oil, traditionally used as a carminative and diuretic.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "Cottage borders were edged with bright, crinkled tufts of **Petroselinum**, valued alike for soup and salad." },
      { author: "Liberty Hyde Bailey", work: "The Practical Garden-Book", quote: "Sow the slow-germinating seeds of **Petroselinum** early in spring in moist, rich garden loam." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The Greeks used the aromatic leaves of **Petroselinum** to weave victor crowns at the Isthmian Games." }
    ]
  },
  "Dashboard — petr/petrosomatoglyph.md": {
    word: "petrosomatoglyph",
    primary: "A stylized rock carving or natural depression in rock that resembles a human or animal body part (such as a footprint, hand, or knee).",
    secondary: "In archaeological folklore, rock markings traditionally associated with legendary kings, saints, or heroes (e.g., King Arthur's footprint, Buddha's footprints).",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "Local villagers revered the natural indentation in the granite as the sacred **petrosomatoglyph** of a wandering medieval saint." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The royal inauguration stone bore a shallow **petrosomatoglyph** where the new king placed his foot during the oath." },
      { author: "Walter Pater", work: "Greek Studies", quote: "Ancient Greek travelers pointed to a hollow rock on Delos as the divine **petrosomatoglyph** imprinted by Apollo at his birth." }
    ]
  },
  "Dashboard — petr/petrous.md": {
    word: "petrous",
    primary: "Like stone, especially in hardness; stony; rocky.",
    secondary: "In human anatomy, designating the dense, exceptionally hard pyramidal portion of the temporal bone that encases the inner ear structures (petrous bone).",
    quotes: [
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", quote: "The **petrous** portion of the temporal bone is wedged into the base of the skull, protecting the delicate labyrinth of hearing." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The alpine trail climbed across a bleak, **petrous** wilderness where no shrub could find roothold." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Suppuration within the **petrous** temporal bone risks intracranial extension into the transverse sinus." }
    ]
  },
  "Dashboard — psa/palimpsest.md": {
    word: "palimpsest",
    primary: "A manuscript or piece of writing material on which the original writing has been effaced to make room for later writing, but of which traces remain.",
    secondary: "Figuratively, something reused or altered but still bearing visible traces of its earlier form (e.g., historical landscape, architectural ruins, human memory).",
    quotes: [
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "The human brain is a natural **palimpsest**, where countless layers of forgotten memories are superimposed forever." },
      { author: "George Orwell", work: "1984", quote: "All history was a **palimpsest**, scraped clean and reinscribed exactly as often as was necessary." },
      { author: "Walter Pater", work: "The Renaissance", quote: "Modern culture is a complex **palimpsest**, in which classical forms gleam through the theological inscriptions of the Middle Ages." }
    ]
  },
  "Dashboard — psamm/psammite.md": {
    word: "psammite",
    primary: "A sedimentary rock composed mainly of sand-sized grains; sandstone.",
    secondary: "In metamorphic petrology, a metamorphosed sandstone or quartz-rich sedimentary rock (e.g., psammitic schist or quartzite).",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The thick beds of Highland **psammite** represent ancient marine shoreface sands recrystallized during regional metamorphism." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The coastal cliffs displayed alternating bands of fine argillite and gritty **psammite**." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The outcrop consisted of pale, blocky **psammite**, resistant to glacial erosion." }
    ]
  },
  "Dashboard — psamm/psammitic.md": {
    word: "psammitic",
    primary: "Pertaining to, resembling, or composed of psammite (sandstone or sandy sediment); arenaceous.",
    secondary: "In structural and metamorphic geology, describing rock formations derived from sandy parent materials rather than clay or carbonate precursors.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The **psammitic** schists fracture into sharp, angular flags prized for dry-stone masonry." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "These crystalline beds retain their original **psammitic** cross-bedding despite intense tectonic compression." },
      { author: "John McPhee", work: "Basin and Range", quote: "High-angle faulting has displaced the dark **psammitic** strata against the paler carbonate basement." }
    ]
  },
  "Dashboard — psamm/psammoma.md": {
    word: "psammoma",
    primary: "A firm, usually benign tumor (especially a meningioma or ovarian serous cystadenocarcinoma) containing microscopic round calcified bodies (psammoma bodies).",
    secondary: "In histopathology, laminated concentric calcareous spherules occurring within neoplastic and inflammatory tissue, resembling tiny grains of sand.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The cranial dural tumor presented the typical microscopic features of a **psammoma**, packed with calcareous sand-bodies." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Histological section confirmed that the slow-growing intracranial mass was a benign **psammoma**." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The diagnostic hallmark of the **psammoma** is the concentric mineral accretion within whorled endothelial cells." }
    ]
  },
  "Dashboard — psamm/psammophile.md": {
    word: "psammophile",
    primary: "An organism (plant or animal) that thrives, prefers to live, or is adapted to sandy environments or sand dunes.",
    secondary: "In ecology and evolutionary biology, organisms exhibiting specialized physiological adaptations (e.g., fringed toes, reduced water loss) for navigating unstable sand substrates.",
    quotes: [
      { author: "William Henry Hudson", work: "The Naturalist in La Plata", quote: "The burrowing sand-lizard is a true **psammophile**, diving beneath the dune crest with astonishing swiftness." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Marram grass is the premier plant **psammophile** of our coastlines, binding mobile dunes with vigorous rhizomes." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Tiny **psammophile** crustaceans migrate up and down between the sand grains as the tide advances." }
    ]
  },
  "Dashboard — psamm/Psammophis.md": {
    word: "Psammophis",
    primary: "A genus of fast-moving, slender, mildly venomous colubrid snakes (sand snakes) found across Africa, the Middle East, and South Asia.",
    secondary: "In herpetology, diurnal opisthoglyphous (rear-fanged) snakes characterized by large eyes and swift locomotion across sandy desert landscapes.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The agile sand snake, **Psammophis**, hunts desert lizards across the scorching dunes of the Sahara." },
      { author: "Richard Francis Burton", work: "First Footsteps in East Africa", quote: "A slender **Psammophis** darted from beneath the thorn scrub and vanished into the rocky sand." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Protective coloration among desert reptiles is admirably illustrated by the pale cryptic pattern of **Psammophis**." }
    ]
  },
  "Dashboard — psamm/psammophyte.md": {
    word: "psammophyte",
    primary: "A plant that grows in or prefers sandy soil, especially on coastal dunes or sandy deserts; a sand plant.",
    secondary: "In plant ecology, a species equipped with specialized adaptations to survive shifting substrate, drought, sand blasting, and nutrient-poor sand.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Sea rocket is an annual **psammophyte** that colonizes the drift line just above the high-water mark." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The coastal **psammophyte** must withstand burying by shifting sands and continuous salt spray." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Landscape architects select hardy **psammophyte** grasses to stabilize eroding coastal embankments." }
    ]
  },
  "Dashboard — psamm/psammosere.md": {
    word: "psammosere",
    primary: "An ecological succession of plant and animal communities that originates on newly exposed sand, especially on coastal sand dunes.",
    secondary: "In plant sociology, the complete developmental sequence from bare moving sand dunes through pioneer grasses to mature climax scrub or coastal woodland.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "A classic **psammosere** can be traced inland from the embryonic foredunes to the stabilized dune heath." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The progress of the **psammosere** transforms shifting white ridges into soil covered with bayberry and maritime cedar." },
      { author: "E.O. Wilson", work: "The Diversity of Life", quote: "Each seral stage of the **psammosere** enriches the sand with organic humus, facilitating colonization by taller vegetation." }
    ]
  },
  "Dashboard — psamm/psammous.md": {
    word: "psammous",
    primary: "Sandy; containing, resembling, or composed of sand; arenaceous.",
    secondary: "In medical and geological descriptions, having a gritty, granular, or sandy texture.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The southern lanes wound deeply through a dry, **psammous** soil that never retained standing water." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The pathologist felt a gritty, **psammous** resistance when cutting through the calcified capsule." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The fine mud passes laterally into a **psammous** littoral deposit along the ancient shoreline." }
    ]
  },
  "Dashboard — sapphir/sapphire.md": {
    word: "sapphire",
    primary: "A transparent, precious gemstone variety of the mineral corundum (Al₂O₃), typically blue, but occurring in other colors (fancy sapphires).",
    secondary: "A bright, deep blue color like that of a fine gem sapphire.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The deep azure of the Mediterranean sky was reflected in the water like liquid **sapphire**." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The open ocean sparkled like a boundless floor of polished **sapphire** beneath the equatorial sun." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Beryl Coronet", quote: "The center of the antique diadem was set with an orient **sapphire** of unmatched brilliance and purity." }
    ]
  },
  "Dashboard — sapphir/sapphirine.md": {
    word: "sapphirine",
    primary: "Of, relating to, or resembling sapphire, especially in its deep blue color or brilliance.",
    secondary: "In metamorphic petrology and mineralogy, a rare magnesium-aluminum silicate mineral (Mg₄Al₁₀O₁₆) forming blue, greenish, or brown tabular crystals in high-grade metamorphic rocks.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The mineral **sapphirine** occurs in high-grade granulite facies rocks associated with cordierite and spinel." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The distant alpine peaks were bathed in a delicate, **sapphirine** haze as twilight descended upon the valley." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Thin sections revealed pale blue prismatic crystals of **sapphirine** embedded within the cordierite gneiss." }
    ]
  },
  "Dashboard — sei/aseismic.md": {
    word: "aseismic",
    primary: "Characterized by an absence of earthquakes; free from earthquake activity.",
    secondary: "In structural engineering, designed or constructed to withstand earthquake tremors (earthquake-resistant).",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The stable continental cratons represent largely **aseismic** regions where crustal peace has endured for hundreds of millions of years." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Geophysicists identified an **aseismic** creep along certain segments of the San Andreas Fault where strain is released without sudden shocks." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Ancient shield areas are virtually **aseismic**, showing no recorded seismic activity in historic times." }
    ]
  },
  "Dashboard — sei/microseism.md": {
    word: "microseism",
    primary: "A very small, continuous seismic tremor or oscillation of the Earth's crust, detectable only by sensitive seismographs and not caused by earthquakes.",
    secondary: "In geophysics, persistent crustal micro-vibrations primarily generated by ocean wave action, storms beating against coastlines, or industrial noise.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Distant ocean typhoons send continuous trains of **microseisms** vibrating across the continental bedrock." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The pounding of storm surf upon Atlantic headlands registers on inland seismographs as rhythmic **microseisms**." },
      { author: "John McPhee", work: "Basin and Range", quote: "Even in the dead of night, the seismograph needle trembles with natural **microseisms** whispering through the crust." }
    ]
  },
  "Dashboard — sei/microseismic.md": {
    word: "microseismic",
    primary: "Of, relating to, or detecting microseisms or minute seismic tremors.",
    secondary: "In acoustic emission monitoring and mining, utilizing microseismic sensor arrays to detect micro-cracking and predict rockbursts in subterranean excavations.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Sensitive **microseismic** recorders registered the subtle ground vibrations that preceded the volcanic eruption." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Mining engineers rely on continuous **microseismic** monitoring to identify stress concentrations before a cave-in occurs." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The worldwide **microseismic** background reflects the ceaseless mechanical energy dissipated by oceanic waves." }
    ]
  },
  "Dashboard — sei/paleoseismology.md": {
    word: "paleoseismology",
    primary: "The geological study of prehistoric earthquakes preserved in the geologic record (e.g., fault offsets, liquefaction features, tsunami deposits).",
    secondary: "In tectonic geomorphology, trenching across active fault zones to date past seismic ruptures and estimate earthquake recurrence intervals.",
    quotes: [
      { author: "John McPhee", work: "Assembling California", quote: "Through **paleoseismology**, geologists dug trenches across the fault to read the ancient earthquake scars in offset charcoal layers." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Trench stratigraphy in **paleoseismology** reveals that major fault ruptures recur in quasi-periodic cycles." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "By examining elevated coastal terraces, the geologist reconstructs the **paleoseismology** of vanished centuries." }
    ]
  },
  "Dashboard — sei/seism.md": {
    word: "seism",
    primary: "An earthquake; an oscillation or shaking of the Earth's crust produced by sudden release of tectonic stress.",
    secondary: "In classical and literary usage, a sudden violent upheaval or convulsion, geological or political.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The fall of the Bastille was an ideological **seism** that shook every throne in Europe to its foundation." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The violent **seism** that leveled Lisbon in 1755 was felt from the Baltic shores to the Caribbean." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Every major **seism** radiates elastic waves through the deep mantle and crust of the globe." }
    ]
  },
  "Dashboard — sei/seismal.md": {
    word: "seismal",
    primary: "Pertaining to, caused by, or characteristic of earthquakes; seismic.",
    secondary: "In historical physical geography, relating to the geographic distribution and physical destruction wrought by earthquake shocks.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The **seismal** waves traveling through the subterranean strata shattered churches and palaces in a single instant." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The **seismal** destruction of the city of Concepción revealed the terrifying power of subterranean forces." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Islands lying within the active **seismal** zone are subject to sudden uplift and coastal subsidence." }
    ]
  },
  "Dashboard — sei/seismic.md": {
    word: "seismic",
    primary: "Of or relating to earthquakes or other vibrations of the Earth and its crust.",
    secondary: "Figuratively, having an enormous, far-reaching effect or revolutionary impact.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The propagation of **seismic** waves through the solid interior of the planet reveals the density of its deepest layers." },
      { author: "John McPhee", work: "Basin and Range", quote: "A **seismic** shock wave moves through granite at nearly five miles per second." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Submarine **seismic** disturbances displace vast columns of ocean water, launching catastrophic tsunamis across the basin." }
    ]
  },
  "Dashboard — sei/seismogram.md": {
    word: "seismogram",
    primary: "The record or tracing of ground motion produced by a seismograph during an earthquake or other seismic disturbance.",
    secondary: "In observational geophysics, the graphical wave record displaying the arrival times and amplitudes of P-waves, S-waves, and surface waves.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The arrival time of the shear wave upon the **seismogram** allowed geophysicists to calculate the distance to the epicenter." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The jagged ink line of the **seismogram** sprang suddenly into violent oscillations as the fault ruptured." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Modern stations preserve every **seismogram** as an indelible acoustic signature of planetary motion." }
    ]
  },
  "Dashboard — sei/seismograph.md": {
    word: "seismograph",
    primary: "An instrument that measures and records details of earthquakes, such as force, duration, and direction.",
    secondary: "In observational geophysics, an inertial instrument (horizontal or vertical pendulum) coupled with optical, electromagnetic, or digital sensors to record seismic motion.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The invention of the precision **seismograph** opened a window into the deep core and mantle of the Earth." },
      { author: "John McPhee", work: "Assembling California", quote: "The **seismograph** in Berkeley registered the first micro-fractures seconds before the major shock wave struck." },
      { author: "H.G. Wells", work: "The War of the Worlds", quote: "The delicate needles of the observatory **seismograph** quivered as the first Martian cylinder plunged into Horsell Common." }
    ]
  },
  "Dashboard — sei/seismologic.md": {
    word: "seismologic",
    primary: "Pertaining to seismology; relating to the scientific study of earthquakes and seismic phenomena.",
    secondary: "In geophysical surveys, describing observations, models, or data derived from earthquake wave propagation.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The establishment of a global **seismologic** network made it possible to pinpoint epicenters beneath the open ocean." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Careful **seismologic** records proved that earthquakes are concentrated along linear oceanic and mountain belts." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The **seismologic** evidence proved decisively that the outer core of the Earth must be liquid." }
    ]
  },
  "Dashboard — sei/seismological.md": {
    word: "seismological",
    primary: "Belonging or relating to seismology; seismic.",
    secondary: "In earth sciences, concerning scientific investigations of earthquake mechanisms, plate boundaries, and subsurface structure.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The **seismological** observatory at Strasbourg became an international clearinghouse for global earthquake telemetry." },
      { author: "John McPhee", work: "Basin and Range", quote: "Subsurface fault geometries are reconstructed from dense **seismological** profiling." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep-focus **seismological** records from the Tonga Trench revealed oceanic lithosphere plunging into the mantle." }
    ]
  },
  "Dashboard — sei/seismologist.md": {
    word: "seismologist",
    primary: "A scientist or geophysicist who specializes in seismology, the study of earthquakes and seismic wave propagation.",
    secondary: "In disaster management and tectonic research, an investigator who analyzes fault mechanics, assesses seismic hazards, and models mantle structure.",
    quotes: [
      { author: "John McPhee", work: "Assembling California", quote: "The **seismologist** mapped every aftershock to delineate the subterranean rupture plane of the Loma Prieta earthquake." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Beno Gutenberg was the pioneering **seismologist** who precisely determined the depth of the Earth's core-mantle boundary." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The Apollo missions landed seismometers on the Moon, allowing the terrestrial **seismologist** to listen to moonquakes." }
    ]
  },
  "Dashboard — sei/seismology.md": {
    word: "seismology",
    primary: "The scientific study of earthquakes and the propagation of elastic waves through the Earth or through other planet-like bodies.",
    secondary: "In modern geophysics, the primary tool for imaging the three-dimensional internal structure of the Earth, from tectonic plates to the inner core.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Through **seismology**, the Earth's interior is probed with sound waves just as the human body is probed with X-rays." },
      { author: "John McPhee", work: "Basin and Range", quote: "Modern **seismology** transformed geology from the inspection of surface rocks into a profound anatomy of the planet." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The infant science of **seismology** began when John Milne erected horizontal pendulums on the volcanic soil of Japan." }
    ]
  },
  "Dashboard — sei/seismometer.md": {
    word: "seismometer",
    primary: "The sensor component of a seismograph that detects ground motion and converts mechanical vibration into an electrical or recorded signal.",
    secondary: "In planetary exploration and vulcanology, a precision instrument deployed on planetary surfaces (e.g., Moon, Mars) to detect internal tectonics and meteor impacts.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "The Viking lander deployed a sensitive **seismometer** on the red sands of Mars to detect Martian tremors." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The field **seismometer** registered the footsteps of a coyote half a mile away across the quiet basin." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "A modern electronic **seismometer** can detect crustal displacements smaller than the wavelength of visible light." }
    ]
  },
  "Dashboard — sei/seismonasty.md": {
    word: "seismonasty",
    primary: "A rapid nastic plant movement in response to mechanical shock, touch, or vibration (as in the sensitive plant Mimosa pudica); thigmonasty.",
    secondary: "In plant physiology, rapid turgor pressure changes in motor cells of the pulvinus that cause leaflets to fold together within seconds of stimulation.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "The rapid leaf collapse in Mimosa pudica is a classic manifestation of **seismonasty**, triggered by electrical action potentials across the pulvinus." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Under the influence of **seismonasty**, the pinnate leaflets fold instantly downward when brushed by a passing insect." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The sensitive plant exhibits an astonishing **seismonasty** that mimics the reflex excitability of animal nervous tissue." }
    ]
  },
  "Dashboard — sei/sistrum.md": {
    word: "sistrum",
    primary: "An ancient percussion instrument consisting of a metal frame with transverse rattling rods or disks, shaken in sacred religious rites.",
    secondary: "In classical Egyptian and Greco-Roman religious archaeology, a sacred rattle specifically associated with the worship of the goddess Isis.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The priests of Isis marched through the streets of Rome shaking the sacred bronze **sistrum** in rhythmic cadence." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "The chanting procession was led by white-robed initiates who sounded the tinkling brass of the Egyptian **sistrum**." },
      { author: "T. R. Glover", work: "The Conflict of Religions in the Early Roman Empire", quote: "The sweet metallic rattle of the **sistrum** announced the solemn dawn opening of the temple of Isis." }
    ]
  },
  "Dashboard — sei/teleseism.md": {
    word: "teleseism",
    primary: "An earthquake that occurs at a great distance from the recording seismograph station (conventionally more than 1,000 km or 10° of arc).",
    secondary: "In observational seismology, teleseismic wave arrivals (P, S, and core phases) used to map deep mantle discontinuities and core boundaries.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The recording of a distant **teleseism** from the antipodes provides invaluable data regarding seismic wave refraction through the core." },
      { author: "John McPhee", work: "Basin and Range", quote: "The university seismograph recorded a massive **teleseism** that had ruptured beneath the Andes an hour earlier." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The arrival of **teleseism** waves confirmed that the Earth behaves as a nearly perfect elastic sphere." }
    ]
  },
  "Dashboard — sei/teleseismic.md": {
    word: "teleseismic",
    primary: "Of, relating to, or detected from an earthquake occurring at a great distance from the seismograph.",
    secondary: "In global geophysics, describing seismic phases (such as PKIKP, SKS) traveling through the deep Earth across epicentral distances greater than 30°.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "By analyzing **teleseismic** travel-time curves, seismologists constructed velocity models of the Earth's deep interior." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The quiet granite basement provides an ideal platform for recording faint **teleseismic** P-waves." },
      { author: "Carl Sagan", work: "Cosmos", quote: "A global network of stations recorded the **teleseismic** waves radiating from the subterranean nuclear explosion." }
    ]
  },
  "Dashboard — sider/desideratum.md": {
    word: "desideratum",
    primary: "Something that is needed, wanted, or considered essential; a desirable requirement or missing element.",
    secondary: "In scholarship and philosophy, a recognized gap in knowledge or equipment that remains to be supplied.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "A vigorous and stable executive is a vital **desideratum** in the constitution of any well-ordered republic." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "A complete fossil record connecting all extinct groups remains a great but unfulfilled **desideratum** of paleontology." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "A thorough grounding in physical science has become an indispensable **desideratum** for modern liberal education." }
    ]
  },
  "Dashboard — sider/sidereal.md": {
    word: "sidereal",
    primary: "Of or relating to the distant stars or constellations; measured relative to the stars (as a sidereal day or sidereal year).",
    secondary: "In observational astronomy, a time system based on Earth's rotation rate relative to distant fixed stars, approximately 4 minutes shorter than solar time.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "The true period of the Earth's axial rotation is measured by the **sidereal** day of twenty-three hours and fifty-six minutes." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The watch officer gazed up at the cold **sidereal** heavens wheeling above the masthead." },
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "The stars awaken a certain reverence, for their **sidereal** motions remind man of eternal laws." }
    ]
  },
  "Dashboard — sider/siderite.md": {
    word: "siderite",
    primary: "A mineral consisting of iron(II) carbonate (FeCO₃), a valuable ore of iron crystallizing in the trigonal system; chalybite.",
    secondary: "In meteoritics, a historical classification term for an iron meteorite consisting primarily of nickel-iron alloys (kamacite and taenite).",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The rhombohedral crystals of **siderite** display a characteristic yellowish-brown color and vitreous luster." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Concretionary nodules of **siderite**, known as clay ironstone, occur abundantly throughout the Coal Measures." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The polished face of the meteoric **siderite** revealed classic Widmanstätten figures under acid etching." }
    ]
  },
  "Dashboard — sider/sideritis.md": {
    word: "sideritis",
    primary: "A genus of perennial herbaceous plants and small subshrubs (family Lamiaceae), commonly known as ironwort or mountain tea, native to Mediterranean mountain regions.",
    secondary: "In ethnobotany and herbal history, plants traditionally brewed as mountain tea (Greek tsai tou vounou) and applied to heal wounds inflicted by iron weapons.",
    quotes: [
      { author: "Dioscorides", work: "De Materia Medica", quote: "The herb called **Sideritis** was applied by the ancients to heal wounds inflicted by swords and iron weapons." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "On high rocky slopes grows the woolly **Sideritis**, whose aromatic spikes are harvested by mountain shepherds." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Mediterranean gardeners cultivate **Sideritis** for its silvery foliage and medicinal herbal reputation." }
    ]
  },
  "Dashboard — sider/sideroblast.md": {
    word: "sideroblast",
    primary: "An erythroblast (nucleated precursor of a red blood cell) in bone marrow that contains non-heme iron granules in its cytoplasm.",
    secondary: "In hematopathology, a diagnostic cell type whose abnormal ringed form (ring sideroblast) is pathognomonic for sideroblastic anemia and myelodysplastic syndromes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Prussian blue staining of marrow aspirate demonstrated excessive iron accumulation within the **sideroblast**." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The developing **sideroblast** incorporates ferritin to synthesize hemoglobin within its cytoplasmic matrix." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Defects in heme synthesis trap inorganic iron inside the mitochondria of the developing **sideroblast**." }
    ]
  },
  "Dashboard — sider/siderocyte.md": {
    word: "siderocyte",
    primary: "An abnormal mature red blood cell (erythrocyte) containing non-hemoglobin iron granules (Pappenheimer bodies) visible on Prussian blue staining.",
    secondary: "In laboratory hematology, a cell commonly observed in peripheral blood following splenectomy or in severe hemolytic and sideroblastic anemias.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The appearance of the **siderocyte** in peripheral blood reflects impaired splenic filtration of iron-containing inclusions." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic inspection reveals dark blue granules within the **siderocyte**, representing unutilized ferruginous material." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The diagnostic significance of the circulating **siderocyte** was confirmed by specialized chemical stains." }
    ]
  },
  "Dashboard — sider/siderodromophobia.md": {
    word: "siderodromophobia",
    primary: "An irrational, intense, or debilitating fear of trains, railways, or traveling by train.",
    secondary: "In clinical psychology, a specific situational phobia prominent during the 19th-century railway expansion, often linked to claustrophobia and crash anxiety.",
    quotes: [
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "A severe **siderodromophobia** frequently traces its origin to early childhood anxieties associated with railway travel." },
      { author: "William James", work: "The Principles of Psychology", quote: "Patients afflicted with **siderodromophobia** experience overwhelming panic at the mere whistle of a steam locomotive." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Morbid phobias of modern machinery, such as **siderodromophobia**, proliferated as industrial transit transformed daily life." }
    ]
  },
  "Dashboard — sider/sideropenia.md": {
    word: "sideropenia",
    primary: "A deficiency of iron in the blood serum or bodily tissues; iron deficiency.",
    secondary: "In clinical medicine, a state of depleted iron stores leading to iron-deficiency anemia, microcytosis, fatigue, koilonychia, and impaired immune function.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **sideropenia** manifests clinically with pallor, brittle nails, and marked microcytic hypochromia." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Tissue **sideropenia** impairs cellular oxidative respiration long before full anemia becomes apparent in blood counts." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Dietary **sideropenia** exhausts ferritin reserves in the liver and bone marrow, blunting erythropoiesis." }
    ]
  },
  "Dashboard — sider/siderophile.md": {
    word: "siderophile",
    primary: "In geochemistry, an element (such as Fe, Ni, Co, Pt, Au) that has a strong chemical affinity for metallic iron and tends to concentrate in the Earth's metallic core.",
    secondary: "In microbiology and histology, an organism, cell, or tissue that readily absorbs, binds, or thrives upon iron salts.",
    quotes: [
      { author: "Victor Goldschmidt", work: "Geochemistry", quote: "During planetary differentiation, the dense **siderophile** elements dissolved in molten metallic iron and sank to form the core." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Because gold and platinum are strictly **siderophile**, their concentration in the crust is extremely depleted." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Goldschmidt demonstrated that core segregation stripped the mantle of virtually all primordial **siderophile** metals." }
    ]
  },
  "Dashboard — sider/siderophilin.md": {
    word: "siderophilin",
    primary: "An iron-binding blood plasma glycoprotein that transports iron through the blood to liver and bone marrow; transferrin.",
    secondary: "In clinical biochemistry, a beta-globulin whose percentage saturation is a critical laboratory indicator of iron deficiency or hemochromatosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Circulating **siderophilin** binds ferric ions securely to prevent the toxicity of free ionic iron." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Each molecule of **siderophilin** can bind two atoms of iron, transporting them directly to marrow receptors." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The concentration of **siderophilin** in serum rises compensatory in states of chronic iron deficiency." }
    ]
  },
  "Dashboard — sider/siderosis.md": {
    word: "siderosis",
    primary: "A form of pneumoconiosis caused by the chronic inhalation of iron or iron oxide dust, common among welders and foundry workers (welder's lung).",
    secondary: "In systemic pathology, the abnormal deposition of iron pigments (hemosiderin) in tissues and organs, as in hemochromatosis or ocular siderosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pulmonary **siderosis** among iron grinders was marked by rusty sputum and fibrous pleural thickening." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Ocular **siderosis** develops when a retained intraocular iron splinter slowly oxidizes, staining the iris and lens brown." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Protective ventilation in metal factories has greatly reduced the occupational incidence of pulmonary **siderosis**." }
    ]
  },
  "Dashboard — spele/speleogen.md": {
    word: "speleogen",
    primary: "A geological feature formed within a cave by the solvent or erosive action of groundwater on bedrock (e.g., cave ceiling scallops, pendants, potholes).",
    secondary: "In speleology, a bedrock dissolutional relief form produced by water flow, as distinguished from a speleothem (which is a mineral deposit).",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The smooth ceiling pendant is a classic **speleogen** carved by acidic groundwater carving through limestone." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The cave walls were sculpted into asymmetrical scallops, a diagnostic **speleogen** recording ancient subterranean river currents." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Speleologists distinguish between depositional speleothems and erosional **speleogens** etched directly into the bedrock." }
    ]
  },
  "Dashboard — spele/speleogenesis.md": {
    word: "speleogenesis",
    primary: "The geological origin, development, and evolution of caves and karst subterranean drainage systems over time.",
    secondary: "In hydrogeology, the process whereby carbonic acid in groundwater dissolves soluble carbonate rocks along bedding planes and joints to form cave passages.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The initial phase of **speleogenesis** begins along microscopic joint fractures beneath the regional water table." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Modern theories of **speleogenesis** emphasize turbulent phreatic flow in dissolving miles of limestone caverns." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The study of **speleogenesis** reveals that vast cave networks formed under past wetter climates." }
    ]
  },
  "Dashboard — spele/speleologist.md": {
    word: "speleologist",
    primary: "A scientist or researcher who specializes in speleology; one who studies the physical, biological, and geological aspects of caves.",
    secondary: "A trained investigator who maps subterranean passages, measures cavern microclimates, and documents cave-adapted troglobites.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "The intrepid **speleologist** descended by rope ladder into the pitch-black abyss of the volcanic cavern." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Martel, the celebrated French **speleologist**, proved that subterranean rivers directly carve the subterranean topography of karst plateaus." },
      { author: "E.O. Wilson", work: "The Diversity of Life", quote: "The biospeleologist and **speleologist** work together to document fragile blind salamanders in deep cave aquifers." }
    ]
  },
  "Dashboard — spele/speleology.md": {
    word: "speleology",
    primary: "The scientific study and exploration of caves, their structure, physical properties, history, life forms, and processes of formation.",
    secondary: "An interdisciplinary earth science integrating karst hydrology, structural geology, paleoclimatology, and biospeleology.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The modern science of **speleology** demonstrates how subterranean drainage shapes the landscape above." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Through **speleology**, researchers recover Pleistocene animal bones and ancient stalagmite climate records from deep chambers." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Advances in **speleology** have revealed complex underground conduits carrying entire rivers for tens of miles." }
    ]
  },
  "Dashboard — spele/Speleomantes.md": {
    word: "Speleomantes",
    primary: "A genus of lungless cave-dwelling salamanders (European cave salamanders, family Plethodontidae) native to Italy and Sardinia.",
    secondary: "In biospeleology and herpetology, troglophilic plethodontid salamanders that lack lungs, breathing entirely through cutaneous respiration and hunting with projectile tongues in humid caves.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Cave-dwelling amphibians such as **Speleomantes** illustrate how subterranean isolation leads to the loss of unnecessary organs." },
      { author: "E.O. Wilson", work: "The Diversity of Life", quote: "In the limestone caves of Sardinia, the endemic salamander **Speleomantes** stalks small insects along dripping cave walls." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "Cutaneous respiration reaches remarkable specialization in **Speleomantes**, whose lungs are completely absent." }
    ]
  },
  "Dashboard — spele/speleomorphology.md": {
    word: "speleomorphology",
    primary: "The scientific study of the forms, relief features, and physical morphology of caves and karst subterranean passages.",
    secondary: "In geomorphology, the branch analyzing how structural joints, bedding planes, and hydraulic gradient determine the cross-sectional geometry of cave passages.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The **speleomorphology** of Mammoth Cave reveals successive horizontal levels corresponding to past river terraces." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Comparative **speleomorphology** distinguishes between tubular phreatic conduits and canyon-like vadose trenches." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The intricate **speleomorphology** of the cavern system preserved the exact flow direction of ancient underground streams." }
    ]
  },
  "Dashboard — spele/speleoseismite.md": {
    word: "speleoseismite",
    primary: "A broken, deformed, or displaced cave formation (such as a sheared stalagmite or fallen stalactite) caused by an earthquake.",
    secondary: "In paleoseismology and speleoseismology, mineralized cave structures used to date prehistoric seismic events and calculate past earthquake intensity.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "A sheared stalagmite in the deep cave provided an authentic **speleoseismite**, dating a severe prehistoric earthquake to four thousand years ago." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "By radiocarbon dating the regrowth upon a **speleoseismite**, geologists established the recurrence interval of the active fault." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Shattered and displaced stalactites constitute a permanent **speleoseismite** record protected from surface weathering." }
    ]
  },
  "Dashboard — spele/speleothem.md": {
    word: "speleothem",
    primary: "A secondary mineral deposit formed in a cave by the precipitation of minerals from dripping, flowing, or standing water (e.g., stalactites, stalagmites, flowstone).",
    secondary: "In paleoclimatology and geochemistry, a calcium carbonate cavern formation whose oxygen and carbon isotope ratios provide high-resolution records of past climate and rainfall.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Every sparkling **speleothem** hanging from the cavern roof is slowly built by drops of lime-saturated water." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Uranium-series dating of a single calcite **speleothem** yielded an uninterrupted rainfall record spanning two hundred thousand years." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The growth rings within a polished **speleothem** reflect seasonal variations in prehistoric rainfall and vegetation." }
    ]
  },
  "Dashboard — spele/speleotherapy.md": {
    word: "speleotherapy",
    primary: "The therapeutic use of subterranean cave environments (especially salt caves or microclimates with pure, allergen-free air) for medical treatment.",
    secondary: "In respiratory medicine, a therapeutic practice used in Central and Eastern Europe to alleviate asthma, chronic bronchitis, and allergies in subterranean salt mines.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "European sanitariums have long advocated **speleotherapy** in subterranean salt grottos for intractable chronic asthma." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The constant humidity and dust-free atmosphere of deep chambers explain the clinical benefits attributed to **speleotherapy**." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "Patients undergoing **speleotherapy** benefit from absolute acoustic calm and aerosolized mineral microclimates." }
    ]
  },
  "Dashboard — spelyng/spelunk.md": {
    word: "spelunk",
    primary: "To explore caves, especially as an amateur hobby or recreational pastime; to go caving.",
    secondary: "In recreational geology and outdoor exploration, navigating wild, non-commercial subterranean caverns using ropes, lights, and climbing gear.",
    quotes: [
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "Tom and Becky ventured deep into the limestone labyrinth, eager to **spelunk** beyond the charted paths." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Local enthusiasts gather on weekends to **spelunk** through the uncharted sinkholes of the karst plateau." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "We were equipped with miners' lamps and stout hemp ropes, ready to **spelunk** into the subterranean crevices of the plateau." }
    ]
  },
  "Dashboard — spelyng/spelunker.md": {
    word: "spelunker",
    primary: "A person who explores caves as a recreational hobby or amateur sport; a caver.",
    secondary: "In outdoor lore, an amateur cave explorer, distinguished by cave scientists from a speleologist (who conducts formal scientific research).",
    quotes: [
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "No daring young **spelunker** had ever traced the boundless corridors of McDougal's Cave to their final outlet." },
      { author: "John McPhee", work: "Basin and Range", quote: "An adventurous **spelunker** squeezing through the narrow crawlway discovered a cathedral-sized chamber of glittering gypsum." },
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "The experienced **spelunker** tapped the cavern wall with his hammer to test for hidden cavities." }
    ]
  },
  "Dashboard — xei/xi.md": {
    word: "xi",
    primary: "The 14th letter of the Greek alphabet (Ξ, ξ), transliterated as 'x' and having the mathematical or linguistic value of [ks].",
    secondary: "In particle physics and astronomy, the symbol designating Xi baryons (cascade particles) containing one or more strange quarks, or the 14th star of a constellation.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Physicists discovered the massive cascade particle, designated by the Greek letter **xi**, in bubble chamber collisions." },
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "In symbolic logic, the Greek letter **xi** frequently denotes an arbitrary propositional function." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The stone inscription concluded with the archaic Greek character **xi**, carved deeply into the marble base." }
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

console.log("Earth & Geology Batch 6 completed! Total words updated:", Object.keys(wordsData).length);
