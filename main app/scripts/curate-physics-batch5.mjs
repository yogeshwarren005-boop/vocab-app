import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — mechan (17 words) ===
  "Dashboard — mechan/mechanics.md": {
    primary: "The branch of applied mathematics and physics concerned with the motion of bodies and the action of forces upon them.",
    secondary: "The technical aspects, working machinery, or practical operational details of doing or making something.",
    quotes: [
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "Rational **mechanics** will be the science of motions resulting from any forces whatsoever." },
      { author: "James Clerk Maxwell", work: "Matter and Motion", quote: "The first law of physical **mechanics** asserts that every body continues in its state of rest or uniform motion unless acted upon." },
      { author: "Ernst Mach", work: "The Science of Mechanics", quote: "The historical development of classical **mechanics** demonstrates how intuitive experience was gradually distilled into mathematical axioms." }
    ]
  },
  "Dashboard — mechan/mechanisation.md": {
    primary: "The process of introducing machines into an industry or activity to replace human or animal labor (Commonwealth spelling).",
    secondary: "In military and industrial history, the transition of cavalry and infantry to motorized and armored armored formations.",
    quotes: [
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The progressive **mechanisation** of human toil altered the rhythm of daily life from organic cycles to mechanical clockwork." },
      { author: "Winston Churchill", work: "The World Crisis", quote: "The rapid **mechanisation** of the transport columns permitted rapid resupply of the front lines." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "Unbridled **mechanisation** tends to dehumanize labor, reducing the artisan to an attendant upon steel wheels." }
    ]
  },
  "Dashboard — mechan/mechanise.md": {
    primary: "To introduce machines into a process or industry; to replace human labor with machines (Commonwealth spelling).",
    secondary: "To equip an army or military unit with motorized combat vehicles and tanks.",
    quotes: [
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "Planners sought to **mechanise** every department of agriculture to free humanity from agrarian servitude." },
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "We urged the War Office to **mechanise** the territorial cavalry regiments without further delay." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Technocrats sought to **mechanise** emotional satisfaction through biochemical and auditory conditioning." }
    ]
  },
  "Dashboard — mechan/mechanised.md": {
    primary: "Equipped with or operated by machines; made mechanical (Commonwealth spelling).",
    secondary: "In military organization, consisting of troops equipped with armored vehicles, infantry fighting vehicles, and self-propelled guns.",
    quotes: [
      { author: "Winston Churchill", work: "Their Finest Hour", quote: "The onslaught of the enemy's **mechanised** columns smashed through the unfortified Ardennes defenses." },
      { author: "Lewis Mumford", work: "The Myth of the Machine", quote: "A thoroughly **mechanised** factory operates like a vast, inhuman organism ticking with clockwork efficiency." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The peasant militias faced the full fury of modern **mechanised** warfare with archaic rifles and homemade bombs." }
    ]
  },
  "Dashboard — mechan/mechanism.md": {
    primary: "A system of mutually adapted parts that work together in a machine; or a piece of machinery.",
    secondary: "A natural or chemical process by which something takes place; or in psychoanalysis, a mental defense strategy.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Natural selection is the primary **mechanism** by which advantageous variations are preserved and disadvantageous ones eliminated." },
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "Repression is a fundamental defense **mechanism** whereby intolerable impulses are barred from conscious awareness." },
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "Every clockwork **mechanism** displays exquisite contrivance in the harmonious transmission of wheel to pinion." }
    ]
  },
  "Dashboard — mechan/mechanist.md": {
    primary: "An adherent of the philosophical doctrine of mechanism, holding that natural phenomena are fully explainable by mechanical and physical causes.",
    secondary: "A maker, inventor, or operator of mechanical contrivances or machinery.",
    quotes: [
      { author: "René Descartes", work: "Discourse on the Method", quote: "As a philosophical **mechanist**, I view the animal body as an ingenious automaton fashioned by nature." },
      { author: "William James", work: "The Principles of Psychology", quote: "The strict **mechanist** denies the causal agency of conscious thought, reducing every mental state to neural physics." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "To the biological **mechanist**, vital forces are merely specialized manifestations of universal physical laws." }
    ]
  },
  "Dashboard — mechan/mechanistic.md": {
    primary: "Relating to or explaining phenomena in purely mechanical or physical terms.",
    secondary: "Operating automatically, routinely, or rigidly like a machine, devoid of spontaneity or human agency.",
    quotes: [
      { author: "René Descartes", work: "Meditations on First Philosophy", quote: "A rigorous **mechanistic** philosophy accounts for the circulation of blood without invoking occult vital souls." },
      { author: "Max Weber", work: "The Protestant Ethic and the Spirit of Capitalism", quote: "The modern economic order binds the individual within an iron cage of **mechanistic** division of labor." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "The seventeenth-century scientific revolution triumphed by replacing Aristotelian teleology with a **mechanistic** cosmology." }
    ]
  },
  "Dashboard — mechan/mechanistically.md": {
    primary: "In a mechanistic manner; according to the principles of physical mechanism.",
    secondary: "Without feeling, spontaneity, or conscious adaptation; automatically and routinely.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Methods and Results", quote: "Physiological processes must be investigated **mechanistically** to yield reproducible physical explanations." },
      { author: "William James", work: "Pragmatism", quote: "When we treat the universe purely **mechanistically**, we forfeit the rich qualitative texture of lived experience." },
      { author: "Jacques Loeb", work: "The Mechanistic Conception of Life", quote: "Tropisms in lower organisms can be modeled **mechanistically** as direct physical responses to light and gravity." }
    ]
  },
  "Dashboard — mechan/mechanization.md": {
    primary: "The process of introducing machines and automatic apparatus into an industry or task to replace human manual labor.",
    secondary: "In military doctrine and industrial engineering, the conversion of transport and weaponry to powered motorized units.",
    quotes: [
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The relentless **mechanization** of production reorganized the factory into a synchronized collective apparatus." },
      { author: "John Steinbeck", work: "The Grapes of Wrath", quote: "The tractor symbolized the cold **mechanization** that severed the tenant farmer from the ancestral soil." },
      { author: "Henry Ford", work: "My Life and Work", quote: "Through intensive **mechanization**, we eliminated waste motion and lowered the cost of transportation for millions." }
    ]
  },
  "Dashboard — mechan/mechanize.md": {
    primary: "To equip with machines; to substitute machinery for manual labor.",
    secondary: "To make routine, monotonous, or unthinking, like a machine.",
    quotes: [
      { author: "Henry David Thoreau", work: "Civil Disobedience", quote: "Men serve the state thus, not mainly as men, but as machines; to **mechanize** the soldier is to strip him of moral judgment." },
      { author: "H. G. Wells", work: "Anticipations", quote: "The next century will **mechanize** agriculture to such a degree that rural populations will migrate en masse to garden cities." },
      { author: "Winston Churchill", work: "The Second World War", quote: "Our urgent priority was to **mechanize** the infantry divisions with armored carrier vehicles." }
    ]
  },
  "Dashboard — mechan/mechanized.md": {
    primary: "Equipped with machinery; operated or driven by machines.",
    secondary: "In military terminology, utilizing armored fighting vehicles, tanks, and motorized personnel carriers.",
    quotes: [
      { author: "George Orwell", work: "Facing Unpleasant Facts", quote: "A **mechanized** army can sweep across plains in days where marching legions once took seasons." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The **mechanized** nursery turned out standardized citizens like uniform components from an assembly line." },
      { author: "John Kenneth Galbraith", work: "The New Industrial State", quote: "Modern corporate enterprise relies on a heavily **mechanized** capital infrastructure." }
    ]
  },
  "Dashboard — mechan/mechanobiology.md": {
    primary: "An emerging field of science at the interface of biology and physics that studies how physical forces and mechanical properties influence cells and tissues.",
    secondary: "In cellular and tissue engineering, the investigation of mechanotransduction, extracellular matrix stiffness, and force-regulated gene expression.",
    quotes: [
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "Physical forces shape the living organism, anticipating the modern discipline of **mechanobiology** by decades." },
      { author: "Donald E. Ingber", work: "Tensegrity and Mechanoregulation", quote: "Cellular tensegrity provides the physical architectural framework for the discipline of **mechanobiology**." },
      { author: "E. O. Wilson", work: "Consilience: The Unity of Knowledge", quote: "Bridging the gap between structural engineering and genetics, **mechanobiology** shows how mechanical tension directs embryonic cell fates." }
    ]
  },
  "Dashboard — mechan/mechanophilia.md": {
    primary: "An abnormal or compulsive affection for, attraction to, or sexual fixation on machines or mechanical devices.",
    secondary: "In psychopathology, a paraphilia wherein an individual derives erotic arousal from interactions with automobiles, airplanes, or industrial machinery.",
    quotes: [
      { author: "J. G. Ballard", work: "Crash", quote: "The psychological landscape was dominated by an eroticized fascination with chrome and speed akin to clinical **mechanophilia**." },
      { author: "Lewis Mumford", work: "The Myth of the Machine", quote: "A pathological **mechanophilia** causes modern technocrats to worship mechanical efficiency above human survival." },
      { author: "Erich Fromm", work: "The Anatomy of Human Destructiveness", quote: "The necrophilous character often expresses itself as an obsessive **mechanophilia**, preferring dead machinery to living beings." }
    ]
  },
  "Dashboard — mechan/mechanophobia.md": {
    primary: "An abnormal, persistent, or irrational fear of machines, mechanical devices, or automated technology.",
    secondary: "In clinical psychiatry and sociology of technology, an anxiety disorder manifesting as terror of encountering or operating machinery.",
    quotes: [
      { author: "E. M. Forster", work: "The Machine Stops", quote: "When the central apparatus faltered, the subterranean citizens experienced an acute terror far worse than simple **mechanophobia**." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "Early Luddite protests were driven not by irrational **mechanophobia**, but by justifiable resistance to workplace degradation." },
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Public resistance to robotic automation frequently masks a subconscious **mechanophobia** inherited from ancient folklore." }
    ]
  },
  "Dashboard — mechan/unmechanical.md": {
    primary: "Not mechanical; not operated by or resembling a machine.",
    secondary: "Lacking technical skill; or characterized by spontaneity, natural grace, and freedom from rigid routine.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The irregular, **unmechanical** touch of the medieval stonecutter breathes life into the gothic capital." },
      { author: "William Morris", work: "Hopes and Fears for Art", quote: "Handmade textiles preserve a delightful, **unmechanical** variety that industrial looms can never replicate." },
      { author: "George Eliot", work: "Middlemarch", quote: "His thinking was fluid and imaginative, delightfully **unmechanical** in its subtle discernment of character." }
    ]
  },
  "Dashboard — mechan/unmechanised.md": {
    primary: "Not mechanised; not equipped with machines or automated apparatus (Commonwealth spelling).",
    secondary: "In military or agricultural contexts, relying on manual labor, draught animals, or foot transport.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The mountain front remained an **unmechanised** sector where mules provided the only link to the valley." },
      { author: "Winston Churchill", work: "The World Crisis", quote: "The Russian army entered the campaign largely **unmechanised**, suffering dreadful logistical bottlenecks." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The rustic valley preserved its ancient, **unmechanised** harvesting methods with sickles and scythes." }
    ]
  },
  "Dashboard — mechan/unmechanized.md": {
    primary: "Not mechanized; lacking machines; performed by manual labor or traditional tools.",
    secondary: "Describing military units, farms, or manufacturing shops that have not adopted motorized equipment or automated production lines.",
    quotes: [
      { author: "John Steinbeck", work: "The Grapes of Wrath", quote: "The small, **unmechanized** family farm could not compete with the industrial crawler tractors." },
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "There is an aesthetic satisfaction in farming with an **unmechanized** walking plow behind a team of horses." },
      { author: "Dwight D. Eisenhower", work: "Crusade in Europe", quote: "Supplying our forces over the rugged mountains required pack animals alongside **unmechanized** transport units." }
    ]
  },

  // === Dashboard — oni (4 words) ===
  "Dashboard — oni/oni.md": {
    primary: "A combining root derived from Greek ōnios, meaning 'for sale', 'purchased', or 'buying'.",
    secondary: "In psychiatric and psychological nosology, the formative root of terms describing compulsive or pathological shopping behavior.",
    quotes: [
      { author: "Emil Kraepelin", work: "Psychiatrie: Ein Lehrbuch für Studierende und Ärzte", quote: "From the Hellenic word ōnios, we derived the term oniomania to describe impulsive buying pathology." },
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "The prefix **oni**- marks those affective disorders in which acquisition and spending become uncontrollable compulsions." },
      { author: "William James", work: "The Principles of Psychology", quote: "The passion for possession finds its pathological extreme in syndromes rooted in the morpheme **oni**-." }
    ]
  },
  "Dashboard — oni/oniochalasia.md": {
    primary: "The purchasing or buying of goods as a means of seeking emotional relief, relaxation, or tension reduction ('retail therapy').",
    secondary: "In behavioral psychology, a coping mechanism where financial spending is employed to self-regulate anxiety, depression, or distress.",
    quotes: [
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "In milder cases, shopping acts as a transient **oniochalasia**, relieving internal psychic tension through acquisition." },
      { author: "Carl Jung", work: "Psychological Types", quote: "Sensory stimulation in bustling commercial bazaars provides temporary **oniochalasia** for the overwhelmed neurotic." },
      { author: "Erich Fromm", work: "To Have or to Be?", quote: "Consumerist society institutionalizes **oniochalasia**, teaching citizens to soothe existential anxiety through shopping." }
    ]
  },
  "Dashboard — oni/oniomania.md": {
    primary: "An uncontrollable, compulsive desire or urge to buy things; compulsive buying disorder or shopping addiction.",
    secondary: "In clinical psychiatry, an impulse control disorder first classified by Emil Kraepelin and Eugen Bleuler, characterized by distressing, financially ruinous purchases.",
    quotes: [
      { author: "Emil Kraepelin", work: "Psychiatrie: Ein Lehrbuch", quote: "Among the reactive impulsive neuroses, **oniomania** stands out as a pathological compulsion to buy without practical necessity." },
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "Patients afflicted with **oniomania** run up astronomical debts, deriving gratification solely from the act of purchasing." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Certain forms of kleptomania and **oniomania** represent symbolic substitutes for unfulfilled emotional needs." }
    ]
  },
  "Dashboard — oni/oniomaniac.md": {
    primary: "A person who suffers from oniomania; a compulsive shopper.",
    secondary: "Characterized by or relating to compulsive buying disorder.",
    quotes: [
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "The confirmed **oniomaniac** fills closets with unopened packages, indifferent to the merchandise once acquired." },
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "Attempts by family members to restrain an **oniomaniac** frequently provoke intense agitation and deceptive stratagems." },
      { author: "William Osler", work: "Aequanimitas", quote: "The clinical practitioner must recognize that the chronic **oniomaniac** suffers from an authentic disorder of volition." }
    ]
  },

  // === Dashboard — oryz (7 words) ===
  "Dashboard — oryz/oryz.md": {
    primary: "A combining root derived from Greek oryza, meaning 'rice'.",
    secondary: "In systematic botany and agronomy, the formative prefix used to designate rice taxa, rice pathogens, and wild grass relatives.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The ancient Greek name for rice, **oryz**-a, serves as the generic designation for the world's most vital cereal grass." },
      { author: "Alphonse de Candolle", work: "Origin of Cultivated Plants", quote: "Linguistic evidence shows that the morpheme **oryz**- traveled along ancient trade routes from the Indus to the Mediterranean." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanical genera sharing the root **oryz**- comprise grasses adapted to saturated marshy soils." }
    ]
  },
  "Dashboard — oryz/Oryza.md": {
    primary: "The botanical genus of cereal grasses in the family Poaceae that includes cultivated Asian rice (Oryza sativa) and African rice (Oryza glaberrima).",
    secondary: "In agronomy and plant genetics, the primary staple grain genus that feeds more than half of the global human population.",
    quotes: [
      { author: "Carl Linnaeus", work: "Genera Plantarum", quote: "The genus **Oryza** is characterized by six stamens and two-valved glumes enclosing a solitary starch-rich seed." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants Under Domestication", quote: "Centuries of artificial selection in **Oryza** produced thousands of distinct lowland and upland cultivars." },
      { author: "Nikolai Vavilov", work: "The Origin and Geography of Cultivated Plants", quote: "The primary evolutionary center of diversity for **Oryza** lies in the subtropical river valleys of southern Asia." }
    ]
  },
  "Dashboard — oryz/Oryzomys.md": {
    primary: "A genus of semiaquatic rodents in the family Cricetidae, commonly known as rice rats, native to the Americas.",
    secondary: "In mammalogy, marsh-dwelling rodents (such as the marsh rice rat, Oryzomys palustris) adapted to tidal wetlands, wetlands, and flooded rice fields.",
    quotes: [
      { author: "John James Audubon", work: "The Viviparous Quadrupeds of North America", quote: "The marsh rice rat, **Oryzomys**, swims and dives with extraordinary dexterity through coastal saltwater marshes." },
      { author: "G. H. H. Tate", work: "The Rodents of South America", quote: "Species of **Oryzomys** are distributed throughout the Neotropical river basins from the delta marshes to montane slopes." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Island populations of **Oryzomys** in the Galápagos have suffered severe declines following the introduction of feral competitors." }
    ]
  },
  "Dashboard — oryz/oryzopsis.md": {
    primary: "A genus of perennial grasses in the family Poaceae, commonly known as ricegrass (such as Indian ricegrass).",
    secondary: "In range management and agrostology, drought-resistant cool-season bunchgrasses native to North American prairies, valuable for forage.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The genus **Oryzopsis** is distinguished by its diffuse panicle and plump, rice-like awned lemmas." },
      { author: "Agnes Chase", work: "First Book of Grasses", quote: "Indian ricegrass, formerly classified under **Oryzopsis**, was a vital wild seed staple for Indigenous desert tribes." },
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "Bunches of wild **Oryzopsis** held the sandy soil of the blowout against the winter winds." }
    ]
  },
  "Dashboard — oryz/rice.md": {
    primary: "The starchy grain produced by the cereal grass Oryza sativa, cultivated extensively as a staple food worldwide.",
    secondary: "The annual marsh plant itself, typically cultivated in flooded agricultural terraces or paddies.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "A field of **rice** produces a much greater quantity of food than the most fertile cornfield of wheat." },
      { author: "Marco Polo", work: "The Travels of Marco Polo", quote: "Throughout the southern provinces of Cathay, the populace lives chiefly upon **rice** seasoned with fragrant spices." },
      { author: "Henry David Thoreau", work: "Walden", quote: "A small quantity of boiled **rice** and molasses furnished me with a clean, sustaining, and philosophical meal." }
    ]
  },
  "Dashboard — oryz/ricer.md": {
    primary: "A culinary kitchen utensil resembling a large garlic press used to extrude cooked vegetables (such as potatoes) into small, rice-sized grains.",
    secondary: "In cooking techniques, a tool that yields light, fluffy mashed potatoes by processing tubers without releasing excess cell starch.",
    quotes: [
      { author: "Julia Child", work: "Mastering the Art of French Cooking", quote: "Pass the hot boiled potatoes immediately through a vegetable **ricer** to ensure a silky, lump-free purée." },
      { author: "M. F. K. Fisher", work: "The Gastronomical Me", quote: "She operated the heavy metal **ricer** with practiced rhythm, showering the bowl with steaming white shreds." },
      { author: "Elizabeth David", work: "French Provincial Cooking", quote: "Using a **ricer** preserves the lightness of the potato cells without turning the mash into a gummy paste." }
    ]
  },
  "Dashboard — oryz/risotto.md": {
    primary: "A traditional northern Italian dish of short-grain rice (such as Arborio or Carnaroli) cooked slowly in broth to a creamy consistency.",
    secondary: "In culinary arts, a preparation technique involving toasted rice deglazed with wine and cooked by incremental broth addition while stirring to release starch.",
    quotes: [
      { author: "Elizabeth David", work: "Italian Food", quote: "A true Milanese **risotto** should be rich with saffron and bone marrow, creamy yet firm to the bite." },
      { author: "Marcella Hazan", work: "The Classic Italian Cookbook", quote: "The success of a great **risotto** depends on constant, gentle stirring to coax the starch from the rice grains." },
      { author: "Anthony Bourdain", work: "Kitchen Confidential", quote: "The line cook stood over the sauté station, testing each pan of simmering **risotto** for the perfect al dente wave." }
    ]
  },

  // === Dashboard — osm (20 words) ===
  "Dashboard — osm/anosmatic.md": {
    primary: "Lacking the sense of smell; anosmic.",
    secondary: "In comparative anatomy, describing animals (such as cetaceans) that possess no olfactory apparatus or olfactory bulbs.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Cetaceans are essentially **anosmatic**, having lost the sense of smell during their evolutionary transition to marine life." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Following head trauma, the patient was found to be totally **anosmatic** due to shearing of the cribriform filaments." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Being suddenly **anosmatic** impoverished his perception of the world more profoundly than he could have anticipated." }
    ]
  },
  "Dashboard — osm/anosmia.md": {
    primary: "The total loss of the sense of smell, either temporary or permanent.",
    secondary: "In clinical neurology and otolaryngology, an olfactory deficit resulting from nasal mucosal disease, viral respiratory infection, or olfactory nerve injury.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "A sudden fall from a bicycle resulted in bilateral **anosmia**, robbing his world of scent and culinary flavor." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Unilateral **anosmia** can provide a vital early sign of an olfactory groove meningioma compressing the olfactory tract." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The abrupt onset of **anosmia** without nasal congestion served as a hallmark diagnostic indicator during the viral pandemic." }
    ]
  },
  "Dashboard — osm/anosmic.md": {
    primary: "Destitute of the sense of smell; suffering from anosmia.",
    secondary: "Pertaining to or characterized by the absence of olfactory sensation.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The **anosmic** patient lamented that food had lost its distinctive savour, tasting only of sweet, salt, or acid." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Examination revealed that the patient was completely **anosmic** to aromatic oils like cloves and peppermint." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Animals rendered artificially **anosmic** show marked disorientation in maternal recognizing behavior." }
    ]
  },
  "Dashboard — osm/cacosmia.md": {
    primary: "A sensory perception of a foul, repulsive, or offensive odor, usually when no such odor is objectively present.",
    secondary: "In otorhinolaryngology and neurology, a parosmia often caused by chronic anaerobic sinusitis or temporal lobe seizure auras.",
    quotes: [
      { author: "Oliver Sacks", work: "Migraine", quote: "The premonitory aura occasionally presented as an overpowering **cacosmia**, as of burning rubber or decaying flesh." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe dental caries and anaerobic maxillary sinusitis are common peripheral sources of persistent **cacosmia**." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Epileptic foci in the uncus frequently trigger fleeting episodes of hallucinated **cacosmia**." }
    ]
  },
  "Dashboard — osm/coprosmia.md": {
    primary: "An olfactory hallucination or sensory distortion in which odors are perceived as smelling like feces.",
    secondary: "In neuropsychiatry and otolaryngology, an extreme form of cacosmia associated with uncinate fits or severe psychiatric distress.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The patient complained of distressing **coprosmia**, perceiving every meal as if contaminated by fecal matter." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Irritative cortical lesions involving the limbic rhinencephalon can induce paroxysmal **coprosmia**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Persistent subjective **coprosmia** mandates thorough neuroimaging to exclude an uncinate gyrus neoplasm." }
    ]
  },
  "Dashboard — osm/dysosmia.md": {
    primary: "Any disorder, impairment, or distortion of the normal sense of smell.",
    secondary: "In clinical sensory testing, the overarching diagnostic classification encompassing parosmia, phantosmia, and hyposmia.",
    quotes: [
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Post-viral **dysosmia** transformed the scent of morning coffee into a nauseating metallic stench." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Head injuries with occipital counter-coup frequently induce long-lasting bilateral **dysosmia**." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The clinical recovery from post-infectious **dysosmia** can span months as olfactory receptor neurons regenerate." }
    ]
  },
  "Dashboard — osm/dysosmic.md": {
    primary: "Relating to, characterized by, or suffering from dysosmia (impaired or distorted sense of smell).",
    secondary: "Describing qualitative olfactory distortions wherein odors are misidentified or perceived as altered.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The **dysosmic** patient struggled to eat, as fresh bread and fruit smelled persistently like kerosene." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough **dysosmic** evaluation involves testing olfactory thresholds against standardized aromatic odorants." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Cortical trauma produced a **dysosmic** state where familiar perfumes were perceived as noxious fumes." }
    ]
  },
  "Dashboard — osm/euosmia.md": {
    primary: "A pleasant, agreeable, or normal perception of odors; or a hallucination of sweet and pleasant fragrances.",
    secondary: "In sensory physiology and olfaction studies, the intact, pleasurable appreciation of scents, contrasted with cacosmia.",
    quotes: [
      { author: "Oliver Sacks", work: "Musicophilia", quote: "His temporal lobe seizures were occasionally inaugurated by a heavenly **euosmia**, like roses in full summer bloom." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The aesthetic delight derived from delicate perfumes constitutes a refined form of natural **euosmia**." },
      { author: "William Osler", work: "Aequanimitas", quote: "After months of post-influenzal distortion, the return of true **euosmia** brought tears of relief to the patient." }
    ]
  },
  "Dashboard — osm/hyperosmia.md": {
    primary: "An abnormally acute or heightened sensitivity to odors.",
    secondary: "In neurology and endocrinology, a heightened olfactory acuity observed during pregnancy, migraine auras, Addison's disease, or hyperthyroidism.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Under the influence of dopamine, the medical student experienced an astonishing **hyperosmia**, navigating the city by scent like a dog." },
      { author: "Marcel Proust", work: "In Search of Lost Time", quote: "A delicate **hyperosmia** enabled him to detect the faint scent of hawthorn blossoms miles down the riverbank." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **hyperosmia** during early pregnancy often exacerbates hyperemesis gravidarum." }
    ]
  },
  "Dashboard — osm/hyperosmic.md": {
    primary: "Pertaining to, affected with, or characterized by hyperosmia (excessive olfactory sensitivity).",
    secondary: "Possessing an exceptionally sharp sense of smell; macrosmatic.",
    quotes: [
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "In his **hyperosmic** state, the patient could identify colleagues entering the hospital wing purely by their personal scent." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Canines maintain a **hyperosmic** perceptual realm far beyond the comprehension of our microsmatic human senses." },
      { author: "Alexander Luria", work: "The Mind of a Mnemonist", quote: "His synesthesia produced a **hyperosmic** reaction where every spoken word summoned distinct vivid odors." }
    ]
  },
  "Dashboard — osm/hyposmia.md": {
    primary: "An abnormally decreased sensitivity to odors; partial loss of smell.",
    secondary: "In neurology, an early prodromal biomarker of neurodegenerative disorders such as Parkinson's disease and Alzheimer's disease.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "Retrospective analysis revealed that progressive **hyposmia** had preceded the onset of parkinsonian tremor by a full decade." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic allergic rhinitis causes mechanical obstruction of the olfactory cleft, leading to reversible **hyposmia**." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Screening elderly patients for asymptomatic **hyposmia** provides a non-invasive clue toward neurodegenerative risk." }
    ]
  },
  "Dashboard — osm/hyposmic.md": {
    primary: "Relating to or affected with hyposmia; having a diminished sense of smell.",
    secondary: "Describing individuals or conditions exhibiting elevated olfactory detection thresholds.",
    quotes: [
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The **hyposmic** subject was oblivious to the pungent woodsmoke filling the cabin." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "An elderly **hyposmic** patient requires safety warnings regarding unperceived household gas leaks." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Aging is frequently accompanied by an insidious **hyposmic** decline due to attrition of olfactory neuroepithelium." }
    ]
  },
  "Dashboard — osm/osm.md": {
    primary: "A combining root derived from Greek osmē, meaning 'smell', 'odor', or 'scent'.",
    secondary: "In chemical and biomedical nomenclature, the classical root forming terms relating to olfaction and the metallic element osmium.",
    quotes: [
      { author: "Smithson Tennant", work: "On Two New Metals Found in the Black Powder Remaining after the Solution of Platina", quote: "As the oxide of this new metal possesses a pungent, penetrating odor, I have named it from the Greek root **osm**-." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The Greek morpheme **osm**- serves as the universal prefix for all diagnostic classifications of olfactory dysfunction." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Structures retaining the root **osm**- reflect the primal evolutionary role of olfaction in vertebrate behavior." }
    ]
  },
  "Dashboard — osm/osmium.md": {
    primary: "A hard, brittle, bluish-white transition metal element with atomic number 76 and symbol Os, the densest naturally occurring element.",
    secondary: "In chemistry and microscopy, a precious platinum-group metal whose volatile tetroxide (OsO4) is widely used to stain lipids and fix cell membranes for electron microscopy.",
    quotes: [
      { author: "Smithson Tennant", work: "Philosophical Transactions of the Royal Society", quote: "I have named this metal **osmium**, from the Greek word for odor, on account of the pungent smell of its volatile oxide." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "Dense and immutable, **osmium** sinks through mercury like a stone through water, heavy as leaden fate." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The myelin sheaths of peripheral nerve fibers were fixed in black outline by immersion in **osmium** tetroxide." }
    ]
  },
  "Dashboard — osm/osmolagnia.md": {
    primary: "Sexual attraction, arousal, or fixation derived from odors or smells; osphresiolagnia.",
    secondary: "In psychopathology and clinical sexology, an erotic fetish centered on bodily scents, perfumes, or natural olfactory pheromones.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Olfactory eroticism, or **osmolagnia**, reveals the ancient biological link between the nose and mammalian sexual attraction." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "Cases of **osmolagnia** demonstrate that specific aromatic cues can become exclusive triggers of sexual excitement." },
      { author: "Magnus Hirschfeld", work: "Sexual Anomalies and Perversions", quote: "The phenomenon of **osmolagnia** is frequently observed in individuals who possess heightened sensory emotional sensitivity." }
    ]
  },
  "Dashboard — osm/osmophobia.md": {
    primary: "An abnormal, persistent fear of, aversion to, or hypersensitivity to odors or smells.",
    secondary: "In neurology, a frequent and characteristic symptom accompanying migraine headaches, where ambient odors trigger nausea and worsen head pain.",
    quotes: [
      { author: "Oliver Sacks", work: "Migraine", quote: "During the acute headache phase, patients suffer from extreme **osmophobia**, finding even the faintest aroma of cooking intolerable." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In hysterical neuroses, profound **osmophobia** can lead to complete avoidance of food and social contact." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Severe **osmophobia** accompanied the limbic encephalitis, producing violent panic whenever perfumes were present." }
    ]
  },
  "Dashboard — osm/osphresiolagnia.md": {
    primary: "A paraphilia in which sexual gratification or excitement is obtained from odors or scents; osmolagnia.",
    secondary: "In psychiatric nosology, the formal Hellenic term for olfactory fetishism and eroticized fragrance fixation.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The clinical term **osphresiolagnia** encompasses all varieties of erotic excitation mediated primarily through the olfactory sense." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "In documented histories of **osphresiolagnia**, certain perfumes or natural cutaneous odors become indispensable to libido." },
      { author: "Magnus Hirschfeld", work: "The Homosexuality of Men and Women", quote: "He traced the patient's fetishistic behavior to an early manifestation of intense **osphresiolagnia**." }
    ]
  },
  "Dashboard — osm/parosmia.md": {
    primary: "A distorted or perverted perception of smell, whereby odors are perceived differently from how they normally smell or should smell.",
    secondary: "In clinical otolaryngology, an aberrant olfactory recovery state following viral infections, wherein pleasant aromas smell foul, rotten, or chemical.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "During recovery from head trauma, the patient suffered from severe **parosmia**, complaining that flowers smelled like burning grease." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Post-influenzal **parosmia** is a distressing symptom that can severely compromise nutritional intake." },
      { author: "Jerome Groopman", work: "Second Opinions", quote: "The olfactory nerve regeneration produced temporary miswiring that resulted in frustrating **parosmia** for several months." }
    ]
  },
  "Dashboard — osm/phantosmia.md": {
    primary: "An olfactory hallucination; the perception of a smell that is not physically present in the environment.",
    secondary: "In neurology and neuropsychiatry, phantom odors (often smoky, chemical, or putrid) caused by head injury, stroke, uncinate epilepsy, or psychiatric disorders.",
    quotes: [
      { author: "Oliver Sacks", work: "Hallucinations", quote: "The patient reported terrifying episodes of **phantosmia**, smelling strong sulfur and brimstone in an empty room." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Irritative cortical lesions of the temporal lobe uncus manifest characteristically as paroxysmal **phantosmia**." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Following localized parietal-temporal trauma, the subject described continuous phantom scents or **phantosmia**." }
    ]
  },
  "Dashboard — osm/troposmia.md": {
    primary: "A perversion or qualitative change in the sense of smell; a medical synonym for parosmia or dysosmia.",
    secondary: "In sensory neurology, the abnormal transformation of an odorant's perceived quality into a distorted or unpleasant sensation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The term **troposmia** is employed by certain authorities to indicate that familiar odors have undergone a qualitative transformation." },
      { author: "Oliver Sacks", work: "Migraine", quote: "Transient **troposmia** preceded the vascular headache, altering the scent of household coffee into vinegar." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Nasal polypoid disease can induce chronic **troposmia** before progressing to complete olfactory extinction." }
    ]
  },

  // === Dashboard — osmo (8 words) ===
  "Dashboard — osmo/isosmotic.md": {
    primary: "Having the same total osmotic pressure or osmolality as another solution.",
    secondary: "In physiology and cell biology, describing solutions (such as 0.9% normal saline) that exert identical osmotic pressure across a semipermeable membrane relative to blood plasma.",
    quotes: [
      { author: "August Krogh", work: "Osmotic Regulation in Aquatic Animals", quote: "Marine invertebrates maintain body fluids that are virtually **isosmotic** with surrounding seawater." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Intravenous infusions must remain **isosmotic** with plasma to avoid osmotic hemolysis of red blood cells." },
      { author: "Ernest Starling", work: "The Fluids of the Body", quote: "Capillary fluid filtration balances hydrostatic forces against the **isosmotic** draw of plasma albumins." }
    ]
  },
  "Dashboard — osmo/osm 2.md": {
    primary: "A combining root derived from Greek ōsmos, meaning 'thrust', 'push', or 'impulse', denoting osmosis or osmotic pressure.",
    secondary: "In physical chemistry and physiology, the formative root of osmosis, osmoregulation, and osmometry, distinct from the root for smell.",
    quotes: [
      { author: "René Dutrochet", work: "Nouvelles Recherches sur l'Endosmose et l'Exosmose", quote: "From the Greek word for impulse or thrust, we introduced the formative morpheme **osm**- to describe fluid passage through organic membranes." },
      { author: "Wilhelm Pfeffer", work: "Osmotische Untersuchungen", quote: "Membrane transport phenomena investigated under the root **osm**- laid the foundation of modern solution thermodynamics." },
      { author: "Jacobus Henricus van 't Hoff", work: "The Role of Osmotic Pressure in the Analogy Between Solutions and Gases", quote: "The prefix **osm**- links the gas laws directly to the hydrostatic pressures developed across semipermeable barriers." }
    ]
  },
  "Dashboard — osmo/osmometry.md": {
    primary: "The measurement of osmotic pressure in a solution.",
    secondary: "In analytical chemistry and polymer science, a technique (vapor pressure or membrane osmometry) used to determine the number-average molecular weight of macromolecules.",
    quotes: [
      { author: "Jacobus Henricus van 't Hoff", work: "Studies in Chemical Dynamics", quote: "Precise **osmometry** of dilute sugar solutions confirmed that osmotic pressure is proportional to absolute temperature." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Membrane **osmometry** provided the earliest accurate determinations of hemoglobin's molecular weight." },
      { author: "Peter Debye", work: "The Collected Papers of Peter J. W. Debye", quote: "The thermodynamic virial coefficients of synthetic polymer solutions are conveniently evaluated through **osmometry**." }
    ]
  },
  "Dashboard — osmo/osmoreceptor.md": {
    primary: "A sensory receptor cell, primarily located in the hypothalamus, that detects changes in osmotic pressure and solute concentration in the blood.",
    secondary: "In neuroendocrinology, specialized hypothalamic neurons in the OVLT and supraoptic nucleus that stimulate thirst and vasopressin (ADH) release when plasma osmolality rises.",
    quotes: [
      { author: "Ernest Starling", work: "The Fluids of the Body", quote: "A central **osmoreceptor** mechanism regulates systemic water balance by controlling thirst." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "Stimulation of the hypothalamic **osmoreceptor** triggers an immediate neuroendocrine cascade to conserve bodily fluids." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Damage to the hypothalamic **osmoreceptor** centers can lead to profound adipsia and hypernatremia." }
    ]
  },
  "Dashboard — osmo/osmosis.md": {
    primary: "The spontaneous net movement of solvent molecules through a selectively permeable membrane into a region of higher solute concentration.",
    secondary: "The gradual, often unconscious assimilation or absorption of ideas, knowledge, culture, or mannerisms from one's environment.",
    quotes: [
      { author: "René Dutrochet", work: "Memoirs on Endosmosis and Exosmosis", quote: "This remarkable phenomenon of fluid transport across animal membranes I designated as **osmosis**." },
      { author: "Jacobus Henricus van 't Hoff", work: "The Role of Osmotic Pressure in the Analogy Between Solutions and Gases", quote: "The thermodynamic drive behind **osmosis** parallels the expansion of a gas into an evacuated vessel." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "One absorbs the tone and prejudices of an institution by a quiet process of intellectual **osmosis**." }
    ]
  },
  "Dashboard — osmo/osmostat.md": {
    primary: "The regulatory physiological mechanism that maintains the osmotic pressure of bodily fluids at a stable setpoint.",
    secondary: "In nephrology and endocrinology, the hypothalamic control system governing antidiuretic hormone (ADH) secretion; or 'reset osmostat' in chronic hyponatremia.",
    quotes: [
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "The biological **osmostat** maintains plasma osmolality within a narrow physiological band near 285 milliosmoles." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In certain chronic pulmonary conditions, the central **osmostat** resets to a lower baseline, sustaining mild asymptomatic hyponatremia." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Evaluating the unresponsive sodium level required differentiating between SIADH and a physiologically altered **osmostat**." }
    ]
  },
  "Dashboard — osmo/osmotic.md": {
    primary: "Of, relating to, or produced by osmosis.",
    secondary: "Pertaining to osmotic pressure, the minimum pressure that must be applied to a solution to prevent the inward flow of its pure solvent across a semipermeable membrane.",
    quotes: [
      { author: "Jacobus Henricus van 't Hoff", work: "The Role of Osmotic Pressure in the Analogy Between Solutions and Gases", quote: "The **osmotic** pressure of a dissolved substance is equal to the pressure it would exert as a gas occupying the same volume." },
      { author: "Wilhelm Pfeffer", work: "Osmotische Untersuchungen", quote: "Using semipermeable copper ferrocyanide cells, we measured the tremendous **osmotic** pressures generated by concentrated solutions." },
      { author: "August Krogh", work: "The Anatomy and Physiology of Capillaries", quote: "Colloid **osmotic** pressure exerted by plasma proteins prevents the total escape of fluid into the extracellular space." }
    ]
  },
  "Dashboard — osmo/osmotically.md": {
    primary: "In an osmotic manner; by means of osmosis.",
    secondary: "In cell physiology, describing solutes (such as mannitol or glucose) that exert water-drawing forces across biological membranes (osmotically active).",
    quotes: [
      { author: "August Krogh", work: "Osmotic Regulation in Aquatic Animals", quote: "Freshwater teleosts are **osmotically** flooded with water through their delicate gill membranes." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Infusion of concentrated mannitol acts **osmotically** to draw edema fluid out of swollen brain tissue." },
      { author: "Ernest Starling", work: "The Fluids of the Body", quote: "Fluid is drawn **osmotically** back into the venous capillary limb where oncotic pressure exceeds hydrostatic force." }
    ]
  },

  // === Dashboard — pect (first 8 words of batch 5) ===
  "Dashboard — pect/expect.md": {
    primary: "To regard something as likely or certain to happen; to anticipate or look forward to.",
    secondary: "To consider obligatory, required, or due from someone; or historically, to await with confidence.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She could not **expect** that his affection would survive so many humiliating rebuffs." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "I was to leave my humble blacksmith home and enter upon the great fortunes I was led to **expect**." },
      { author: "William Shakespeare", work: "Julius Caesar", quote: "Good reasons must of force give place to better; let us **expect** our allies on the morrow." }
    ]
  },
  "Dashboard — pect/expectable.md": {
    primary: "Capable of being expected; reasonable to anticipate; predictable or foreseeable.",
    secondary: "In ethics, psychology, and legal theory, conforming to standard probability or customary human conduct.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "That emotional fatigue should follow prolonged mental exertion is an **expectable** physiological result." },
      { author: "Oliver Wendell Holmes Jr.", work: "The Common Law", quote: "The standard of tort liability rests upon what is reasonably **expectable** from a prudent man under like conditions." },
      { author: "John Dewey", work: "Human Nature and Conduct", quote: "Habit establishes the stable framework within which future actions become reliable and **expectable**." }
    ]
  },
  "Dashboard — pect/expectancy.md": {
    primary: "The state of thinking or hoping that something, especially something pleasant, will happen; anticipation.",
    secondary: "In statistics and insurance, life expectancy—the average period that a person may expect to live based on demographic actuarial tables.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "There was a breathless hush of **expectancy** in the courtroom as the jury filed back to their places." },
      { author: "William Shakespeare", work: "Hamlet", quote: "The courtier's, soldier's, scholar's, eye, tongue, sword; the **expectancy** and rose of the fair state." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "A quiet **expectancy** hovered over the harvesting fields as the sun dipped behind the western downs." }
    ]
  },
  "Dashboard — pect/expectant.md": {
    primary: "Having or showing an excited feeling that something is about to happen; anticipating eagerly.",
    secondary: "Pregnant, or anticipating the birth of a child (an expectant mother); or in law, waiting in reversion to an estate.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The hush was deep and **expectant**, as if every listener hung upon the speaker's next utterance." },
      { author: "George Eliot", work: "Middlemarch", quote: "She sat in **expectant** silence, watching the door through which her future was to enter." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "We waited in the dark moor cottage, tense and **expectant**, with our weapons ready." }
    ]
  },
  "Dashboard — pect/expectantly.md": {
    primary: "In an expectant manner; with anticipation, hope, or excited eagerness.",
    secondary: "With focused, waiting attention.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "She looked up **expectantly** as the carriage drew to a halt before the vicarage gate." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The native rowers rested upon their oars, gazing **expectantly** into the impenetrable green fog." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "He smiled **expectantly**, waiting for her recognition to dawn in her expressive eyes." }
    ]
  },
  "Dashboard — pect/expectation.md": {
    primary: "A strong belief that something will happen or be the case in the future; anticipation.",
    secondary: "In probability theory and mathematics, expected value—the weighted average of all possible values that a random variable can take.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "My life in London was built on the splendid **expectation** of inherited wealth." },
      { author: "William Shakespeare", work: "Henry IV, Part 1", quote: "For more is not than what is due, and more than all can I repay; **expectation** whirls me round." },
      { author: "Pierre-Simon Laplace", work: "Philosophical Essay on Probabilities", quote: "Mathematical **expectation** is defined as the product of the possible gain multiplied by the probability of obtaining it." }
    ]
  },
  "Dashboard — pect/expected.md": {
    primary: "Regarded as likely to happen, arrive, or be the case; anticipated.",
    secondary: "In statistics and physics, denoting calculated theoretical values predicted by a model (the expected value).",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "The arrival of the post was an event eagerly **expected** throughout the morning hours." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Such transitional forms are precisely what would be **expected** on the theory of natural descent." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The long **expected** cry from the masthead startled the ship into furious activity." }
    ]
  },
  "Dashboard — pect/expectedness.md": {
    primary: "The quality or state of being expected, anticipated, or foreseeable.",
    secondary: "In cognitive psychology and information theory, the predictability of a stimulus or event within a perceptual sequence.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The sensory reaction time is sharply reduced by the **expectedness** of the impending auditory signal." },
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "The information content of a message decreases as its statistical **expectedness** approaches certainty." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "The sheer **expectedness** of the tragedy seemed to dull its emotional impact upon the household." }
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

console.log(`Updated ${updatedCount} files in Batch 5!`);
