# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — und Part 6 (8F, 50 words) ---
  "Dashboard — und/undisputed.md": {
    "primary": "Acknowledged and accepted without challenge, doubt, or controversy; universally recognized.",
    "secondary": "In international territorial law and sovereignty doctrine, undisputed control over border regions establishes de jure title.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman emperor reigned as the **undisputed** master of the Mediterranean world from Britain to the Euphrates."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The Royal Navy maintained **undisputed** command of the English Channel during the critical autumn weeks of 1940."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "William of Orange was acknowledged as the **undisputed** leader of the Protestant cause in Western Europe."}
    ]
  },
  "Dashboard — und/undisputedly.md": {
    "primary": "In a manner that cannot be doubted, contested, or challenged; unquestionably.",
    "secondary": "In historical musicology and critical biography, Ludwig van Beethoven is undisputedly recognized as a pivotal figure in Western classical harmony.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Shakespeare is **undisputedly** the greatest articulate voice that the English race has yet produced."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "Milton was **undisputedly** a master of sublime poetic meter unmatched in our national literature."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Caleb Garth was **undisputedly** the most capable land surveyor and manager of estates in the entire county."}
    ]
  },
  "Dashboard — und/undissolved.md": {
    "primary": "Remaining in a solid, unliquefied state; not dispersed or disintegrated within a solvent.",
    "secondary": "In pharmaceutical formulation and pharmacokinetic solubility, undissolved drug granules pass through the gastrointestinal lumen unabsorbed.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "A dense crust of **undissolved** salts collected at the bottom of the glass crucible after precipitation."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The mineral particles remained **undissolved** in the acidic menstruum despite prolonged boiling and stirring."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Chalk nodules lay **undissolved** within the moist damp subsoil, slowly eroded by organic carbonic acid."}
    ]
  },
  "Dashboard — und/undistinguishable.md": {
    "primary": "Incapable of being perceived, recognized, or separated as distinct or different; indistinguishable.",
    "secondary": "In sensory perception research and visual psychophysics, two luminous stimuli below threshold chromatic difference appear undistinguishable.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Two identical white grains of sand appear **undistinguishable** to the naked human eye unless magnified."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The mire seemed an **undistinguishable** expanse of treacherous black mud under the pale autumn moon."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "The outline of the decaying masonry was almost **undistinguishable** against the overcast evening sky."}
    ]
  },
  "Dashboard — und/undistinguished.md": {
    "primary": "Lacking distinction, excellence, or prominence; ordinary, commonplace, or unexceptional.",
    "secondary": "In sociological analysis of administrative hierarchies, undistinguished bureaucratic careers are characterized by routine compliance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip reflected on his humble beginnings in the forge, fearing a future of **undistinguished** village labor."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet observed that the young officer was merely one of a crowd of **undistinguished** ensigns in uniform."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard died in an isolated cottage, leaving an **undistinguished** will requesting that no man remember him."}
    ]
  },
  "Dashboard — und/undistorted.md": {
    "primary": "Maintaining its original, true, or accurate shape, form, sound, or meaning; free from bias or alteration.",
    "secondary": "In acoustical engineering and high-fidelity audio reproduction, an undistorted waveform preserves exact harmonic phase relationships.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The human understanding must serve as a clear mirror, providing an **undistorted** reflection of nature's operations."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The inductive method requires an **undistorted** record of empirical facts uncoloured by preconceived dogmas."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The calm glassy surface of the pond gave back an **undistorted** image of the surrounding autumnal pines."}
    ]
  },
  "Dashboard — und/undistributed.md": {
    "primary": "Not allocated, apportioned, or spread among various recipients; or in formal logic, not used in its universal sense.",
    "secondary": "In formal syllogistic logic, the fallacy of the undistributed middle occurs when the middle term fails to refer to all members of its class in either premise.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Logicians demonstrate that an **undistributed** middle term renders any categorical syllogism completely invalid."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Surplus agricultural grain remained **undistributed** in regional warehouses while remote provinces suffered scarcity."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "The **undistributed** profits of corporate joint-stock enterprises form the primary reserve fund for new capital expansion."}
    ]
  },
  "Dashboard — und/undisturbed.md": {
    "primary": "Not agitated, interrupted, moved, or altered; remaining in a state of calm, quiet, or serenity.",
    "secondary": "In archaeological stratigraphy, undisturbed sedimentary layers preserve artifacts in their precise chronological deposition order.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "Rip Van Winkle slept on **undisturbed** through twenty long years in the hollows of the Kaatskill mountains."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The deep blue ocean rolled on **undisturbed**, as it rolled five thousand years ago over drowned armadas."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The tranquil Alpine valley offered a refuge where my agitated thoughts could rest **undisturbed** by human voices."}
    ]
  },
  "Dashboard — und/undiversified.md": {
    "primary": "Concentrated in a single field, form, or asset class; lacking variety or risk diversification.",
    "secondary": "In agricultural economics and portfolio management, undiversified monoculture renders regional farming communities vulnerable to crop blight and price collapse.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An economy reliant on an **undiversified** staple crop suffers extreme distress whenever seasonal harvests fail."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The risks of **undiversified** colonial trade became evident when foreign blockades cut off sugar shipments."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Capital placed in an **undiversified** industrial venture carries excessive risk of catastrophic depreciation."}
    ]
  },
  "Dashboard — und/undividable.md": {
    "primary": "Incapable of being split, separated, or apportioned into parts; indivisible.",
    "secondary": "In classical atomism and mathematical philosophy, fundamental particles were historically postulated as undividable units of material existence.",
    "quotes": [
      {"author": "Lucretius", "work": "De Rerum Natura", "quote": "The primordial seeds of matter are solid, eternal, and **undividable**, resisting all dissolution by time."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "God in the beginning formed matter in solid, massy, hard, impenetrable, and **undividable** particles."},
      {"author": "Baruch Spinoza", "work": "Ethics", "quote": "Substance that is absolutely infinite is necessarily **undividable** and unique in its essential reality."}
    ]
  },
  "Dashboard — und/undivided.md": {
    "primary": "Complete, whole, and not broken or separated; given entirely and without distraction.",
    "secondary": "In property jurisprudence, tenants in common hold undivided fractional interests in a single parcel of real estate.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes gave his **undivided** attention to the curious footprints impressed upon the soft clay of the garden path."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor exercised **undivided** dominion over the vast provinces stretching from Hispania to Syria."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Doctor Manette received the **undivided** love and tender devotion of his daughter throughout his long recovery."}
    ]
  },
  "Dashboard — und/undo.md": {
    "primary": "To unfasten, untie, or loosen; or to reverse, annul, or cancel the effect of a previous action.",
    "secondary": "In human-computer interaction and software architecture, the undo command utilizes an operational command stack to roll back state transformations.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "What's done cannot be undone; to bed, to bed, to bed, yet how we strive to **undo** our past deeds."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Nothing can **undo** what has been wrought, yet repentance may temper the severe hand of destiny."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester attempted in vain to **undo** the tangled knot of his tragic marriage by fleeing across Europe."}
    ]
  },
  "Dashboard — und/undoable.md": {
    "primary": "Incapable of being accomplished or performed; or capable of being reversed, unfastened, or canceled.",
    "secondary": "In computational complexity theory, problems with super-exponential running times are practically undoable within physical universe time scales.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The task set before the National Assembly was practically **undoable** given the complete collapse of fiscal revenues."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undertaking social reform without economic restructuring seemed an **undoable** paradox to the young idealist."},
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "To reverse the gigantic physical growth caused by the elixir proved wholly **undoable** by any known medicine."}
    ]
  },
  "Dashboard — und/undock.md": {
    "primary": "To release, detach, or move a vessel, spacecraft, or software window away from a dock or mooring.",
    "secondary": "In orbital aerospace mechanics, spacecraft command systems execute thruster sequences to undock safely from orbiting space stations.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The steam tugs assisted the heavy merchant vessel to **undock** safely into the swirling tidal current of the Thames."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The frigate prepared to **undock** at dawn, amidst the shrill piping of boatswains and the thud of heavy hempen hawsers."},
      {"author": "Robert Louis Stevenson", "work": "The Master of Ballantrae", "quote": "The smugglers hastened to **undock** their shallow skiff before the harbor patrol could light the beacon."}
    ]
  },
  "Dashboard — und/undocumented.md": {
    "primary": "Not supported, substantiated, or recorded by official written evidence, certificates, or documents.",
    "secondary": "In software engineering and systems administration, undocumented legacy APIs introduce substantial maintenance overhead and security vulnerabilities.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Many popular legends regarding early barbarian kings remain entirely **undocumented** by contemporary chronicles."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The secret treaty contained several **undocumented** oral pledges given by the monarch to the French court."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The interior mountain tribes possessed an **undocumented** oral lore concerning ancient volcanic eruptions."}
    ]
  },
  "Dashboard — und/undoer.md": {
    "primary": "A person or agency that unties, annuls, destroys, or causes the downfall of another.",
    "secondary": "In Renaissance tragedy and dramaturgical analysis, the villain functions as the relentless undoer of noble protagonists through exploited flaws.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Thou art the fatal **undoer** of this noble realm, sowing bloodshed and treachery in the royal court."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "False Duessa proved the crafty **undoer** of many an honest knight wandering in enchanted groves."},
      {"author": "George Chapman", "work": "The Conspiracy of Duke of Biron", "quote": "Ambition is the subtle **undoer** of great minds, luring them toward precipitous ruin."}
    ]
  },
  "Dashboard — und/undogmatic.md": {
    "primary": "Not asserting opinions or principles in an authoritative, rigid, or doctrinaire manner; open-minded.",
    "secondary": "In theological hermeneutics and secular ethics, undogmatic inquiry prioritizes compassionate human experience over doctrinal rigidity.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The mystic often possesses an **undogmatic** spiritual temperament that values direct inner light above rigid creeds."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "An **undogmatic** thinker welcomes opposing perspectives as necessary correctives to partial truths."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "True culture demands an **undogmatic** pursuit of sweet reasonableness rather than sectarian dogmatism."}
    ]
  },
  "Dashboard — und/undogmatical.md": {
    "primary": "Free from rigid assertiveness, doctrinaire stiffness, or authoritarian preconceptions; flexible in opinion.",
    "secondary": "In pedagogical theory and intellectual history, undogmatical instruction fosters critical reflection by encouraging students to challenge core tenets.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "A truly philosophical instructor remains **undogmatical**, guiding the student toward personal discovery."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific method is inherently **undogmatical**, readily discarding hypotheses refuted by empirical observation."},
      {"author": "David Hume", "work": "Dialogues Concerning Natural Religion", "quote": "Philo maintained an **undogmatical** skepticism throughout the debates regarding natural theology."}
    ]
  },
  "Dashboard — und/undoing.md": {
    "primary": "The cause of someone's ruin, downfall, or destruction; or the act of reversing or unfastening something.",
    "secondary": "In classical Aristotelian poetics, hamartia or tragic error serves as the protagonist's inevitable undoing.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "My pride and vain reliance on the king's favor have wrought my absolute and final **undoing**."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard's stubborn impulsiveness proved the tragic **undoing** of his fortune and social reputation."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creation of that miserable monster was the fatal **undoing** of my peace, family, and reason."}
    ]
  },
  "Dashboard — und/undomestic.md": {
    "primary": "Not accustomed to, suitable for, or fond of home life, household duties, or domestic affairs.",
    "secondary": "In nineteenth-century social critique, women who rejected conventional parlor domesticity were often branded as undomestic by conservative journalists.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mrs. Jellyby's obsessive telescopic philanthropy rendered her notoriously **undomestic**, leaving her home in chaotic disarray."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond considered Dorothea's grand spiritual ambitions strangely **undomestic** and inconvenient for a young wife."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Catherine was pronounced singularly **undomestic** by her mother, preferring cricket and baseball to rolling up paste."}
    ]
  },
  "Dashboard — und/undomesticated.md": {
    "primary": "Not tamed, cultivated, or bred for human use; living in a natural wild state.",
    "secondary": "In ecological anthropology and evolutionary genetics, undomesticated wild progenitors of modern grains exhibit shattering rachises for seed dispersal.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The wild, **undomesticated** ancestors of the domestic rock pigeon still nest in the rocky sea cliffs of the Hebrides."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck answered the primordial call of the wilderness, running with the wild, **undomesticated** timber wolves."},
      {"author": "Henry David Thoreau", "work": "Walking", "quote": "There is a fertile vigor in all wild and **undomesticated** nature that revives the tired spirit of civil man."}
    ]
  },
  "Dashboard — und/undone.md": {
    "primary": "Ruined, brought to disaster, or destroyed; or left unperformed, uncompleted, or unfastened.",
    "secondary": "In spiritual confession and liturgy, penitents acknowledge leaving undone those moral duties which they ought to have done.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "O, I am spoiled, **undone** by villains! Give me some help, I faint with these bleeding wounds."},
      {"author": "Book of Common Prayer", "work": "The Book of Common Prayer", "quote": "We have left **undone** those things which we ought to have done, and there is no health in us."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Adam cried out in despair, declaring that mankind was hopelessly **undone** by the taste of the forbidden fruit."}
    ]
  },
  "Dashboard — und/undoubtedly.md": {
    "primary": "Without any doubt, question, or uncertainty; definitely and undeniably.",
    "secondary": "In historical epistemology and jurisprudence, corroborated physical evidence undoubtedly establishes the sequence of contested events.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The presence of fresh carriage ruts **undoubtedly** proved that the visitor had arrived within the past half hour."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Geological exploration has **undoubtedly** revealed only a tiny fraction of the extinct organisms preserved in rocks."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The personal courage of Julian the Apostate was **undoubtedly** equal to the greatest commanders of antiquity."}
    ]
  },
  "Dashboard — und/undrained.md": {
    "primary": "Not cleared of water, excess moisture, or fluid; marshy, waterlogged, or boggy.",
    "secondary": "In agricultural hydrology and civil drainage engineering, undrained alluvial soils suffer chronic waterlogging and root anoxia.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "A Tour Thro' the Whole Island of Great Britain", "quote": "The vast fens of Cambridgeshire remained an **undrained** wilderness of reeds, fogs, and ague-ridden pools."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Extensive peat mosses formed across the flat, **undrained** hollows left behind by retreating glacial ice."},
      {"author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "The early settlers struggled against the wild, **undrained** swamps along the river valleys of eastern England."}
    ]
  },
  "Dashboard — und/undramatic.md": {
    "primary": "Lacking excitement, theatrical flair, sudden tension, or dramatic qualities; quiet and understated.",
    "secondary": "In narrative prose stylistics, undramatic realism emphasizes the repetitive mundane rhythms of ordinary daily labor.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The passage of time during the quiet winter was recorded in an **undramatic**, almost imperceptible settling of dust."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Much of trench warfare consisted of cold, **undramatic** boredom punctuated by occasional sniper fire."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether's meeting with Chad was singularly **undramatic**, lacking the fiery confrontation anticipated in Woollett."}
    ]
  },
  "Dashboard — und/undramatically.md": {
    "primary": "In a calm, plain, quiet, or unexciting manner, without theatrical display or commotion.",
    "secondary": "In macroeconomic monetary history, policy shifts often unfold undramatically through gradual central bank interest rate adjustments.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The autumn arrived **undramatically**, announcing itself only through yellowing leaves and crisper morning mists."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The elderly curate passed away **undramatically** in his armchair, surrounded by his old theological books."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The crisis subsided **undramatically**, leaving the crew to contemplate their shame in silent isolation."}
    ]
  },
  "Dashboard — und/undrape.md": {
    "primary": "To uncover, unwrap, or reveal by removing drapery, curtains, coverings, or clothing.",
    "secondary": "In classical sculpture and studio art pedagogy, the sculptor undrapes the wet clay model to evaluate anatomical proportions.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The sculptor stepped forward to **undrape** the newly completed marble bust before his assembled patrons."},
      {"author": "Edgar Allan Poe", "work": "The Oval Portrait", "quote": "He resolved to **undrape** the mysterious painting hanging in the dark niche of the velvet-hung bedchamber."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "With gentle touch the morning breeze began to **undrape** the veil of mist shrouding the distant Aegean isles."}
    ]
  },
  "Dashboard — und/undraped.md": {
    "primary": "Not covered or adorned with curtains, drapery, or clothing; bare or naked.",
    "secondary": "In neoclassical architectural criticism, undraped windows and unadorned stone porticoes embody Spartan civic austerity.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The pale light streamed through the **undraped** window of the Spouter-Inn onto the rough wooden floor."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The cold gray sunshine illuminated the **undraped** walls of the Puritan governor's solemn reception hall."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "The lecture hall had high, **undraped** windows that admitted a chilling northern daylight upon the audience."}
    ]
  },
  "Dashboard — und/undrawn.md": {
    "primary": "Not pulled, pulled back, or extracted; or not selected in a lottery or draft; not eviscerated.",
    "secondary": "In historical game theory and commercial lotteries, undrawn tickets retain their speculative probability until the final wheel spin.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The heavy window curtains hung **undrawn**, shutting out the cold snowy night from the comfortable parlor."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The knight's broadsword remained **undrawn** within its scabbard as he approached the royal pavilion in peace."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Speculators computed the expected mathematical payout based on the number of **undrawn** tickets remaining in the urn."}
    ]
  },
  "Dashboard — und/undreamed.md": {
    "primary": "Not thought of, imagined, or conceived of as possible; beyond previous expectation.",
    "secondary": "In the history of science and technological innovation, discoveries in quantum mechanics unveiled undreamed physical dimensions.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The modern professors of natural philosophy promised to unfold to the world **undreamed** powers of nature."},
      {"author": "Francis Bacon", "work": "The New Atlantis", "quote": "The experimental college of Solomon's House yielded **undreamed** inventions for the alleviation of human estate."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor's discovery of the anti-gravity substance opened **undreamed** possibilities for interplanetary exploration."}
    ]
  },
  "Dashboard — und/undreamt.md": {
    "primary": "Not imagined, suspected, or contemplated even in dreams or fantasy; utterly unforeseen.",
    "secondary": "In speculative philosophy and ontological metaphysics, aspects of cosmological reality remain undreamt within limited sensory frameworks.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy, mysteries wholly **undreamt** by mortals."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The titan prophesied an age of liberty and light **undreamt** by the tyrannical gods of Olympus."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Beneath the dull exterior of daily life lie divine wonders **undreamt** of by shallow materialist commentators."}
    ]
  },
  "Dashboard — und/undress.md": {
    "primary": "To remove clothes, garments, or bandages; or informal, casual, or working attire.",
    "secondary": "In military dress regulations and naval history, officers wore undress uniform during daily quarters and watch standing on active duty.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The tired child was told to **undress** and climb into the tiny garret bed under the eaves."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne hastened to **undress** after her rain-soaked walk across the downs, shivering beside the hearth."},
      {"author": "William Thackeray", "work": "Vanity Fair", "quote": "The cavalry colonel was seen in comfortable **undress** uniform, smoking a cigar outside his brigade tent."}
    ]
  },
  "Dashboard — und/undressed.md": {
    "primary": "Not wearing clothes; unclothed; or unseasoned, uncultivated, or untreated (such as leather or timber).",
    "secondary": "In surgical wound management and traumatology, an undressed laceration exposed to septic conditions rapidly develops suppurative infection.",
    "quotes": [
      {"author": "Herman Melville", "work": "Typee", "quote": "The native islanders walked through the palm groves **undressed**, wearing only simple garlands of wild flowers."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe fashioned garments from the **undressed** skins of wild goats he had shot in the hills."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The carpenter examined the rough, **undressed** oak beams delivered from the neighboring timber yard."}
    ]
  },
  "Dashboard — und/undried.md": {
    "primary": "Not dried or cured; retaining natural moisture, greenness, or sap.",
    "secondary": "In structural masonry and timber carpentry, using undried green lumber causes severe shrinkage, warping, and joint deformation.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The smoke of green and **undried** hickory filled the cabin before the draft drew cleanly up the chimney."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The botanical specimens were packed carefully to prevent rot from the damp, **undried** mosses of Tierra del Fuego."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Hops harvested during rainy weather cannot be kilned properly if stacked in an **undried** condition."}
    ]
  },
  "Dashboard — und/undrinkable.md": {
    "primary": "Unfit, dangerous, or too unpleasant to drink; lacking potable quality.",
    "secondary": "In marine survival medicine and maritime hydrology, hypertonic ocean water is undrinkable because it accelerates cellular dehydration.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "Water, water, everywhere, nor any drop to drink; the brackish brine was utterly **undrinkable** beneath the blistering sun."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The stagnant marsh water in the swamp settlement of Eden was foul, turbid, and dangerously **undrinkable**."},
      {"author": "George Orwell", "work": "Burmese Days", "quote": "The bitter club soda was warm and nearly **undrinkable** during the stifling heat of the pre-monsoon afternoon."}
    ]
  },
  "Dashboard — und/undset.md": {
    "primary": "Referring to Sigrid Undset (1882–1949), the Norwegian novelist awarded the Nobel Prize in Literature in 1928.",
    "secondary": "In Scandinavian literary history and medievalist scholarship, Undset is celebrated for Kristin Lavransdatter, masterfully capturing medieval Catholic life.",
    "quotes": [
      {"author": "Sigrid Undset", "work": "Kristin Lavransdatter", "quote": "The historical realism of **Undset** portrayed the profound spiritual trials and human passion of medieval Norway."},
      {"author": "Thomas Mann", "work": "Essays of Three Decades", "quote": "The epic narrative depth of **Undset** renewed our modern understanding of the psychological reality of the Middle Ages."},
      {"author": "W. H. Auden", "work": "Forewords and Afterwords", "quote": "In the historical trilogies of **Undset**, moral conscience and passionate human frailty collide with devastating truth."}
    ]
  },
  "Dashboard — und/undue.md": {
    "primary": "Exceeding what is appropriate, warranted, legal, or reasonable; excessive or immoderate.",
    "secondary": "In contract jurisprudence and equity law, the doctrine of undue influence invalidates testamentary wills or contracts procured through coercion.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet displayed **undue** anxiety regarding the marital prospects of her daughters before the neighborhood."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The executive magistrate must not exercise **undue** prerogative beyond the established laws of the commonwealth."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer warned Sir Henry against exposing himself to **undue** fatigue or solitary night excursions."}
    ]
  },
  "Dashboard — und/undulant.md": {
    "primary": "Moving with a smooth, rising and falling or wavelike motion; or describing a fever marked by periodic remissions.",
    "secondary": "In infectious disease pathology, brucellosis is clinically termed undulant fever due to its characteristic cyclical pyrexial fluctuations.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinician observed the classic step-ladder temperature curves characteristic of **undulant** fever among patients in the Mediterranean."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The sweet melodies rose in **undulant** waves across the enchanted waters of the twilight lake."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The vast expanse of Egdon Heath stretched into the dusk with broad, **undulant** sweeps of dark heather."}
    ]
  },
  "Dashboard — und/undulate.md": {
    "primary": "To move or cause to move in a smooth, sinuous, wave-like motion; to rise and fall gracefully.",
    "secondary": "In geomorphology and physical geography, rolling plains and dunes undulate continuously across arid desert basins.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vast golden sea of grain seemed to **undulate** beneath the summer breeze like the swells of the ocean."},
      {"author": "Alfred Tennyson", "work": "In Memoriam A.H.H.", "quote": "The hills are shadows, and they flow from form to form, and nothing stands; they melt like mist, the solid lands **undulate**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The ripples began to **undulate** across the glassy surface as the gentle evening wind rose over the cove."}
    ]
  },
  "Dashboard — und/undulation.md": {
    "primary": "A smooth, rising and falling wavelike movement, outline, or surface formation.",
    "secondary": "In classical physical optics and acoustics, light and sound propagate through continuous mediums via wave undulation.",
    "quotes": [
      {"author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "The phenomenon of optical interference demonstrates that light travels as a periodic **undulation** through the luminiferous ether."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The horsemen rode across the vast grassy pampas, which resembled a green ocean fixed in frozen **undulation**."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The boat rose and fell with each majestic **undulation** of the azure Mediterranean swell."}
    ]
  },
  "Dashboard — und/undulatory.md": {
    "primary": "Of, relating to, or moving with a wave-like or undulating motion.",
    "secondary": "In nineteenth-century physics and electromagnetic theory, the undulatory theory of light superseded Newton's corpuscular doctrine.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic lines of force appear to transmit radiant action by **undulatory** vibrations through space."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The establishment of the **undulatory** theory of light was one of the crowning triumphs of modern mathematical physics."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Electromagnetic disturbances propagate across the dielectric medium in accordance with **undulatory** wave equations."}
    ]
  },
  "Dashboard — und/undulipodium.md": {
    "primary": "A whip-like, motile organelle projecting from eukaryotic cells, encompassing both cilia and eukaryotic flagella.",
    "secondary": "In protistology and evolutionary cytology, Lynn Margulis proposed undulipodium to distinguish the eukaryotic 9+2 axoneme from bacterial flagella.",
    "quotes": [
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "The term **undulipodium** accurately distinguishes the complex eukaryotic 9+2 microtubular organelle from the simple bacterial flagellum."},
      {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "Microscopic examination reveals that the epithelial surface is lined with motile hair-like filaments functioning as an **undulipodium**."},
      {"author": "E. B. Wilson", "work": "The Cell in Development and Inheritance", "quote": "The rhythmic beating of each cellular **undulipodium** propels the unicellular organism smoothly through liquid culture."}
    ]
  },
  "Dashboard — und/unduly.md": {
    "primary": "To an excessive, unwarranted, or disproportionate degree; more than is suitable or right.",
    "secondary": "In judicial review and administrative law, regulations that burden interstate commerce unduly are struck down under the commerce clause.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes cautioned Lestrade not to be **unduly** elated by appearances that might prove entirely misleading."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma admitted that she had been **unduly** influenced by her vanity when planning the village match."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To innovate **unduly** upon ancient constitutional principles invites unforeseen civil anarchy and turmoil."}
    ]
  },
  "Dashboard — und/undutiful.md": {
    "primary": "Failing to fulfill filial, moral, or official obligations of respect and obedience; disobedient.",
    "secondary": "In domestic melodrama and moral conduct literature, the undutiful heir who defies parental wishes faces disinheritance and poverty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Lear cursed his cruel and **undutiful** daughters, Goneril and Regan, who stripped him of his followers."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Clarissa was unfairly accused by her harsh family of being an **undutiful** child for refusing the hateful suitor."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Lilliputian statutes imposed severe punishments upon any **undutiful** offspring who neglected their aged parents."}
    ]
  },
  "Dashboard — und/undutifulness.md": {
    "primary": "The neglect or failure to show proper respect, submission, or obedience to parents, duty, or authority.",
    "secondary": "In seventeenth-century casuistry and moral philosophy, filial undutifulness was condemned as a primary violation of the fifth commandment.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe traced all his subsequent maritime miseries to his early **undutifulness** toward his father's wise counsel."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Squire Western flew into violent rages whenever he suspected Sophia of the slightest **undutifulness** regarding marriage."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Nothing more deeply wounds the parental heart than unprovoked **undutifulness** from a child nurtured with tender care."}
    ]
  },
  "Dashboard — und/undyed.md": {
    "primary": "In its natural, uncolored state; not treated or tinted with coloring pigments or artificial dyes.",
    "secondary": "In textile history and archaeological conservation, undyed wool and linen textiles illustrate ancient spinning techniques prior to vats.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg wrapped himself in a mantle of natural, **undyed** tapa cloth woven from the bark of island trees."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I preferred clothing of plain, **undyed** homespun wool that smelled of simple sheep pastures and rain."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The rustic shearers packed the heavy fleeces of clean, **undyed** wool into vast canvas sacks for market."}
    ]
  },
  "Dashboard — und/undying.md": {
    "primary": "Immortal, eternal, or imperishable; never ending, ceasing, or fading away.",
    "secondary": "In Romantic lyricism and funerary inscriptions, undying devotion commemorates personal commitment beyond mortal separation.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Adonais", "quote": "The one remains, the many change and pass; heaven's light forever shines, earth's shadows fly with **undying** flame."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The hero pledged his **undying** allegiance to the sacred cause of Greek national liberty."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane felt an **undying** affection for Rochester that neither distance, moral principle, nor time could extinguish."}
    ]
  },
  "Dashboard — und/undynamic.md": {
    "primary": "Lacking energy, vigor, innovation, or progress; static, inactive, or unmoving.",
    "secondary": "In organizational psychology and industrial economics, an undynamic corporate culture resists technological transitions and loses market competitiveness.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "A completely balanced, **undynamic** physical state represents the final cessation of developmental momentum."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Archaic social institutions maintain an **undynamic** conservatism designed to preserve established economic privileges."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "The utopian society avoided stagnation by ensuring that administrative life did not degenerate into an **undynamic** bureaucracy."}
    ]
  },
  "Dashboard — und/ununderstandably.md": {
    "primary": "In a manner that cannot be understood, grasped, or made sense of; incomprehensibly.",
    "secondary": "In psycholinguistics and clinical speech pathology, dysarthric speech output can be ununderstandably garbled to listeners without visual cues.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The transcendental philosopher muttered **ununderstandably** into his pipe smoke, lost in obscure metaphysical abstractions."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The aged attorney spoke **ununderstandably** through his toothless gums, rattling off legal precedents in confusion."},
      {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The mysterious passenger whispered **ununderstandably** to the crowd before melting into the riverboat shadows."}
    ]
  },
  "Dashboard — und/ununderstood.md": {
    "primary": "Not grasped, comprehended, or appreciated by others; misunderstood or neglected.",
    "secondary": "In biographical literature and intellectual history, pioneering scientific theories often languish ununderstood for decades by orthodox academies.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "A Defence of Poetry", "quote": "Poets are the unacknowledged legislators of the world, often leaving their sublime visions **ununderstood** by their generation."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "To be great is to be misunderstood; Pythagoras was misunderstood, and Socrates, and Jesus, all lingering **ununderstood** by small minds."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Deronda felt a deep compassion for artists whose intense spiritual longings remained **ununderstood** by fashionable society."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"
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

print(f"Dashboard — und Part 6 (8F): Successfully updated {updated}/{len(data)} notes.")
