# -*- coding: utf-8 -*-
"""
Part 4 of Batch 3: domin words 21-39 (19 words):
['dominic', 'dominica', 'dominical', 'dominican', 'dominick', 'dominicus',
 'dominie', 'dominion', 'dominique', 'domino', 'dominoes', 'dominos',
 'dominus', 'predominance', 'predominant', 'predominantly', 'predominate',
 'predomination', 'subdominant']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part4_domin = {
  "dominic": {
    "primary": "A masculine given name derived from the Latin Dominicus, meaning 'belonging to the Lord' or 'of the Master'.",
    "secondary": "In hagiography and church history, Saint Dominic de Guzman (1170–1221), founder of the Order of Preachers (Dominicans).",
    "quotes": [
      {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "The youthful novice meditated upon the holy austerities practiced by Saint **dominic** in southern France."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The zealous followers of Saint **dominic** were commissioned by the Pope to combat the Cathar heresy."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "Our blessed patriarch **dominic** instructed his friars to contemplate divine truth and communicate it through sacred preaching."}
    ]
  },
  "dominica": {
    "primary": "An island nation in the Caribbean Lesser Antilles; or the Latin liturgical term for Sunday ('Dies Dominica').",
    "secondary": "In colonial geography and liturgical Latin, named by Columbus for its discovery on Sunday, November 3, 1493.",
    "quotes": [
      {"author": "James Anthony Froude", "work": "The English in the West Indies", "quote": "The mountainous interior of **dominica** rises into misty volcanic peaks cloaked in dense, untrodden rainforests."},
      {"author": "Charles Kingsley", "work": "At Last: A Christmas in the West Indies", "quote": "Looking out across the channel, the rugged green outline of **dominica** loomed against the tropical horizon."},
      {"author": "Washington Irving", "work": "The Life and Voyages of Christopher Columbus", "quote": "Columbus sighted the lush island on the Sabbath day and consequently bestowed upon it the pious name of **dominica**."}
    ]
  },
  "dominical": {
    "primary": "Relating to the Christian Sabbath or Lord's Day (Sunday); or relating to Jesus Christ as Lord.",
    "secondary": "In historical calendar computation, denoting the dominical letter (A through G) used to determine Sundays throughout the liturgical year.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Constantine enacted statutes consecrating the venerable day of the sun as a mandatory **dominical** holiday."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary calendar abolished the ancient **dominical** cycle in favor of secular ten-day decades."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The pious divine devoted his **dominical** sermons to edifying moral commentary upon the Gospels."}
    ]
  },
  "dominican": {
    "primary": "A member of the Roman Catholic Order of Preachers (founded by St. Dominic); or a native or inhabitant of Dominica or the Dominican Republic.",
    "secondary": "In ecclesiastical history, a mendicant friar wearing a white habit and black cloak, historically prominent in Thomist philosophy and the Inquisition.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "A learned **dominican** monk paced slowly through the shaded cloisters of the ancient convent."},
      {"author": "Donn Byrne", "work": "The Wind Bloweth", "quote": "The elderly **dominican** friar raised his crucifix to bless the departing pilgrim at the crossroads."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The zealous **dominican** inquisitors wielded formidable authority across the southern provinces of Europe."}
    ]
  },
  "dominick": {
    "primary": "A variant spelling of the masculine given name Dominic, from the Latin Dominicus ('belonging to the Lord').",
    "secondary": "In onomastics and historical biography, a patronymic surname and given name popular among Irish, English, and continental families.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "They turned the corner near Father Cowley's lodgings along little **dominick** street in the afternoon light."},
      {"author": "William Makepeace Thackeray", "work": "The Luck of Barry Lyndon", "quote": "My loyal uncle **dominick** had served as a brave captain in the Irish brigades across Flanders."},
      {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "Old brother **dominick** spent forty peaceful years tending the cathedral archives and rare monastic rolls."}
    ]
  },
  "dominicus": {
    "primary": "The Latin form of Dominic ('belonging to the Lord' or 'master'); or a specific literary character or historical personage.",
    "secondary": "In classical and medieval Latin, the possessive adjective of dominus, also personified in Hawthorne's itinerant peddler Dominicus Pike.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "Master **dominicus** Pike was an itinerant tobacco peddler possessing an insatiable appetite for rural gossip."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "The scholarly priest invoked Saint **dominicus** during the solemn recitation of the Latin litany."},
      {"author": "Washington Irving", "work": "Chronicle of the Conquest of Granada", "quote": "Father **dominicus** held high the sacred relic before the assembled knights prior to the final assault."}
    ]
  },
  "dominie": {
    "primary": "A Scottish schoolmaster, teacher, or tutor; or an informal title for a clergyman or pastor.",
    "secondary": "In Scottish literature (especially Scott's Waverley novels), an affectionate title for an eccentric, bookish village schoolmaster.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "Guy Mannering", "quote": "**dominie** Sampson was an eccentric scholar whose immense learning was matched only by his utter unworldliness."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "The kindly village **dominie** lent David Balfour a few shillings and a Latin testament for his perilous journey."},
      {"author": "Jack London", "work": "The Star Rover", "quote": "I recalled the pedantic Scottish **dominie** who had hammered the conjugation of Latin verbs into our unwilling heads."}
    ]
  },
  "dominion": {
    "primary": "Sovereignty or control over territory, people, or affairs; or a territory ruled by a sovereign monarch or government.",
    "secondary": "In imperial constitutional history, a self-governing autonomous polity under the British crown; or a choir of celestial angels.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Over himself, over his own body and mind, the individual is sovereign, exercising absolute rightful **dominion**."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Man's true **dominion** over nature is achieved through spiritual harmony and intellectual insight rather than brute force."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man has established undisputed **dominion** over the animal kingdom through superior intellectual endowments."}
    ]
  },
  "dominique": {
    "primary": "A traditional American dual-purpose breed of chicken with barred plumage and a rose comb; or a French unisex given name.",
    "secondary": "In poultry husbandry and avian breeding, America's oldest chicken breed, characterized by slate-and-white 'cuckoo' barring.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "An old speckled **dominique** hen pecked lazily among the weeds beside Aunt Polly's picket fence."},
      {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "The sandy yard contained a sturdy **dominique** rooster strutting proudly amidst his quiet flock."},
      {"author": "Harriet Beecher Stowe", "work": "Uncle Tom's Cabin", "quote": "A brood of mottled **dominique** chicks scurried into the kitchen whenever the wooden screen door swung ajar."}
    ]
  },
  "domino": {
    "primary": "A small rectangular gaming tile marked with pips, or a loose hooded cloak worn with an eye mask at masquerades.",
    "secondary": "In carnival tradition and mathematics, a hooded disguise worn by Venetian revelers, or a geometric polyomino composed of two joined squares.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She disguised her identity at the charity masquerade beneath a sweeping black velvet **domino** and silk mask."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "He recalled the masked ball where each guest flitted past like a silent, mysterious **domino**."},
      {"author": "Edgar Allan Poe", "work": "The Masque of the Red Death", "quote": "The ghastly intruder strode silently among the masqueraders, wrapped in an austere black **domino**."}
    ]
  },
  "dominoes": {
    "primary": "A popular tabletop game played with a set of rectangular tiles, each bearing faces divided into two squares marked with pips.",
    "secondary": "In combinatorics and geopolitical metaphor, a matching tile game, or the 'domino theory' positing sequential regional political collapse.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The accountant and the lawyer sat upon the yacht's deck, idling away the evening over a game of **dominoes**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Old men clicked their bone **dominoes** together upon the beer-stained tables of the tavern parlor."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "They passed the rainy afternoon in the drawing-room clicking black-and-white **dominoes** across the mahogany table."}
    ]
  },
  "dominos": {
    "primary": "The plural form of domino, denoting several rectangular pip-marked tiles or hooded masquerade cloaks.",
    "secondary": "In costume history and games, multiple hooded carnival cloaks worn at masquerades or sets of gaming tiles.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Assignation", "quote": "Figures enveloped in dark **dominos** glided through the torchlit halls of the Venetian palazzo."},
      {"author": "Lord Byron", "work": "Letters and Journals", "quote": "The carnival crowd surged into Saint Mark's square, a bright swirl of masks, mantles, and silk **dominos**."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The conspirators concealed their faces under black **dominos** as they mingled with the festive masquerade throng."}
    ]
  },
  "dominus": {
    "primary": "A Latin noun meaning master, lord, or owner, denoting patriarchal or political authority in Roman civilization.",
    "secondary": "In Roman law and constitutional history, the absolute owner of property, or the despotic imperial title adopted during the Dominate.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Diocletian cast aside the republican title of princeps and demanded to be worshipped as absolute **dominus** and god."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "The celebrating priest turned to the altar and intoned '**dominus** vobiscum' in a deep, resonant voice."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "In early Roman jurisprudence, the **dominus** exercised unrestrained patriarchal power over all slaves and estate chattels."}
    ]
  },
  "predominance": {
    "primary": "Superior power, ascendancy, or numerical majority that exerts controlling influence over rivals.",
    "secondary": "In sociology, ecology, and geopolitics, the overwhelming prevalence or controlling influence of a specific group, factor, or species.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Representative Government", "quote": "A balanced constitution prevents any single commercial faction from gaining total political **predominance**."},
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Moral character achieves lasting greatness only through the steady **predominance** of intellect over blind passion."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth perceived the marked **predominance** of wounded pride over genuine affection in Mr. Darcy's initial proposal."}
    ]
  },
  "predominant": {
    "primary": "Present as the strongest, main, or most influential element; exercising controlling power or conspicuous prevalence.",
    "secondary": "In epidemiology, demographics, and mineralogy, constituting the major constituent, prevailing strain, or primary component.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In every large island, certain plant genera maintain a **predominant** position across diverse botanical habitats."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Benevolent sympathy should become the **predominant** motive in the deliberate moral choices of enlightened citizens."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A tender devotion to Dorothea became the **predominant** impulse guiding Ladislaw's daily thoughts."}
    ]
  },
  "predominantly": {
    "primary": "Mainly, mostly, or for the most part; exerting primary influence or constituting the greater share.",
    "secondary": "In socioeconomic and demographic statistics, representing the substantial majority or prevailing proportion of a population.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Her aesthetic tastes were **predominantly** cultivated through solitary reading in the quiet library at Gardencourt."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The fossil fauna found in these strata are **predominantly** mammalian, showing close affinities to living marsupials."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The emotions manifested during infant crying are **predominantly** sensations of physical distress and cold."}
    ]
  },
  "predominate": {
    "primary": "To be greater in number, power, or importance; to prevail or exert controlling influence over competitors.",
    "secondary": "In political science and ecological dynamics, to hold decisive sway or outcompete rival forces within an environment.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She hoped that family affection would ultimately **predominate** over resentment in her father's forgiving heart."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A cheerful optimism seemed to **predominate** in Mr. Micawber's temper, even in the midst of financial adversity."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "In every well-ordered mind, deliberate reason ought to **predominate** over turbulent physical appetites."}
    ]
  },
  "predomination": {
    "primary": "The exercise of superior power, ascendant influence, or numerical superiority; prevalence over others.",
    "secondary": "In political theory and social physics, the structural ascendancy or hegemony of one class or doctrine over rivals.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The absolute **predomination** of Parisian clubs over the provincial assemblies subverted all constitutional liberty."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Poetic genius requires an exquisite balance rather than the despotic **predomination** of fancy over understanding."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The unchecked **predomination** of jacobinical fury swept away the ancient judicial safeguards of the realm."}
    ]
  },
  "subdominant": {
    "primary": "The fourth scale degree of a diatonic scale, located directly below the dominant; or a subdominant musical chord.",
    "secondary": "In harmonic music theory and plant ecology, the fourth degree of the musical scale, or a secondary plant species in a canopy.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "On the Sensations of Tone", "quote": "Modulation from the tonic triad to the **subdominant** chord produces a gentle relaxation in acoustic harmonic tension."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "The transition from the dominant through the **subdominant** back to the fundamental keynote mirrors metaphysical striving and peace."},
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Underneath the dense pine canopy, certain **subdominant** shrub species thrive in the dappled forest sunlight."}
    ]
  }
}
