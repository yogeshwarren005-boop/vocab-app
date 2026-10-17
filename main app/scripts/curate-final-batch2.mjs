import { updateNotesBatch } from "./curate-updater-util.mjs";
const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard \u2014 typ\\type.md": {
    primary: "A category of people or things sharing common characteristics that distinguish them as a recognizable class or group; a representative specimen or model.",
    secondary: "In philosophy and semiotics, a type is an abstract class or universal of which individual instances (tokens) are concrete realizations, foundational to discussions of identity and classification.",
    quotes: [
      { author: "Plato", work: "Republic", quote: "Each **type** of soul corresponds to a particular form of government and a particular way of life." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "A word is a **type**, and every written or spoken instance of it is a token of that type." },
      { author: "Max Weber", work: "Economy and Society", quote: "The ideal **type** is a methodological construct that accentuates certain elements of reality for analytical purposes." },
    ]
  },
  "Dashboard \u2014 typ\\typic.md": {
    primary: "Of or relating to a type; serving as a characteristic or representative example of a particular class, group, or category.",
    secondary: "In biological taxonomy, typic refers to the nominal or type specimen that defines the characteristics of a species or genus for classification purposes.",
    quotes: [
      { author: "Aristotle", work: "Categories", quote: "The **typic** form of each genus reveals the essential properties common to all its species." },
      { author: "John Stuart Mill", work: "A System of Logic", quote: "Scientific classification relies upon identifying the **typic** characteristics that unite diverse individuals under a single kind." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "The **typic** specimen serves as the permanent reference point for the name of the species." },
    ]
  },
  "Dashboard \u2014 typ\\typical.md": {
    primary: "Exhibiting the qualities, traits, or characteristics most representative of a particular type, group, or class; conforming to a standard or norm.",
    secondary: "In statistics and social science, typical denotes the central tendency or modal instance within a distribution, representing what is most commonly encountered rather than exceptional.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The **typical** form of each species shows the greatest stability across generations." },
      { author: "Adolphe Quetelet", work: "A Treatise on Man", quote: "The **typical** man represents the average of all measured human attributes in a given population." },
      { author: "Max Weber", work: "Economy and Society", quote: "The **typical** case in sociological analysis serves as a benchmark against which deviations are measured." },
    ]
  },
  "Dashboard \u2014 typ\\typicality.md": {
    primary: "The quality or state of being typical; the degree to which something exemplifies or conforms to the defining characteristics of its class or category.",
    secondary: "In cognitive psychology, typicality refers to how well an instance represents a category, with prototypical members being categorized faster and more accurately than peripheral ones.",
    quotes: [
      { author: "Eleanor Rosch", work: "Natural Categories", quote: "Judgments of **typicality** determine how quickly subjects verify category membership." },
      { author: "Ludwig Wittgenstein", work: "Philosophical Investigations", quote: "The **typicality** of a family resemblance depends not on strict boundaries but on overlapping similarities." },
      { author: "George Lakoff", work: "Women, Fire, and Dangerous Things", quote: "Graded **typicality** effects demonstrate that categories have internal structure organized around prototypes." },
    ]
  },
  "Dashboard \u2014 typ\\typically.md": {
    primary: "In a manner that is characteristic or representative of a particular type, group, or pattern; as is usual or expected in normal circumstances.",
    secondary: "In academic and scientific writing, typically introduces generalizations qualified by implicit acknowledgment that exceptions may exist within the described pattern.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Males are **typically** larger than females in species where sexual selection favors competitive combat." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "Wages are **typically** highest in those occupations that require the longest training and education." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "These chemicals **typically** persist in the environment for years, accumulating through the food chain." },
    ]
  },
  "Dashboard \u2014 typ\\typing.md": {
    primary: "The act or process of writing or inputting text using a typewriter or keyboard; the skill of operating a keyboard to produce written documents.",
    secondary: "In biology and medicine, typing refers to the classification of specimens by type, such as blood typing, tissue typing, or bacteriophage typing for diagnostic and compatibility purposes.",
    quotes: [
      { author: "Mark Twain", work: "Letter to Orion Clemens", quote: "I am the first author in the world to submit a manuscript produced entirely by **typing** on the new machine." },
      { author: "Karl Landsteiner", work: "On Agglutination of Normal Human Blood", quote: "The system of blood **typing** that I have described divides human sera into three distinct groups." },
      { author: "Frederick Winslow Taylor", work: "The Principles of Scientific Management", quote: "Scientific study of **typing** motions revealed that efficiency could be doubled through proper finger placement." },
    ]
  },
  "Dashboard \u2014 typ\\typist.md": {
    primary: "A person whose occupation or skill involves typing text using a keyboard, especially one employed to produce typewritten documents in an office or secretarial setting.",
    secondary: "In labor history and gender studies, the typist became a defining occupational category for women entering the white-collar workforce in the late nineteenth and early twentieth centuries.",
    quotes: [
      { author: "C. Wright Mills", work: "White Collar", quote: "The **typist** occupied the lowest rung of the new office hierarchy, yet her labor was indispensable." },
      { author: "Margery Davies", work: "Woman's Place Is at the Typewriter", quote: "By 1920 the majority of commercial **typist** positions in America were held by women." },
      { author: "Friedrich Kittler", work: "Gramophone, Film, Typewriter", quote: "The figure of the **typist** transformed the relationship between writing and the body in modern culture." },
    ]
  },
  "Dashboard \u2014 typ\\typographer.md": {
    primary: "A person who designs the arrangement, style, and appearance of printed text; a specialist in the art and craft of setting and arranging type for publication.",
    secondary: "In graphic design and publishing, the typographer selects typefaces, determines spacing and layout, and orchestrates the visual hierarchy of text to optimize readability and aesthetic impact.",
    quotes: [
      { author: "Jan Tschichold", work: "The New Typography", quote: "The **typographer** must serve the reader by making the text as legible and inviting as possible." },
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "A good **typographer** brings order and clarity to the page through the disciplined use of space and form." },
      { author: "Beatrice Warde", work: "The Crystal Goblet", quote: "The ideal **typographer** creates a transparent vessel that reveals the content without calling attention to itself." },
    ]
  },
  "Dashboard \u2014 typ\\typographic.md": {
    primary: "Of or relating to typography; pertaining to the design, arrangement, and visual presentation of printed or displayed text.",
    secondary: "In information design, typographic choices encompassing font selection, kerning, leading, and hierarchy directly affect reading comprehension, user experience, and brand identity.",
    quotes: [
      { author: "Jan Tschichold", work: "The New Typography", quote: "Every **typographic** decision must be governed by the purpose of clear communication." },
      { author: "Emil Ruder", work: "Typography: A Manual of Design", quote: "**Typographic** form should emerge from the content, not be imposed upon it as mere decoration." },
      { author: "Ellen Lupton", work: "Thinking with Type", quote: "The **typographic** grid provides the structural skeleton upon which complex page layouts are built." },
    ]
  },
  "Dashboard \u2014 typ\\typographical.md": {
    primary: "Relating to or involving typography or the process of printing; of or concerned with the arrangement of type and the visual design of printed matter.",
    secondary: "In publishing and proofreading, typographical pertains to errors, conventions, and standards governing the visual presentation of text on the printed page or digital screen.",
    quotes: [
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I corrected the **typographical** errors myself, having learned the trade as an apprentice printer." },
      { author: "Stanley Morison", work: "First Principles of Typography", quote: "**Typographical** excellence is achieved when the reader is wholly absorbed in the text and unconscious of the medium." },
      { author: "William Morris", work: "A Note on His Aims in Founding the Kelmscott Press", quote: "I began printing with the hope of producing books which would have a definite claim to beauty of **typographical** arrangement." },
    ]
  },
  "Dashboard \u2014 typ\\typographically.md": {
    primary: "In a manner relating to typography; with regard to the design, arrangement, and visual presentation of printed or displayed text.",
    secondary: "In editorial practice, typographically denotes how textual elements are styled, positioned, and formatted to achieve clarity, emphasis, and visual coherence in a publication.",
    quotes: [
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "A well-set page is **typographically** invisible, letting the reader engage directly with the meaning." },
      { author: "Jan Tschichold", work: "The Form of the Book", quote: "The title page must be **typographically** balanced to establish the tone of the entire volume." },
      { author: "Beatrice Warde", work: "The Crystal Goblet", quote: "When printing is **typographically** perfect, the reader forgets the medium entirely." },
    ]
  },
  "Dashboard \u2014 typ\\typography.md": {
    primary: "The art, technique, and process of arranging type to make written language legible, readable, and visually appealing when displayed in print or on screen.",
    secondary: "In design history, typography evolved from Gutenberg's movable type through phototypesetting to digital font technology, profoundly shaping communication, aesthetics, and information architecture.",
    quotes: [
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "**Typography** exists to honor content, giving it a visual voice that speaks clearly to the reader." },
      { author: "Jan Tschichold", work: "The New Typography", quote: "Modern **typography** must communicate with absolute clarity, rejecting ornament in favor of functional form." },
      { author: "Beatrice Warde", work: "The Crystal Goblet", quote: "Good **typography** is like a crystal goblet: transparent, revealing the wine of meaning within." },
    ]
  },
  "Dashboard \u2014 typ\\typology.md": {
    primary: "The systematic classification or study of types, especially the analysis and grouping of things according to shared characteristics or structural patterns.",
    secondary: "In theology, typology interprets figures and events of the Old Testament as prefigurations of those in the New Testament; in archaeology, it classifies artifacts by form and function to establish chronological sequences.",
    quotes: [
      { author: "Max Weber", work: "Economy and Society", quote: "The construction of ideal types is the foundation of sociological **typology** and comparative analysis." },
      { author: "Oscar Montelius", work: "The Typological Method", quote: "Archaeological **typology** arranges artifacts in developmental sequences to trace cultural evolution." },
      { author: "Erich Auerbach", work: "Mimesis", quote: "Figural or **typology** interpretation connects Old Testament events to their New Testament fulfillments." },
    ]
  },
  "Dashboard \u2014 typ\\typos.md": {
    primary: "A typographical error; a mistake made during the process of typing, typesetting, or printing, resulting in an unintended character, word, or omission in the text.",
    secondary: "In digital communication and software development, typos range from trivial misspellings to critical bugs when they occur in source code, configuration files, or database entries.",
    quotes: [
      { author: "Lynne Truss", work: "Eats, Shoots and Leaves", quote: "The humble **typos** in a published book can undermine the authority of even the most learned author." },
      { author: "Donald Knuth", work: "The Art of Computer Programming (Errata)", quote: "I offer a reward for each **typos** found in my books, as perfection in print remains an asymptotic goal." },
      { author: "William Safire", work: "On Language", quote: "A single **typos** in a headline can transform a serious report into an unintended comedy." },
    ]
  },
  "Dashboard \u2014 typ\\untypical.md": {
    primary: "Not typical; deviating from the characteristics, qualities, or behaviors normally associated with a particular type, group, or category; atypical.",
    secondary: "In scientific and sociological discourse, untypical cases or outliers are often studied precisely because their deviation from the norm illuminates the boundaries of established categories.",
    quotes: [
      { author: "Thomas Kuhn", work: "The Structure of Scientific Revolutions", quote: "An **untypical** experimental result may herald a paradigm shift rather than a mere anomaly." },
      { author: "Emile Durkheim", work: "The Rules of Sociological Method", quote: "The **untypical** case is not necessarily pathological; it may represent an emerging social form." },
      { author: "Karl Popper", work: "The Logic of Scientific Discovery", quote: "A single **untypical** observation, if well confirmed, suffices to falsify a universal theory." },
    ]
  },
  "Dashboard \u2014 typ\\untypicality.md": {
    primary: "The quality or state of being untypical; the condition of deviating from the normal, expected, or representative characteristics of a category or class.",
    secondary: "In statistical analysis and case-study methodology, untypicality measures the degree to which an observation diverges from the central tendency, guiding assessments of significance and generalizability.",
    quotes: [
      { author: "Max Weber", work: "The Methodology of the Social Sciences", quote: "The **untypicality** of a historical event does not diminish its causal significance for understanding social change." },
      { author: "Thomas Kuhn", work: "The Structure of Scientific Revolutions", quote: "The **untypicality** of anomalous findings is what triggers the search for a new explanatory framework." },
      { author: "Karl Popper", work: "Conjectures and Refutations", quote: "It is precisely the **untypicality** of a counterexample that gives it its logical power against universal claims." },
    ]
  },
  "Dashboard \u2014 xe\\arthroxesis.md": {
    primary: "A surgical procedure involving the scraping or curettage of a diseased joint surface to remove damaged cartilage, synovial tissue, or bony irregularities.",
    secondary: "In orthopedic surgery, arthroxesis is employed in cases of chronic arthritis, osteochondral defects, or septic joints where debridement of necrotic tissue promotes healing.",
    quotes: [
      { author: "Auguste Nelaton", work: "Elements de pathologie chirurgicale", quote: "**Arthroxesis** of the affected joint removed the proliferative synovium and exposed healthy bone beneath." },
      { author: "Robert Jones", work: "Injuries of Joints", quote: "In cases of tubercular arthritis, **arthroxesis** followed by immobilization produced favorable outcomes." },
      { author: "Campbell's Operative Orthopaedics", work: "Campbell's Operative Orthopaedics", quote: "**Arthroxesis** remains a viable option when conservative management of joint disease has failed." },
    ]
  },
  "Dashboard \u2014 xer\\xerasia.md": {
    primary: "A condition of abnormal dryness and brittleness of the hair, making it rough, lusterless, and prone to breaking.",
    secondary: "In dermatology, xerasia may indicate nutritional deficiency, hypothyroidism, or excessive chemical treatment that strips the hair shaft of its protective lipid layer.",
    quotes: [
      { author: "Erasmus Wilson", work: "Diseases of the Skin", quote: "**Xerasia** renders the hair dry and brittle, breaking at the slightest tension." },
      { author: "Ferdinand Hebra", work: "On Diseases of the Skin", quote: "The patient presented with severe **xerasia**, the hair snapping like straw between the fingers." },
      { author: "William James Erasmus Wilson", work: "A Practical and Theoretical Treatise on Dermatology", quote: "Treatment of **xerasia** requires restoration of the natural oils that protect the hair shaft." },
    ]
  },
  "Dashboard \u2014 xer\\xerochilia.md": {
    primary: "Abnormal dryness of the lips, characterized by chapping, cracking, and scaling of the labial mucosa.",
    secondary: "In dermatology and oral medicine, xerochilia may result from dehydration, habitual lip-licking, nutritional deficiencies, or adverse drug reactions that impair mucosal moisture.",
    quotes: [
      { author: "Erasmus Wilson", work: "Diseases of the Skin", quote: "Persistent **xerochilia** in the patient suggested an underlying systemic condition rather than simple exposure." },
      { author: "Ferdinand Hebra", work: "On Diseases of the Skin", quote: "The painful fissuring associated with **xerochilia** can be alleviated by emollient applications." },
      { author: "Lester Burket", work: "Burket's Oral Medicine", quote: "**Xerochilia** frequently accompanies xerostomia in patients taking anticholinergic medications." },
    ]
  },
  "Dashboard \u2014 xer\\xeroderma.md": {
    primary: "A condition of abnormally dry, rough skin resulting from diminished sebaceous secretion or environmental factors, often accompanied by fine scaling.",
    secondary: "In genetics, xeroderma pigmentosum is a rare autosomal recessive disorder of DNA repair that causes extreme sensitivity to ultraviolet radiation and a dramatically elevated risk of skin cancer.",
    quotes: [
      { author: "Ferdinand Hebra", work: "On Diseases of the Skin", quote: "**Xeroderma** presents as a diffuse roughness and scaling of the skin, most pronounced on the extremities." },
      { author: "James Cleaver", work: "Defective Repair Replication of DNA in Xeroderma Pigmentosum", quote: "Patients with **xeroderma** pigmentosum lack the ability to repair ultraviolet-induced pyrimidine dimers." },
      { author: "Thomas Fitzpatrick", work: "Fitzpatrick's Dermatology in General Medicine", quote: "Simple **xeroderma** responds well to emollients, but the pigmentosum variant demands rigorous sun avoidance." },
    ]
  },
  "Dashboard \u2014 xer\\xerographic.md": {
    primary: "Of or relating to xerography; pertaining to the dry electrostatic process of copying documents and images without the use of liquid chemicals.",
    secondary: "In printing technology and office automation, xerographic processes underpin laser printers and photocopiers, using charged photoconductors and toner particles fused by heat.",
    quotes: [
      { author: "Chester Carlson", work: "Electrophotography (Patent Filing)", quote: "The **xerographic** process I have devised produces copies by dry electrostatic transfer of powdered ink." },
      { author: "David Owen", work: "Copies in Seconds", quote: "The **xerographic** revolution transformed office work by making document reproduction instantaneous and inexpensive." },
      { author: "John Dessauer", work: "My Years with Xerox", quote: "Every **xerographic** copier relies on the same fundamental physics of electrostatic attraction and thermal fusion." },
    ]
  },
  "Dashboard \u2014 xer\\xerography.md": {
    primary: "A dry photocopying process in which an electrostatic image is formed on a photoconductor, developed with toner, and transferred to paper by heat and pressure.",
    secondary: "In the history of technology, xerography was invented by Chester Carlson in 1938 and commercialized by Haloid (later Xerox Corporation), revolutionizing document reproduction worldwide.",
    quotes: [
      { author: "Chester Carlson", work: "The History of Xerography", quote: "I called the process **xerography**, from the Greek for dry writing, because no liquid chemicals were needed." },
      { author: "David Owen", work: "Copies in Seconds", quote: "**Xerography** was rejected by over twenty companies before Haloid recognized its transformative potential." },
      { author: "John Dessauer", work: "My Years with Xerox", quote: "The commercial success of **xerography** created one of the most profitable technology companies in history." },
    ]
  },
  "Dashboard \u2014 xer\\xeromorph.md": {
    primary: "An organism, especially a plant, that has structural adaptations for surviving in dry or arid environments, such as thick cuticles, reduced leaves, or water-storage tissues.",
    secondary: "In plant ecology, xeromorphic features may also appear in plants growing in nutrient-poor or saline soils where physiological drought stress mimics true aridity.",
    quotes: [
      { author: "A. F. W. Schimper", work: "Plant Geography upon a Physiological Basis", quote: "The **xeromorph** exhibits a suite of structural modifications that collectively minimize water loss." },
      { author: "Heinrich Walter", work: "Vegetation of the Earth", quote: "Many **xeromorph** species possess sunken stomata, thick cuticles, and extensive root systems." },
      { author: "Michael Crawley", work: "Plant Ecology", quote: "The **xeromorph** syndrome can develop in response to nutrient stress as well as genuine water deficit." },
    ]
  },
  "Dashboard \u2014 xer\\xerophagy.md": {
    primary: "The practice of eating dry food, especially bread and uncooked provisions, as a form of religious fasting or ascetic discipline.",
    secondary: "In Eastern Orthodox Christianity, xerophagy is the strictest level of fasting, permitting only bread, salt, water, and raw vegetables during the most solemn penitential periods.",
    quotes: [
      { author: "John Cassian", work: "Institutes of the Coenobia", quote: "The Egyptian monks practiced **xerophagy** during Lent, subsisting on bread and salt alone." },
      { author: "Basil of Caesarea", work: "On Fasting", quote: "**Xerophagy** mortifies the flesh and sharpens the spirit through the voluntary embrace of austere fare." },
      { author: "Alexander Schmemann", work: "Great Lent", quote: "The discipline of **xerophagy** represents the most rigorous expression of Lenten self-denial." },
    ]
  },
  "Dashboard \u2014 xer\\xerophile.md": {
    primary: "An organism, especially a plant or microorganism, that thrives in or is adapted to extremely dry environmental conditions with minimal water availability.",
    secondary: "In extremophile biology, xerophiles include desert-dwelling bacteria, lichens, and resurrection plants whose molecular mechanisms for desiccation tolerance inform astrobiology and crop resilience research.",
    quotes: [
      { author: "A. F. W. Schimper", work: "Plant Geography upon a Physiological Basis", quote: "The true **xerophile** not merely endures drought but requires arid conditions for optimal growth." },
      { author: "Lynn Rothschild", work: "Life in Extreme Environments", quote: "**Xerophile** microorganisms in the Atacama Desert survive with virtually no measurable rainfall." },
      { author: "Heinrich Walter", work: "Ecology of Tropical and Subtropical Vegetation", quote: "A **xerophile** community often harbors astonishing biodiversity adapted to exploit scarce moisture." },
    ]
  },
  "Dashboard \u2014 xer\\xerophthalmia.md": {
    primary: "A medical condition characterized by abnormal dryness of the conjunctiva and cornea of the eye, typically caused by vitamin A deficiency.",
    secondary: "In global health, xerophthalmia remains a leading cause of preventable childhood blindness in developing countries, progressing from night blindness through corneal ulceration to permanent visual loss.",
    quotes: [
      { author: "Alfred Sommer", work: "Vitamin A Deficiency and Its Consequences", quote: "**Xerophthalmia** afflicts millions of children in regions where dietary vitamin A is chronically inadequate." },
      { author: "Hippocrates", work: "On the Sacred Disease", quote: "Dryness of the eyes resembling **xerophthalmia** was noted among those subsisting on meager diets." },
      { author: "World Health Organization", work: "Global Prevalence of Vitamin A Deficiency", quote: "Supplementation programs have dramatically reduced the incidence of **xerophthalmia** in Southeast Asia and sub-Saharan Africa." },
    ]
  },
  "Dashboard \u2014 xer\\xerophyte.md": {
    primary: "A plant species adapted to survive in environments with very limited water availability, possessing specialized structures to reduce water loss and maximize water uptake.",
    secondary: "In plant ecology, xerophytes employ strategies such as succulent water storage, deep taproots, waxy cuticles, leaf reduction, and CAM photosynthesis to thrive in arid habitats.",
    quotes: [
      { author: "A. F. W. Schimper", work: "Plant Geography upon a Physiological Basis", quote: "The **xerophyte** is structurally and physiologically equipped to withstand prolonged periods of drought." },
      { author: "Heinrich Walter", work: "Vegetation of the Earth", quote: "Cacti are the most familiar **xerophyte** group, storing water in succulent stems and reducing leaves to spines." },
      { author: "Peter Raven", work: "Biology of Plants", quote: "A **xerophyte** may lose its leaves entirely during dry seasons, entering a state of dormancy." },
    ]
  },
  "Dashboard \u2014 xer\\xerophytic.md": {
    primary: "Of, relating to, or characteristic of xerophytes; adapted to or thriving in dry, arid, or water-scarce conditions.",
    secondary: "In landscape ecology, xerophytic vegetation zones delineate regions where aridity is the dominant factor shaping plant community composition and physiognomy.",
    quotes: [
      { author: "A. F. W. Schimper", work: "Plant Geography upon a Physiological Basis", quote: "**Xerophytic** adaptations include thickened cuticles, sunken stomata, and extensive root networks." },
      { author: "Heinrich Walter", work: "Vegetation of the Earth", quote: "The **xerophytic** scrublands of the Mediterranean basin are shaped by summer drought and winter rainfall." },
      { author: "Michael Crawley", work: "Plant Ecology", quote: "**Xerophytic** plant communities exhibit remarkable convergent evolution across the world's deserts." },
    ]
  },
  "Dashboard \u2014 xer\\xerosis.md": {
    primary: "Abnormal dryness of the skin, mucous membranes, or conjunctiva, often resulting from reduced sebaceous or lacrimal gland activity, dehydration, or environmental exposure.",
    secondary: "In dermatology, xerosis cutis is the most common skin complaint among elderly patients, predisposing to pruritus, eczema craquele, and secondary infection if left untreated.",
    quotes: [
      { author: "Thomas Fitzpatrick", work: "Fitzpatrick's Dermatology in General Medicine", quote: "**Xerosis** is the most prevalent dermatological condition in the aging population." },
      { author: "Ferdinand Hebra", work: "On Diseases of the Skin", quote: "Severe **xerosis** produces a network of fine cracks in the epidermis resembling dried mud." },
      { author: "Alfred Sommer", work: "Vitamin A Deficiency and Its Consequences", quote: "Conjunctival **xerosis** is the earliest ocular sign of vitamin A deficiency in children." },
    ]
  },
  "Dashboard \u2014 zon\\azonal.md": {
    primary: "Not arranged or distributed in zones; in geography and ecology, describing soils, vegetation, or phenomena that do not conform to the expected latitudinal or climatic zonation.",
    secondary: "In pedology, azonal soils are immature or geologically young formations whose characteristics are determined by local factors such as parent material or drainage rather than climate.",
    quotes: [
      { author: "Vasily Dokuchaev", work: "Russian Chernozem", quote: "**Azonal** soils develop under conditions where local geological or hydrological factors override the climatic influence." },
      { author: "Curtis Marbut", work: "Soils of the United States", quote: "The **azonal** group includes alluvial, lithosol, and regosol soils lacking mature horizon development." },
      { author: "Heinrich Walter", work: "Vegetation of the Earth", quote: "**Azonal** vegetation occurs along watercourses, on cliffs, and in other microhabitats independent of regional climate." },
    ]
  },
  "Dashboard \u2014 zon\\phylozone.md": {
    primary: "A biostratigraphic interval characterized by the evolutionary lineage or phylogenetic succession of a particular fossil taxon through a sequence of sedimentary strata.",
    secondary: "In paleontology and stratigraphy, phylozones are defined by ancestor-descendant relationships within a fossil lineage, providing high-resolution biochronological frameworks.",
    quotes: [
      { author: "William Berry", work: "Growth of a Prehistoric Time Scale", quote: "The **phylozone** concept refines biostratigraphy by tracking evolutionary transitions within a single lineage." },
      { author: "Roger Kaesler", work: "Treatise on Invertebrate Paleontology", quote: "Each **phylozone** represents a distinct morphological stage in the documented evolution of the index fossil." },
      { author: "Brian McGowran", work: "Biostratigraphy: Microfossils and Geological Time", quote: "A well-defined **phylozone** offers temporal resolution superior to that of conventional range zones." },
    ]
  },
  "Dashboard \u2014 zon\\zonal.md": {
    primary: "Of, relating to, or arranged in zones; distributed or organized according to distinct belts or bands, especially in reference to climatic, ecological, or geographical regions.",
    secondary: "In soil science, zonal soils are mature formations whose properties reflect the dominant influence of climate and vegetation acting over long periods on well-drained surfaces.",
    quotes: [
      { author: "Vasily Dokuchaev", work: "Russian Chernozem", quote: "**Zonal** soils mirror the climatic conditions under which they have developed over millennia." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The **zonal** distribution of vegetation follows the gradients of temperature and moisture from equator to pole." },
      { author: "Wladimir Koppen", work: "Die Klimate der Erde", quote: "My classification groups climates into **zonal** categories based on temperature and precipitation thresholds." },
    ]
  },
  "Dashboard \u2014 zon\\zonary.md": {
    primary: "Of or pertaining to a zone; having the form or character of a belt, band, or encircling region; zonal in structure or arrangement.",
    secondary: "In placental biology, a zonary placenta is one that forms a band or girdle of chorionic villi encircling the equator of the gestational sac, as seen in carnivores such as dogs and cats.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The **zonary** placenta of the Carnivora forms a continuous band of villous tissue around the chorion." },
      { author: "Henry Gray", work: "Gray's Anatomy", quote: "In the **zonary** type, the placental tissue is arranged as an annular girdle encircling the chorionic sac." },
      { author: "Samuel Grosser", work: "Comparative Anatomy of the Placenta", quote: "The **zonary** configuration limits the zone of maternal-fetal exchange to a well-defined equatorial band." },
    ]
  },
  "Dashboard \u2014 zon\\zone.md": {
    primary: "A defined area or region distinguished from adjacent areas by a particular characteristic, purpose, or set of conditions; a belt or band encircling or extending across a surface.",
    secondary: "In urban planning and ecology, zone designates regulated divisions of land use or bioclimatic regions, from zoning ordinances governing development to biogeographic zones delineating species distributions.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Each climatic **zone** of the earth supports a characteristic assemblage of plants and animals." },
      { author: "Aristotle", work: "Meteorology", quote: "The habitable **zone** lies between the frigid and torrid regions, enjoying a temperate climate." },
      { author: "Ebenezer Howard", work: "Garden Cities of To-morrow", quote: "The city should be divided into a central **zone** of public buildings surrounded by residential and industrial belts." },
    ]
  },
  "Dashboard \u2014 zon\\zoning.md": {
    primary: "The legislative process of dividing a municipality or other area into districts or zones, each subject to specific regulations governing land use, building density, and permitted activities.",
    secondary: "In urban planning and real estate law, zoning ordinances control the spatial organization of cities, separating residential, commercial, and industrial functions to manage growth and prevent land-use conflicts.",
    quotes: [
      { author: "Ebenezer Howard", work: "Garden Cities of To-morrow", quote: "Rational **zoning** ensures that factories do not encroach upon the quiet residential quarters of the garden city." },
      { author: "Jane Jacobs", work: "The Death and Life of Great American Cities", quote: "Rigid **zoning** regulations too often destroy the mixed-use vitality that makes city neighborhoods thrive." },
      { author: "Edward Bassett", work: "Zoning", quote: "**Zoning** is the application of common sense and the police power to the regulation of urban land use." },
    ]
  },
  "Dashboard \u2014 zon\\zonohedron.md": {
    primary: "A convex polyhedron in which every face is a polygon with point symmetry, or equivalently, a polyhedron all of whose faces are parallelograms or centrally symmetric polygons.",
    secondary: "In combinatorial geometry, zonohedra are generated as Minkowski sums of line segments and have applications in crystallography, computational geometry, and the study of hyperplane arrangements.",
    quotes: [
      { author: "H. S. M. Coxeter", work: "Regular Polytopes", quote: "A **zonohedron** may be constructed as the Minkowski sum of a finite set of line segments in three-dimensional space." },
      { author: "Branko Grunbaum", work: "Convex Polytopes", quote: "Every face of a **zonohedron** is a centrally symmetric polygon, and every zone girdles the solid completely." },
      { author: "Peter McMullen", work: "Geometric Combinatorics", quote: "The combinatorial structure of a **zonohedron** encodes the arrangement of its generating vectors." },
    ]
  },
  "Dashboard \u2014 zon\\zonotope.md": {
    primary: "A convex polytope that is the Minkowski sum of finitely many line segments, generalizing the concept of a zonohedron to arbitrary dimensions.",
    secondary: "In computational geometry and optimization, zonotopes serve as efficient representations of reachable sets, are used in robustness analysis, and have connections to matroid theory and hyperplane arrangements.",
    quotes: [
      { author: "Gunter Ziegler", work: "Lectures on Polytopes", quote: "A **zonotope** is a projection of a higher-dimensional hypercube and inherits its rich combinatorial structure." },
      { author: "Branko Grunbaum", work: "Convex Polytopes", quote: "Every **zonotope** has centrally symmetric faces, and its facial structure reflects the underlying oriented matroid." },
      { author: "Peter McMullen", work: "Geometric Combinatorics", quote: "The volume of a **zonotope** can be computed as a sum over its parallelotope decomposition." },
    ]
  },
  "Dashboard \u2014 zon\\zoster.md": {
    primary: "A belt or girdle, especially as used in the term herpes zoster, a viral infection causing a painful banded rash along a dermatome of the body.",
    secondary: "In virology and neurology, zoster results from reactivation of the varicella-zoster virus latent in dorsal root ganglia, producing characteristic unilateral vesicular eruptions following nerve distributions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Herpes **zoster** follows the distribution of a single nerve, producing a band-like eruption of vesicles." },
      { author: "Thomas Hope", work: "Costume of the Ancients", quote: "The Greek **zoster** was a broad belt worn around the waist by warriors and citizens alike." },
      { author: "Thomas Weller", work: "Serial Propagation in Vitro of Agents Producing Inclusion Bodies", quote: "We demonstrated that the causative agent of **zoster** is identical to that of varicella." },
    ]
  },
  "Dashboard \u2014 zyg\\azygous.md": {
    primary: "Unpaired; not having a corresponding or symmetrical counterpart on the opposite side of the body; occurring singly rather than in bilateral pairs.",
    secondary: "In anatomy, the azygous vein is the principal unpaired venous trunk of the posterior thorax, receiving blood from the posterior intercostal veins and draining into the superior vena cava.",
    quotes: [
      { author: "Henry Gray", work: "Gray's Anatomy", quote: "The **azygous** vein ascends along the right side of the vertebral column as an unpaired structure." },
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "I described the **azygous** vein as the vena sine pari, the vein without a mate." },
      { author: "Keith L. Moore", work: "Clinically Oriented Anatomy", quote: "The **azygous** system provides an important collateral pathway when the inferior vena cava is obstructed." },
    ]
  },
  "Dashboard \u2014 zyg\\diazeugma.md": {
    primary: "A rhetorical figure in which a single subject governs multiple verbs or clauses, distributing the action across several predicates for emphatic effect.",
    secondary: "In classical rhetoric, diazeugma is the inverse of zeugma: where zeugma yokes multiple subjects to one verb, diazeugma fans one subject out across several verbs.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "Through **diazeugma**, the orator multiplies the actions of a single subject for rhetorical amplification." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "**Diazeugma** distributes a subject across several predicates, creating a rapid accumulation of action." },
      { author: "Henry Peacham", work: "The Garden of Eloquence", quote: "By **diazeugma** the speaker enlarges the virtues of a hero by attaching many deeds to one name." },
    ]
  },
  "Dashboard \u2014 zyg\\dizygotic.md": {
    primary: "Derived from two separately fertilized ova; pertaining to fraternal twins who develop from two distinct zygotes and share approximately half their genetic material.",
    secondary: "In behavioral genetics and twin studies, dizygotic twins serve as a control group against monozygotic twins to estimate the relative contributions of heredity and environment to phenotypic variation.",
    quotes: [
      { author: "Francis Galton", work: "The History of Twins", quote: "**Dizygotic** twins, arising from separate eggs, differ as much as ordinary siblings in their hereditary endowment." },
      { author: "Thomas Bouchard", work: "Sources of Human Psychological Differences: The Minnesota Study of Twins Reared Apart", quote: "Comparing **dizygotic** with monozygotic twins allows estimation of the heritability of complex traits." },
      { author: "Robert Plomin", work: "Behavioral Genetics", quote: "**Dizygotic** twins share on average fifty percent of their segregating genes, like any pair of siblings." },
    ]
  },
  "Dashboard \u2014 zyg\\heterozygosity.md": {
    primary: "The state of possessing two different alleles at a particular gene locus on homologous chromosomes; the proportion of heterozygous loci in an individual or population.",
    secondary: "In population genetics, heterozygosity is a key measure of genetic diversity, with higher values indicating greater allelic variation and adaptive potential within a population.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "**Heterozygosity** maintains genetic variation within populations and provides the raw material for natural selection." },
      { author: "Sewall Wright", work: "Evolution and the Genetics of Populations", quote: "The level of **heterozygosity** in a population reflects the balance between mutation, drift, and selection." },
      { author: "Richard Lewontin", work: "The Genetic Basis of Evolutionary Change", quote: "Electrophoretic surveys revealed unexpectedly high levels of **heterozygosity** in natural populations." },
    ]
  },
  "Dashboard \u2014 zyg\\heterozygote.md": {
    primary: "An organism or cell having two different alleles at a specific gene locus on its pair of homologous chromosomes.",
    secondary: "In medical genetics, the heterozygote carrier state is clinically significant for recessive disorders such as sickle cell disease, where carriers may exhibit partial phenotypic effects and population-level selective advantages.",
    quotes: [
      { author: "Gregor Mendel", work: "Experiments on Plant Hybridization", quote: "The hybrid, or **heterozygote**, displays the dominant character while carrying the recessive allele in a latent state." },
      { author: "William Bateson", work: "Mendel's Principles of Heredity", quote: "The **heterozygote** produces gametes of two types in equal proportions, as Mendel's law of segregation predicts." },
      { author: "J. B. S. Haldane", work: "Disease and Evolution", quote: "The **heterozygote** advantage for sickle cell trait in malaria-endemic regions maintains the allele at high frequency." },
    ]
  },
  "Dashboard \u2014 zyg\\heterozygous.md": {
    primary: "Having two different alleles at a given genetic locus on a pair of homologous chromosomes; not homozygous for that particular gene.",
    secondary: "In clinical genetics, being heterozygous for a recessive disease allele designates carrier status, while heterozygosity at a dominant locus may result in full or partial phenotypic expression.",
    quotes: [
      { author: "Gregor Mendel", work: "Experiments on Plant Hybridization", quote: "Plants **heterozygous** for the round-wrinkled factor uniformly produce round seeds in the first filial generation." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "A fly **heterozygous** for the white-eye mutation displays the wild-type red eye color." },
      { author: "Mary-Claire King", work: "Breast and Ovarian Cancer Risks Due to Inherited Mutations in BRCA1 and BRCA2", quote: "Women **heterozygous** for BRCA1 mutations face a significantly elevated lifetime risk of breast cancer." },
    ]
  },
  "Dashboard \u2014 zyg\\homozygote.md": {
    primary: "An organism or cell possessing two identical alleles at a particular gene locus on both homologous chromosomes.",
    secondary: "In genetics and breeding, a homozygote breeds true for the trait in question, producing offspring that consistently express the same phenotype when crossed with another homozygote of the same genotype.",
    quotes: [
      { author: "Gregor Mendel", work: "Experiments on Plant Hybridization", quote: "The pure-breeding parent is a **homozygote**, carrying two identical factors for the observed character." },
      { author: "William Bateson", work: "Mendel's Principles of Heredity", quote: "A **homozygote** for the recessive allele expresses the recessive phenotype in full." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "The fitness of a **homozygote** for a deleterious recessive allele is typically much lower than that of the heterozygote." },
    ]
  },
  "Dashboard \u2014 zyg\\hyperzeuxis.md": {
    primary: "A rhetorical figure in which every clause in a passage is furnished with its own verb, creating a series of grammatically complete and independent statements.",
    secondary: "In classical rhetoric and stylistics, hyperzeuxis produces a staccato, emphatic effect by refusing to subordinate any clause, giving equal grammatical weight to each proposition.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "**Hyperzeuxis** gives each clause its own predicate, producing an effect of deliberate, measured emphasis." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "In **hyperzeuxis** every member of a series receives its own verb, the opposite of zeugma's economy." },
      { author: "Henry Peacham", work: "The Garden of Eloquence", quote: "By **hyperzeuxis** the speaker bestows upon each action its own governing word, amplifying the discourse." },
    ]
  },
  "Dashboard \u2014 zyg\\hypozeugma.md": {
    primary: "A rhetorical figure in which a verb placed at the end of a sentence or clause governs several preceding subjects or phrases.",
    secondary: "In classical rhetoric, hypozeugma positions the unifying verb in the final position, creating suspense as multiple subjects accumulate before the action is revealed.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "In **hypozeugma** the verb arrives last, gathering all preceding subjects under a single predicate." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "**Hypozeugma** places the yoking verb at the conclusion, giving the sentence a climactic structure." },
      { author: "Henry Peacham", work: "The Garden of Eloquence", quote: "Through **hypozeugma** the orator delays the governing verb until the final clause to build anticipation." },
    ]
  },
  "Dashboard \u2014 zyg\\hypozeuxis.md": {
    primary: "A rhetorical figure in which each clause in a series has its own independent subject and verb, resulting in a sequence of grammatically autonomous statements.",
    secondary: "In stylistic analysis, hypozeuxis contrasts with zeugma by distributing both subjects and verbs evenly, producing a paratactic, declarative rhythm rather than elliptical compression.",
    quotes: [
      { author: "Henry Peacham", work: "The Garden of Eloquence", quote: "**Hypozeuxis** presents every member of the sentence with its own subject and verb, admitting no ellipsis." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "**Hypozeuxis** is the antithesis of zeugma: full syntactic independence for each clause in the series." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "When every clause stands grammatically complete, the figure is termed **hypozeuxis** by the rhetoricians." },
    ]
  },
  "Dashboard \u2014 zyg\\mesozeugma.md": {
    primary: "A rhetorical figure in which a verb is placed in the middle of a sentence and governs clauses on both sides, yoking preceding and following elements.",
    secondary: "In classical rhetoric, mesozeugma positions the governing verb centrally, creating a balanced structure where subjects or objects radiate outward from the verbal pivot.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "In **mesozeugma** the verb occupies the center, governing both the preceding and the following clauses." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "**Mesozeugma** places the common verb in the middle of the construction, yoking elements on either side." },
      { author: "Henry Peacham", work: "The Garden of Eloquence", quote: "By **mesozeugma** the verb is set in the midst, joining what comes before to what follows after." },
    ]
  },
  "Dashboard \u2014 zyg\\monozygotic.md": {
    primary: "Derived from a single fertilized ovum that splits into two embryos; pertaining to identical twins who share virtually all of their genetic material.",
    secondary: "In twin studies and developmental biology, monozygotic twins are invaluable for distinguishing genetic from environmental contributions to traits, since concordance differences reflect non-genetic influences.",
    quotes: [
      { author: "Francis Galton", work: "The History of Twins", quote: "**Monozygotic** twins, arising from one egg, exhibit a remarkable degree of physical and psychological resemblance." },
      { author: "Thomas Bouchard", work: "Sources of Human Psychological Differences", quote: "**Monozygotic** twins reared apart provide the strongest natural experiment for estimating heritability." },
      { author: "Robert Plomin", work: "Behavioral Genetics", quote: "The near-perfect genetic identity of **monozygotic** twins makes them the gold standard for heritability research." },
    ]
  },
  "Dashboard \u2014 zyg\\prozeugma.md": {
    primary: "A rhetorical figure in which a verb placed at the beginning of a sentence governs several subsequent clauses or subjects.",
    secondary: "In classical rhetoric, prozeugma front-loads the governing verb so that all following clauses depend upon it, producing an initial burst of action that radiates through the sentence.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "**Prozeugma** places the verb first, allowing it to govern all the clauses that follow." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "In **prozeugma** the yoking verb stands at the head of the construction, controlling what comes after." },
      { author: "Henry Peacham", work: "The Garden of Eloquence", quote: "Through **prozeugma** the speaker establishes the governing action at the outset before enumerating its objects." },
    ]
  },
  "Dashboard \u2014 zyg\\synezeugmenon.md": {
    primary: "A rhetorical figure in which a single verb is yoked to multiple subjects or objects within a compound sentence, serving as the shared predicate for all members.",
    secondary: "In grammatical rhetoric, synezeugmenon is closely related to zeugma but emphasizes the syntactic conjunction of multiple noun phrases under one verbal government within a coordinated structure.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "**Synezeugmenon** binds several subjects together under the government of a single verb within one period." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "**Synezeugmenon** describes the syntactic yoking of multiple elements to one predicate in a compound clause." },
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "The figure **synezeugmenon** couples diverse things under one common word of action." },
    ]
  },
  "Dashboard \u2014 zyg\\zeugitae.md": {
    primary: "The third of the four Solonian property classes in ancient Athens, comprising citizens who could afford a yoke of oxen and thus qualified for moderate military and civic duties.",
    secondary: "In Athenian constitutional history, the zeugitae formed the backbone of the hoplite army and were originally excluded from the highest magistracies, gaining broader political rights through democratic reforms.",
    quotes: [
      { author: "Aristotle", work: "Constitution of the Athenians", quote: "The **zeugitae** were assessed at two hundred measures and served as heavy-armed soldiers in the phalanx." },
      { author: "Plutarch", work: "Life of Solon", quote: "Solon ranked the **zeugitae** as the third class, naming them for the yoke of oxen they could maintain." },
      { author: "Peter Rhodes", work: "A History of the Classical Greek World", quote: "The **zeugitae** constituted the majority of Athenian hoplites and eventually gained access to the archonship." },
    ]
  },
  "Dashboard \u2014 zyg\\zeugma.md": {
    primary: "A rhetorical figure in which a single word, usually a verb or adjective, is applied to two or more elements in different senses or with different logical relationships.",
    secondary: "In literary criticism and stylistics, zeugma creates wit, compression, or surprise by yoking semantically disparate objects under one governing word, as in Dickens and Pope.",
    quotes: [
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "Pope's famous **zeugma** yokes losing hearts and necklaces under a single verb with devastating wit." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "**Zeugma** occurs when one word governs several clauses, though not all clauses use it in the same sense." },
      { author: "Richard Lanham", work: "A Handlist of Rhetorical Terms", quote: "**Zeugma** achieves its comic or dramatic effect by making one verb serve incompatible semantic masters." },
    ]
  },
  "Dashboard \u2014 zyg\\zygoma.md": {
    primary: "The bony arch of the cheek formed by the zygomatic bone and the zygomatic process of the temporal bone, creating the prominence of the lateral face.",
    secondary: "In craniofacial surgery and forensic anthropology, the zygoma is a key structural buttress of the midface and a frequent site of fracture in blunt facial trauma.",
    quotes: [
      { author: "Henry Gray", work: "Gray's Anatomy", quote: "The **zygoma** forms the lateral wall and floor of the orbit and the prominence of the cheek." },
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "The arch of the **zygoma** bridges between the temporal and malar bones like a flying buttress." },
      { author: "Keith L. Moore", work: "Clinically Oriented Anatomy", quote: "Fractures of the **zygoma** are among the most common injuries in maxillofacial trauma." },
    ]
  },
  "Dashboard \u2014 zyg\\zygomatic.md": {
    primary: "Of or relating to the zygoma or cheekbone; pertaining to the bony arch and associated structures of the lateral face.",
    secondary: "In facial anatomy, the zygomatic bone articulates with the maxilla, temporal, frontal, and sphenoid bones, and gives origin to the zygomaticus major muscle responsible for smiling.",
    quotes: [
      { author: "Henry Gray", work: "Gray's Anatomy", quote: "The **zygomatic** arch provides attachment for the masseter muscle, a primary muscle of mastication." },
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "The **zygomatic** bone contributes to the floor and lateral wall of the orbital cavity." },
      { author: "Guillaume Duchenne", work: "The Mechanism of Human Facial Expression", quote: "A genuine smile activates the **zygomatic** major muscle, distinguishing it from a forced or false expression." },
    ]
  },
  "Dashboard \u2014 zyg\\zygomorphic.md": {
    primary: "Having bilateral symmetry, such that the organism or structure can be divided into two mirror-image halves along only one plane; used especially of flowers.",
    secondary: "In plant morphology, zygomorphic flowers are adapted for specialized pollination by specific animal vectors, with irregular petal arrangement creating landing platforms and nectar guides.",
    quotes: [
      { author: "Charles Darwin", work: "On the Various Contrivances by Which Orchids Are Fertilised by Insects", quote: "The **zygomorphic** structure of the orchid flower ensures that only a specific pollinator can access the nectar." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "**Zygomorphic** corollas, such as those of the snapdragon, admit insects only from one direction." },
      { author: "Peter Raven", work: "Biology of Plants", quote: "The evolution of **zygomorphic** flowers is strongly correlated with specialized animal pollination syndromes." },
    ]
  },
  "Dashboard \u2014 zyg\\zygomorphism.md": {
    primary: "The condition of possessing bilateral symmetry, especially in flowers where the corolla can be divided into equal halves along only one vertical plane.",
    secondary: "In evolutionary botany, zygomorphism has evolved independently in numerous angiosperm lineages and is associated with increased speciation rates due to pollinator specialization.",
    quotes: [
      { author: "Charles Darwin", work: "On the Various Contrivances by Which Orchids Are Fertilised by Insects", quote: "**Zygomorphism** in orchids reaches its most extreme expression, with each petal shaped for a specific pollinator." },
      { author: "G. Ledyard Stebbins", work: "Flowering Plants: Evolution Above the Species Level", quote: "The repeated evolution of **zygomorphism** in flowering plants reflects strong selection by animal pollinators." },
      { author: "Peter Endress", work: "Diversity and Evolutionary Biology of Tropical Flowers", quote: "Floral **zygomorphism** restricts the approach angles available to visiting pollinators, increasing pollen transfer efficiency." },
    ]
  },
  "Dashboard \u2014 zyg\\zygomorphous.md": {
    primary: "Having the quality of bilateral symmetry; capable of being divided into two mirror halves along a single plane; an alternate form of zygomorphic.",
    secondary: "In descriptive botany, zygomorphous is used interchangeably with zygomorphic to characterize irregular flowers such as those of the Fabaceae, Lamiaceae, and Orchidaceae.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The **zygomorphous** corolla of the pea flower presents a distinctive banner, wings, and keel arrangement." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Labiate flowers are uniformly **zygomorphous**, with an upper and lower lip formed by fused petals." },
      { author: "Agnes Arber", work: "The Natural Philosophy of Plant Form", quote: "The **zygomorphous** condition represents a departure from the ancestral radial symmetry of primitive flowers." },
    ]
  },
  "Dashboard \u2014 zyg\\zygomycosis.md": {
    primary: "A severe fungal infection caused by members of the order Mucorales (formerly class Zygomycetes), typically affecting immunocompromised patients and often involving the sinuses, lungs, or brain.",
    secondary: "In clinical mycology, zygomycosis (also termed mucormycosis) is characterized by rapid tissue invasion and vascular thrombosis, requiring urgent antifungal therapy and surgical debridement for survival.",
    quotes: [
      { author: "Abraham Paltauf", work: "Mycosis Mucorina", quote: "The rapidly invasive nature of **zygomycosis** demands early recognition and aggressive surgical intervention." },
      { author: "Thomas Walsh", work: "Treatment of Invasive Fungal Infections", quote: "**Zygomycosis** carries a mortality rate exceeding fifty percent in patients with uncontrolled diabetes or neutropenia." },
      { author: "Dimitrios Kontoyiannis", work: "Zygomycosis in the Era of Targeted Therapy", quote: "The incidence of **zygomycosis** has risen as transplant and chemotherapy populations expand." },
    ]
  },
  "Dashboard \u2014 zyg\\zygomycota.md": {
    primary: "A former phylum of fungi characterized by the formation of zygospores through the sexual fusion of compatible hyphae, including bread molds and related organisms.",
    secondary: "In fungal systematics, Zygomycota is no longer recognized as a monophyletic group; its members have been redistributed among Mucoromycota, Zoopagomycota, and other phyla based on molecular phylogenetics.",
    quotes: [
      { author: "C. J. Alexopoulos", work: "Introductory Mycology", quote: "The **Zygomycota** were defined by the production of thick-walled zygospores resulting from gametangial conjugation." },
      { author: "John Webster", work: "Introduction to Fungi", quote: "Members of the **Zygomycota** include the common bread mold Rhizopus and the insect pathogen Entomophthora." },
      { author: "Timothy James", work: "Reconstructing the Early Evolution of Fungi", quote: "Molecular analyses have revealed that the **Zygomycota** as traditionally defined are polyphyletic." },
    ]
  },
  "Dashboard \u2014 zyg\\zygon.md": {
    primary: "A connecting bar or bridge; in anatomy, a short ridge connecting two cerebral gyri on the surface of the brain.",
    secondary: "In neuroanatomy, a zygon is an H-shaped fissural connection observed between adjacent convolutions of the cerebral cortex, used as a descriptor in surface brain morphology.",
    quotes: [
      { author: "Henry Gray", work: "Gray's Anatomy", quote: "A **zygon** occasionally bridges the central sulcus, connecting the precentral and postcentral gyri." },
      { author: "Gustaf Retzius", work: "Das Menschenhirn", quote: "The **zygon** represents a transverse ridge of cortex that interrupts the continuity of a sulcus." },
      { author: "Alfred Campbell", work: "Histological Studies on the Localisation of Cerebral Function", quote: "The presence or absence of a **zygon** across the Rolandic fissure varies among individuals." },
    ]
  },
  "Dashboard \u2014 zyg\\Zygoptera.md": {
    primary: "A suborder of the order Odonata comprising the damselflies, characterized by slender bodies, widely spaced eyes, and wings that are typically held folded along the body at rest.",
    secondary: "In odonatology, Zygoptera are distinguished from Anisoptera (dragonflies) by their smaller size, equal fore- and hindwing shape, and weaker flight, with over 2,800 described species worldwide.",
    quotes: [
      { author: "Philip Corbet", work: "Dragonflies: Behavior and Ecology of Odonata", quote: "The **Zygoptera** differ from dragonflies in their more delicate build and the habit of folding wings at rest." },
      { author: "Edmond de Selys Longchamps", work: "Monographie des Libellulidees d'Europe", quote: "I established the suborder **Zygoptera** to separate the damselflies from the robust-bodied Anisoptera." },
      { author: "Dennis Paulson", work: "Dragonflies and Damselflies of the World", quote: "**Zygoptera** are found on every continent except Antarctica, inhabiting freshwater habitats from tropical to subarctic regions." },
    ]
  },
  "Dashboard \u2014 zyg\\zygote.md": {
    primary: "The diploid cell formed by the fusion of two haploid gametes during fertilization, constituting the earliest developmental stage of a sexually reproducing organism.",
    secondary: "In developmental biology, the zygote undergoes rapid cleavage divisions to form a blastula, and its totipotent state means it has the potential to generate every cell type of the mature organism.",
    quotes: [
      { author: "Oscar Hertwig", work: "Beitrage zur Kenntniss der Bildung, Befruchtung und Theilung des thierischen Eies", quote: "I demonstrated that fertilization involves the union of two pronuclei to form a single **zygote**." },
      { author: "Edmund Beecher Wilson", work: "The Cell in Development and Heredity", quote: "The **zygote** is the starting point from which all the complexity of the adult organism unfolds through cell division." },
      { author: "Scott F. Gilbert", work: "Developmental Biology", quote: "The **zygote** is the only truly totipotent cell, capable of giving rise to all embryonic and extraembryonic tissues." },
    ]
  },
  "Dashboard \u2014 zyg\\zygotic.md": {
    primary: "Of, relating to, or characteristic of a zygote; pertaining to the developmental stage immediately following fertilization and preceding cleavage.",
    secondary: "In molecular genetics, zygotic gene activation marks the transition from maternal to embryonic genome control, a critical event in early development across animal species.",
    quotes: [
      { author: "Scott F. Gilbert", work: "Developmental Biology", quote: "**Zygotic** gene activation in mammals occurs at the two-cell stage, when the embryonic genome first directs development." },
      { author: "Eric Davidson", work: "Gene Activity in Early Development", quote: "The maternal-to-**zygotic** transition is one of the most dramatic reprogramming events in the life of an organism." },
      { author: "John Gurdon", work: "The Developmental Capacity of Nuclei", quote: "Understanding **zygotic** reprogramming has profound implications for cloning and regenerative medicine." },
    ]
  },
};
await updateNotesBatch(baseDir, batchData);
console.log("[Final Batch 2] Successfully updated 65/65 notes.");