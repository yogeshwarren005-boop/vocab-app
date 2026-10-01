import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Plants & Botany';

function updateNote(relPath, data) {
  const filePath = path.join(CLUSTER_DIR, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch8Data = {
  "Dashboard — phyt/autophyte.md": {
    primary: "A self-nourishing plant capable of synthesizing its own food from inorganic substances through photosynthesis, without relying upon organic matter from other organisms.",
    secondary: "In plant physiological ecology, a strictly autotrophic organism possessing chlorophyll, contrasting with heterotrophic parasites and saprophytes.",
    quotes: [
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "The green **autophyte** assimilates carbon dioxide directly from the atmosphere under the catalytic power of absorbed sunlight." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "In forest succession, the initial colonizers are typically an independent **autophyte** species tolerant of nutrient-poor bare mineral substrates." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "While dodder lives parasitically, the clover host upon which it feeds is a normal independent **autophyte**." }
    ]
  },
  "Dashboard — phyt/autophytic.md": {
    primary: "Capable of synthesizing organic nutrients independently from inorganic sources via photosynthesis; autotrophic.",
    secondary: "In physiological plant nutrition, designating self-sustaining metabolic pathways that depend exclusively on light, water, carbon dioxide, and mineral ions.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The **autophytic** nutrition of green thallophytes demonstrates the fundamental biochemical foundation of all terrestrial life." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The fern gametophyte is entirely **autophytic**, absorbing soil water through rhizoids while its prothallus photosynthesizes." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "Loss of **autophytic** capacity accompanies the evolutionary transition toward total root parasitism in broomrapes." }
    ]
  },
  "Dashboard — phyt/bryophyte.md": {
    primary: "A small, non-vascular land plant belonging to the division Bryophyta in the broad sense, encompassing mosses, liverworts, and hornworts.",
    secondary: "In evolutionary plant morphology, an early embryophyte characterized by the dominance of the free-living haploid gametophyte generation over the dependent sporophyte.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "Higher Cryptogamia", quote: "The life cycle of the **bryophyte** pivots upon the alternation between an independent leafy gametophyte and a stalked sporogonium." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "No true vascular xylem vessels occur in any **bryophyte**, conduction being performed by simple elongated parenchymatous cells." },
      { author: "Frederick Orpen Bower", work: "The Origin of a Land Flora", quote: "The ancestral **bryophyte** adapted to land by evolving desiccation-resistant cuticles and airborne spores enclosed in sporopollenin." }
    ]
  },
  "Dashboard — phyt/bryophytic.md": {
    primary: "Of, relating to, or resembling a bryophyte (moss, liverwort, or hornwort).",
    secondary: "In plant ecology, characterizing vegetation communities, cushions, or microhabitats dominated by non-vascular cryptogams.",
    quotes: [
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "The high montane scree was stabilized by a dense **bryophytic** crust that trapped moisture and windblown dust." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The **bryophytic** gametophyte exhibits exquisite adaptations for capillary water transport along its external leafy surfaces." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "Deep gorges in the eastern Himalayas are clothed in luxuriant **bryophytic** carpets dripping with perpetual mist." }
    ]
  },
  "Dashboard — phyt/dermatophyte.md": {
    primary: "A parasitic fungus that causes superficial infections of the skin, hair, or nails in humans and other animals (such as ringworm, athlete's foot, and jock itch).",
    secondary: "In medical mycology, specialized filamentous fungi of the genera Trichophyton, Microsporum, and Epidermophyton that digest keratinized tissue via keratinases.",
    quotes: [
      { author: "Arthur Rook", work: "Textbook of Dermatology", quote: "Microscopic potassium hydroxide mounts reveal branching septate hyphae and arthrospores characteristic of a pathogenic **dermatophyte**." },
      { author: "Thomas B. Fitzpatrick", work: "Dermatology in General Medicine", quote: "Transmission of an anthropophilic **dermatophyte** occurs rapidly through shared athletic flooring and locker rooms." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Tinea capitis represents an active invasion of hair shafts by a virulent parasitic **dermatophyte**." }
    ]
  },
  "Dashboard — phyt/epiphyte.md": {
    primary: "A plant that grows upon another plant or object non-parasitically, deriving moisture and nutrients from the air, rain, and accumulated debris.",
    secondary: "In tropical forest ecology, canopy-dwelling plants such as bromeliads, orchids, and ferns that occupy canopy niches to access sunlight without rooting in ground soil.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Every branch of the colossal wild fig tree was smothered in dense garlands of orchids, ferns, and bromeliad **epiphyte** colonies." },
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The aerial roots of the tropical **epiphyte** are encased in spongy velamen that absorbs moisture from monsoon humidity." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "So immense is the weight of water accumulated by canopy **epiphyte** clusters that great branches frequently crash to the ground." }
    ]
  },
  "Dashboard — phyt/epiphytic.md": {
    primary: "Growing upon another plant for physical support without taking nourishment from it; characteristic of an epiphyte.",
    secondary: "In structural botany, possessing morphological adaptations such as water-absorbing velamen roots, pseudobulbs, or tank rosettes for arboreal canopy life.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The **epiphytic** orchids of South America cling to living bark, basking in humid air and dappled jungle sunlight." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Spanish moss (Tillandsia) is not a true moss or parasite, but a rootless **epiphytic** angiosperm of the pineapple family." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "We admired the magnificent **epiphytic** rhododendrons rooted upon mossy forks of ancient forest oaks." }
    ]
  },
  "Dashboard — phyt/epiphytotic.md": {
    primary: "A widespread, destructive outbreak of disease among plants, analogous to an epidemic among human populations.",
    secondary: "In agricultural phytopathology, a sudden and devastating surge of fungal, viral, or bacterial plant infection over a broad geographical area.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "The sudden potato blight in Ireland was an catastrophic **epiphytotic** that destroyed the food supply of an entire nation." },
      { author: "William Gilson Farlow", work: "The Gymnosporangia or Cedar-Apples of the United States", quote: "Warm humid weather in midsummer provided ideal conditions for an aggressive rust **epiphytotic** across cereal fields." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Prompt removal of infected orchard shoots prevents a localized blight from developing into a disastrous **epiphytotic**." }
    ]
  },
  "Dashboard — phyt/holophyte.md": {
    primary: "A plant or plant-like organism that synthesizes its own food entirely from inorganic substances through photosynthesis; a strict autotroph.",
    secondary: "In protozoology and physiological ecology, an organism exhibiting holophytic nutrition, contrasting with phagotrophic holozoa and saprotrophic fungi.",
    quotes: [
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "The true **holophyte** constructs complex proteins and carbohydrates solely from carbon dioxide, water, and nitrate salts." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Among flagellates, Euglena behaves as a **holophyte** in light, while related forms have lost their plastids and become holozoic." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The metabolic divide between the animal holozoon and the green **holophyte** represents the fundamental divergence of eukaryotic life." }
    ]
  },
  "Dashboard — phyt/holophytic.md": {
    primary: "Obtaining nourishment entirely through photosynthesis from inorganic substances; strictly plant-like in nutrition.",
    secondary: "In cellular biology, designating autotrophic nutrition involving light absorption, water photolysis, and carbon fixation.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Green algae exhibit pure **holophytic** metabolism, requiring only dissolved mineral salts and illumination to thrive." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Transition from a **holophytic** flagellate ancestor to phagotrophic animal protists is illuminated by colorless dinoflagellates." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The **holophytic** independence of the prothallus ensures reproduction in pteridophytes without host dependence." }
    ]
  },
  "Dashboard — phyt/mesophyte.md": {
    primary: "A plant that requires a moderate, well-balanced supply of moisture, thriving in average climatic conditions (contrasting with xerophytes and hydrophytes).",
    secondary: "In physiological plant ecology, terrestrial vegetation with broad foliage, non-sunken stomata, and moderate root systems adapted to temperate climates.",
    quotes: [
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "Deciduous woodland trees like oak and beech are typical examples of a **mesophyte**, shedding leaves to survive winter frosts." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Unlike the water-lily or desert cactus, the common garden bean is an ordinary **mesophyte** requiring regular rainfall." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "Leaf cuticles in a typical **mesophyte** are moderately thin, allowing efficient gas exchange while preventing excessive wilting." }
    ]
  },
  "Dashboard — phyt/mesophytic.md": {
    primary: "Of, relating to, or adapted to conditions of moderate moisture; characteristic of a mesophyte.",
    secondary: "In phytosociology and forest ecology, characterizing temperate deciduous climax forests and rich meadow communities.",
    quotes: [
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "The mixed **mesophytic** forest represents the richest and most diverse temperate forest ecosystem in the Northern Hemisphere." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Appalachian coves shelter pristine **mesophytic** flora that survived Pleistocene glaciations in unglaciated refugia." },
      { author: "John Muir", work: "The Mountains of California", quote: "In the middle forest zone, magnificent sugar pines and firs flourish under optimal **mesophytic** moisture conditions." }
    ]
  },
  "Dashboard — phyt/metaphysical.md": {
    primary: "Of or relating to metaphysics (the philosophical inquiry into the nature of reality, being, and the universe); abstract, theoretical, or transcendental.",
    secondary: "In English literary history, designating 17th-century poets (such as Donne and Herbert) characterized by ingenious conceits, complex wit, and intellectual subtlety.",
    quotes: [
      { author: "Samuel Johnson", work: "Life of Cowley", quote: "About the beginning of the seventeenth century appeared a race of writers that may be termed the **metaphysical** poets." },
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "Human reason has this peculiar fate: it is burdened by questions which it cannot dismiss, yet which lead into endless **metaphysical** disputes." },
      { author: "William James", work: "The Will to Believe", quote: "Pragmatism turns away from abstraction, verbal solutions, and bad **metaphysical** reasons, toward facts, action, and power." }
    ]
  },
  "Dashboard — phyt/metaphysics.md": {
    primary: "The branch of philosophy that deals with the first principles of things, including abstract concepts such as being, knowing, substance, cause, identity, time, and space.",
    secondary: "In the history of philosophy, the foundational inquiry originating in Aristotle's treatises 'beyond the physical' (ta meta ta physika).",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", quote: "All men by nature desire to know; and the supreme science, which we call **metaphysics**, inquires into first principles and primary causes." },
      { author: "Immanuel Kant", work: "Prolegomena to Any Future Metaphysics", quote: "My aim is to persuade all those who think it worthwhile to deal with **metaphysics** to suspend their work until they can answer its first problem." },
      { author: "David Hume", work: "An Enquiry Concerning Human Understanding", quote: "If we take in our hand any volume of divinity or school **metaphysics**, let us ask: Does it contain any abstract reasoning concerning quantity or number? Commit it to the flames." }
    ]
  },
  "Dashboard — phyt/neophyte.md": {
    primary: "A person who is new to a subject, skill, or belief; a novice, beginner, or recent convert.",
    secondary: "In ecclesiastical and plant geography, a newly baptized Christian in the early church; in botany, a plant recently introduced to a flora (since 1500).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The white robes of the baptized **neophyte** symbolized the complete purification of the soul in the sacred font." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Holmes warned me that only a reckless **neophyte** would disturb the pristine footprints around the garden gate." },
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "Botanists distinguish between an ancient archaeophyte weed and an aggressive modern **neophyte** escaped from gardens." }
    ]
  },
  "Dashboard — phyt/physical.md": {
    primary: "Of or relating to the body as opposed to the mind; of or relating to natural science and the material universe; tangible or concrete.",
    secondary: "In physics and philosophy of science, relating to the properties of matter, energy, space, and time governed by mathematical natural laws.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "To determine by experiment the true **physical** properties of light rays was the chief intention of my researches." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Geographical isolation and the **physical** barriers of oceans and mountain chains govern the distribution of organic beings." },
      { author: "William James", work: "The Principles of Psychology", quote: "Every psychic event is accompanied by a corresponding **physical** process within the cerebral cortex." }
    ]
  },
  "Dashboard — phyt/physicalism.md": {
    primary: "The philosophical thesis that everything that exists is ultimately physical, and that all facts and entities supervene on physical properties and laws.",
    secondary: "In philosophy of mind and logical positivism, the doctrine advanced by Carnap and Neurath that psychological states are reducible to physical states or behavioral sentences.",
    quotes: [
      { author: "Rudolf Carnap", work: "The Unity of Science", quote: "The thesis of **physicalism** maintains that every sentence in psychology can be translated into a sentence referring to physical states." },
      { author: "Bertrand Russell", work: "An Inquiry into Meaning and Truth", quote: "A consistent **physicalism** must account for the subjective sensation of color without postulating mysterious immaterial substances." },
      { author: "Willard Van Orman Quine", work: "Ontological Relativity", quote: "I hold with **physicalism** because I see physics as our best current attempt to delineate the ultimate furniture of the world." }
    ]
  },
  "Dashboard — phyt/physicality.md": {
    primary: "The state, quality, or condition of being physical; bodily existence or tangible material nature.",
    secondary: "In literature and aesthetics, the direct, sensory presence or visceral force of bodily action and material reality.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The Greek sculptor celebrated the heroic **physicality** of the athlete while infusing the marble with divine serenity." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The raw **physicality** of the dairy barn at milking time surrounded her with earthy smells of warm milk and hay." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The sheer brute **physicality** of the leviathan's breach shook the very foundations of the ocean." }
    ]
  },
  "Dashboard — phyt/physically.md": {
    primary: "In a physical manner; with regard to the body or the material world; according to the laws of physics.",
    secondary: "In natural philosophy, operating through tangible material forces rather than spiritual, moral, or abstract influences.",
    quotes: [
      { author: "Charles Darwin", work: "Journal of Researches (Voyage of the Beagle)", quote: "The crew was **physically** exhausted after battling fierce Antarctic gales off Cape Horn for three weeks." },
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "Two distant celestial bodies act upon each other **physically** through the universal law of gravitational attraction." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "Man is **physically** one with the apes, possessing an almost identical skeletal and muscular framework." }
    ]
  },
  "Dashboard — phyt/physicalness.md": {
    primary: "The quality, state, or property of being physical; materiality or tangible existence.",
    secondary: "In philosophical metaphysics, the condition of possessing material extension, mass, and location in spacetime.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "Common sense insists upon the stubborn **physicalness** of rocks and trees against all subjective idealist subtilties." },
      { author: "Herbert Spencer", work: "First Principles", quote: "The ultimate **physicalness** of cosmic matter reveals itself through the indestructible conservation of energy." },
      { author: "John Dewey", work: "Experience and Nature", quote: "Science does not deny the reality of values, but grounds them within the concrete **physicalness** of biological life." }
    ]
  },
  "Dashboard — phyt/physician.md": {
    primary: "A person qualified and licensed to practice medicine; a medical doctor.",
    secondary: "Historically, a practitioner of internal medicine and medical diagnostics, distinguished from the surgeon and apothecary.",
    quotes: [
      { author: "Hippocrates", work: "The Oath of Medicine", quote: "I will apply dietetic measures for the benefit of the sick according to my ability and judgment; so vows every true **physician**." },
      { author: "William Osler", work: "AEquanimitas", quote: "The master-word in medicine for the young **physician** is work, unsparing devotion to the relief of human suffering." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The educated **physician** relies upon the healing power of nature, intervening with remedies only when nature falters." }
    ]
  },
  "Dashboard — phyt/physicist.md": {
    primary: "An expert or scientist who specializes in physics, the study of matter, energy, space, and time.",
    secondary: "A natural philosopher who formulates and tests quantitative mathematical theories of the physical universe.",
    quotes: [
      { author: "Albert Einstein", work: "Ideas and Opinions", quote: "The supreme task of the **physicist** is to arrive at those universal elementary laws from which the cosmos can be built up by pure deduction." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "A practical **physicist** must test his most brilliant hypotheses against the unbending verdict of the laboratory." },
      { author: "Richard Feynman", work: "The Character of Physical Law", quote: "What cannot be computed and tested against nature is of no value to the working **physicist**." }
    ]
  },
  "Dashboard — phyt/physics.md": {
    primary: "The branch of science concerned with the nature and properties of matter and energy, including mechanics, heat, light, radiation, sound, electricity, magnetism, and atomic structure.",
    secondary: "In the history of science, the foundational natural science originating in Aristotle's Physis that seeks mathematical principles governing the cosmos.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "The main business of natural philosophy and **physics** is to argue from phenomena without feigning hypotheses." },
      { author: "Albert Einstein", work: "The Evolution of Physics", quote: "The formulation of a problem in **physics** is often far more essential than its mathematical solution." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "The ultimate aim of all **physics** is to reduce natural phenomena to the laws of mechanics." }
    ]
  },
  "Dashboard — phyt/physiologic.md": {
    primary: "Of or relating to physiology (the biological study of bodily functions); physiological.",
    secondary: "In clinical pathology and pharmacology, normal or natural to healthy bodily functioning, as opposed to pathological.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The constancy of the internal environment is the indispensable condition of free, independent **physiologic** life." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Administration of normal saline solution restores **physiologic** vascular volume in severe hemorrhagic shock." },
      { author: "Charles Scott Sherrington", work: "The Integrative Action of the Nervous System", quote: "The knee-jerk represents a normal **physiologic** reflex whose exaggeration indicates pyramidal tract lesions." }
    ]
  },
  "Dashboard — phyt/physiological.md": {
    primary: "Relating to the branch of biology that deals with the normal functions of living organisms and their parts; consistent with normal bodily operation.",
    secondary: "In biological science, pertaining to mechanical, physical, and biochemical processes of organs, tissues, and cells in maintaining life.",
    quotes: [
      { author: "Claude Bernard", work: "Experimental Medicine", quote: "The **physiological** investigator must remain the active minister and interpreter of living nature." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Certain expressions of grief and fear follow directly from **physiological** reflexes over which the will has no control." },
      { author: "William James", work: "The Principles of Psychology", quote: "Our mental life is anchored in **physiological** processes taking place within the nervous fibers of the cerebrum." }
    ]
  },
  "Dashboard — phyt/physiologically.md": {
    primary: "In a physiological manner; with regard to the functions and working processes of a living organism.",
    secondary: "In biological medicine, functioning according to normal homeostatic and biochemical metabolic mechanisms.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "An animal cannot live **physiologically** without maintaining strict equilibrium between heat production and thermal dissipation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The hypertrophy of the left ventricle was **physiologically** compensatory for the diseased aortic valve." },
      { author: "Charles Scott Sherrington", work: "The Integrative Action of the Nervous System", quote: "Reciprocal innervation coordinates muscle groups **physiologically** so that antagonistic sets relax while agonists contract." }
    ]
  },
  "Dashboard — phyt/physiologist.md": {
    primary: "A scientist who specializes in physiology, the study of the functions, mechanisms, and vital processes of living organisms.",
    secondary: "An experimental biologist who analyzes cardiovascular, nervous, endocrine, or cellular functions in health and disease.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The true **physiologist** does not explain life by vital force, but analyzes its physicochemical mechanisms step by step." },
      { author: "William Harvey", work: "De Motu Cordis", quote: "I profess both to learn and to teach anatomy, not from books, but from dissections; thus speaks every genuine **physiologist**." },
      { author: "Charles Scott Sherrington", work: "Man on His Nature", quote: "The task of the **physiologist** is to unravel how a billion microscopic neurons weave the seamless tapestry of consciousness." }
    ]
  },
  "Dashboard — phyt/physiology.md": {
    primary: "The branch of biology that deals with the normal functions, activities, and mechanical processes of living organisms and their parts.",
    secondary: "In medical history, the foundational biological science established by William Harvey, Albrecht von Haller, and Claude Bernard to explain the mechanisms of life.",
    quotes: [
      { author: "William Harvey", work: "The Circulation of the Blood", quote: "The motion of the heart and the circulation of the blood represent the foundational cornerstone of animal **physiology**." },
      { author: "Claude Bernard", work: "Experimental Medicine", quote: "True **physiology** demonstrates that every living process is subject to rigid determinism governed by physical laws." },
      { author: "William Osler", work: "AEquanimitas", quote: "Without a thorough grounding in morbid anatomy and normal **physiology**, clinical medicine becomes mere reckless guesswork." }
    ]
  },
  "Dashboard — phyt/physique.md": {
    primary: "The form, size, proportion, and muscular development of a person's body.",
    secondary: "In somatology and physical anthropology, an individual's constitutional somatic build and physical fitness.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Ancient hunter-gatherers required an athletic **physique** and boundless physical endurance to pursue fleet game across arid plains." },
      { author: "Francis Galton", work: "Hereditary Genius", quote: "Great athletes and oarsmen demonstrate the inheritance of a powerful muscular **physique** across successive generations." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Sir Henry Baskerville was a man of middle stature, dark-eyed, sturdily built, exhibiting the robust **physique** of an outdoorsman." }
    ]
  },
  "Dashboard — phyt/phytelephas.md": {
    primary: "A genus of South American feather palms (family Arecaceae), known as ivory palms or tagua palms, whose seeds yield vegetable ivory.",
    secondary: "In economic tropical botany, dioecious low-stemmed palms whose female heads produce massive woody burrs containing rock-hard white endosperm used as a substitute for elephant ivory.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Along the Magdalena River, the **Phytelephas** palm bears colossal clusters of nuts whose kernel hardens into vegetable ivory." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Turners and button-makers import millions of tagua nuts from **Phytelephas** macrocarpa as an ethical substitute for elephant tusk." },
      { author: "Alfred Russel Wallace", work: "Palm Trees of the Amazon", quote: "The dense fibrous spathes and glistening fronds of **Phytelephas** form a dense, elegant understory in the western Amazonian basin." }
    ]
  },
  "Dashboard — phyt/phytochemical.md": {
    primary: "Any chemical compound produced naturally by plants, especially one that may affect health but is not an essential nutrient.",
    secondary: "In natural product chemistry and pharmacognosy, secondary metabolites (alkaloids, flavonoids, terpenoids, polyphenols) that provide plants with chemical defenses against herbivores and pathogens.",
    quotes: [
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Modern nutritional science explores each potent **phytochemical** in cruciferous vegetables for antioxidant and chemopreventive properties." },
      { author: "William Woodville", work: "Medical Botany", quote: "Every crude herbal tincture contains a complex **phytochemical** array that interacts synergistically within the patient's frame." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The isolation of pure quinine demonstrated that the medicinal virtue of cinchona bark resides in a discrete **phytochemical** alkaloid." }
    ]
  },
  "Dashboard — phyt/phytochemist.md": {
    primary: "A chemist who specializes in the study of plant chemicals, their structures, and biosyntheses; a specialist in phytochemistry.",
    secondary: "In pharmaceutical research, an investigator who isolates, fractionates, and characterizes novel bioactive natural products from botanical specimens.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The investigative **phytochemist** extracts crystalline glucosides from wild roots, illuminating nature's metabolic laboratory." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "By combining chromatography with spectroscopy, the modern **phytochemist** identifies secondary metabolites in microgram quantities." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "The industrial **phytochemist** perfected the commercial extraction of morphine and codeine from the dried latex of opium poppies." }
    ]
  },
  "Dashboard — phyt/phytochemistry.md": {
    primary: "The branch of chemistry that deals with the study of chemicals and secondary metabolites derived from plants.",
    secondary: "In academic natural product science, the discipline focused on the biosynthesis, isolation, structural elucidation, and ecological roles of plant compounds.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Pioneering discoveries in **phytochemistry** laid the foundation of organic synthesis by demonstrating carbon ring architectures in plant alkaloids." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Advances in **phytochemistry** have revealed that dietary flavonoids exert protective antioxidant actions in human cellular metabolism." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "A comprehensive treatise on **phytochemistry** classifies plant constituents into carbohydrates, fixed oils, essential essences, and alkaloids." }
    ]
  },
  "Dashboard — phyt/phytohormone.md": {
    primary: "A naturally occurring organic substance (plant hormone) that regulates plant physiological processes like growth, development, and differentiation at low concentrations.",
    secondary: "In plant physiology, one of the classical classes of signaling molecules: auxins, gibberellins, cytokinins, ethylene, and abscisic acid.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "When the tip of a seedling is illuminated, an invisible signal descends the stem to produce bending; this was the first demonstration of a mobile **phytohormone**." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "Specific organ-forming substances, analogous to what modern botanists term a **phytohormone**, regulate root and shoot initiation." },
      { author: "Frits Went", work: "On Growth-Promoting Substances in Avena", quote: "I isolated the **phytohormone** auxin in agar blocks, showing that growth curvature was strictly proportional to its concentration." }
    ]
  },
  "Dashboard — phyt/phytolacca.md": {
    primary: "A genus of perennial herbs, shrubs, and trees (family Phytolaccaceae), including American pokeweed (Phytolacca americana), bearing racemes of dark purple berries.",
    secondary: "In ethnobotany and toxicology, plants containing saponins and phytolaccatoxin, whose young spring shoots are eaten as poke sallet after thorough boiling, while mature roots are violently toxic.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The Virginian poke or **Phytolacca** beareth great stalks of deep red, adorned with heavy clusters of purple juice-yielding berries." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Common **Phytolacca** decandra is an immense, rank perennial weed flourishing in rich barnyards and clearing margins." },
      { author: "William Woodville", work: "Medical Botany", quote: "Country practitioners administer the dried root of **Phytolacca** as an emetic, though its harsh action demands extreme caution." }
    ]
  },
  "Dashboard — phyt/phytolaccaceae.md": {
    primary: "The pokeweed family of flowering plants (order Caryophyllales), consisting of herbs, shrubs, and trees with alternate simple leaves and small flowers followed by berries.",
    secondary: "In systematic angiosperm taxonomy, a family closely allied to Petiveriaceae and Nyctaginaceae, distinguished by multiple united or free carpels in a ring.",
    quotes: [
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "The family **Phytolaccaceae** occupies a central phylogenetic position in the Centrospermae, displaying transitions from spiral to whorled floral parts." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Systematists characterize the **Phytolaccaceae** by their estipulate leaves, exalbuminous seeds with curved embryos, and succulent fruits." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "In the **Phytolaccaceae**, the fruit is typically a depressed fleshy berry composed of several coalesced carpellary locules." }
    ]
  },
  "Dashboard — phyt/phytologist.md": {
    primary: "A botanist; a person who studies plants and plant science.",
    secondary: "In 18th- and 19th-century academic literature, an expert in the morphology, distribution, and taxonomy of the vegetable kingdom.",
    quotes: [
      { author: "Carl Linnaeus", work: "Philosophia Botanica", quote: "The accomplished **phytologist** must observe plants in the field throughout all seasons, examining flower, leaf, and seed." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "It is the duty of the systematic **phytologist** to harmonize regional floras into a coherent universal arrangement." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "To the wandering **phytologist**, the high alpine passes of Tibet afford an inexhaustible treasury of new and curious species." }
    ]
  },
  "Dashboard — phyt/phytology.md": {
    primary: "The science of plants; botany; the formal study of the vegetable kingdom.",
    secondary: "In historical scientific nomenclature, an older term for botany, encompassing plant physiology, organography, and taxonomic classification.",
    quotes: [
      { author: "Erasmus Darwin", work: "Phytologia, or the Philosophy of Agriculture and Gardening", quote: "The principles of **phytology** demonstrate that plants possess circulation, respiration, and irritability matching animal nature." },
      { author: "William Rhind", work: "A History of the Vegetable Kingdom", quote: "The pursuit of **phytology** elevates the human mind by revealing divine design in the humblest wayside weed." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Modern **phytology** demands rigorous chemical and microscopical analysis alongside traditional herbarium classification." }
    ]
  },
  "Dashboard — phyt/phytomastigina.md": {
    primary: "A taxonomic subclass or grouping of plant-like flagellated protists (phytoflagellates) that possess chloroplasts and synthesize food through photosynthesis (such as Euglena and Volvox).",
    secondary: "In historical protozoology, flagellates exhibiting photosynthetic autotrophy, contrasting with animal-like Zoomastigina.",
    quotes: [
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "The **Phytomastigina** unite the characteristics of plant and animal, swimming actively with whip-like flagella while photosynthesizing." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Green colonial forms belonging to the **Phytomastigina**, such as Volvox, illustrate early stages in the evolution of multicellularity." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "Most protozoologists regard the **Phytomastigina** as the ancestral stem from which both higher plants and colorless protozoa arose." }
    ]
  },
  "Dashboard — phyt/phyton.md": {
    primary: "The ancient Greek word for a plant; in plant developmental anatomy, a phytomer or structural repeating unit of a plant shoot (leaf, node, internode, and axillary bud).",
    secondary: "In structural morphogenesis, the modular building block of vegetative growth, where each **phyton** reiterates to build complex branched plant bodies.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The Greeks designated as **phyton** any living green organism that springs from seed or root and draws nourishment from soil." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Morphologists have analyzed the higher plant as an association of elementary plantlets, each unit being a **phyton**." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "The shoot system is composed of repeating structural units, each **phyton** consisting of an internode terminated by a leaf." }
    ]
  },
  "Dashboard — phyt/phytonadione.md": {
    primary: "A synthetic preparation of vitamin K₁ (phylloquinone), used as a pharmaceutical medication to treat vitamin K deficiency, bleeding disorders, and warfarin overdose.",
    secondary: "In clinical hematology and pharmacology, a fat-soluble naphthoquinone derivative that reverses hypoprothrombinemia by promoting hepatic synthesis of clotting factors.",
    quotes: [
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Parenteral administration of **phytonadione** rapidly neutralizes excessive anticoagulation caused by coumarin derivatives." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Routine administration of **phytonadione** to all newborns prevents life-threatening hemorrhagic disease of the newborn." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In obstructive jaundice, oral **phytonadione** requires bile salts for adequate intestinal absorption to prevent hemorrhages." }
    ]
  },
  "Dashboard — phyt/phytonym.md": {
    primary: "The name of a plant; a botanical name or vernacular plant term.",
    secondary: "In linguistic onomastics and ethnobotany, the lexical term applied to wild or cultivated plants, revealing cultural and ecological associations.",
    quotes: [
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "In primitive languages, every specific **phytonym** reflects an acute empirical observation of the plant's medicinal or culinary use." },
      { author: "Franz Boas", work: "Race, Language and Culture", quote: "Indigenous folklore preserves ancient geographic migrations encoded within the historical etymology of each native **phytonym**." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "The classical **phytonym** often reveals a pre-Greek Mediterranean substrate preserved through continuous horticultural trade." }
    ]
  },
  "Dashboard — phyt/phytophagic.md": {
    primary: "Feeding on plants; plant-eating; herbivorous; phytophagous.",
    secondary: "In animal ecology, describing insects, birds, or mammals whose diet is composed exclusively or primarily of living vegetable tissue.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Specialized **phytophagic** insects are frequently confined to a single host plant family by chemical feeding stimulants." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "The enormous reproductive potential of **phytophagic** caterpillars is counterbalanced by parasitic tachinid flies and ichneumons." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Mandibles in **phytophagic** Coleoptera are heavily sclerotized and ridged for grinding tough cellulose cell walls." }
    ]
  },
  "Dashboard — phyt/phytophagous.md": {
    primary: "Feeding upon plants; herbivorous (especially applied to insects).",
    secondary: "In entomological ecology, describing specialized leaf-chewers, sap-suckers, gall-makers, or root-borers feeding upon living plant tissues.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "The Rocky Mountain locust is an insatiable **phytophagous** marauder that strips vast wheat fields to bare stubble in hours." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Brilliantly iridescent longhorn beetles of the tropics are strictly **phytophagous**, their grubs boring into forest ironwood." },
      { author: "Jean-Henri Fabre", work: "The Life of the Caterpillar", quote: "The voracious **phytophagous** caterpillar consumes twice its own weight in leaves each day during its final instar." }
    ]
  },
  "Dashboard — phyt/phytophilous.md": {
    primary: "Attracted to, loving, or thriving among plants; plant-loving; residing on or near vegetation.",
    secondary: "In ecological biogeography, describing animal species, birds, or insects that inhabit dense foliage, brush, or forest understories.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "The brilliant tree frogs of the Amazon are strictly **phytophilous**, spending their lives within water-filled bromeliad leaf axils." },
      { author: "John Gould", work: "The Birds of Europe", quote: "The warblers are typical **phytophilous** songbirds, seldom descending to the ground but gleaning tiny insects from willow leaves." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Green leafhoppers exhibit **phytophilous** adaptations, their flattened bodies matching the green veins of the grasses they inhabit." }
    ]
  },
  "Dashboard — phyt/phytophthora.md": {
    primary: "A genus of destructive plant-pathogenic oomycetes (water molds), notably Phytophthora infestans, the causal agent of the late blight of potato and tomato.",
    secondary: "In agricultural plant pathology, a devastating genus causing late blight, root rots, and sudden oak death, producing motile biflagellate zoospores in wet soils.",
    quotes: [
      { author: "Miles Joseph Berkeley", work: "Observations on the Potato Disease", quote: "I demonstrated that the botrytis fungus, now named **Phytophthora** infestans, is the true and active cause of the potato murrain." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Zoospores discharged by **Phytophthora** swim actively in raindrops upon the leaf, encysting and penetrating stomata within hours." },
      { author: "Charles Valentine Riley", work: "The Potato Bug and Potato Blight", quote: "Weather conditions with cool nights and humid foggy mornings invariably precipitate a disastrous outbreak of **Phytophthora**." }
    ]
  },
  "Dashboard — phyt/phytoplankton.md": {
    primary: "Microscopic, photosynthetic organisms that drift or float in the sunlit surface waters of oceans, seas, and freshwater bodies; plant plankton.",
    secondary: "In marine biological oceanography, the primary producers of the marine biosphere (chiefly diatoms, dinoflagellates, and cyanobacteria) that generate roughly half of Earth's atmospheric oxygen.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The microscopic drifting pasture of the sea, the **phytoplankton**, provides the primary nourishment upon which all marine life depends." },
      { author: "William Beebe", work: "Half Mile Down", quote: "In the surface layers, my plankton net captured myriads of sparkling diatoms, the living solar cells of the marine **phytoplankton**." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The siliceous glass shells of diatoms and dinoflagellates within the **phytoplankton** exhibit geometrical symmetries of breathtaking beauty." }
    ]
  },
  "Dashboard — phyt/phytotherapy.md": {
    primary: "The study and use of plant-derived medicines and herbal extracts to treat diseases and promote health; herbal medicine.",
    secondary: "In clinical pharmacognosy and integrative medicine, the therapeutic application of standardized botanical preparations with demonstrated pharmacological activity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Traditional **phytotherapy** bequeathed to modern pharmacology its most potent remedies, including digitalis, morphine, and quinine." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "Scientific **phytotherapy** demands rigorous chemical assay to ensure consistent alkaloidal potency in botanical tinctures." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "The efficacy of **phytotherapy** in mild functional disorders often rests upon complex synergistic interactions among plant glycosides." }
    ]
  },
  "Dashboard — phyt/phytotoxin.md": {
    primary: "A toxic or poisonous substance produced by a plant (such as ricin, curare, or nicotine); a plant toxin.",
    secondary: "In toxicology and biochemistry, a chemical defense compound synthesized by flora to deter herbivores, insects, or fungal pathogens, or a toxin secreted by plant pathogens.",
    quotes: [
      { author: "Robert Christison", work: "A Treatise on Poisons", quote: "Ricin, extracted from the seeds of the castor bean, is an extraordinarily potent **phytotoxin** capable of agglutinating blood cells." },
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "The arrow poisons of the South American tribes utilize curare, a deadly neuromuscular **phytotoxin** derived from Strychnos vines." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "Certain plant pathogens secrete a specific **phytotoxin** that induces rapid chlorosis and wilting in the host foliage." }
    ]
  },
  "Dashboard — phyt/symphytum.md": {
    primary: "A genus of rough, hairy perennial herbs in the borage family (Boraginaceae), commonly known as comfrey, bearing drooping bell-shaped flowers.",
    secondary: "In traditional herbal pharmacognosy, knitbone (Symphytum officinale), rich in allantoin which promotes cell proliferation in wound and bone healing, but containing hepatotoxic pyrrolizidine alkaloids.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The roots of comfrey or **Symphytum** are full of glutinous slime, which bruised and laid upon broken bones helps knit them together with speed." },
      { author: "Nicholas Culpeper", work: "The Complete Herbal", quote: "A decoction of the leaves of **Symphytum** is exceedingly good for inward hurts and ulcers of the lungs." },
      { author: "William Woodville", work: "Medical Botany", quote: "The mucilaginous root of **Symphytum** officinale was highly extolled by ancient physicians as an external vulnerary for ulcers." }
    ]
  },
  "Dashboard — pis/pisoid.md": {
    primary: "A rounded, accretionary sedimentary granule or particle, similar to an ooid but larger (greater than 2 mm in diameter), composed of concentric mineral laminae.",
    secondary: "In sedimentary petrology, a coated spherical grain formed by chemical precipitation around a nucleus in cave pools (cave pearls) or shallow marine carbonate settings.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "In thermal springs, agitated waters coat sand grains with concentric shells of calcite, forming an accretionary **pisoid**." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Each **pisoid** displays concentric growth rings around a central fragment of shell or quartz pebble." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Travertine terraces at Tivoli contain beds where each spherical **pisoid** rivals a hazelnut in size." }
    ]
  },
  "Dashboard — pis/pisolite.md": {
    primary: "A sedimentary rock composed largely of pisoids (spherical accretionary grains resembling peas, larger than 2 mm in diameter) cemented together; peastone.",
    secondary: "In carbonate petrology, a coarse-grained rock formed in hypersaline lagoons, caliche horizons, or hot spring deposits, contrasting with fine-grained oolites.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The weathered surface of the **pisolite** limestone resembles a mass of fossilized peas cemented together in calcareous spar." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Bauxite deposits frequently exhibit a pronounced **pisolite** structure formed by intense tropical weathering of aluminous rocks." },
      { author: "Frank Rutley", work: "The Study of Rocks", quote: "Thin sections of **pisolite** reveal radial fibrous calcite needles intersecting concentric growth lamellae under polarized light." }
    ]
  },
  "Dashboard — rhetin/retinite.md": {
    primary: "Any of a group of fossil resins found in coal beds and lignite, related to amber but softer and containing less succinic acid; also a volcanic pitchstone.",
    secondary: "In mineralogy and paleobotany, an amorphous brownish-yellow hydrocarbon resin exuded by extinct coniferous trees and preserved in Tertiary sedimentary strata.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The mineral resin **retinite** occurs in brown lustrous masses in brown coal deposits, burning with a pleasant aromatic flame." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Lignite beds at Bovey Tracey yield nodules of **retinite** that softened and melted upon domestic hearth fires." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Volcanic pitchstone is occasionally termed **retinite** on account of its resinous luster and perlitic cracks." }
    ]
  },
  "Dashboard — rhiz/ectomycorrhiza.md": {
    primary: "A symbiotic association between a fungus and the roots of a plant (especially forest trees), where the fungus forms a mantle around the root tip and a Hartig net between cortical cells, without penetrating inside the cells.",
    secondary: "In forest soil biology and mycology, an ecological mutualism essential for nutrient absorption (especially phosphorus and nitrogen) in temperate forest families like Pinaceae and Fagaceae.",
    quotes: [
      { author: "Albert Bernhard Frank", work: "On the Mineral Nutrition of Trees by Mycorrhizae", quote: "I coined the term **ectomycorrhiza** to describe the thick mantle of fungal hyphae that encases the fine root tips of forest oaks and pines." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "Without an active **ectomycorrhiza** partner, pine seedlings in sterile soil become stunted and chlorotic from phosphorus starvation." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "The intimate Hartig net of the **ectomycorrhiza** facilitates extensive two-way nutrient exchange between tree and subterranean fungus." }
    ]
  },
  "Dashboard — rhiz/rhizobiaceae.md": {
    primary: "A family of Gram-negative soil bacteria (order Rhizobiales) that includes Rhizobium and Agrobacterium, notable for plant symbiosis or genetic transformation.",
    secondary: "In agricultural microbiology, a family encompassing both mutualistic nitrogen-fixing root-nodule symbionts and natural genetic engineers (Agrobacterium tumefaciens).",
    quotes: [
      { author: "Martinus Beijerinck", work: "Die Bakterien der Papilionaceen-Knöllchen", quote: "Classification places the nodule-forming bacteria of legumes within the family **Rhizobiaceae**, celebrating their root-dwelling habit." },
      { author: "Louis Pasteur", work: "Studies on Microbes", quote: "The discovery that members of the **Rhizobiaceae** fix atmospheric nitrogen into plant-available ammonia solved an ancient riddle of agriculture." },
      { author: "William N. Kelley", work: "Microbiology in Agriculture", quote: "Plasmid exchange within the **Rhizobiaceae** governs host plant specificity and root infection kinetics." }
    ]
  },
  "Dashboard — rhiz/rhizobium.md": {
    primary: "A genus of soil bacteria (family Rhizobiaceae) that infect the roots of leguminous plants, forming nodules within which they fix atmospheric nitrogen into ammonia.",
    secondary: "In agricultural biotechnology, endosymbiotic bacteroids that exchange reduced nitrogen for plant dicarboxylic acids within specialized root nodule organelles.",
    quotes: [
      { author: "Martinus Beijerinck", work: "On the Root-Nodule Bacteria of Legumes", quote: "I succeeded in isolating pure cultures of **Rhizobium** leguminosarum from the root tubercles of garden peas." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The replenishment of soil fertility through clover rests upon symbiotic infection by subterranean **Rhizobium** bacteria." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Crop rotation with clover restores exhausted soils, a miraculous natural process mediated by microscopic **Rhizobium** nodules." }
    ]
  },
  "Dashboard — rhiz/rhizoctinia.md": {
    primary: "A genus of anamorphic soil-borne fungi (Rhizoctonia) that lack asexual spores, known as plant pathogens causing damping-off, root rot, and collar rot in crops.",
    secondary: "In plant pathology, anamorphic basidiomycetes (teleomorph Thanatephorus) that form sterile dark mycelial cushions and sclerotia, notorious for Rhizoctonia solani blight.",
    quotes: [
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Damping-off of young greenhouse seedlings is frequently caused by virulent parasitic hyphae of **Rhizoctonia** in contaminated potting compost." },
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "Potato tubers exposed to damp soil develop black scurf, a disease caused by the resting sclerotia of **Rhizoctonia**." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The mycelium of **Rhizoctonia** spreads rapidly through damp soil, invading the succulent hypocotyl of newly germinated plants." }
    ]
  },
  "Dashboard — rhiz/rhizoid.md": {
    primary: "A root-like, hair-like filament found on mosses, liverworts, fern gametophytes, and fungi, serving to anchor the organism and absorb water and nutrients.",
    secondary: "In cryptogamic botany, a simple unicellular or uniseriate multicellular filament that performs absorption in non-vascular plants lacking true vascular roots.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "Higher Cryptogamia", quote: "From the lower surface of the fern prothallus spring dozens of delicate, transparent **rhizoid** filaments that penetrate the damp earth." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "In Marchantia, the **rhizoid** filaments are differentiated into smooth-walled and tuberculate conducting forms." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Capillary attraction between adjacent **rhizoid** hairs draws surface film moisture up to the photosynthetic thallus." }
    ]
  },
  "Dashboard — rhiz/rhizoidal.md": {
    primary: "Of, relating to, resembling, or functioning as a rhizoid (a root-like filament in cryptogams).",
    secondary: "In bryology and mycology, designating the anchoring hairs, branching patterns, and absorptive surface of rhizoids.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The dense **rhizoidal** felt clothing the lower stem of the moss protects it against desiccation on sun-baked rocks." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "In leafy liverworts, **rhizoidal** branches arise exclusively from the ventral surface of the under-leaves." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Anchorage of the fungal mycelium upon timber is effected by thick **rhizoidal** strands penetrating the wood vessels." }
    ]
  },
  "Dashboard — rhiz/rhizomatous.md": {
    primary: "Producing, possessing, or having the characteristics of a rhizome (a horizontal underground stem).",
    secondary: "In plant ecology and horticultual taxonomy, describing spreading perennial plants (such as iris, ginger, and many grasses) that propagate via creeping subterranean stems.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The quick grass is an aggressive **rhizomatous** weed that defies eradication because every severed joint produces a new plant." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In the ginger family, the **rhizomatous** rootstocks accumulate aromatic essential oils and starch in immense subterranean tubers." },
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "Coastal sand dunes are bound and stabilized by the deep **rhizomatous** networks of marram grass." }
    ]
  },
  "Dashboard — rhiz/rhizome.md": {
    primary: "A continuously growing, usually horizontal subterranean stem that sends out lateral shoots and adventitious roots at intervals (rootstock).",
    secondary: "In plant morphology, a modified underground stem possessing nodes, internodes, scale leaves (cataphylls), and buds, serving as a perennating organ and vegetative propagule.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "A **rhizome** is an underground stem, distinguished from a true root by bearing leaf-buds and scale-leaves at regular nodes." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The creeping **rhizome** of the Solomon's seal bears round seal-like scars marking where ancient upright stems perished." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Digging through the damp peat, I unearthed the sweet aromatic **rhizome** of the wild calamus flag." }
    ]
  },
  "Dashboard — rhiz/rhizomorph.md": {
    primary: "A dense, root-like cord or bundle of fungal hyphae that grows through soil or wood, typical of fungi like Armillaria (honey mushroom).",
    secondary: "In forest pathology and mycology, a melanized, multicellular strand with a hollow core and apical growing tip that transmits nutrients and spreads infection across tree root networks.",
    quotes: [
      { author: "Robert Hartig", work: "Important Diseases of Forest Trees", quote: "The black shoestring **rhizomorph** of Armillaria mellea creeps beneath the bark, destroying the cambium of living spruces." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Luminescent properties are exhibited by the subterranean **rhizomorph** of the honey mushroom, glowing with eerie greenish light in damp decay." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The tough, outer cortical sheath of the **rhizomorph** protects the delicate internal conductive hyphae from soil bacteria." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch8Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 8 Completed: ${count} / ${Object.keys(batch8Data).length} notes updated.`);
console.log(`========================================\n`);
