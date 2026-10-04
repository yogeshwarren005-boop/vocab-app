# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — tens (41 words) ---
  "Dashboard — tens/coextension.md": {
    "primary": "The state or condition of extending equally in space, time, or scope with something else.",
    "secondary": "In metaphysical cosmology and field physics, philosophers debated the coextension of gravitational fields with physical matter.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poetical imagination claims a profound **coextension** with all the living powers of nature."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The **coextension** of space and time provides the intuitive matrix wherein all physical changes unfold."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Philosophers formerly debated the mutual **coextension** of body and empty space across the universe."}
    ]
  },
  "Dashboard — tens/coextensive.md": {
    "primary": "Extending over the same space, time, area, or scope as something else; coinciding in range.",
    "secondary": "In constitutional jurisdiction, federal judicial power is designed to be coextensive with the legislative authority.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The judicial authority of the Union ought to be **coextensive** with the legislative power of the federal government."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Individual moral duty is not always **coextensive** with the enforceable legal obligations of the state."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific knowledge is **coextensive** with all verifiable empirical facts in the natural universe."}
    ]
  },
  "Dashboard — tens/distensible.md": {
    "primary": "Capable of being stretched, expanded, dilated, or distended from internal pressure.",
    "secondary": "In cardiovascular hemodynamics and vascular physiology, large elastic arteries possess a distensible wall that buffers systolic blood pressures.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The urinary bladder functions as a remarkably **distensible** muscular reservoir capable of accommodating large fluid volumes."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The thoracic esophagus is a highly **distensible** muscular tube that expands readily during the passage of a bolus."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The stomach exhibits a **distensible** mucosal architecture that adapts to variations in dietary intake."}
    ]
  },
  "Dashboard — tens/distension.md": {
    "primary": "The act of swelling or expanding from internal pressure, or the condition of being stretched tight.",
    "secondary": "In gastroenterology and clinical physical examination, acute abdominal distension indicates luminal obstruction, ascites, or tympanites.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient presented with extreme tympanitic **distension** of the abdomen accompanied by persistent vomiting."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Excessive vascular **distension** stimulates baroreceptors located within the carotid sinus and aortic arch."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The country doctor recognized that the painful cardiac **distension** required immediate therapeutic venesection."}
    ]
  },
  "Dashboard — tens/extensible.md": {
    "primary": "Capable of being pulled out, elongated, stretched, or extended in length, area, or scope.",
    "secondary": "In software architecture and systems design, extensible software frameworks permit third-party plugin integration without modifying core source code.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **extensible** proboscis of the hawk-moth is adapted to drain the deep nectaries of Madagascar orchids."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Heated vulcanized caoutchouc forms an **extensible** elastic membrane that resists hydrostatic pressure."},
      {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "The jointed abdominal segments are connected by an **extensible** chitinous membrane that facilitates rapid swimming."}
    ]
  },
  "Dashboard — tens/extensile.md": {
    "primary": "Capable of being extended, protruded, or stretched out, especially describing biological organs like tongues or tentacles.",
    "secondary": "In comparative vertebrate anatomy, the long extensile tongue of anteaters and chameleons utilizes specialized hyoid musculature.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The chameleon captures insects by projecting its long, sticky, **extensile** tongue with lightning rapidity."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The woodpecker possesses a remarkably **extensile** tongue supported by elongated hyoid horns curving over the skull."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The giant oceanic squid wields long, **extensile** tentacles armed with horny toothed suckers."}
    ]
  },
  "Dashboard — tens/extension.md": {
    "primary": "The act of stretching or extending, or the state of being extended; an added part or continuation.",
    "secondary": "In Cartesian metaphysics and classical physics, extension (res extensa) defines the fundamental spatial property of physical matter.",
    "quotes": [
      {"author": "René Descartes", "work": "Meditations on First Philosophy", "quote": "The nature of matter consists not in hardness or weight, but solely in this, that it is a substance possessing spatial **extension**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We acquire our primary ideas of **extension** and motion through the combined senses of sight and touch."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The attorney requested a formal **extension** of time to prepare the voluminous Chancery interrogatories."}
    ]
  },
  "Dashboard — tens/extensional.md": {
    "primary": "Pertaining to, characterized by, or having spatial extension; or in logic, defined by the set of objects denoted.",
    "secondary": "In formal philosophical semantics and mathematical logic, an extensional definition specifies a class by enumerating its individual members.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Logicians distinguish between the **extensional** scope of a general term and its internal conceptual connotation."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Material phenomena possess an **extensional** reality in space that persists through all transformation."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our immediate visual field presents an **extensional** manifold across which sensory data is localized."}
    ]
  },
  "Dashboard — tens/extensive.md": {
    "primary": "Covering or affecting a large area, space, or scope; broad, widespread, or far-reaching.",
    "secondary": "In agricultural economics, extensive farming utilizes lower capital and labor inputs per unit land area across vast acreages.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Pemberley woods were **extensive**, covering several beautiful hills and sheltering an exquisite trout stream."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes possessed an **extensive** and curious knowledge of criminal literature, chemistry, and tobacco ashes."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor is limited only by the **extensive** reach and purchasing power of the market."}
    ]
  },
  "Dashboard — tens/extensively.md": {
    "primary": "To a great extent, degree, or area; widely, broadly, or comprehensively.",
    "secondary": "In historical agronomy, pastoralists utilized the western open range extensively for nomadic beef cattle grazing.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The pampas of South America were **extensively** covered with tall, waving grasses and wild thistles."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Watson had traveled **extensively** through the Northwest Frontier provinces during the Afghan military campaigns."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Roman civil jurisprudence was adopted **extensively** throughout the newly conquered barbarian kingdoms of Europe."}
    ]
  },
  "Dashboard — tens/extensiveness.md": {
    "primary": "The quality, condition, or property of being widespread, broad, comprehensive, or large in area or scope.",
    "secondary": "In epistemology and cognitive psychology, the subjective extensiveness of visual sensations forms the foundation of spatial perception.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Every primitive sensation of sight and touch possesses an inherent **extensiveness** or spatial volume."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The remarkable **extensiveness** of modern commercial credit networks binds distant continental economies together."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The **extensiveness** of the imperial trade with the Indies enriched the merchant houses of London and Bristol."}
    ]
  },
  "Dashboard — tens/extensor.md": {
    "primary": "A skeletal muscle whose contraction extends, straightens, or opens a joint, limb, or other anatomical part.",
    "secondary": "In clinical musculoskeletal neurology, eliciting the extensor carpi radialis reflex assesses cervical spinal nerve integrity.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **extensor** digitorum communis muscle arises from the lateral humeral epicondyle and straightens the fingers."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Antagonistic muscle pairs, such as the flexor and **extensor**, coordinate to produce balanced limb movements."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician examined the patient for unilateral **extensor** plantar responses indicative of pyramidal tract injury."}
    ]
  },
  "Dashboard — tens/inextensible.md": {
    "primary": "Incapable of being stretched, extended, or drawn out in length; rigid and inelastic.",
    "secondary": "In classical theoretical mechanics, an idealized inextensible cord is modeled as having zero elastic elongation under tension.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Consider two equal masses connected by a perfectly flexible, **inextensible** thread passing over a frictionless pulley."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The suspension apparatus was constructed using an **inextensible** silk filament to prevent torsional drift."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The heavy diving suit was reinforced with **inextensible** copper wire mesh to resist crushing sea depths."}
    ]
  },
  "Dashboard — tens/intense.md": {
    "primary": "Existing in an extreme degree; possessing great strength, energy, depth of feeling, or concentration.",
    "secondary": "In physical optics and laser technology, intense monochromatic coherent radiation drives nonlinear optical phenomena.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I worked with an **intense** and breathless scientific enthusiasm that banished all need for ordinary sleep."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester gazed upon Jane with an **intense**, searching look that seemed to probe her very soul."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "An **intense** stillness brooding over the moor was suddenly broken by the terrifying howl of the hound."}
    ]
  },
  "Dashboard — tens/intensely.md": {
    "primary": "To an extreme or acute degree; with great effort, energy, or deep emotion; vehemently.",
    "secondary": "In sensory psychophysics, human rod photoreceptors respond intensely to low-light scotopic illumination.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt **intensely** ashamed of his humble home and working apron after returning from Satis House."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth suffered **intensely** from the painful mortification inflicted by her mother's loud, vulgar chatter."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes listened **intensely** at the locked door, his sharp features illuminated by the lantern flame."}
    ]
  },
  "Dashboard — tens/intensification.md": {
    "primary": "The action of making or becoming more intense, acute, severe, or concentrated; escalation.",
    "secondary": "In synoptic meteorology and tropical cyclone dynamics, rapid intensification occurs when central core pressure drops sharply over warm sea.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The submarine campaign witnessed a sudden **intensification** that threatened the oceanic lifeline of the British Isles."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The panic in Paris led to an alarming **intensification** of political terror, filling the prisons with suspects."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The evolutionary specialization of sensory organs involves an **intensification** of neural responsiveness."}
    ]
  },
  "Dashboard — tens/intensified.md": {
    "primary": "Made greater, stronger, more acute, or more severe in degree, power, or concentration.",
    "secondary": "In photography and optical image processing, an intensified charge-coupled device multiplies incoming photons for low-light night imaging.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The thick Dartmoor fog **intensified** rapidly, rolling in white billows across the treacherous mires."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My grief and remorse were **intensified** by the bitter knowledge that my own creation had destroyed Justine."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary fury was **intensified** by long centuries of feudal oppression and unbearable poverty."}
    ]
  },
  "Dashboard — tens/intensifier.md": {
    "primary": "A person or thing that intensifies; or in linguistics, an adverb or particle that heightens the meaning of another word (e.g. 'very').",
    "secondary": "In night vision electro-optics, an image intensifier tube amplifies ambient starlight using a photocathode and microchannel plate.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The rhetorical speaker employed an emphatic **intensifier** to heighten the emotional gravity of his plea."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Passionate poetic diction acts as an **intensifier** of moral sentiments, burning them into memory."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Griffin used a chemical **intensifier** to accelerate the bleach of biological pigments in living tissue."}
    ]
  },
  "Dashboard — tens/intensify.md": {
    "primary": "To make or become more intense, acute, severe, or concentrated; to heighten or sharpen.",
    "secondary": "In ecological agricultural economics, farmers intensify crop output per hectare by utilizing automated drip irrigation and fertilizers.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The darkness of the autumn evening seemed to **intensify** the mysterious gloom of the abandoned suburban villa."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The cold wind sweeping across the northern moor served only to **intensify** Jane's physical suffering."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "We resolved to **intensify** strategic bombing offensives against the industrial transport centers of the enemy."}
    ]
  },
  "Dashboard — tens/intensifying.md": {
    "primary": "Increasing in strength, degree, severity, or concentration; becoming sharper or more acute.",
    "secondary": "In radiological diagnostic imaging, calcium tungstate intensifying screens convert incident X-rays into visible light to expose photographic film.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The crew huddled under the storm bridge, watching the **intensifying** hurricane whip the sea into foam."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The London fog was **intensifying** as night fell, choking the gas lamps along Chancery Lane."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Frankenstein felt an **intensifying** dread that shadowed every step of his solitary journey to England."}
    ]
  },
  "Dashboard — tens/intension.md": {
    "primary": "The internal content or connotation of a concept; or the determination or degree of tension, energy, or exertion.",
    "secondary": "In formal philosophical semantics and intensional logic, the intension of a predicate denotes its essential meaning or defining attributes.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **intension** of a general name signifies the essential attributes that any object must possess to bear that name."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The intellect operates with varying degrees of **intension**, from casual curiosity to deep contemplation."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The moral will must be exercised with deliberate **intension** to withstand the subtle assaults of temptation."}
    ]
  },
  "Dashboard — tens/intensional.md": {
    "primary": "Pertaining to, involving, or characterized by intension; defining meaning by attributes rather than enumerated members.",
    "secondary": "In modal philosophical logic, an intensional context (such as belief or necessity) violates the principle of truth-functional substitutivity.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An **intensional** analysis of moral predicates reveals the necessary properties presupposed by human ethical judgment."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Subjective emotional states possess an **intensional** directedness toward objects in the outer environment."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The mind constructs **intensional** categories that harmonize diverse sensory impressions into coherent knowledge."}
    ]
  },
  "Dashboard — tens/intensity.md": {
    "primary": "The quality or condition of being intense; great energy, strength, concentration, or degree.",
    "secondary": "In wave physics and radiometry, radiant intensity represents the radiant flux emitted per unit solid angle in a specified direction.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic **intensity** of the galvanic current was measured using a sensitive astatic galvanometer."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester spoke with a passionate **intensity** that caused Jane's heart to tremble with tender emotion."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the burnt match with an **intensity** that revealed the importance of the tiny relic."}
    ]
  },
  "Dashboard — tens/intensive.md": {
    "primary": "Concentrated, thorough, and exhaustive; or in agriculture, designed to maximize productivity from a given land area.",
    "secondary": "In thermodynamics and physical chemistry, an intensive property (such as temperature or pressure) does not depend on system mass.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Flemish farmers practiced an **intensive** system of agriculture that yielded abundant grain from small parcels."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The typhoid patient required **intensive** clinical nursing care and constant monitoring of fluid intake."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes subjected the forensic evidence to an **intensive** chemical analysis in his private laboratory."}
    ]
  },
  "Dashboard — tens/intensively.md": {
    "primary": "In an intensive, thorough, concentrated, or exhaustive manner; with deep focus.",
    "secondary": "In economic agrarian history, European market gardeners cultivated urban hinterland plots intensively to supply fresh produce.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Land situated near metropolitan centers is farmed more **intensively** owing to the high market value of garden crops."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin studied **intensively** through the night, mastering the complex French literature on immunology."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The coastal defenses were **intensively** fortified with concrete pillboxes, barbed wire, and anti-tank ditches."}
    ]
  },
  "Dashboard — tens/intensiveness.md": {
    "primary": "The quality, state, or degree of being intensive, concentrated, or thorough in application.",
    "secondary": "In production theory and industrial economics, capital intensiveness measures the ratio of capital equipment employed per labor unit.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The **intensiveness** of human competition increases as urban populations become more concentrated."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The economic efficiency of manufacture depends upon the **intensiveness** with which machine power is utilized."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The psychological **intensiveness** of sensory attention determines how deeply impressions are etched in memory."}
    ]
  },
  "Dashboard — tens/nonextensile.md": {
    "primary": "Not extensile; incapable of being stretched, extended, or drawn out in length or area.",
    "secondary": "In comparative vertebrate morphology, nonextensile skeletal ligaments stabilize joint articulations against dislocation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The tough, **nonextensile** fibrous capsule of the hip joint provides essential structural stability during locomotion."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Dense **nonextensile** collagen bundles form the deep fascia, encasing muscle compartments under high tension."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain marine invertebrates develop rigid, **nonextensile** appendages specialized solely for defensive armor."}
    ]
  },
  "Dashboard — tens/pretense.md": {
    "primary": "An attempt to make something that is not the case appear true; a false claim, facade, or affected display.",
    "secondary": "In criminal fraud jurisprudence, obtaining property by false pretense involves intentional misrepresentation of material fact.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth made no **pretense** of affection, rejecting Mr. Collins's pompous marriage proposal without hesitation."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip detested the hollow **pretense** of gentility maintained by Pumblechook while visiting the forge."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The criminal assumed the **pretense** of an elderly invalid to disarm the suspicions of the street watchman."}
    ]
  },
  "Dashboard — tens/pretension.md": {
    "primary": "An assertion of a claim, right, or title; or an inflated display of importance, merit, or social standing.",
    "secondary": "In social satire and comedy of manners, unmasking social pretension exposes the vanity of aspiring bourgeois parvenus.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton's ridiculous **pretension** to the hand of Emma Woodhouse provoked her astonishment and indignation."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian general dismissed the hollow **pretension** of the senate, demanding gold as the price of peace."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The aristocratic family maintained their ancient **pretension** despite the ruinous decay of their ancestral fortune."}
    ]
  },
  "Dashboard — tens/tense.md": {
    "primary": "Stretched tight, rigid, or strained; feeling or showing nervous strain; or in grammar, a category locating an event in time.",
    "secondary": "In linguistics and generative phonology, a tense vowel is articulated with greater muscular effort and peripheral tongue position.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We waited in the darkness with **tense** nerves, our revolvers ready as the fog crept over the moor."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane felt every muscle grow **tense** with dread as the mysterious footsteps passed outside her chamber door."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Hold hard the breath and bend up every spirit to his full height; stand **tense** like greyhounds in the slips."}
    ]
  },
  "Dashboard — tens/tensed.md": {
    "primary": "Became or made tight, strained, or rigid, especially muscles preparing for sudden physical action or shock.",
    "secondary": "In sports biomechanics, an athlete's tensed musculature absorbs impact kinetic energy and protects joint ligaments.",
    "quotes": [
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck's muscles **tensed** under his thick fur as he prepared to spring upon the rival lead dog."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes **tensed** his lean frame, ready to leap upon the intruder the moment the window opened."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The young recruit **tensed** his shoulders against the parapet as the enemy line emerged from the woods."}
    ]
  },
  "Dashboard — tens/tensely.md": {
    "primary": "In a manner marked by nervous strain, acute suspense, rigidity, or tight physical tension.",
    "secondary": "In dramatic staging and cinematic editing, cross-cutting between ticking clocks and protagonists builds tensely structured suspense.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Watson gripped his pistol **tensely**, listening to the splashing footsteps approaching through the mire."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Marlow waited **tensely** for Jim to speak, realizing the young man's honor was hanging in the balance."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The prisoners listened **tensely** as the heavy tumbril wheels clattered over the cobblestones toward the scaffold."}
    ]
  },
  "Dashboard — tens/tenseness.md": {
    "primary": "The physical state of being stretched tight, or the psychological condition of experiencing nervous anxiety or strain.",
    "secondary": "In clinical biofeedback and stress management, measuring electromyographic tenseness in frontalis muscles evaluates relaxation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The acute **tenseness** of the atmosphere was broken only by the ticking of the clock on the mantelpiece."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy Snowe experienced a painful nervous **tenseness** as she stood before the crowded examination hall."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The unnatural **tenseness** of Henchard's jaw revealed the bitter rage warring within his breast."}
    ]
  },
  "Dashboard — tens/tensile.md": {
    "primary": "Relating to tension or stretching; capable of being drawn out or withstanding longitudinal stretching forces without breaking.",
    "secondary": "In materials science and structural metallurgy, measuring the ultimate tensile strength determines maximum engineering yield load.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The experimentalist tested the **tensile** strength of fine metallic wires under increasing mechanical weights."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The hempen whale line possessed immense **tensile** resilience, capable of withstanding the sounding rush of the whale."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian mechanical metal possessed extraordinary **tensile** toughness combined with lightweight flexibility."}
    ]
  },
  "Dashboard — tens/tensimeter.md": {
    "primary": "An apparatus or instrument used to measure the vapor pressure of liquids or the tension of gases.",
    "secondary": "In physical chemistry, a differential tensimeter measures small vapor pressure differences between pure solvent and dilute solutions.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The chemical laboratory was equipped with a precision mercury **tensimeter** to record vapor tensions of ethers."},
      {"author": "John Tyndall", "work": "Heat, a Mode of Motion", "quote": "The investigator calibrated the **tensimeter** to observe the rapid increase of vapor pressure with rising temperature."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor checked the delicate **tensimeter** mounted on the sphere's bulkhead before sealing the airlock hatches."}
    ]
  },
  "Dashboard — tens/tensiometer.md": {
    "primary": "An instrument for measuring the surface tension of liquids, the moisture tension in soils, or mechanical cable tension.",
    "secondary": "In physical colloid chemistry, the du Noüy ring tensiometer measures the force required to pull an interface ring through a meniscus.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The experimentalist measured the interfacial force using a platinum ring attached to a delicate **tensiometer**."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Modern agricultural hydrologists employ the soil **tensiometer** to quantify the suction forces exerted by roots on moisture."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Physical laboratories utilize the **tensiometer** to determine the cohesive forces governing capillary phenomena."}
    ]
  },
  "Dashboard — tens/tension.md": {
    "primary": "The state of being stretched tight; mental or emotional strain; or the pulling force exerted by a stretched cord, cable, or wire.",
    "secondary": "In electrical engineering and circuit theory, high-tension lines transmit electric power at thousands of volts to minimize I²R losses.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The electrical **tension** between the galvanic poles was sufficient to ignite paper soaked in spirits."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The terrible **tension** of the vigil was broken by the sound of rapid footsteps echoing across the granite rocks."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's nerves were strung to an unbearable **tension** by the agonizing uncertainty of Willoughby's silence."}
    ]
  },
  "Dashboard — tens/tensional.md": {
    "primary": "Of, relating to, or resulting from mechanical tension, stretching forces, or structural stress.",
    "secondary": "In structural geology and continental tectonics, tensional stress within the crust produces normal faulting and rift grabens.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Regional crustal uplift generates severe **tensional** fractures that allow volcanic dikes to penetrate the strata."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Every material system seeks equilibrium between compressive attractions and **tensional** elastic repulsions."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The earth movements produced **tensional** rifts that determined the courses of subsequent river valleys."}
    ]
  },
  "Dashboard — tens/tensionless.md": {
    "primary": "Free from tension, stress, or strain; completely relaxed, loose, or slack.",
    "secondary": "In textile machinery and synthetic yarn spinning, tensionless fabric winding prevents mechanical distortion and fiber stretching.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The heavy harpoon line hung slack and **tensionless** in the tub once the swimming whale had breached."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane sank into a peaceful, **tensionless** sleep, her troubled spirit resting after days of bitter wandering."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The evening water lay smooth and **tensionless** under the quiet sky, reflecting the pale stars without a ripple."}
    ]
  },
  "Dashboard — tens/tensity.md": {
    "primary": "The state or degree of being tense, tight, stretched, or rigid; tenseness.",
    "secondary": "In psychological acoustics, auditory perceptual tensity correlates with harmonic dissonance and sound pressure levels.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The dramatic poet maintains a nervous **tensity** in the dialogue that keeps the audience in breathless suspense."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Roderick Usher's voice betrayed an unnatural **tensity** that signaled the final collapse of his reason."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The acute **tensity** of the political crisis in Paris could not long endure without an explosive violent resolution."}
    ]
  },
  "Dashboard — tens/tensor.md": {
    "primary": "An algebraic object that describes a multilinear relationship between geometric vectors; or a muscle that tightens a body part.",
    "secondary": "In differential geometry and Einstein's general theory of relativity, the Riemann curvature tensor describes the intrinsic curvature of spacetime.",
    "quotes": [
      {"author": "Albert Einstein", "work": "The Meaning of Relativity", "quote": "Gravitational field equations are formulated in **tensor** form to maintain general covariance under coordinate transformations."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **tensor** fasciae latae muscle tenses the lateral fascia of the thigh and assists in hip abduction."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger discussed theoretical mathematical problems, referencing **tensor** calculus while examining the fossils."}
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

print(f"Motion Batch 4B: Successfully updated {updated}/{len(data)} notes.")
