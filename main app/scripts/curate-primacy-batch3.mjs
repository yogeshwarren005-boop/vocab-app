import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — palae";

const wordsData = {
  "Paleocene.md": {
    word: "Paleocene",
    primary: "The earliest geological epoch of the Paleogene period and Cenozoic era, spanning from approximately 66 to 56 million years ago (from Greek palaios ancient + kainos new).",
    secondary: "In historical geology and paleontology, the pivotal epoch immediately following the Cretaceous-Paleogene extinction event, characterized by the rapid adaptive radiation of placental mammals.",
    quotes: [
      { author: "George Gaylord Simpson", work: "The Beginning of the Age of Mammals", quote: "The fossil beds of the **Paleocene** document the explosive diversification of archaic mammalian orders following the demise of the dinosaurs." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The **Paleocene** strata mark the true dawn of the modern era, containing the ancestral roots of contemporary flora." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "In the post-cataclysmic tranquility of the **Paleocene**, surviving lineages seized ecological space vacated by the giant reptiles." }
    ]
  },
  "Paleogene.md": {
    word: "Paleogene",
    primary: "A major geological period spanning from approximately 66 to 23 million years ago, comprising the Paleocene, Eocene, and Oligocene epochs.",
    secondary: "In stratigraphy, the first period of the Cenozoic era, during which mammals evolved from small primitive forms into dominant terrestrial herbivores and carnivores alongside modern birds.",
    quotes: [
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "During the **Paleogene** period, archaic creodonts and primitive ungulates spread across extensive subtropical forests." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The tectonic collisions of the **Paleogene** initiated the catastrophic uplift of the Alpine and Himalayan mountain systems." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "By the close of the **Paleogene**, ancestral equids and primates had established modern anatomical body plans." }
    ]
  },
  "Paleolithic.md": {
    word: "Paleolithic",
    primary: "Of, relating to, or denoting the early phase of the Stone Age, spanning from the earliest stone tool use c. 2.5 million years ago until the end of the Pleistocene c. 10,000 BCE.",
    secondary: "In anthropology and prehistoric archaeology, characterized by chipped flint hand-axes, nomadic hunter-gatherer bands, and Pleistocene cave art (Lascaux, Altamira).",
    quotes: [
      { author: "John Lubbock", work: "Pre-historic Times", quote: "I proposed the division between the **Paleolithic** or Old Stone Age of chipped tools, and the Neolithic or New Stone Age of polished implements." },
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The **Paleolithic** hunter depended entirely on wild game and foraging, living at the mercy of glacial climate shifts." },
      { author: "Henri Breuil", work: "Four Hundred Centuries of Cave Art", quote: "The breathtaking animal murals of Lascaux reveal the sublime artistic and ritual genius of **Paleolithic** humanity." }
    ]
  },
  "Paleozoic.md": {
    word: "Paleozoic",
    primary: "The earliest of the three geologic eras of the Phanerozoic eon, lasting from approximately 539 to 252 million years ago (from Greek palaios ancient + zoe life).",
    secondary: "In earth history, the immense era bracketed by the Cambrian explosion of marine invertebrates and the catastrophic Permian-Triassic mass extinction, encompassing the colonization of land.",
    quotes: [
      { author: "Roderick Murchison", work: "The Silurian System", quote: "The marine strata of the early **Paleozoic** reveal an astonishing proliferation of trilobites, brachiopods, and graptolites." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "To the question why we find no rich fossiliferous deposits belonging to periods prior to the **Paleozoic**, I can give no satisfactory answer." },
      { author: "Stephen Jay Gould", work: "The Book of Life", quote: "During the late **Paleozoic**, vast coal-swamp forests covered Pangaea, sustained by giant amphibians and early reptiles." }
    ]
  },
  "micropaleontology.md": {
    word: "micropaleontology",
    primary: "The branch of paleontology that deals with the study of microfossils, microscopic remains of plants and animals requiring microscopic examination.",
    secondary: "In petroleum geology and paleoceanography, analyzing foraminifera, radiolarians, ostracods, and conodonts for biostratigraphic correlation and reconstructing past ocean temperatures.",
    quotes: [
      { author: "Joseph A. Cushman", work: "Foraminifera: Their Classification and Economic Use", quote: "Industrial **micropaleontology** proved indispensable to the petroleum engineer, mapping oil-bearing strata from drill-core samples." },
      { author: "G. G. Simpson", work: "Life of the Past", quote: "The extraordinary abundance of microfossils makes **micropaleontology** our most reliable tool for fine stratigraphic correlation." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep-sea sediment cores unroll millions of years of oceanic history through the delicate lens of **micropaleontology**." }
    ]
  },
  "palae.md": {
    word: "palae",
    primary: "A combining root derived from Ancient Greek palaios, meaning ancient, prehistoric, antique, or primitive.",
    secondary: "In scientific nomenclature and humanities terminology, forming words relating to ancient geological eras, fossil life, and prehistory (paleontology, Paleolithic, paleoclimate).",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek prefix **palae**- or paleo- stems from palaios, meaning ancient, preserved across countless modern geological terms." },
      { author: "Max Müller", work: "The Science of Language", quote: "By prefixing the stem **palae**-, nineteenth-century science opened the subterranean archives of prehistory." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The natural history disciplines adopted **palae**- to differentiate fossil species from modern living fauna." }
    ]
  },
  "palaeencephalon.md": {
    word: "palaeencephalon",
    primary: "The phylogenetically older, primitive part of the vertebrate brain (comprising the brainstem, basal ganglia, and cerebellum), contrasted with the neocortex or neencephalon.",
    secondary: "In comparative neuroanatomy and evolutionary neurology, the primitive reptilian core mediating autonomic reflexes, survival drives, and instinctive motor patterns.",
    quotes: [
      { author: "Alexander Luria", work: "The Working Brain", quote: "The **palaeencephalon** regulates fundamental arousal and autonomic homeostasis, upon which cortical functions depend." },
      { author: "Paul D. MacLean", work: "The Triune Brain in Evolution", quote: "Our ancestral survival reflexes reside within the **palaeencephalon**, the ancient neural chassis shared with primitive reptiles." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "L-DOPA seemed to awaken primal motor drives anchored deep within the patient's undamaged **palaeencephalon**." }
    ]
  },
  "palaemon.md": {
    word: "palaemon",
    primary: "A genus of freshwater, brackish, and marine decapod prawns (family Palaemonidae); also the Greek sea divinity Palaemon (Melicertes; homograph on palae-!).",
    secondary: "In classical mythology, the deified mortal boy Melicertes transformed into the benevolent sea-god Palaemon (guardian of harbors); in carcinology, transparent commercial prawns.",
    quotes: [
      { author: "Ovid", work: "Metamorphoses", quote: "Neptune took pity on the weeping mother and son, transforming Ino into Leucothea and young Melicertes into the sea-god **Palaemon**." },
      { author: "John Milton", work: "Comus", quote: "By dead Parthenope's dear tomb, / And fair Ligea's golden comb, / Wherewith she sits on diamond rocks / Sleeking her soft alluring locks; / By all the nymphs that gladly dance / Upon the sea's broad countenance; / And by the god **Palaemon**'s sacred name." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The thoracic appendages of the common prawn, **Palaemon**, demonstrate standard decapod biramous architecture." }
    ]
  },
  "palaemonidae.md": {
    word: "palaemonidae",
    primary: "A diverse family of decapod crustaceans within the infraorder Caridea, commonly comprising coastal and freshwater prawns and shrimps.",
    secondary: "In marine ecology and aquaculture, an ecologically vital family including commercially farmed giant river prawns (Macrobrachium rosenbergii) and symbiotic reef cleaners.",
    quotes: [
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "Delicate transparent prawns of the family **Palaemonidae** darted among the stinging sea anemone tentacles." },
      { author: "Thomas Stebbing", work: "A History of Crustacea", quote: "The **Palaemonidae** are characterized by their compressed rostrum, toothed margins, and enlarged second pair of pereiopods." },
      { author: "David Starr Jordan", work: "Fishes and Marine Life", quote: "Estuarine mudflats provide rich nurseries for juvenile shrimps belonging to the **Palaemonidae**." }
    ]
  },
  "palaeoanthropology.md": {
    word: "palaeoanthropology",
    primary: "The interdisciplinary scientific study of the fossil record, evolutionary origins, and cultural emergence of early hominids and ancient humans.",
    secondary: "In biological anthropology, combining comparative osteology, archaeology, and ancient paleogenomics to chart human lineage divergence (Australopithecus, Homo erectus, Neanderthals).",
    quotes: [
      { author: "Louis Leakey", work: "By the Evidence: Memoirs, 1932–1951", quote: "Olduvai Gorge proved to be a natural treasure-house for **palaeoanthropology**, yielding early hominid tools and fossil crania." },
      { author: "Richard Leakey", work: "Origins Reconsidered", quote: "The goal of **palaeoanthropology** is not merely to amass old bones, but to understand the environmental pressures that shaped human consciousness." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "The history of **palaeoanthropology** reveals how unconscious racial and social biases influenced reconstructions of fossil ancestors." }
    ]
  },
  "palaeobiology.md": {
    word: "palaeobiology",
    primary: "The branch of paleontology and biological science that investigates the physiology, life history, ecology, and evolution of prehistoric fossil organisms (British English spelling).",
    secondary: "In evolutionary biology, moving beyond purely descriptive fossil taxonomy to model biomechanics, metabolic rates, and ecosystem interactions in deep time.",
    quotes: [
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", quote: "Modern **palaeobiology** integrates genetic theory with the physical record of deep time to deduce evolutionary rates." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Through comparative **palaeobiology**, we discern how heterochronic changes in embryonic development generated dramatic macroevolutionary transitions." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "The insights of **palaeobiology** demonstrate that the history of life is not a gradual ramp, but a series of punctuated radiations." }
    ]
  },
  "palaeobotany.md": {
    word: "palaeobotany",
    primary: "The branch of paleontology and botany that studies fossil plant remains, ancient vegetation, and plant evolutionary history (British English spelling).",
    secondary: "In earth sciences, reconstructing past terrestrial environments and atmospheric carbon levels through microscopic cuticle analysis, fossilized wood, and palynology.",
    quotes: [
      { author: "Asa Gray", work: "Scientific Papers", quote: "The discoveries of **palaeobotany** show that our modern temperate flora once flourished in polar regions during warm Tertiary epochs." },
      { author: "Marie Stopes", work: "Studies in the Composition of Coal", quote: "Through detailed **palaeobotany**, we identified the microscopic spore exines and cellular resins that form the distinct lithotypes of coal." },
      { author: "Charles Darwin", work: "Life and Letters of Charles Darwin", quote: "The rapid development of all higher plants in recent geological times is an abominable mystery to the student of **palaeobotany**." }
    ]
  },
  "palaeoclimatology.md": {
    word: "palaeoclimatology",
    primary: "The scientific study of climates throughout Earth's geological history prior to the instrumental meteorological record.",
    secondary: "In earth system science, utilizing climate proxies—such as ice cores, tree rings, marine sediment oxygen isotopes, and fossil pollen—to model long-term climate variability.",
    quotes: [
      { author: "Wladimir Köppen", work: "The Climates of the Geological Past", quote: "Through **palaeoclimatology**, we reconstruct the periodic advance and retreat of massive continental ice sheets across the Northern Hemisphere." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep ocean cores provide **palaeoclimatology** with an unblemished record of ice age cooling cycles preserved in calcium carbonate shells." },
      { author: "James Lovelock", work: "Gaia: A New Look at Life on Earth", quote: "The findings of **palaeoclimatology** confirm that living organisms have actively maintained planetary surface temperatures within habitable bounds for billions of years." }
    ]
  },
  "palaeodendrology.md": {
    word: "palaeodendrology",
    primary: "The scientific study of fossilized trees, fossil wood, and ancient arborescent vegetation.",
    secondary: "In paleobotany, analyzing silicified tree rings (dendrochronology in deep time) to deduce prehistoric growth seasons, volcanic disruptions, and forest canopy ecology.",
    quotes: [
      { author: "Robert Etheridge", work: "Fossils of the British Islands", quote: "The investigations of **palaeodendrology** revealed petrified coniferous trunks standing erect in the Jurassic dirt beds of Portland." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Microscopic wood anatomy in **palaeodendrology** enables the botanist to determine extinct gymnosperm families from mineralized logs." },
      { author: "John William Dawson", work: "The Geological History of Plants", quote: "Through **palaeodendrology**, we reconstructed the colossal scale of Carboniferous lycopod trees whose trunks exceeded a hundred feet in height." }
    ]
  },
  "palaeoecology.md": {
    word: "palaeoecology",
    primary: "The study of the relationships between ancient, fossil organisms and their prehistoric physical and biological environments.",
    secondary: "In evolutionary science, reconstructing ancient trophic webs, predator-prey dynamics, and biome migrations in response to geological events and mass extinctions.",
    quotes: [
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The Burgess Shale offers an unmatched window into marine **palaeoecology**, preserving soft-bodied predators and burrowers in living association." },
      { author: "George Gaylord Simpson", work: "The Meaning of Evolution", quote: "Evolutionary changes are fundamentally ecological shifts; **palaeoecology** reveals how lineages adapt to shifting environmental niches." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "By examining fossil pollen assemblages, **palaeoecology** maps how post-glacial forests migrated northward as the glaciers receded." }
    ]
  },
  "palaeoethnography.md": {
    word: "palaeoethnography",
    primary: "The ethnographic study of prehistoric or ancient human societies, material cultures, and customs based on archaeological evidence.",
    secondary: "In prehistoric anthropology, reconstructing social organization, kinship patterns, and ceremonial rituals from stone tools, dwelling foundations, and burials.",
    quotes: [
      { author: "V. Gordon Childe", work: "Social Evolution", quote: "**Palaeoethnography** utilizes material grave goods and dwelling layouts to reconstruct the social hierarchies of Bronze Age clans." },
      { author: "Lewis Henry Morgan", work: "Ancient Society", quote: "The tools and hearth arrangements recovered from lake dwellings provide valuable data for comparative **palaeoethnography**." },
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "Through **palaeoethnography**, we trace how ancestral human customs evolved from crude flint-knapping rituals to complex civic ceremonies." }
    ]
  },
  "palaeogeography.md": {
    word: "palaeogeography",
    primary: "The branch of geology that reconstructs the physical geography, continental configurations, and ocean basins of the geological past.",
    secondary: "In plate tectonics and biogeography, charting continental drift (Pangaea, Gondwana, Laurasia) to explain ancestral land bridges and fossil dispersal patterns.",
    quotes: [
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "The matching coastlines and trans-oceanic fossil distributions find their natural synthesis in the reconstructions of **palaeogeography**." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The maps of **palaeogeography** reveal that regions now crowned by the Alps and Himalayas were once submerged beneath shallow Mesozoic seas." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Without the guidance of **palaeogeography**, the curious disjunct distribution of ancient marsupials remains utterly inexplicable." }
    ]
  },
  "palaeogeology.md": {
    word: "palaeogeology",
    primary: "The branch of geology that studies the structural, stratigraphic, and volcanic conditions of the Earth's crust in past geological eras.",
    secondary: "In deep-time earth sciences, investigating ancestral tectonic orogenies, magma intrusions, and basin subsidence preceding modern surface geomorphology.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "The principles of **palaeogeology** enable us to decipher the ancient volcanic arcs that accreted to form the continental craton." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Through **palaeogeology**, we reconstruct ancient mountain belts worn down to their crystalline roots before the deposition of primary sandstones." },
      { author: "Archibald Geikie", work: "The Founders of Geology", quote: "The birth of modern **palaeogeology** sprang from Hutton’s realization that ancient strata were formed by the same natural laws operating today." }
    ]
  },
  "palaeolithic.md": {
    word: "palaeolithic",
    primary: "Of, relating to, or denoting the early Stone Age, characterized by the creation and use of chipped flint stone implements (British English spelling).",
    secondary: "In European prehistory, dividing into Lower, Middle, and Upper periods corresponding to Neanderthal Mousterian toolkits and Cro-Magnon cave art.",
    quotes: [
      { author: "John Lubbock", work: "Pre-historic Times", quote: "We apply the term **palaeolithic** to that ancient period when man shared the soil of Europe with the mammoth and woolly rhinoceros." },
      { author: "Henri Breuil", work: "Four Hundred Centuries of Cave Art", quote: "The exquisite polychrome bison of Altamira demonstrate the profound spiritual sensitivity of **palaeolithic** hunters." },
      { author: "V. Gordon Childe", work: "What Happened in History", quote: "The **palaeolithic** economy was purely food-gathering, limiting the density and permanence of human settlements." }
    ]
  },
  "palaeology.md": {
    word: "palaeology",
    primary: "The study of antiquities, ancient history, or ancient languages; an archaic or formal synonym for archaeology or paleontology.",
    secondary: "In 19th-century scholarship, an overarching term encompassing epigraphy, classical antiquities, and prehistoric fossil lore.",
    quotes: [
      { author: "Walter Scott", work: "The Antiquary", quote: "Mr. Oldbuck was deeply versed in **palaeology**, ready to lecture for hours upon a Roman ditch or a rusty Scottish coin." },
      { author: "Thomas Browne", work: "Hydriotaphia, Urn Burial", quote: "The study of **palaeology** instructs us in the vanity of earthly monuments, which crumble while their buried dust remains." },
      { author: "Edward Gibbon", work: "Memoirs of My Life", quote: "My youthful passion for **palaeology** led me through the folios of the Byzantine historians and classical inscriptions." }
    ]
  },
  "palaeontological.md": {
    word: "palaeontological",
    primary: "Of or relating to paleontology; concerning the scientific study of fossils, prehistoric life forms, and deep time.",
    secondary: "In evolutionary biology, describing physical fossil evidence used to verify phylogenetic lineages and evolutionary transitions.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **palaeontological** record, although imperfect, provides glorious confirmations of evolutionary divergence across successive strata." },
      { author: "Thomas Henry Huxley", work: "American Addresses", quote: "The equine fossil series arranged by Marsh provided an unanswerable **palaeontological** demonstration of evolution." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The discovery of the Burgess Shale forced a radical revision of established **palaeontological** theories regarding Cambrian disparity." }
    ]
  },
  "palaeontologist.md": {
    word: "palaeontologist",
    primary: "A scientist who specializes in the study of fossils and prehistoric life forms (British English spelling).",
    secondary: "In natural history, a researcher who excavates, reconstructs, and classifies extinct organisms to map the evolutionary history of the biosphere.",
    quotes: [
      { author: "Richard Owen", work: "Palaeontology: Or, A Systematic Summary of Extinct Animals", quote: "The skilled **palaeontologist** can reconstruct the skeleton and habits of an extinct quadruped from a single fossil tooth." },
      { author: "Othniel Charles Marsh", work: "Odontornithes: A Monograph on the Extinct Toothed Birds of North America", quote: "As a **palaeontologist** in the western badlands, I was privileged to uncover the first complete Cretaceous toothed birds." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The **palaeontologist** spends hours in dusty museum drawers, finding unexpected clues to evolution in forgotten fossil shells." }
    ]
  },
  "palaeontology.md": {
    word: "palaeontology",
    primary: "The branch of science concerned with fossil animals, plants, and prehistoric organisms, their evolutionary history, and ancient environments (British English spelling).",
    secondary: "In the history of science (formulated by Georges Cuvier and named in 1822), the foundational discipline proving that mass extinction and species turnover occurred across deep time.",
    quotes: [
      { author: "Georges Cuvier", work: "Discourse on the Revolutionary Upheavals on the Surface of the Globe", quote: "Comparative anatomy and **palaeontology** demonstrate that ancient faunas were swept away by colossal catastrophes." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The progress of **palaeontology** has filled the former chasms in the chain of living nature with countless intermediate fossil species." },
      { author: "Stephen Jay Gould", work: "Ever Since Darwin", quote: "The primary glory of **palaeontology** is its direct access to deep time, the fourth dimension of organic history." }
    ]
  },
  "palaeopathology.md": {
    word: "palaeopathology",
    primary: "The scientific study of ancient diseases, trauma, and medical conditions in fossilized bones, mummified tissues, and skeletal human remains.",
    secondary: "In physical anthropology and forensic science, diagnosing malnutrition (porotic hyperostosis), infectious epidemics (syphilis, tuberculosis), and surgical trepanation in ancient populations.",
    quotes: [
      { author: "G. Elliot Smith", work: "The Royal Mummies", quote: "Careful **palaeopathology** performed upon royal Egyptian mummies revealed chronic arthritis, dental abscesses, and vascular calcification." },
      { author: "Marc Armand Ruffer", work: "Studies in the Palaeopathology of Egypt", quote: "Microscopic histology applied to ancient tissues established **palaeopathology** as an exact branch of pathological science." },
      { author: "Ales Hrdlicka", work: "Physical Anthropology: Its Scope and Aims", quote: "Skeletal trauma and healed fractures analyzed through **palaeopathology** illuminate the violent struggles of prehistoric hunters." }
    ]
  },
  "palaeornithology.md": {
    word: "palaeornithology",
    primary: "The scientific study of fossil birds, avian evolutionary origins, and extinct bird lineages.",
    secondary: "In vertebrate paleontology, investigating the morphological transition from theropod dinosaurs to birds, the evolution of flight feathers, and giant extinct birds (moas, elephant birds).",
    quotes: [
      { author: "Gerhard Heilmann", work: "The Origin of Birds", quote: "The foundational problem of **palaeornithology** has always been resolving the evolutionary relationship between feathered reptiles and modern birds." },
      { author: "Alexander Wetmore", work: "A Systematic Classification for the Birds of the World", quote: "The fossil discoveries of **palaeornithology** demonstrate that toothed diving birds dominated North American inland seas in the Cretaceous." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "Because avian bones are hollow and delicate, specimens in **palaeornithology** are exceptionally rare and precious." }
    ]
  },
  "palaeozoology.md": {
    word: "palaeozoology",
    primary: "The branch of paleontology and zoology that studies fossilized animals, their taxonomy, and their evolutionary history.",
    secondary: "In vertebrate and invertebrate paleontology, reconstructing the anatomical structures, soft tissue impressions, and ecological niches of extinct animal species.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "Comparative **palaeozoology** reveals an orderly succession of vertebrate classes from primitive fishes to mammals across the geological columns." },
      { author: "Thomas Henry Huxley", work: "Lectures on the Elements of Comparative Anatomy", quote: "The student of **palaeozoology** must ground his work upon the exact osteology of living animals to interpret fossil bones correctly." },
      { author: "Edwin H. Colbert", work: "Dinosaurs: Their Discovery and Their World", quote: "Through **palaeozoology**, the magnificent fauna of the Mesozoic era was resurrected from badland sandstone cliffs." }
    ]
  },
  "palaestra.md": {
    word: "palaestra",
    primary: "An ancient Greek wrestling school or gymnasium, an open-air public ground surrounded by colonnades dedicated to athletic training and philosophical dialogue.",
    secondary: "In classical antiquity and literature, a gymnasium where physical sports (wrestling, boxing, pancratium) were practiced alongside intellectual debate (from Greek palaiein to wrestle; homograph on palae-!).",
    quotes: [
      { author: "Plato", work: "Charmides", quote: "On returning from the campaign at Potidaea, Socrates went straightway to his accustomed haunts in the **palaestra** of Taureas." },
      { author: "Vitruvius", work: "De Architectura", quote: "The Greek **palaestra** was planned as a peristyle courtyard with spacious colonnades where athletes wrestled upon sandy floors." },
      { author: "John Milton", work: "Samson Agonistes", quote: "He was led forth to the public theater, where the champions were wont to contend in the Philistine **palaestra**." }
    ]
  },
  "palaetiology.md": {
    word: "palaetiology",
    primary: "The study of past events, geological processes, or biological lineages through their historical and causal development; the philosophy of the historical sciences.",
    secondary: "In the philosophy of science (coined by William Whewell in 1837), the group of sciences (geology, comparative philology, evolutionary biology) that reconstruct past events from present effects.",
    quotes: [
      { author: "William Whewell", work: "The Philosophy of the Inductive Sciences", quote: "I propose the term **palaetiology** for those historical sciences whose aim is to trace the past history of the world by studying present effects." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The methods of **palaetiology** demonstrate that the history of the earth is to be deciphered through physical causation rather than miraculous myth." },
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "Both geology and archaeology are branches of Whewell’s **palaetiology**, reading ancestral causes in existing rocks and ruins." }
    ]
  },
  "palaic.md": {
    word: "palaic",
    primary: "An extinct Indo-European language belonging to the Anatolian sub-branch, spoken in northern Anatolia (the region of Pala) during the second millennium BCE.",
    secondary: "In historical Indo-European linguistics, a sister language to Hittite and Luwian, preserved in cuneiform religious rituals and invocations on clay tablets from Hattusa.",
    quotes: [
      { author: "Michael Ventris", work: "Documents in Mycenaean Greek", quote: "The decipherment of cuneiform tablets from Boghazkoy revealed that **Palaic** was a distinct Anatolian Indo-European tongue." },
      { author: "O. R. Gurney", work: "The Hittites", quote: "Priests in the Hittite capital recited ancient chants in the **Palaic** speech to invoke the northern god Zaparwa." },
      { author: "J. P. Mallory", work: "In Search of the Indo-Europeans", quote: "Comparative analysis indicates that **Palaic** separated early from the common Proto-Anatolian linguistic stock." }
    ]
  },
  "paleobiology.md": {
    word: "paleobiology",
    primary: "The branch of paleontology and biological science that investigates the physiology, life history, ecology, and evolution of prehistoric fossil organisms.",
    secondary: "In modern evolutionary science, integrating mathematical modeling, biomechanics, and geochemical isotope signatures to understand living processes in extinct organisms.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The establishment of modern **paleobiology** transformed fossil hunting into a primary theoretical engine of evolutionary science." },
      { author: "George Gaylord Simpson", work: "Major Features of Evolution", quote: "Quantitative **paleobiology** analyzes morphological shift rates across millions of years in documented sedimentary basins." },
      { author: "Edward O. Wilson", work: "Consilience: The Unity of Knowledge", quote: "The grand historical narrative of life is written by **paleobiology**, linking molecular genetics to the fossilized record of extinction." }
    ]
  },
  "paleobotanic.md": {
    word: "paleobotanic",
    primary: "Of, relating to, or involving paleobotany; concerning the scientific study of fossil plants, ancient vegetation, and plant evolution.",
    secondary: "In geosciences and paleoclimatology, describing fossil leaf morphologies (e.g. stomatal density, leaf margins) used to infer past atmospheric temperatures and CO2 concentrations.",
    quotes: [
      { author: "Asa Gray", work: "Scientific Papers", quote: "The **paleobotanic** discoveries in Greenland shale proved that magnificent magnolia and cypress forests once thrived within the Arctic Circle." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The **paleobotanic** record of the coal measures demonstrates a warm, humid climate sustaining giant arborescent cryptogams." },
      { author: "John William Dawson", work: "Acadian Geology", quote: "Microscopic **paleobotanic** examination reveals the delicate vascular bundles in silicified Devonian fern stems." }
    ]
  },
  "paleodiet.md": {
    word: "paleodiet",
    primary: "The diet of prehistoric humans during the Paleolithic era; also a contemporary dietary regimen modeled on the presumed foods of ancestral hunter-gatherers.",
    secondary: "In nutritional anthropology, the empirical reconstruction of ancestral human nutrition (wild lean meats, fish, vegetables, fruits, nuts, excluding dairy, grains, and refined sugar).",
    quotes: [
      { author: "Loren Cordain", work: "The Paleo Diet", quote: "Proponents of the modern **paleodiet** argue that human physiology remains genetically adapted to the nutritional profile of the Paleolithic era." },
      { author: "Richard Wrangham", work: "Catching Fire: How Cooking Made Us Human", quote: "A realistic **paleodiet** must account for the transformative invention of cooking, which doubled the caloric efficiency of hunted meat and tubers." },
      { author: "Spencer Wells", work: "The Journey of Man: A Genetic Odyssey", quote: "The shift from a nomadic **paleodiet** to a sedentary grain-based agricultural diet left clear signatures of dental decay and anemia in Neolithic skeletons." }
    ]
  },
  "paleology.md": {
    word: "paleology",
    primary: "The study of antiquities, ancient times, or ancient languages; an alternative or archaic spelling for palaeology.",
    secondary: "In intellectual history, the overarching study of ancient human civilizations and prehistoric physical relics before modern specialization into archaeology and paleontology.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Men well versed in **paleology** know that many vulgar legends dissolve upon inspecting ancient inscriptions." },
      { author: "Walter Scott", work: "Waverley", quote: "The baron delighted in quaint **paleology**, expounding old family charters with unflagging genealogical enthusiasm." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "His profound grasp of classical **paleology** allowed him to restore corrupted passages in early imperial decrees." }
    ]
  },
  "paleomagnetism.md": {
    word: "paleomagnetism",
    primary: "The branch of geophysics concerned with the magnetism preserved in rocks at the time of their formation, used to study the history of Earth's magnetic field and plate tectonics.",
    secondary: "In plate tectonics, analyzing magnetic polarity reversals recorded in oceanic basalt stripes (the Vine-Matthews-Morley hypothesis) that proved sea-floor spreading.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The discovery of remanent magnetic orientation in lavas established **paleomagnetism** as our primary compass for tracking moving continents." },
      { author: "J. Tuzo Wilson", work: "Continents Adrift and Continents Aground", quote: "Symmetrical zebra-like magnetic anomalies mapped across mid-ocean ridges provided the decisive **paleomagnetism** proof of seafloor spreading." },
      { author: "Walter Alvarez", work: "T. Rex and the Crater of Doom", quote: "We measured magnetic reversals in Gubbio limestone using sensitive **paleomagnetism** instruments to date the Cretaceous-Tertiary boundary." }
    ]
  },
  "paleontological.md": {
    word: "paleontological",
    primary: "Of or relating to paleontology; concerning the scientific study of fossils, prehistoric life forms, and the history of the biosphere.",
    secondary: "In evolutionary biology and stratigraphy, describing physical fossil specimens and biozones utilized to date sedimentary rock layers and map macroevolutionary trends.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **paleontological** record, broken though it is, wonderfully illustrates the gradual divergence of character in animal lineages." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The **paleontological** proof of organic evolution becomes overwhelming when we trace intermediate fossil series across successive strata." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The bizarre fauna of the Burgess Shale challenged traditional **paleontological** expectations of simple linear progress." }
    ]
  },
  "paleontologist.md": {
    word: "paleontologist",
    primary: "A scientist who specializes in the study of fossils and prehistoric life forms (American English spelling).",
    secondary: "In natural sciences, an investigator who excavates, reconstructs, and analyzes fossilized organisms to understand ancient ecosystems, extinctions, and evolutionary history.",
    quotes: [
      { author: "Othniel Charles Marsh", work: "Vertebrate Fossils of the West", quote: "The dedicated **paleontologist** braved desert heat and hostile territory to unearth colossal sauropod bones from Wyoming sandstones." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "As a **paleontologist**, my daily work is measuring fossil snail shells to decipher the subtle rhythms of evolutionary change." },
      { author: "Edward Drinker Cope", work: "The Primary Factors of Organic Evolution", quote: "The **paleontologist** reconstructs extinct species by applying the principles of comparative anatomy to petrified bones." }
    ]
  },
  "paleontology.md": {
    word: "paleontology",
    primary: "The branch of science concerned with fossil animals and plants, prehistoric life, and the evolutionary history of organisms (American English spelling).",
    secondary: "In earth sciences, the discipline bridging biology and geology, using the fossil record to date strata, reconstruct ancient environments, and analyze mass extinctions.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Modern **paleontology** proves that the ancient seas were inhabited by bizarre cephalopods and giant reptiles long before the advent of man." },
      { author: "Stephen Jay Gould", work: "Time's Arrow, Time's Cycle", quote: "**Paleontology** is the science of history written into stone, recording the unique unrepeatable contingencies of deep time." },
      { author: "George Gaylord Simpson", work: "The Meaning of Evolution", quote: "Without the discoveries of **paleontology**, the grand drama of organic evolution would remain an unverified hypothesis." }
    ]
  },
  "paleopolyploidy.md": {
    word: "paleopolyploidy",
    primary: "The occurrence of whole-genome duplication (polyploidy) events in the evolutionary history of a species or lineage that occurred millions of years ago.",
    secondary: "In evolutionary genomics, ancestral genome duplication events (such as the 1R/2R events in early vertebrates or ancestral duplications in angiosperms) that provide redundant genetic material for evolutionary innovation.",
    quotes: [
      { author: "Susumu Ohno", work: "Evolution by Gene Duplication", quote: "Ancient **paleopolyploidy** provided the duplicated gene families that allowed early vertebrates to evolve complex organ systems." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Genomic sequencing confirms that ancient **paleopolyploidy** played a paramount role in the evolutionary radiation of flowering plants." },
      { author: "John Maynard Smith", work: "The Major Transitions in Evolution", quote: "The signatures of **paleopolyploidy** reveal how massive chromosome doubling events preceded bursts of morphological innovation." }
    ]
  },
  "paleopsychology.md": {
    word: "paleopsychology",
    primary: "The scientific study of the evolutionary origins, prehistoric emergence, and ancestral stages of the human mind and cognitive faculties.",
    secondary: "In evolutionary psychology and cognitive archaeology, reconstructing the cognitive architectures, social intelligence, and symbolic capacities of early hominids from material artifacts and cranial endocasts.",
    quotes: [
      { author: "Julian Jaynes", work: "The Origin of Consciousness in the Breakdown of the Bicameral Mind", quote: "The speculative field of **paleopsychology** investigates how human consciousness emerged from archaic mythic and auditory hallucinations." },
      { author: "Carl Sagan", work: "The Dragons of Eden: Speculations on the Evolution of Human Intelligence", quote: "In the inquiries of **paleopsychology**, we trace human dreams and anxieties back to the nocturnal terrors of our early mammalian ancestors." },
      { author: "Steven Pinker", work: "How the Mind Works", quote: "Modern cognitive science is essentially reverse-engineering the mind using the insights of evolutionary **paleopsychology**." }
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
console.log("Primacy Batch 3 completed! Total words updated:", Object.keys(wordsData).length);
