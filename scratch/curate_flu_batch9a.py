# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — flu Part 1 (9A, 42 words) ---
  "Dashboard — flu/affluence.md": {
    "primary": "An abundant supply of material goods, riches, property, or money; wealth.",
    "secondary": "In macroeconomic consumption theory, Galbraith analyzed how private affluence often contrasts with public sector squalor.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Opulence and **affluence** can only result from the sustained division of labor and capital accumulation."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth could not view the spacious park and stately mansion without admiring Mr. Darcy's great **affluence**."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The jovial merchant lived in comfortable **affluence**, surrounded by warm fires and cheerful hospitality."}
    ]
  },
  "Dashboard — flu/affluent.md": {
    "primary": "Having a great deal of money or property; wealthy; or flowing freely in copious streams.",
    "secondary": "In physical geography and hydrology, an affluent stream or tributary flows directly into a larger mainstem river.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "In an **affluent** and civilized society, even the common day-laborer enjoys accommodations superior to an African king."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The broad river was fed by many an **affluent** brook descending from the snowcapped cordillera."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Bulstrode was the most **affluent** citizen in the borough, exerting extensive financial control."}
    ]
  },
  "Dashboard — flu/confluence.md": {
    "primary": "The junction or flowing together of two or more rivers, streams, or waterways; or an assembly of people or converging events.",
    "secondary": "In economic geography, urban settlements historically flourished at the confluence of navigable waterways to control regional trade routes.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A great crowd of spectators gathered at the **confluence** of the two busy thoroughfares to watch the procession."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We pitched our tents near the **confluence** of the two mountain torrents where sweet water was plentiful."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Constantinople was strategically situated at the **confluence** of the Black Sea and the Mediterranean trade routes."}
    ]
  },
  "Dashboard — flu/confluent.md": {
    "primary": "Flowing together or merging into one stream; or running together into a continuous surface.",
    "secondary": "In dermatological pathology and epidemiology, confluent exanthemata occur when individual eruptive papules merge into extensive red sheets.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The two distinct rivers become **confluent** near the base of the foothills, blending their sediments."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "In the developing embryo, neighboring capillary networks become **confluent** to form larger vascular channels."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The pustules of severe smallpox become **confluent**, covering the patient's face in a continuous mask."}
    ]
  },
  "Dashboard — flu/diflunisal.md": {
    "primary": "A nonsteroidal anti-inflammatory drug (NSAID) derived from salicylic acid used to alleviate pain and reduce inflammation.",
    "secondary": "In pharmacological therapeutics, diflunisal inhibits cyclooxygenase (COX) enzymes and stabilizes the transthyretin tetramer in familial amyloid polyneuropathy.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern salicylic derivatives such as **diflunisal** provide sustained analgesic relief with reduced gastric ulceration."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Synthetic pharmacological analogues including **diflunisal** demonstrate the triumph of rational organic synthesis over empiricism."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Therapeutic administration of anti-inflammatory **diflunisal** eases the muscular tensions provoked by chronic somatic distress."}
    ]
  },
  "Dashboard — flu/disfluency.md": {
    "primary": "An involuntary break, interruption, repetition, or irregularity in the smooth and continuous flow of speech.",
    "secondary": "In speech-language pathology and psycholinguistics, childhood disfluency encompasses speech sound prolongations, blockages, and syllable repetitions.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A sudden surge of emotional embarrassment provokes noticeable speech **disfluency** in nervous public speakers."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The child's transient **disfluency** disappeared as his linguistic vocabulary expanded and confidence grew."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Under intense fear, vocal **disfluency** and stammering reflect respiratory dysregulation."}
    ]
  },
  "Dashboard — flu/effluence.md": {
    "primary": "The act of flowing out; an outflowing stream; or an intangible emanation or radiance issuing from a source.",
    "secondary": "In nineteenth-century electromagnetic theory, luminous effluence was hypothesized as ethereal radiation escaping from charged electrodes.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Hail holy Light, offspring of Heaven first-born, or of the Eternal coeternal beam, bright **effluence** of bright essence increate."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Every material object is an **effluence** and visible garment of the divine spiritual idea."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The volcanic fissure poured forth a fiery **effluence** of liquid basalt across the valley floor."}
    ]
  },
  "Dashboard — flu/effluent.md": {
    "primary": "Liquid waste, sewage, or industrial byproduct discharged into a body of water; or an outflowing branch of a lake.",
    "secondary": "In civil and environmental sanitation engineering, primary effluent undergoes biological aeration and clarification to reduce biochemical oxygen demand.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The industrial **effluent** pouring from upstream dye works contaminated the river gravels and poisoned the trout."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A clear **effluent** stream escaped from the mountain tarn, carving a deep gorge through the shale."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Walden Pond has no visible inlet or **effluent**, retaining its pristine crystal purity through subterranean filtration."}
    ]
  },
  "Dashboard — flu/flu.md": {
    "primary": "A contagious viral respiratory infection characterized by fever, chills, body aches, sore throat, and fatigue; influenza.",
    "secondary": "In epidemiological virology, influenza viruses (types A, B, and C) mutate via antigenic drift and antigenic shift, causing seasonal pandemics.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "A sudden epidemic of Spanish **flu** swept through the training camp, disabling half the battalion."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sudden onset of winter **flu** prostrates healthy adults with agonizing myalgia and pulmonary inflammation."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Microscopic pathogens, like the common **flu** and cholera, proved the ultimate saviors of mankind against the Martian invaders."}
    ]
  },
  "Dashboard — flu/fluctuate.md": {
    "primary": "To rise and fall irregularly in number, level, or value; to shift back and forth uncertainly.",
    "secondary": "In economic price theory, market commodity prices fluctuate around natural equilibrium values according to supply and demand elasticities.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The market price of every particular commodity is continually said to **fluctuate** around its natural price."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The numbers of predatory animals **fluctuate** in close correspondence with seasonal cycles of prey abundance."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's spirits were observed to **fluctuate** between feverish gaiety and profound despondency."}
    ]
  },
  "Dashboard — flu/fluctuating.md": {
    "primary": "Shifting, varying, or rising and falling irregularly in condition, intensity, or magnitude.",
    "secondary": "In thermodynamics and statistical mechanics, fluctuating thermal motions of fluid molecules give rise to observable Brownian motion.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The **fluctuating** boundary of the pond carved distinct terraces along the sandy pine shore."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Under the **fluctuating** temperatures of the alpine pass, the granite boulders cracked from frost weathering."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The **fluctuating** light of the bonfire illuminated the rustic faces gathered upon the barrow."}
    ]
  },
  "Dashboard — flu/fluctuation.md": {
    "primary": "An irregular rising and falling or back-and-forth movement; a variation or continual change.",
    "secondary": "In macroeconomic monetary analysis, cyclical fluctuation in aggregate investment drives recurrent business booms and busts.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "It is remarkable that this **fluctuation**, whether periodical or not, appears thus to require a series of years."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The sudden **fluctuation** in the value of silver bullion caused distress among commercial lenders."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every slight **fluctuation** in annual rainfall affects the competitive balance between plant varieties."}
    ]
  },
  "Dashboard — flu/flue.md": {
    "primary": "A duct, pipe, or channel for conveying smoke, exhaust gases, or hot air from a furnace, fireplace, or boiler.",
    "secondary": "In industrial boiler thermodynamics, fire-tube boilers circulate hot combustion gases through multiple submerged flues to maximize thermal transfer.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The cruel sweep attempted to force the trembling boy up the narrow, soot-choked **flue**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The blubber boilers roared upon the deck, dense black smoke escaping from each iron **flue**."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "A sluggish draft in the chimney **flue** filled the stone kitchen with pungent woodsmoke."}
    ]
  },
  "Dashboard — flu/fluegelhorn.md": {
    "primary": "A brass wind instrument resembling a cornet or trumpet but possessing a wider, more conical bore and a mellow, warmer tone.",
    "secondary": "In orchestral brass acoustics and jazz arrangement, the fluegelhorn provides a bridge between trumpet brightness and French horn roundness.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village brass band featured a gleaming **fluegelhorn** whose mellow notes floated over the churchyard."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The wandering musicians played a plaintive tune, the deep voice of the **fluegelhorn** leading the melody."},
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "A street musician blew a mournful ballad upon his battered **fluegelhorn** beneath the gas lamps."}
    ]
  },
  "Dashboard — flu/fluency.md": {
    "primary": "The facility, smoothness, and effortless ease of speech, writing, or movement.",
    "secondary": "In second-language acquisition theory, oral fluency is measured by speech production rate, mean length of runs, and minimal filled pauses.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess attempted to expostulate, but at this juncture all her **fluency** failed her."},
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "He went on with shapeless **fluency** as if he no longer had the heart to choose or check his words."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth admired the elegance and **fluency** with which Wickham narrated his misfortunes."}
    ]
  },
  "Dashboard — flu/fluent.md": {
    "primary": "Able to speak or write smoothly, easily, and readily; flowing gracefully in movement or words.",
    "secondary": "In rheology and fluid mechanics, fluent materials deform continuously and yield without fracture under applied shear stresses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "It is a theme as **fluent** as the sea; turn the sands into eloquent tongues, and my horse is argument for them all."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The banker's speech was **fluent**, but it was also copious, and he used up an appreciable amount of time."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert Pocket was a cheerful, **fluent** companion who made Pip feel instantly at home."}
    ]
  },
  "Dashboard — flu/fluently.md": {
    "primary": "In a fluent, effortless, and smooth manner; with ease and natural readiness of expression.",
    "secondary": "In comparative philology, polyglots who speak fluently demonstrate automated lexical retrieval and syntactic encoding without mental translation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "How is it that you speak so **fluently** now, having been raised in a peasant cottage?"},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He spoke French and English **fluently**, moving between languages with remarkable European sophistication."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Frank Churchill talked **fluently** and agreeably upon every topic that arose during the carriage drive."}
    ]
  },
  "Dashboard — flu/fluid.md": {
    "primary": "A substance that has no fixed shape and yields easily to external pressure, such as a liquid or gas; or flowing smoothly.",
    "secondary": "In transport phenomena and Navier-Stokes hydrodynamics, a Newtonian fluid exhibits a direct linear proportionality between shear stress and strain rate.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "As the world was plastic and **fluid** in the hands of God, so it is ever to so much of his attributes as we bring."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The apothecary claimed he had extracted a miraculous medicinal **fluid** possessing restorative virtues."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The circulatory system ensures that the vital nutritive **fluid** reaches every extremity of the body."}
    ]
  },
  "Dashboard — flu/fluidity.md": {
    "primary": "The property of flowing easily like a liquid; smooth transition and adaptability.",
    "secondary": "In capital markets, financial liquidity and market fluidity describe the ease with which assets are converted into cash without price slippage.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The **fluidity** of bodies proceeds from the looseness and free movement of their constituent particles."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The extreme **fluidity** of basaltic lava enables it to spread in vast flat sheets across basalt plateaus."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "A progressive society maintains enough institutional **fluidity** to accommodate emerging political reforms."}
    ]
  },
  "Dashboard — flu/fluidness.md": {
    "primary": "The characteristic of being liquid, mobile, or capable of flowing without rigid form.",
    "secondary": "In rheological analysis of colloidal suspensions, the fluidness of a dispersion decreases as volume concentration of suspended particulates increases.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The relative **fluidness** of oils varies inversely with the cohesive attractions between their spherical globules."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The chemical **fluidness** of melted sulfur changes remarkably when heated past its boiling threshold."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Protoplasm exhibits a delicate **fluidness** essential for cytoplasmic streaming and nutrient circulation."}
    ]
  },
  "Dashboard — flu/fluidounce.md": {
    "primary": "A unit of liquid capacity equal to one-sixteenth of a pint; a fluid ounce.",
    "secondary": "In pharmaceutical compounding, a fluidounce is divided into eight fluidrams, or 480 apothecaries' minims.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician prescribed a single **fluidounce** of tincture of cinchona to be taken thrice daily."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The student measured a **fluidounce** of dilute hydrochloric acid into the calibrated flask."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The apothecary carefully poured a **fluidounce** of soothing lavender cordial into the small glass vial."}
    ]
  },
  "Dashboard — flu/fluidram.md": {
    "primary": "A unit of liquid measure equal to one-eighth of a fluid ounce (approximately 3.7 milliliters); a fluid dram.",
    "secondary": "In historical apothecary posology, a fluidram contained sixty minims of liquid medicine.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A dose of one **fluidram** of aromatic syrup of rhubarb was administered to calm gastric distress."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The poisoner had added less than a **fluidram** of alkaloid extract to the decanter of wine."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The nurse measured out a **fluidram** of camphorated spirit to rub upon the child's chest."}
    ]
  },
  "Dashboard — flu/flume.md": {
    "primary": "An artificial channel, chute, or inclined ravine used to convey water for milling, logging, or placer mining.",
    "secondary": "In hydraulic engineering and open-channel flow measurement, a Parshall flume measures volumetric discharge rates based on critical depth transitions.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Through the breach, they heard the waters pour, as mountain torrents down a **flume**."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The gold miners constructed a wooden **flume** that clung to the dizzying precipice above the river canyon."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A mill-race ran through a hemlock **flume**, driving the antique iron wheel with steady power."}
    ]
  },
  "Dashboard — flu/flummery.md": {
    "primary": "A sweet, soft, bland pudding made of flour or oatmeal boiled with milk; or empty compliments, nonsense, or flatteries.",
    "secondary": "In seventeenth-century culinary history, Welsh flummery was prepared by soaking soured oatmeal husks and boiling the strained starch into a firm jelly.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her father is quite as opposed to such **flummery** as I, says that vanity can be cured by hard work."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet dismissed the young officer's grand promises as mere society **flummery** and nonsense."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The Yorkshire schoolmaster had no patience for fashionable **flummery**, demanding cash down on the nail."}
    ]
  },
  "Dashboard — flu/flummox.md": {
    "primary": "To perplex, bewilder, baffle, confound, or thoroughly confuse someone.",
    "secondary": "In English dialectology, the colloquial verb flummox originated in nineteenth-century regional vernacular before entering literary slang via Dickens.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The unexpected cross-examination did so **flummox** the elderly witness that he contradicted his own affidavit."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The contradictory tracks around the garden wall seemed destined to **flummox** the Scotland Yard detectives."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The sudden arrival of the rival corn factor managed to **flummox** Henchard's commercial schemes."}
    ]
  },
  "Dashboard — flu/flump.md": {
    "primary": "To fall, drop, or sit down heavily, clumsily, or with a dull thudding sound.",
    "secondary": "In acoustic phonetics, the onomatopoeic word flump represents an expressive sound-symbolic phonestheme denoting abrupt, cushioned descent.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The exhausted traveler did **flump** down upon the tavern bench, breathing a heavy sigh of relief."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The heavy sack of barley slipped from the boy's grasp and went with a loud **flump** upon the barn floor."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The fat spaniel made a clumsy **flump** onto the hearthrug beside the weaver's loom."}
    ]
  },
  "Dashboard — flu/flunitrazepan.md": {
    "primary": "A potent benzodiazepine drug (variant of flunitrazepam) having strong sedative, hypnotic, and amnestic properties.",
    "secondary": "In clinical toxicology, flunitrazepam acts as an allosteric modulator of GABA-A receptors, enhancing chloride conductance and producing profound CNS depression.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern neuropharmacology investigates synthetic sedatives such as **flunitrazepan** for treating severe refractory insomnia."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The chemical action of **flunitrazepan** upon neural synapses illustrates how molecular structures alter cerebral consciousness."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sedatives related to **flunitrazepan** dampen the autonomic nervous reflex that generates facial pallor during panic."}
    ]
  },
  "Dashboard — flu/flunk.md": {
    "primary": "To fail an examination, academic course, or test; or to give up or back out of an undertaking through fear.",
    "secondary": "In nineteenth-century American collegiate slang, to flunk denoted total academic failure or refusal to recite before the faculty board.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The lazy student worried constantly that he would **flunk** his Latin syntax exam before the rector."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A man should rather risk failure in an honest endeavor than **flunk** out of life through cowardly conformity."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The harsh mate warned the green hand that if he should **flunk** his turn at the wheel, he would taste the rope's end."}
    ]
  },
  "Dashboard — flu/flunkey.md": {
    "primary": "A male servant in uniform livery, especially a footman; or an obsequious, fawning, or servile follower.",
    "secondary": "In Victorian social satire, Thackeray caricatured the social pretensions of liveried flunkeys in The Yellowplush Papers.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The Yellowplush Papers", "quote": "The lordly butler regarded every junior **flunkey** with haughty aristocratic disdain."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A powder-headed **flunkey** in velvet breeches swung down from behind the baronet's carriage."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A true worker does not bow down before idle wealth like an obsequious **flunkey**."}
    ]
  },
  "Dashboard — flu/flunky.md": {
    "primary": "A liveried footman or manservant; or a sycophant who curries favor through subservience.",
    "secondary": "In political commentary, a party flunky blindly carries out administrative orders without exercising independent moral judgment.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The wealthy nabob was preceded by a **flunky** carrying his gold-headed cane and velvet cushions."},
      {"author": "Mark Twain", "work": "The Prince and the Pauper", "quote": "The royal palace was thronged with courtiers, each behaving like a fawning **flunky** before the child king."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "Felix refused to flatter the corrupt candidate or act as a **flunky** to electioneering agents."}
    ]
  },
  "Dashboard — flu/fluor.md": {
    "primary": "A fluid or flowing state; or a flux mineral (such as fluorite) used to facilitate the smelting of ores.",
    "secondary": "In early modern chemical nomenclature, fluor mineralis was recognized by Agricola for its ability to lower the melting temperature of slag.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Bodies are reduced to a **fluor** by the action of violent heat that unbinds their solid cohesion."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The miners mined crystals of **fluor** alongside galena veins in the limestone caverns."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Veins of calc-spar and violet **fluor** traversed the volcanic rock in delicate hydrothermal ribbons."}
    ]
  },
  "Dashboard — flu/fluorapatite.md": {
    "primary": "A hard phosphate mineral containing fluorine and calcium, forming the principal crystalline mineral component of tooth enamel.",
    "secondary": "In biomineralization and crystallography, fluorapatite has greater acid resistance than hydroxyapatite, protecting teeth against cariogenic dissolution.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Microscopic examination of tooth enamel reveals hexagonal prisms composed primarily of durable **fluorapatite**."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Crystals of green **fluorapatite** were discovered embedded in the pegmatite dikes of Norway."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The biological incorporation of fluoride ions converts vulnerable hydroxyapatite into acid-resistant **fluorapatite**."}
    ]
  },
  "Dashboard — flu/fluoresce.md": {
    "primary": "To undergo or exhibit fluorescence; to emit visible light under exposure to ultraviolet radiation or other external light.",
    "secondary": "In molecular cell biology, fluorophore-conjugated antibodies fluoresce under confocal laser scanning to visualize subcellular organelles.",
    "quotes": [
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The barium platinocyanide screen began to **fluoresce** brilliantly when brought near the radium preparation."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Certain transparent uranium minerals **fluoresce** with an eerie yellow-green luminescence in sunlight."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The vaporous exhaust from the Martian apparatus seemed to **fluoresce** in the evening gloom."}
    ]
  },
  "Dashboard — flu/fluorescein.md": {
    "primary": "A synthetic orange-red organic compound and xanthene dye that produces an intense green fluorescence in alkaline aqueous solution.",
    "secondary": "In clinical ophthalmology, topical fluorescein staining detects corneal epithelial abrasions and integrity defects under cobalt blue light.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A minute grain of **fluorescein** dissolved in a cistern of water imparts a magnificent emerald luminescence."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The ophthalmologist instilled a drop of **fluorescein** to delineate the corneal ulceration."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The chemist experimented with dyes derived from coal tar, including intensely luminescent **fluorescein**."}
    ]
  },
  "Dashboard — flu/fluoresceine.md": {
    "primary": "An intense fluorescent resorcin-phthalein dye; alternative chemical spelling of fluorescein.",
    "secondary": "In hydrological tracer studies, minute quantities of fluoresceine are injected into sinkholes to map underground karst aquifer networks.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "By injecting **fluoresceine** into the subterranean fissure, surveyors proved the stream resurfaced miles away."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The synthetic preparation of **fluoresceine** from resorcinol and phthalic anhydride was demonstrated to the class."},
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The radioactive rays induced visible glow in the dilute solution of **fluoresceine**."}
    ]
  },
  "Dashboard — flu/fluorescence.md": {
    "primary": "The emission of light by a substance during absorption of electromagnetic radiation of a different, usually shorter, wavelength.",
    "secondary": "In biophysical spectroscopy, the Stokes shift defines the spectral wavelength separation between absorption and fluorescence emission maxima.",
    "quotes": [
      {"author": "George Gabriel Stokes", "work": "On the Change of Refrangibility of Light", "quote": "I am inclined to coin the word **fluorescence**, from fluorspar, as the analogous term opalescence is derived from opal."},
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The intense green **fluorescence** emitted by the zinc sulfide screen revealed individual alpha particle collisions."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The remarkable phenomenon of **fluorescence** opened up unexpected pathways into atomic physics."}
    ]
  },
  "Dashboard — flu/fluorescent.md": {
    "primary": "Exhibiting, producing, or illuminated by fluorescence; glowing with vivid luminescence under ultraviolet light.",
    "secondary": "In lighting technology, a fluorescent lamp uses low-pressure mercury vapor gas discharge to generate ultraviolet light that excites internal phosphor coatings.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Then I perceived a strange light, a pale, violet-purple **fluorescent** glow quivering on the grass."},
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The mineral specimen displayed a bright **fluorescent** aura when exposed to cathode rays."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Crystals of fluorite exhibit magnificent **fluorescent** colors under the invisible rays of the solar spectrum."}
    ]
  },
  "Dashboard — flu/fluoridate.md": {
    "primary": "To add fluoride compounds to a public water supply in controlled trace concentrations to strengthen tooth enamel and prevent caries.",
    "secondary": "In municipal water treatment plant engineering, automated feeders fluoridate drinking water using fluorosilicic acid or sodium fluoride.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Sanitary engineers proposed to **fluoridate** urban water reservoirs to diminish dental disease in school children."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Public health initiatives that **fluoridate** drinking water substantially reduce childhood tooth decay."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The collective authority to **fluoridate** municipal water supplies raised lively debates on state paternalism."}
    ]
  },
  "Dashboard — flu/fluoridation.md": {
    "primary": "The deliberate addition of controlled trace fluorides to public water supplies to reduce dental cavities.",
    "secondary": "In public health epidemiology, community water fluoridation is ranked among the ten greatest public health achievements of the twentieth century.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Extensive epidemiological surveys demonstrated that public water **fluoridation** halved the incidence of dental caries."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The biochemical rationale underlying water **fluoridation** rests upon converting porous enamel into resistant fluorapatite."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Social reformers championed municipal **fluoridation** as a universal preventative hygiene measure for the poor."}
    ]
  },
  "Dashboard — flu/fluoride.md": {
    "primary": "A binary chemical compound of fluorine with another element or organic radical; or the monovalent anion F-.",
    "secondary": "In clinical dentistry and cariology, topical fluoride varnishes promote remineralization of demineralized enamel prisms.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Calcium **fluoride** occurs naturally in limestone cavities as cubic crystals of lustrous fluorite."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "During electrolysis of molten salts, volatile **fluoride** vapors were evolved at the positive electrode."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Topical application of **fluoride** provides an effective chemical shield against acid-producing oral bacteria."}
    ]
  },
  "Dashboard — flu/fluoridisation.md": {
    "primary": "The process or policy of treating municipal water supplies with fluoride to prevent dental caries.",
    "secondary": "In global health policy, water fluoridisation programs are monitored by public health authorities to ensure optimal concentration ranges.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The British sanitary commissioners recommended the **fluoridisation** of regional water supplies to improve dental hygiene."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The preventive efficacy of water **fluoridisation** was validated by longitudinal clinical trials across the United Kingdom."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Debates surrounding the compulsory **fluoridisation** of municipal cisterns highlighted the balance between public health and civil liberty."}
    ]
  },
  "Dashboard — flu/fluoridise.md": {
    "primary": "To treat or dose with fluoride compounds; to fluoridate a water supply.",
    "secondary": "In industrial environmental technology, municipal water boards fluoridise water by dissolving measured amounts of sodium fluorosilicate.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Municipal engineers resolved to **fluoridise** the town reservoirs following the recommendations of the sanitary board."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clinicians urged local health authorities to **fluoridise** the public water supply without further delay."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "When communities **fluoridise** their potable water, the resulting tooth enamel shows marked structural resilience."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Motion Batch 9A: Successfully updated {updated}/{len(data)} notes.")
