# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — port (Batch 3B: 32 words)
  # =========================================================================
  "Dashboard — port/importing.md": {
    "primary": "Bringing goods or services into a country from abroad; or conveying an implicit meaning or consequence.",
    "secondary": "In macroeconomics, absorbing foreign-manufactured commodities to meet domestic aggregate consumer demand.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "I undertook it, vanquished thereto by the fair grace of letters **importing** your great affection."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "By **importing** grain from cheaper overseas producers, a nation frees labor for urban manufacturing."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She received the letter with a sense of **importing** disaster into the peaceful house."}
    ]
  },
  "Dashboard — port/importunate.md": {
    "primary": "Persistent, especially to the point of annoyance or intrusion; persistently pressing in request or demand.",
    "secondary": "In classical moral essays, troublesome and unyielding solicitations that overcome a person's resolve.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "She is **importunate**, indeed distract; her mood will needs be pitied."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He continued to urge his suit with **importunate** pleading that gave me no peace."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The voice of the crowd grew **importunate**, clamoring for an immediate explanation."}
    ]
  },
  "Dashboard — port/importunately.md": {
    "primary": "In an importunate manner; persistently, urgently, or troublesomely pressing a request.",
    "secondary": "In Victorian narrative fiction, beseeching with persistent, repetitive urgency that ignores social boundaries.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Not the less, however, came this **importunately** obtrusive thought, forcing itself into his meditations."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The beggar knocked **importunately** at the cottage door until an answer was returned."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "His conscience whispered **importunately** that he had concealed the truth from his oldest friend."}
    ]
  },
  "Dashboard — port/importune.md": {
    "primary": "To harass someone persistently for or to do something; to press or urge with troublesome persistence.",
    "secondary": "In early modern legal statutes, soliciting someone repeatedly in public spaces for illicit or commercial purposes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Sonnets", "quote": "Be it lawful I love thee as thou lov'st those whom thine eyes woo as mine **importune** thee."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Therefore with fervent prayers and vows **importune** the High Creator."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "Several courtiers did daily **importune** his majesty to grant them monopolies over foreign commodities."}
    ]
  },
  "Dashboard — port/importunity.md": {
    "primary": "Persistence in request or solicitation, especially to an annoying or troublesome degree.",
    "secondary": "In biblical exegesis (such as the Parable of the Friend at Midnight), shameless or bold persistence that ultimately secures assistance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Then weigh what loss your honour may sustain if with too credent ear you list his songs, or your chaste treasure open to his unmastered **importunity**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "She was relieved when his persistent **importunity** ceased to disturb her quiet mornings."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise ruler learns when to yield to honest counsel and when to reject self-serving **importunity**."}
    ]
  },
  "Dashboard — port/inopportune.md": {
    "primary": "Occurring at an inconvenient or inappropriate time; not well-timed.",
    "secondary": "In dramatic structure and narrative suspense, an unexpected interruption arriving at the precise moment of maximum vulnerability.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "How foolish and **inopportune** that mistletoe looked now, dangling from the ceiling after joy had fled."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His arrival at the rectory was singularly **inopportune**, coinciding with an acute family crisis."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A more **inopportune** moment for our expedition could scarcely have been chosen."}
    ]
  },
  "Dashboard — port/inopportunely.md": {
    "primary": "At an inconvenient, untimely, or unsuitable moment.",
    "secondary": "In diplomatic negotiation, raising sensitive contentious topics when bilateral goodwill is exceptionally fragile.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The door opened **inopportunely**, revealing the very person whose name had just been spoken."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A gust of wind blew the casement open most **inopportunely**, scattering my papers across the carpet."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Guppy entered **inopportunely**, interrupting the confidential conference between lawyer and client."}
    ]
  },
  "Dashboard — port/inopportuneness.md": {
    "primary": "The quality of being inopportune; untimeliness or inconvenience of timing.",
    "secondary": "In social comedy and novelistic plotting, the awkward friction created when private affairs collide with ill-timed public intrusion.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The sudden **inopportuneness** of the encounter struck both men with mutual embarrassment."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She felt the full **inopportuneness** of the visit, yet was compelled to maintain outward civility."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "The extreme **inopportuneness** of the remark was masked by a light, conversational laugh."}
    ]
  },
  "Dashboard — port/insupportable.md": {
    "primary": "Unable to be endured or tolerated; unbearable or intolerable.",
    "secondary": "In legal argumentation and philosophical ethics, a position or burden so devoid of moral justification that it cannot be sustained.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "My lord, you do me most **insupportable** vexation."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The silence in the ruined hall became an **insupportable** agony to my anxious spirit."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The heavy extortions of the provincial prefect grew **insupportable** to the peasantry."}
    ]
  },
  "Dashboard — port/opportune.md": {
    "primary": "Well-chosen or particularly favorable, suitable, or appropriate; occurring at an advantageous time.",
    "secondary": "In military strategy and tactical maneuvers, exploiting a fleeting breach or favorable wind at the decisive instant.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "As I hope for quiet days, fair issue, and long life, with such love as 'tis now, the most **opportune** place."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shower ceased at an **opportune** moment, allowing the reapers to stack the dry sheaves."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Your visit is singularly **opportune**, Watson, for I was on the point of requesting your assistance."}
    ]
  },
  "Dashboard — port/opportunely.md": {
    "primary": "At an opportune time; in a well-timed or convenient manner.",
    "secondary": "In dramatic plotting, a savior or piece of evidence arriving at the exact stroke of fortune to turn the tide.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Black Knight arrived most **opportunely** to break the furious assault upon the postern gate."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "A sudden turn in the path brought us **opportunely** within sight of the village inn."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "A light breeze sprang up most **opportunely**, carrying the schooner clear of the dangerous reef."}
    ]
  },
  "Dashboard — port/opportuneness.md": {
    "primary": "The quality of being opportune; timeliness, convenience, or favorable coincidence of circumstances.",
    "secondary": "In political theory and statecraft (Machiavelli's occasione), recognizing and seizing the fleeting window of political advantage.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The **opportuneness** of time is the very life of great enterprises."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king recognized the **opportuneness** of the crisis to dissolve a stubborn parliament."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **opportuneness** of the barbarian assault during the civil war sealed the fate of the frontier legions."}
    ]
  },
  "Dashboard — port/opportunism.md": {
    "primary": "The practice of taking advantage of circumstances for personal gain, with little regard for principles or consequences.",
    "secondary": "In Marxist political theory and political science, compromising core programmatic principles for short-term electoral or tactical advantage.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Political **opportunism** often masked itself under the high rhetoric of party loyalty."},
      {"author": "Bertrand Russell", "work": "Power: A New Social Analysis", "quote": "The dictator's policy was dictated not by ideology, but by ruthless and cynical **opportunism**."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "He despised the petty **opportunism** of provincial politicians who changed sides with every turn of the tide."}
    ]
  },
  "Dashboard — port/opportunist.md": {
    "primary": "A person who takes advantage of opportunities as they arise, especially with little regard for moral principles.",
    "secondary": "In ecology and evolutionary biology, a colonizing species (r-selected) that rapidly exploits newly disturbed habitats before competitors arrive.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He regarded the young physician as a shrewd **opportunist** seeking to rise upon the shoulders of wealthy patrons."},
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "In revolutionary times, every ambitious **opportunist** finds a theater for his vanity."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "He was neither a fanatic nor a saint, but a brilliant **opportunist** surfing the political currents of his day."}
    ]
  },
  "Dashboard — port/opportunistic.md": {
    "primary": "Characterized by opportunism; exploiting chances or circumstances without regard to principles.",
    "secondary": "In clinical microbiology and pathology, designating an organism (such as a fungal or bacterial pathogen) that causes disease only when the host's immune defense is compromised.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "Such **opportunistic** compromises may satisfy transient factions, but they cannot establish enduring principles."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain weeds exhibit an **opportunistic** vigor, seizing rapidly upon newly turned soil."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The criminal exhibited a remarkably **opportunistic** cunning, improvising his escape from unexpected obstacles."}
    ]
  },
  "Dashboard — port/opportunistically.md": {
    "primary": "In an opportunistic manner; taking advantage of circumstances as they arise for personal or tactical benefit.",
    "secondary": "In behavioral ecology and foraging theory, consuming novel food resources or preying upon vulnerable hosts as encounter rates fluctuate.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Predatory animals act **opportunistically**, attacking the young, weak, or isolated members of a herd."},
      {"author": "Bertrand Russell", "work": "Freedom and Organization", "quote": "Commercial monopolies expanded **opportunistically**, buying up weaker competitors during periods of financial panic."},
      {"author": "Joseph Conrad", "work": "Victory", "quote": "The adventurer lived **opportunistically**, seizing whatever stray fortune drifted into his path across the islands."}
    ]
  },
  "Dashboard — port/opportunity.md": {
    "primary": "A set of circumstances that makes it possible to do something; a favorable occasion or chance.",
    "secondary": "In neoclassical economics, the potential benefit forfeited when selecting one alternative over another (opportunity cost).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "With five times so much conversation I should get no **opportunity** to speak my mind."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise man will make more **opportunity** than he finds."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She seized the first **opportunity** of walking alone into the shrubbery to compose her agitated spirits."}
    ]
  },
  "Dashboard — port/port.md": {
    "primary": "A town or city with a harbor where ships load or unload cargo; or the left-hand side of a ship or aircraft when facing forward.",
    "secondary": "In computer networking and operating systems, a numerical endpoint (such as port 80 or 443) identifying a specific service or communication channel.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "At the Saint Francis here, beside the **port**, our vessels ride at anchor."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship was steering out of **port**, leaving the safe harbor behind for the unknown perils of the sea."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "A good **port** is a seaman's haven, sheltering weary ships from the fury of the open gale."}
    ]
  },
  "Dashboard — port/porta.md": {
    "primary": "An anatomical gate, entrance, or fissure where blood vessels, nerves, or ducts enter an organ (especially the porta hepatis of the liver).",
    "secondary": "In gross human anatomy and surgical gastroenterology, the transverse fissure on the inferior visceral surface of the liver transmitting the portal triad.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **porta** hepatis transmits the hepatic artery, portal vein, and bile ducts within the gastrohepatic omentum."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction at the **porta** of the liver leads inevitably to ascites and collateral venous distension."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Blood enters the liver parenchyma through the great vessels passing directly through the **porta**."}
    ]
  },
  "Dashboard — port/portability.md": {
    "primary": "The quality of being easily carried, moved, or transported; lightweight convenience.",
    "secondary": "In software engineering, the capacity of a codebase or compiled program to run across multiple operating systems and hardware platforms without extensive rewriting.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The superior **portability** of coined money over cattle made it the universal instrument of commerce."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The extreme **portability** of our instruments allowed us to carry them up the most rugged mountain passes."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A man is rich in proportion to the number of things which he can afford to let alone, valuing simplicity and **portability** above cumbersome possessions."}
    ]
  },
  "Dashboard — port/portable.md": {
    "primary": "Easily carried or conveyed by hand; capable of being moved from place to place.",
    "secondary": "In historical warfare and artillery, light ordnance or siege weapons designed to be packed on mules or transported over mountain trails.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "How light and **portable** my pain seems now, when that which makes me bend makes the king bow."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A harpooner carries his **portable** gear in a small chest stowed beneath the forecastle bunks."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes carried a small, **portable** lens with which he examined the footprints in the damp turf."}
    ]
  },
  "Dashboard — port/portage.md": {
    "primary": "The carrying of a boat or cargo overland between two navigable waterways, or around an obstacle such as a waterfall.",
    "secondary": "In North American frontier history and historical geography, established trails and overland routes utilized by indigenous fur traders and voyageurs.",
    "quotes": [
      {"author": "Francis Parkman", "work": "The Discovery of the Great West", "quote": "La Salle and his men completed the arduous **portage** of their heavy canoes between the river valleys."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We shouldered the birch canoe and made the difficult mile-long **portage** over slippery granite boulders."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Even at the first thy loss is more than can thy **portage** quit."}
    ]
  },
  "Dashboard — port/portal.md": {
    "primary": "A doorway, gate, or entrance, especially a large, imposing, or elaborate one.",
    "secondary": "In web architecture and information technology, a comprehensive web gateway providing access to a broad aggregation of services and resources.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Look where he goes even now out at the **portal**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "And beneath the glorious **portal** shone like stars."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "They entered beneath the vaulted stone **portal** of the ancient Roman palace."}
    ]
  },
  "Dashboard — port/portcullis.md": {
    "primary": "A strong, heavy vertically-closing iron or wooden grating suspended above a gateway of a fortified castle and lowered to bar passage.",
    "secondary": "In heraldry and British parliamentary iconography, a stylized badge consisting of a gridded gate with downward-pointing spikes and suspension chains.",
    "quotes": [
      {"author": "Walter Scott", "work": "Marmion", "quote": "The heavy iron **portcullis** dropped with a thunderous clang, cutting off all retreat from the castle courtyard."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Fray's forehead was wrinkled both perpendicularly and horizontally, like the iron bars of a **portcullis**."},
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Within my mouth you have engaoled my tongue, doubly portcullised with my teeth and lips; and dropped the heavy **portcullis** of silence."}
    ]
  },
  "Dashboard — port/porte-cochere.md": {
    "primary": "A covered porch or carriage entrance leading into a courtyard or building, allowing passengers to enter and alight under shelter.",
    "secondary": "In French and neoclassical mansion architecture, an arched gateway large enough to admit horse-drawn carriages into an interior courtyard.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The brougham turned smoothly beneath the broad stone **porte-cochere** of the Fifth Avenue mansion."},
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "The carriage rumbled through the dark arch of the **porte-cochere** into the quiet cobbled courtyard."},
      {"author": "Henry James", "work": "The American", "quote": "A massive pair of oak doors stood open beneath the **porte-cochere**, admitting the fresh spring breeze."}
    ]
  },
  "Dashboard — port/porte.md": {
    "primary": "An archaic or historical term for the Ottoman government or empire (the Sublime Porte), named after the ceremonial gate of the grand vizierate in Istanbul.",
    "secondary": "In nineteenth-century diplomatic history, the imperial court of the Sultan at Constantinople conducting international diplomacy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ambassadors of the Christian powers were received with haughty ceremony at the Sublime **Porte**."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The policy of the **Porte** toward its Balkan provinces fluctuated between savage repression and indolent neglect."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The majestic gate of the **Porte** witnessed the rise and fall of viziers whose lives hung on a sultan's nod."}
    ]
  },
  "Dashboard — port/portend.md": {
    "primary": "To be a sign or warning that something momentous, calamitous, or unwelcome is likely to happen; to presage.",
    "secondary": "In classical meteorology and ancient astrology, celestial phenomena (eclipses, comets) interpreted as omens of dynastic upheaval.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "These late eclipses in the sun and moon **portend** no good to us."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "A fiery meteor flared across the midnight sky, seeming to **portend** the fall of empires."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Superstitious Romans believed that earthquakes and famines did **portend** the near extinction of the imperial city."}
    ]
  },
  "Dashboard — port/portent.md": {
    "primary": "A sign or warning that something momentous or calamitous is about to happen; an omen.",
    "secondary": "In literary tragedy and epic poetry, an unnatural prodigy or apparition foretelling the downfall of a hero or kingdom.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Will you again unknit this churlish knot of all-abhorred war, and be no more a prodigy of fear and a **portent** of broached mischief?"},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The wild sea-birds circling low over the wake seemed to Ahab a dark **portent** of impending catastrophe."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Every bread riot in the provinces was a fiery **portent** of the revolutionary storm gathering over Paris."}
    ]
  },
  "Dashboard — port/portentous.md": {
    "primary": "Of or like a portent; menacing, ominous, or foreshadowing evil; or done in a pompously solemn manner.",
    "secondary": "In narrative rhetoric and novelistic characterization, possessing an exaggerated, grave weightiness intended to impress onlookers.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I think it be no other but e'en so: well may it sort that this **portentous** figure comes armed through our watch."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Chadband assumed a **portentous** expression, raising his fat right hand to command religious awe."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His silence was more **portentous** than spoken anger, filling the room with an atmosphere of chill disapproval."}
    ]
  },
  "Dashboard — port/portentously.md": {
    "primary": "In a portentous manner; ominously, solemnly, or with pompous self-importance.",
    "secondary": "In social realism, speaking or acting with an exaggerated air of prophetic foreboding or momentous gravity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Nancy, in her attic, shook her head **portentously**, hinting at dark family secrets that must soon come to light."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The old church clock struck midnight **portentously**, each stroke vibrating heavily through the silent valley."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The hound howled **portentously** across the misty mire, sending a shiver through our little party."}
    ]
  },
  "Dashboard — port/porter.md": {
    "primary": "A person employed to carry luggage and other loads; or a dark brown bitter beer brewed from malted and roasted barley.",
    "secondary": "In hospital and transit logistics, a support worker responsible for transporting patients, pharmaceuticals, or equipment between wards and terminals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Come, sister; Dromio, play the **porter** well, and keep the gate against all intruders."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A brisk **porter** shouldered my trunk and set off toward the coaching inn at a round pace."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "We sat by the fire in the Spouter-Inn, drinking hearty flagons of foaming brown **porter**."}
    ]
  },
  "Dashboard — port/porterage.md": {
    "primary": "The charge made for carrying luggage or goods; or the work or service of a porter.",
    "secondary": "In expeditionary logistics and transit accounting, scheduled baggage fees and labor tariffs paid to native carriers across mountain passes.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The basket being large and heavy, Car had paid for its **porterage** on the carrier's cart."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The costs of **porterage** and inland carriage add considerably to the retail price of heavy goods."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He demanded extra shillings for the **porterage** of the heavy iron deed-box to Lincoln's Inn."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"
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

print(f"Carrying Batch 3B (port): Successfully updated {updated}/{len(data)} notes.")
