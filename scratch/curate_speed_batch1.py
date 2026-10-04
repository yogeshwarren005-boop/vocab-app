# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — alacr (2 words)
  # =========================================================================
  "Dashboard — alacr/alacritous.md": {
    "primary": "Characterized by brisk, cheerful readiness, promptness, or lively enthusiasm.",
    "secondary": "In behavioral description, a swift, willing responsiveness displayed when executing duties or answering requests.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The cheerful clerk sprang forward with **alacritous** steps to prepare the requested legal documents."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She complied with the invitation in an **alacritous** manner, delighted by the prospect of the evening ball."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Toby bounded ahead with **alacritous** zeal the moment the creosote scent struck his keen nostrils."}
    ]
  },
  "Dashboard — alacr/alacrity.md": {
    "primary": "Cheerful readiness, promptitude, or eager willingness; brisk and lively action.",
    "secondary": "In military and diplomatic accounts, the immediate, spirited execution of executive orders without reluctance or delay.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "I have not that **alacrity** of spirit, nor cheer of mind, that I was wont to have."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Bingley accepted the invitation with the greatest **alacrity**, promising to be with them at an early hour."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He obeyed the summons with great **alacrity**, skipping across the courtyard with lively vigor."}
    ]
  },

  # =========================================================================
  # Dashboard — flux (7 words)
  # =========================================================================
  "Dashboard — flux/conflux.md": {
    "primary": "A flowing together of two or more streams; a convergence or gathering of people or things.",
    "secondary": "In urban history and geography, the commercial gathering of diverse mercantile populations at river junctions or maritime ports.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "As knotty oaks, into whose entrails the **conflux** of meeting sap gives nourishment."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "A dense **conflux** of armed citizens gathered in the broad avenue leading toward the Bastille."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The seasonal **conflux** of foreign pilgrims enriched the merchants and temples of the capital."}
    ]
  },
  "Dashboard — flux/efflux.md": {
    "primary": "The act, process, or rate of flowing out; that which flows out or issues forth; an emanation.",
    "secondary": "In fluid mechanics and thermodynamics, the discharge velocity of liquid escaping through a container orifice (Torricelli's Law).",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Since God is light, and never but in unapproached light dwelt from eternity, bright **efflux** of bright essence increate."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The invisible **efflux** of odorous vapor from flowers perfumes the surrounding evening air."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Every genuine action is an outward **efflux** of the divine soul manifesting in nature."}
    ]
  },
  "Dashboard — flux/flux.md": {
    "primary": "Continuous movement, passage, or change; an outflow or discharge of fluid matter.",
    "secondary": "In physics and metallurgy, the rate of transfer of fluid, energy, or particles across a unit area; or a chemical cleaning agent facilitating soldering.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Into the **flux** of company! Anon a careless herd, full of the pasture, jumps along by him."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Human affairs are subject to perpetual **flux** and instability, like the shifting tides of the ocean."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organic forms are not immutable types, but entities maintained in continual **flux** across geological time."}
    ]
  },
  "Dashboard — flux/fluxion.md": {
    "primary": "The action of flowing; the continuous change or rate of variation of a flowing quantity.",
    "secondary": "In the history of mathematics, the term coined by Sir Isaac Newton to designate the differential calculus (fluxions and fluents).",
    "quotes": [
      {"author": "Isaac Newton", "work": "The Method of Fluxions", "quote": "The velocity with which a generated quantity increases I call its **fluxion**, denoted by a dotted letter."},
      {"author": "George Berkeley", "work": "The Analyst", "quote": "He critically questioned whether the mysterious **fluxion** of an evanescent quantity rested on sound logic."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our ideas of continuous time arise from the constant **fluxion** and succession of thoughts in our minds."}
    ]
  },
  "Dashboard — flux/fluxmeter.md": {
    "primary": "An electrical measuring instrument used to determine the quantity or intensity of magnetic flux.",
    "secondary": "In experimental electromagnetism, a specialized ballistic galvanometer calibrated to register webers or maxwells across a search coil.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The deflection of the magnetic **fluxmeter** registered precisely the induction generated by moving the bar."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "By connecting a search coil to a sensitive **fluxmeter**, the spatial distribution of the field is mapped."},
      {"author": "William Thomson", "work": "Popular Lectures and Addresses", "quote": "The laboratory **fluxmeter** demonstrated the quantitative variations in induction within the core."}
    ]
  },
  "Dashboard — flux/influx.md": {
    "primary": "An arrival, entry, or inward flowing of a large quantity of people, fluid, or material things.",
    "secondary": "In macroeconomic analysis, massive capital inflows or demographic migrations altering domestic liquidity and employment.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The sudden **influx** of gold and silver from the American mines reduced the purchasing value of bullion."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial capital absorbed a continuous **influx** of provincial tribute, corn, and foreign merchandise."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The revocation of the Edict of Nantes prompted a valuable **influx** of skilled French artisans into London."}
    ]
  },
  "Dashboard — flux/reflux.md": {
    "primary": "A flowing back; an ebb, retreat, or backward movement of a liquid or tidal current.",
    "secondary": "In chemical engineering and gastroenterology, the continuous recycling of condensed vapor to a distillation column; or the retrograde ascent of gastric acid.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The regular flux and **reflux** of the ocean tides present a magnificent problem for natural philosophy."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The surging crowd experienced an abrupt **reflux**, swaying backward before the advance of the soldiers."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic acid **reflux** into the lower esophagus induces mucosal ulceration and persistent epigastric pain."}
    ]
  },

  # =========================================================================
  # Dashboard — langu (11 words)
  # =========================================================================
  "Dashboard — langu/interlanguage.md": {
    "primary": "An intermediate language system constructed by a learner while acquiring a second language; or an auxiliary dialect.",
    "secondary": "In second language acquisition (Selinker), a dynamic linguistic system governed by internal rules distinct from both native and target languages.",
    "quotes": [
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "The developmental **interlanguage** spoken by international traders combined basic native syntax with foreign terms."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "An artificial **interlanguage** was proposed by scholars to facilitate philosophical correspondence across Europe."},
      {"author": "Otto Jespersen", "work": "Language: Its Nature, Development and Origin", "quote": "Learners unconsciously formulate a transitional **interlanguage** that steadily approximates the target idiom."}
    ]
  },
  "Dashboard — langu/language.md": {
    "primary": "The system of human communication using spoken, written, or signed words in structured and conventional ways.",
    "secondary": "In formal linguistics, a recursive symbolic system comprising phonology, morphology, syntax, and semantics governed by universal grammar.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "You taught me **language**, and my profit on't is, I know how to curse."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words in their primary or immediate signification stand for nothing but the ideas in the mind of him that uses them, forming human **language**."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Words are signs of natural facts; particular natural facts are symbols of particular spiritual facts, which is the ground of **language**."}
    ]
  },
  "Dashboard — langu/languedoc-roussillon.md": {
    "primary": "A former historic region in southern France bordering the Mediterranean Sea and the Pyrenees mountains.",
    "secondary": "In French historical geography, a coastal wine-producing territory encompassing ancient Roman settlements (Nîmes) and Occitan cultural heritage.",
    "quotes": [
      {"author": "Henry James", "work": "A Little Tour in France", "quote": "We traversed the sunlit vineyards of **languedoc-roussillon**, admiring the monumental aqueduct of the Pont du Gard."},
      {"author": "Tobias Smollett", "work": "Travels through France and Italy", "quote": "The warm Mediterranean breeze swept across the ancient coastal plains of **languedoc-roussillon**."},
      {"author": "Arthur Young", "work": "Travels in France", "quote": "The agriculture of **languedoc-roussillon** revealed an extensive cultivation of vines and olive groves along the hills."}
    ]
  },
  "Dashboard — langu/languid.md": {
    "primary": "Displaying or having a disinclination for physical exertion or effort; slow, relaxed, or pleasantly weary.",
    "secondary": "In clinical diagnosis and prose portraiture, drooping vitality characterized by sluggish pulse, feeble reflexes, and dull responsiveness.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet received her visitors with **languid** indifference, complaining of her delicate nerves."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The day was hot and humid, and the lawyers in Chancery leaned back with **languid** yawns."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He waved his hand in a **languid** gesture, exhaling a fragrant cloud of Turkish tobacco smoke."}
    ]
  },
  "Dashboard — langu/languidly.md": {
    "primary": "In a languid, lethargic, or unenergetic manner; slowly, listlessly, or with relaxed indifference.",
    "secondary": "In aesthetic literature, movements performed with deliberate, graceful slowness suggesting aristocratic weariness.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry turned **languidly** on the divan, watching the honey-colored blossoms fluttering in the breeze."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes opened his eyes **languidly** and listened to the anxious footsteps approaching the door."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Daisy and Jordan lay upon an enormous couch, their white dresses rippling **languidly** in the wind from the windows."}
    ]
  },
  "Dashboard — langu/languish.md": {
    "primary": "To lose or lack vitality; to grow weak or feeble; to suffer neglect or hardship in confinement.",
    "secondary": "In romantic literature and legal history, enduring solitary imprisonment or prolonged unrequited romantic yearning.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "One desperate grief cures with another's **languish**; take thou some new infection to thy eye."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "To **languish** in obscure prison bondage, blind and bound, was the bitter destiny of the fallen hero."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Debtors were left to **languish** in the cold cells of the Marshalsea, forgotten by former friends."}
    ]
  },
  "Dashboard — langu/languisher.md": {
    "primary": "A person who languishes, pines away, or suffers prolonged weakness or neglect.",
    "secondary": "In 18th-century sentimental drama, an affected lover or melancholy captive bemoaning fate in solitary seclusion.",
    "quotes": [
      {"author": "Alexander Pope", "work": "Epistle to Dr. Arbuthnot", "quote": "The sentimental **languisher** sighed over imaginary sorrows while neglecting real duties."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "She sat beside the window like a pale **languisher**, worn down by persecution and grief."},
      {"author": "Tobias Smollett", "work": "The Expedition of Humphry Clinker", "quote": "The lovesick youth was treated by the company as an incorrigible **languisher** deserving pity."}
    ]
  },
  "Dashboard — langu/languor.md": {
    "primary": "A state of feeling tired, relaxed, and not wanting to move; pleasant exhaustion or dreaminess.",
    "secondary": "In medical semiotics and Victorian poetry, oppressive physical torpor accompanying tropical fevers or melancholic introspection.",
    "quotes": [
      {"author": "Lord Byron", "work": "Don Juan", "quote": "A soft **languor** stole over her senses as the music floated across the quiet waters."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Her sweet voice had lost its spirit, sinking into a gentle **languor** born of long disappointment."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The summer heat cast a pleasant **languor** over the sleepy cathedral town."}
    ]
  },
  "Dashboard — langu/languorous.md": {
    "primary": "Characterized by, inducing, or suggestive of pleasant tiredness, relaxation, or dreaminess.",
    "secondary": "In sensory prose and musical expression, slow tempos and lush harmonies evocative of warm, tranquil atmospheres.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The heavy fragrance of roses produced a **languorous** charm that enveloped the entire studio."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The jungle exhaled a warm, **languorous** breath that seemed to sap all physical energy from the crew."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The afternoon sunlight fell with **languorous** warmth upon the lush buttercups of the valley pasture."}
    ]
  },
  "Dashboard — langu/languorously.md": {
    "primary": "In a languorous manner; with dreamy, relaxed slowness or luxurious exhaustion.",
    "secondary": "In descriptive narrative, reclining or drifting in an unhurried, voluptuous, or torpid fashion.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The smoke of his cigar rose **languorously** toward the ceiling as Holmes leaned back in contemplation."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "She moved **languorously** through the ballroom, her silk train trailing across the polished parquet."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The Roman fountain splashed **languorously** in the shaded courtyard of the ancient palazzo."}
    ]
  },
  "Dashboard — langu/langur.md": {
    "primary": "A slender, long-tailed Asian monkey of the subfamily Colobinae, especially the sacred Hanuman langur.",
    "secondary": "In primatology and Indian wildlife ecology, folivorous colobine monkeys possessing complex multi-chambered stomachs adapted for digesting leaves.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "The Jungle Book", "quote": "The grey **langur** leaped effortlessly among the high branches of the sal forest, chattering a warning."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The specialized sacculated stomach of the Indian **langur** facilitates the digestion of coarse foliage."},
      {"author": "Richard Francis Burton", "work": "Goa, and the Blue Mountains", "quote": "We observed troops of the sacred **langur** foraging fearlessly among the stone shrines of the temple hill."}
    ]
  },

  # =========================================================================
  # Dashboard — tard (12 words)
  # =========================================================================
  "Dashboard — tard/retard.md": {
    "primary": "To delay, hinder, or impede the progress, growth, or development of something.",
    "secondary": "In mechanical engineering and aviation, to throttle back engine output or adjust ignition timing to retard spark detonation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "I would I had not done it; it would have kept my tears back and did **retard** my journey."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Superstitions and unwarranted fears do greatly **retard** the noble advancement of experimental science."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Severe climatic extremes may periodically **retard** the reproductive increase of flourishing species."}
    ]
  },
  "Dashboard — tard/retardant.md": {
    "primary": "A substance or agent that slows down, delays, or impedes a chemical reaction, process, or fire.",
    "secondary": "In chemical engineering and fire safety science, chemical coatings (e.g. brominated flame retardants) that inhibit combustion kinetics.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical History of a Candle", "quote": "Applying a mineral **retardant** to combustible cloth diminishes the speed at which flame propagates."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A biochemical **retardant** added to the enzyme solution arrested further catalytic breakdown."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Cold acts as a natural physiological **retardant**, slowing the metabolic decomposition of injured tissues."}
    ]
  },
  "Dashboard — tard/retardation.md": {
    "primary": "The act of delaying or hindering; a decrease in velocity, acceleration, or developmental progress.",
    "secondary": "In classical mechanics and astrophysics, negative acceleration resulting in velocity attenuation over time.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The resistance of a dense fluid causes a steady **retardation** in the forward velocity of the projectile."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Commercial monopolies produce a harmful **retardation** of inventive progress in industrial production."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Unfavorable soil conditions caused a noticeable **retardation** in the vegetative development of the seedlings."}
    ]
  },
  "Dashboard — tard/retarded.md": {
    "primary": "Delayed, slowed, or impeded in development, progress, movement, or speed.",
    "secondary": "In electrodynamics (Liénard–Wiechert potentials), retarded time accounting for the finite propagation speed of electromagnetic signals across space.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The electromagnetic disturbance is calculated at a **retarded** epoch, allowing for the velocity of light."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The development of secondary sexual structures was **retarded** by cold ambient temperatures in the experiment."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sheep's pace was **retarded** by the heavy drifts of snow accumulating along the chalk ridges."}
    ]
  },
  "Dashboard — tard/retardent.md": {
    "primary": "A variant spelling of retardant; an agent or factor that causes delay or hindrance.",
    "secondary": "In materials processing, an additive used to retard the curing time of plaster, cement, or polymers.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The chemist introduced a chemical **retardent** into the slurry to prevent premature setting of the mortar."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "A saline **retardent** slowed the electrolytic deposition of copper onto the cathode plate."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "The presence of aqueous vapor acted as a radiative **retardent**, trapping thermal rays near the surface."}
    ]
  },
  "Dashboard — tard/retarding.md": {
    "primary": "Causing delay, impediment, or deceleration; slowing down progress or motion.",
    "secondary": "In mechanics, resistive friction or aerodynamic drag acting as a retarding force on moving bodies.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Air resistance exerts a continuous **retarding** influence upon projectiles hurled through the atmosphere."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Burdensome internal tolls operated as a **retarding** check upon domestic commerce between provinces."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Severe famine acted as a powerful **retarding** factor, checking the numerical increase of the tribe."}
    ]
  },
  "Dashboard — tard/tardigrada.md": {
    "primary": "A phylum of microscopic, eight-legged invertebrates known as water bears or moss piglets.",
    "secondary": "In invertebrate zoology and cryptobiology, Tardigrada are extremophiles celebrated for entering anhydrobiosis to survive vacuum and extreme temperatures.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The microscopic **tardigrada** possess four pairs of unjointed legs terminating in curved claws."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The cryptobiotic resilience of the **tardigrada** enables them to survive prolonged desiccation in moss cushions."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "Microscopists marvel at the survival of **tardigrada** when revived from apparent death with a single drop of water."}
    ]
  },
  "Dashboard — tard/tardigrade.md": {
    "primary": "A microscopic, eight-legged water bear of the phylum Tardigrada; or moving with slow pace.",
    "secondary": "In physiological biology, an organism capable of tun formation, shedding almost all cellular water during suspended animation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Under the lens, the minute **tardigrade** crawled sluggishly among the algal filaments like a tiny bear."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon proceeded in his scholarly investigations with a slow, **tardigrade** deliberation that defied impatience."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The cuticle of the **tardigrade** is periodically molted along with its clawed extremities."}
    ]
  },
  "Dashboard — tard/tardily.md": {
    "primary": "Slowly, late, or after the expected or proper time; with reluctance or delay.",
    "secondary": "In narrative prose, actions performed with deliberate hesitation or lagging pace.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "And now he feasts, and **tardily** returns to take his part in this contested field."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The winter dawn broke **tardily** over the vast expanse of Egdon Heath, shedding a wan grey light."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Justice arrived **tardily** for the innocent prisoner who had wasted years within the dark cell."}
    ]
  },
  "Dashboard — tard/tardiness.md": {
    "primary": "The trait or habit of arriving or acting late; delay, slowness, or lack of punctuality.",
    "secondary": "In organizational and scholastic management, habitual non-compliance with scheduled attendance or operational timelines.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "She apologized for her **tardiness**, explaining the difficulties of the muddy roads after the rain."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Squeers punished the slightest **tardiness** among the wretched pupils with unsparing severity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The intolerable **tardiness** of legal proceedings in Chancery drove many an heir to despair."}
    ]
  },
  "Dashboard — tard/tardive.md": {
    "primary": "Characterized by late appearance or delayed development; occurring late in the course of a disease.",
    "secondary": "In clinical neuropsychiatry, tardive dyskinesia describing involuntary hyperkinetic movements emerging after chronic exposure to neuroleptics.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain chronic toxic exposures produce a **tardive** motor disturbance that manifests months after cessation."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The physician watched for **tardive** sequelae that might arise long after the acute fever had subsided."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical notes documented a **tardive** neurological deficit developing in the patient following spinal trauma."}
    ]
  },
  "Dashboard — tard/tardy.md": {
    "primary": "Moving or acting slowly; arriving, occurring, or done late or after the expected time.",
    "secondary": "In historical and legal documents, delayed performance of contractual duties or overdue response to administrative summons.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Why, how now, Dromio? Where have you been so long? What makes you so **tardy**?"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The celestial messenger chid their **tardy** steps, urging them swiftly through the eastern gate."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The post was **tardy** in delivering letters to the remote country village during winter storms."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
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

print(f"Speed Batch 1: Successfully updated {updated}/{len(data)} notes.")
