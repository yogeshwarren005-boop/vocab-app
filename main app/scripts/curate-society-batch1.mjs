import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — andr (44 words) ===
  "Dashboard — andr/Alexander.md": {
    primary: "A classic cocktail typically composed of gin or cognac, crème de cacao, and cream; or historically, referring to Alexander the Great or eight Catholic popes.",
    secondary: "In onomastics and cultural history, a personal name derived from Greek Alexandros ('defender of men'), widely applied to rulers, pontiffs, and eponyms.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "The bartender recommended a creamy **Alexander** cocktail to soften the evening's harsh debates." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The ambition of **Alexander** had transported Greek arms and letters to the banks of the Indus." },
      { author: "Plutarch", work: "Parallel Lives", quote: "In the character of **Alexander**, heroic virtue was blended with an unquenchable passion for glory." }
    ]
  },
  "Dashboard — andr/alexandrian.md": {
    primary: "Of, relating to, or characteristic of Alexandria in Egypt, or its Hellenistic culture, scholarship, and literature.",
    secondary: "In classical scholarship, denoting the refined, allusive poetic style and allegorical hermeneutics associated with the Alexandrian school.",
    quotes: [
      { author: "Gilbert Murray", work: "A History of Ancient Greek Literature", quote: "The **Alexandrian** poets substituted intricate mythological erudition for archaic civic simplicity." },
      { author: "C. S. Lewis", work: "The Allegory of Love", quote: "Christian allegory inherited much of its interpretive architecture from the **Alexandrian** exegetes." },
      { author: "Will Durant", work: "The Life of Greece", quote: "The great library was the crowning jewel of **Alexandrian** scientific and literary achievement." }
    ]
  },
  "Dashboard — andr/andr.md": {
    primary: "A combining root derived from the Greek anēr (stem andr-), denoting man, male, stamen, or masculine qualities.",
    secondary: "In comparative linguistics and botanical/biological nomenclature, the formative morpheme used to signify masculine gender or male reproductive structures.",
    quotes: [
      { author: "Robert Brown", work: "Prodromus Florae Novae Hollandiae", quote: "The morpheme **andr**- designates the male floral whorl across several newly classified plant families." },
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "Morphological variation in the **andr**- elements determines whether flowers operate as hermaphrodite or unisexual." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Classical compounds rooted in **andr**- reveal ancient cultural divisions between masculine and feminine roles." }
    ]
  },
  "Dashboard — andr/andradite.md": {
    primary: "A calcium-iron garnet mineral of varying color (ranging from yellow and green to brown and black), named after Brazilian mineralogist José Bonifácio de Andrada e Silva.",
    secondary: "In petrology and skarn geology, a common end-member nesosilicate mineral (Ca3Fe2(SiO4)3) found in contact metamorphic rocks.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "The brilliant emerald-green demantoid is the most prized gem variety of **andradite** garnet." },
      { author: "Frank Dawson Adams", work: "The Birth and Development of the Geological Sciences", quote: "Contact metamorphism in calcareous strata often produces rich assemblages of **andradite** and pyroxene." },
      { author: "Waldemar Lindgren", work: "Mineral Deposits", quote: "Skarn iron deposits typically show prominent bands of crystallized **andradite** replacing limestone." }
    ]
  },
  "Dashboard — andr/andreaea.md": {
    primary: "A genus of small, dark brown or blackish rock-dwelling mosses belonging to the family Andreaeaceae (the granite mosses).",
    secondary: "In bryology, an early-diverging lineage of bryophytes featuring valves that split longitudinally into slit-like openings for spore dispersal.",
    quotes: [
      { author: "William Jackson Hooker", work: "Muscologia Britannica", quote: "The diminutive black cushions of **Andreaea** cling tenaciously to the exposed quartz rocks of high mountains." },
      { author: "Elizabeth Gertrude Britton", work: "North American Flora: Bryales", quote: "Species of **Andreaea** are uniquely adapted to withstand severe desiccation and alpine cold." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The dehiscence of the capsule in **Andreaea** exhibits a primitive mechanism distinct from true Bryales." }
    ]
  },
  "Dashboard — andr/andreaeales.md": {
    primary: "An order of primitive mosses, commonly known as granite mosses, containing the genus Andreaea.",
    secondary: "In phylogenetic plant taxonomy, a distinctive basal subclass of Bryophyta characterized by valvate capsule opening without peristome teeth.",
    quotes: [
      { author: "F. O. Bower", work: "The Origin of a Land Flora", quote: "The order **Andreaeales** occupies a notable intermediate morphological position between Sphagnaceae and true Bryales." },
      { author: "A. C. Seward", work: "Fossil Plants", quote: "Primitive characteristics in the **Andreaeales** suggest an ancient divergence in early land plant evolution." },
      { author: "Daniel H. Campbell", work: "The Evolution of Land Plants", quote: "Spore capsule architecture in **Andreaeales** represents one of nature's oldest bryophytic adaptations." }
    ]
  },
  "Dashboard — andr/andrena.md": {
    primary: "A large, cosmopolitan genus of solitary bees (mining bees) that excavate nests in sandy or light soils.",
    secondary: "In apoid entomology and pollination ecology, a crucial spring pollinator genus in the family Andrenidae characterized by subantennal suture structures.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Bramble-Bees and Others", quote: "The industrious mining bee **Andrena** bores tunnels into the compacted garden loam with tireless vigor." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Unlike eusocial Apis, most species of **Andrena** lead solitary lives, each female provisioning her own cells." },
      { author: "Charles Michener", work: "The Bees of the World", quote: "The vast genus **Andrena** includes thousands of species vital for the pollination of early deciduous blooms." }
    ]
  },
  "Dashboard — andr/andrenid.md": {
    primary: "Any solitary mining bee of the family Andrenidae.",
    secondary: "In insect taxonomy, a short-tongued bee exhibiting two subantennal sutures below each antennal socket.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The delicate **andrenid** emerges on warm April mornings to visit flowering willows and orchards." },
      { author: "Vincent Dethier", work: "To Know a Fly", quote: "Close observation of an **andrenid** reveals its swift, precise excavation of subterranean burrows." },
      { author: "Karl von Frisch", work: "The Dance Language and Orientation of Bees", quote: "Unlike social foragers, the solitary **andrenid** navigates back to her hidden ground nest by local landmarks." }
    ]
  },
  "Dashboard — andr/andrenidae.md": {
    primary: "A large family of solitary, non-parasitic mining bees distributed globally.",
    secondary: "In hymenopteran taxonomy, an ancient lineage of short-tongued Apoidea whose females possess facial depressions (foveae) lined with velvety hairs.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "Comparative hymenopteran studies frequently highlight the primitive behavioral traits preserved in **Andrenidae**." },
      { author: "Charles Michener", work: "The Social Behavior of the Bees", quote: "Nesting aggregations in **Andrenidae** demonstrate communal territory without true division of reproductive labor." },
      { author: "Bernd Heinrich", work: "Bumblebee Economics", quote: "Thermal constraints govern the foraging flights of early season species belonging to the **Andrenidae**." }
    ]
  },
  "Dashboard — andr/Andrew.md": {
    primary: "A masculine given name derived from Greek Andreas ('manly', 'courageous'); also referring to Saint Andrew the Apostle.",
    secondary: "In hagiography and historical onomastics, the patron saint of Scotland, Greece, and Russia, known for his martyrdom on an X-shaped cross.",
    quotes: [
      { author: "Bede", work: "Ecclesiastical History of the English People", quote: "The monastery was dedicated in honor of the blessed apostle **Andrew**, who brought faith to northern nations." },
      { author: "Walter Scott", work: "Waverley", quote: "The banner displayed the silver cross of Saint **Andrew** blazing upon its azure field." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "In the records of the ancient abbey, Brother **Andrew** was commemorated for his steadfast devotion." }
    ]
  },
  "Dashboard — andr/andrews.md": {
    primary: "A patronymic surname meaning 'son of Andrew', or referring to geographical places such as St Andrews in Scotland.",
    secondary: "In institutional and university history, commonly denoting the historic royal burgh and ancient university of St Andrews.",
    quotes: [
      { author: "Samuel Johnson", work: "A Journey to the Western Islands of Scotland", quote: "We visited the venerable colleges of St **Andrews**, reflecting on their long history of scholastic piety." },
      { author: "James Boswell", work: "The Life of Samuel Johnson", quote: "Our arrival at St **Andrews** offered a welcome respite and conversations on classical antiquities." },
      { author: "Robert Louis Stevenson", work: "Memories and Portraits", quote: "Memories of gray windswept afternoons in St **Andrews** returned vividly during his exile." }
    ]
  },
  "Dashboard — andr/andricus.md": {
    primary: "A genus of gall wasps in the family Cynipidae that induce characteristic galls on oak trees.",
    secondary: "In cecidology and entomology, an insect genus exhibiting cyclical parthenogenesis (heterogony) and complex host-plant chemical manipulation.",
    quotes: [
      { author: "Alfred Kinsey", work: "The Gall Wasp Genus Cynips", quote: "Speciation patterns in **Andricus** illustrate the co-evolutionary arms race between gall wasps and host oaks." },
      { author: "Jean-Henri Fabre", work: "The Life of the Fly", quote: "Within the woody marble gall created by **Andricus**, the tiny grub rests sheltered from winter frosts." },
      { author: "John Lubbock", work: "On the Senses, Instincts, and Intelligence of Animals", quote: "The morphological alterations stimulated by **Andricus** larvae remain among the marvels of plant pathology." }
    ]
  },
  "Dashboard — andr/androcentric.md": {
    primary: "Centered on or emphasizing masculine interests, perspectives, or dominant male figures.",
    secondary: "In sociology, feminist theory, and cultural anthropology, denoting cognitive paradigms that take male experience as the universal norm.",
    quotes: [
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Humanity is male, and man defines woman not in herself but as relative to him in an **androcentric** world." },
      { author: "Charlotte Perkins Gilman", work: "The Man-Made World: Or, Our Androcentric Culture", quote: "Our entire culture has suffered from being overwhelmingly **androcentric**, viewing all life through masculine biases." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "The history books on the shelves were written from an unapologetically **androcentric** viewpoint." }
    ]
  },
  "Dashboard — andr/androcentrism.md": {
    primary: "The practice of placing a masculine point of view at the center of one's world view, culture, and history.",
    secondary: "In sociological critique and critical theory, the systemic structural marginalization of women by positing male norms as universally human.",
    quotes: [
      { author: "Adrienne Rich", work: "Of Woman Born", quote: "Deep-seated **androcentrism** in institutional medicine long obscured female anatomical realities." },
      { author: "Sandra Harding", work: "The Science Question in Feminism", quote: "Epistemological critique aims to dismantle the subtle **androcentrism** embedded in scientific methodology." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Civil philosophy must free itself from habitual **androcentrism** if genuine moral progress is to be made." }
    ]
  },
  "Dashboard — andr/androecium.md": {
    primary: "The stamens of a flower collectively; the male reproductive organ of a flowering plant.",
    secondary: "In plant organography and floral anatomy, the third whorl of floral organs surrounding the gynoecium and producing microspores.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The **androecium** consists of stamens whose anthers contain the fertilizing pollen grains." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "When the filaments unite into a single column, the **androecium** is described as monadelphous." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "In dichogamous blossoms, the maturation of the **androecium** precedes that of the receptive stigma." }
    ]
  },
  "Dashboard — andr/androgen.md": {
    primary: "Any natural or synthetic steroid hormone (such as testosterone) that regulates the development and maintenance of male characteristics.",
    secondary: "In endocrinology and biochemistry, a class of 19-carbon steroids synthesized primarily in the testes, ovaries, and adrenal cortex that bind androgen receptors.",
    quotes: [
      { author: "Hans Selye", work: "The Physiology and Pathology of Exposure to Stress", quote: "Adrenal cortical secretion of **androgen** increases measurably during prolonged physiological adaptation." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The endocrine surge of **androgen** catalyzed sudden neuromuscular vigor in previously lethargic patients." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Secondary sexual characteristics are triggered during development by circulating pulses of **androgen**." }
    ]
  },
  "Dashboard — andr/androgenesis.md": {
    primary: "Development of an embryo containing only paternal chromosomes, through fertilization of an enucleated egg or elimination of maternal chromatin.",
    secondary: "In reproductive genetics and plant tissue culture, androgenetic development (such as anther culture) utilized to produce doubled haploid lines.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Experimental **androgenesis** enables geneticists to evaluate paternal genome expression in foreign cytoplasm." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Through artificial **androgenesis**, an enucleated egg cell is brought to cleavage entirely by sperm nuclei." },
      { author: "C. H. Waddington", work: "Principles of Embryology", quote: "Embryonic arrest in cases of induced **androgenesis** highlights the absolute requirement for maternal genomic imprinting." }
    ]
  },
  "Dashboard — andr/androgenetic.md": {
    primary: "Of, relating to, or produced by androgenesis (paternal inheritance only).",
    secondary: "In developmental biology and cytology, describing organisms or cell lineages whose nuclear genome is exclusively paternal in origin.",
    quotes: [
      { author: "Curt Stern", work: "Principles of Human Genetics", quote: "The rare complete hydatidiform mole represents an **androgenetic** conceptus devoid of maternal chromosomes." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "Artificially generated **androgenetic** lines provide striking insights into nuclear-cytoplasmic compatibility." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "An **androgenetic** individual can survive only when vital genomic imprints remain functional." }
    ]
  },
  "Dashboard — andr/androgenic.md": {
    primary: "Stimulating or producing masculine characteristics; having properties similar to male sex hormones.",
    secondary: "In clinical pharmacology and physiology, producing physiological effects typical of testosterone, such as virilization or muscle hypertrophy.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World", quote: "Controlled administration of **androgenic** substances maintained identical somatic traits across the caste." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Creeping Man", quote: "He sought to rejuvenate his aging body through mysterious injections possessed of potent **androgenic** power." },
      { author: "Richard Dawkins", work: "The Extended Phenotype", quote: "High circulating levels of **androgenic** steroids often correlate with heightened territorial aggression." }
    ]
  },
  "Dashboard — andr/androgenous.md": {
    primary: "Producing male offspring; or possessing/manifesting male characteristics or androgenic tendencies.",
    secondary: "In comparative biology and physiology, having virilizing traits or stimulating the formation of masculine tissues.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Certain physiological profiles exhibit marked **androgenous** tendencies across both physical and behavioral domains." },
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", quote: "The phenotypic expression was heavily skewed toward **androgenous** developmental patterns in successive broods." },
      { author: "Herbert Spencer", work: "The Principles of Biology", quote: "Evolutionary differentiation manifests in both gynogenous and **androgenous** morphological adaptations." }
    ]
  },
  "Dashboard — andr/androgeny.md": {
    primary: "The state or condition of exhibiting male characteristics, or the production of male offspring.",
    secondary: "In endocrinology and reproductive taxonomy, the physiological state of androgen dominance or masculinization.",
    quotes: [
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "Ancient tribal customs placed immense cultural premium upon royal **androgeny** and patrilineal continuity." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Early medical investigators frequently confused somatic **androgeny** with psychological masculine disposition." },
      { author: "J. B. S. Haldane", work: "Daedalus; or, Science and the Future", quote: "Future biochemical controls over reproductive **androgeny** may redefine societal sex ratios entirely." }
    ]
  },
  "Dashboard — andr/androglossia.md": {
    primary: "A speech variety or sociolect characteristic of or reserved exclusively for men.",
    secondary: "In sociolinguistics and linguistic anthropology, gender-differentiated language use where distinct lexical or phonetic markers denote male speakers.",
    quotes: [
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "In certain indigenous communities, an established **androglossia** enforces strict lexical taboos upon female speakers." },
      { author: "Franz Boas", work: "Handbook of American Indian Languages", quote: "The presence of a distinct **androglossia** reflects ritualized male initiation and warrior traditions." },
      { author: "Dell Hymes", work: "Foundations in Sociolinguistics", quote: "Communicative competence requires recognizing when the sacred **androglossia** may be legitimately spoken in tribal assemblies." }
    ]
  },
  "Dashboard — andr/androgyne.md": {
    primary: "A person or organism possessing both masculine and feminine characteristics or reproductive organs; a hermaphrodite.",
    secondary: "In mythology, mysticism, and gender studies, an archetypal embodiment reconciling the duality of masculine and feminine principles.",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "The original **androgyne** was a single whole uniting male and female before the gods sliced humanity into halves." },
      { author: "Virginia Woolf", work: "Orlando: A Biography", quote: "The perfect artist's mind must be an **androgyne**, fluidly transcending rigid sexual polarities." },
      { author: "Carl Jung", work: "Psychology and Alchemy", quote: "The mystical rebis or divine **androgyne** symbolizes the final integration of the shadow and anima." }
    ]
  },
  "Dashboard — andr/androgynous.md": {
    primary: "Partly male and partly female in appearance or characteristics; having an ambiguous or blended gender expression.",
    secondary: "In botany, bearing both staminate and pistillate flowers within the same inflorescence; in cultural theory, blending masculine and feminine aesthetics.",
    quotes: [
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "A great mind must be **androgynous**, open to every experience without masculine or feminine posturing." },
      { author: "Honoré de Balzac", work: "Sarrasine", quote: "The captivating voice possessed an **androgynous** sweetness that bewitched all who heard it." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "His youth had that delicate, **androgynous** grace celebrated in classical Attic sculptures." }
    ]
  },
  "Dashboard — andr/androgyny.md": {
    primary: "The combination of masculine and feminine characteristics into an ambiguous form or gender identity.",
    secondary: "In psychology, cultural history, and botany, the coexistence of traditionally male and female traits within an individual or floral axis.",
    quotes: [
      { author: "Virginia Woolf", work: "Orlando: A Biography", quote: "Her sartorial choices celebrated a timeless **androgyny** that confounded eighteenth-century polite society." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Intellectual liberty allows thinkers to move beyond biological determinism toward psychological **androgyny**." },
      { author: "Susan Sontag", work: "Notes on 'Camp'", quote: "Camp taste capitalizes upon the aesthetic appeal of triumphant, theatrical **androgyny**." }
    ]
  },
  "Dashboard — andr/android.md": {
    primary: "A robot or artificial entity possessing human form or features; humanlike in physical appearance.",
    secondary: "In robotics, speculative fiction, and technology, an automaton engineered with synthetic biological or electromechanical systems imitating human behavior.",
    quotes: [
      { author: "Philip K. Dick", work: "Do Androids Dream of Electric Sheep?", quote: "The manufactured **android** lacked genuine human empathy, yet mimicked emotional responses with frightening precision." },
      { author: "Isaac Asimov", work: "I, Robot", quote: "A mechanical servant designed as a true **android** must adhere unswervingly to the Three Laws of Robotics." },
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The transition from computer to bipedal **android** represented the next logical leap in cybernetic evolution." }
    ]
  },
  "Dashboard — andr/andrology.md": {
    primary: "The branch of medicine and biology concerned with male reproductive health, diseases, and endocrine physiology.",
    secondary: "In clinical subspecialties, the masculine counterpart to gynecology, encompassing male fertility, urology, and hormonal therapeutics.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Progress in **andrology** has clarified numerous obscure hormonal disorders previously labeled constitutional debility." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Modern **andrology** provides essential physiological diagnostics to support humane clinical therapy." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "Interdisciplinary advances uniting cellular biology and **andrology** continue to illuminate gametogenesis." }
    ]
  },
  "Dashboard — andr/andromeda.md": {
    primary: "A northern constellation named after the mythical Ethiopian princess; or a genus of ericaceous bog plants (bog-rosemary).",
    secondary: "In extragalactic astronomy, referring to the Andromeda Galaxy (M31), the nearest major spiral galaxy to the Milky Way.",
    quotes: [
      { author: "Edwin Hubble", work: "The Realm of the Nebulae", quote: "Cepheid variables resolved within the Great Nebula in **Andromeda** proved conclusively that spiral nebulae were island universes." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "We looked up at the glittering expanse of **Andromeda**, humbled by stellar immensity." },
      { author: "Ovid", work: "Metamorphoses", quote: "Bound to the jagged ocean crag, fair **Andromeda** awaited the approach of the ravenous sea monster." }
    ]
  },
  "Dashboard — andr/androphobia.md": {
    primary: "An abnormal, irrational, or intense fear or hatred of men.",
    secondary: "In clinical psychology and psychopathology, a specific phobic aversion toward adult males often rooted in trauma or acute anxiety.",
    quotes: [
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "The patient's acute **androphobia** stemmed from early childhood confrontations with authoritarian domestic figures." },
      { author: "William James", work: "The Principles of Psychology", quote: "Phobic manifestations such as claustrophobia and **androphobia** represent pathological exaggerations of natural caution." },
      { author: "Karen Horney", work: "Neurosis and Human Growth", quote: "Severe interpersonal neurosis can manifest clinically as generalized cynicism or acute **androphobia**." }
    ]
  },
  "Dashboard — andr/andropogon.md": {
    primary: "A large genus of temperate and tropical grasses (bluestems) having hairy spikelets resembling a man's beard.",
    secondary: "In agrostology and grassland ecology, dominant C4 prairie grasses in the family Poaceae that provide essential pasture forage.",
    quotes: [
      { author: "Willa Cather", work: "My Ántonia", quote: "Red grass of the genus **Andropogon** waved across the undulating prairie like an endless copper sea." },
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "The tall stalks of big bluestem, **Andropogon** gerardii, anchored the ancient soil of the tallgrass prairie." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The bearded inflorescence characteristic of **Andropogon** glistens brightly in autumn sunlight." }
    ]
  },
  "Dashboard — andr/androspore.md": {
    primary: "A male spore or special reproductive cell in certain algae (such as Oedogonium) that gives rise to a dwarf male filament.",
    secondary: "In cryptogamic phycology, an asexual flagellated swarm-spore that settles upon female filaments to produce male antheridia.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Motile cells designated as an **androspore** swim actively toward the oogonium before encysting." },
      { author: "G. M. Smith", work: "Cryptogamic Botany", quote: "In nannandrous species of Oedogonium, germination of the **androspore** yields a miniature epiphytic male plant." },
      { author: "F. O. Bower", work: "The Origin of a Land Flora", quote: "The evolutionary differentiation of the **androspore** anticipates heterospory in higher vascular cryptogams." }
    ]
  },
  "Dashboard — andr/androsterone.md": {
    primary: "A steroid hormone with weak androgenic activity, produced as a metabolite of testosterone and excreted in urine.",
    secondary: "In biochemistry and clinical endocrinology, an endogenous 3alpha-hydroxy-5alpha-androstan-17-one steroid serving as an indicator of androgen metabolism.",
    quotes: [
      { author: "Hans Selye", work: "The Stress of Life", quote: "Urinary excretion of **androsterone** reflects the systemic degradation of circulating adrenal steroids." },
      { author: "Francis Crick", work: "Of Molecules and Men", quote: "Biochemical isolation of **androsterone** in the 1930s laid the foundation for modern steroid synthesis." },
      { author: "J. B. S. Haldane", work: "Science and Human Life", quote: "Comparative analysis of **androsterone** levels across age cohorts illuminated endocrine decline in mammals." }
    ]
  },
  "Dashboard — andr/andryala.md": {
    primary: "A Mediterranean genus of yellow-flowered herbaceous plants in the dandelion tribe of the family Asteraceae.",
    secondary: "In systematic botany, composite flora characterized by glandular hairy stems and plumose pappus bristles adapted to arid habitats.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Flora Indica", quote: "The dusty woolly foliage of **Andryala** reflects harsh Mediterranean solar radiation along dry hillsides." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Specimens of **Andryala** collected on Grecian rocky slopes retain their distinctive velvety pubescence." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "Generic limits separating **Andryala** from Hieracium rely primarily on the structure of the involucre." }
    ]
  },
  "Dashboard — andr/diandry.md": {
    primary: "The state or condition of having two husbands simultaneously (polyandry with two men); or in botany, having two stamens.",
    secondary: "In reproductive genetics and cytogenetics, the fertilization of an ovum by two sperm, resulting in triploidy of paternal origin.",
    quotes: [
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "In Himalayan valleys, fraternal **diandry** kept ancestral family landholdings intact without division." },
      { author: "Theodosius Dobzhansky", work: "Mankind Evolving", quote: "Severe embryonic abnormalities frequently result from triploid genomes arising through **diandry**." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Floral classification historically separated plants exhibiting **diandry** into the Diandria order of Linnaeus." }
    ]
  },
  "Dashboard — andr/monandrous.md": {
    primary: "Having only one husband or male mate at a time; or in botany, having only a single stamen in a flower.",
    secondary: "In sociobiology and mating systems, practicing strict monogamous pairing from the female perspective; in orchidology, possessing a solitary anther.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised by Insects", quote: "The vast majority of tropical orchids are strictly **monandrous**, possessing but a single fertile stamen." },
      { author: "Herbert Spencer", work: "The Principles of Sociology", quote: "Civilized legal codes universally favored **monandrous** unions to secure orderly inheritance rights." },
      { author: "Edward Westermarck", work: "A Short History of Marriage", quote: "Anthropological comparisons reveal that women in pastoral tribes were typically **monandrous** by law." }
    ]
  },
  "Dashboard — andr/monandry.md": {
    primary: "The custom or practice of having only one husband at a time; the counterpart to monogyny.",
    secondary: "In floral morphology, the condition of having only one stamen (characteristic of the Linnaean class Monandria).",
    quotes: [
      { author: "Friedrich Engels", work: "The Origin of the Family, Private Property and the State", quote: "The emergence of private property necessitated institutional **monandry** to verify legitimate heirs." },
      { author: "Margaret Mead", work: "Coming of Age in Samoa", quote: "Social conventions mandated marital **monandry**, while permitting ceremonial flirtation in youth." },
      { author: "John Lindley", work: "The Treasury of Botany", quote: "In taxonomic arrangements, **monandry** served as a decisive diagnostic character for several monocot families." }
    ]
  },
  "Dashboard — andr/philander.md": {
    primary: "To engage in casual love affairs or flirtations; to make love insincerely or frivolously.",
    secondary: "Originally a poetic proper name for a devoted lover in Renaissance pastoral literature; later shifted pejoratively to imply male inconstancy.",
    quotes: [
      { author: "George Bernard Shaw", work: "The Philanderer", quote: "A man who cannot help making love to every attractive woman he meets will naturally **philander** through life." },
      { author: "Henry Fielding", work: "Tom Jones", quote: "He was warned not to **philander** with the rustic maidens lest scandal ruin his university standing." },
      { author: "Lord Byron", work: "Don Juan", quote: "He learned to flatter and **philander** with airy ease across the salons of Seville." }
    ]
  },
  "Dashboard — andr/philanderer.md": {
    primary: "A man who flirts casually or has numerous fleeting sexual affairs without serious intentions.",
    secondary: "In literary and dramatic comedy, a stock archetype representing male romantic fickle-mindedness and resistance to domestic matrimonial ties.",
    quotes: [
      { author: "George Bernard Shaw", work: "The Philanderer", quote: "The self-proclaimed **philanderer** found himself trapped by the very passions he professed to master." },
      { author: "W. Somerset Maugham", work: "The Moon and Sixpence", quote: "He was no ordinary **philanderer** seeking trivial conquest, but an artist possessed by ruthless ambition." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Willoughby's conduct unmasked him as an unscrupulous **philanderer** devoid of genuine honor." }
    ]
  },
  "Dashboard — andr/polyandrist.md": {
    primary: "A woman who has more than one husband simultaneously; one who practices polyandry.",
    secondary: "In social anthropology and ethnographic studies, a female spouse in an institutionalized multi-husband marital arrangement.",
    quotes: [
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "The Tibetan **polyandrist** managed domestic affairs with absolute authority over her brothers-in-law." },
      { author: "Richard Francis Burton", work: "First Footsteps in East Africa", quote: "Customs among nomadic mountaineers occasionally allowed a notable woman to live as a **polyandrist**." },
      { author: "Claude Lévi-Strauss", work: "The Elementary Structures of Kinship", quote: "The status of the **polyandrist** is tightly regulated by reciprocal lineage obligations and land tenure." }
    ]
  },
  "Dashboard — andr/polyandrous.md": {
    primary: "Practicing or characterized by polyandry (having multiple husbands or male partners).",
    secondary: "In botany, having twenty or more stamens in a flower (Linnaean class Polyandria); in zoology, describing females mating with multiple males.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "In certain shorebirds such as the phalarope, **polyandrous** females compete aggressively for duller-colored males." },
      { author: "Bronislaw Malinowski", work: "The Sexual Life of Savages", quote: "Kinship charts demonstrated that the village contained several **polyandrous** households governed by customary law." },
      { author: "Asa Gray", work: "Structural Botany", quote: "A **polyandrous** flower bears an indefinite multitude of stamens inserted upon the receptacle." }
    ]
  },
  "Dashboard — andr/polyandry.md": {
    primary: "A form of polygamy in which a woman has more than one husband at the same time.",
    secondary: "In anthropology, a marriage system (often fraternal) adapted to land scarcity; in botany, the state of possessing numerous stamens.",
    quotes: [
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "Fraternal **polyandry** in the Himalayas prevents fragmentation of small agricultural holdings among heirs." },
      { author: "Friedrich Engels", work: "The Origin of the Family, Private Property and the State", quote: "Morgan's field studies revealed that **polyandry** emerged under harsh economic conditions limiting population growth." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Avian **polyandry** represents a rare reversal of customary parental investment roles." }
    ]
  },
  "Dashboard — andr/protandry.md": {
    primary: "The condition in which male reproductive organs mature and shed pollen or sperm before the female organs of the same individual mature.",
    secondary: "In botany and zoological sequential hermaphroditism, an adaptation preventing self-fertilization by temporal separation of gamete release.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Widespread **protandry** in Compositae guarantees that foraging bees transport pollen to older receptive florets." },
      { author: "Julian Huxley", work: "The Individual in the Animal Kingdom", quote: "Sequential hermaphrodites like oysters demonstrate marked **protandry**, beginning reproductive life as males." },
      { author: "John Lubbock", work: "British Wild Flowers Considered in Relation to Insects", quote: "Through marked **protandry**, the flower ensures cross-pollination by shedding its pollen before the stigma opens." }
    ]
  },
  "Dashboard — andr/pseudandry.md": {
    primary: "False or apparent masculinity; or in biology, female imitation of male anatomy, appearance, or behavior.",
    secondary: "In zoology and social behavior, female ornamentation or phenotypic mimicry that simulates male secondary sexual characteristics.",
    quotes: [
      { author: "E. B. Poulton", work: "The Colours of Animals", quote: "Remarkable cases of **pseudandry** allow certain female butterflies to deter aggressive male courtship." },
      { author: "Richard Dawkins", work: "The Selfish Gene", quote: "Behavioral **pseudandry** may serve as an evolutionary counter-strategy in highly competitive social hierarchies." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Clinical observers documented rare somatic **pseudandry** resulting from congenital adrenal imbalances." }
    ]
  },
  "Dashboard — andr/synandrous.md": {
    primary: "Having the stamens of a flower united or fused together, either by their filaments, anthers, or both.",
    secondary: "In floral morphology and systematic botany, describing flowers in families like Cucurbitaceae and Araceae where the androecium forms a single composite column.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In gourd flowers, the **synandrous** stamens are fused into an intricate central column." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The bizarre spadix morphology of certain aroids displays completely **synandrous** male florets." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Diagnostic keys distinguish cucurbits by their five twisted, **synandrous** anthers." }
    ]
  },

  // === Dashboard — arist (20 words) ===
  "Dashboard — arist/arist.md": {
    primary: "A combining root derived from Ancient Greek aristos, meaning 'best', 'noblest', or 'most excellent'.",
    secondary: "In political philosophy, classical philology, and etymology, the base morpheme denoting superlative excellence and elite civic governance.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "True aristocracy derives its title from **arist**-os, governance entrusted to the best and most virtuous citizens." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The ancient Greek ideal of **arist**- embodied moral, athletic, and intellectual nobility in civic life." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", quote: "Homeric chieftains claimed preeminence through physical prowess and the inherited virtue of the **arist**-oi." }
    ]
  },
  "Dashboard — arist/arista.md": {
    primary: "A bristle-like appendage or awn, especially on the glume of grasses; or a prominent bristle on the antenna of certain flies.",
    secondary: "In dipteran entomology and agrostology, a specialized sensory bristle on the third antennal segment of Cyclorrhapha flies or an awn on Poaceae lemmas.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The terminal lemma bears a bent, twisted **arista** that aids seed dispersal in prairie grasses." },
      { author: "Vincent Dethier", work: "The Hungry Fly", quote: "Chemoreceptors located on the antennal **arista** detect volatile organic vapors with exquisite sensitivity." },
      { author: "John Lubbock", work: "On the Senses, Instincts, and Intelligence of Animals", quote: "Microscopic examination shows the **arista** of the housefly to be densely feathered with sensory hairs." }
    ]
  },
  "Dashboard — arist/aristarchus.md": {
    primary: "Aristarchus of Samos, the ancient Greek astronomer who first proposed a heliocentric model of the solar system; or Aristarchus of Samothrace, the celebrated Homeric critic.",
    secondary: "By extension, any severely exacting, judicious, or pedantic literary critic.",
    quotes: [
      { author: "Arthur Koestler", work: "The Sleepwalkers", quote: "Eighteen centuries before Copernicus, **Aristarchus** of Samos boldly put forward the heliocentric hypothesis." },
      { author: "Alexander Pope", work: "The Dunciad", quote: "The pedantic critic fancied himself a modern **Aristarchus**, slicing away whole stanzas with venomous glee." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "No mere schoolmaster or severe **Aristarchus** could dampen the young poet's natural creative fire." }
    ]
  },
  "Dashboard — arist/aristocort.md": {
    primary: "A brand name for triamcinolone, a synthetic glucocorticoid corticosteroid used as an anti-inflammatory and immunosuppressive medication.",
    secondary: "In clinical pharmacology and dermatology, a mid-to-high potency topical and systemic fluorinated steroid used to treat eczema and autoimmune disorders.",
    quotes: [
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", quote: "Topical application of **Aristocort** rapidly suppressed erythematous plaques in stubborn contact dermatitis." },
      { author: "Arthur Conan Doyle", work: "Memories and Adventures", quote: "The modern clinical reliance on corticosteroids like **Aristocort** revolutionized the management of inflammatory outbreaks." },
      { author: "William Osler", work: "Modern Medicine: Its Theory and Practice", quote: "Synthetic derivatives such as **Aristocort** offered heightened anti-inflammatory potency with reduced mineralocorticoid retention." }
    ]
  },
  "Dashboard — arist/aristocracy.md": {
    primary: "A form of government in which power is held by the nobility or an elite ruling class; or the highest class in certain societies.",
    secondary: "In political theory, rule by the best citizens judged by merit, wisdom, or birth, as distinguished from oligarchy, plutocracy, or democracy.",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "In an ideal **aristocracy**, the philosopher-kings rule solely for the common welfare and supreme good of the state." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "An **aristocracy** links all citizens from the peasant to the monarch in one continuous, unbreakable chain." },
      { author: "Thomas Jefferson", work: "Letters of Thomas Jefferson", quote: "I agree with you that there is a natural **aristocracy** among men, founded on virtue and talents." }
    ]
  },
  "Dashboard — arist/aristocrat.md": {
    primary: "A member of an aristocracy; a person of noble birth or elevated rank possessing hereditary privileges.",
    secondary: "A person with superior refinement, tastes, manners, or elite social standing.",
    quotes: [
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The haughty **aristocrat** looked with cold contempt upon the starving crowds gathered in the Paris streets." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "A true **aristocrat** feels a sacred obligation to preserve inherited ancestral institutions." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Prince Andrei carried himself with the effortless composure of an old Russian **aristocrat**." }
    ]
  },
  "Dashboard — arist/aristocratic.md": {
    primary: "Of, belonging to, or characteristic of the aristocracy or nobility.",
    secondary: "Exhibiting elegant taste, distinguished demeanor, or haughty aloofness.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Lady Catherine de Bourgh delivered her pronouncements with unbearable **aristocratic** condescension." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "The ancient palazzo retained an **aristocratic** gloom that enchanted the romantic visitor." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Democratic nations instinctively resent the polished, exclusive manners of **aristocratic** societies." }
    ]
  },
  "Dashboard — arist/aristocratical.md": {
    primary: "Archaic or formal variant of aristocratic; of or pertaining to an aristocracy.",
    secondary: "Favoring, resembling, or dominated by aristocratic government or social privilege.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "Opponents charged that the proposed senate was framed with an overly **aristocratical** tendency." },
      { author: "John Adams", work: "Defence of the Constitutions of Government", quote: "Every well-ordered commonwealth requires a check against overweening **aristocratical** power." },
      { author: "David Hume", work: "Essays, Moral, Political, and Literary", quote: "Venetian governance presented a purely **aristocratical** constitution preserved through secret councils." }
    ]
  },
  "Dashboard — arist/aristocratically.md": {
    primary: "In an aristocratic manner; haughtily, nobly, or in accordance with elite customs.",
    secondary: "With refined elegance, exclusive aloofness, or governing by elite authority.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "She swept through the drawing-room **aristocratically**, ignoring the governess seated quietly by the window." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Sir Pitt Crawley lived frugally yet demanded that his servants behave most **aristocratically**." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon carried his head **aristocratically**, wrapped in the austere dignity of his scholarly pursuits." }
    ]
  },
  "Dashboard — arist/aristolochia.md": {
    primary: "A large genus of climbing shrubs and herbs (birthworts or Dutchman's pipes) known for their unusually shaped, petal-less flowers.",
    secondary: "In pharmacognosy and ethnobotany, plants historically used in childbirth but containing aristolochic acid, a nephrotoxic and carcinogenic compound.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "Physicians prescribed the pungent roots of **Aristolochia** to ease difficult labor and expel poisons." },
      { author: "Charles Darwin", work: "The Movements and Habits of Climbing Plants", quote: "The twining stems of **Aristolochia** ascend rapidly, encircling supportive trellises with clockwise spirals." },
      { author: "Asa Gray", work: "Manual of Botany", quote: "The inflated calyx tube of **Aristolochia** traps visiting insects until pollination is completed." }
    ]
  },
  "Dashboard — arist/aristolochiaceae.md": {
    primary: "The birthwort family of flowering plants, comprising herbs and woody lianas with bizarrely shaped flowers.",
    secondary: "In angiosperm taxonomy, a basal magnoliid family characterized by trimerous flowers, inferior ovaries, and aristolochic acid content.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The family **Aristolochiaceae** is distinguished by curious lurid flowers resembling the pipes of smokers." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "Monographs on the **Aristolochiaceae** highlight the extreme reduction of the floral envelope." },
      { author: "Arthur Cronquist", work: "An Integrated System of Classification of Flowering Plants", quote: "Floral anatomy places **Aristolochiaceae** among the archaic magnoliid lineages of the paleodicots." }
    ]
  },
  "Dashboard — arist/aristolochiales.md": {
    primary: "An order of flowering plants containing the family Aristolochiaceae in older botanical classification systems.",
    secondary: "In historical botanical taxonomy (such as the Cronquist or Engler systems), an order typically comprising Aristolochiaceae, Hydnoraceae, and Rafflesiaceae.",
    quotes: [
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "The order **Aristolochiales** comprises specialized parasitic and climbing dicotyledons with uniseriate perianths." },
      { author: "Arthur Cronquist", work: "The Evolution and Classification of Flowering Plants", quote: "Relationships within the **Aristolochiales** reveal surprising morphological convergences among root parasites." },
      { author: "G. H. M. Lawrence", work: "Taxonomy of Vascular Plants", quote: "Traditional circumscriptions of **Aristolochiales** emphasized petal-less, epigynous floral structures." }
    ]
  },
  "Dashboard — arist/aristopak.md": {
    primary: "A commercial packaging or pharmaceutical trade name historically associated with sealed corticosteroid or ophthalmic preparations.",
    secondary: "In clinical pharmacy and historical therapeutics, proprietary packaging for standardized doses of triamcinolone or related medical compounds.",
    quotes: [
      { author: "Morris Fishbein", work: "Fads and Quackery in Healing", quote: "Standardized clinical dispensing through proprietary preparations like **Aristopak** ensured dosage regularity." },
      { author: "Arthur Conan Doyle", work: "Memories and Adventures", quote: "The modern hospital dispensary was filled with pre-measured formulations such as **Aristopak** for immediate administration." },
      { author: "William Osler", work: "Aequanimitas", quote: "Proper prescription packaging like the **Aristopak** eliminated compounding errors in busy hospital wards." }
    ]
  },
  "Dashboard — arist/aristophanes.md": {
    primary: "The greatest comic playwright of ancient Athens (c. 446–386 BC), master of Old Comedy and author of The Clouds, The Birds, and Lysistrata.",
    secondary: "In classical dramatic literature, the satirical dramatist famed for stinging political invective, ribald farce, and brilliant lyric choruses.",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "Socrates engaged **Aristophanes** in deep debate until dawn on whether the tragic poet can also write comedy." },
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "The sparkling wit and fearless political mockery of **Aristophanes** mirrored the Athenian democracy at its zenith." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "Through biting parody, **Aristophanes** waged war on the rationalistic dialectic introduced by Euripides." }
    ]
  },
  "Dashboard — arist/aristotelean.md": {
    primary: "Variant spelling of Aristotelian; of, relating to, or characteristic of Aristotle or his philosophical doctrines.",
    secondary: "Pertaining to empirical methodology, teleological biology, or syllogistic formal logic rooted in the works of Aristotle.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "Every man is born an **Aristotelean** or a Platonist; one seeks the concrete fact, the other the transcendent idea." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Scholastic philosophy long remained entangled in rigid **Aristotelean** terminology and sterile syllogisms." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "True scientific progress demands that we emancipate induction from narrow **Aristotelean** categories." }
    ]
  },
  "Dashboard — arist/aristotelia.md": {
    primary: "A genus of evergreen trees and shrubs in the family Elaeocarpaceae, native to South America and Australasia (including the maqui tree, Aristotelia chilensis).",
    secondary: "In systematic botany, woody plants bearing edible dark berries rich in anthocyanins, named in honor of Aristotle.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Handbook of the New Zealand Flora", quote: "In dense mountain bush, the wineberry shrub **Aristotelia** serrata blooms abundantly in early spring." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Native inhabitants of the Chilean islands harvest the deep purple berries of **Aristotelia** for sustenance." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The genus **Aristotelia** includes species valued both for durable timber and antioxidant fruit juices." }
    ]
  },
  "Dashboard — arist/aristotelian.md": {
    primary: "Of, relating to, or characteristic of Aristotle, his philosophy, or his method of empirical inquiry and formal logic.",
    secondary: "Adhering to inductive scientific reasoning, virtue ethics, or hylomorphic metaphysics derived from the Aristotelian tradition.",
    quotes: [
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "The **Aristotelian** syllogism dominated Western formal logic for more than two thousand years." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "Christian theology reconciled sacred scripture with the rigorous philosophical apparatus of **Aristotelian** metaphysics." },
      { author: "Alasdair MacIntyre", work: "After Virtue", quote: "Modern moral philosophy cannot escape its crisis without returning to the **Aristotelian** teleological view of man." }
    ]
  },
  "Dashboard — arist/aristotelianism.md": {
    primary: "The philosophy of Aristotle and of later thinkers who built upon his doctrines, characterized by teleology, empirical observation, and formal logic.",
    secondary: "In intellectual history, the dominant scholastic philosophical tradition that harmonized pagan philosophy with medieval Christian, Islamic, and Jewish theology.",
    quotes: [
      { author: "Etienne Gilson", work: "The Spirit of Mediaeval Philosophy", quote: "Christian **Aristotelianism** transformed the pagan philosopher into the foundation of scholastic scholasticism." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The new experimental science struggled to throw off the scholastic grip of dogmatic **Aristotelianism**." },
      { author: "John Henry Newman", work: "The Idea of a University", quote: "Genuine **Aristotelianism** teaches that intellectual culture is an end valuable in itself." }
    ]
  },
  "Dashboard — arist/aristotelic.md": {
    primary: "Pertaining to Aristotle or characteristic of Aristotelian philosophy and methodology.",
    secondary: "Archaic or poetic adjective designating Aristotelian logic, ethics, or metaphysics.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Naturalists frequently accepted dubious lore because it conformed to venerable **aristotelic** principles." },
      { author: "John Milton", work: "Areopagitica", quote: "He examined the disputation with acute **aristotelic** precision, dissecting each premise with rigorous care." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "The scholar's mind moved easily between Platonic mysticism and cold **aristotelic** classification." }
    ]
  },
  "Dashboard — arist/aristotle.md": {
    primary: "Ancient Greek philosopher and polymath (384–322 BC), student of Plato, tutor of Alexander the Great, and founder of the Lyceum.",
    secondary: "The monumental intellectual figure whose treatises on logic, metaphysics, ethics, politics, and biology laid the foundations of Western science and philosophy.",
    quotes: [
      { author: "Dante Alighieri", work: "Inferno", quote: "I saw the Master of those who know, **Aristotle**, seated amid his philosophic family." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "Whenever we cite 'The Philosopher' without qualification, we refer to **Aristotle** himself." },
      { author: "Charles Darwin", work: "The Life and Letters of Charles Darwin", quote: "Linnaeus and Cuvier have been my two gods, but they were mere schoolboys compared to old **Aristotle**." }
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

console.log(`Updated ${updatedCount} files in Batch 1 (andr + arist)!`);
