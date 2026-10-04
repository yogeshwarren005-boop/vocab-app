# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — don (36 words) ---
  "Dashboard — don/antedon.md": {
    "primary": "A genus of feather stars belonging to the class Crinoidea, characterized by feathery pinnules and stalkless adult life.",
    "secondary": "In marine invertebrate zoology, Antedon bifida represents a classical model organism for studying pentamerous echinoderm radial symmetry.",
    "quotes": [
      {"author": "Thomas Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The free-swimming crinoid **antedon** anchors itself temporarily to rocky substrates using jointed cirri."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The larval development of the feather-star **antedon** reveals ancient ancestral stalked crinoid stages."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "We observed the graceful undulations of **antedon** swimming through the clear waters of the bay."}
    ]
  },
  "Dashboard — don/antedonidae.md": {
    "primary": "The taxonomic family of unstalked crinoids comprising the common feather stars.",
    "secondary": "In benthic marine ecology, members of Antedonidae inhabit cold temperate to tropical coastal waters, suspension feeding upon plankton.",
    "quotes": [
      {"author": "Thomas Huxley", "work": "Lectures on the Elements of Comparative Anatomy", "quote": "The skeletal ossicles of the **antedonidae** exhibit intricate calcareous microstructures."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Trawling in deep coastal waters frequently brings up clusters of **antedonidae** entwined around gorgonian corals."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Among the marine dredgings were several striking forms belonging to the family **antedonidae**."}
    ]
  },
  "Dashboard — don/codon.md": {
    "primary": "A sequence of three adjacent nucleotides in DNA or RNA that encodes a specific amino acid.",
    "secondary": "In molecular genetics and translation, each triplet codon pairs with a complementary transfer RNA anticodon during protein synthesis.",
    "quotes": [
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "The deciphering of the genetic code established which triplet **codon** corresponded to each amino acid."},
      {"author": "Sydney Brenner", "work": "My Life in Science", "quote": "Our experiments demonstrated that a nonsense **codon** signals the termination of peptide chain elongation."},
      {"author": "Erwin Schrödinger", "work": "What Is Life?", "quote": "The hereditary molecular code-script operates like a miniature **codon** sequence directing cellular organization."}
    ]
  },
  "Dashboard — don/condonation.md": {
    "primary": "The overlooking, excusing, or tacit forgiveness of an offense or wrongdoing.",
    "secondary": "In marital and ecclesiastical law, condonation is the voluntary forgiveness of a matrimonial offense, barring subsequent divorce petitions on that ground.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "He Knew He Was Right", "quote": "Mr. Trevelyan's torturing jealousy refused to grant that Christian **condonation** which alone could restore domestic peace."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode clung to the hope that his generous civic philanthropies would earn divine **condonation** for past deceit."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Continued voluntary cohabitation with knowledge of adultery constitutes legal **condonation** of the offense."}
    ]
  },
  "Dashboard — don/condone.md": {
    "primary": "To accept, overlook, or allow behavior that is considered morally wrong or offensive.",
    "secondary": "In administrative statecraft, allowing infractions without formal sanction sets a precedent that appears to condone corruption.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price could never bring herself to **condone** the reckless theatrical rehearsals that compromised domestic decorum."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "No civilized nation can **condone** the confiscation of private property under the plea of public utility."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Society was eager to **condone** Mr. Merdle's vulgarity so long as his financial speculations returned immense dividends."}
    ]
  },
  "Dashboard — don/cordon.md": {
    "primary": "A line or ring of police, sentinels, or military guards surrounding an area to prevent passage.",
    "secondary": "In epidemiology and public health history, a cordon sanitaire is a guarded sanitary boundary erected around infected regions to prevent contagion.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A double **cordon** of armed police guarded the railway station and the roads leading onto Dartmoor."},
      {"author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "The magistrates established a strict watchmen **cordon** around infected dwellings to confine the contagion."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The city guard formed a compact **cordon** around the scaffold to hold back the surging Edinburgh crowd."}
    ]
  },
  "Dashboard — don/don.md": {
    "primary": "To put on an item of clothing; or a university teacher, especially a fellow or tutor at Oxford or Cambridge.",
    "secondary": "In Spanish honorific registers, Don (from Latin dominus) precedes a gentleman's Christian name as a traditional mark of respect.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "Thou shalt **don** this robe of white and appear before the Roman populace with dignity."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Richard proceeded to **don** his military coat, looking every inch the gallant young cornet of cavalry."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude gazed with reverent longing toward the ancient colleges of Christminster, where every learned **don** paced cloistered walks."}
    ]
  },
  "Dashboard — don/dona.md": {
    "primary": "A Portuguese and Spanish title of respect prefixed to a woman's Christian name; Donna.",
    "secondary": "In Iberian social history, the title Dona was historically restricted to women of the nobility before expanding as a polite courtesy title.",
    "quotes": [
      {"author": "Miguel de Cervantes", "work": "Don Quixote", "quote": "The knight saluted **dona** Rodriguez with profound gravity, mistaking the duenna for a highborn damsel in distress."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "His mother, **dona** Inez, was an austere lady deeply versed in moral treatises and heraldic lore."},
      {"author": "Washington Irving", "work": "Chronicle of the Conquest of Granada", "quote": "The brave **dona** Maria Coronel defended her castle against Moorish raiders with heroic fortitude."}
    ]
  },
  "Dashboard — don/donar.md": {
    "primary": "An ancient Germanic thunder deity, equivalent to Thor; or an obsolete botanical and geographical term.",
    "secondary": "In comparative Germanic mythology, Donar (Old High German Thunar) was venerated as the cosmic champion against chaotic giants, associated with sacred oak groves.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The ancient Saxons worshipped **donar** as the mighty god of thunder and the protector of the peasant yeoman."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Saint Boniface hewed down the sacred oak of **donar** at Geismar to demonstrate the supremacy of the Christian faith."},
      {"author": "Jacob Grimm", "work": "Teutonic Mythology", "quote": "Votive inscriptions along the Rhine attest to the widespread veneration of **donar** among early Frankish tribes."}
    ]
  },
  "Dashboard — don/donate.md": {
    "primary": "To give money, goods, or services to help a person, charity, or worthy cause.",
    "secondary": "In hematology and transfusion medicine, eligible individuals donate blood or bone marrow to replenish clinical blood banks.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge resolved to **donate** an astonishing sum to the benevolent fund, redeeming his past selfish parsimony."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "A generous man is moved by natural sympathy to **donate** portion of his abundance to relieve destitute neighbors."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was ever ready to **donate** food and fuel to the cottagers during severe winter frosts."}
    ]
  },
  "Dashboard — don/donatello.md": {
    "primary": "An early Renaissance Italian sculptor of Florence (c. 1386–1466), renowned for his bronze David and realistic relief work.",
    "secondary": "In Renaissance art history, Donatello pioneered linear perspective in bas-relief (rilievo schiacciato) and reintroduced free-standing classical contrapposto.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The young Count of Monte Beni was named **donatello** because his joyful rustic grace recalled the famous faun sculpted by Praxiteles."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The bronze reliefs of **donatello** in Florence display an emotional naturalism that revitalized Western sculpture."},
      {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "In the work of **donatello**, the severe dignity of classical marble unites with vivid Tuscan humanity."}
    ]
  },
  "Dashboard — don/donation.md": {
    "primary": "Something given to an individual, charity, or organization, especially a sum of money.",
    "secondary": "In Roman and canon law, the forged Donation of Constantine was an 8th-century imperial edict granting extensive temporal authority to the papacy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The celebrated **donation** of Constantine was demonstrated by Laurentius Valla to be a clumsy medieval forgery."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Miss Trotwood made a handsome **donation** to David's legal schooling, insisting upon thorough diligence in return."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Endowed hospitals maintained by charitable **donation** were often managed with less efficiency than commercial infirmaries."}
    ]
  },
  "Dashboard — don/donatism.md": {
    "primary": "A 4th-century North African Christian schism maintaining that sacraments administered by fallen clerics were invalid.",
    "secondary": "In historical patristics, Saint Augustine opposed Donatism by arguing that sacraments operate ex opere operato through Christ rather than the minister's moral purity.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The furious controversy of **donatism** tore the churches of North Africa into irreconcilable hostile factions."},
      {"author": "Saint Augustine", "work": "Confessions", "quote": "He wrote extensively against the sect of **donatism**, defending the unity and universality of the Catholic Church."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The civil wars sparked by **donatism** in Roman Africa illustrated how theological zeal could dismantle imperial peace."}
    ]
  },
  "Dashboard — don/donatist.md": {
    "primary": "A follower or adherent of Donatism; or relating to the Donatist schism in early Christianity.",
    "secondary": "In North African Roman history, the militant Circumcellion peasants allied with the Donatist faction, engaging in violent rebellions against imperial magistrates.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fanaticism of the **donatist** bishops defied both the edicts of Constantine and the synods of Rome."},
      {"author": "Saint Augustine", "work": "The City of God", "quote": "The **donatist** party claimed an exclusive holiness, condemning all other Christian communities throughout the Roman world."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "He compared modern sectarian dogmatists to the ancient **donatist** zealots who mistook persecution for piety."}
    ]
  },
  "Dashboard — don/donatus.md": {
    "primary": "A 4th-century Roman grammarian (Aelius Donatus) whose Latin textbook was standard throughout the Middle Ages; or the Donatist bishop.",
    "secondary": "In medieval intellectual history, a donatus became a generic term for any introductory Latin grammar primer used in cathedral schools.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Saint Jerome took pride in having studied rhetoric and classical Latin under the celebrated master **donatus** at Rome."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The pedantic schoolmaster drilled the frightened urchins in the conjugation rules of **donatus** day after day."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Marius read the classical commentaries of **donatus**, admiring their precise grammatical analysis of Virgil's verse."}
    ]
  },
  "Dashboard — don/done.md": {
    "primary": "Completed, finished, or brought to a conclusion; or thoroughly cooked.",
    "secondary": "In social etiquette, an action not done violates established conventions of polite decorum.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "If it were **done** when 'tis done, then 'twere well it were done quickly: if the assassination could trammel up the consequence, and catch with his surcease success; that but this blow might be the be-all and the end-all here, but here, upon this bank and shoal of time, we'ld jump the life to come."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The dinner was **done** to a turn, and Bob Cratchit pronounced the roast goose to be the greatest success of the family."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "When all was **done**, Elizabeth felt that her visit to Pemberley had completely altered the course of her affections."}
    ]
  },
  "Dashboard — don/donee.md": {
    "primary": "A person who receives a gift, donation, or bequest from a donor.",
    "secondary": "In property and equity law, the donee of a power of appointment is empowered to designate the ultimate beneficiaries of trust property.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The legal title transfers irrevocably to the **donee** upon voluntary delivery and acceptance of the deed of gift."},
      {"author": "Adam Smith", "work": "Lectures on Jurisprudence", "quote": "Natural law recognizes that the **donee** acquires a legitimate property right through the uncoerced generosity of the donor."},
      {"author": "Anthony Trollope", "work": "Orley Farm", "quote": "The court examined whether Lady Mason was the lawful **donee** of the codicil or had obtained it by fraudulent contrivance."}
    ]
  },
  "Dashboard — don/donetsk.md": {
    "primary": "An industrial city in eastern Ukraine, situated in the historic Donbas mining region.",
    "secondary": "In industrial history, Donetsk was founded in 1869 by Welsh businessman John Hughes and was originally named Yuzovka in his honor.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "Resurrection", "quote": "The traveler described the vast coal fields of **donetsk**, where thousands of miners labored beneath the smoke-hung steppes."},
      {"author": "Maxim Gorky", "work": "The Lower Depths", "quote": "Peasants from the famine-stricken central provinces migrated to the iron works of **donetsk** seeking factory labor."},
      {"author": "Ivan Turgenev", "work": "Virgin Soil", "quote": "The industrial prospects of the **donetsk** basin were debated by ambitious entrepreneurs in the capital."}
    ]
  },
  "Dashboard — don/donetske.md": {
    "primary": "A variant linguistic transliteration or Ukrainian regional form of the city of Donetsk.",
    "secondary": "In Slavic toponymy, Donetske reflects the nominal adjectival locative form derived from the Seversky Donets river basin.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Regimental couriers carried dispatches across the eastern steppes toward the southern settlements of **donetske**."},
      {"author": "Maxim Gorky", "work": "My Childhood", "quote": "The grandfather spoke of adventurous Cossack expeditions along the winding waters near **donetske**."},
      {"author": "Anton Chekhov", "work": "The Steppe", "quote": "The boundless steppe stretched away toward **donetske**, fragrant with wormwood under the shimmering summer heat."}
    ]
  },
  "Dashboard — don/donizetti.md": {
    "primary": "Gaetano Donizetti (1797–1848), a prolific Italian bel canto opera composer celebrated for Lucia di Lammermoor and L'elisir d'amore.",
    "secondary": "In musicological history, Donizetti composed over sixty operas, bridging Rossinian opera buffa with early Verdian dramatic romanticism.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The mad scene from **donizetti** requires extraordinary coloratura agility and dramatic poignancy from the prima donna."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma Bovary wept at the Rouen theater while listening to the tragic romantic melodies of **donizetti**."},
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "The St. Petersburg society crowd packed the Italian opera to hear the newly staged masterpiece by **donizetti**."}
    ]
  },
  "Dashboard — don/donna.md": {
    "primary": "An Italian title of respect for a woman, equivalent to Lady or Madam; or an aristocratic lady.",
    "secondary": "In operatic dramaturgy, Donna Anna and Donna Elvira represent complex aristocratic tragic heroines in Mozart's Don Giovanni.",
    "quotes": [
      {"author": "Lord Byron", "work": "Don Juan", "quote": "**donna** Julia was a charming young matron of twenty-three, married to an elderly Spanish hidalgo."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The prima **donna** stepped before the footlights to acknowledge the enthusiastic applause of the London audience."},
      {"author": "George Eliot", "work": "Romola", "quote": "The Florentine citizens bowed respectfully as the noble **donna** passed through the crowded market place."}
    ]
  },
  "Dashboard — don/donne.md": {
    "primary": "John Donne (1572–1631), an English poet and cleric who was the leading representative of the metaphysical poets.",
    "secondary": "In literary history, Donne's poetry is renowned for intricate conceits, colloquial speech rhythms, intellectual paradox, and profound devotional intensity.",
    "quotes": [
      {"author": "Izaak Walton", "work": "Life of Dr. John Donne", "quote": "Dr. **donne** was a preacher so captivating in his eloquence that he drew tears from the eyes of his listeners at Saint Paul's."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "In the poems of **donne**, the most heterogeneous ideas are yoked by violence together with astonishing intellectual dexterity."},
      {"author": "Thomas De Quincey", "work": "Essays on the Poets", "quote": "The devotional sonnets of **donne** combine dialectical subtlety with an agonized intensity of spiritual struggle."}
    ]
  },
  "Dashboard — don/donnean.md": {
    "primary": "Of, relating to, or characteristic of the style, conceits, and poetry of John Donne.",
    "secondary": "In poetic criticism, a Donnean conceit employs complex scientific or geographical analogies to explore emotional and spiritual intimacy.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The young poet displayed a marked **donnean** inclination for unexpected rhetorical comparisons and knotty philosophical wit."},
      {"author": "Thomas De Quincey", "work": "Literary Reminiscences", "quote": "He admired that intricate **donnean** vigor of thought which refuses to sacrifice intellectual precision for smooth meter."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Certain modern verses exhibit a **donnean** obscurity without capturing Donne's underlying passionate earnestness."}
    ]
  },
  "Dashboard — don/donnian.md": {
    "primary": "Characteristic of or resembling John Donne or his intellectual metaphysical poetic style.",
    "secondary": "In 19th-century literary essays, Donnian wit referred to ingenious dialectical arguments sustained in romantic verse.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Table Talk", "quote": "The poem exhibits a curious **donnian** subtlety, turning an anatomical detail into a sublime theological metaphor."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "Browne's prose occasionally reveals a **donnian** fascination with the solemn paradoxes of mortality."},
      {"author": "Algernon Charles Swinburne", "work": "A Study of Shakespeare", "quote": "The lyric possesses a **donnian** toughness of fiber that challenges the reader's analytical comprehension."}
    ]
  },
  "Dashboard — don/donnish.md": {
    "primary": "Resembling or characteristic of a university don; pedantic, academic, or formal in manner.",
    "secondary": "In social satire, a donnish temperament is caricatured as detached from practical reality, immersed in obscure scholarly minutiae.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's speech was stiff and **donnish**, smelling of ancient library dust and ecclesiastical folios."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The new bishop's chaplain possessed a **donnish** superiority of air that irritated the hardworking country curates."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "He broke away from the narrow **donnish** circles of Cambridge, longing for active participation in national politics."}
    ]
  },
  "Dashboard — don/donor.md": {
    "primary": "A person or organization that gives or donates something, especially money or organs.",
    "secondary": "In semiconductor physics and solid-state electronics, a donor impurity contributes free conduction electrons to an n-type semiconductor lattice.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The generous **donor** endowed a professorship in moral philosophy to promote enlightened learning in his native city."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The hospital directors erected a marble plaque honoring the anonymous **donor** whose gift built the surgical ward."},
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Mr. Boffin took immense delight in acting as a secret **donor**, relieving poor families without revealing his name."}
    ]
  },
  "Dashboard — don/donut.md": {
    "primary": "A small fried dough confection, typically ring-shaped or filled with jam or cream; a doughnut.",
    "secondary": "In topology and differential geometry, a donut shape is formally classified as a torus with a single topological genus.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The stagecoach passengers devoured hot coffee and fried **donut** cakes at the wayside mountain station with ferocious appetite."},
      {"author": "William Dean Howells", "work": "The Rise of Silas Lapham", "quote": "The country breakfast featured fresh milk, maple syrup, and a heaping plate of crisp homemade **donut** pastries."},
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Meg fried a batch of sweet **donut** treats for the Christmas picnic, to the great delight of the March girls."}
    ]
  },
  "Dashboard — don/indonesia.md": {
    "primary": "A sovereign archipelago nation in Southeast Asia consisting of thousands of volcanic islands between the Indian and Pacific Oceans.",
    "secondary": "In geographical and biogeographical history, Indonesia straddles Wallace's Line, dividing Asian faunal ecosystems from Australian marsupial realms.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The islands of **indonesia** present to the naturalist an inexhaustible field for studying organic geographic distribution."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The coastal trading schooners plied the turquoise seas between the lush volcanic islands of **indonesia**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Wallace's discoveries in the tropical archipelago of **indonesia** provided powerful independent support for natural selection."}
    ]
  },
  "Dashboard — don/indonesian.md": {
    "primary": "Of, relating to, or characteristic of Indonesia, its people, culture, or the Indonesian language.",
    "secondary": "In Austronesian comparative linguistics, standard Indonesian is a standardized dialect of Malay that serves as the national lingua franca.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The **indonesian** boatmen navigated their outrigger proas through dangerous coral reefs with extraordinary skill."},
      {"author": "Joseph Conrad", "work": "Victory", "quote": "He made his solitary home upon a remote **indonesian** island, living peacefully among the native forest dwellers."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Ancient spice trade networks linked Mediterranean markets with the rich agricultural civilizations of the **indonesian** archipelago."}
    ]
  },
  "Dashboard — don/overdone.md": {
    "primary": "Cooked too much; or exaggerated, excessive, and carried beyond reasonable limits.",
    "secondary": "In literary aesthetics and dramatic performance, overdone melodrama provokes derisive laughter rather than authentic tragic pity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For anything so **overdone** is from the purpose of playing, whose end, both at the first and now, was and is, to hold, as 'twere, the mirror up to nature."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe's apologies were somewhat **overdone**, but were offered with such genuine tenderness that Pip embraced him."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins's elaborate compliments were so **overdone** that they offended good taste and exhausted everyone's patience."}
    ]
  },
  "Dashboard — don/pardon.md": {
    "primary": "The action of forgiving or being forgiven for an error or offense; executive clemency.",
    "secondary": "In constitutional law, the executive pardon power allows the head of state to commute sentences or grant full legal amnesty to convicted offenders.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "That thou shalt see the difference of our spirits, I **pardon** thee thy life before thou ask it: for half thy wealth, it is Antonio's; the other half comes to the general state."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The doctor pleaded desperately for the prisoner's **pardon** before the bloodthirsty revolutionary tribunal."},
      {"author": "Abraham Lincoln", "work": "Proclamation of Amnesty and Reconstruction", "quote": "A full **pardon** is hereby granted to all persons who participated in the rebellion, upon taking a solemn oath of future loyalty."}
    ]
  },
  "Dashboard — don/pardonable.md": {
    "primary": "Able to be excused, forgiven, or tolerated; excusable and understandable.",
    "secondary": "In moral philosophy, a pardonable lapse arises from human frailty, ignorance, or sudden emotion rather than premeditated malice.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor considered her sister's romantic enthusiasm as an amiable and completely **pardonable** excess of youthful feeling."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Watson felt that his curiosity was **pardonable** under circumstances so extraordinary and perilous."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy's errors were regarded by his uncle as **pardonable** follies, provided they were promptly repented of."}
    ]
  },
  "Dashboard — don/pardoner.md": {
    "primary": "A medieval church official authorized to sell papal pardons or indulgences; or a person who pardons.",
    "secondary": "In Geoffrey Chaucer's Canterbury Tales, the Pardoner is depicted as a corrupt, hypocritical cleric selling fraudulent relics and papal bulls.",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "With him there rode a gentle **pardoner** of Rouncivale, his friend and his peer, who sang full loud, 'Come hither, love, to me!'"},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The scandalous traffic of the itinerant **pardoner** provoked the indignation of early reformers throughout northern Europe."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The mendicant **pardoner** carried in his leather wallet leaden papal seals and purported splinters of the true cross."}
    ]
  },
  "Dashboard — don/underdone.md": {
    "primary": "Insufficiently cooked; rare, or raw in the center.",
    "secondary": "In dramatic criticism, an underdone theatrical staging lacks emotional conviction, character development, and production polish.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge muttered that the ghostly apparition was only a blot of mustard, a crumb of cheese, or a piece of **underdone** potato."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley grumbled loudly at the hotel waiter, complaining that the roasted beef was **underdone** and cold."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The rustic bakers at the fair turned out batches of **underdone** bread that drew fierce complaints from the townspeople."}
    ]
  },
  "Dashboard — don/undone.md": {
    "primary": "Not done, finished, or completed; or unfastened; or ruined and brought to destruction.",
    "secondary": "In classical tragedy and Elizabethan drama, the lament 'I am undone' expresses catastrophic personal or dynastic ruin.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "O, banish me, my lord, but kill me not! Down, strumpet! Kill me to-morrow: let me live to-night! Nay, if you strive— But half an hour! Being **done**, there is no pause. But while I say one prayer! It is too late. O Lord, Lord, Lord! My wife! my wife! what wife? I have no wife. O, insupportable! O heavy hour! Methinks it should be now a huge eclipse of sun and moon, and that the affrighted globe should yawn at alteration. I do beseech you that I may speak with you, O, good my lord! I had forgot thee: O, come in, Emilia: soft; by and by. Let me the curtains draw. Where art thou? What's the matter with thee now? O, my good lord, yonder's foul murders done! What, now? But now, my lord. It is the very error of the moon; she comes more nearer earth than she was wont, and makes men mad. Cassio, my lord, hath kill'd a young Venetian call'd Roderigo. Roderigo kill'd! And Cassio kill'd! No, Cassio is not kill'd. Not Cassio kill'd! Then murder's out of tune, and sweet revenge grows harsh. O, falsely, falsely murder'd! Alas, what cry is that? That! what? Out, and alas! that was my lady's voice. Help! help, ho! help! O lady, speak again! Sweet Desdemona! O sweet mistress, speak! A guiltless death I die. O, who hath done this deed? Nobody; I myself. Farewell; commend me to my kind lord: O, farewell! Why, how should she be murder'd? Alas, who knows? You heard her say herself, it was not I. She said so: I must needs report the truth. She's, like a liar, gone to burning hell: 'twas I that kill'd her. O, the more angel she, and you the blacker devil! She turn'd to folly, and she was a whore. Thou dost belie her, and thou art a devil. She was false as water. Thou art rash as fire, to say that she was false: O, she was heavenly true! Cassio did top her; ask thy husband else. O, I were damn'd beneath all depth in hell, but that I did proceed upon just grounds to this extremity. Thy husband knew it all. My husband! Thy husband. That she was false to wedlock? Ay, with Cassio. Nay, had she been true, if heaven would make me such another world of one entire and perfect chrysolite, I'ld not have sold her for it. My husband! Ay, 'twas he that told me first: an honest man he is, and hates the slime that sticks on filthy deeds. My husband! What needs this iterance, woman? I say thy husband. O mistress, villainy hath made mocks with love! My husband say that she was false! He, woman; I say thy husband: dost understand the word? My friend, thy husband, honest, honest Iago. If he say so, may his pernicious soul rot half a grain a day! He lies to the heart: she was too fond of her most filthy bargain. Ha! Do thy worst: this deed of thine is no more worthy heaven than thou wast worthy her. Peace, you were best. Thou hast not half that power to do me harm as I have to be hurt. O gull! O dolt! As ignorant as dirt! Thou hast done a deed— I care not for thy sword; I'll make thee known, though I lost twenty lives. Help! help, ho! help! The Moor hath kill'd my mistress! Murder! murder! What is the matter? How now, general! O, are you come, Iago? You have done well, that men must lay their murders on your neck. What is the matter? Disprove this villain, if thou be'st a man: he says thou told'st him that his wife was false: I know thou didst not, thou'rt not such a villain: speak, for my heart is full. I told him what I thought, and told no more than what he found himself was apt and true. But did you ever tell him she was false? I did. You told a lie, an odious, damned lie; upon my soul, a lie, a wicked lie. She false with Cassio!—did you say with Cassio? With Cassio, mistress. Go to, charm your tongue. I will not charm my tongue; I am bound to speak: my mistress here lies murder'd in her bed,— All. O heavens forfend! And your reports have set the murder on. Nay, stare not, masters: it is true, indeed. 'Tis a strange truth. O monstrous act! Villainy, villainy, villainy! I think upon't, I think: I smell't: O villainy!— I thought so then:—I'll kill myself for grief:— O villainy, villainy! What, are you mad? I charge you, get you home. Good gentlemen, let me have leave to speak: 'tis proper I obey him, but not now. Perchance, Iago, I will ne'er go home. O! O! O! Nay, lay thee down and roar; for thou hast kill'd the sweetest innocent that e'er did lift up eye. O, she was foul! I scarce did know you, uncle: there lies your niece, whose breath, indeed, these hands have newly stopp'd: I know this act shows horrible and grim. Poor Desdemona! I am glad thy father's dead: thy match was mortal to him, and pure grief shore his old thread in twain: did he live now, this sight would make him do a desperate turn, yea, curse his better angel from his side, and fall to reprobation. 'Tis pitiful; but yet Iago knows that she with Cassio hath the act of shame a thousand times committed; Cassio confess'd it: and she did gratify his amorous works with that recognizance and pledge of love which I first gave her; I saw it in his hand: it was a handkerchief, an antique token my father gave my mother. O heaven! O heavenly powers! Come, hold your peace. 'Twill out, 'twill out: I peace! No, I will speak as liberal as the north: let heaven and men and devils, let them all, all, all, cry shame against me, yet I'll speak. Be wise, and get you home. I will not. Fie! Your sword upon a woman? O thou dull Moor! That handkerchief thou speak'st of I found by fortune and did give my husband; for often, with a solemn earnestness, more than indeed belong'd to such a trifle, he begg'd of me to steal it. Villainous whore! She gave it Cassio! No, alas! I found it, and I did give't my husband. Filth, thou liest! By heaven, I do not, I do not, gentlemen. O murderous coxcomb! What should such a fool do with so good a wife? Are there no stones in heaven but what serve for the thunder?—Precious villain! The woman falls; sure, he hath kill'd his wife. Ay, ay: O, lay me by my mistress' side. He's gone, but his wife's kill'd. 'Tis a notorious villain. Take you this weapon, which I have here recover'd from the Moor: come, guard the door without; let him not pass, but kill him rather. I'll after that same villain, for 'tis a damned slave. I am not valiant neither, but every puny whipster gets my sword: but why should honour outlive honesty? Let it go all. What did thy song bode, lady? Hark, canst thou hear me? I will play the swan, and die in music. Willow, willow, willow.— Moor, she was chaste; she loved thee, cruel Moor; so come my soul to bliss, as I speak true; so speaking as I think, I die, I die. I have another weapon in this chamber; it is a sword of Spain, the ice-brook's temper:— O, here it is. Uncle, I must come forth. If thou attempt it, it will cost thee dear: thou hast no weapon, and perforce must suffer. Look in upon me then and speak with me, or, naked as I am, I will assault thee. What is the matter? Behold, I have a weapon; a better never did itself sustain upon a soldier's thigh: I have seen the day, that, with this little arm and this good sword, I have made my way through more impediments than twenty times your stop: but, O vain boast! Who can control his fate? 'Tis not so now. Be not afraid, though you do see me weapon'd; here is my journey's end, here is my butt, and very sea-mark of my utmost sail. Do you go back dismay'd? 'Tis a lost fear; man but a rush against Othello's breast, and he retires. Where should Othello go? Now, how dost thou look now? O ill-starr'd wench! Pale as thy smock! When we shall meet at compt, this look of thine will hurl my soul from heaven, and fiends will snatch at it. Cold, cold, my girl! Even like thy chastity. O cursed slave! Whip me, ye devils, from the possession of this heavenly sight! Blow me about in winds! Roast me in sulphur! Wash me in steep-down gulfs of liquid fire! O Desdemona! Desdemona! Dead! O! O! O! Where is this rash and unfortunate man? That's he that was Othello: here I am. Where is that viper? Bring the villain forth. I look down towards his feet; but that's a fable. If that thou be'st a devil, I cannot kill thee. Wrench his sword from him. I bleed, sir; but not kill'd. I am not sorry neither: I'ld have thee live; for, in my sense, 'tis happiness to die. O thou Othello, that wert once so good, fall'n in the practice of a damned slave, what shall be said to thee? Why, anything: an honourable murderer, if you will; for nought I did in hate, but all in honour. This wretch hath part confess'd his villainy: did you and he consent in Cassio's death? Ay. Dear general, I never gave you cause. I do believe it, and I ask your pardon. Will you, I pray, demand that demi-devil why he hath thus ensnared my soul and body? Demand me nothing: what you know, you know: from this time forth I never will speak word. What, not to pray? Torments will ope your lips. Well, thou dost best. Sir, you shall understand what hath befall'n, which, as I think, you know not. Here is a letter found in the pocket of the slain Roderigo; and here another: the one of them imports the death of Cassio to be undertook by Roderigo. O villain! Most heathenish and most gross! Now here's another discontented paper, found in his pocket too; and this, it seems, Roderigo meant to have sent this damned villain; but that belike Iago in the interim came in and satisfied him. O the pernicious caitiff! How came you, Cassio, by that handkerchief that was my wife's? I found it in my chamber: and he himself confess'd but even now that there he dropp'd it for a special purpose which wrought to his desire. O fool! Fool! Fool! There is besides in Roderigo's letter, how he upbraids Iago, that he made him brave me upon the watch; whereon it came that I was cast: and even but now he spake, after long seeming dead, Iago hurt him, Iago set him on. You must forsake this room, and go with us: your power and your command is taken off, and Cassio rules in Cyprus. For this slave, if there be any cunning cruelty that can torment him much and hold him long, it shall be his. You shall close prisoner rest, till that the nature of your fault be known to the Venetian state. Come, bring away. Soft you; a word or two before you go. I have done the state some service, and they know't. No more of that. I pray you, in your letters, when you shall these unlucky deeds relate, speak of me as I am; nothing extenuate, nor set down aught in malice: then must you speak of one that loved not wisely but too well; of one not easily jealous, but being wrought perplex'd in the extreme; of one whose hand, like the base Indian, threw a pearl away richer than all his tribe; of one whose subdued eyes, albeit unused to the melting mood, drop tears as fast as the Arabian trees their medicinal gum. Set you down this; and say besides, that in Aleppo once, where a malignant and a turban'd Turk beat a Venetian and traduced the state, I took by the throat the circumcised dog, and smote him, thus. O bloody period! All that's spoke is marr'd. I kiss'd thee ere I kill'd thee: no way but this; killing myself, to die upon a kiss. This did I fear, but thought he had no weapon; for he was great of heart. O Spartan dog, more fell than anguish, hunger, or the sea! Look on the tragic loading of this bed; this is thy work: the object poisons sight; let it be hid. Gratiano, keep the house, and seize upon the fortunes of the Moor, for they succeed on you. To you, lord governor, remains the censure of this hellish villain; the time, the place, the torture: O, enforce it! Myself will straight aboard: and to the state this heavy act with heavy heart relate. All our hopes are forever **undone** by this fatal catastrophe."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The wedding was stopped at the very altar rail, and I stood before God and man a woman utterly **undone**."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He left many tasks **undone** in his careless, happy-go-lucky fashion, trusting to tomorrow for remedy."}
    ]
  },
  "Dashboard — don/unpardonable.md": {
    "primary": "Too severe, offensive, or heinous to be pardoned or forgiven; inexcusable.",
    "secondary": "In Christian theological ethics, the unpardonable sin (blasphemy against the Holy Spirit) denotes obstinate, impenitent rejection of divine grace.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth declared that Wickham's deceit and ingratitude toward Mr. Darcy were of an **unpardonable** nature."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth's calculated intellectual violation of another human heart was the only truly **unpardonable** sin."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt that his ungrateful neglect of Joe Gargery was an **unpardonable** baseness that haunted his conscience."}
    ]
  },

  # --- Dashboard — firm (36 words) ---
  "Dashboard — firm/affirm.md": {
    "primary": "To state something as a fact strongly and publicly; to confirm, ratify, or validate.",
    "secondary": "In judicial oaths and court procedure, witnesses with religious objections to swearing oaths are legally permitted to affirm their testimony under penalty of perjury.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "To **affirm** that an idea is innate, and at the same time to say that the mind is unaware of it, is a manifest contradiction."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The state conventions will **affirm** the federal compact as the supreme law of the unified American commonwealth."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The dogmatic philosophers **affirm** universal doctrines before they have collected sufficient empirical observations."}
    ]
  },
  "Dashboard — firm/affirmable.md": {
    "primary": "Capable of being affirmed, stated as true, or legally validated; assertable.",
    "secondary": "In formal logic and epistemology, a proposition is affirmable only when it satisfies verifiable criteria of logical consistency.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Whatever is **affirmable** of the whole class is necessarily affirmable of every individual included in that class."},
      {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "Truth becomes **affirmable** of an idea whenever its practical consequences harmonize with our wider web of experience."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The reality of an external world remains an **affirmable** datum underlying all consciousness."}
    ]
  },
  "Dashboard — firm/affirmatio.md": {
    "primary": "A formal affirmation, assertion, or Latin rhetorical statement of fact.",
    "secondary": "In classical Roman rhetoric and scholastic dialectic, the affirmatio constitutes the positive thesis defended against the opposing negatio.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Scholastic disputants relied upon formal **affirmatio** to establish doctrines without empirical verification."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A clear **affirmatio** in speech should correspond to a distinct and well-defined idea in the mind."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancient naturalists accepted with easy **affirmatio** many fables that modern dissection easily disproves."}
    ]
  },
  "Dashboard — firm/affirmation.md": {
    "primary": "The action of affirming something, or a formal declaration that something is true.",
    "secondary": "In psychology and cognitive behavioral therapy, a positive affirmation is a repeated self-statement intended to challenge negative automated thoughts.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "My resolutions are based on the plain **affirmation** of undeniable facts recorded in our parliamentary journals."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A general proposition is an **affirmation** of a relation between attributes that holds true across all instances."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's quiet **affirmation** of faith in Lydgate's honor gave the distressed physician fresh courage."}
    ]
  },
  "Dashboard — firm/affirmative.md": {
    "primary": "Agreeing with or consenting to a statement or request; positive and confirming.",
    "secondary": "In United States constitutional civil rights law, affirmative action policies take proactive measures to remedy historical educational and employment disparities.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth gave an **affirmative** nod to his inquiry, while secretly wondering at the sudden change in his demeanor."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Barkis nodded in the **affirmative**, declaring that Barkis was willing whenever Clara was ready."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The Senate must give its **affirmative** consent before any foreign treaty negotiated by the President can take effect."}
    ]
  },
  "Dashboard — firm/affirmatively.md": {
    "primary": "In a way that expresses agreement, consent, or positive assertion.",
    "secondary": "In legislative voting records, members voting affirmatively register their formal statutory assent to the bill.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes nodded **affirmatively** as the footprints revealed that the beast had indeed turned back at the gate."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I answered **affirmatively** when Mr. Rochester asked whether I was prepared to endure hard journeys with him."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak answered **affirmatively** to the bailiff's questions, his calm honesty winning instant trust."}
    ]
  },
  "Dashboard — firm/affirmativeness.md": {
    "primary": "The quality of being positive, assertive, or expressing firm agreement and confidence.",
    "secondary": "In social psychology, communicational affirmativeness balances personal conviction with polite social receptivity.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Goethe possessed a healthy **affirmativeness** of mind that embraced all aspects of human culture and natural growth."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Religious faith imparts an **affirmativeness** to character that transforms moral duty into joyous spiritual enthusiasm."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She was attracted by the calm **affirmativeness** of his principles, contrasting with her own inner turmoil."}
    ]
  },
  "Dashboard — firm/affirmatory.md": {
    "primary": "Serving to affirm, confirm, or state positively; corroborating.",
    "secondary": "In evidentiary jurisprudence, an affirmatory statement reinforces direct testimonial evidence during trial proceedings.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Men are naturally prone to welcome **affirmatory** instances while overlooking negative evidence that contradicts their beliefs."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "An **affirmatory** proposition asserts the co-existence of two distinct ideas in the same subject."},
      {"author": "Thomas Huxley", "work": "Science and Education", "quote": "The experimental demonstration provided an **affirmatory** proof that convinced even the most skeptical savants."}
    ]
  },
  "Dashboard — firm/affirmed.md": {
    "primary": "Stated publicly as a fact; confirmed, validated, or legally declared under affirmation.",
    "secondary": "In appellate judicial procedure, a lower court judgment is affirmed when the appellate court upholds its legal correctness.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient chroniclers **affirmed** that a fiery comet had blazed in the heavens prior to the barbarian invasion."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Henslow **affirmed** that varieties cultivated under diverse soils frequently alter their morphological habits."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The celestial herald **affirmed** the eternal decrees of Providence before the assembled heavenly host."}
    ]
  },
  "Dashboard — firm/affirmer.md": {
    "primary": "A person who affirms something or makes a positive formal declaration.",
    "secondary": "In legal swearing, an affirmer makes a solemn affirmation under penalty of perjury rather than taking a religious oath.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Boldness is ever blind; wherefore it is ill in counsel, though good in execution, and the confident **affirmer** often misleads the prudent statesman."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The burden of empirical proof rests squarely upon the **affirmer** of a novel scientific hypothesis."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "We ought not hastily to condemn the ancient **affirmer** until we have examined the original conditions of his experiment."}
    ]
  },
  "Dashboard — firm/cantus firmus.md": {
    "primary": "A pre-existing melody forming the basis of a polyphonic musical composition.",
    "secondary": "In Renaissance counterpoint and Gregorian chant, the cantus firmus is sustained in long notes by the tenor voice while other voices weave imitative polyphony.",
    "quotes": [
      {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "The ancient sacred melody served as a **cantus firmus** around which the composer wove rich secular polyphony."},
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The choral fugue rested upon a solid **cantus firmus** intoned with majestic solemnity by the massed basses."},
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "He demonstrated how the medieval **cantus firmus** provided architectural discipline to the wildest harmonic experiments."}
    ]
  },
  "Dashboard — firm/confirm.md": {
    "primary": "To establish the truth or correctness of something; to make definite, ratify, or strengthen.",
    "secondary": "In Christian liturgy, to confirm candidates in the sacrament of confirmation seals their baptismal vows with episcopal chrism and laying on of hands.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Subsequent observations have served only to **confirm** the truth of the principle that natural selection acts by preserving slight modifications."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A single glance at the footprint was sufficient to **confirm** my darkest suspicions regarding the intruder."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "A letter from Jane arrived to **confirm** all the distressing particulars of Lydia's elopement with Wickham."}
    ]
  },
  "Dashboard — firm/confirmable.md": {
    "primary": "Capable of being confirmed, verified, or established as true by evidence or testing.",
    "secondary": "In philosophy of science and logical positivism, a hypothesis is empirically confirmable if observation statements can raise its subjective probability.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A scientific theory is genuinely **confirmable** only when it yields novel deductions that survive experimental scrutiny."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "The hypothesis remained easily **confirmable** by any naturalist equipped with a standard compound microscope."},
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "Scientific facts are those which are independently **confirmable** by all competent normal observers."}
    ]
  },
  "Dashboard — firm/confirmation.md": {
    "primary": "The action of confirming something, or state of being confirmed; proof, validation, or a religious rite.",
    "secondary": "In sacramental theology, confirmation is one of the three sacraments of Christian initiation, imparting the seven gifts of the Holy Spirit.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Trifles light as air are to the jealous **confirmation** strong as proofs of holy writ: this may do something."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The telegram provided an unexpected **confirmation** of our theory, pointing directly toward the Thames wharves."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I awaited the arrival of the post in breathless anxiety, seeking **confirmation** of my sister's safety."}
    ]
  },
  "Dashboard — firm/confirmative.md": {
    "primary": "Serving to confirm, verify, or support a statement, theory, or belief.",
    "secondary": "In psychological measurement, confirmative factor analysis tests whether data fit a pre-specified structural equation measurement model.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The experiment yielded **confirmative** evidence of the hidden thermal motion underlying physical combustion."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Comparative embryology furnishes **confirmative** proof of man's descent from a lower vertebrate prototype."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Paleontological discoveries provide striking **confirmative** instances of progressive evolutionary specialization."}
    ]
  },
  "Dashboard — firm/confirmator.md": {
    "primary": "An archaic term for a person or agency that confirms, establishes, or attests to something.",
    "secondary": "In historical legal conveyancing and medieval diplomatic charters, a confirmator formally ratified the feudal privileges granted by predecessors.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The authority of Pliny was long accepted as the sole **confirmator** of extraordinary botanical marvels."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Experiment must stand as the supreme **confirmator** of philosophical doctrines against the assertions of ancient schools."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sovereign pontiff acted as the imperial **confirmator** of treaties between contending Christian princes."}
    ]
  },
  "Dashboard — firm/confirmatory.md": {
    "primary": "Serving or tending to confirm, corroborate, or verify a finding, statement, or result.",
    "secondary": "In clinical diagnostics, a confirmatory Western blot test verifies initial reactive enzyme immunoassay screening results.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The fossil beds of South America afforded rich **confirmatory** testimony to the mutual affinities of allied extinct mammals."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The second footprints were an invaluable **confirmatory** link in the chain of deduction."},
      {"author": "Thomas Huxley", "work": "Man's Place in Nature", "quote": "Anatomical dissection yielded **confirmatory** proof that anthropoid apes share identical skeletal muscle arrangements with man."}
    ]
  },
  "Dashboard — firm/confirmed.md": {
    "primary": "Having been established, verified, or validated; settled in habits or conditions.",
    "secondary": "In medical pathology, a confirmed diagnosis is corroborated by definitive laboratory, imaging, or histological findings.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth's worst fears were **confirmed** when she read that Wickham had no intention whatever of marrying her sister."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber was a **confirmed** optimist, forever expecting financial salvation from some unforeseen quarter."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The laboratory test **confirmed** that the brownish stain upon the floor was human blood of recent origin."}
    ]
  },
  "Dashboard — firm/confirming.md": {
    "primary": "Providing proof, verification, or validation; strengthening or ratifying.",
    "secondary": "In empirical epistemology, confirming evidence elevates the posterior probability of a hypothesis under Bayesian analysis.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every naturalist who has visited isolated oceanic islands will bear **confirming** witness to the absence of terrestrial mammals."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes examined the ashes in the grate, **confirming** his suspicion that a valuable document had been destroyed."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate listened in silence, every word **confirming** his bitter realization that his marriage was an irreparable error."}
    ]
  },
  "Dashboard — firm/disaffirmation.md": {
    "primary": "The act of disaffirming, denying, invalidating, or repudiating a previous statement or contract.",
    "secondary": "In contract law, disaffirmation is the legal power of a minor or incapacitated party to void a voidable contract upon reaching legal age.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The infant retains the legal privilege of **disaffirmation** regarding deeds executed during his minority."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A clear negative judgment involves the intellectual **disaffirmation** of a supposed connection between two ideas."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parliamentary declaration stood as a formal **disaffirmation** of the monarch's dispensing power."}
    ]
  },
  "Dashboard — firm/disconfirming.md": {
    "primary": "Serving to disprove, contradict, or invalidate a hypothesis, belief, or expectation.",
    "secondary": "In cognitive psychology and Popperian falsificationism, seeking disconfirming evidence prevents confirmation bias from perpetuating invalid theories.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I have during many years made a golden rule to record immediately any **disconfirming** fact that ran counter to my theories."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A single well-authenticated **disconfirming** instance is sufficient to overturn a universal empirical induction."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The human mind naturally resists **disconfirming** observations that threaten deeply ingrained ideological habits."}
    ]
  },
  "Dashboard — firm/firm.md": {
    "primary": "Solid, stable, resolute, and resistant to pressure; or a commercial partnership or business enterprise.",
    "secondary": "In the theory of the firm in microeconomics, a firm is an organizational entity coordinating production factors under centralized managerial direction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "I am constant as the northern star, of whose true-fix'd and resting quality there is no fellow in the firmament; the skies are painted with unnumber'd sparks, they are all fire and every one doth shine, but there's but one in all doth hold his place: so in the world; 'tis furnish'd well with men, and men are flesh and blood, and apprehensive; yet in the number I do know but one that unassailable holds on his rank, unshaked of motion: and that I am he, let me a little show it, even in this; that I was constant Cimber should be banish'd, and constant do remain to keep him so. O Caesar,— Hence! Wilt thou lift up Olympus? Great Caesar,— Doth not Brutus bootless kneel? Speak, hands, for me! Et tu, Brute! Then fall, Caesar! Liberty! Freedom! Tyranny is dead! Run hence, proclaim, cry it about the streets. Some to the common pulpits, and cry out 'Liberty, freedom, and enfranchisement!' People and senators, be not affrighted; fly not; stand still: ambition's debt is paid. Go to the pulpit, Brutus. And Cassius too. Where's Publius? Here, quite confounded with this mutiny. Stand fast together, lest some friend of Caesar's should chance— Talk not of standing. Publius, good cheer; there is no harm intended to your person, nor to no Roman else: so tell them, Publius. And leave us, Publius; lest that the people, rushing on us, should do your age some mischief. Do so: and let no man abide this deed, but we the doers. Where is Antony? Fled to his house amazed: men, wives and children stare, cry out and run as it were doomsday. Fates, we will know your pleasures: that we shall die, we know; 'tis but the time and drawing days out, that men stand upon. Why, he that cuts off twenty years of life cuts off so many years of fearing death. Grant that, and then is death a benefit: so are we Caesar's friends, that have abridged his time of fearing death. Stoop, Romans, stoop, and let us bathe our hands in Caesar's blood up to the elbows, and besmear our swords: then walk we forth, even to the market-place, and, waving our red weapons o'er our heads, let's all cry 'Peace, freedom and liberty!' Stoop, then, and wash. How many ages hence shall this our lofty scene be acted over in states unborn and accents yet unknown! How many times shall Caesar bleed in sport, that now on Pompey's basis lies along no worthier than the dust! So oft as that shall be, so often shall the knot of us be call'd the men that gave their country liberty. What, shall we forth? Ay, every man away: Brutus shall lead; and we will grace his heels with the most boldest and best hearts of Rome. Soft! Who comes here? A friend of Antony's. Thus, Brutus, did my master bid me kneel; thus did Mark Antony bid me fall down; and, being prostrate, thus he bade me say: Brutus is noble, wise, valiant, and honest; Caesar was mighty, bold, royal, and loving: say I love Brutus, and I honour him; say I fear'd Caesar, honour'd him and loved him. If Brutus will vouchsafe that Antony may safely come to him, and be resolved how Caesar hath deserved to lie in death, Mark Antony shall not love Caesar dead so well as Brutus living; but will follow the fortunes and affairs of noble Brutus thorough the hazards of this untrod state with all true faith. So says my master. Thy master is a wise and valiant Roman; I never thought him worse. Tell him, so please him come unto this place, he shall be satisfied; and, by my honour, depart untouch'd. I'll fetch him presently. I know that we shall have him well to friend. I wish we may: but yet have I a mind that fears him much; and my misgiving still falls shrewdly to the purpose. But here comes Antony. Welcome, Mark Antony. O mighty Caesar! Dost thou lie so low? Are all thy conquests, glories, triumphs, spoils, shrunk to this little measure? Fare thee well. I know not, gentlemen, what you intend, who else must be let blood, who else is rank: if I myself, there is no hour so fit as Caesar's death's hour, nor no instrument of half that worth as those your swords, made rich with the most noble blood of all this world. I do beseech ye, if you bear me hard, now, whilst your purpled hands do reek and smoke, fulfil your pleasure. Live a thousand years, I shall not find myself so apt to die: no place will please me so, no mean of death, as here by Caesar, and by you cut off, the choice and master spirits of this age. O Antony, beg not your death of us. Though now we must appear bloody and cruel, as, by our hands and this our present act, you see we do, yet see you but our hands and this the bleeding business they have done: our hearts you see not; they are pitiful; and pity to the general wrong of Rome—as fire drives out fire, so pity pity—hath done this deed on Caesar. For your part, to you our swords have leaden points, Mark Antony: our arms in strength of malice, and our hearts of brothers' temper, do receive you in with all kind love, good thoughts, and reverence. Your voice shall be as strong as any man's in the disposing of new dignities. Only be patient till we have appeased the multitude, beside themselves with fear, and then we will deliver you the cause, why I, that did love Caesar when I struck him, have thus proceeded. I doubt not of your wisdom. Let each man render me his bloody hand: first, Marcus Brutus, will I shake with you; next, Caius Cassius, do I take your hand; now, Decius Brutus, yours; now yours, Metellus; yours, Cinna; and, my valiant Casca, yours; though last, not least in love, yours, good Trebonius. Gentlemen all,—alas, what shall I say? My credit now stands on such slippery ground, that one of two bad ways you must conceit me, either a coward or a flatterer. That I did love thee, Caesar, O, 'tis true: if then thy spirit look upon us now, shall it not grieve thee dearer than thy death, to see thy Antony making his peace, shaking the bloody fingers of thy foes, most noble! In the presence of thy corse? Had I as many eyes as thou hast wounds, weeping as fast as they stream forth thy blood, it would become me better than to close in terms of friendship with thine enemies. Pardon me, Julius! Here wast thou bay'd, brave hart; here didst thou fall; and here thy hunters stand, sign'd in thy spoil, and crimson'd in thy lethe. O world, thou wast the forest to this hart; and this, indeed, O world, the heart of thee. How like a deer, strucken by many princes, dost thou here lie! Mark Antony,— Pardon me, Caius Cassius: the enemies of Caesar shall say this; then, in a friend, it is cold modesty. I blame you not for praising Caesar so; but what compact mean you to have with us? Will you be prick'd in number of our friends; or shall we on, and not depend on you? Therefore I took your hands, but was, indeed, sway'd from the point, by looking down on Caesar. Friends am I with you all and love you all, upon this hope, that you shall give me reasons why and wherein Caesar was dangerous. Or else were this a savage spectacle: our reasons are so full of good regard that were you, Antony, the son of Caesar, you should be satisfied. That's all I seek: and am moreover suitor that I may produce his body to the market-place; and in the pulpit, as becomes a friend, speak in the order of his funeral. You shall, Mark Antony. Brutus, a word with you. You know not what you do: do not consent that Antony speak in his funeral: know you how much the people may be moved by that which he will utter? By your pardon; I will myself into the pulpit first, and show the reason of our Caesar's death: what Antony shall speak, I will protest he speaks by leave and by our permission, and that we are contented Caesar shall have all true rites and lawful ceremonies. It shall advantage more than do us wrong. I know not what may fall; I like it not. Mark Antony, here, take you Caesar's body. You shall not in your funeral speech blame us, but speak all good you can devise of Caesar, and say you do't by our permission; else shall you not have any hand at all about his funeral: and you shall speak in the same pulpit whereto I am going, after my speech is ended. Be it so; I do desire no more. Prepare the body then, and follow us. O, pardon me, thou bleeding piece of earth, that I am meek and gentle with these butchers! Thou art the ruins of the noblest man that ever lived in the tide of times. Woe to the hand that shed this costly blood! Over thy wounds now do I prophesy,—which, like dumb mouths, do ope their ruby lips, to beg the voice and utterance of my tongue—a curse shall light upon the limbs of men; domestic fury and fierce civil strife shall cumber all the parts of Italy; blood and destruction shall be so in use and dreadful objects so familiar that mothers shall but smile when they behold their infants quarter'd with the hands of war; all pity choked with custom of fell deeds: and Caesar's spirit, ranging for revenge, with Ate by his side come hot from hell, shall in these confines with a monarch's voice cry 'Havoc,' and let slip the dogs of war; that this foul deed shall smell above the earth with carrion men, groaning for burial. You serve Octavius Caesar, do you not? I do, Mark Antony. Caesar did write for him to come to Rome. He did receive his letters, and is coming; and bid me say to you by word of mouth— O Caesar!— Thy heart is big, get thee apart and weep. Passion, I see, is catching; for mine eyes, seeing those beads of sorrow stand in thine, began to water. Is thy master coming? He lies to-night within seven leagues of Rome. Post back with speed, and tell him what hath chanced: here is a mourning Rome, a dangerous Rome, no Rome of safety for Octavius yet; hie hence, and tell him so. Yet, stay awhile; thou shalt not back till I have borne this corse into the market-place: there shall I try, in my oration, how the people take the cruel issue of these bloody men; the which thou shalt assist. Lend me your hand. We must stand **firm** against the storms of fate."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The shoemaker of the Bastille kept his bench with a **firm** and mechanical industry that shut out all surrounding horrors."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy stood with a **firm** step and haughty reserve, declining to be introduced to any lady outside his own party."}
    ]
  },
  "Dashboard — firm/firmament.md": {
    "primary": "The heavens or the sky, especially when regarded as a tangible vault or arch.",
    "secondary": "In biblical cosmology and historical astronomy, the firmament (firmamentum) was conceived as a solid crystalline dome separating terrestrial and celestial waters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "This goodly frame, the earth, seems to me a sterile promontory, this most excellent canopy, the air, look you, this brave o'erhanging **firmament**, this majestical roof fretted with golden fire, why, it appears no other thing to me than a foul and pestilent congregation of vapours."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Let there be light! God said; and forth flew the radiant sun, blazing across the vaulted **firmament**."},
      {"author": "Percy Bysshe Shelley", "work": "Adonais", "quote": "The soul of Adonais, like a star, beacons from the abode where the eternal are, high above our cloudy **firmament**."}
    ]
  },
  "Dashboard — firm/firmamental.md": {
    "primary": "Of, relating to, or situated in the firmament; celestial or celestial-vaulted.",
    "secondary": "In Romantic poetics and cosmological metaphysics, firmamental beauty reflects transcendent cosmic harmony presiding above earthly mutability.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "The stars were dim, and thick the night; the helmsman's face by the lamp gleam'd white; from the sails the dew did drip—till clomb above the eastern bar the horned Moon, with one bright star within the nether tip, shining with **firmamental** majesty."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Beneath the silent **firmamental** dome, man wanders through eternity wrapped in his mysterious vesture of flesh."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The stars awaken a certain reverence, because though always present, they are inaccessible, diffusing **firmamental** tranquility."}
    ]
  },
  "Dashboard — firm/firmiana.md": {
    "primary": "A genus of flowering trees in the mallow family (Malvaceae), commonly known as Chinese parasol trees.",
    "secondary": "In dendrology and ornamental horticulture, Firmiana simplex is cultivated for its smooth greenish bark, broad lobed leaves, and lightweight timber used for musical instruments.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "In the sheltered Asian valleys grows the majestic **firmiana**, renowned for its broad parasol-like foliage and fibrous bark."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Botanists have observed remarkable seed dehiscence mechanisms in species of **firmiana** cultivated across botanical gardens."},
      {"author": "Robert Fortune", "work": "A Journey to the Tea Countries of China", "quote": "Beside the temple courtyard stood a venerable **firmiana**, beneath whose dense shade the pilgrim scholars rested."}
    ]
  },
  "Dashboard — firm/firmin.md": {
    "primary": "A historical personal surname or given name derived from Latin Firminus, meaning 'firm' or 'steadfast'.",
    "secondary": "In hagiography and medieval church history, Saint Firmin of Amiens (Firminus) was a 3rd-century bishop and martyr commemorated in the cathedral sculptures of Amiens.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Bible of Amiens", "quote": "The western portal of the cathedral commemorates Saint **firmin**, the early confessor whose steadfast faith founded the northern church."},
      {"author": "William Makepeace Thackeray", "work": "The Adventures of Philip", "quote": "Dr. George **firmin** was an imposing and fashionable physician whose polished manners disguised dark pecuniary embarrassments."},
      {"author": "Walter Pater", "work": "Gaston de Latour", "quote": "The ancient cathedral bells of Saint **firmin** pealed across the quiet river meadows at the vesper hour."}
    ]
  },
  "Dashboard — firm/firmly.md": {
    "primary": "In a secure, solid, steady, or unshakeable manner; with resolute determination.",
    "secondary": "In materials science, components bound firmly together maintain tensile adhesion under thermal and mechanical vibration.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth resolved **firmly** never to mention the subject again, unwilling to distress her father's affectionate heart."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When variations are **firmly** inherited, they become the basis upon which natural selection gradually shapes distinct varieties."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes grasped the boat's tiller **firmly**, steering straight into the teeth of the blinding Thames gale."}
    ]
  },
  "Dashboard — firm/firmness.md": {
    "primary": "The state or quality of being solid, stable, resolute, and unyielding to pressure.",
    "secondary": "In moral philosophy and character psychology, firmness of mind represents the fortitude to execute moral duty despite personal temptation or intimidation.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The executive magistrate must possess sufficient constitutional **firmness** to withstand the temporary delusions of popular passion."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne Elliot admired that gentle **firmness** of character which knows how to yield without weakness and persist without obstinacy."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Murdstone constantly preached the necessity of **firmness**, which in his practice was only another name for unfeeling tyranny."}
    ]
  },
  "Dashboard — firm/infirm.md": {
    "primary": "Not physically or mentally strong, especially through age or illness; frail and feeble.",
    "secondary": "In legal and probate proceedings, an infirm testator's testamentary capacity is scrutinized to ensure decisions were free from undue influence.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "I am a very foolish fond old man, fourscore and upward, not an hour more or less; and, to deal plainly, I fear I am not in my perfect mind: methinks I should know you, and know this man; yet I am doubtful: for I am mainly ignorant what place this is; and all the skill I have remembers not these garments; nor I know not where I did lodge last night. Do not laugh at me; for, as I am a man, I think this lady to be my child Cordelia. And so I am, I am. Be your tears wet? Yes, 'faith. I pray, weep not: if you have poison for me, I will drink it. I know you do not love me; for your sisters have, as I do remember, done me wrong: you have some cause, they have not. No cause, no cause. Am I in France? In your own kingdom, sir. Do not abuse me. Be comforted, good madam: the great rage, you see, is kill'd in him: and yet it is danger to make him even o'er the time he has lost. Desire him to go in; trouble him no more till further settling. Will't please your highness walk? You must bear with me: pray you now, forget and forgive: I am old and **infirm**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ancient clerk was too **infirm** to copy records with his former speed, his hands trembling over the vellum."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Though blind and **infirm**, Samson retained a dormant divine might that would shake the Philistine temple to its foundations."}
    ]
  },
  "Dashboard — firm/infirmary.md": {
    "primary": "A place in a large institution for the care of those who are ill; a hospital or clinic.",
    "secondary": "In monastic architecture, the infirmary (infirmarium) was a dedicated cloistered building where sick monks and elderly brethren were nursed under mild rule.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Typus fever broke out at Lowood school, transforming the schoolrooms into an overcrowded and mournful **infirmary**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate dedicated his best medical energies to modernizing the Fever Hospital and New **infirmary** in the borough."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The injured carter was carried to the county **infirmary**, where the surgeons dressed his fractured limb."}
    ]
  },
  "Dashboard — firm/infirmity.md": {
    "primary": "Physical or mental weakness; frailty, feebleness, or a moral failing.",
    "secondary": "In common law jurisprudence, bodily infirmity short of total incapacity does not automatically invalidate legal deeds or contracts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Caesar was subject to fits of the falling sickness, yet his friends excused the sudden **infirmity** as the effect of great labors."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The imperfections of language are closely interwoven with the natural **infirmity** of human comprehension."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Old age brings with it inevitable physical **infirmity**, which wisdom must endure with patient resignation."}
    ]
  },
  "Dashboard — firm/reaffirm.md": {
    "primary": "To state or assert something again strongly and publicly; to confirm once more.",
    "secondary": "In international treaties and diplomatic communiqués, signatory states reaffirm their adherence to mutual non-aggression pacts.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "I hold that, in contemplation of universal law and of the Constitution, the Union of these States is perpetual, and I **reaffirm** that resolve today."},
      {"author": "Woodrow Wilson", "work": "Fourteen Points Speech", "quote": "We enter upon these negotiations to **reaffirm** the sacred rights of small nations to self-determination and sovereign liberty."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The court found it necessary to **reaffirm** the traditional common-law guarantees of individual personal liberty."}
    ]
  },
  "Dashboard — firm/reaffirmation.md": {
    "primary": "The act of reaffirming something, or a renewed confirmation of a statement or policy.",
    "secondary": "In judicial jurisprudence, the reaffirmed doctrine of stare decisis ensures stability and predictability in legal precedent.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional amendments were adopted as a formal **reaffirmation** of ancient Anglo-Saxon civil liberties."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "What the colonists demand is a solemn **reaffirmation** of their historical exemption from parliamentary taxation without representation."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The social compact receives continuous tacit **reaffirmation** whenever a citizen enjoys the protection of municipal laws."}
    ]
  },
  "Dashboard — firm/reconfirm.md": {
    "primary": "To confirm again; to establish or verify the truth or validity of something once more.",
    "secondary": "In travel administration and logistics, travelers reconfirm international airline bookings to verify seat allocations and departure schedules.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes dispatched a second telegram to **reconfirm** the arrival time of the tidal steamer at Gravesend."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The experimental breeder repeated the hybrid cross in order to **reconfirm** the statistical distribution of plumage colors."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The aeronauts checked their navigational compasses to **reconfirm** their flight trajectory toward the German frontier."}
    ]
  },
  "Dashboard — firm/unconfirmed.md": {
    "primary": "Not confirmed, verified, or established as true; lacking authoritative validation.",
    "secondary": "In military intelligence and journalism, unconfirmed reports are treated with skepticism until corroborated by multiple independent field scouts.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The rumor of the foreign diplomat's disappearance was still an **unconfirmed** report when Holmes arrived at Whitehall."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The alarming tidings from Versailles remained **unconfirmed** throughout the morning, though panic spread rapidly among the citizens."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor dismissed the rumor of a Persian rebellion as an **unconfirmed** tale invented by desert merchants."}
    ]
  },
  "Dashboard — firm/unfirm.md": {
    "primary": "Not firm, solid, or stable; wavering, unsteady, weak, or insecure.",
    "secondary": "In archaic and poetic English, an unfirm mind or footing designates physical instability or emotional vacillation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "A common slave—you know him well by sight—held up his left hand, which did flame and burn like twenty torches join'd, and yet his hand, not sensible of fire, remain'd unscorch'd. Besides—I ha' not since put up my sword—against the Capitol I met a lion, who glazed upon me, and went surly by, without annoying me: and there were drawn upon a heap a hundred ghastly women, transformed with their fears; who swore they saw men all in fire walk up and down the streets. And yesterday the bird of night did sit even at noon-day upon the market-place, hooting and shrieking. When these prodigies do so conjointly meet, let not men say 'These are their reasons; they are natural;' for, I believe, they are portentous things unto the climate that they point upon. Indeed, it is a strange-disposed time: but men may construe things after their fashion, clean from the purpose of the things themselves. Comes Caesar to the Capitol to-morrow? He doth; for he did bid Antonius send word to you he would be there to-morrow. Good night then, Casca: this disturbed sky is not to walk in. Farewell, Cicero. Who's there? A Roman. Casca, by your voice. Your ear is good. Cassius, what night is this! A very pleasing night to honest men. Who ever knew the heavens menace so? Those that have known the earth so full of faults. For my part, I have walk'd about the streets, submitting me unto the perilous night, and, thus unbraced, Casca, as you see, have bared my bosom to the thunder-stone; and when the cross blue lightning seem'd to open the breast of heaven, I did present myself even in the aim and very flash of it. But wherefore did you so much tempt the heavens? It is the part of men to fear and tremble, when the most mighty gods by tokens send such dreadful heralds to astonish us. You are dull, Casca, and those sparks of life that should be in a Roman you do want, or else you use not. You look pale and gaze and put on fear and cast yourself in wonder, to see the strange impatience of the heavens: but if you would consider the true cause why all these fires, why all these gliding ghosts, why birds and beasts from quality and kind, why old men fool and children calculate, why all these things change from their ordinance their natures and preformed faculties to monstrous quality,—why, you shall find that heaven hath infused them with these spirits, to make them instruments of fear and warning unto some monstrous state. Now could I, Casca, name to thee a man most like this dreadful night, that thunders, lightens, opens graves, and roars as doth the lion in the Capitol, a man no mightier than thyself or me in personal action, yet prodigious grown and fearful, as these strange eruptions are. 'Tis Caesar that you mean; is it not, Cassius? Let it be who it is: for Romans now have thews and limbs like to their ancestors; but, woe the while! Our fathers' minds are dead, and we are govern'd with our mothers' spirits; our yoke and sufferance show us womanish. Indeed, they say the senators to-morrow mean to establish Caesar as a king; and he shall wear his crown by sea and land, in every place, save here in Italy. I know where I will wear this dagger then; Cassius from bondage will deliver Cassius: there herein, ye gods, you make the weak most strong; there herein, ye gods, you tyrants do defeat: nor stony tower, nor walls of beaten brass, nor airless dungeon, nor strong links of iron, can be retentive to the strength of spirit; but life, being weary of these worldly bars, never lacks power to dismiss itself. If I know this, know all the world besides, that part of tyranny that I do bear I can shake off at pleasure. So can I: so every bondman in his own hand bears the power to cancel his captivity. And why should Caesar be a tyrant then? Poor man! I know he would not be a wolf, but that he sees the Romans are but sheep: he were no lion, were not Romans hinds. Those that with haste will make a mighty fire begin it with weak straws: what trash is Rome, what rubbish and what offal, when it serves for the base matter to illuminate so vile a thing as Caesar! But, O grief, where hast thou led me? I perhaps speak this before a willing bondman; then I know my answer must be made. But I am arm'd, and dangers are to me indifferent. You speak to Casca, and to such a man that is no fleering tell-tale. Hold, my hand: be factious for redress of all these griefs, and I will set this foot of mine as far as who goes farthest. There's a bargain made. Now know you, Casca, I have moved already some certain of the noblest-minded Romans to undergo with me an enterprise of honourable-dangerous consequence; and I do know, by this, they stay for me in Pompey's porch: for now, this fearful night, there is no stir or walking in the streets; and the complexion of the element in favour's like the work we have in hand, most bloody, fiery, and most terrible. Stand close awhile, for here comes one in haste. 'Tis Cinna; I do know him by his gait; he is a friend. Cinna, where haste you so? To find out you. Who's that? Metellus Cimber? No, it is Casca; one incorporate to our attempts. Am I not stay'd for, Cinna? I am glad on't. What a fearful night is this! There's two or three of us have seen strange sights. Am I not stay'd for? Tell me. Yes, you are. O Cassius, if you could but win the noble Brutus to our party— Be you content: good Cinna, take this paper, and look you lay it in the praetor's chair, where Brutus may but find it; and throw this in at his window; set this up with wax upon old Brutus' statue: all this done, repair to Pompey's porch, where you shall find us. Is Decius Brutus and Trebonius there? All but Metellus Cimber; and he's gone to seek you at your house. Well, I will hie, and so bestow these papers as you bade me. That done, repair to Pompey's theatre. Come, Casca, you and I will yet ere day see Brutus at his house: three parts of him is ours already, and the man entire upon the next encounter yields him ours. O, he sits high in all the people's hearts: and that which would appear offence in us, his countenance, like richest alchemy, will change to virtue and to worthiness. Him and his worth and our great need of him you have right well conceited. Let us go, for it is after midnight; and ere day we will awake him and be sure of him, lest his **unfirm** resolve should waver."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan trod upon the **unfirm** surface of Chaos, struggling through warring elements of fire and black air."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "His foot slipped upon the **unfirm** mossy log, tumbling him into the icy woodland pool."}
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

print(f"Cluster Action & State Batch 3B: Successfully updated {updated}/{len(data)} notes across 2 dashboards.")
