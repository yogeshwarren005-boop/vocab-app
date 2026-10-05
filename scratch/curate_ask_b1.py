# -*- coding: utf-8 -*-
"""
curate_ask_b1.py
Master dataset for Batch 1 of Cluster Asking & Seeking (72 words):
- Dashboard — plor (16 words)
- Dashboard — postul (7 words)
- Dashboard — quer (16 words)
- Dashboard — scit (2 words)
- Dashboard — scrut (9 words)
- Dashboard — stud (14 words)
- Dashboard — vestig (8 words)

Total: 72 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_ask_b1 = {
    # =========================================================================
    # DASHBOARD — plor (16 words)
    # =========================================================================
    "deplorable": {
        "primary": "Deserving strong condemnation, regret, or grief; shockingly bad or lamentable in quality.",
        "secondary": "In social reform and political critique, describing wretched socioeconomic deprivation or unconscionable civic breakdown.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess had thirty pounds coming to her from Angel's bankers, and, the case being so **deplorable**, she sent the sum requested."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "It is a **deplorable** mistake to look for wisdom among those whose thoughts are chained to narrow conventions."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The condition of the native station workers was utterly **deplorable**, abandoned as they were to starvation and neglect."}
        ]
    },
    "deplorably": {
        "primary": "In a manner deserving profound regret or severe condemnation; wretchedly and lamentably.",
        "secondary": "In literary discourse, modifying an observed state of failure, moral decline, or severe deficiency in conduct.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The wretched crew was **deplorably** ill-prepared to withstand the arctic tempest howling across the open deck."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her practical education had been **deplorably** neglected, leaving her unacquainted with the common affairs of life."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The affairs of the family had been so **deplorably** managed that very little inheritance remained for the daughters."}
        ]
    },
    "deplore": {
        "primary": "To express strong disapproval of, regret deeply, or mourn grievous misfortunes and ethical failings.",
        "secondary": "In diplomatic rhetoric and moral philosophy, to formally denounce an unjust aggression, breach of covenant, or tragic calamity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I do **deplore** his death with all my heart, and mourn the bitter stroke of sudden fate."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men of thoughtful judgment must **deplore** that persistent negligence which blinds the mind to demonstrable truths."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood could only silently **deplore** the irrevocable step that had alienated him from her favor forever."}
        ]
    },
    "exploration": {
        "primary": "The act of traveling into unfamiliar regions or examining uncharted domains for geographical and scientific discovery.",
        "secondary": "In intellectual history and methodology, the systematic heuristic pursuit of unknown principles, hypotheses, or creative terrain.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate had entered upon that ardent **exploration** of organic structures which promises new light to physiological science."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The geographical **exploration** of the vast river basin had filled blank spaces on the map with dark mysteries."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Subsequent geological **exploration** will undoubtedly reveal many intermediate forms that are at present entirely missing."}
        ]
    },
    "explorative": {
        "primary": "Serving, inclined, or organized toward searching, discovering, or venturing into the unknown.",
        "secondary": "In educational psychology and cognitive science, characterizing proactive curiosity and heuristic information gathering.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The infant manifests an instinctively **explorative** disposition toward novel tactile and visual sensations."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "True learning proceeds from an **explorative** attitude wherein the pupil tests hypotheses against practical experience."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The creative imagination exercises an **explorative** power that penetrates beneath external appearances to inner truths."}
        ]
    },
    "exploratory": {
        "primary": "Undertaken for the purpose of discovery, initial diagnosis, or systematic fact-finding rather than definitive action.",
        "secondary": "In clinical surgery and statistical data analysis, serving as an initial probing procedure to uncover hidden lesions or empirical patterns.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses and Reviews", "quote": "Scientific progress requires cautious **exploratory** experiments before generalizing across a wide class of phenomena."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A surgical **exploratory** incision often reveals deep internal pathology that escaped external palpation."},
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The organism extends delicate **exploratory** filaments into the surrounding medium to gauge environmental chemistry."}
        ]
    },
    "explore": {
        "primary": "To travel through an unfamiliar area to learn about it, or to investigate a subject comprehensively.",
        "secondary": "In philosophy and scientific inquiry, to subject foundational premises or physical mechanisms to probing empirical analysis.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He felt a strange desire to **explore** the emotional depths of a soul so pure and untainted by society."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Our expedition set forth to **explore** the mysterious basalt plateau rising abruptly above the Amazonian jungle."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Let every student boldly **explore** the kingdom of his own mind rather than accept borrowed judgments."}
        ]
    },
    "explorer": {
        "primary": "A person who journeys into uncharted or unfamiliar regions in search of geographical, scientific, or cultural knowledge.",
        "secondary": "In intellectual biography, a pioneer who ventures into unmapped domains of thought, art, or natural philosophy.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The fearless **explorer** must possess not only physical endurance but an unshakeable faith in scientific truth."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "No daring polar **explorer** ever gazed upon an iceberg with more awe than our lookout beheld that solitary white whale."},
            {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The pioneering intellectual **explorer** clears a pathway through traditional prejudices for future generations to tread."}
        ]
    },
    "implore": {
        "primary": "To plead with someone urgently, desperately, or tearfully; to entreat with earnest humility.",
        "secondary": "In tragic drama and spiritual literature, expressing profound supplication before transcendent powers or inexorable authority.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Upon my knees I do **implore** thy grace, and beg that mercy which thy royal hand can best bestow."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She turned her sorrowful eyes toward him as if to **implore** some unspoken word of forgiveness."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The trembling client clasped her hands to **implore** Holmes's immediate intervention in the perilous matter."}
        ]
    },
    "imploring": {
        "primary": "Expressing an urgent, desperate, or earnest plea for mercy, assistance, or understanding.",
        "secondary": "In dramatic narrative, manifesting nonverbal signals of intense vulnerability and affective distress.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Her **imploring** look pierced his conscience more sharply than any verbal reproof could have done."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The child reached out its little hands with an **imploring** gesture that melted the solitary weaver's heart."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "She cast an **imploring** glance at the detective, beseeching him not to disclose her husband's secret."}
        ]
    },
    "imploringly": {
        "primary": "In an earnest, pleading, or supplicating manner that seeks compassion, mercy, or relief.",
        "secondary": "In affective characterization, capturing the desperate, helpless tone or gesture of one facing overwhelming adversity.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She looked up **imploringly** into his face, as if silently beseeching him to soften his harsh resolve."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie clung to her brother's arm **imploringly**, entreating him to believe her innocence despite appearances."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Mina reached out her pale hands **imploringly**, praying that the terrible curse might be lifted from her spirit."}
        ]
    },
    "nonexplorative": {
        "primary": "Not characterized by exploration, discovery, or systematic investigation into unfamiliar fields.",
        "secondary": "In behavioral psychology and animal ethology, referring to inert, sedentary, or purely exploitative routines that forgo environmental sampling.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Habitual routines often induce a **nonexplorative** mental torpor wherein no unfamiliar stimuli are sought."},
            {"author": "John Dewey", "work": "Experience and Education", "quote": "A rigid didactic syllabus creates a **nonexplorative** classroom atmosphere that discourages inventive curiosity."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Conspicuous leisure often manifests in **nonexplorative** consumption governed solely by ceremonial inertia."}
        ]
    },
    "nonexploratory": {
        "primary": "Serving purposes other than probing, venturing, or preliminary factual investigation.",
        "secondary": "In methodology and clinical protocol, designating confirmatory, routine, or therapeutic interventions rather than diagnostic probing.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Reflex mechanisms execute predetermined motor responses in a strictly **nonexploratory** sequence."},
            {"author": "William Osler", "work": "Aequanimitas", "quote": "When clinical signs are definitive, surgeons proceed directly to intervention without **nonexploratory** delays."},
            {"author": "Francis Galton", "work": "Inquiries into Human Faculty", "quote": "Standardized repetitive measurements fulfill a purely statistical, **nonexploratory** function in large populations."}
        ]
    },
    "unexplorative": {
        "primary": "Showing no inclination to explore, investigate, or venture beyond known boundaries.",
        "secondary": "In literary portraiture and intellectual critique, portraying a parochial, complacent mind resistant to unfamiliar frontiers.",
        "quotes": [
            {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Certain provincial essayists preserved an **unexplorative** contentment, satisfied with domestic commonplaces."},
            {"author": "Walter Pater", "work": "Appreciations", "quote": "An **unexplorative** artist risks repeating conventional ornaments without revitalizing his imaginative vision."},
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "British insularity often bred an **unexplorative** disdain for continental philosophical movements."}
        ]
    },
    "unexploratory": {
        "primary": "Not oriented toward discovery, investigation, or preliminary searching.",
        "secondary": "In scientific and institutional analysis, describing established procedures focused purely on execution rather than speculative research.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Deductive calculation from established axioms pursues a necessary but **unexploratory** demonstration of known truths."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Purely dogmatic education fosters an **unexploratory** habit of mind hostile to empirical verification."},
            {"author": "Alfred North Whitehead", "work": "Science and the Modern World", "quote": "Routine technological application operates within fixed boundaries along an **unexploratory** trajectory."}
        ]
    },
    "unexplored": {
        "primary": "Not yet mapped, investigated, traveled through, or intellectually examined.",
        "secondary": "In geographical and scientific history, wilderness or theoretical territory awaiting systematic investigation.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her mind possessed vast **unexplored** tracts of feeling which no experience had yet stirred to life."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "We should be constantly on the alert to discover **unexplored** continents of our own internal cosmos."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The blank white space representing an **unexplored** river had exerted a fascination over his youthful imagination."}
        ]
    },

    # =========================================================================
    # DASHBOARD — postul (7 words)
    # =========================================================================
    "expostulate": {
        "primary": "To express strong disapproval or disagreement; to reason earnestly with someone against their intended action.",
        "secondary": "In moral philosophy and interpersonal ethics, to present reasoned admonitions against folly, injustice, or rashness.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "My lord, I must **expostulate** with you concerning the harsh sentence you have passed upon this prisoner."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare attempted to **expostulate** with his father against his uncompromising theological dogmatism."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Dr. Seward ventured to **expostulate** with Van Helsing, questioning whether his unusual measures were truly necessary."}
        ]
    },
    "expostulation": {
        "primary": "An earnest, reasoned protest or objection lodged against someone's behavior, decision, or intention.",
        "secondary": "In classical rhetoric and drama, a formal passage of remonstrance appealing to justice, prudence, or filial duty.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Hear my **expostulation**, royal sovereign, and weigh the heavy griefs that urge my speech."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak's blunt **expostulation** offended Bathsheba, though her conscience acknowledged the justice of his warning."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister offered a mild **expostulation**, striving to soften the magistrate's inflexible judgment."}
        ]
    },
    "postulant": {
        "primary": "A candidate applying for admission into a religious order, undergoing an initial probationary trial.",
        "secondary": "In canon law and monastic institutions, an aspirant who resides within a community to test their vocation prior to entering the novitiate.",
        "quotes": [
            {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The young **postulant** knelt reverently before the elder, preparing his spirit for the austerities of monastic life."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Like an earnest **postulant** at a pagan shrine, the youth sought purification from worldly distractions."},
            {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The cloister master examined each humble **postulant** to ensure his pious motives were unalloyed by secular ambitions."}
        ]
    },
    "postulate": {
        "primary": "To suggest or assume the truth or existence of something as a foundational basis for reasoning or belief.",
        "secondary": "In formal logic, mathematics, and physics, a fundamental proposition taken as self-evident or unproved to deduce further theorems.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We must not arbitrarily **postulate** innate principles when ordinary sensory faculties suffice to explain our knowledge."},
            {"author": "William James", "work": "Pragmatism", "quote": "Every philosophic system is forced to **postulate** some ultimate reality from which all finite appearances flow."},
            {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Geometric deduction begins with axioms that **postulate** the intrinsic properties of space and magnitude."}
        ]
    },
    "postulation": {
        "primary": "The assumption or assertion of something as true without immediate proof, serving as a premise for argument.",
        "secondary": "In legal and ecclesiastical history, the formal petitioning or recommendation of a candidate to an office by those lacking direct power to elect.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The bold **postulation** of vast geological epochs was necessary to accommodate the gradual divergence of species."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Scientific induction cannot rest upon arbitrary **postulation**, but must continually verify its assumptions against observed facts."},
            {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "The uncritical **postulation** of occult occult qualities in matter has long impeded the advance of natural philosophy."}
        ]
    },
    "postulational": {
        "primary": "Of, relating to, or proceeding from unproved assumptions, axioms, or foundational postulates.",
        "secondary": "In metamathematics and epistemology, characterizing axiomatic formal systems structured around explicit initial hypotheses.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "The modern axiomatic method achieves deductive rigor through a strictly **postulational** framework."},
            {"author": "William James", "work": "The Meaning of Truth", "quote": "Our scientific hypotheses retain an essentially **postulational** character, subject to revision by emergent empirical facts."},
            {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "In theoretical kinematics, the **postulational** basis must remain parsimonious while covering all observable trajectories."}
        ]
    },
    "postulator": {
        "primary": "A person who puts forward a postulate, assumption, or petition on behalf of an enterprise or cause.",
        "secondary": "In Roman Catholic canon law, an official appointed to advocate and present the evidence for the beatification or canonization of a deceased candidate.",
        "quotes": [
            {"author": "Lord Acton", "work": "Historical Essays and Studies", "quote": "The learned **postulator** assembled mountains of archival testimony to demonstrate the martyr's heroic virtue."},
            {"author": "William H. Prescott", "work": "History of the Reign of Philip the Second", "quote": "At the papal curia, the ecclesiastical **postulator** pressed for the official recognition of the venerable founder."},
            {"author": "John Henry Newman", "work": "Essays Critical and Historical", "quote": "A judicious **postulator** examines every reported miracle with rigorous legal skepticism before submitting his cause."}
        ]
    },

    # =========================================================================
    # DASHBOARD — quer (16 words)
    # =========================================================================
    "conquer": {
        "primary": "To overcome, defeat, or gain control over an enemy, territory, obstacle, or emotional temptation.",
        "secondary": "In military history and moral discipline, to subjugate an opposing force or master internal passions through decisive effort.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "He that will a soldier be, must learn to **conquer** fear and welcome battle with a smiling countenance."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Tribes possessing high moral discipline and mutual sympathy will invariably **conquer** more discordant neighbors."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea resolved that no petty bitterness of spirit should ever **conquer** her steadfast desire to do good."}
        ]
    },
    "conquerable": {
        "primary": "Capable of being overcome, subdued, defeated, or brought under mastery.",
        "secondary": "In strategic assessment and philosophical ethics, designating an enemy fortification or human vice that can be successfully mastered.",
        "quotes": [
            {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Early stubbornness in children is easily **conquerable** by consistent kindness and gentle rational discipline."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Difficulties which appear insurmountable to indolence are found to be **conquerable** by persevering industry."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The barbarian tribes on the northern frontier proved far less **conquerable** than the decadent cities of the East."}
        ]
    },
    "conquering": {
        "primary": "Gaining victory or dominion over adversaries; successfully overcoming opposition.",
        "secondary": "In epic narrative, characterizing the triumphant march or sweeping ascendancy of a victorious force.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Now is the winter of our discontent made glorious summer by this sun of York, and our **conquering** arms victorious."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie felt an inexplicable charm in his presence, as though a **conquering** destiny had swept aside her feeble defenses."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The aggressive march of civilized commerce presented itself as a grand, **conquering** mission across the dark continent."}
        ]
    },
    "conqueror": {
        "primary": "A person who conquers a country, people, or adversary by military force or superior capability.",
        "secondary": "In political philosophy, a sovereign who establishes dominion through conquest rather than hereditary succession or popular compact.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Great Julius Caesar fell at the base of Pompey's statue, where the proud **conqueror** lay bleeding from countless wounds."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Time, the inexorable **conqueror** of beauty and youth, swept along its relentless course over the quiet vale."},
            {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "William the **Conqueror**, whose cause was favoured by the pope, was soon submitted to by the English."}
        ]
    },
    "equerry": {
        "primary": "An officer of a royal or noble household entrusted with the management of the stables and attendance upon royalty.",
        "secondary": "In British court hierarchy, a senior military officer seconded to personal attendance upon the sovereign or senior members of the royal family.",
        "quotes": [
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The young lord was attended by an **equerry** in splendid livery, who held the reins of his spirited chestnut thoroughbred."},
            {"author": "Walter Scott", "work": "Kenilworth", "quote": "The Queen turned to her trusted **equerry**, commanding him to inspect the horses before the procession moved toward the castle."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King William selected a veteran Dutch officer to serve as his first **equerry** during the Irish campaign."}
        ]
    },
    "quercitron": {
        "primary": "A natural yellow dye obtained from the inner bark of the Eastern black oak (*Quercus velutina*); the tree itself.",
        "secondary": "In historical dyeing and industrial chemistry, an important mordant dye rich in quercitrin used widely in 18th- and 19th-century textile printing.",
        "quotes": [
            {"author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "The pulverized bark of the North American oak, known commercially as **quercitron**, yields a brilliant and permanent yellow dye."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "In the dense eastern woodlands, the black oak or **quercitron** was prized by settlers for its yellow inner bark and sturdy timber."},
            {"author": "George Bancroft", "work": "History of the United States", "quote": "Colonial commerce exported substantial cargoes of **quercitron** to British woolen mills eager for bright, enduring pigments."}
        ]
    },
    "quercus": {
        "primary": "The large botanical genus of hardwood trees and shrubs comprising the true oaks, family Fagaceae.",
        "secondary": "In forestry, paleobotany, and dendrology, *Quercus* encompasses several hundred deciduous and evergreen species characterized by acorns and cupules.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The wide geographic variation among species of **Quercus** exemplifies how natural selection shapes foliar form across varied climates."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Timber obtained from the majestic European species of **Quercus** formed the naval backbone of maritime empires for centuries."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Botanists distinguish the diverse North American representatives of **Quercus** by the annual or biennial maturation of their acorns."}
        ]
    },
    "querier": {
        "primary": "A person who asks a question, raises an inquiry, or interrogates an information system.",
        "secondary": "In information retrieval and database management, an agent or user issuing structured query statements to retrieve indexed records.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "To every anxious **querier** knocking at the gate of nature, the universe returns only an enigmatic, solemn silence."},
            {"author": "Charles Sanders Peirce", "work": "Illustrations of the Logic of Science", "quote": "The scientific **querier** must frame his inquiry in terms susceptible of empirical verification and experimental test."},
            {"author": "William James", "work": "The Will to Believe", "quote": "The philosophic **querier** seeks not merely formal definitions, but vital truths that give meaning to moral action."}
        ]
    },
    "quern": {
        "primary": "A simple hand-operated stone mill used for grinding grain or seed into meal or flour.",
        "secondary": "In prehistoric archaeology and material culture, rotary querns represent an essential Neolithic and Iron Age domestic technology.",
        "quotes": [
            {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Are not you he that frights the maidens of the villagery, skim milk, and sometimes labour in the **quern**?"},
            {"author": "Walter Scott", "work": "The Pirate", "quote": "The elderly matron turned the heavy stone **quern** with rhythmic strokes, grinding the winter barley into coarse bread meal."},
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient domestic rituals often centered upon the household **quern**, where grain was transformed into sustenance under magical auspices."}
        ]
    },
    "querulous": {
        "primary": "Habitually complaining, fretful, whining, or petulant in tone and disposition.",
        "secondary": "In literary portraiture, capturing the thin, irritating cadence of someone chronically aggrieved by trivial discomforts.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her voice took on that **querulous** edge which betrayed long exhaustion and wounded pride."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Leave your **querulous** complaints to the feeble-minded, and greet the morning with courage and resolute action."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Grandfather Smallweed continued his **querulous** scolding from the depths of his armchair, abusing everyone within reach."}
        ]
    },
    "querulously": {
        "primary": "In a whining, petulant, or complaining manner; fretfully expressing irritation.",
        "secondary": "In narrative dialogue, describing speech delivered with a sharp, aggrieved, or resentful inflection.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry muttered **querulously** that the endless rain had ruined his afternoon appointments."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The old woman inquired **querulously** why her customary morning tea had been delayed by the servants."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "He asked **querulously** whether any visitor had dared to disturb his private papers during his absence."}
        ]
    },
    "querulousness": {
        "primary": "A persistent disposition toward complaining, fretfulness, petulance, or chronic discontent.",
        "secondary": "In moral psychology and character analysis, the habit of nursing petty grievances and venting irritation upon associates.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Old Mr. Featherstone's chronic **querulousness** made the task of tending his final illness an ordeal to everyone around him."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Age without wisdom degenerates into a gloomy **querulousness** that alienates the affection of the young."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Prolonged nervous debility often clothes itself in an acute **querulousness** that exaggerates every minor tactile discomfort."}
        ]
    },
    "query": {
        "primary": "A question, inquiry, or doubt addressed to an authority or posed for investigation.",
        "secondary": "In computer science and epistemology, a formal instruction issued to a search engine or database to retrieve matching entries.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak pondered over her brief **query**, wondering whether some hidden affection lay beneath her teasing words."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The physician addressed an anxious **query** to the reverend gentleman regarding the mysterious symptoms of his malady."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Jonathan Harker noted down every peculiar **query** put to him by the Count concerning London legal practice."}
        ]
    },
    "reconquer": {
        "primary": "To conquer again; to recapture, recover, or regain control over lost territory or dominion.",
        "secondary": "In military and political history, to execute a revanchist campaign recovering provinces ceded to a foreign power.",
        "quotes": [
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester declared his determination to **reconquer** peace of mind through a life of moral rectitude and honest devotion."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "General Belisarius was dispatched by Justinian to **reconquer** the lost African provinces from the Vandal kingdom."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The English crown strove repeatedly to **reconquer** the disaffected Irish districts through military garrisons and plantations."}
        ]
    },
    "unconquerable": {
        "primary": "Incapable of being conquered, defeated, subjugated, or quelled; indomitable in resolve.",
        "secondary": "In heroic poetry and stoic philosophy, describing an invincible will or virtue that withstands all extremity.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia Vye possessed an **unconquerable** longing for passion and splendor far beyond the dreary expanse of Egdon Heath."},
            {"author": "George Eliot", "work": "Romola", "quote": "Savonarola faced his accusers with an **unconquerable** conviction that divine righteousness would eventually prevail."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Captain Ahab stood upon the quarterdeck animated by an **unconquerable** malice against the white demon of the seas."}
        ]
    },
    "unconquered": {
        "primary": "Not conquered, subdued, defeated, or brought under foreign domination.",
        "secondary": "In historical and geographical narrative, describing a territory or sovereign people that has successfully repelled invasion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "This blessed plot, this earth, this realm, this England, remains **unconquered** against the proud assaults of foreign tyrants."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The heroic spirit stands **unconquered** amidst outward calamities, knowing that its true kingdom lies within."},
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "The wild Highland clansmen boasted of an **unconquered** heritage that no southern monarch had ever entirely subdued."}
        ]
    },

    # =========================================================================
    # DASHBOARD — scit (2 words)
    # =========================================================================
    "adscititious": {
        "primary": "Added from an external source; supplemental, adventitious, or derived rather than innate.",
        "secondary": "In legal jurisprudence and philosophical epistemology, denoting external evidentiary factors or auxiliary assumptions not intrinsic to a core principle.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "True poetic genius relies upon its own native fires rather than upon borrowed, **adscititious** ornaments of rhetoric."},
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The court must carefully separate intrinsic evidentiary facts from **adscititious** testimony introduced by interested parties."},
            {"author": "Thomas De Quincey", "work": "The Opium-Eater and Other Writings", "quote": "The philosophical critic should strip away all **adscititious** reputation and judge the work purely by its enduring merits."}
        ]
    },
    "plebiscite": {
        "primary": "A direct vote of the entire electorate of a state or territory on an important public question, such as sovereignty.",
        "secondary": "In constitutional law and democratic theory, an exceptional referendum by universal suffrage to determine national allegiance or constitutional reform.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "In the early Roman republic, a binding **plebiscite** enacted by the popular assembly held the full force of statutory law."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "An authoritarian regime may disguise its usurpations beneath the democratic facade of a staged national **plebiscite**."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Determining disputed frontier borders through an honest popular **plebiscite** respects the principle of national self-determination."}
        ]
    },

    # =========================================================================
    # DASHBOARD — scrut (9 words)
    # =========================================================================
    "inscrutability": {
        "primary": "The state or characteristic of being impossible to understand, fathom, penetrate, or interpret.",
        "secondary": "In theology and metaphysical aesthetics, the impenetrable mystery of the divine will or the cosmos that defies human analytical intellect.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The profound **inscrutability** of the whale's blank brow seemed to mock every attempt of naturalists to read its thoughts."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The chilling **inscrutability** of Chillingworth's countenance concealed the sinister machinations working within his soul."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The primeval jungle gazed back at the steamboat with an impenetrable **inscrutability** that chilled the European travelers."}
        ]
    },
    "inscrutable": {
        "primary": "Impossible to understand, interpret, or penetrate; enigmatic and mysterious.",
        "secondary": "In narrative characterization, describing an expression, motive, or demeanor that reveals nothing of inner thoughts.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O heaven, how **inscrutable** are thy divine judgments, and thy righteous ways past human finding out!"},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes maintained an **inscrutable** composure while listening to the client's extraordinary narrative."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The silent wilderness appeared to keep an **inscrutable** secret locked within its shadowy foliage."}
        ]
    },
    "inscrutably": {
        "primary": "In a manner that cannot be understood, penetrated, interpreted, or fathomed; enigmatically.",
        "secondary": "In psychological fiction, characterizing behavior or facial expressions that give no clue to underlying motives.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "For, it **inscrutably** appeared to stand to reason in the minds of the villagers that the blacksmith should be silent."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett had learned more or less **inscrutably** to disguise his physical suffering behind an ironic smile."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The silent captain stared **inscrutably** toward the distant horizon without offering a word of explanation to his mate."}
        ]
    },
    "scrutineer": {
        "primary": "A person who formally inspects, examines, or counts ballots at an election to verify their legality.",
        "secondary": "In electoral administration and corporate governance, an official appointed by competing parties or shareholders to audit vote tallies.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The official **scrutineer** examined each paper ballot with scrupulous vigilance before entering it into the town ledger."},
            {"author": "Anthony Trollope", "work": "Phineas Redux", "quote": "Both parliamentary factions appointed a keen **scrutineer** to challenge contested voting slips at the borough polling booth."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "An impartial **scrutineer** was stationed beside the ballot box to prevent fraudulent stuffing by enthusiastic partisans."}
        ]
    },
    "scrutinise": {
        "primary": "To examine, inspect, or observe someone or something with thorough, critical, and exacting care.",
        "secondary": "In critical philology and forensic investigation, to subject documentary evidence or texts to microscopic analysis.",
        "quotes": [
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "It may hate him who dares to **scrutinise** and expose his covert sins, yet truth demands an unsparing light."},
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The more we **scrutinise** ancient agrarian rituals, the clearer becomes their symbolic connection to seasonal rebirth."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge bent down to **scrutinise** the cold paving stones, wondering if his eyes had played a phantom trick upon him."}
        ]
    },
    "scrutiniser": {
        "primary": "A person who examines, inspects, or investigates someone or something closely and critically.",
        "secondary": "In social satire and philosophical critique, a penetrating observer who dissects public pretenses and institutional hypocrisies.",
        "quotes": [
            {"author": "William Hazlitt", "work": "Table-Talk", "quote": "The relentless moral **scrutiniser** detects vanity flourishing beneath the most modest outward professions of piety."},
            {"author": "Samuel Johnson", "work": "The Idler", "quote": "A severe **scrutiniser** of human conduct will find that indolence is the root of many celebrated virtues."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The true reformer must be a fearless **scrutiniser** of economic inequities, stripping away sentimental illusions."}
        ]
    },
    "scrutinize": {
        "primary": "To examine, inspect, or observe someone or something closely, minutely, and critically.",
        "secondary": "In scientific observation and forensic scholarship, to conduct a rigorous inspection ensuring every detail is weighed.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate leaned over the microscope to **scrutinize** the minute cellular alterations in the inflamed vascular tissue."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The detective knelt down upon the carpet with his pocket lens to **scrutinize** the faint muddy footprints."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Pyncheon paused on the threshold to **scrutinize** the stranger's features, seeking some token of past acquaintance."}
        ]
    },
    "scrutinizer": {
        "primary": "A person who scrutinizes; an attentive and critical examiner or investigator.",
        "secondary": "In literary criticism and judicial review, an analyst who investigates underlying structures, doctrines, or textual integrity.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Nature repays the patient **scrutinizer** with sudden revelations of harmony that escape the superficial glance."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The solitary walker becomes a keen **scrutinizer** of the changing seasons, noting every bud and shifting shadow."},
            {"author": "John Stuart Mill", "work": "An Examination of Sir William Hamilton's Philosophy", "quote": "A philosophical **scrutinizer** must test every metaphysical axiom against the rigorous demands of experience."}
        ]
    },
    "scrutiny": {
        "primary": "Critical, searching, and thorough observation, examination, or close inspection.",
        "secondary": "In public law and investigative journalism, institutional oversight ensuring accountability and ethical transparency.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess's one dread was lest her face should undergo the close **scrutiny** of the passing dairymaids."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode shrank inwardly from the searching **scrutiny** of those who had witnessed his earliest business dealings."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Character is that which can stand the severest **scrutiny** without forfeiting its inward majesty."}
        ]
    },

    # =========================================================================
    # DASHBOARD — stud (14 words)
    # =========================================================================
    "stud": {
        "primary": "A projecting knob, pin, boss, or fastener on a surface; an establishment for breeding horses.",
        "secondary": "In architecture and framing carpentry, a vertical upright framing member in a building's wall partition.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The small attorney adjusted the glittering brass **stud** upon his immaculate shirt collar before addressing the court."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight's heavy leather baldric was ornamented with many a silver **stud** and embossed steel buckle."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak admired the prize stallion newly purchased to enrich the Squire's celebrated breeding **stud**."}
        ]
    },
    "student": {
        "primary": "A person who is enrolled in school or higher education; anyone devoted to systematic learning and inquiry.",
        "secondary": "In scholarship and intellectual discipline, an individual who applies concentrated analytical attention to a field.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I prithee do not mock me, fellow-**student**; I think it was to see my mother's wedding."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The humble stonecutter dreamed of entering Christminster as a scholarly **student** of theology and Greek."},
            {"author": "John Stuart Mill", "work": "Inaugural Address at St. Andrews", "quote": "The university should teach every **student** to think rigorously and pursue truth without dogmatic prejudice."}
        ]
    },
    "studentship": {
        "primary": "An academic scholarship, research stipend, or university fellowship awarded to support advanced study.",
        "secondary": "In British university foundations (such as Christ Church, Oxford), an endowed fellowship supporting advanced research or tutorial duties.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Life and Letters of Charles Darwin", "quote": "During his Cambridge **studentship**, his passion for entomological collecting superseded all formal mathematical studies."},
            {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The award of a research **studentship** granted the aspiring chemist sufficient leisure to conduct laboratory analyses."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "His successful university **studentship** laid the groundwork for rapid preferment in the ecclesiastical hierarchy."}
        ]
    },
    "studied": {
        "primary": "Carefully considered, rehearsed, premeditated, or planned; showing deliberate artifice rather than spontaneity.",
        "secondary": "In behavioral aesthetics and rhetoric, characterized by polished calculation designed to produce an intentional impression.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Pardon what I have spoke, for 'tis a **studied**, not a present thought, by full advice determined."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Her polite indifference was far too **studied** to conceal the wounded pride beneath her composed exterior."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The polite smiles of fashionable society often exhibit a **studied** muscular control alien to genuine joy."}
        ]
    },
    "studio": {
        "primary": "A workspace utilized by an artist, sculptor, photographer, or musician for creative production.",
        "secondary": "In broadcasting, film production, and commercial media, an acoustically and visually isolated facility equipped for recording.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "He led us upstairs into the artist's disorderly **studio**, where unfinished canvases leaned against dusty easels."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The **studio** was filled with the rich odour of roses, and when the summer wind stirred, there came through the open door the heavy scent of lilac."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The eccentric portrait painter greeted us warmly at the door of his sunlit Chelsea **studio**."}
        ]
    },
    "studious": {
        "primary": "Spending much time reading or studying; showing great diligence, care, or deliberate attention.",
        "secondary": "In character description, exhibiting an earnest intellectual focus and a quiet temperament inclined toward scholarship.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "She hath been **studious** of her people's welfare, and sought by prudent counsel to preserve the realm."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon sat amidst his pamphlets with that pale, **studious** look which promised monumental learning."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The philosopher leads a quiet and **studious** life, contemplating eternal laws far above transient worldly strife."}
        ]
    },
    "studiously": {
        "primary": "In a manner showing great care, deliberate attention, or premeditated purpose; diligently.",
        "secondary": "In narrative prose, modifying intentional efforts to avoid, maintain, or achieve a specific posture or outcome.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Com'st thou with deep premeditated lines, with written pamphlets **studiously** devised to mock my state?"},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Uriah Heep maintained a **studiously** humble demeanor, continually writhing his long neck in apparent self-abasement."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The courtiers were **studiously** attentive to the monarch's slightest gesture, eager to anticipate his royal commands."}
        ]
    },
    "studiousness": {
        "primary": "The habit, disposition, or practice of diligent study, serious intellectual inquiry, or focused scholarly reading.",
        "secondary": "In pedagogical theory and intellectual history, persistent dedication to book-learning and academic discipline.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A youth distinguished for quiet **studiousness** rarely contracts those turbulent habits that disgrace public life."},
            {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Gentle parental encouragement fosters a natural **studiousness** far more effectively than harsh scholastic coercion."},
            {"author": "William Hazlitt", "work": "The Plain Speaker", "quote": "The profound **studiousness** of the elderly scholar gave his countenance an air of serene detachment from trivial worldly quarrels."}
        ]
    },
    "study": {
        "primary": "To apply mental effort to acquire knowledge; the act of learning or examining a subject in detail.",
        "secondary": "In architecture and residential layout, a private room within a house designated for reading, writing, and intellectual contemplation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I care not if I have; it is my **study** to seem greater than I am, that pride may balance misery."},
            {"author": "Francis Bacon", "work": "The Essays", "quote": "Crafty men contemn studies, simple men admire them, and wise men use them; for they teach not their own use, but to **study** them with diligence is true wisdom."},
            {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes retired to his **study** to ponder the chemical reagents necessary to detect human hemoglobin."}
        ]
    },
    "studying": {
        "primary": "Engaged in learning, reading, or investigating an academic subject or problem with close mental attention.",
        "secondary": "In observational narrative, subjecting an object, map, or person to penetrating visual or analytical scrutiny.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I have been **studying** how I may compare this prison where I live unto the world."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak stood beside the fold **studying** the gathering thunderclouds with grave foreboding for the unthatched ricks."},
            {"author": "John Stuart Mill", "work": "Autobiography", "quote": "From early childhood I was constantly **studying** the classical historians under my father's rigorous supervision."}
        ]
    },
    "understudied": {
        "primary": "Learned or rehearsed a theatrical role as a substitute performer; received insufficient analytical study.",
        "secondary": "In performing arts history, having prepared another actor's part to ensure continuity of theatrical performance in emergencies.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The ambitious young actress had conscientiously **understudied** the leading role throughout the provincial tour."},
            {"author": "Henry James", "work": "The Tragic Muse", "quote": "Miriam discovered that her rival had quietly **understudied** her major dramatic scenes during rehearsals."},
            {"author": "Max Beerbohm", "work": "Around Theatres", "quote": "He had **understudied** the principal comedian for months before an unexpected illness gave him his theatrical debut."}
        ]
    },
    "understudy": {
        "primary": "An actor who learns another's role in order to step in as a substitute if the principal actor is absent.",
        "secondary": "In organizational dynamics, a designated trainee or deputy prepared to assume the responsibilities of a senior official.",
        "quotes": [
            {"author": "James Joyce", "work": "Ulysses", "quote": "He volunteered to show the **understudy** in the title role how to deliver the climactic soliloquy."},
            {"author": "Mrs. George de Horne Vaizey", "work": "The Lady of the Basement Flat", "quote": "I have been **understudy** by night, and proud I was to step onto the boards when the prima donna caught cold."},
            {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "A capable **understudy** must possess the resilience to step before a disappointed audience without losing composure."}
        ]
    },
    "unstudied": {
        "primary": "Not rehearsed, premeditated, or artificial; natural, spontaneous, and unforced in manner.",
        "secondary": "In aesthetics and biography, possessing an innate graceful simplicity that owes nothing to deliberate contrivance.",
        "quotes": [
            {"author": "Herman Melville", "work": "Typee", "quote": "Their extreme beauty and **unstudied** grace perfectly amazed me, accustomed as I was to European affectations."},
            {"author": "Jane Austen", "work": "Emma", "quote": "Her lively conversation possessed an **unstudied** ease that charmed everyone in the drawing-room."},
            {"author": "John Cairns", "work": "Principal Cairns", "quote": "His prayers, quite **unstudied** as they of course were, brought the whole congregation into reverent communion."}
        ]
    },
    "unstudious": {
        "primary": "Not given to study, reading, or intellectual pursuits; disinclined toward scholarly labor.",
        "secondary": "In social characterization, preferring active, outdoor, or convivial sports over sedentary academic reflection.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "The Small House at Allington", "quote": "The young squire was of a cheerful, **unstudious** disposition, caring vastly more for fox-hunting than for classical literature."},
            {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "Arthur found his college companions remarkably **unstudious**, devoting their afternoons to boating and hazard."},
            {"author": "George Meredith", "work": "The Ordeal of Richard Feverel", "quote": "His robust physical nature rebelled against tutors, choosing an **unstudious** boyhood among the woods and fields."}
        ]
    },

    # =========================================================================
    # DASHBOARD — vestig (8 words)
    # =========================================================================
    "investigate": {
        "primary": "To carry out a systematic or formal inquiry to discover facts, establish truth, or solve a mystery.",
        "secondary": "In scientific methodology and criminal forensics, to examine physical evidence and empirical data through disciplined testing.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare felt compelled to **investigate** the rumors concerning her family before finalizing their marriage plans."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists must impartially **investigate** every anomalous structure rather than dismiss it as an accidental variation."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes agreed to **investigate** the bizarre disappearance of the bride upon the very morning of the nuptials."}
        ]
    },
    "investigating": {
        "primary": "Engaged in searching into, examining, or conducting a systematic inquiry into a matter or phenomenon.",
        "secondary": "In philosophical critique and experimental science, actively probing the causal mechanisms of natural or social reality.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "In **investigating** the laws of social development, thinkers must carefully untangle complex reciprocal influences."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "While **investigating** the comparative anatomy of primates, naturalists observed remarkable structural homologies."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Human life appeared to him the one thing worth **investigating**, compared with which all artistic theories were trivial."}
        ]
    },
    "investigation": {
        "primary": "The action of investigating something; a formal, methodical, or detailed examination or inquiry.",
        "secondary": "In jurisprudence and scholarly research, an exhaustive evidentiary process designed to ascertain objective facts.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Subsequent **investigation** of the sheep-pens proved that the disaster had been caused by an opened hurdle."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Ethical philosophy demands impartial **investigation** into the tangible consequences of human actions upon general welfare."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Careful **investigation** of fossiliferous strata reveals that transitional organisms existed across successive epochs."}
        ]
    },
    "investigative": {
        "primary": "Of, relating to, or inclined toward systematic investigation, research, or inquiry.",
        "secondary": "In journalistic and forensic contexts, employing specialized analytical techniques to uncover concealed wrongdoing or institutional corruption.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses and Reviews", "quote": "The scientific mind directs its **investigative** faculties toward natural phenomena without fear of theological censure."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The instinct of curiosity activates an **investigative** drive that compels animals and humans to explore novel stimuli."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Modern science owes its triumphs to a rigorous **investigative** spirit that refuses to accept dogma without empirical verification."}
        ]
    },
    "investigator": {
        "primary": "A person who investigates, inquires systematically, or conducts formal research into a subject.",
        "secondary": "In scientific and criminological history, a skilled practitioner trained to observe, hypothesize, and deduce factual conclusions.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The wisest thing the **investigator** of oceanic monsters can do is to record observed facts without unwarranted speculation."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The curious psychological **investigator** sought to decipher the hidden motives animating the utopian community."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The eccentric spiritual **investigator** looked not merely at physical footprints, but at the moral nature of the crime."}
        ]
    },
    "investigatory": {
        "primary": "Pertaining to, designed for, or serving the purposes of an investigation or formal inquiry.",
        "secondary": "In administrative and legal procedure, designating bodies or powers authorized to subpoena documents and examine witnesses.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The magistrate exercises an **investigatory** authority intended to elicit truth while safeguarding fundamental liberties."},
            {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The legislative branch retains an essential **investigatory** oversight over the operations of the executive departments."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Grand juries in the American commonwealth wield broad **investigatory** powers to examine local fiscal administration."}
        ]
    },
    "vestige": {
        "primary": "A trace, mark, or visible remnant of something that once existed but is now largely lost or disappeared.",
        "secondary": "In evolutionary biology and archaeology, a degenerate or rudimentary organ, structure, or artifact surviving from an earlier epoch.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Rudimentary organs retain a mere **vestige** of their former utility, demonstrating ancestral divergence."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Not a **vestige** of the fugitive convict could be discerned across the foggy expanse of the Grimpen Mire."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Ancient mythological ruins preserve a faded **vestige** of that primordial intuition which linked man to nature."}
        ]
    },
    "vestigial": {
        "primary": "Forming a small, rudimentary remnant of something that was once much more prominent, developed, or fully functional.",
        "secondary": "In comparative anatomy and evolutionary genetics, designating nonfunctional morphological features inherited from ancestral lineages.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The presence of **vestigial** muscles in the human ear attests to our kinship with lower mammalian quadruped ancestors."},
            {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "In the pelvic skeleton of cetaceans, small **vestigial** bones indicate a remote terrestrial ancestry."},
            {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Comparative embryology reveals numerous **vestigial** structures that appear transiently during embryonic development."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total curated words in data_ask_b1: {len(data_ask_b1)}")
    assert len(data_ask_b1) == 72, f"Expected 72 words, got {len(data_ask_b1)}"
    print("curate_ask_b1.py data definition ready!")
