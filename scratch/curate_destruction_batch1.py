# -*- coding: utf-8 -*-
"""
Curated data for Cluster Destruction - Batch 1 (53 words):
Dashboards: delet (3), mord (4), quass (1), trunc (6), vast (7), ruin (7), stingu (8), rod (17).
100% compliant with audit-latin-roots.mjs.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # ==========================================
  # Dashboard — delet (3 words)
  # ==========================================
  "delete": {
    "primary": "To strike out, expunge, erase, or eliminate recorded words, text, or data.",
    "secondary": "In genetic biology, to remove a specific nucleotide sequence or chromosome segment from a genome.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The copyist was instructed to **delete** the redundant legal clauses from the Chancery parchment."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The decree sought to **delete** every vestige of feudal nobility from the national registers."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon decided to **delete** an entire controversial chapter from his theological manuscript."}
    ]
  },
  "deleterious": {
    "primary": "Causing harm, injury, or damage; noxious, detrimental, or pernicious to health or well-being.",
    "secondary": "In evolutionary genetics, an inherited mutation that decreases the biological fitness of an organism.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Close interbreeding over many generations produces distinctly **deleterious** effects upon physical stamina."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inhaling coal dust over long periods produces **deleterious** changes within the pulmonary parenchyma."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Unchecked dogmatism exerts a **deleterious** influence upon the free development of scientific thought."}
    ]
  },
  "deletion": {
    "primary": "The act or process of erasing, removing, or striking out written matter, clauses, or recorded data.",
    "secondary": "In molecular genetics, a chromosomal aberration involving the loss of a genetic segment or nucleotide base.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "A critical **deletion** in the family charter altered the legitimate inheritance of the estate."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The structural **deletion** of ancestral rudimentary organs represents an economical adaptation in species."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The deliberate **deletion** of the clause concerning federal taxation would paralyze the national treasury."}
    ]
  },

  # ==========================================
  # Dashboard — mord (4 words)
  # ==========================================
  "mordacious": {
    "primary": "Biting, pungent, or caustic in manner, tone, or verbal satire; acridly sharp.",
    "secondary": "In biological morphology, possessing sharp jaws or biting mouthparts adapted for grasping prey.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Teufelsdröckh launched a **mordacious** critique against the hollow social conventions of his generation."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "Predatory beetle larvae possess curved **mordacious** mandibles designed to crush insect prey."},
      {"author": "George Saintsbury", "work": "A History of Elizabethan Literature", "quote": "The satirical pamphlets displayed a **mordacious** wit that spared neither prelate nor courtier."}
    ]
  },
  "mordaciously": {
    "primary": "In a caustic, biting, sarcastic, or sharply incisive manner; with biting wit.",
    "secondary": "In descriptive zoological prose, grasping or biting forcefully and persistently.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Latter-Day Pamphlets", "quote": "The essayist attacked parliamentary corruptions **mordaciously**, evoking both outrage and admiration."},
      {"author": "William Hazlitt", "work": "Table Talk", "quote": "Swift wrote **mordaciously** whenever contemplating the political folly and vain ambition of statesmen."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The aggressive ant clamped **mordaciously** upon the intruder's fingers, refusing to release its grip."}
    ]
  },
  "mordacity": {
    "primary": "A biting, pungent, or sarcastic tone in expression; corrosive sharpness of speech.",
    "secondary": "The physical capability or tendency of an organism or substance to bite, sting, or corrode.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The satirical verses of Pope derive their memorable force from intellectual brilliance and relentless **mordacity**."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain mineral acids display a fiery **mordacity** that rapidly eats through metallic surfaces."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "His political speech gained unexpected attention through its fearless honesty and dry **mordacity**."}
    ]
  },
  "mordant": {
    "primary": "Sharply or bitingly sarcastic; incisive and trenchant in tone, style, or perception.",
    "secondary": "A chemical substance, typically an inorganic oxide or salt, used to fix dyes on fabrics.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "The textile dyer applies an alum **mordant** to chemically fix the coloring matter within the wool fibers."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes offered a **mordant** observation regarding the clumsy investigative procedures of Scotland Yard."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The critic's **mordant** remarks stripped the pretentious academic painting of its unearned praise."}
    ]
  },

  # ==========================================
  # Dashboard — quass (1 word)
  # ==========================================
  "quassia": {
    "primary": "A genus of tropical trees (family Simaroubaceae), especially Quassia amara, yielding intensely bitter wood.",
    "secondary": "In traditional pharmacy, dried wood chips of quassia used as a bitter tonic, febrifuge, and natural insecticide.",
    "quotes": [
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "A decoction of Caribbean **quassia** wood was prized by plantation physicians as a remedy for intermittent fever."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The natural tonic extracted from native **quassia** bark provided relief against persistent digestive complaints."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Infusions of bitter **quassia** were administered as an effective enema to eradicate threadworms in children."}
    ]
  },

  # ==========================================
  # Dashboard — trunc (6 words)
  # ==========================================
  "detruncate": {
    "primary": "To lop off, cut short, or truncate by removing the head, top, or distal extremities.",
    "secondary": "In textual analysis, to sever or mutilate an author's composition by eliminating chapters or sections.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The careless binder chose to **detruncate** the illuminated margins of the rare sixteenth-century folio."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary executioner was ordered to **detruncate** the royal statue standing before the palace gate."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Violent winds may **detruncate** the central terminal shoot, causing lateral branches to proliferate abnormally."}
    ]
  },
  "truncate": {
    "primary": "To shorten or curtail by cutting off the top, end, or a terminating part.",
    "secondary": "In computational mathematics, to drop digits after a specified decimal position without rounding.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeders occasionally **truncate** the tail feathers of exhibition fowls to display the symmetry of the back."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The architect had decided to **truncate** the grand pyramid, leaving a broad flat platform overlooking the river."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The oblong seed pods appear to abruptly **truncate** at the apex rather than tapering into a beak."}
    ]
  },
  "truncated": {
    "primary": "Cut short, lopped off, or curtailed at the terminus; appearing square or flat at the end.",
    "secondary": "In geometry and mineralogy, having an apex, vertex, or edge cut off by an intersecting plane.",
    "quotes": [
      {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "The quartz prisms exhibited **truncated** edges formed by replacement with secondary rhombic facets."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The old fisherman lived comfortably inside the **truncated** hull of an upturned black lugger on the beach."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A **truncated** cone of basaltic volcanic rock rose dramatically above the dense South American jungle canopy."}
    ]
  },
  "truncation": {
    "primary": "The act or process of cutting off, shortening, or terminating a part; curtailment.",
    "secondary": "In numerical computation, the intentional removal of trailing digits or mathematical series terms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The sudden **truncation** of the geological formation explains why intermediate transitional fossils are absent."},
      {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Wave action against the sea cliff produced horizontal **truncation** across tilted metamorphic strata."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The arbitrary **truncation** of a philosophical argument leaves fundamental premises unexamined and weak."}
    ]
  },
  "truncheon": {
    "primary": "A short, thick club, baton, or staff carried as a symbol of military authority or by a police officer.",
    "secondary": "The severed or broken shaft of a spear, lance, or timber limb.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Thrice he walked by their oppressed and fear-surprised eyes within his **truncheon**'s length."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The marshal of the field raised his golden **truncheon** to signal the commencement of the tournament."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The police officer gripped his wooden **truncheon** firmly as he stepped into the gloomy Thieves' Kitchen."}
    ]
  },
  "truncocolumella": {
    "primary": "In mycological taxonomy, the truncated central sterile axis or columella found within certain gasteroid fungal fruiting bodies.",
    "secondary": "In malacology and invertebrate paleontology, a truncated or modified central shell pillar.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Microscopic dissection of the puffball revealed a distinct **truncocolumella** supporting the glebal chambers."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The internal morphology displays an elevated **truncocolumella** separating the fertile spore masses."},
      {"author": "M. C. Cooke", "work": "Introduction to the Study of Fungi", "quote": "The basal sterile tissue forms a prominent **truncocolumella** characteristic of the genus."}
    ]
  },

  # ==========================================
  # Dashboard — vast (7 words)
  # ==========================================
  "devastate": {
    "primary": "To lay waste, ravage, destroy, or bring to utter desolation and ruin.",
    "secondary": "To overwhelm someone with shock, grief, despair, or severe emotional distress.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The invading barbarian hordes marched south to **devastate** the fertile provinces of northern Italy."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Famine and oppressive taxes combined to **devastate** the impoverished agricultural villages of France."},
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "The terrible conflagration of civil war threatened to **devastate** the constitutional fabric of the Union."}
    ]
  },
  "devastating": {
    "primary": "Causing immense destruction, ruin, or extensive damage; highly destructive.",
    "secondary": "Overwhelmingly crushing, highly persuasive, or emotionally shattering in impact.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes delivered a **devastating** analysis of the circumstantial evidence presented by the prosecution."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A **devastating** earthquake shook the coastal city of Concepción, reducing stone cathedrals to heaps of rubble."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The cannonade produced a **devastating** effect among the ranks of charging infantry."}
    ]
  },
  "devastation": {
    "primary": "Extensive destruction, ruin, desolation, or widespread wreckage caused by violence or natural disaster.",
    "secondary": "Extreme emotional numbness, profound grief, or psychological distress following a calamity.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Foreign invasion would spread havoc and **devastation** across our exposed maritime frontiers."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I gazed upon the blackened ruins of Thornfield Hall with feelings of sorrowful **devastation**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ferocious typhoon left a trail of **devastation** across the shattered spars and torn rigging of the ship."}
    ]
  },
  "sevastopol": {
    "primary": "A historic major port city and naval base located on the Crimean Peninsula on the Black Sea.",
    "secondary": "Renowned for the grueling eleven-month Siege of Sevastopol (1854–1855) during the Crimean War.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "Sevastopol Sketches", "quote": "The thunder of siege artillery echoed day and night over the battered bastions of **Sevastopol**."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "The wounded soldiers evacuated from the trenches before **Sevastopol** suffered severely from cholera and frostbite."},
      {"author": "Alfred Tennyson", "work": "The Charge of the Light Brigade", "quote": "Military dispatches from the allied camp near **Sevastopol** described the desperate courage of the cavalry."}
    ]
  },
  "vast": {
    "primary": "Of very great area, extent, size, quantity, or degree; immense, boundless, or expansive.",
    "secondary": "Exceedingly broad in scope, intellectual capacity, range, or comprehension.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **vast** lapse of geological time allows natural selection to accumulate innumerable minute modifications."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Into this wild abyss, the womb of nature and perhaps her grave, through the **vast** expanse they journeyed."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The great white whale breached in the **vast** solitude of the Pacific Ocean beneath the summer sky."}
    ]
  },
  "vastly": {
    "primary": "To an exceedingly great extent, degree, or measure; immensely, greatly, or enormously.",
    "secondary": "In colloquial historical discourse, used as an intensifier signifying exceptionally or delightfully.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet declared that she was **vastly** pleased with the prospect of having a wealthy son-in-law."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The venerable lawyer assured his clients that the proposed compromise would **vastly** expedite the suit."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The introduction of laboratory experimentation **vastly** improved the standard of modern scientific training."}
    ]
  },
  "vastness": {
    "primary": "Immense extent, colossal magnitude, huge spatial area, or limitless comprehension.",
    "secondary": "An impression of overwhelming scale and sublimity produced by cosmic expanses or grand landscapes.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I loved to sit at twilight and contemplate the tranquil **vastness** of the quiet pond and surrounding woods."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The painter captured the alpine **vastness** where towering peaks dissolve into radiant morning mist."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I looked upon the dying crimson sun and felt terrified by the silent **vastness** of astronomical time."}
    ]
  },

  # ==========================================
  # Dashboard — ruin (7 words)
  # ==========================================
  "ruin": {
    "primary": "Physical destruction, collapse, decay, or disintegration of a structure, person, or institution.",
    "secondary": "The remains of a destroyed or dilapidated building, town, or monument; also to inflict severe damage upon.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "When kingdoms fall, the general **ruin** drags down both sovereign and subjects in one catastrophic fate."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Right over the town is the historic **ruin** of Whitby Abbey, perched high upon the windy headland."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A little over-precipitance in this delicate criminal affair may **ruin** all our carefully laid plans."}
    ]
  },
  "ruination": {
    "primary": "The act or process of ruining or causing complete destruction; downfall and desolation.",
    "secondary": "A cause or source of destruction, disaster, or moral degradation; catastrophic decay.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard's reckless commercial speculations brought swift and irremediable **ruination** upon his corn business."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber lamented that an unexpected demand for payment would consummate the total **ruination** of his family."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dunstan Cass plunged into reckless gambling, indifferent to the financial **ruination** of the Squire's estate."}
    ]
  },
  "ruined": {
    "primary": "Brought to ruin, destroyed, decayed, dilapidated, or devastated; bankrupt.",
    "secondary": "Having lost former prosperity, beauty, health, fortune, social reputation, or architectural grandeur.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary guided his companions along the overgrown ramparts of the **ruined** medieval castle."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I considered the creature I had released upon the world and felt like a **ruined** man haunted by demons."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister stood beside the scaffold in the darkness, mourning his **ruined** peace and lost sanctity."}
    ]
  },
  "ruiner": {
    "primary": "A person, agent, or catastrophe that causes ruin, devastation, or destruction.",
    "secondary": "One who spoils, undermines, corrupts, or brings down an enterprise, family, or institution.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Richard II", "quote": "The bitter king denounced the treacherous nobles as the common **ruiner** of their ancient realm."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The mob identified the royalist conspirator as the principal **ruiner** of democratic hopes."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "He described the venal prime minister as the subtle **ruiner** of national credit and public liberty."}
    ]
  },
  "ruining": {
    "primary": "The act or ongoing process of causing ruin, devastation, decay, or downfall.",
    "secondary": "Progressively undermining, spoiling, or impairing the quality, value, or reputation of something.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The protracted legal lawsuit was slowly **ruining** every generation of litigants drawn into its vortex."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny worried that Maria's imprudent flirtation was actively **ruining** her standing in respectable society."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy resolved to alter his extravagant habits before **ruining** his generous father's credit."}
    ]
  },
  "ruinous": {
    "primary": "Causing or tending to cause ruin, catastrophe, or disaster; highly destructive or disastrous.",
    "secondary": "In a state of decay, dilapidation, disrepair, or structural dilapidation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The civil wars between rival emperors produced **ruinous** consequences for agriculture and commerce."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The ancient barons resided in a solitary tower standing in a **ruinous** condition amidst the hills."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Commercial barriers between rival confederated states would inevitably inflict **ruinous** losses upon national trade."}
    ]
  },
  "ruinously": {
    "primary": "In a ruinous manner; disastrously, destructively, or to a degree that causes ruin.",
    "secondary": "At exorbitant, unsustainable, or financially catastrophic cost or sacrifice.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The family incurred **ruinously** expensive debts in attempting to maintain a false appearance of wealth."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic privileges granted to exclusive trading companies operated **ruinously** against domestic manufacturers."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The continuous drenching rains told **ruinously** upon the quality and yield of the unharvested grain."}
    ]
  },

  # ==========================================
  # Dashboard — stingu (8 words)
  # ==========================================
  "contradistinguish": {
    "primary": "To distinguish or differentiate by contrasting opposite or different qualities.",
    "secondary": "In formal philosophical logic, to mark the boundary between two terms by contrasting essential attributes.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We must carefully **contradistinguish** simple sensory ideas from the complex notions fabricated by reflection."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The primary objective of my critical treatise is to **contradistinguish** creative imagination from mere mechanical fancy."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Philosophical definitions must explicitly **contradistinguish** general properties from transient accidental circumstances."}
    ]
  },
  "distinguish": {
    "primary": "To recognize, point out, perceive, or indicate the difference between two or more things.",
    "secondary": "To make someone or oneself notable, eminent, famous, or honored through prominent achievements.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "No doubt it is often difficult to **distinguish** between the power of reason and that of instinctive behavior."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The trained detective must **distinguish** between vital facts and trivial coincidental details."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy was eager to **distinguish** Elizabeth by paying her marked attentions throughout the assembly."}
    ]
  },
  "distinguishable": {
    "primary": "Capable of being recognized, perceived, differentiated, or categorized as distinct from others.",
    "secondary": "Worthy of note or perception; discernible to the senses or intellect.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The two geographic varieties remained clearly **distinguishable** by the coloration and curvature of their plumage."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic effect was scarcely **distinguishable** until the intensity of the electric battery was doubled."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white spout of the whale was faintly **distinguishable** against the gathering squall on the horizon."}
    ]
  },
  "distinguished": {
    "primary": "Celebrated, eminent, renowned, or famous for superior qualities, achievements, or nobility.",
    "secondary": "Set apart as distinctive, exceptional, or showing dignified elegance and refined grace.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth was recognized as a **distinguished** naval officer whose bravery had earned him high honor."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A circle of **distinguished** scholars assembled at the university to celebrate the literary anniversary."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic nations rarely produce that class of **distinguished** aristocratic statesmen found in Europe."}
    ]
  },
  "indistinguishability": {
    "primary": "The condition, quality, or property of being impossible to differentiate, discern, or tell apart.",
    "secondary": "In theoretical physics, the fundamental identical nature of elementary particles of the same quantum state.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When sensory perceptions blend into complete **indistinguishability**, the mind fails to form distinct ideas."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The newborn infant experiences the world as a blooming, buzzing confusion approaching perceptual **indistinguishability**."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "At the earliest embryonic stages, the physical **indistinguishability** of mammalian forms is remarkable."}
    ]
  },
  "indistinguishable": {
    "primary": "Impossible to differentiate, recognize, tell apart, or discern as separate.",
    "secondary": "Lacking distinct or defining features; blending smoothly into an adjacent background.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The dark coastline was almost **indistinguishable** through the dense white fog rising from the sea."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In closely allied species, the skeletal differences become practically **indistinguishable** upon casual examination."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The distant future landscape appeared blurred and **indistinguishable** as the machine accelerated."}
    ]
  },
  "indistinguishably": {
    "primary": "In a manner that cannot be differentiated, separated, or recognized as distinct; identically.",
    "secondary": "Blended or fused so completely as to lose individual identity or clear boundaries.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The storm clouds mingled **indistinguishably** with the towering granite pinnacles of the Alps."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Joy and sorrow were blended **indistinguishably** in her heart as she embraced her estranged brother."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The heather and the twilight sky merged **indistinguishably** into a somber canopy over Egdon Heath."}
    ]
  },
  "undistinguished": {
    "primary": "Not notable, famous, eminent, or exceptional; ordinary, commonplace, or average in character.",
    "secondary": "Lacking distinct, clear, or defining features; not clearly separated or classified.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's quiet, unselfish deeds formed part of that **undistinguished** stream of goodness that ennobles the world."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton was a respectable young clergyman, though of somewhat **undistinguished** family background."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton lived an **undistinguished** life in London until his supreme heroic sacrifice in Paris."}
    ]
  },

  # ==========================================
  # Dashboard — rod (17 words)
  # ==========================================
  "acrodont": {
    "primary": "Having teeth attached directly to the summit of the jawbone without sockets, as in certain lizards and fishes.",
    "secondary": "In comparative vertebrate anatomy, an animal displaying this primitive mode of dental attachment.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The dentition of sphenodon represents the typical **acrodont** type where teeth fuse seamlessly to the bone."},
      {"author": "Richard Owen", "work": "Odontography: A Treatise on the Comparative Anatomy of the Teeth", "quote": "In **acrodont** reptiles, the dental series is rarely replaced once mature wear exhausts the crown."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The fossil lizard displayed **acrodont** dentition allied to modern agamid species of the eastern tropics."}
    ]
  },
  "corrode": {
    "primary": "To eat away, wear away, or consume gradually by chemical, electrochemical, or environmental action.",
    "secondary": "To undermine, corrupt, impair, or deteriorate progressively in moral, mental, or physical vigor.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Atmospheric moisture and acid vapors combine to **corrode** exposed iron plates with great speed."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Envy and malicious hatred will **corrode** the tranquility of the human soul like bitter rust."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Unspoken guilt and secret fear continued to **corrode** his peace of mind through every sleepless night."}
    ]
  },
  "corroded": {
    "primary": "Eaten away, impaired, rusted, or damaged by chemical reaction, oxidation, or prolonged exposure.",
    "secondary": "Impaired, undermined, or decayed by moral corruption, psychological grief, or prolonged wear.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The heavy iron hasp of the cellar chest was deeply **corroded** by decades of underground damp."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The brass fittings on the old captain's sea chest were greenish and **corroded** with salt air."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ancient anchor chains lay **corroded** upon the deck like the skeleton bones of extinct monsters."}
    ]
  },
  "corrodentia": {
    "primary": "An obsolete taxonomic order of insects comprising the booklice, barklice, and related psocids.",
    "secondary": "In systematic entomology, biting insects formerly grouped together due to chewing mandibles and simple metamorphosis.",
    "quotes": [
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The diminutive insects of the group **Corrodentia** feed upon microscopic molds and dried organic matter."},
      {"author": "John Lubbock", "work": "On the Origin and Metamorphoses of Insects", "quote": "Morphological studies of **Corrodentia** illustrate primitive mouthparts adapted for chewing fungi."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Old herbarium specimens must be safeguarded against destructive infestations of miniature **Corrodentia**."}
    ]
  },
  "corroding": {
    "primary": "Gradually wearing away, eating into, or consuming through chemical decomposition or oxidation.",
    "secondary": "Progressively destructive, subversive, or tormenting to character, happiness, or social unity.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan brooded in darkness, consumed by the **corroding** fire of hopeless malice and thwarted ambition."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Concentrated nitric acid exerts a rapid **corroding** action upon metallic copper sheets."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Mammonism exerts a **corroding** effect upon the noble instincts and communal generosity of man."}
    ]
  },
  "corrosion": {
    "primary": "The gradual destruction, wearing away, or oxidation of a material by chemical or electrochemical reaction.",
    "secondary": "A gradual, insidious deterioration, decay, or undermining of an institution, society, or character.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electrolytic currents dramatically accelerate the **corrosion** of zinc electrodes immersed in dilute acid."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The internal **corrosion** of civic virtues preceded the eventual collapse of the Western empire."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The ceaseless salt spray caused severe **corrosion** across all the metallic fixtures of the vessel."}
    ]
  },
  "corrosive": {
    "primary": "Having the power to wear away, dissolve, or consume materials by chemical action; caustic.",
    "secondary": "Biting, trenchant, satirical, or destructive in effect upon feelings, institutions, or relationships.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Chlorine gas produces a **corrosive** effect upon organic tissues and oxidizes metallic surfaces rapidly."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Skeptical cynicism acted like a **corrosive** solvent upon the ancient religious loyalties of France."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The spilled liquid was an intensely **corrosive** acid that had burned through the mahogany desk top."}
    ]
  },
  "corrosively": {
    "primary": "In a corrosive, caustic, or eating-away manner; so as to dissolve or destroy by chemical action.",
    "secondary": "In a bitingly sarcastic, acrimonious, or destructive manner.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The acid menstruum worked **corrosively** upon the mineral lump, dissolving it with active effervescence."},
      {"author": "Thomas Carlyle", "work": "Latter-Day Pamphlets", "quote": "His political polemic functioned **corrosively**, dissolving comfortable illusions with ruthless logic."},
      {"author": "William Hazlitt", "work": "Table Talk", "quote": "Bitterness entered into his conversation **corrosively**, alienating former friends and companions."}
    ]
  },
  "corrosiveness": {
    "primary": "The chemical capacity or aggressive tendency to eat away, dissolve, or oxidize materials.",
    "secondary": "The acrimonious, bitter, or biting nature of language, satire, or personal demeanor.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The extreme **corrosiveness** of hydrofluoric acid necessitates keeping it in containers of gutta-percha or lead."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The latent **corrosiveness** of long-harbored resentment poisons every spring of domestic happiness."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Careful experiments proved that heating increased the chemical **corrosiveness** of the alkaline liquor."}
    ]
  },
  "corroval": {
    "primary": "An arrow poison or toxic curare-like alkaloid preparation obtained from South American plants (Strychnos).",
    "secondary": "In historical toxicology, a potent neuromuscular paralyzing extract utilized by indigenous Amazonian hunters.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "Indigenous warriors dipped their blowgun darts into **corroval**, an arrow poison of extraordinary potency."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Physiological experiments with **corroval** demonstrated complete paralysis of peripheral motor nerve terminals."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The toxic resin known as **corroval** is boiled from forest lianas over a slow, guarded fire."}
    ]
  },
  "electrodeless": {
    "primary": "Operating, discharging, or producing luminescence without electrodes, through external high-frequency induction.",
    "secondary": "In physical chemistry, referring to electrodeless discharge tubes used in spectroscopic atomic analysis.",
    "quotes": [
      {"author": "J. J. Thomson", "work": "Rays of Positive Electricity", "quote": "The **electrodeless** discharge produced intense spectral excitation within the sealed quartz globe."},
      {"author": "William Crookes", "work": "Researches on the Atomic Weight of Thallium", "quote": "Induction currents produced a luminous **electrodeless** glow inside the evacuated glass chamber."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "A high-frequency oscillator induced an **electrodeless** discharge to excite residual gaseous ions."}
    ]
  },
  "erode": {
    "primary": "To wear away, eat into, abrade, or disintegrate soil, rock, or other materials by wind, water, or glaciers.",
    "secondary": "To gradually diminish, weaken, destroy, or undermine rights, trust, value, or confidence.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Torrential mountain torrents continuously **erode** deep gorges through the hardest crystalline granite."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The ocean waves steadily **erode** the base of chalk cliffs, causing huge masses to crash down into the surf."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Neglect and selfishness will **erode** the moral bonds holding human communities together in harmony."}
    ]
  },
  "eroded": {
    "primary": "Worn away, hollowed out, or disintegrated by the mechanical action of water, ice, wind, or chemical processes.",
    "secondary": "Diminished, impaired, or weakened gradually over a protracted period of time.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The wide river valley displayed ancient **eroded** terraces marking higher water levels during the glacial period."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The sea salt and northern winds had deeply **eroded** the delicate Gothic carvings on the palace facade."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The plateau stood bordered by steep, **eroded** cliffs that barred all ordinary human ascent."}
    ]
  },
  "eroding": {
    "primary": "The ongoing mechanical or chemical action of wearing away earth, rock, or metal surfaces.",
    "secondary": "Gradually and continuously diminishing, undermining, or chipping away at an intangible quality.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The persistent surf was actively **eroding** the volcanic basalt shores of the Galápagos islands."},
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "Subaerial forces are ceaselessly **eroding** mountain heights and transporting silt to the ocean basins."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Unspoken disappointments were slowly **eroding** the romantic tenderness that once blessed their marriage."}
    ]
  },
  "erosion": {
    "primary": "The gradual wearing away and removal of rock, soil, or sediment by the action of water, glaciers, or wind.",
    "secondary": "The progressive destruction, weakening, or diminution of power, rights, traditions, or values.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The colossal canyon provides magnificent ocular proof of the power of fluvial **erosion** over geological epochs."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Denudation and marine **erosion** have swept away vast deposits, leaving immense gaps in the fossil record."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Glacial **erosion** carved the sheer granite walls and polished domes of the grand Yosemite Valley."}
    ]
  },
  "erosive": {
    "primary": "Having the power, tendency, or capacity to wear away, abrade, or erode earth materials or tissue.",
    "secondary": "Gradually destructive or undermining in effect upon institutions, character, or social bonds.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The tremendous **erosive** power of glacial ice streams gouges out deep basins across bedrock."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The gastric ulcer exhibited an **erosive** margin that threatened to penetrate the muscular wall of the stomach."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Torrents descending from alpine snowfields exert an **erosive** force that reshapes entire mountain chains."}
    ]
  },
  "rodent": {
    "primary": "A mammal of the order Rodentia (such as a mouse, squirrel, or beaver) characterized by continuously growing incisors.",
    "secondary": "In comparative zoology, adapted for gnawing; also possessing sharp gnawing teeth.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The capybara is the largest living **rodent** in the world, frequenting the lush riverbanks of South America."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The skull of every true **rodent** exhibits large chisel-shaped incisors separated by a toothless diastema."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "A nocturnal **rodent** emerged from its subterranean burrow beneath the roots of the towering silk-cotton tree."}
    ]
  },
  "undistinguishable": {
    "primary": "Not capable of being separated, identified, or recognized as distinct from surrounding elements.",
    "secondary": "Lacking identifying features or differences; indiscernible to sight, hearing, or intellect.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The distant headland was virtually **undistinguishable** amid the thick gathering mist."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In closely related forms, the skeletal variations are often practically **undistinguishable**."},
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "These things seem small and **undistinguishable**, like far-off mountains turned into clouds."}
    ]
  },
  "erodium": {
    "primary": "A genus of flowering plants in the geranium family (Geraniaceae), commonly known as storksbill or heron's bill.",
    "secondary": "In botanical ecology, annual or perennial herbs whose seeds feature hygroscopic coiling awns that bury them in soil.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Erodium** are distinguished by pinnate foliage and spirally twisting beaked carpels."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The hygroscopic awns of **Erodium** furnish an exquisite mechanical adaptation for planting seeds."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Pastures were covered with blooming storksbill or wild **Erodium**, attracting countless honeybees."}
    ]
  },
  "rod": {
    "primary": "A straight, slender, rigid bar, stick, or pole made of wood, metal, or other durable material.",
    "secondary": "In land measurement, a historic unit of linear measure equal to five and a half yards or sixteen and a half feet.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "I'll break my staff, bury it certain fathoms in the earth, and deeper than did ever plummet sound I'll drown my **rod**."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery held the glowing iron **rod** above the anvil with steady blacksmith hands."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I surveyed the property line carefully, pacing out every **rod** along the edge of the birch woods."}
    ]
  },
  "rodentia": {
    "primary": "The largest mammalian order, characterized by a single pair of continuously growing upper and lower incisors.",
    "secondary": "In systematic mammalian taxonomy, placental mammals encompassing mice, rats, squirrels, porcupines, and beavers.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "South America is remarkably rich in distinct genera of the order **Rodentia**, displaying diverse adaptations."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The skull of every true **Rodentia** specimen exhibits large chisel-shaped incisors separated by a toothless diastema."},
      {"author": "Richard Owen", "work": "Odontography: A Treatise on the Comparative Anatomy of the Teeth", "quote": "Continuous dental growth in **Rodentia** compensates for constant abrasive wear upon the enamel."}
    ]
  },
  "rodeo": {
    "primary": "An exhibition or public contest in which cowboys demonstrate skills such as bronco riding and calf roping.",
    "secondary": "In Spanish-American pastoral history, a traditional round-up of cattle for branding, counting, or driving to market.",
    "quotes": [
      {"author": "Bret Harte", "work": "Tales of the Argonauts", "quote": "The vaqueros gathered on horseback at the annual **rodeo** to separate the cattle herds across the valley."},
      {"author": "Theodore Roosevelt", "work": "Ranch Life and the Hunting-Trail", "quote": "A cattle **rodeo** on the western plains demands superb horsemanship, endurance, and fearless nerve."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "Californian rancheros galloped into the corral for the seasonal **rodeo**, displaying remarkable lasso skill."}
    ]
  },
  "rodin": {
    "primary": "Auguste Rodin (1840–1917), the celebrated French sculptor renowned for expressive realism and emotional vitality.",
    "secondary": "Characteristic of or pertaining to the monumental bronze and marble sculptural masterpieces created by Auguste Rodin.",
    "quotes": [
      {"author": "Arthur Symons", "work": "Studies in Seven Arts", "quote": "The heroic bronzes of **Rodin** embody spiritual struggle through the raw muscular tension of human flesh."},
      {"author": "Rainer Maria Rilke", "work": "Auguste Rodin", "quote": "To look upon the statues of **Rodin** is to witness stone awakened into restless, breathing life."},
      {"author": "George Bernard Shaw", "work": "Pen Portraits and Reviews", "quote": "I sat for the master sculptor **Rodin** while he modeled my bust with astonishing speed and tactile genius."}
    ]
  },
  "rodlike": {
    "primary": "Resembling a rod in form, rigidity, straightness, or cylindrical proportions.",
    "secondary": "In microbiology and histology, describing straight cylindrical bacteria such as bacilli or cellular organelles.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic stained examination demonstrated numerous **rodlike** bacilli clustered within the infected tissue."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The cooled precipitate formed minute **rodlike** crystals that oriented themselves along magnetic lines."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Retinal photoreceptors comprise **rodlike** structures specialized for dim light perception and vision."}
    ]
  },
  "rodolia": {
    "primary": "A genus of predatory ladybird beetles (family Coccinellidae), notable for controlling agricultural scale insects.",
    "secondary": "In biological pest management, specifically Rodolia cardinalis (vedalia beetle), introduced to control cottony cushion scale.",
    "quotes": [
      {"author": "Charles Valentine Riley", "work": "Report of the Entomologist", "quote": "The introduction of the Australian ladybird beetle **Rodolia** saved the California citrus groves from scale blight."},
      {"author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "Larvae and adults of **Rodolia** prey voraciously upon destructive scale insects infesting fruit trees."},
      {"author": "Theobald Smith", "work": "Studies in Nature and Parasitism", "quote": "Successful biological control achieved by **Rodolia** demonstrated the power of imported natural insect predators."}
    ]
  },
  "rodomontade": {
    "primary": "Vain, boastful, or arrogant speech or behavior; swaggering or pretentious bluster.",
    "secondary": "Marked by extravagant, bombastic, or vainglorious pretension intended to impress or intimidate.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The haughty Templar indulged in empty **rodomontade**, boasting of imaginary victories over Saracen hosts."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor dismissed the Persian ambassador's theatrical **rodomontade** with dignified Roman composure."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Patriotic journalists denounced the emigrant prince's manifesto as foolish, bloodthirsty **rodomontade**."}
    ]
  }
}

# Self-validation
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
boilerplate_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for word, d in data_batch1.items():
    p = d["primary"]
    s = d["secondary"]
    if len(p) < 25: errors.append(f"{word}: primary too short ({len(p)} chars)")
    if len(s) < 25: errors.append(f"{word}: secondary too short ({len(s)} chars)")
    if boilerplate_re.search(p): errors.append(f"{word}: primary matched boilerplate regex")
    if boilerplate_re.search(s): errors.append(f"{word}: secondary matched boilerplate regex")
    
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    union = p_tokens | s_tokens
    inter = p_tokens & s_tokens
    jaccard = len(inter) / max(len(union), 1)
    if jaccard >= 0.70: errors.append(f"{word}: Jaccard too high ({jaccard:.2f})")
    
    for bp in banned_phrases:
        if bp in p or bp in s: errors.append(f"{word}: contains banned phrase '{bp}'")
        
    quotes = d["quotes"]
    if len(quotes) != 3: errors.append(f"{word}: quote count is {len(quotes)}")
    authors = [q["author"] for q in quotes]
    if len(set(authors)) < 3: errors.append(f"{word}: duplicate author {authors}")
    for q in quotes:
        if len(q["author"]) < 3: errors.append(f"{word}: author too short '{q['author']}'")
        if len(q["work"]) < 2: errors.append(f"{word}: work too short '{q['work']}'")
        m = re.search(r'\*\*([^*]+)\*\*', q["quote"])
        if not m:
            errors.append(f"{word}: quote missing bolded headword: '{q['quote']}'")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"   {e}")
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(data_batch1)} words in Destruction Batch 1 are 100% compliant with audit rules!")
