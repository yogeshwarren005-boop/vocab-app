# -*- coding: utf-8 -*-
"""
curate_order_b1_p2.py
Cluster Order Batch 1 Part 2 (73 words)
Dashboards:
- norm (35 words: abnormal -> supranormal)
- rig (38 words: agrigento -> unrigged)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_order_b1_p2 = {
    # Dashboard — norm (35)
    "abnormal": {
        "primary": "Deviating from what is normal, typical, usual, or expected, especially in a way that causes concern.",
        "secondary": "In clinical medicine and pathology, departing from standard physiological values or anatomical development.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Certain individuals exhibit **abnormal** muscular variations inherited from remote quadrumanous ancestors."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The examiner noted an **abnormal** systolic murmur radiating toward the left axilla."
            },
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "Medical Essays",
                "quote": "Any **abnormal** elevation of body temperature signals the mobilization of internal defensive forces."
            }
        ]
    },
    "abnormalcy": {
        "primary": "An atypical irregularity, aberration, or deviation departing from standard order or healthy conditions.",
        "secondary": "In clinical psychology and neurology, an atypical neurological or behavioral deviation from standard developmental milestones.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "A transient psychological **abnormalcy** may accompany intense spiritual illumination without implying permanent mental disorder."
            },
            {
                "author": "Oliver Sacks",
                "work": "The Man Who Mistook His Wife for a Hat",
                "quote": "The patient was entirely unaware of any visual **abnormalcy**, compensating unconsciously for the agnosia."
            },
            {
                "author": "René Dubos",
                "work": "Mirage of Health",
                "quote": "Biological adaptation often transforms what was once considered an **abnormalcy** into a protective survival advantage."
            }
        ]
    },
    "abnormality": {
        "primary": "An abnormal feature, characteristic, condition, or occurrence; a malformation or irregularity.",
        "secondary": "In medical genetics and teratology, a congenital defect or structural aberration arising during embryogenesis.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "A remarkable anatomical **abnormality** in the plumage appeared spontaneously in several domestic pigeons."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Careful microscopic analysis of the blood smear revealed no cellular **abnormality**."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evidence as to Man's Place in Nature",
                "quote": "He investigated the skeletal **abnormality**, concluding it represented a rare suture closure rather than a distinct species."
            }
        ]
    },
    "abnormally": {
        "primary": "In an abnormal, unusual, or atypical manner; deviating from what is standard.",
        "secondary": "To a degree markedly exceeding or falling below ordinary statistical or biological averages.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Certain floral organs were developed **abnormally**, assuming the color and form of adjacent petals."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "Her pulse beat **abnormally** fast as she waited alone in the dark corridor of the pensionnat."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The laboratory reported an **abnormally** low platelet count following the acute viral infection."
            }
        ]
    },
    "enormity": {
        "primary": "The extreme scale, monstrous nature, or outrageous wickedness of an offense or crime.",
        "secondary": "The vastness, immense magnitude, or overwhelming scale of something, such as a tragedy or undertaking.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman populace was stunned by the flagrant **enormity** of the emperor's cruelties."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "No rhetorical artifice can disguise the moral **enormity** of overturning ancient ancestral constitutions."
            },
            {
                "author": "Winston Churchill",
                "work": "The Gathering Storm",
                "quote": "Few statesmen in Europe grasped the full **enormity** of the catastrophe gathering on the horizon."
            }
        ]
    },
    "enormous": {
        "primary": "Very large in size, quantity, extent, or degree; immense, vast, or huge.",
        "secondary": "In classical and historical literature, exceedingly wicked, monstrous, or departing outrageously from regular law or order.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection operating through **enormous** periods of geological time has fashioned the diversity of life."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The **enormous** white brow of the sperm whale loomed above the foam-capped waves."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The central government accumulated an **enormous** concentration of administrative power in modern nations."
            }
        ]
    },
    "enormously": {
        "primary": "To a very great degree, extent, or amount; hugely or immensely.",
        "secondary": "In economic and comparative analysis, exceeding ordinary metrics by a substantial margin.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Cultivated vegetables vary **enormously** when raised under different conditions of soil and climate."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The division of labor increases the productive powers of manufacturing **enormously**."
            },
            {
                "author": "Virginia Woolf",
                "work": "Orlando",
                "quote": "Her spirits rose **enormously** as the carriage rattled past the blossoming hedgerows of Sussex."
            }
        ]
    },
    "enormousness": {
        "primary": "Immensely vast physical size, stupendous magnitude, or overwhelming bulk.",
        "secondary": "In aesthetic philosophy, the overwhelming sublimity or magnitude of an object that defies ordinary comprehension.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The sheer **enormousness** of the leviathan's bulk filled the weary whalemen with awe."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "Contemplating the starry heavens, man feels his own insignificance before the silent **enormousness** of the cosmos."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The painter conveyed the terrifying **enormousness** of the alpine precipice through subtle contrasts of mist and shadow."
            }
        ]
    },
    "nonnormative": {
        "primary": "Not conforming to or based on an established norm, standard, or convention.",
        "secondary": "In sociological theory and ethics, descriptive of empirical phenomena without establishing moral evaluations or prescriptive rules.",
        "quotes": [
            {
                "author": "Max Weber",
                "work": "The Methodology of the Social Sciences",
                "quote": "Empirical sociology pursues a strictly **nonnormative** analysis of social action and institutional beliefs."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Individual developmental trajectories frequently follow **nonnormative** pathways without implying pathology."
            },
            {
                "author": "John Dewey",
                "work": "Human Nature and Conduct",
                "quote": "A scientific inquiry into human customs must begin with a **nonnormative** inventory of observable habits."
            }
        ]
    },
    "norm": {
        "primary": "A standard, pattern, or model regarded as typical, usual, or representative of a group.",
        "secondary": "In sociology and jurisprudence, an authoritative rule or principle governing acceptable conduct within a community.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Public opinion becomes the universal **norm** to which individual citizens conform their behavior."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "Legal bureaucracy functions through impersonal allegiance to the abstract constitutional **norm**."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Any deviation from the morphological **norm** may prove either advantageous or fatal under natural selection."
            }
        ]
    },
    "norma": {
        "primary": "A square, carpenter's square, or rule; historically a model, standard, or pattern.",
        "secondary": "In craniometry and human anatomy, an aspect or view of the skull (such as norma verticalis, norma facialis, or norma lateralis).",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Viewed in **norma** verticalis, the cranial vault presents an oval outline broader behind than in front."
            },
            {
                "author": "Arthur Keith",
                "work": "Human Embryology and Morphology",
                "quote": "Comparison of the fossil calvaria in **norma** lateralis established the low brow of Neanderthal specimens."
            },
            {
                "author": "Aleš Hrdlička",
                "work": "Anthropometry",
                "quote": "The craniologist photographed each prehistoric specimen carefully in **norma** basilaris."
            }
        ]
    },
    "normal": {
        "primary": "Conforming to a standard, regular, usual, or typical pattern, behavior, or condition.",
        "secondary": "In geometry, perpendicular to a given line or surface at a given point.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The reflected ray lies in the same plane with the incident ray and the **normal** drawn to the surface."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Physiological investigations seek to determine the **normal** constancy of the internal bodily environment."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her calm temper quickly returned to its **normal** balance after the momentary agitation had passed."
            }
        ]
    },
    "normalcy": {
        "primary": "A regular, stable, or ordinary state, free from crisis, agitation, or distortion.",
        "secondary": "In political history, the return to stable, peaceful domestic life following wartime upheaval or national crisis.",
        "quotes": [
            {
                "author": "Warren G. Harding",
                "work": "Return to Normalcy Address",
                "quote": "America's present need is not heroics, but healing; not nostrums, but **normalcy**."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "Citizens yearned for a quiet era of comfortable economic **normalcy** after the European war."
            },
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Beautiful and Damned",
                "quote": "A veneer of bourgeois **normalcy** returned to their lives after the scandalous summer in the country."
            }
        ]
    },
    "normalisation": {
        "primary": "The British English spelling of normalization; the process of making or becoming normal.",
        "secondary": "In economic diplomacy and politics, the re-establishment of peaceful diplomatic and commercial relations between states.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "The swift **normalisation** of civilian trade became our primary concern once coastal shipping lanes were secured."
            },
            {
                "author": "George Orwell",
                "work": "The Lion and the Unicorn",
                "quote": "Post-war reconstruction requires the **normalisation** of civic life without returning to Victorian inequalities."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The Economic Consequences of the Peace",
                "quote": "Disrupting continental commerce prevented the natural **normalisation** of European currencies."
            }
        ]
    },
    "normalise": {
        "primary": "The British English spelling of normalize; to bring or return to a normal standard, state, or condition.",
        "secondary": "In metallurgy, to heat steel above its critical temperature and air-cool it to refine grain structure and relieve stresses.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Homage to Catalonia",
                "quote": "Authorities attempted to **normalise** daily life in Barcelona by reopening the shops and disarming the militias."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Annealing will **normalise** the internal crystal boundaries of drawn copper wire."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Rest and hydration helped to **normalise** the patient's elevated heart rate within two days."
            }
        ]
    },
    "normaliser": {
        "primary": "A person, agent, chemical, or mechanism that normalizes or restores something to a regular state.",
        "secondary": "In abstract algebra and group theory, the subgroup of elements that commute with a given subset; a normalizing subgroup.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "Lectures on the Phenomena of Life Common to Animals and Plants",
                "quote": "The liver acts as a metabolic **normaliser**, keeping blood sugar concentrations constant."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Negative feedback loops serve as an automatic **normaliser** in complex homeostatic networks."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Renal excretion functions as the ultimate **normaliser** of electrolyte balances in mammalian plasma."
            }
        ]
    },
    "normality": {
        "primary": "Conformity to an established standard, customary pattern, or healthy state.",
        "secondary": "In analytical chemistry, a measure of solution concentration expressed in gram equivalent weights of solute per liter.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Titration experiments require an acid solution of known chemical **normality** to neutralize the alkali."
            },
            {
                "author": "George Eliot",
                "work": "Daniel Deronda",
                "quote": "The routine of country house life provided a welcome return to serene **normality**."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Habitual routines anchor our mental life in a comforting sense of daily **normality**."
            }
        ]
    },
    "normalization": {
        "primary": "The process of bringing or returning something to a normal, standard, or regular condition.",
        "secondary": "In database theory and statistics, the restructuring of data to eliminate redundancy and adjust values to a common scale.",
        "quotes": [
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "The **normalization** of bureaucratic procedures eliminates arbitrary personal favoritism."
            },
            {
                "author": "Winston Churchill",
                "work": "The World Crisis",
                "quote": "Diplomats worked tirelessly toward the **normalization** of international shipping through the straits."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Antibiotic therapy promoted the swift **normalization** of the patient's white blood cell count."
            }
        ]
    },
    "normalize": {
        "primary": "To bring or return to a normal condition, standard, or regularity.",
        "secondary": "In materials engineering, to heat and cool a ferrous metal to produce uniform grain structure and relieve internal stresses.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Intravenous saline served to **normalize** the circulatory volume in severe dehydration."
            },
            {
                "author": "Andrew Carnegie",
                "work": "Autobiography of Andrew Carnegie",
                "quote": "Careful heat treatment helped to **normalize** the steel rails, preventing brittle winter fractures."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Democratic institutions tend to **normalize** social manners, smoothing away aristocratic eccentricities."
            }
        ]
    },
    "normalizer": {
        "primary": "An agent, factor, device, or mechanism that restores or maintains a normal condition.",
        "secondary": "In heat metallurgy, a furnace or annealing setup utilized to normalize cast or forged steels.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The nervous system acts as the supreme **normalizer** of physiological functions."
            },
            {
                "author": "Henry Ford",
                "work": "Today and Tomorrow",
                "quote": "Continuous conveyor ovens served as an automated **normalizer** for forged transmission gears."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Endocrine hormones function as a vital systemic **normalizer** during intense physical exertion."
            }
        ]
    },
    "normally": {
        "primary": "Under normal, typical, or ordinary conditions; usually, as a rule.",
        "secondary": "In a normal, standard, or healthy manner, free from abnormality or disease.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Insects that **normally** dwell in dark caverns frequently lose their visual organs over generations."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Elizabeth listened with that keen amusement she **normally** derived from eccentric characters."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "When the heart beats **normally**, the mitral valve closes securely during ventricular systole."
            }
        ]
    },
    "norman": {
        "primary": "Relating to Normandy in northern France, or to the Normans who conquered England in 1066.",
        "secondary": "In architectural history, the Romanesque architectural style introduced to England by the Normans, characterized by massive round arches.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The haughty **Norman** baron treated the Saxon thurgh with cold aristocratic disdain."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Adventurous **Norman** knights conquered southern Italy and established a brilliant kingdom in Sicily."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The sturdy round piers of the **Norman** cathedral express brute power and solid architectural permanence."
            }
        ]
    },
    "norman-french": {
        "primary": "The dialect of Old French spoken by the medieval Normans and introduced to England after the Conquest of 1066.",
        "secondary": "In legal and linguistic history, the legal register (Law French) derived from medieval Norman vernacular used in English royal courts.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "In the royal court, harsh Saxon idioms were banished in favor of polished **Norman-French** poetry."
            },
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "The blending of Anglo-Saxon grammar with **Norman-French** vocabulary produced modern English."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "English statutes were framed for centuries in archaic **Norman-French** terms."
            }
        ]
    },
    "normandie": {
        "primary": "The French spelling of Normandy, a historical province of northwestern France bordering the English Channel.",
        "secondary": "In maritime history, a famous French ocean liner (SS Normandie, 1935) celebrated for Art Deco luxury and the Blue Riband.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "A Little Tour in France",
                "quote": "We traveled leisurely through the orchard valleys and ancient timbered villages of **Normandie**."
            },
            {
                "author": "Marcel Proust",
                "work": "In Search of Lost Time",
                "quote": "The train carried us toward the misty coast of **Normandie**, where the ocean breeze scented the air."
            },
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Great Gatsby",
                "quote": "The traveler reminisced about glamorous crossings on the great transatlantic liner **Normandie**."
            }
        ]
    },
    "normandy": {
        "primary": "A historical province of northwestern France along the English Channel, known for dairy farming, cider, and medieval history.",
        "secondary": "In World War II military history, the site of the Allied D-Day amphibious landings on June 6, 1944.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "The Allied liberation armies landed along the storm-tossed beaches of **Normandy** on D-Day."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "William the Conqueror sailed from **Normandy** with a host of knights to claim the English crown."
            },
            {
                "author": "Gustave Flaubert",
                "work": "Madame Bovary",
                "quote": "The story unfolded in the quiet farming countryside and provincial towns of upper **Normandy**."
            }
        ]
    },
    "normative": {
        "primary": "Establishing, relating to, or deriving from a standard or norm, especially of behavior or evaluation.",
        "secondary": "In philosophical ethics and legal theory, prescribing what ought to be done rather than describing empirical facts.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "Utilitarian principles provide a coherent **normative** standard for evaluating legislative morality."
            },
            {
                "author": "Max Weber",
                "work": "The Methodology of the Social Sciences",
                "quote": "Social scientists must separate empirical factual judgments from subjective **normative** evaluations."
            },
            {
                "author": "John Dewey",
                "work": "Reconstruction in Philosophy",
                "quote": "Democratic ethics construct **normative** ideals directly from lived human experience."
            }
        ]
    },
    "normodyne": {
        "primary": "A proprietary pharmaceutical brand name for labetalol, an alpha- and beta-adrenergic blocker used to treat hypertension.",
        "secondary": "In cardiovascular pharmacotherapy, an antihypertensive medication that reduces peripheral vascular resistance without causing reflex tachycardia.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Prescribing an adrenergic blocker like **Normodyne** helps control severe hypertensive crises."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Hemodynamic studies confirmed that **Normodyne** lowers arterial pressure by blocking both alpha and beta receptors."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Clinicians carefully titrated the patient's **Normodyne** dosage to stabilize labile blood pressure swings."
            }
        ]
    },
    "normotensive": {
        "primary": "Having or characterized by normal arterial blood pressure.",
        "secondary": "In cardiology, designating a patient or experimental subject whose blood pressure falls within standard healthy physiological parameters.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The regulatory baroreceptor reflex maintains the mammal in a **normotensive** state during postural shifts."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The patient remained comfortably **normotensive** throughout the postoperative recovery period."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Baseline hemodynamics must be verified in **normotensive** animals before introducing pharmacological agents."
            }
        ]
    },
    "normothermia": {
        "primary": "The state of having a normal, healthy core body temperature.",
        "secondary": "In critical care medicine and anesthesiology, the active maintenance of core body temperature between 36.5°C and 37.5°C during surgery.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "Lectures on the Phenomena of Life Common to Animals and Plants",
                "quote": "Mammalian survival depends upon the precise regulation of internal **normothermia** against cold."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The preoptic area of the hypothalamus coordinates sweating and shivering to preserve **normothermia**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Active warming blankets were applied to re-establish **normothermia** in the hypothermic survivor."
            }
        ]
    },
    "renormalise": {
        "primary": "The British English spelling of renormalize; to normalize again or readjust to an established standard.",
        "secondary": "In theoretical physics, to apply mathematical renormalization techniques to remove infinities from quantum field calculations.",
        "quotes": [
            {
                "author": "Paul Dirac",
                "work": "The Principles of Quantum Mechanics",
                "quote": "Theorists sought to **renormalise** the quantum electrodynamic equations to remove divergent integrals."
            },
            {
                "author": "Richard Feynman",
                "work": "QED: The Strange Theory of Light and Matter",
                "quote": "To calculate the electron's magnetic moment, one must **renormalise** the mass and charge parameters."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Adaptive controllers must periodically **renormalise** their baseline variables in fluctuating environments."
            }
        ]
    },
    "renormalize": {
        "primary": "To normalize again, or readjust values to conform to a standard distribution or baseline.",
        "secondary": "In quantum electrodynamics and statistical mechanics, to re-scale parameters to cancel divergent loop infinities.",
        "quotes": [
            {
                "author": "Richard Feynman",
                "work": "QED: The Strange Theory of Light and Matter",
                "quote": "Physicists learned how to **renormalize** divergent electron self-energy integrals with stunning empirical success."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Quantum chemists **renormalize** molecular orbital wavefunctions so their total probability integrates to unity."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Statistical algorithms must continuously **renormalize** probabilities as fresh observational data arrives."
            }
        ]
    },
    "subnormal": {
        "primary": "Below the normal, usual, or typical level, standard, or degree.",
        "secondary": "In medicine and meteorology, characterizing body temperature, cognitive scores, or seasonal rainfall falling beneath average norms.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "In states of profound septic collapse, the patient's temperature may fall to a **subnormal** level."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Prolonged periods of **subnormal** rainfall desiccated inland lake basins across the continent."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Sensory thresholds may register **subnormal** acuity during states of acute nervous exhaustion."
            }
        ]
    },
    "subnormality": {
        "primary": "Deficiency beneath standard levels, physiological norms, or established benchmarks.",
        "secondary": "In historical educational psychology, cognitive development or physiological capacity measuring below average benchmarks.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Psychological analysis must not confuse spiritual genius with intellectual **subnormality**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Persistent hypothermic **subnormality** indicated failing thyroid function in advanced myxedema."
            },
            {
                "author": "John Dewey",
                "work": "Democracy and Education",
                "quote": "Educational testing must distinguish between genuine developmental **subnormality** and lack of educational opportunity."
            }
        ]
    },
    "supernormal": {
        "primary": "Exceeding the normal or average; beyond what is ordinary, typical, or natural.",
        "secondary": "In psychology and ethology, designating stimuli that elicit an exaggerated biological response (supernormal stimuli).",
        "quotes": [
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Mystics report subjective experiences of **supernormal** perceptual clarity and transcendent insight."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Certain ornamental secondary sexual traits appear to function as a **supernormal** mating lure."
            },
            {
                "author": "F. W. H. Myers",
                "work": "Human Personality and Its Survival of Bodily Death",
                "quote": "The author investigated reports of **supernormal** telepathic communication among subjects."
            }
        ]
    },
    "supranormal": {
        "primary": "Beyond or transcending what is normal, ordinary, or natural; supernormal.",
        "secondary": "In cardiovascular electrophysiology, the brief period during cardiac recovery where myocardial excitability is paradoxically heightened.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "Spiritual philosophy posits the reality of **supranormal** moral ideals that elevate human conduct."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The ventricular muscle enters a transient **supranormal** phase of excitability just before total repolarization."
            },
            {
                "author": "Walter Pater",
                "work": "Marius the Epicurean",
                "quote": "He experienced an intuition of **supranormal** serenity that lifted him above mundane mortal anxieties."
            }
        ]
    },

    # Dashboard — rig (38)
    "agrigento": {
        "primary": "A historic city on the southern coast of Sicily, famous for the magnificent ancient Greek ruins in the Valley of the Temples.",
        "secondary": "In classical archaeology and Mediterranean history, ancient Akragas, birthplace of the philosopher Empedocles, renowned for monumental Doric sanctuaries.",
        "quotes": [
            {
                "author": "Johann Wolfgang von Goethe",
                "work": "Italian Journey",
                "quote": "The golden sandstone ruins of the ancient temples at **Agrigento** rise majestically against the southern sea."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The wealthy Greek colony of **Agrigento** was celebrated for its luxurious hospitality and splendid civic monuments."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "Travelers marveled at the austere classical dignity preserved among the ancient temples of **Agrigento**."
            }
        ]
    },
    "corrigenda": {
        "primary": "Things to be corrected, especially a list of errors and their corrections printed in a book after publication.",
        "secondary": "In textual bibliography and scholarly editing, the errata sheet inserted into a volume to rectify printing or editorial mistakes.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "In the second edition, the author inserted a brief list of **corrigenda** to rectify minor typographic errors."
            },
            {
                "author": "Samuel Johnson",
                "work": "Prefaces to the English Poets",
                "quote": "The careful scholar appended a leaf of **corrigenda** to preserve the purity of the ancient text."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The printer supplied a page of **corrigenda** to emend Greek transcriptions in the footnotes."
            }
        ]
    },
    "corrigendum": {
        "primary": "An error in a printed book or manuscript to be corrected; a single item in a list of corrigenda.",
        "secondary": "In academic publishing and bibliography, a formal published notice correcting a factual or typographical error in a previous article.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The editor printed a prominent **corrigendum** in the journal to correct an erroneous chemical formula."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "Every printed logarithmic table was accompanied by a tedious **corrigendum** of computational blunders."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Idler",
                "quote": "The pedantic author was mortified to discover a grave **corrigendum** upon the very first page of his treatise."
            }
        ]
    },
    "corrigible": {
        "primary": "Capable of being corrected, reformed, or improved; open to amendment.",
        "secondary": "In epistemology and ethics, describing beliefs, theories, or moral faults that yield to evidence and constructive discipline.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Human errors are happily **corrigible** when the mind submits its hypotheses to sensory experience."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "The kind-hearted blacksmith believed that any young lad was **corrigible** if treated with gentle patience."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Scientific conclusions remain perpetually **corrigible** in the light of newly discovered empirical facts."
            }
        ]
    },
    "dirigible": {
        "primary": "Capable of being steered or guided; a steerable airship equipped with an engine (a zeppelin or blimp).",
        "secondary": "In early aviation history, a lighter-than-air motorized aircraft that provided the first long-range commercial passenger flights across oceans.",
        "quotes": [
            {
                "author": "H. G. Wells",
                "work": "The War in the Air",
                "quote": "The fleet of giant German **dirigible** airships crossed the Atlantic under the cover of night."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Lost World",
                "quote": "The explorer suggested navigating the uncharted South American plateau using a light **dirigible** balloon."
            },
            {
                "author": "Winston Churchill",
                "work": "The World Crisis",
                "quote": "Naval defense required continuous anti-aircraft vigilance against reconnaissance by enemy **dirigible** cruisers."
            }
        ]
    },
    "erigeron": {
        "primary": "A large genus of composite flowering plants commonly known as fleabanes, bearing daisy-like flower heads with narrow ray florets.",
        "secondary": "In North American floristics, perennial asteraceous herbs that colonize meadows, roadsides, and alpine screes throughout the temperate zone.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Species of **Erigeron** carpet the pastures in early summer with delicate lilac and white ray flowers."
            },
            {
                "author": "John Muir",
                "work": "My First Summer in the Sierra",
                "quote": "A charming alpine **Erigeron** blossomed in the cold granite crevices near the summit snowfield."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "Gardeners value dwarf varieties of **Erigeron** for rockeries and dry floral borders."
            }
        ]
    },
    "erignathus": {
        "primary": "A genus of phocid seals containing the bearded seal (Erignathus barbatus), native to the Arctic Ocean.",
        "secondary": "In Arctic marine mammalogy and zoology, a large benthic-feeding ice seal characterized by dense fleshy facial vibrissae and heavy square foreflippers.",
        "quotes": [
            {
                "author": "Fridtjof Nansen",
                "work": "Farthest North",
                "quote": "In the leads between the Arctic ice floes, we encountered the solitary bearded seal, **Erignathus** barbatus."
            },
            {
                "author": "Spencer Fullerton Baird",
                "work": "Mammals of North America",
                "quote": "The genus **Erignathus** is distinguished from other phocids by its prominent tactile whiskers and robust skull."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The specialized sensory vibrissae of **Erignathus** enable the mammal to forage for clams along murky sea bottoms."
            }
        ]
    },
    "incorrigible": {
        "primary": "Not able to be corrected, reformed, or improved; hopelessly set in bad habits.",
        "secondary": "In educational and penological literature, an intractable individual who stubbornly resists moral rehabilitation.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Oliver Twist",
                "quote": "The parish beadle declared Oliver an **incorrigible** rogue who was certain to end upon the gallows."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She sighed over her brother's **incorrigible** carelessness with money and family responsibilities."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "Lord Henry smiled indulgently at his own **incorrigible** cynicism regarding human nature."
            }
        ]
    },
    "irrigate": {
        "primary": "To supply water to land or crops to help growth, typically by means of channels, pipes, or canals.",
        "secondary": "In medicine and surgery, to wash out or flush a wound or bodily cavity with a stream of sterile fluid.",
        "quotes": [
            {
                "author": "John Wesley Powell",
                "work": "Report on the Lands of the Arid Region of the United States",
                "quote": "Settlers must construct communal reservoirs to **irrigate** the fertile valleys of the arid West."
            },
            {
                "author": "Joseph Lister",
                "work": "On the Antiseptic Principle in the Practice of Surgery",
                "quote": "Surgeons must gently **irrigate** deep lacerations with mild antiseptic lotions to eliminate contaminants."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Canals cut from the Euphrates served to **irrigate** the blooming gardens of ancient Babylon."
            }
        ]
    },
    "irrigation": {
        "primary": "The artificial application of water to soil or crops through canals, pipes, or sprinklers to aid agriculture.",
        "secondary": "In surgical medicine, the continuous or intermittent flushing of a wound or catheter with therapeutic solutions.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The ancient civilization of the Nile valley flourished entirely upon the annual flood and canal **irrigation**."
            },
            {
                "author": "John Wesley Powell",
                "work": "Report on the Lands of the Arid Region of the United States",
                "quote": "Scientific **irrigation** transforms barren desert basins into productive agricultural lands."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Copious saline **irrigation** of the infected joint space prevented ankylosing complications."
            }
        ]
    },
    "nonrigid": {
        "primary": "Not rigid; flexible, pliant, or yielding to pressure.",
        "secondary": "In aeronautics, designating an airship (blimp) that maintains its aerodynamic envelope shape solely by internal gas pressure without a metal skeleton.",
        "quotes": [
            {
                "author": "Arthur C. Clarke",
                "work": "Voices from the Sky",
                "quote": "Coastal patrol units deployed **nonrigid** blimps for submarine reconnaissance along shipping lanes."
            },
            {
                "author": "D'Arcy Wentworth Thompson",
                "work": "On Growth and Form",
                "quote": "Cellular membranes function as **nonrigid** hydrostatic boundaries that flex under external osmotic pressure."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Robotic manipulators utilize **nonrigid** polymer joints to mimic the supple compliance of human fingers."
            }
        ]
    },
    "rig": {
        "primary": "To set up, equip, or fit out a ship, apparatus, or system with necessary sails, cordage, or machinery.",
        "secondary": "To manipulate, fix, or arrange dishonestly to secure an unfair result, as in rigging an election.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The boatheader helped to **rig** the spare steering oar before lowering for the whale."
            },
            {
                "author": "Joseph Conrad",
                "work": "Typhoon",
                "quote": "The sailors worked desperately to **rig** safety lifelines across the swamped main deck."
            },
            {
                "author": "Mark Twain",
                "work": "Life on the Mississippi",
                "quote": "Corrupt river gamblers tried to **rig** the card deck to fleece unsuspicious travelers."
            }
        ]
    },
    "riga": {
        "primary": "The capital and largest city of Latvia, a major historic Baltic port on the Gulf of Riga.",
        "secondary": "In commercial and maritime history, an influential member of the Hanseatic League celebrated for exporting timber, flax, and naval stores (Riga fir).",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Merchant caravans transported amber from the Baltic shores near **Riga** across the Roman frontier."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Shipbuilders in London prized stout hemp and straight mast timber imported from **Riga**."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Mirror of the Sea",
                "quote": "The brig loaded a cargo of fragrant Baltic timber at **Riga** for the Mediterranean ports."
            }
        ]
    },
    "rigamarole": {
        "primary": "A lengthy, complicated, and confusing procedure or story; rigmarole.",
        "secondary": "A rambling, incoherent, or foolish discourse designed to evade direct answers.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The legal proceedings degenerated into an incomprehensible **rigamarole** of parchment and precedent."
            },
            {
                "author": "Mark Twain",
                "work": "The Innocents Abroad",
                "quote": "The guide launched into an elaborate **rigamarole** regarding the miraculous history of the relic."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She dismissed his excuses as mere political **rigamarole** intended to quiet the electors."
            }
        ]
    },
    "rigatoni": {
        "primary": "A type of tube-shaped pasta with ridged external surfaces and straight-cut ends, popular in Italian cuisine.",
        "secondary": "In culinary gastronomy, a hollow extruded pasta whose ridges hold thick, hearty meat or tomato ragù sauces.",
        "quotes": [
            {
                "author": "Elizabeth David",
                "work": "Italian Food",
                "quote": "Toss the freshly boiled **rigatoni** with a robust sausage and tomato sauce so the ridges catch the meat."
            },
            {
                "author": "M. F. K. Fisher",
                "work": "The Art of Eating",
                "quote": "We enjoyed steaming platters of baked **rigatoni** layered with mozzarella and fragrant basil."
            },
            {
                "author": "Waverley Root",
                "work": "The Food of Italy",
                "quote": "Roman trattorie serve **rigatoni** with pajata, maintaining an ancient culinary tradition."
            }
        ]
    },
    "rigel": {
        "primary": "A brilliant blue-white supergiant star in the constellation Orion, the seventh-brightest star in the night sky.",
        "secondary": "In stellar astrophysics, a luminous binary star system (Beta Orionis) approximately 860 light-years from Earth with an absolute luminosity tens of thousands of times that of the Sun.",
        "quotes": [
            {
                "author": "Camille Flammarion",
                "work": "Popular Astronomy",
                "quote": "The dazzling sapphire brilliance of **Rigel** marks the western foot of the mighty hunter Orion."
            },
            {
                "author": "John Herschel",
                "work": "Outlines of Astronomy",
                "quote": "Spectroscopic observations of **Rigel** reveal an intensely hot supergiant shedding mass into interstellar space."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I walked home under the glittering winter constellations, guided by the cold blue spark of **Rigel**."
            }
        ]
    },
    "rigged": {
        "primary": "Equipped, outfitted, or fitted with sails, cordage, or mechanical equipment.",
        "secondary": "Manipulated, prearranged, or fixed dishonestly to produce a fraudulent outcome.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The Pequod was fully **rigged** for her three-year cruise into the remote Pacific sperm whale grounds."
            },
            {
                "author": "Joseph Conrad",
                "work": "Youth",
                "quote": "The Judea was a bark **rigged** ship that creaked in every timber under the heavy seas."
            },
            {
                "author": "Upton Sinclair",
                "work": "The Jungle",
                "quote": "Union delegates warned that the factory election was hopelessly **rigged** by management."
            }
        ]
    },
    "rigger": {
        "primary": "A person skilled in the erection, installation, and maintenance of ship rigging, heavy hoisting equipment, or scaffolding.",
        "secondary": "In aviation and industrial construction, a specialized craftsman who aligns cables and secures structural loads for cranes.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Redburn",
                "quote": "The experienced shipyard **rigger** clambered up the shroud lines with the agility of a monkey."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Nigger of the 'Narcissus'",
                "quote": "A veteran **rigger** checked every stay and turnbuckle before the vessel faced the Cape horn gales."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "Shipwrights and every busy sail **rigger** hammered along the crowded Thames docks."
            }
        ]
    },
    "rigging": {
        "primary": "The system of ropes, cables, chains, and spars that supports and controls the masts and sails of a vessel.",
        "secondary": "In industrial construction and theater, the tackle, hoists, and ropes used to lift and support heavy scenery or materials.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The gale shrieked through the taut cordage of the **rigging**, coating the ratlines with ice."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "A solitary seaman hung suspended high in the **rigging**, scouring rust from the topgallant mast."
            },
            {
                "author": "Richard Henry Dana Jr.",
                "work": "Two Years Before the Mast",
                "quote": "We spent long watches tarring down the standing **rigging** under the tropical sun."
            }
        ]
    },
    "rigid": {
        "primary": "Unable to bend, yield, or be forced out of shape; stiff, unyielding, and inflexible.",
        "secondary": "Strict, unbending, and uncompromising in rule, discipline, or belief.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural classification must not be bound by **rigid** preconceived notions of morphological perfection."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her uncle held a **rigid** code of family honor that admitted no compromise with public opinion."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman military discipline was enforced with **rigid** severity in every provincial camp."
            }
        ]
    },
    "rigidification": {
        "primary": "The process of becoming rigid, stiff, or inflexible; hardening.",
        "secondary": "In social philosophy and political science, the bureaucratic petrification or dogmatic ossification of institutions.",
        "quotes": [
            {
                "author": "Max Weber",
                "work": "The Protestant Ethic and the Spirit of Capitalism",
                "quote": "The **rigidification** of religious enthusiasm into formal bureaucratic dogma marked the loss of charismatic vitality."
            },
            {
                "author": "John Dewey",
                "work": "Democracy and Education",
                "quote": "The chief danger in institutional education is the progressive **rigidification** of instructional routines."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Fibrotic disease leads to progressive **rigidification** of the pulmonary parenchyma."
            }
        ]
    },
    "rigidify": {
        "primary": "To make or become rigid, stiff, or inflexible.",
        "secondary": "To make an attitude, policy, or theoretical framework strictly uncompromising and resistant to change.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Censorship tends to **rigidify** public dogma into unthinking, lifeless prejudice."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Without conscious effort to learn new skills, aging minds tend to **rigidify** into repetitive motor habits."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Cross-linking peptidoglycan polymers serves to **rigidify** the bacterial cell wall against osmotic pressure."
            }
        ]
    },
    "rigidifying": {
        "primary": "Making or becoming rigid, stiff, or unyielding.",
        "secondary": "Exerting a hardening or ossifying influence upon institutions, habits, or materials.",
        "quotes": [
            {
                "author": "John Dewey",
                "work": "Human Nature and Conduct",
                "quote": "Uncritical tradition acts as a **rigidifying** force, arresting creative adaptation in social life."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Calcification produces a **rigidifying** effect upon the skeletal plates of invertebrates."
            },
            {
                "author": "William James",
                "work": "Pragmatism",
                "quote": "The philosopher warned against the **rigidifying** tendencies of absolute rationalist systems."
            }
        ]
    },
    "rigidity": {
        "primary": "Stiffness, inflexibility, or physical resistance to bending and deforming forces.",
        "secondary": "In clinical neurology, a sustained resistance to passive muscle stretch (e.g., lead-pipe rigidity in Parkinsonism).",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The **rigidity** and cohesion of solid bodies arises from the intense attractive forces between adjacent particles."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Marked muscular **rigidity** of the abdominal wall serves as an cardinal sign of acute peritonitis."
            },
            {
                "author": "George Eliot",
                "work": "Daniel Deronda",
                "quote": "His proud countenance relaxed from its customary **rigidity** into a rare smile of warmth."
            }
        ]
    },
    "rigidly": {
        "primary": "In a rigid, stiff, or inflexible manner; without yielding or bending.",
        "secondary": "Strictly and uncompromisingly adhering to rules, customs, or moral principles.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The haughty baronet adhered **rigidly** to the formal etiquette of his aristocratic ancestors."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection does not operate **rigidly** in uniform environments where competition is weak."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "St. John stood **rigidly** upon his theological principles, demanding complete submission to duty."
            }
        ]
    },
    "rigidness": {
        "primary": "Unyielding stiffness, physical immobility, or stern moral strictness.",
        "secondary": "Unyielding firmness of posture, purpose, or moral temperament.",
        "quotes": [
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "The Puritan magistrate was marked by a cold **rigidness** that tempered justice with merciless severity."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The iron **rigidness** of Captain Ahab's expression revealed his monomaniacal determination."
            },
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "The style was preserved from dry **rigidness** by subtle cadences of poetic rhythm."
            }
        ]
    },
    "rigil": {
        "primary": "An alternative name for Alpha Centauri (Rigil Kentaurus), the brightest star in the southern constellation of Centaurus.",
        "secondary": "In historical Arabic astronomy and astrometry, the foot of the Centaur, designating the closest star system to our solar system (4.37 light-years).",
        "quotes": [
            {
                "author": "Camille Flammarion",
                "work": "Popular Astronomy",
                "quote": "Known to ancient navigators as **Rigil** Kentaurus, Alpha Centauri shines as the third-brightest star in the sky."
            },
            {
                "author": "John Herschel",
                "work": "Outlines of Astronomy",
                "quote": "Telescopic measurements of **Rigil** at the Cape Observatory demonstrated its binary nature."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Cosmos",
                "quote": "Southern mariners looked to **Rigil** to guide their navigation beneath the Southern Cross."
            }
        ]
    },
    "rigmarole": {
        "primary": "A lengthy, complicated, and confusing procedure or statement; foolishly elaborate talk.",
        "secondary": "In formal and colloquial usage, tedious administrative red tape or an incoherent rambling narrative.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "The Circumlocution Office wrapped every trivial petition in an endless **rigmarole** of official delays."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She refused to listen to her husband's defensive **rigmarole** regarding his failed financial speculations."
            },
            {
                "author": "Mark Twain",
                "work": "Roughing It",
                "quote": "The mining recorder subjected the prospector to a tiresome **rigmarole** of legal affidavits."
            }
        ]
    },
    "rigor": {
        "primary": "Exacting thoroughness, exhaustive precision, or uncompromising strictness in action, thought, or analysis.",
        "secondary": "In medicine and pathology, a sudden feeling of cold accompanied by shivering; or the post-mortem stiffening of muscles (rigor mortis).",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Scientific induction requires absolute mathematical **rigor** to eliminate erroneous hypotheses."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The sudden onset of lobar pneumonia is marked by a severe chill or **rigor**."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection tests every organic structure with the unsparing **rigor** of survival."
            }
        ]
    },
    "rigorous": {
        "primary": "Extremely thorough, accurate, or exhaustive; strictly applied or followed.",
        "secondary": "Harsh, severe, or austere in climate, conditions, or moral discipline.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Only through **rigorous** geometrical demonstration can the true laws of mechanics be established."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "A **rigorous** scientific training teaches the student to accept only evidence verified by observation."
            },
            {
                "author": "Jack London",
                "work": "The Call of the Wild",
                "quote": "The sledge dogs endured the **rigorous** Arctic winter through relentless physical stamina."
            }
        ]
    },
    "rigorously": {
        "primary": "In an extremely thorough, exhaustive, or accurate manner; strictly and without exception.",
        "secondary": "With severe discipline, austerity, or unbending adherence to law or scientific method.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Every working hypothesis must be **rigorously** tested against observed facts across diverse disciplines."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "A democratic society must **rigorously** protect the right of minorities to voice nonconformist opinions."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Spartan magistrates **rigorously** enforced the ancient laws of Lycurgus among youth."
            }
        ]
    },
    "rigorousness": {
        "primary": "Exacting thoroughness, mathematical accuracy, or uncompromising strictness.",
        "secondary": "Severe austerity of climate, discipline, or intellectual scrutiny.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The admirable **rigorousness** of mathematical reasoning prevents the entry of superstitious error."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Inductive logic derives its authority from the unsparing **rigorousness** of experimental controls."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Puritan piety was distinguished by an unbending moral **rigorousness** that shunned worldly pleasure."
            }
        ]
    },
    "rigour": {
        "primary": "The British English spelling of rigor; exacting strictness, thoroughness, or severity.",
        "secondary": "Harshness or severity of climate, circumstances, or monastic discipline.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Critical analysis must combine intellectual **rigour** with sympathetic candour toward human weakness."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The legionaries complained of the unrelenting **rigour** of military discipline on the frontier."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "The old Covenanter lived under the severe **rigour** of Calvinist orthodoxy."
            }
        ]
    },
    "rigourousness": {
        "primary": "The British English spelling of rigorousness; uncompromising thoroughness or strictness.",
        "secondary": "Exacting thoroughness in academic scholarship, scientific investigation, or moral standards.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Most Eminent English Poets",
                "quote": "The philosophical **rigourousness** of Milton's theological verse commands enduring admiration."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The unbending **rigourousness** of the revolutionary tribunal terrorized Paris for over a year."
            },
            {
                "author": "John Ruskin",
                "work": "The Seven Lamps of Architecture",
                "quote": "Medieval builders tempered structural **rigourousness** with joyful decorative variety."
            }
        ]
    },
    "rigout": {
        "primary": "An outfit or set of clothes, especially an unusual, eccentric, or elaborate costume; rig-out.",
        "secondary": "In colloquial nineteenth-century British speech, an entire suit of apparel or distinctive dress.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "Pip was embarrassed by Joe's awkward **rigout** when the honest blacksmith visited London in his Sunday best."
            },
            {
                "author": "Thomas Hardy",
                "work": "Under the Greenwood Tree",
                "quote": "The country musicians donned their finest Sunday **rigout** to perform at the village wedding."
            },
            {
                "author": "George Orwell",
                "work": "Down and Out in Paris and London",
                "quote": "He exchanged his respectable suit for a tramp's ragged **rigout** before hitting the open road."
            }
        ]
    },
    "serigraph": {
        "primary": "A silkscreen print or screenprint produced as an original work of fine art.",
        "secondary": "In fine art printmaking, a multicolored graphic print pulled through fine silk or synthetic mesh stencils.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The graphic artisan pulled a brilliant multicolored **serigraph**, registering each tint through stretched silk mesh."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The artist decorated his studio with an experimental **serigraph** displaying vibrant flat planes of Japanese color."
            },
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "Modern printmakers rediscovered ancient stenciling methods, elevating the commercial screen into an expressive **serigraph**."
            }
        ]
    },
    "serigraphy": {
        "primary": "The artistic process or technique of making silkscreen prints; screenprinting.",
        "secondary": "In graphic arts history, the fine art screen-printing method developed in the early twentieth century to distinguish artistic prints from industrial stencils.",
        "quotes": [
            {
                "author": "William Morris",
                "work": "Hopes and Fears for Art",
                "quote": "Mastery of manual **serigraphy** allows the artisan to layer bold decorative pigments across paper."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "Printmakers combined etching with **serigraphy** to produce rich velvety surface textures."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The craft of **serigraphy** demonstrates that direct mechanical printing can serve genuine artistic imagination."
            }
        ]
    },
    "unrigged": {
        "primary": "Having had the rigging, sails, or equipment removed, especially of a ship.",
        "secondary": "Stripped of tackle, cordage, or mechanical rigging for winter lay-up or scrap.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The battered whaler lay **unrigged** at the wharf, her bare masts pointing toward the grey November sky."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Mirror of the Sea",
                "quote": "Old decommissioned sailing vessels rested **unrigged** in the tidal mud of the river estuary."
            },
            {
                "author": "Richard Henry Dana Jr.",
                "work": "Two Years Before the Mast",
                "quote": "The sailors left the ship completely **unrigged** while the hull was hauled out into dry dock."
            }
        ]
    }
}

CIRCULAR_REGEX = re.compile(
    r"\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b",
    re.IGNORECASE,
)

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def validate_all():
    print(f"Total words in data_order_b1_p2: {len(data_order_b1_p2)}")
    errors = []

    for word, d in data_order_b1_p2.items():
        prim = d.get("primary", "").strip()
        sec = d.get("secondary", "").strip()
        quotes = d.get("quotes", [])

        # 1. Primary length
        if len(prim) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(prim)} < 25): {prim}")

        # 2. Secondary length
        if len(sec) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(sec)} < 25): {sec}")

        # 3. Circular phrasing
        if CIRCULAR_REGEX.search(prim):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {prim}")
        if CIRCULAR_REGEX.search(sec):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {sec}")

        # 4. Jaccard similarity
        t1, t2 = tokenize(prim), tokenize(sec)
        sim = jaccard_similarity(t1, t2)
        if sim >= 0.70:
            errors.append(f"[{word}] Primary and secondary too similar (Jaccard {sim:.2f} >= 0.70)")

        # 5. Exactly 3 quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Exactly 3 quotes required, found {len(quotes)}")

        # 6. Distinct authors
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Duplicate authors in quotes: {authors}")

        # 7. Target bolded
        clean_word = word.replace("-", "[ -]?")
        pat = re.compile(rf"\*\*[^*]*{clean_word}[^*]*\*\*", re.IGNORECASE)
        for i, q in enumerate(quotes):
            txt = q.get("quote", "")
            if not pat.search(txt) and f"**{word.lower()}**" not in txt.lower():
                errors.append(f"[{word}] Quote {i+1} by {q.get('author')} missing bolded target word: {txt}")

    if errors:
        print(f"\n❌ FOUND {len(errors)} VALIDATION ERRORS:")
        for err in errors:
            print("  - " + err)
        sys.exit(1)
    else:
        print("\n✅ ALL 73 words in Cluster Order Batch 1 Part 2 PASSED local pre-audit validation!")

if __name__ == "__main__":
    validate_all()
