import json
import os

BATCH2_DATA = {
  "Dashboard — in/in.md": {
    "primary": "In anatomical and biochemical nomenclature, a combining root denoting fibrous tissue, sinew, or muscular strength (from Greek ἴς, ἰνός); also functioning in standard English as a fundamental preposition or adverb indicating inclusion within limits of space, time, or circumstance.",
    "secondary": "In physiological terminology, designating fiber components or fibrous formations (as in inosinic acid or inoma); colloquially and idiomatically used in English to designate social belonging, advantage, or internal operational details ('the ins and outs').",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Knowledge that tendeth but to satisfaction is but as a courtesan, which is for pleasure, and not for fruit or generation; but that which is fruitful, is **in** such sort as may be profitable to human life."
      },
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "To be, or not to be, that is the question: Whether 'tis nobler **in** the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The mind is its own place, and **in** itself can make a heaven of hell, a hell of heaven."
      }
    ]
  },
  "Dashboard — in/inion.md": {
    "primary": "The most prominent projection of the external occipital protuberance at the lower posterior portion of the human skull, serving as a critical craniometric landmark.",
    "secondary": "In physical anthropology and cephalometry, the midline point at the junction of the superior nuchal lines, utilized to determine cranial capacity, facial angles, and nuchal ligament attachment.",
    "quotes": [
      {
        "author": "William Henry Flower",
        "work": "Fashion in Deformity",
        "quote": "The external occipital protuberance, or **inion**, serves as a fundamental posterior boundary in craniometrical determinations."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Measurements of cranial height and sagittal arc consistently employ the **inion** as the posterior anchor point."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The ligamentum nuchae attaches directly to the **inion**, providing structural suspension for the head."
      }
    ]
  },
  "Dashboard — in/inotrope.md": {
    "primary": "An agent, drug, or chemical substance that alters the force or energy of muscular contractions, particularly within the myocardium.",
    "secondary": "In cardiovascular pharmacology and critical care, an agent classified as positive (augmenting contractile force, e.g., dobutamine, milrinone) or negative (decreasing contractile force, e.g., beta-blockers) to optimize cardiac output.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "The administration of a positive **inotrope** is indicated to restore hemodynamic stability in acute cardiogenic decompensation."
      },
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "Digoxin functions as a classic cardiac **inotrope** by inhibiting sodium-potassium ATPase and elevating intracellular calcium."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When cardiac dilatation threatens catastrophic failure, the judicious application of a myocardial **inotrope** may restore ventricular tone."
      }
    ]
  },
  "Dashboard — in/inotropic.md": {
    "primary": "Influencing or modifying the force or energy of muscular contractions, especially of the heart muscle.",
    "secondary": "In hemodynamics and cardiology, designating physiological mechanisms or therapeutic agents that modulate myocardial contractile performance independently of heart rate or preload.",
    "quotes": [
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Sympathetic stimulation exerts a powerful positive **inotropic** effect upon ventricular muscle, substantially increasing stroke work."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Beta-adrenergic agonists augment **inotropic** state by activating adenylate cyclase and increasing intracellular cyclic AMP."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Digitalis remains the sovereign agent for augmenting the **inotropic** energy of the failing myocardium."
      }
    ]
  },
  "Dashboard — in/rein.md": {
    "primary": "A long, narrow strap fastened to each side of a bridle bit, used by a rider or driver to guide, control, and restrain a horse or other draft animal.",
    "secondary": "Any figurative means of restraint, direction, or sovereign governance exercised over passions, administrative affairs, or public institutions.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Winter's Tale",
        "quote": "Give me the lie to my face, and I will check my horses, and give the **rein** to you."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "He checked his steeds, and reined them back from the precipice, holding a firm **rein** over unruly desire."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "Words are like leaves; and where they most abound, much fruit of sense beneath is rarely found; false eloquence, like the prancing steed, needs the **rein**."
      }
    ]
  },
  "Dashboard — ischi/ischi.md": {
    "primary": "A combining form or prefix derived from Greek ἰσχίον (ischion), signifying the ischium, hip joint, or pelvic region in vertebrate anatomy.",
    "secondary": "In anatomical nomenclature, an affix employed in designating structural complexes, muscles, or nerves uniting the ischium with adjoining regions (such as ischiofemoral or ischiorectal).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The prefix **ischi** designates anatomical connections uniting the hip bone with neighboring spinal and pelvic ligaments."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "In comparative anatomy, the **ischi**-pubic arch exhibits profound modifications reflecting bipedal versus quadrupedal locomotion."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The **ischi**-bulbar musculature differentiates early in embryonic life around the perineal floor."
      }
    ]
  },
  "Dashboard — ischi/ischia.md": {
    "primary": "The plural of ischium; the paired curved bones forming the lower and posterior parts of the pelvic girdle on either side of the pelvis.",
    "secondary": "In vertebrate osteology, the inferoposterior pelvic bones that bear body weight during sitting and provide origin for the hamstring musculature.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The comparative breadth of the **ischia** across anthropoid primates reveals anatomical adaptations to habitual posture."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The tuberosities of the **ischia** bear the entire weight of the trunk in the sitting posture."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "In reptiles and birds, the **ischia** extend backward parallel to the iliac shafts, forming an elongated pelvic frame."
      }
    ]
  },
  "Dashboard — ischi/ischiadic.md": {
    "primary": "Relating to or located in the ischium or hip; anatomical synonym of sciatic.",
    "secondary": "In classical human anatomy and neuroanatomy, designating pelvic ligaments, foramina, vessels, or nerves associated with the ischial framework (e.g., the greater ischiadic notch).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The great **ischiadic** notch gives exit to the piriformis muscle and the superior gluteal vessels."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Compression along the **ischiadic** trunk produces the characteristic radiation of severe neuralgia."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The primitive **ischiadic** artery forms the axial arterial vessel of the embryonic lower limb bud before disappearing."
      }
    ]
  },
  "Dashboard — ischi/ischium.md": {
    "primary": "The lowest and posterior of the three primary bones that fuse to form each half of the vertebrate pelvis (os coxae).",
    "secondary": "In human osteology, the heavy bone composed of a body, superior and inferior rami, and a large rugose tuberosity that supports sitting posture and serves as attachment for posterior thigh muscles.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **ischium** forms the lower and back part of the innominate bone, terminating inferiorly in the great tuberosity."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "Homologies between the **ischium** of terrestrial mammals and the pelvic rudiments of cetaceans reveal ancestral pelvic architecture."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Ossification of the **ischium** proceeds from a primary center appearing during the third month of fetal development."
      }
    ]
  },
  "Dashboard — ischi/ischys.md": {
    "primary": "Bodily strength, physical vigor, or muscular power, derived directly from the classical Greek noun ἰσχύς.",
    "secondary": "In classical Hellenic philosophy, physiology, and gymnastics, the kinetic force and constitutional robust health of the athlete or organism.",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "Socrates distinguished mere physical **ischys**, or brute strength, from virtue guided by philosophical temperance."
      },
      {
        "author": "Richard Claverhouse Jebb",
        "work": "Sophocles: The Plays and Fragments",
        "quote": "The hero's **ischys** faltered when grief overcame his bodily endurance."
      },
      {
        "author": "William Henry Smith",
        "work": "A Dictionary of Greek and Roman Antiquities",
        "quote": "Athletic training in the palaestra sought to cultivate harmonious **ischys** rather than hypertrophied bulk."
      }
    ]
  },
  "Dashboard — ischi/sciatic.md": {
    "primary": "Pertaining to, situated in, or affecting the ischium, hip region, or the sciatic nerve.",
    "secondary": "In gross human anatomy and neurology, designating the largest nerve in the body (the sciatic nerve) arising from the sacral plexus, or describing lancinating neuralgic discomfort along its course.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **sciatic** nerve is the largest nerve in the body, continuing the main trunk of the sacral plexus into the thigh."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unilateral tenderness along the **sciatic** trunk is the hallmark of radicular compression."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "Medical Essays",
        "quote": "The agonizing twinges of **sciatic** neuralgia have tested the patience of physicians and patients for generations."
      }
    ]
  },
  "Dashboard — ischi/sciatica.md": {
    "primary": "Neuralgic pain radiating along the sciatic nerve from the lower back down the buttock, thigh, leg, and foot.",
    "secondary": "In clinical orthopedics and neurology, a symptom complex typically provoked by lumbosacral disc displacement, spinal canal stenosis, or piriformis compression irritating spinal nerve roots.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute **sciatica**, absolute rest in bed with immobilization of the limb offers the most reliable relief."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Stark Munro Letters",
        "quote": "The old squire had been laid up with a fierce bout of **sciatica** that made every step a torment."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "Medical Essays",
        "quote": "He hobbled into the consulting room, bent double by an intractable siege of **sciatica**."
      }
    ]
  },
  "Dashboard — leg/acatalectic.md": {
    "primary": "In classical prosody, having the full and complete number of syllables in the final metrical foot of a poetic verse.",
    "secondary": "In metric analysis and literary criticism, describing verse that strictly adheres to the established rhythmic scheme without terminal syllable omission or truncation.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The sonorous march of the iambic tetrameter **acatalectic** lends stability to the lyric stanza."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "A pure **acatalectic** line maintains the equilibrium of the rhythmic period without requiring pause or syncopation."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Rationale of Verse",
        "quote": "In scanning the trochaic measure, the poet may alternate between catalectic endings and the full **acatalectic** cadence."
      }
    ]
  },
  "Dashboard — leg/alexia.md": {
    "primary": "A neurological condition characterized by the loss of the ability to read or comprehend written language, usually following brain injury or stroke.",
    "secondary": "In behavioral neurology, a focal cortical impairment (often termed word blindness) associated with left occipito-temporal or angular gyrus lesions, frequently distinguishing alexia with agraphia from pure alexia without agraphia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden onset of pure **alexia** without agraphia points reliably to an infarction in the territory of the posterior cerebral artery."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Patients with cortical **alexia** can trace letters tactilely yet fail completely to synthesize visual graphemes into words."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The musician developed an astonishing musical **alexia**, losing the capacity to decipher musical notation while maintaining spoken literacy."
      }
    ]
  },
  "Dashboard — leg/alexithymia.md": {
    "primary": "A psychological condition characterized by the inability to identify, describe, and express one's own emotional states.",
    "secondary": "In psychosomatic medicine and clinical psychology, a trait characterized by difficulty distinguishing between feelings and bodily sensations, an impoverished fantasy life, and an externally oriented cognitive style.",
    "quotes": [
      {
        "author": "Peter Sifneos",
        "work": "Short-Term Psychotherapy and Emotional Crisis",
        "quote": "Patients presenting with profound **alexithymia** tend to describe visceral discomfort rather than verbalizing fear, anger, or despair."
      },
      {
        "author": "Bessel van der Kolk",
        "work": "The Body Keeps the Score",
        "quote": "Trauma frequently induces an acquired **alexithymia**, leaving survivors unable to articulate what their bodies are registering."
      },
      {
        "author": "Antonio Damasio",
        "work": "Descartes' Error",
        "quote": "The cognitive impairment of **alexithymia** highlights the fundamental role of somatic markers in emotional awareness."
      }
    ]
  },
  "Dashboard — leg/analogical.md": {
    "primary": "Based upon, expressing, or utilizing analogy; showing a correspondence or likeness between dissimilar things.",
    "secondary": "In philosophical logic and linguistics, denoting reasoning that infers common attributes between systems from partial resemblances, or describing morphological regularization modeled on parallel paradigms.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "The understanding readily falls into **analogical** reasoning, projecting familiar structural affinities upon obscure phenomena."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "An **analogical** inference provides only probable conjecture until reinforced by direct inductive verification."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The human mind relies upon **analogical** associations to bridge the chasm between known sensations and novel concepts."
      }
    ]
  },
  "Dashboard — leg/apologetic.md": {
    "primary": "Expressing or showing regret, remorse, or an acknowledgment of fault or error.",
    "secondary": "In theology and rhetorical philosophy, designed or delivered as a formal vindication, reasoned defense, or justification of a doctrine, belief, or philosophical position.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "He offered an **apologetic** cough, stepping backward as though fearful of intruding upon the private gathering."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Christian Tradition",
        "quote": "The **apologetic** literature of the period struggled vigorously to reconcile biblical chronology with geological discoveries."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Casaubon wore a faintly **apologetic** air, defending the protracted delay of his theological treatise."
      }
    ]
  },
  "Dashboard — leg/apologia.md": {
    "primary": "A formal, systematic defense or justification of one's opinions, conduct, beliefs, or life.",
    "secondary": "In intellectual and literary autobiography, a published treatise in which an author elucidates and justifies the principles and motives guiding their public career or philosophical evolution.",
    "quotes": [
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "I recognized that nothing less than a comprehensive **apologia** could make clear the internal course of my religious convictions."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Plato's account of Socrates' **apologia** stands as the immortal defense of philosophical enquiry before political dogmatism."
      },
      {
        "author": "George Orwell",
        "work": "Collected Essays",
        "quote": "His latest memoir reads less like history and more like an elaborate **apologia** for past political blunders."
      }
    ]
  },
  "Dashboard — leg/apologist.md": {
    "primary": "A person who defends or offers a formal argumentative justification for a cause, belief, or controversial policy.",
    "secondary": "In historical theology, an early Christian writer (such as Tertullian or Justin Martyr) defending Christian doctrine against pagan or state persecution.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The early Christian **apologist** addressed emperors with persuasive rhetoric, seeking toleration for his persecuted brethren."
      },
      {
        "author": "Thomas Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "No sophisticated **apologist** can excuse the tyrannical excesses of the late administration."
      },
      {
        "author": "Bertrand Russell",
        "work": "Why I Am Not a Christian",
        "quote": "The modern religious **apologist** frequently abandons historical claims to seek shelter in vague metaphysical metaphors."
      }
    ]
  },
  "Dashboard — leg/apologize.md": {
    "primary": "To acknowledge an offense or error and express regret or remorse to an injured party.",
    "secondary": "In formal rhetoric and historical disputation, to present an explanatory defense or reasoned justification for an opinion, stance, or action.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Mr. Collins felt it incumbent upon him to **apologize** for having spoken without a formal introduction."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "He had no reason to **apologize** for an act dictated by common decency and loyalty."
      },
      {
        "author": "Mark Twain",
        "work": "Following the Equator",
        "quote": "It is better to **apologize** promptly than to nurse a grievance that grows tenfold in silence."
      }
    ]
  },
  "Dashboard — leg/apology.md": {
    "primary": "An expression of regret, sorrow, or repentance offered to someone for having caused grievance, injury, or mistake.",
    "secondary": "In classical literature, rhetoric, and law, a formal defense, justification, or vindication of an individual's conduct or philosophical convictions (e.g., Plato's Apology of Socrates).",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "In the **Apology**, Socrates refuses to compromise truth to secure a favorable verdict from the Athenian jury."
      },
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "A polite note of **apology** arrived before noon, begging forgiveness for the unexpected postponement."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "He published an **apology** for his dramatic satire, asserting that his sole aim had been the improvement of public morals."
      }
    ]
  },
  "Dashboard — leg/catalectic.md": {
    "primary": "In classical and modern poetics, having a metrical verse that lacks one or more syllables in the final foot.",
    "secondary": "In prosodic analysis, designating a verse truncation deliberately used to create an abrupt, emphatic cadence at the end of a line or stanza.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Rationale of Verse",
        "quote": "The Raven is composed largely in trochaic octameter, with every stanza ending upon a mournful **catalectic** syllable."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "By employing a **catalectic** line, the poet injects a sharp rhythmic pause into the ballad measure."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The rhythmical effect of the **catalectic** dactyl lies in the sudden arrest of the tripping motion."
      }
    ]
  },
  "Dashboard — leg/catalexis.md": {
    "primary": "The omission or dropping of one or more syllables in the final metrical foot of a line of verse.",
    "secondary": "In metric theory, the structural mechanism of rhythmic truncation that imparts terminal emphasis or marks stanzaic boundaries in poetic meters.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "Manual of English Prosody",
        "quote": "Through calculated **catalexis**, Greek tragic choruses produced an effect of solemn finality at the strophic close."
      },
      {
        "author": "Ezra Pound",
        "work": "The ABC of Reading",
        "quote": "The student of metric must recognize **catalexis** as a conscious rhythmic device rather than a careless metrical lapse."
      },
      {
        "author": "John Addington Symonds",
        "work": "Studies of the Greek Poets",
        "quote": "The dramatic tension in Aeschylus owes much to the abrupt **catalexis** terminating his anapestic systems."
      }
    ]
  },
  "Dashboard — leg/delegation.md": {
    "primary": "The act of assigning, entrusting, or transferring responsibility, power, or authority to another person or body.",
    "secondary": "A designated group of representatives or deputies chosen to represent an organization, nation, or constituency at a conference or assembly.",
    "quotes": [
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The complete **delegation** of legislative power to an executive council is incompatible with republican liberty."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Municipal government requires the prudent **delegation** of administrative functions to local selectmen."
      },
      {
        "author": "Max Weber",
        "work": "Economy and Society",
        "quote": "Bureaucratic authority operates through the systematic **delegation** of official duties governed by established rules."
      }
    ]
  },
  "Dashboard — leg/dialect.md": {
    "primary": "A regional or social variety of a language distinguished by pronunciation, grammar, and vocabulary.",
    "secondary": "In historical and descriptive linguistics, a localized branch of a language system that maintains mutual intelligibility with neighboring sister varieties.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "What we call a language is often little more than a **dialect** that has achieved political and educational dominance."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Pygmalion",
        "quote": "It is impossible for an Englishman to open his mouth without making some other Englishman hate or despise his **dialect**."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "Every local **dialect** preserves archaic grammatical forms that standard national tongues have long discarded."
      }
    ]
  },
  "Dashboard — leg/dialectal.md": {
    "primary": "Pertaining to, characteristic of, or resembling a dialect or regional linguistic variant.",
    "secondary": "In linguistic geography, describing phonological, lexical, or syntactic features that demarcate a specific speech community from the standard literary language.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The preservation of unrounded vowels is a notable **dialectal** feature of northern communities."
      },
      {
        "author": "Otto Jespersen",
        "work": "Growth and Structure of the English Language",
        "quote": "Chaucer carefully utilized **dialectal** idioms in the Reeve's Tale to characterize his northern clerks."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Geographical boundaries between speech communities rarely show sharp cleavages, but rather continuous **dialectal** transitions."
      }
    ]
  },
  "Dashboard — leg/dialectic.md": {
    "primary": "The art or method of examining opinions and arriving at truth through logical discourse, questioning, and exchange of counterarguments.",
    "secondary": "In philosophy (particularly in Plato, Kant, and Hegel), the developmental process whereby contradictions are uncovered, clarified, and resolved through progressive synthesis.",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "For Socrates, philosophical **dialectic** was the highest instrument for liberating the soul from unexamined dogmas."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Transcendental **dialectic** exposes the inevitable illusions that arise when pure reason oversteps empirical boundaries."
      },
      {
        "author": "Georg Wilhelm Friedrich Hegel",
        "work": "The Phenomenology of Spirit",
        "quote": "The movement of the concept follows an internal **dialectic** wherein every determinate reality overcomes its own contradiction."
      }
    ]
  },
  "Dashboard — leg/dialectical.md": {
    "primary": "Relating to or employing dialectic; based upon logical inquiry and debate.",
    "secondary": "In philosophical and social analysis, pertaining to the dynamic evolution of ideas or historical realities driven by internal tensions, contradictions, and transformations.",
    "quotes": [
      {
        "author": "Karl Marx",
        "work": "Das Kapital",
        "quote": "My **dialectical** method is not only different from the Hegelian, but is its direct opposite, grounding development in material reality."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Plato's early dialogues provide vivid examples of **dialectical** inquiry exposing flawed definitions."
      },
      {
        "author": "Jean-Paul Sartre",
        "work": "Critique of Dialectical Reason",
        "quote": "Human praxis constitutes the core of **dialectical** movement within historical structures."
      }
    ]
  },
  "Dashboard — leg/dialectically.md": {
    "primary": "In a manner involving dialectic; through logical discussion, reasoned inquiry, or debate.",
    "secondary": "In philosophical analysis, progressing through the reciprocal interaction, tension, and resolution of conceptual opposites.",
    "quotes": [
      {
        "author": "Friedrich Engels",
        "work": "Anti-Dühring",
        "quote": "To comprehend nature **dialectically** is to grasp phenomena in their interconnected motion, growth, and transformation."
      },
      {
        "author": "Georg Wilhelm Friedrich Hegel",
        "work": "Lectures on the History of Philosophy",
        "quote": "Thought develops **dialectically**, advancing by necessity from abstract immediacy to concrete self-determination."
      },
      {
        "author": "Theodor Adorno",
        "work": "Negative Dialectics",
        "quote": "Critical theory must proceed **dialectically**, refusing to reconcile genuine social contradictions into a false totality."
      }
    ]
  },
  "Dashboard — leg/dialectician.md": {
    "primary": "A thinker skilled in dialectic, logical disputation, or philosophical debate.",
    "secondary": "In the history of philosophy, a philosopher recognized for rigorous cross-examination and systemic analysis of intellectual contradictions (e.g., Zeno, Socrates, Hegel).",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "Socrates was hailed by his companions as the foremost **dialectician** of Athens, unmatched in dismantling pretense."
      },
      {
        "author": "John Stuart Mill",
        "work": "Autobiography",
        "quote": "My father trained me from boyhood to be a thorough **dialectician**, testing every premise before granting a conclusion."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Zeno of Elea was honored by Aristotle as the inventor of dialectic and the first master **dialectician**."
      }
    ]
  },
  "Dashboard — leg/dialectologist.md": {
    "primary": "A linguist who specializes in the study of regional dialects and linguistic variation.",
    "secondary": "In field linguistics and sociolinguistics, a researcher who compiles linguistic atlases, documents isoglosses, and analyzes phonetic differences across speech communities.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Selected Writings in Language, Culture and Personality",
        "quote": "The field **dialectologist** must record oral transcriptions with meticulous acoustic accuracy before local idioms vanish."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "The modern **dialectologist** no longer seeks merely curious provincialisms, but traces living phonetic laws."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "Through systematic interviews and questionnaires, the **dialectologist** maps the geographic contours of linguistic variation."
      }
    ]
  },
  "Dashboard — leg/dialectology.md": {
    "primary": "The scientific branch of linguistics concerned with the study of dialects and dialectal divergence.",
    "secondary": "In sociolinguistic geography, the comparative investigation of geographic, social, and historical variations in pronunciation, vocabulary, and grammar within a language family.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "Linguistic atlases compiled through modern **dialectology** demonstrate that speech boundaries are gradient rather than absolute."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Comparative **dialectology** sheds invaluable light upon the historical processes of language divergence."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The findings of geographical **dialectology** dismantled the older notion of sharply demarcated dialect territories."
      }
    ]
  },
  "Dashboard — leg/dialog.md": {
    "primary": "A conversation between two or more individuals; a conversational interchange of perspectives or ideas.",
    "secondary": "In literary composition and philosophy, a work presented in dramatic conversational form to explore complex ethical or intellectual topics; in computing, an interactive prompt window.",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "The philosophical **dialog** allowed Socrates to interrogate abstract doctrines through lively dramatic exchange."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Genuine **dialog** demands that both speakers abandon dogmatic postures to meet in common intellectual pursuit."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Dramatic Opinions and Essays",
        "quote": "In serious theater, realistic **dialog** must convey character and moral conflict without degenerating into mere lecture."
      }
    ]
  },
  "Dashboard — leg/dyslectic.md": {
    "primary": "Pertaining to, experiencing, or characteristic of dyslexia; an alternate orthography for dyslexic.",
    "secondary": "In neuropsychology and educational diagnostics, describing individuals or cognitive processing deficits marked by difficulty deciphering printed orthography.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "The **dyslectic** child often possesses remarkable spatial intelligence despite profound struggles with printed text."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Careful neurological assessment reveals that **dyslectic** difficulties can arise from either visual-spatial or auditory-phonetic deficits."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The **dyslectic** reader hesitates before the visual symbol, struggling to link the visible sign with its internal acoustic image."
      }
    ]
  },
  "Dashboard — leg/dyslexia.md": {
    "primary": "A learning condition characterized by difficulty in reading, spelling, and recognizing words despite normal intelligence and sensory acuity.",
    "secondary": "In cognitive neurology and developmental psychology, a neurodevelopmental disorder involving atypical phonological processing and visual-orthographic decoding mechanisms in the cerebral cortex.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "His lifelong struggle with developmental **dyslexia** had never hindered his extraordinary mechanical and artistic talents."
      },
      {
        "author": "Alexander Luria",
        "work": "Higher Cortical Functions in Man",
        "quote": "Acquired **dyslexia** following parieto-occipital trauma manifests as a breakdown in the optical synthesis of word shapes."
      },
      {
        "author": "Norman Geschwind",
        "work": "Selected Papers on Language and the Brain",
        "quote": "Cerebral asymmetry and atypical cortical architecture provide compelling anatomical correlates for developmental **dyslexia**."
      }
    ]
  },
  "Dashboard — leg/dyslexic.md": {
    "primary": "Affected with or relating to dyslexia; a person who experiences dyslexia.",
    "secondary": "In special education and cognitive science, designating specialized pedagogies or cognitive profiles associated with reading and phonological processing variations.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Musicophilia",
        "quote": "Several **dyslexic** musicians whom I examined showed an astonishing ability to memorize intricate scores purely by ear."
      },
      {
        "author": "Norman Geschwind",
        "work": "Cerebral Lateralization",
        "quote": "A significant proportion of **dyslexic** individuals exhibit left-handedness and pronounced artistic or mathematical aptitude."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "The **dyslexic** patient required specific phonetic retraining to reconnect the visual symbol with spoken phonemes."
      }
    ]
  },
  "Dashboard — leg/dyslogia.md": {
    "primary": "Difficulty or impairment in expressing thoughts through articulate speech due to mental disturbance or central nervous impairment.",
    "secondary": "In clinical psychiatry, a speech pathology characterized by conceptual fragmentation, incoherence, or illogical syntax arising from cognitive deterioration or psychosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The profound **dyslogia** observed in advanced cerebral degeneration reflects widespread destruction of association pathways."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "Severe cases of dementia praecox frequently display marked **dyslogia**, wherein ideas lose all logical cohesion."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "The symptom of **dyslogia** must be carefully distinguished from mechanical dysarthria of the peripheral musculature."
      }
    ]
  },
  "Dashboard — leg/dyslogism.md": {
    "primary": "A word, phrase, or appellation that carries a disparaging or derogatory connotation; a dysphemism.",
    "secondary": "In political rhetoric and semantic analysis, an emotionally loaded term applied to discredit a policy, group, or person without rational argument (contrasted with eulogism).",
    "quotes": [
      {
        "author": "Jeremy Bentham",
        "work": "The Book of Fallacies",
        "quote": "The partisan relies upon a well-chosen **dyslogism** to cast odium upon measures he cannot refute by honest argument."
      },
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Modern political jargon abounds in **dyslogism**, using defamatory labels to stifle independent thought."
      },
      {
        "author": "William Hazlitt",
        "work": "Table-Talk",
        "quote": "A stinging **dyslogism** hurled from the hustings will often turn an election when reasoned eloquence fails."
      }
    ]
  },
  "Dashboard — leg/ethnolect.md": {
    "primary": "A variety of a language spoken by a specific ethnic or cultural subgroup within a larger linguistic community.",
    "secondary": "In sociolinguistics, a distinctive linguistic code carrying phonetic, syntactic, and lexical markers that express cultural identity and communal solidarity.",
    "quotes": [
      {
        "author": "William Labov",
        "work": "Sociolinguistic Patterns",
        "quote": "An **ethnolect** serves not merely as a communicative tool, but as a primary badge of community solidarity and identity."
      },
      {
        "author": "Peter Trudgill",
        "work": "Sociolinguistics: An Introduction to Language and Society",
        "quote": "Features of an **ethnolect** frequently migrate into the wider vernacular of multicultural urban centers."
      },
      {
        "author": "John McWhorter",
        "work": "The Power of Babel",
        "quote": "Every vibrant **ethnolect** possesses an internal grammatical regularity as intricate and rigorous as any national standard."
      }
    ]
  },
  "Dashboard — leg/heterologic.md": {
    "primary": "Deviating from normal or expected logical, biological, or structural relations; exhibiting heterology.",
    "secondary": "In anatomical pathology, characterizing abnormal tissues or neoplasms composed of elements not native to the anatomical site; in semantics, self-refuting or not applying to itself.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A **heterologic** neoplasm arises when cellular proliferation deviates entirely from the architectural type of the parent organ."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The presence of **heterologic** elements such as bone or cartilage within soft tissue tumors demands thorough microscopic study."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "A word is called **heterologic** if it does not describe itself, generating acute semantic antinomies."
      }
    ]
  },
  "Dashboard — leg/heterological.md": {
    "primary": "Of or pertaining to heterology; not describing itself (applied to adjectives); abnormal in structure.",
    "secondary": "In philosophical logic and semantic theory, designating words that do not possess the property they denote (e.g. 'monosyllabic' is not monosyllabic), forming the crux of the Grelling-Nelson antinomy.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "The Grelling paradox asks whether the word **heterological** is itself **heterological**, generating a direct contradiction."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "The Ways of Paradox",
        "quote": "If 'long' is **heterological** because it is short, what must we say of the word '**heterological**' itself?"
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "We designate these morbid growths as **heterological** because their structure violates the histological norms of the host tissue."
      }
    ]
  },
  "Dashboard — leg/homologic.md": {
    "primary": "Displaying homology; corresponding in anatomical structure, origin, or logical category.",
    "secondary": "In evolutionary morphology, describing morphological parts sharing a common phylogenetic ancestor despite divergence in function or external appearance.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "The wing of a bat and the paddle of a porpoise present clear **homologic** correspondence to the human arm."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The existence of **homologic** parts across disparate mammalian classes points indisputably to descent from a common ancestor."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "A thorough **homologic** examination of primate cranial bones demonstrates precise morphological continuity."
      }
    ]
  },
  "Dashboard — leg/homological.md": {
    "primary": "Pertaining to homology; exhibiting fundamental correspondence in structural plan, evolutionary descent, or algebraic topology.",
    "secondary": "In comparative vertebrate biology, describing organs derived from the same embryonic and ancestral structures; in algebraic topology, pertaining to homology groups and boundaries.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The **homological** relations of homologous organs remain traceable even when divergent functions cause drastic modifications."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals",
        "quote": "We establish **homological** identity by tracing developmental origin and anatomical connections rather than superficial function."
      },
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "The introduction of **homological** cycles into topology provided the decisive tool for classifying higher-dimensional manifolds."
      }
    ]
  },
  "Dashboard — leg/hypercatalectic.md": {
    "primary": "In classical verse, having one or more syllables beyond the normal metrical measure at the end of a line.",
    "secondary": "In poetic prosody, designating an overflowing or redundant syllable that extends the terminal foot to impart an expansive, cascading rhythm.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "By adding an extra syllable to create a **hypercatalectic** line, the poet softens the conclusion of the rhyming couplet."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Rationale of Verse",
        "quote": "The verse is strictly trochaic, though occasional **hypercatalectic** endings give a pleasant variety to the stanza."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "A **hypercatalectic** redundancy at the hemistich breaks the monotony of the regular Alexandrine."
      }
    ]
  },
  "Dashboard — leg/leg.md": {
    "primary": "One of the lower limbs on which an animal or biped walks, runs, and stands; in humans, the lower extremity from the thigh or knee to the ankle.",
    "secondary": "A vertical supporting structure or member of a piece of furniture; a distinct portion or stage of a race, course, flight, or travel journey.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "As You Like It",
        "quote": "I would I were invisible, to catch the strong fellow by the **leg**."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "He had a great iron upon his **leg**, and he limped along the marshes through the mist."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Captain Ahab stood before them with an ivory **leg** fashioned from the polished jawbone of a sperm whale."
      }
    ]
  },
  "Dashboard — leg/legal.md": {
    "primary": "Conforming to, permitted by, or established by statutory or common law; lawful.",
    "secondary": "Relating to the jurisprudence system, judicial courts, or the profession of law, as distinguished from moral or administrative realms.",
    "quotes": [
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The interpretation of laws is the proper and peculiar province of the courts; a **legal** judgment must be governed by statutory precedent."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Scarcely any political question arises in the United States that is not resolved sooner or later into a **legal** question."
      },
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "Municipal law is a rule of civil conduct prescribed by supreme power, commanding what is right and prohibiting what is **legal** wrong."
      }
    ]
  },
  "Dashboard — leg/legalise.md": {
    "primary": "To make lawful or officially sanction by legislative enactment; British English spelling of legalize.",
    "secondary": "In political jurisprudence, to repeal statutory prohibitions on an activity, bringing it under civil authorization and regulatory oversight.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "To **legalise** combinations among workingmen was a necessary step toward establishing true equality of contract."
      },
      {
        "author": "Jeremy Bentham",
        "work": "The Theory of Legislation",
        "quote": "The legislator must decide whether to penalize a practice or **legalise** and regulate its operation for the public good."
      },
      {
        "author": "Thomas Macaulay",
        "work": "History of England",
        "quote": "Parliament hesitated long before passing the enactments that would **legalise** dissenters' places of worship."
      }
    ]
  },
  "Dashboard — leg/legalism.md": {
    "primary": "Strict, literal, or pedantic adherence to statutory regulations, legal forms, or religious codes.",
    "secondary": "In theological ethics and jurisprudence, an ideological stance prioritizing external procedural conformity over moral intention, mercy, or equity.",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "Rigid ethical **legalism** characterized Puritan communities, where moral conduct was scrutinized with judicial precision."
      },
      {
        "author": "Reinhold Niebuhr",
        "work": "Moral Man and Immoral Society",
        "quote": "The moralist who falls into sterile **legalism** mistakes rigid codification for genuine social justice."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Spiritual regeneration frequently rebels against formal **legalism**, seeking a direct and vital relationship with the divine."
      }
    ]
  },
  "Dashboard — leg/legality.md": {
    "primary": "The state, condition, or quality of being in accordance with the law; lawfulness.",
    "secondary": "In constitutional theory and jurisprudence, the foundational doctrine requiring that all executive power and state action derive from validly established statutory norms.",
    "quotes": [
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The judicial authority must determine the **legality** of legislative acts against the supreme benchmark of the Constitution."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The American respect for the **legality** of established statutes moderates the sudden impulses of democratic assemblies."
      },
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "The fundamental **legality** of our common law resides in its immemorial usage and parliamentary sanction."
      }
    ]
  },
  "Dashboard — leg/legalize.md": {
    "primary": "To make legal, authorized, or lawful; to remove statutory prohibitions against an action.",
    "secondary": "To give formal judicial sanction or certified validity to a document, decree, or institutional status.",
    "quotes": [
      {
        "author": "Abraham Lincoln",
        "work": "Collected Works",
        "quote": "No act of executive power can **legalize** an arbitrary infringement of constitutional rights in peaceful states."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "The state should hesitate to criminalize conduct that harms no one, and instead **legalize** voluntary civic arrangements."
      },
      {
        "author": "Woodrow Wilson",
        "work": "The State: Elements of Historical and Practical Politics",
        "quote": "Societies continually revise their statutes to **legalize** practices that evolving public opinion has come to approve."
      }
    ]
  },
  "Dashboard — leg/legally.md": {
    "primary": "In a manner according to, permitted by, or authorized by law; lawfully.",
    "secondary": "From a formal legal perspective or juristic standard, as distinguished from ethical, moral, or practical considerations.",
    "quotes": [
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "An individual cannot be **legally** bound by an agreement procured through duress or deceit."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "He was **legally** ruined by forty years of protracted Chancery proceedings before any decree could be rendered."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "A treaty constitutes the supreme law of the land, **legally** binding upon all state courts and legislatures."
      }
    ]
  },
  "Dashboard — leg/legate.md": {
    "primary": "An official emissary, deputy, or ambassador, especially one representing the Pope or Roman Curia.",
    "secondary": "In ancient Roman history, a deputy magistrate or military commander (*legatus*) directing a legion or administering an imperial province on behalf of the central authority.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The imperial **legate** commanded the legions of the Rhine with absolute authority delegated directly by the Caesar."
      },
      {
        "author": "Niccolò Machiavelli",
        "work": "The Prince",
        "quote": "The Pope dispatched his personal **legate** to negotiate a truce between the warring republics of northern Italy."
      },
      {
        "author": "William Shakespeare",
        "work": "King John",
        "quote": "Pandulph, of fair Milan cardinal, And from Pope Innocent the **legate** here, do I demand thy answer."
      }
    ]
  },
  "Dashboard — leg/legateship.md": {
    "primary": "The office, dignity, authority, or term of service of a legate.",
    "secondary": "In Roman administrative history and canon law, the jurisdiction and plenary powers exercised by a diplomatic representative or papal nuncio.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "During his tenure of the Syrian **legateship**, he restored discipline to the eastern frontier."
      },
      {
        "author": "David Hume",
        "work": "The History of England",
        "quote": "Cardinal Wolsey obtained the perpetual **legateship** from Rome, uniting in his person supreme spiritual and temporal influence."
      },
      {
        "author": "Thomas Macaulay",
        "work": "The History of England",
        "quote": "The powers annexed to the papal **legateship** were viewed with deep jealousy by the domestic bishops."
      }
    ]
  },
  "Dashboard — leg/legation.md": {
    "primary": "A diplomatic mission, embassy, or delegation sent to represent a state or sovereign abroad; the official residence and offices of such a mission.",
    "secondary": "The dispatching or sending forth of an official envoy; the collective body of diplomatic ministers and attachés assigned to a foreign station.",
    "quotes": [
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "During the Civil War, the American **legation** in London became the storm center of transatlantic diplomacy."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The staff of the foreign **legation** observed republican political customs with keen curiosity."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "Urgent dispatches reached the British **legation** warning of immediate troop mobilizations along the border."
      }
    ]
  },
  "Dashboard — leg/leger.md": {
    "primary": "Nimble, light, or quick (archaic, from French léger); also surviving in sleight of hand (legerdemain) and ledger lines in musical notation.",
    "secondary": "In freshwater angling, designating stationary tackle with a heavy sliding lead weight (*leger*) that holds bait on the bottom of a current; historically, a fixed book or register.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "By nimbleness and **leger** dexterity of wit, the sophist can dazzle an uncritical assembly."
      },
      {
        "author": "Izaak Walton",
        "work": "The Compleat Angler",
        "quote": "For bottom fishing in a swift stream, the **leger** tackle keeps the worm securely anchored amidst the gravel."
      },
      {
        "author": "Walter Scott",
        "work": "The Antiquary",
        "quote": "The old antiquary consulted his ancient **leger** of monastic accounts to verify the disputed tithe."
      }
    ]
  },
  "Dashboard — leg/leggy.md": {
    "primary": "Having noticeably long, slender, or awkwardly proportioned legs.",
    "secondary": "In horticulture and arboriculture, having abnormally tall, weak, spindly stems with sparse foliage, typical of plants starved of adequate sunlight.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "A **leggy** colt trotted beside the fence, its spindly limbs trembling with nervous energy."
      },
      {
        "author": "D. H. Lawrence",
        "work": "Sons and Lovers",
        "quote": "The seedlings in the shaded windowsill had grown tall and **leggy**, reaching pathetically toward the daylight."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "She watched the **leggy** foal gambol across the spring meadow on limbs that seemed too long for its body."
      }
    ]
  },
  "Dashboard — leg/legibility.md": {
    "primary": "The quality or condition of being easily read, deciphered, or understood, especially regarding handwriting or typography.",
    "secondary": "In graphic design and typography, the distinctiveness and clarity of individual letterforms that enable immediate visual identification by the reader.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Murders in the Rue Morgue",
        "quote": "The minute perfection and pristine **legibility** of the script suggested a professional copyist's hand."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The architectural inscription loses none of its dignity when carved with bold, monumental **legibility**."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The rapid recognition of words depends upon the visual **legibility** of letter contours stored in perceptual memory."
      }
    ]
  },
  "Dashboard — leg/legible.md": {
    "primary": "Capable of being easily read, deciphered, or distinguished (said of text or handwriting).",
    "secondary": "Plainly visible, evident, or unmistakable in meaning or significance; transparently expressed.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "The old tombstone bore an epitaph still partially **legible** beneath the creeping moss."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Upon his weathered countenance, decades of maritime storm and peril had carved a **legible** history."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of Four",
        "quote": "The handwriting on the envelope was firm, **legible**, and indicative of a person of precise habits."
      }
    ]
  },
  "Dashboard — leg/leging.md": {
    "primary": "A protective outer covering for the lower extremity, typically extending from the foot or ankle to the knee or thigh.",
    "secondary": "In historical costume and occupational gear, an article of stout cloth, buckskin, or leather (such as a gaiter, legging, or greave) worn against cold, briars, and rugged terrain.",
    "quotes": [
      {
        "author": "Washington Irving",
        "work": "A History of New York",
        "quote": "He wore a stout leather **leging** to shield his shins against the thorny briars of the woodland path."
      },
      {
        "author": "James Fenimore Cooper",
        "work": "The Last of the Mohicans",
        "quote": "The hunter laced his buckskin **leging** securely above the moccasin before venturing into the dense thicket."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "A coarse woollen **leging** served as sufficient armor against the winter snowdrifts around the pond."
      }
    ]
  },
  "Dashboard — leg/legomenon.md": {
    "primary": "A word or phrase that occurs in a text or literary corpus (chiefly known in the compound *hapax legomenon*, a word recorded only once).",
    "secondary": "In classical philology, biblical studies, and corpus linguistics, a lexical item analyzed according to its frequency and distribution across ancient manuscripts or authors.",
    "quotes": [
      {
        "author": "John Addington Symonds",
        "work": "Studies of the Greek Poets",
        "quote": "The Homeric text presents many a disputed **legomenon** whose precise archaic sense remains a riddle to modern scholars."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "The textual critic examines each rare **legomenon** to ascertain the authenticity of the tragic fragments."
      },
      {
        "author": "C. S. Lewis",
        "work": "Selected Literary Essays",
        "quote": "A solitary **legomenon** in an Anglo-Saxon poem often bears the entire weight of an obsolete cultural concept."
      }
    ]
  },
  "Dashboard — leg/lexeme.md": {
    "primary": "A fundamental unit of the lexicon of a language, representing an abstract vocabulary word that encompasses all its grammatical inflectional forms.",
    "secondary": "In structural morphology and semantic theory, the minimal distinctive lexical entry stored in the mental lexicon that carries conceptual signification.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The linguist isolates each fundamental **lexeme** to study how morphological affixes alter its functional role."
      },
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings",
        "quote": "The semantic identity of a **lexeme** persists throughout its various syntactical and morphological transformations."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Within the lexical system, every **lexeme** derives its conceptual value through opposition to other vocabulary items."
      }
    ]
  },
  "Dashboard — leg/lexical.md": {
    "primary": "Relating to the words, vocabulary, or lexicon of a language, as contrasted with its grammatical syntax.",
    "secondary": "In lexicography and linguistics, pertaining to dictionary entries, morpheme inventories, or the lexical semantic structure of speech.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "A language consists of both grammatical rules and a vast **lexical** store of arbitrary form-meaning pairings."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "The rapid expansion of scientific discovery demands an enormous increase in **lexical** resources."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Grammatical categories often emerge historically from the petrifaction of formerly independent **lexical** roots."
      }
    ]
  },
  "Dashboard — leg/lexicalise.md": {
    "primary": "To incorporate a concept, compound, or phrase into the permanent lexicon of a language as a recognized single word; British English spelling of lexicalize.",
    "secondary": "In historical and cognitive linguistics, the evolutionary process whereby syntactic collocations petrify into unitary, dictionary-codified vocabulary items.",
    "quotes": [
      {
        "author": "Otto Jespersen",
        "work": "Growth and Structure of the English Language",
        "quote": "Languages tend to **lexicalise** frequent compound phrases into unified words with specialized meanings."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Over generations, living speech communities **lexicalise** novel cultural concepts to economize communicative effort."
      },
      {
        "author": "Edward Sapir",
        "work": "Selected Writings in Language, Culture and Personality",
        "quote": "The urge to **lexicalise** complex perceptual experiences is universal across diverse human cultures."
      }
    ]
  },
  "Dashboard — leg/lexicalize.md": {
    "primary": "To make into a single word; to express an idea or syntactic sequence as an established lexical entry in a language.",
    "secondary": "In psycholinguistics and morphology, the process of assigning a dedicated lexical form to an experiential or conceptual category in the lexicon.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "When speakers **lexicalize** a technical innovation, the new word quickly acquires its own derivative morphological paradigm."
      },
      {
        "author": "Roman Jakobson",
        "work": "Six Lectures on Sound and Meaning",
        "quote": "The cognitive capacity to **lexicalize** subtle nuances of feeling distinguishes mature linguistic systems."
      },
      {
        "author": "John McWhorter",
        "work": "The Power of Babel",
        "quote": "Every language chooses to **lexicalize** certain everyday actions that other languages express through cumbersome phrases."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = ''' + json.dumps(BATCH2_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Body Part 4 Batch 2 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 2 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_body4_batch2.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_body4_batch2.mjs with {len(BATCH2_DATA)} entries.")
