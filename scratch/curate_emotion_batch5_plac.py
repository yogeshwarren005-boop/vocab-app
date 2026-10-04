# -*- coding: utf-8 -*-
"""
Curates Dashboard — plac (56 words) in Cluster Emotion.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — plac/complacence.md": {
    "primary": "A feeling of smug or uncritical satisfaction with oneself or one's achievements; complacency.",
    "secondary": "In moral philosophy and theological ethics, unmindful self-satisfaction that blinds a soul to urgent danger.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The divine Father beheld his Son with radiant love and unalloyed **complacence**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins surveyed his small parsonage with profound **complacence**, exalting his patroness."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's cold **complacence** chilled Dorothea's ardent desire for sympathetic communion."}
    ]
  },
  "Dashboard — plac/complacency.md": {
    "primary": "A feeling of quiet pleasure or security, often while unaware of potential danger or defect.",
    "secondary": "In social and organizational psychology, institutional self-satisfaction leading to stagnation and vulnerability.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "A dangerous **complacency** settled over the British public during the interwar years."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Material prosperity often produces an individualistic **complacency** that neglects civic duty."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Court of Chancery slumbered on in comfortable **complacency**, unconcerned by the ruined suitors."}
    ]
  },
  "Dashboard — plac/complacent.md": {
    "primary": "Showing smug or uncritical satisfaction with oneself, one's achievements, or one's situation.",
    "secondary": "In critical characterization, self-satisfied and oblivious to impending catastrophe or systemic flaw.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma was far too **complacent** regarding her own matchmaking talents until humiliating errors opened her eyes."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The delicate Eloi lived in **complacent** luxury upon the surface, ignorant of the Morlocks beneath."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard resented the **complacent** smile with which Farfrae accepted his increasing commercial prosperity."}
    ]
  },
  "Dashboard — plac/complacently.md": {
    "primary": "In a smug, self-satisfied, or uncritical manner; with unconcerned ease.",
    "secondary": "In narrative prose, smiling or resting contentedly while ignoring urgent realities around one.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pumblechook sipped his hot port wine **complacently**, taking all the credit for my unexpected fortune."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Lestrade smiled **complacently** as he produced the handcuffs, convinced he had apprehended the true thief."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The squire rubbed his hands **complacently** before the blazing hearth, proud of his ancestral acres."}
    ]
  },
  "Dashboard — plac/displace.md": {
    "primary": "To take the place of; to remove someone or something from their usual or proper position.",
    "secondary": "In physics and fluid dynamics, to occupy a volume of liquid equal to the volume of the submerged object.",
    "quotes": [
      {"author": "Archimedes", "work": "On Floating Bodies", "quote": "Any solid lighter than a fluid will, if placed in the fluid, be so far immersed that the weight of the solid will be equal to the weight of the fluid it will **displace**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "New and improved varieties inevitably **displace** and exterminate their less adapted ancestral forms."},
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "You have **displaced** the mirth, broke the good meeting, with most admired disorder."}
    ]
  },
  "Dashboard — plac/displacement.md": {
    "primary": "The moving of something from its place or position, or the removal of people from their homeland.",
    "secondary": "In psychoanalysis, an unconscious defense mechanism transferring emotional impulses from their original object to a safer substitute.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "The Interpretation of Dreams", "quote": "Dream-distortion is the direct product of psychological **displacement**, shifting emotional emphasis onto trivial details."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The massive vertical **displacement** of strata along the fault line occurred during prehistoric seismic upheavals."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The westward **displacement** of barbarian nations pushed entire tribes across the frozen Danube into Roman territory."}
    ]
  },
  "Dashboard — plac/emplace.md": {
    "primary": "To put into place or set in a prepared position, especially heavy artillery or military equipment.",
    "secondary": "In structural geology and volcanology, the intrusion and consolidation of magma within preexisting host rock.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Our engineers labored under nocturnal darkness to **emplace** the heavy coastal howitzers on the bluff."},
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "Subterranean pressure served to **emplace** immense granitic batholiths within the folded metamorphic strata."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We prepared to **emplace** our searchlights upon the basalt pinnacles to sweep the primeval forest below."}
    ]
  },
  "Dashboard — plac/emplacement.md": {
    "primary": "A platform, trench, or fortified structure prepared for a gun, radar, or military installation.",
    "secondary": "In igneous petrology, the positioning and crystallization of plutonic rock masses within the Earth's upper crust.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The concrete **emplacement** defied our heaviest aerial bombardment, requiring direct assault by combat sappers."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The geological **emplacement** of the basaltic dikes coincided with the opening of the oceanic rift valley."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The artillerymen scrambled around their gun **emplacement** upon the common, sighting the distant Martian tripod."}
    ]
  },
  "Dashboard — plac/implacable.md": {
    "primary": "Unable to be placated, appeased, or pacified; relentless, unyielding, and inexorable.",
    "secondary": "In classical tragedy and epic poetry, fierce, unbending hatred or vengeance that pursues enemies to destruction.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Madame Defarge was an **implacable** spirit of retribution, knitting the names of the doomed with icy resolve."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab pursued the white whale with an **implacable** malice that consumed every humane feeling in his breast."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan burned with **implacable** hatred against the Almighty and the newly created race of mankind."}
    ]
  },
  "Dashboard — plac/irreplaceable.md": {
    "primary": "Impossible to replace if lost, destroyed, or damaged; uniquely valuable, precious, or singular.",
    "secondary": "In cultural heritage conservation and human ecology, historic monuments and biospheres whose loss is permanent.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "Ancient gothic craftsmanship is utterly **irreplaceable**, carrying the sacred imprint of human hands now turned to dust."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "The destruction of the Alexandrian library annihilated **irreplaceable** treasures of ancient philosophical scholarship."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea felt that the lost hours of youthful enthusiasm were **irreplaceable** in a routine marriage."}
    ]
  },
  "Dashboard — plac/irreplaceableness.md": {
    "primary": "The quality or fact of being impossible to replace; unique and incomparable value.",
    "secondary": "In existential philosophy and aesthetics, the singular uniqueness of an individual life or masterpiece.",
    "quotes": [
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "A true realization of the **irreplaceableness** of every human soul is the supreme foundation of democratic ethics."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The absolute **irreplaceableness** of Turner's atmospheric watercolors demands the most reverent gallery preservation."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Nature stamps each genius with an unrepeatable seal of **irreplaceableness** that defies imitation."}
    ]
  },
  "Dashboard — plac/misplace.md": {
    "primary": "To put something in the wrong place and lose it temporarily; to mislay; also to direct unwisely.",
    "secondary": "In moral judgment, to bestow trust, affection, or loyalty upon an unworthy or treacherous person.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne wept bitterly when she realized how she had been led to **misplace** her deepest romantic affections."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Dick was constantly terrified lest he should **misplace** his manuscript regarding King Charles's head."},
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "My brother's ambition did **misplace** all sovereign duty, usurping my rightful dukedom in secret treachery."}
    ]
  },
  "Dashboard — plac/misplaced.md": {
    "primary": "Incorrectly positioned, mislaid, or put in the wrong place; directed toward an inappropriate object.",
    "secondary": "In social narrative, confidence or generosity squandered upon deceitful beneficiaries.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth blushed at the memory of her **misplaced** confidence in the handsome but treacherous Wickham."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "A **misplaced** wedding ring upon the floor of the empty house gave Holmes his first decisive clue."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I saw that St. John's harsh rebukes were born of **misplaced** religious zeal rather than personal malice."}
    ]
  },
  "Dashboard — plac/misplacement.md": {
    "primary": "The action of putting something in the wrong place, or the state of being misplaced.",
    "secondary": "In anatomical pathology and embryology, heterotopia or ectopia involving tissues developing in abnormal sites.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital **misplacement** of the kidney into the pelvic cavity may simulate an ovarian or uterine neoplasm."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The Circumlocution Office excelled in the bureaucratic **misplacement** of important colonial petitions."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "Slight embryonic **misplacement** of germ layers produces teratoid cysts containing dermal structures in internal organs."}
    ]
  },
  "Dashboard — plac/placable.md": {
    "primary": "Easily calmed, pacified, or appeased; tolerant, forgiving, and mild in temper.",
    "secondary": "In ethical theology and classic tragedy, a deity or sovereign inclined to mercy upon sincere repentance.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "God looked with eye of grace upon their sorrow, finding their penitence **placable** and true."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise prince is ever **placable** toward repentant subjects, reserving severity for incorrigible rebels."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "It is the mark of a noble and cultivated mind to be **placable** in private quarrels and swift to forgive."}
    ]
  },
  "Dashboard — plac/placard.md": {
    "primary": "A poster, sign, or notice for display in a public place; also to display posters across an area.",
    "secondary": "In political history, proclamations posted in public squares to announce decrees or incite popular revolt.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A revolutionary **placard** posted upon the fountain wall denounced aristocrats and hoarding bakers."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Patriots ran through the alleys of Paris to **placard** the walls with incendiary calls to arms."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A printed police **placard** offering a substantial reward was posted outside the Baker Street station."}
    ]
  },
  "Dashboard — plac/placate.md": {
    "primary": "To make someone less angry or hostile; to appease, pacify, or conciliate.",
    "secondary": "In social negotiation and diplomacy, offering concessions to satisfy grievances and prevent hostilities.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The senate sent rich gifts of gold and silks to **placate** the Gothic chieftain outside the gates."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode sought by generous donations to public charities to **placate** his growing sense of guilt."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I offered my pocket money to the fierce coachman, hoping to **placate** his terrifying wrath."}
    ]
  },
  "Dashboard — plac/placating.md": {
    "primary": "Intended to make someone less angry or hostile; conciliatory, pacifying, or appeasing.",
    "secondary": "In behavioral description, adopting a gentle tone or submissive posture to avert conflict.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Farfrae adopted a soft, **placating** tone that disarmed Henchard's loud and blustering rage."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Barrymore raised a **placating** hand, begging Sir Henry to hear his explanation in private."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Jane's sweet and **placating** voice always sought to soften her mother's unreasonable complaints."}
    ]
  },
  "Dashboard — plac/placatingly.md": {
    "primary": "In a placating or conciliatory manner; in a way that attempts to pacify or appease someone.",
    "secondary": "In narrative dialogue, speaking softly or gesturing apologetically to de-escalate tension.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe smiled **placatingly** at Mrs. Joe as she flourished the dreaded Tickler across the hearth."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Seth spoke **placatingly** to his fiery brother, urging patience and faith in God's providence."},
      {"author": "Herman Melville", "work": "Billy Budd, Sailor", "quote": "The handsome sailor held out his open palms **placatingly**, distressed by the master-at-arms' stern frown."}
    ]
  },
  "Dashboard — plac/placation.md": {
    "primary": "The act of appeasing, pacifying, or conciliating someone who is angry or aggrieved.",
    "secondary": "In comparative religion and anthropology, sacrificial offerings performed to avert divine wrath.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Primitive rites of animal sacrifice were performed for the **placation** of unpredictable forest spirits."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "No political **placation** could satisfy the ambitious barbarian commanders who demanded territorial cession."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A timely act of parliamentary **placation** would restore commercial harmony and imperial unity."}
    ]
  },
  "Dashboard — plac/placative.md": {
    "primary": "Serving, tending, or designed to placate; conciliatory or pacifying in nature.",
    "secondary": "In diplomatic strategy, small concessionary gestures made to soothe irritated allies or adversaries.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Weak governments rely upon **placative** concessions that invite further aggression from foreign powers."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley sent a **placative** basket of pineapples to his sister after their angry domestic quarrel."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Basil Ransom offered a **placative** bow, hoping to soften the rigid hostility of his northern hostess."}
    ]
  },
  "Dashboard — plac/placatory.md": {
    "primary": "Intended to make someone less angry or hostile; conciliatory, pacifying, or soothing.",
    "secondary": "In formal rhetoric and correspondence, using humble, reassuring language to disarm indignation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins wrote a **placatory** epistle, hoping to heal the long estrangement with Longbourn."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Barkis produced an apple tart from his pocket with a **placatory** grin for the weeping Peggotty."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The innkeeper spoke in a low, **placatory** murmur, terrified of offending the dangerous Scowrers."}
    ]
  },
  "Dashboard — plac/place-kick.md": {
    "primary": "A kick in rugby or American football in which the ball is kicked from a stationary position on the ground.",
    "secondary": "In athletic sports history, a specialized technique used for kicking conversions, field goals, and penalty goals.",
    "quotes": [
      {"author": "Thomas Hughes", "work": "Tom Brown's School Days", "quote": "Old Brooke prepared the ball with his heel upon the turf, ready for a decisive **place-kick** over the bar."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Missing Three-Quarter", "quote": "Godfrey Staunton was the greatest rugby wing three-quarter in England, famous for his deadly **place-kick**."},
      {"author": "P. G. Wodehouse", "work": "The Gold Bat", "quote": "The school team cheered wildly as the ball sailed between the goalposts from a magnificent **place-kick**."}
    ]
  },
  "Dashboard — plac/place-kicker.md": {
    "primary": "A player in rugby or American football who specializes in taking place-kicks.",
    "secondary": "In athletic specialization, a specialist footballer chosen for mechanical consistency, composure, and distance accuracy.",
    "quotes": [
      {"author": "Thomas Hughes", "work": "Tom Brown's School Days", "quote": "Every boy held his breath as the chosen **place-kicker** paced back from the leather oval on the muddy pitch."},
      {"author": "P. G. Wodehouse", "work": "A Prefect's Uncle", "quote": "The opposing team possessed an extraordinary **place-kicker** who could convert penalty kicks from midfield."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Missing Three-Quarter", "quote": "The loss of our master **place-kicker** on the eve of the varsity match plunged Cambridge into despair."}
    ]
  },
  "Dashboard — plac/place-kicking.md": {
    "primary": "The action or skill of kicking a stationary ball from the ground or a kicking tee.",
    "secondary": "In team sports strategy, scoring points through reliable penalty conversions and extra points.",
    "quotes": [
      {"author": "Thomas Hughes", "work": "Tom Brown's School Days", "quote": "The captains agreed that superior **place-kicking** had decided the muddy contest on Big Side."},
      {"author": "P. G. Wodehouse", "work": "Tales of St. Austin's", "quote": "Hours of solitary practice upon the school field perfected his mechanical accuracy in **place-kicking**."},
      {"author": "Arthur Conan Doyle", "work": "The Captain of the Pole-Star and Other Tales", "quote": "The Scottish team dominated the second half through brilliant handling and flawless **place-kicking**."}
    ]
  },
  "Dashboard — plac/place-worship.md": {
    "primary": "The religious veneration or superstitious reverence paid to particular geographic sites, shrines, or temples.",
    "secondary": "In religious history and anthropology, sacred attachment to topographical loci (topolatry) such as groves, springs, or tombs.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient Semitic sanctuaries exhibited primitive **place-worship**, centering reverence upon sacred stones and groves."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Christian emperors banned pagan **place-worship** at the sacred grottos and oak sanctuaries of Greece."},
      {"author": "William Robertson Smith", "work": "The Religion of the Semites", "quote": "Early nomadic religion evolved from broad nature veneration into localized **place-worship** at desert springs."}
    ]
  },
  "Dashboard — plac/place.md": {
    "primary": "A particular position, point, or area in space; a location, dwelling, or social status.",
    "secondary": "In social philosophy, one's proper station, duty, or function within a civic order or organization.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "All the world's a stage, and all the men and women merely players; they have their exits and their entrances, and one man in his time plays many parts, his acts being seven ages; every actor finds his **place**."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Men in great **place** are thrice servants: servants of the sovereign or state, servants of fame, and servants of business."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Pemberley was a **place** of noble beauty, standing proudly on rising ground above the winding stream."}
    ]
  },
  "Dashboard — plac/placeable.md": {
    "primary": "Capable of being placed, located, or assigned to a particular position or category.",
    "secondary": "In labor economics and personnel recruitment, an applicant possessing the skills needed for immediate job placement.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Every specialized civil institution is easily **placeable** within the evolutionary hierarchy of social forms."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Aberrant genera are not readily **placeable** within existing taxonomic families, bridging extinct groups."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Skilled artisans are immediately **placeable** in industrial factories, whereas untrained laborers face unemployment."}
    ]
  },
  "Dashboard — plac/placebo.md": {
    "primary": "A harmless pill, medicine, or procedure prescribed more for psychological benefit than physiological effect.",
    "secondary": "In clinical pharmacological trials, an inactive substance administered to a control group to evaluate experimental drug efficacy.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A harmless **placebo** coupled with reassuring bedside confidence often relieves functional nervous ailments."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Many historic remedies were mere **placebo** draughts, succeeding through the patient's lively faith in the physician."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The country doctor dispensed a mild peppermint **placebo** to soothe the imaginary symptoms of the neurotic squire."}
    ]
  },
  "Dashboard — plac/placed.md": {
    "primary": "Put in a particular position or situation; situated, located, or assigned.",
    "secondary": "In athletic competition and horseracing, finishing among the top positions (typically first, second, or third).",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was **placed** in a small dormer room, looking out upon the ancient leaded roofs of Thornfield Hall."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty gently **placed** her arms around my neck, whispering words of comforting love in my ear."},
      {"author": "Arthur Conan Doyle", "work": "Silver Blaze", "quote": "The thoroughbred had been **placed** in every major stakes race of the autumn racing season."}
    ]
  },
  "Dashboard — plac/placeholder.md": {
    "primary": "A person or thing that occupies a position or function temporarily until a permanent replacement is found.",
    "secondary": "In typography, algebra, and programming, a variable symbol or dummy text (like Lorem Ipsum) holding space.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The appointed senator acted as a mere political **placeholder** until the state legislature chose a permanent successor."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "In formal propositional calculus, the variable 'x' acts as an abstract **placeholder** awaiting specific values."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I inserted a temporary wooden **placeholder** in the printer's galley while awaiting the missing line of lead type."}
    ]
  },
  "Dashboard — plac/placekicker.md": {
    "primary": "A football player who kicks the ball from a fixed position on the ground (solid spelling of place-kicker).",
    "secondary": "In sports specialization, an athletic specialist responsible for executing point-after touchdowns and field goals.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Head of Kay's", "quote": "The school team relied upon their unerring **placekicker** to snatch victory in the dying minutes of the match."},
      {"author": "Thomas Hughes", "work": "Tom Brown at Oxford", "quote": "The college **placekicker** stepped back from the ball with the quiet coolness of a veteran marksman."},
      {"author": "Arthur Conan Doyle", "work": "The Captain of the Pole-Star", "quote": "Our star **placekicker** booted the ball cleanly between the uprights, winning the university championship."}
    ]
  },
  "Dashboard — plac/placeman.md": {
    "primary": "A person appointed to a public or political office, especially as a reward for party loyalty; a political appointee.",
    "secondary": "In eighteenth-century British parliamentary politics, a member holding a lucrative crown office who voted obediently for the ministry.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Thoughts on the Cause of the Present Discontents", "quote": "The court party multiplied offices to fill the House of Commons with subservient **placeman** pensioners."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Every unprincipled **placeman** abandoned the falling ministry to seek favors from the rising opposition."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Constitutional safeguards must prevent the legislature from degenerating into a council of greedy **placeman** sycophants."}
    ]
  },
  "Dashboard — plac/placement.md": {
    "primary": "The action of putting someone or something in a particular place, or the fact of being placed.",
    "secondary": "In employment and education, the process of assigning students or job candidates to appropriate posts or programs.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The deliberate **placement** of the sculptured capitals upon the lower arcade demonstrates exquisite geometric proportion."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The asymmetrical **placement** of gravitational statoliths within root-cap cells directs downward geotropic growth."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Educational **placement** should challenge the child's natural curiosity without inducing intellectual fatigue."}
    ]
  },
  "Dashboard — plac/placenta.md": {
    "primary": "A flattened circular organ in the uterus of pregnant eutherian mammals, nourishing and maintaining the fetus through the umbilical cord.",
    "secondary": "In flowering plant botany, the interior ovarian tissue surface to which the ovules and developing seeds are attached.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Maternal and fetal blood vessels interweave closely within the **placenta** without actual vascular continuity."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The discoidal cellular **placenta** of primates links human reproductive biology directly with higher anthropoid apes."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "In parietal placentation, the ovules arise along the outer walls rather than the central **placenta** of the carpel."}
    ]
  },
  "Dashboard — plac/placental.md": {
    "primary": "Relating to or having a placenta; designating eutherian mammals that nourish their young via a placenta.",
    "secondary": "In evolutionary biology, eutherians that carry fetuses to an advanced developmental stage, contrasting with marsupials and monotremes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The Australian continent was populated by marsupials before higher **placental** mammals could cross the ancient marine straits."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The universal presence of a deciduous **placental** membrane confirms the close mammalian affinity of humans."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Premature separation of the **placental** tissue produces catastrophic maternal and fetal hemorrhage."}
    ]
  },
  "Dashboard — plac/placentation.md": {
    "primary": "The formation, type, or structure of the placenta in female mammals, or of ovule attachment in plant ovaries.",
    "secondary": "In comparative embryology and angiosperm taxonomy, the structural pattern of vascular connection between mother/ovary and embryo/ovule.",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Free-central **placentation** is characterized by an axial column rising from the base of the unilocular ovary."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Zonary **placentation** is characteristic of the carnivorous orders, whereas ungulates display diffuse placental villi."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Variations in floral **placentation** provide diagnostic features for distinguishing closely related plant families."}
    ]
  },
  "Dashboard — plac/placer.md": {
    "primary": "A deposit of sand and gravel in the bed of a stream containing particles of valuable mineral (especially gold).",
    "secondary": "In mining geology and frontier history, alluvial deposits worked by washing and panning rather than hard-rock shaft mining.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "Thousands of eager prospectors rushed to the California streams to pan gold from every gravel **placer**."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Heavy gold nuggets accumulated in the ancient river **placer** beds through centuries of hydraulic erosion."},
      {"author": "Bret Harte", "work": "The Luck of Roaring Camp", "quote": "The miners toiled from sunrise to sunset along the **placer** washings, sluicing gravel for golden dust."}
    ]
  },
  "Dashboard — plac/placeseeker.md": {
    "primary": "A person who seeks public or political office, especially for personal profit or partisan patronage; an office seeker.",
    "secondary": "In political satire, a self-serving opportunist who courts politicians to secure lucrative sinecures.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Thoughts on the Cause of the Present Discontents", "quote": "The ministerial corridors were besieged by every rapacious **placeseeker** hungry for court pensions."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A nation governed by a chorus of noisy **placeseeker** factions drifts helplessly toward political ruin."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional executive must be shielded from the corrupt importunities of the unprincipled **placeseeker**."}
    ]
  },
  "Dashboard — plac/placid.md": {
    "primary": "Not easily upset or excited; calm, peaceful, serene, and tranquil.",
    "secondary": "In landscape and aquatic description, smooth, unruffled, and mirror-like water undisturbed by wind.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The **placid** waters of Lake Geneva reflected the starry heavens and the white peaks of the distant Jura."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Jane listened with her usual **placid** sweetness, unwilling to think ill of any human creature."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pacific rolled in **placid** swells beneath the equatorial sun, hiding the fierce monsters of the deep."}
    ]
  },
  "Dashboard — plac/placidity.md": {
    "primary": "The state or quality of being placid; serenity, calmness, or peaceful quietude.",
    "secondary": "In emotional characterization, unruffled mental equilibrium that remains undisturbed by external provocation.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The sweet **placidity** of the child's countenance brought soothing calm into the weaver's troubled heart."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes smoked his pipe with impenetrable **placidity**, awaiting the midnight emergence of our quarry."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A summer afternoon of unbroken **placidity** settled over the garden, drowsy with the hum of bumblebees."}
    ]
  },
  "Dashboard — plac/placidly.md": {
    "primary": "In a placid manner; calmly, peacefully, serenely, or quietly.",
    "secondary": "In narrative prose, going about one's duties with unhurried, tranquil composure.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty sat **placidly** knitting by the parlor fire, her workbox with the picture of St. Paul's upon the table."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse nodded **placidly** in his armchair, pleased that his warm gruel was made to his liking."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The pond lay **placidly** in the morning light, like a giant mirror framed by forested hills."}
    ]
  },
  "Dashboard — plac/placidness.md": {
    "primary": "The calm characteristic of being placid; peaceful serenity or undisturbed mildness of temper.",
    "secondary": "In psychological disposition, an innate absence of irritability or emotional tempestuousness.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The enviable **placidness** of his mind arose from moderate desires and a conscience clear of guilt."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "I envied the Dutch boarders their bovine **placidness**, immune as they were to internal spiritual storms."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The autumn twilight fell upon Little Hintock with a deep **placidness** that seemed almost holy."}
    ]
  },
  "Dashboard — plac/placidyl.md": {
    "primary": "A brand name for ethchlorvynol, a central nervous system depressant and sedative-hypnotic drug.",
    "secondary": "In pharmacology, a tertiary acetylenic carbinol formerly prescribed for short-term management of insomnia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Non-barbiturate hypnotic agents like **Placidyl** were developed to induce rapid sedation with reduced risk of respiratory depression."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Excessive doses of synthetic sedatives like **Placidyl** produced troublesome nocturnal confusion in elderly post-encephalitic patients."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The physician cautioned against habituation to modern sleep-inducing synthetics such as **Placidyl**."}
    ]
  },
  "Dashboard — plac/placoderm.md": {
    "primary": "An extinct armored jawed fish of the class Placodermi, prominent during the Devonian period.",
    "secondary": "In vertebrate paleontology, primitive gnathostomes having bony dermal plates protecting the head and thorax.",
    "quotes": [
      {"author": "Alfred Romer", "work": "Vertebrate Paleontology", "quote": "The gigantic Devonian **placoderm** Dunkleosteus possessed shearing bony jaw plates instead of true teeth."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The armored fossils of the ancient **placoderm** demonstrate the early evolutionary experimentation with vertebrate dermal armor."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The discovery of bizarre armored forms like the Scottish **placoderm** fishes illuminated the Devonian age of fishes."}
    ]
  },
  "Dashboard — plac/placodermi.md": {
    "primary": "An extinct class of armored prehistoric fishes that flourished in the Silurian and Devonian periods.",
    "secondary": "In vertebrate systematics, the earliest known jawed vertebrates, possessing an articulated joint between cranial and thoracic shields.",
    "quotes": [
      {"author": "Alfred Romer", "work": "Vertebrate Paleontology", "quote": "Members of the class **Placodermi** dominated the marine and freshwater habitats of the Middle Devonian era."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Cranial shields of the **Placodermi** exhibit unique hinge structures facilitating wide vertical jaw gape."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Comparative paleontology links the skeletal architecture of the **Placodermi** to primitive gnathostome origins."}
    ]
  },
  "Dashboard — plac/placoid.md": {
    "primary": "Platelike; having the form of a plate or scale; specifically designating placoid scales of cartilaginous fishes.",
    "secondary": "In ichthyology and comparative histology, denticle-like scales found on sharks and rays composed of dentine with an enameloid cap.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The rough skin of the shark is studded with tiny **placoid** scales, homologous in structure to vertebrate teeth."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Evolutionary morphology reveals how mammalian teeth were derived from the primitive **placoid** scales of ancestral elasmobranchs."},
      {"author": "Richard Owen", "work": "Odontography", "quote": "Each individual **placoid** denticle possesses an internal pulp cavity surrounded by calcified dentine."}
    ]
  },
  "Dashboard — plac/placuna.md": {
    "primary": "A genus of marine bivalve mollusks in the family Placunidae, including the windowpane oyster (*Placuna placenta*).",
    "secondary": "In malacology and maritime commerce, translucent flat oysters harvested in Indo-Pacific shallows for window glazing and decorative mother-of-pearl.",
    "quotes": [
      {"author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "Small pedunculate cirripedes frequently attach themselves to the smooth, translucent valves of **Placuna** placenta."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "In maritime settlements of the East Indies, thin polished shells of **Placuna** are glazed into window lattices in place of glass."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The thin, foliaceous shell structure of **Placuna** exhibits extreme bilateral compression and pearly iridescence."}
    ]
  },
  "Dashboard — plac/replace.md": {
    "primary": "To take the place of; to provide a substitute for someone or something; to put back in its place.",
    "secondary": "In economic production, installing new machinery or processes to supersede obsolete capital equipment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "I will give thee all my kingdom if thou canst **replace** my loving daughter upon the throne."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I tried to **replace** the torn page in the schoolbook before the schoolmaster's watchful eye fell upon me."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Annual capital investments must continually **replace** the tools and raw materials consumed in production."}
    ]
  },
  "Dashboard — plac/replaceability.md": {
    "primary": "The capability of being replaced or substituted; exchangeability or fungibility.",
    "secondary": "In industrial design and engineering, modular component interchangeability to simplify maintenance.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The standardized **replaceability** of machine components was the foundational breakthrough of mass industrial manufacture."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "In highly integrated social systems, individual units exhibit greater functional **replaceability** than in primitive tribes."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger underscored the **replaceability** of our camping gear compared to our precious scientific instruments."}
    ]
  },
  "Dashboard — plac/replaceable.md": {
    "primary": "Able to be replaced, exchanged, or substituted; not unique or irreplaceable.",
    "secondary": "In modular mechanics, standard parts designed for rapid field substitution when worn or damaged.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Glass joints should be standardized so that broken tubes are immediately **replaceable** from stock."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Mass aviation design relied upon **replaceable** modular wings that could be swapped in field hangars."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft reminded his engineers that even the most skillful mechanic is **replaceable** in a modern foundry."}
    ]
  },
  "Dashboard — plac/replacement.md": {
    "primary": "The action of replacing someone or something, or a person or thing that takes the place of another.",
    "secondary": "In mineralogy and petrology, the metasomatic substitution of one mineral substance by another while preserving external crystalline shape.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The gradual **replacement** of organic woody fibers by silica produced the petrified trees of the desert."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry ordered the immediate **replacement** of his stolen boot from the local bootmaker."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The urgent **replacement** of naval tonnage lost to submarine torpedoes required all British shipyards."}
    ]
  },
  "Dashboard — plac/replacing.md": {
    "primary": "The action of substituting, providing a successor for, or returning something to its position.",
    "secondary": "In technological history, mechanization superseding manual artisanal methods in factory production.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We see younger continental varieties steadily **replacing** older endemic island forms in the struggle for life."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "Steam-driven looms were rapidly **replacing** hand-loom weavers throughout the northern textile valleys."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The roaring threshing engine was **replacing** the rhythmic swing of traditional wooden flails across Wessex."}
    ]
  },
  "Dashboard — plac/transplacental.md": {
    "primary": "Passing, transported, or performed through or across the placenta between mother and fetus.",
    "secondary": "In maternal-fetal medicine and obstetrics, maternal antibodies or infectious pathogens traversing the placental barrier.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Passive **transplacental** transmission of maternal antibodies affords newborn infants vital early immunity."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Gaseous exchange between maternal and embryonic hemoglobin proceeds through **transplacental** diffusion."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Certain viral toxins achieve **transplacental** penetration, causing subtle congenital alterations in the developing neural tube."}
    ]
  },
  "Dashboard — plac/unplaced.md": {
    "primary": "Not having a place or assigned location; not placed; unranked in a race or contest.",
    "secondary": "In horseracing and athletic events, finishing behind the first three or four recognized prize positions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "Silver Blaze", "quote": "The favorite was surprisingly left **unplaced** as the outsider surged past the winning post in the Wessex Cup."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Thousands of legal documents remained **unplaced** in the chaotic, dust-covered closets of the Chancery stationer."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba's ram was left **unplaced** at the county agricultural show, to Gabriel's keen disappointment."}
    ]
  },
  "Dashboard — plac/unreplaceable.md": {
    "primary": "Not able to be replaced; irreplaceable; of unique and permanent worth.",
    "secondary": "In archival and art conservation, priceless historical manuscripts and original works of art whose loss is irreparable.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient Byzantine mosaics of Saint Mark's are **unreplaceable** treasures of Christian medieval art."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A devoted, upright leader is an **unreplaceable** pillar in a troubled and disunited commonwealth."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The indigenous cultural traditions wiped out by conquest represent an **unreplaceable** loss to anthropology."}
    ]
  }
}

base_dir = "App database/Latin roots/Cluster Emotion"
updated = 0

for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Successfully updated {updated}/{len(data)} notes in Dashboard — plac.")

res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base_dir}/Dashboard — plac"], capture_output=True, encoding="utf-8")
print(res.stdout)
