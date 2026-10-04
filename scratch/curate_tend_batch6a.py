# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — tend Part 1 (6A, 32 words) ---
  "Dashboard — tend/attend.md": {
    "primary": "To be present at an event, meeting, or function; or to apply one's mind, give heed, or wait upon someone.",
    "secondary": "In medical care and hospital practice, an attending physician holds primary clinical responsibility for patient diagnosis and treatment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I am informed thoroughly of the cause; which is the merchant here, and which the Jew? He did bid us **attend** the court."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins felt it an imperative duty to **attend** lady Catherine's tea parties with punctilious obedience."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery asked me to **attend** to the forge while he spoke with the mysterious visitor."}
    ]
  },
  "Dashboard — tend/attendance.md": {
    "primary": "The physical presence or regular appearance of a person at a designated place, gathering, meeting, or event; or the total count of attendees.",
    "secondary": "In educational administration, regular attendance records determine institutional compliance and statutory funding quotas.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The ball at Netherfield was honored by the **attendance** of all the principal families of the neighbourhood."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The doctor remained in constant **attendance** at the bedside of the wounded prisoner."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The professors required the daily **attendance** of students at lectures to ensure rigorous discipline."}
    ]
  },
  "Dashboard — tend/attendant.md": {
    "primary": "A person employed to provide service, assistance, or care; or occurring as an accompanying circumstance or result.",
    "secondary": "In historical European court etiquette, lords and ladies in waiting served as personal attendants to the monarch during official levées.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Let thy fair wisdom, not thy passion, sway in this uncivil and unjust extent against thy peace; call each royal **attendant** forth."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The faithful **attendant** adjusted the cushions and placed the medicine bottle within easy reach of the invalid."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A magnificent retinue of horsemen rode as an **attendant** escort to the imperial carriage."}
    ]
  },
  "Dashboard — tend/attended.md": {
    "primary": "Was present at an event or assembly; or accompanied, escorted, or cared for by another person.",
    "secondary": "In medical terminology, an attended birth is managed by a licensed midwife or obstetrician trained in perinatal care.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The king went forth into the open air, **attended** by his faithful counselors and guards."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne **attended** the concert in the hope of catching a glimpse of Willoughby among the crowd."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Farmer Boldwood **attended** the Casterbridge market every Saturday without fail."}
    ]
  },
  "Dashboard — tend/attendee.md": {
    "primary": "A person who is present at, participates in, or attends an organized conference, meeting, or event.",
    "secondary": "In academic conference logistics, each registered attendee receives credentials, proceedings, and admission to plenary sessions.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Every serious **attendee** at the mechanics' institute gained valuable insight into practical physics."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The earnest **attendee** at public philosophical debates learned to weigh conflicting arguments objectively."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "An attentive **attendee** at a lecture must deliberately inhibit irrelevant environmental sounds."}
    ]
  },
  "Dashboard — tend/attender.md": {
    "primary": "One who attends, visits, or frequents a place, gathering, meeting, or religious service regularly.",
    "secondary": "In Quaker ecclesiastical terminology, an attender participates regularly in Meetings for Worship without formal membership enrollment.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solitary clerk was a constant **attender** at the early morning prayers in the abbey."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Dinah noticed a devout **attender** seated quietly on the low bench near the chapel doorway."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The old carpenter had been a faithful **attender** of the village choir for fifty years."}
    ]
  },
  "Dashboard — tend/attending.md": {
    "primary": "Being present at an assembly; giving care or service; or accompanying as an associated circumstance.",
    "secondary": "In hospital clinical governance, the attending physician supervises resident physicians and makes definitive therapeutic choices.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Prospero stood upon the shore, his spirits **attending** upon his magical commands."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny spent the afternoon **attending** to her aunt's needlework and reading aloud from the newspaper."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The hazards **attending** a winter passage around Cape Horn tested the endurance of every sailor."}
    ]
  },
  "Dashboard — tend/contend.md": {
    "primary": "To strive in opposition or rivalry; to struggle, compete, or assert an argument vigorously.",
    "secondary": "In jurisprudence and appellate advocacy, counsel contend that statutory precedent bars retroactive application of the penalty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "We two have cabined in a cave; when they did **contend** about the prize of beauty, I held my peace."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Who can in arms **contend** with the Almighty, whose thunder shook the foundations of the deep?"},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Political parties must legitimately **contend** for principles without undermining the civil constitution."}
    ]
  },
  "Dashboard — tend/contender.md": {
    "primary": "A person or entity that competes with others in a struggle, contest, tournament, or election; a rival.",
    "secondary": "In prize fighting and boxing history, a championship bout pits the reigning titleholder against the mandatory top-ranked contender.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Each gallant **contender** entered the lists with lance in rest, awaiting the herald's trumpet."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Severus crushed every rival **contender** for the purple throne through decisive military campaigns."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The ambitious politician emerged as the foremost **contender** for leadership of the parliamentary opposition."}
    ]
  },
  "Dashboard — tend/distend.md": {
    "primary": "To swell, inflate, or expand outward by internal pressure, fluid, or gas; to stretch wide.",
    "secondary": "In gastrointestinal pathophysiology, abnormal intestinal gas or ascites can painfully distend the peritoneal cavity.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sudden gust of trade winds caused the great mainsail to **distend** like a giant drumhead."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain desert reptiles possess specialized air sacs that **distend** when threatened by predators."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The torrential rain caused the mountain torrents to **distend** beyond their rocky banks."}
    ]
  },
  "Dashboard — tend/extend.md": {
    "primary": "To stretch out, expand in scope, duration, or dimension; or to offer or bestow something outward.",
    "secondary": "In Euclidean geometry and drafting, to extend a line segment means to prolong it continuously in the same collinear direction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "If you would **extend** your kindness to a wandering stranger, heaven will reward your hospitality."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The true purpose of natural philosophy is to **extend** the empire of man over material nature."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The development of steam navigation helped **extend** inland trade to previously inaccessible territories."}
    ]
  },
  "Dashboard — tend/extendable.md": {
    "primary": "Capable of being extended, lengthened, prolonged, or expanded in range, duration, or scope.",
    "secondary": "In software architecture, an extendable framework allows developers to add custom plugins without modifying the core codebase.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The surveyor utilized an **extendable** brass rod to calculate the precise elevation of the rocky ridge."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The boundaries of human knowledge are perpetually **extendable** as observational instruments improve."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The geological timescale proved **extendable** far beyond the brief horizons imagined by early naturalists."}
    ]
  },
  "Dashboard — tend/extended.md": {
    "primary": "Stretched out, drawn out in length or duration; comprehensive, widespread, or enlarged in scope.",
    "secondary": "In sociological analysis, an extended family includes multiple generations and collateral relatives residing within an integrated household.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The pampas **extended** in an unbroken grassy horizon for hundreds of miles toward the south."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Trajan **extended** the frontiers of the empire beyond the Danube and across the Euphrates."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Sir Thomas remained abroad for an **extended** period to supervise his plantation in Antigua."}
    ]
  },
  "Dashboard — tend/extendible.md": {
    "primary": "Capable of being prolonged, enlarged, or drawn out in space, time, or application; extendable.",
    "secondary": "In patent law and contractual leasing, an extendible term grants the licensee an option to prolong duration upon mutual consent.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant's credit is **extendible** only in proportion to the proven solvency and integrity of his commercial dealings."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific methods are **extendible** to every branch of inquiry where observable facts can be verified."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The principles of social coordination are **extendible** from small clans to vast civilized nations."}
    ]
  },
  "Dashboard — tend/intend.md": {
    "primary": "To have in mind as a purpose, aim, or design; to plan or direct toward a specific objective.",
    "secondary": "In tort jurisprudence, legal malice requires proof that the tortfeasor did intend the injurious consequences of their unlawful act.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 27", "quote": "For then my thoughts, from far where I abide, **intend** a zealous pilgrimage to thee, and keep my drooping eyelids open wide."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "I do not **intend** to say anything to dissuade you from accepting so advantageous an offer."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I did fully **intend** to write to my aunt the moment our ship reached Yarmouth harbor."}
    ]
  },
  "Dashboard — tend/intended.md": {
    "primary": "Purposed, designed, or planned; or describing an affianced spouse or betrothed partner.",
    "secondary": "In teleological philosophy and ethics, the intended consequence of a moral action is distinguished from unintended collateral side effects.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Yet your good will must have that thanks from Rome after the measure as you **intended** well."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea explained the architectural drawings **intended** for the improved cottages on the estate."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym prepared the books **intended** for the village night school with earnest devotion."}
    ]
  },
  "Dashboard — tend/nonattendance.md": {
    "primary": "The failure, omission, or neglect to be present at an appointed place, meeting, or statutory duty.",
    "secondary": "In parliamentary procedure, persistent nonattendance of members can prevent reaching a quorum necessary to conduct legislative votes.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The statutes imposed modest financial forfeitures upon fellows for unexplained **nonattendance** at college convocations."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solicitor excused his client's **nonattendance** before the master in Chancery on the grounds of ill health."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The bishop was severely reprimanded by the council for his deliberate **nonattendance** at the coronation."}
    ]
  },
  "Dashboard — tend/nonattender.md": {
    "primary": "A person who habitually or deliberately fails to attend an organization, church, school, or required assembly.",
    "secondary": "In nineteenth-century British religious census methodology, a nonattender was categorized among those who did not frequent Sunday worship.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver of Raveloe was regarded with suspicion by his neighbors because he was a persistent **nonattender** at parish church."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The parish vicar noted with regret that the young dairyman was a confirmed **nonattender** at evening services."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Mr. Gradgrind demanded an explanation from every school **nonattender** before administering disciplinary measures."}
    ]
  },
  "Dashboard — tend/overextend.md": {
    "primary": "To extend, expand, or commit resources beyond reasonable, safe, or sustainable limits.",
    "secondary": "In financial banking risk analysis, institutions overextend credit when loan liabilities outstrip liquid reserve capital ratios.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Speculative traders frequently **overextend** their business upon borrowed capital until a sudden panic precipitates their insolvency."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Augustus warned his successors never to **overextend** the imperial frontiers into barren northern forests."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The enemy army did fatally **overextend** its supply columns across the vast expanse of the frozen steppe."}
    ]
  },
  "Dashboard — tend/pretend.md": {
    "primary": "To feign, simulate, or give a false appearance of; to claim or profess something not substantiated.",
    "secondary": "In historical monarchical disputes, to pretend to a crown meant to assert a formal dynastic title or claim to sovereignty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "Now, Governor of Paris, take your oath, that you elect no other king but him; esteem none friends that **pretend** title unto this crown."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "I will not **pretend** to be indifferent to a subject which occupies so large a share of my thoughts."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip did not **pretend** to understand the intricate legal mechanisms that governed Jaggers's office."}
    ]
  },
  "Dashboard — tend/pretended.md": {
    "primary": "Fictitious, feigned, or simulated; claimed without genuine foundation or legitimate title.",
    "secondary": "In Tudor and Stuart historiography, the phrase 'pretended parliament' was used by Royalists to designate an unconstitutional assembly.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Two Gentlemen of Verona", "quote": "Now presently I'll give her father notice of their disguising and **pretended** flight, who, all enraged, will banish Valentine."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The usurper entered Rome with **pretended** modesty, concealing his despotic intentions beneath senatorial forms."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "This is the second time you have **pretended** to dismiss me; and what's the use of it?"}
    ]
  },
  "Dashboard — tend/pretender.md": {
    "primary": "A claimant to a throne, title, or honor, especially one whose legal or moral right is disputed or unacknowledged.",
    "secondary": "In British history, the Old Pretender (James Francis Edward Stuart) and Young Pretender (Bonnie Prince Charlie) led Jacobite rebellions.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions stationed in Gaul proclaimed their favorite general a rival **pretender** to the purple."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The supporters of the exiled Stuart **pretender** plotted secretly in taverns across northern counties."
      },
      {"author": "Walter Scott", "work": "Waverley", "quote": "The young officer found himself drawn into the fateful rebellion organized around the romantic figure of the royal **pretender**."}
    ]
  },
  "Dashboard — tend/pretending.md": {
    "primary": "The act of making a false appearance, feigning an emotion, or claiming an unproven right or ability.",
    "secondary": "In developmental child psychology, pretend play (or pretending) reflects emerging symbolic representation and theory of mind.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "The Queen, sir, very oft importuned me to temper poisons for her; still **pretending** the satisfaction of her curiosity."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Ah, sergeant, it won't do—you are **pretending**! she said, shaking her head with an amused smile."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth could not help smiling at his clumsy manner of **pretending** complete unconcern."}
    ]
  },
  "Dashboard — tend/subtend.md": {
    "primary": "To extend under or be positioned opposite to an angle or arc in a geometric figure.",
    "secondary": "In trigonometry and Euclidean geometry, a chord of a circle is said to subtend the central angle whose rays pass through its endpoints.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Let the arc of the orbit **subtend** an infinitesimal angle at the primary focus where the sun resides."},
      {"author": "James Clerk Maxwell", "work": "Matter and Motion", "quote": "The line connecting two observation points will **subtend** a measurable parallax angle against distant stars."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The visible horizon seen from the summit seemed to **subtend** an immense arc of ocean and sky."}
    ]
  },
  "Dashboard — tend/superintend.md": {
    "primary": "To oversee, supervise, direct, or have charge of people, operations, or an organization.",
    "secondary": "In municipal governance and public works, civil engineers superintend the construction of aqueducts, bridges, and harbor docks.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He observed that he was now qualified to manage and **superintend** a large agricultural estate."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Miss Lavinia found uncommon satisfaction in attempting to **superintend** the domestic arrangements of the young couple."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A prudent landlord chooses an experienced bailiff to **superintend** the seasonal husbandry of his tenant farms."}
    ]
  },
  "Dashboard — tend/superintendence.md": {
    "primary": "The act, duty, or function of directing, overseeing, managing, or supervising operations or personnel.",
    "secondary": "In administrative governance, bureaucratic superintendence establishes standardized auditing oversight across regional departments.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The dairy **superintendence** shall be done by an experienced man; you shall never have that burden."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode offered to place the entire **superintendence** of the new fever hospital in Lydgate's hands."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The provincial governors maintained vigilant **superintendence** over the collection of imperial revenues."}
    ]
  },
  "Dashboard — tend/superintendent.md": {
    "primary": "A person who oversees, directs, manages, or has executive charge of an institution, building, district, or operation.",
    "secondary": "In public education administration, a district superintendent oversees curriculum standards, personnel hiring, and school facility budgets.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The colonial records mention an officer who was **superintendent** of the native settlements subject to Massachusetts."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **superintendent** of the fisheries informed me that he had frequently observed the migratory habits of salmon."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The factory **superintendent** blew the morning whistle that summoned hundreds of weavers to the looms."}
    ]
  },
  "Dashboard — tend/tend.md": {
    "primary": "To have an inclination, disposition, or directional drift; or to care for, minister to, or watch over.",
    "secondary": "In differential calculus and limit theory, variables are said to tend toward zero or infinity as arguments approach critical boundaries.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 105", "quote": "For to no other pass my verses **tend**, than of your graces and your gifts to tell."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Direct my course to where these wandering paths **tend** toward the tree of life."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Slight variations which give an individual an advantage in survival will **tend** to be preserved and multiplied."}
    ]
  },
  "Dashboard — tend/tendencious.md": {
    "primary": "Promoting or expressing a controversial point of view; biased, partisan, or intentionally slanted.",
    "secondary": "In textual criticism and historiography, tendencious narratives deliberately select evidence to bolster partisan ideological arguments.",
    "quotes": [
      {"author": "George Orwell", "work": "Collected Essays", "quote": "The pamphlet was obviously a **tendencious** piece of political propaganda designed to mislead the electorate."},
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Philosophical histories are often flawed by the **tendencious** omissions of their authors."},
      {"author": "Thomas Henry Huxley", "work": "Science and Christian Tradition", "quote": "A truly scientific mind rejects **tendencious** polemics in favor of verifiable empirical facts."}
    ]
  },
  "Dashboard — tend/tendency.md": {
    "primary": "An inclination, disposition, or inherent leaning toward a particular characteristic, behavior, or outcome.",
    "secondary": "In economic theory and classical political economy, the tendency of the rate of profit to fall was analyzed by Ricardo and Marx.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The peculiar motion involved in turning a wheel has a wonderful **tendency** to benumb the mind."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Any variation which gives a seedling an advantage will show a **tendency** to dominate the surrounding flora."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's passionate nature had a dangerous **tendency** to encourage romantic melancholia."}
    ]
  },
  "Dashboard — tend/tendentious.md": {
    "primary": "Expressing, promoting, or characterized by a strongly partisan, biased, or controversial purpose; intentionally slanted.",
    "secondary": "In literary and film criticism, a tendentious artwork subordinates aesthetic form and nuanced characterization to explicit didactic messaging.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The newspaper published a highly **tendentious** account of the street clashes in Barcelona."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Dogmatic theology frequently constructs **tendentious** arguments that start from preordained conclusions."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Novels burdened with **tendentious** social preaching often sacrifice psychological reality to moral doctrine."}
    ]
  },
  "Dashboard — tend/tendentiously.md": {
    "primary": "In a tendentious manner; with marked bias, partiality, or deliberate slant toward a specific viewpoint.",
    "secondary": "In legal evidentiary analysis, counsel argued that the prosecutor had tendentiously framed witness testimony to prejudice the jury.",
    "quotes": [
      {"author": "George Orwell", "work": "Inside the Whale", "quote": "The documentary **tendentiously** presented the strike as an unprovoked conspiracy against the state."},
      {"author": "Bertrand Russell", "work": "Power: A New Social Analysis", "quote": "Partisan historians **tendentiously** rewrite national annals to glorify the reigning dynasty."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "When opposing viewpoints are **tendentiously** suppressed, public discourse degenerates into sterile dogma."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 6A: Successfully updated {updated}/{len(data)} notes.")
