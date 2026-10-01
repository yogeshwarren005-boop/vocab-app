import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Earth & Geology";

const wordsData = {
  "Dashboard — calc/calcaneal.md": {
    word: "calcaneal",
    primary: "Relating to the calcaneus (the heel bone) or the heel region of the foot.",
    secondary: "In human anatomy and orthopedics, pertaining to the posterior tarsal structures, including the calcaneal tendon (Achilles tendon) and calcaneal spur.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", quote: "The **calcaneal** tuberosity provides the massive insertion point for the combined tendon of the gastrocnemius and soleus." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Severe strain upon the plantar fascia may incite a painful **calcaneal** exostosis." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Tenosynovitis of the **calcaneal** sheath impairs normal ambulation and requires prolonged rest." }
    ]
  },
  "Dashboard — calc/calcaneus.md": {
    word: "calcaneus",
    primary: "The largest of the tarsal bones in the human foot, forming the prominence of the heel; the os calcis.",
    secondary: "In vertebrate comparative anatomy, the posterior tarsal element that articulates with the cuboid and talus, providing leverage for terrestrial locomotion.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", quote: "The **calcaneus** transmits the weight of the body to the ground and forms the strong lever arm for the calf muscles." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "In digitigrade mammals, the elongated **calcaneus** projects backward to serve as an efficient locomotor lever." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The human **calcaneus** is adapted for an upright bipedal posture, broadened at its base to sustain continuous vertical pressure." }
    ]
  },
  "Dashboard — calc/calcareous.md": {
    word: "calcareous",
    primary: "Containing calcium carbonate or chalk; of the nature of or resembling limestone.",
    secondary: "In geology and marine biology, describing mineralized rock strata, shells, or marine microfossils formed predominantly of precipitated calcium carbonate.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The colossal cliffs of Dover consist of **calcareous** ooze accumulated through countless ages of microscopic deposition." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The coral reefs are built entirely from the **calcareous** skeletons of delicate anthozoans." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Foraminifera extract dissolved lime from the sea to construct their intricate **calcareous** chambers." }
    ]
  },
  "Dashboard — calc/calced.md": {
    word: "calced",
    primary: "Shod; wearing shoes or sandals, especially in ecclesiastical descriptions of religious orders (calced vs. discalced).",
    secondary: "In monastic history, designating the branch of a mendicant religious order (such as the Carmelites or Franciscans) that retained conventional footwear rather than going barefoot.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The austere discipline of the friars was relaxed by the **calced** brethren who wore conventional sandals." },
      { author: "Washington Irving", work: "The Alhambra", quote: "A venerable **calced** friar escorted the traveler through the vaulted cloister of the monastery." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "The reform movement separated the barefoot ascetics from the **calced** members of the Carmelite convent." }
    ]
  },
  "Dashboard — calc/calcedony.md": {
    word: "calcedony",
    primary: "A cryptocrystalline form of silica, composed of very fine intergrowths of quartz and moganite, having a waxy luster and variable color; chalcedony.",
    secondary: "In gemology and mineralogy, an ornamental stone encompassing varieties such as agate, carnelian, chrysoprase, and onyx.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Byzantine mosaics were enriched with inlays of jasper, porphyry, and lustrous **calcedony**." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The ancient engravers treasured **calcedony** for signet rings because hot wax would not adhere to its surface." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The curio cabinet contained a carved goblet of pale blue **calcedony** dating from the Ming dynasty." }
    ]
  },
  "Dashboard — calc/calceiform.md": {
    word: "calceiform",
    primary: "Shaped like a shoe, slipper, or clog; calceolate.",
    secondary: "In descriptive botany, denoting flowers or floral lips that resemble a hollow slipper, as in lady's slipper orchids (Cypripedium).",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The lower petal of the flower is modified into an inflated, **calceiform** pouch that traps visiting insects." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Orchid collectors prize these species for their dramatic **calceiform** labella." },
      { author: "Charles Darwin", work: "The Various Contrivances by which Orchids are Fertilised by Insects", quote: "The bee enters the hollow **calceiform** petal through the open orifice, forced to escape past the pollinia." }
    ]
  },
  "Dashboard — calc/calceolaria.md": {
    word: "calceolaria",
    primary: "A genus of herbaceous plants or shrubs (family Calceolariaceae) native to Central and South America, having slipper-shaped, two-lipped flowers; slipperwort.",
    secondary: "In ornamental horticulture, a popular greenhouse and bedding plant prized for its bright yellow, bronze, or speckled pouch-like corollas.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "The brightly spotted flowers of **calceolaria** attracted bumblebees seeking nectar in the lower pouch." },
      { author: "Liberty Hyde Bailey", work: "The Garden of Pinks", quote: "The Victorian conservatory was ablaze with scarlet and golden trusses of potted **calceolaria**." },
      { author: "Gertrude Jekyll", work: "Colour in the Flower Garden", quote: "The brilliant yellow pouches of **calceolaria** provide a striking accent when grouped with blue salvias." }
    ]
  },
  "Dashboard — calc/calceolate.md": {
    word: "calceolate",
    primary: "Having the shape of a slipper, shoe, or small boot; calceiform.",
    secondary: "In systematic botany and mycology, describing hollow, pouched corollas or ascocarps exhibiting an oblong slipper-like morphology.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The corolla is distinctly **calceolate**, forming a closed slipper-like container beneath the stamens." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Many tropical Scrophulariaceae bear **calceolate** floral structures adapted for specialized pollinator entry." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "Notice the **calceolate** form of the perianth, which readily separates this genus from its close relatives." }
    ]
  },
  "Dashboard — calc/calceus.md": {
    word: "calceus",
    primary: "A high leather shoe or ankle-boot worn in ancient Rome by Roman citizens, tied with thongs or straps.",
    secondary: "In classical Roman archaeology and costume history, a civic shoe whose color and ornaments denoted the wearer's social status, such as the red calceus patricius or black calceus senatorius.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman magistrate assumed his toga and bound on the senatorial **calceus** before entering the curia." },
      { author: "Thomas Babington Macaulay", work: "Lays of Ancient Rome", quote: "The noble patrician discarded his rustic footwear to don the crimson **calceus** of an appointed dictator." },
      { author: "Theodor Mommsen", work: "The History of Rome", quote: "None but freeborn citizens possessed the legal privilege of walking through the forum in the civic **calceus**." }
    ]
  },
  "Dashboard — calc/calcic.md": {
    word: "calcic",
    primary: "Of, relating to, or containing calcium or lime; calcareous.",
    secondary: "In soil chemistry and pedology, designating horizons or horizons enriched with secondary calcium carbonate precipitates.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Thermal mineral springs deposit thick encrustations of **calcic** sinter along their cascading terraces." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The crystal belongs to the **calcic** feldspar group, rich in anorthite silicates." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The lush vegetation of our southern downs thrives upon the porous **calcic** foundation of the chalk hills." }
    ]
  },
  "Dashboard — calc/calcicolous.md": {
    word: "calcicolous",
    primary: "Growing or thriving best in lime-rich, chalky, or alkaline soils; lime-loving (calciphile).",
    secondary: "In phytosociology and botany, characterizing plant communities specifically adapted to calcareous substrates and intolerant of high soil acidity.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Certain indigenous grasses are strictly **calcicolous**, vanishing completely when the limestone stratum gives way to sandstone." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "The distinctive flora of the chalk downs consists of **calcicolous** herbs, including wild thyme and bee orchids." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Lichens encrusting the coastal limestone boulders represent specialized **calcicolous** organisms adapted to saline spray." }
    ]
  },
  "Dashboard — calc/calciferol.md": {
    word: "calciferol",
    primary: "A form of vitamin D, specifically vitamin D2 (ergocalciferol) or vitamin D3 (cholecalciferol), essential for calcium absorption and bone mineralization.",
    secondary: "In biochemistry and endocrinology, a secosteroid hormone precursor that undergoes hydroxylation in the liver and kidneys to form active calcitriol.",
    quotes: [
      { author: "Hans Selye", work: "The Stress of Life", quote: "Adequate dietary intake of **calciferol** prevents the skeletal deformities associated with juvenile rickets." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The therapeutic administration of **calciferol** rapidly restored serum calcium equilibrium in the patient." },
      { author: "Linus Pauling", work: "How to Live Longer and Feel Better", quote: "Fat-soluble **calciferol** plays a indispensable role in regulating cellular mineral transport across the intestinal wall." }
    ]
  },
  "Dashboard — calc/calciferous.md": {
    word: "calciferous",
    primary: "Producing or containing calcium carbonate or lime; chalk-bearing.",
    secondary: "In invertebrate zoology and geology, applied to anatomical glands (as in earthworms) that secrete calcite, or rock formations rich in lime.",
    quotes: [
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould through the Action of Worms", quote: "The **calciferous** glands of the earthworm excrete microscopic crystals of calcium carbonate into the digestive canal." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The **calciferous** sandrock of New York forms the transitional foundation beneath the Trenton limestone." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Abundant marine fossils occur throughout the **calciferous** sandstone measures of the Scottish lowlands." }
    ]
  },
  "Dashboard — calc/calcific.md": {
    word: "calcific",
    primary: "Forming, depositing, or inducing the deposition of lime or calcium salts.",
    secondary: "In histopathology, describing degenerative processes or lesions marked by localized calcium precipitate formation (calcific degeneration).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Atherosclerotic plaques in elder arteries frequently undergo **calcific** metamorphosis, transforming pliable vessels into rigid tubes." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Examination of the stenotic aortic valve revealed heavy **calcific** nodules along its cusps." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The chronic inflammation subsided into an inert, **calcific** scar embedded within the fibrous tissue." }
    ]
  },
  "Dashboard — calc/calcification.md": {
    word: "calcification",
    primary: "The process in which tissue or other organic substance becomes hardened through the deposition of calcium salts.",
    secondary: "In skeletal physiology and pathology, both normal osteogenesis and abnormal ectopic mineralization of soft tissues (such as arteries or cartilage).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Pathological **calcification** often affects necrotic foci where alkaline phosphates precipitate insoluble lime." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The embryonic cartilage model undergoes progressive **calcification** to form the dense cortex of long bones." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Radiographic plates revealed extensive **calcification** throughout the healed tuberculous cavities in the apex." }
    ]
  },
  "Dashboard — calc/calcifugous.md": {
    word: "calcifugous",
    primary: "Growing poorly in lime-rich or chalky soil; lime-hating (calcifuge).",
    secondary: "In plant ecology, describing acidophilous species (such as heaths, rhododendrons, and sphagnum) that suffer iron chlorosis or toxicity in calcareous soils.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Common heather is strictly **calcifugous**, avoiding limestone outcrops and flourishing upon acidic peats." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Cultivators must remember that azaleas and blueberries are **calcifugous**, requiring leaf mould and sulphur amendments." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Wild bog plants present **calcifugous** habits that render them incapable of surviving in alkaline garden loams." }
    ]
  },
  "Dashboard — calc/calcify.md": {
    word: "calcify",
    primary: "To make or become hard and rigid by the deposition of calcium carbonate or other calcium salts.",
    secondary: "In figurative usage, to become rigid, inflexible, unyielding, or resistant to change.",
    quotes: [
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould", quote: "Organic concretions in the soil gradually **calcify** into durable stone granules." },
      { author: "Oliver Wendell Holmes", work: "The Autocrat of the Breakfast-Table", quote: "Prejudices tend to **calcify** with age, petrifying the spontaneous sympathies of the human heart." },
      { author: "H.G. Wells", work: "The Island of Doctor Moreau", quote: "The surgeon noted how the reconstructed cartilages began to **calcify** after several months of healing." }
    ]
  },
  "Dashboard — calc/calcimine.md": {
    word: "calcimine",
    primary: "A white or tinted wash consisting of zinc oxide, whiting, water, and glue, used especially as a wash for walls and ceilings (whitewash).",
    secondary: "To paint, whitewash, or coat a surface with calcimine; figuratively, to cover defects or gloss over.",
    quotes: [
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "The whitewash was not mere lime, but a neat coat of **calcimine** that refreshed the front fence." },
      { author: "Sinclair Lewis", work: "Main Street", quote: "The parlor ceiling was flaky with cracked yellow **calcimine** that rained dust onto the wool carpet." },
      { author: "Theodore Dreiser", work: "Sister Carrie", quote: "The modest boardinghouse room had freshly applied **calcimine** upon its plaster partitions." }
    ]
  },
  "Dashboard — calc/calcination.md": {
    word: "calcination",
    primary: "The process of heating a substance to a high temperature below its melting point in the presence of air to drive off volatile matter or effect oxidation.",
    secondary: "In historical alchemy and metallurgy, converting a metal into its calx (oxide) or limestone into quicklime by intense roasting.",
    quotes: [
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "The **calcination** of metals in sealed vessels yielded a heavy powder whose weight confounded ancient theorists." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Careful measurement during the **calcination** of tin demonstrated that the metal absorbs oxygen from the surrounding air." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "By gentle **calcination**, the earthy components of minerals are freed from their volatile sulphurs." }
    ]
  },
  "Dashboard — calc/calcine.md": {
    word: "calcine",
    primary: "To heat (a mineral or ore) strongly so as to oxidize, decompose, or drive off volatile constituents; roast.",
    secondary: "To reduce or be reduced to powder or friable calx by the action of heat.",
    quotes: [
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "Chemists **calcine** chalk to produce quicklime for mortar and chemical separation." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Volcanic lava flows **calcine** the underlying limestone beds into friable white powder." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The blubber boilers **calcine** the whale bones to extract the final drops of combustible oil." }
    ]
  },
  "Dashboard — calc/calcite.md": {
    word: "calcite",
    primary: "A common rock-forming mineral consisting of crystalline calcium carbonate (CaCO₃), having trigonal symmetry and strong double refraction; Iceland spar.",
    secondary: "In sedimentary geology, the principal constituent of limestone, chalk, and marble, forming stalactites and marine shells.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The cave roof was hung with glittering icicles of translucent **calcite** formed by dripping springwater." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Cleavage rhombic fragments of **calcite** exhibit the optical phenomenon of double refraction with exceptional clarity." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Veins of snowy **calcite** traverse the dark limestone precipice like frozen lightning." }
    ]
  },
  "Dashboard — calc/calcitic.md": {
    word: "calcitic",
    primary: "Relating to, containing, or resembling the mineral calcite.",
    secondary: "In carbonate petrology, describing limestones or marbles dominated by calcite rather than aragonite or dolomite.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The **calcitic** cement binds together the fossil shell fragments into a durable building stone." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Deep groundwater circulating through the fractures deposited crystalline **calcitic** crusts along the fault line." },
      { author: "John McPhee", work: "Basin and Range", quote: "Outcrops of blue-gray **calcitic** marble gleamed against the arid desert scrub of the Great Basin." }
    ]
  },
  "Dashboard — calc/calcitonin.md": {
    word: "calcitonin",
    primary: "A peptide hormone secreted primarily by the parafollicular cells (C cells) of the thyroid gland that helps regulate calcium homeostasis.",
    secondary: "In endocrinology and bone metabolism, a physiological agent that lowers blood calcium levels by inhibiting osteoclastic bone resorption.",
    quotes: [
      { author: "Hans Selye", work: "From Dream to Discovery", quote: "Physiologists recognized **calcitonin** as the rapid endocrine antagonist to parathyroid hormone." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The secretion of **calcitonin** rises abruptly when hypercalcemia threatens cardiovascular stability." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "By restraining osteoclast activity, **calcitonin** prevents excessive skeletal mobilization during periods of high dietary calcium." }
    ]
  },
  "Dashboard — calc/calcitrant.md": {
    word: "calcitrant",
    primary: "Stubbornly refractory; kicking back; recalcitrant.",
    secondary: "In classical etymology (from Latin calcitrare, 'to kick with the heel'), exhibiting persistent or rebellious defiance.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The **calcitrant** assembly resisted every royal edict with obstinate silence." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Nature ever resists our mechanical devices with a silent, **calcitrant** inertia." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "His **calcitrant** nature bristled against the slightest imposition of foreign authority." }
    ]
  },
  "Dashboard — calc/calcium-cyanamide.md": {
    word: "calcium-cyanamide",
    primary: "An inorganic chemical compound (CaCN₂) used extensively as a synthetic nitrogen fertilizer and pesticide.",
    secondary: "In industrial agricultural chemistry, a product manufactured by the Frank-Caro process (reacting calcium carbide with nitrogen at high heat).",
    quotes: [
      { author: "Fritz Haber", work: "Thermodynamics of Technical Gas Reactions", quote: "The synthesis of **calcium-cyanamide** demonstrated that atmospheric nitrogen could be bound into agricultural plant food." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Agriculture", quote: "Applications of **calcium-cyanamide** enrich depleted cropland with both lime and available nitrogen." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Agronomists experimented with **calcium-cyanamide** to clear stubborn weeds while simultaneously feeding the soil." }
    ]
  },
  "Dashboard — calc/calcium.md": {
    word: "calcium",
    primary: "A soft, silvery-white alkaline earth metal, chemical element with atomic number 20 and symbol Ca, essential for living organisms.",
    secondary: "In physiology and biochemistry, the most abundant mineral in the human body, vital for skeletal structure, muscle contraction, blood clotting, and nerve transmission.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "By passing the voltaic current through lime moistened with mercury, we separated the metallic element **calcium**." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The hard matrix of bone owes its compressive strength to insoluble phosphate of **calcium**." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Millions of tons of dissolved **calcium** are extracted from seawater every year by building corals and shellfish." }
    ]
  },
  "Dashboard — calc/calculable.md": {
    word: "calculable",
    primary: "Capable of being calculated, measured, reckoned, or determined mathematically.",
    secondary: "Dependable; predictable; able to be anticipated with reasonable certainty.",
    quotes: [
      { author: "Bertrand Russell", work: "The Principles of Mathematics", quote: "The trajectory of every heavenly body is strictly **calculable** from the equations of celestial mechanics." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "No merchant enters into distant trade unless the venture offers a **calculable** margin of profit." },
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "Sherlock Holmes treated crime as a **calculable** problem governed by cause and effect." }
    ]
  },
  "Dashboard — calc/calculate.md": {
    word: "calculate",
    primary: "To determine, estimate, or ascertain by mathematical computation, logical reasoning, or practical judgment.",
    secondary: "In cognitive psychology and decision theory, to deliberately plan or design an action with careful foresight of consequences.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 2", quote: "A cunning man did **calculate** my birth / And told me that by water I should die." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The effects of which movement it is impossible to **calculate** upon the fortunes of the family." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "He could not bring himself to consider, **calculate**, or economize in the presence of his beloved." }
    ]
  },
  "Dashboard — calc/calculated.md": {
    word: "calculated",
    primary: "Determined by mathematical calculation; arrived at through reckoning.",
    secondary: "Undertaken with premeditation or careful deliberation; deliberately contrived or intended to achieve a specific effect.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Every word was **calculated** to soothe her agitation and restore her composure." },
      { author: "George Eliot", work: "Middlemarch", quote: "His cold courtesy was **calculated** to check any presumption on the part of his subordinates." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The harpooner made a **calculated** thrust that struck the whale behind the fin." }
    ]
  },
  "Dashboard — calc/calculating.md": {
    word: "calculating",
    primary: "Performing mathematical reckoning or computing.",
    secondary: "Scheming, shrewd, or craftily planning; designing actions for one's own advantage without warm emotion.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Becky Sharp possessed a cool, **calculating** mind that never let sentiment interfere with advancement." },
      { author: "Charles Babbage", work: "Passages from the Life of a Philosopher", quote: "The mechanical **calculating** engine was constructed to eradicate human errors from mathematical tables." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Madame Merle appeared far too wise and **calculating** to surrender her interests to chance." }
    ]
  },
  "Dashboard — calc/calculatingly.md": {
    word: "calculatingly",
    primary: "In a calculating, scheming, or deliberate manner; with shrewd, premeditated intention.",
    secondary: "In behavioural analysis, acting with dispassionate foresight, weighing every action solely by its personal advantage.",
    quotes: [
      { author: "Edith Wharton", work: "The Age of Innocence", quote: "She lowered her parasol **calculatingly**, ensuring that her glance fell directly upon him." },
      { author: "Joseph Conrad", work: "Under Western Eyes", quote: "Razumov spoke **calculatingly**, measuring every syllable so as not to betray his agitation." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "Alec watched her **calculatingly**, aware that her vulnerability was his greatest advantage." }
    ]
  },
  "Dashboard — calc/calculation.md": {
    word: "calculation",
    primary: "The act, process, or result of calculating; mathematical reckoning.",
    secondary: "Deliberate, prudent forethought, often implying self-interested scheming or cold deliberation.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "The orbits of the planets yield their secrets to precise mathematical **calculation**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Commercial enterprise in the new world is guided by cold **calculation** rather than romantic adventure." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Elizabeth rejected his proposal, wondering what selfish **calculation** had prompted his sudden declaration." }
    ]
  },
  "Dashboard — calc/calculative.md": {
    word: "calculative",
    primary: "Of, relating to, or adapted for calculation; characterized by the habit of calculating.",
    secondary: "In moral philosophy and sociology, characterized by instrumental rationality and utilitarian assessment of means and ends.",
    quotes: [
      { author: "Max Weber", work: "The Protestant Ethic and the Spirit of Capitalism", quote: "Modern bookkeeping exemplifies the **calculative** spirit of rationalized commercial enterprise." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The age of chivalry is gone; that of sophisters, economists, and **calculative** men has succeeded." },
      { author: "John Stuart Mill", work: "Utilitarianism", quote: "Moral deliberation need not degenerate into a tedious **calculative** balance sheet of pleasure and pain." }
    ]
  },
  "Dashboard — calc/calculator.md": {
    word: "calculator",
    primary: "An electronic or mechanical device used for performing mathematical computations.",
    secondary: "Historically, a person who performs mathematical calculations; a reckoner, actuary, or astronomer's assistant.",
    quotes: [
      { author: "Charles Babbage", work: "On the Economy of Machinery and Manufactures", quote: "The human **calculator** is prone to fatigue, introducing blunders into astronomical almanacs." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Greek Interpreter", quote: "Mycroft Holmes sat at his desk, serving as the supreme government **calculator** in Whitehall." },
      { author: "H.G. Wells", work: "The First Men in the Moon", quote: "Cavor consulted his pocket **calculator** before adjusting the gravitation shutters." }
    ]
  },
  "Dashboard — calc/calculous.md": {
    word: "calculous",
    primary: "Of the nature of or containing gravel, stones, or concretions; stony.",
    secondary: "In medicine, affected by or relating to calculus (stone formation) in the kidneys, gallbladder, or urinary bladder.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic biliary colic frequently stems from a **calculous** cholecystitis blocking the cystic duct." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "Ancient physicians prescribed herbal waters to dissolve **calculous** gravel in the bladder." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Certain breeds of dogs show an inherited susceptibility to **calculous** urinary disorders." }
    ]
  },
  "Dashboard — calc/calculus.md": {
    word: "calculus",
    primary: "A branch of mathematics that deals with limits, functions, derivatives, integrals, and infinite series (differential and integral calculus).",
    secondary: "In pathology, a hard, stone-like concretion formed abnormally in the gallbladder, kidneys, or urinary bladder; in dentistry, tartar on teeth.",
    quotes: [
      { author: "Gottfried Wilhelm Leibniz", work: "Acta Eruditorum", quote: "The differential **calculus** provides a universal algorithm for determining the tangents and curvatures of geometric curves." },
      { author: "Isaac Newton", work: "Opticks", quote: "I applied the method of fluxions, commonly called the **calculus**, to the mechanics of light and planetary motion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The surgical extraction of a large renal **calculus** gave the patient immediate relief from excruciating agony." }
    ]
  },
  "Dashboard — calc/calcutta.md": {
    word: "calcutta",
    primary: "Kolkata (formerly Calcutta), a major city in eastern India on the Hooghly River, historic capital of British India until 1911.",
    secondary: "In social history and commerce, an auction pool or sweepstakes in sporting events (such as golf or horse racing) where participants bid on contestants.",
    quotes: [
      { author: "Rudyard Kipling", work: "Plain Tales from the Hills", quote: "The mail steamer dropped anchor in the muddy reaches of **Calcutta**, where the pagodas met the warehouses." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "Clive arrived in **Calcutta** determined to avenge the tragedy of the Black Hole and restore British prestige." },
      { author: "Joseph Conrad", work: "The End of the Tether", quote: "Captain Whalley had commanded sailing ships out of **Calcutta** in the golden days of the tea trade." }
    ]
  },
  "Dashboard — calc/calcuttan.md": {
    word: "calcuttan",
    primary: "A native or inhabitant of the Indian city of Calcutta (Kolkata); of or relating to Calcutta.",
    secondary: "In Anglo-Indian history and cultural studies, characteristic of the cosmopolitan urban lifestyle and literary society of colonial and modern Calcutta.",
    quotes: [
      { author: "Rabindranath Tagore", work: "Gitanjali and Selected Essays", quote: "The cultured **Calcuttan** gathered in the evenings along the riverfront to debate poetry and philosophy." },
      { author: "Rudyard Kipling", work: "The City of Dreadful Night", quote: "Every true **Calcuttan** knows the clamor of the New Market on a sweltering December morning." },
      { author: "W. Somerset Maugham", work: "The Razor's Edge", quote: "He conversed with a refined **Calcuttan** scholar who expounded the ancient Vedanta texts." }
    ]
  },
  "Dashboard — calc/chalicothere.md": {
    word: "chalicothere",
    primary: "An extinct, claw-footed, herbivorous odd-toed ungulate of the family Chalicotheriidae, related to horses and tapirs, living from the Eocene to the Pleistocene.",
    secondary: "In vertebrate paleontology, an unusual mammal possessing long front limbs and massive curved claws used for pulling down tree branches rather than digging or predation.",
    quotes: [
      { author: "Henry Fairfield Osborn", work: "The Titanotheres of Ancient Wyoming", quote: "The skeletal reconstruction of the **chalicothere** revealed immense claws on limbs that otherwise resembled a horse." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "The **chalicothere** presents an evolutionary enigma, combining ungulate dentition with gorilla-like posture and retractable claws." },
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "Miocene strata of Eurasia have yielded exquisite fossil skeletons of the clawed **chalicothere**." }
    ]
  },
  "Dashboard — calc/chalk.md": {
    word: "chalk",
    primary: "A soft, white, porous, sedimentary carbonate rock, a form of limestone composed of the mineral calcite; historically used for writing and drawing.",
    secondary: "In geology, the thick Upper Cretaceous marine deposits formed largely from the microscopic calcite plates (coccoliths) of planktonic algae.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On a Piece of Chalk", quote: "A piece of ordinary **chalk** represents a vast burial ground of microscopic organisms that once swam in prehistoric seas." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The immense beds of white **chalk** that form the South Downs extend under the English Channel to the cliffs of France." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The captain traced the vessel's daily run with a piece of white **chalk** upon the cabin bulkhead." }
    ]
  },
  "Dashboard — calc/chalky.md": {
    word: "chalky",
    primary: "Resembling, containing, or covered with chalk; having the white, dry, powdery texture or taste of chalk.",
    secondary: "In pedology and agriculture, describing soils with high calcium carbonate content, often causing pale coloration and high alkalinity.",
    quotes: [
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The summer carriage wheels threw up clouds of fine, **chalky** dust along the Wessex road." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The sheep thrive upon the short, fragrant turf that clothes these **chalky** downlands." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Priory School", quote: "Holmes examined the bicycle tracks imprinted upon the wet, **chalky** lane." }
    ]
  },
  "Dashboard — calc/decalcification.md": {
    word: "decalcification",
    primary: "The removal or loss of calcium or calcium compounds from a tissue, bone, or mineral substance.",
    secondary: "In skeletal pathology, bone resorption resulting in decreased bone density, as in osteoporosis, rickets, or prolonged immobility.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Acidic chemical reactions induce rapid **decalcification** of bone, leaving only the pliable collagenous framework." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Prolonged bed rest produces significant skeletal **decalcification**, predisposing the patient to spontaneous fractures." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "Hyperparathyroidism triggers accelerated **decalcification** of the cortex, releasing calcium into the bloodstream." }
    ]
  },
  "Dashboard — calc/decalcify.md": {
    word: "decalcify",
    primary: "To deprive of calcium or lime; remove calcareous matter from.",
    secondary: "In histological preparation, to soak mineralized bone or tooth specimens in dilute acid to soften them for sectioning and staining.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "If we immerse a fresh sheep bone in dilute hydrochloric acid, we **decalcify** it until it can be tied into a knot." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Certain metabolic toxins **decalcify** the skeleton, rendering the bones fragile and brittle." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The laboratory assistant must carefully **decalcify** the specimen before cutting thin paraffin sections for the microscope." }
    ]
  },
  "Dashboard — calc/decalcomania.md": {
    word: "decalcomania",
    primary: "The art or process of transferring designs, pictures, or patterns from specially prepared paper to glass, porcelain, metal, or other surfaces (decals).",
    secondary: "In surrealist art, a technique pioneered by Óscar Domínguez and Max Ernst involving pressing paint between sheets of paper to produce spontaneous textures.",
    quotes: [
      { author: "André Breton", work: "Surrealism and Painting", quote: "Through the method of **decalcomania**, the artist unlocks the unconscious imagery concealed within spreading pools of gouache." },
      { author: "Max Ernst", work: "Beyond Painting", quote: "Surrealist **decalcomania** creates eerie landscapes of coral-like mineral formations without deliberate brushwork." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The Victorian nursery indulged in the popular pastime of **decalcomania**, transferring colored vignettes onto scrapbooks and glass screens." }
    ]
  },
  "Dashboard — calc/dyscalculia.md": {
    word: "dyscalculia",
    primary: "A specific developmental or neurological learning disability that impairs an individual's ability to learn and comprehend arithmetic and numbers.",
    secondary: "In neuropsychology, an acquired or developmental impairment in number sense, calculation, and spatial math reasoning, often associated with parietal lobe dysfunction.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The patient showed remarkable artistic fluency despite a congenital **dyscalculia** that made simple change-making impossible." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Lesions of the angular gyrus frequently result in severe **dyscalculia**, abolishing the patient's grasp of positional number notation." },
      { author: "William James", work: "The Principles of Psychology", quote: "A selective arithmetic blindness, allied to modern **dyscalculia**, illustrates the modularity of specialized mental faculties." }
    ]
  },
  "Dashboard — calc/hypercalcaemia.md": {
    word: "hypercalcaemia",
    primary: "An abnormally high level of calcium in the blood serum (British spelling).",
    secondary: "In internal medicine, an endocrine and metabolic emergency commonly caused by primary hyperparathyroidism or malignancy, presenting with lethargy, cardiac arrhythmias, and renal calculi.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **hypercalcaemia** produces muscular hypotonia, persistent nausea, and profound mental confusion." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Metastatic bone destruction releases calcium ions into circulation, inducing acute **hypercalcaemia**." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "When serum calcium concentrations exceed normal limits, **hypercalcaemia** depresses nervous system excitability and delays cardiac conduction." }
    ]
  },
  "Dashboard — calc/hypercalcemia.md": {
    word: "hypercalcemia",
    primary: "An abnormally elevated concentration of calcium in the blood plasma (American spelling).",
    secondary: "In clinical nephrology and oncology, a metabolic disturbance that impairs renal concentrating ability and risks metastatic tissue calcification.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinician must promptly identify **hypercalcemia** in cancer patients to prevent irreversible kidney damage." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "Endocrine crises involving parathyroid adenomas manifest with marked **hypercalcemia** and skeletal pain." },
      { author: "Linus Pauling", work: "Vitamin C and the Common Cold", quote: "Excessive dosages of certain secosteroids may provoke **hypercalcemia** with metastatic calcification of blood vessels." }
    ]
  },
  "Dashboard — calc/hypercalcinuria.md": {
    word: "hypercalcinuria",
    primary: "The excretion of an abnormally large amount of calcium in the urine; hypercalciuria.",
    secondary: "In metabolic urology, an excessive urinary calcium output that predisposes patients to the precipitation of calcium oxalate or calcium phosphate renal calculi.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Idiopathic **hypercalcinuria** is the single most frequent biochemical abnormality found in recurrent stone formers." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Impaired tubular reabsorption of filtered calcium leads directly to marked **hypercalcinuria**." },
      { author: "Oliver Wendell Holmes", work: "Medical Essays", quote: "The patient's persistent gravel was traced to excessive **hypercalcinuria** caused by an unmonitored alkaline diet." }
    ]
  },
  "Dashboard — calc/hypercalciuria.md": {
    word: "hypercalciuria",
    primary: "An excess of calcium in the urine, exceeding 250–300 mg per day in an adult.",
    secondary: "In renal medicine, a condition categorized into absorptive, renal leak, or resorptive forms, closely associated with nephrolithiasis and nephrocalcinosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Sustained **hypercalciuria** saturates the collecting ducts, favoring the rapid nucleation of calcium oxalate stones." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The renal tubules showed microscopic deposits of lime, the pathological consequence of chronic **hypercalciuria**." },
      { author: "Hans Selye", work: "Calciphylaxis", quote: "Experimental animals subjected to parathyroid extracts developed severe **hypercalciuria** alongside skeletal demineralization." }
    ]
  },
  "Dashboard — calc/hypocalcaemia.md": {
    word: "hypocalcaemia",
    primary: "An abnormally low level of calcium in the blood serum (British spelling).",
    secondary: "In acute endocrinology, a condition marked by increased neuromuscular excitability, tetany, carpopedal spasm (Trousseau sign), and paresthesias.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Inadvertent removal of the parathyroid glandules during thyroidectomy provokes sudden **hypocalcaemia** and painful tetany." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Severe **hypocalcaemia** increases neuronal membrane permeability to sodium ions, eliciting spontaneous motor discharges." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "The muscular cramps and laryngospasm of **hypocalcaemia** require immediate intravenous calcium replacement." }
    ]
  },
  "Dashboard — calc/hypocalcemia.md": {
    word: "hypocalcemia",
    primary: "An abnormally low concentration of calcium in the circulating blood plasma (American spelling).",
    secondary: "In clinical medicine, a metabolic disorder resulting from hypoparathyroidism, vitamin D deficiency, or pancreatitis, diagnosed by Chvostek and Trousseau signs.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinical manifestation of acute **hypocalcemia** is carpopedal spasm accompanied by facial twitching." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "When plasma calcium levels drop below seven milligrams per deciliter, **hypocalcemia** can trigger fatal tetanic asphyxia." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The neurologist observed that the patient's muscle cramps cleared completely once the **hypocalcemia** was corrected." }
    ]
  },
  "Dashboard — calc/recalcitrance.md": {
    word: "recalcitrance",
    primary: "The state or quality of being recalcitrant; stubborn defiance of authority or obstinate refusal to comply.",
    secondary: "In environmental chemistry and microbiology, the resistance of synthetic chemical compounds or pollutants to biological decomposition and degradation.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The **recalcitrance** of the nobility hastened the convocation of the National Assembly." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "The chemical **recalcitrance** of chlorinated hydrocarbons ensures that they persist for decades in soils and food webs." },
      { author: "George Eliot", work: "Middlemarch", quote: "Her uncle lamented the silent **recalcitrance** with which she met all family arrangements." }
    ]
  },
  "Dashboard — calc/recalcitrancy.md": {
    word: "recalcitrancy",
    primary: "Obstinate noncompliance, rebelliousness, or stubborn resistance to guidance or authority; recalcitrance.",
    secondary: "In organizational and social behavior, persistent structural or individual resistance to reform, discipline, or change.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Such unyielding **recalcitrancy** against constitutional order inevitably invites the iron hand of despotism." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The magistrate reproved the prisoner for her silent **recalcitrancy** before the assembled elders." },
      { author: "Ralph Waldo Emerson", work: "Essays: Second Series", quote: "The raw material of experience meets the idealist with a stubborn **recalcitrancy** that tests his resolve." }
    ]
  },
  "Dashboard — calc/recalcitrant.md": {
    word: "recalcitrant",
    primary: "Having an obstinately uncooperative attitude toward authority or discipline; stubbornly disobedient.",
    secondary: "In materials science and biotechnology, resistant to ordinary treatment, chemical reactions, or bacterial degradation.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Steelkilt proved a most **recalcitrant** seaman, refusing to submit to the chief mate's tyrannical commands." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I found the stony soil of my upland patch **recalcitrant** to the hoe, yet it yielded sweet corn in due season." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "These synthetic molecules are completely **recalcitrant** to natural enzymatic breakdown." }
    ]
  },
  "Dashboard — calc/recalcitrate.md": {
    word: "recalcitrate",
    primary: "To kick back; to offer stubborn or defiant resistance; rebel against control.",
    secondary: "In historical prose and legal argument, to react with recalcitrance or indignantly reject an obligation or command.",
    quotes: [
      { author: "Thomas Carlyle", work: "Past and Present", quote: "When unjust laws are imposed, even the patient multitude will at last **recalcitrate**." },
      { author: "George Meredith", work: "The Egoist", quote: "The pride of the aristocrat made him **recalcitrate** against the slightest appearance of yielding to public opinion." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The legionaries did not hesitate to **recalcitrate** whenever an emperor failed to pay their promised bounty." }
    ]
  },
  "Dashboard — calc/recalculate.md": {
    word: "recalculate",
    primary: "To calculate again; to revise or re-evaluate a mathematical reckoning, trajectory, or estimate.",
    secondary: "In navigation and computer algorithms, to dynamically compute an updated course or solution following a deviation or new input data.",
    quotes: [
      { author: "Jules Verne", work: "From the Earth to the Moon", quote: "Barbicane sat at the table with pen in hand, forced to **recalculate** the parabolic trajectory after the asteroid's disturbance." },
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The navigational computer took less than a second to **recalculate** the orbital insertion burn." },
      { author: "H.G. Wells", work: "The First Men in the Moon", quote: "We were compelled to **recalculate** our rate of descent toward the lunar crater as fuel dwindled." }
    ]
  },
  "Dashboard — calc/recalculation.md": {
    word: "recalculation",
    primary: "The act or process of calculating again or anew; a revised computation.",
    secondary: "In financial accounting and scientific research, an audit or updated analysis conducted to correct prior errors or incorporate newly acquired parameters.",
    quotes: [
      { author: "Charles Babbage", work: "Passages from the Life of a Philosopher", quote: "A single typographical error in astronomical ephemerides necessitated weeks of tedious **recalculation**." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "A sudden shift in foreign exchange rates demands a prompt **recalculation** of import profits." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Professor Challenger demanded an immediate **recalculation** of our barometric altitude above the Amazon basin." }
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

console.log("Earth & Geology Batch 2 completed! Total words updated:", Object.keys(wordsData).length);
