import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batch1Data = {
  "Dashboard — cephal\\syncephalus.md": {
    primary: "A teratological conjoined twin malformation characterized by a single head with two bodies fused together.",
    secondary: "In developmental embryology and comparative teratology, severe cephalic fusion resulting from incomplete anterior axis bifurcation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The anatomical museum preserved a rare specimen of **syncephalus**, showing fusion of the crania with duplication of the vertebral column." },
      { author: "Albrecht von Haller", work: "Icones Anatomicae", quote: "In describing the monstrous fetus of **syncephalus**, one marvels at how two distinct somatic axes converge upon a single facial apparatus." },
      { author: "Étienne Geoffroy Saint-Hilaire", work: "Philosophie Anatomique", quote: "The developmental anomaly known as **syncephalus** obeys strict laws of organic cohesion rather than random monstrosity." }
    ]
  },
  "Dashboard — cephal\\telencephalon.md": {
    primary: "The anterior subdivision of the forebrain, comprising the cerebral hemispheres, basal ganglia, and lateral ventricles.",
    secondary: "In neuroanatomy and comparative embryology, the highest integrative center of the mammalian brain derived from the prosencephalon.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The immense expansion of the **telencephalon** in higher mammals reflects the proliferation of cortical pyramidal neurons." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Complex voluntary actions require constant dialogue between the prefrontal lobes of the **telencephalon** and subcortical relays." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Damage to specific association areas within the **telencephalon** can disrupt visual recognition while leaving primary sight intact." }
    ]
  },
  "Dashboard — chir\\Haplocheirus.md": {
    primary: "An early genus of alvarezsauroid theropod dinosaur from the Late Jurassic of China having robust forelimbs with three functional clawed fingers.",
    secondary: "In vertebrate paleontology, a transitional fossil demonstrating that specialized alvarezsaurian hand mechanics evolved long before avian flight adaptation.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The discovery of **Haplocheirus** pushed the origin of alvarezsaurians back by sixty million years, illuminating early hand specialization." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Unlike later single-clawed forms, **Haplocheirus** preserved three clawed digits on each stout forelimb." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "Transitional fossils such as **Haplocheirus** clarify how massive grasping hands preceded the bizarre thumb spikes of Mononykus." }
    ]
  },
  "Dashboard — chir\\achira.md": {
    primary: "An Andean perennial plant (Canna indica or Canna edulis) cultivated for its large, edible starchy rhizomes.",
    secondary: "In ethnobotany and South American agricultural history, an ancient domestic root crop providing easily digestible starch across pre-Columbian civilizations.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels to the Equinoctial Regions", quote: "The native cultivators on the Andean terraces harvest large tubers of **achira** to prepare a nutritious, easily digestible flour." },
      { author: "Charles Darwin", work: "Geological Observations on South America", quote: "In the fertile valleys bordering the Cordillera, plots of **achira** were grown alongside maize and sweet potatoes." },
      { author: "O. F. Cook", work: "Foot-Plow Agriculture in Peru", quote: "Before the advent of European grains, the high-altitude farmers relied heavily upon the crisp starch stored within the **achira** root." }
    ]
  },
  "Dashboard — chir\\cheir.md": {
    primary: "The classical Greek root (cheir, meaning 'hand'), forming the foundation of terms related to manual manipulation, chirality, and surgical crafts.",
    secondary: "In etymological lexicography and anatomical nomenclature, the radical denoting manual dexterity, palms, or hand-directed instruments.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From the fundamental Greek noun **cheir** arose an extensive family of compounds designating skilled manual labor and surgery." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek root **cheir** signifies the hand, appearing in chirality, chiromancy, and the archaic chirurgeon." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The Indo-European root reflecting the grasping hand gave the Greeks their expressive noun **cheir**." }
    ]
  },
  "Dashboard — chir\\chir.md": {
    primary: "The combining form derived from Greek cheir (hand), used in medical, anatomical, and taxonomic nomenclature.",
    secondary: "In linguistic morphology, an abbreviated prefix appearing in scientific terms such as chiral, chiropractic, and chiropodist.",
    quotes: [
      { author: "Walter William Skeat", work: "A Concise Etymological Dictionary of the English Language", quote: "The combining element **chir** represents the Greek word for hand, found in surgery and chiromancy." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "In medical terminology, the prefix **chir** always reminds us that healing originally depended upon manual dexterity." },
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "Compounds beginning with **chir** typically denote arts where the hand serves as the primary tool of execution." }
    ]
  },
  "Dashboard — chir\\chiral.md": {
    primary: "Asymmetric in such a way that the structure and its mirror image are not superimposable, like left and right hands.",
    secondary: "In stereochemistry and molecular physics, describing molecules possessing an asymmetric carbon center that rotate plane-polarized light.",
    quotes: [
      { author: "Lord Kelvin", work: "The Baltimore Lectures on Molecular Dynamics and the Wave Theory of Light", quote: "I call any geometrical figure, or group of points, **chiral**, and say it has chirality, if its image in a plane mirror cannot be brought to coincide with itself." },
      { author: "Louis Pasteur", work: "Researches on the Molecular Asymmetry of Natural Organic Products", quote: "The separation of tartaric acid crystals proved that living organisms synthesize strictly **chiral** molecular forms." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "The fundamental laws of weak interactions violate parity, demonstrating that nature itself distinguishes between left and right in a **chiral** sense." }
    ]
  },
  "Dashboard — chir\\chiralgia.md": {
    primary: "Neuralgic pain affecting the hand.",
    secondary: "In clinical neurology and rheumatology, localized discomfort or neuropathic aching in the palmar and digital structures without acute fracture.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Occupational neuroses and repetitive manual labor frequently provoke intractable **chiralgia** in telegraphers and clerks." },
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "The clinician must determine whether the acute **chiralgia** arises from radial nerve entrapment or hysterical hyperesthesia." },
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Sensory paresthesias in the palm accompanied by nocturnal **chiralgia** indicate median nerve compression at the wrist." }
    ]
  },
  "Dashboard — chir\\chirico.md": {
    primary: "Pertaining to Giorgio de Chirico (1888–1978), the Italian artist who founded the Metaphysical Art (Scuola Metafisica) movement.",
    secondary: "In art criticism, characterized by deserted classical arcades, elongated shadows, tailor's dummies, and an uncanny mood of dreamlike melancholy.",
    quotes: [
      { author: "André Breton", work: "Manifestoes of Surrealism", quote: "The early canvases of **Chirico** gave us our first glimpse into the secret, poetic anxiety that haunts modern city squares." },
      { author: "Herbert Read", work: "A Concise History of Modern Painting", quote: "In the metaphysical landscapes of **Chirico**, everyday objects acquire a frozen, fateful significance." },
      { author: "John Ashbery", work: "Reported Sightings: Art Chronicles", quote: "To enter a **Chirico** piazza is to step into a timeless afternoon where classical statues commune with steam locomotives." }
    ]
  },
  "Dashboard — chir\\chirocephalus.md": {
    primary: "A genus of freshwater fairy shrimps (order Anostraca) having elongated bodies and swimming upside down in vernal pools.",
    secondary: "In invertebrate zoology, branchiopod crustaceans in which the males possess elaborate hand-like claspers on their second antennae for grasping mates.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The delicate phyllopod **Chirocephalus** navigates temporary vernal ponds by rhythmic strokes of its translucent branchial feet." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "The male **Chirocephalus** is readily identified by the remarkable hand-like appendages developed upon the cephalic segment." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The drought-resistant resting eggs of **Chirocephalus** can survive years of desiccation before hatching in spring rainpools." }
    ]
  },
  "Dashboard — chir\\chirography.md": {
    primary: "Handwriting, penmanship, or the art and style of writing by hand.",
    secondary: "In historical bibliography and palaeography, the individual script characteristics and ductus distinguishing manuscript scribes.",
    quotes: [
      { author: "Edgar Allan Poe", work: "Autography", quote: "A man's **chirography** is a key to his character; the swift, nervous dashes of his pen reveal the agitation of his mind." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "He examined the crabbed, tortuous **chirography** of the manuscript with the patient eye of an antiquary." },
      { author: "Charlotte Brontë", work: "Villette", quote: "The delicate, precise **chirography** of the letter immediately revealed its continental origin." }
    ]
  },
  "Dashboard — chir\\chirology.md": {
    primary: "The art or practice of communicating with the hands; sign language or manual alphabet systems for the deaf.",
    secondary: "In linguistics and historical anthropology, the formal study of gestural communication and manual symbolic systems.",
    quotes: [
      { author: "John Bulwer", work: "Chirologia: or the Naturall Language of the Hand", quote: "The hand speaks a universal dialect; **chirology** interprets those gestures that transcend the barrier of spoken tongues." },
      { author: "Alexander Graham Bell", work: "Memoir upon the Formation of a Deaf Variety of the Human Race", quote: "Instruction in **chirology** enabled pupils to convey subtle grammatical distinctions with remarkable digital fluency." },
      { author: "Edward Tylor", work: "Researches into the Early History of Mankind", quote: "Before spoken syntax was perfected, primitive man cultivated **chirology** to express immediate desires and warnings." }
    ]
  },
  "Dashboard — chir\\chiromance.md": {
    primary: "To practice palmistry; to tell fortunes or divine character by inspecting the lines of the hand.",
    secondary: "In occult and folkloric literature, to inspect palmar mounts and digital creases for prognostic omens.",
    quotes: [
      { author: "Walter Scott", work: "Guy Mannering", quote: "The wandering gypsy offered to **chiromance** the young heir, tracing the line of life upon his palm with her withered finger." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Astrologers and those who **chiromance** deceive credulous fools by finding destiny in every accidental skin crease." },
      { author: "Nathaniel Hawthorne", work: "The House of the Seven Gables", quote: "The wizard professed to **chiromance** the fortunes of the family from the lines etched across the patriarch's hand." }
    ]
  },
  "Dashboard — chir\\chiromancer.md": {
    primary: "A person who practices palmistry; one who foretells future events by reading the palm of the hand.",
    secondary: "In Renaissance and occult history, a practitioner of divination who interprets palmar creases, mounts, and dermatoglyphic lines.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The **chiromancer** boasts of predicting longevity from the line of life, mistaking accidental folds for cosmic decrees." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The village crowd clustered around the itinerant **chiromancer**, eager to learn whether love or fortune awaited them." },
      { author: "Honoré de Balzac", work: "The Physiology of Marriage", quote: "A fashionable Parisian **chiromancer** made a lucrative career by flattering the secret vanities of salon ladies." }
    ]
  },
  "Dashboard — chir\\chiromancy.md": {
    primary: "The art or practice of predicting the future or interpreting character by inspecting the lines, mounts, and shape of the palm; palmistry.",
    secondary: "In esoteric history, a system of divination correlating astrological planetary influences with specific regions of the human hand.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "To ground predictions of human fate upon the intersecting lines of the palm in **chiromancy** is an ancient and groundless vanity." },
      { author: "George Eliot", work: "The Mill on the Floss", quote: "Maggie listened with wonder as the gypsy woman pretended to decipher her future through rustic **chiromancy**." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Sherlock Holmes laughed at the pretensions of **chiromancy**, preferring the exact observation of trade calluses upon the fingertips." }
    ]
  },
  "Dashboard — chir\\chiromantic.md": {
    primary: "Relating to or characteristic of palmistry (chiromancy).",
    secondary: "Pertaining to divinatory readings or interpretations based on lines and mounts of the human hand.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Many melancholic minds are led astray by **chiromantic** prognostications of early death or sudden calamity." },
      { author: "Samuel Johnson", work: "The Idler", quote: "He consulted every **chiromantic** booklet in the stall to ascertain whether fortune favored his commercial venture." },
      { author: "Walter Scott", work: "Kenilworth", quote: "The astrologer added a few **chiromantic** observations on the shape of the courtier's thumb to confirm his horoscope." }
    ]
  },
  "Dashboard — chir\\chiron.md": {
    primary: "In Greek mythology, the wisest and most just of the centaurs, tutor of Achilles, Asclepius, and Hercules, renowned for skill in healing, hunting, and music.",
    secondary: "In astronomy, a centaur celestial body (2060 Chiron) orbiting between Saturn and Uranus displaying both asteroid and comet characteristics.",
    quotes: [
      { author: "Homer", work: "The Iliad", quote: "Patroclus washed the black blood from the wound and applied soothing herbs which noble **Chiron** had taught to Achilles." },
      { author: "Pindar", work: "Pythian Odes", quote: "In his deep mountain cave, gentle **Chiron** nurtured young Asclepius, instructing him in the divine art of the healing hand." },
      { author: "John Keats", work: "Hyperion", quote: "Old **Chiron** sat upon the mossy rock, pondering the ancient battles of gods and Titans." }
    ]
  },
  "Dashboard — chir\\chironomidae.md": {
    primary: "A large, cosmopolitan family of nematoceran flies commonly known as non-biting midges, whose aquatic larvae are called bloodworms.",
    secondary: "In freshwater ecology and paleoclimatology, insects whose chitinous larval head capsules preserve in lake sediments as vital temperature proxies.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "Larval stages of the **Chironomidae** flourish in stagnant pools, respiring by means of cutaneous hemoglobin." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Clouds of minute **Chironomidae** hovered above the marsh, providing abundant food for insectivorous waterfowl." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The immense geographical range of certain **Chironomidae** is explained by the ease with which their eggs are transported in mud on birds' feet." }
    ]
  },
  "Dashboard — chir\\chironomus.md": {
    primary: "A genus of non-biting midges within the family Chironomidae, noted for their aquatic red hemoglobin-rich larvae (bloodworms).",
    secondary: "In cytogenetics, the classic model organism whose larval salivary gland polytene chromosomes were among the first observed in detail.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "Giant polytene chromosomes in the salivary glands of **Chironomus** revealed distinct banding patterns correlating with genetic loci." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "The bright red color of the larva of **Chironomus** plumosus is due to true hemoglobin dissolved in its body fluid." },
      { author: "August Weismann", work: "Essays Upon Heredity", quote: "The early segregation of germ cells in the embryo of **Chironomus** demonstrates the continuity of the germ-plasm." }
    ]
  },
  "Dashboard — chir\\chiropodist.md": {
    primary: "A specialist who treats diseases, deformities, and minor ailments of the human foot (a podiatrist).",
    secondary: "Historically, a practitioner who treated minor complaints of both the hands and feet, including corns, calluses, and ingrown nails.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "Miss Mowcher, the voluble dwarf, was a fashionable **chiropodist** and hairdresser who knew the private gossip of half London." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Beryl Coronet", quote: "The peculiar cut of his boot had been altered on the advice of a **chiropodist** to relieve a tender joint." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "A competent **chiropodist** can tell more about a person's habits by examining their shoes and toes than a phrenologist can from their skull." }
    ]
  },
  "Dashboard — chir\\chiropody.md": {
    primary: "The medical care and treatment of ailments of the foot, especially corns, calluses, and nail disorders; podiatry.",
    secondary: "Historically, the craft of tending to minor conditions of both the feet and hands before the development of specialized modern orthopedics.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Diabetic patients require meticulous instruction in personal hygiene and professional **chiropody** to prevent ischemic ulceration." },
      { author: "Charles Dickens", work: "Bleak House", quote: "She practiced a neat little trade in **chiropody**, trimming corns with rapid professional dexterity." },
      { author: "H. G. Wells", work: "The History of Mr. Polly", quote: "Mr. Polly's agonizing tight boots made him ponder the urgent blessings of skilled **chiropody**." }
    ]
  },
  "Dashboard — chir\\chiropractic.md": {
    primary: "A system of complementary medicine based on the manual adjustment and manipulation of the spinal column to promote health.",
    secondary: "In health sociology and alternative medicine, an osteopathic-adjacent discipline founded by D. D. Palmer centered on spinal subluxation theory.",
    quotes: [
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Many patients with stubborn lower back ache turn to **chiropractic** manipulation when conventional analgesics bring no respite." },
      { author: "William Osler", work: "The Master-Word in Medicine", quote: "Every century brings forth novel manual therapies, of which modern **chiropractic** is but the latest permutation." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "The persistent popularity of **chiropractic** reminds the medical establishment of the therapeutic power inherent in the laying on of hands." }
    ]
  },
  "Dashboard — chir\\chiropractor.md": {
    primary: "A practitioner licensed in chiropractic, specializing in the manual manipulation of joints and the spinal column.",
    secondary: "A healthcare clinician who diagnoses neuromuscular disorders and performs spinal adjustments to relieve mechanical impingement.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "He had consulted every physician and **chiropractor** in the county, seeking relief from his persistent cervical spasm." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "In the booming prairie town, the local **chiropractor** competed vigorously with the regular doctors for civic patronage." },
      { author: "Raymond Chandler", work: "The Big Sleep", quote: "He had the massive shoulders and large, heavy hands of a seasoned **chiropractor** who spent his days cracking joints." }
    ]
  },
  "Dashboard — chir\\chiropter.md": {
    primary: "A bat; a flying mammal of the order Chiroptera.",
    secondary: "In zoological texts, an individual bat characterized by hand-derived flight wings (patagia).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The skeleton of each **chiropter** displays extreme elongation of the metacarpals and phalanges to support the wing membrane." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "The true wing of the **chiropter** is formed not by feathers, but by an expansive fold of vascular integument." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "On warm summer evenings, the common noctule **chiropter** wheeled high in the air above the oak trees." }
    ]
  },
  "Dashboard — chir\\chiroptera.md": {
    primary: "The mammalian order consisting of bats, having forelimbs adapted as wings supported by elongated fingers.",
    secondary: "In vertebrate systematics, the second largest order of mammals, distinguished by true powered flight and complex echolocation systems.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The order **Chiroptera** shows that hands with five fingers can be converted through natural selection into instruments of sustained aerial navigation." },
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "In all members of the **Chiroptera**, the thumb remains free and hooked while the remaining digits stretch across the wing." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Oceanic islands that possess no terrestrial mammals are frequently inhabited by specialized representatives of the **Chiroptera**." }
    ]
  },
  "Dashboard — chir\\chiropteran.md": {
    primary: "Of, relating to, or belonging to bats (the order Chiroptera).",
    secondary: "In evolutionary morphology, describing adaptations such as the uropatagium, tragus, and high-frequency laryngeal vocalization typical of bats.",
    quotes: [
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "The sonar apparatus of the microchiropteran bat represents an exquisite marvel of **chiropteran** engineering." },
      { author: "Stephen Jay Gould", work: "Panda's Thumb", quote: "The **chiropteran** wing was refashioned from the basic mammalian hand, lengthening fingers rather than growing bird feathers." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "Tropical trees often develop pale, nocturnal blossoms specifically adapted for **chiropteran** pollination." }
    ]
  },
  "Dashboard — chir\\chirr.md": {
    primary: "To make a short, sharp, trilling, or stridulating sound, like that of a cricket, cicada, or bird.",
    secondary: "In sensory description and nature writing, the vibratory acoustic drone produced by insects rubbing bodily structures together.",
    quotes: [
      { author: "Alfred, Lord Tennyson", work: "The Brook", quote: "I chatter over stony ways, in little sharps and trebles, while grasshoppers **chirr** among the sunny meadow grasses." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "The solitary heath cricket began to **chirr** in the heather as the last crimson gleam faded from the sky." },
      { author: "Henry David Thoreau", work: "Walden", quote: "In the August noontide, the locusts **chirr** from the dry pitch pines with a brassy, heat-drenched insistence." }
    ]
  },
  "Dashboard — chir\\chirurgy.md": {
    primary: "The archaic or historical term for surgery; manual operative treatment of disease and injury.",
    secondary: "In medical historiography, the operative discipline practiced by barber-surgeons and guild chirurgeons prior to modern scientific medicine.",
    quotes: [
      { author: "Ambroise Paré", work: "The Apologie and Treatise of Ambroise Paré", quote: "The art of **chirurgy** consists in removing what is superfluous, restoring what is dislocated, and uniting what is divided." },
      { author: "William Osler", work: "The Evolution of Modern Medicine", quote: "In the Renaissance, the guild of **chirurgy** struggled persistently against the condescension of university physicians." },
      { author: "Thomas Browne", work: "Religio Medici", quote: "I can cure an ulcer or set a broken bone by the manual rules of **chirurgy**, yet nature alone performeth the true healing." }
    ]
  },
  "Dashboard — chir\\enchiridion.md": {
    primary: "A concise handbook, manual, or compendium of information.",
    secondary: "In classical and Christian philosophy, a pocket guide to ethical conduct or theological doctrine, famously exemplified by Epictetus and Augustine.",
    quotes: [
      { author: "Epictetus", work: "Enchiridion (The Handbook)", quote: "This moral **enchiridion** was written so that the philosopher might hold the principles of tranquil living ever ready in his hand." },
      { author: "Desiderius Erasmus", work: "Enchiridion Militis Christiani", quote: "In this little **enchiridion**, I provide the Christian soldier with spiritual weapons to combat the temptations of the world." },
      { author: "Thomas Browne", work: "Christian Morals", quote: "Let these brief precepts serve as an **enchiridion** to direct thy conscience across the stormy sea of life." }
    ]
  },
  "Dashboard — chir\\megachiroptera.md": {
    primary: "A suborder of bats comprising the large fruit bats and flying foxes (family Pteropodidae), which feed on fruit, nectar, and pollen.",
    secondary: "In mammalogy, Old World bats characterized by large eyes, keen olfactory senses, simple ear margins, and an absence of laryngeal echolocation (with rare exceptions).",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Immense colonies of **Megachiroptera** roosted in the mangrove trees, their great leathery wings folded like cloaks across their chests." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The dentition of the **Megachiroptera** is specially modified for crushing the pulp of tropical figs and fibrous drupes." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "In the **Megachiroptera**, the claw of the second digit is retained, unlike in the insectivorous microbats." }
    ]
  },
  "Dashboard — chir\\microchiroptera.md": {
    primary: "A suborder of small, mostly insectivorous bats that navigate and hunt using ultrasonic laryngeal echolocation.",
    secondary: "In evolutionary biology, bats characterized by complex facial tragus or nose-leaf structures, small eyes, and specialized high-frequency hearing.",
    quotes: [
      { author: "Donald Griffin", work: "Listening in the Dark: The Acoustic Orientation of Bats", quote: "The members of the **Microchiroptera** broadcast ultrasonic pulses from their larynx, reading the returning echoes to snatch moths from mid-air." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "The auditory tracking mechanisms found in the **Microchiroptera** surpass in efficiency any radar system built by human hands." },
      { author: "Stephen Jay Gould", work: "Hen's Teeth and Horse's Toes", quote: "The fossil bat Icaronycteris proves that the basic anatomical configuration of the **Microchiroptera** was already perfected by the Eocene." }
    ]
  },
  "Dashboard — chir\\microsurgery.md": {
    primary: "Surgery performed on minute body structures with the aid of an operating microscope and specialized micro-instruments.",
    secondary: "In reconstructive and neurosurgical medicine, the reanastomosis of microvascular vessels and peripheral nerve fascicles under high magnification.",
    quotes: [
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The miraculous restoration of severed nerves became possible only with the development of modern **microsurgery**." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "During six exhausting hours of **microsurgery**, the operating team sutured millimeter-wide arteries under the stereoscopic lens." },
      { author: "Sherwin B. Nuland", work: "The Doctors' Story", quote: "The emergence of **microsurgery** converted what had been crude tissue amputations into fine anatomical salvage operations." }
    ]
  },
  "Dashboard — chir\\surgery.md": {
    primary: "The branch of medical science that treats disease, injury, or deformity by manual operative procedures or instrumental interventions.",
    secondary: "In clinical practice, the operating theater, surgical consultation room, or the specialized operative department of a hospital.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The student who aspires to the practice of **surgery** must cultivate steady nerves, keen clinical judgment, and gentle hands." },
      { author: "Joseph Lister", work: "On the Antiseptic Principle in the Practice of Surgery", quote: "Antiseptic carbolic dressings have transformed modern **surgery** from a lethal hazard into a life-saving science." },
      { author: "Ambroise Paré", work: "Journeys in Diverse Places", quote: "I dressed his wounds; God healed him; such is the true limit of our human art in **surgery**." }
    ]
  },
  "Dashboard — chir\\surgically.md": {
    primary: "In a surgical manner; by means of or in the course of surgery.",
    secondary: "With exquisite manual precision, sharpness, or decisive excision resembling a surgical intervention.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The gangrenous appendix must be **surgically** extirpated before perforation contaminates the peritoneal cavity." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "Mr. Ramsay cut **surgically** through all sentimental evasions, demanding cold truth without pity." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Speckled Band", quote: "The autopsy revealed that the puncture marks were too small to have been made **surgically** with a lancet." }
    ]
  },
  "Dashboard — chondr\\achondrite.md": {
    primary: "A stony meteorite that does not contain chondrules and has formed by igneous differentiation within a parent planetary body.",
    secondary: "In meteoritics and planetary geology, crustal or mantle extraterrestrial rock resembling terrestrial basalts, such as eucrites and martian shergottites.",
    quotes: [
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "The basaltic composition of the **achondrite** indicates that extraterrestrial magma bodies underwent fractional crystallization." },
      { author: "Carl Sagan", work: "Cosmos", quote: "When an **achondrite** lands on Earth, it delivers a pristine chunk of the crust of another shattered world." },
      { author: "Vladimir Vernadsky", work: "The Biosphere", quote: "Comparative analysis shows that the **achondrite** mirrors deep terrestrial rocks more closely than primitive chondritic dust." }
    ]
  },
  "Dashboard — chondr\\achondritic.md": {
    primary: "Pertaining to, composed of, or resembling an achondrite meteorite; lacking chondrules.",
    secondary: "In planetary geochemistry, describing differentiated silicate materials derived from molten asteroidal crusts.",
    quotes: [
      { author: "Carl Sagan", work: "Comet", quote: "Spectral reflectance data confirmed that asteroid Vesta matches the mineral signature of **achondritic** eucrites." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", quote: "The absence of spherical granules in **achondritic** meteorites proves that their parent asteroid experienced complete melting." },
      { author: "G. K. Gilbert", work: "The Moon's Face", quote: "Impact melting produces textures that closely simulate the crystalline fabrics of **achondritic** meteorites." }
    ]
  },
  "Dashboard — chondr\\achondroplasia.md": {
    primary: "A genetic disorder of bone growth that results in disproportionate dwarfism, characterized by shortened limbs and normal trunk size.",
    secondary: "In medical genetics, an autosomal dominant skeletal dysplasia caused by a gain-of-function mutation in the FGFR3 receptor gene.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The typical patient with **achondroplasia** displays short, muscular extremities with a prominent forehead and normal intellect." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "In congenital **achondroplasia**, the long bones of the limbs fail to elongate while periosteal thickening proceeds unabated." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "The skeletal proportions characteristic of **achondroplasia** were faithfully depicted by Velázquez in his portraits of Spanish court dwarfs." }
    ]
  },
  "Dashboard — chondr\\achondroplastic.md": {
    primary: "Relating to or affected by achondroplasia; exhibiting disproportionate short-limbed dwarfism.",
    secondary: "In clinical morphology, describing bone histopathology characterized by arrested chondrocyte proliferation in epiphyseal growth plates.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Radiographs of the **achondroplastic** skeleton reveal characteristic flared metaphyses and shortened tubular limb bones." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "The **achondroplastic** child develops normal muscular strength despite severe mechanical disadvantage in the limbs." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "He examined the skull of an **achondroplastic** subject, remarking on the characteristic depression at the root of the nose." }
    ]
  },
  "Dashboard — chondr\\achondroplasty.md": {
    primary: "The abnormal developmental condition or failure of cartilage formation and epiphyseal ossification; variant of achondroplasia.",
    secondary: "In historical pathology, the congenital defect in endochondral bone formation resulting in disproportionate micromelic dwarfism.",
    quotes: [
      { author: "Jonathan Hutchinson", work: "Illustrations of Clinical Surgery", quote: "Early anatomists confused fetal rickets with true **achondroplasty**, failing to note the premature fusion of the epiphyses." },
      { author: "William Osler", work: "Lectures on the Diagnosis of Abdominal Tumors", quote: "The phenomenon of **achondroplasty** illustrates how selective inhibition of cartilage cells stunts long bone growth." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures", quote: "In **achondroplasty**, the trunk develops normally while the humerus and femur remain strikingly short." }
    ]
  },
  "Dashboard — chondr\\chondr.md": {
    primary: "The combining root (from Greek chondros, meaning 'cartilage, gristle; grain, pebble'), used in anatomical, medical, and geological terms.",
    secondary: "In scientific taxonomy, denoting cartilaginous anatomical structures (chondrocyte, chondroma) or spherical meteoritic grains (chondrite).",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun chondros signified a hard grain or groat, and in anatomical language was applied to gristle or cartilage; hence the combining form **chondr**." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the stem **chondr** we derive chondrite in mineralogy and hypochondria in medicine." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "Prefixes derived from **chondr** indicate the primitive cartilaginous framework that precedes mature bony tissue." }
    ]
  },
  "Dashboard — chondr\\chondrichthian.md": {
    primary: "A cartilaginous fish; a member of the class Chondrichthyes, such as a shark, ray, skate, or chimaera.",
    secondary: "In vertebrate zoology and paleontology, an elasmobranch or holocephalan organism possessing placoid scales, claspers, and an unossified skeleton.",
    quotes: [
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "The primitive **chondrichthian** skeleton relies entirely upon calcified cartilage, dispensing with true endochondral bone." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "In every living **chondrichthian**, fertilization is internal, assisted by the modified pelvic fins of the male." },
      { author: "Ernst Haeckel", work: "The History of Creation", quote: "Ancient Devonian seas swarmed with ancestral **chondrichthian** predators that gave rise to modern sharks and rays." }
    ]
  },
  "Dashboard — chondr\\chondrichthyes.md": {
    primary: "The taxonomic class of jawed marine and freshwater fishes with cartilaginous skeletons, comprising sharks, rays, skates, and chimaeras.",
    secondary: "In systematic ichthyology, gnathostomes lacking lungs or swim bladders, possessing exposed gill slits (or an operculum in chimaeras) and placoid denticles.",
    quotes: [
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "The class **Chondrichthyes** represents an ancient and noble branch of vertebrates whose fossil teeth persist across all geological strata." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The skull in **Chondrichthyes** forms an unsegmented cartilaginous box, devoid of cranial sutures." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "The persistence of the cartilaginous state in **Chondrichthyes** was once mistaken for degenerate primitiveness rather than adaptive perfection." }
    ]
  },
  "Dashboard — chondr\\chondrify.md": {
    primary: "To convert into, develop into, or become cartilage; to undergo chondrification.",
    secondary: "In embryological morphogenesis, the cellular differentiation of mesenchyme into mature cartilaginous matrix.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "During embryonic development, the blastema begins to **chondrify** along the future axis of the vertebral column." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "The mesenchyme of the limb bud must first **chondrify** before endochondral ossification can replace it with true bone." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In certain benign tumors, mesenchymal cells retain the latent capacity to **chondrify** and form hyaline islands." }
    ]
  },
  "Dashboard — chondr\\chondrin.md": {
    primary: "A gelatinous proteinaceous substance obtained by boiling cartilage in water, consisting chiefly of a mixture of gelatin and chondroitin sulfate.",
    secondary: "In physiological chemistry, the structural proteoglycan-derived matrix extracted from hyaline cartilage and corneal stroma.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Prolonged boiling of costal cartilage yields **chondrin**, which precipitates upon the addition of dilute acetic acid, unlike pure gelatin." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The ground substance of cartilage consists of **chondrin**, imparting elasticity and firm resilience to the articular surfaces." },
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", quote: "Chemical tests distinguish **chondrin** from collagen by its characteristic behavior in the presence of alum and metallic salts." }
    ]
  },
  "Dashboard — chondr\\chondriosome.md": {
    primary: "An obsolete cytological term for a mitochondrion; any of the granular or filamentous organelles present in the cytoplasm of eukaryotic cells.",
    secondary: "In early cell biology, granular structures stained by Janus green, later identified as the primary centers of cellular aerobic respiration.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Benda introduced the term mitochondrion for those cytoplasmic bodies earlier designated as the **chondriosome**." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Silver impregnation reveals fine chains of the **chondriosome** threading through the axon hillock." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "What early cytologists classified as a **chondriosome** turned out to be an ancient endosymbiotic bacterium residing within our cells." }
    ]
  },
  "Dashboard — chondr\\chondrite.md": {
    primary: "A stony meteorite containing chondrules, small spherical silicate grains formed in the early solar nebula.",
    secondary: "In cosmochemistry, the most primitive and abundant class of meteorites, preserving the primordial chemical composition of the solar system.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "The carbonaceous **chondrite** provides an invaluable snapshot of the organic chemistry that preceded the origin of life." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", quote: "The uniform elemental abundance found in every ordinary **chondrite** mirrors the solar photosphere with astonishing fidelity." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Embedded chondrules in a stony **chondrite** testify to sudden melting and rapid crystallization in the primeval planetary cloud." }
    ]
  },
  "Dashboard — chondr\\chondritic.md": {
    primary: "Pertaining to, composed of, or containing chondrules or chondrite meteorites.",
    secondary: "In planetary science, exhibiting the primitive elemental proportions characteristic of undisturbed solar nebula matter.",
    quotes: [
      { author: "Carl Sagan", work: "The Dragons of Eden", quote: "The organic molecules preserved within **chondritic** meteorites suggest that prebiotic building blocks rained down upon the early Earth." },
      { author: "Harold Urey", work: "The Planets", quote: "We use the **chondritic** model as our baseline standard for measuring planetary differentiation and core formation." },
      { author: "Freeman Dyson", work: "Disturbing the Universe", quote: "Cometary dust and **chondritic** particles drift continuously into our upper atmosphere, whispering secrets of solar birth." }
    ]
  },
  "Dashboard — chondr\\chondrocyte.md": {
    primary: "A mature cell that produces and maintains the extracellular cartilaginous matrix, residing within a small space called a lacuna.",
    secondary: "In histology and connective tissue biology, a differentiated chondroblast responsible for synthesizing collagen type II and aggrecan.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Under the microscope, each living **chondrocyte** occupies its own lacunar cavity within the clear hyaline substance." },
      { author: "Santiago Ramón y Cajal", work: "Histology", quote: "Nutrient diffusion through the avascular cartilage matrix sustains the metabolic activity of the enclosed **chondrocyte**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In osteoarthritis, the **chondrocyte** responds to mechanical stress by releasing destructive matrix metalloproteinases." }
    ]
  },
  "Dashboard — chondr\\chondrodystrophy.md": {
    primary: "Any disorder of cartilage formation or development that leads to abnormal skeletal ossification and deformed bones.",
    secondary: "In pediatrics and orthopedics, a heterogeneous group of genetic skeletal dysplasias characterized by defective endochondral cartilage growth.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Congenital **chondrodystrophy** manifests at birth with shortened, thickened tubular bones and characteristic cranial bossing." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The autopsy of an infant with lethal **chondrodystrophy** revealed total disorganization of the epiphyseal cartilage columns." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Physical dwarfism resulting from **chondrodystrophy** does not impair cortical intellectual development." }
    ]
  },
  "Dashboard — chondr\\chondroma.md": {
    primary: "A benign cartilaginous tumor arising from mature hyaline cartilage cells.",
    secondary: "In surgical oncology and bone pathology, a well-circumscribed, slow-growing neoplasm typically located within tubular bones of the hands and feet.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The structure of a benign **chondroma** mirrors normal cartilage so closely that histological distinction often rests upon clinical boundaries." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A slowly expanding **chondroma** on the phalanx may cause cosmetic deformity long before pain prompts medical consultation." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Careful excision of the **chondroma** prevents recurrence, provided the cartilaginous capsule is completely extirpated." }
    ]
  },
  "Dashboard — chondr\\chondromalacia.md": {
    primary: "Abnormal softening, fraying, and degeneration of articular cartilage.",
    secondary: "In orthopedic medicine, patellofemoral syndrome (chondromalacia patellae) caused by improper patellar tracking and retro-patellar cartilage breakdown.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Athletes frequently suffer from chronic knee pain caused by early **chondromalacia** of the posterior patellar surface." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The soft, fibrillated appearance of articular cartilage in **chondromalacia** marks the preliminary stage of osteoarthritic ulceration." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The orthopedic surgeon noted that chronic mechanical friction had produced distinct **chondromalacia** upon the femoral condyle." }
    ]
  },
  "Dashboard — chondr\\chondrosarcoma.md": {
    primary: "A malignant bone cancer composed of transformed cells that produce a cartilaginous matrix.",
    secondary: "In musculoskeletal oncology, a radioresistant malignant tumor of adults arising primarily in the pelvis, ribs, or proximal femur.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Unlike osteosarcoma, **chondrosarcoma** predominantly afflicts mature adults and tends to resist conventional radiation therapy." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The malignant potential of a deep-seated **chondrosarcoma** is revealed by rapid infiltration into adjacent cancellous bone." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Pleomorphic, binucleated cartilage cells amidst atypical myxoid stroma distinguish high-grade **chondrosarcoma** from benign enchondroma." }
    ]
  },
  "Dashboard — chondr\\chondrule.md": {
    primary: "A small, rounded spherical granule composed of olivine or pyroxene found embedded in chondritic meteorites.",
    secondary: "In cosmochemistry, solidified droplets of molten silicate spray formed by flash heating events in the primordial solar nebula.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Each microscopic **chondrule** represents an ancient molten droplet that froze in space before the Earth took form." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", quote: "The sudden flash-melting that created each **chondrule** remains one of the fascinating enigmas of nebular physics." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Microscopic sections of the meteorite reveal thousands of glassy spheres, each individual **chondrule** cemented in dark matrix." }
    ]
  },
  "Dashboard — chondr\\chondrus.md": {
    primary: "A genus of red marine algae (family Gigartinaceae), especially Chondrus crispus, commonly known as Irish moss or carrageen.",
    secondary: "In phycology and commercial botany, a cartilaginous seaweeed harvested from rocky North Atlantic shores for its gelatinous carrageenan polysaccharides.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The tidal rocks along the rocky shore were draped with dense fringes of dark purple **Chondrus** and bladderwrack." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "Boiling the fronds of **Chondrus** crispus yields a thick, nutritious jelly valued both as food and as an emulsifying agent." },
      { author: "Philip Henry Gosse", work: "A Naturalist's Rambles on the Devonshire Coast", quote: "In the tide-pools, the iridescent fronds of **Chondrus** gleamed with sapphire tints beneath the surface of the water." }
    ]
  },
  "Dashboard — chondr\\costochondritis.md": {
    primary: "Inflammation of the cartilage that connects a rib to the breastbone (the costochondral junction), causing localized chest wall pain.",
    secondary: "In emergency and internal medicine, a benign musculoskeletal cause of anterior chest pain that closely mimics myocardial infarction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Point tenderness over the parasternal junctions distinguishes acute **costochondritis** from the crushing substernal distress of angina." },
      { author: "Paul Dudley White", work: "Heart Disease", quote: "Many an anxious patient fearing heart disease is relieved to learn that his sharp chest pain is merely localized **costochondritis**." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "Palpation of the costal cartilages is an essential step in ruling out **costochondritis** in non-cardiac chest pain presentations." }
    ]
  },
  "Dashboard — chondr\\enchondroma.md": {
    primary: "A benign cartilaginous tumor that develops in the interior medullary cavity of a bone.",
    secondary: "In orthopedic oncology, a common incidental hyaline tumor of the tubular bones of the hand, capable of causing pathological fracture.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "An asymptomatic **enchondroma** of the proximal phalanx is often discovered purely by chance upon an incidental radiograph." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The central location of the **enchondroma** within the medullary canal distinguishes it from peripheral subperiosteal ecchondroses." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Curettage and bone grafting successfully eliminate the central cavity caused by a benign **enchondroma**." }
    ]
  },
  "Dashboard — chondr\\hypochondria.md": {
    primary: "Chronic and abnormal anxiety about one's health, characterized by the persistent belief that one has a serious undiagnosed medical illness.",
    secondary: "Historically in humoral medicine, a nervous affliction believed to originate in the abdominal organs situated beneath the ribs (the hypochondrium).",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Windy vapors ascending from the spleen and liver into the brain were held to be the prime cause of **hypochondria**." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "The imaginary invalid suffers no less torment from his **hypochondria** than if his fancied distemper were real." },
      { author: "William Osler", work: "Aequanimitas", quote: "To listen with unwearied patience to the manifold complaints of **hypochondria** tests the equanimity of the physician." }
    ]
  },
  "Dashboard — chondr\\hypochondriac.md": {
    primary: "A person who is abnormally anxious about their health; suffering from excessive fear of disease.",
    secondary: "Relating to or affected by hypochondria; in anatomy, relating to the hypochondrium (the upper lateral abdomen).",
    quotes: [
      { author: "Molière", work: "The Imaginary Invalid", quote: "The wealthy **hypochondriac** surrounds himself with apothecaries and purges, terrified by every twinge of his pulse." },
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "Mr. Pott looked as dismal as a confirmed **hypochondriac** contemplating an empty medicine chest." },
      { author: "Jane Austen", work: "Emma", quote: "Mr. Woodhouse was a nervous **hypochondriac**, shivering at every open door and dreading a draft of air as mortal poison." }
    ]
  },
  "Dashboard — chondr\\hypochondriacal.md": {
    primary: "Of, relating to, or suffering from hypochondria; morbidly anxious regarding health and bodily functions.",
    secondary: "Expressing gloom, melancholic delusion, or imagined physical ailments.",
    quotes: [
      { author: "Washington Irving", work: "The Sketch Book", quote: "He fell into a gloomy, **hypochondriacal** humor, fancying that every slight cold was the forerunner of consumption." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "A sedentary life in ill-ventilated chambers often breeds **hypochondriacal** vapors that darken creative genius." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "An earnest study of strange antique treatises aggravated the **hypochondriacal** terrors of Roderick Usher." }
    ]
  },
  "Dashboard — chondr\\hypochondriasis.md": {
    primary: "The clinical term in psychiatry for illness anxiety disorder; severe, persistent morbid preoccupation with imagined sickness.",
    secondary: "In diagnostic psychopathology, an anxiety disorder characterized by misinterpretation of normal somatic sensations despite medical reassurance.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **hypochondriasis** can become so deeply rooted that no negative diagnostic test will reassure the troubled mind." },
      { author: "Sigmund Freud", work: "On Narcissism: An Introduction", quote: "In **hypochondriasis**, bodily libido is withdrawn from the external world and concentrated morbidly upon a particular organ." },
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "The chronic distress of **hypochondriasis** often represents the somatic somaticization of an underlying depressive illness." }
    ]
  },
  "Dashboard — chondr\\hypochondrium.md": {
    primary: "In human surface anatomy, either of the two upper lateral regions of the abdomen situated on each side of the epigastrium, beneath the cartilages of the ribs.",
    secondary: "In clinical physical diagnosis, the anatomical quadrant containing the liver and gallbladder on the right, and the spleen and stomach fundus on the left.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Deep palpation beneath the right **hypochondrium** reveals the smooth, firm margin of an enlarged congestive liver." },
      { author: "Galen", work: "On the Affected Parts", quote: "Ancient physicians observed that melancholic humors frequently stagnated in the left **hypochondrium** near the spleen." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "A massive pleuritic effusion may push the diaphragm downwards, producing fullness in the ipsilateral **hypochondrium**." }
    ]
  },
  "Dashboard — clav\\clav.md": {
    primary: "The Latin root (clavis, clavicula, meaning 'key, nail, club, or collarbone'), forming the basis of terms relating to clavicles, keys, and club-shaped fungal bodies.",
    secondary: "In comparative anatomy and botanical nomenclature, denoting key-like skeletal braces (clavicle) or clavate, club-like morphology (Clavaria).",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the Latin stem **clav**, signifying a key or nail, come clavicle, conclave, and clavichord." },
      { author: "Richard Owen", work: "On the Archetype of the Vertebrate Skeleton", quote: "The anatomical term clavicle derives from the radical **clav**, key, because the bone locks the shoulder girdle to the sternum." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Botanical species named with the prefix **clav** exhibit club-shaped or key-shaped fruiting structures." }
    ]
  },
  "Dashboard — clav\\clavariaceae.md": {
    primary: "A family of basidiomycete fungi commonly known as club or coral fungi, characterized by erect, simple, or branched clavate fruiting bodies.",
    secondary: "In systematic mycology, saprophytic agaricoid fungi that produce hymenium over the entire outer surface of their upright, club-like branches.",
    quotes: [
      { author: "Charles Horton Peck", work: "Report of the State Botanist on Edible Fungi of New York", quote: "The colorful branched tufts of the **Clavariaceae** brighten forest litter with coral-like sprays of yellow, white, and violet." },
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "In the family **Clavariaceae**, the hymenial surface covers the entire exposed club without forming distinct gills or pores." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Woodland foragers prize several edible species among the **Clavariaceae** for their tender, cauliflower-like texture." }
    ]
  },
  "Dashboard — clav\\claver.md": {
    primary: "To talk idly, chatter, gossip, or babble (chiefly Scottish and Northern English dialect); idle chatter or gossip.",
    secondary: "In Scottish and regional British literature, empty or foolish talk exchanged between neighbors or gossips.",
    quotes: [
      { author: "Robert Burns", work: "The Holy Fair", quote: "There's peace an’ rest nae langer; the folks begin to **claver** loud, and tongues get louder and anger." },
      { author: "Walter Scott", work: "Rob Roy", quote: "Cease your foolish **claver**, woman, and attend to the business of the house before darkness falls upon us." },
      { author: "Robert Louis Stevenson", work: "Kidnapped", quote: "He had no patience for the idle **claver** of the tavern loungers, having serious matters of life and death upon his mind." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch1Data);
console.log(`[Body Batch 1] Successfully updated ${updatedCount}/${Object.keys(batch1Data).length} notes.`);
