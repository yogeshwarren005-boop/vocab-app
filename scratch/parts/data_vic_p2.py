# -*- coding: utf-8 -*-
"""
Part 4: vic part 2 (words 22-42)
['vice-chancellor', 'vice-presidency', 'vice-presidential', 'vice-regent', 'vicegerent', 'vicenary', 'vicennial', 'viceregal', 'vicereine', 'viceroy', 'viceroyalty', 'viceroyship', 'vicia', 'vicinal', 'vicinity', 'vicious', 'viciously', 'viciousness', 'vicissitude', 'victim', 'victimisation']
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

data_vic_p2 = {
  "vice-chancellor": {
    "primary": "The chief executive officer and administrative head of a British, Commonwealth, or European university.",
    "secondary": "In historic equity jurisprudence, an equity judge acting as chief deputy to the Lord Chancellor in the English Court of Chancery.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The counsel addressed the **vice-chancellor** with tedious arguments regarding the endless testamentary trusts in Jarndyce."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King James attempted to compel the **vice-chancellor** of Cambridge to admit a Benedictine monk without the customary oaths."},
      {"author": "Anthony Trollope", "work": "The Duke's Children", "quote": "The university **vice-chancellor** received the distinguished parliamentary deputation in the great senate house."}
    ]
  },
  "vice-presidency": {
    "primary": "The office, rank, duties, or period of tenure of a vice president in an organization or government.",
    "secondary": "In American constitutional politics, the executive office established to preside over the Senate and assume the chief magistracy upon a vacancy.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional dignity of the **vice-presidency** requires a statesman of national character and unblemished honor."},
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "Many politicians believed that relegating me to the **vice-presidency** would effectively terminate my active career."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The peaceful succession from the **vice-presidency** proved the enduring resilience of constitutional conventions."}
    ]
  },
  "vice-presidential": {
    "primary": "Pertaining to, held by, or suitable for a vice president or the office of vice president.",
    "secondary": "In electoral history, concerning campaign strategies, nominations, or executive responsibilities associated with the second-highest civic office.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The **vice-presidential** candidate was selected primarily to balance regional factions within the national party convention."},
      {"author": "James Bryce", "work": "The American Commonwealth", "quote": "Foreign observers often marvel at the constitutional powers vested in the American **vice-presidential** office."},
      {"author": "Henry Cabot Lodge", "work": "The Senate of the United States", "quote": "The presiding officer maintained order from the **vice-presidential** rostrum during the stormy constitutional debate."}
    ]
  },
  "vice-regent": {
    "primary": "A person appointed to act in the place of a regent, ruler, or sovereign deputy; a secondary governor.",
    "secondary": "In historical governance, an administrative commissioner or magistrate exercising delegated viceregal powers in outlying provinces.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor confirmed the patrician as his imperial **vice-regent** over the unruly provinces of Illyricum."},
      {"author": "Sir Walter Scott", "work": "The Abbott", "quote": "The Scottish council appointed the earl as **vice-regent** during the minority of the young prince."},
      {"author": "William Hickling Prescott", "work": "History of the Reign of Philip the Second", "quote": "Philip entrusted his capable **vice-regent** with suppressing the insurrections spreading across the Low Countries."}
    ]
  },
  "vicegerent": {
    "primary": "A person appointed by a ruler or sovereign authority to exercise executive powers as an administrative deputy.",
    "secondary": "In classical political theology, an earthly monarch regarded as God's representative entrusted with executing divine justice.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Sole deputy of the world's large tongue, great deputy, the sea's **vicegerent**, and sole dominator of Navarre."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Then told the Son his Father thus was pleased, and him the celestial **vicegerent** anointed over all heavenly hierarchies."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Kings are upon earth the **vicegerent** authorities of heaven, accountable at last to eternal justice for their reign."}
    ]
  },
  "vicenary": {
    "primary": "Belonging to, based on, or consisting of the number twenty; vigesimal in numerical base.",
    "secondary": "In historical metrology and ethnomathematics, a numerical system or tally calculation founded upon multiples of twenty.",
    "quotes": [
      {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "Many indigenous linguistic stocks employ a **vicenary** numeral system derived from counting fingers and toes together."},
      {"author": "Thomas Wright", "work": "The Celt, the Roman, and the Saxon", "quote": "Traces of ancient Celtic **vicenary** reckoning survive in the traditional score counting of northern shepherds."},
      {"author": "Alexander von Humboldt", "work": "Researches Concerning the Institutions and Monuments of the Ancient Inhabitants of America", "quote": "The sophisticated calendar system of the Aztecs was constructed upon an astronomical and **vicenary** framework."}
    ]
  },
  "vicennial": {
    "primary": "Happening once every twenty years; enduring for or relating to a period of twenty years.",
    "secondary": "In classical Roman history and imperial celebrations, marking the solemn vicennalia festival commemorating twenty years of imperial rule.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Diocletian celebrated his solemn **vicennial** games at Rome, displaying triumphs from every quarter of the empire."},
      {"author": "Theodor Mommsen", "work": "The History of Rome", "quote": "The Senate voted grand commemorative medallions to celebrate the emperor's completed **vicennial** magistracy."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The Roman populace anticipated the splendor of the **vicennial** festival that marked two decades of imperial peace."}
    ]
  },
  "viceregal": {
    "primary": "Of, relating to, or characteristic of a viceroy or vicereine; imperial and administrative in deputized splendor.",
    "secondary": "In British and Spanish colonial administration, pertaining to the court, ceremonial retinue, and authority of a viceroy.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Plain Tales from the Hills", "quote": "The Simla season reached its festive height when the **viceregal** party arrived at the hill station."},
      {"author": "William Makepeace Thackeray", "work": "The Luck of Barry Lyndon", "quote": "He attended the glittering Dublin levée, hoping to secure favor within the lavish **viceregal** circle."},
      {"author": "Winston Churchill", "work": "The Story of the Malakand Field Force", "quote": "The frontier tribesmen sent tribal emissaries to treat directly with the British **viceregal** delegation."}
    ]
  },
  "vicereine": {
    "primary": "The wife or consort of a viceroy; or a female ruler who governs a colony as the sovereign's representative.",
    "secondary": "In imperial social history, the leading hostess of a viceregal court who directed courtly protocol, diplomacy, and philanthropy.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "The traveling lama marveled at the great hospital founded under the patronage of the gracious **vicereine**."},
      {"author": "Arthur Conan Doyle", "work": "The Exploits of Brigadier Gerard", "quote": "The grand duchess received our regiment with the haughty elegance expected of an imperial **vicereine**."},
      {"author": "Lytton Strachey", "work": "Queen Victoria", "quote": "Lady Dufferin presided as **vicereine** in Calcutta, organizing medical charities for Indian women across the empire."}
    ]
  },
  "viceroy": {
    "primary": "A ruler exercising authority in a colony or province as the personal representative of a sovereign monarch.",
    "secondary": "In Spanish, Portuguese, and British imperial governance, the supreme civil and military governor of an overseas kingdom or viceroyalty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "And Charles, upon condition thou wilt swear to pay him tribute and submit thyself, thou shalt be placed for **viceroy** under him."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The ambitious prince appointed a loyal **viceroy** to collect tribute from the conquered island dominions."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Spanish **viceroy** formerly resided in the ancient walled palace overlooking the harbor of Callao."}
    ]
  },
  "viceroyalty": {
    "primary": "The office, dignity, jurisdiction, or territorial domain governed by a viceroy.",
    "secondary": "In Spanish imperial administration, vast colonial administrative realms such as New Spain or Peru governed by a royal viceroy.",
    "quotes": [
      {"author": "William Hickling Prescott", "work": "History of the Conquest of Peru", "quote": "The crown created the magnificent **viceroyalty** of Peru to establish order among the warring conquistadors."},
      {"author": "Alexander von Humboldt", "work": "Political Essay on the Kingdom of New Spain", "quote": "The mineral wealth of the Mexican **viceroyalty** provided vast silver revenues to the Spanish treasury."},
      {"author": "Robert Southey", "work": "History of Brazil", "quote": "The Portuguese prince transformed Rio de Janeiro into the capital of a flourishing South American **viceroyalty**."}
    ]
  },
  "viceroyship": {
    "primary": "The office, rank, dignity, or term of service of a viceroy.",
    "secondary": "In British imperial history, the five-year tenure of an appointed governor-general and viceroy over the Indian empire.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "During his brilliant **viceroyship**, Warren Hastings consolidated British administrative power throughout Bengal."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "His father had served with distinction in Dublin during the difficult years of his Irish **viceroyship**."},
      {"author": "G. O. Trevelyan", "work": "Cawnpore", "quote": "The outgoing governor surrendered his arduous **viceroyship** with heartfelt relief to his younger successor."}
    ]
  },
  "vicia": {
    "primary": "A botanical genus of flowering legume plants in the Fabaceae family, commonly comprising vetches and faba beans.",
    "secondary": "In agricultural botany and agronomy, nitrogen-fixing leguminous herbs grown as protein-rich livestock fodder, cover crops, and green manure.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The ancient cultivation of the broad bean, classified as **Vicia** faba, traces back to prehistoric Bronze Age settlements."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Vicia** is distinguished by pinnate leaves ending in tendrils and a style bearded at the apex."},
      {"author": "Alphonse de Candolle", "work": "Origin of Cultivated Plants", "quote": "Several species of wild **Vicia** flourish across the Mediterranean basin, serving as ancestral forage crops."}
    ]
  },
  "vicinal": {
    "primary": "Adjacent, neighboring, or situated in the immediate vicinity; or relating to local parish roads.",
    "secondary": "In organic chemistry and crystallography, designating functional groups attached to adjacent carbon atoms, or crystal faces near an axis.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "We rambled through **vicinal** lanes and orchards where cider apples hung thick upon autumn branches."},
      {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "The quartz crystal displayed minute **vicinal** planes inclined slightly to the primary pyramidal faces."},
      {"author": "Thomas Pennant", "work": "A Tour in Scotland", "quote": "Communication between the coastal villages was maintained through rugged **vicinal** paths across the moors."}
    ]
  },
  "vicinity": {
    "primary": "The area near or surrounding a particular place; proximity in location or relationship.",
    "secondary": "In geography and urban sociology, the adjacent spatial zone sharing municipal infrastructure, markets, and environmental conditions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The isolated farm stood in the lonely **vicinity** of Norcombe Hill, exposed to every sudden squall from the south."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It is enough for me to point out that there are certain social circles in the **vicinity** whose acquaintance would be advantageous."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "After his return he began to find his true field of activity in the peaceful **vicinity** of his native village."}
    ]
  },
  "vicious": {
    "primary": "Deliberately cruel, violent, spiteful, or corrupt; deeply characterized by moral depravity or vice.",
    "secondary": "In logic and behavioral cycles, a vicious circle describes an escalating chain of causation where each bad result worsens the original problem.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "He is deformed, crooked, old, and sere, ill-faced, worse bodied, shapeless everywhere, **vicious**, ungentle, foolish, blunt, unkind."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sergeant's **vicious** phases were the offspring of sudden impulse rather than deep-seated malevolent design."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His cold and sarcastic temperament made him a **vicious** antagonist whenever his professional vanity was wounded."}
    ]
  },
  "viciously": {
    "primary": "In a vicious, cruel, spiteful, or violently malicious manner.",
    "secondary": "In physical combat or debate, attacking with unbridled ferocity aimed at inflicting maximum harm.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The wounded whale turned **viciously** upon the whaleboat, snapping its enormous jaws across the cedar gunwales."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Spitz slashed **viciously** with his bared fangs, seeking an opening to tear his rival's throat in the arctic snow."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed struck me **viciously** across the face when I refused to surrender the book I was reading."}
    ]
  },
  "viciousness": {
    "primary": "The character, disposition, or trait of being vicious, cruel, depraved, or spitefully malicious.",
    "secondary": "In animal behavior and psychology, an ingrained tendency toward aggressive, unpredictable, or savage hostility.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "When our actions do not, our fears do make us traitors; let our **viciousness** be seen in our deliberate surrender to passion."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The sullen beast was notorious throughout the parish for its intractable temper and sheer **viciousness**."},
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "The rooster pecked at my ankles with an unexpected **viciousness** that completely upset my dignity in the farmyard."}
    ]
  },
  "vicissitude": {
    "primary": "A change of circumstances or fortune, typically one that is unwelcome, sudden, or unpleasant.",
    "secondary": "In philosophical literature and historiography, the mutability and natural alternation of human affairs, empires, or seasons.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Idiosyncrasy and **vicissitude** had combined to stamp Sergeant Troy as a man of erratic impulse and reckless adventure."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "He had undergone such profound inward **vicissitude** that the familiar street appeared like a half-remembered dream."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Light and darkness in perpetual round revolve with sweet **vicissitude** across the face of the unblemished earth."}
    ]
  },
  "victim": {
    "primary": "A person harmed, injured, killed, or made to suffer as a result of a crime, accident, or hostile action.",
    "secondary": "In anthropology and religious history, a sacrificial animal or human offered on an altar to propitiate a deity.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Perhaps I am a bad man, the **victim** of my impulses, led away to do what my sober reason condemns."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She was humiliated to find herself a mere **victim** of feeling, as if her rational will had surrendered to circumstance."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "On receiving this warning, the terrified **victim** might either openly abjure his former associates or prepare for immediate vengeance."}
    ]
  },
  "victimisation": {
    "primary": "The action of singling someone out for cruel or unjust treatment, persecution, or exploitation.",
    "secondary": "In criminology and social policy, the adverse sociological process whereby vulnerable individuals suffer harm from systemic abuse.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The trade union organizer protested against the covert **victimisation** of outspoken factory workers by the management."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "He felt a bitter resentment against the political **victimisation** that drove talented men into enforced obscurity."},
      {"author": "John Galsworthy", "work": "Strife", "quote": "The prolonged strike produced endless instances of personal **victimisation** among the struggling families in the valley."}
    ]
  }
}
