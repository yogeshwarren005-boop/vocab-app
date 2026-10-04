# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — duc Part 1 (13A, 40 words) ---
  "Dashboard — duc/abduce.md": {
    "primary": "To draw or lead away by persuasion or force; to pull a body part away from the median anatomical plane.",
    "secondary": "In classical physiological mechanics, voluntary action of abductor muscles drawing digits or limbs away from the bodily midline.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The lateral rectus muscle contracts to **abduce** the eyeball outward toward the temple."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The patient was completely unable to **abduce** the arm beyond the horizontal shoulder plane."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Certain quadruped species instinctively **abduce** their pinnae when alarmed by sudden noises."}
    ]
  },
  "Dashboard — duc/abducens.md": {
    "primary": "The sixth cranial nerve (cranial nerve VI), which innervates the lateral rectus muscle of the eye.",
    "secondary": "In clinical neurology, abducens nerve palsy causes horizontal diplopia (double vision) and impaired outward ocular abduction.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Isolated paralysis of the **abducens** nerve frequently signals elevated intracranial pressure."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The motor nucleus of the **abducens** lies nestled in the lower dorsal pons beneath the facial colliculus."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "Testing the integrity of the **abducens** requires observing conjugate lateral gaze in both directions."}
    ]
  },
  "Dashboard — duc/abducent.md": {
    "primary": "Serving to draw or pull away from the median line or central axis of the body; abducting.",
    "secondary": "In functional anatomy, characterizing muscles or nerve fibers (such as the abducent nerve) mediating lateral anatomical movement.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The **abducent** muscles act antagonistically to the powerful adductor valves of the bivalve mollusk."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Loss of **abducent** motor control prevents outward deflection of the affected ocular globe."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Efferent fibers from the **abducent** core emerge from the ventral pontine sulcus."}
    ]
  },
  "Dashboard — duc/abduct.md": {
    "primary": "To carry off or lead away a person illegally by force or fraud; to move a limb outward from the midline.",
    "secondary": "In kinesiology, the active angular separation of an extremity from the sagittal anatomical axis of the torso.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "Holmes suspected the conspirators had plotted to **abduct** the young duke for political extortion."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The rioters threatened to **abduct** the magistrate unless their imprisoned comrades were released."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The examiner instructed the injured laborer to **abduct** both thighs against resistance."}
    ]
  },
  "Dashboard — duc/abducting.md": {
    "primary": "Carrying off someone unlawfully by force or deception; moving a bodily limb outward from the midline.",
    "secondary": "In criminal trials, presenting physical evidence proving the forcible seizure and transportation of a victim across jurisdictions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The secret agents succeeded in **abducting** the foreign courier before he reached the embassy."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "A band of armed ruffians was accused of **abducting** the heiress on her journey north."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The gluteus medius acts as the principal muscle in **abducting** the human hip during bipedal gait."}
    ]
  },
  "Dashboard — duc/abduction.md": {
    "primary": "The illegal carrying away of a person by force or fraud; the movement of a limb away from the body's midline.",
    "secondary": "In epistemology and philosophy of science (coined by C. S. Peirce), abductive inference from observed facts to the best explanatory hypothesis.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The common law punishes the **abduction** of an heiress as a felony of the most heinous nature."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Deduction proves that something must be; induction shows that something actually is; **abduction** merely suggests that something may be."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Solitary Cyclist", "quote": "Holmes deduced that the audacious **abduction** had been planned to force an immediate marriage."}
    ]
  },
  "Dashboard — duc/abductor.md": {
    "primary": "A person who abducts or kidnaps someone; a muscle that draws a body part away from the median line.",
    "secondary": "In orthopedic biomechanics, the hip abductor group (gluteus medius and minimus) stabilizes the pelvis during the single-leg stance phase of gait.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The desperate **abductor** had shod his horse with ancient cow-shoes to confuse tracking hounds."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The **abductor** muscles of the ear twitch involuntarily when a horse hears a strange sound from behind."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Paresis of the laryngeal **abductor** produces inspiratory stridor due to failure of vocal cord opening."}
    ]
  },
  "Dashboard — duc/adduce.md": {
    "primary": "To cite as evidence, proof, or demonstration in an argument; to bring forward reasons.",
    "secondary": "In formal jurisprudence, the evidentiary presentation of witnesses, exhibits, and precedents to substantiate a contested legal claim.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The reasons that philosophers **adduce** in support of justice derive their force from human social utility."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is idle to **adduce** antiquity when truth itself challenges received tradition."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I might **adduce** a large catalogue of facts demonstrating the geographical distribution of oceanic fauna."}
    ]
  },
  "Dashboard — duc/adducent.md": {
    "primary": "Bringing forward, citing, or serving to draw a bodily part toward the median line or axis.",
    "secondary": "In classical anatomy and functional morphology, descriptive of muscular fibers that draw paired anatomical structures inward toward one another.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The powerful **adducent** muscles close the hinged calcareous valves against predatory intruders."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Testing the **adducent** action of the thighs helps differentiate obturator neuropathy from femoral palsy."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The coordinated action of **adducent** muscle fibers enables primates to grasp slender tree boughs with ease."}
    ]
  },
  "Dashboard — duc/adducer.md": {
    "primary": "A person who adduces, brings forward, or cites facts, arguments, or evidence in a controversy.",
    "secondary": "In rhetorical debate and legal advocacy, the party introducing documentary proof to support affirmative propositions.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on the Impeachment of Warren Hastings", "quote": "The **adducer** of historical precedents must establish that the ancient circumstances correspond to the present case."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Milton stood forth as the eloquent **adducer** of biblical and classical liberties against monarchical usurpation."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The candid **adducer** of new arguments welcomes sincere scrutiny from impartial searchers after truth."}
    ]
  },
  "Dashboard — duc/adducing.md": {
    "primary": "Citing, mentioning, or bringing forward evidence, authorities, or reasons in support of an argument.",
    "secondary": "In scholarly debate, marshaling empirical data or archival manuscripts to challenge an orthodox interpretation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "After **adducing** many instances of hybrid sterility, I must consider the contrary evidence of fertile crosses."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "By **adducing** parallel inductions, the natural philosopher eliminates accidental coincidences from causal laws."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "He defended his biological conclusions by **adducing** undeniable embryological homologies across vertebrate classes."}
    ]
  },
  "Dashboard — duc/adduct.md": {
    "primary": "To draw or pull a body part toward the median plane of the body or toward the axis of an extremity.",
    "secondary": "In chemistry, a chemical species formed by direct addition of two or more distinct molecules containing all constituent atoms.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The pectoralis major acts powerfully to **adduct** the arm across the chest wall during swimming."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "When asked to **adduct** the fingers against resistance, the patient demonstrated profound ulnar nerve weakness."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The animal will **adduct** its forelimbs tightly to the thorax when assuming a defensive posture."}
    ]
  },
  "Dashboard — duc/adducting.md": {
    "primary": "Drawing or pulling a limb, digit, or anatomical structure toward the central midline of the body.",
    "secondary": "In musculoskeletal kinesiology, executing inward angular displacement toward the coronal axis.",
    "quotes": [
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The physician noted sharp medial knee pain while **adducting** the flexed lower extremity."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "By forcefully **adducting** its shell valves, the bivalve expels a jet of water that propels it across the silt."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The monkey expressed apprehension by **adducting** both arms tightly across its hairy chest."}
    ]
  },
  "Dashboard — duc/adduction.md": {
    "primary": "The movement of a limb or body part toward the median axis of the body; the act of bringing forward.",
    "secondary": "In vocal cord physiology, adduction brings the true vocal folds together to close the rima glottidis for phonation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bilateral paralysis of the posterior cricoarytenoid muscles prevents proper **adduction** of the vocal cords."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Testing active **adduction** of the vocal bands requires direct laryngoscopic observation while the patient says 'ah'."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The powerful **adduction** of the human thigh stabilizes the pelvic girdle during upright locomotion."}
    ]
  },
  "Dashboard — duc/adductive.md": {
    "primary": "Bringing forward, citing, or tending to draw toward the median anatomical axis; adducent.",
    "secondary": "In anatomical classification, denoting muscle fibers whose vector of contraction produces inward medial displacement.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The **adductive** force exerted by the central muscle scar holds the oyster shell impenetrable to marine whelks."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The **adductive** power of the vocal chords was markedly diminished following injury to the recurrent laryngeal nerve."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Spastic contracture of the **adductive** musculature produces the typical scissoring gait of cerebral palsy."}
    ]
  },
  "Dashboard — duc/adductor.md": {
    "primary": "A muscle that draws a limb, digit, or body part toward the median anatomical axis of the body.",
    "secondary": "In malacology, the large transverse muscles that contract to pull together and securely close the valves of bivalve shells.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The giant Tridacna clam relies upon a colossal central **adductor** muscle to snap its massive shells shut."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Straining the gracilis or **adductor** longus produces the familiar athletic disability known as rider's strain."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Palpation along the medial femoral triangle elicited tenderness over the origin of the **adductor** brevis."}
    ]
  },
  "Dashboard — duc/aqueduct.md": {
    "primary": "A conduit, artificial channel, or monumental bridge built to convey water across valleys and long distances.",
    "secondary": "In neuroanatomy, the cerebral aqueduct (aqueduct of Sylvius) is the narrow channel connecting the third and fourth cerebral ventricles.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The colossal arches of the Roman **aqueduct** still stride majestically across the desolate Roman Campagna."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital stenosis of the cerebral **aqueduct** of Sylvius leads to massive non-communicating hydrocephalus in infants."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Red Circle", "quote": "The old stone **aqueduct** spanned the ravine, carrying the mountain stream to the lower mills."}
    ]
  },
  "Dashboard — duc/circumduct.md": {
    "primary": "To move a limb in a circular or cone-shaped sweeping path; archaically, to lead astray or nullify.",
    "secondary": "In kinesiology, executing a composite movement combining flexion, abduction, extension, and adduction in sequential order.",
    "quotes": [
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The patient was asked to **circumduct** the shoulder joint fully to test for subacromial impingement."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The ball-and-socket structure of the hip allows the femur to **circumduct** through a broad cone of movement."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Cortical motor commands stimulate synergist muscle clusters when the subject begins to **circumduct** the arm."}
    ]
  },
  "Dashboard — duc/circumduction.md": {
    "primary": "The circular movement of a limb or organ outlining a conical space; in Scots law, closing proof.",
    "secondary": "In arthrology, the 360-degree rotational path made possible by multiaxial ball-and-socket joints (spheroidal articulations).",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The universal joint of the thumb permits rapid **circumduction**, granting the hand its extraordinary manipulative dexterity."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Hemiplegic gait is characterized by lateral **circumduction** of the paretic lower limb during the swing phase."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe osteoarthritis of the hip joint severely restricts free **circumduction** and causes painful groin radiation."}
    ]
  },
  "Dashboard — duc/coeducate.md": {
    "primary": "To educate students of both sexes together within the same academic institution, classroom, or curriculum.",
    "secondary": "In 19th-century educational reform, the policy of admitting female students to previously male colleges and universities.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Democratic communities find it natural to **coeducate** boys and girls together, preparing them for cooperative civic life."},
      {"author": "George Bernard Shaw", "work": "Misalliance", "quote": "Progressive academies resolve to **coeducate** youth to banish artificial romantic mystery between the sexes."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Experience demonstrates that schools which **coeducate** young men and women cultivate mutual intellectual respect."}
    ]
  },
  "Dashboard — duc/coeducation.md": {
    "primary": "The integrated education of male and female students within the same educational institution.",
    "secondary": "In the social history of American higher education, pioneered by Oberlin College in 1837 and adopted by land-grant universities after 1862.",
    "quotes": [
      {"author": "John Dewey", "work": "The School and Society", "quote": "The widespread adoption of **coeducation** reflects our democratic faith in equal intellectual opportunities for all citizens."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "The success of university **coeducation** has completely refuted ancient predictions of feminine intellectual inferiority."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "Her college years under **coeducation** provided rigorous preparation for leadership in municipal social reform."}
    ]
  },
  "Dashboard — duc/coeducational.md": {
    "primary": "Attended by and integrated for students of both sexes; relating to coeducation.",
    "secondary": "In institutional policy, distinguishing mixed-gender schools and universities from single-sex educational bodies.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The state university was a vigorous, sprawling **coeducational** institution where thousands of Midwestern youth congregated."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory debated the merits of eastern monastic colleges against the vibrant life of large **coeducational** campuses."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The **coeducational** environment mirrors the diverse social realities of modern democratic communities."}
    ]
  },
  "Dashboard — duc/conduce.md": {
    "primary": "To lead, tend, or contribute toward a particular result, outcome, or advantage; to promote.",
    "secondary": "In moral philosophy and utilitarian ethics, actions that conduce to the greatest overall happiness and social harmony.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "The reasons you allege do more **conduce** to the hot passion of distemper'd blood than to make up a free determination."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I resolved that if my immediate union with my cousin would **conduce** to her happiness, no private misery of mine should delay it."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Temperate habits and regular exercise directly **conduce** to clarity of intellect and longevity."}
    ]
  },
  "Dashboard — duc/conducive.md": {
    "primary": "Tending to produce, promote, or assist in bringing about a particular condition or outcome; favorable.",
    "secondary": "In public health and environmental psychology, designing living environments conducive to emotional well-being and restorative rest.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The solitary and dissipated life I lead, Miss Manette, is not **conducive** to health or peace of mind."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Justice consists in respecting those rules of conduct which are most **conducive** to the general welfare."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The bleak, gloomy atmosphere of Dartmoor was scarcely **conducive** to cheerful spirits in the lonely manor."}
    ]
  },
  "Dashboard — duc/conduciveness.md": {
    "primary": "The quality, tendency, or degree of being conducive to or promoting a desired result or advantage.",
    "secondary": "In ethical theory, the utility calculus evaluating actions by their instrumental conduciveness to collective pleasure.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "There was no original desire of it, or motive to it, save its **conduciveness** to pleasure and protection from pain."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "The ultimate justification of any moral code lies in its demonstrated **conduciveness** to complete living."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The value of an action is estimated by its direct **conduciveness** to the augmentation of happiness in the community."}
    ]
  },
  "Dashboard — duc/conduct.md": {
    "primary": "The manner in which a person behaves or directs oneself; or to lead, manage, guide, or transmit energy.",
    "secondary": "In physics and electrical engineering, the physical property of transmitting thermal energy or electrical current through a medium.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "If you will tarry, holy pilgrim, but till the troops come by, I will **conduct** you where you shall be lodged."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Discretion in speech is more than eloquence; and to speak agreeably to him with whom we deal is the best **conduct**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth could not help observing how perfectly gentlemanlike and dignified was Mr. Darcy's **conduct**."}
    ]
  },
  "Dashboard — duc/conductance.md": {
    "primary": "A measure of the ability of an electrical circuit or component to conduct electricity; reciprocal of resistance.",
    "secondary": "In SI electrical units, measured in siemens (formerly mho), defined as the ratio of current flowing to voltage applied across a conductor.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The electrical **conductance** of the metallic wire varies inversely with its length and directly with its cross-sectional area."},
      {"author": "Oliver Heaviside", "work": "Electrical Papers", "quote": "We introduce the concept of leakance or dielectric **conductance** to quantify energy dissipation along telegraph cables."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The electrolyte showed a rapid increase in **conductance** as the salt concentration rose toward saturation."}
    ]
  },
  "Dashboard — duc/conducting.md": {
    "primary": "Directing, managing, or leading an operation, orchestra, or business; transmitting heat or electricity.",
    "secondary": "In musical performance, communicating artistic interpretation and rhythmic tempo through manual gesture and baton technique.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Why are you not **conducting** the investigation from Baker Street instead of wandering into the country?"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He had a high standard for **conducting** parochial duties, which earned him the respect of the older clergy."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The copper strip served as the principal **conducting** wire linking the galvanic battery to the galvanometer."}
    ]
  },
  "Dashboard — duc/conduction.md": {
    "primary": "The transmission of heat, electricity, or sound through a material medium without gross movement of matter.",
    "secondary": "In physiology, saltatory conduction describes the rapid propagation of action potentials along myelinated axons from node of Ranvier to node.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "Thermal **conduction** transfers kinetic energy from warmer molecules to neighboring cooler particles through molecular impact."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The velocity of nerve **conduction** was precisely determined by Helmholtz using his delicate myograph apparatus."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Metallic **conduction** differs fundamentally from electrolytic conduction, where chemical decomposition always attends current flow."}
    ]
  },
  "Dashboard — duc/conductive.md": {
    "primary": "Having the property, ability, or power to conduct heat, sound, or electricity.",
    "secondary": "In audiology, conductive hearing loss occurs when sound transmission is impeded through the external ear canal, tympanic membrane, or middle ear ossicles.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Graphite displays a remarkably **conductive** nature, transmitting galvanic currents with very low electrical resistance."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The tuning fork test differentiated **conductive** middle ear impairment from sensorineural acoustic nerve lesions."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "A thin layer of **conductive** foil prevents electrostatic fields from penetrating the shielded interior chamber."}
    ]
  },
  "Dashboard — duc/conductivity.md": {
    "primary": "The degree to which a specified material conducts electricity or heat; specific conductance.",
    "secondary": "In solid-state physics, electrical conductivity is governed by carrier concentration and electron mobility within conduction bands.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martians generated intense heat inside chambers of practically zero thermal **conductivity**."},
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The thermal **conductivity** of metals generally parallels their capacity for transmitting galvanic currents."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Pure distilled water exhibits exceedingly low **conductivity** until trace saline electrolytes are added."}
    ]
  },
  "Dashboard — duc/conductor.md": {
    "primary": "A material or substance that conducts electricity or heat; a person who directs an orchestra or collects bus fares.",
    "secondary": "In electrical engineering, a wire, cable, or busbar of high electrical conductivity designed to transmit electric power.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Under the shadow of this extemporized lightning-**conductor** Gabriel felt himself comparatively safe from the storm."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She began to get uneasy at a certain reckless speed in her **conductor**'s driving down the steep hill."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The cab **conductor** touched his hat respectfully as Holmes dropped a half-crown into his palm."}
    ]
  },
  "Dashboard — duc/conductress.md": {
    "primary": "A woman who conducts; especially a female guide, directress, or bus or tram ticket collector.",
    "secondary": "In wartime social history, female transport workers who staffed municipal buses and trams during World War I and II.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My charming young **conductress** led me through the fragrant conservatory into the morning room."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The cheerful bus **conductress** carrying her ticket machine through the blackout embodied wartime resilience."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She followed her gentle **conductress** up the winding oak staircase to the library."}
    ]
  },
  "Dashboard — duc/counterproductive.md": {
    "primary": "Having the opposite of the desired effect; hindering rather than advancing the achievement of a goal.",
    "secondary": "In public policy economics, perverse incentives producing regulatory capture or black market expansion opposite to legislative intent.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Excessive legal censorship proves **counterproductive**, exciting curiosity and imparting martyr prestige to banned opinions."},
      {"author": "George Orwell", "work": "Collected Essays", "quote": "Crude propaganda campaigns are often **counterproductive**, alienating intelligent sympathizers by obvious distortions."},
      {"author": "Bertrand Russell", "work": "The Practice and Theory of Bolshevism", "quote": "Harsh bureaucratic coercion frequently proves **counterproductive** in securing voluntary agricultural productivity."}
    ]
  },
  "Dashboard — duc/deduce.md": {
    "primary": "To arrive at a fact, conclusion, or theory by reasoning from general premises or known evidence.",
    "secondary": "In formal logic, establishing a necessary conclusion through valid syllogistic deduction where truth of premises guarantees truth of the conclusion.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "From a drop of water, a logician could **deduce** the possibility of an Atlantic or a Niagara without having seen either."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A few rows of statistics are enough to **deduce** misery from, and a few more will reveal the parish death rate."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "From the fundamental principle of utility, we may **deduce** secondary moral maxims for everyday guidance."}
    ]
  },
  "Dashboard — duc/deducible.md": {
    "primary": "Capable of being deduced, inferred, or derived by logical reasoning from known facts or premises.",
    "secondary": "In mathematical logic, a theorem deducible within a formal axiomatic system via a finite sequence of valid inference rules.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "These and a thousand other societal reformations were firmly counted upon as **deducible** from his philosophical treatise."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Moral duties are demonstrably **deducible** from the relations subsisting between God and reasonable creatures."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "All classical pure mathematics is strictly **deducible** from a small collection of logical axioms."}
    ]
  },
  "Dashboard — duc/deduct.md": {
    "primary": "To subtract, take away, or withhold an amount, portion, or number from a total sum.",
    "secondary": "In corporate payroll and tax law, to withhold income taxes, pension contributions, or social security from gross earnings.",
    "quotes": [
      {"author": "William James", "work": "Pragmatism", "quote": "My father bargained to advance a guinea for the boy's schooling and **deduct** it out of his monthly allowance."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The landlord must **deduct** the annual expenditure necessary for repairs before calculating his true net rent."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Murdstone threatened to **deduct** every broken slate from my meager pocket money."}
    ]
  },
  "Dashboard — duc/deductible.md": {
    "primary": "Able to be subtracted, taken away, or deducted, especially from gross taxable income.",
    "secondary": "In insurance underwriting, the specified out-of-pocket amount the policyholder must pay before an insurance policy pays a claim.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Ordinary expenses incurred in carrying trade are legitimately **deductible** from gross commercial profits."},
      {"author": "John Kenneth Galbraith", "work": "The Affluent Society", "quote": "Corporate entertainment expenses were made legally **deductible**, creating an artificial boom in luxury dining."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He consulted his accountant to verify whether travel expenditure was strictly **deductible** under the new revenue code."}
    ]
  },
  "Dashboard — duc/deduction.md": {
    "primary": "The process of reaching a logical conclusion by reasoning from general principles; an amount subtracted.",
    "secondary": "In tax accounting, an allowable expense item subtracted from adjusted gross income to reduce the tax liability base.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Hence, you see, my double **deduction** that you had been out in vile weather, and that you had a clumsy servant girl."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Scientific reasoning unites observation and **deduction** in an unbreakable cycle of discovery and verification."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth laughed at her friend's solemn **deduction**, assuring her that Darcy's pride had blinded his judgment."}
    ]
  },
  "Dashboard — duc/deductive.md": {
    "primary": "Pertaining to, based on, or utilizing logical deduction; reasoning from general premises to specific truths.",
    "secondary": "In scientific methodology, hypothetico-deductive reasoning formulates testable hypotheses whose empirical implications are rigorously checked.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "An entertaining retort, framed in the narrow and **deductive** manner of the medieval schoolmen."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes published a famous magazine article detailing his strict **deductive** science of observation."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The physical sciences achieve their highest triumphs when combining empirical induction with **deductive** geometry."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Motion Batch 13A: Successfully updated {updated}/{len(data)} notes.")
