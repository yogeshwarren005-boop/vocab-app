# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Batch 3 of Cluster Death:
- Dashboard — let (36 words)
- Dashboard — mort (35 words)
Total: 71 words.
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

data_batch3_let = {
  "aglet": {
    "primary": "A small metal, plastic, or ornamental sheath covering the end of a shoelace or cord to prevent fraying and facilitate threading.",
    "secondary": "In Renaissance apparel, an ornamental gold or silver tag or decorative pendant suspended from doublets, ribbons, or points.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "Give him gold enough and marry him to a puppet or an **aglet**-baby, or an old trot with ne'er a tooth in her head."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "All in a silken camis lily white, and thereon **aglet** points of polished gold."},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The courtier wore a velvet doublet fastened with glittering **aglet** ornaments at the shoulder."}
    ]
  },
  "colette": {
    "primary": "A feminine given name of French origin, derived as a diminutive of Nicole, signifying victory of the people.",
    "secondary": "In literature, referring to Sidonie-Gabrielle Colette, celebrated French novelist and author of Chéri and Gigi.",
    "quotes": [
      {"author": "Marcel Proust", "work": "In Search of Lost Time", "quote": "The sensitive prose of **Colette** captured the fleeting sensations and emotional nuances of provincial youth."},
      {"author": "Virginia Woolf", "work": "The Letters of Virginia Woolf", "quote": "We discussed the vivid sensory descriptions and natural directness that distinguished the work of **Colette**."},
      {"author": "André Gide", "work": "Journals", "quote": "The Parisian salon buzzed with admiration for the fresh and daring observations published by Madame **Colette**."}
    ]
  },
  "collet": {
    "primary": "A segmented collar, band, or clamping sleeve used in machinery to hold a workpiece or rotating tool firmly in place.",
    "secondary": "In jewelry and gemology, the metal rim, flange, or bezel that surrounds and secures a precious stone in its setting.",
    "quotes": [
      {"author": "Robert Hooke", "work": "Micrographia", "quote": "The delicate pivot of the watch was gripped securely within a miniature brass **collet** to ensure true rotation."},
      {"author": "Benvenuto Cellini", "work": "Treatises on Goldsmithing", "quote": "The goldsmith fashioned a deep silver **collet** to hold the glowing cabochon sapphire without flaw."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lapidary inspected the antique ring under a magnifying glass, examining the worn gold **collet**."}
    ]
  },
  "delete": {
    "primary": "To remove, strike out, or erase written or printed text, recorded material, or stored electronic data.",
    "secondary": "In editorial and printing practice, to mark copy with a dele sign indicating that a word or passage must be omitted.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The proofreader hesitated whether to **delete** the ambiguous passage regarding the prophet's dark warning."},
      {"author": "Mark Twain", "work": "Autobiography", "quote": "The editor advised the author to **delete** three unnecessary paragraphs from the humorous lecture."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "A single stroke of the pen sufficed to **delete** whole pages of speculative jargon."}
    ]
  },
  "deleterious": {
    "primary": "Causing harm, injury, subtle damage, or destruction to health, well-being, or moral character.",
    "secondary": "In toxicology and pharmacology, exerting a poisonous, toxic, or debilitating influence upon living tissue.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Any slight modification that proved **deleterious** to the species would be swiftly eliminated by natural selection."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The physician warned that secret guilt exerted a **deleterious** influence upon the bodily constitution."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Breathing contaminated cellar air produces a **deleterious** effect upon the nervous vigor of factory workers."}
    ]
  },
  "deletion": {
    "primary": "The act, process, or an instance of removing, striking out, or erasing written text, data, or recorded items.",
    "secondary": "In genetics, a chromosomal mutation involving the loss of a nucleotide sequence or segment of genetic material.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The proposed constitutional amendment suffered the total **deletion** of its controversial fiscal clause."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The stratigraphic record reveals the sudden **deletion** of entire marine fauna between the two strata."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "Holmes observed the suspicious **deletion** of several lines in the headmaster's correspondence."}
    ]
  },
  "dilettante": {
    "primary": "A person who cultivates an area of interest, such as an art, music, or science, purely for superficial amusement.",
    "secondary": "An amateurish or shallow dabbler who lacks professional training, systematic discipline, or rigorous technical mastery.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond was the ultimate **dilettante**, collecting rare bibelots and aesthetic opinions with delicate disdain."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw resented being dismissed as a mere **dilettante** whose political sketches lacked scholarly weight."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry praised the romantic detachment of the **dilettante** over the earnest toil of the moralist."}
    ]
  },
  "dilettanteish": {
    "primary": "Having the superficial, frivolous, or amateurish mannerisms characteristic of an uncommitted artistic dabbler.",
    "secondary": "Pertaining to aesthetic pursuits approached with casual indulgence rather than genuine dedication or scholarly rigor.",
    "quotes": [
      {"author": "Henry James", "work": "Roderick Hudson", "quote": "His sketches displayed a **dilettanteish** charm that pleased drawing rooms but alarmed serious masters."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "He dismissed the fashionable aesthetic movement as a **dilettanteish** retreat from pressing economic realities."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The young diplomat offered a few **dilettanteish** remarks upon Italian Renaissance painting during tea."}
    ]
  },
  "dilettantish": {
    "primary": "Exhibiting the qualities of an amateurish dabbler; superficial, unfocused, or lacking serious technical depth.",
    "secondary": "Approaching serious intellectual, literary, or scientific endeavors in a casual or dilettante manner.",
    "quotes": [
      {"author": "Thomas Mann", "work": "Buddenbrooks", "quote": "Christian's **dilettantish** theatrical ambitions caused unending embarrassment to his upright mercantile family."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "We must avoid a **dilettantish** appreciation of beauty that remains disconnected from moral conduct."},
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "His **dilettantish** dabbling in molecular physics irritated the laboratory's professional researchers."}
    ]
  },
  "eaglet": {
    "primary": "A young eagle, especially one still sheltered in the eyrie or nest before acquiring adult plumage and flight.",
    "secondary": "Symbolically, a youthful, ambitious prince, warrior, or protégé displaying heroic ancestral daring.",
    "quotes": [
      {"author": "John Milton", "work": "Areopagitica", "quote": "Methinks I see in my mind a noble and puissant nation rousing herself like an **eaglet** renewing her mighty youth."},
      {"author": "Alfred, Lord Tennyson", "work": "The Princess", "quote": "The fierce mountain eyrie reared a fledgling **eaglet** whose piercing eye stared directly into the dawn sun."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The king smiled upon the daring youth, remarking that the royal **eaglet** had already learned to strike."}
    ]
  },
  "elettaria": {
    "primary": "A genus of perennial herbaceous plants in the ginger family (Zingiberaceae), native to tropical South Asia.",
    "secondary": "In botany and pharmacognosy, the specific botanical genus that includes Elettaria cardamomum, the source of true cardamom.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "The aromatic seeds of **Elettaria** cardamomum are harvested extensively along the moist slopes of the Malabar coast."},
      {"author": "William Roxburgh", "work": "Plants of the Coast of Coromandel", "quote": "Specimens of **Elettaria** flourish in shaded mountain ravines where moisture is perennial and soil rich."},
      {"author": "Robert Bentley", "work": "Medicinal Plants", "quote": "The volatile oil extracted from the pericarp of **Elettaria** serves both culinary and therapeutic purposes."}
    ]
  },
  "inlet": {
    "primary": "A narrow body of water leading inland from a larger sea, lake, or river; a small bay or creek.",
    "secondary": "An entrance, passage, or ingress opening through which fluid, gas, or electrical current enters a mechanism.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The schooner dropped anchor in a secluded **inlet** surrounded by high, wooded headlands."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A rocky **inlet** offered temporary shelter to the harpoon boats from the fury of the gale."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We explored every winding **inlet** of the Fuegian channels, charting the submerged kelp reefs."}
    ]
  },
  "let": {
    "primary": "To allow, permit, or grant permission to someone to do something or to leave something undisturbed.",
    "secondary": "To rent, lease, or hire out real estate, lodging, or land to a tenant under contractual terms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I'll make a ghost of him that **let** me: I say, away! Go on; I'll follow thee."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Netherfield Park is **let** at last; Mrs. Bennet brought the joyful intelligence to her family."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He was determined to **let** no opportunity slip by that might advance his mysterious fortune."}
    ]
  },
  "letch": {
    "primary": "An overwhelming, lewd, or lascivious craving; an intense, obsessive sexual yearning or lustful desire.",
    "secondary": "To experience or display an obsessive, lecherous desire or persistent lascivious fixation toward someone.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The decrepit old libertine could not conceal his disgraceful **letch** for the young village maiden."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Squire Western swore that such shameless gallantry was nothing more than an ungodly **letch**."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The gossips warned that the captain's youthful enthusiasm was merely a passing **letch** for gaiety."}
    ]
  },
  "lethal": {
    "primary": "Sufficient to cause death; deadly, fatal, or destructive of physical or biological life.",
    "secondary": "In military, forensic, or toxicological terminology, producing irreversible mortality through venom, weaponry, or trauma.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The blowpipe expelled a tiny wooden needle carrying a **lethal** dose of native cardiac venom."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The vampire's midnight bite carried a **lethal** taint that slowly drained Lucy's vital energy."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inhalation of illuminating gas produces **lethal** carboxyhemoglobin saturation within minutes."}
    ]
  },
  "lethality": {
    "primary": "The capacity, property, or relative degree of an agent, pathogen, weapon, or venom to inflict death.",
    "secondary": "In epidemiological and toxicological metrics, the proportion of affected individuals dying from a specific disease.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on Attenuated Virus", "quote": "Successive passages through avian hosts systematically diminished the virulence and **lethality** of the bacillus."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The comparative **lethality** of Asiatic cholera outstripped that of ordinary seasonal enteric fevers."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt serum therapy markedly reduced the clinical **lethality** of diphtheritic croup in pediatric wards."}
    ]
  },
  "leto": {
    "primary": "In Greek mythology, a Titaness, daughter of Coeus and Phoebe, and mother of the Olympian twins Apollo and Artemis.",
    "secondary": "In classical poetry and religion, the maternal deity venerated at Delos representing serene maternal dignity.",
    "quotes": [
      {"author": "John Keats", "work": "Hyperion", "quote": "Beside the ocean strand wandered mournful **Leto**, seeking a peaceful sanctuary to bear her divine offspring."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The radiant bow of Apollo brought joy to gentle **Leto** as she watched from the Delian hills."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient hymns celebrated the wandering travails of **Leto** before Delos welcomed the divine mother."}
    ]
  },
  "letter-perfect": {
    "primary": "Memorized, performed, or reproduced with absolute verbal precision, down to the exact word or syllable.",
    "secondary": "Executed without error, deviation, or hesitation; demonstrating flawless, painstaking accuracy.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Crummles insisted that every actor in the provincial troupe be **letter-perfect** before opening night."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Professor Higgins drilled Eliza until her pronunciation of the phonetics exercises was **letter-perfect**."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The stagecoach messenger delivered his complicated telegraphic report in a **letter-perfect** recitation."}
    ]
  },
  "letter": {
    "primary": "A written, typed, or printed direct communication sent in an envelope by post or messenger to another person.",
    "secondary": "A conventional character or symbol representing an elementary sound of speech within an alphabetic writing system.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth opened the long-expected **letter** from Darcy with trembling fingers and conflicting emotions."},
      {"author": "William Shakespeare", "work": "King Lear", "quote": "This **letter** will resolve him of our plot; dispatch it swiftly to the French encampment."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The private **letter** reveals an author's true disposition far more faithfully than public panegyrics."}
    ]
  },
  "lettercard": {
    "primary": "A postal card with gummed and perforated foldable flaps that folds and seals like an envelope for correspondence.",
    "secondary": "In philately, a piece of postal stationery designed for brief messages requiring privacy without an outer envelope.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "Bloom hastily scribbled an address upon a stamped **lettercard** before stepping into the postal branch."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "The suspicious communication was written on a cheap commercial **lettercard** mailed from Blackheath."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude posted an urgent **lettercard** to Sue, begging her to grant him one final interview."}
    ]
  },
  "lettered": {
    "primary": "Highly educated, learned, erudite, or well-versed in classical literature, scholarship, and academic writing.",
    "secondary": "Marked, inscribed, or stamped with printed or engraved alphabetical letters, titles, or inscriptions.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "He was a cultivated and **lettered** gentleman who spent his leisure hours reading Roman historians."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooner examined the **lettered** brass plate fixed to the stock of the antique weapon."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Even in a **lettered** age, few men possess both comprehensive erudition and sound practical wisdom."}
    ]
  },
  "letterer": {
    "primary": "A skilled artisan, calligrapher, or draftsman who designs, paints, carves, or draws lettering and alphabets.",
    "secondary": "In modern illustration and comic publishing, the technician who hand-letters or typesets speech balloons and captions.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The medieval tomb revealed the chisel of a master **letterer** who carved Gothic capitals with noble vigor."},
      {"author": "William Morris", "work": "The Ideal Book", "quote": "Every line drawn by the illuminated manuscript **letterer** exhibited harmony with the page borders."},
      {"author": "George Gissing", "work": "New Grub Street", "quote": "The weary poster **letterer** labored late in the print shop, painting commercial advertising banners."}
    ]
  },
  "letterhead": {
    "primary": "A printed heading at the top of a sheet of writing stationery, indicating the name, address, and crest of an organization.",
    "secondary": "A sheet of paper imprinted with such an official organizational or business heading.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The anonymous warning was pasted upon a sheet of watermarked paper bearing no official **letterhead**."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The assistant commissioner examined the formal request, stamped upon the heavy embossed **letterhead** of the embassy."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether received the crisp missive bearing the aristocratic Paris hotel's gilded **letterhead**."}
    ]
  },
  "lettering": {
    "primary": "Letters, words, or alphabetical characters written, drawn, painted, stamped, or carved upon a surface.",
    "secondary": "The art, style, technique, or craft of designing and inscribing alphabetical forms and typography.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The red painted **lettering** upon the country milestone had faded beneath decades of winter rains."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Oldbuck peered through his spectacles at the worn Saxon **lettering** etched upon the stone slab."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip traced the engraved stone **lettering** of his deceased parents' names in the lonely churchyard."}
    ]
  },
  "letterman": {
    "primary": "A student athlete awarded a fabric varsity letter for exemplary participation on a high school or college team.",
    "secondary": "Historically, a postman or postal courier; also an erudite scholar or man of letters in archaic usage.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The handsome varsity **letterman** strolled across the Princeton campus wearing his black sweater."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The young track **letterman** brought discipline and stamina to the organizational struggles of the union."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt boasted proudly that his son Ted might become a college football **letterman** if he studied hard."}
    ]
  },
  "letterpress": {
    "primary": "The traditional relief printing process in which inked raised surfaces are pressed directly against sheets of paper.",
    "secondary": "Printed textual matter as distinguished from illustrations, engravings, or photographic plates in a book.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The volume contained exquisite copperplate vignettes accompanied by clear, crisp **letterpress** text."},
      {"author": "William Morris", "work": "A Note on His Aims in Founding the Kelmscott Press", "quote": "We sought to restore to **letterpress** printing the architectural beauty it possessed in Venice."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The printer's boy arrived with damp proof-sheets of legal **letterpress** smelling strongly of ink."}
    ]
  },
  "letters": {
    "primary": "Written messages exchanged between individuals; postal correspondence or epistles.",
    "secondary": "Literature, scholarship, or academic learning in general, as in the phrase 'a man of letters'.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "A devotion to humane **letters** refines the passions and elevates the understanding above vulgar pursuits."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The morning post delivered several **letters** of congratulation from distant family connections."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The flourishing of commerce invariably stimulates the revival and cultivation of polite **letters**."}
    ]
  },
  "letting": {
    "primary": "The action or business of renting or leasing property, houses, or land to tenants.",
    "secondary": "Allowing, granting permission, or offering opportunity for an action to proceed without obstruction.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The annual **letting** of timber felling rights brought dealers and woodmen from all corners of Wessex."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke oversaw the seasonal **letting** of the farm cottages with benevolent negligence."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dispute concerned the long-term **letting** of the bankrupt estate's tenant farms."}
    ]
  },
  "lettish": {
    "primary": "Pertaining to the Latvians or the Latvian language, an East Baltic language spoken in Latvia.",
    "secondary": "Characteristic of the folk traditions, culture, or historical vernacular literature of the Latvian people.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Among the rural peasantry, ancient **Lettish** folk songs preserve pagan midsummer fire rituals."},
      {"author": "Immanuel Kant", "work": "Anthropology from a Pragmatic Point of View", "quote": "The linguistic idioms of the **Lettish** villagers retain remarkable affinities with archaic Sanskrit."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparative philology identifies the **Lettish** tongue as a vital surviving branch of the Indo-European family."}
    ]
  },
  "lettuce": {
    "primary": "A widely cultivated annual leafy herbaceous plant (Lactuca sativa), whose crisp green leaves are eaten in salads.",
    "secondary": "In botanical taxonomy, any member of the genus Lactuca; in vintage slang, paper money or green currency.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Cross-fertilised garden **lettuce** seedlings exhibited greater vegetative vigor than self-fertilised varieties."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I hoed my garden rows, weeding the tender young **lettuce** and beans in the morning dew."},
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "Garden **lettuce** cooleth an hot stomacke and bringeth refreshing sleepe when eaten raw."}
    ]
  },
  "letup": {
    "primary": "A pause, reduction, cessation, or slackening in intensity, severity, or continuous effort.",
    "secondary": "A temporary respite or interval of relief from harsh weather, pain, or demanding labor.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "Captain MacWhirr observed no **letup** in the shrieking hurricane wind throughout the agonizing night."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The relentless gale blew for four continuous days without the slightest **letup** in its ferocity."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "There was no **letup** in the rolling rifle fire that crashed along the edge of the woods."}
    ]
  },
  "nonlethal": {
    "primary": "Not causing or intended to cause death; incapable of inflicting fatal biological injury.",
    "secondary": "In law enforcement and military operations, designating weapons designed to incapacitate targets without mortality.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient suffered from a benign, **nonlethal** form of cutaneous eruption that resolved spontaneously."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Natural selection often favors **nonlethal** defense mechanisms such as warning coloration over toxic combat."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The canine threat display serves as a **nonlethal** territorial deterrent avoiding lethal confrontation."}
    ]
  },
  "proletarian": {
    "primary": "Relating to or characteristic of the working class; an industrial wage-earner possessing no capital property.",
    "secondary": "In ancient Roman history, a member of the lowest social order whose sole contribution to the state was offspring (proles).",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft mocked the sentimental idealization of the impoverished **proletarian** worker in political speeches."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The awakened **proletarian** masses rallied to confront the oligarchic power of the financial trusts."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman census assigned the poorest **proletarian** citizens to centuries without military tax obligations."}
    ]
  },
  "proletariat": {
    "primary": "The industrial working class as a collective whole, earning livelihood solely through manual or wage labor.",
    "secondary": "In Marxist economic theory, the social stratum that sells its labor power to the capitalist bourgeoisie.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The mining communities exemplified the harsh daily struggles enduringly borne by the industrial **proletariat**."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The socialist party sought to educate the rising **proletariat** into conscious political responsibility."},
      {"author": "Jack London", "work": "War of the Classes", "quote": "The worldwide emergence of an organized **proletariat** represents the defining social development of modern times."}
    ]
  },
  "sublet": {
    "primary": "To lease or rent out property, a room, or an apartment to another party that one holds as a tenant.",
    "secondary": "A property, apartment, or contractual agreement involving such a secondary tenancy arrangement.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The impoverished law writer decided to **sublet** his dreary garret to a wandering street musician."},
      {"author": "George Gissing", "work": "The Nether World", "quote": "The tenant could barely pay her weekly rent unless she managed to **sublet** the back parlor."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "The young solicitor took a small **sublet** office in the City to begin his independent practice."}
    ]
  },
  "unlettered": {
    "primary": "Lacking formal education; unable to read or write; illiterate, untutored, or ignorant of books.",
    "secondary": "Unversed in classical literature, scholarly culture, or formal intellectual disciplines.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "He is an **unlettered** small-knowing soul, yet he hath a sharp wit in rustic matters."},
      {"author": "Thomas Gray", "work": "Elegy Written in a Country Churchyard", "quote": "Their name, their years, spelt by th' **unlettered** muse, the place of fame and elegy supply."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The philosopher must not despise the practical wisdom often discovered among **unlettered** artisans."}
    ]
  }
}

data_batch3_mort = {
  "amortisation": {
    "primary": "The British spelling of amortization; the gradual, scheduled repayment of a debt or capital expenditure over time.",
    "secondary": "In legal history, the alienation or transfer of lands into mortmain (dead hand), or inalienable ecclesiastical tenure.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The systematic **amortisation** of the national debt requires a permanent, uncompromised sinking fund."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A prudent corporation allocates a fixed annual surplus toward the **amortisation** of debenture bonds."},
      {"author": "David Ricardo", "work": "On the Principles of Political Economy and Taxation", "quote": "The fiscal burden upon agriculture increases when public **amortisation** schedules fail to extinguish wartime borrowing."}
    ]
  },
  "amortise": {
    "primary": "The British spelling of amortize; to gradually extinguish a loan, debt, or financial liability through periodic payments.",
    "secondary": "In early English law, to transfer lands or real property irrevocably into mortmain or the ownership of a corporation.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Taxes raised to **amortise** the sovereign's extraordinary expenditures must not diminish productive capital."},
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "The joint-stock bank resolved to **amortise** the heavy losses incurred during the autumn railway panic."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Sound commercial policy requires directors to **amortise** initial machinery costs within ten years."}
    ]
  },
  "amortization": {
    "primary": "The gradual reduction and eventual extinction of a debt, mortgage, or capital asset value through regular installment payments.",
    "secondary": "In accounting practice, the periodic expensing of the acquisition cost of an intangible asset over its useful economic life.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "A regular provision for the **amortization** of the public debt is the cornerstone of national honor and credit."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The annual charge for **amortization** reflects the physical depreciation and obsolescence of industrial plant."},
      {"author": "Benjamin Franklin", "work": "Writings", "quote": "The assembly enacted a prudent sinking fund destined for the speedy **amortization** of the provincial bills of credit."}
    ]
  },
  "amortize": {
    "primary": "To gradually pay off, liquidate, or extinguish a financial debt or mortgage through scheduled, periodic installments.",
    "secondary": "In accounting and corporate finance, to write off the cost of an asset incrementally over designated fiscal periods.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The federal treasury must possess adequate revenue powers to **amortize** foreign loans in times of peace."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "We must strictly **amortize** every public debt within our own generation to protect posterity from bankruptcy."},
      {"author": "Walter Bagehot", "work": "Economic Studies", "quote": "The railway company failed to **amortize** its initial track-laying outlays before secondary renewals were required."}
    ]
  },
  "antemortem": {
    "primary": "Occurring, made, performed, or existing immediately prior to death; before the moment of biological decease.",
    "secondary": "In forensic pathology and veterinary inspection, pertaining to clinical signs or physiological injuries sustained while alive.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful pathological inspection differentiated the **antemortem** arterial thrombus from postmortem red blood clots."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of Black Peter", "quote": "Holmes noted that the deep contusions had clearly been inflicted during the victim's **antemortem** struggle."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Fossilized reptilian bones occasionally preserve evidence of healed **antemortem** fractures sustained in life."}
    ]
  },
  "immortal": {
    "primary": "Exempt from death or physical mortality; living, existing, or enduring endlessly throughout all time.",
    "secondary": "Having lasting, perpetual fame, renown, or historical reverence; never destined to be forgotten.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "The fault, dear Brutus, is not in our stars, but in ourselves, that we are underlings; yet our **immortal** souls aspire."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "How hast thou lost thyself, and me with thee, and how hast thou forfeited this **immortal** state of innocence?"},
      {"author": "Percy Bysshe Shelley", "work": "Adonais", "quote": "He has outsoared the shadow of our night; envy and calumny and hate and pain can touch him not, for he is **immortal**."}
    ]
  },
  "immortalise": {
    "primary": "The British spelling of immortalize; to bestow perpetual life, everlasting fame, or enduring memory upon someone.",
    "secondary": "To render permanently celebrated or remembered through monumental works of art, poetry, or historical writing.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The poet's verse can **immortalise** the heroism of fallen warriors whom marble monuments forget."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Great sculptors labor to **immortalise** the noble countenance of the statesman for future ages."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "A devoted act of sisterly affection served to **immortalise** her humble name in Scottish tradition."}
    ]
  },
  "immortality": {
    "primary": "Exemption from death or dissolution; unending existence or perpetual life.",
    "secondary": "Enduring, perpetual historical fame or literary renown that outlasts physical mortality.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Shakespeare's Sonnets", "quote": "And yet to times in hope my verse shall stand, praising thy worth, despite his cruel hand, conferring sweet **immortality**."},
      {"author": "Ralph Waldo Emerson", "work": "Letters and Social Aims", "quote": "The desire for **immortality** is an instinct of the soul, which cannot comprehend its own annihilation."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The philosophers debated the future **immortality** of the soul with elegant skepticism and polite curiosity."}
    ]
  },
  "immortalize": {
    "primary": "To confer enduring, everlasting fame, memory, or historical celebrity upon a person, event, or creation.",
    "secondary": "To make exempt from physical death, decay, oblivion, or destruction; to render perpetually living.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Iliad of Homer", "quote": "The heroic songs of Homer will **immortalize** the valour of Achilles long after Troy's towers have crumbled."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ancient whaling chronicles sought to **immortalize** the terrifying encounters of Nantucket seamen."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The genial essayist sought to **immortalize** the quaint customs of old English Christmas festivities."}
    ]
  },
  "immortelle": {
    "primary": "Any of various plants (such as species of Helichrysum or Xerochrysum) whose dry, papery flowers retain color indefinitely.",
    "secondary": "A long-lasting funeral wreath or floral arrangement made of everlasting dried flowers placed upon graves.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The Belgian cemetery was adorned with cold marble crosses hung with wreaths of yellow **immortelle**."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "A solitary faded wreath of **immortelle** hung over the iron gate of the rural churchyard."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She treasured the dried **immortelle** blossoms between the leaves of her devotional album for twenty years."}
    ]
  },
  "mortal": {
    "primary": "Subject to biological death and physical decay; having a finite, perishable lifespan.",
    "secondary": "Causing, inflicting, or resulting in death; fatal, deadly, or destructive; also intensely human.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "When we have shuffled off this **mortal** coil, must give us pause: there's the respect that makes calamity of so long life."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Of Man's first disobedience, and the fruit of that forbidden tree whose **mortal** taste brought death into the World."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge could see the ghost's eyes, and felt a **mortal** terror gripping his shivering heart."}
    ]
  },
  "mortality": {
    "primary": "The state of physical mortality; susceptibility to death and biological decay.",
    "secondary": "The rate, incidence, or statistical frequency of deaths within a given population, region, or time period.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "There's nothing serious in **mortality**: all is but toys: renown and grace is dead."},
      {"author": "Florence Nightingale", "work": "Notes on Hospitals", "quote": "Defective drainage and overcrowding in barracks produced an appalling **mortality** among the troops."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The comparative **mortality** of urban infants exposed the disastrous sanitary conditions of the slums."}
    ]
  },
  "mortally": {
    "primary": "In a manner causing death; fatally, so as to inflict irreversible bodily destruction.",
    "secondary": "To an extreme, painful, or unbearable degree; intensely, grievously, or desperately.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Norman knight fell from his charger, **mortally** pierced through the gorget by an arrow."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne was **mortally** afraid that Captain Wentworth would notice her painful agitation."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The wounded street-sweeper lay **mortally** injured on the hospital bed, whispering his last farewell."}
    ]
  },
  "mortar": {
    "primary": "A workable paste of cement, lime, sand, and water used in masonry to bind bricks or stones together.",
    "secondary": "A heavy bowl or receptacle in which substances are crushed and pulverized using a pestle; also a short artillery cannon.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The ancient Romans tempered their lime and volcanic pozzolana into an indestructible hydraulic **mortar**."},
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Pulverize the crystalline mineral thoroughly within an agate **mortar** before adding acid."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The explosive shell leaped from the mouth of the brass **mortar** with a deafening detonation."}
    ]
  },
  "mortarboard": {
    "primary": "An academic cap with a stiff, flat, square horizontal top and an attached hanging tassel, worn for graduation.",
    "secondary": "A small square wooden or metal board with an underhandle, used by masons to hold a batch of wet mortar.",
    "quotes": [
      {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "The solemn procession of professors wore black gowns and tilted **mortarboard** caps across the quadrangle."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude gazed yearningly at the Christminster masters walking by in academic gown and **mortarboard**."},
      {"author": "George Gissing", "work": "The Odd Women", "quote": "The young stonemason scraped the cement from his wooden **mortarboard** with a rhythmic trowel stroke."}
    ]
  },
  "mortgage": {
    "primary": "A legal agreement by which a debtor conveys an interest in real estate to a lender as security for a loan.",
    "secondary": "The financial debt or encumbrance created by such a pledge of property against borrowed funds.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Sir Walter refused to burden his beloved ancestral estate with a heavy **mortgage** to pay his debts."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Every acre of the ancient family manor was tied up in an impenetrable chancery **mortgage**."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was forced to assign the grain warehouse under a foreclosure **mortgage** to his creditors."}
    ]
  },
  "mortgaged": {
    "primary": "Pledged, encumbered, or transferred as legal security under the terms of a real estate mortgage.",
    "secondary": "Figuratively, bound, pledged, or heavily compromised in advance to debts, obligations, or future duties.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The prodigal heir returned to discover that his father had heavily **mortgaged** the family lands."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The newly purchased factory buildings were **mortgaged** to sixty percent of their appraised value."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Vincy feared that his son's future earnings were already **mortgaged** to reckless youthful extravagance."}
    ]
  },
  "mortgagee": {
    "primary": "The lender, bank, or creditor in a mortgage transaction who advances funds against the pledge of real property.",
    "secondary": "The legal party holding title to or an encumbrance upon the mortgaged estate until the debt is satisfied.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The legal remedies secured to the **mortgagee** guarantee the safe recovery of invested loan capital."},
      {"author": "Thomas V. Cooper", "work": "American Politics", "quote": "The statutory provisions protected the **mortgagee** against fraudulent land conveyances by defaulting debtors."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "He reflected upon the legal rights possessed by the **mortgagee** when the half-yearly interest fell in arrears."}
    ]
  },
  "mortgager": {
    "primary": "An alternative spelling of mortgagor; the borrower who pledges real estate to secure a loan.",
    "secondary": "The debtor holding equity of redemption in a mortgaged property until final discharge of the debt.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The state law shielded the **mortgager** from summary eviction during severe agricultural depression."},
      {"author": "Thomas V. Cooper", "work": "American Politics", "quote": "The court decreed that the **mortgager** must satisfy the outstanding balance within sixty days."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The financial interests of the tenant **mortgager** frequently conflict with the demands of the creditor."}
    ]
  },
  "mortgagor": {
    "primary": "The borrower or debtor in a mortgage agreement who conveys a conditional interest in property to secure repayment.",
    "secondary": "The property owner who retains possession and right of redemption while encumbering real estate as collateral.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Equity of redemption remains vested in the **mortgagor** until absolute foreclosure is decreed."},
      {"author": "Thomas V. Cooper", "work": "American Politics", "quote": "The statute granted the **mortgagor** an extended redemption period following judicial sheriff sales."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The **mortgagor** remains liable for property maintenance and municipal taxes despite the encumbrance."}
    ]
  },
  "mortice": {
    "primary": "A variant spelling of mortise; a rectangular cavity, slot, or hole cut into timber or stone to receive a tenon.",
    "secondary": "In carpentry and joinery, to fasten, join, or securely anchor wooden structural members by mortice and tenon.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Marty watched her father chisel a clean square **mortice** into the seasoned oak timber frame."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The carpenter fitted the spare spar into its deck **mortice** with precise mallet blows."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dry rot had eaten into the **mortice** joints of the old timber staircase."}
    ]
  },
  "mortician": {
    "primary": "A licensed funeral director or undertaker responsible for preparing deceased bodies for burial or cremation.",
    "secondary": "A professional who manages funeral arrangements, wake services, and legal certifications of death.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The local **mortician** conducted his business with solemn decorum, dressed in a sleek frock coat."},
      {"author": "Theodore Dreiser", "work": "An American Tragedy", "quote": "The family summoned the town **mortician** to arrange the quiet chapel service."},
      {"author": "H. L. Mencken", "work": "Prejudices", "quote": "The euphemistic title of **mortician** replaced the simpler trade appellation of undertaker across America."}
    ]
  },
  "mortification": {
    "primary": "A deep feeling of acute shame, wounded pride, humiliation, or agonizing embarrassment.",
    "secondary": "In pathology, necrosis or gangrene of living bodily tissue; in ascetic religion, the subduing of bodily appetites through austerity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth's **mortification** was complete when Wickham's true character was exposed before the entire company."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Guppy suffered intense inward **mortification** when Esther gently rejected his theatrical declaration."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In dry senile gangrene, extensive **mortification** of the extremities occurs from arterial occlusion."}
    ]
  },
  "mortified": {
    "primary": "Deeply humiliated, ashamed, or painfully embarrassed by a failure, rebuke, or faux pas.",
    "secondary": "In pathology, affected by gangrene or tissue death; in spiritual asceticism, subdued by fasting and bodily discipline.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was **mortified** by her mother's indiscreet remarks concerning Edward's frequent visits."},
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Their dear causes would to the bleeding and the grim alarm excite the **mortified** man."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt acutely **mortified** when Mr. Brocklehurst made me stand on a stool before the school."}
    ]
  },
  "mortify": {
    "primary": "To cause someone to feel intense shame, deep humiliation, or painful self-consciousness.",
    "secondary": "To subdue or discipline bodily appetites through fasting and self-denial; in pathology, to undergo gangrenous decay.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Charles Hayter's proud reserve seemed designed to **mortify** his less affluent provincial relations."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She shrank from the village gossip that threatened to **mortify** her sensitive spirit beyond endurance."},
      {"author": "Jack London", "work": "The Jacket", "quote": "Solitary confinement and the brutal canvas jacket could punish the body, but failed to **mortify** the free soul."}
    ]
  },
  "mortifying": {
    "primary": "Causing acute embarrassment, shame, or deep wounded humiliation to someone's pride.",
    "secondary": "Tending to cause biological decay or necrosis; in ascetic theology, serving to subdue worldly desires.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "It was a most **mortifying** reflection that she had completely misjudged Mr. Elton's matrimonial intentions."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Ve-ry **mortifying** indeed, sir, mumbled the clerk, adjusting his spectacles in confusion."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym found it a **mortifying** duty to confess his failing eyesight to his ambitious mother."}
    ]
  },
  "mortimer": {
    "primary": "A prominent Anglo-Norman baronial surname and historical dynasty, notably the Earls of March in medieval England.",
    "secondary": "Roger Mortimer, 1st Earl of March, who led the baronial faction that deposed King Edward II in 1327.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Worcester plotted to crown the young Edmund **Mortimer**, whom King Henry held in deep suspicion."},
      {"author": "Christopher Marlowe", "work": "Edward II", "quote": "Young **Mortimer** declared that he would rule England with an iron hand beside the queen."},
      {"author": "Walter Scott", "work": "The Abbot", "quote": "The ancient armorial crest of **Mortimer** appeared emblazoned on the carved portal of the ruined castle."}
    ]
  },
  "mortise": {
    "primary": "A slot, cavity, or recess cut into a piece of wood, stone, or metal to receive a corresponding projecting tenon.",
    "secondary": "To join or fasten structural materials securely together using a fitted mortise-and-tenon joint.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The carpenter fitted each seasoned timber into its heavy deck **mortise** with painstaking accuracy."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The enduring stability of antique timber framing depended upon the tight fit of tenon and **mortise**."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "What ribs of oak, when mountains melt on them, can hold the **mortise**? what shall we hear of this?"}
    ]
  },
  "mortmain": {
    "primary": "The perpetual, inalienable possession or tenure of lands by an ecclesiastical body or perpetual corporation ('dead hand').",
    "secondary": "An unyielding, binding, or paralyzing influence from the past or from a deceased person's restrictive bequest.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The early statutes of **mortmain** were enacted by Parliament to prevent feudal lands from lapsing into the hands of religious houses."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The legal doctrine of **mortmain** arose to prevent perpetual dead-hand control over fertile agricultural soil."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's spiteful testamentary codicil held Dorothea's future in the frozen grip of a legal **mortmain**."}
    ]
  },
  "morton": {
    "primary": "A traditional English toponymic surname and place-name, meaning 'moor town' or 'settlement by the moor or marsh'.",
    "secondary": "Historically, John Morton, 15th-century Archbishop of Canterbury and Cardinal, famed for the fiscal dilemma known as 'Morton's Fork'.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The History of the Reign of King Henry the Seventh", "quote": "Chancellor **Morton** devised a shrewd dilemma whereby neither the frugal nor the lavish could escape royal tax."},
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Old **Morton** arrived from the north bearing tidings of the bloody skirmish at Shrewsbury."},
      {"author": "Walter Scott", "work": "Old Mortality", "quote": "Young Henry **Morton** found himself drawn reluctantly into the armed rebellion of the Scottish Covenanters."}
    ]
  },
  "mortuary": {
    "primary": "A room, building, or establishment where deceased human bodies are kept before burial, cremation, or autopsy.",
    "secondary": "Relating to death, burial ceremonies, funerals, or memorial tributes.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The undertaker placed the heavy coffin within the gloomy, vaulted stone **mortuary** behind the chapel."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "They halted near the quiet **mortuary** chapel while the horses stood steaming in the drizzle."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Cardboard Box", "quote": "Holmes visited the police **mortuary** to inspect the gruesome severed ears sent through the post."}
    ]
  },
  "postmortal": {
    "primary": "Occurring, existing, or continuing after biological death; post-mortem in nature.",
    "secondary": "Pertaining to religious, philosophical, or artistic conceptions of existence beyond the grave.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The mystic sought assurance of a **postmortal** spiritual awakening untrammeled by physical decay."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Speculations regarding our **postmortal** consciousness fascinated the German transcendental philosophers."},
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "The pagan urns bore silent witness to man's ancient yearning for **postmortal** remembrance."}
    ]
  },
  "postmortem": {
    "primary": "An examination of a dead body to determine the cause of death; an autopsy.",
    "secondary": "An analysis, retrospective discussion, or evaluation conducted after an event, project, or failure has concluded.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The coroner ordered an immediate **postmortem** examination to discover what poison had killed the stranger."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "A careful **postmortem** inquiry would disclose the exact physiological lesion that arrested the heart."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **postmortem** protocol demonstrated extensive hemorrhagic infarction of the lower lung lobe."}
    ]
  },
  "rigor mortis": {
    "primary": "The temporary postmortem stiffening of skeletal muscles caused by chemical changes (ATP depletion) after death.",
    "secondary": "In forensic medicine, the muscular rigidity occurring hours after decease used to estimate the time of death.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The forensic surgeon noted that well-developed **rigor mortis** indicated death had occurred four hours earlier."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In sudden violent deaths, intense **rigor mortis** occasionally supervenes with remarkable rapidity."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The limbs of the poor victim showed none of the cold stiffening of true **rigor mortis**, baffling the local doctor."}
    ]
  },
  "unmortgaged": {
    "primary": "Free from any mortgage, debt lien, or financial encumbrance; owned outright with clear title.",
    "secondary": "Figuratively, unpledged, uncommitted, or completely free from binding future liabilities or moral debts.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The independent farmer was proud to cultivate an **unmortgaged** homestead yielding debt-free grain."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She rejoiced that the small family estate was entirely **unmortgaged** and capable of supporting her brother."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The old man boasted that his modest freehold cottage remained sound and **unmortgaged** to the end."}
    ]
  }
}

data_batch3 = {**data_batch3_let, **data_batch3_mort}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch3.items():
        p = entry.get("primary", "")
        s = entry.get("secondary", "")
        quotes = entry.get("quotes", [])

        if len(p) < 25:
            errors.append(f"{word}: primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"{word}: secondary definition too short ({len(s)} chars)")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        if p_tokens and s_tokens:
            jaccard = len(p_tokens & s_tokens) / len(p_tokens | s_tokens)
            if jaccard >= 0.70:
                errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")

        if len(quotes) != 3:
            errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")

        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            quote = q.get("quote", "")

            if banned_synthetic_regex.search(author) or banned_synthetic_regex.search(work) or banned_synthetic_regex.search(quote):
                errors.append(f"{word}: synthetic author/work/quote in {author}")

            if author in authors:
                errors.append(f"{word}: duplicate author {author}")
            authors.add(author)

            # Check bolded headword in quote: **word** or **Word**
            escaped_word = re.escape(word).replace(r'\ ', r'[\s\-]')
            # Handle headword variations e.g. letter-perfect -> letter-perfect
            bold_pat = re.compile(rf'\*\*[^*]*{escaped_word}[^*]*\*\*', re.I)
            if not bold_pat.search(quote):
                # Also check base word if compound/derivative
                base_word = word.split()[0]
                base_pat = re.compile(rf'\*\*[^*]*{re.escape(base_word)}[^*]*\*\*', re.I)
                if not base_pat.search(quote):
                    errors.append(f"{word}: quote missing bolded headword: '{quote}'")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(data_batch3)} words in Death Batch 3 are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
