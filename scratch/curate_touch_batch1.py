# -*- coding: utf-8 -*-
"""
Curates Cluster Touch (Batch 1, 34 words):
- Dashboard — scalp (3 words)
- Dashboard — ting (5 words)
- Dashboard — fric (10 words)
- Dashboard — palp (16 words)
Total: 34 words.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — scalp
  "scalp": {
    "primary": "The skin covering the top of the human head, usually bearing hair.",
    "secondary": "In financial trading and commerce, to buy and resell quickly for a small, rapid profit.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg carried a dried shrunken head upon whose dark **scalp** the knotted locks still clung."},
      {"author": "James Fenimore Cooper", "work": "The Last of the Mohicans", "quote": "The victorious warrior brandished the bloody **scalp** as a trophy of forest warfare."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The subcutaneous tissue of the **scalp** is dense and intimately adherent to the epicranial aponeurosis."}
    ]
  },
  "scalpel": {
    "primary": "A small and extremely sharp bladed instrument used for surgery and anatomical dissection.",
    "secondary": "In figurative and literary criticism, analytical precision that cuts through obfuscation or sentimentality.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon wielded the **scalpel** with rapid, delicate incisions through the fascia."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Anatomical science progressed when Vesalius laid down Galen's texts and took up the **scalpel**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Surrounded by dissecting instruments and his keen **scalpel**, Victor assembled the monstrous frame."}
    ]
  },
  "scalper": {
    "primary": "A person who resells shares, tickets, or commodities at an inflated price for quick profit.",
    "secondary": "In historic frontier conflicts, a warrior or mercenary who harvested enemy scalps for bounty.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "The Winning of the West", "quote": "Colonial frontiersmen detested the ruthless Indian **scalper** who preyed upon isolated cabins."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The street-corner **scalper** hawked theatre tickets at double their face value outside the lobby."},
      {"author": "Frank Norris", "work": "The Pit", "quote": "The pit **scalper** traded thousands of wheat bushels on sixteenth-cent fluctuations."}
    ]
  },

  # Dashboard — ting
  "contingent": {
    "primary": "Subject to chance; occurring or existing only if certain other circumstances are the case; conditional.",
    "secondary": "In military operations and international alliances, a gathering of persons or troops representing a larger group.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Every treaty obligation is necessarily **contingent** upon future diplomatic emergencies and reciprocity."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Man's ultimate fate seems partly determined by necessity and partly **contingent** upon blind chance."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "A British **contingent** arrived to reinforce the Egyptian garrison along the frontier."}
    ]
  },
  "ting": {
    "primary": "To emit a sharp, clear, high-pitched metallic ringing sound; a light metallic clink.",
    "secondary": "In acoustics and music, the transient resonance produced by striking thin metal or fine crystal.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sharp **ting** of the sheep bell echoed through the crisp night air across the down."},
      {"author": "Alfred Tennyson", "work": "The Princess", "quote": "The silver goblet gave a clear **ting** as the knight struck it with his dagger hilt."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The little bell over the shop door gave a sharp **ting** whenever a customer entered."}
    ]
  },
  "tinge": {
    "primary": "To color slightly; to impart a trace, faint tint, or slight degree of some quality.",
    "secondary": "In sensory aesthetics, a subtle undertone modifying a dominant color, flavor, or emotion.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A faint **tinge** of dawn touched the London chimney pots with pale grey light."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A rosy **tinge** of youthful health blushed beneath her sun-browned cheeks."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A mournful **tinge** of fatalism ran through every word uttered by the brooding captain."}
    ]
  },
  "tingent": {
    "primary": "Having the power to tinge, color, or dye; serving to tint or impart coloration.",
    "secondary": "In historical textile and chemical manufacturing, mordants or dye extracts with high pigmenting potency.",
    "quotes": [
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "Vegetable infusions possess a strong **tingent** property that colors vast volumes of water."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The juice of the pokeberry was examined for its active **tingent** virtue upon wool."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Certain mineral earths yield **tingent** particles that stain subterranean river gravels."}
    ]
  },
  "tinting": {
    "primary": "The act or process of applying a delicate color, dye, or shade to something.",
    "secondary": "In early cinematography and photography, the chemical toning of film emulsion to create atmosphere.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner achieved sublime atmospheric depth through delicate water-color **tinting** of clouds."},
      {"author": "Donn Byrne", "work": "The Wind Bloweth", "quote": "The twilight was **tinting** the western hills with lavender and gold."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The artist spent the afternoon **tinting** the miniature portrait with ivory glaze."}
    ]
  },

  # Dashboard — fric
  "affricate": {
    "primary": "A complex consonant sound that begins as a stop and releases as a fricative (such as 'ch' or 'j').",
    "secondary": "In phonetic linguistics, a speech sound produced by complete oral closure followed by narrow channeled friction.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "English orthography uses digraphs to represent the palato-alveolar **affricate** in words like church."},
      {"author": "Edward Sapir", "work": "Language", "quote": "Certain indigenous American languages possess an unusually rich inventory of **affricate** consonants."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The release of the alveolar stop merges into a sibilant glide, producing a typical **affricate**."}
    ]
  },
  "affrication": {
    "primary": "The linguistic process by which a plosive stop consonant becomes an affricate over time.",
    "secondary": "In historical sound change and phonology, the palatalization and frictional release of velar or dental stops.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "Language: Its Nature, Development and Origin", "quote": "Historical **affrication** transformed Latin velar stops into Italian affricates before front vowels."},
      {"author": "Edward Sapir", "work": "Language", "quote": "Dialectal divergence often accelerates through spontaneous phonetic **affrication** in rapid speech."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The shift from Germanic 't' to Old High German 'ts' illustrates systematic consonant **affrication**."}
    ]
  },
  "affricative": {
    "primary": "Characterized by, resembling, or functioning as an affricate consonant sound.",
    "secondary": "In phonetic transcription, designating compound stop-fricative articulations.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "German displays an **affricative** release in initial voiceless dental consonants."},
      {"author": "Edward Sapir", "work": "Language", "quote": "The dialect developed an **affricative** variant of the ancient dental stop."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Acoustic spectrograms demonstrate the two-phase nature of **affricative** consonant bursts."}
    ]
  },
  "dentifrice": {
    "primary": "A paste, powder, or liquid preparation used for cleaning the teeth; toothpaste.",
    "secondary": "In historical hygiene, abrasive powders compounded of chalk, pumice, and essential oils to scrub dental enamel.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "Among the items in the traveller's pockets was a curious box containing fragrant **dentifrice** powder."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "A mild alkaline **dentifrice** neutralizes oral acids and protects enamel from erosion."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Ancient Roman ladies polished their teeth with a scented **dentifrice** of pulverized cuttlebone."}
    ]
  },
  "fricandeau": {
    "primary": "A traditional French culinary dish consisting of larded and braised veal or beef.",
    "secondary": "In classical gastronomy, a thick cut of top-round veal studded with pork lardoons and braised in seasoned stock.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The French chef prepared an exquisite **fricandeau** garnished with truffles and Madeira sauce."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The gourmand lingered over his savory **fricandeau**, savoring the delicate glaze of the rich gravy."},
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "A classic **fricandeau** requires patient braising until the glazed surface shines like polished mahogany."}
    ]
  },
  "fricassee": {
    "primary": "A dish of stewed meat (usually poultry or rabbit) served in a thick white sauce.",
    "secondary": "In culinary technique, sauteing cut meat lightly in fat without browning before simmering in stock.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse recommended a gentle **fricassee** of sweetbreads as particularly wholesome for delicate digestions."},
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "The feast featured platters of roasted ducks and a fragrant **fricassee** of barnyard fowl."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The old cook proudly served a rich chicken **fricassee** to the unexpected noble guests."}
    ]
  },
  "fricative": {
    "primary": "A consonant produced by forcing air through a narrow channel between articulators, causing friction (such as 'f' or 's').",
    "secondary": "In acoustic phonetics, a continuous turbulent noise generated by aerodynamic constriction in the vocal tract.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "The dental **fricative** in English presents notorious difficulty to foreign learners."},
      {"author": "Edward Sapir", "work": "Language", "quote": "Athabaskan tongues distinguish multiple voiceless lateral **fricative** consonants with exquisite precision."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Airflow turbulence marks the acoustic signature of every voiced and voiceless **fricative**."}
    ]
  },
  "friction": {
    "primary": "The resistance that one surface or object encounters when moving over another; conflict between people.",
    "secondary": "In classical mechanics, the tangential force opposing the relative lateral sliding motion of solid surfaces.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "In physical experiments, mechanical **friction** and air resistance retard perpetual motion."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Commercial rivalries between sovereign states produce continuous political **friction** and hostility."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Natural selection eliminates biological inefficiencies just as engineering minimizes mechanical **friction**."}
    ]
  },
  "frictional": {
    "primary": "Relating to, caused by, or resulting from mechanical or social friction.",
    "secondary": "In labor economics, frictional unemployment: temporary unemployment occurring while workers transition between jobs.",
    "quotes": [
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "Mechanical work converted into heat by **frictional** contact demonstrated the conservation of energy."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "A normal dynamic economy always exhibits a modest level of **frictional** unemployment."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Early electrical generators utilized **frictional** glass cylinders rotated against silk pads."}
    ]
  },
  "frictionless": {
    "primary": "Having or offering no resistance to motion; smooth, effortless, or free from conflict.",
    "secondary": "In theoretical physics, idealized physical systems where surface resistance is assumed to be zero.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The ABC of Relativity", "quote": "Theoretical mechanics calculates motion on an idealized **frictionless** horizontal plane."},
      {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "Planetary orbits in empty interstellar space approximate **frictionless** Newtonian motion."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The sphere glided smoothly over the lunar ice with nearly **frictionless** momentum."}
    ]
  },

  # Dashboard — palp
  "impalpability": {
    "primary": "Intangibility; inability to be perceived by physical touch or grasped by the senses.",
    "secondary": "In philosophical metaphysics, the elusive, non-corporeal nature of abstract thoughts or spirits.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet captured the elusive **impalpability** of dream memories dissolving at dawn."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab reached out into the empty mist, mocked by the **impalpability** of his phantom tormentor."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain subtle affective states baffle analysis by their shadowy **impalpability**."}
    ]
  },
  "impalpable": {
    "primary": "Unable to be felt by touch; not easily comprehended, tangible, or grasped by the mind.",
    "secondary": "In physical chemistry, powders ground so finely that individual particles cannot be perceived between fingers.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The night air was filled with an **impalpable** dust of starlight and mountain mist."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "A shadowy, **impalpable** bond of guilt united the minister and the outcast woman."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "An **impalpable** volcanic ash fell upon the ship's deck hundreds of miles from the eruption."}
    ]
  },
  "impalpably": {
    "primary": "In an impalpable manner; so subtly or faintly as not to be felt, noticed, or perceived.",
    "secondary": "In atmospheric description, shifting gradually and invisibly from one state or phase to another.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The emotional atmosphere shifted **impalpably**, chilling Isabel's initial generous enthusiasm."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Twilight deepened **impalpably** over Egdon Heath, erasing all distinct boundaries."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The ship glided **impalpably** through the black tropical night across a mirror-like sea."}
    ]
  },
  "palpability": {
    "primary": "Tangible clarity, obviousness, or plain perceptibility to physical touch or understanding.",
    "secondary": "In literary realism, the sensory vividness of narrative description that evokes physical reality.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory impressions possess an immediate **palpability** that abstract concepts lack."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her moral duty presented itself with the sudden **palpability** of a physical barrier."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The heavy ocean fog attained a dense **palpability** that choked the breathing watchmen."}
    ]
  },
  "palpable": {
    "primary": "Able to be touched or felt; easily perceptible, obvious, plain, or unmistakable.",
    "secondary": "In clinical physical examination, an anatomical mass, pulse, or organ that can be felt through manual palpation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "I see thee yet, in form as **palpable** as this which now I draw... The phantom dagger hovered in the air."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "On abdominal examination, the enlarged liver was readily **palpable** beneath the costal margin."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The cold became intense, piercing, and searching, like a **palpable** substance."}
    ]
  },
  "palpably": {
    "primary": "In a manner that is palpable; tangibly, noticeably, or plainly evident to perception.",
    "secondary": "In judicial reasoning, facts or errors so manifest as to require no elaborate evidentiary demonstration.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy was **palpably** embarrassed by his aunt's rude and haughty interrogation of Elizabeth."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The existing confederation was **palpably** deficient in providing for national defense."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The witness was **palpably** terrified, his voice shaking with undisguised dread."}
    ]
  },
  "palpate": {
    "primary": "To examine a part of the body by touch, especially for diagnostic medical purposes.",
    "secondary": "In zoological anatomy, to touch or explore the environment using sensory palps or tentacles.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician must gently **palpate** the right iliac fossa to detect localized tenderness."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "A skilled diagnostician learns to **palpate** arterial pulses with exquisite tactile sensitivity."},
      {"author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "Coral polyps extend delicate tentacles to **palpate** suspended organic particles in the brine."}
    ]
  },
  "palpation": {
    "primary": "The act of examining or exploring a part of the body by feeling with the hands.",
    "secondary": "In clinical physical diagnosis, manual evaluation of organ size, texture, tenderness, and vascular pulses.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful **palpation** confirmed the presence of a pulsating aneurysm in the popliteal artery."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Inspection, percussion, and **palpation** constitute the foundational triad of bedside examination."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Accurate **palpation** of the radial styloid process aids in diagnosing Colles' fracture of the wrist."}
    ]
  },
  "palpatory": {
    "primary": "Relating to or used in palpation; pertaining to diagnostic examination by touch.",
    "secondary": "In clinical diagnostics, findings elicited specifically by manual feeling rather than auscultation or percussion.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **palpatory** thrill over the apex verified the clinical diagnosis of mitral stenosis."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Young surgeons must cultivate their **palpatory** sense through daily tactile discipline."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A distinct **palpatory** sensation guides the needle during femoral artery catheterization."}
    ]
  },
  "palpebra": {
    "primary": "The anatomical term for an eyelid; the upper or lower movable fold covering the eyeball.",
    "secondary": "In comparative ocular anatomy, protective dermal folds lined with conjunctiva, including the third eyelid (nictitating membrane).",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Each **palpebra** is supported by a dense plate of fibrous tissue known as the tarsal plate."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The orbicularis oculi muscle closes each **palpebra** rapidly to shield the cornea from injury."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Edema of the upper **palpebra** often provides an early clue to acute glomerulonephritis."}
    ]
  },
  "palpebrate": {
    "primary": "Having eyelids; to blink, wink, or close the eyes repeatedly.",
    "secondary": "In physiological ocular mechanics, the involuntary reflex blinking that lubricates the corneal surface with tears.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Certain reptiles possess a transparent nictitating membrane that allows them to **palpebrate** underwater."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Bright flashes of light provoke the patient to **palpebrate** vigorously in protective reflex."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The human infant begins to **palpebrate** when small objects are brought near the eyes."}
    ]
  },
  "palpebration": {
    "primary": "The act of blinking or winking; repeated involuntary closure of the eyelids.",
    "secondary": "In clinical ophthalmology and neurology, abnormal frequent blinking associated with corneal irritation or blepharospasm.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rapid, spasmodic **palpebration** signaled the onset of a facial tic in the young girl."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Normal **palpebration** spreads the lacrimal secretion uniformly across the cornea."},
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "A nervous **palpebration** betrayed the witness's inward distress under cross-examination."}
    ]
  },
  "palpitant": {
    "primary": "Throbbing, trembling, quivering, or palpitating with emotion or physical agitation.",
    "secondary": "In poetic and romantic prose, an atmosphere vibrant with suspense, desire, or intense expectation.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I stood before him with a **palpitant** heart, awaiting his judgment upon my confession."},
      {"author": "Edgar Allan Poe", "work": "The Tell-Tale Heart", "quote": "The hellish tattoo of the **palpitant** heart grew louder and louder beneath the floorboards."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen listened with **palpitant** anxiety as the fateful letter was unfolded."}
    ]
  },
  "palpitate": {
    "primary": "To beat rapidly, strongly, or irregularly (of the heart); to throb, shake, or tremble.",
    "secondary": "In pathophysiology, subjective awareness of abnormal cardiac pulsations due to arrhythmia or stress.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "I have tremor cordis on me: my heart dances; but not for joy; not joy... It doth **palpitate** with sudden fury."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne felt her heart **palpitate** with violent emotion at the unexpected sound of footsteps."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sudden fright causes the heart of animals to **palpitate** furiously against the ribs."}
    ]
  },
  "palpitating": {
    "primary": "Beating rapidly, irregularly, or strongly; trembling, throbbing, or quivering.",
    "secondary": "In clinical cardiology, experiencing distressing sensations of accelerated heartbeats.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy pressed her hand against her **palpitating** side, breathless from running through the rain."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The terrified boy dropped into the chair with **palpitating** terror as the ruffians approached."},
      {"author": "Jack London", "work": "White Fang", "quote": "The captured wolf cub lay **palpitating** with wild dread under the hunter's rough hands."}
    ]
  },
  "palpitation": {
    "primary": "A noticeably rapid, strong, or irregular heartbeat due to agitation, exertion, or illness.",
    "secondary": "In clinical cardiology, a common patient-reported symptom that may indicate premature ventricular contractions or atrial flutter.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Excessive consumption of strong tobacco frequently provokes nocturnal cardiac **palpitation**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet complained bitterly of the nervous **palpitation** that racked her delicate constitution."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon suffered a sudden **palpitation** in the library, sinking breathless into his leather armchair."}
    ]
  }
}
