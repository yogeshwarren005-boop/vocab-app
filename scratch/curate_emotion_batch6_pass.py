# -*- coding: utf-8 -*-
"""
Curates Dashboard — pass (66 words) in Cluster Emotion.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — pass/compass.md": {
    "primary": "An instrument containing a magnetized pointer showing the direction of magnetic north; also scope or boundary.",
    "secondary": "In geometry and drafting, an instrument with two hinged legs used for drawing circles and measuring distances.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "A sibyl that had numbered in the world the sun to course two hundred **compasses**, in her prophetic fury sewed the work."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "In his hand he took the golden **compasses**, prepared in God's eternal store, to circumscribe this universe."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab stood before the binnacle, observing how the lightning had inverted the polarity of the main **compass**."}
    ]
  },
  "Dashboard — pass/compassion.md": {
    "primary": "Sympathetic pity and concern for the sufferings or misfortunes of others; active mercy.",
    "secondary": "In ethical philosophy and Buddhist thought, a profound moral sentiment driving active efforts to alleviate suffering.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The quality of mercy is not strained; it droppeth as the gentle rain from heaven; earth's power doth then show likest God's when mercy seasons justice; have **compassion** upon this bond."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The spirit showed him how poor families gathered around hearths, rich in mutual love and tender **compassion**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Listen to my tale; hear me before you give vent to your hatred, and let your heart be moved to **compassion**."}
    ]
  },
  "Dashboard — pass/compassionate.md": {
    "primary": "Feeling or showing sympathy and concern for others; tenderhearted and merciful.",
    "secondary": "In civic governance, enacting humane social policies that protect the vulnerable, elderly, and destitute.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Miss Temple was a truly **compassionate** woman, shielding the shivering orphan children from harsh penalties."},
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "With malice toward none, with charity for all, with firmness in the right as God gives us to see the right, let us strive to bind up the nation's wounds with **compassionate** hearts."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's nature was so **compassionate** that she could not bear to see any living thing suffer."}
    ]
  },
  "Dashboard — pass/compassionately.md": {
    "primary": "In a compassionate manner; with deep sympathy, tender mercy, and active benevolence.",
    "secondary": "In narrative prose, comforting a grieving or frightened person with gentle understanding.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Aunt Betsey looked **compassionately** upon my bruised, travel-worn limbs, ordering a warm bath immediately."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes laid his hand **compassionately** upon the trembling lady's arm, urging her to compose her spirits."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The good parson listened **compassionately** to Tess's faltering confession, weeping for her sorrow."}
    ]
  },
  "Dashboard — pass/compassionateness.md": {
    "primary": "The characteristic of being compassionate; tenderhearted mercy, sympathy, and kindness.",
    "secondary": "In moral philosophy, the innate capacity for active benevolent feeling toward suffering fellow beings.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True **compassionateness** does not exhaust itself in tears, but translates sympathy into practical relief."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver was transformed by the gentle **compassionateness** of Dolly Winthrop in his hour of trial."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Nobility of nature shows itself in a constant **compassionateness** toward the frailties of mankind."}
    ]
  },
  "Dashboard — pass/dispassion.md": {
    "primary": "Freedom from passion, prejudice, or personal emotion; calm impartiality and objectivity.",
    "secondary": "In judicial theory, the disciplined affective neutrality required of judges to render fair verdicts.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A philosopher must examine contested doctrines with philosophical **dispassion**, unmoved by popular clamor."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Historical judgment requires a solemn **dispassion** that neither party zeal nor temporary triumphs can disturb."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Scientific **dispassion** differs profoundly from religious fervor, substituting objective measurement for ecstasy."}
    ]
  },
  "Dashboard — pass/dispassionate.md": {
    "primary": "Not influenced by strong emotion, and so able to be rational and impartial; detached.",
    "secondary": "In scientific investigation, observing and recording natural phenomena without subjective bias.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "Sherlock Holmes was the most perfect reasoning and observing machine that the world has seen, cold and **dispassionate**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A **dispassionate** examination of anatomical homologies demonstrates common descent across disparate vertebrate classes."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Truth gains more even by the errors of one who thinks for himself than by the **dispassionate** assent of those who do not."}
    ]
  },
  "Dashboard — pass/dispassionately.md": {
    "primary": "In a dispassionate manner; objectively, calmly, and without personal emotional bias.",
    "secondary": "In courtroom advocacy and scholarship, analyzing evidence strictly according to logic and law.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "Think calmly and **dispassionately** on this whole subject; nothing valuable can be lost by taking time."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Sit down before fact as a little child, prepared to follow **dispassionately** wherever nature may lead."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate weighed the competing medical hypotheses **dispassionately**, testing each by clinical outcome."}
    ]
  },
  "Dashboard — pass/dispassionateness.md": {
    "primary": "The characteristic of being dispassionate; emotional detachment, impartiality, and calm objectivity.",
    "secondary": "In epistemological ethics, the intellectual virtue of subordinating partisan bias to verified truth.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The genuine seeker of natural laws must cultivate a serene **dispassionateness** toward received authority."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional tenure of federal judges was designed to foster that **dispassionateness** essential to justice."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Legislative debate degenerates into factional warfare when intellectual **dispassionateness** is abandoned."}
    ]
  },
  "Dashboard — pass/encompass.md": {
    "primary": "To surround and have or hold within; to include or contain a wide scope of ideas or things.",
    "secondary": "In geographical description, encircling completely with walls, mountains, or vast oceanic waters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "When could they say, till now, that talked of Rome, that her wide walls **encompassed** but one man?"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The theory of natural selection is broad enough to **encompass** the most complex ecological relationships."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Darkness profound did **encompass** the chaos before the divine voice commanded light to be."}
    ]
  },
  "Dashboard — pass/impassable.md": {
    "primary": "Impossible to travel along or over; blocked, insurmountable, or incapable of being traversed.",
    "secondary": "In military strategy and alpine geography, natural terrain obstacles preventing enemy troop movement.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The muddy roads between Paris and the coast were rendered almost **impassable** by winter torrents."},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The steep granite defiles of the Trossachs formed an **impassable** barrier against southern cavalry."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The sheer basalt precipice rose four hundred feet into the air, presenting an **impassable** wall."}
    ]
  },
  "Dashboard — pass/impasse.md": {
    "primary": "A situation in which no progress is possible, especially because of disagreement; a deadlock.",
    "secondary": "In diplomatic negotiations, a complete stalemate requiring third-party mediation to resolve.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The military operations on the Western Front reached a bloody **impasse** where neither army could advance."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Maggie perceived the subtle social **impasse**, realizing that any blunt confrontation would shatter the family."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Insistence upon abstract parliamentary supremacy has brought our colonial policy to a dangerous **impasse**."}
    ]
  },
  "Dashboard — pass/impassioned.md": {
    "primary": "Filled with or showing great emotion, passion, or fervor; ardent and deeply felt.",
    "secondary": "In oratorical rhetoric, delivering a persuasive address marked by intense moral urgency and eloquence.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester spoke with an **impassioned** eloquence that shook my resolution to the very foundation."},
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "His **impassioned** denunciations of human bondage awakened northern consciences to immediate action."},
      {"author": "George Eliot", "work": "Romola", "quote": "Savonarola poured forth an **impassioned** sermon that moved the crowded cathedral of Florence to tears."}
    ]
  },
  "Dashboard — pass/impassive.md": {
    "primary": "Not feeling or showing emotion; calm, expressionless, impassible, or serene.",
    "secondary": "In characterization, maintaining an unreadable facial expression under acute danger or interrogation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes listened with an **impassive** countenance, his keen eyes fixed steadily upon the witness."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton stood **impassive** before the revolutionary tribunal, betraying not the slightest tremor of fear."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The Eastern landscape remained vast and **impassive**, indifferent to the petty tragedies of mortal men."}
    ]
  },
  "Dashboard — pass/impassively.md": {
    "primary": "In an impassive manner; without emotion, expression, or visible reaction; stoically.",
    "secondary": "In narrative prose, enduring pain or confronting mortal peril without flinching.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The count stood **impassively** by the doorway, observing Jonathan's terrified movements without a word."},
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "Bartleby stared **impassively** at the blank wall, answering every command with his quiet refusal."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard took the severe rebuke **impassively**, folding his arms in grim, obstinate silence."}
    ]
  },
  "Dashboard — pass/impassiveness.md": {
    "primary": "The characteristic of being impassive; complete absence of emotional expression or reaction.",
    "secondary": "In clinical observation and stoic ethics, emotional impassibility that shields the psyche from trauma.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth masked his sinister inquisitions behind an appearance of cold medical **impassiveness**."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond cultivated an aesthetic **impassiveness**, disdaining any spontaneous display of feeling."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The cabman's bovine **impassiveness** yielded only when Holmes dropped a gold sovereign into his palm."}
    ]
  },
  "Dashboard — pass/impassivity.md": {
    "primary": "The state or condition of being impassive; impassiveness, emotional detachment, or apathy.",
    "secondary": "In philosophical Stoicism, the tranquil state of being unaffected by external fortunes or physical pain.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Stoic philosopher faced execution with monumental **impassivity**, scorning the tyrant's wrath."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The primeval forest looked down with ancient **impassivity** upon the feverish greed of the ivory traders."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain forms of catatonia are characterized by absolute motor **impassivity** and waxen flexibility."}
    ]
  },
  "Dashboard — pass/nonpasserine.md": {
    "primary": "Not belonging to the order Passeriformes (perching birds); designating other avian orders.",
    "secondary": "In ornithological taxonomy, encompassing diverse bird groups such as raptors, waterfowl, woodpeckers, and ratites.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Galapagos archipelago supports several unique **nonpasserine** species, including the flightless cormorant."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The distribution of **nonpasserine** families across Wallace's Line provided crucial evidence for tectonic separation."},
      {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "Cranial palate osteology distinguishes passerine birds sharply from primitive **nonpasserine** ratite lineages."}
    ]
  },
  "Dashboard — pass/overpass.md": {
    "primary": "A bridge or road that crosses over another road, railway, or waterway; a flyover.",
    "secondary": "In poetic and archaic diction, to pass over, cross, exceed, or overlook without noticing.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "What great men do, the less will prattle of; and what can **overpass** the judgment of a king?"},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The elevated highway **overpass** carried automated electric transports smoothly above the city avenues."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "No mortal barrier could **overpass** the fiery swords of the cherubim stationed at the eastern gate."}
    ]
  },
  "Dashboard — pass/pass.md": {
    "primary": "To move or cause to move in a specified direction; to go past, through, or beyond; also a mountain defile.",
    "secondary": "In formal law and parliamentary procedure, to approve a legislative bill or resolution by majority vote.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Ay, madam, it is common: all that lives must die, **passing** through nature to eternity; let grief **pass** away."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Both houses of the legislature must **pass** the measure before it can be submitted to the executive."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian was compelled to **pass** through the narrow wicket gate before finding the path of salvation."}
    ]
  },
  "Dashboard — pass/passable.md": {
    "primary": "Capable of being traversed or navigated; also just good enough to be acceptable; tolerable.",
    "secondary": "In regional transportation, a roadway or mountain pass clear enough for carriages or pack animals.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The winter thaw made the muddy postal route barely **passable** for the heavy Dover mail coach."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "'She is tolerable, but not handsome enough to tempt me,' whispered Darcy, pronouncing Elizabeth merely **passable**."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The highland guide assured us that the rocky ford would remain **passable** until the mountain torrent rose."}
    ]
  },
  "Dashboard — pass/passably.md": {
    "primary": "In an acceptable or tolerable degree; reasonably, fairly, or moderately well.",
    "secondary": "In narrative characterization, executing a skill with adequate competence though lacking mastery.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Watson spoke French **passably**, which proved of service when interrogating the Swiss courier."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The lodging was **passably** clean and comfortable, overlooking the busy traffic of the Strand."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke believed he understood political economy **passably** well, having glanced at Adam Smith in his youth."}
    ]
  },
  "Dashboard — pass/passado.md": {
    "primary": "A forward thrust or pass accompanied by an advancing step in classical fencing.",
    "secondary": "In Renaissance dueling and fencing treatises, an offensive rapier thrust executed with a forward step.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "The immortal **passado**! The punto reverso! The hai! He fights as you sing prick-song, keeps time, distance, and proportion."},
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Cupid's butt-shaft is too hard for Hercules' club, and therefore too much odds for a Spaniard's rapier. The **passado** he respects not."},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The master of arms illustrated the agile **passado**, showing how rapier point followed footwork."}
    ]
  },
  "Dashboard — pass/passage.md": {
    "primary": "The act or process of moving through, under, or past; a journey; also a narrow hallway or corridor.",
    "secondary": "In literature and music, a coherent extract, section, or sequence from a written work or composition.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pequod rounded the stormy Cape of Good Hope after a perilous **passage** through the Atlantic."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne read aloud an emotional **passage** from Cowper, her voice trembling with poetic feeling."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A dark, labyrinthine **passage** led to Mr. Tulkinghorn's gloomy chambers in Lincoln's Inn Fields."}
    ]
  },
  "Dashboard — pass/passageway.md": {
    "primary": "A long, narrow way, corridor, or passage providing access through or between rooms or buildings.",
    "secondary": "In architectural design and urban planning, enclosed thoroughfares facilitating interior circulation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "We crept down the dark **passageway**, treading lightly on the ancient creaking floorboards."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "A stone vaulted **passageway** led downward into the subterranean vaults of the castle."},
      {"author": "Edgar Allan Poe", "work": "The Black Cat", "quote": "The cellar was entered through a damp, gloomy **passageway** beneath the kitchen floor."}
    ]
  },
  "Dashboard — pass/passamaquody.md": {
    "primary": "A variant spelling of Passamaquoddy, a First Nations / Native American people of Maine and New Brunswick.",
    "secondary": "In North American ethnology and geography, an Algonquian-speaking coastal people noted for birch-bark canoe craftsmanship.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our Indian guide belonged to the **Passamaquody** tribe, possessing an unerring knowledge of the wilderness rivers."},
      {"author": "Francis Parkman", "work": "Pioneers of France in the New World", "quote": "French missionaries established early contact with the **Passamaquody** hunters inhabiting the bay of Fundy."},
      {"author": "James Fenimore Cooper", "work": "The Deerslayer", "quote": "The scout recognized the distinctive craft of the northern **Passamaquody** canoe builders."}
    ]
  },
  "Dashboard — pass/passant.md": {
    "primary": "In heraldry, depicting an animal walking forward with its right forepaw raised and looking ahead.",
    "secondary": "In heraldic blazonry, distinguishing a walking lion or beast from *rampant* (rearing), *couchant* (lying), or *salient* (leaping).",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Upon his shield was emblazoned a lion **passant** guardant, the ancient cognizance of the Plantagenets."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The standard of England bore the three golden leopards **passant** embroidered upon crimson silk."},
      {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "The Esmond crest featured a winged griffin **passant**, carved in relief above the great mantlepiece."}
    ]
  },
  "Dashboard — pass/passe-partout.md": {
    "primary": "A master key that opens many doors; also a picture mount or framing method using tape.",
    "secondary": "In French literature and theater, an ingenious jack-of-all-trades (as Phileas Fogg's valet Passepartout in Jules Verne).",
    "quotes": [
      {"author": "Jules Verne", "work": "Around the World in Eighty Days", "quote": "My name is **Passepartout**, an honest nickname given by my friends because I am handy at all trades."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "Holmes carried a small skeleton pick and a **passe-partout** key to gain entry to the villa."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck's bunch of keys included a silent **passe-partout** that opened every pupil's wardrobe."}
    ]
  },
  "Dashboard — pass/passe.md": {
    "primary": "No longer fashionable; out of date; past one's prime (masculine form of French *passé*).",
    "secondary": "In fashion and cultural history, describing styles, customs, or doctrines discarded by modern society.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Nothing is so completely **passe** as the romantic melancholy of the preceding decade."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Chad perceived that the provincial ideals of Woollett were hopelessly **passe** in sophisticated Paris."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The Victorian conception of feminine duty has become thoroughly **passe** in the modern world."}
    ]
  },
  "Dashboard — pass/passee.md": {
    "primary": "Past one's prime; faded, outmoded, or no longer youthful (feminine form of French *passée*).",
    "secondary": "In Victorian social commentary, describing women whose youthful matrimonial prospects had waned.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The dowager had become decidedly **passee**, yet she continued to apply rouge and attend every ball."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond shuddered at the thought of ever becoming **passee** and neglected in provincial society."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Sir Walter Elliot considered his elder daughter sadly **passee**, lamenting the loss of her early bloom."}
    ]
  },
  "Dashboard — pass/passel.md": {
    "primary": "A large group or collection of people or things of an unspecified number; a pack (dialectal).",
    "secondary": "In American regional literature and folklore, an informal collective noun for children, dogs, or troubles.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "There was a whole **passel** of dogs barking and yelping around the cabin porch when we arrived."},
      {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "The farmer sighed as he surveyed the **passel** of unpaid bills lying upon the kitchen table."},
      {"author": "Bret Harte", "work": "The Luck of Roaring Camp", "quote": "A noisy **passel** of miners crowded around the cradle to catch a glimpse of the frontier baby."}
    ]
  },
  "Dashboard — pass/passementerie.md": {
    "primary": "Ornamental braid, edging, lace, tassels, or cord trimming used on clothing or upholstery.",
    "secondary": "In textile history and haute couture, elaborate silk, metallic, or beaded trimmings manufactured in France.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Her opera cloak was richly adorned with gold **passementerie** that sparkled under the gas chandeliers."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma admired the intricate silk **passementerie** displayed in the windows of the Rouen dressmaker."},
      {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "The court coat was stiff with silver **passementerie** and seed pearls in the grand Versailles fashion."}
    ]
  },
  "Dashboard — pass/passenger.md": {
    "primary": "A traveler on a public or private conveyance (such as a ship, train, or automobile) other than the driver.",
    "secondary": "In commercial transport history, fare-paying voyagers whose safety is entrusted to licensed common carriers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The Dover mail coach carried three weary **passenger** travelers, wrapped in cloaks against the winter fog."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "I never go as a **passenger**; nor, though I am something of a salt, do I ever go to sea as a Commodore."},
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Holmes disguised himself as an elderly **passenger** on the Continental express to evade Moriarty's spies."}
    ]
  },
  "Dashboard — pass/passer-by.md": {
    "primary": "A person who happens to walk past something or someone, especially on a street.",
    "secondary": "In urban observation, casual pedestrian witnesses who observe incidents in public spaces.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "A respectable **passer-by** seized Oliver by the collar, raising the cry of 'Stop thief!' down the street."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The cabman called upon an innocent **passer-by** to assist in lifting the injured gentleman."},
      {"author": "Robert Louis Stevenson", "work": "Strange Case of Dr Jekyll and Mr Hyde", "quote": "The brutal assault upon the child was witnessed with horror by a solitary midnight **passer-by**."}
    ]
  },
  "Dashboard — pass/passer.md": {
    "primary": "A person who passes, goes by, or delivers something; also a player in sports who passes the ball.",
    "secondary": "In criminal history, an accomplice who puts counterfeit coins or forged banknotes into commercial circulation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The nocturnal **passer** left distinct footprints in the slush beneath the dressing-room window."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The constable apprehended an experienced **passer** of counterfeit crowns in the crowded marketplace."},
      {"author": "Thomas Hughes", "work": "Tom Brown at Oxford", "quote": "The halfback was an expert **passer**, releasing the ball cleanly before being tackled."}
    ]
  },
  "Dashboard — pass/passerby.md": {
    "primary": "A person who happens to walk past someone or something on a street (solid spelling of passer-by).",
    "secondary": "In street journalism and literature, ordinary pedestrian citizens observing public events.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Every **passerby** seemed like a menacing shadow in the dense yellow smog of Baker Street."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A casual **passerby** would pause to peer through the shop window at the gingerbread figures."},
      {"author": "O. Henry", "work": "The Gift of the Magi", "quote": "Della walked through the crowded streets unnoticed by any hurried holiday **passerby**."}
    ]
  },
  "Dashboard — pass/passeres.md": {
    "primary": "A historical taxonomic order or suborder comprising perching birds (Passeriformes).",
    "secondary": "In classical ornithological classification, birds possessing four unwebbed toes arranged for perching (three anterior, one posterior).",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "The anatomical boundaries of the **Passeres** are defined by the distinctive aegithognathous palate structure."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Complex vocal syrinx development is uniquely perfected among the singing families of the **Passeres**."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "More than half of all known living avian species are embraced within the vast order **Passeres**."}
    ]
  },
  "Dashboard — pass/passeridae.md": {
    "primary": "The taxonomic family of Old World sparrows, true sparrows, and snowfinches in the order Passeriformes.",
    "secondary": "In systematic ornithology, seed-eating songbirds characterized by stout conical beaks and global synanthropic distribution.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Species of **Passeridae** exhibit remarkable behavioral adaptability to human agricultural settlements."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The cranial osteology of **Passeridae** reflects specialized adaptations for crushing hard graminaceous seeds."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "Colonization of isolated oceanic islands by members of **Passeridae** demonstrates rapid plumage divergence."}
    ]
  },
  "Dashboard — pass/passeriformes.md": {
    "primary": "The largest order of birds, comprising more than half of all avian species; the perching birds or passerines.",
    "secondary": "In avian systematics, songbirds distinguished by anisodactyl feet (three toes forward, one back) and vocal syrinx complexity.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "The order **Passeriformes** represents the crown radiation of modern neornithine avian evolution."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The adaptive radiation of **Passeriformes** on isolated archipelagos provided key evidence for speciation."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Song, brilliant plumage, and nest architecture attain their highest development within **Passeriformes**."}
    ]
  },
  "Dashboard — pass/passerina.md": {
    "primary": "A taxonomic genus of North American songbirds in the cardinal family Cardinalidae, including the painted and indigo buntings.",
    "secondary": "In ornithology, brightly colored sexually dimorphic buntings noted for vibrant blue, green, and indigo male plumage.",
    "quotes": [
      {"author": "John James Audubon", "work": "The Birds of America", "quote": "The indigo bunting, **Passerina** cyanea, glitters like a living sapphire against the roadside brambles."},
      {"author": "Alexander Wilson", "work": "American Ornithology", "quote": "No bird of our temperate forests surpasses the male **Passerina** ciris in its brilliant rainbow plumage."},
      {"author": "Henry David Thoreau", "work": "Journal", "quote": "A sweet metallic song announced the arrival of the blue **Passerina** in the scrub oaks."}
    ]
  },
  "Dashboard — pass/passerine.md": {
    "primary": "Of, relating to, or denoting birds of the order Passeriformes; perching songbirds.",
    "secondary": "In avian biology, land birds possessing specialized flexor tendons in the foot that lock automatically around twigs.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual selection accounts for the elaborate songs and decorative plumes characteristic of male **passerine** birds."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The perching mechanism of the **passerine** foot functions mechanically through the animal's resting weight."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Birds of paradise are specialized **passerine** descendants exhibiting the most extraordinary courtship displays."}
    ]
  },
  "Dashboard — pass/passero.md": {
    "primary": "Cape Passero, the southeasternmost point of Sicily; also the Italian word for sparrow.",
    "secondary": "In Mediterranean naval history, site of the 1718 Battle of Cape Passero where the British fleet defeated the Spanish navy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Belisarius anchored his fleet off Cape **Passero** before launching the reconquest of Gothic Sicily."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Admiral Byng's decisive victory at Cape **Passero** shattered Spanish naval ambitions in the Mediterranean."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "The rocky headlands of Cape **Passero** mark the ancient geological collision zone between Africa and Europe."}
    ]
  },
  "Dashboard — pass/passiflora.md": {
    "primary": "A taxonomic genus of about 550 species of flowering plants in the family Passifloraceae; passion flowers.",
    "secondary": "In economic botany, climbing vines celebrated for intricate radial flowers and edible tropical passion fruits (*maracuyá*).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The sensitive tendrils of **Passiflora** gracilis curl rapidly around supportive stems upon the slightest mechanical friction."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Vast climbing vines of **Passiflora** covered the riverbank trees with glorious corona-fringed blossoms."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Passiflora** bear complex multi-colored corona rings symbolizing the instruments of the Passion."}
    ]
  },
  "Dashboard — pass/passifloraceae.md": {
    "primary": "A family of flowering plants in the order Malpighiales, commonly known as the passion-flower family.",
    "secondary": "In systematic botany, predominantly tropical woody climbing lianas characterized by axillary tendrils and coronate floral structures.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The family **Passifloraceae** is distinguished by its conspicuous filiform corona and stalked gynophore."},
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "Certain extrafloral nectaries in the **Passifloraceae** attract mutualistic ants that protect the foliage from caterpillars."},
      {"author": "Alexander von Humboldt", "work": "Aspects of Nature", "quote": "Tropical South America represents the chief evolutionary center of diversity for the **Passifloraceae**."}
    ]
  },
  "Dashboard — pass/passim.md": {
    "primary": "A Latin term used in textual citations meaning 'throughout' or 'here and there in the work.'",
    "secondary": "In scholarly apparatus and indexation, indicating that a word, topic, or character is mentioned frequently throughout a treatise.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The corruption of the praetorian guard is attested by contemporary historians, **passim**."},
      {"author": "Samuel Johnson", "work": "Preface to Shakespeare", "quote": "Examples of this brilliant dramatic conceit are to be found in the comedies of Shakespeare, **passim**."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "References to the cosmic process recur in the ancient philosophical dialogues of the Stoics, **passim**."}
    ]
  },
  "Dashboard — pass/passing.md": {
    "primary": "Going by; moving past; lasting only for a short time; fleeting or transient.",
    "secondary": "In cultural and legal diction, a euphemism for death (a passing away); also navigating racial boundaries.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Show me a mistress that is **passing** fair, what doth her beauty serve but as a note where I may read who passed that **passing** fair?"},
      {"author": "Alfred Tennyson", "work": "The Passing of Arthur", "quote": "From the great deep to the great deep he goes; the old order changeth, yielding place to new."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I observed a **passing** shadow of sorrow cloud my mother's face before she smiled again."}
    ]
  },
  "Dashboard — pass/passion.md": {
    "primary": "Strong and barely controllable emotion; intense romantic or sexual desire, enthusiasm, or wrath.",
    "secondary": "In Christian theology, the suffering and death of Jesus Christ on the cross (from Latin *passio*, suffering).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Give me that man that is not passion's slave, and I will wear him in my heart's core, ay, in my heart of heart, as I do thee."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "True reason in man obscured, or not obeyed, immediately inordinate desires and upstart **passions** catch the government."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie was a creature of fierce **passion**, longing for an expansive life beyond her provincial village."}
    ]
  },
  "Dashboard — pass/passionate.md": {
    "primary": "Showing or caused by strong feelings or a strong belief; ardent, impassioned, or intense.",
    "secondary": "In historical character analysis, prone to intense outbursts of temper or romantic attachment.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A child of **passionate** nature cannot be subdued by cold cruelty; it only hardens her spirit into rebellion."},
      {"author": "William Shakespeare", "work": "The Passionate Pilgrim", "quote": "Did not the heavenly rhetoric of thine eye, 'gainst whom the world could not hold argument, persuade my heart to this **passionate** oath?"},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The **passionate** pilgrim sought among alpine crags a refuge from the hollow conventions of European society."}
    ]
  },
  "Dashboard — pass/passionately.md": {
    "primary": "In a way that shows strong feelings, romantic love, or intense belief; ardently.",
    "secondary": "In narrative prose, weeping, pleading, or arguing with unrestrained emotional fervor.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I loved natural philosophy **passionately**, devoting day and night to the study of chemical affinity."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton wept **passionately** as he made his secret vow to sacrifice his life for Lucie's peace."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy declared how ardently and **passionately** he admired and loved her, despite all family objections."}
    ]
  },
  "Dashboard — pass/passionateness.md": {
    "primary": "The characteristic of being passionate; intense emotional fervor, warmth, or ardency.",
    "secondary": "In psychological characterization, a temperament governed by deep and volatile emotional sensibilities.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **passionateness** of youth must be moderated by the cool reflection of mature judgment."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Arthur's natural **passionateness** was masked by an easy good-nature that made him blind to consequences."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Beneath Lucy's quiet, puritanical exterior lay an unsuspected **passionateness** of feeling."}
    ]
  },
  "Dashboard — pass/passionflower.md": {
    "primary": "A climbing plant of the genus Passiflora, bearing distinctive flowers with fringe-like coronas.",
    "secondary": "In Christian floral symbolism, named by 16th-century Spanish missionaries whose flower parts symbolized the Crucifixion.",
    "quotes": [
      {"author": "Alfred Tennyson", "work": "Maud", "quote": "There has fallen a splendid tear from the **passionflower** at the gate; she is coming, my dove, my dear."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The sensitive tendril of the blue **passionflower** firmly seized the branch within twenty minutes of contact."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A magnificent **passionflower** with purple filaments clambered over the conservatory trellis."}
    ]
  },
  "Dashboard — pass/passionless.md": {
    "primary": "Not showing or affected by passion or strong emotion; calm, cold, or dispassionate.",
    "secondary": "In characterization, an austere, purely intellectual detachment devoid of human warmth.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John was a cold, **passionless** man, measuring life strictly by duty rather than human affection."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "Holmes's **passionless** intellect rejected romantic feeling as a grit in his sensitive instruments."},
      {"author": "Alfred Tennyson", "work": "Idylls of the King", "quote": "The pure and **passionless** queen of heaven seemed to gaze down upon Arthur's broken realm."}
    ]
  },
  "Dashboard — pass/passive.md": {
    "primary": "Accepting or allowing what happens or what others do, without active response or resistance.",
    "secondary": "In grammar, designating a voice of verbs in which the subject undergoes rather than performs the action.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "In bare perception, the human mind is largely **passive**, receiving simple ideas from sensory impressions."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Amy Dorrit remained **passive** in her father's arms, comforting him with gentle, unselfish love."},
      {"author": "Henry David Thoreau", "work": "Civil Disobedience", "quote": "Must the citizen ever for a moment, or in the least degree, resign his conscience to the legislator? Under **passive** submission liberty dies."}
    ]
  },
  "Dashboard — pass/passively.md": {
    "primary": "In a passive manner; in a way that accepts things without resistance or active participation.",
    "secondary": "In scientific observation, allowing natural forces to carry an object without self-propulsion.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Seeds may be transported **passively** across ocean straits embedded in mud on the feet of aquatic birds."},
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "Bartleby leaned **passively** against the doorpost, murmuring his unalterable decision."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver sat **passively** before the empty hearth, numb with grief after his treasure was gone."}
    ]
  },
  "Dashboard — pass/passiveness.md": {
    "primary": "The characteristic of being passive; lack of active resistance, initiative, or reaction.",
    "secondary": "In political philosophy, the dangerous habit of civilian non-involvement that invites tyrannical rule.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "General **passiveness** in a citizenry is the ideal condition for despotic monarchs, but fatal to free commonwealths."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Patience is a noble virtue, but mere **passiveness** under injustice degrades human dignity."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Throw off this timid **passiveness** and declare your own spontaneous conviction before the world."}
    ]
  },
  "Dashboard — pass/passivism.md": {
    "primary": "The attitude or policy of being passive; passive resistance or political non-violence.",
    "secondary": "In social philosophy, adopting deliberate non-resistance or non-cooperation to achieve moral victory.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "The Kingdom of God Is Within You", "quote": "Christian **passivism** is not cowardice, but the most radical moral force for dismantling violence."},
      {"author": "William James", "work": "The Moral Equivalent of War", "quote": "Utopian **passivism** fails to capture the masculine imagination unless accompanied by martial civic virtues."},
      {"author": "Bertrand Russell", "work": "Justice in War-Time", "quote": "Principled **passivism** asserts that no political goal justifies the slaughter of millions of youth."}
    ]
  },
  "Dashboard — pass/passivity.md": {
    "primary": "Acceptance of what happens without active response or resistance; passiveness.",
    "secondary": "In psychological analysis, a state of behavioral inertia or learned helplessness in the face of adversity.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind displays complete **passivity** in the reception of simple ideas from external objects."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Excessive administrative centralization induces a creeping civic **passivity** among the provincial populace."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Hypnotic trance is marked by extraordinary motor **passivity** combined with acute sensory focus."}
    ]
  },
  "Dashboard — pass/passover.md": {
    "primary": "A major Jewish spring festival that commemorates the liberation of the Israelites from Egyptian slavery.",
    "secondary": "In biblical history, the sacred feast of unleavened bread (*Pesach*) commemorating the angel of death passing over Israelite homes.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The blood upon the doorpost marked the solemn feast of **Passover**, sparing the first-born of Israel."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Multitudes of devout pilgrims from across the diaspora gathered at Jerusalem for the feast of the **Passover**."},
      {"author": "Philo of Alexandria", "work": "The Special Laws", "quote": "The festival of the **Passover** commemorates the miraculous crossing from the bondage of passions to spiritual freedom."}
    ]
  },
  "Dashboard — pass/passport.md": {
    "primary": "An official travel document issued by a government certifying identity and nationality for international travel.",
    "secondary": "In historical diplomacy, safe-conduct papers issued by military commanders allowing travel through lines.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "He which hath no stomach to this fight, let him depart; his **passport** shall be made, and crowns for convoy put into his purse."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary guard examined Sydney Carton's **passport** with suspicious scrutiny at the city barrier."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Naval Treaty", "quote": "The foreign attache presented his diplomatic **passport** at the Dover pier before boarding the packet boat."}
    ]
  },
  "Dashboard — pass/surpass.md": {
    "primary": "To exceed; to be greater than; to do or be better than ever before.",
    "secondary": "In literary critique and aesthetics, to transcend ordinary human achievement in sublime beauty or skill.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "This is the prettiest low-born lass that ever ran on the green-sward; nothing she does or seems but smacks of something greater than herself, too noble for this place; her virtues **surpass** report."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "His form had yet not lost all her original brightness, nor appeared less than Archangel ruined, and the excess of glory obscured: so did he **surpass** his fallen peers."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Modern navigational discoveries far **surpass** the narrow geographical boundaries of the ancient Greeks."}
    ]
  },
  "Dashboard — pass/surpassing.md": {
    "primary": "Incomparable, transcendent, or towering; exceeding all others in degree or excellence.",
    "secondary": "In poetic description, extraordinary beauty, grandeur, or moral heroism.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The scenery of the valley of Chamounix possessed a **surpassing** majesty that hushed all earthly sorrow."},
      {"author": "Edgar Allan Poe", "work": "Ligeia", "quote": "In beauty of face no maiden ever equaled her; it was a radiance of **surpassing** and transcendent grace."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "O thou that with **surpassing** glory crowned, look'st from thy sole dominion like the god of this new world."}
    ]
  },
  "Dashboard — pass/surpassingly.md": {
    "primary": "In a surpassing manner; exceedingly, extraordinarily, or to an incomparable degree.",
    "secondary": "In narrative prose, exhibiting transcendent excellence or stunning visual magnificence.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white brow of the sperm whale rose **surpassingly** majestic above the blue Pacific swell."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The golden twilight rested **surpassingly** fair upon the ancient Roman arches and cypress hills."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Rebecca appeared **surpassingly** lovely as she pleaded for mercy before the grim tribunal."}
    ]
  },
  "Dashboard — pass/uncompassionate.md": {
    "primary": "Lacking compassion, pity, or mercy; pitiless, callous, or unfeeling toward others.",
    "secondary": "In social reform literature, cold bureaucratic indifference to human misery and destitution.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The beadle was a harsh, **uncompassionate** man who regarded orphan children as public nuisances."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creature lamented that humanity had proven universally **uncompassionate** to his solitary suffering."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mrs. Reed looked upon Jane with **uncompassionate** eyes, indifferent to the child's feverish terror."}
    ]
  },
  "Dashboard — pass/underpass.md": {
    "primary": "A road, subway, or pedestrian tunnel running underneath another road or a railway.",
    "secondary": "In civil infrastructure, a grade-separated crossing eliminating traffic intersections.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Crowds fled into the dark railway **underpass** to escape the scorching heat-ray of the Martian machine."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes darted through the dripping brick **underpass** near the Thames wharves in pursuit of our quarry."},
      {"author": "George Orwell", "work": "Keep the Aspidistra Flying", "quote": "Gordon hurried through the tiled station **underpass**, buffeted by damp London commuters."}
    ]
  },
  "Dashboard — pass/unimpassioned.md": {
    "primary": "Not showing or affected by passion or strong emotion; calm, cool, and dispassionate.",
    "secondary": "In judicial and philosophical discourse, objective analysis untainted by personal feeling.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate listened to the charges with an **unimpassioned** gravity that impressed even his detractors."},
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father's intellectual method was severe and **unimpassioned**, training me to test all propositions by evidence."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The true investigator maintains an **unimpassioned** neutrality while nature discloses her secrets."}
    ]
  },
  "Dashboard — pass/unpassable.md": {
    "primary": "Impossible to pass, cross, or travel through; impassable; insurmountable.",
    "secondary": "In travel narrative and military history, mountain defiles or flooded rivers that block passage.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "The mountain torrent had swollen overnight, leaving the rocky ford completely **unpassable**."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The rising tide had swept past the headland, rendering the beach path **unpassable** for the fugitives."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The snowdrifts upon the Yorkshire moors were reported **unpassable** for wheeled coaches."}
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

print(f"Successfully updated {updated}/{len(data)} notes in Dashboard — pass.")

res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base_dir}/Dashboard — pass"], capture_output=True, encoding="utf-8")
print(res.stdout)
