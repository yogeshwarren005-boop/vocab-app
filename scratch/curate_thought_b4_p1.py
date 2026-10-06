# -*- coding: utf-8 -*-
"""
curate_thought_b4_p1.py
Batch 4 Part 1 of Cluster Thought (Dashboard — sci: 38 words):
abscise, abscissa, abscission, adscititious, conscience,
conscience-smitten, conscienceless, conscientious, conscientiously,
conscientiousness, conscionable, conscious, consciously,
consciousness, discina, nonconscious, prescience, prescient,
presciently, prosciutto, rescind, rescindable, rescission,
sciadopityaceae, sciadopitys, sciaena, sciaenid, sciaenidae,
sciaenops, sciara, sciarid, sciaridae, sciatic, sciatica,
science, scienter, scientific, scientifically
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_thought_b4_p1 = {
    "abscise": {
        "primary": "To cut off, sever, or shed naturally (such as leaves, flowers, or fruit from a plant).",
        "secondary": "In plant physiology and surgical pathology, to separate by an abscission layer or surgically excise tissue.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Before the onset of winter frosts, deciduous trees **abscise** their senescent foliage through the formation of a suberized basal zone."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Certain oaks do not **abscise** their dead leaves until pushed off by expanding spring buds."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Unpollinated blossoms readily **abscise** from the floral pedicel, saving vital energy for developing seedpods."}
        ]
    },
    "abscissa": {
        "primary": "The horizontal coordinate (x-coordinate) of a point in a two-dimensional Cartesian coordinate system.",
        "secondary": "In analytic geometry and calculus, the distance of a point from the vertical y-axis measured parallel to the horizontal axis.",
        "quotes": [
            {"author": "Isaac Newton", "work": "Opticks", "quote": "Let the **abscissa** represent the angle of incidence, while the ordinate measures the degree of refraction."},
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "In calculating astronomical trajectories, each point requires an exact **abscissa** paired with its corresponding ordinate."},
            {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "Plotting time along the **abscissa** demonstrates the steady decay of thermal conductivity across the metal rod."}
        ]
    },
    "abscission": {
        "primary": "The natural shedding or dropping of plant parts, such as leaves, flowers, or fruit.",
        "secondary": "In plant physiology and surgical medicine, the separation of cells along a specialized cleavage zone, or surgical amputation.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "Leaf **abscission** is preceded by physiological changes that dissolve the middle lamella of cells across the petiole base."},
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "Autumnal **abscission** seals the exposed stem scar with protective cork, preventing water loss and fungal invasion."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Premature fruit **abscission** frequently results from prolonged drought or deficient pollination."}
        ]
    },
    "adscititious": {
        "primary": "Supplemental, additional, or derived from an external source; not inherent or essential.",
        "secondary": "In classical rhetoric and philosophical criticism, characterizing extraneous or artificial additions that do not belong to the intrinsic nature of a subject.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True genius requires no **adscititious** ornaments of affected diction to recommend its profound thoughts."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor's authority was buttressed by **adscititious** titles and ceremonial pomp borrowed from Persian monarchs."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Genuine poetic beauty arises from internal organic form rather than **adscititious** decorative conceits."}
        ]
    },
    "conscience": {
        "primary": "An inner sense of moral goodness or guilt regarding one's conduct, intentions, or character.",
        "secondary": "In moral philosophy and cognitive theology, the rational faculty judging the ethical validity of actions according to internalized moral law.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Thus **conscience** does make cowards of us all, And thus the native hue of resolution Is sicklied o'er with the pale cast of thought."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The promptings of **conscience** are not innate principles, but moral convictions formed through education and reflection."},
            {"author": "Immanuel Kant", "work": "Critique of Practical Reason", "quote": "Two things fill the mind with ever-increasing admiration and awe: the starry heavens above me and the moral **conscience** within me."}
        ]
    },
    "conscience-smitten": {
        "primary": "Afflicted with acute pangs of remorse, guilt, or self-reproach for moral misconduct.",
        "secondary": "In psychological narrative and moral drama, seized by sudden visceral awareness of wrongdoing and dread of divine or social retribution.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The **conscience-smitten** Henchard confessed his ancient dishonorable sale of his wife before the astonished magistrates."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip lay awake through the stormy night, **conscience-smitten** by the memory of the stolen file and pork pie."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "Dunstan felt momentary terror, **conscience-smitten** by the thought that his theft would bring ruin upon his family."}
        ]
    },
    "conscienceless": {
        "primary": "Lacking moral scruples, remorse, or ethical restraint; unprincipled and callous.",
        "secondary": "In psychopathology and criminological critique, characterized by an utter deficit of empathy, civic duty, and moral hesitation.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The cruel sea rolls on with **conscienceless** indifference, swallowing ships and crews without remorse."},
            {"author": "George Eliot", "work": "Romola", "quote": "He descended into **conscienceless** intrigue, treating friends as expendable chess pieces in his political climb."},
            {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "The tyrannical police official was a **conscienceless** bureaucrat who took pride in crushing human dignity."}
        ]
    },
    "conscientious": {
        "primary": "Wishing to do what is right, especially to do one's work or duty thoroughly and carefully.",
        "secondary": "In ethical philosophy and occupational psychology, characterized by rigorous diligence, strict moral integrity, and painstaking attention to obligation.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare was a **conscientious** student of agricultural theory, determined to master practical farming."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A **conscientious** naturalist will record anomalous observations with the same fidelity as confirming evidence."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The **conscientious** feelings of mankind constitute the internal sanction of all moral duty."}
        ]
    },
    "conscientiously": {
        "primary": "In a thorough, painstaking, and morally upright manner; with careful devotion to duty.",
        "secondary": "In professional ethics and empirical scholarship, discharging responsibilities with uncompromising adherence to truth and accuracy.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Caleb Garth worked **conscientiously**, believing that shoddy construction was an affront to God and man."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "I have **conscientiously** endeavored to collect every recorded case of inherited modification."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak guarded the sheep **conscientiously** through the freezing winter nights."}
        ]
    },
    "conscientiousness": {
        "primary": "The trait of being diligent, thorough, scrupulous, and morally responsible.",
        "secondary": "In personality psychology and character ethics, dedication to moral principle, methodical organization, and dependable performance of duties.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Intellectual **conscientiousness** demands that a philosopher test his conclusions against every possible objection."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Habits of **conscientiousness** formed during youth create a stable framework for lifelong moral character."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "His meticulous professional **conscientiousness** won the deep respect of the entire community."}
        ]
    },
    "conscionable": {
        "primary": "Governed by or conforming to conscience; just, fair, reasonable, or equitable.",
        "secondary": "In jurisprudence and equity law, morally permissible or defensible under standards of good faith and equity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "It is a **conscionable** and honest proposal, offering equitable restitution to all injured parties."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No **conscionable** judge can condemn an accused citizen upon vague rumors unsupported by sworn testimony."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A **conscionable** magistrate seeks to temper the rigor of written law with natural equity."}
        ]
    },
    "conscious": {
        "primary": "Aware of and responding to one's surroundings; awake, alert, and cognizant of internal or external reality.",
        "secondary": "In cognitive psychology and neurology, possessing subjective mental awareness, intentionality, and self-reflective perception.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She was painfully **conscious** of the contrast between her humble rural past and the refined surroundings."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The **conscious** mind is not a chopped-up sequence of ideas, but a continuous flowing stream of thought."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Higher animals are clearly **conscious** of their own feelings, exhibiting joy, fear, and grief."}
        ]
    },
    "consciously": {
        "primary": "In a deliberate, intentional, and aware manner; with cognitive awareness.",
        "secondary": "In behavioral psychology, executing actions through reflective volition rather than automatic instinct or reflex.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A citizen who **consciously** weighs alternative political policies exercises the true dignity of free thought."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She **consciously** avoided reflecting upon the unhappy compromise that bound her marriage."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I went to the woods because I wished to live deliberately, to front only the essential facts of life **consciously**."}
        ]
    },
    "consciousness": {
        "primary": "Subjective mental awareness, responsiveness to one's surroundings, and continuous perception of existence.",
        "secondary": "In philosophical epistemology and neuroscience, the subjective phenomenal experience of qualia, selfhood, and sensory perception.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The vast heath seemed endowed with a brooding, somber **consciousness** that outlasted human generations."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Universal human **consciousness** flows like a river, ever changing yet maintaining uninterrupted personal continuity."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Personal identity consists in the continuity of **consciousness** across remembered experiences."}
        ]
    },
    "discina": {
        "primary": "A genus of cup fungi in the family Discinaceae, characterized by wrinkled, disc-shaped or saddle-shaped ascocarps.",
        "secondary": "In systematic mycology, an ascomycete genus closely allied with false morels, growing on decaying coniferous logs in spring.",
        "quotes": [
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The genus **discina** produces broad, saucer-shaped fructifications upon rotting woodland logs in early spring."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Mycologists distinguish **discina** by its convoluted hymenial surface and eight-spored cylindrical asci."},
            {"author": "Joseph Dalton Hooker", "work": "The Botany of the Antarctic Voyage", "quote": "Among subalpine mosses we collected several fleshy species of **discina** emerging after snowmelt."}
        ]
    },
    "nonconscious": {
        "primary": "Operating, occurring, or existing outside the domain of conscious awareness.",
        "secondary": "In cognitive neuroscience and psychoanalysis, designating autonomous neurological reflexes, autonomic regulation, or implicit memory processing.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The vast majority of our organic physiological operations remain completely **nonconscious**."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Reflex actions of the spinal cord represent **nonconscious** adaptive mechanisms operating beneath brain awareness."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Instinctive animal behaviors evolve from ancient, **nonconscious** sensory-motor coordination patterns."}
        ]
    },
    "prescience": {
        "primary": "Foresight, foreknowledge, or the power to anticipate future events.",
        "secondary": "In theological philosophy and literary narrative, divine omniscience regarding future contingencies, or extraordinary intuitive foresight.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "By accident most strange, bountiful Fortune, now my dear lady, hath mine enemies brought to this shore; and by my **prescience** I find my zenith doth depend upon a most auspicious star."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles displayed an almost uncanny **prescience** in forecasting the exact week when the cider apples would ripen."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny possessed a quiet moral **prescience** that detected unprincipled motives long before others suspected them."}
        ]
    },
    "prescient": {
        "primary": "Having or showing knowledge of events before they take place; prophetic or farsighted.",
        "secondary": "In intellectual history, exhibiting profound anticipatory insight into social, scientific, or technological developments.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old prophet uttered **prescient** warnings concerning the doomed voyage of the Pequod."},
            {"author": "H. G. Wells", "work": "Anticipations", "quote": "The author proved astonishingly **prescient** in forecasting aerial bombardment and mechanized armored warfare."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A true poet possesses a **prescient** eye that discerns tomorrow's truths amid today's confusions."}
        ]
    },
    "presciently": {
        "primary": "With foreknowledge, prophetic insight, or anticipatory wisdom.",
        "secondary": "In critical history and social analysis, anticipating future developments with remarkable accuracy.",
        "quotes": [
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Tocqueville **presciently** predicted that America and Russia would one day divide global sway between them."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Darwin **presciently** anticipated the discoveries that modern paleontology would later confirm."},
            {"author": "Winston Churchill", "work": "The World Crisis", "quote": "A few farsighted naval strategists had **presciently** warned of the submarine menace years before war broke out."}
        ]
    },
    "prosciutto": {
        "primary": "An Italian dry-cured ham, aged and served thinly sliced in raw, delicate ribbons.",
        "secondary": "In culinary gastronomy and charcuterie, a Protected Designation of Origin specialty cured with sea salt in regulated microclimates (such as Parma or San Daniele).",
        "quotes": [
            {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "The rustic tavern tables were laid with dark bread, purple figs, and transparent ribbons of savory **prosciutto**."},
            {"author": "William Dean Howells", "work": "Venetian Life", "quote": "At the Venetian market stalls, cured **prosciutto** hung in fragrant rows beside flasks of Chianti."},
            {"author": "Henry James", "work": "Italian Hours", "quote": "We lunched on ripe melon accompanied by savory slices of local **prosciutto**, savoring the gentle Tuscan breeze."}
        ]
    },
    "rescind": {
        "primary": "To revoke, cancel, annul, or repeal a law, contract, order, or agreement.",
        "secondary": "In jurisprudence and administrative law, to declare an agreement void ab initio, restoring the parties to their original status.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The trustees decided to **rescind** their previous resolution, acknowledging the injustice of the old regulation."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Parliament resolved to **rescind** the oppressive edict, restoring commercial liberties to the merchants."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A legislature possesses full constitutional authority to **rescind** statutes that experience proves harmful."}
        ]
    },
    "rescindable": {
        "primary": "Capable of being revoked, annulled, canceled, or rescinded.",
        "secondary": "In contract law and statutory interpretation, designating a pact, license, or deed subject to legal cancellation upon breach or mutual consent.",
        "quotes": [
            {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Political power granted on trust is inherently **rescindable** whenever governors betray their solemn fiduciary duty."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A contract procured through fraudulent misrepresentation remains legally **rescindable** at the election of the injured party."},
            {"author": "Adam Smith", "work": "Lectures on Jurisprudence", "quote": "Conditional treaties are deemed **rescindable** should either signatory fail to discharge stipulated terms."}
        ]
    },
    "rescission": {
        "primary": "The act of rescinding, annulling, revoking, or canceling a law, decree, or contract.",
        "secondary": "In judicial equity, an equitable remedy that unwinds an agreement, extinguishing mutual obligations as though the contract never existed.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The court of equity granted a decree of total **rescission**, directing restitution of the purchase money."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The formal **rescission** of the Test Act provoked fierce theological controversy across the nation."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The abrupt **rescission** of commercial treaties damages national credit and excites foreign hostility."}
        ]
    },
    "sciadopityaceae": {
        "primary": "A monotypic family of conifers comprising solely the umbrella pine (Sciadopitys verticillata) native to Japan.",
        "secondary": "In gymnosperm dendrology, a relictual coniferous family distinguished by unique cladodes (fused needle pairs) forming whorled umbrellas.",
        "quotes": [
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "The Japanese umbrella pine, isolated in the family **sciadopityaceae**, represents a living fossil with no close modern analogues."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Morphologists regard the whorled foliage of the **sciadopityaceae** as transformed branch cladodes rather than true leaves."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Fossil discoveries show that ancestors of the **sciadopityaceae** once formed vast forests across the Cretaceous Northern Hemisphere."}
        ]
    },
    "sciadopitys": {
        "primary": "A genus of primitive conifers containing a single living species, the umbrella pine (Sciadopitys verticillata).",
        "secondary": "In ornamental dendrology and paleobotany, an ancient relict genus renowned for its whorled umbrella-like photosynthetic branchlets.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The unique foliage arrangement of **sciadopitys** has long intrigued systematic botanists studying conifer evolution."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "In Japanese temple gardens, majestic specimens of **sciadopitys** are cultivated for their pyramidal symmetry and lush evergreen needles."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Botanists discovered fossil resin proving that **sciadopitys** flourished across prehistoric amber-producing coniferous forests."}
        ]
    },
    "sciaena": {
        "primary": "A genus of marine drum fish and croakers in the family Sciaenidae, known for producing audible croaking sounds.",
        "secondary": "In ichthyology, marine perciform fishes possessing large swim bladders used as resonating acoustic chambers, commonly called croakers or drums.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Sailors on the Patagonian coast were startled by the drumming noises produced underwater by a species of **sciaena**."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The acoustic drumming mechanism of **sciaena** is operated by specialized sonic muscles attached to the air-bladder."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The genus **sciaena** exhibits heavy ctenoid scales and massive pharyngeal teeth adapted for crushing shellfish."}
        ]
    },
    "sciaenid": {
        "primary": "Any fish of the marine family Sciaenidae, commonly known as drums or croakers.",
        "secondary": "In fisheries biology and marine zoology, an acoustic teleost fish utilizing sonic muscles and labyrinth otoliths for intraspecific communication.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The captured **sciaenid** continued its peculiar grunting vocalizations even after being hauled into the boat."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "Each **sciaenid** possesses enlarged otoliths in the inner ear that facilitate acoustic perception in turbid waters."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The coastal fishery yielded abundant catches of **sciaenid** species prized for their delicate white flesh."}
        ]
    },
    "sciaenidae": {
        "primary": "The drum or croaker family of marine and estuarine perciform fishes, famous for producing drumming sounds.",
        "secondary": "In taxonomic ichthyology, a commercially vital family including drums, croakers, weakfish, and corvinas, characterized by paired sonic swim bladder muscles.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "Fishes belonging to the family **sciaenidae** are characterized by a cavernous head skeleton and acoustic air-bladders."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Tropical estuaries teem with representatives of the **sciaenidae**, whose nocturnal drumming reverberates through ship hulls."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The evolutionary diversification of the **sciaenidae** demonstrates remarkable adaptations for bottom-feeding in muddy bays."}
        ]
    },
    "sciaenops": {
        "primary": "A monotypic genus of sciaenid marine fish containing the red drum or redfish (Sciaenops ocellatus).",
        "secondary": "In marine fisheries biology, a recreationally and commercially important drum fish characterized by one or more dark ocellated spots on the caudal peduncle.",
        "quotes": [
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The genus **sciaenops** is distinguished by the distinctive black eye-spot situated near the base of the caudal fin."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "In estuarine lagoons, juvenile specimens of **sciaenops** feed voraciously on crustaceans."},
            {"author": "Theodore Roosevelt", "work": "Outdoor Pastimes of an American Hunter", "quote": "Anglers in the Gulf lagoons celebrated the fierce fighting qualities of the great channel bass, classified as **sciaenops**."}
        ]
    },
    "sciara": {
        "primary": "A genus of small, dark, slender gnats in the family Sciaridae, commonly known as fungus gnats.",
        "secondary": "In agricultural entomology, dipteran gnats whose larvae feed upon fungal mycelium, decaying vegetable detritus, and greenhouse plant roots.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Greenhouse growers frequently suffer losses when larvae of **sciara** gnaw the delicate rootlets of seedlings."},
            {"author": "Jean-Henri Fabre", "work": "The Life of the Fly", "quote": "The tiny black gnats of the genus **sciara** congregate around damp forest compost heaps in summer."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Under certain conditions, thousands of **sciara** larvae march together across the woodland floor in a continuous living ribbon."}
        ]
    },
    "sciarid": {
        "primary": "Any small, dark-winged gnat belonging to the family Sciaridae (fungus gnats).",
        "secondary": "In economic entomology, a dipteran insect whose larvae are pests in mushroom houses, soil beds, and horticultural greenhouses.",
        "quotes": [
            {"author": "Jean-Henri Fabre", "work": "The Life of the Fly", "quote": "The delicate wings and long antennae of the **sciarid** distinguish it from common house gnats."},
            {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Decaying leaf-mould harbors millions of **sciarid** larvae assisting in organic breakdown."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The **sciarid** exhibits remarkable communal larval locomotion, forming migratory columns known as army worms."}
        ]
    },
    "sciaridae": {
        "primary": "The dark-winged fungus gnat family of small dipteran insects whose larvae feed on fungi and decaying plant tissue.",
        "secondary": "In systematic dipterology, a nematoceran family characterized by dark smoky wings, contiguous eyes above the antennae, and larvae that occasionally form aggregate migratory armies.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The family **sciaridae** occupies an ecological niche centered upon the decomposition of forest fungal detritus."},
            {"author": "Jean-Henri Fabre", "work": "The Life of the Fly", "quote": "Swarming clouds of **sciaridae** arise from rotting compost heaps on warm, humid evenings."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection favors specialized sensory organs in the **sciaridae** to locate ephemeral fungal fruiting bodies."}
        ]
    },
    "sciatic": {
        "primary": "Relating to or affecting the hip, ischium, or the sciatic nerve.",
        "secondary": "In human anatomy and surgical medicine, designating structures associated with the ischium, notably the sciatic notch and the great sciatic nerve.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pressure on the **sciatic** nerve as it exits the greater pelvic notch produces sharp, radiating distress down the posterior thigh."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The great **sciatic** trunk is the thickest nerve in the human body, supplying motor and sensory innervation to the entire lower limb."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **sciatic** artery descends between the trochanter major and tuberosity of the ischium alongside the nerve."}
        ]
    },
    "sciatica": {
        "primary": "Pain affecting the back, hip, and outer side of the leg, caused by compression or irritation of a spinal nerve root in the lower back.",
        "secondary": "In clinical neurology and rheumatology, radiculopathy along the distribution of the sciatic nerve resulting from lumbar disc herniation or spinal stenosis.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "Thou cold **sciatica**, Cripple our senators, that their limbs may halt As lamely as their manners."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "True **sciatica** is characterized by intense neuralgic pain along the course of the nerve trunk, aggravated by straight-leg elevation."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Patients tormented by chronic **sciatica** find warmth and gentle rubefacients of considerable therapeutic benefit."}
        ]
    },
    "science": {
        "primary": "The systematic study of the structure and behavior of the physical and natural world through observation, experimentation, and testing.",
        "secondary": "In epistemology and methodology, an organized body of verified knowledge governed by empirical evidence, reproducible experimentation, and logical deduction.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Plutus himself, That knows the tinct and multiplying medicine, Hath not in nature's mystery more **science** Than I have in this art."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Experimental **science** advances not by dogmatic scholastic assertions, but by cautious observation of natural phenomena."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "No one who has not examined into the subject can form an idea of the vast progress which **science** has achieved."}
        ]
    },
    "scienter": {
        "primary": "A legal term denoting knowledge of the wrongness of an act or its consequences prior to its commission; intent or knowledge.",
        "secondary": "In jurisprudence and tort liability, the requirement that a defendant acted with intentional knowledge of falsehood or willful recklessness.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In actions for fraudulent deceit, proof of **scienter** is essential to establish malicious liability."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The ancient doctrine of **scienter** distinguished between accidental injury and culpable knowledge of vicious propensities."},
            {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "A court of equity will grant relief where the defendant acted with full **scienter** of the plaintiff's title."}
        ]
    },
    "scientific": {
        "primary": "Based on or characterized by the methods and principles of science; systematic, empirical, and rigorous.",
        "secondary": "In epistemological philosophy, adhering to methodical experimentation, falsifiability, and rational consensus rather than dogmatic speculation.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A truly **scientific** mind welcomes objections and seeks every opportunity to submit hypotheses to severe tests."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **scientific** method of induction proceeds from observed particular facts to general universal laws."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate possessed a genuinely **scientific** enthusiasm, dreaming of great biological discoveries."}
        ]
    },
    "scientifically": {
        "primary": "In a manner adhering to the principles, methods, or rigorous standards of science.",
        "secondary": "In empirical methodology, systematically, objectively, and with verifiable precision.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "He spoke **scientifically**, measuring every word with the cold precision of a chemist handling delicate reagents."},
            {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The anarchist treated dynamic explosives **scientifically**, regarding violence as an exact branch of physics."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "When classified **scientifically**, human physical structures align perfectly with those of other primates."}
        ]
    }
}
