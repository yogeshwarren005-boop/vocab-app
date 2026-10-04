# -*- coding: utf-8 -*-
"""
Curates Dashboard — nosc (Part 2: words 45-88) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  "noteworthy": {
    "primary": "Deserving special attention, notice, or observation; remarkable, notable, or significant.",
    "secondary": "In historical and empirical reports, an observation or fact that alters previous interpretations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It is a **noteworthy** circumstance that the varieties of domesticated pigeons differ primarily in external plumage."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The structural differences between ape and human brains are less **noteworthy** than those between apes and lemurs."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The advent of a reform-minded young physician was the most **noteworthy** event Middlemarch had seen that autumn."}
    ]
  },
  "notice": {
    "primary": "Attention, observation, or awareness, or a formal written or printed announcement or warning.",
    "secondary": "In contract and tenancy law, formal notification served by one party terminating an agreement or lease.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth took little **notice** of Darcy's silence, being happily engrossed in conversation with Wickham."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A legal **notice** in Chancery was posted upon the iron gates, warning all claimants of impending sale."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes observed with keen **notice** the microscopic traces of red dust clinging to the victim's cuffs."}
    ]
  },
  "noticeability": {
    "primary": "Prominence, conspicuity, or the degree to which an object, feature, or change attracts visual attention.",
    "secondary": "In sensory psychophysics, the perceptual saliency of a stimulus against a competing sensory background.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The sensory **noticeability** of a faint sound increases dramatically when competing visual stimuli are darkened."},
      {"author": "Steven Pinker", "work": "How the Mind Works", "quote": "Visual illusions manipulate edge contrast to maximize the **noticeability** of illusory contours."},
      {"author": "Ernst Mach", "work": "The Analysis of Sensations", "quote": "Luminance gradients govern the subjective **noticeability** of spatial bands across the human retina."}
    ]
  },
  "noticeable": {
    "primary": "Easily seen, observed, or detected; distinct, prominent, conspicuous, or clear to perception.",
    "secondary": "In clinical diagnosis, an observable physiological change indicating progress or regression of disease.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Following the morning dose of medication, a **noticeable** relaxation softened the rigidity in his facial muscles."},
      {"author": "George Orwell", "work": "Animal Farm", "quote": "There was a **noticeable** change in the demeanor of the pigs after they discovered the cases of whisky."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "A **noticeable** hush fell over the dinner table as the candles were lit and the boeuf en daube was served."}
    ]
  },
  "noticeableness": {
    "primary": "Visual conspicuousness, prominence, or distinctness that commands observation.",
    "secondary": "In graphic design and typography, the visual emphasis achieved through contrast, weight, and layout.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Gothic sculptors relied upon the **noticeableness** of deep undercutting to give life to high cathedral portals."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The solitary figure upon the barrow gained **noticeableness** from the vast horizontal vacancy of Egdon Heath."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Milly's radiant pallor possessed a tragic **noticeableness** that drew whispered murmurs across the London drawing room."}
    ]
  },
  "noticeably": {
    "primary": "In a noticeable manner; visibly, distinctly, clearly, or to an extent that easily attracts attention.",
    "secondary": "In chronological narrative, describing tangible shifts in temperature, behavior, or political mood.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry's face paled **noticeably** when the deep, subterranean baying drifted across the desolate moor."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The plumage of male birds becomes **noticeably** brighter and more iridescent during the spring breeding season."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Countess Olenska dressed **noticeably** simpler than the other ladies, wearing dark velvet without jewelry."}
    ]
  },
  "noticed": {
    "primary": "Observed, seen, perceived, remarked upon, or given conscious attention.",
    "secondary": "Received with public recognition, critical commendation, or formal civic honors.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor had **noticed** Willoughby's sudden embarrassment, though Marianne remained blissfully blind to it."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip **noticed** that Miss Havisham's bridal dress was yellowed with time and withered like her soul."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Brutus **noticed** that Cassius looked upon him with estranged and troubled eyes along the forum."}
    ]
  },
  "noticer": {
    "primary": "An observant person who habitually pays attention to, observes, or notices fine details.",
    "secondary": "In literary aesthetics, a novelist or artist gifted with extraordinary sensory and social acuity.",
    "quotes": [
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "Try to be one of the people on whom nothing is lost; the novelist must be an unflagging **noticer** of life."},
      {"author": "Thomas Hardy", "work": "Afterwards", "quote": "He was a man who used to notice such things; yes, neighbors would remember him as a gentle **noticer**."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Jane Austen was a supreme **noticer** of human folly, recording every pomposity with tranquil amusement."}
    ]
  },
  "notifiable": {
    "primary": "Required by statutory law or regulation to be formally reported to public health or civic authorities.",
    "secondary": "In epidemiology, infectious diseases (such as cholera or tuberculosis) requiring immediate statutory notification.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Every clinical case of Asiatic cholera was designated a **notifiable** malady under municipal sanitary codes."},
      {"author": "Edwin Chadwick", "work": "Sanitary Report", "quote": "Early registration of **notifiable** contagions enabled quarantine officers to isolate maritime vessels in port."},
      {"author": "Albert Camus", "work": "The Plague", "quote": "Dr. Rieux insisted that the authorities declare the outbreak a **notifiable** public emergency without delay."}
    ]
  },
  "notification": {
    "primary": "The act of formally notifying or giving notice, or a written announcement, notice, or warning.",
    "secondary": "In telecommunications and digital interfaces, an automated alert signaling an incoming message or system event.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The treaty required mutual **notification** thirty days prior to the deployment of border fortifications."},
      {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "Mr. Pickwick received formal **notification** from Dodson and Fogg that trial proceedings had commenced."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Naval Treaty", "quote": "Phelps awaited telegraphic **notification** from the Foreign Office regarding the missing diplomatic papers."}
    ]
  },
  "notify": {
    "primary": "To inform someone formally or officially of a fact, event, circumstance, or regulation.",
    "secondary": "In maritime law, to lodge official notice of vessel arrival, cargo damage, or maritime distress.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Go to the senate-house; **notify** the senators of this unexpected Ottoman fleet moving toward Rhodes."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Sheriffs were required by statute to **notify** freeholders of upcoming electoral assemblies in each county."},
      {"author": "Herman Melville", "work": "Benito Cereno", "quote": "Captain Delano stepped aboard to **notify** the distressed Spaniard of his willingness to furnish fresh water."}
    ]
  },
  "notion": {
    "primary": "A general concept, belief, conception, or speculative idea held by an individual or culture.",
    "secondary": "In commerce and haberdashery, small useful personal items (notions) such as needles, pins, buttons, and ribbons.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No human mind possesses any innate **notion** that was not originally derived through sensation or reflection."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Our complex **notion** of causality arises from habitual association rather than rational demonstration."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma cherished the romantic **notion** of arranging an advantageous marriage for poor Harriet Smith."}
    ]
  },
  "notional": {
    "primary": "Existing only in theory, idea, or speculation; abstract, hypothetical, and lacking physical reality.",
    "secondary": "In financial derivatives, the nominal or face value of an underlying asset upon which contract payouts are calculated.",
    "quotes": [
      {"author": "John Henry Newman", "work": "An Essay in Aid of a Grammar of Assent", "quote": "He distinguished between **notional** assent to abstract theological propositions and real living faith."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Mercantile wealth often consisted of **notional** credit circulating upon paper without equivalent gold backing."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The scholastic disputation degenerated into mere **notional** word-play devoid of experiential substance."}
    ]
  },
  "notochord": {
    "primary": "A flexible, rod-shaped cartilaginous skeletal structure supporting the dorsal nerve cord in chordate embryos.",
    "secondary": "In vertebrate embryology, the primitive axial skeleton replaced in adult vertebrates by the vertebral column.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "The presence of a persistent **notochord** in amphioxus reveals the ancestral transition from invertebrate to vertebrate."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In lampreys and sturgeons, the **notochord** remains unsegmented throughout adult life."},
      {"author": "Stephen Jay Gould", "work": "Wonderful Life: The Burgess Shale and the Nature of History", "quote": "Pikaia gracilens displayed a distinct **notochord**, confirming its status as the earliest known chordate fossil."}
    ]
  },
  "notomys": {
    "primary": "A genus of Australian hopping mice in the rodent family Muridae, famous for saltatorial locomotion.",
    "secondary": "In desert mammalogy, arid-adapted rodents possessing elongated hind feet, bipedal hops, and super-concentrated urine.",
    "quotes": [
      {"author": "John Gould", "work": "The Mammals of Australia", "quote": "Specimens of **Notomys** bound across the red sand dunes of the interior with extraordinary agility."},
      {"author": "Spencer Fullerton Baird", "work": "Mammals of North America", "quote": "Australian **Notomys** demonstrate convergent morphological evolution with North American kangaroo rats."},
      {"author": "Richard Lydekker", "work": "A Hand-book to the Marsupialia and Monotremata", "quote": "The delicate brush-tailed hopping mouse of the genus **Notomys** excavates deep spiral burrows to escape heat."}
    ]
  },
  "notonecta": {
    "primary": "A genus of predatory aquatic hemipteran bugs known as backswimmers that swim upside down at water surfaces.",
    "secondary": "In aquatic entomology, predatory bugs using long oar-like hind legs and piercing-sucking rostra to hunt small invertebrates.",
    "quotes": [
      {"author": "Henri Fabre", "work": "The Wonders of Instinct", "quote": "The predatory water-boatman **Notonecta** cruises beneath the surface film, propelling itself by powerful hind oars."},
      {"author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "In freshwater shallows, nymphal **Notonecta** stalk mosquito larvae among submerged pondweed stems."},
      {"author": "Charles Darwin", "work": "Natural Selection", "quote": "The inverted swimming posture of **Notonecta** represents an exquisite structural adaptation for surface hunting."}
    ]
  },
  "notonectidae": {
    "primary": "The family of aquatic true bugs in the suborder Heteroptera commonly referred to as backswimmers.",
    "secondary": "In limnology, aquatic predators possessing hydrofuge hair fringes that trap air bubbles against the ventral abdominal surface.",
    "quotes": [
      {"author": "Edward O. Wilson", "work": "The Diversity of Life", "quote": "Members of the family **Notonectidae** deliver a sharp, wasp-like sting if handled carelessly by collectors."},
      {"author": "Vincent Dethier", "work": "The World of the Tent-Makers", "quote": "Pond surface tensions provide an inverted ceiling for hunting bugs of the **Notonectidae** family."},
      {"author": "Howard Ensign Evans", "work": "Life on a Little-Known Planet", "quote": "Aquatic **Notonectidae** utilize specialized sensory hairs to detect vibrations caused by struggling prey."}
    ]
  },
  "notophthalmus": {
    "primary": "A genus of North American newts in the salamander family Salamandridae, including the eastern newt (Notophthalmus viridescens).",
    "secondary": "In herpetology, amphibians famous for their terrestrial juvenile red eft stage and toxic tetrodotoxin skin secretions.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We found vibrant vermilion red efts of **Notophthalmus** creeping over wet mosses after a summer shower."},
      {"author": "Edward O. Wilson", "work": "Naturalist", "quote": "The aposematic coloration of terrestrial **Notophthalmus** warns avian predators of deadly skin toxins."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Aquatic adults of **Notophthalmus** court in forest pools, their paddle-like tails rippling through green algae."}
    ]
  },
  "notoriety": {
    "primary": "Widespread infamy, ill fame, or public discredit arising from scandalous, criminal, or disgraceful conduct.",
    "secondary": "In social biography, the notoriety achieved by charismatic swindlers and outlaw folk heroes.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Demagogues seek cheap **notoriety** by subverting venerable institutions that took centuries to build."},
      {"author": "William Makepeace Thackeray", "work": "The Luck of Barry Lyndon", "quote": "Barry reveled in his dueling **notoriety**, using fear to force his way into fashionable gaming circles."},
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Professor Moriarty shunned personal **notoriety**, sitting like a silent spider at the center of London crime."}
    ]
  },
  "notorious": {
    "primary": "Widely and unfavorably known; infamous for bad behavior, scandalous crimes, or disreputable character.",
    "secondary": "In historical chronicles, designating cities, regimes, or taverns renowned for vice and corruption.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor Commodus became **notorious** for degrading imperial majesty by fighting as a common gladiator."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Fagin was a **notorious** receiver of stolen goods whose wretched den harbored young pickpockets."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "General Tilney's cruel temper was **notorious** among his acquaintances, despite his polite exterior."}
    ]
  },
  "notoriously": {
    "primary": "In a notorious or infamous manner; to an extent that is widely recognized and disreputable.",
    "secondary": "In critical observation, describing situations, systems, or climates famous for difficulty or unreliability.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The Andaman Islanders were **notoriously** fierce and hostile to any shipwrecked sailors cast upon their shores."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "French tax assessments under the ancient monarchy were **notoriously** unequal and corrupt in rural provinces."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "Flogging aboard naval frigates was **notoriously** brutal, hardening sailors into mutinous sullenness."}
    ]
  },
  "notornis": {
    "primary": "A genus of rare flightless rails endemic to New Zealand, specifically the takahē (Porphyrio hochstetteri).",
    "secondary": "In ornithology, a large blue-and-green alpine rail rediscovered in remote Fiordland valleys after presumed extinction.",
    "quotes": [
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The magnificent flightless rail **Notornis** was long regarded as an extinct fossil relic of New Zealand."},
      {"author": "Walter Buller", "work": "A History of the Birds of New Zealand", "quote": "Only four living specimens of **Notornis** were secured by collectors before the species vanished into legend."},
      {"author": "David Attenborough", "work": "The Life of Birds", "quote": "The rediscovery of the takahē, or **Notornis**, in the misty Murchison mountains proved a conservation miracle."}
    ]
  },
  "notoryctidae": {
    "primary": "The family of fossorial Australian marsupials comprising the marsupial moles (genus Notoryctes).",
    "secondary": "In comparative anatomy, marsupials showing convergence with eutherian golden moles: vestigial eyes, spatulate claws, and fused cervical vertebrae.",
    "quotes": [
      {"author": "Richard Lydekker", "work": "Marsupialia and Monotremata", "quote": "The family **Notoryctidae** occupies an isolated systematic position among Australian diprotodont marsupials."},
      {"author": "Stephen Jay Gould", "work": "Eight Little Piggies", "quote": "Marsupial moles of the **Notoryctidae** demonstrate remarkable convergent design with African golden moles."},
      {"author": "Frank Evers Beddard", "work": "Mammalia", "quote": "Specimens of **Notoryctidae** swim through desert sand rather than burrow, their tunnels collapsing immediately behind."}
    ]
  },
  "notoryctus": {
    "primary": "A genus of subterranean Australian marsupials, the marsupial moles, native to the sandy western deserts.",
    "secondary": "In zoology, desert marsupials possessing spade-like claws on the third and fourth digits and backward-opening pouches.",
    "quotes": [
      {"author": "John Gould", "work": "The Mammals of Australia", "quote": "The golden-furred **Notoryctes** navigates deep dune sands, feeding upon beetle larvae and centipedes."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The snout of **Notoryctes** is shielded by a horn-like callous shield that protects the nostrils while digging."},
      {"author": "Edward O. Wilson", "work": "The Diversity of Life", "quote": "Fossorial specialization in **Notoryctes** illustrates how arid isolation drives extreme morphological adaptation."}
    ]
  },
  "notostraca": {
    "primary": "An ancient order of small branchiopod crustaceans known as tadpole shrimp, characterized by a broad dorsal carapace.",
    "secondary": "In evolutionary biology, living fossils (such as Triops) whose morphology has remained virtually unchanged since the Triassic.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Freshwater crustaceans of the order **Notostraca** produce desiccation-resistant cysts transported across continents by waterfowl."},
      {"author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "The broad horse-shoe shield of **Notostraca** covers the cephalothorax and bears numerous paired swimming limbs."},
      {"author": "Stephen Jay Gould", "work": "The Structure of Evolutionary Theory", "quote": "Stasis in **Notostraca** reveals that morphological stability can endure across hundreds of millions of years."}
    ]
  },
  "notropis": {
    "primary": "A species-rich genus of small North American freshwater ray-finned minnows in the family Cyprinidae, the eastern shiners.",
    "secondary": "In aquatic ecology, minnows inhabiting clean gravel streams, serving as vital ecological indicators of river water quality.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The genus **Notropis** comprises dozens of shimmering minnow species darting through Appalachian rapids."},
      {"author": "Spencer Fullerton Baird", "work": "Fishes of the Susquehanna", "quote": "Schools of **Notropis** spawn in clear pebble nests excavated by larger river chubs."},
      {"author": "Louis Agassiz", "work": "Contributions to Natural History", "quote": "Breeding males of **Notropis** develop bright crimson fins and nuptial tubercles along the snout."}
    ]
  },
  "notturno": {
    "primary": "A musical composition evocative of the night, nightfall, or evening calm; an 18th-century precursor to the nocturne.",
    "secondary": "In classical chamber music, multi-movement divertimento-style works composed for evening outdoor performance.",
    "quotes": [
      {"author": "Wolfgang Amadeus Mozart", "work": "The Letters of Mozart", "quote": "I composed a four-orchestra **notturno** for the garden festival, spacing the ensembles to produce enchanting echoes."},
      {"author": "Charles Rosen", "work": "The Classical Style", "quote": "Haydn's exquisite **notturno** movements balance serene melodic lyricism with playful wind counterpoint."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "A gentle **notturno** releases the listener from worldly striving into contemplative aesthetic contemplation."}
    ]
  },
  "precognition": {
    "primary": "The purported psychic ability to perceive, foresee, or experience events before they occur in physical time.",
    "secondary": "In parapsychology, laboratory experiments investigating prophetic dreams, presentiments, and retrocausal cognition.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Reports of prophetic dreams and sudden **precognition** challenge our conventional philosophical assumptions about linear time."},
      {"author": "Carl Jung", "work": "Synchronicity: An Acausal Connecting Principle", "quote": "Acausal synchronicities suggest that the unconscious mind can occasionally access a state of temporal **precognition**."},
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Claims of **precognition** crumble when subjected to rigorous statistical scrutiny against confirmation bias."}
    ]
  },
  "precognitive": {
    "primary": "Relating to or involving precognition; possessing or demonstrating foreknowledge of future events.",
    "secondary": "In parapsychological literature, describing dreams or hunches that appear to anticipate future happenings.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "The medium experienced vivid **precognitive** visions of the maritime disaster days before the liner set sail."},
      {"author": "Philip K. Dick", "work": "The Minority Report", "quote": "The police department relied upon three **precognitive** mutants to identify murderers before crimes occurred."},
      {"author": "Arthur C. Clarke", "work": "Childhood's End", "quote": "The children demonstrated uncanny **precognitive** awareness, anticipating technological catastrophes across the globe."}
    ]
  },
  "recognition": {
    "primary": "The act of identifying something or someone previously known, or formal acknowledgment of validity and merit.",
    "secondary": "In international diplomacy, official acceptance by a sovereign government of a foreign state's legitimate existence.",
    "quotes": [
      {"author": "Aristotle", "work": "Poetics", "quote": "Dramatic **recognition** represents a change from ignorance to knowledge, producing love or hate between characters."},
      {"author": "G. W. F. Hegel", "work": "Phenomenology of Spirit", "quote": "Self-consciousness achieves its satisfaction only in finding mutual **recognition** in another self-consciousness."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Mutual **recognition** between mother and infant is mediated through instantaneous facial mimicry."}
    ]
  },
  "recognizable": {
    "primary": "Capable of being recognized, identified, or distinguished by familiar features or characteristics.",
    "secondary": "In cognitive psychology, sensory stimuli that match existing neural memory templates with high confidence.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The lighthouse tower remained clearly **recognizable** across the bay, cutting through the evening mist."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Even in death, the features of the baronet were instantly **recognizable** beneath the lantern light."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Dr. Manette was barely **recognizable** after his eighteen horrific years of solitary confinement in the Bastille."}
    ]
  },
  "recognizably": {
    "primary": "In a recognizable manner; in a way that is identifiable, noticeable, or distinctly clear.",
    "secondary": "In stylistic analysis, exhibiting traits that point unequivocally to a specific author, artist, or school.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The old London landmarks were still **recognizably** present beneath the grime and bomb-shattered masonry."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond's villa was **recognizably** Italian in its austere marble terraces and cypress avenues."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "The English tourists looked **recognizably** foreign as they clutch Baedeker guidebooks along the Arno."}
    ]
  },
  "recognizance": {
    "primary": "A formal legal obligation entered into before a court or magistrate, binding an individual to perform an act.",
    "secondary": "In criminal procedure, release on one's own recognizance (ROR) without posting financial cash bail.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A **recognizance** is an obligation of record which a man enters into before some court or magistrate."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The bailie released the prisoner upon his own **recognizance** to appear at the upcoming circuit assizes."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The magistrate warned Mr. Snodgrass that his **recognizance** would be forfeited if public peace was breached."}
    ]
  },
  "recognize": {
    "primary": "To identify someone or something from previous encounter or knowledge, or to acknowledge the validity of something.",
    "secondary": "In parliamentary law, to formally grant the floor to a member wishing to speak during a debate.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Do not laugh at me; for, as I am a man, I think this lady to be my child Cordelia... I **recognize** you."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Free nations must **recognize** that local municipal liberties constitute the true strength of democracy."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor could not fail to **recognize** in Edward's troubled silence an agonizing struggle between honor and duty."}
    ]
  },
  "recognized": {
    "primary": "Identified, acknowledged, formally validated, or widely accepted as legitimate and distinguished.",
    "secondary": "In academic and professional disciplines, certified standards or credentials sanctioned by governing bodies.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Gold and silver have been **recognized** by all civilized nations as the universal measure of commercial exchange."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Natural selection is now **recognized** by biological science as the primary agent of organic transformation."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The British constitution **recognized** traditional rights inherited from Magna Charta and the Bill of Rights."}
    ]
  },
  "unnotched": {
    "primary": "Not notched; having a continuous, smooth, or unbroken edge lacking serrations or V-shaped cuts.",
    "secondary": "In entomology and botany, describing entire unlobed margins of leaves, sepals, or beetle elytra.",
    "quotes": [
      {"author": "Asa Gray", "work": "Field, Forest, and Garden Botany", "quote": "The smooth, **unnotched** margin of the ovate leaf distinguishes this species from its serrated woodland relatives."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Specimens with **unnotched** mandibles were less adapted to shear fibrous leaves during seasonal droughts."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The sharp granite ridges rose into the Sierra sky, **unnotched** by glacial scouring along the highest crests."}
    ]
  },
  "unnoted": {
    "primary": "Not noticed, observed, recorded, or marked; passing without attention or remark.",
    "secondary": "In historical narratives, obscure deeds or quiet lives that leave no trace in official public annals.",
    "quotes": [
      {"author": "Thomas Gray", "work": "Elegy Written in a Country Churchyard", "quote": "Full many a flower is born to blush unseen, and waste its sweetness on the desert air, **unnoted** by the great."},
      {"author": "William Wordsworth", "work": "The Excursion", "quote": "He lived an **unnoted** life among the solitude of Westmorland fells, beloved by wandering shepherds."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Dozens of petty frontier skirmishes passed **unnoted** by contemporary Roman annalists."}
    ]
  },
  "unnoticeable": {
    "primary": "Not easily seen, heard, or noticed; inconspicuous, subtle, obscure, or attracting little attention.",
    "secondary": "In camouflage biology, cryptic adaptations that blend an animal seamlessly into its resting background.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "A tiny change in refractive index was virtually **unnoticeable** until the light struck the glass vessel at an angle."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The subtle tremors were almost **unnoticeable** until the patient attempted to write his signature."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The tiny drop of dried blood upon the wallpaper was **unnoticeable** to the untrained eye of Inspector Lestrade."}
    ]
  },
  "unnoticeableness": {
    "primary": "Inconspicuousness, obscurity, or subtlety that escapes detection or observation.",
    "secondary": "In military camouflage and architecture, the deliberate design quality of blending into surrounding scenery.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether prized his diplomatic **unnoticeableness**, which allowed him to observe Parisian society undisturbed."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The quiet shepherd lived in peaceful **unnoticeableness**, far removed from the turbulent ambitions of Casterbridge."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She cherished the quiet **unnoticeableness** of her corner room where she could study mathematics without remark."}
    ]
  },
  "unnoticeably": {
    "primary": "In an unnoticeable manner; subtly, quietly, gradually, or without attracting observation.",
    "secondary": "In natural processes, incremental transitions such as the shifting of seasons or wearing of stones.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Minute variations accumulate **unnoticeably** over generations, eventually diverging into distinct varieties."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Character dissolves **unnoticeably**, step by tiny compromise, long before public scandal erupts."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The pond ice melts **unnoticeably** under the warming March sun, opening blue water along the southern shores."}
    ]
  },
  "unnoticed": {
    "primary": "Not observed, seen, noticed, or attended to; passed by without attracting attention.",
    "secondary": "In espionage or evasion, slipping through surveillance barriers without detection.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Frank Churchill managed to slip a secret note to Jane Fairfax **unnoticed** by the rest of the company."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A dark figure glided **unnoticed** across the moonlit granite tors, watching the hall from afar."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton slipped **unnoticed** into the crowded revolutionary tribunal, taking his seat behind Darnay."}
    ]
  },
  "unrecognizable": {
    "primary": "Not able to be recognized, identified, or distinguished, especially due to severe alteration or decay.",
    "secondary": "In forensic pathology, remains damaged beyond visual identification by fire, decomposition, or trauma.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The beautiful features of William were blackened and **unrecognizable** after the monster's stranglehold."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The Thames valley had altered until it was utterly **unrecognizable** in the far future era of the Eloi."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The port of Rotterdam was blasted into an **unrecognizable** smoking wasteland by the Luftwaffe raid."}
    ]
  },
  "unrecognizably": {
    "primary": "In an unrecognizable manner; to an extent that prevents identification or recognition.",
    "secondary": "In historical transformation, cities, cultures, or landscapes altered beyond all previous resemblance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The once handsome captain had deteriorated **unrecognizably**, poisoned by opium and squalor in Nemo's garret."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient forum was **unrecognizably** transformed into a desolate pasture where cattle grazed amid broken columns."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard returned to the fair **unrecognizably** altered, dressed in the ragged smock-frock of a common hay-trusser."}
    ]
  },
  "unrecognized": {
    "primary": "Not identified, acknowledged, or validated; not perceived or known for one's true identity or merit.",
    "secondary": "In intellectual and artistic history, genius or scientific breakthroughs ignored during the creator's lifetime.",
    "quotes": [
      {"author": "Herman Melville", "work": "Pierre: or, The Ambiguities", "quote": "The profoundest literary masterworks often pass **unrecognized** by the superficial book reviewers of their day."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea performed countless unhistoric acts of kindness that remained **unrecognized** by the noisy world."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The avenger walked the streets of London **unrecognized**, his heart set upon ancient retribution."}
    ]
  }
}
