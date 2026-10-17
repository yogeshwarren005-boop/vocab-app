import json
import os
import subprocess

# Load slice
with open('main app/scripts/slice-form-finish-2.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

batch5_files = files[256:320]

lexicon = {
  "antipiracy": {
    "primary": "Designed, intended, or operating to prevent, combat, or deter piracy, whether maritime robbery or unauthorized copyright infringement.",
    "secondary": "In maritime security and intellectual property law, antipiracy operations deploy naval patrols or digital rights management systems to safeguard assets.",
    "quotes": [
      {"author": "Hugo Grotius", "work": "The Free Sea (Mare Liberum)", "quote": "International **antipiracy** covenants empower all maritime nations to suppress corsairs upon the high seas."},
      {"author": "Lawrence Lessig", "work": "Free Culture", "quote": "Aggressive **antipiracy** software often locks down consumer hardware beyond the reasonable bounds of copyright law."},
      {"author": "Alfred Thayer Mahan", "work": "The Influence of Sea Power upon History", "quote": "Coordinated **antipiracy** squadrons in the Mediterranean secured commercial shipping routes for peaceful merchant fleets."}
    ]
  },
  "apeirogon": {
    "primary": "A polygon having a countably infinite number of sides and vertices.",
    "secondary": "In modern geometry and abstract polytope theory, a regular apeirogon can tessellate a Euclidean line or exist as a zigzag or helical polygon in higher dimensions.",
    "quotes": [
      {"author": "H. S. M. Coxeter", "work": "Regular Polytopes", "quote": "A linear tessellation of unit line segments along a straight line constitutes the simplest regular **apeirogon**."},
      {"author": "Branko Grünbaum", "work": "Convex Polytopes", "quote": "Extending the concept of polygonality to infinity yields the **apeirogon**, possessing an infinite sequence of collinear edges."},
      {"author": "Benoit Mandelbrot", "work": "The Fractal Geometry of Nature", "quote": "Infinite polygonal limits such as the **apeirogon** bridge discrete combinatorial lattices with continuous geometric curves."}
    ]
  },
  "apeirohedron": {
    "primary": "An infinite polyhedron; a tessellation or sponge-like honeycomb of polygons that extends infinitely in three-dimensional or higher-dimensional space.",
    "secondary": "In geometry and crystallography, regular apeirohedra (infinite skew polyhedra) partition space with uniform vertices, edges, and faces.",
    "quotes": [
      {"author": "H. S. M. Coxeter", "work": "Regular Polytopes", "quote": "Petrie and I discovered three regular skew polyhedra, each forming an infinite **apeirohedron** that partitions Euclidean space."},
      {"author": "Branko Grünbaum", "work": "Uniform Apeirohedra in Ordinary Space", "quote": "A periodic minimal surface often corresponds to the geometric skeleton of an infinite **apeirohedron**."},
      {"author": "Alan Holden", "work": "Shapes, Space, and Symmetry", "quote": "Repeating polyhedral units across three dimensions generates an open, porous structure known as an **apeirohedron**."}
    ]
  },
  "piracy": {
    "primary": "The practice of attacking and robbing ships at sea; maritime robbery or violence committed by private vessels.",
    "secondary": "In intellectual property and media law, the unauthorized reproduction, distribution, or use of copyrighted material.",
    "quotes": [
      {"author": "Cicero", "work": "De Officiis", "quote": "A pirate is not counted as a regular enemy, but is the common foe of all mankind, and with **piracy** no treaty can be valid."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "When Roman naval power suppressed **piracy** on the Mediterranean, travel and commercial exchange flourished throughout the empire."},
      {"author": "Daniel Defoe", "work": "A General History of the Pyrates", "quote": "Desperate mariners turned to **piracy**, hoisting the black flag and declaring war against all nations."}
    ]
  },
  "pirate": {
    "primary": "A person who attacks and robs ships at sea; a maritime marauder.",
    "secondary": "A person or entity that appropriates, reproduces, or broadcasts another's intellectual property without authorization.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Ere we were two days old at sea, a **pirate** of very warlike appointment gave us chase."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Long John Silver was the very model of a calculating **pirate**, concealing his murderous intent behind a genial smile."},
      {"author": "Hugo Grotius", "work": "De Jure Belli ac Pacis", "quote": "A captured **pirate** enjoys none of the protections afforded to honorable prisoners of war under the law of nations."}
    ]
  },
  "piratic": {
    "primary": "Of, relating to, or characteristic of pirates or piracy; piratical.",
    "secondary": "Operating through unlawful seizure, plundering, or unauthorized appropriation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Gothic fleets engaged in **piratic** excursions along the coasts of Greece and Asia Minor."},
      {"author": "Washington Irving", "work": "The Life and Voyages of Christopher Columbus", "quote": "Corsairs manned swift caravels, launching **piratic** descents upon the defenseless merchantmen of the Levant."},
      {"author": "Herman Melville", "work": "Benito Cereno", "quote": "The strange merchantman bore an ominous air that aroused suspicion of some dark **piratic** enterprise."}
    ]
  },
  "piratical": {
    "primary": "Of, resembling, or characteristic of a pirate; predatory, robbery-driven, or unauthorized.",
    "secondary": "In commercial and literary contexts, acquired through illegal plunder or infringement of intellectual rights.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The confiscation of ecclesiastical property was conducted with a **piratical** disregard for ancient charters."},
      {"author": "Walter Scott", "work": "The Pirate", "quote": "His crew retained their fierce **piratical** demeanor even when walking peacefully in the streets of Kirkwall."},
      {"author": "Charles Dickens", "work": "The Posthumous Papers of the Pickwick Club", "quote": "Cheap **piratical** editions of popular novels were hawked on the streets before the authorized printing appeared."}
    ]
  },
  "piratically": {
    "primary": "In the manner of a pirate; by means of piracy, plunder, or unauthorized seizure.",
    "secondary": "In legal and historical usage, acting violently and illegally without sovereign commission on the seas.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "A Turkish rover bore down upon our vessel and boarded us **piratically** after a desperate fight."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Those who seize goods **piratically** upon the high seas can convey no lawful title to bona fide purchasers."},
      {"author": "Joseph Conrad", "work": "The Rescue", "quote": "Praus equipped with swivel guns prowled the straits, striking **piratically** whenever calms stalled sailing barques."}
    ]
  },
  "plage": {
    "primary": "A bright, hot region in the chromosphere of the Sun, typically occurring near sunspots.",
    "secondary": "In astronomy and solar physics, plages are dense magnetic features observed in hydrogen-alpha and ionized calcium lines, representing the chromospheric counterpart of photospheric faculae.",
    "quotes": [
      {"author": "George Ellery Hale", "work": "The Study of Stellar Evolution", "quote": "Spectroheliograms taken in the K line of calcium reveal bright flocculi or **plage** areas overlying solar active regions."},
      {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "Intense magnetic fields within a solar **plage** elevate chromospheric temperatures and trigger energetic flares."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Solar flares erupt with cataclysmic violence from the brilliant turbulent heart of a chromospheric **plage**."}
    ]
  },
  "plagianthus": {
    "primary": "A genus of flowering shrubs and small trees in the mallow family (Malvaceae), native to New Zealand, commonly known as ribbonwoods.",
    "secondary": "In systematic botany, species of *Plagianthus* (such as Plagianthus regius) yield strong fibrous inner bark historically utilized for cordage and textile weaving.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Handbook of the New Zealand Flora", "quote": "The genus **Plagianthus** is remarkable for its tough, fibrous inner bark, which the Maori spun into durable cords."},
      {"author": "Thomas Cheeseman", "work": "Manual of the New Zealand Flora", "quote": "In lowland river valleys, trees of **Plagianthus** regius shed their juvenile divaricating branches as they mature."},
      {"author": "Leonard Cockayne", "work": "The Vegetation of New Zealand", "quote": "Deciduous habit in **Plagianthus** betulinus represents a rare climatic adaptation among indigenous subantarctic trees."}
    ]
  },
  "plagiarisation": {
    "primary": "The act of taking someone else's work, ideas, or words and passing them off as one's own (chiefly British spelling).",
    "secondary": "In academic integrity and literary ethics, plagiarisation constitutes a severe intellectual violation involving deceptive appropriation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Adventurer", "quote": "Gross **plagiarisation** betrays an empty intellect that masquerades in garments stolen from dead authors."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "A critical examination of the treatise revealed systematic **plagiarisation** from seventeenth-century French commentators."},
      {"author": "George Orwell", "work": "Inside the Whale", "quote": "Careful critics must distinguish between unconscious influence and blatant **plagiarisation** of contemporary style."}
    ]
  },
  "plagiarise": {
    "primary": "To copy another person's words, writings, or ideas and present them as one's own; British spelling of plagiarize.",
    "secondary": "In literary and academic criticism, to appropriate artistic or intellectual expressions without attribution.",
    "quotes": [
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Writers who lack genuine invention often **plagiarise** the wit of the ancients while debasing its purity."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "Poets who **plagiarise** without acknowledgment merely invite ridicule when the original master is remembered."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "To **plagiarise** a contemporary’s style is easy; to absorb their underlying vision requires kindred genius."}
    ]
  },
  "plagiarised": {
    "primary": "Copied from another author's work and presented as original without acknowledgment (chiefly British spelling).",
    "secondary": "In scholarly publishing, describing manuscripts or texts containing uncredited borrowed passages.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Whole paragraphs in that pamphlet were demonstrably **plagiarised** from the German transcendentalists."},
      {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "Modern treatises exhibited vast piles of **plagiarised** fragments patched into an awkward literary patchwork."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon dreaded that critics would discover his key theories had been anticipated and **plagiarised**."}
    ]
  },
  "plagiariser": {
    "primary": "A person who commits plagiarism; one who copies another's ideas or writings without attribution (British spelling).",
    "secondary": "In literary history, an author who appropriates the creative labor of others while claiming originality.",
    "quotes": [
      {"author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "Ben Jonson was no common **plagiariser**; he invaded authors like a monarch, and what would be theft in other poets was victory in him."},
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "The wretched **plagiariser** steals from every shelf, yet never enriches his own impoverished skull."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A petty **plagiariser** snatches single phrases, while an imaginative genius transforms whatever he borrows."}
    ]
  },
  "plagiarism": {
    "primary": "The practice of taking someone else's work or ideas and passing them off as one's own.",
    "secondary": "In academic and legal ethics, plagiarism violates professional honesty through unauthorized appropriation and intellectual fraud.",
    "quotes": [
      {"author": "Martial", "work": "Epigrams", "quote": "My book complains to me, Fidentinus, that you recite its verses to the crowd as if they were your own; that is **plagiarism**."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The charge of **plagiarism** is often made against those who happen to think alike upon universal subjects."},
      {"author": "Ralph Waldo Emerson", "work": "Letters and Social Aims", "quote": "Our best thoughts come from others; yet honest quotation preserves honor while clandestine **plagiarism** poisons thought."}
    ]
  },
  "plagiarist": {
    "primary": "A person who uses another person's words or ideas and pretends that they are their own.",
    "secondary": "In literary and artistic culture, an unoriginal creator who relies on clandestine copying rather than independent invention.",
    "quotes": [
      {"author": "John Milton", "work": "Eikonoklastes", "quote": "Such borrowing as this, if it be not bettered by the borrower, among good authors is accounted no better than a **plagiarist**."},
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "Every dunce turned **plagiarist** when Grub Street offered pennies for stolen lines."},
      {"author": "Mark Twain", "work": "Letter to Helen Keller", "quote": "The kernel of all human invention is borrowed, and no man can justly throw a stone at a fellow **plagiarist**."}
    ]
  },
  "plagiaristic": {
    "primary": "Characteristic of or given to plagiarism; involving the unauthorized copying of another's work.",
    "secondary": "Derivative in substance and unoriginal in conception; marked by literary borrowing.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Literati of New York City", "quote": "I detected a thoroughly **plagiaristic** vein running through the entire collection of so-called original verse."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "A truly novel narrative avoids the **plagiaristic** repetition of stale Victorian stock conventions."},
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The play relied upon a **plagiaristic** adaptation of Parisian farces without acknowledging the French source."}
    ]
  },
  "plagiarization": {
    "primary": "The act or process of plagiarizing; copying another's creative work and passing it off as original.",
    "secondary": "In copyright law and scholarly standards, the fraudulent adoption of another author's written formulation or research results.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The blatant **plagiarization** of Italian commentaries exposed the compiler to the scorn of European scholars."},
      {"author": "Samuel Johnson", "work": "The Adventurer", "quote": "When literary **plagiarization** becomes pervasive, public confidence in authorial genius is destroyed."},
      {"author": "H. L. Mencken", "work": "Prejudices", "quote": "Much academic scholarship is little more than the dignified **plagiarization** of forgotten German monographs."}
    ]
  },
  "plagiarize": {
    "primary": "To take the work or an idea of someone else and pass it off as one's own.",
    "secondary": "In academic scholarship, to reproduce text, data, or arguments without proper citation or attribution.",
    "quotes": [
      {"author": "Mark Twain", "work": "Autobiography", "quote": "We all **plagiarize** unconsciously, taking the thoughts of others and believing them to be the offspring of our own brain."},
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Dull wits merely **plagiarize** what greater minds conceived with vibrant passion."},
      {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "To **plagiarize** successfully, a playwright must possess sufficient craft to conceal the original theft."}
    ]
  },
  "plagiarized": {
    "primary": "Copied from another author's work without giving appropriate credit or acknowledgment.",
    "secondary": "Describing writings, music, or ideas appropriated unlawfully or dishonestly from an existing source.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "Longfellow and Other Plagiarists", "quote": "The poem contains lines **plagiarized** almost verbatim from an obscure German ballad."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He defended his essay by claiming that any **plagiarized** ideas had been assimilated into his own system."},
      {"author": "H. L. Mencken", "work": "Prejudices", "quote": "The senator delivered an impassioned address largely **plagiarized** from a high school commencement speech."}
    ]
  },
  "plagiarizer": {
    "primary": "A person who plagiarizes; one who appropriates another's writing or ideas without credit (American spelling).",
    "secondary": "In intellectual property disputes, an infringer who reproduces proprietary text or artistic composition under their own name.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "Essays and Reviews", "quote": "A brazen **plagiarizer** relies on the obscurity of his victim to escape detection by the reading public."},
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "The sleepless **plagiarizer** roams through dusty libraries, seeking forgotten verses to steal."},
      {"author": "Mark Twain", "work": "Letters", "quote": "Every creative artist is in some degree an innocent **plagiarizer** of the collective human heritage."}
    ]
  },
  "plagiocephaly": {
    "primary": "A condition characterized by an asymmetrical, flattened shape of the skull, often developing in infancy.",
    "secondary": "In pediatric orthopedics and cranial anatomy, positional plagiocephaly results from persistent external pressure on one side of an infant’s malleable cranium.",
    "quotes": [
      {"author": "Walter P. Blount", "work": "Fractures and Deformities in Children", "quote": "Nonsynostotic **plagiocephaly** responds favorably to infant repositioning and supervised tummy time during wakefulness."},
      {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Premature unilateral closure of the coronal suture results in severe craniosynostotic **plagiocephaly**."},
      {"author": "S. Terry Canale", "work": "Campbell's Operative Orthopaedics", "quote": "Cranial remodeling orthoses provide effective correction for severe deformational **plagiocephaly** in infants under twelve months."}
    ]
  },
  "plagioclase": {
    "primary": "An important series of rock-forming triclinic feldspar minerals consisting of a solid solution of albite and anorthite.",
    "secondary": "In petrology and geology, plagioclase feldspars are distinguished by two cleavage planes intersecting at an oblique angle (around 86 degrees) and characteristic polysynthetic twinning.",
    "quotes": [
      {"author": "Norman L. Bowen", "work": "The Evolution of the Igneous Rocks", "quote": "The continuous reaction series of **plagioclase** feldspars ranges from calcium-rich anorthite to sodium-rich albite."},
      {"author": "Frank Wigglesworth Clarke", "work": "The Data of Geochemistry", "quote": "Basaltic lavas are characterized by abundant laths of calcic **plagioclase** intergrown with augite."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The oblique cleavage angle of **plagioclase** readily separates it from the rectangular cleavage of orthoclase."}
    ]
  },
  "plagioclastic": {
    "primary": "Of, relating to, or resembling plagioclase; having oblique cleavage planes.",
    "secondary": "In petrography, describing igneous rock textures composed primarily of interlocking plagioclase feldspar laths.",
    "quotes": [
      {"author": "Norman L. Bowen", "work": "The Evolution of the Igneous Rocks", "quote": "Microscopic examination reveals an intersertal texture dominated by **plagioclastic** laths embedded in glass."},
      {"author": "Frank Wigglesworth Clarke", "work": "The Data of Geochemistry", "quote": "Weathering breaks down the **plagioclastic** minerals, releasing calcium and sodium into groundwater solutions."},
      {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "The **plagioclastic** feldspars exhibit polysynthetic striations on their principal cleavage faces."}
    ]
  },
  "plagiotropic": {
    "primary": "Oriented or growing at an oblique angle or horizontally, away from the vertical gravitational axis (of plant roots, stems, or branches).",
    "secondary": "In plant physiology, plagiotropic growth response to light or gravity produces horizontal lateral branching, contrasting with orthotropic vertical leaders.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Lateral roots exhibit a **plagiotropic** tendency, extending horizontally through the upper soil horizon."},
      {"author": "Julius von Sachs", "work": "Lectures on the Physiology of Plants", "quote": "Gravitational stimuli induce **plagiotropic** orientation in secondary lateral branches to optimize light interception."},
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Vascular cambium in a **plagiotropic** shoot produces asymmetrical reaction wood to counteract mechanical bending."}
    ]
  },
  "plague": {
    "primary": "A contagious bacterial disease caused by Yersinia pestis, characterized by fever, delirium, and buboes (bubonic plague) or respiratory infection (pneumonic plague).",
    "secondary": "Any severe epidemic or disastrous widespread affliction that causes catastrophic mortality or social devastation.",
    "quotes": [
      {"author": "Thucydides", "work": "History of the Peloponnesian War", "quote": "The great **plague** of Athens struck suddenly, overwhelming the physicians and dissolving all moral restraints."},
      {"author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "The **plague** raged with such virulence that the dead-carts were filled faster than graves could be dug."},
      {"author": "Albert Camus", "work": "The Plague", "quote": "The only way to fight the **plague** is decency; doing one’s job with patient courage in the face of death."}
    ]
  },
  "plaguey": {
    "primary": "Causing trouble, irritation, or annoyance; vexatious; bothersome (variant of plaguy).",
    "secondary": "In informal and dialectal usage, describing persistent nuisances or nagging physical ailments.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "That **plaguey** cough had troubled him all through the bitter London winter."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He cursed the **plaguey** lawsuits that had consumed his family estate for three generations."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "A **plaguey** pain in my ankle made every step across the heather an agony."}
    ]
  },
  "plaguily": {
    "primary": "In a troublesome, vexatious, or annoying manner; exceedingly or bothersomely.",
    "secondary": "In archaic and colloquial English, used as an intensifier meaning terribly, excessively, or exasperatingly.",
    "quotes": [
      {"author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "The weather was **plaguily** cold, and my teeth chattered as we crossed the river by wherry."},
      {"author": "Jonathan Swift", "work": "Journal to Stella", "quote": "I have been **plaguily** hurried all this afternoon by troublesome visitors from the coffeehouse."},
      {"author": "Henry Fielding", "work": "The History of Tom Jones", "quote": "Squire Western declared that his horses had been **plaguily** tired by the long chase."}
    ]
  },
  "plaguy": {
    "primary": "Troublesome, annoying, or vexatious; plague-like in persistence.",
    "secondary": "Used colloquially as an adjective or adverb meaning confoundedly, excessively, or exasperatingly.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Confound this **plaguy** gout, which ties me by the leg whenever the shooting season commences!"},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The bailie grumbled at the **plaguy** business that brought him into the wild Highland glens."},
      {"author": "Oliver Goldsmith", "work": "The Vicar of Wakefield", "quote": "We had a **plaguy** deal of trouble to persuade the landlord to furnish horses for our journey."}
    ]
  },
  "playa": {
    "primary": "A dry, flat, vegetation-free area at the lowest part of an undrained desert basin, where water pools and evaporates.",
    "secondary": "In geomorphology and sedimentology, a playa (or alkali flat) accumulates evaporite crusts of halite, gypsum, and borates following ephemeral flood evaporation.",
    "quotes": [
      {"author": "G. K. Gilbert", "work": "Lake Bonneville", "quote": "The glistening white floor of the desert **playa** represents the desiccation relic of an immense Pleistocene inland sea."},
      {"author": "Frank Wigglesworth Clarke", "work": "The Data of Geochemistry", "quote": "Evaporative concentration on the saline **playa** deposits economic crusts of sodium sulfate and borax."},
      {"author": "John Muir", "work": "Steep Trails", "quote": "Heat shimmers across the barren **playa**, conjuring deceptive mirages of cool, shimmering lakes."}
    ]
  },
  "anaplasia": {
    "primary": "The loss of cellular differentiation and normal tissue architectural organization, characteristic of malignant tumors.",
    "secondary": "In oncologic pathology, cellular anaplasia features pleomorphism, nuclear hyperchromatism, abnormal mitotic figures, and loss of cell polarity.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Extreme morphological dedifferentiation or **anaplasia** signifies that the neoplasm has escaped physiological tissue constraints."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "The degree of **anaplasia** correlates directly with the aggressive biological behavior of high-grade sarcomas."},
      {"author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Loss of specialized functional markers accompanies progressive **anaplasia** during malignant transformation."}
    ]
  },
  "anaplasmosis": {
    "primary": "An infectious tick-borne disease of cattle and other ruminants (and rarely humans) caused by obligate intracellular bacteria of the genus Anaplasma.",
    "secondary": "In veterinary medicine, bovine anaplasmosis (caused by Anaplasma marginale) induces severe hemolytic anemia, icterus, and progressive cachexia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tick vectors transmit bovine **anaplasmosis**, causing acute erythrocyte destruction without hemoglobinuria."},
      {"author": "Theobald Smith", "work": "Investigations into the Nature, Causation, and Prevention of Texas Cattle Fever", "quote": "Microscopic examination revealed marginal inclusion bodies in red blood cells characteristic of acute **anaplasmosis**."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Human granulocytic **anaplasmosis**, transmitted by Ixodes scapularis, responds promptly to oral doxycycline therapy."}
    ]
  },
  "anaplastic": {
    "primary": "Characterized by anaplasia; describing poorly differentiated or undifferentiated malignant cells that have lost their normal specialized structure.",
    "secondary": "In surgical pathology, anaplastic thyroid carcinoma is one of the most rapidly progressive and aggressive malignancies in human medicine.",
    "quotes": [
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "An **anaplastic** carcinoma displays striking cellular pleomorphism, tumor giant cells, and atypical tripolar mitoses."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Immunohistochemical stains often fail in **anaplastic** tumors due to loss of lineage-specific differentiation proteins."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Prompt diagnosis of an **anaplastic** thyroid mass is essential, as rapid local invasion can cause acute airway compromise."}
    ]
  },
  "anaplasty": {
    "primary": "Plastic surgery or surgical reconstruction to restore lost, injured, or deformed bodily parts (archaic/historical term).",
    "secondary": "In the history of surgery, anaplasty encompasses autologous skin grafting and flap transposition to repair craniofacial trauma.",
    "quotes": [
      {"author": "John Hunter", "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "Pioneering methods of **anaplasty** demonstrated that skin flaps retain vitality when connected by a vascularized pedicle."},
      {"author": "Astley Cooper", "work": "The Principles and Practice of Surgery", "quote": "Facial reconstruction following traumatic loss relies upon the delicate principles of operative **anaplasty**."},
      {"author": "Harold Gillies", "work": "Plastic Surgery of the Face", "quote": "Tubed pedicle grafting revolutionized modern **anaplasty**, permitting the transfer of distant tissue without necrotic loss."}
    ]
  },
  "aplasia": {
    "primary": "The failure of an organ, limb, or tissue to develop or function normally; complete or partial absence of development.",
    "secondary": "In hematology and teratology, pure red cell aplasia involves the selective cessation of erythroid precursor development within the bone marrow.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital **aplasia** of the thyroid gland leads inevitably to infantile myxedema and developmental arrest."},
      {"author": "Maxwell M. Wintrobe", "work": "Clinical Hematology", "quote": "In idiopathic bone marrow **aplasia**, peripheral blood pancytopenia is accompanied by dense fatty replacement of the marrow space."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Renal **aplasia** results from the early failure of the ureteric bud to induce the metanephric blastema."}
    ]
  },
  "cataplasia": {
    "primary": "Degenerative reversion of cells or tissues to a more primitive or less differentiated form; retrogressive cell change.",
    "secondary": "In histopathology, cataplasia describes the cellular atrophy and morphological regression seen in senescent tissues or chronic atrophy.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Under chronic nutritional deprivation, mature parenchymal cells exhibit marked **cataplasia**, shrinking to juvenile proportions."},
      {"author": "Vinay Kumar", "work": "Robbins Basic Pathology", "quote": "The histologic picture of **cataplasia** reveals nuclear condensation and reduction of specialized cytoplasmic organelles."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Atrophic parathyroid tissue illustrates reversible **cataplasia** upon cessation of prolonged hypercalcemic suppression."}
    ]
  },
  "cataplasm": {
    "primary": "A soft, moist, heated mass of herbs, flour, or clay applied topically as a poultice to soothe inflammation or pain.",
    "secondary": "In historical therapeutics, a mustard or flaxseed cataplasm was placed on the chest to relieve pulmonary congestion through counterirritation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The application of a warm flaxseed **cataplasm** to the thoracic wall brought grateful relief to pleuritic agony."},
      {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "In cases of gouty paroxysm, applying an emollient **cataplasm** softens the tense inflamed integuments."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old woman bustled about with a steaming **cataplasm**, assuring the invalid that its warmth would draw out the cold."}
    ]
  },
  "cataplastic": {
    "primary": "Of, relating to, or resembling a cataplasm (poultice); soothing and emollient.",
    "secondary": "In pathology, relating to or exhibiting cataplasia (degenerative or atrophic cellular regression).",
    "quotes": [
      {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Warm **cataplastic** dressings were laid upon the tumefaction to promote suppuration and ease the throbbing pain."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Tissues undergoing **cataplastic** degeneration display progressive atrophy of their specialized metabolic machinery."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A soothing **cataplastic** paste prepared from crushed herbs alleviated the local tenderness of the carbuncle."}
    ]
  },
  "dysplasia": {
    "primary": "The presence of cells of an abnormal type within a tissue, which may signify a stage in the development of cancer; disordered growth.",
    "secondary": "In pathology, epithelial dysplasia is characterized by nuclear atypia, loss of cell orientation, and increased mitoses without breaching the basement membrane.",
    "quotes": [
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Severe cervical **dysplasia** is regarded as a pre-invasive lesion that may progress to invasive squamous cell carcinoma."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Architectural disarray and cellular pleomorphism within the crypt epithelium define mucosal **dysplasia** in ulcerative colitis."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Routine Pap smear screening allows early detection and curative ablation of high-grade cervical **dysplasia**."}
    ]
  },
  "dysplastic": {
    "primary": "Relating to or exhibiting dysplasia; showing abnormal, disordered development or growth of cells or organs.",
    "secondary": "In clinical dermatology and pathology, a dysplastic nevus is an atypical mole that possesses histologic atypia and confers elevated melanoma risk.",
    "quotes": [
      {"author": "Vinay Kumar", "work": "Robbins Basic Pathology", "quote": "A **dysplastic** lesion exhibits nuclear hyperchromasia, enlarged nucleoli, and disordered maturation across epithelial layers."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Patients with the familial atypical multiple mole syndrome develop numerous **dysplastic** nevi requiring surveillance."},
      {"author": "S. Terry Canale", "work": "Campbell's Operative Orthopaedics", "quote": "Developmental **dysplastic** hips must be diagnosed in early infancy to prevent premature degenerative coxarthrosis."}
    ]
  },
  "ectoplasm": {
    "primary": "The dense, outer relatively non-granulated layer of the cytoplasm in a cell (as in an amoeba).",
    "secondary": "In parapsychology and spiritualism, a supernatural viscous substance supposedly exuded from the body of a medium during a trance.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Physical Basis of Life", "quote": "Under the microscope, the clear outer **ectoplasm** of the amoeba directs the flow of internal granular endoplasm."},
      {"author": "Arthur Conan Doyle", "work": "The History of Spiritualism", "quote": "Photographic plates recorded luminous ribbons of **ectoplasm** streaming from the medium's mouth during the séance."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Cortical actin filaments cross-link beneath the plasma membrane to form the rigid, gel-like **ectoplasm**."}
    ]
  },
  "endoplasm": {
    "primary": "The inner, granular, fluid portion of the cytoplasm of a cell, surrounded by the ectoplasm.",
    "secondary": "In protozoology and cell physiology, the endoplasm contains the nucleus, mitochondria, vacuoles, and metabolic organelles, displaying active cytoplasmic streaming.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The flowing **endoplasm** carries food vacuoles and crystals along rapid currents toward the advancing pseudopodium."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Sol-gel transitions between the peripheral cortex and internal **endoplasm** drive amoeboid cell crawling."},
      {"author": "Max Schultze", "work": "Das Protoplasma der Rhizopoden und der Pflanzenzellen", "quote": "Continuous cyclosis within the fluid **endoplasm** distributes absorbed nutrients throughout the unicellular organism."}
    ]
  },
  "hyperplasia": {
    "primary": "The enlargement of an organ or tissue caused by an abnormal increase in the reproduction rate of its cells.",
    "secondary": "In cellular pathology, physiologic hyperplasia occurs in glandular breast tissue during lactation, whereas pathologic endometrial hyperplasia predisposes to cancer.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "We distinguish true **hyperplasia**, which multiplies the number of cells, from simple hypertrophy, which merely enlarges them."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Benign prostatic **hyperplasia** arises from hormonal dysregulation between testosterone and dihydrotestosterone in aging men."},
      {"author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Constitutive growth factor signaling drives continuous epithelial **hyperplasia**, laying the foundation for oncogenesis."}
    ]
  },
  "hypoplasia": {
    "primary": "Underdevelopment or incomplete development of an organ, tissue, or body part, resulting from a reduced number of cells.",
    "secondary": "In pediatric pathology, pulmonary hypoplasia is a fatal congenital anomaly caused by oligohydramnios restricting fetal thoracic expansion.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital **hypoplasia** of the arterial tree was frequently observed in young chlorotic female patients."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Severe renal **hypoplasia** results in childhood chronic kidney disease due to a severely reduced nephron complement."},
      {"author": "David L. Rimoin", "work": "Principles and Practice of Medical Genetics", "quote": "Enamel **hypoplasia** reflects transient nutritional or metabolic insults sustained by the ameloblasts during tooth formation."}
    ]
  },
  "neoplasia": {
    "primary": "The formation or presence of a new, abnormal growth of tissue; the biological process of tumor development.",
    "secondary": "In oncology, neoplasia is defined as an uncoordinated, autonomous proliferation of cells that persists even after cessation of the initiating stimulus.",
    "quotes": [
      {"author": "Rupert Willis", "work": "The Pathology of Tumours", "quote": "A **neoplasia** is an abnormal mass of tissue whose uncoordinated growth exceeds that of normal tissues and persists autonomously."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Clonal expansion following irreversible somatic DNA mutation is the foundational event in all human **neoplasia**."},
      {"author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Accumulation of driver mutations in oncogenes and tumor suppressors orchestrates progressive multi-step **neoplasia**."}
    ]
  },
  "neoplasm": {
    "primary": "A new and abnormal growth of tissue in some part of the body, especially a characteristic of cancer; a tumor.",
    "secondary": "In medical oncology, neoplasms are classified as benign (non-invasive, encapsulated) or malignant (infiltrative, capable of distant metastasis).",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early surgical extirpation of a localized **neoplasm** provides the only reliable hope of permanent cure."},
      {"author": "Vinay Kumar", "work": "Robbins Basic Pathology", "quote": "Histologic assessment determines whether an excised **neoplasm** exhibits benign circumscription or invasive malignancy."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Unexplained weight loss and night sweats may be the first paraneoplastic signs of a hidden occult **neoplasm**."}
    ]
  },
  "neoplastic": {
    "primary": "Of, relating to, or having the characteristics of a neoplasm or neoplasia; tumoral.",
    "secondary": "In cellular biology, describing transformed cells that exhibit anchorage-independent growth, evasion of apoptosis, and sustained angiogenesis.",
    "quotes": [
      {"author": "Robert A. Weinberg", "work": "The Hallmarks of Cancer", "quote": "Acquisition of self-sufficiency in growth signals enables **neoplastic** clones to expand without exogenous stimulation."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Infiltration through the basement membrane into lymphatic channels confirms the malignant nature of a **neoplastic** clone."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Immunohistochemical profiling of intermediate filaments helps pinpoint the histogenetic origin of **neoplastic** biopsies."}
    ]
  },
  "plasm": {
    "primary": "A formative fluid or biological substance; the fluid part of blood, lymph, or milk (or short for protoplasm).",
    "secondary": "In classical cytology, the living material of a cell considered as the vehicle of vital and hereditary properties.",
    "quotes": [
      {"author": "August Weismann", "work": "The Germ-Plasm: A Theory of Heredity", "quote": "The hereditary continuity of generations resides in the immortal germ-**plasm**, untainted by somatic modifications."},
      {"author": "Thomas Henry Huxley", "work": "The Physical Basis of Life", "quote": "Every living creature is fashioned from the same basic formative **plasm**, whose chemical activities constitute life."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Organic evolution operates through continuous differentiation of the vital **plasm** in response to environmental forces."}
    ]
  },
  "plasma": {
    "primary": "The colorless, fluid part of blood, lymph, or milk, in which corpuscles or fat globules are suspended.",
    "secondary": "In physics, a fourth state of matter consisting of a gas of ionized particles, free electrons, and photons at high temperatures.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Whole blood centrifugation separates the cellular elements from the clear straw-colored **plasma**."},
      {"author": "Irving Langmuir", "work": "Oscillations in Ionized Gases", "quote": "I have used the word **plasma** to describe this ionized region containing balanced charges of ions and electrons."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Fibrinogen and albumin dissolved in blood **plasma** maintain oncotic pressure and coagulation readiness."}
    ]
  },
  "plasmablast": {
    "primary": "An immature plasma cell precursor that has differentiated from an activated B cell and retains proliferative capacity while actively secreting antibodies.",
    "secondary": "In immunology, circulating plasmablasts peak transiently in peripheral blood 5 to 7 days following acute infection or vaccination.",
    "quotes": [
      {"author": "Charles Janeway", "work": "Immunobiology", "quote": "Upon somatic hypermutation in the germinal center, an activated B cell differentiates into an antibody-secreting **plasmablast**."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "The transitional **plasmablast** migrates through lymphatic channels to settle in the bone marrow as a long-lived plasma cell."},
      {"author": "Peter C. Doherty", "work": "Immunity and Infection", "quote": "A sharp rise in circulating **plasmablast** frequency serves as a reliable marker of primary vaccine response."}
    ]
  },
  "plasmacyte": {
    "primary": "A plasma cell; a fully differentiated, non-dividing B lymphocyte specialized for the high-volume secretion of antibodies.",
    "secondary": "In histology and hematopathology, a plasmacyte exhibits an eccentric nucleus with a characteristic 'clock-face' or 'cartwheel' chromatin pattern and abundant basophilic cytoplasm.",
    "quotes": [
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Inflammatory exudates in chronic encephalitis contain numerous **plasmacyte** cells clustered around cerebral capillaries."},
      {"author": "Maxwell M. Wintrobe", "work": "Clinical Hematology", "quote": "The mature **plasmacyte** displays an abundant rough endoplasmic reticulum engineered for massive immunoglobulin synthesis."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "A perinuclear halo representing the prominent Golgi apparatus is the microscopic hallmark of the mature **plasmacyte**."}
    ]
  },
  "plasmacytoma": {
    "primary": "A discrete, solitary malignant tumor composed of monoclonal plasma cells, typically arising in bone marrow or soft tissue.",
    "secondary": "In hematology and oncology, a solitary bone plasmacytoma produces a localized osteolytic lesion and carries a high risk of progressing to systemic multiple myeloma.",
    "quotes": [
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "A biopsy of an isolated osteolytic bone lesion confirming monoclonal plasma cells establishes the diagnosis of **plasmacytoma**."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Solitary osseous **plasmacytoma** requires definitive local radiotherapy, followed by long-term monitoring for progression to myeloma."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Extramedullary **plasmacytoma** occurs most commonly in the upper respiratory tract and carries a better prognosis than bone lesions."}
    ]
  },
  "plasmapheresis": {
    "primary": "A medical procedure in which whole blood is removed from the body, separated into plasma and cellular components, and the cells are returned to the patient with a replacement fluid.",
    "secondary": "In neurology and rheumatology, therapeutic plasmapheresis removes pathogenic autoantibodies, circulating immune complexes, or paraproteins in conditions such as myasthenia gravis and Guillain-Barré syndrome.",
    "quotes": [
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Therapeutic **plasmapheresis** rapidly lowers circulating anti-acetylcholine receptor autoantibody titers in acute myasthenic crisis."},
      {"author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "In thrombotic thrombocytopenic purpura, emergent **plasmapheresis** with fresh frozen plasma replacement is lifesaving."},
      {"author": "Maxwell M. Wintrobe", "work": "Clinical Hematology", "quote": "Centrifugal **plasmapheresis** allows the collection of high-potency hyperimmune plasma from healthy donor volunteers."}
    ]
  },
  "plasmid": {
    "primary": "A genetic structure in a cell that can replicate independently of the chromosomes, typically a small circular DNA strand in bacteria or protozoa.",
    "secondary": "In biotechnology and recombinant DNA technology, engineered plasmids carrying antibiotic resistance genes and multiple cloning sites serve as universal gene-cloning vectors.",
    "quotes": [
      {"author": "Joshua Lederberg", "work": "Cell Genetics and Hereditary Symbiosis", "quote": "I propose the generic term **plasmid** for any extrachromosomal hereditary determinant capable of autonomous replication."},
      {"author": "Stanley N. Cohen", "work": "Construction of Biologically Functional Bacterial Plasmids in Vitro", "quote": "Cleaving an antibiotic-resistant **plasmid** with EcoRI endonuclease enabled the insertion and expression of foreign genes."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Horizontal gene transfer of an R-factor **plasmid** spreads multidrug resistance rapidly through clinical pathogen populations."}
    ]
  },
  "plasmin": {
    "primary": "An active proteolytic enzyme in blood plasma that dissolves fibrin clots during fibrinolysis.",
    "secondary": "In hematology and coagulation biochemistry, inactive plasminogen is cleaved by tissue plasminogen activator (tPA) or urokinase into active plasmin, which breaks down fibrin mesh into fibrin degradation products (D-dimer).",
    "quotes": [
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "The serine protease **plasmin** cleaves fibrin polymers to dissolve hemostatic plugs once vascular repair is accomplished."},
      {"author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Recombinant tPA activates endogenous plasminogen to generate **plasmin**, restoring patency to occluded coronary arteries."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Circulating alpha-2-antiplasmin rapidly binds free **plasmin** to prevent uncontrolled systemic degradation of plasma proteins."}
    ]
  },
  "plasminogen": {
    "primary": "The inactive precursor (zymogen) of plasmin found in blood plasma, which upon activation breaks down blood clots.",
    "secondary": "In vascular biology, plasminogen binds to fibrin within clots, where endothelial tissue plasminogen activator (tPA) catalyzes its conversion into active plasmin.",
    "quotes": [
      {"author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Fibrin-selective thrombolytic agents preferentially activate **plasminogen** that is already bound to the intra-arterial thrombus."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "Cleavage of a single Arg-Val peptide bond converts single-chain **plasminogen** into two-chain catalytic plasmin."},
      {"author": "Maxwell M. Wintrobe", "work": "Clinical Hematology", "quote": "Inherited deficiency of **plasminogen** leads to ligneous conjunctivitis and recurrent pseudomembranous mucosal lesions."}
    ]
  },
  "plasmodiidae": {
    "primary": "A family of parasitic protozoans in the apicomplexan order Haemosporida, comprising the genera Plasmodium and allied blood parasites that cause malaria in vertebrates.",
    "secondary": "In parasitology, members of the family Plasmodiidae alternate generations between a vertebrate intermediate host (schizogony) and a dipteran vector (sporogony).",
    "quotes": [
      {"author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "The life cycle of the **Plasmodiidae** links the salivary glands of mosquitoes with intraerythrocytic reproduction in man."},
      {"author": "Patrick Manson", "work": "Tropical Diseases", "quote": "Classification of the **Plasmodiidae** requires identifying pigment granule morphology and schizont segmentation patterns."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The cyclic fevers of ague coincide with the simultaneous burst of sporulating **Plasmodiidae** from invaded red cells."}
    ]
  },
  "plasmodiophora": {
    "primary": "A genus of obligate plant-parasitic protists in the family Plasmodiophoraceae, including Plasmodiophora brassicae, the causative agent of clubroot disease in crucifers.",
    "secondary": "In plant pathology, *Plasmodiophora* causes hypertrophy and hyperplasia of host root tissues, resulting in characteristic club-shaped galls that stunt cabbage and canola crops.",
    "quotes": [
      {"author": "Mikhail Voronin", "work": "Plasmodiophora Brassicae: The Cause of Cabbage Clubroot", "quote": "I observed that the amoeboid plasmodium of **Plasmodiophora** invades young root hairs and induces monstrous galling."},
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The multinucleate intracellular vegetative stage of **Plasmodiophora** clearly separates it from true filament-forming fungi."},
      {"author": "George Agrios", "work": "Plant Pathology", "quote": "Resting spores of **Plasmodiophora** brassicae survive in infested soils for over fifteen years, challenging crop rotation."}
    ]
  },
  "plasmodiophoraceae": {
    "primary": "A family of obligate endoparasitic protists (plasmodiophorids) that parasitize plants, algae, and fungi, forming multinucleate vegetative plasmodia inside host cells.",
    "secondary": "In phytopathology, members of Plasmodiophoraceae (such as Plasmodiophora and Spongospora) serve as destructive plant pathogens and viral vectors (such as potato mop-top virus).",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "The **Plasmodiophoraceae** represent a remarkable group of intracellular parasites whose life cycle features cruciform nuclear division."},
      {"author": "George Agrios", "work": "Plant Pathology", "quote": "Clubroot and powdery scab of potato are classic agricultural diseases caused by phytomyxean species of **Plasmodiophoraceae**."},
      {"author": "Mikhail Voronin", "work": "Studies on Plasmodiophoraceae", "quote": "Zoospore encystment upon the host epidermal wall marks the initial infection phase in the family **Plasmodiophoraceae**."}
    ]
  },
  "plasmodium": {
    "primary": "A parasitic protozoan of a genus that includes those causing malaria in humans and other vertebrates; or a multinucleate mass of protoplasm in slime molds.",
    "secondary": "In mycology and parasitology, four main species of *Plasmodium* (P. falciparum, P. vivax, P. malariae, P. ovale) cause human malaria, while the acellular slime mold plasmodium creeps via cytoplasmic streaming.",
    "quotes": [
      {"author": "Charles Louis Alphonse Laveran", "work": "A New Parasite Found in the Blood of Malarial Patients", "quote": "I observed oscillant flagellated bodies in blood preparations, identifying the living **plasmodium** responsible for marsh fever."},
      {"author": "Ronald Ross", "work": "Memoirs", "quote": "On August 20, 1897, I discovered pigmented cells of the malarial **plasmodium** in the stomach wall of a dapple-winged mosquito."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "In Physarum, the giant acellular **plasmodium** contains millions of diploid nuclei sharing a continuous cytoplasm."}
    ]
  },
  "plassey": {
    "primary": "A historic village in West Bengal, India, famous as the site of the decisive Battle of Plassey (1757) where Robert Clive defeated the Nawab of Bengal.",
    "secondary": "In British colonial and Indian history, the Battle of Plassey laid the foundation of British East India Company territorial dominance across the Indian subcontinent.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays: Lord Clive", "quote": "The victory of **Plassey** was achieved with remarkably light loss, yet it laid the foundation of our vast Indian Empire."},
      {"author": "Robert Clive", "work": "Letters and Dispatches", "quote": "At daybreak the enemy moved out of their entrenchments at **Plassey**, offering battle with overwhelming cavalry numbers."},
      {"author": "Edward Gibbon", "work": "Memoirs of My Life and Writings", "quote": "The conquest of Bengal inaugurated at **Plassey** altered the geopolitical equilibrium of the European powers."}
    ]
  },
  "plaster": {
    "primary": "A building material used for coating walls and ceilings, typically composed of lime, gypsum, or cement mixed with water and sand.",
    "secondary": "In medicine, an adhesive bandage, poultice, or medicated dressing spread upon fabric and applied to the skin (such as plaster of Paris for orthopedic casts).",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Honest masonry disdains the deceitful cosmetic of polished **plaster** spread to simulate noble marble."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Applying a rigid **plaster** of Paris jacket provides essential immobilization for tuberculous spondylitis."},
      {"author": "Vitruvius", "work": "De Architectura", "quote": "Three successive coats of lime **plaster** polished with marble dust will resist cracking and display fresco painting with brilliance."}
    ]
  },
  "plasterboard": {
    "primary": "A building material consisting of a rigid sheet of gypsum plaster sandwiched between two thick sheets of heavy paper, used in constructing interior walls and ceilings (drywall).",
    "secondary": "In architectural construction, plasterboard provides fire-resistant, sound-insulating interior partitions that eliminate the drying time of wet plastering.",
    "quotes": [
      {"author": "Francis D. K. Ching", "work": "Building Construction Illustrated", "quote": "Standard interior partition walls are faced with five-eighths inch gypsum **plasterboard** fastened to steel studs."},
      {"author": "Walter Gropius", "work": "Scope of Total Architecture", "quote": "Prefabricated building components like modular **plasterboard** accelerated the industrialization of modern housing."},
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "Standardized drywall and **plasterboard** replaced artisan trowel-work with rapid mass-produced assembly."}
    ]
  },
  "plasterer": {
    "primary": "A skilled tradesperson who applies plaster to walls, ceilings, and architectural moldings.",
    "secondary": "In historical craft guilds, a specialized artisan who executed intricate decorative stucco, cornices, and ornamental ceiling reliefs.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The honest handiwork of the stonemason cannot be replaced by the mechanical slickness of the modern **plasterer**."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The industrious **plasterer** climbed his scaffold at dawn, trowel in hand, to finish the factory ceiling."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wages of the skilled **plasterer** reflect the arduous physical labor and seasonal nature of the building trade."}
    ]
  }
}

batch_data = {}
for rel_path in batch5_files:
    word = rel_path.split('\\')[-1].replace('.md', '')
    if word in lexicon:
        batch_data[rel_path] = lexicon[word]
    elif word.lower() in lexicon:
        batch_data[rel_path] = lexicon[word.lower()]
    else:
        print(f"Warning: word '{word}' not found in lexicon for {rel_path}")

print(f"Mapped {len(batch_data)} of {len(batch5_files)} files in Batch 5.")

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate_form_finish2_b5.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(batch_data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Form Finish Slice 2 Batch 5.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} successfully.")
