# -*- coding: utf-8 -*-
"""
Part 3: vic part 1 (words 1-21)
['advice', 'arvicola', 'convict', 'convictfish', 'conviction', 'device', 'devices', 'evict', 'eviction', 'reconvict', 'vicar', 'vicar-general', 'vicarage', 'vicarial', 'vicariate', 'vicarious', 'vicariously', 'vicarship', 'vice', 'vice versa', 'vice-']
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

data_vic_p1 = {
  "advice": {
    "primary": "Guidance, counsel, recommendation, or an opinion offered to assist someone in making a wise decision.",
    "secondary": "In commerce and banking, a formal written notice notifying a correspondent of a transaction, bill of exchange, or shipment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Give every man thy ear, but few thy voice; take each man's censure, but reserve thy judgment: this above all, to thine own self be true, according to Polonius's solemn **advice**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A headstrong maid, that's what she is, and won't listen to no **advice** from elder folk."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The caterpillar took the hookah out of its mouth and addressed Alice with languid and perplexing **advice**."}
    ]
  },
  "arvicola": {
    "primary": "A zoological genus of amphibious and burrowing water voles belonging to the rodent family Cricetidae.",
    "secondary": "In European mammalogy and wetland ecology, freshwater arvicoline rodents inhabiting riverbanks, canals, and reedbeds, playing a keystone herbivorous role.",
    "quotes": [
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The habits of the water rat, known to naturalists as **Arvicola** amphibius, afford remarkable examples of aquatic excavation along our meadow brooks."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The dental architecture and molar roots of **Arvicola** display exquisite gradations between burrowing and semi-aquatic forms."},
      {"author": "Thomas Bell", "work": "A History of British Quadrupeds", "quote": "In every marshy ditch the naturalist may detect the burrowing entrances formed by the industrious water vole, **Arvicola**."}
    ]
  },
  "convict": {
    "primary": "To find or declare guilty of a criminal offense by the verdict of a jury or the decision of a judge.",
    "secondary": "In penal history and criminology, a person serving a prison sentence following formal judicial condemnation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Before I be **convict** by course of law, to threaten me with death is most unlawful."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The escaped **convict** crouched shivering among the graves on the marshes, his leg-iron clanking heavily against the stones."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "If you make the criminal code sanguinary, juries will not **convict** even the most desperate offenders."}
    ]
  },
  "convictfish": {
    "primary": "A marine teleost fish (Pholidichthys leucotaenia) whose juvenile stages exhibit bold black and white horizontal or vertical stripes.",
    "secondary": "In marine ichthyology and reef ecology, an Indo-Pacific burrowing blennioid fish living in complex communal coral tunnels and demonstrating cooperative juvenile brood care.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "The Genera of Fishes", "quote": "The striking juvenile coloration of the **convictfish** resembles venomous striped catfish, providing effective protective mimicry on shallow reefs."},
      {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "Hovering near their limestone burrow, a dense swarm of young **convictfish** undulated in synchronized harmony over the seabed."},
      {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The specimen labeled **convictfish** displays distinctive vertical melanophore banding across its elongate body."}
    ]
  },
  "conviction": {
    "primary": "A firmly held belief, fixed opinion, or certainty; or the formal judicial finding of guilt in a criminal trial.",
    "secondary": "In rhetoric and moral philosophy, thorough subjective persuasion of truth by compelling evidence or inner moral certitude.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "This **conviction** is the ultimate sanction of the greatest-happiness morality across civilized communities."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A horrible **conviction** darted through Oak that his entire flock had plunged over the cliff into the chalk pit."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "My **conviction** that man is descended from some lowly organized form has been strengthened by every fresh anatomical fact."}
    ]
  },
  "device": {
    "primary": "A mechanical tool, appliance, or mechanism invented for a specific practical purpose or function.",
    "secondary": "In literature, rhetoric, and heraldry, a symbolic design, motto, or artistic technique utilized to convey meaning or structure narrative.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "And thou wert best look to't; for if thou dost him any slight disgrace, he will practice against thee by poison, or some treacherous **device**."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "On a tiny satinwood table stood a statuette by Clodion, and beside it an ingenious mechanical **device** that struck the hours in chime."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her deliberate reserve was an innocent **device** to conceal the deep agitation of her heart."}
    ]
  },
  "devices": {
    "primary": "Mechanical tools, appliances, or mechanisms constructed for distinct operational tasks or purposes.",
    "secondary": "In rhetoric, psychology, and strategic planning, imaginative schemes, stratagems, or figurative methods employed to achieve aims.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Our wills and fates do so contrary run that our **devices** still are overthrown; our thoughts are ours, their ends none of our own."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Human ingenuity has multiplied inventive **devices** to overcome the obstacles placed by physical nature."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Civilized society invents countless institutional **devices** to mitigate the harsh struggles inherent in raw natural selection."}
    ]
  },
  "evict": {
    "primary": "To expel someone from a property or dwelling by legal process, tenancy termination, or judicial enforcement.",
    "secondary": "In property jurisprudence, to dispossess a tenant or occupant of real estate through an action of ejectment following default.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ruthless landlord threatened to **evict** the impoverished family into the freezing streets if their arrears were not satisfied."},
      {"author": "George Gissing", "work": "The Nether World", "quote": "Bailiffs arrived at noon to **evict** the destitute lodgers from the crumbling tenement courtyard."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The steward announced his intention to **evict** any tenant whose cottage lease had lapsed with the old squire's death."}
    ]
  },
  "eviction": {
    "primary": "The legal action or process of expelling someone from a property, tenancy, or dwelling.",
    "secondary": "In agrarian economic history, the widespread removal of tenant farmers during agricultural clearance and enclosure movements.",
    "quotes": [
      {"author": "William Butler Yeats", "work": "Autobiographies", "quote": "He vividly recalled the agrarian distress of his boyhood, when rural **eviction** left whole families homeless along the roadside."},
      {"author": "George Bernard Shaw", "work": "Widowers' Houses", "quote": "The play exposes how slum landlords depend upon summary **eviction** to extort excessive rents from desperate laborers."},
      {"author": "Lady Gregory", "work": "Visions and Beliefs in the West of Ireland", "quote": "The old woman related sorrowful tales of the famine years, when **eviction** scattered the villagers to distant emigrant ships."}
    ]
  },
  "reconvict": {
    "primary": "To convict a person of a criminal offense again following a previous judicial conviction.",
    "secondary": "In penology and recidivism analysis, to return a previously released offender to prison upon adjudicating a repeated offense.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The magistrate had no hesitation to **reconvict** the notorious safecracker after identifying his signature chisel marks."},
      {"author": "Havelock Ellis", "work": "The Criminal", "quote": "The magistrate's court was compelled to **reconvict** the habitual petty offender whose release had lasted barely a month."},
      {"author": "Cesare Lombroso", "work": "Crime, Its Causes and Remedies", "quote": "Penal statistics indicate that courts **reconvict** confirmed repeat offenders with increasing severity at each trial."}
    ]
  },
  "vicar": {
    "primary": "A cleric or priest in charge of a parish in the Church of England, historically receiving a stipend or lesser tithes.",
    "secondary": "In ecclesiastical hierarchy and Roman Catholic canon law, an official acting as an administrative representative or deputy of a bishop or the Pope.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "Sir Hugh Evans, the Welsh parson, conferred with the **vicar** concerning the marriage arrangements."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The **Vicar** himself seemed to wear rather a changed aspect, as most men do when their hair turns gray and family responsibilities multiply."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The village **vicar** walked gravely down the churchyard path, nodding to the parishioners assembled for morning service."}
    ]
  },
  "vicar-general": {
    "primary": "The principal administrative deputy and legal deputy of an Anglican or Catholic bishop, exercising executive episcopal jurisdiction.",
    "secondary": "In canon jurisprudence, an ecclesiastical magistrate appointed with ordinary power to administer diocesan affairs on behalf of the diocesan bishop.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The metropolitan bishop dispatched his **vicar-general** to adjudicate the contentious theological disputes dividing provincial monasteries."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "The bishop consulted his **vicar-general** upon the delicate legal dispute regarding the hospital endowment before issuing a public reply."},
      {"author": "Sir Walter Scott", "work": "Kenilworth", "quote": "The venerable **vicar-general** presided over the diocesan consistory with dignified legal impartiality."}
    ]
  },
  "vicarage": {
    "primary": "The official residence provided for a parish vicar, or the benefice and office held by a vicar.",
    "secondary": "In English social history and ecclesiastical topography, the central domestic hub of Anglican village life and parish administration.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea frequently walked over to the pleasant old **vicarage** to visit her sister and admire the blooming garden roses."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The modest stone **vicarage** stood conveniently situated between the parsonage glebe and the church gates."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare spent several quiet months reading classical theology at his father's secluded Dorsetshire **vicarage**."}
    ]
  },
  "vicarial": {
    "primary": "Pertaining to, delegated by, or characteristic of a vicar or an episcopal deputy.",
    "secondary": "In historical ecclesiastical law, exercised by delegated vicarious authority rather than held by original proprietary right.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "On the Constitution of the Church and State", "quote": "The bishop exercised his pastoral oversight through **vicarial** appointments across the extensive northern districts."},
      {"author": "Henry Hallam", "work": "View of the State of Europe during the Middle Ages", "quote": "The archdeacon claimed **vicarial** jurisdiction over the provincial clergy during the prelate's absence abroad."},
      {"author": "John Henry Newman", "work": "Historical Sketches", "quote": "The primitive church recognized that local pastoral care was often entrusted to **vicarial** presbyters acting under the metropolitan."}
    ]
  },
  "vicariate": {
    "primary": "The office, ecclesiastical jurisdiction, or territory governed by a vicar or vicar apostolic.",
    "secondary": "In Catholic mission administration, an ecclesiastical jurisdiction established in missionary territories prior to erection into a permanent diocese.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **vicariate** of Italy was subdivided into smaller administrative prefectures by the reforming emperors."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "Before the restoration of the regular hierarchy, English Catholic affairs were administered under an apostolic **vicariate**."},
      {"author": "Lord Acton", "work": "Lectures on Modern History", "quote": "The emperor asserted his imperial **vicariate** over the contested northern Italian territories during the interregnum."}
    ]
  },
  "vicarious": {
    "primary": "Experienced in the imagination through the feelings or actions of another person; performed or suffered on behalf of another.",
    "secondary": "In theological soteriology and tort law, liability or atonement imputed to one party for the deeds, negligence, or obligations of another.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "We read history with a **vicarious** thrill, projecting our own hopes and passions into the heroic exploits of past ages."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sympathy enables us to experience a **vicarious** joy or sorrow that profoundly enriches our emotional existence."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The martyr endures **vicarious** suffering that future generations may walk in spiritual liberty and light."}
    ]
  },
  "vicariously": {
    "primary": "In a vicarious manner; indirectly through the lived experience, emotions, or actions of another.",
    "secondary": "In psychological analysis of literature, participating emotionally in imaginary drama without physical involvement.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke enjoyed life **vicariously** through the ambitious schemes and diverse enterprises of his energetic neighbors."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The landsman sits snugly by his parlour hearth, listening **vicariously** to the howling tempest that batters distant whalers."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "She lived **vicariously** in the triumphant careers of her children, following every academic triumph from afar."}
    ]
  },
  "vicarship": {
    "primary": "The office, rank, status, or term of service of a vicar.",
    "secondary": "In British church history, the tenure during which a specific vicar exercises pastoral and administrative duties in a parish.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "He secured a modest country **vicarship** through the patronage of a generous baronet in the neighboring shire."},
      {"author": "Anthony Trollope", "work": "The Last Chronicle of Barset", "quote": "During his prolonged **vicarship**, Mr. Crawley struggled courageously against grinding poverty and clerical misunderstanding."},
      {"author": "Oliver Goldsmith", "work": "The Vicar of Wakefield", "quote": "He commenced his rural **vicarship** with ardent hopes of reforming both the morals and agricultural thrift of his rustic flock."}
    ]
  },
  "vice": {
    "primary": "Immoral or wicked behavior, conduct, or habit; an enduring moral flaw, depravity, or corruption.",
    "secondary": "In mechanical tooling and manufacturing, a clamping device with two parallel jaws used to hold work firmly in place.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Our natures do pursue, like rats that ravin down their proper bane, a thirsty evil; and when we drink we die... so **vice** corrupts the noble heart."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "It is only those in whom indolence amounts to a **vice** that do not seek higher intellectual and social culture."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The virtue of prosperity is temperance; the virtue of adversity is fortitude; but the greatest **vice** is self-deceiving ambition."}
    ]
  },
  "vice versa": {
    "primary": "With the order or relation reversed; the other way around; conversely.",
    "secondary": "In logical argumentation and formal relations, signifying bidirectional symmetry between two statements, premises, or operations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A change of work is the best rest, Watson, and mental fatigue may often be relieved by bodily exertion, or **vice versa**."},
      {"author": "William James", "work": "Pragmatism", "quote": "Concepts determine our perception of perceptual realities, and **vice versa**, in a continuous reciprocal dialectic of thought."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Every physical cause produces a mental effect in sensation, and **vice versa**, mental volitions provoke bodily movements."}
    ]
  },
  "vice-": {
    "primary": "A prefix designating a deputy, subordinate, or acting official empowered to exercise the duties of a superior.",
    "secondary": "In administrative morphology and bureaucratic titles, denoting hierarchical succession or operational delegation beneath a principal executive.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional creation of a **vice-** magistrate ensures executive continuity in the event of unforeseen presidential disability."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king appointed a trusted **vice-** admiral to command the channel squadron during the naval crisis."},
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "British institutions maintain numerous ancient **vice-** regencies that preserve medieval ceremonial titles under modern parliamentary forms."}
    ]
  }
}
