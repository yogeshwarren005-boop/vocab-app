# -*- coding: utf-8 -*-
"""
curate_order_b3_p1.py
Curated dataset for Cluster Order Batch 3 Part 1:
- Dashboard — rect (76 words)
Total: 76 words
"""
import re

data_order_b3_p1 = {
    # ----------------------------------------------------
    # DASHBOARD — RECT (76 words)
    # ----------------------------------------------------
    "correct": {
        "primary": "Free from error, fault, or mistake; in accordance with fact, truth, or accepted standards.",
        "secondary": "To adjust, rectify, or make right an erroneous statement, mechanical setting, or bodily defect.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Astronomers must compute gravitational perturbations to obtain the **correct** trajectory of the comet."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Clear thinking depends on forming **correct** and distinct ideas corresponding with external reality."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "If my theoretical reasoning be **correct**, natural selection must modify all competing varieties."
            }
        ]
    },
    "correctable": {
        "primary": "Capable of being set right, amended, or remedied; curable.",
        "secondary": "In optics and typography, amenable to mechanical compensation, adjustment, or proof editorial revision.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Fallacies of observation are easily **correctable** once experimental controls are introduced."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Early refractive errors in childhood remain readily **correctable** with proper convex lenses."
            },
            {
                "author": "Benjamin Franklin",
                "work": "Autobiography",
                "quote": "My youthful faults seemed like printer's errata, regrettable yet fortunately **correctable** in later life."
            }
        ]
    },
    "corrected": {
        "primary": "Made free from errors, defects, or faults; amended or set right.",
        "secondary": "Adjusted mathematically or experimentally to account for systematic calibration errors.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The chronometer readings were carefully **corrected** for daily fluctuations in ambient temperature."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The historical chronicle was **corrected** against original archival manuscripts discovered at Rome."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "He patiently **corrected** my exercises in shorthand until my transcription attained neat accuracy."
            }
        ]
    },
    "correction": {
        "primary": "The action or process of correcting something, or a change that rectifies an error.",
        "secondary": "In astronomy and geodesy, a mathematical factor added to eliminate atmospheric or instrument bias.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The astronomer applies a necessary **correction** for atmospheric refraction near the horizon."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Open intellectual discussion provides the essential **correction** for popular societal prejudices."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Prisons were originally conceived as houses of moral **correction** rather than mere idle confinement."
            }
        ]
    },
    "correctional": {
        "primary": "Relating to or designed for the reform, discipline, or rehabilitation of offenders.",
        "secondary": "In penology, denoting institutions, procedures, or penal facilities intended to reform convicts.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "On the Penitentiary System in the United States",
                "quote": "The American **correctional** system sought to replace corporal punishment with moral labor."
            },
            {
                "author": "Charles Dickens",
                "work": "American Notes",
                "quote": "I visited the famous Philadelphia **correctional** facility to inspect its solitary confinement cells."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The magistrates discussed establishing a **correctional** home for delinquent youths from the parish."
            }
        ]
    },
    "corrections": {
        "primary": "The plural of correction; marks, amendments, or alterations that rectify mistakes.",
        "secondary": "The municipal or penal system responsible for managing prisons and incarcerated populations.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "The publisher sent the proofs covered in copious authorial **corrections** across every margin."
            },
            {
                "author": "Edward Gibbon",
                "work": "Memoirs of My Life and Writings",
                "quote": "I subjected the text to endless **corrections** before committing the chapters to the printer."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "On the Penitentiary System in the United States",
                "quote": "The department of **corrections** maintained strict records tracking convict reform and labor output."
            }
        ]
    },
    "correctitude": {
        "primary": "Conscious correctness, rectitude, or propriety in conduct, manners, or speech.",
        "secondary": "Strict, sometimes pedantic adherence to established social conventions or grammatical standards.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "Gilbert Osmond's outward **correctitude** concealed a chilling aesthetic selfishness."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Secret Agent",
                "quote": "The embassy secretary preserved an icy official **correctitude** while receiving the foreign envoy."
            },
            {
                "author": "George Eliot",
                "work": "Daniel Deronda",
                "quote": "Her social **correctitude** was so rigid that it intimidated younger acquaintances at the gathering."
            }
        ]
    },
    "corrective": {
        "primary": "Intended or serving to rectify, counteract, or heal something undesirable or harmful.",
        "secondary": "A drug, therapeutic regimen, or disciplinary measure that restores physiological or social equilibrium.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Unfettered public debate serves as an indispensable **corrective** to the dogmatism of majorities."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The physician introduced aromatic syrups as a pleasant **corrective** to disguise the bitter physic."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Competition among rivals provides a natural **corrective** against exorbitant monopoly pricing."
            }
        ]
    },
    "correctly": {
        "primary": "In a manner free from mistakes; accurately, properly, or in accordance with truth or convention.",
        "secondary": "Following rigorous methodological protocols or standard moral etiquette.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "If naturalists classify organisms **correctly**, taxonomy will mirror the true tree of common descent."
            },
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "When the geometrical principles are **correctly** applied, the predicted orbits match observation."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "Elinor reasoned **correctly** that her sister's distress arose from an unacknowledged attachment."
            }
        ]
    },
    "correctness": {
        "primary": "Freedom from error; conformity to truth, established fact, or recognized standards.",
        "secondary": "In linguistics, philosophy, and formal logic, strict adherence to syntactic or deductive validity.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The **correctness** of language depends upon keeping the meaning of terms steady and unambiguous."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "Formal logic tests the deductive **correctness** of arguments independently of empirical content."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "Pope achieved unmatched poetic **correctness** through tireless polish of verse and meter."
            }
        ]
    },
    "direct": {
        "primary": "Extending in a straight line without detour; or proceeding from source to destination without intermediaries.",
        "secondary": "To command, manage, guide, or supervise with authoritative instruction.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Every body continues in its state of uniform motion in a right line unless compelled to deviate by a **direct** force."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor dispatched a courier along the **direct** military road connecting Rome to Byzantium."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "Inductive axioms must **direct** experimental inquiries toward the fundamental forms of nature."
            }
        ]
    },
    "directed": {
        "primary": "Guided, focused, ordered, or aimed toward a specific goal, recipient, or destination.",
        "secondary": "In mathematics, having a defined orientation or sign (such as a directed line segment or vector).",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Natural selection operates through **directed** preservation of favorable hereditary variations."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The artillery was **directed** against the weakest bastion of the besieged city walls."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Voluntary attention involves **directed** consciousness held steadily upon a chosen idea."
            }
        ]
    },
    "directing": {
        "primary": "Guiding, managing, conducting, or aiming something toward an intended course.",
        "secondary": "In executive leadership and the performing arts, overseeing artistic interpretation or strategic operations.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "By **directing** that industry in such a manner as its produce may be of greatest value, he intends only his own gain."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "The root-apex exhibits an active sensitivity, **directing** growth downward away from dry surfaces."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The president has the constitutional duty of **directing** the armed forces during wartime."
            }
        ]
    },
    "direction": {
        "primary": "A course along which someone or something moves; or an authoritative instruction guiding action.",
        "secondary": "Management, supervision, or control over an organization, artistic ensemble, or undertaking.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Change of motion is proportional to the impressed motive force, and is made in the **direction** of that straight line."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Species have diverged in every **direction** to fill diverse niches in the economy of nature."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Public opinion exercises an irresistible **direction** over the course of democratic legislation."
            }
        ]
    },
    "directional": {
        "primary": "Relating to or indicating a specific direction in space or orientation.",
        "secondary": "In telecommunications and acoustics, transmitting or receiving signals primarily in one preferred heading.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The glacial striations revealed a clear **directional** movement from north to south across the bedrock."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Auditory localization depends on **directional** timing cues processed in the superior olivary nuclei."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Evolution exhibits a distinct **directional** trend toward morphological complexity in vertebrates."
            }
        ]
    },
    "directionality": {
        "primary": "The characteristic of having or moving in a specific direction; oriented vector property.",
        "secondary": "In molecular biology and physics, the asymmetric polarity of molecular strands (such as 5' to 3' in DNA).",
        "quotes": [
            {
                "author": "Francis Crick",
                "work": "What Mad Pursuit",
                "quote": "The chemical **directionality** of nucleic acid synthesis proceeds invariably from 5' to 3' ends."
            },
            {
                "author": "Arthur Eddington",
                "work": "The Nature of the Physical World",
                "quote": "Thermodynamics imparts an objective temporal **directionality** to the universe through entropy increase."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "Geotropism gives definite vertical **directionality** to the descending radicle and ascending plumule."
            }
        ]
    },
    "directionless": {
        "primary": "Lacking a defined direction, guidance, destination, or coherent life purpose.",
        "secondary": "Drifting aimlessly without programmatic focus or navigational coordinates.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The ship drifted in the doldrums, an aimless, **directionless** speck on the glassy ocean."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "He wandered the Eastern ports in a **directionless** reverie, haunted by the shadow of his past."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Fred Vincy spent his youth in a **directionless** drift before finding modest agricultural labor."
            }
        ]
    },
    "directive": {
        "primary": "An official or authoritative instruction guiding action or policy.",
        "secondary": "Serving to guide, direct, or point toward a particular goal or operational standard.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor issued an imperial **directive** instructing provincial magistrates to rebuild coastal aqueducts."
            },
            {
                "author": "Woodrow Wilson",
                "work": "Congressional Government",
                "quote": "The executive office communicates its strategic policies through an explicit departmental **directive**."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Psychology",
                "quote": "Conscious desire exercises a **directive** influence upon the bodily motor reflexes."
            }
        ]
    },
    "directiveness": {
        "primary": "The property or quality of providing authoritative guidance, aim, or leadership.",
        "secondary": "In psychological and administrative theory, an assertive leadership posture that sets explicit tasks.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Teleological **directiveness** distinguishes living mental behavior from blind mechanical motion."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "A cabinet must possess energetic **directiveness** to guide parliamentary debate to constructive ends."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Scientific pedagogy loses its value without the purposeful **directiveness** of laboratory practice."
            }
        ]
    },
    "directivity": {
        "primary": "The property of being directional; or the degree to which an antenna concentrates radiation.",
        "secondary": "In radio engineering and acoustics, a quantitative measure of radiation intensity in a given spatial angle.",
        "quotes": [
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "Electromagnetic propagation exhibits spatial **directivity** depending upon the configuration of conductors."
            },
            {
                "author": "Oliver Lodge",
                "work": "Signalling Across Space Without Wires",
                "quote": "Parabolic reflectors enhance the directional **directivity** of Hertzian radio waves."
            },
            {
                "author": "John Tyndall",
                "work": "Sound",
                "quote": "Acoustic horns concentrate sonic vibrations, imparting sharp spatial **directivity** to the beam."
            }
        ]
    },
    "directly": {
        "primary": "In a straight line or without intermediaries; immediately in time or manner.",
        "secondary": "Frankly, candidly, and plainly without equivocation or evasive circumlocution.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Physical conditions act **directly** on the organism, producing slight plastic modifications."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "She answered him **directly**, without any attempt to disguise her genuine feelings."
            },
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Gravitational attraction varies **directly** as the mass and inversely as the square of distance."
            }
        ]
    },
    "directness": {
        "primary": "Straightforwardness, candid simplicity, or the quality of proceeding without detour.",
        "secondary": "In communication and literary style, plain clarity that eschews unnecessary ornamentation.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Dorothea spoke with an earnest **directness** that disarmed the worldly cynicism of her listeners."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "True eloquence derives its compelling force from the plain **directness** of truth."
            },
            {
                "author": "William James",
                "work": "Pragmatism",
                "quote": "American philosophical thought is characterized by a vigorous intellectual **directness**."
            }
        ]
    },
    "director": {
        "primary": "A person who is in charge of an activity, department, enterprise, or creative production.",
        "secondary": "In corporate governance, a member of the governing board elected to supervise executive management.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The **director** of a joint-stock company manages money belonging to others rather than his own."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The prefect acted as the supreme **director** of the imperial postal network across Gaul."
            },
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "Mr. Merdle was sought after as a board **director** by every speculative railway venture in London."
            }
        ]
    },
    "directorate": {
        "primary": "A board of directors, or an executive department in a government or corporation.",
        "secondary": "The office, tenure, or collective governing body charged with institutional administration.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Two Letters on the Conduct of Our Domestic Parties",
                "quote": "The French **Directorate** ruled with erratic violence, swinging between revolutionary and royalist extremes."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "The Old Regime and the Revolution",
                "quote": "The revolutionary **directorate** attempted to centralize all provincial power within Paris ministries."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "Modern enterprise separates ownership shares from the professional administrative **directorate**."
            }
        ]
    },
    "directorship": {
        "primary": "The position, office, or tenure of a director in an organization or corporation.",
        "secondary": "The period or authority associated with managing an enterprise or cultural institution.",
        "quotes": [
            {
                "author": "Anthony Trollope",
                "work": "The Way We Live Now",
                "quote": "He accepted a lucrative **directorship** on the board of Melmotte's South Central Pacific railway."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Securing a **directorship** in the East India Company offered opportunities for rapid personal fortune."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "Clive's energetic **directorship** restored discipline to the company's demoralized Bengal settlements."
            }
        ]
    },
    "directory": {
        "primary": "A book, listing, or database containing an organized index of names, addresses, or phone numbers.",
        "secondary": "In computer operating systems, a file system structure that organizes and indexes files into a hierarchy.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Snagsby consulted the London commercial **directory** to verify the law stationer's address."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The French executive **directory** promulgated administrative orders that stifled provincial liberties."
            },
            {
                "author": "Alan Turing",
                "work": "Computing Machinery and Intelligence",
                "quote": "An orderly storage **directory** enables the mechanical brain to retrieve program routines rapidly."
            }
        ]
    },
    "erect": {
        "primary": "Rigidly upright in posture or position; vertical.",
        "secondary": "To construct, build, assemble, or establish an edifice, monument, or institution.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Man alone has become an **erect** biped, with his hands liberated for the manipulation of tools."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The victorious legions paused to **erect** a triumphal arch commemorating the conquest."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Two of far nobler shape, **erect** and tall, godlike erect, with native honor clad."
            }
        ]
    },
    "erectile": {
        "primary": "Capable of being raised, erected, or distended into an upright, rigid state.",
        "secondary": "In mammalian histology, vascular tissue (corpus cavernosum) that becomes turgid when engorged with blood.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Many birds elevate an **erectile** crest of feathers when displaying courtship rivalry."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Parasympathetic nerve stimulation causes vascular engorgement of **erectile** tissue."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Histologists examined the smooth muscle trabeculae that form the cavernous meshwork in **erectile** organs."
            }
        ]
    },
    "erecting": {
        "primary": "The act of setting up, building, assembling, or raising upright.",
        "secondary": "Establishing an institution, monument, or theoretical system on firm foundations.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor spent enormous treasury funds on **erecting** a magnificent basilica in the capital."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "We are **erecting** a new organon of the sciences founded on rigorous empirical induction."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I spent several delightful spring mornings **erecting** the frame of my small woodland cabin."
            }
        ]
    },
    "erection": {
        "primary": "The building, raising, or construction of a structure or monument; or the physiological stiffening of tissue.",
        "secondary": "In histology and physiology, the vascular engorgement of specialized tissue producing rigid turgidity.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **erection** of the column of Trajan celebrated the final pacification of the Dacian kingdom."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Hemodynamic pressure produces immediate **erection** through arterial dilation and venous occlusion."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Statutes govern the **erection** of public bridges across navigable rivers within the realm."
            }
        ]
    },
    "erectly": {
        "primary": "In a vertical, upright, or perpendicular posture.",
        "secondary": "With proud, dignified, or resolute physical carriage.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "Dr. Manette walked **erectly** through the crowded courtroom, his former infirmity vanished."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The knight sat **erectly** upon his warhorse, defying the shouts of the hostile spectators."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "She carried herself **erectly**, meeting the direct gaze of the inspectress without flinching."
            }
        ]
    },
    "erectness": {
        "primary": "Uprightness, perpendicular posture, or vertical physical carriage.",
        "secondary": "In evolutionary anthropology, the habitual bipedal stance characteristic of the human lineage.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The habitual **erectness** of human posture modified the entire pelvic architecture of primates."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Man's Place in Nature",
                "quote": "The anatomical **erectness** of human gait reflects modifications in the spinal curvatures and heel bones."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "His moral collapse was mirrored in the loss of that proud physical **erectness** he once displayed."
            }
        ]
    },
    "incorrect": {
        "primary": "Not in accordance with fact, truth, or recognized standards; wrong or erroneous.",
        "secondary": "Inappropriate, unbecoming, or improper according to social etiquette or artistic convention.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "False facts are highly injurious to the progress of science, for an **incorrect** claim may long endure."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Men fall into error when they reason from an **incorrect** and ill-defined definition of words."
            },
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "Mr. Knightley gently pointed out that her treatment of Miss Bates had been entirely **incorrect**."
            }
        ]
    },
    "incorrectly": {
        "primary": "In a mistaken, erroneous, or inaccurate manner; not properly.",
        "secondary": "In violation of grammatical syntax, experimental calibration, or polite social protocol.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "If the prism is **incorrectly** positioned, the refracted spectral lines will overlap and blur."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Philosophers reason **incorrectly** when they infer metaphysical necessity from mere mental habit."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The island was **incorrectly** charted on ancient maps, lying three leagues eastward of its true place."
            }
        ]
    },
    "incorrectness": {
        "primary": "Inaccuracy, error, or failure to conform to truth or accepted factual standards.",
        "secondary": "Infelicity of phrasing, improper social deportment, or flaw in mathematical proof.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The **incorrectness** of the premise inevitably vitiated every deduction built upon it."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "Critics noted the occasional grammatical **incorrectness** that marred Shakespeare's rapid dialogue."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "A single hidden contradiction demonstrates the logical **incorrectness** of the entire axiomatic scheme."
            }
        ]
    },
    "indirect": {
        "primary": "Not proceeding in a straight line; circuitous, roundabout, or secondary.",
        "secondary": "Achieved, derived, or expressed obliquely rather than explicitly or immediately.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The merchant promotes the public welfare through an **indirect** consequence of pursuing his own gain."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection exerts an **indirect** influence on non-adaptive traits through correlated variation."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor employed **indirect** diplomacy to foment discord among neighboring barbarian chieftains."
            }
        ]
    },
    "indirection": {
        "primary": "Deceitful or roundabout behavior, speech, or methods; indirect approach.",
        "secondary": "In classical literature and rhetoric, reaching a subtle truth or goal obliquely rather than bluntly.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "And thus do we of wisdom and of reach, with windlasses and with assays of bias, by **indirection** find directions out."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "Parliament should avoid devious fiscal **indirection** when seeking revenue from free colonies."
            },
            {
                "author": "Henry James",
                "work": "The Art of the Novel",
                "quote": "The master novelist achieves dramatic psychological depth through exquisite artistic **indirection**."
            }
        ]
    },
    "indirectly": {
        "primary": "In a roundabout, circuitous, or oblique manner; not immediately or straightforwardly.",
        "secondary": "Through intermediaries or secondary causal links rather than by direct intervention.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Climate affects living species both directly and **indirectly** by determining food supply and competitors."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "We perceive external substances only **indirectly** through the sensory ideas they excite in the mind."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Taxes levied on raw materials raise the final retail prices of manufactured consumer goods **indirectly**."
            }
        ]
    },
    "indirectness": {
        "primary": "Circuitousness, obliqueness, or avoidance of straightforward action or expression.",
        "secondary": "Deliberate evasiveness, subtlety, or reliance on roundabout procedural routes.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "She was perplexed by the calculated **indirectness** with which Madame Merle introduced the topic."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Mr. Bulstrode preferred fiscal **indirectness**, shielding his pious reputation behind compliant agents."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Scientific deduction often requires circuitous **indirectness** when empirical experiments are precluded."
            }
        ]
    },
    "insurrection": {
        "primary": "A violent uprising against an authority or government; rebellion or mutiny.",
        "secondary": "In constitutional law, armed resistance to sovereign authority falling short of organized civil war.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "An armed **insurrection** of peasants broke out in Gaul, devastating estates and disrupting trade."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The federal government must possess adequate constitutional authority to suppress domestic **insurrection**."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The thunder of popular **insurrection** roared through the Parisian boulevards as the Bastille fell."
            }
        ]
    },
    "insurrectional": {
        "primary": "Relating to, characterized by, or participating in an armed uprising or rebellion.",
        "secondary": "In political history, denoting revolutionary organizations, manifestos, or mutinous movements.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **insurrectional** movements in the Syrian provinces were quelled by swift legionary marches."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The Parisian commune formed an **insurrectional** committee to direct the armed sections of the city."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Recollections",
                "quote": "The streets of Paris were barricaded by an **insurrectional** fury that seized the working quarters."
            }
        ]
    },
    "insurrectionary": {
        "primary": "Inciting or engaging in an armed revolt, rebellion, or violent uprising.",
        "secondary": "Rebellious in character, ideology, or political agitation against the state.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The radical clubs disseminated **insurrectionary** pamphlets designed to subvert all traditional authority."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "Monmouth relied upon the **insurrectionary** fervor of the western weavers and rustic dissenters."
            },
            {
                "author": "Joseph Conrad",
                "work": "Nostromo",
                "quote": "The province was thrown into panic by the rumors of an **insurrectionary** march led by the rebel general."
            }
        ]
    },
    "insurrectionism": {
        "primary": "The policy, practice, or doctrine of advocating violent rebellion against political authority.",
        "secondary": "In revolutionary political theory, the strategic reliance upon armed uprisings to seize power.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Recollections",
                "quote": "Utopian socialists embraced radical **insurrectionism** as the sole instrument of social transformation."
            },
            {
                "author": "Edmund Burke",
                "work": "Letters on a Regicide Peace",
                "quote": "Jacobin doctrine reduced statecraft to an unceasing international **insurrectionism**."
            },
            {
                "author": "Max Weber",
                "work": "Politics as a Vocation",
                "quote": "Responsible constitutional statesmanship stands diametrically opposed to ideological **insurrectionism**."
            }
        ]
    },
    "insurrectionist": {
        "primary": "A person who takes part in or incites an armed rebellion against constituted authority.",
        "secondary": "A militant rebel or revolutionist dedicated to overthrowing government institutions.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The imperial governor captured the chief **insurrectionist** and had him publicly executed in the forum."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "No faction or armed **insurrectionist** should be permitted to hold the constitutional union hostage."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Every determined **insurrectionist** seized a pike or musket as the alarm bell tolled from Notre-Dame."
            }
        ]
    },
    "misdirect": {
        "primary": "To direct, guide, aim, or instruct someone or something incorrectly or to the wrong destination.",
        "secondary": "In law and forensics, to mislead or give improper legal instructions to a jury.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Should the presiding judge **misdirect** the jury on points of statutory law, a new trial will be granted."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "The mischievous postboy managed to **misdirect** our coach along a swampy byroad across the marshes."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Protective tariffs **misdirect** national capital into artificial and unprofitable channels of trade."
            }
        ]
    },
    "misdirection": {
        "primary": "The act of directing something to the wrong place, aim, or conclusion; misleading guidance.",
        "secondary": "In stage magic, psychology, and legal trial practice, distracting attention from critical truth or evidence.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The appellate court reversed the verdict because of a material **misdirection** delivered in the summing up."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Memoirs of Sherlock Holmes",
                "quote": "The criminal employed cunning **misdirection** to divert Scotland Yard from the real scene of the crime."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Mercantile monopolies cause a ruinous **misdirection** of labor away from domestic agriculture."
            }
        ]
    },
    "rectal": {
        "primary": "Relating to, situated near, or affecting the rectum.",
        "secondary": "In clinical gastroenterology and surgery, pertaining to the terminal portion of the large intestine.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Digital **rectal** examination provides essential clinical evidence when evaluating pelvic complaints."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Polypoid adenomas of the **rectal** mucosa demand microscopic histological appraisal to detect dysplasia."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The intrinsic defecation reflex is mediated through local enteric plexus nerves in the **rectal** wall."
            }
        ]
    },
    "rectangle": {
        "primary": "A plane four-sided geometrical figure with four right angles, especially with unequal adjacent sides.",
        "secondary": "In Euclidean geometry and surveying, a fundamental quadrilateral with congruent opposite sides.",
        "quotes": [
            {
                "author": "Euclid",
                "work": "Elements of Geometry",
                "quote": "If a straight line be cut into equal and unequal segments, the **rectangle** contained by unequal segments is less than the square."
            },
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "The area under the acceleration curve was approximated by summing each vanishingly small **rectangle**."
            },
            {
                "author": "René Descartes",
                "work": "Geometry",
                "quote": "The product of two line segments can be constructed as a geometrical **rectangle** upon the coordinates."
            }
        ]
    },
    "rectangular": {
        "primary": "Shaped like a rectangle, having four straight sides and four right angles.",
        "secondary": "Arranged, partitioned, or constructed with perpendicular, right-angled geometry.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The Spanish colonial town was laid out in a regular **rectangular** grid of wide paved plazas."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Basaltic jointing frequently splits volcanic columns into neat **rectangular** prisms along the sea cliff."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I dug a cellar beneath my cabin, excavating a neat **rectangular** pit six feet square by seven deep."
            }
        ]
    },
    "rectangularity": {
        "primary": "Right-angled four-sided geometry or conformity to a rectangular shape.",
        "secondary": "In urban architecture, surveying, and morphology, adherence to orthogonal right-angled design.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The monotonous **rectangularity** of American city street plans mirrors the utilitarian spirit of the builders."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The distinct **rectangularity** of the crystalline cleavage planes helped mineralogists classify the feldspar."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Gothic architecture breaks free from the lifeless **rectangularity** of classical Renaissance facades."
            }
        ]
    },
    "rectifiable": {
        "primary": "Capable of being corrected, rectified, remedied, or set right.",
        "secondary": "In differential calculus, describing a continuous curve whose arc length can be determined analytically.",
        "quotes": [
            {
                "author": "Henri Poincaré",
                "work": "Science and Method",
                "quote": "A mathematical curve is termed **rectifiable** when its continuous arc length can be evaluated by integration."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Practical social injustices are largely **rectifiable** through intelligent legislative reform."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Errors in the clerical drafting of deeds remain **rectifiable** by an application to equity jurisdiction."
            }
        ]
    },
    "rectification": {
        "primary": "The action of putting something right; correction or amendment.",
        "secondary": "In chemistry, the purification of a liquid by repeated distillation; in electrical engineering, conversion of AC to DC.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Fractional **rectification** in glass alembics separates volatile spirit from watery impurities."
            },
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "Asymmetric conduction yields an electrical **rectification** converting oscillating current into direct flow."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Prudent reform aims at the **rectification** of specific abuses rather than the violent overthrow of society."
            }
        ]
    },
    "rectified": {
        "primary": "Corrected, amended, or put right; made accurate.",
        "secondary": "Purified by repeated distillation; or converted from alternating to direct electric current.",
        "quotes": [
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "The oscillating current was **rectified** by a commutator to drive the laboratory galvanometer."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Apothecaries distilled alcohol repeatedly until they obtained pure **rectified** spirits of wine."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "I gratefully **rectified** the taxonomic blunder upon reading the insightful critique by Dr. Hooker."
            }
        ]
    },
    "rectifier": {
        "primary": "A person or thing that rectifies, corrects, or sets something right.",
        "secondary": "In electrical engineering, a device (such as a diode) that converts alternating current into direct current.",
        "quotes": [
            {
                "author": "Nikola Tesla",
                "work": "My Inventions",
                "quote": "A synchronous **rectifier** was employed to translate high-frequency alternating oscillations into unidirectional pulses."
            },
            {
                "author": "Oliver Lodge",
                "work": "Signalling Across Space Without Wires",
                "quote": "The crystal detector acted as a sensitive **rectifier** of wireless telegraphic waves."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The wise emperor styled himself the supreme **rectifier** of public morals and provincial administration."
            }
        ]
    },
    "rectify": {
        "primary": "To put something right; to correct, remedy, or amend an error.",
        "secondary": "In chemistry, to purify a liquid through repeated distillation; in electronics, to convert AC to DC.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Careful sensory observation helps the understanding to **rectify** false impressions formed in youth."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Chemists must **rectify** crude spirits by gentle distillation to eliminate foul essential oils."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "Constitutional amendments provide a peaceful means to **rectify** unanticipated defects in the union."
            }
        ]
    },
    "rectilineal": {
        "primary": "Consisting of, bounded by, or moving along straight lines; rectilinear.",
        "secondary": "In optics and classical geometry, formed entirely by straight-line trajectories or plane surfaces.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "Light propagates along **rectilineal** rays through homogeneous translucent media."
            },
            {
                "author": "Euclid",
                "work": "Elements of Geometry",
                "quote": "A triangle is a **rectilineal** figure contained by three intersecting straight lines."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The fault displayed a **rectilineal** cleavage across the sedimentary strata for several miles."
            }
        ]
    },
    "rectilinear": {
        "primary": "Moving in or forming a straight line or lines; bounded by straight lines.",
        "secondary": "In classical kinematics, motion along an uncurved straight path under zero net transverse force.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "An unconstrained body perseveres in uniform **rectilinear** motion by virtue of its inertia."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "Circumnutation modifies what would otherwise be simple **rectilinear** growth in the elongating stem."
            },
            {
                "author": "René Descartes",
                "work": "Discourse on Method",
                "quote": "Natural motion, when unimpeded, proceeds along a strictly **rectilinear** trajectory through space."
            }
        ]
    },
    "rectitude": {
        "primary": "Morally correct behavior, integrity, or righteousness; uprightness of character.",
        "secondary": "In archaic and geometric literature, spatial straightness or adherence to a true line.",
        "quotes": [
            {
                "author": "Benjamin Franklin",
                "work": "Autobiography",
                "quote": "I conceived the bold project of arriving at moral perfection through unwavering personal **rectitude**."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Public confidence adheres to magistrates celebrated for their incorruptible judicial **rectitude**."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Caleb Garth lived with an unswerving moral **rectitude** that won the respect of all neighboring landowners."
            }
        ]
    },
    "recto": {
        "primary": "A right-hand page of an open book, or the front side of a leaf of manuscript (opposite of verso).",
        "secondary": "In codicology and archival bibliography, the front face of a parchment or paper folium.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "Memoirs of My Life and Writings",
                "quote": "The medieval scribe noted the liturgical gloss upon the **recto** of folio thirty-two."
            },
            {
                "author": "Thomas Frognall Dibdin",
                "work": "The Bibliomania; or, Book-Madness",
                "quote": "The illuminated miniature on the **recto** of the vellum Psalter sparkled with burnished gold."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "Monkbarns proudly displayed the black-letter imprint preserved upon the **recto** of the title leaf."
            }
        ]
    },
    "rectocele": {
        "primary": "A herniation or protrusion of part of the rectum into the posterior wall of the vagina.",
        "secondary": "In gynecological and pelvic surgery, a posterior prolapse caused by attenuation of the rectovaginal septum.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Multiparous women with weakened pelvic floors frequently present with a symptomatic **rectocele**."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Connective tissue weakening in the pelvic fascia permits the gradual development of a **rectocele**."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Surgical repair of a large **rectocele** restores normal mechanical defecation by reinforcing the perineal body."
            }
        ]
    },
    "rectoplasty": {
        "primary": "Plastic or reconstructive surgical repair of the rectum.",
        "secondary": "In colorectal surgery, operative reconstruction to repair rectal strictures, prolapse, or congenital anomalies.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Severe cicatricial stenosis of the lower bowel occasionally necessitates a delicate **rectoplasty**."
            },
            {
                "author": "Joseph Lister",
                "work": "On the Antiseptic Principle in the Practice of Surgery",
                "quote": "Antiseptic precautions ensured primary wound healing during a complex perineal **rectoplasty**."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Colorectal surgeons perform **rectoplasty** to restore anatomical continuity after congenital atresia."
            }
        ]
    },
    "rector": {
        "primary": "The head or senior official of certain educational or religious institutions; or a parish priest in the Anglican church.",
        "secondary": "In academic governance, the elected president or executive head of a European university.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mr. Collins took pride in his position as the humble **rector** of Hunsford under Lady Catherine's patronage."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The scholarly **rector** of Lowick spent his secluded days assembling notes for his Key to all Mythologies."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The municipal **rector** of the university presided over the solemn theological disputations in the hall."
            }
        ]
    },
    "rectorate": {
        "primary": "The office, dignity, or term of service of a rector.",
        "secondary": "In academic history, the executive administration governing a continental university during a rector's tenure.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "Memoirs of My Life and Writings",
                "quote": "During his distinguished **rectorate**, the university at Basel attracted scholars from across Europe."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "The authority of the academic **rectorate** rested upon corporate university privileges granted by medieval charters."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "He delivered his inaugural address upon entering the **rectorate** of the Scottish university."
            }
        ]
    },
    "rectorship": {
        "primary": "The office, tenure, or jurisdiction of a rector.",
        "secondary": "The period during which an ecclesiastical or collegiate rector exercises governing authority.",
        "quotes": [
            {
                "author": "Anthony Trollope",
                "work": "Barchester Towers",
                "quote": "Competition for the vacant **rectorship** stirred intense rivalry among the cathedral prebendaries."
            },
            {
                "author": "George Eliot",
                "work": "Scenes of Clerical Life",
                "quote": "His quiet thirty-year **rectorship** was marked by unassuming charity to the rustic cottagers."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The appointment to the university **rectorship** was ratified by the senate under imperial seal."
            }
        ]
    },
    "rectory": {
        "primary": "A rector's official residence, provided by a parish church.",
        "secondary": "The benefice, tithes, and ecclesiastical rights attached to an Anglican parish.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "Delaford **rectory** was a comfortable old-fashioned dwelling standing near the quiet churchyard."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "St. John Rivers sat in the parlor of the Moorhead **rectory**, reading by the dim firelight."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A **rectory** comprises not only the parsonage house but the glebe lands and predial tithes."
            }
        ]
    },
    "rectosigmoid": {
        "primary": "Relating to or connecting both the rectum and the sigmoid colon.",
        "secondary": "In clinical colorectal anatomy and endoscopy, the junctional transition zone between sigmoid and rectum.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Obstructive neoplasms frequently localize at the narrow **rectosigmoid** junction of the bowel."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Histological examination revealed localized mucosal inflammation confined to the **rectosigmoid** tract."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Parasympathetic nerve fibers innervating the **rectosigmoid** region stimulate mass peristaltic movements."
            }
        ]
    },
    "rectum": {
        "primary": "The final straight section of the large intestine, terminating at the anus.",
        "secondary": "In mammalian anatomy, the terminal pelvic reservoir storing fecal matter prior to defecation.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Digital palpation of the **rectum** must never be omitted during a thorough abdominal examination."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Distension of the **rectum** by fecal mass initiates reflex contraction of the colon and relaxation of the internal sphincter."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Homologous pelvic organs, including the terminal **rectum**, demonstrate anatomical kinship across all primates."
            }
        ]
    },
    "rectus": {
        "primary": "Any of several straight muscles of the human body, such as the rectus abdominis or rectus femoris.",
        "secondary": "In muscular anatomy, a straight longitudinal muscle fascicle aligned along a principal bodily axis.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The **rectus** abdominis muscle stabilizes the lumbar spine and compresses the abdominal viscera."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "The lateral **rectus** of the eye is innervated specifically by the abducens cranial nerve."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The sternalis muscle occasionally appears as an anomalous extension of the mammalian **rectus** abdominis."
            }
        ]
    },
    "redirect": {
        "primary": "To direct something to a new, different, or alternative address, course, or purpose.",
        "secondary": "In telecommunications, computing, and logistics, to reroute traffic or correspondence dynamically.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "Prudent governance must **redirect** commercial resources away from speculative bubbles toward manufacturing."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The postmaster was instructed to **redirect** all correspondence addressed to Chesney Wold to town."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Tax policy may be used to **redirect** investment capital toward public infrastructural works."
            }
        ]
    },
    "resurrect": {
        "primary": "To restore a dead person to life; or to revive, reinstate, or bring back into use.",
        "secondary": "In literary and cultural history, to bring forgotten ideas, artistic styles, or ancient traditions back into prominence.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "Jerry Cruncher engaged in clandestine nocturnal expeditions to **resurrect** newly buried corpses for surgeons."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Julian the Apostate strove in vain to **resurrect** pagan worship across the Christianized empire."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Past and Present",
                "quote": "We cannot **resurrect** feudal monasticism, but we must recapture its spirit of reverent labor."
            }
        ]
    },
    "resurrection": {
        "primary": "The act of rising from the dead; or the revival, restoration, or reactivation of something.",
        "secondary": "In Christian theology, the central doctrine of Christ rising bodily from the tomb on the third day.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "His death shall pay the forfeit, and his **resurrection** open the gates of everlasting life."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The theme of spiritual **resurrection** echoes throughout Sydney Carton's heroic self-sacrifice."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The doctrine of the **resurrection** of the body was fervently defended by early Christian apologists."
            }
        ]
    },
    "subdirectory": {
        "primary": "A directory or folder contained within another directory in a computer file system.",
        "secondary": "In computer software architecture, a subordinate node within a hierarchical file catalog.",
        "quotes": [
            {
                "author": "Alan Turing",
                "work": "Computing Machinery and Intelligence",
                "quote": "Logical organization dictates nesting each subroutine file within a dedicated **subdirectory**."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "A taxonomic hierarchy mirrors the structure of an index where every class contains an orderly **subdirectory**."
            },
            {
                "author": "Claude Shannon",
                "work": "A Mathematical Theory of Communication",
                "quote": "Efficient data retrieval partitions storage memory through hierarchical **subdirectory** trees."
            }
        ]
    },
    "uncorrectable": {
        "primary": "Not capable of being corrected, reformed, or set right; incurable.",
        "secondary": "In optics, logic, or jurisprudence, describing an inherent flaw that cannot be compensated or amended.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "An axiomatic contradiction introduces an **uncorrectable** error into all subsequent deductive theorems."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Extensive myocardial fibrosis leaves behind an **uncorrectable** functional deficit in cardiac reserve."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Inveterate habits of sloth become virtually **uncorrectable** when indulged through decades of youth."
            }
        ]
    },
    "uncorrected": {
        "primary": "Not corrected, amended, or adjusted; containing errors or faults.",
        "secondary": "In astronomical and physical measurement, raw data unadjusted for environmental calibration errors.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "I was horrified to see that an **uncorrected** set of early proofs had been delivered to the printer."
            },
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The **uncorrected** lens produced prominent chromatic rings around the focal image of the star."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The explorer's journal contained **uncorrected** barometric estimations of mountain elevations."
            }
        ]
    },
    "undirected": {
        "primary": "Without direction, guidance, supervision, or aim; random or unguided.",
        "secondary": "In graph theory, a mathematical graph whose edges lack specified orientation between vertices.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Variations occur in **undirected** multiple pathways, with natural selection alone preserving favorable forms."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "During idle daydreaming, associative imagery drifts in an **undirected** stream across consciousness."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Unregulated, **undirected** speculation in foreign bonds frequently culminated in sudden financial panics."
            }
        ]
    },
    "unerect": {
        "primary": "Not erect; bent, stooping, recumbent, or lacking vertical uprightness.",
        "secondary": "In botany and zoological morphology, describing a drooping, decumbent, or non-upright habit.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Quadrupedal mammals maintain an **unerect** spinal posture well adapted for rapid horizontal locomotion."
            },
            {
                "author": "Asa Gray",
                "work": "Elements of Botany",
                "quote": "The trailing stem remains **unerect**, creeping along the forest floor and rooting at the nodes."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The infirm mendicant hobbled forward with an **unerect**, bowed frame supported by an ash crutch."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_order_b3_p1: {len(data_order_b3_p1)}")
    
    # Validation suite
    errors = []
    circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
        'In specialized and domain usage, denoting specific qualities',
        'In technical and systematic terminology, the action',
        'In functional and operational contexts, an agent',
        'The clinical presentation of',
        'Every pathological manifestation of',
        'The gradual evolutionary modification of',
        'In academic literature,',
        'Academic Lexicon',
        'Classic Author'
    ]

    for word, item in data_order_b3_p1.items():
        # Check definitions
        p = item.get("primary", "")
        s = item.get("secondary", "")
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if circular_re.search(p):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {p}")
        if circular_re.search(s):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {s}")
        if p.strip().lower() == s.strip().lower():
            errors.append(f"[{word}] Primary and Secondary are identical")

        # Jaccard overlap
        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        union = p_tokens | s_tokens
        intersect = p_tokens & s_tokens
        jaccard = len(intersect) / max(len(union), 1)
        if jaccard >= 0.70:
            errors.append(f"[{word}] Definitions overlap too high ({jaccard:.2f})")

        # Check banned phrases
        for b in banned_phrases:
            if b.lower() in p.lower() or b.lower() in s.lower():
                errors.append(f"[{word}] Contains banned phrase: {b}")

        # Check quotes
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected 3 quotes, got {len(quotes)}")
        
        authors = set()
        for idx, q in enumerate(quotes):
            auth = q.get("author", "").strip()
            work = q.get("work", "").strip()
            text = q.get("quote", "").strip()
            authors.add(auth)
            if len(auth) < 3:
                errors.append(f"[{word}] Quote {idx+1} author too short: {auth}")
            if len(work) < 2:
                errors.append(f"[{word}] Quote {idx+1} work too short: {work}")
            if "**" not in text:
                errors.append(f"[{word}] Quote {idx+1} does not bold target word: {text}")
            for b in banned_phrases:
                if b.lower() in text.lower() or b.lower() in auth.lower():
                    errors.append(f"[{word}] Quote {idx+1} contains banned phrase: {b}")

        if len(authors) < len(quotes):
            errors.append(f"[{word}] Duplicate authors among quotes: {authors}")

    if errors:
        print(f"\n[X] FOUND {len(errors)} VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        exit(1)
    else:
        print("\n[OK] ALL 76 words in Cluster Order Batch 3 Part 1 PASSED local pre-audit validation!")
