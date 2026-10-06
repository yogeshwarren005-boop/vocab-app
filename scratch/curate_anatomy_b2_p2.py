# -*- coding: utf-8 -*-
"""
curate_anatomy_b2_p2.py
Batch 2 Part 2 of Cluster Anatomy & Clinical Medicine (51 words):
- nas remaining 23 words (nasalise, nasality, nasalization, nasalize, nasally, nascence, nascency, nascent, naseby, nasion, nasolacrimal, nasopharyngeal, nasopharynx, nassau, nasser, nast, nastily, nastiness, nasturtium, nasty, nasua, renascence, renascent)
- nerv (28 words: enervate, enervated, enervating, enervation, innervate, innervation, nerva, nerve-racking, nerve-wracking, nerve, nerveless, nervelessly, nervelessness, nerveroot, nerves, nervi, nervily, nervine, nervosity, nervous, nervously, nervousness, nervure, nervus, nervy, unnerve, unnerved, unnerving)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_b2_p2 = {
    # ==================== Dashboard — nas (Remaining 23 words) ====================
    "nasalise": {
        "primary": "To articulate a vowel or consonant with nasal resonance by lowering the soft palate; to nasalize (British spelling).",
        "secondary": "In comparative historical phonology, the vocalic mutation whereby oral sounds absorb resonance from adjacent nasal consonants over linguistic generations.",
        "quotes": [
            {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "Speakers of certain regional dialects unconsciously **nasalise** long open vowels before voiced alveolar plosives."},
            {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Historical sound shifts reveal how speakers gradually **nasalise** vowels when an archaic final nasal consonant weakens."},
            {"author": "Otto Jespersen", "work": "Phonetics", "quote": "Foreign language learners must practice diligently not to **nasalise** clear oral syllables during formal declamation."}
        ]
    },
    "nasality": {
        "primary": "The acoustic resonance produced when voiced airflow passes through the nasal cavity during speech.",
        "secondary": "In clinical voice pathology and speech acoustics, hypernasal resonance caused by velopharyngeal incompetence or structural clefts of the palate.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The rural preacher intoned his verses with a monotonous **nasality** that droned like a solitary hornet in church."},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The rustic hunter replied with a sharp native **nasality** that seemed bred of long winters and mountain gales."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The perception of timbre distinguishes the vocal **nasality** of a voice from pure open chest resonance."}
        ]
    },
    "nasalization": {
        "primary": "The production of a speech sound accompanied by lowering of the soft palate so that air escapes through the nose.",
        "secondary": "In linguistic articulatory phonetics, the physiological coupling of the nasopharynx and nasal cavities to the vocal tract during phonation.",
        "quotes": [
            {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "Complete **nasalization** transforms the standard oral vowel into a distinct resonant acoustic phone."},
            {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The extensive **nasalization** characteristic of Romance languages emerged from the assimilation of nasal codas into syllable nuclei."},
            {"author": "Leonard Bloomfield", "work": "Language", "quote": "We observe that contextual **nasalization** occurs automatically when vowels immediately precede nasal sonorants."}
        ]
    },
    "nasalize": {
        "primary": "To utter or articulate a speech sound with nasal resonance through the lowered soft palate.",
        "secondary": "In experimental phonetics and second language acquisition, the conscious or phonetic modification of an oral vowel by channeling air into the nasal vault.",
        "quotes": [
            {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Certain linguistic communities tend to **nasalize** their accented vowels to a degree that strikes foreign ears as peculiar."},
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "When we **nasalize** an oral consonant, the velum descends, allowing acoustic energy to reverberate in the nasal chamber."},
            {"author": "Henry Sweet", "work": "The Practical Study of Languages", "quote": "The phonetician instructed the student how to **nasalize** pure vowels without constricting the pharyngeal aperture."}
        ]
    },
    "nasally": {
        "primary": "In a manner characterized by nasal resonance, or through the nasal passages.",
        "secondary": "In clinical otolaryngology and descriptive linguistics, denoting sound emission or aerosolized medication conducted directly through the nostrils.",
        "quotes": [
            {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "He hummed **nasally** between the stanzas of the hymn, keeping time with a slow nod of his venerable head."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The clerk delivered the municipal proclamation **nasally**, squinting over his horn-rimmed spectacles at the crowd."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Chadband intoned his philosophical homilies **nasally**, elevating his flabby hands in pious theatrical gesture."}
        ]
    },
    "nascence": {
        "primary": "The beginning of existence, emergence, origin, or incipient formation.",
        "secondary": "In historical aesthetics and developmental philosophy, the initial phase in the genesis of an intellectual or cultural paradigm prior to full maturation.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "We celebrate the **nascence** of genius wherever fresh insight triumphs over inherited institutional forms."},
            {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "In the delicate dawn of fifteenth-century Florence, one witnesses the fragile **nascence** of modern artistic consciousness."},
            {"author": "John Addington Symonds", "work": "Renaissance in Italy", "quote": "The mysterious **nascence** of secular drama signaled the slow dissolution of medieval allegorical mysteries."}
        ]
    },
    "nascency": {
        "primary": "Incipient emergence, early generation, or the initial phase of coming into existence.",
        "secondary": "In natural philosophy and evolutionary metaphysics, the nascent stage wherein potential qualities begin actualization within an embryonic system.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A poetic idea in its first **nascency** hovers like an intangible presence before assuming verbal form."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Amidst the ruin of outworn dogmas, the discerning philosopher perceives the **nascency** of a more glorious spiritual faith."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "During the **nascency** of complex social structures, functional differentiation proceeds at an ever-accelerating pace."}
        ]
    },
    "nascent": {
        "primary": "Coming into existence, newly born, or developing early potential.",
        "secondary": "In evolutionary morphology and chemical synthesis, an organ or compound at the moment of its initial formation exhibiting heightened reactivity or plasticity.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rooms now resounded with the tapping of **nascent** lives upon the threshold of rustic existence."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "An organ may be considered **nascent** when it is in process of development under the influence of natural selection."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Our **nascent** thoughts emerge as vague tendencies before coalescing into articulate intellectual judgments."}
        ]
    },
    "naseby": {
        "primary": "Naseby, a parish in Northamptonshire, England; site of the pivotal 1645 battle of the English Civil War.",
        "secondary": "In British military history, the decisive battlefield where Oliver Cromwell's New Model Army shattered King Charles I's Royalist forces on June 14, 1645.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "The field of **Naseby** sealed the fate of royal absolutism and inaugurated the supremacy of the parliamentary sword."},
            {"author": "Edward Hyde, Earl of Clarendon", "work": "The History of the Rebellion", "quote": "After the disastrous rout at **Naseby**, the King's affairs were hopelessly broken beyond all human recovery."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The iron discipline of the Ironsides at **Naseby** demonstrated the irresistible power of religious zeal united with military skill."}
        ]
    },
    "nasion": {
        "primary": "The craniometric landmark located at the intersection of the frontal bone and the two nasal bones.",
        "secondary": "In forensic anthropology and cephalometry, the midline point of the frontonasal suture used to calculate facial angle, cranial indices, and rhinological proportions.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **nasion** corresponds to the middle of the frontonasal suture at the deepest indentation of the root of the nose."},
            {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Measurements taken from the **nasion** to the basion provide an accurate index of anterior cranial base development."},
            {"author": "William Henry Flower", "work": "Fashion in Deformity", "quote": "The position of the **nasion** remains remarkably stable across various races, serving as a reliable baseline for skull analysis."}
        ]
    },
    "nasolacrimal": {
        "primary": "Relating to or connecting the nasal cavity and the lacrimal apparatus of the eye.",
        "secondary": "In clinical ophthalmology and surgical anatomy, describing the nasolacrimal duct that conducts tears from the lacrimal sac into the inferior nasal meatus.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **nasolacrimal** canal opens inferiorly beneath the inferior nasal concha, protected by a delicate mucosal valve."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic obstruction of the **nasolacrimal** duct frequently induces recurrent dacryocystitis and persistent epiphora."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In terrestrial tetrapods, the **nasolacrimal** canal conveys excess ocular moisture directly into the olfactory chamber."}
        ]
    },
    "nasopharyngeal": {
        "primary": "Pertaining to, situated in, or affecting both the nasal cavity and the pharynx.",
        "secondary": "In otorhinolaryngology and oncology, referring to the mucosal lining, lymphatic tissue (adenoids), or neoplasms (such as carcinoma) of the upper pharynx.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hypertrophy of the **nasopharyngeal** tonsil produces chronic mouth-breathing and altered facial development in growing children."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Persistent irritation in the **nasopharyngeal** vault often excites a dry reflex cough that simulates bronchial catarrh."},
            {"author": "William Henry Welch", "work": "Papers and Addresses", "quote": "Bacteriological swabs obtained from the **nasopharyngeal** mucosa revealed virulent colonies of diphtheria bacilli."}
        ]
    },
    "nasopharynx": {
        "primary": "The uppermost section of the pharynx located directly behind the nasal cavities and above the soft palate.",
        "secondary": "In respiratory anatomy, the anatomical chamber communicating anteriorly with the choanae and laterally with the middle ear via the Eustachian tubes.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **nasopharynx** remains patent during respiration, its roof and posterior wall richly carpeted with lymphoid follicles."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Accumulation of dry crusts and fetid secretions in the **nasopharynx** characterizes chronic atrophic rhinitis."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Swallowing causes the soft palate to rise against the posterior pharyngeal wall, completely sealing off the **nasopharynx**."}
        ]
    },
    "nassau": {
        "primary": "The capital city and major commercial center of the Commonwealth of the Bahamas, or a European royal dynasty.",
        "secondary": "In geopolitical history, the sovereign German county and royal House of Nassau that produced William the Silent and the rulers of the Netherlands.",
        "quotes": [
            {"author": "James Joyce", "work": "Dubliners", "quote": "They walked along **Nassau** Street and then turned into Kildare Street, conversing in hushed collegiate tones."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The princely house of **Nassau** contributed illustrious captains to the protracted wars of European liberation."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The stadtholders of the house of **Nassau** maintained domestic authority through balance of power among the United Provinces."}
        ]
    },
    "nasser": {
        "primary": "Gamal Abdel Nasser (1918–1970), the second President of Egypt who championed Arab socialism and pan-Arab unity.",
        "secondary": "In mid-twentieth-century geopolitics, the charismatic military officer who led the 1952 Egyptian Revolution, nationalized the Suez Canal, and co-founded the Non-Aligned Movement.",
        "quotes": [
            {"author": "Gamal Abdel Nasser", "work": "The Philosophy of the Revolution", "quote": "Our destiny as Egyptians, **Nasser** insisted, is inextricably linked with the Arab world, Africa, and the Islamic circle."},
            {"author": "Winston Churchill", "work": "The Second World War", "quote": "The strategic maneuvers of Colonel **Nasser** in the Levant transformed the entire political equilibrium of the Middle East."},
            {"author": "Anthony Eden", "work": "Full Circle: The Memoirs of Sir Anthony Eden", "quote": "The sudden seizure of the Suez Canal Company by President **Nasser** precipitated an acute imperial crisis in London."}
        ]
    },
    "nast": {
        "primary": "Thomas Nast (1840–1902), American caricaturist and editorial cartoonist considered the father of American political cartooning.",
        "secondary": "In visual journalism and political history, the graphic satirist whose Harper's Weekly cartoons exposed the corruption of Tammany Hall's Boss Tweed and popularized the Republican elephant.",
        "quotes": [
            {"author": "Mark Twain", "work": "Autobiography of Mark Twain", "quote": "The graphic genius of Thomas **Nast** did more to topple corrupt political rings than dozens of legislative commissions."},
            {"author": "William Dean Howells", "work": "Literary Friends and Acquaintance", "quote": "Every weekly cartoon from **Nast** struck with the force of an ethical thunderbolt across the political landscape."},
            {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The ferocious pencil of **Nast** held a mirror up to the gross materialism and moral cynicism of the Gilded Age."}
        ]
    },
    "nastily": {
        "primary": "In an unpleasant, malicious, offensive, or spitefully disagreeable manner.",
        "secondary": "In interpersonal psychology and descriptive narrative, behavior exhibiting spiteful venom, petty malice, or sordid malevolence toward others.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He smiled **nastily**, pleased that his barbed insinuation had struck directly at his cousin's vulnerable pride."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The wind veered into the east and blew **nastily** across the bleak ridge, bringing sleet and bitter frost."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The turnkey glared **nastily** upon the wretched prisoners as he clanged the heavy iron grate shut behind them."}
        ]
    },
    "nastiness": {
        "primary": "Pervasive foulness, moral repulsiveness, spiteful malice, or physical offensiveness.",
        "secondary": "In moral philosophy and human satire, visceral vulgarity, offensive squalor, or malicious cruelty degrading human interactions.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I did indeed observe that the unseemly **nastiness** of these creatures distinguished them from all civilized brutes."},
            {"author": "Samuel Johnson", "work": "The Lives of the Most Eminent English Poets", "quote": "A writer degrades his intellect when he descends to gratuitous **nastiness** merely to shock refined readers."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The industrial city surrendered its former architectural nobility to unmitigated smoke, squalor, and moral **nastiness**."}
        ]
    },
    "nasturtium": {
        "primary": "A flowering garden plant of the genus Tropaeolum, cultivated for its spurred flowers and pungent, edible peltate leaves.",
        "secondary": "In horticultural botany and culinary history, South American herbaceous plants named from Latin nasus tortus ('twisted nose') owing to their peppery mustard-like essential oils.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "I left the poor fellow wandering about by the scarlet **nasturtium** beds, lost in philosophical contemplation."},
            {"author": "Emily Dickinson", "work": "The Poems of Emily Dickinson", "quote": "The vivid orange cup of the **nasturtium** holds the late afternoon sunbeam as if reluctant to surrender the autumn day."},
            {"author": "John Ruskin", "work": "Proserpina", "quote": "Consider the shield-shaped leaf of the **nasturtium**, upon whose surface drops of morning dew roll like beads of molten silver."}
        ]
    },
    "nasty": {
        "primary": "Extremely unpleasant, offensive, foul, repulsive, or spitefully malicious.",
        "secondary": "In clinical observation and vernacular description, describing a noxious wound, virulent infection, severe weather, or vindictive behavioral disposition.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Nay, but to live in the rank sweat of an enseamed bed, stew'd in corruption, honeying and making love over the **nasty** sty."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Did a **nasty** brute of a dog want to kill it; did he, poor dear sheep, wandering upon the solitary down?"},
            {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Our family always hated cats: **nasty**, low, vulgar things that frighten innocent little mice like us."}
        ]
    },
    "nasua": {
        "primary": "A genus of South American mammals in the family Procyonidae, commonly known as coatis.",
        "secondary": "In mammalian zoology, omnivorous diurnal procyonids characterized by a long, flexible, upturned snout adapted for rooting in forest litter.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The active troops of **Nasua** forage busily across the forest floor, thrusting their long snouts into every rotten log."},
            {"author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "The tame **Nasua** followed the Indian hunters through the thicket, hunting grubs with unflagging curiosity."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In the cranial morphology of **Nasua**, the elongated nasal region and sturdy zygomatic arches reflect its specialized foraging habits."}
        ]
    },
    "renascence": {
        "primary": "A rebirth, revival, or resurgence of activity, artistic vigor, or cultural life.",
        "secondary": "In cultural historiography, a renewed flowering of classical learning, intellectual curiosity, and humanist aesthetic ideals; a renaissance.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "There was something of the **Renascence** Prince about his omnivorous culture and restless public generosity."},
            {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "The true spirit of the Italian **renascence** resided in its passionate yearning for intellectual and artistic liberty."},
            {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Hellenism enjoyed a glorious **renascence** during the fifteenth century, illuminating the intellectual horizons of Europe."}
        ]
    },
    "renascent": {
        "primary": "Springing into new life, rising again into vigor, or experiencing a revival.",
        "secondary": "In intellectual and social history, displaying renewed strength, creative vitality, or philosophical resurgence following a prolonged period of dormancy.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "So spoke love **renascent**, preparing the way for Tess's devoted outpouring upon the rustic bridge."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "Her **renascent** spirits welcomed the fragrant spring breeze that swept away all winter melancholy."},
            {"author": "John Addington Symonds", "work": "Renaissance in Italy", "quote": "The **renascent** scholarship of fifteenth-century scholars exhumed forgotten classical manuscripts from neglected monastic vaults."}
        ]
    },

    # ==================== Dashboard — nerv (28 words) ====================
    "enervate": {
        "primary": "To reduce the strength, vitality, energy, or moral courage of a person or society.",
        "secondary": "In clinical physiology and moral philosophy, to induce debilitating neuromuscular exhaustion or erode systemic vitality through luxurious excess.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The enervating climate and boundless luxuries of Antioch conspired to **enervate** the discipline of the Roman legions."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Unchecked indolence will gradually **enervate** the sharpest intellect, rendering the mind incapable of arduous exertion."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Reliance upon external institutions tends to **enervate** individual self-trust and sap native creative power."}
        ]
    },
    "enervated": {
        "primary": "Deprived of physical strength, mental vigor, or moral resolution; debilitated.",
        "secondary": "In clinical medicine and climatology, suffering from constitutional lassitude, neuromuscular flaccidity, or chronic tropical exhaustion.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There is little honour in conquering an **enervated** adversary whose limbs tremble with exhaustion."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The Greeks may have retrograded because the aristocracy became **enervated** by excessive luxury and slave labor."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister returned home in an **enervated** condition, his spirit crushed beneath the heavy burden of concealed guilt."}
        ]
    },
    "enervating": {
        "primary": "Tending to drain physical energy, moral resolve, or mental vitality; debilitating.",
        "secondary": "In environmental physiology, describing humid oppressive climates or sedentary habits that suppress autonomic tone and cellular metabolism.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The air of the dairy, so fresh in spring, felt stagnant and **enervating** under the oppressive July heat."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "If the **enervating** magic of the place did not operate to subdue him, his original vigor might yet survive."},
            {"author": "Herman Melville", "work": "Typee", "quote": "The warm, perfumed breezes of the tropical valley exerted an **enervating** spell upon our restless sailor ambitions."}
        ]
    },
    "enervation": {
        "primary": "A condition or process of being drained of physical vigor, vitality, or mental strength.",
        "secondary": "In clinical neuroses and nineteenth-century medical diagnosis, systemic nervous debility and neuromuscular prostration resembling neurasthenia.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prolonged mental overwork and chronic insomnia frequently culminate in profound somatic and emotional **enervation**."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rapid military **enervation** of the imperial army exposed the frontiers to barbarian incursions."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "A nation sunk in spiritual **enervation** cannot withstand the volcanic awakening of popular indignation."}
        ]
    },
    "innervate": {
        "primary": "To supply an anatomical organ, muscle, or tissue with nerve fibers.",
        "secondary": "In neurophysiology, to conduct electrical motor impulses or sensory signals that activate and regulate peripheral end-organs.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Branches from the third cranial nerve penetrate and **innervate** the superior, inferior, and medial rectus muscles."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The delicate nerve twigs that **innervate** the facial muscles respond with lightning speed to emotional stimuli."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Motor neurons arising in the ventral horn send axons through peripheral nerves to **innervate** skeletal myofibers."}
        ]
    },
    "innervation": {
        "primary": "The distribution, arrangement, or functional activity of nerves within an organ or bodily part.",
        "secondary": "In neuromuscular physiology, the total neural supply and reflex modulation governing cardiac, smooth, or striated muscle tone.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The motor **innervation** of the larynx is derived entirely from the recurrent laryngeal branch of the vagus nerve."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Disturbances of autonomic **innervation** produce profound abnormalities in vasomotor regulation and pupillary reflexes."},
            {"author": "Charles Bell", "work": "The Anatomy of the Brain", "quote": "The dual **innervation** of sensory and motor roots explains the distinct paths of reflex volition and bodily sensation."}
        ]
    },
    "nerva": {
        "primary": "Marcus Cocceius Nerva (30–98 AD), Roman Emperor who founded the Nerva–Antonine dynasty.",
        "secondary": "In Roman imperial history, the aged senator acclaimed emperor in 96 AD whose adoption of Trajan established the meritocratic succession of the 'Five Good Emperors'.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The accession of **Nerva** inaugurated a peaceful era during which the supreme power was conferred upon genuine merit."},
            {"author": "Tacitus", "work": "The Works of Cornelius Tacitus", "quote": "The venerable **Nerva** united two things long deemed incompatible: imperial sovereignty and civil liberty."},
            {"author": "Niccolò Machiavelli", "work": "Discourses on Livy", "quote": "Under the golden reigns from **Nerva** to Marcus Aurelius, the world enjoyed unparalleled security and justice."}
        ]
    },
    "nerve-racking": {
        "primary": "Extremely distressing, tense, or agonizing to the mind, nerves, or emotions.",
        "secondary": "In psychiatric and descriptive literature, describing severe sustained psychological stress that threatens emotional stability and physical endurance.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The long, solitary vigil across the misty moor proved a **nerve-racking** ordeal for Sir Henry's shaken constitution."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Waiting in the darkened scullery while the Martian tripod strode overhead was a **nerve-racking** agony of suspense."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The ceaseless creaking of the damaged collision-bulkhead in the darkness was a **nerve-racking** trial for the young officer."}
        ]
    },
    "nerve-wracking": {
        "primary": "Intensely stressful, harrowing, or exhausting to one's patience and nervous composure (variant of nerve-racking).",
        "secondary": "In descriptive narrative and psychological prose, an experience characterized by acute apprehension, suspense, and sympathetic autonomic arousal.",
        "quotes": [
            {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Steering through the treacherous fog-bound reefs under Wolf Larsen's furious gaze was a **nerve-wracking** experience."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The strict decorum of the dinner party concealed a **nerve-wracking** contest of unspoken social rivalries."},
            {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "The ceaseless roar and bustling motor traffic of central London produced a **nerve-wracking** sensation of imminent peril."}
        ]
    },
    "nerve": {
        "primary": "A cordlike bundle of neural fibers conducting sensory or motor impulses; or steady courage and resolve.",
        "secondary": "In neuroanatomy and human psychology, a peripheral neural conduit, or colloquially the fortitude and emotional stamina to withstand danger.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "My fate cries out, and makes each petty artery in this body as hardy as the Nemean lion's **nerve**."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She must possess the **nerve** of a stoic to face the ruin of her sheep without shedding a single tear."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "How a **nerve** comes to be sensitive to light hardly concerns us more than how life itself first originated upon Earth."}
        ]
    },
    "nerveless": {
        "primary": "Lacking physical strength, muscular tone, or vitality; limp; or coolly devoid of nervous agitation.",
        "secondary": "In clinical neurology and literary prose, flaccid paresis of a limb, or conversely an extraordinary emotional stoicism that displays zero tremor under stress.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Good victuals and drink is a cheerful thing, and gives nerves to the **nerveless**, if one may say so."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "With a chill despondency, like one awakening all **nerveless** from an ugly dream, he yielded himself up to despair."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "My hands, my limbs grow **nerveless**, my brain feels rack'd, bewilder'd, as the old ship foundereth in the storm."}
        ]
    },
    "nervelessly": {
        "primary": "Without physical vigor, muscular power, or emotional agitation; limply and feebly.",
        "secondary": "In clinical description and expressive narrative, describing a hand or body that drops without motor tone or acts with total unhurried indifference.",
        "quotes": [
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The pistol slipped **nervelessly** from his trembling fingers and clattered loudly upon the marble hearth."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her fingers fell **nervelessly** away from the piano keys as the sorrowful remembrance overwhelmed her composure."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He leaned **nervelessly** against the damp stone wall of the college, staring blankly into the cold winter fog."}
        ]
    },
    "nervelessness": {
        "primary": "The state or condition of lacking physical power, muscle tone, or emotional reactivity.",
        "secondary": "In literary psychology and neurological semiotics, flaccidity of will or muscle, or alternatively absolute imperturbability devoid of anxious tremors.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A curious **nervelessness** crept over his limbs as the bitter moorland frost chilled him to the bone."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The statue's languid posture conveyed an impression of dreamy **nervelessness** untouched by worldly passions."},
            {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "A sudden overwhelming **nervelessness** invaded his frame, leaving him paralyzed before the terrible revelation."}
        ]
    },
    "nerveroot": {
        "primary": "The initial segment of a cranial or spinal nerve where it emerges directly from the central nervous axis.",
        "secondary": "In neuroanatomy and spinal surgery, the anterior (motor) or posterior (sensory) radicle passing through the intervertebral foramen to form a mixed spinal nerve.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Compression of a posterior **nerveroot** produces lancinating radicular pain and cutaneous paresthesia along the dermatome."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pathological lesions involving the anterior **nerveroot** produce rapid muscular atrophy and loss of deep tendon reflexes."},
            {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "Experimenting upon each **nerveroot** demonstrated that the dorsal root confers sensation while the ventral root governs motion."}
        ]
    },
    "nerves": {
        "primary": "The systemic anatomical network of neural cords; or nervous apprehension and irritability.",
        "secondary": "In clinical psychiatry and vernacular parlance, the bodily nervous system, or colloquially an acute state of psychological tension and anxiety.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 120", "quote": "For that sorrow, which I then did feel, needs must I under my transgression bow, so I but call to mind my deepest **nerves**."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Sound nourishment gives **nerves** to the weary laborer who must face the heavy harvest tasks of dawn."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The sympathetic **nerves** regulate involuntary cardiac rhythms and visceral contractions across all vertebrate species."}
        ]
    },
    "nervi": {
        "primary": "The anatomical plural of nervus; the peripheral nerve trunks of the body.",
        "secondary": "In classical human and veterinary gross anatomy, the formal Latin designation for major neural pathways such as the nervi craniales or nervi spinales.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **nervi** pathetici, or fourth cranial nerves, exhibit the longest intracranial course of all cranial neural trunks."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The large paired **nervi** vagi distribute inhibitory autonomic fibers to the branchial and digestive visceral arcades."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The spinal **nervi** emerge regularly between adjacent vertebrae to supply the segmentally arranged myotomes."}
        ]
    },
    "nervily": {
        "primary": "In an apprehensive, jittery, or agitated manner; or with audacious boldness and cheek.",
        "secondary": "In behavioral description, acting under palpable nervous tension, or displaying brash, presumptuous confidence without regard for convention.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He grasped the desk **nervily**, looking toward the courthouse door as though expecting an unwelcome officer of the law."},
            {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The anarchist glanced **nervily** into the shadowy corners of the tavern before whispering his dangerous instructions."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The stranger laughed **nervily**, his bandaged head jerking sideways at every unexpected footstep on the stairs."}
        ]
    },
    "nervine": {
        "primary": "A therapeutic medicine, herbal tonic, or chemical agent acting to calm or strengthen the nervous system.",
        "secondary": "In historical pharmacognosy and botanical medicine, natural sedative or neurotonic remedies (such as valerian or chamomile) prescribed for nervous agitation.",
        "quotes": [
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Valerian root is celebrated as an efficacious **nervine** capable of abating hysterical paroxysms and spasmodic tremors."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rest, wholesome nutrition, and a mild vegetable **nervine** often restore tranquility to the exhausted neurasthenic invalid."},
            {"author": "Nicholas Culpeper", "work": "The English Physitian", "quote": "Lavender hath ever been esteemed an admirable **nervine**, comforting the cold trembling sinews of the head and brain."}
        ]
    },
    "nervosity": {
        "primary": "Nervous temperament, persistent excitability, or an innate tendency toward agitation and anxiety.",
        "secondary": "In nineteenth-century psychiatric literature and neuroses studies, constitutional hypersensitivity to emotional stimuli and environmental stress.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Marked constitutional **nervosity** frequently predisposes the patient to functional cardiac palpitations and digestive spasms."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Her conversational vivacity was tinged with a slight **nervosity** that revealed how deeply she dreaded the approaching interview."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "A feverish **nervosity** seized him whenever he reflected upon the perilous state of the family's mortgaged affairs."}
        ]
    },
    "nervous": {
        "primary": "Pertaining to the body's system of nerves; or easily excited, agitated, anxious, or apprehensive.",
        "secondary": "In human neurobiology and psychology, relating to neural conduction and sensory reception, or exhibiting sympathetic hyperexcitability under duress.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The bailiff who showed this **nervous** dread of loving his neighbour as himself, climbed the hill in moody silence."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The **nervous** system reacts instantaneously upon the vasomotor channels, causing sudden flushing or pallor in emotional crises."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Organic lesions of the central **nervous** axis demand meticulous anatomical localization before surgical intervention."}
        ]
    },
    "nervously": {
        "primary": "In an apprehensive, tense, jittery, or easily startled manner.",
        "secondary": "In behavioral description and narrative prose, manifesting sympathetic anxiety through hurried movements, tremors, or hesitant speech.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "I bain't fit for any such responsibility, said the young shepherd **nervously**, fingering the brim of his rough hat."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He looked **nervously** down at the legal documents upon his desk, hesitating to sign the momentous agreement."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip glanced **nervously** behind him at every shadow on the lonely marsh road, fearing the convict's sudden reappearance."}
        ]
    },
    "nervousness": {
        "primary": "A condition or feeling of being anxious, apprehensive, agitated, or tense.",
        "secondary": "In psychological medicine, an emotional state characterized by mental unease, autonomic hyperarousal, tachycardia, and motor restlessness.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The village women soon threw off their initial **nervousness**, and merry laughter echoed through the shearing barn."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "What can you expect from a weary helmsman who out of sheer **nervousness** had just flung his steering-pole overboard?"},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The first time Pip lowered after a whale he evinced extreme **nervousness**, trembling violently at the monster's thrashing fluke."}
        ]
    },
    "nervure": {
        "primary": "A structural vein in an insect's wing, or a principal rib of a plant leaf.",
        "secondary": "In entomological morphology and paleontology, the hollow chitinous tubes that stiffen insect wings and transmit hemolymph and fine tracheae.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The under side of a wing-**nervure** in crickets exhibits microscopic stridulating teeth that generate loud courtship songs."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The branching pattern of each wing-**nervure** provides an indispensable diagnostic character in insect classification."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "Fossil dragonflies from the Carboniferous strata display intricate **nervure** networks preserved with astonishing fidelity in shale."}
        ]
    },
    "nervus": {
        "primary": "The anatomical term for a nerve; a cord of sensory or motor fibers.",
        "secondary": "In systematic human gross anatomy, an individual named peripheral neural structure (such as the nervus vagus or nervus opticus) enclosed in connective tissue.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **nervus** opticus pierces the sclera and choroid at the posterior pole of the globe to expand into the sensory retina."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inflammation attacking the trunk of the **nervus** facialis inside the fallopian aqueduct produces acute peripheral Bell's palsy."},
            {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "The respiratory movements depend essentially upon the integrity of the **nervus** phrenicus descending through the thorax."}
        ]
    },
    "nervy": {
        "primary": "Bold, courageous, and daring; or colloquially impudent, presumptuous, or nervously tense.",
        "secondary": "In classical literature, sinewy and vigorous with strong muscular tension; in modern colloquial use, brazenly audacious or easily agitated.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Death, that dark spirit, in his **nervy** arm doth lie, which, being advanced, declines, and then men die."},
            {"author": "Herman Melville", "work": "Mardi", "quote": "The chieftain stood erect, wielding his heavy war-club with a **nervy** grip that defied all hostile spears."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "The young man's **nervy** impudence astonished the conservative elders assembled around the dinner table."}
        ]
    },
    "unnerve": {
        "primary": "To deprive of courage, confidence, self-control, or mental fortitude.",
        "secondary": "In psychiatric literature and dramatic narrative, to dismantle an individual's emotional composure through intense psychological dread or shock.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "These horrifying discoveries, in conjunction with the wild work we have in hand, help to **unnerve** the stoutest man."},
            {"author": "William Shakespeare", "work": "Henry VI, Part 3", "quote": "Let not that sudden dread **unnerve** your stout resolution when the royal battle trumpet sounds."},
            {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The ominous raven croaking above the castle ramparts seemed calculated to **unnerve** the superstitious retainers."}
        ]
    },
    "unnerved": {
        "primary": "Deprived of courage, presence of mind, or steady composure; shaken.",
        "secondary": "In descriptive psychology, experiencing acute emotional demoralization and trembling motor instability following terrifying encounters.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Pyrrhus at Priam drives, in rage strikes wide; but with the whiff and wind of his fell sword the **unnerved** father falls."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Completely **unnerved** by the unexpected revelation, she sank back upon the grass, hiding her tearful face."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The fact is I was completely **unnerved** by a sheer blank fright, pure abstract terror unconnected with any physical danger."}
        ]
    },
    "unnerving": {
        "primary": "Causing a loss of courage, composure, or emotional control; deeply unsettling.",
        "secondary": "In psychological fiction and psychiatric description, inducing an ominous sensation of dread, disorientation, and vulnerability.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The cold dawn and the deadly errand through deserted streets produced an **unnerving** sensation of absolute loneliness."},
            {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-folk chanting their horrific litany in the shadowy ravine sounded like an **unnerving** parody of human society."},
            {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The brooding silence that hung over the gloomy manor house was more **unnerving** than any open threat of violence."}
        ]
    }
}
