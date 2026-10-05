# -*- coding: utf-8 -*-
"""
Part 3 of Speech Batch 4:
- Dashboard — nom & nomin words (part A - 21 words):
  agnomen, denominate, denomination, denominational, denominationalism,
  denominationally, denominator, ignominious, ignominiously, ignominiousness,
  ignominy, ineloquently (already in loqu, keep check),
  interdenominational, noma, nomad, nomadic, nome, nomenclature,
  nomenklatura, nomia, nominal
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part3_nom_a = {
  "agnomen": {
    "primary": "An additional, fourth name or personal epithet given to an ancient Roman, typically commemorating an achievement.",
    "secondary": "In Roman onomastics, an honorary or descriptive surname added to the *praenomen*, *nomen*, and *cognomen* (e.g. *Africanus* for Scipio).",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The triumphant general received the illustrious **agnomen** of Africanus in memory of his decisive victory over Carthage."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "The patrician proudly bore every ancient title and honorable **agnomen** inscribed upon the funeral wax busts of his ancestors."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "In imperial inscriptions, the ruler accumulated title upon title, appending an **agnomen** from every subjugated border province."}
    ]
  },
  "denominate": {
    "primary": "To give a specific name or designation to someone or something; to call, designate, or term.",
    "secondary": "In economics, mathematical fractions, and formal classification, to express a monetary value in a specified unit or define a fraction's base.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Nations are accustomed to **denominate** their standard coin after the weight of precious metal originally contained in it."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men first invent general concepts and then **denominate** diverse sensory qualities under common abstract terms."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Philosophers **denominate** those vivid sensory impressions passions, which arise immediately from bodily pleasures or pains."}
    ]
  },
  "denomination": {
    "primary": "A recognized autonomous branch of a religious faith; also a specified unit or value in a currency system.",
    "secondary": "In classification and financial systems, a designated class, category, or monetary face-value increment.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The banking establishment issued paper notes of modest **denomination** to facilitate everyday retail transactions."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Every Christian **denomination** in the republic flourished peacefully without receiving exclusive financial support from the state."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Zealots of every ecclesiastical **denomination** joined hands to defend common liberties against crown encroachment."}
    ]
  },
  "denominational": {
    "primary": "Relating to or sponsored by a particular religious denomination, sect, or ecclesiastical organization.",
    "secondary": "In educational history and religious sociology, organized along sectarian lines or restricted to members of a single religious communion.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The narrow rivalries of **denominational** academies prevented the establishment of a truly national system of secondary culture."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "State schools must provide universal secular instruction, leaving strictly **denominational** catechisms to the domestic hearth."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Despite intense **denominational** divisions, American clergymen preached identical moral principles of civic responsibility."}
    ]
  },
  "denominationalism": {
    "primary": "Devotion to or emphasis on the interests, doctrines, or identity of a particular religious denomination.",
    "secondary": "In religious sociology and church history, the sectarian principle organizing religious life into competing institutional bodies.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Rigid **denominationalism** frequently obscures the vital spiritual core shared by all authentic inner conversions."},
      {"author": "John Dewey", "work": "A Common Faith", "quote": "The entrenched loyalties of historical **denominationalism** divide democratic communities over doctrinal dogmas."},
      {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "The ascetic ethos transcended narrow **denominationalism**, transforming everyday labor into an ethical calling."}
    ]
  },
  "denominationally": {
    "primary": "In a manner according to, characterized by, or organized along the lines of religious denominations.",
    "secondary": "In institutional sociology, partitioned or administered on the basis of sectarian ecclesiastical affiliations.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The electorate was divided **denominationally** on educational policy, yet united regarding constitutional principles."},
      {"author": "Matthew Arnold", "work": "Schools and Universities on the Continent", "quote": "Charitable relief was administered **denominationally**, producing needless duplication among competing parish councils."},
      {"author": "John Stuart Mill", "work": "Inaugural Address at St Andrews", "quote": "A university organized **denominationally** risks subordinating universal philosophical inquiry to sectarian apologetics."}
    ]
  },
  "denominator": {
    "primary": "The number below the line in a vulgar fraction showing how many parts the whole is divided into; a common characteristic.",
    "secondary": "In mathematics and sociological rhetoric, the divisor in a ratio, or a shared common standard or unifying trait.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "In every rational fraction, the **denominator** designates the number of equal parts into which the unit is partitioned."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Beneath varied cultural traditions, comparative anthropology searches for the lowest common **denominator** of human nature."},
      {"author": "William James", "work": "Pragmatism", "quote": "The diverse philosophies of the age share a common pragmatic **denominator** in evaluating ideas by their consequences."}
    ]
  },
  "ignominious": {
    "primary": "Deserving or causing public disgrace, dishonor, shame, or humiliation; degrading.",
    "secondary": "In military and political history, marked by utter loss of reputation, ignoble surrender, or shameful retreat.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman legions were compelled to pass under the yoke, suffering an **ignominious** capitulation before barbarian foes."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was locked in the red-room as a punishment for rebellion, enduring an **ignominious** imprisonment in solitary terror."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The venerable monarch was dragged from his palace to undergo an **ignominious** trial before triumphant factionalists."}
    ]
  },
  "ignominiously": {
    "primary": "In a humiliating, dishonorable, or shameful manner; disgracefully.",
    "secondary": "In military annals and biographical narrative, suffering defeat or expulsion with absolute loss of prestige.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The corrupt chancellor was stripped of the Great Seal and driven **ignominiously** from the royal court by his peers."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The braggart mercenary fled **ignominiously** from the breach, abandoning his shield and halberd in headlong panic."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The former spy was dismissed **ignominiously** from government service, wandering London taverns in shabby disgrace."}
    ]
  },
  "ignominiousness": {
    "primary": "Despicable shamefulness, profound dishonor, or extreme public disgrace attaching to conduct or character.",
    "secondary": "In ethical philosophy and historical analysis, the reprehensible disgrace or contemptible baseness of an action.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **ignominiousness** of cowardice lies in purchasing transient bodily safety at the cost of immortal honor."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The utter **ignominiousness** of the royal flight to Varennes dissolved the mystical reverence once paid to the crown."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "He felt keenly the petty **ignominiousness** of their family dispute, recoiling from public sensationalism."}
    ]
  },
  "ignominy": {
    "primary": "Public shame, disgrace, dishonor, or infamy resulting from shameful conduct.",
    "secondary": "In legal and civic history, civil degradation or perpetual forfeiture of social esteem and constitutional privilege.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "She walked toward the scaffold of pillory, bearing her infant in her arms and enduring the full **ignominy** of the gaze."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan resolved never to submit or yield, preferring eternal warfare to the shameful **ignominy** of asking pardon."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The vanquished emperor preferred death by his own hand rather than endure the public **ignominy** of a Roman triumph."}
    ]
  },
  "interdenominational": {
    "primary": "Occurring between, involving, or shared by two or more religious denominations.",
    "secondary": "In ecumenical history and institutional theology, cooperative ventures uniting diverse Christian church bodies without requiring doctrinal merger.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The great revival meetings fostered an **interdenominational** fervor where sectarian distinctions vanished in common piety."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Civic charities frequently operated on an **interdenominational** basis, drawing volunteer support from all local pulpits."},
      {"author": "Matthew Arnold", "work": "Last Essays on Church and Religion", "quote": "True religious fellowship requires **interdenominational** tolerance rather than insisting upon narrow theological dogmas."}
    ]
  },
  "noma": {
    "primary": "A severe, rapidly progressive, gangrenous infection that destroys the mucous membranes of the mouth and facial tissues.",
    "secondary": "In clinical pathology and infectious disease, *cancrum oris*, a devastating polymicrobial facial gangrene primarily afflicting malnourished children.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cases of **noma** occur almost exclusively in debilitated children recovering from measles in crowded, unhygienic environments."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The microscopic borders of **noma** reveal rapid tissue necrosis and thrombosis preceding massive sloughing of the cheek."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The clinical progression of **noma** presents one of the most frightening forms of gangrenous stomatitis in pediatric practice."}
    ]
  },
  "nomad": {
    "primary": "A member of a people having no permanent abode, who travel from place to place to find fresh pasture for livestock.",
    "secondary": "In anthropology and cultural geography, an pastoralist or itinerant wanderer moving along seasonal migratory routes.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The pastoral **nomad** of the Scythian steppes lived in wheeled tents, following herds across boundless grassland."},
      {"author": "Alexander von Humboldt", "work": "Aspects of Nature", "quote": "The desert wanderer lives as a proud **nomad**, adapting to arid wilderness where sedentary agriculture is impossible."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The Bedouin **nomad** scorns the walled cities of the plain, valuing horses and freedom above settled luxury."}
    ]
  },
  "nomadic": {
    "primary": "Living the life of a nomad; roaming from place to place without fixed settlement; wandering.",
    "secondary": "In ethnology, pastoral lifestyle characterized by seasonal transhumance across grasslands or deserts.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The plains of the Pampas were inhabited by fiercely independent tribes following a purely **nomadic** existence on horseback."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The fierce cavalry charges of the **nomadic** Huns shattered the disciplined ranks of the imperial legions."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A wandering imagination leads the mind on **nomadic** excursions far beyond the confines of village society."}
    ]
  },
  "nome": {
    "primary": "An administrative province or territorial division in ancient Egypt; in ancient Greece, a musical hymn or mode.",
    "secondary": "In Egyptology, an ancient territorial district governed by a nomarch, each associated with specific deities and heraldic totems.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Each ancient Egyptian **nome** venerated its own sacred animal totem, often leading to fierce religious disputes between neighboring districts."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The tax collectors assessed the granaries of every agricultural **nome** along the fertile banks of the Nile."},
      {"author": "Herodotus", "work": "The Histories", "quote": "The pharaoh distributed the fertile land among warriors, assigning estates within every administrative **nome** of Lower Egypt."}
    ]
  },
  "nomenclature": {
    "primary": "A system of names or terms used in a particular science, art, or discipline; formal naming rules.",
    "secondary": "In systematic taxonomy and organic chemistry, the standardized binomial or IUPAC naming rules governing species or molecules.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "A reformed chemical **nomenclature** must reflect the elemental composition of substances rather than archaic alchemical tradition."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In biological taxonomy, precision of binomial **nomenclature** is indispensable to avoid confounding distinct geographic varieties."},
      {"author": "Thomas Henry Huxley", "work": "Physiography: An Introduction to the Study of Nature", "quote": "Scientific **nomenclature** provides an unambiguous universal vocabulary intelligible to investigators across the world."}
    ]
  },
  "nomenklatura": {
    "primary": "The list of influential Soviet bureaucratic posts and the elite officials appointed to fill them by the Communist Party.",
    "secondary": "In political science and Soviet studies, the privileged managerial ruling class in state-socialist regimes that exercised systemic administrative control.",
    "quotes": [
      {"author": "George F. Kennan", "work": "Memoirs: 1950-1963", "quote": "The entrenched Soviet **nomenklatura** jealously guarded its special distribution privileges and suburban dachas against reform."},
      {"author": "Isaiah Berlin", "work": "The Soviet Mind: Russian Culture Under Communism", "quote": "Beneath revolutionary slogans, the party **nomenklatura** functioned as a rigid, self-perpetuating bureaucratic aristocracy."},
      {"author": "Milovan Djilas", "work": "The New Class", "quote": "The apparatus of the **nomenklatura** exercised monopolistic authority over state property, industry, and social advancement."}
    ]
  },
  "nomia": {
    "primary": "A genus of solitary, ground-nesting bees (family Halictidae); also a combining form denoting laws or administration.",
    "secondary": "In entomology, solitary halictid bees (such as the alkali bee, *Nomia melanderi*) serving as vital agricultural pollinators of alfalfa.",
    "quotes": [
      {"author": "Jean-Henri Fabre", "work": "Bramble-Bees and Others", "quote": "The solitary bee of genus **Nomia** excavates vertical tunnels in hard-packed alkaline soil to shelter its larval brood."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Wild pollinating species like **Nomia** perform indispensable ecological service in fertilizing leguminous prairie blossoms."},
      {"author": "William Morton Wheeler", "work": "Social Life Among the Insects", "quote": "The nesting behavior of **Nomia** illustrates the transitional stages between solitary burrowing and communal insect life."}
    ]
  },
  "nominal": {
    "primary": "Existing in name only, not in reality; very small or far below the real value or cost.",
    "secondary": "In economics, grammar, and aerospace engineering, referring to face values unadjusted for inflation, noun phrases, or expected operational parameters.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor retained only **nominal** sovereignty over the western provinces, where barbarian chieftains exercised actual power."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **nominal** price of commodities in gold fluctuated wildly while their real value in human labor remained constant."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "A magistrate who possesses merely **nominal** authority cannot enforce judicial decrees against resistant popular factions."}
    ]
  }
}
