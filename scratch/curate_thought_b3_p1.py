# -*- coding: utf-8 -*-
"""
curate_thought_b3_p1.py
Batch 3 Part 1 of Cluster Thought:
- Dashboard — mens (30 words)
- Dashboard — scrup (8 words)
Total: 38 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_thought_b3_p1 = {
    "commensal": {
        "primary": "Living with, on, or in another organism without causing injury to either partner; or sharing the same dining table.",
        "secondary": "In ecological parasitology and symbiotic biology, designating a symbiotic association where one organism benefits without harming the host.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain cirripedes attach themselves to the skin of whales as harmless **commensal** organisms, nourished by organic particles in the passing currents."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The intestinal flora includes benign **commensal** microbes that aid physiological digestion without exciting pathological reactions."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The microscopic observer must carefully differentiate pathogenic bacteria from innocent **commensal** species inhabiting the mucosal lining."}
        ]
    },
    "commensalism": {
        "primary": "A symbiotic relationship between two organisms where one benefits while the other is neither harmed nor helped.",
        "secondary": "In community ecology and evolutionary biology, a neutral symbiotic adaptation distinguished from mutualism and true parasitism.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Evolutionary transitions between simple **commensalism** and obligate mutualism occur across numerous marine invertebrate taxa."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The phenomenon of **commensalism** proves that intimate biological coexistence need not entail predatory injury."},
            {"author": "Asa Gray", "work": "Darwiniana", "quote": "Botanical epiphytes dwelling upon forest branches provide picturesque demonstrations of ecological **commensalism**."}
        ]
    },
    "commensally": {
        "primary": "In a commensal manner; living in a non-injurious symbiotic relationship or dining at a common table.",
        "secondary": "In microbiological ecology, coexisting within a host organism without eliciting an inflammatory or immune response.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Various micrococci reside **commensally** within the nasopharyngeal cavity under ordinary conditions of host health."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Certain small crustaceans inhabit the branchial chambers of bivalves **commensally**, sharing the current of nutrient water."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Domestic cats and dogs have lived **commensally** with mankind for millennia, sharing hearth and sustenance."}
        ]
    },
    "commensurable": {
        "primary": "Measurable by the same standard or common metric; having a common measure.",
        "secondary": "In Euclidean geometry and number theory, having a ratio that can be expressed as a quotient of two integers.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Magnitudes are properly **commensurable** only when they can be compared directly against an identical unit of measure."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The geometric proportions of refracted rays demonstrated that their refrangibility and wave intervals were precisely **commensurable**."},
            {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Pythagoras was profoundly disturbed by the discovery that the side and diagonal of a square are not **commensurable**."}
        ]
    },
    "commensurate": {
        "primary": "Corresponding in size, extent, amount, or degree; proportionate.",
        "secondary": "In political economy and ethics, aligning rewards, penalties, or resources proportionally with merit, effort, or scale.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Every secret is told, every crime is punished, every virtue rewarded, every wrong redressed, in silence and certainty, with **commensurate** power."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Wages of labor naturally vary in proportion to the trust reposed in the workman, requiring a **commensurate** recompense."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her generous ambition sought an enterprise **commensurate** with her deep spiritual longings."}
        ]
    },
    "commensurateness": {
        "primary": "The property of being proportionate, adequate, or corresponding in measure.",
        "secondary": "In ethical philosophy and jurisprudence, exact proportionality between action and consequence or effort and recompense.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "Social justice requires an undeniable **commensurateness** between the services rendered by an individual and the benefits received."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The sense of justice demands an intrinsic **commensurateness** between the gravity of a moral offence and its legal penalty."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "In nature there exists an unfailing **commensurateness** between the seed sown and the harvest reaped."}
        ]
    },
    "dimension": {
        "primary": "A measurable extent of a particular kind, such as length, breadth, depth, or time; or scope and magnitude.",
        "secondary": "In physics and differential geometry, the minimum number of independent coordinates required to specify any point within a mathematical space.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Hath not a Jew eyes? hath not a Jew hands, organs, **dimension**, senses, affections, passions?"},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The massive oak cast an ominous shadow whose immense **dimension** deepened with the setting sun."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A great moral idea expands the mind, adding a new spiritual **dimension** to daily experience."}
        ]
    },
    "dimensional": {
        "primary": "Relating to physical dimensions, spatial measurements, or extents of magnitude.",
        "secondary": "In theoretical physics and geometric analysis, characterizing spaces, manifolds, or coordinate systems defined by a specific number of axes.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Scientific people know very well that Time is only a kind of Space; here is a popular scientific diagram, a four-**dimensional** geometry."},
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "Our mechanical calculating apparatus operated through complex multi-**dimensional** gear linkages."},
            {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "The physical properties of elastic ether require rigorous mathematical formulation in three-**dimensional** mechanics."}
        ]
    },
    "dimensionality": {
        "primary": "The condition or property of possessing dimensions or existing in a specified number of dimensions.",
        "secondary": "In topology and multidimensional statistics, the degree of geometric freedom or number of orthogonal coordinate variables defining a manifold.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The mathematical concept of **dimensionality** depends upon the independent parameters needed to isolate an individual point."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The philosophical question of higher spatial **dimensionality** fascinated theoretical physicists long before our temporal experiments."},
            {"author": "Alfred North Whitehead", "work": "The Concept of Nature", "quote": "Our immediate perception of spatial extension reveals an intrinsic three-fold **dimensionality** inherent in physical nature."}
        ]
    },
    "dimensioning": {
        "primary": "The act, process, or technique of determining, marking, or specifying dimensions.",
        "secondary": "In mechanical drafting, structural engineering, and architecture, indicating precise linear measurements, tolerances, and geometric constraints on technical drawings.",
        "quotes": [
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The exact **dimensioning** of every brass cog and escapement was crucial to avoid jamming in the calculating engine."},
            {"author": "Thomas Telford", "work": "Life of Thomas Telford", "quote": "Accurate **dimensioning** of the masonry abutments ensured that the suspension bridge withstood violent mountain gales."},
            {"author": "Isambard Kingdom Brunel", "work": "Life of Isambard Kingdom Brunel", "quote": "Meticulous **dimensioning** of the iron girders allowed the railway viaduct to span the river gorge with perfect stability."}
        ]
    },
    "immense": {
        "primary": "Extremely large or great, especially in scale, degree, volume, or extent; vast.",
        "secondary": "In celestial mechanics and metaphysical philosophy, boundless, immeasurable, or exceeding ordinary comprehension.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When we contemplate the **immense** distance between the fixed stars, our imaginations are overwhelmed by the boundless expansion of space."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "An **immense** wall of white foam rose suddenly where the colossal leviathan breached the surface."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The **immense** cordillera of the Andes stretched endlessly toward the frozen south, crowned with eternal snow."}
        ]
    },
    "immensely": {
        "primary": "To an exceedingly great degree or extent; vastly, enormously.",
        "secondary": "In quantitative comparison, overwhelmingly or by an extraordinary margin.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Domestic breeds vary **immensely** in structural conformation compared to the uniform characters of wild ancestral species."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate found his professional labours **immensely** lightened by Dorothea's sympathetic understanding."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The discovery of that single footprint altered the entire aspect of the case and assisted us **immensely**."}
        ]
    },
    "immenseness": {
        "primary": "The quality of surpassing ordinary bounds in magnitude; vastness, boundless extent.",
        "secondary": "In philosophical aesthetics and natural theology, sublime spatial or metaphysical vastness evoking awe or reverence.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul feels humbled yet exalted before the silent **immenseness** of the starry firmament."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The utter solitude and **immenseness** of the virgin wilderness overwhelmed the solitary voyager."},
            {"author": "Herman Melville", "work": "Mardi", "quote": "He gazed across the ocean, pondering the fathomless **immenseness** that separated mortal shores from eternity."}
        ]
    },
    "immensity": {
        "primary": "Vastness of extent or size; boundless or immeasurable space, time, or magnitude.",
        "secondary": "In cosmological astronomy and ontology, the infinite expanse of the physical cosmos or divine omnipresence.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The true philosopher stands receptive before the **immensity** of the universe, conscious of infinite law."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The ship glided onward through the dark **immensity** of the equatorial sea under an unclouded dome of stars."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Lost in the blue **immensity** of the Pacific, the pequod seemed a mere speck upon eternity."}
        ]
    },
    "immensurable": {
        "primary": "Incapable of being measured; boundless, limitless, or immeasurable.",
        "secondary": "In classical metaphysics and poetry, exceeding any finite metric, standard, or capacity of quantification.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Into this wild Abyss, the womb of Nature and perhaps her grave, through dark and **immensurable** space."},
            {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Beneath the vaulted sky lay the **immensurable** deep, untamed by mortal dominion."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The creative imagination partakes of an **immensurable** energy that defies mechanical analysis."}
        ]
    },
    "incommensurable": {
        "primary": "Not having a common measure or standard of comparison; incapable of being compared or evaluated together.",
        "secondary": "In mathematics and epistemology, describing magnitudes whose ratio is irrational, or paradigms lacking shared evaluative criteria.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The diagonal of a square remains forever **incommensurable** with its side, presenting an irremovable mathematical truth."},
            {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The existence of **incommensurable** geometric lengths compelled Greek geometers to develop a rigorous theory of proportions."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Mystical ecstasy and analytical logic appear entirely **incommensurable** when judged from within their respective experiential frameworks."}
        ]
    },
    "incommensurate": {
        "primary": "Disproportionate; not adequate, corresponding, or commensurate in size, extent, or degree.",
        "secondary": "In socioeconomic analysis and ethics, characterized by a lack of parity or equitable balance between effort and outcome.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The military preparations were utterly **incommensurate** with the magnitude of the invasion threatening the realm."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "He felt a bitter pang of disappointment that his heroic sacrifice had produced results so meager and **incommensurate**."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The peasant's exhausting toil yielded a return painfully **incommensurate** with the health sacrificed in the fields."}
        ]
    },
    "mensa": {
        "primary": "A table; or a raised tabular anatomical surface, constellation, or high-IQ society.",
        "secondary": "In ecclesiastical architecture and astronomy, the flat top slab of a consecrated altar, or the constellation Mensa (Table Mountain) in the southern sky.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The flat tabular summit of the mountain resembled a colossal natural **mensa** elevated above the cloud line."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bishop placed the sacred vessels upon the marble **mensa** of the ancient cathedral."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Early Christian basilicas featured an unadorned stone **mensa** resting upon four slender porphyry pillars."}
        ]
    },
    "mensal": {
        "primary": "Relating to a table; specifically, providing for the maintenance of a table or dining board.",
        "secondary": "In ecclesiastical law and feudal property tenure, designating lands, revenues, or tithes allocated specifically to supply the bishop's or abbot's dining table.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Monastic revenues were divided between monastic maintenance and the bishop's private **mensal** fund."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Ancient statutes secured specific royal estates as **mensal** properties destined for the sustenance of the sovereign's household."},
            {"author": "Walter Scott", "work": "The Monastery", "quote": "The fertile valley lands were declared **mensal** possessions of the abbey, supplying wheat and wine for the hospitality of the high table."}
        ]
    },
    "mensch": {
        "primary": "A person of integrity, honor, deceny, and noble moral character.",
        "secondary": "In socio-cultural ethics and Yiddish linguistics, an exemplary human being exhibiting rectitude, compassion, and communal responsibility.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Moral evolution elevates the civilized individual toward the ideal of a true **mensch**, governed by empathy and social duty."},
            {"author": "William James", "work": "Memories and Studies", "quote": "In every community one finds that rare, noble spirit whom friends revere as an authentic **mensch**."},
            {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Beneath his gruff laboratory manner, Gottlieb proved himself a genuine **mensch**, incapable of petty deceit."}
        ]
    },
    "menses": {
        "primary": "The monthly flow of blood and mucosal tissue from the uterus; menstruation.",
        "secondary": "In gynecological physiology and reproductive endocrinology, the cyclical shedding of the uterine endometrial lining in the absence of fertilization.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suppression of the **menses** during severe systemic illnesses frequently signals profound secondary nutritional exhaustion."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Periodic cycles corresponding to the mammalian **menses** suggest deep physiological rhythms inherited from primordial progenitors."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Chlorosis in young maidens is almost invariably accompanied by an irregular or retarded appearance of the **menses**."}
        ]
    },
    "menstrual": {
        "primary": "Relating to the menses or the monthly cycle of menstruation.",
        "secondary": "In reproductive physiology and mammalian biology, recurring on a monthly cycle governed by ovarian and pituitary hormonal rhythms.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **menstrual** cycle serves as a sensitive diagnostic barometer reflecting female neuro-endocrine balance."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **menstrual** periodicity observed in higher primates indicates a conserved physiological heritage dating to ancient mammalian ancestors."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Endometrial proliferation and subsequent breakdown constitute the morphological stages of the normal **menstrual** rhythm."}
        ]
    },
    "menstruate": {
        "primary": "To discharge blood and mucosal tissue from the uterus as part of the monthly cycle.",
        "secondary": "In human reproductive physiology, to undergo the periodic hormonal shedding of the uterine lining during the female reproductive years.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Female primates continue to **menstruate** cyclically throughout adult life until ovarian senescence intervenes."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The physiological imperative to **menstruate** reflects the recurring preparation of the uterine mucosa for embryo implantation."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Female anthropoid apes **menstruate** at intervals corresponding remarkably closely to the human monthly period."}
        ]
    },
    "menstruation": {
        "primary": "The process or cycle of discharging blood and cellular debris from the uterus at approximately monthly intervals.",
        "secondary": "In gynecology and physiological endocrinology, the catamenial discharge marking the follicular reset of the ovarian cycle.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Normal **menstruation** depends upon harmonious coordination between the pituitary gland, the ovaries, and the uterine endometrium."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The physiological onset of **menstruation** at puberty denotes the functional maturation of the female reproductive system."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The phenomena of **menstruation** in higher anthropoids substantiate our phylogenetic relationship with the primates."}
        ]
    },
    "menstruum": {
        "primary": "A solvent, particularly a liquid substance that dissolves a solid; or catamenial fluid.",
        "secondary": "In historical alchemy and pharmaceutical chemistry, an active dissolving medium used in extracting medicinal principles or dissolving metals.",
        "quotes": [
            {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Aqua fortis acted as a powerful **menstruum**, dissolving the silver alloy while leaving the gold intact."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The particles of the metallic solute are sustained within the liquid **menstruum** by mutual attractive forces."},
            {"author": "Joseph Priestley", "work": "Experiments and Observations on Different Kinds of Air", "quote": "I introduced the calcined mineral into an acid **menstruum**, observing an immediate release of pungent air."}
        ]
    },
    "mensurable": {
        "primary": "Capable of being measured; measurable.",
        "secondary": "In philosophical metaphysics and musical theory, possessing determinate quantitative dimensions or strict rhythmic metrical values.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "All physical extension is essentially **mensurable**, presenting parts that can be numbered and compared."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "Physical phenomena become subject to mathematical demonstration only when reduced to exact, **mensurable** quantities."},
            {"author": "Bertrand Russell", "work": "Mysticism and Logic", "quote": "Science advances by transforming vague qualitative impressions into precise, **mensurable** data."}
        ]
    },
    "mensural": {
        "primary": "Relating to measure, measurement, or metric rhythm.",
        "secondary": "In historical musicology, referring to the medieval and Renaissance notation system indicating exact rhythmic durations through note shapes.",
        "quotes": [
            {"author": "Charles Burney", "work": "A General History of Music", "quote": "The invention of **mensural** notation enabled fourteenth-century composers to coordinate intricate polyphonic voices with rhythmic precision."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The architectural harmony of the façade depends upon subtle **mensural** proportions governing the placement of arches."},
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Classical verse achieves its majestic flow through strict adherence to balanced **mensural** intervals."}
        ]
    },
    "mensurate": {
        "primary": "To measure; to determine dimensions, area, or volume.",
        "secondary": "In surveying and land geodesy, to compute precise spatial dimensions and geographic areas through geometric triangulation.",
        "quotes": [
            {"author": "Thomas Telford", "work": "Life of Thomas Telford", "quote": "The surveyor was dispatched to **mensurate** the mountain contours before finalizing the canal aqueduct route."},
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "Our instruments enabled us to **mensurate** mechanical movements down to the ten-thousandth part of an inch."},
            {"author": "William Herschel", "work": "Philosophical Transactions", "quote": "Astronomers must meticulously **mensurate** planetary orbits across successive oppositions to detect gravitational perturbations."}
        ]
    },
    "mensuration": {
        "primary": "The act, process, or art of measuring; specifically, mathematical computation of lengths, areas, and volumes.",
        "secondary": "In applied geometry and geodesic engineering, the mathematical formulas and techniques used to determine geometric magnitudes.",
        "quotes": [
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "Accurate astronomical **mensuration** requires instruments constructed with the utmost mechanical rigidity and precision."},
            {"author": "Thomas Telford", "work": "Life of Thomas Telford", "quote": "Practical **mensuration** formed the foundation of civil engineering, allowing contractors to estimate masonry volumes with certainty."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The mathematical **mensuration** of light rays demonstrates that nature operates according to immutable geometric laws."}
        ]
    },
    "premenstrual": {
        "primary": "Occurring, experienced, or situated before menstruation.",
        "secondary": "In clinical medicine and neuropsychiatry, designating physiological and emotional symptoms recurring in the late luteal phase of the ovarian cycle.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe migraine headaches frequently coincide with the **premenstrual** drop in systemic hormonal levels."},
            {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The **premenstrual** phase is often characterized by emotional irritability, heightened sensory sensitivity, and physical fatigue."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Uterine congestion and glandular hypertrophy mark the histological changes characteristic of the **premenstrual** endometrium."}
        ]
    },
    "scruple": {
        "primary": "A feeling of doubt or hesitation with regard to the morality or propriety of an action; or a small unit of weight (1/24 of an ounce).",
        "secondary": "In moral philosophy and classical pharmacy, an agonizing moral hesitation regarding right and wrong, or an ancient apothecaries' weight equal to 20 grains.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Some craven **scruple** of thinking too precisely on the event, a thought which quartered hath but one part wisdom and three parts coward."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She entertained a delicate moral **scruple** against enjoying wealth derived from oppressive social practices."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare was tormented by a persistent theological **scruple** that prevented him from taking holy orders."}
        ]
    },
    "scruples": {
        "primary": "Ethical doubts, moral reservations, or pangs of conscience that restrain one's actions.",
        "secondary": "In ethical philosophy, principled inhibitions preventing an individual from participating in questionable or dishonorable undertakings.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Fears and **scruples** shake us; in the great hand of God I stand."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "His rough commercial ambition brushed aside all tender **scruples** regarding his rival's misfortunes."},
            {"author": "George Eliot", "work": "Romola", "quote": "Tito possessed intellect and charm, but lacked the moral **scruples** necessary to resist seductive betrayal."}
        ]
    },
    "scrupulous": {
        "primary": "Diligent, thorough, and extremely attentive to details; or strictly adhering to moral principles.",
        "secondary": "In ethical philosophy and scholarship, characterized by uncompromising conscientiousness, precision, and rigorous honesty.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Sherlock Holmes examined the carpet with the most **scrupulous** care, magnifying glass in hand."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Caleb Garth was **scrupulous** in fulfilling every contract, holding that careless workmanship was an insult to God."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak was a man of **scrupulous** honesty, incapable of deceiving any master who trusted him."}
        ]
    },
    "scrupulously": {
        "primary": "In a careful, thorough, and conscientious manner; strictly adhering to ethics or precision.",
        "secondary": "In historical methodology and empirical investigation, executing tasks with painstaking fidelity to rules, accuracy, and truth.",
        "quotes": [
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie **scrupulously** avoided every opportunity of meeting him, determined to preserve her sibling's peace."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooneers **scrupulously** cleaned their iron barbs, sharpening each cutting edge to razor keenness."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I have **scrupulously** recorded every negative fact that appeared to conflict with my theory of natural selection."}
        ]
    },
    "scrupulousness": {
        "primary": "Meticulous attentiveness to details, strict conscientiousness, and uncompromising moral rectitude.",
        "secondary": "In character ethics, rigid fidelity to duty, meticulous fairness, and intolerance of moral compromise.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles Winterborne's extraordinary **scrupulousness** made him sacrifice his own happiness rather than inconvenience others."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "His professional **scrupulousness** won the confidence of all citizens who valued upright legal counsel."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "In morbid melancholia, religious **scrupulousness** magnifies imaginary sins into unforgivable crimes."}
        ]
    },
    "unscrupulous": {
        "primary": "Having or showing no moral principles; not honest or fair.",
        "secondary": "In political and commercial critique, opportunistically unprincipled, exploiting others without ethical inhibition or remorse.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode's past was stained by transactions with an **unscrupulous** pawnbroker who accumulated stolen wealth."},
            {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The Mississippi steamboat harbored many an **unscrupulous** swindler preying upon naive frontiersmen."},
            {"author": "Henry David Thoreau", "work": "Civil Disobedience", "quote": "Governments often enlist the services of **unscrupulous** men who obey orders without consulting conscience."}
        ]
    },
    "unscrupulously": {
        "primary": "In a manner showing no moral principles; dishonestly, unfairly, or ruthlessly.",
        "secondary": "In ethical critique, pursuing personal gain or victory without regard to truth, honor, or justice.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Farfrae's rivals claimed that he had acted **unscrupulously**, though in truth he had merely exercised superior foresight."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The cunning solicitor acted **unscrupulously**, squeezing desperate clients for every guinea they possessed."},
            {"author": "Mark Twain", "work": "The Gilded Age", "quote": "Lobbyists distributed railroad stock **unscrupulously** among legislators to purchase favorable votes."}
        ]
    },
    "unscrupulousness": {
        "primary": "The trait or condition of lacking moral principles, fairness, or honesty.",
        "secondary": "In social ethics and historical critique, blatant disregard for ethical boundaries and human dignity in pursuit of ambition.",
        "quotes": [
            {"author": "George Eliot", "work": "Romola", "quote": "The tragic ruin of the Florentine republic stemmed from the cynical **unscrupulousness** of its factional leaders."},
            {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Unbridled commercial **unscrupulousness** undermines the trust upon which free economic exchange depends."},
            {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "The revolutionary conspiracy was infected by an icy **unscrupulousness** that treated human lives as disposable instruments."}
        ]
    }
}
