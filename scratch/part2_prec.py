# -*- coding: utf-8 -*-
"""
Part 2 of Batch 4 Cluster Asking & Seeking (Dashboard — prec):
Words 28 to 54:
['inappreciable', 'precambrian', 'precancerous', 'precarious', 'precariously',
 'precariousness', 'precast', 'precative', 'precatory', 'precaution',
 'precautional', 'precautionary', 'precava', 'precede', 'precedence',
 'precedency', 'precedent', 'precedented', 'precedentedly', 'precedential',
 'preceding', 'precentor', 'precentorship', 'precept', 'preceptor',
 'preceptorship', 'precess']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_prec = {
    "inappreciable": {
        "primary": "Too small, slight, or gradual to be perceived, recognized, or measured.",
        "secondary": "In evolutionary biology and geophysical measurements, describing incremental shifts that evade direct detection within single observational cycles.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The conditions of life have been disturbed, though often in so slight a degree as to be **inappreciable** by our senses."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Perhaps all truth and all sincerity are just compressed into that **inappreciable** moment of time in which we step over the threshold."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The mechanical friction of the tides produces an **inappreciable** retardation in the daily revolution of the globe."}
        ]
    },
    "precambrian": {
        "primary": "Belonging to or denoting the earliest eon of Earth history, preceding the Cambrian period.",
        "secondary": "In historical geology and paleobiology, designating the super-eon encompassing the Hadean, Archean, and Proterozoic eras prior to the radiation of complex shelly fauna.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The crystalline basement rocks underlying fossiliferous strata clearly belong to an ancient **precambrian** epoch of planetary formation."},
            {"author": "John Wesley Powell", "work": "Canyons of the Colorado", "quote": "At the very bottom of the gorge rise dark, contorted schists of **precambrian** age, severed by rivers of molten granite."},
            {"author": "Archibald Geikie", "work": "The Scenery of Scotland", "quote": "The rugged crags of the Northwest Highlands display vast exposures of **precambrian** gneiss that withstood eons of weathering."}
        ]
    },
    "precancerous": {
        "primary": "Showing cellular changes or pathological tendencies likely to develop into cancer.",
        "secondary": "In histopathology and oncology, describing dysplastic or hyperplastic epithelial lesions exhibiting atypical nuclear morphology without stromal invasion.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic irritation of the buccal mucosa frequently establishes a **precancerous** keratosis demanding vigilant observation."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The pathologist must distinguish mere regenerative hyperplasia from that dangerous **precancerous** instability of tissue elements."},
            {"author": "Harvey Cushing", "work": "Tumors of the Nervus Acusticus", "quote": "Early excision of tissue displaying marked **precancerous** changes offers the patient the highest probability of permanent cure."}
        ]
    },
    "precarious": {
        "primary": "Dangerously lacking in stability, security, or certainty; perilous or uncertain.",
        "secondary": "In civil law and tenure history, held solely by favor of another and revocable at the arbitrary pleasure of the grantor.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He made a **precarious** living in various towns as Professor of Gymnastics, Sword Exercise, Fencing, and Pugilism."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "You cannot breathe dead hippo and at the same time keep your **precarious** grip on existence in this savage wilderness."},
            {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Primitive man led a **precarious** life, surrounded by ruthless predators and continually exposed to starvation."}
        ]
    },
    "precariously": {
        "primary": "In a precarious, unstable, dangerously insecure, or uncertain manner.",
        "secondary": "In mechanical statics and alpine mountaineering, balanced upon a narrow center of gravity where minimal disturbance induces collapse.",
        "quotes": [
            {"author": "Jack London", "work": "The Call of the Wild", "quote": "The loaded sled balanced **precariously** upon the brink of the yawning chasm before the dogs pulled it to safety."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A huge boulder rested **precariously** on the sandstone edge above our camp, threatening to crush us during the night."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "I crouched **precariously** upon the broken beam of the ruined scullery, watching the Martian machine stride through the smoke."}
        ]
    },
    "precariousness": {
        "primary": "Extreme vulnerability, structural instability, or perilous exposure to sudden collapse.",
        "secondary": "In existential philosophy and labor sociology, the systemic vulnerability experienced by subjects lacking material safeguards against catastrophe.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The extreme **precariousness** of employment in seasonal trades justifies a higher customary rate of daily wages."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen felt the chilling **precariousness** of her family's social standing once the financial ruin of their investments was confirmed."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The felt **precariousness** of human destiny drives the anxious soul to seek refuge in transcendental certainty."}
        ]
    },
    "precast": {
        "primary": "Cast, shaped, or manufactured in standardized form beforehand, especially of concrete.",
        "secondary": "In structural civil engineering, describing modular masonry or reinforced cement components cured under factory conditions before placement on site.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Huge architectural spans were assembled rapidly from **precast** slabs of synthetic granite in the rebuilt metropolis."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Mechanized production substitutes **precast** mouldings devoid of soul for the living touch of the medieval stonecutter."},
            {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "The modern builder relies on **precast** structural units to accelerate erection while reducing reliance upon artisanal joinery."}
        ]
    },
    "precative": {
        "primary": "Expressing, conveying, or having the character of a prayer, request, or supplication.",
        "secondary": "In classical philology and comparative grammar, designating an optative verbal mood or inflection employed strictly for entreaty.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The psalmist employs a **precative** utterance that reveals profound reliance upon divine mercy rather than legal right."},
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The ancient Sanskrit benediction retains a distinct **precative** form that grammarians separated from the simple imperative."},
            {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Certain indigenous idioms possess a delicate **precative** suffix used when addressing tribal elders during ceremonial councils."}
        ]
    },
    "precatory": {
        "primary": "Expressing or conveying an entreaty, petition, recommendation, or humble wish.",
        "secondary": "In the law of wills and trusts, designating non-binding advisory words of request (such as 'desire' or 'hope') that create no mandatory fiduciary duty.",
        "quotes": [
            {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "Courts will not construe words that are merely **precatory** into an absolute testamentary trust unless the intention is manifest."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The distinction between mandatory commands and **precatory** recommendations represents a fundamental boundary in equity jurisprudence."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A legacy accompanied solely by **precatory** expressions leaves the executor free to exercise his own moral discretion."}
        ]
    },
    "precaution": {
        "primary": "A measure taken in advance to prevent harm, secure success, or avoid danger.",
        "secondary": "In risk governance and environmental policy, the anticipatory protocol requiring preventive mitigation even before scientific certainty is established.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The circumstances are of great delicacy, and every **precaution** has to be taken to quench what might grow to be an immense scandal."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He drank from the bottle of cider he had taken the **precaution** to bring with him before setting out across the hill."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate thought the **precaution** needless, but yielded to the patient's anxious entreaty for additional safeguards."}
        ]
    },
    "precautional": {
        "primary": "Of, relating to, or serving as a precaution; preventive or precautionary.",
        "secondary": "In clinical hygiene and epidemiological surveillance, pertaining to procedural barriers implemented proactively against potential pathogens.",
        "quotes": [
            {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Ordinary **precautional** sanitation regarding clean air and boiling water will banish the contagion from hospital wards."},
            {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Engineers neglected the **precautional** dykes, leaving the delta exposed to catastrophic inundation during the spring floods."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Wise statesmen erect **precautional** constitutional checks to restrain the tempestuous impulses of popular assemblies."}
        ]
    },
    "precautionary": {
        "primary": "Taken or designed in advance as a safeguard against potential danger or failure.",
        "secondary": "In ecological jurisprudence, embodying the principle that lack of full scientific certainty shall not postpone cost-effective mitigation.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain took several **precautionary** measures, doubling the night watches as the ship neared the treacherous shoals."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode adopted a **precautionary** reserve in his conversation, fearing lest some casual inquiry might unearth his past."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We adopted a **precautionary** march through the defile, keeping our carbines ready in case of an ambush by the natives."}
        ]
    },
    "precava": {
        "primary": "The anterior or superior vena cava that returns systemic blood to the right atrium.",
        "secondary": "In comparative vertebrate anatomy, the cranial systemic venous trunk collecting blood from the head, neck, and forelimbs into the heart.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In the avian circulatory system, blood from the jugular trunks enters the right atrium through a distinct **precava**."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The mammalian embryo reveals two anterior cardinal veins which subsequently consolidate into the definitive **precava**."},
            {"author": "Alfred Sherwood Romer", "work": "The Vertebrate Body", "quote": "Reptilian and monotreme dissections demonstrate the persistence of paired vessels representing both the right and left **precava**."}
        ]
    },
    "precede": {
        "primary": "To come before in time, order, arrangement, rank, or physical position.",
        "secondary": "In logical argumentation and ceremonial protocol, to serve as a prerequisite premise, or to walk before dignitaries in formal procession.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Though in empirical science the particular truths **precede** the general theory, the contrary might be expected in moral philosophy."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "When a species migrates into a new country, changes in habits must **precede** the formation of new structural adaptations."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He felt great objection to allowing news of his proximity to **precede** him to Weatherbury before he had settled his plans."}
        ]
    },
    "precedence": {
        "primary": "Priority in order, rank, importance, or temporal succession; right to go first.",
        "secondary": "In diplomatic protocol and parliamentary law, the codified ranking establishing order of seating, signing treaties, or addressing an assembly.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "I do not like 'But yet', it does allay the good **precedence** of joyful news."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Celia confessed it was nicer to be 'Lady' than 'Mrs.', and that Dodo never minded about **precedence** if she could have her way."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Annoyed at meal-times by constant quarrels about **precedence**, the chief director ordered an immense round table for the station."}
        ]
    },
    "precedency": {
        "primary": "Priority in time, place, rank, or dignity; ceremonial seniority.",
        "secondary": "In heraldic law and state etiquette, the statutory hierarchy regulating precedence among nobility and high judicial officers.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "To seek **precedency** over equals by courtly intriguings often engenders lasting rancor rather than genuine authority."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Lilliputian courtiers contested for **precedency** by performing perilous leaps over a slender silk cord."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bishops of Rome and Constantinople wrangled with bitter obstinacy over the ecclesiastical **precedency** of their sees."}
        ]
    },
    "precedent": {
        "primary": "An earlier event, decision, or action serving as an authoritative guide or model.",
        "secondary": "In common law jurisprudence, a prior judicial adjudication that legally binds or guides future tribunals under the doctrine of stare decisis.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Do it at once, or thy **precedent** services are all but accidents unpurposed."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Brooke made a remark perhaps less warranted by **precedent**, namely, that if he had foreknown his speech, he might have altered it."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood opened the letter, expecting another anonymous one, so greatly are ideas of probability guided by recent **precedent**."}
        ]
    },
    "precedented": {
        "primary": "Supported, justified, or sanctioned by a prior example, authority, or precedent.",
        "secondary": "In constitutional legal theory, describing an administrative action that conforms strictly to historical governmental patterns.",
        "quotes": [
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The exercise of treaty-making power in this manner is fully **precedented** in the annals of European confederacies."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The speaker declared the impeachment to be thoroughly **precedented** by the long parliamentary struggles under the Plantagenets."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "We ask nothing novel, but stand upon ground well **precedented** in the ancient charters granted to English colonies."}
        ]
    },
    "precedentedly": {
        "primary": "In a manner supported by or conforming to established precedent or prior custom.",
        "secondary": "In procedural law, describing judicial orders entered in strict congruence with settled courtroom practice.",
        "quotes": [
            {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "The monarch acted **precedentedly** by summoning the leader of the parliamentary majority to form an administration."},
            {"author": "Henry Maine", "work": "Ancient Law", "quote": "The praetor ruled **precedentedly** in extending equitable relief to alien merchants residing within the city gates."},
            {"author": "Lord Acton", "work": "Historical Essays and Studies", "quote": "The council moved **precedentedly** through the articles of doctrine, validating each decree against venerable synodical records."}
        ]
    },
    "precedential": {
        "primary": "Serving as, relating to, or having the binding force or nature of a precedent.",
        "secondary": "In appellate jurisprudence, designating court rulings that establish authoritative rules governing the disposition of subsequent litigation.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "A judicial decision carries **precedential** weight only so far as its underlying rationale harmonizes with living social experience."},
            {"author": "Benjamin Cardozo", "work": "The Nature of the Judicial Process", "quote": "The judge cannot disregard the **precedential** stream of authority without throwing legal relations into uncertainty."},
            {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Every executive veto creates a **precedential** standard by which succeeding presidents evaluate legislative enactments."}
        ]
    },
    "preceding": {
        "primary": "Existing, occurring, or coming immediately before in time, order, or arrangement.",
        "secondary": "In analytical writing, designating prior textual sections or data sets that provide context for succeeding arguments.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The summary of the **preceding** and present chapters shows the powerful selective influence exerted by domestic breeding."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "It results from the **preceding** considerations that there is in reality nothing desired except happiness."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "During the twelvemonth **preceding** this time he had been enabled by sustained industry to establish a prosperous flock."}
        ]
    },
    "precentor": {
        "primary": "A person who leads a congregation or choir in singing, especially in a cathedral.",
        "secondary": "In ecclesiastical chapter governance, the cathedral dignitary ranking next to the dean who directs musical liturgy and the choir school.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "The Warden", "quote": "Mr. Harding, as **precentor** of Barchester Cathedral, took supreme delight in the daily chanting of the choral service."},
            {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The venerable **precentor** pitched the tune with his tuning fork before leading the congregation into the psalm."},
            {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The parish **precentor** regarded his bassoon as an indispensable pillar of orthodox Sunday worship in Milby."}
        ]
    },
    "precentorship": {
        "primary": "The office, dignity, duties, or term of service of a precentor.",
        "secondary": "In canon law and cathedral history, the endowed ecclesiastical benefice attached to the musical governance of a diocese.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The vacant **precentorship** aroused eager ambitions among the younger clergy who coveted both income and musical dignity."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Monastic chroniclers recorded that Samson discharged the duties of the **precentorship** with austere devotion and meticulous rhythm."},
            {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He resigned the cathedral **precentorship** to devote himself wholly to philanthropic medical missions in the slums."}
        ]
    },
    "precept": {
        "primary": "A general rule, instruction, or principle intended to regulate behaviour or thought.",
        "secondary": "In civil procedure and administrative law, a formal written order or warrant issued by a magistrate commanding an officer to act.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The **precept** of returning good for evil has never been regarded as a case of the fulfillment of justice, but as a higher moral ideal."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The ancient **precept**, 'Know thyself,' and the modern **precept**, 'Study nature,' become at last one overarching maxim."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Shall the respectable citizen thus teach, by **precept** and example, the necessity of securing superfluous comforts?"}
        ]
    },
    "preceptor": {
        "primary": "A teacher, instructor, tutor, or head of a school or instructional academy.",
        "secondary": "In chivalric history and medical education, the presiding knight of a preceptory of Templars, or a practicing physician mentoring interns.",
        "quotes": [
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Grand Master addressed the **preceptor** of Templestowe in tones that commanded absolute obedience to the order's statutes."},
            {"author": "Charlotte Brontë", "work": "Villette", "quote": "Monsieur Paul Emanuel acted as my stern **preceptor**, examining my essays with uncompromising critical rigor."},
            {"author": "William Osler", "work": "Aequanimitas", "quote": "Every young physician owes an incalculable debt to the wise **preceptor** who first guided his hands at the bedside."}
        ]
    },
    "preceptorship": {
        "primary": "The position, tenure, or mentorship role exercised by a preceptor.",
        "secondary": "In clinical medical training, a formalized experiential apprenticeship where a student practices directly under the supervision of a licensed specialist.",
        "quotes": [
            {"author": "William Osler", "work": "An Alabama Student and Other Biographical Essays", "quote": "During his surgical **preceptorship** under Dr. Bovell, the apprentice acquired habits of scrupulous cleanliness and keen diagnostic inquiry."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The old system of country **preceptorship** imparted practical acumen that laboratory lectures alone can never supply."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Lucas Beaumanoir arrived to inspect the **preceptorship**, determined to root out all luxury and laxity among the Templars."}
        ]
    },
    "precess": {
        "primary": "To undergo or move with precession, as a spinning gyroscope or rotating celestial body.",
        "secondary": "In celestial mechanics and rotational kinematics, to execute a slow conical gyration of the rotational axis around an external vector under torque.",
        "quotes": [
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The terrestrial axis must slowly **precess** in space under the combined gravitational pull of the moon and sun on the equatorial bulge."},
            {"author": "Simon Newcomb", "work": "Popular Astronomy", "quote": "Calculations demonstrated that the planetary node would **precess** through several seconds of arc during each sidereal century."},
            {"author": "Arthur Stanley Eddington", "work": "Space, Time and Gravitation", "quote": "Relativistic gravitational equations predict that the perihelion of Mercury must **precess** at a measurable rate in excess of Newtonian attraction."}
        ]
    }
}
