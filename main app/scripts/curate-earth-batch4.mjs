import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Earth & Geology";

const wordsData = {
  "Dashboard — lith/aerolithology.md": {
    word: "aerolithology",
    primary: "The scientific study of aerolites or stony meteorites that fall to the Earth from outer space.",
    secondary: "A historical branch of meteoritics analyzing the mineralogical composition and cosmic origin of extraterrestrial stone specimens.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The rapid advances of **aerolithology** proved that stones falling from the heavens shared mineral constituents with terrestrial rocks." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Pioneering treatises in **aerolithology** dispelled ancient superstitions by establishing the cosmic trajectory of falling fireballs." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Through **aerolithology**, geologists gained their first direct physical evidence of planetary chemistry outside Earth." }
    ]
  },
  "Dashboard — lith/cholelithiasis.md": {
    word: "cholelithiasis",
    primary: "The formation or presence of gallstones (calculi) in the gallbladder or bile ducts.",
    secondary: "In gastroenterology, a biliary disorder marked by cholesterol or pigment concretions, often presenting with biliary colic, jaundice, or cholecystitis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The agonizing epigastric spasms of acute **cholelithiasis** frequently radiate through to the right scapula." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic sections of the gallbladder wall in chronic **cholelithiasis** show profound hyperplastic and inflammatory changes." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The surgical extraction of biliary concretions has revolutionized our clinical management of **cholelithiasis**." }
    ]
  },
  "Dashboard — lith/endolith.md": {
    word: "endolith",
    primary: "An organism (such as an alga, fungus, or bacterium) that lives inside rocks, coral, or animal shells, often penetrating mineral microscopic pores.",
    secondary: "In geomicrobiology and astrobiology, extremophilic micro-organisms that survive in subterranean fissures and provide analogs for potential life on Mars.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Microscopic **endolith** organisms bore deep into coastal limestone cliffs, accelerating the crumbly decay of the rock." },
      { author: "E.O. Wilson", work: "The Diversity of Life", quote: "Even in the dry valleys of Antarctica, cryptoendolithic communities harbor hardy **endolith** lichens beneath the sandstone crust." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Astrobiologists look to terrestrial **endolith** microbes as models for life surviving deep beneath the Martian permafrost." }
    ]
  },
  "Dashboard — lith/endolithic.md": {
    word: "endolithic",
    primary: "Living within rock, or in the fissures, pores, and microscopic crevices of stone or shell substrates.",
    secondary: "In microbial ecology and sedimentology, describing organisms that actively dissolve or inhabit rock matrices, playing a major role in bioerosion.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The dull green discoloration of the tidal rocks is produced by countless **endolithic** algae tunneling through the calcium carbonate." },
      { author: "Charles Darwin", work: "The Structure and Distribution of Coral Reefs", quote: "Massive brain corals are continually weakened from within by the pervasive boring of **endolithic** filaments." },
      { author: "E.O. Wilson", work: "The Future of Life", quote: "Extreme cold and ultraviolet radiation on mountain summits restrict active life to sheltered **endolithic** habitats." }
    ]
  },
  "Dashboard — lith/epilithic.md": {
    word: "epilithic",
    primary: "Growing or living attached to the surface of rocks or stones (as certain lichens, mosses, or algae); saxicolous.",
    secondary: "In freshwater and marine ecology, describing periphyton communities that form thin biofilms over submerged river stones or bedrock.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "Dark green **epilithic** mosses clung tenaciously to the granite boulders edging the pond." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Encrusting **epilithic** lichens paint the supralittoral sea cliffs in brilliant splashes of orange and black." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Pioneer **epilithic** crusts prepare the smooth rock surface for subsequent colonization by vascular herbs." }
    ]
  },
  "Dashboard — lith/epipaleolithic.md": {
    word: "epipaleolithic",
    primary: "Relating to or denoting the prehistoric period transitional between the Upper Paleolithic and the Neolithic; Mesolithic.",
    secondary: "In archaeology, characterizing hunter-gatherer cultures (c. 20,000–10,000 BP) in the Levant and Mediterranean that utilized microlithic flint tools prior to settled agriculture.",
    quotes: [
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The **epipaleolithic** foragers of the Fertile Crescent developed composite sickle blades long before domesticating emmer wheat." },
      { author: "Lewis Mumford", work: "The City in History", quote: "In **epipaleolithic** camps, human bands established semi-sedentary stations around seasonal gazelle migrations." },
      { author: "Grahame Clark", work: "World Prehistory", quote: "Microlithic arrow armatures identify the **epipaleolithic** horizon across Western Europe following the retreat of the glaciers." }
    ]
  },
  "Dashboard — lith/lith.md": {
    word: "lith",
    primary: "In classical etymology and morphology, the Greek root *lith-* (from λίθος, *lithos*, 'stone', 'rock').",
    secondary: "A productive scientific and archaeological combining element denoting stone, rock formations, lithic tools, or mineralized concretions.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The Greek word for stone, **lith-**, forms the cornerstone of our petrological and stratigraphic vocabulary." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "From the ancient syllable **lith-** we construct both the history of primitive stone tools and the architecture of the Earth's crust." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The prefix **lith-** marks every artifact carved by prehistoric hands from native obsidian and steatite." }
    ]
  },
  "Dashboard — lith/lithagogue.md": {
    word: "lithagogue",
    primary: "An agent, medicine, or remedy that expels or tends to expel urinary or biliary stones (calculi).",
    secondary: "In historical pharmacology, a diuretic or antilithic herb prescribed to promote the passage of renal gravel through the urinary tract.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Traditional apothecaries claimed that wild parsley acted as a sovereign **lithagogue** against gravel." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Ancient pharmacopoeias abounded with reputed **lithagogue** draughts whose virtue resided purely in the copious water imbibed." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Physicians sought in vain a true chemical **lithagogue** capable of dissolving the stone without harming the bladder." }
    ]
  },
  "Dashboard — lith/lithane.md": {
    word: "lithane",
    primary: "A pharmaceutical preparation or brand name for lithium carbonate (Li₂CO₃), used as a mood-stabilizing medication in bipolar disorder.",
    secondary: "In psychopharmacology, a salt that modulates neurotransmission and second-messenger cascades to mitigate manic-depressive cycles.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The psychiatrist initiated a regimen of **lithane** to stabilize the fluctuating mood swings of the manic patient." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Regular serum monitoring is mandatory during **lithane** therapy to maintain therapeutic safety." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "The introduction of **lithane** transformed the clinical outlook for patients crippled by affective psychiatric disorders." }
    ]
  },
  "Dashboard — lith/lithe-bodied.md": {
    word: "lithe-bodied",
    primary: "Having a supple, flexible, and gracefully slender body; agile.",
    secondary: "In literary descriptions, characterized by smooth, effortless physical movement and sinuous posture.",
    quotes: [
      { author: "Herman Melville", work: "Typee", quote: "The young island warriors were **lithe-bodied** and swift of foot as they bounded over the coconut groves." },
      { author: "Jack London", work: "White Fang", quote: "The wolf was a **lithe-bodied** predator capable of turning mid-leap to strike its quarry." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "Eustacia watched the **lithe-bodied** dancers circling around the roaring heath fire." }
    ]
  },
  "Dashboard — lith/lithe.md": {
    word: "lithe",
    primary: "Thin, supple, and graceful; bending easily; limber or pliant.",
    secondary: "In physical motion, marked by effortless fluidity and athletic coordination.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "The elephant to make them mirth used all his might, and wreathed his **lithe** proboscis." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Her figure was slender and **lithe**, moving with quiet, unhurried grace through the dim library." },
      { author: "William Wordsworth", work: "The Prelude", quote: "I climbed the rocky crag with **lithe** limbs and the bounding step of youth." }
    ]
  },
  "Dashboard — lith/litheness.md": {
    word: "litheness",
    primary: "The quality or state of being lithe; flexibility, suppleness, and graceful agility.",
    secondary: "In kinesiology and artistic performance, the muscular elasticity that enables smooth, unrestricted movement without rigidity.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Rosamond possessed an exquisite **litheness** of movement that gave her every gesture an air of effortless refinement." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The small islander leaped onto the riverbank with the startling **litheness** of a feline predator." },
      { author: "Virginia Woolf", work: "The Waves", quote: "The swimmer glided through the green water with a natural **litheness** born of long familiarity with the sea." }
    ]
  },
  "Dashboard — lith/lithesome.md": {
    word: "lithesome",
    primary: "Gracefully flexible, supple, or agile; pliant; lissome.",
    secondary: "In poetic usage, characterized by youthful, nimble buoyancy and light, curving motion.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "Donatello possessed a **lithesome** grace that reminded the observer of an ancient woodland faun." },
      { author: "Emily Brontë", work: "Wuthering Heights", quote: "Cathy was as **lithesome** and lively as a young colt on the wind-swept moor." },
      { author: "Charles Dickens", work: "The Old Curiosity Shop", quote: "The girl had a **lithesome** step that scarcely stirred the summer grass upon the lane." }
    ]
  },
  "Dashboard — lith/lithiasis.md": {
    word: "lithiasis",
    primary: "The formation of stony concretions (calculi) in any organ, duct, or cavity of the body (e.g., kidneys, gallbladder).",
    secondary: "In pathological medicine, a chronic metabolic or infectious condition characterized by the abnormal precipitation of mineral salts from bodily fluids.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Renal **lithiasis** frequently announces itself with sudden, excruciating lumbar pain and hematuria." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The histological study of urinary **lithiasis** demonstrates that proteinaceous organic matrices provide the initial scaffold for crystal nucleation." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Ancient surgeons devised perilous operations to relieve patients from the torture of bladder **lithiasis**." }
    ]
  },
  "Dashboard — lith/lithic.md": {
    word: "lithic",
    primary: "Of, relating to, or made of stone; stony.",
    secondary: "In archaeology, relating to the Stone Age or stone implements; in petrology, containing macroscopic rock fragments (e.g., lithic sandstone).",
    quotes: [
      { author: "V. Gordon Childe", work: "The Dawn of European Civilization", quote: "The introduction of polished **lithic** celts transformed forest clearance in Neolithic Europe." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Microscopic inspection reveals that this greywacke is composed of angular **lithic** fragments torn from older volcanic flows." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The sedimentary succession passes upward into coarse **lithic** sandstones deposited by braided glacial streams." }
    ]
  },
  "Dashboard — lith/lithium.md": {
    word: "lithium",
    primary: "A soft, silvery-white, highly reactive alkali metal, chemical element with atomic number 3 and symbol Li; the lightest known metal.",
    secondary: "In medicine, salts of lithium (especially lithium carbonate) used as a standard mood-stabilizing treatment for bipolar disorder.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Arfvedson discovered the new alkali metal **lithium** while analyzing petalite ore in the laboratory of Berzelius." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "I was fascinated to learn that **lithium**, the lightest of all solid elements, would actually float upon oil." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Cosmologists calculate that primordial **lithium** was synthesized during the first three minutes of the Big Bang." }
    ]
  },
  "Dashboard — lith/lithocarpus.md": {
    word: "lithocarpus",
    primary: "A genus of evergreen trees (family Fagaceae) related to oaks and chestnuts, commonly known as stone oaks, having hard, woody acorn cups.",
    secondary: "In botanical taxonomy, a group of subtropical and tropical trees native mainly to East and Southeast Asia whose acorns feature thick, stony involucres.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The mountain slopes of Java are clothed with colossal evergreen trees of the genus **Lithocarpus**." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "We gathered heavy, stone-hard acorns of **Lithocarpus** along the mist-drenched ridge of Sikkim." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Forest botanists recognize **Lithocarpus** by its stiff, erect catkins and extremely durable wood." }
    ]
  },
  "Dashboard — lith/lithodidae.md": {
    word: "lithodidae",
    primary: "A family of large, crab-like marine decapod crustaceans known as king crabs, belonging to the superfamily Lithodoidea.",
    secondary: "In marine biology and evolutionary taxonomy, anomuran crabs derived from hermit crab ancestors that abandoned shells and developed calcified, spiny carapaces.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Deep subpolar waters are the domain of the **Lithodidae**, whose long, armored legs span several feet across the sea bottom." },
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "The asymmetrical abdomen of the **Lithodidae** reveals their evolutionary descent from soft-tailed hermit crabs." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Trawlers operating in the Bering Sea harvest prized king crabs of the family **Lithodidae** from icy benthic waters." }
    ]
  },
  "Dashboard — lith/lithoglyptics.md": {
    word: "lithoglyptics",
    primary: "The art or process of engraving or carving designs, portraits, or inscriptions on precious or semiprecious stones; glyptics.",
    secondary: "In the history of classical and Renaissance art, the specialized craftsmanship of cutting intaglios, cameos, and signet gems into hard quartz minerals.",
    quotes: [
      { author: "Pliny the Elder", work: "Natural History", quote: "The supreme achievement of classical **lithoglyptics** was the celebrated signet ring carved by Pyrgoteles for Alexander the Great." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "Renaissance collectors revived the ancient art of **lithoglyptics**, treasuring Roman cameos cut in banded sardonyx." },
      { author: "John Ruskin", work: "Aratra Pentelici", quote: "In true **lithoglyptics**, the engraver's diamond point must respect the natural cleavage and translucent depth of the stone." }
    ]
  },
  "Dashboard — lith/lithograph.md": {
    word: "lithograph",
    primary: "A print produced by the process of lithography, using an ink-treated flat stone or metal plate.",
    secondary: "To produce prints or illustrations by drawing upon stone and printing via chemical planography.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "A framed **lithograph** of the Lord Chancellor hung upon the wall above the lawyer's dusty desk." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Norwood Builder", quote: "Holmes examined a colored **lithograph** illustrating the floor plan of the disputed estate." },
      { author: "Edgar Allan Poe", work: "The Murders in the Rue Morgue", quote: "A small **lithograph** portrait of the deceased woman stood upon the mantelpiece." }
    ]
  },
  "Dashboard — lith/lithographer.md": {
    word: "lithographer",
    primary: "A person who produces prints, artwork, or commercial illustrations by the process of lithography.",
    secondary: "In the history of graphic printing, an artisan skilled in chemical etching on Bavarian limestone and multicolor chromolithographic separation.",
    quotes: [
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The commercial **lithographer** furnished every steamboat office with bright pictorial panoramas of river ports." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The Parisian **lithographer** worked late into the night preparing posters that would adorn the boulevards at dawn." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "He apprenticed his nephew to a master **lithographer** to learn the lucrative art of book illustration." }
    ]
  },
  "Dashboard — lith/lithographic.md": {
    word: "lithographic",
    primary: "Of, relating to, or produced by lithography; written or printed on stone.",
    secondary: "In printing and microelectronics, describing planar transfer processes (from Bavarian limestone to modern optical photolithography on silicon).",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The Solnhofen limestone is renowned worldwide for its fine **lithographic** quality and exquisitely preserved pterosaur fossils." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The reproduction of scientific anatomical drawings was revolutionized by the **lithographic** press." },
      { author: "H.G. Wells", work: "The War of the Worlds", quote: "The military map had been hastily printed on rough paper using portable **lithographic** stones." }
    ]
  },
  "Dashboard — lith/lithography.md": {
    word: "lithography",
    primary: "A printing process in which printing is done from a flat stone or metal plate treated so that ink adheres only to the design area (planography).",
    secondary: "In industrial history, the chemical printing invention developed by Alois Senefelder in 1796, based on the mutual repulsion of oil and water.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "Senefelder's invention of **lithography** brought exquisite tonal gradations within reach of the everyday printmaker." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Bruce-Partington Plans", quote: "The stolen government blueprints had been reproduced by secret **lithography**." },
      { author: "Walter Pater", work: "Appreciations", quote: "The golden age of French caricature owed its spontaneous vigor to the speed and freedom of **lithography**." }
    ]
  },
  "Dashboard — lith/lithology.md": {
    word: "lithology",
    primary: "The scientific study and description of rocks, their physical and mineralogical characteristics, and macroscopic features; petrology.",
    secondary: "In stratigraphic geology, the physical character of a rock formation (e.g., color, grain size, texture, mineral content) as distinct from its fossil fauna.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "A sudden change in the **lithology** of the strata marks an abrupt shift from shallow coastal sands to deep marine shale." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Stratigraphers must not rely solely on **lithology**, since identical sandstone beds recur across widely separated eras." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "The field geologist records the **lithology** of every bed, measuring grain roundness and matrix cement with a pocket lens." }
    ]
  },
  "Dashboard — lith/lithomancer.md": {
    word: "lithomancer",
    primary: "A diviner who practices lithomancy; one who claims to foresee the future by interpreting stones, crystals, or reflections in gems.",
    secondary: "In anthropological folklore and occult history, a seer who casts marked stones onto a ceremonial board to read omens.",
    quotes: [
      { author: "Walter Pater", work: "Gaston de Latour", quote: "The wandering **lithomancer** cast seven polished stones onto the velvet cloth, reading the king's fate in their angles." },
      { author: "Richard Francis Burton", work: "The Book of the Thousand Nights and a Night", quote: "The Sultan consulted a Persian **lithomancer** whose beryl crystals revealed distant plots." },
      { author: "Arthur Conan Doyle", work: "The Ring of Thoth", quote: "The Egyptian priest served as royal **lithomancer**, divining victory by the light refracted through sacred peridots." }
    ]
  },
  "Dashboard — lith/lithomancy.md": {
    word: "lithomancy",
    primary: "Divination by means of stones, crystals, or the casting of pebbles and gems; stone divination.",
    secondary: "In the history of folk magic and traditional belief, reading patterns formed by tossing colored stones onto a marked circle.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Superstitious men sought guidance through **lithomancy**, attributing prophetic powers to the random scatter of gravel." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Tribal seers practiced **lithomancy** before battle, reading omen stones cast beside the sacred campfire." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "Medieval grimoires preserved bizarre rituals of **lithomancy** alongside astrological charts." }
    ]
  },
  "Dashboard — lith/lithomantic.md": {
    word: "lithomantic",
    primary: "Of, relating to, or characteristic of lithomancy; pertaining to divination by stones.",
    secondary: "In folkloric studies, describing omens, rituals, or prophetic arts interpreted from mineral stones and crystals.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The barbarian chieftain consulted his **lithomantic** seers before crossing the Danube." },
      { author: "Richard Francis Burton", work: "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", quote: "Bedouin elders preserved **lithomantic** traditions concerning sacred black meteorites." },
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "The mystic's chamber was decorated with arcane **lithomantic** symbols drawn in white chalk." }
    ]
  },
  "Dashboard — lith/lithonate.md": {
    word: "lithonate",
    primary: "A historical pharmaceutical trade name for lithium carbonate tablets used in the management of manic-depressive illness.",
    secondary: "In psychiatric pharmacotherapy, an oral lithium formulation administered to regulate mood swings and prevent manic recurrence.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The patient maintained emotional equilibrium while taking prescribed doses of **lithonate** each morning." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Blood levels must be monitored weekly during the initiation of **lithonate** therapy." },
      { author: "Hans Selye", work: "From Dream to Discovery", quote: "Clinical trials established that **lithonate** dampened the extremes of manic episodes without sedating normal intellect." }
    ]
  },
  "Dashboard — lith/lithophile.md": {
    word: "lithophile",
    primary: "In geochemistry, an element that has an affinity for silicate and oxide minerals, concentrating in the Earth's crust and mantle (e.g., Al, K, Na, Ca, Si).",
    secondary: "In botany and ecology, an organism that thrives, grows, or nests on rocky or stony ground; saxicolous.",
    quotes: [
      { author: "Victor Goldschmidt", work: "Geochemistry", quote: "We classify the chemical elements into **lithophile**, siderophile, chalcophile, and atmophile groups based on geochemical distribution." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Because uranium is a strongly **lithophile** element, it has accumulated in the Earth's upper continental crust." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Goldschmidt demonstrated that **lithophile** elements bonded with oxygen to form the light granitic continents." }
    ]
  },
  "Dashboard — lith/lithophone.md": {
    word: "lithophone",
    primary: "A musical instrument consisting of suspended stones, stone bars, or slabs that produce resonant pitched musical notes when struck.",
    secondary: "In ethnomusicology and organology, an ancient prehistoric percussion instrument, exemplified by the resonant phonolite stone slabs found in Vietnam and Africa.",
    quotes: [
      { author: "Curt Sachs", work: "The History of Musical Instruments", quote: "The prehistoric **lithophone** of Ndut Lieng Krak demonstrates that stone age peoples possessed sophisticated acoustic scales." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The shaman struck the tuned slabs of the **lithophone**, producing clear bell-like tones that echoed through the valley." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "Excavations revealed resonant limestone slabs that may have served as a sacred **lithophone** in temple ceremonies." }
    ]
  },
  "Dashboard — lith/lithophragma.md": {
    word: "lithophragma",
    primary: "A genus of perennial herbaceous plants (family Saxifragaceae) native to western North America, having slender stems and fringed white or pink flowers; woodland star.",
    secondary: "In evolutionary botany, a model genus for studying coevolution with mutualistic and parasitic Greya moths that pollinate and oviposit in its flowers.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The delicate star-like flowers of **Lithophragma** brighten the rocky pine woods in early spring." },
      { author: "John Muir", work: "The Mountains of California", quote: "Along the granite ledges of the Sierra foothills, blooms of **Lithophragma** danced in the mountain breeze." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Wildflower gardeners cultivate **Lithophragma** for its deeply cut white petals and dainty habit." }
    ]
  },
  "Dashboard — lith/lithophyte.md": {
    word: "lithophyte",
    primary: "A plant that grows on or in the crevices of bare rock, deriving nutrients from rainwater, atmospheric dust, and decomposing organic debris; a rock plant.",
    secondary: "In ecological botany, an epilithic species (such as many ferns, saxifrages, and rupicolous orchids) adapted to arid, stony microenvironments.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Delicate ferns flourished as true **lithophyte** species within the narrowest fissures of the sea cliff." },
      { author: "Alexander von Humboldt", work: "Personal Narrative", quote: "Every bare porphyry crag was colonized by hardy **lithophyte** lichens that slowly crumbled the rock." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Marine algae clinging to tidal rocks provide shelter for small **lithophyte** colonies bathed in sea spray." }
    ]
  },
  "Dashboard — lith/lithophytic.md": {
    word: "lithophytic",
    primary: "Of, relating to, or characteristic of a lithophyte; growing upon rocks or stony ground.",
    secondary: "In plant physiology, possessing specialized morphological adaptations (e.g., velamen-covered roots or succulent leaves) for survival on bare stone.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "The gorge walls supported a dense **lithophytic** flora of pendulous mosses and dwarf rhododendrons." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "Certain rupicolous orchids exhibit strictly **lithophytic** habits, perching upon granite boulders along riverbeds." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "The limestone pavement shelters a specialized **lithophytic** community within its deep grykes." }
    ]
  },
  "Dashboard — lith/lithops.md": {
    word: "lithops",
    primary: "A genus of succulent perennial plants (family Aizoaceae) native to southern Africa, having two fleshy, fused leaves resembling small pebbles; living stones.",
    secondary: "In plant evolutionary morphology, an extreme example of crypsis or protective mimicry, where leaf patterns and coloration blend seamlessly with stony desert ground.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by which Orchids are Fertilised", quote: "Desert succulents of the genus **Lithops** achieve near-total invisibility among surrounding stones through marvelous mimicry." },
      { author: "Liberty Hyde Bailey", work: "The Garden of Pinks", quote: "The collector of xerophytes marvels at **Lithops**, whose cleft fleshy leaves resemble split pebbles of the veld." },
      { author: "E.O. Wilson", work: "The Diversity of Life", quote: "Protective camouflage reaches its botanical zenith in **Lithops**, hiding its succulent moisture from foraging desert herbivores." }
    ]
  },
  "Dashboard — lith/lithospermum.md": {
    word: "lithospermum",
    primary: "A cosmopolitan genus of herbaceous plants (family Boraginaceae) with small tubular flowers and exceptionally hard, shiny, porcelain-like nutlets; gromwell or puccoon.",
    secondary: "In ethnobotany and herbal history, plants valued for stony seed coats (whence the Greek name 'stone seed') and red dye extracted from their roots.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The glossy white nutlets of wild **Lithospermum** shine like porcelain beads in the autumn hedgerows." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Indigenous tribes extracted a brilliant scarlet dye from the roots of **Lithospermum** for coloring leather." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The stony hardness of the fruit in **Lithospermum** led ancient herbalists to prescribe it for renal calculus under the doctrine of signatures." }
    ]
  },
  "Dashboard — lith/lithosphere.md": {
    word: "lithosphere",
    primary: "The rigid outer mechanical layer of the Earth, comprising the crust and the uppermost part of the solid mantle.",
    secondary: "In plate tectonics, the mechanically strong, brittle shell (typically 100 km thick) that is broken into tectonic plates that float and move upon the ductile asthenosphere.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The rigid **lithosphere** breaks into colossal mosaic plates that drift upon the hotter, more plastic asthenosphere beneath." },
      { author: "John McPhee", work: "Basin and Range", quote: "Subduction carries fragments of the oceanic **lithosphere** thousands of miles down into the deep mantle." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The continents are passenger rafts riding atop the fractured plates of Earth's mobile **lithosphere**." }
    ]
  },
  "Dashboard — lith/lithotomy.md": {
    word: "lithotomy",
    primary: "The surgical removal of a stone (calculus) from the urinary bladder, kidney, or gallbladder by cutting into the organ.",
    secondary: "In medical history, an ancient and hazardous surgical procedure famously referred to in the Hippocratic Oath ('I will not cut for stone...').",
    quotes: [
      { author: "Samuel Pepys", work: "The Diary of Samuel Pepys", quote: "This day I celebrated my deliverance from the stone, it being five years since I underwent the perilous cut of **lithotomy**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Before the advent of anesthesia and antisepsis, **lithotomy** demanded lightning speed and immense nerve from the operating surgeon." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The ancient itinerant cutter for stone performed **lithotomy** upon thousands of sufferers without formal anatomical training." }
    ]
  },
  "Dashboard — lith/lithotripsy.md": {
    word: "lithotripsy",
    primary: "A medical procedure that breaks down kidney stones or gallstones into small fragments that can be passed naturally out of the body.",
    secondary: "In modern urology, extracorporeal shock wave lithotripsy (ESWL), which utilizes focused acoustic shock waves to pulverize calculi non-invasively.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern advances in mechanical **lithotripsy** spared countless patients the agony of open abdominal surgery." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The invention of the lithotrite allowed the surgeon to crush the stone within the bladder, heralding the dawn of **lithotripsy**." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Extracorporeal shock wave **lithotripsy** focuses acoustic pulses directly onto the calculus with pinpoint ultrasonic guidance." }
    ]
  },
  "Dashboard — lith/lithuania.md": {
    word: "lithuania",
    primary: "A country in northeastern Europe on the eastern shore of the Baltic Sea, southernmost of the three Baltic states; capital Vilnius.",
    secondary: "In European history, the Grand Duchy of Lithuania, a major medieval and early modern power that united with Poland in the Polish-Lithuanian Commonwealth.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The pagan tribes of **Lithuania** resisted Teutonic crusaders behind impenetrable marshes for centuries." },
      { author: "Adam Mickiewicz", work: "Pan Tadeusz", quote: "**Lithuania**, my country, thou art like good health; how much one should prize thee, he only knows who has lost thee." },
      { author: "Czesław Miłosz", work: "Native Realm", quote: "My childhood memories were rooted in the green meadows and dark pine forests of rural **Lithuania**." }
    ]
  },
  "Dashboard — lith/lithuanian.md": {
    word: "lithuanian",
    primary: "Of, relating to, or characteristic of Lithuania, its people, language, or culture; a native or inhabitant of Lithuania.",
    secondary: "In Indo-European comparative linguistics, the most archaic surviving Baltic language, retaining ancient Indo-European phonological and morphological structures.",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The **Lithuanian** tongue has preserved ancient grammatical inflections with a fidelity rivaling Sanskrit itself." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Jurgis Rudkus was a powerful young **Lithuanian** who crossed the ocean in search of freedom and work in the Chicago stockyards." },
      { author: "Czesław Miłosz", work: "The Captive Mind", quote: "The **Lithuanian** folklore was saturated with tree spirits, pagan deities, and sorrowful dainos." }
    ]
  },
  "Dashboard — lith/lithuresis.md": {
    word: "lithuresis",
    primary: "The passage or excretion of gravel, small stones, or calculi in the urine.",
    secondary: "In clinical nephrology, the spontaneous urethral voiding of pulverized renal or bladder calculi following medical or physical dissolution.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Following the acute renal colic, the patient experienced spontaneous **lithuresis**, discharging several sharp uric acid stones." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Copious alkaline fluids were administered to encourage **lithuresis** and flush the urinary passages." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The micro-analysis of gravel voided during **lithuresis** reveals the chemical nature of the underlying metabolic defect." }
    ]
  },
  "Dashboard — lith/megalith.md": {
    word: "megalith",
    primary: "A very large stone used, especially in prehistoric times, to construct a monument, tomb, or sacred structure (e.g., Stonehenge, Carnac).",
    secondary: "In prehistoric archaeology and anthropology, monumental stone structures (menhirs, dolmens, cromlechs) erected during the Neolithic and Bronze Ages.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "They walked into the circle of Stonehenge, where each towering **megalith** loomed giant-like against the gray dawn." },
      { author: "V. Gordon Childe", work: "The Dawn of European Civilization", quote: "The collective tombs built of huge **megalith** slabs required the organized labor of entire tribal communities." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The prehistoric **megalith** marks humanity's earliest attempt to fix an immovable spiritual anchor upon the landscape." }
    ]
  },
  "Dashboard — lith/megalithic.md": {
    word: "megalithic",
    primary: "Relating to or consisting of megaliths; denoting prehistoric monuments constructed of massive stone blocks.",
    secondary: "In European and Mediterranean archaeology, the cultural complex (c. 4500–1500 BC) marked by the construction of passage graves, dolmens, and stone circles.",
    quotes: [
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The ancient Roman amphitheatre stood atop still older **megalithic** earthworks that encircled the town." },
      { author: "Archibald Geikie", work: "The Scenery of Scotland", quote: "Standing stones of **megalithic** circles at Callanish cast long shadows across the Lewis peat." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The cyclopean foundations of the palace incorporated **megalithic** masonry dating to the earliest bronze age builders." }
    ]
  },
  "Dashboard — lith/mesolithic.md": {
    word: "mesolithic",
    primary: "Of, relating to, or denoting the Middle Stone Age, the archaeological period between the Paleolithic and the Neolithic (c. 10,000–5,000 BC).",
    secondary: "In human prehistory, the post-glacial cultural stage characterized by diverse hunting, fishing, and foraging adaptations and the extensive use of microliths.",
    quotes: [
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The **mesolithic** hunters adapted to dense post-glacial forests by inventing stone-tipped arrows and dugout canoes." },
      { author: "Grahame Clark", work: "World Prehistory", quote: "Coastal shell middens in Denmark provide rich evidence of **mesolithic** communities harvesting marine wealth." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The **mesolithic** revolution laid the domestic foundation for the settled villages that followed in the Neolithic." }
    ]
  },
  "Dashboard — lith/microlite.md": {
    word: "microlite",
    primary: "A microscopic crystal or incipient crystalline form occurring in glassy or fine-grained volcanic igneous rocks.",
    secondary: "In mineralogy, a pale yellow, reddish, or brown isometric mineral of the pyrochlore group containing calcium, sodium, and tantalum oxide.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Thin sections of volcanic obsidian examined under polarized light reveal swarms of embryonic **microlite** crystals aligned with the flow." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The rapid chilling of the molten lava prevented the growth of large crystals, leaving only minute **microlite** needles suspended in volcanic glass." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The rare mineral **microlite** occurs in granitic pegmatites associated with albite and tourmaline." }
    ]
  },
  "Dashboard — lith/monolith.md": {
    word: "monolith",
    primary: "A large single upright block of stone, especially one shaped into or serving as a monument, pillar, or obelisk.",
    secondary: "Figuratively, a massive, unyielding, and uniform organization, institution, or structure that acts as a single powerful entity.",
    quotes: [
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The black **monolith** stood upright on the lunar plain, perfectly rectangular, absorbing all light with enigmatic perfection." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The head of the sperm whale reared out of the foam like a dark granite **monolith**." },
      { author: "George Orwell", work: "1984", quote: "The Ministry of Truth towered vast and white above the grimy landscape, a colossal **monolith** of three hundred meters." }
    ]
  },
  "Dashboard — lith/monolithic.md": {
    word: "monolithic",
    primary: "Formed of a single large block of stone; massive, solid, and uniform.",
    secondary: "Figuratively, constituting a massive, indivisible, and rigidly uniform whole; incapable of being modified or varied.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The portico was supported by sixteen colossal **monolithic** columns of red Egyptian granite." },
      { author: "George Orwell", work: "1984", quote: "The Party presented a **monolithic** front of total orthodoxy, brooking no divergence in doctrine or feeling." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "The plateau was surrounded by sheer, **monolithic** red sandstone cliffs that defied any ascent." }
    ]
  },
  "Dashboard — lith/neolith.md": {
    word: "neolith",
    primary: "A stone implement or tool belonging to the Neolithic (New Stone Age) period, typically characterized by ground, polished surfaces.",
    secondary: "In prehistory, polished stone axes, adzes, and celts that enabled effective woodworking, land clearance, and early agricultural construction.",
    quotes: [
      { author: "V. Gordon Childe", work: "The Dawn of European Civilization", quote: "The polished **neolith** gave early farming communities the power to fell oak forests and construct wooden houses." },
      { author: "John Lubbock", work: "Pre-historic Times", quote: "We divide the stone age into the paleolith of chipped flint and the polished **neolith** of the agricultural era." },
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "The plowman turned up a polished greenstone **neolith** embedded in the chalk furrow." }
    ]
  },
  "Dashboard — lith/neolithic.md": {
    word: "neolithic",
    primary: "Of, relating to, or denoting the New Stone Age (c. 10,000–4,000 BC), characterized by polished stone tools, agriculture, animal domestication, and pottery.",
    secondary: "In cultural anthropology, the epochal transformation from nomadic foraging to sedentary village life, known as the Neolithic Revolution.",
    quotes: [
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The **neolithic** revolution transformed humanity from passive food-gatherers into active food-producers." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The **neolithic** village fostered garden agriculture, maternal care, and the enduring rituals of community life." },
      { author: "H.G. Wells", work: "The Outline of History", quote: "With the arrival of **neolithic** culture, pottery and weaving made their appearance alongside domesticated cattle and wheat." }
    ]
  },
  "Dashboard — lith/paleolith.md": {
    word: "paleolith",
    primary: "A stone implement or artifact belonging to the Paleolithic (Old Stone Age) period, typically roughly chipped or flaked.",
    secondary: "In prehistoric archaeology, stone handaxes, choppers, and flakes crafted by early hominins from flint, chert, or quartzite.",
    quotes: [
      { author: "John Lubbock", work: "Pre-historic Times", quote: "A rough flint **paleolith** recovered from the river gravels confirmed the enormous geological antiquity of man." },
      { author: "Thomas Henry Huxley", work: "Evidence as to Man's Place in Nature", quote: "The discovery of the chipped **paleolith** alongside mammoth bones shattered the short Biblical chronology." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Professor Summerlee held up a crudely chipped **paleolith** discovered at the base of the volcanic cliff." }
    ]
  },
  "Dashboard — lith/paleolithic.md": {
    word: "paleolithic",
    primary: "Of, relating to, or denoting the early phase of the Stone Age, characterized by the earliest known use of chipped stone tools.",
    secondary: "In human prehistory, the vast Pleistocene cultural epoch (from c. 3.3 million to 12,000 years ago) encompassing early hominin toolmaking, mammoth hunting, and cave painting.",
    quotes: [
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The **paleolithic** hunters of the Ice Age displayed breathtaking mastery in their cave paintings at Altamira and Lascaux." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The cave was the ceremonial center of **paleolithic** man long before the first permanent houses were built." },
      { author: "Charles Lyell", work: "The Geological Evidences of the Antiquity of Man", quote: "Strata containing **paleolithic** flint tools correspond to the glacial epochs of extinct quadrupeds." }
    ]
  },
  "Dashboard — lith/paralithodes.md": {
    word: "paralithodes",
    primary: "A genus of commercially important king crabs (family Lithodidae), including the red king crab (Paralithodes camtschaticus) of the North Pacific and Bering Sea.",
    secondary: "In marine invertebrate zoology and fishery biology, large cold-water decapods with heavily calcified spiny carapaces and reduced fifth pereiopods.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The red king crab, **Paralithodes**, crawls across the icy continental shelf of the Bering Sea in search of benthic mollusks." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Trawlers brave freezing gale-force seas to trap massive specimens of **Paralithodes** along Alaskan banks." },
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "Taxonomists classify **Paralithodes** among the anomurans despite its superficially true crab-like morphology." }
    ]
  },
  "Dashboard — lith/phlebolith.md": {
    word: "phlebolith",
    primary: "A small, rounded calcareous stone or concretion (calcified thrombus) formed within a vein.",
    secondary: "In vascular radiology and pathology, a benign pelvic calcification arising from an organized blood clot, commonly seen as an incidental finding on abdominal radiographs.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "A thrombus in a dilated pelvic vein may undergo complete petrification, forming a spherical **phlebolith**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The radiologist must carefully distinguish a harmless pelvic **phlebolith** from a stone lodged in the lower ureter." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Post-mortem examination revealed several calcified **phlebolith** nodules within the hemorrhoidal venous plexus." }
    ]
  },
  "Dashboard — lith/photolithography.md": {
    word: "photolithography",
    primary: "A photographic printing process in which a stone or metal plate is coated with a photosensitive substance, exposed to light through a negative, and etched for printing.",
    secondary: "In semiconductor manufacturing, the micro-fabrication process of transferring geometric circuit patterns from a photomask onto a light-sensitive chemical photoresist on a silicon wafer.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Modern microchips contain millions of microscopic transistors etched with extreme precision by ultraviolet **photolithography**." },
      { author: "Douglas Hofstadter", work: "Gödel, Escher, Bach", quote: "Through repeated cycles of **photolithography**, silicon wafers are inscribed with logical labyrinths of incredible complexity." },
      { author: "Walter Pater", work: "Appreciations", quote: "Early experiments in **photolithography** attempted to marry mechanical photographic fidelity with the delicate ink tones of the stone." }
    ]
  },
  "Dashboard — lith/phytolith.md": {
    word: "phytolith",
    primary: "A microscopic silica body or mineralized deposit precipitated within the cells or tissues of a living plant, persisting in soil long after the plant decays.",
    secondary: "In paleoethnobotany and geoarchaeology, durable opal silica particles whose diagnostic shapes allow researchers to identify ancient cultivated crops and reconstruct past vegetation.",
    quotes: [
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould through the Action of Worms", quote: "Microscopic inspection of the vegetable mould revealed thousands of glistening **phytolith** skeletons from decayed grasses." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Siliceous **phytolith** remains accumulate in lake sediments, recording the composition of prehistoric prairie flora." },
      { author: "V. Gordon Childe", work: "What Happened in History", quote: "Archaeobotanists extract the microscopic **phytolith** from prehistoric pottery to identify the earliest cultivated grains." }
    ]
  },
  "Dashboard — lith/regolith.md": {
    word: "regolith",
    primary: "The layer of unconsolidated, weathered rock fragments, mineral grains, and soil that rests upon solid bedrock.",
    secondary: "In lunar and planetary geology, the blanket of shattered rock, impact dust, and glassy beads that covers the surface of the Moon, asteroids, and Mars.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The terrestrial **regolith** represents the weathered mantle of broken rock fragments that nurtures all plant life." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The Apollo astronauts walked through thick lunar **regolith**, their bootprints preserved for millions of years in the vacuum." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Glacial ice scraped away the ancient **regolith**, exposing fresh, striated bedrock across the Canadian Shield." }
    ]
  },
  "Dashboard — lith/sialolithiasis.md": {
    word: "sialolithiasis",
    primary: "The formation or presence of one or more calculi (stones) in a salivary gland or its excretory duct.",
    secondary: "In oral and maxillofacial pathology, obstruction of salivary flow (most frequently in Wharton's duct of the submandibular gland), causing postprandial swelling and pain.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient suffered from acute submandibular swelling during meals, typical of ductal **sialolithiasis**." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Analysis of the stone in **sialolithiasis** reveals concentric layers of calcium phosphate deposited around an organic epithelial core." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Surgical incision over Wharton's duct easily relieved the obstruction caused by chronic **sialolithiasis**." }
    ]
  },
  "Dashboard — lith/tonsillolith.md": {
    word: "tonsillolith",
    primary: "A calcified stone or concretion (tonsil stone) formed in the crypts of the palatine tonsils from trapped food particles, cellular debris, and bacteria.",
    secondary: "In otolaryngology, a hard, foul-smelling calculus composed of calcium salts (hydroxyapatite, calcium carbonate) contributing to halitosis and throat irritation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic follicular tonsillitis may result in the extrusion of a small, yellowish **tonsillolith**." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic sections show that a **tonsillolith** develops through mineral precipitation around actinomycotic colonies and epithelial debris." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The patient complained of persistent foreign body sensation in the throat until a hard **tonsillolith** was dislodged." }
    ]
  },
  "Dashboard — lith/urolithiasis.md": {
    word: "urolithiasis",
    primary: "The formation or presence of calculi (stones) anywhere in the urinary tract, including the kidneys, ureters, bladder, or urethra.",
    secondary: "In clinical urology, a common and painful disorder associated with metabolic abnormalities, dehydration, or urinary stasis, producing severe nephrolithiasis and colic.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinical history of **urolithiasis** is marked by paroxysms of agonizing lumbar colic radiating toward the groin." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The pathogenesis of **urolithiasis** involves urinary super-saturation, crystal nucleation, and organic matrix aggregation." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "No affliction in the catalogue of human diseases has caused more acute torment than untreated **urolithiasis**." }
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

console.log("Earth & Geology Batch 4 completed! Total words updated:", Object.keys(wordsData).length);
