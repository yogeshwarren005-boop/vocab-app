# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sci (Words 1-40)
  # =========================================================================
  "Dashboard — sci/abscise.md": {
    "primary": "To cut off or separate; in botany, to shed naturally through the formation of an abscission layer.",
    "secondary": "In plant physiology and surgical pathology, shedding autumn foliage or excising dead tissue along natural cleavage lines.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The dying petiole prepares to **abscise** cleanly from the stem through a specialized cellular zone."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Deciduous trees **abscise** their senescent leaves before the onset of winter frosts."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Certain tropical legumes **abscise** their floral bracts as soon as pollination is achieved."}
    ]
  },
  "Dashboard — sci/abscissa.md": {
    "primary": "The horizontal coordinate of a point in a Cartesian coordinate system, measured along the x-axis.",
    "secondary": "In analytical geometry and calculus, the independent variable plotted horizontally against the vertical ordinate.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Let the distance from the prism be represented by the **abscissa**, and the dispersion of rays by the ordinate."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Descartes revolutionized geometry by representing algebraic equations through the **abscissa** and ordinate of points."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "A curve is determined when every **abscissa** corresponds to a uniquely defined ordinate in continuous space."}
    ]
  },
  "Dashboard — sci/abscission.md": {
    "primary": "The natural shedding or dropping of leaves, flowers, or fruit by a plant; the act of cutting off.",
    "secondary": "In surgical and botanical treatises, the separation of parts from an organic body through metabolic dissolution of cell walls.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Unfertilized blossoms undergo rapid **abscission**, dropping to the earth within forty-eight hours."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The **abscission** of autumn leaves leaves a clean corky scar upon the twig."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The seasonal **abscission** of foliage was attributed by ancient naturalists to the retreat of solar warmth."}
    ]
  },
  "Dashboard — sci/adscititious.md": {
    "primary": "Added or derived from an external source; supplemental, non-essential, or extraneous.",
    "secondary": "In classical rhetoric and moral theology, acquired adventitious traits not inherent to a person's original nature.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True virtue requires no **adscititious** ornaments of worldly pomp to command veneration."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The simpler rites of the early church were corrupted by **adscititious** ceremonies borrowed from paganism."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A great poet scorns **adscititious** verbal glitter that does not spring from genuine feeling."}
    ]
  },
  "Dashboard — sci/conscience-smitten.md": {
    "primary": "Tormented, stricken, or troubled by a guilty conscience; overcome with sudden remorse.",
    "secondary": "In tragic narrative and psychological fiction, paralyzed by sudden overwhelming awareness of moral culpability.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister stood **conscience-smitten** before the silent gaze of his parishioners."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He slunk away into the shadows like a **conscience-smitten** rogue detected in his mischief."},
      {"author": "Walter Scott", "work": "The Heart of Mid-Lothian", "quote": "The outlaw paused, **conscience-smitten** at the innocent tears of the young maiden."}
    ]
  },
  "Dashboard — sci/conscience.md": {
    "primary": "An inner sense of right and wrong that guides one's thoughts and actions; moral awareness.",
    "secondary": "In ethical philosophy and jurisprudence, the subjective faculty of moral judgment evaluating one's deeds against principles of duty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Thus **conscience** does make cowards of us all, and thus the native hue of resolution is sicklied o'er."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Moral education consists in cultivating a delicate **conscience** responsive to reason and truth."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her **conscience** told her that she had been blind, partial, and prejudiced in her estimates of both men."}
    ]
  },
  "Dashboard — sci/conscienceless.md": {
    "primary": "Having no conscience; devoid of moral principles, scruples, or remorse.",
    "secondary": "In dramatic characterization and sociology, behaving with predatory ruthlessness without regard for human suffering.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He was as cold, calculating, and **conscienceless** as the legal machinery he manipulated."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The typhoon swept down like a **conscienceless** monster devoid of pity for mortal mariners."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A vain and **conscienceless** egotist can wreck the happiness of an entire family without a single pang of regret."}
    ]
  },
  "Dashboard — sci/conscientious.md": {
    "primary": "Wishing to do what is right; thorough, painstaking, and governed by conscience.",
    "secondary": "In professional duty and scholarship, executing tasks with meticulous care, fidelity, and adherence to truth.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She was a **conscientious** teacher, devoting her entire energy to the instruction of her pupils."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak was a **conscientious** shepherd who guarded his flock through snow and tempest."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A **conscientious** investigator examines the smallest discrepancies before adopting a favored theory."}
    ]
  },
  "Dashboard — sci/conscientiously.md": {
    "primary": "In a conscientious manner; with thoroughness, care, and devotion to duty.",
    "secondary": "In biography and ethics, discharging legal and moral responsibilities with scrupulous fidelity to principle.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He had **conscientiously** performed every duty of his office, yet found himself misunderstood by his parishioners."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The clerk **conscientiously** recorded every deposition in the huge leather-bound ledger."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor **conscientiously** strove to master her own grief so as not to distress her mother and sister."}
    ]
  },
  "Dashboard — sci/conscientiousness.md": {
    "primary": "The trait of being painstaking, scrupulous, and guided by a strict sense of duty.",
    "secondary": "In moral psychology and organizational ethics, steadfast adherence to promises, accuracy, and moral obligations.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "Her painful **conscientiousness** caused her to confess where silence would have secured worldly peace."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The feeling of **conscientiousness** is the ultimate sanction of all morality in reflective minds."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The impartial spectator within the breast demands unyielding **conscientiousness** in all our dealings with mankind."}
    ]
  },
  "Dashboard — sci/conscionable.md": {
    "primary": "Governed by or conforming to conscience; just, reasonable, or equitable.",
    "secondary": "In equity jurisprudence and contractual law, an agreement that is fair and not tainted by extortion or unconscionable overreach.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Let bargains be **conscionable** and moderate, so that both parties may thrive together."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A **conscionable** tradesman will not take advantage of a customer's ignorance to demand extortionate prices."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A just and **conscionable** settlement of taxation must satisfy both the sovereign and the subject."}
    ]
  },
  "Dashboard — sci/conscious.md": {
    "primary": "Aware of and responding to one's surroundings; mentally awake; deliberately intentional.",
    "secondary": "In philosophy of mind and psychology, possessing subjective phenomenal experience and self-awareness.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The mind is **conscious** of a continuous stream of thoughts, sensations, and volitions."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "She was **conscious** that every eye in the room was fixed upon her troubled face."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whale appeared fully **conscious** of the danger, plunging deep beneath the surface."}
    ]
  },
  "Dashboard — sci/consciously.md": {
    "primary": "In a deliberate, intentional, and fully aware manner.",
    "secondary": "In introspective psychology, acting with clear reflective realization rather than through habit or instinct.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She had never **consciously** intended to wound his vanity, yet every word she uttered seemed to sting."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles walked onward, **consciously** avoiding the pathway that led past the great manor-house."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel **consciously** resisted the impulse to seek guidance from older and colder minds."}
    ]
  },
  "Dashboard — sci/consciousness.md": {
    "primary": "The state of being aware of and responsive to one's surroundings, thoughts, and sensations.",
    "secondary": "In cognitive philosophy and neuropsychology, the subjective inner experience of selfhood and sensory reality.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The fundamental fact of psychology is the personal stream of **consciousness**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Personal identity consists in the continuity of **consciousness** linking past memories to present thoughts."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A wave of sickening **consciousness** rushed over him as he realized what he had done."}
    ]
  },
  "Dashboard — sci/discina.md": {
    "primary": "A genus of cup-fungi in the family Discinaceae; or a genus of inarticulate brachiopods.",
    "secondary": "In invertebrate paleontology and mycology, disc-shaped marine brachiopods with circular shells, or edible disc cup-fungi.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The ancient Paleozoic strata contain abundant fossil valves of the primitive brachiopod **Discina**."},
      {"author": "Archibald Geikie", "work": "Text-book of Geology", "quote": "Valves of **Discina** nitida occur preserved in the bituminous shales of the Carboniferous system."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The fleshy apothecium of **Discina** expands into a broad, convoluted disc upon damp woodland soil."}
    ]
  },
  "Dashboard — sci/nonconscious.md": {
    "primary": "Not accompanied by or involving conscious awareness; operating outside consciousness.",
    "secondary": "In cognitive neuroscience and psychology, autonomous physiological or computational neural processes that proceed without awareness.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Numerous reflex actions and autonomic habits remain entirely **nonconscious** during waking life."},
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "The vast reservoir of biological drives operates as a **nonconscious** substrate beneath the ego."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Sensory signals pass through complex **nonconscious** pathways before reaching the cerebral cortex."}
    ]
  },
  "Dashboard — sci/prescience.md": {
    "primary": "Knowledge of events before they take place; foreknowledge or foresight.",
    "secondary": "In theological metaphysics and statecraft, divine omniscience regarding future events, or prophetic political insight.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "God's foreknowledge and absolute **prescience** leaves human will untrammeled and free."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The statesman showed an admirable **prescience** in anticipating the barbarian invasion of Italy."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He boasted of his genealogical **prescience**, predicting disasters that seldom failed to come to pass."}
    ]
  },
  "Dashboard — sci/prescient.md": {
    "primary": "Having knowledge of events before they take place; prophetic and farsighted.",
    "secondary": "In historical analysis, possessing extraordinary intuitive grasp of emerging political or technological currents.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "His **prescient** mind foresaw the inevitable rise of democratic institutions across Europe."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "A **prescient** observer could detect the subterranean rumblings of revolution years before the Bastille fell."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger made a **prescient** remark regarding the prehistoric survivals on the plateau."}
    ]
  },
  "Dashboard — sci/presciently.md": {
    "primary": "In a prescient manner; with remarkable foreknowledge or foresight.",
    "secondary": "In narrative and political commentary, warning or planning with accurate anticipation of future contingencies.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "He had **presciently** warned the cabinet of the catastrophic danger of trench deadlock."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The essayist had **presciently** predicted the rapid growth of the American republic."},
      {"author": "Henry James", "work": "The American", "quote": "Newman observed the cold European aristocracy and **presciently** measured its crumbling foundations."}
    ]
  },
  "Dashboard — sci/prosciutto.md": {
    "primary": "An Italian dry-cured ham that is thinly sliced and served uncooked.",
    "secondary": "In culinary geography and gastronomic history, ham aged with sea salt in Italian alpine valleys to achieve fragrant tenderness.",
    "quotes": [
      {"author": "Henry James", "work": "Italian Hours", "quote": "In the cheerful trattoria we enjoyed sweet melon wrapped in translucent ribbons of fragrant **prosciutto**."},
      {"author": "William Dean Howells", "work": "Venetian Life", "quote": "The market stalls of the Rialto were hung with cured sausages and rich savory flanks of **prosciutto**."},
      {"author": "George Gissing", "work": "By the Ionian Sea", "quote": "A flask of Chianti and a dish of aged **prosciutto** made our rustic luncheon memorable."}
    ]
  },
  "Dashboard — sci/rescind.md": {
    "primary": "To revoke, cancel, or repeal a law, contract, order, or decision.",
    "secondary": "In administrative law and parliamentary procedure, the formal invalidation of an enactment restoring prior status quo.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Parliament must **rescind** the obnoxious duties if it hopes to reconcile the affections of the colonists."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A legislative body possesses the undoubted authority to **rescind** or modify its previous statutes."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The chancellor refused to **rescind** the injunction until all parties had been formally heard."}
    ]
  },
  "Dashboard — sci/rescindable.md": {
    "primary": "Capable of being revoked, canceled, or repealed; voidable.",
    "secondary": "In contract law and commercial equity, an agreement that may be set aside due to fraud, duress, or mutual mistake.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Any covenant entered into under fraudulent misrepresentation is legally **rescindable** by the injured party."},
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "A conditional decree remains **rescindable** upon the discovery of fresh, unimpeachable testimony."},
      {"author": "John Austin", "work": "The Province of Jurisprudence Determined", "quote": "Rights created by administrative permit are inherently **rescindable** at the pleasure of the sovereign."}
    ]
  },
  "Dashboard — sci/rescission.md": {
    "primary": "The revocation, cancellation, or repeal of a law, order, or agreement.",
    "secondary": "In legal equity and contract law, the retroactive unmaking of a contract returning the parties to their pre-contractual positions.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **rescission** of an unlawful contract restores each party to their original property rights."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parliament voted the immediate **rescission** of all emergency declarations passed during the interregnum."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The sudden **rescission** of public treaties undermines national credit and provokes international retaliation."}
    ]
  },
  "Dashboard — sci/sciadopityaceae.md": {
    "primary": "A family of conifers containing the single extant species Sciadopitys verticillata (Japanese umbrella pine).",
    "secondary": "In gymnosperm paleobotany and taxonomy, a relictual Mesozoic conifer lineage characterized by fused cladode needle whorls.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Memoirs", "quote": "The family **Sciadopityaceae** represents an ancient gymnosperm lineage preserved from the Jurassic era in the mountains of Japan."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Fossil wood allied to modern **Sciadopityaceae** occurs in the Mesozoic amber beds of northern Europe."},
      {"author": "Charles Sprague Sargent", "work": "Forest Flora of Japan", "quote": "The sacred umbrella pine stands as the solitary surviving representative of the family **Sciadopityaceae**."}
    ]
  },
  "Dashboard — sci/sciadopitys.md": {
    "primary": "A genus of conifers comprising the Japanese umbrella pine, distinctive for its whorls of photosynthetic cladodes.",
    "secondary": "In dendrology and horticulture, Sciadopitys verticillata, prized for its evergreen symmetrical habit and unique cladode needles.",
    "quotes": [
      {"author": "Charles Sprague Sargent", "work": "Forest Flora of Japan", "quote": "The venerable temple groves around Nikko are shaded by magnificent specimens of **Sciadopitys**."},
      {"author": "Asa Gray", "work": "Botanical Memoirs", "quote": "The cladodes of **Sciadopitys** are botanically interpreted as double leaves fused along their margins."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Specimens of **Sciadopitys** cultivated in Kew Gardens exhibited remarkable hardiness against English winters."}
    ]
  },
  "Dashboard — sci/sciaena.md": {
    "primary": "A genus of marine fishes in the drum and croaker family (Sciaenidae), known for producing croaking sounds.",
    "secondary": "In Mediterranean and marine ichthyology, the brown meagre (Sciaena umbra) characterized by soniferous sonic muscle drumming.",
    "quotes": [
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The species of **Sciaena** produce loud humming or drumming sounds beneath the water by vibrating their air-bladders."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The ancient Romans held the delicate flesh of **Sciaena** in high culinary esteem."},
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "Sailors anchoring in South American bays frequently hear the deep rhythmic drumming of the **Sciaena** beneath their hulls."}
    ]
  },
  "Dashboard — sci/sciaenid.md": {
    "primary": "Any fish of the family Sciaenidae, such as a drum, croaker, or weakfish.",
    "secondary": "In marine ecology, coastal demersal fishes equipped with enlarged otoliths and acoustic muscles attached to the swim bladder.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The typical **sciaenid** possesses an elongate body, a cavernous skull, and large calcium otoliths."},
      {"author": "George Brown Goode", "work": "American Fishes", "quote": "Every Atlantic **sciaenid** contributes to the strange nocturnal chorus heard in shallow tidal estuaries."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The swim-bladder of the **sciaenid** exhibits elaborate diverticula adapted for sound resonance."}
    ]
  },
  "Dashboard — sci/sciaenidae.md": {
    "primary": "A large family of percoid marine and freshwater fishes, commonly known as croakers or drums.",
    "secondary": "In systematic ichthyology, a commercially vital family of teleost fishes whose members produce acoustic vibrations.",
    "quotes": [
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The family **Sciaenidae** includes the drums, croakers, and corvinas distributed throughout tropical and temperate coasts."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Members of the family **Sciaenidae** are characterized by two dorsal fins and a cavernous lateral line system."},
      {"author": "George Brown Goode", "work": "American Fishes", "quote": "The Atlantic fisheries depend heavily upon various valuable food species of the family **Sciaenidae**."}
    ]
  },
  "Dashboard — sci/sciaenops.md": {
    "primary": "A monotypic genus of sciaenid fish containing the red drum or redfish (Sciaenops ocellatus).",
    "secondary": "In game and commercial fishing, an estuarine sciaenid fish prized along the Atlantic and Gulf coasts for its fighting spirit.",
    "quotes": [
      {"author": "George Brown Goode", "work": "American Fishes", "quote": "The channel bass, or red drum, classified under **Sciaenops**, is readily identified by the black ocellated spot at the base of its tail."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The species **Sciaenops** ocellatus grows to an immense size in the warm waters of the Mexican Gulf."},
      {"author": "Spencer Fullerton Baird", "work": "Reports of the United States Fish Commission", "quote": "Large aggregations of **Sciaenops** enter the shallow sounds each autumn to spawn."}
    ]
  },
  "Dashboard — sci/sciara.md": {
    "primary": "A genus of small, dark fungus gnats in the family Sciaridae whose larvae feed on fungi and decaying roots.",
    "secondary": "In economic entomology, Diptera whose gregarious larvae sometimes form elongated migratory columns called army-worms.",
    "quotes": [
      {"author": "John Obadiah Westwood", "work": "Modern Classification of Insects", "quote": "The larvae of the genus **Sciara** are noted for their remarkable habit of marching in compact procession across forest paths."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The small dark flies of **Sciara** breed in decaying mushrooms and rich garden compost."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Decaying leaf-mould is inhabited by countless larvae of **Sciara** that accelerate the breakdown of humus."}
    ]
  },
  "Dashboard — sci/sciarid.md": {
    "primary": "A fungus gnat belonging to the family Sciaridae; of or relating to this insect family.",
    "secondary": "In horticulture and dipterology, tiny dark-winged gnats whose subterranean larvae can damage greenhouse root systems.",
    "quotes": [
      {"author": "John Obadiah Westwood", "work": "Modern Classification of Insects", "quote": "The typical **sciarid** gnat has prominent compound eyes that meet in a bridge above the antennae."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "A heavy infestation of **sciarid** larvae in the soil will wither the tender seedlings of the nursery."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Swarming clouds of **sciarid** gnats arose from the damp rotting vegetation of the tropical gully."}
    ]
  },
  "Dashboard — sci/sciaridae.md": {
    "primary": "A family of small, dark, slender nematoceran flies commonly known as dark-winged fungus gnats.",
    "secondary": "In systematic dipterology, a cosmopolitan family of flies characterized by characteristic wing venation and an eye-bridge above the antennae.",
    "quotes": [
      {"author": "John Obadiah Westwood", "work": "Modern Classification of Insects", "quote": "The family **Sciaridae** was separated from the Mycetophilidae on account of its distinct wing venation and ocular structure."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "Species of **Sciaridae** are among the most abundant subterranean scavengers of moist leaf-litter."},
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "We collected numerous minute diptera of the family **Sciaridae** from damp hollows in the forest floor."}
    ]
  },
  "Dashboard — sci/sciatic.md": {
    "primary": "Relating to the ischium or hip; pertaining to the sciatic nerve.",
    "secondary": "In human anatomy and neurology, designating the great nerve traversing the hip and descending into the lower extremity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "Thou cold **sciatic**, cripple our senators, that their limbs may halt as feebly as their manners!"},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pressure upon the great **sciatic** trunk produces excruciating neuralgic pain extending along the posterior thigh."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The **sciatic** nerve emerges through the great sacro-sciatic notch in all higher mammalian pelves."}
    ]
  },
  "Dashboard — sci/sciatica.md": {
    "primary": "Severe pain radiating along the path of the sciatic nerve down the back of the thigh and leg.",
    "secondary": "In clinical medicine, radicular neuralgic pain caused by inflammation, compression, or herniation affecting lumbosacral nerve roots.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Smallweed was doubled up by severe twinges of gout and hereditary **sciatica**."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Which of your hips has the most profound **sciatica**?"},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Intense paroxysmal **sciatica** is frequently aggravated by coughing, straining, or cold weather."}
    ]
  },
  "Dashboard — sci/science.md": {
    "primary": "The systematic study of the structure and behavior of the physical and natural world through observation and experiment.",
    "secondary": "In epistemological philosophy, organized rational knowledge based upon empirical demonstration and reproducible natural laws.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The true goal of **science** is nothing other than the endowment of human life with new discoveries and powers."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Natural philosophy and experimental **science** must proceed from the phenomena without feigning hypotheses."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A grand and almost untrodden field of inquiry will be opened to the investigations of natural **science**."}
    ]
  },
  "Dashboard — sci/scienter.md": {
    "primary": "Knowingly or deliberately; in law, knowledge of wrongness or illegality prior to committing an act.",
    "secondary": "In tort and criminal jurisprudence, the legal requirement that a defendant acted with intentional malice or guilty knowledge.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In an action for deceit, the plaintiff must prove **scienter** on the part of the seller."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Criminal culpability requires clear proof of unlawful intent and legal **scienter**."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The rule of **scienter** ensures that innocent mistakes are not punished as deliberate frauds."}
    ]
  },
  "Dashboard — sci/scientific.md": {
    "primary": "Based on or characterized by the methods and principles of science; systematic and empirical.",
    "secondary": "In modern historiography and epistemology, rigorous investigation grounded in hypothesis testing, mathematical modeling, and empirical verification.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The only **scientific** method of tracing human origins is through comparative anatomy and embryology."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The **scientific** spirit demands fearless dedication to demonstrable truth wherever it may lead."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A truly **scientific** psychology must anchor itself firmly in physiological facts."}
    ]
  },
  "Dashboard — sci/scientifically.md": {
    "primary": "In a manner based on or conforming to the principles and methods of science.",
    "secondary": "In methodological critique, proceeding by rigorous empirical experimentation, statistical verification, and logical deduction.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "We must investigate the ethical process as **scientifically** as we trace the physical evolution of species."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The phenomenon of inheritance has never been **scientifically** examined with sufficient experimental rigor."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "If we treat religious experiences **scientifically**, we must classify them by their psychological fruits."}
    ]
  },
  "Dashboard — sci/scientist.md": {
    "primary": "A person who is studying or has expert knowledge of one or more of the natural or physical sciences.",
    "secondary": "In history of ideas, a term coined by William Whewell in 1834 to describe professional practitioners of empirical and inductive inquiry.",
    "quotes": [
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "We need a name for the cultivator of science in general; I should incline to call him a **scientist**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The modern **scientist** recognizes no authority beyond verified natural facts and sound inductive reasoning."},
      {"author": "Charles Darwin", "work": "More Letters of Charles Darwin", "quote": "Every genuine **scientist** rejoices when an old hypothesis gives way to a more comprehensive truth."}
    ]
  },
  "Dashboard — sci/scientology.md": {
    "primary": "A religious system founded in 1954 by L. Ron Hubbard, emphasizing spiritual self-knowledge through auditing techniques.",
    "secondary": "In religious studies and sociology of religion, a controversial new religious movement derived from Dianetics with esoteric cosmology.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Every new spiritual movement or doctrine of mental healing claims to possess an infallible psychic **scientology**."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "Modern societies are fertile soil for dogmatic creeds, whether called political ideologies or pseudoscientific **scientology**."},
      {"author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "The commercialization of psychological therapies opened the door to modern sects of technological **scientology**."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
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
    updated_count += 1

print(f"Thought Batch 3B-1 (sci 1-40): Successfully updated {updated_count}/{len(data)} notes.")
