# -*- coding: utf-8 -*-
"""
Curates Dashboard — disc (Part 1: words 1-52) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part1 = {
  "disc": {
    "primary": "A flat, thin, circular plate or object, or an anatomical structure such as an intervertebral pad.",
    "secondary": "In computer technology, magnetic or optical storage media such as hard discs and compact discs.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The image of the sun cast through a tiny pinhole formed a luminous golden **disc** upon the opposite wall."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The adhesive **disc** at the tip of the tendril secretes a resinous cement that anchors the vine to rock."},
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The colossal spherical command module rotated slowly, framing the pale blue **disc** of Earth in the viewport."}
    ]
  },
  "discalceate": {
    "primary": "To strip of shoes or sandals; to go barefoot as an act of ascetic humility or religious devotion.",
    "secondary": "In ecclesiastical history, religious orders whose members walked without footwear as a penance.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Eastern worshippers **discalceate** their feet prior to crossing the threshold of the sacred sanctuary."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The austere monks chose to **discalceate** themselves, enduring winter snows on bare soles to mortify the flesh."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The penitent knight was commanded to **discalceate** his feet before kneeling at the Holy Sepulchre."}
    ]
  },
  "discalced": {
    "primary": "Barefoot or wearing only sandals; designating certain reformed religious monastic orders.",
    "secondary": "In Catholic church history, the Discalced Carmelites reformed by Saint Teresa of Ávila and Saint John of the Cross.",
    "quotes": [
      {"author": "Saint Teresa of Ávila", "work": "The Life of Saint Teresa of Jesus", "quote": "Our primitive Carmelite rule was restored by the **discalced** sisters, who embraced joyful poverty and fasting."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "A brown-robed **discalced** friar paced the cloisters of the Ara Coeli, whispering his rosary beneath the arches."},
      {"author": "George Eliot", "work": "Romola", "quote": "Processions of **discalced** penitents followed Savonarola through the crowded streets of renaissance Florence."}
    ]
  },
  "discant": {
    "primary": "An alternative spelling of descant; a melody or counterpoint sung above the plainsong, or a discourse.",
    "secondary": "In early polyphonic music, an upper melodic voice improvised or composed over a Gregorian tenor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Why, I, in this weak piping time of peace, have no delight to pass away the time, unless to see my shadow in the sun and **discant** on mine own deformity."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The wakeful nightingale all night long her amorous **discant** sung, filling the grove with solemn melodies."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Rhetoricians love to **discant** upon the miseries of life while taking care to secure every earthly comfort."}
    ]
  },
  "discard": {
    "primary": "To get rid of something as useless, undesirable, or obsolete; to throw away or cast off.",
    "secondary": "In card games, to play or dispose of an unwanted card from one's hand.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection is daily and hourly scrutinizing every variation, rejecting and ready to **discard** that which is bad."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth resolved to **discard** every lingering prejudice that had blinded her judgment regarding Darcy."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The true philosopher must courageously **discard** all idolized traditional dogmas that obstruct clear observation."}
    ]
  },
  "discarded": {
    "primary": "Thrown away, rejected, or abandoned as no longer useful, needed, or desirable.",
    "secondary": "In archaeology, refuse, sherds, and faunal bones deposited in ancient midden heaps.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip surveyed the decaying bridal feast, noticing the **discarded** wedding veil yellowing under spiders' webs."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "Wandering tramps searched the gutter for **discarded** cigarette stubs to roll into fresh paper."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The abandoned thresher stood in the wintry field like a **discarded** engine of prehistoric warfare."}
    ]
  },
  "discase": {
    "primary": "To strip of covering, clothing, armor, or outer case; to undress, expose, or uncover.",
    "secondary": "In dramatic literature, removing a disguise or ceremonial robe to reveal one's true identity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "I will **discase** me, and myself present as I was sometime Milan; quickly, spirit, thou shalt ere long be free."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The wounded knight was compelled to **discase** his heavy steel greaves before the surgeon could examine his limbs."},
      {"author": "John Dryden", "work": "The Spanish Friar", "quote": "The conspirator was forced to **discase** his dark cloak and reveal the poisoned dagger hidden in his doublet."}
    ]
  },
  "disceptation": {
    "primary": "Controversy, dispute, formal debate, or contentious verbal disputation.",
    "secondary": "In legal and scholastic history, an oral argumentation between advocates before a tribunal.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Fierce **disceptation** among rival commentators obscured the original text beneath clouds of angry pedantry."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Constitutional liberties were forged through pragmatic experience rather than metaphysical **disceptation** in salons."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "Truth requires no subtle **disceptation** of licensed censors to prevail against error in open combat."}
    ]
  },
  "discern": {
    "primary": "To perceive, recognize, distinguish, or detect with the eyes or with the intellect.",
    "secondary": "In moral philosophy, exercising ethical wisdom to separate genuine virtue from fraudulent appearance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Does any here know me? This is not Lear. Does Lear walk thus? speak thus? Where are his eyes? Either his notion weakens, his **discern** is lethargied."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "An observant naturalist can **discern** minute transitional variations linking geographically separated races."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma was too quick-witted not to **discern** that Mr. Knightley disapproved of her intimacy with Harriet."}
    ]
  },
  "discernability": {
    "primary": "The property of being discernible, perceptual distinctness, or clarity sufficient for sensory detection.",
    "secondary": "In optics and astronomy, the resolution limit at which adjacent stellar points are distinguished.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Atmospheric turbulence reduces the **discernability** of delicate lunar rilles even through large reflectors."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory thresholds define the mathematical limits of conscious **discernability** for auditory tones."},
      {"author": "Ernst Mach", "work": "The Analysis of Sensations", "quote": "Luminance contrast governs the immediate **discernability** of fine grid lines upon the visual retina."}
    ]
  },
  "discernable": {
    "primary": "Able to be discerned, perceived, detected, or distinguished by sight or the intellect; discernible.",
    "secondary": "In clinical observation, tangible symptoms or physiological changes evident upon examination.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Through the dense moor fog, a faint pale light was barely **discernable** in the direction of the hall."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The gradual uplift of ancient marine terraces along the Baltic coast is clearly **discernable** over centuries."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "A subtle shade of ironic amusement was **discernable** in Gilbert Osmond's quiet polite greetings."}
    ]
  },
  "discernible": {
    "primary": "Able to be perceived, recognized, distinguished, or detected by the senses or the intellect.",
    "secondary": "In historical analysis, distinct trends or causal patterns emerging from archival records.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "No **discernible** boundary separates the cognitive faculties of higher mammals from the primal instincts of man."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A **discernible** decay in military discipline was already evident during the luxurious reign of Severus."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The stroke of the lighthouse beam was clearly **discernible** across the dark water, rhythmic and austere."}
    ]
  },
  "discerning": {
    "primary": "Having or showing good judgment, sharp perception, and intellectual insight; discriminating.",
    "secondary": "In aesthetic criticism, a connoisseur who recognizes subtle artisanal craftsmanship and genius.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the Poets", "quote": "A **discerning** critic separates the permanent gold of true genius from the transient tinsel of fashion."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was regarded by her father as a more **discerning** and sensible observer than her foolish sisters."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The novel appeals to the **discerning** reader who values delicate psychological nuances over melodramatic action."}
    ]
  },
  "discernment": {
    "primary": "The ability to judge well, perceive keenly, and distinguish subtle differences in truth, character, or art.",
    "secondary": "In spiritual theology, the contemplative grace of distinguishing divine promptings from selfish impulses.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's lack of worldly **discernment** led her to place unbounded trust in Willoughby's glamorous exterior."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Discretion in speech is more than eloquence; to speak agreeably to him with whom we deal requires **discernment**."},
      {"author": "Edmund Burke", "work": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful", "quote": "A refined aesthetic taste is nothing other than natural sensibility guided by cultivated intellectual **discernment**."}
    ]
  },
  "discerp": {
    "primary": "To tear into pieces, rend apart, or sever forcibly into fragments; to dismember.",
    "secondary": "In metaphysical debates on the soul, the question of whether an indivisible spiritual substance can be lacerated.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "An immaterial thinking substance cannot be divided or **discerp** into physical parts like extended matter."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "Time and oblivion **discerp** the proudest marble monuments, scattering their dust across neglected fields."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "Analytical pedantry attempts to **discerp** the living unity of the poetic symbol into cold mechanical abstractions."}
    ]
  },
  "disciform": {
    "primary": "Having the shape or form of a disc; flat, round, and discoid.",
    "secondary": "In ophthalmology, disciform keratitis or disciform macular degeneration characterized by round lesions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "Solitary mushroom corals exhibit a flat, **disciform** skeleton anchored lightly upon the reef sand."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination revealed a dense **disciform** keratitis involving the deep corneal stroma."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The spore capsules of certain aquatic fungi present a curious **disciform** outline beneath the lens."}
    ]
  },
  "discina": {
    "primary": "A genus of cup fungi in the family Discinaceae, or an ancient genus of inarticulate inarticulate brachiopods.",
    "secondary": "In paleontology and mycology, sessile brachiopods possessing circular chitinophosphatic shells or disc-shaped ascomycetes.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Fossil shells belonging to the ancient brachiopod genus **Discina** persist virtually unchanged from the Silurian strata."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The persistent survival of **Discina** through vast geological epochs illustrates remarkable evolutionary morphological stasis."},
      {"author": "Richard Owen", "work": "Palaeontology", "quote": "Inarticulate brachiopods such as **Discina** anchor their flat valves to subterranean rocks by a muscular pedicle."}
    ]
  },
  "disciple": {
    "primary": "A dedicated follower or pupil of a religious, philosophical, or artistic teacher or master.",
    "secondary": "In Christianity, specifically one of the twelve chosen personal companions of Jesus Christ.",
    "quotes": [
      {"author": "Plato", "work": "Phaedo", "quote": "Every weeping **disciple** gathered around the couch of Socrates, listening to his final discourse upon immortality."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The faithful **disciple** pressed forward toward the Celestial City, heedless of the mockery of Vanity Fair."},
      {"author": "Friedrich Nietzsche", "work": "Thus Spoke Zarathustra", "quote": "One repays a teacher badly if one remains always nothing more than a docile **disciple**."}
    ]
  },
  "discipleship": {
    "primary": "The state, condition, or practice of being a disciple; following the teachings of a revered leader or master.",
    "secondary": "In Christian ethics, the sacrificial, disciplined commitment to living out the moral teachings of the Gospel.",
    "quotes": [
      {"author": "Dietrich Bonhoeffer", "work": "The Cost of Discipleship", "quote": "Costly grace calls us to true **discipleship**, which requires surrendering worldly security to follow the master."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The psychological hallmarks of authentic **discipleship** include saintly self-surrender, peace, and fervent charity."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Reverent **discipleship** is the natural homage which lesser minds gladly pay to transcendent heroic genius."}
    ]
  },
  "disciplinal": {
    "primary": "Relating to discipline, regular order, systematic correction, or educational training; disciplinary.",
    "secondary": "In monastic and ecclesiastical codes, regulations enforcing penitential exercises and ascetic obedience.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The monastic orders imposed rigorous **disciplinal** fasts to subdue all rebellious carnal desires."},
      {"author": "Jeremy Bentham", "work": "Panopticon; or, The Inspection-House", "quote": "The central inspection tower served as an ideal **disciplinal** mechanism for reforming incarcerated convicts."},
      {"author": "John Henry Newman", "work": "The Idea of a University", "quote": "The university curriculum exercises a profound **disciplinal** influence upon the intellectual habits of youths."}
    ]
  },
  "disciplinarian": {
    "primary": "A person who enforces strict discipline, obedience, and order, especially in a school, military, or household.",
    "secondary": "In institutional history, a stern master or officer noted for uncompromising adherence to regulations.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Creakle was a relentless **disciplinarian**, stalking the schoolroom with a cane tucked beneath his arm."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The naval captain was a merciless **disciplinarian**, ordering daily floggings for trivial maritime infractions."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Brocklehurst was an austere **disciplinarian** who ordered girls' curls shorn to mortify worldly vanity."}
    ]
  },
  "disciplinary": {
    "primary": "Relating to discipline, punishment, or correction, or relating to an academic branch of knowledge or learning.",
    "secondary": "In administrative governance, official proceedings held to address professional misconduct or ethical breaches.",
    "quotes": [
      {"author": "Michel Foucault", "work": "Discipline and Punish", "quote": "The birth of the prison reflected a new **disciplinary** apparatus aimed at normalizing docile bodies in society."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A regular army requires strict **disciplinary** codes to ensure that armed soldiers obey civilian authority."},
      {"author": "John Henry Newman", "work": "The Idea of a University", "quote": "A liberal education harmonizes multiple **disciplinary** perspectives into a comprehensive philosophical vision."}
    ]
  },
  "discipline": {
    "primary": "The practice of training people to obey rules, code of behavior, or a field of academic study and learning.",
    "secondary": "In monastic asceticism, an instrument of penance, such as a whip or scourge, used for self-mortification.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The legions conquered the world not by superior numbers, but through unbending, relentless military **discipline**."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Party members practiced crimestop, a voluntary mental **discipline** that halted heterodox thoughts at the threshold."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale kept in his secret closet a bloody **discipline**, scourging his flesh in private remorse."}
    ]
  },
  "disciplined": {
    "primary": "Showing a controlled form of behavior or training; orderly, obedient, and adhering to strict standards.",
    "secondary": "In athletic or intellectual performance, executing complex routines with calm, rehearsed precision.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The British pilots displayed a **disciplined** courage that turned the tide of battle in the summer of 1940."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth commanded a **disciplined** crew whose devoted loyalty was forged through mutual respect."},
      {"author": "Marcus Aurelius", "work": "Meditations", "quote": "Maintain a calm and **disciplined** mind, undisturbed by the external praise or censure of fleeting crowds."}
    ]
  },
  "disclaim": {
    "primary": "To deny, refuse, or renounce any connection with, claim to, or responsibility for something.",
    "secondary": "In property and inheritance law, to formally renounce an interest in an estate, trust, or legal right.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The authors of the Constitution **disclaim** any intention to create an imperial or monarchical executive."},
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Here I **disclaim** all my paternal care, propinquity and property of blood, and as a stranger hold thee to my heart."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was eager to **disclaim** any share in her mother's ill-bred and offensive insinuations at the ball."}
    ]
  },
  "disclaimer": {
    "primary": "A statement that denies something, especially responsibility, legal liability, or connection to an event.",
    "secondary": "In intellectual property and patent law, a formal repudiation of certain claims in a patent application.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "A clear legal **disclaimer** alerts contracting parties that certain warranties are explicitly excluded from the covenant."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The publisher prefixed an ironic **disclaimer**, pretending the traveler's memoirs were unvarnished literal truth."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "Holmes made an emphatic **disclaimer** of personal ambition, seeking only to shield the noble family from ruin."}
    ]
  },
  "disclike": {
    "primary": "Resembling or having the round, flattened shape of a disc; circular, flat, and discoid.",
    "secondary": "In astronomy and cytology, describing planar structures like planetary rings or red blood cells.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The surface of the lagoon was covered with millions of tiny, **disclike** medusae pulsing in the clear water."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Saturn is encircled by an immense, thin, **disclike** system of rings that casts shadows across its equator."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Mammalian erythrocytes possess a biconcave **disclike** morphology that maximizes oxygen exchange surface area."}
    ]
  },
  "disclose": {
    "primary": "To make secret, new, or unknown information known; to reveal, uncover, or expose to view.",
    "secondary": "In securities and corporate law, providing complete financial records and risks to investors.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy's letter served to **disclose** the true villainy of Wickham, exposing his past debts and treachery."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The canker galls the infants of the spring, too oft before their buttons be **disclose**d, and in the morn of youth."},
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Holmes promised to **disclose** the full ramifications of the Moriarty criminal syndicate to the Prime Minister."}
    ]
  },
  "disclosed": {
    "primary": "Made known, revealed, uncovered, or exposed to public knowledge or view.",
    "secondary": "In legal proceedings, evidence or documents formally revealed to opposing counsel during pretrial discovery.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The mysterious papers found in Nemo's trunk **disclosed** the secret parentage of Lady Dedlock's child."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A palace slave **disclosed** the impending conspiracy against the tyrant, saving the imperial court from assassination."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Victor **disclosed** his tragic secret to the magistrate, who listened with mixture of pity and incredulity."}
    ]
  },
  "disclosure": {
    "primary": "The act of making secret or new information known, or the secret revelation that is disclosed.",
    "secondary": "In corporate governance, mandatory filings (such as 10-K statements) ensuring transparent financial reporting.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Lucy Steele's triumphant **disclosure** of her secret engagement shattered Elinor's quiet hopes in an instant."},
      {"author": "Alexander Hamilton", "work": "The Reynolds Pamphlet", "quote": "Hamilton published a candid **disclosure** of his private indiscretion to vindicate his public fiscal integrity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The unexpected **disclosure** of Bulstrode's past disgraced him forever before the pious society of the town."}
    ]
  },
  "disco": {
    "primary": "A club or party where people dance to recorded pop and dance music, or a genre of 1970s dance-pop music.",
    "secondary": "In music history, an uptempo style characterized by four-on-the-floor bass drums, strings, and syncopated basslines.",
    "quotes": [
      {"author": "Tom Wolfe", "work": "The Bonfire of the Vanities", "quote": "Youths crowded into the subterranean **disco**, moving beneath mirrored globes and pulsing neon lights."},
      {"author": "David Foster Wallace", "work": "A Supposedly Fun Thing I'll Never Do Again", "quote": "The cruise ship featured an underground **disco** where vacationers danced to synthetic seventies anthems."},
      {"author": "Hunter S. Thompson", "work": "The Great Shark Hunt", "quote": "The booming bass of the casino **disco** echoed across the parking lot into the hot desert midnight air."}
    ]
  },
  "discocephali": {
    "primary": "An order or suborder of marine ray-finned fishes comprising the remoras or sharksuckers (family Echeneidae).",
    "secondary": "In ichthyology, fishes possessing a flat oval laminated sucker on top of the head modified from the dorsal fin.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The **Discocephali** are distinguished by the transformation of the spinous dorsal fin into a powerful suctorial disc."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We captured a specimen of **Discocephali** firmly attached to the belly of a blue shark alongside the frigate."},
      {"author": "Louis Agassiz", "work": "Contributions to Natural History", "quote": "Transverse cartilaginous lamellae in **Discocephali** create powerful hydraulic vacuums that resist dislodgement."}
    ]
  },
  "discoglossidae": {
    "primary": "An archaic family of primitive frogs, including the painted frogs and midwife toads (order Anura).",
    "secondary": "In herpetology, anuran amphibians characterized by a disc-shaped, round tongue that cannot be extended, and opistocoelous vertebrae.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Primitive anurans of the family **Discoglossidae** retain ancestral anatomical traits linking frogs with fossil stegocephalians."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The famous midwife toad of Europe belongs to the family **Discoglossidae**, the male carrying egg strings upon his thighs."},
      {"author": "Edward O. Wilson", "work": "The Diversity of Life", "quote": "Ancient lineages like the **Discoglossidae** provide vital evolutionary benchmarks for understanding modern amphibian radiation."}
    ]
  },
  "discography": {
    "primary": "A descriptive catalog or comprehensive list of musical recordings made by a particular performer or composer.",
    "secondary": "In musicology, the bibliographical and critical study of audio recordings, matrix numbers, and release formats.",
    "quotes": [
      {"author": "Theodor Adorno", "work": "Essays on Music", "quote": "A critical **discography** charts how commercial recording studios shaped twentieth-century interpretation of Beethoven."},
      {"author": "Oliver Sacks", "work": "Musicophilia", "quote": "The amnesic musician could instantly reconstruct the complete recorded **discography** of Bach cantatas from memory."},
      {"author": "Aaron Copland", "work": "Copland on Music", "quote": "The collector consults a scholarly **discography** to trace the conductor's evolving tempos across five decades."}
    ]
  },
  "discoid": {
    "primary": "Resembling or shaped like a disc; flat and circular in form.",
    "secondary": "In botany, flower heads in Asteraceae composed solely of tubular disc florets without ray petals.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain composite plants bear purely **discoid** flower heads, having lost their radiating marginal petals entirely."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The **discoid** stigma expands horizontally upon the apex of the style, presenting a moist receptive surface."},
      {"author": "Stephen Jay Gould", "work": "Wonderful Life", "quote": "The Ediacaran fossil Tribrachidium displayed a bizarre, three-lobed **discoid** body that rested upon benthic mud."}
    ]
  },
  "discoidal": {
    "primary": "Having the form of a disc; circular, flat, and round; discoid.",
    "secondary": "In embryology, discoidal cleavage where cell division is restricted to a small disc of cytoplasm at the animal pole.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Reptiles and birds exhibit **discoidal** cleavage, with embryonic blastomeres multiplying atop a vast yolk mass."},
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "Fossil nummulites formed colossal limestone beds composed of billions of flat, **discoidal** foraminiferal shells."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The jellyfish bell pulsates through rhythmic contractions of its muscular **discoidal** margin."}
    ]
  },
  "discolor": {
    "primary": "To change, stain, fade, or tarnish the natural or original color of an object or surface.",
    "secondary": "In chemical corrosion, oxidation that darkens metallic luster or leaves unsightly blemishes.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Putrefaction had begun to **discolor** the features of the corpse, marring the fair youth of Elizabeth's brother."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Soot and coal smoke from the London hearths settled everywhere, threatening to **discolor** the finest linens."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "Chemical vapors rising from the graduated glass began to **discolor** the crystal liquid from crimson to dark purple."}
    ]
  },
  "discoloration": {
    "primary": "The process of becoming discolored, or a stained, faded, or tarnished spot on a surface.",
    "secondary": "In clinical forensic pathology, livor mortis or postmortem purplish staining caused by venous pooling.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A characteristic bronze **discoloration** of the skin alerted the physician to adrenal cortical failure in Addison's disease."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes pointed out a dark brownish **discoloration** upon the sills, proving that the assassin had climbed the drainpipe."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister bore a strange scarlet **discoloration** carved into the flesh over his breast, hidden from mortal eyes."}
    ]
  },
  "discolorise": {
    "primary": "To remove color from; to bleach, clarify, or decolorize (British spelling).",
    "secondary": "In sugar refining and chemical purification, filtering crude syrups through animal charcoal to remove pigments.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Bone charcoal is widely employed in laboratories to **discolorise** organic solutions and precipitate coloring resins."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Chlorine gas will rapidly **discolorise** moist vegetable dyes, bleaching litmus and indigo papers to pure white."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Repeated distillations over absorbent earth served to **discolorise** the volatile spirit of petroleum."}
    ]
  },
  "discolorize": {
    "primary": "To deprive of color; to bleach, whiten, or decolorize.",
    "secondary": "In industrial manufacturing, removing impurities and yellow tints from vegetable oils and waxes.",
    "quotes": [
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "Sulfurous fumes will instantly **discolorize** the red petals of a fresh rose, turning them translucent white."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "We treated the crude rubber with acid solvents to **discolorize** the resin before vulcanization."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Oxidizing reagents can **discolorize** the deep red pigments of grape skins during artificial fermentation."}
    ]
  },
  "discolour": {
    "primary": "To spoil, alter, or stain the natural color of something; to fade or tarnish (British spelling).",
    "secondary": "In art restoration, chemical yellowing of aged varnish that darkens Renaissance oil paintings.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Moisture and atmospheric soot slowly **discolour** the delicate marble relief sculptures of Venice."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The tears that sprang to her eyes threatened to **discolour** the pristine parchment on which she sketched."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Damp river fogs crept up the marsh to **discolour** the gravestones and rust the churchyard ironwork."}
    ]
  },
  "discolouration": {
    "primary": "A stain, blemish, or alteration of color; loss of original chromatic purity (British spelling).",
    "secondary": "In dermatology and botany, chlorotic blotches or necrotic spots on leaves and animal tissues.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "There was a faint yellowish **discolouration** around the lips, suggesting the presence of an alkaloid poison."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Humic acids produce a gradual **discolouration** of limestone fragments buried within rich topsoil."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Fungal **discolouration** along the felled oak trunks indicated that rot had begun to compromise the timber."}
    ]
  },
  "discolourise": {
    "primary": "To deprive of color; to bleach or decolorize (alternative British spelling).",
    "secondary": "In textile processing, using chemical mordants and bleaching agents to prepare fabrics for uniform dyeing.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Sulfur dioxide was introduced into the glass tube to **discolourise** the crimson potassium permanganate solution."},
      {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "Fine porcelain clay is washed with dilute acid to **discolourise** iron oxide stains prior to firing in the kiln."},
      {"author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "Sunlight and dew cooperate naturally to **discolourise** unbleached linen laid out across meadow grass."}
    ]
  },
  "discombobulate": {
    "primary": "To confuse, upset, disconcert, frustrate, or throw into a state of humorous confusion.",
    "secondary": "In informal American narrative, suddenly disrupting someone's poise, dignity, or train of thought.",
    "quotes": [
      {"author": "Mark Twain", "work": "Autobiography", "quote": "The unexpected arrival of the river pilot was enough to **discombobulate** the greenest apprentice in the wheelhouse."},
      {"author": "David Foster Wallace", "work": "Infinite Jest", "quote": "The blizzard of overlapping sensory data served to **discombobulate** the freshman tennis prodigy."},
      {"author": "Tom Wolfe", "work": "The Right Stuff", "quote": "The sudden centrifuge spin was calculated to **discombobulate** the test candidate and evaluate vestibular recovery."}
    ]
  },
  "discombobulated": {
    "primary": "Confused, disconcerted, disoriented, or flustered; thrown out of one's normal composure.",
    "secondary": "In travel narrative, describing jetlagged or bewildered wanderers navigating foreign transit hubs.",
    "quotes": [
      {"author": "Hunter S. Thompson", "work": "Fear and Loathing in Las Vegas", "quote": "We stumbled into the neon casino lobby feeling thoroughly **discombobulated** after our frantic desert dash."},
      {"author": "David Foster Wallace", "work": "A Supposedly Fun Thing I'll Never Do Again", "quote": "I awoke feeling completely **discombobulated**, unable to tell cabin ceiling from bulkhead in the dark."},
      {"author": "Kurt Vonnegut", "work": "Slaughterhouse-Five", "quote": "Billy Pilgrim felt perpetually **discombobulated**, coming unstuck in time without notice or explanation."}
    ]
  },
  "discombobulation": {
    "primary": "Disorientation, confusion, or a flustered mental state provoked by sudden disruption or sensory chaos.",
    "secondary": "In psychological humor, the comic state of bafflement that follows sudden unexpected mishaps.",
    "quotes": [
      {"author": "David Foster Wallace", "work": "Brief Interviews with Hideous Men", "quote": "The awkward romantic rejection produced a wave of acute social **discombobulation** that silenced the diner."},
      {"author": "Tom Wolfe", "work": "A Man in Full", "quote": "Charlie Croker struggled against the sudden **discombobulation** brought on by hostile bank creditors."},
      {"author": "Michael Chabon", "work": "The Amazing Adventures of Kavalier & Clay", "quote": "Sammy observed the publisher's **discombobulation** with glee as the superhero sketches were unveiled."}
    ]
  },
  "discomfit": {
    "primary": "To make someone feel uneasy, embarrassed, or confused, or to defeat and overthrow an adversary.",
    "secondary": "In historical military annals, routing and throwing opposing forces into complete tactical disarray.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman cavalry counterattacked with furious momentum to **discomfit** the disorderly Gothic advance."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth's playful retorted banter served to **discomfit** Darcy's stiff reserve, forcing a reluctant smile."},
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Defeat our foes and **discomfit** their proud ranks before the setting of this auspicious sun!"}
    ]
  },
  "discomfited": {
    "primary": "Feeling uneasy, embarrassed, or thwarted, or thoroughly routed and defeated in battle.",
    "secondary": "In social dialogue, nonplussed by an unexpected moral rebuke or sharp satirical retort.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton looked thoroughly **discomfited** when Emma refused his addresses with dignified astonishment."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook sat **discomfited** in the corner, unable to reclaim his former swaggering condescension."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Templar withdrew from the tilt-yard **discomfited**, his haughty pride stung by the unknown challenger."}
    ]
  },
  "discomfiture": {
    "primary": "Embarrassment, confusion, frustration, or the defeat and thwarting of one's plans.",
    "secondary": "In military history, the total rout, collapse, or tactical humiliation of an invading army.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Caroline Bingley could not conceal her **discomfiture** when Darcy openly praised Elizabeth's fine dark eyes."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The disastrous **discomfiture** of the Roman legions in the Teutoburg forest halted imperial expansion eastward."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Uriah Heep writhed in agonizing **discomfiture** as Mr. Micawber systematically exposed his financial forgeries."}
    ]
  },
  "discomfort": {
    "primary": "A state of physical or mental unease, mild pain, embarrassment, or awkwardness.",
    "secondary": "In medicine and nursing, physical distress falling short of acute pain, such as malaise, stiffness, or nausea.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Substernal oppression and mild epigastric **discomfort** often precede severe cardiac ischemic events."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The freezing winter cold and persistent lice in the trenches were a source of ceaseless bodily **discomfort**."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Peter Walsh felt an acute social **discomfort** as he fumbled with his pocket-knife before the haughty guests."}
    ]
  },
  "discommode": {
    "primary": "To cause inconvenience, trouble, or discomfort to someone; to incommode.",
    "secondary": "In Victorian etiquette, politely requesting a favor while apologizing for any disruption caused.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse apologized repeatedly, fearing that his delicate health would **discommode** the dinner guests."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sudden arrival of the bailiffs threatened to **discommode** the entire household of Mr. Skimpole."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "Mr. Harding was anxious not to **discommode** his daughter's domestic arrangements in the quiet rectory."}
    ]
  },
  "discompose": {
    "primary": "To disturb the composure, calm, or self-possession of someone; to agitate, ruffle, or disorder.",
    "secondary": "In formal demeanor, unsettling someone's dignified exterior through unexpected news or insolence.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Nothing could **discompose** Mr. Bennet's cynical equanimity, not even Mrs. Bennet's frantic nervous complaints."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle was careful never to let sudden domestic crises **discompose** her impeccably cultivated poise."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Monsieur Paul's fierce scowl failed to **discompose** Lucy, who quietly continued correcting the French exercises."}
    ]
  }
}
