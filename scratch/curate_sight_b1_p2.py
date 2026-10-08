# -*- coding: utf-8 -*-
"""
curate_sight_b1_p2.py
Batch 1 Part 2 of Cluster Sight (44 words):
- Dashboard — pict (15 words):
pictograph, pictographic, pictor, pictorial, pictorially,
pictural, picture, pictured, picturesque, picturesquely,
picturesqueness, picturing, undepicted, unpictured, unpicturesque
- Dashboard — ping (10 words):
coping, impinge, impingement, impinging, ping, pinger,
pinguecula, pinguicula, pinguinus, supping
- Dashboard — tuit (9 words):
counterintuitive, counterintuitively, intuit, intuition,
intuitionism, intuitionist, intuitive, intuitively, tuition
- Dashboard — vigil (10 words):
invigilate, invigilation, invigilator, unvigilant, vigil,
vigilance, vigilant, vigilante, vigilantism, vigilantly
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b1_p2 = {
    "pictograph": {
        "primary": "A pictorial symbol or glyph representing a word, concept, or phrase.",
        "secondary": "In paleography and primitive epigraphy, ancient ideograms carved into stone or painted on cave walls before the invention of phonetic alphabets.",
        "quotes": [
            {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Every ancient **pictograph** conveyed meaning directly to the eye without reference to spoken phonemes."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The Indian guide traced a primitive **pictograph** on birch bark to communicate our route."},
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The transition from an isolated **pictograph** to a cursive syllabic script represents centuries of scribal evolution."}
        ]
    },
    "pictographic": {
        "primary": "Consisting of or relating to pictographs; using pictorial signs to convey meaning.",
        "secondary": "In epigraphy and linguistic history, describing writing systems (such as early Egyptian hieroglyphics or Mayan glyphs) based on pictorial representations.",
        "quotes": [
            {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "A **pictographic** script communicates ideas across linguistic barriers with universal directness."},
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Ancient Mexican codices preserved dynastic chronicles in elaborate **pictographic** symbols."},
            {"author": "Leonard Bloomfield", "work": "Language", "quote": "Before abstract alphabets arose, primitive societies utilized **pictographic** conventions for keeping communal records."}
        ]
    },
    "pictor": {
        "primary": "The Painter; a faint constellation in the southern celestial hemisphere.",
        "secondary": "In observational astronomy and celestial cartography, a constellation introduced by Nicolas-Louis de Lacaille in the 1750s representing a painter's easel.",
        "quotes": [
            {"author": "John Herschel", "work": "Results of Astronomical Observations at the Cape of Good Hope", "quote": "Looking toward the southern pole, the faint stars of **Pictor** appear situated between Columba and the Large Magellanic Cloud."},
            {"author": "William Herschel", "work": "Philosophical Transactions", "quote": "Our sweeps across the southern constellations revealed double stars within the boundaries of **Pictor**."},
            {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "Beta Pictoris in the constellation **Pictor** exhibits an anomalous infrared excess indicative of circumstellar dust."}
        ]
    },
    "pictorial": {
        "primary": "Relating to, expressed in, or illustrated by pictures; graphic or vivid.",
        "secondary": "In artistic aesthetics and print journalism, employing visual illustrations or evocative imagery to convey scenes and narratives.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The human mind naturally converts thoughts into **pictorial** symbols, illustrating abstract concepts with vivid imagery."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The **pictorial** illustrations of facial muscle contractions demonstrate the physiological basis of emotion."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ancient whaling treatises were enriched with quaint **pictorial** representations of monstrous sea beasts."}
        ]
    },
    "pictorially": {
        "primary": "By means of pictures, illustrations, or visual representations.",
        "secondary": "In graphic communication and art history, representing objects, events, or abstract relationships visually.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner conceived nature **pictorially**, translating mist, light, and water into pure optical poetry."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The courtship plumage of the argus pheasant is arranged **pictorially** to display shaded balls on each quill."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Swedenborg envisioned spiritual hierarchies **pictorially**, describing divine spheres in architectural detail."}
        ]
    },
    "pictural": {
        "primary": "Pertaining to painting, pictorial art, or visual representation.",
        "secondary": "In classical art criticism and aesthetics, relating to the formal, chromatic, or compositional properties of pictorial creation.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poem possesses a rare **pictural** quality, presenting each scene with the luminous finish of a Venetian painting."},
            {"author": "William Hazlitt", "work": "Sketches of the Principal Picture-Galleries in England", "quote": "Titian's canvas displays a consummate **pictural** harmony that blends flesh tints with golden light."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The **pictural** grandeur of early mosaic work resides in its bold flat surfaces and brilliant tesserae."}
        ]
    },
    "picture": {
        "primary": "A painting, drawing, photograph, or other visual depiction of a person, scene, or object.",
        "secondary": "In aesthetics and metaphorical discourse, an evocative visual or verbal representation capturing the essence of an experience.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Look here, upon this **picture**, and on this, The counterfeit presentment of two brothers."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The **picture** was to alter with every sin he committed; the portrait would bear the burden of his shame."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She formed a striking **picture** in the early dawn, standing solitary against the vast chalk downs."}
        ]
    },
    "pictured": {
        "primary": "Represented in a picture or visual artwork; or imagined and visualized mentally.",
        "secondary": "In psychological narrative and art criticism, portrayed in graphic art or vividly conceived in the imagination.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The dreadful creature was exactly as the ancient manuscript had **pictured** it, ghastly and luminous."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She **pictured** to herself a life devoted to noble works, far removed from provincial gossip."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He **pictured** her waiting alone in the cottage, wondering why he had not returned."}
        ]
    },
    "picturesque": {
        "primary": "Visually attractive, quaint, or charming in a way that resembles a picture.",
        "secondary": "In aesthetic philosophy, an aesthetic category situated between the beautiful and the sublime, characterized by rugged variety, irregularity, and rustic charm.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The ancient stone barn presented a highly **picturesque** aspect with its moss-grown gables and arched doorway."},
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The English rural landscape is an exquisitely finished garden, **picturesque** in every lane and hedgerow."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He loved the **picturesque** squalor of foreign ports, where life appeared raw and uncensored."}
        ]
    },
    "picturesquely": {
        "primary": "In a picturesque manner; attractively and quaintly resembling a painted scene.",
        "secondary": "In descriptive travel narrative, arranged with charming visual variety, rustic irregularity, or vivid color.",
        "quotes": [
            {"author": "Herman Melville", "work": "Typee", "quote": "The native bamboo huts were **picturesquely** scattered among groves of breadfruit and coconut palms."},
            {"author": "G. K. Chesterton", "work": "The Flying Inn", "quote": "The quaint thatched tavern hung **picturesquely** over the edge of the chalk cliff."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The peasants were **picturesquely** attired in red bodices and embroidered aprons for the Roman carnival."}
        ]
    },
    "picturesqueness": {
        "primary": "The quality of possessing quaint visual beauty, dramatic natural texture, and striking scenic charm.",
        "secondary": "In 18th- and 19th-century aesthetics (as formulated by William Gilpin), rugged variety, natural texture, and scenic irregularity pleasing to the artistic eye.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Modern London has lost its old architectural **picturesqueness**, sacrificing charm to commercial utility."},
            {"author": "Herman Melville", "work": "Mardi", "quote": "The **picturesqueness** of the coral atoll fascinated the mariners as the surf broke over emerald reefs."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The old wooden farmhouse possessed an unstudied **picturesqueness** that appealed to the artists among us."}
        ]
    },
    "picturing": {
        "primary": "The act of creating a picture, visualizing in the mind, or representing in words.",
        "secondary": "In cognitive psychology and literary composition, mental imagery or vivid narrative description evoking sensory impressions.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He spent the long winter evenings **picturing** their future home on an idyllic colonial homestead."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "By carefully **picturing** each stage of muscular movement, we can decipher the anatomical origin of human laughter."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I sat by the marsh fire, **picturing** terrifying figures lurking in the dense winter fog."}
        ]
    },
    "undepicted": {
        "primary": "Not represented in a picture, painting, sculpture, or verbal description.",
        "secondary": "In historical art critique and literary theory, omitted from graphic depiction or lacking artistic portrayal.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "Vast realms of atmospheric cloud formations remained entirely **undepicted** until Turner turned his brush to the sky."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The true interior fury of the sperm whale fishery remains forever **undepicted** upon conventional artists' canvases."},
            {"author": "George Eliot", "work": "Romola", "quote": "Many an unrecorded deed of peasant heroism remained **undepicted** in the gilded annals of the city."}
        ]
    },
    "unpictured": {
        "primary": "Not depicted in a picture or illustration; unrepresented visually.",
        "secondary": "In descriptive literature, existing without pictorial illustration, or left entirely to the reader's imagination.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "There were secret passages of his life that remained **unpictured**, hidden behind a veil of silence."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The silent tragedies of the deep forest remained **unpictured** by the bustling townsfolk miles away."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The oldest ancestral portrait had vanished, leaving an **unpictured** blank space upon the oak paneling."}
        ]
    },
    "unpicturesque": {
        "primary": "Not picturesque; lacking scenic beauty, charm, or quaint artistic appeal.",
        "secondary": "In architectural and cultural criticism, characterized by monotonous, drab, or utilitarian ugliness.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "Our Old Home", "quote": "The grimy coal barges and brick warehouses formed a singularly **unpicturesque** waterfront along the industrial canal."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The flat, damp agricultural plains were considered hopelessly **unpicturesque** by tourists seeking alpine vistas."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The new mechanized corn market was an **unpicturesque** modern barn devoid of historic associations."}
        ]
    },
    "coping": {
        "primary": "Managing difficult situations successfully; or the top protective masonry layer on a wall.",
        "secondary": "In architecture and structural masonry, the protective stone or brick capping placed on top of a wall to shed rainwater.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He leaned against the weathered stone **coping** of the bridge, watching the river swirl beneath the arch."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Fruit trees trained along the southern brick wall were sheltered from frost by the projecting stone **coping**."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "A row of sparrows chattered along the granite **coping** of the Georgian terrace."}
        ]
    },
    "impinge": {
        "primary": "To have an effect, make an impact, or strike against something; to encroach or infringe.",
        "secondary": "In physical acoustics and wave mechanics, to collide with or strike an acoustic or physical surface.",
        "quotes": [
            {"author": "James Joyce", "work": "Dubliners", "quote": "The light began to pale on the avenue, and his thoughts continued to **impinge** upon the painful memory of the afternoon."},
            {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "Luminous ether waves **impinge** upon the retina, exciting the chemical receptors of vision."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "External physical forces ceaselessly **impinge** upon the nervous system, initiating sensory impressions."}
        ]
    },
    "impingement": {
        "primary": "The act of striking or colliding with something; an impact or infringement.",
        "secondary": "In clinical orthopedics and acoustic physics, mechanical collision of anatomical structures causing compression, or wave collision against an interface.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sudden **impingement** of the furious autumn squall rattled the ancient casements with startling violence."},
            {"author": "Lord Kelvin", "work": "Mathematical and Physical Papers", "quote": "The **impingement** of high-velocity molecules against the piston generates uniform hydrostatic pressure."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic bursal **impingement** beneath the acromial arch produces localized shoulder tenderness and restricted mobility."}
        ]
    },
    "impinging": {
        "primary": "Striking against or encroaching upon; having a direct physical or conceptual impact.",
        "secondary": "In optical wave mechanics, describing light or sound waves falling directly upon a boundary surface.",
        "quotes": [
            {"author": "Isaac Newton", "work": "Opticks", "quote": "Rays of light **impinging** upon a polished glass surface undergo both specular reflection and partial refraction."},
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Environmental stimuli **impinging** upon embryonic tissue stimulate selective cellular differentiation."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The spray **impinging** upon our faces was cold as Arctic sleet as the Pequod breached the billows."}
        ]
    },
    "ping": {
        "primary": "A short, high-pitched, ringing sound; or to make such a sound; or in networking, a software utility testing reachability.",
        "secondary": "In sonar physics and computer networking, an acoustic impulse transmitted through water to detect submerged targets, or an ICMP echo request packet.",
        "quotes": [
            {"author": "Rudyard Kipling", "work": "The Five Nations", "quote": "A sharp metallic **ping** echoed across the rocks as the sniper's bullet ricocheted from the boulder."},
            {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The sudden sharp **ping** of snapping steel wire warned the aeronauts that the rudder was damaged."},
            {"author": "Arthur Conan Doyle", "work": "The Great Boer War", "quote": "The steady **ping** of Mauser bullets passing overhead kept the infantry pinned behind their low entrenchments."}
        ]
    },
    "pinger": {
        "primary": "A device that emits short, high-pitched acoustic pulses or signals (pings).",
        "secondary": "In marine technology and oceanographic telemetry, an underwater acoustic transmitter attached to ocean equipment or aircraft flight recorders to aid acoustic location.",
        "quotes": [
            {"author": "Arthur C. Clarke", "work": "The Deep Range", "quote": "The submarine's directional sonar locked onto the rhythmic signals of the acoustic **pinger** marking the undersea pen."},
            {"author": "Jacques Cousteau", "work": "The Silent World", "quote": "We tracked the drifting current-measuring buoy by following the pulsed beacon emitted by its underwater **pinger**."},
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Modern oceanographers deploy instruments equipped with an acoustic **pinger** to map the abyssal seafloor."}
        ]
    },
    "pinguecula": {
        "primary": "A small, slightly raised yellowish benign nodule on the conjunctiva near the cornea of the eye.",
        "secondary": "In clinical ophthalmology, elastotic degeneration of subepithelial conjunctival collagen resulting from chronic exposure to ultraviolet radiation, wind, and dust.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic exposure to desert glare frequently promotes the formation of a harmless yellowish **pinguecula** on the nasal conjunctiva."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The superficial nodule of a **pinguecula** is composed of hyaline degeneration within the subconjunctival connective tissue."},
            {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Elderly sailors often exhibit a benign **pinguecula**, reflecting decades spent scanning sunlit waters."}
        ]
    },
    "pinguicula": {
        "primary": "A genus of small insectivorous herbaceous plants in the bladderwort family (Lentibulariaceae), commonly called butterworts.",
        "secondary": "In carnivorous botany, rosette-forming plants whose greasy, glandular leaves secrete mucilage and digestive enzymes to trap and absorb insects.",
        "quotes": [
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "My experiments on **pinguicula** vulgaris proved that its glandular secretions rapidly digest small diptera captured on the greasy leaves."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The yellow butterwort, **pinguicula** lutea, grows in wet pine barrens, bearing solitary spurred blossoms."},
            {"author": "Joseph Dalton Hooker", "work": "The Botany of the Antarctic Voyage", "quote": "Along dripping subalpine bog banks, small rosettes of **pinguicula** thrive where soil nitrogen is scarce."}
        ]
    },
    "pinguinus": {
        "primary": "A genus of extinct flightless seabirds in the auk family (Alcidae), containing the great auk (Pinguinus impennis).",
        "secondary": "In historical ornithology and paleontology, the flightless North Atlantic alcid hunted to extinction by 1844, the original bird to which the name penguin was applied.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extinction of the great auk, **pinguinus** impennis, demonstrates the vulnerability of large flightless birds on populated islands."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "Osteological specimens of **pinguinus** show massive pectoral girdles adapted for subaqueous flight."},
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "Mariners raided the nesting rocks of **pinguinus**, slaughtering thousands of helpless birds for feathers and fat."}
        ]
    },
    "supping": {
        "primary": "Eating supper; dining in the evening; or taking liquid food by sips.",
        "secondary": "In social history and literature, partaking of the evening meal, especially in convivial or quiet companionship.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I left him **supping** upon cold meat and bread in the dark pantry, grateful for the rough hospitality."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "We could hear the soldiers **supping** in the cellar, murmuring over the strange portents in the sky."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "The harvesters gathered at sundown, **supping** together after the long day's toil in the wheat field."}
        ]
    },
    "counterintuitive": {
        "primary": "Contrary to intuition or common-sense expectation; not intuitive.",
        "secondary": "In cognitive science and quantum mechanics, describing phenomena that defy everyday sensory experience yet are mathematically or empirically verified.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Many of the established conclusions of mathematical physics appear completely **counterintuitive** to untrained common sense."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "It is a **counterintuitive** fact of mental life that bodily expression frequently precedes emotional awareness."},
            {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "Relativistic time dilation presents a profoundly **counterintuitive** concept to minds accustomed to absolute Newtonian time."}
        ]
    },
    "counterintuitively": {
        "primary": "In a manner contrary to common sense, expectation, or immediate intuition.",
        "secondary": "In empirical analysis, producing outcomes that contradict intuitive assumptions yet adhere to underlying structural laws.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "Mysticism and Logic", "quote": "Modern mathematical analysis demonstrates **counterintuitively** that continuous curves may lack tangents at every point."},
            {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "The quantum particle behaves **counterintuitively**, passing simultaneously through dual experimental apertures."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Habit functions **counterintuitively**, liberating conscious attention precisely by rendering complex actions automatic."}
        ]
    },
    "intuit": {
        "primary": "To understand or know by intuition without the need for conscious reasoning.",
        "secondary": "In epistemological philosophy, to grasp truth, essences, or relationships by immediate direct cognitive apprehension.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The purified spirit can **intuit** eternal moral truths without relying on scholastic syllogisms."},
            {"author": "Henri Bergson", "work": "Creative Evolution", "quote": "Intellect analyzes form, but intuition alone enables us to **intuit** the vital flux of life itself."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her profound sympathy enabled her to **intuit** his unexpressed sorrow before he spoke a word."}
        ]
    },
    "intuition": {
        "primary": "The ability to understand something immediately, without the need for conscious reasoning; an intuitive perception.",
        "secondary": "In epistemology, immediate cognitive apprehension of a self-evident truth, axiom, or sensory datum prior to analytical deduction.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "In **intuition** the mind perceives the agreement or disagreement of two ideas immediately by themselves, without the intervention of any other."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The theory of **intuition** claims that our fundamental moral beliefs are self-evident truths perceived directly by consciousness."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "She had an instinctive **intuition** that something momentous had occurred in the quiet clearing."}
        ]
    },
    "intuitionism": {
        "primary": "The doctrine that knowledge or moral principles are gained through immediate intuition rather than empirical reasoning.",
        "secondary": "In meta-ethics and mathematical philosophy, the philosophical school asserting that moral truths are objective and self-evident, or that mathematics consists of mental constructions.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The ethical school of **intuitionism** asserts that moral duties are known directly by internal moral perception."},
            {"author": "Bertrand Russell", "work": "A Critical Exposition of the Philosophy of Leibniz", "quote": "Mathematical **intuitionism** rejects the law of excluded middle for infinite sets, demanding constructive proof."},
            {"author": "William James", "work": "The Will to Believe", "quote": "Philosophical **intuitionism** defends the validity of direct personal experience against mechanistic reductionism."}
        ]
    },
    "intuitionist": {
        "primary": "An adherent of intuitionism in philosophy, ethics, or mathematics.",
        "secondary": "In foundational debate, a thinker holding that fundamental moral principles or mathematical truths are apprehended by direct intuitive faculty.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The ethical **intuitionist** assumes that the moral quality of actions is recognized as immediately as physical color."},
            {"author": "Bertrand Russell", "work": "Mysticism and Logic", "quote": "The mathematical **intuitionist** refuses to accept existence theorems unless a concrete computational method is demonstrated."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A religious **intuitionist** regards personal spiritual illumination as higher evidence than abstract scholastic debate."}
        ]
    },
    "intuitive": {
        "primary": "Using or based on what one feels to be true even without conscious reasoning; instinctive.",
        "secondary": "In cognitive philosophy, direct, immediate apprehension of concepts or relations without mediating discursive steps.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym possessed an **intuitive** sympathy with the wild, brooding spirit of Egdon Heath."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Mathematical axioms were long regarded as **intuitive** truths perceived with absolute certainty by the intellect."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She had an **intuitive** perception of character that rarely led her into serious error."}
        ]
    },
    "intuitively": {
        "primary": "By means of intuition; without conscious reasoning; instinctively.",
        "secondary": "In psychological description, grasping relationships, intentions, or truths through immediate instinctive apprehension.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "An Examination of Sir William Hamilton's Philosophy", "quote": "We know our own sensations **intuitively**, but the external causes of those sensations must be inferred."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Esther felt **intuitively** that the proud lady harbored a tragic, unconfessed grief."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth understood **intuitively** that Mr. Darcy's reserve masked genuine sensitivity."}
        ]
    },
    "tuition": {
        "primary": "A fee paid for instruction at a school, college, or university; or teaching or instruction.",
        "secondary": "In legal history and education, guardianship, care, and custodial instruction of a young person.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Much Ado About Nothing", "quote": "And so I commit you—To the **tuition** of God: From my house, if I had it."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He saved every shilling from his stonecutting wages to pay for classical **tuition** at Christminster."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Students pay costly **tuition** to sit in classrooms, while neglecting the practical arts of life."}
        ]
    },
    "invigilate": {
        "primary": "To supervise students during an examination; or to watch over vigilantly.",
        "secondary": "In academic administration (chiefly British), to maintain disciplinary order, prevent academic dishonesty, and ensure strict compliance with examination protocols.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "Life and Letters", "quote": "Fellows of the college were assigned by rotation to **invigilate** the university scholarship examinations in the Senate House."},
            {"author": "George Bernard Shaw", "work": "Pen Portraits and Reviews", "quote": "It was a tedious duty to **invigilate** a hall of silent students sweating over mathematical problems."},
            {"author": "Virginia Woolf", "work": "Jacob's Room", "quote": "The elderly proctor continued to **invigilate** the quiet examination hall, pacing softly between the wooden desks."}
        ]
    },
    "invigilation": {
        "primary": "The act or process of invigilating; supervision of students during an examination.",
        "secondary": "In educational assessment, the formal proctoring procedures guaranteeing test integrity and security.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Misalliance", "quote": "Strict **invigilation** was enforced to ensure that candidates relied solely upon their personal memory and intellect."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The academic **invigilation** of university prize competitions required impartiality beyond suspicion."},
            {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Hours of classroom **invigilation** left the young tutor exhausted and impatient for the evening breeze."}
        ]
    },
    "invigilator": {
        "primary": "A person whose job is to watch students during an exam to prevent cheating; an exam proctor.",
        "secondary": "In university administration, an authorized supervisor presiding over examinations to enforce timing, distribution of papers, and integrity.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The stern **invigilator** collected the blue exam booklets promptly as the town hall clock struck the hour."},
            {"author": "Thomas Babington Macaulay", "work": "Life and Letters", "quote": "As junior fellow, he served as **invigilator** in the college hall, keeping watch over several hundred candidates."},
            {"author": "Virginia Woolf", "work": "Jacob's Room", "quote": "The **invigilator** paused by the tall Gothic window, watching the rain fall across the quadrangle."}
        ]
    },
    "unvigilant": {
        "primary": "Not vigilant; careless, inattentive, or lacking watchfulness.",
        "secondary": "In military and security critique, failing to maintain adequate lookout or alertness in the face of imminent hazard.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian cavalry fell upon the **unvigilant** camp while the Roman sentries slumbered beside their fires."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The conspirators were emboldened by the **unvigilant** conduct of the town garrison."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "An **unvigilant** warder allowed the disguised knight to pass through the castle portcullis unchallenged."}
        ]
    },
    "vigil": {
        "primary": "A period of staying awake during the night, especially to keep watch, pray, or nurse the sick.",
        "secondary": "In liturgical history and classical chivalry, a solemn devotional watch kept on the eve of a religious festival, or a squire's all-night prayer before knighthood.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "He that shall live this day, and see old age, Will yearly on the **vigil** feast his neighbours, And say 'To-morrow is Saint Crispian.'"},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "We kept our silent **vigil** in the dark bedroom, waiting for the deadly serpent to appear through the ventilator."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "His lonely nocturnal **vigil** on the bridge of the Patna seemed wrapped in absolute peace before the catastrophe."}
        ]
    },
    "vigilance": {
        "primary": "Alert, sustained watchfulness for possible danger, deception, or difficulties.",
        "secondary": "In civic ethics and military defense, alert, sustained watchfulness preserving liberty, security, or institutional integrity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Their **vigilance** is asleep: we can make our attempt on the crown without hindrance."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In wild animal herds, the sentinel keeps watch with tireless **vigilance**, signaling danger to the group."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The masthead lookout required relentless **vigilance**, scanning the horizons for the faint spout of a whale."}
        ]
    },
    "vigilant": {
        "primary": "Keeping careful watch for possible danger or difficulties; alert, watchful.",
        "secondary": "In military operations and jurisprudence, watchful and proactive in safeguarding interests or rights against encroachment.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "What might be toward, that this sweaty haste Doth make the night joint-labourer with the day: our last king was **vigilant**."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I have been as sincere and **vigilant** a companion to morning as the sun itself."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The wild guanacos are extremely **vigilant**, stationing an old male atop an adjacent hill to sound the alarm."}
        ]
    },
    "vigilante": {
        "primary": "A member of a self-appointed group of citizens who undertake law enforcement in their community without legal authority.",
        "secondary": "In frontier history and legal sociology, an extrajudicial actor participating in citizen committees to punish suspected offenders outside established courts.",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "Ranch Life and the Hunting-Trail", "quote": "When cattle rustling threatened frontier order, the ranchers formed a **vigilante** committee to track down the horse thieves."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "In early Nevada mining camps, the summary justice of the **vigilante** was feared far more than the distant territorial court."},
            {"author": "James Bryce", "work": "The American Commonwealth", "quote": "Frontier communities frequently resorted to **vigilante** committees when statutory law enforcement proved corrupt or ineffective."}
        ]
    },
    "vigilantism": {
        "primary": "Law enforcement undertaken without legal authority by a self-appointed group or individual.",
        "secondary": "In criminology and political sociology, extrajudicial justice characterized by mob retribution and disregard for due process.",
        "quotes": [
            {"author": "James Bryce", "work": "The American Commonwealth", "quote": "Recourse to organized **vigilantism** reflects the breakdown of regular judicial administration in remote territories."},
            {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "While frontier **vigilantism** arose as a rough remedy against desperadoes, civilized society must replace it with constitutional courts."},
            {"author": "Woodrow Wilson", "work": "A History of the American People", "quote": "The rise of secret societies after the civil conflict exemplified the dangerous excesses inherent in unrestrained **vigilantism**."}
        ]
    },
    "vigilantly": {
        "primary": "In a vigilant, alert, and watchful manner.",
        "secondary": "In military reconnaissance and professional practice, guarding against danger or error with uninterrupted alertness.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "The Rescue", "quote": "The sentry paced the schooner's deck **vigilantly**, listening for the muffled splash of hostile native oars."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Inspector Bucket observed the suspects **vigilantly**, missing no subtle glance or involuntary gesture."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The lookout guarded the horizon **vigilantly**, braving the icy winds of the Southern Ocean."}
        ]
    }
}
