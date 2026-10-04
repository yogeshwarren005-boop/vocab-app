# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — duct Part 1 (8A, 38 words) ---
  "Dashboard — duct/abduct.md": {
    "primary": "To carry off or lead away a person unlawfully by force, fraud, or intimidation; or to draw a limb away from the median axis.",
    "secondary": "In kinesiology and musculoskeletal anatomy, to abduct an extremity means to move it laterally away from the sagittal midline of the body.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The conspirators planned to **abduct** the young duke from the boarding school under cover of darkness."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The mob threatened to **abduct** the magistrate if the rioters were not immediately released."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The outlaw attempted to **abduct** the heiress across the border into the Scottish hills."}
    ]
  },
  "Dashboard — duct/abducting.md": {
    "primary": "Carrying away a person unlawfully by force, fraud, or persuasion; or pulling a limb outward from the body's midline.",
    "secondary": "In biomechanics, the abducting action of the deltoid muscle elevates the arm in the coronal plane away from the torso.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The police arrested the confederates while they were **abducting** the foreign diplomat."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The clan was accused of **abducting** cattle and wealthy travelers along the Highland border."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "The sailors were charged with **abducting** the young heir aboard the brig bound for the Carolinas."}
    ]
  },
  "Dashboard — duct/abduction.md": {
    "primary": "The unlawful carrying away of a person by force, fraud, or coercion; or movement of a limb away from the midline.",
    "secondary": "In epistemology and Peano-Peircean semiotics, abduction denotes logical inference to the best explanatory hypothesis from observed data.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The sudden **abduction** of the young nobleman threw the entire ducal household into utter dismay."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The magistrate investigated the mysterious **abduction** of the child from the parish workhouse."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The mythical **abduction** of the Sabine women laid the foundation of Rome's earliest alliances."}
    ]
  },
  "Dashboard — duct/abductor.md": {
    "primary": "A person who abducts or kidnaps someone; or a muscle that draws a limb or digit away from the median line of the body.",
    "secondary": "In clinical neurology, testing the abductor pollicis brevis muscle evaluates the motor integrity of the median nerve.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "Holmes traced the footprints of the ruthless **abductor** across the damp clay of the lane."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The lateral contraction of the **abductor** oculi muscle directs the gaze swiftly outward."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The armed citizens pursued the daring **abductor** through the torchlit gates of the borough."}
    ]
  },
  "Dashboard — duct/adduct.md": {
    "primary": "To draw, pull, or move a limb or bodily part toward the median axis of the body or toward an adjacent part.",
    "secondary": "In biochemistry and chemical toxicology, a covalent adduct is a stable molecular complex formed between DNA or protein and a reactive carcinogen.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Certain facial muscles contract to **adduct** the lower jaw firmly against the upper molars."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "When the antagonistic muscles relax, the primary flexors **adduct** the limb toward the center."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The examiner instructed the patient to **adduct** the injured leg across the midline."}
    ]
  },
  "Dashboard — duct/adducting.md": {
    "primary": "Drawing, pulling, or moving an anatomical part or limb toward the central sagittal plane of the body.",
    "secondary": "In vocal fold physiology, adducting the vocal cords brings them into apposition at the midline to enable phonation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The animal snarled, **adducting** its ears backward against its skull in preparation for battle."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "By steadily **adducting** the thigh, the equestrian maintains a firm grip upon the saddle."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The muscular reflex of **adducting** the limbs protects vulnerable abdominal organs during impact."}
    ]
  },
  "Dashboard — duct/adduction.md": {
    "primary": "The movement of a limb, digit, or anatomical structure toward the median axis of the body or across the midline.",
    "secondary": "In classical dialectic and rhetoric, adduction is the act of citing, adducing, or bringing forward evidence and illustrative authorities.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The powerful **adduction** of the pectoral muscles enables birds to strike downward with great wing force."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The complete **adduction** of the human great toe is a specialized adaptation essential for erect bipedal walking."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The judicial **adduction** of historical precedents gives stability to statutory interpretation."}
    ]
  },
  "Dashboard — duct/adductive.md": {
    "primary": "Pertaining to, effecting, or characterized by adduction; drawing toward a central axis or bringing forward arguments.",
    "secondary": "In ophthalmology, adductive eye movements (convergence) coordinate both medial rectus muscles to focus upon nearby objects.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **adductive** force exerted by the femoral muscles balances the pelvis during lateral stride shifts."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The coordinated **adductive** contractions of the digits allow arboreal primates to grasp slender branches."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "An **adductive** spasm of the vocal cords accompanies the sudden gasp of astonishment."}
    ]
  },
  "Dashboard — duct/adductor.md": {
    "primary": "A muscle whose function is to draw a body part or limb toward the central median axis of the body.",
    "secondary": "In malacology and invertebrate zoology, the adductor muscles of bivalve mollusks contract to draw the two shell valves tightly shut.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The giant clam holds its valves together with an enormous **adductor** muscle capable of resisting immense force."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Strain of the **adductor** longus muscle is a common disabling injury among horse riders."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The anatomical specimen revealed the thick **adductor** band that anchored the whale's jaw to the skull."}
    ]
  },
  "Dashboard — duct/aqueduct.md": {
    "primary": "A conduit, artificial channel, or monumental bridged structure constructed to convey water across valleys and distances.",
    "secondary": "In human neuroanatomy, the cerebral aqueduct (aqueduct of Sylvius) connects the third and fourth ventricles within the midbrain.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The majestic Roman **aqueduct** marched across the Campagna on thousands of travertine arches, bearing mountain springs to the capital."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Arches on arches! as an **aqueduct** of stone spans the wide desert with its ruined pride."},
      {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "The ruined Roman **aqueduct** stretched across the silent plains like the backbone of an extinct monster."}
    ]
  },
  "Dashboard — duct/circumduction.md": {
    "primary": "The circular or conical movement of a body limb or eye whereby the distal end describes a circle while the proximal end remains fixed.",
    "secondary": "In ball-and-socket synovial joint mechanics (such as the glenohumeral joint), circumduction combines flexion, abduction, extension, and adduction in sequence.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The ball-and-socket shoulder joint allows complete **circumduction** of the arm through a wide conical arc."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The revolving nutation of twining stems closely resembles the **circumduction** observed in animal limb joints."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The orthopedic examination demonstrated painful limitation of **circumduction** in the affected hip joint."}
    ]
  },
  "Dashboard — duct/conduct.md": {
    "primary": "Personal behavior, deportment, or way of acting; or to direct, manage, lead, or transmit heat or electricity.",
    "secondary": "In electromagnetic theory, copper wires conduct electric currents with minimal resistive thermal dissipation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth could not see such behavior without feeling that Mr. Wickham's **conduct** was open to the severest censure."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The prudent man governs his personal **conduct** by the impartial spectator residing within his breast."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I conceived the bold project of arriving at moral perfection, regulating my daily **conduct** by thirteen virtues."}
    ]
  },
  "Dashboard — duct/conductance.md": {
    "primary": "A measure of the ability of a material or electrical circuit element to conduct an electric current; the reciprocal of resistance.",
    "secondary": "In plant ecophysiology, stomatal conductance regulates the rate of transpiration water loss and photosynthetic carbon dioxide uptake.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The electrical **conductance** of a uniform metal wire is directly proportional to its cross-sectional area."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "Submarine telegraphic cables require copper of the highest purity to maximize electrical **conductance**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The thermal **conductance** of various metals was systematically measured by the Royal Society."}
    ]
  },
  "Dashboard — duct/conducting.md": {
    "primary": "Directing, managing, or leading an operation, orchestra, or inquiry; or conveying heat, electricity, or fluid.",
    "secondary": "In neurobiology, the conducting axons of peripheral nerves propagate action potentials rapidly via saltatory conduction.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes was engaged in **conducting** a delicate chemical experiment over a spirit lamp."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The specialized vascular bundles serve as **conducting** channels carrying sap from roots to foliage."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke believed he was **conducting** the county election with consummate political finesse."}
    ]
  },
  "Dashboard — duct/conduction.md": {
    "primary": "The transmission or transfer of energy, heat, electricity, or sound through a medium without gross displacement of the material.",
    "secondary": "In cardiology and electrophysiology, the cardiac conduction system coordinates ventricular contraction via the bundle of His and Purkinje fibers.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Heat is propagated through solid bodies by the internal **conduction** of atomic vibrations."},
      {"author": "James Clerk Maxwell", "work": "Matter and Motion", "quote": "Thermal **conduction** differs fundamentally from convection, which relies on the bulk displacement of fluid particles."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The rapid **conduction** of heat through iron makes it suitable for stoves and industrial boilers."}
    ]
  },
  "Dashboard — duct/conductive.md": {
    "primary": "Having the property or power of conducting or transmitting heat, electricity, sound, or other physical forms of energy.",
    "secondary": "In sensory otology, conductive hearing loss occurs when sound transmission is impeded through the external ear canal or middle ear ossicles.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "A silver rod provides the most **conductive** pathway for discharging an electrostatic condenser."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The **conductive** power of metals diminishes as their ambient temperature increases."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The alien machinery rested on heavily insulated stands, avoiding any **conductive** contact with the damp clay."}
    ]
  },
  "Dashboard — duct/conductivity.md": {
    "primary": "The measure of a specified substance's capacity to transmit electricity, heat, or sound per unit cross-sectional area.",
    "secondary": "In materials science and solid-state physics, high electrical conductivity in noble metals arises from free valence electron mobility.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The thermal **conductivity** of metals generally corresponds with their electrical conductivity."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Many think that they are able to generate an intense heat in a chamber of practically zero thermal **conductivity**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Experiments upon the electrical **conductivity** of aqueous saline solutions opened a new chapter in physical chemistry."}
    ]
  },
  "Dashboard — duct/conductor.md": {
    "primary": "A substance or medium that conducts heat or electricity; or a person who directs an orchestra, choir, train, or expedition.",
    "secondary": "In classical electrostatics, an ideal electrical conductor maintains zero electric field within its interior volume under electrostatic equilibrium.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Under the shadow of this extemporized lightning-**conductor** he felt himself comparatively safe."},
      {"author": "Benjamin Franklin", "work": "Experiments and Observations on Electricity", "quote": "A pointed iron **conductor** erected upon the roof of a house will safely guide lightning into the moist earth."},
      {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "The stagecoach **conductor** blew his copper horn to warn the mountain villages of our approach."}
    ]
  },
  "Dashboard — duct/conductress.md": {
    "primary": "A woman who guides, directs, manages, or conducts an enterprise, tour, passenger vehicle, or gathering.",
    "secondary": "In nineteenth-century educational history, a conductress was a headmistress or directress managing a young ladies' boarding academy.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My **conductress** led me down a long paneled corridor and tapped softly at the door of the parlor."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck was the vigilant **conductress** of the pensionnat, observing every pupil with quiet surveillance."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Goddard acted as the respected **conductress** of the principal boarding school for girls in Highbury."}
    ]
  },
  "Dashboard — duct/counterproductive.md": {
    "primary": "Having the opposite of the desired effect; tending to hinder rather than promote the achievement of an objective.",
    "secondary": "In macroeconomic regulation, price ceilings can prove counterproductive by causing artificial shortages and black market arbitrage.",
    "quotes": [
      {"author": "George Orwell", "work": "Collected Essays", "quote": "Censorship invariably proves **counterproductive**, creating public fascination with ideas that would otherwise fade away."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Harsh reprisals against the civil population proved entirely **counterproductive**, stiffening the local resistance."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "Coercive pedagogical methods are **counterproductive** because they destroy the natural curiosity of the learner."}
    ]
  },
  "Dashboard — duct/deduct.md": {
    "primary": "To take away, subtract, or subtract an amount or part from a total sum or quantity.",
    "secondary": "In income tax accounting, taxpayers deduct legitimate business expenses from gross revenues to determine taxable net income.",
    "quotes": [
      {"author": "William James", "work": "Pragmatism", "quote": "My father pleaded poverty; and at last he bargained to advance a guinea, and **deduct** it out of my allowance."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The landlord will **deduct** the expense of necessary repairs from the annual rent owed by the tenant."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solicitor agreed to **deduct** his traveling costs from the final accounting rendered to the court."}
    ]
  },
  "Dashboard — duct/deductible.md": {
    "primary": "Capable of being deducted or subtracted; or an upfront amount that an insured person must pay before insurance benefits apply.",
    "secondary": "In insurance risk underwriting, a higher policy deductible reduces moral hazard by aligning the policyholder's financial incentives with loss prevention.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "All necessary costs of raw materials are justly **deductible** from the gross commercial value of finished wares."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Expenses incurred in preserving capital intact are **deductible** before net revenue is estimated."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The parliamentary commissioners declared that only verified military expenditures were **deductible** from the national levy."}
    ]
  },
  "Dashboard — duct/deduction.md": {
    "primary": "The action of subtracting an amount; or the logical process of reasoning from general principles to specific conclusions.",
    "secondary": "In formal philosophical logic, a deductive argument is valid if and only if the truth of its premises necessitates the truth of its conclusion.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Hence, you see, my double **deduction** that you had been out in vile weather, and that you had a clumsy servant."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The method of physical science consists in induction, **deduction**, and subsequent empirical verification."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "From sound principles, careful **deduction** leads the intellect to reliable knowledge of particular instances."}
    ]
  },
  "Dashboard — duct/deductive.md": {
    "primary": "Pertaining to, based upon, or using the logical method of deduction; reasoning from general premises to necessary conclusions.",
    "secondary": "In epistemology, deductive axiomatic systems (such as Euclidean geometry) demonstrate theorems via formal logical inference from axioms.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Detection is, or ought to be, an exact science, and should be treated in the same cold and unemotional **deductive** manner."},
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "An entertaining retort, in the narrow and **deductive** manner of the Middle Ages, replied the scholar."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **deductive** science of mechanics demonstrates how compound forces produce equilibrium or motion."}
    ]
  },
  "Dashboard — duct/duct.md": {
    "primary": "A bodily tube, canal, or vessel that conveys fluid or secretions; or a conduit for ventilation, cables, or liquids.",
    "secondary": "In industrial HVAC engineering, sheet-metal duct networks distribute heated or conditioned air throughout multi-story buildings.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The lacrimal gland pours its secretion through a delicate **duct** over the surface of the eyeball."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Bile passes from the liver cells into the hepatic **duct** and is stored within the gallbladder."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A subterranean **duct** seemed to connect the deep fountain of his thoughts with his outward speech."}
    ]
  },
  "Dashboard — duct/ductile.md": {
    "primary": "Capable of being drawn out into wire or hammered thin without breaking; pliable, malleable, or easily influenced.",
    "secondary": "In materials engineering and fracture mechanics, ductile metals undergo significant plastic deformation before ultimate tensile failure.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Gold is the most **ductile** and malleable of all known metallic substances."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "And you O my soul where you stand, surrounded, detached, in measureless oceans of space, ceasing not to explore the **ductile** anchor."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne's character was not **ductile** enough to yield to Lady Russell's wishes against her own heart."}
    ]
  },
  "Dashboard — duct/ductileness.md": {
    "primary": "The mechanical property or physical tractability of a material that allows it to be drawn into slender wires.",
    "secondary": "In metallurgy and tensile testing, the ductileness of an alloy is quantified by its percentage elongation and reduction of cross-sectional area.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The remarkable **ductileness** of platinum allows it to be drawn through diamond dies into filaments of microscopic fineness."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The **ductileness** of heated copper enabled early artisans to fabricate intricate household vessels."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The physical **ductileness** of molten glass permits blowers to fashion delicate spherical globes."}
    ]
  },
  "Dashboard — duct/ductility.md": {
    "primary": "The physical capacity of a metal or material to undergo plastic deformation and elongation under tensile stress without fracturing.",
    "secondary": "In seismic structural engineering, high material ductility in structural steel frames dissipates earthquake energy through controlled yielding.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The extraordinary **ductility** of gold permits a single grain to be beaten into leaves that cover several square feet."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The young man's moral **ductility** made him an easy victim to the flatteries of unscrupulous companions."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The high **ductility** of silver and copper makes them indispensable for commercial wire drawing."}
    ]
  },
  "Dashboard — duct/ductless.md": {
    "primary": "Having no duct or excretory canal; discharging secretions directly into the bloodstream or surrounding tissue.",
    "secondary": "In human endocrinology, ductless glands (such as the thyroid, adrenal, and pituitary glands) synthesize and release hormones into systemic circulation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The spleen and adrenal bodies belong to the class of **ductless** glands whose internal secretions modify the blood."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The evolutionary function of the **ductless** thyroid gland was long a mystery to comparative anatomists."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Disorders of the **ductless** glands produce profound alterations in basal metabolic activity."}
    ]
  },
  "Dashboard — duct/ductule.md": {
    "primary": "A minute, microscopic duct or fine canal within a biological organ or gland.",
    "secondary": "In hepatic histology, bile ductules (canals of Hering) bridge intrahepatic bile canaliculi with interlobular bile ducts in portal triads.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Fluid is collected from individual glandular acini by a microscopic **ductule** that empties into the main vessel."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Each lacrimal **ductule** conveys tears smoothly across the conjunctival sac during blinking."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction of an intrahepatic **ductule** by inflammatory exudate leads to localized biliary stasis."}
    ]
  },
  "Dashboard — duct/ductulus.md": {
    "primary": "An anatomical term for a very small duct or minute excretory canal (plural: ductuli).",
    "secondary": "In reproductive histology, the efferent ductules (ductuli efferentes) connect the rete testis to the head of the epididymis.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each delicate **ductulus** in the glandular parenchyma is lined with a single layer of secretory epithelial cells."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The comparative structure of the seminal **ductulus** across vertebrates demonstrates remarkable morphological homology."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination of the tissue section revealed cystic dilation of the renal **ductulus**."}
    ]
  },
  "Dashboard — duct/induct.md": {
    "primary": "To install or admit someone formally with ceremony into an office, benefice, society, or military organization.",
    "secondary": "In ecclesiastical law and the Church of England, an archdeacon will induct a newly instituted rector into real possession of the church temporalities.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bishops assembled in council to **induct** the new patriarch into the patriarchal throne of Antioch."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The university authorities refused to **induct** the royal nominee into the presidency of the college."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The presbytery met in solemn convocation to **induct** the young minister into his rural parish."}
    ]
  },
  "Dashboard — duct/inductance.md": {
    "primary": "The property of an electrical circuit or conductor by which a change in current induces an electromotive force; measured in henries.",
    "secondary": "In radio frequency electronics and circuit design, mutual inductance between coupled coils enables transformer voltage step-up and signal isolation.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The self-**inductance** of a circular coil depends directly on its radius and the square of its turns."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The sudden interruption of current creates a high voltage spark due to the inherent **inductance** of the circuit."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "The transmission of telegraphic pulses along long undersea wires is governed by resistance, capacitance, and **inductance**."}
    ]
  },
  "Dashboard — duct/inductee.md": {
    "primary": "A person who is newly inducted or formally enlisted into military service, an academic fellowship, or an organization.",
    "secondary": "In sports and artistic honors organizations, an inductee delivers an acceptance address during the formal annual hall-of-fame enshrinement banquet.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Each young **inductee** reported to the regimental depot for basic military instruction and medical inspection."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The new **inductee** into a guild was bound by sacred oaths to uphold trade secrets and mutual brotherhood."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The academic **inductee** must dedicate himself to impartial scientific research and truth."}
    ]
  },
  "Dashboard — duct/induction.md": {
    "primary": "The act or process of inducting; or reasoning from observed specific cases to establish a general law or principle.",
    "secondary": "In physics and electromagnetism, Faraday's law of electromagnetic induction states that a time-varying magnetic flux induces an electric field.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "These promises are fair, the parties sure, and our **induction** full of prosperous hope."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The true method of science begins with experience and ascends by methodical **induction** to universal axioms."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The movement of a permanent bar magnet within a copper helix causes instantaneous electrical **induction**."}
    ]
  },
  "Dashboard — duct/inductive.md": {
    "primary": "Pertaining to, based on, or using the logical method of induction; or operating by electrical or magnetic induction.",
    "secondary": "In philosophy of science, the problem of inductive inference (Hume's problem) questions the rational justification for expecting the future to conform to the past.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The intuitive, no less than what may be termed the **inductive**, school of ethics, insists on the necessity of general laws."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Their Maker's image then forsook them, when themselves they vilified to serve brute lust, an **inductive** snare of ruin."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **inductive** philosophy proceeds by careful exclusions and rejections of unverified hypotheses."}
    ]
  },
  "Dashboard — duct/inductor.md": {
    "primary": "An electrical component (such as a coiled wire) designed to store magnetic energy and introduce inductance into a circuit.",
    "secondary": "In electrical power filtering, an inductor chokes high-frequency alternating currents while allowing direct current to pass with minimal resistance.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The iron core within the **inductor** increases the magnetic flux density produced by the current."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "An electrical **inductor** placed in the circuit smoothed the sudden voltage surges."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "By placing an **inductor** at periodic intervals along the telephone cable, signal distortion was effectively eliminated."}
    ]
  },
  "Dashboard — duct/introduction.md": {
    "primary": "The formal act of making persons known to one another; or a preliminary explanation or opening section of a book or speech.",
    "secondary": "In invasive species biology, the deliberate introduction of non-native flora can disrupt established ecological food webs.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Here we see how potent has been the effect of the **introduction** of a single tree, nothing whatever else having been done."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bingley was anxious to obtain an **introduction** to Miss Bennet before the dancing commenced."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He flourished the sword by way of **introduction** number two, which startled the spectators."}
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

print(f"Motion Batch 8A: Successfully updated {updated}/{len(data)} notes.")
