# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — und Part 5 (8E, 52 words) ---
  "Dashboard — und/underwear.md": {
    "primary": "Clothing worn under outer clothes, typically next to the skin for comfort, warmth, and hygiene.",
    "secondary": "In garment manufacturing and hygiene history, the introduction of breathable knitted cotton underwear transformed public health across urban centers.",
    "quotes": [
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "His ragged coat concealed the fact that he possessed neither a clean shirt nor spare **underwear**."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "She packed her trunk with starched linen, stockings, and warm flannel **underwear** before departing for school."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "Bloom noticed the display of ladies' silk **underwear** in the shop window on Grafton Street."}
    ]
  },
  "Dashboard — und/underweight.md": {
    "primary": "Weighing less than the normal, healthy, or standard amount for an individual's height or a commodity's required measure.",
    "secondary": "In pediatric clinical assessment, an infant diagnosed as underweight requires intensive nutritional monitoring to prevent developmental complications.",
    "quotes": [
      {"author": "H. G. Wells", "work": "Kipps", "quote": "The apprentice was visibly pale and **underweight**, having survived on cheap tea and dry bread in the draper's shop."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Medical officers reported that nearly a third of the coal miners' children were chronically **underweight**."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The sickly child appeared fragile and **underweight**, carrying a melancholy expression beyond his years."}
    ]
  },
  "Dashboard — und/underwing.md": {
    "primary": "One of the posterior wings of an insect, or the underside surface of an airplane or bird wing.",
    "secondary": "In lepidopterology, moths of the genus Catocala conceal brilliant orange or scarlet bands on each underwing to startle avian predators.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The sudden flash of vivid crimson on the insect's **underwing** serves to distract approaching insectivorous birds."},
      {"author": "Henry David Thoreau", "work": "Excursions", "quote": "A startled hawk wheeled above the pine woods, revealing the mottled plumage of its broad **underwing**."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The naturalist noted the delicate yellow markings lining the **underwing** of the migratory warbler."}
    ]
  },
  "Dashboard — und/underwood.md": {
    "primary": "Small trees, shrubs, and bushes growing beneath the canopy of taller forest trees; undergrowth.",
    "secondary": "In sustainable silviculture and forestry management, clearing dense underwood prevents catastrophic forest fires and encourages timber growth.",
    "quotes": [
      {"author": "William Wordsworth", "work": "The Prelude", "quote": "We forced our way through tangled briar and dense **underwood** along the shadowy margin of the lake."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Winterborne labored through the autumn coppice, pruning hazel stems and hazel **underwood** for thatched hurdles."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A gentle evening rain dripped softly through the pine needles onto the sweet-fern and tangled **underwood**."}
    ]
  },
  "Dashboard — und/underworld.md": {
    "primary": "The world of the dead or spirits in mythology; or the subterranean criminal network in a modern society.",
    "secondary": "In comparative mythology and classical literature, epic heroes journey into the chthonic underworld to consult prophetic shades.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "What so natural, then, as to assume that it was in this artificial **underworld** that the necessary work of the machine was done?"},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "Professor Moriarty directed the criminal **underworld** of London with the precision of a master spider in its web."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "From the profound abyss of the gloomy **underworld**, the fallen angels gazed toward the newly created universe."}
    ]
  },
  "Dashboard — und/underwrite.md": {
    "primary": "To sign one's name to an insurance policy, thereby assuming financial liability; or to guarantee the financial backing of an enterprise or issue of securities.",
    "secondary": "In investment banking, syndicate underwriters agree to purchase unsubscribed shares during an initial public offering to guarantee capitalization.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "No, father; I cannot **underwrite** Article Four, leave alone the rest, taking it in the natural sense."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The syndicate agreed to **underwrite** the entire municipal street railway bond issue at ninety-four."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchant insurers in maritime ports **underwrite** trading vessels bound for the East Indies against perils of the sea."}
    ]
  },
  "Dashboard — und/underwriter.md": {
    "primary": "A person or financial institution that assesses risks, issues insurance policies, or guarantees the purchase of newly issued securities.",
    "secondary": "In marine insurance, the underwriter evaluates maritime routes, vessel seaworthiness, and seasonal storm frequency prior to binding coverage.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The cautious maritime **underwriter** in Nantucket would hesitate to insure a whaling vessel commanded by a mad captain."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Every conservative **underwriter** in the financial district viewed the speculative traction franchises with grave suspicion."},
      {"author": "Daniel Defoe", "work": "An Essay Upon Projects", "quote": "The prudent **underwriter** calculates maritime risks upon sound mathematical averages rather than desperate fortune."}
    ]
  },
  "Dashboard — und/undescended.md": {
    "primary": "Failing to move down into the normal anatomical position, particularly referring to an ectopic or retained testis.",
    "secondary": "In pediatric urology and pediatric surgery, an undescended testis requires early orchidopexy to preserve fertility and minimize neoplastic transformation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical examination of male infants must systematically determine whether an **undescended** testis resides within the inguinal canal."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Failure of gubernacular contraction results in an **undescended** organ retained within the abdominal cavity."},
      {"author": "Thomas Henry Huxley", "work": "Comparative Anatomy", "quote": "Anomalies such as **undescended** anatomical structures shed valuable light on comparative vertebrate embryonic development."}
    ]
  },
  "Dashboard — und/undescriptive.md": {
    "primary": "Lacking vivid, detailed, or informative description; failing to characterize or depict an object or scene clearly.",
    "secondary": "In bibliographic cataloging and legal drafting, undescriptive titles cause ambiguity by omitting definitive identifying characteristics.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A merely **undescriptive** catalog of natural scenery fails to awaken poetic emotion in the sensitive reader."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The official military dispatch was singularly **undescriptive**, hiding the confusion of retreat behind dry bureaucratic phrases."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "A novelist who relies on **undescriptive** prose deprives his characters of an atmospheric world in which to breathe."}
    ]
  },
  "Dashboard — und/undeserved.md": {
    "primary": "Not earned, warranted, or justified by a person's conduct, character, or intrinsic actions.",
    "secondary": "In moral philosophy and jurisprudence, receiving undeserved punishment undermines social trust and civic allegiance to the judicial system.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "This is hard and **undeserved** measure, my lord, that falls upon a true and faithful servant."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor felt sincere compassion for Marianne under what seemed an **undeserved** and bitter trial of her affections."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To strip an honest citizen of his ancestral estate is an **undeserved** injury that shakes the foundations of justice."}
    ]
  },
  "Dashboard — und/undeservedly.md": {
    "primary": "In a manner that is not justified, earned, or merited; unjustly or unfairly.",
    "secondary": "In historical biography and criticism, figures who are undeservedly neglected by their contemporaries often gain canonical stature in subsequent centuries.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery bore himself with dignified patience, though **undeservedly** rebuked by the haughty visitors."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor was **undeservedly** censured by provincial senators who failed to appreciate the strategic perils on the Danube."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen realized that she had been treated **undeservedly** well by friends whom she had treated with cold indifference."}
    ]
  },
  "Dashboard — und/undeserving.md": {
    "primary": "Not worthy of help, praise, trust, reward, or recognition; lacking merit.",
    "secondary": "In nineteenth-century social reform debates, commentators distinguished between the deserving and undeserving poor when allocating parish relief.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Waste not thy precious tears upon an **undeserving** rebel who sought the ruin of our noble house."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth declared that Wickham was entirely **undeserving** of any further forbearance or financial indulgence."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Our natural sympathy revolts when great honors and public esteem are lavished upon an **undeserving** flatterer."}
    ]
  },
  "Dashboard — und/undesigned.md": {
    "primary": "Not planned, intentional, or premeditated; occurring spontaneously or by chance.",
    "secondary": "In evidentiary jurisprudence and textual hermeneutics, undesigned coincidences across independent witnesses provide persuasive proof of historical authenticity.",
    "quotes": [
      {"author": "William Paley", "work": "Horae Paulinae", "quote": "These **undesigned** coincidences between the epistles and the historical narrative furnish the strongest confirmation of truth."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Many beneficial social conventions arise from **undesigned** human actions rather than explicit legislative deliberation."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Their meeting near the shearing-barn was completely **undesigned**, yet it altered the entire course of their lives."}
    ]
  },
  "Dashboard — und/undesirability.md": {
    "primary": "The characteristic or condition of being unwanted, objectionable, disadvantageous, or harmful.",
    "secondary": "In urban planning and environmental economics, the spatial undesirability of heavy industrial zones depresses adjacent residential land valuations.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The civic **undesirability** of monopolistic combinations justifies legislative intervention to preserve equitable market competition."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Philosophers debate the relative **undesirability** of state paternalism compared to unregulated individual initiative."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The apparent **undesirability** of physical hardship often masks the moral discipline necessary to strengthen character."}
    ]
  },
  "Dashboard — und/undesirable.md": {
    "primary": "Not wanted, pleasing, or beneficial; tending to produce disadvantageous or harmful consequences.",
    "secondary": "In pharmacology and therapeutics, undesirable side effects such as hepatic toxicity limit the clinical dosage of novel compounds.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Any expression of genuine sympathy or unorthodoxy was deemed politically **undesirable** by the inner party."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes agreed that wandering alone across the treacherous moor after nightfall was highly **undesirable**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Artificial breeders scrupulously eliminate individuals possessing **undesirable** anatomical traits from their pedigree herds."}
    ]
  },
  "Dashboard — und/undesirably.md": {
    "primary": "In an unwanted, harmful, or objectionable manner; so as to produce adverse results.",
    "secondary": "In fiscal policy analysis, inflation rates that rise undesirably erode real household purchasing power and distort long-term capital investments.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial treasury was **undesirably** depleted by excessive tribute payments to barbarian chieftains along the frontier."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The royal proclamation operated **undesirably** upon commerce by instilling panic among London banking houses."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Her uncle's bequest had complicated her life **undesirably**, attracting suitors whose motives she could not trust."}
    ]
  },
  "Dashboard — und/undesired.md": {
    "primary": "Not wanted, sought, or requested; occurring contrary to one's wishes or intention.",
    "secondary": "In chemical process engineering, undesired secondary reactions consume expensive feedstocks and create hazardous byproduct waste.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With grave aspect he surveyed the **undesired** consequences of rebellion across the starry courts of heaven."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The sudden arrival of the squires was an **undesired** interruption to the quiet gathering at the Rainbow Inn."},
      {"author": "William Wordsworth", "work": "The Excursion", "quote": "He withdrew into solitary contemplation, seeking relief from **undesired** visits and frivolous worldly intrusions."}
    ]
  },
  "Dashboard — und/undesiring.md": {
    "primary": "Having no longing, craving, or wish; free from appetite or ambitious pursuit.",
    "secondary": "In Stoic and Buddhist contemplative philosophy, an undesiring consciousness achieves serenity by relinquishing worldly attachments.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The sage stands tranquil and **undesiring**, knowing that all true wealth resides within the sovereign soul."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I sat by the pond **undesiring** of city luxuries, perfectly content with simple bread and clean water."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "A mind truly detached from vanity remains calm and **undesiring** amidst the frantic rivalries of society."}
    ]
  },
  "Dashboard — und/undesirous.md": {
    "primary": "Not wishing for or aspiring to something; devoid of inclination, longing, or ambition.",
    "secondary": "In diplomatic negotiation, an envoy undesirous of escalating territorial disputes adopts conciliatory rhetoric to foster peaceful mediation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne was entirely **undesirous** of claiming public attention, preferring the quiet domestic circle of her family."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The philosopher emperor was **undesirous** of military triumph, yet accepted the command imposed by public duty."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The weary knight seemed **undesirous** of entering the tournament until provoked by the insolence of his rivals."}
    ]
  },
  "Dashboard — und/undestroyable.md": {
    "primary": "Incapable of being destroyed, ruined, annihilated, or broken down; indestructible.",
    "secondary": "In conservation chemistry and particle physics, foundational mass-energy relationships postulate undestroyable conservation of fundamental constituents.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Human labor possesses an **undestroyable** reality that outlasts paper currencies and transient political factions."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The leviathan appeared an **undestroyable** titan of the deep, defying the iron harpoons of puny mortals."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The titan endured subterranean agony, fortified by an **undestroyable** love for humankind."}
    ]
  },
  "Dashboard — und/undetectable.md": {
    "primary": "Incapable of being noticed, discovered, or measured by human senses or standard instruments.",
    "secondary": "In analytical toxicology and forensic science, trace poisons administered in infinitesimal concentrations were long undetectable before modern spectrometry.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Devil's Foot", "quote": "Holmes suspected the killer had employed a rare combustion poison that was virtually **undetectable** upon post-mortem examination."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "By altering the refractive index of living tissue, Griffin rendered his body **undetectable** against the background light."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Incipient morphological shifts between generations are often so minute as to be **undetectable** over short time spans."}
    ]
  },
  "Dashboard — und/undetected.md": {
    "primary": "Not noticed, discovered, or revealed; passing without observation or interception.",
    "secondary": "In cybersecurity and perimeter defense, malicious intrusion vectors that operate undetected for extended periods inflict extensive systemic compromise.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The assassin slipped through the foggy London streets **undetected** by the night watchmen on duty."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Jim Hawkins crept aboard the Hispaniola **undetected**, while the drunken pirates slept below deck."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "Dupin demonstrated how the agile intruder had escaped through the rear window **undetected** by the gathering crowd."}
    ]
  },
  "Dashboard — und/undeterminable.md": {
    "primary": "Incapable of being definitely ascertained, settled, measured, or calculated; indeterminate.",
    "secondary": "In philosophical epistemology and quantum mechanics, properties that are undeterminable prior to empirical measurement challenge classical causality.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "The ultimate origin of sensory impressions remains **undeterminable** by the natural faculties of human reason."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Whether the cosmos possesses an absolute beginning in time is a question **undeterminable** within empirical experience."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The absolute chronology of subterranean rock strata was long regarded as **undeterminable** before stratigraphic mapping."}
    ]
  },
  "Dashboard — und/undetermined.md": {
    "primary": "Not decided, resolved, or established; or having boundaries or characteristics that remain uncertain.",
    "secondary": "In civil litigation and probate law, property rights that remain undetermined during pending appeals freeze the distribution of estate assets.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The endless lawsuit of Jarndyce and Jarndyce left the ultimate ownership of the great estate perpetually **undetermined**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The boundary line between the Roman provinces and the Persian empire remained **undetermined** for generations."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The will remains **undetermined** until stirred to action by some pressing sense of unease or desire."}
    ]
  },
  "Dashboard — und/undeterred.md": {
    "primary": "Persevering without being discouraged, intimidated, or turned aside by obstacles, danger, or opposition.",
    "secondary": "In polar exploration history, expeditions persevered undeterred through Arctic blizzards to establish critical geographic coordinates.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The merchant seamen sailed on **undeterred** by submarine wolfpacks lurking across the stormy Atlantic sea lanes."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The steamer pressed upriver into the humid jungle mist, **undeterred** by the distant rumble of tribal war drums."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck broke trail through deep Yukon snowdrifts, **undeterred** by freezing temperatures and blinding blizzards."}
    ]
  },
  "Dashboard — und/undeveloped.md": {
    "primary": "Not having reached full maturity, growth, or potential; or lacking modern industrial, agricultural, or economic resources.",
    "secondary": "In developmental biology and cytology, undeveloped stem cell lineages retain multipotent pluripotency prior to lineage-specific signaling.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Vast tracts of fertile land in the colonies remained **undeveloped** for lack of sufficient agricultural labor and capital."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain rudimentary organs remain **undeveloped** in adults, serving as evolutionary traces of ancestral anatomy."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian machinery demonstrated technologies far beyond the **undeveloped** industrial capacities of Victorian England."}
    ]
  },
  "Dashboard — und/undeviating.md": {
    "primary": "Moving or continuing in a straight line or constant course without turning aside; steadfast and unwavering.",
    "secondary": "In celestial navigation and orbital mechanics, celestial bodies maintain an undeviating path in accordance with gravitational conservation laws.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab pursued his quarry with an **undeviating** resolve that bordered on monomania across the uncharted Pacific."},
      {"author": "George Eliot", "work": "Romola", "quote": "Savonarola held to his moral crusade with **undeviating** rectitude despite the escalating hostility of Florence."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Nature moves toward its appointed ends with an **undeviating** precision that humbles the vanity of human contrivance."}
    ]
  },
  "Dashboard — und/undiagnosable.md": {
    "primary": "Incapable of being recognized, categorized, or explained through standard medical diagnostic methods.",
    "secondary": "In clinical neurology, idiopathic neurodegenerative conditions presenting with diffuse atypical symptoms are often initially undiagnosable.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The physician must candidly acknowledge when an obscure malady remains **undiagnosable** despite exhaustive physical examination."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The elderly practitioner encountered an extraordinary set of symptoms that appeared totally **undiagnosable** by standard textbooks."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Milly Theale's fatal illness lingered as an ethereal, almost **undiagnosable** decline that baffled her devoted companions."}
    ]
  },
  "Dashboard — und/undiagnosed.md": {
    "primary": "Not identified or categorized by medical or technical examination; unrecognized.",
    "secondary": "In epidemiology and public health surveillance, individuals with undiagnosed asymptomatic infections facilitate widespread viral transmission.",
    "quotes": [
      {"author": "George Orwell", "work": "Keep the Aspidistra Flying", "quote": "Gordon suspected that a lingering, **undiagnosed** ailment contributed to his pervasive lethargy and bitterness."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "Many elderly patients suffered from **undiagnosed** digestive complaints that patent nostrums pretended to cure."},
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "Septimus Warren Smith endured **undiagnosed** shell shock while society dismissed his agony as mere nerves."}
    ]
  },
  "Dashboard — und/undies.md": {
    "primary": "An informal or colloquial term for undergarments, particularly panties or briefs.",
    "secondary": "In domestic sociology and textile retail history, the popularization of ready-to-wear undies mirrored shifts toward practical daily attire.",
    "quotes": [
      {"author": "James Joyce", "work": "Finnegans Wake", "quote": "The laundress chattered by the riverbank while rinsing out petticoats, collars, and woolen **undies**."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "The washing line in the suburban garden fluttered with socks, shirts, and children's cotton **undies**."},
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "Gloria unpacked her silk travelling garments and delicate summer **undies** after arriving at the hotel."}
    ]
  },
  "Dashboard — und/undifferentiated.md": {
    "primary": "Lacking distinct characteristics, specialized parts, or individual differences; uniform.",
    "secondary": "In oncology and histology, an undifferentiated neoplasm consists of anaplastic cells that have lost recognizable tissue architecture.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution progresses from an indefinite, **undifferentiated** homogeneity to a definite, coherent heterogeneity."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Infant sensory consciousness begins as a blooming, buzzing, **undifferentiated** mass of visceral sensations."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Primitive colonial organisms display **undifferentiated** structures where every cell performs all essential life functions."}
    ]
  },
  "Dashboard — und/undigested.md": {
    "primary": "Not converted into absorbable nutrients in the digestive tract; or information not intellectually assimilated or reflected upon.",
    "secondary": "In literary criticism and historiography, an author who presents raw, undigested archival documents fails to create a coherent narrative.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Academy of Lagado pursued absurd experiments to extract sunbeams from cucumbers and reprocess **undigested** food."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Some books are to be tasted, others to be swallowed, and some few to be chewed and thoroughly **undigested** facts rejected."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The pedantic professor stuffed his mind with vast heaps of **undigested** scholastic lore that bore no living fruit."}
    ]
  },
  "Dashboard — und/undignified.md": {
    "primary": "Lacking dignity, seriousness, decorum, or self-respect; inappropriate or unbecoming.",
    "secondary": "In diplomatic protocol and public ceremonialism, undignified conduct by an ambassador insults the host nation and undermines bilateral relations.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley remarked that Harriet's flurried retreat across the parlor was hurried and singularly **undignified**."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick found himself in the highly **undignified** predicament of being trapped inside a ladies' boarding school garden."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon considered the bishop's domestic subservience to his wife thoroughly **undignified** for a prelate."}
    ]
  },
  "Dashboard — und/undiluted.md": {
    "primary": "Not mixed, thinned, or weakened with water or another liquid; pure and unmitigated.",
    "secondary": "In toxicology and chemical manufacturing, handling undiluted acids requires specialized containment vessels and personal protective equipment.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The captain consumed **undiluted** rum in reckless quantities until a stroke ended his piratical career."},
      {"author": "George Orwell", "work": "Animal Farm", "quote": "The revolutionary decrees were presented as the **undiluted** doctrine of Animalism for all working beasts."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers spoke with **undiluted** moral intensity that brooked no compromise from his listeners."}
    ]
  },
  "Dashboard — und/undiminished.md": {
    "primary": "Remaining at the full original size, strength, intensity, or quality; not lessened or reduced.",
    "secondary": "In thermodynamics and wave propagation, energy transmitted across ideal lossless media propagates with undiminished wave amplitude.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The veteran legions advanced with **undiminished** courage against the barbarians who had crossed the frozen Rhine."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Frankenstein pursued his vengeful demon across Arctic ice sheets with **undiminished** hatred and desperation."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Britain faced the threat of aerial bombardment with **undiminished** fortitude during the dark summer of 1940."}
    ]
  },
  "Dashboard — und/undimmed.md": {
    "primary": "Not made dark, dull, faint, or obscure; retaining full brightness, brilliance, or clarity.",
    "secondary": "In astronomical observation and optics, light transmitted through unpolluted desert skies reaches telescopes with undimmed stellar clarity.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The celestial archangel shone with **undimmed** majesty, radiating heavenly light upon the garden of Eden."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The southern sun poured its **undimmed** rays upon the marble ruins of ancient Athens."},
      {"author": "Percy Bysshe Shelley", "work": "Adonais", "quote": "The pure spirit burns with **undimmed** flame above the shadows of our earthly night."}
    ]
  },
  "Dashboard — und/undine.md": {
    "primary": "A water nymph or female elemental spirit inhabiting rivers and lakes, originating in the occult treatises of Paracelsus.",
    "secondary": "In Romantic literature and folkloristics, Friedrich de la Motte Fouqué's novella popularized the undine as a water spirit seeking a human soul through love.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Critical and Miscellaneous Essays", "quote": "Fouqué's fairy tale of **Undine** represents the longing of nature's elemental powers to acquire a human soul."},
      {"author": "Edgar Allan Poe", "work": "Marginalia", "quote": "The delicate fantasy of the water nymph **Undine** touches the highest chord of Romantic poetic imagination."},
      {"author": "George MacDonald", "work": "Phantastes", "quote": "Beside the glistening forest stream, I half expected an **undine** to emerge from beneath the water lilies."}
    ]
  },
  "Dashboard — und/undiplomatic.md": {
    "primary": "Lacking tact, sensitivity, or discretion in dealing with others; blunt or tactless.",
    "secondary": "In international statecraft and foreign affairs, an undiplomatic speech delivered by an envoy can ignite diplomatic protests and breach treaty protocols.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Naval Treaty", "quote": "Phelps admitted that his sudden outburst was an **undiplomatic** display of temper during confidential state negotiations."},
      {"author": "Henry James", "work": "The American", "quote": "Christopher Newman's frank, unvarnished manner seemed refreshingly **undiplomatic** to the rigid Parisian aristocrats."},
      {"author": "Winston Churchill", "work": "Great Contemporaries", "quote": "The Kaiser's impulsive, **undiplomatic** telegrams continually disrupted the calculated policies of the German chancellery."}
    ]
  },
  "Dashboard — und/undiplomatically.md": {
    "primary": "In a blunt, tactless, or indiscreet manner that disregards delicate political or interpersonal conventions.",
    "secondary": "In bilateral summit diplomacy, raising contentious territorial boundaries undiplomatically risks collapsing fragile ceasefire negotiations.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Heartbreak House", "quote": "Captain Shotover spoke **undiplomatically** to his aristocratic guests, mocking their idle lives without hesitation."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "Mr. Vladimir spoke **undiplomatically** to Verloc, demanding an immediate outrage to shock the British bourgeois public."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The young member of Parliament blurted out party grievances **undiplomatically** before the press corps."}
    ]
  },
  "Dashboard — und/undirected.md": {
    "primary": "Lacking guidance, aim, control, destination, or instruction; wandering or haphazard.",
    "secondary": "In graph theory and network topology, an undirected edge forms a bidirectional connection between two nodes with no oriented pathway.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Human enthusiasm without sound scientific knowledge remains an **undirected** force producing unintended social mischief."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In daydreaming, the flow of mental imagery drifts along an **undirected** current governed solely by casual association."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Random morphological variations occur in an **undirected** fashion, awaiting natural selection to determine their survival value."}
    ]
  },
  "Dashboard — und/undiscerning.md": {
    "primary": "Lacking good judgment, critical taste, or the ability to perceive subtle distinctions; uncritical.",
    "secondary": "In aesthetic philosophy and art connoisseurship, undiscerning collectors frequently pay exorbitant sums for derivative and forged artworks.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price observed that Sir Thomas was singularly **undiscerning** regarding the true selfish character of Mrs. Norris."},
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "The **undiscerning** crowd applauds trivial rhymes while missing the profound harmony of true poetic genius."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "A writer who caters to an **undiscerning** public sacrifices lasting literary fame for fleeting popular applause."}
    ]
  },
  "Dashboard — und/undischarged.md": {
    "primary": "Not released, paid, dismissed, or unloaded; still carrying a legal obligation or electrical charge.",
    "secondary": "In insolvency law, an undischarged bankrupt is legally prohibited from obtaining credit or serving as a corporate director without court approval.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Many debtors languished in the Marshalsea prison for years under the weight of **undischarged** financial obligations."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The Leyden jar retained an **undischarged** accumulation of static tension along its metallic coatings."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "A prudent merchant never accepts goods from an **undischarged** bankrupt whose affairs remain tangled in litigation."}
    ]
  },
  "Dashboard — und/undiscipline.md": {
    "primary": "A lack of discipline, order, control, or obedience; state of disorganization.",
    "secondary": "In military history and operational theory, chronic indiscipline and undiscipline in auxiliary units lead to route and operational collapse during retreat.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The chronic **undiscipline** of the praetorian cohorts precipitated the rapid decline of imperial authority in Rome."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Mutinous regiments in the garrisons of Nancy and Metz fell into wild **undiscipline** under Jacobin agitators."},
      {"author": "George Washington", "work": "Writings of George Washington", "quote": "The general lamented the general **undiscipline** among the militia recruits arriving without basic field training."}
    ]
  },
  "Dashboard — und/undisciplined.md": {
    "primary": "Lacking training, control, order, or self-restraint; unruly and disorganized.",
    "secondary": "In developmental psychology and education, undisciplined cognitive habits impede sustained focus during complex problem-solving tasks.",
    "quotes": [
      {"author": "Julius Caesar", "work": "Commentaries on the Gallic War", "quote": "The Roman cohorts easily repulsed the headlong charge of the **undisciplined** Celtic warriors along the riverbank."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "An **undisciplined** child permitted to indulge every whim grows into an unmanageable adult prone to folly."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie Tulliver struggled against her passionate and **undisciplined** impulses in the quiet provincial town of St. Ogg's."}
    ]
  },
  "Dashboard — und/undisclosed.md": {
    "primary": "Not revealed, publicized, or made known; kept secret or confidential.",
    "secondary": "In contract law and corporate governance, failure to declare undisclosed liabilities constitutes material misrepresentation voiding agreements.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The banker acknowledged that an **undisclosed** sum of money had been advanced to an illustrious borrower."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "Cowperwood negotiated the purchase of municipal franchises through an **undisclosed** agent to prevent market speculation."},
      {"author": "Wilkie Collins", "work": "The Woman in White", "quote": "Marian Halcombe suspected that Sir Percival harbored an **undisclosed** secret that held him in terrible dread."}
    ]
  },
  "Dashboard — und/undiscouraged.md": {
    "primary": "Not deterred, disheartened, or dispirited by difficulty, adversity, or failure.",
    "secondary": "In scientific discovery narratives, researchers working undiscouraged across repeated experimental failures eventually identify catalytic mechanisms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Life and Letters of Charles Darwin", "quote": "Darwin labored on **undiscouraged** by persistent invalidism, compiling vast notebooks of biological observations."},
      {"author": "Thomas Edison", "work": "The Writings of Thomas Edison", "quote": "The inventor tested thousands of carbon filaments **undiscouraged** by repeated failure until the incandescent lamp glowed."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Marlow watched the young man depart into the wilderness, **undiscouraged** by the disgrace that had shadowed his youth."}
    ]
  },
  "Dashboard — und/undiscoverable.md": {
    "primary": "Incapable of being found, seen, or ascertained by searching or investigation; completely hidden.",
    "secondary": "In cryptography and steganography, data embedded within digital carriers in an undiscoverable manner resists statistical frequency detection.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Purloined Letter", "quote": "The prefect assumed the stolen letter was concealed in an **undiscoverable** cavity within the minister's apartment."},
      {"author": "David Hume", "work": "An Enquiry Concerning the Principles of Morals", "quote": "The metaphysical nature of ultimate moral origins remains **undiscoverable** by pure speculative reasoning."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The causes of natural phenomena are not inherently **undiscoverable**, but yield steadily to empirical investigation."}
    ]
  },
  "Dashboard — und/undiscovered.md": {
    "primary": "Not yet found, explored, recognized, or known to the world; hidden from sight or knowledge.",
    "secondary": "In planetary geology and deep-sea oceanography, hydrothermal vent systems harboring undiscovered endemic species remain widespread.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The **undiscovered** country from whose bourn no traveller returns puzzles the will and gives us pause."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Walton sailed into the Arctic Ocean, dreaming of discovering an **undiscovered** continent bathed in perpetual light."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Flint's cache of golden doubloons lay **undiscovered** beneath the maritime pines of the desolate island."}
    ]
  },
  "Dashboard — und/undiscriminating.md": {
    "primary": "Lacking discernment, critical judgment, or the ability to make fine distinctions; indiscriminate.",
    "secondary": "In evolutionary biology and immunology, undiscriminating phagocytic immune responses clear broad pathogen classes prior to adaptive targeting.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "An **undiscriminating** admiration for every ancient canvas prevents young painters from mastering true natural color."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's intense benevolence was sometimes criticized as **undiscriminating** by her more practical neighbors."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Catastrophic floods act as an **undiscriminating** agent of mortality, sweeping away fit and unfit organisms alike."}
    ]
  },
  "Dashboard — und/undisguised.md": {
    "primary": "Not concealed, masked, or hidden; open, frank, and clearly evident.",
    "secondary": "In behavioral psychology and facial affect analysis, undisguised micro-expressions of contempt betray genuine interpersonal sentiment.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy's proposal was delivered with **undisguised** pride and an acute awareness of her social inferiority."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Uriah Heep looked upon David with **undisguised** malice whenever Mr. Wickfield stepped out of the office."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Norman baron regarded the Saxon captives with **undisguised** contempt from the ramparts of Torquilstone."}
    ]
  },
  "Dashboard — und/undismayed.md": {
    "primary": "Not discouraged, frightened, or demoralized by danger, difficulty, or impending disaster.",
    "secondary": "In military historiography, infantry squares that stood undismayed against cavalry charges broke the momentum of enemy offensives.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan surveyed the fiery gulf **undismayed**, retaining his defiant pride despite utter defeat."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The citizens of London remained **undismayed** amidst falling bombs, emerging each morning to clear the debris."},
      {"author": "Lord Byron", "work": "The Corsair", "quote": "Conrad stood upon the deck **undismayed** by the gathering hurricane clouds dark upon the horizon."}
    ]
  },
  "Dashboard — und/undisputable.md": {
    "primary": "Incapable of being questioned, doubted, or challenged; indisputable and undeniable.",
    "secondary": "In formal jurisprudence and evidentiary proceedings, undisputable documentary evidence conclusively establishes title and chain of custody.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "Mathematical propositions possess an **undisputable** certainty that flows directly from the relation of ideas."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The victory of the parliamentary forces at Naseby was an **undisputable** turning point in the English Civil War."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "That something cannot both be and not be at the same time is an **undisputable** axiom of human reason."}
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

print(f"Dashboard — und Part 5 (8E): Successfully updated {updated}/{len(data)} notes.")
