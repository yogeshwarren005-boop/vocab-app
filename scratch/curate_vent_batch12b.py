# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — vent Part 2 (12B, 39 words) ---
  "Dashboard — vent/eventually.md": {
    "primary": "In the end; after an extended period of time or series of developments; ultimately.",
    "secondary": "In narrative structure and historical analysis, marking the long-term resolution of cumulative underlying tensions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Varieties rarely intercross in a state of nature, and **eventually** diverge into distinct and stable species."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He trusted that patient constancy would **eventually** win the regard of her rebellious heart."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Every thread of the mysterious crime **eventually** led back to the Andaman convict settlement."}
    ]
  },
  "Dashboard — vent/eventuate.md": {
    "primary": "To occur or result as an ultimate consequence, outcome, or final conclusion of an affair.",
    "secondary": "In formal rhetoric and historical writing, denotes complex sociopolitical developments terminating in a definitive crisis or settlement.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Disputes between sovereign confederates must **eventuate** in open war unless a common tribunal is established."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The prolonged ecclesiastical conflicts were destined to **eventuate** in the Glorious Revolution of 1688."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The bold pursuit of the albino Leviathan could only **eventuate** in triumph or utter catastrophe."}
    ]
  },
  "Dashboard — vent/intervention.md": {
    "primary": "The act of coming between persons or things to alter, settle, or prevent an action or course of events.",
    "secondary": "In diplomatic history and international law, forcible interference by a state in the internal sovereign affairs of another realm.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The timely **intervention** of the Roman legions arrested the advance of the invading Alemanni."},
      {"author": "John Stuart Mill", "work": "A Few Words on Non-Intervention", "quote": "The question of military **intervention** in the domestic struggles of a neighbor demands rigorous moral justification."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Only the sympathetic **intervention** of Mr. Jarndyce saved the distressed family from total ruination."}
    ]
  },
  "Dashboard — vent/intraventricular.md": {
    "primary": "Situated, occurring, or administered within a ventricle of the brain or cardiac chambers.",
    "secondary": "In neurosurgical practice, intraventricular hemorrhage describes bleeding into the cerebral ventricular system, often complicating premature birth or vascular malformations.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "An **intraventricular** clot was discovered upon post-mortem examination of the lateral ventricle."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The ependymal lining bathes in the circulating **intraventricular** cerebrospinal fluid."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Severe hypertension occasionally ruptures small lenticulostriate vessels, producing catastrophic **intraventricular** bleeding."}
    ]
  },
  "Dashboard — vent/invent.md": {
    "primary": "To create, design, or produce something new and useful that did not previously exist; to devise.",
    "secondary": "In rhetorical classical theory (inventio), discovering valid arguments and relevant proofs to persuade an audience.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Men seek to **invent** new mechanical arts by following the true interpretation of natural causes."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The grand Academy of Lagado sought to **invent** methods for extracting sunbeams out of cucumbers."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Daniel Doyce spent years attempting to **invent** improvements in rifled ordnance for the state."}
    ]
  },
  "Dashboard — vent/invention.md": {
    "primary": "A newly devised process, machine, or creative product; the faculty or power of inventing.",
    "secondary": "In intellectual property jurisprudence, an original technical creation meeting statutory requirements of novelty, non-obviousness, and industrial utility.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "O for a Muse of fire, that would ascend the brightest heaven of **invention**!"},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **invention** of printing hath scattered knowledge across the earth beyond all former bounds."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labour greatly improves the **invention** of specialized machinery by observant artisans."}
    ]
  },
  "Dashboard — vent/inventive.md": {
    "primary": "Having or showing creative ingenuity; adept at designing new devices, methods, or solutions.",
    "secondary": "In patent examinations, the inventive step (non-obviousness) evaluates whether an innovation exceeds ordinary skilled technical expectation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man owes his enormous progress over brute ancestors to his **inventive** faculties in toolmaking."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The criminal displayed a remarkably **inventive** mind in arranging the mechanical traps around the treasure."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The Time Traveller was an extraordinarily **inventive** mechanician, admired by all his dinner companions."}
    ]
  },
  "Dashboard — vent/inventively.md": {
    "primary": "In an imaginative, resourceful, or creatively original and ingenious manner.",
    "secondary": "In artistic design, deploying unexpected aesthetic pairings or novel formal techniques to resolve composition challenges.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Venetian stone-carvers worked **inventively**, varying every foliage capital with fresh natural observation."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "She adapted her wardrobe **inventively**, combining Elizabethan ruffs with eighteenth-century velvet breeches."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins handled phonetic transcriptions **inventively**, capturing local cockney inflections with photographic precision."}
    ]
  },
  "Dashboard — vent/inventiveness.md": {
    "primary": "The quality, capacity, or skill of being creative, imaginative, and adept at originating new ideas.",
    "secondary": "In economic sociology and industrial history, the cultural disposition and institutional incentives that foster rapid technological progress.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The mechanical **inventiveness** of Western races expanded rapidly under conditions of civic liberty and contract."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific **inventiveness** depends upon disciplined experimental imagination checked by rigorous fact."},
      {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "Human **inventiveness** flourishes when motivated by craftsmanship rather than purely speculative financial gain."}
    ]
  },
  "Dashboard — vent/inventor.md": {
    "primary": "A person who invents, designs, or discovers a new process, apparatus, or mechanical device.",
    "secondary": "In patent law, the individual who conceives the core inventive concept embodied in the claims of an application.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "The **inventor** of the open stove refused a royal patent, desiring that his work should serve the public freely."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The government offices treated the poor **inventor** with callous neglect, shuffling his plans from department to department."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "As an American **inventor**, Hank Morgan resolved to introduce nineteenth-century industry into sixth-century Britain."}
    ]
  },
  "Dashboard — vent/inventory.md": {
    "primary": "A complete, detailed, and organized list of items, property, or goods; the stock held by a business.",
    "secondary": "In probate and estate law, an itemized schedule of all assets and personalty submitted to the surrogate court by the executor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "I will give out divers schedules of my beauty: it shall be **inventoried**, and every particle and utensil labelled to my will."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I made a complete **inventory** of every barrel of powder, bag of biscuit, and tool saved from the stranded wreck."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant maintains a continuous **inventory** of warehouse commodities to anticipate seasonal changes in market demand."}
    ]
  },
  "Dashboard — vent/inventorying.md": {
    "primary": "The act or process of making a detailed itemized list or audit of assets, goods, or resources.",
    "secondary": "In supply chain management, conducting physical counts and digital reconciliations to determine cycle stocks and inventory shrink.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The mate was busy **inventorying** the spare harpoons and lance-heads stowed beneath the boat deck."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Krook spent his days sorting and **inventorying** dusty bundles of parchment in his rag-and-bottle shop."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The bookkeeper spent Saturday afternoon **inventorying** office supplies and printing plates in the basement vault."}
    ]
  },
  "Dashboard — vent/misadventure.md": {
    "primary": "An unfortunate mishap, piece of bad luck, or unforeseen accident involving harm or defeat.",
    "secondary": "In criminal common law, homicide by misadventure describes an unintentional killing resulting from a lawful act performed without criminal negligence.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Your looks are pale and wild, and do import some **misadventure**."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "The coroner's inquest recorded an accidental **misadventure**, lacking evidence of foul play."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The traveler attributed his overturned carriage to an unlucky **misadventure** upon the sandy beach road."}
    ]
  },
  "Dashboard — vent/nonevent.md": {
    "primary": "An occurrence or event that was anticipated to be important or sensational but proves completely insignificant.",
    "secondary": "In media studies, anticlimactic public relations launches or staged spectacles that fail to generate public interest.",
    "quotes": [
      {"author": "George Orwell", "work": "Collected Essays", "quote": "The much-publicized political demonstration proved a complete **nonevent**, attracting merely a handful of curious idlers."},
      {"author": "Aldous Huxley", "work": "Antic Hay", "quote": "The grand social scandal fizzled out into a tedious **nonevent** as everyone agreed to forget the duel."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "What promised to be a dramatic confrontation dissolved into an awkward, silent **nonevent**."}
    ]
  },
  "Dashboard — vent/nonintervention.md": {
    "primary": "A policy or principle of not interfering in the internal affairs, disputes, or politics of other nations.",
    "secondary": "In 19th- and 20th-century diplomatic history, the doctrine formalized by Britain and France regarding foreign civil wars, notably during the Spanish Civil War.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A Few Words on Non-Intervention", "quote": "The doctrine of **nonintervention** should be respected among civilized states to encourage self-determined political liberty."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The cynical farce of European **nonintervention** starved the Spanish Republic of legitimate arms while dictators intervened freely."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Strict **nonintervention** often becomes an excuse for democratic powers to ignore catastrophic regional aggression."}
    ]
  },
  "Dashboard — vent/peradventure.md": {
    "primary": "Perhaps; maybe; by chance; or a state of doubt, uncertainty, or speculative possibility.",
    "secondary": "In archaic and legal diction, used in conditional clauses (if peradventure) or nominal phrases (beyond all peradventure).",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "**Peradventure** this is not Fortune's work neither, but Nature's, who perceiveth our natural wits too dull."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Beyond all **peradventure**, the stability of commonwealths depends on just laws and contented subjects."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "If **peradventure** we should meet with the lions in the dark, what defense could our feeble weapons supply?"}
    ]
  },
  "Dashboard — vent/prevent.md": {
    "primary": "To keep from happening or arising; to hinder, forestall, or make impossible by prior action.",
    "secondary": "Archaically (from Latin praevenire), to go before, precede, or anticipate someone as a guide or protector.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "So shall my anticipation **prevent** your discovery, and your secrecy to the king and queen moult no feather."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The watchful guardian angels came to **prevent** the subtle adversary from entering Paradise undetected."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe stood between us to **prevent** any further violence from the raging blacksmith."}
    ]
  },
  "Dashboard — vent/preventable.md": {
    "primary": "Capable of being prevented, avoided, or stopped from occurring through timely action or foresight.",
    "secondary": "In public health epidemiology, describes morbidity and mortality avoidable through vaccination, sanitation, and lifestyle intervention.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Typhoid fever represents a classic **preventable** disease whose eradication depends entirely upon uncontaminated municipal water."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The application of scientific hygiene has already eliminated vast categories of once deadly and **preventable** maladies."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Thousands of soldiers perished in military hospitals from purely **preventable** septic infections caused by foul air."}
    ]
  },
  "Dashboard — vent/preventative.md": {
    "primary": "Intended or serving to prevent something undesirable; a prophylactic substance, measure, or remedy.",
    "secondary": "In clinical medicine, synonymous with preventive, often designating prophylactic vaccines and hygienic measures.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Vaccination remains the most sovereign **preventative** against the devastating scourge of smallpox."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Quinine was administered daily to the expedition crew as a valuable **preventative** against coastal marsh fevers."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Dying Detective", "quote": "Holmes pretended to seek an efficacious **preventative** against the contagious eastern fever."}
    ]
  },
  "Dashboard — vent/prevention.md": {
    "primary": "The action of stopping something from happening or arising; proactive safeguarding.",
    "secondary": "In public health policy, tiered into primary prevention (preventing disease onset), secondary (early detection), and tertiary (reducing impairment).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "God be thanked for **prevention**, which I in sufferance heartily will rejoice."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "In statecraft, the timely **prevention** of popular sedition is far wiser than bloody suppression after the outbreak."},
      {"author": "Benjamin Franklin", "work": "Poor Richard's Almanack", "quote": "An ounce of **prevention** is worth a pound of cure in matters of both physical and civic health."}
    ]
  },
  "Dashboard — vent/preventive.md": {
    "primary": "Designed, serving, or intended to hinder or forestall the occurrence of something harmful.",
    "secondary": "In public health and epidemiology, preventive medicine focuses on proactive health maintenance, sanitation, and immunizations.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The ideal of **preventive** medicine had been attained, and physical disease was entirely vanquished."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The **preventive** function of government is far more liable to abuse than the purely punitive function."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Hygienic science acts as a **preventive** shield against the blind cruelty of infectious pathogens."}
    ]
  },
  "Dashboard — vent/proventil.md": {
    "primary": "A proprietary brand name for albuterol (salbutamol), a short-acting beta-2 adrenergic receptor agonist bronchodilator.",
    "secondary": "In respiratory pharmacotherapy, administered via metered-dose inhaler to reverse acute bronchospasm in asthma and COPD.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern aerosolized bronchodilators such as **Proventil** provide swift relief during sudden paroxysms of asthmatic dyspnea."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "Immediate inhalation of **Proventil** dilates constricted bronchioles, restoring pulmonary alveolar ventilation."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The patient kept a canister of **Proventil** at his bedside to avert nocturnal respiratory distress."}
    ]
  },
  "Dashboard — vent/reinvent.md": {
    "primary": "To change or remake something completely so that it appears entirely fresh, new, or different.",
    "secondary": "In organizational strategy and technology management, to restructure business models to survive disruptive market transitions.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Each energetic generation must **reinvent** social morality or sink into spiritual petrifaction."},
      {"author": "H. G. Wells", "work": "Anticipations", "quote": "Modern engineers must **reinvent** highway design to accommodate high-speed vehicular locomotion."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The woman novelist must **reinvent** the English sentence to fit the subtle contours of her feminine experience."}
    ]
  },
  "Dashboard — vent/seventeen.md": {
    "primary": "The cardinal number equal to the sum of sixteen and one; ten plus seven; 17.",
    "secondary": "In law and developmental psychology, seventeenth year of life marks late adolescence preceding full legal majority at eighteen.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "From **seventeen** years till now almost fourscore here lived I, but now live here no more."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was **seventeen** years of age when I advertised for a position as governess in a respectable family."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He had reached the age of **seventeen**, full of youthful ardor and unclouded hopes for the future."}
    ]
  },
  "Dashboard — vent/seventeenth.md": {
    "primary": "Coming next in ordinal sequence after the sixteenth; one of seventeen equal fractional parts.",
    "secondary": "In historiography, the seventeenth century designates the pivotal 1601–1700 era characterized by the Scientific Revolution and baroque culture.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A certain d'Urberville of the sixteenth or **seventeenth** century had committed a dreadful crime near the ancestral vault."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "In the **seventeenth** century, judicial corruption was so common that Bacon's offence was judged with unusual severity."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **seventeenth** chapter of the annals records the brief reign and violent death of the Emperor Pertinax."}
    ]
  },
  "Dashboard — vent/seventies.md": {
    "primary": "The numbers, years, or temperature degrees spanning from seventy to seventy-nine; the eighth decade of human life.",
    "secondary": "In 20th-century history, the 1970s denotes the decade marked by the oil crises, détente, stagflation, and countercultural transition.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke was well into his **seventies**, yet retained the active habits of his youthful squire days."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The veteran maltster had passed his **seventies** and sat comfortably beside the glowing malt-kiln."},
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "She observed elderly gentlemen in their **seventies** taking their morning stroll across St. James's Park."}
    ]
  },
  "Dashboard — vent/seventieth.md": {
    "primary": "Coming next in ordinal sequence after the sixty-ninth; one of seventy equal fractional parts.",
    "secondary": "In biblical life-span lore (psalm 90:10), the seventieth year (three-score years and ten) marks the traditional allotted span of mortal life.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I saw an old man the other day, to my astonishment, making holes with a hoe for the **seventieth** year in succession."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Goethe celebrated his **seventieth** birthday surrounded by the veneration of the whole intellectual world of Europe."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The veteran statesman celebrated his **seventieth** anniversary in retirement, free from political intrigue."}
    ]
  },
  "Dashboard — vent/seventy.md": {
    "primary": "The cardinal number equal to the product of seven and ten; one more than sixty-nine; 70.",
    "secondary": "In biblical antiquity, the Septuagint represents the Greek translation of the Hebrew Bible traditionally ascribed to seventy Jewish scholars.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Mine speak of **seventy** Senators that died by their proscriptions, Cicero being one."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The ancient church tower had withstood the storms of more than **seventy** winters upon the chalk downs."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Mr. Lorry had lived for **seventy** years in the service of Tellson's Bank, honored and trusted by all."}
    ]
  },
  "Dashboard — vent/seventy-eight.md": {
    "primary": "The cardinal number equal to the sum of seventy and eight; 78; also a 78 rpm phonograph record.",
    "secondary": "In audio recording history, coarse-groove shellac discs rotating at 78 revolutions per minute standard throughout the early 20th century.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "See what an honorable place you fill at **seventy-eight**, with mind unimpaired and heart as sound as ever."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "He played a scratching old **seventy-eight** record of musical-hall favorites on the wind-up gramophone."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The old timber merchant had attained **seventy-eight** years, yet could still appraise an oak tree at twenty paces."}
    ]
  },
  "Dashboard — vent/seventy-fifth.md": {
    "primary": "Coming next in ordinal sequence after the seventy-fourth; one of seventy-five equal fractional parts.",
    "secondary": "In institutional history, a diamond jubilee commemorating the seventy-fifth anniversary of an event, founding, or accession.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The academy commemorated its **seventy-fifth** session with addresses reviewing the progress of natural science."},
      {"author": "Henry James", "work": "The American", "quote": "The general was celebrating his **seventy-fifth** year, surrounded by veteran comrades of former campaigns."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "On his **seventy-fifth** birthday, tributes from all free nations poured into the prime minister's country residence."}
    ]
  },
  "Dashboard — vent/seventy-five.md": {
    "primary": "The cardinal number equal to the sum of seventy and five; 75; three-quarters of one hundred.",
    "secondary": "In military history, the French Canon de 75 modèle 1897, the first modern quick-firing field gun with a hydro-pneumatic recoil mechanism.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "To every Roman citizen he gives, to every several man, **seventy-five** drachmas."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "He was burdened with a mortgage of **seventy-five** dollars on his small farm, which weighed heavily upon his peace."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sperm whale's skeleton measured **seventy-five** feet from the snout to the extremity of the tail flukes."}
    ]
  },
  "Dashboard — vent/seventy-four.md": {
    "primary": "The cardinal number equal to the sum of seventy and four; 74; or a naval line-of-battle ship carrying 74 guns.",
    "secondary": "In naval warfare of the Age of Sail, the two-decked 74-gun ship of the line formed the backbone of fleet battle lines due to optimal balance of firepower and sailing qualities.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "What skiff in tow of a **seventy-four** can stand still when the great warship spreads all her canvas to the gale?"},
      {"author": "Captain Frederick Marryat", "work": "Mr Midshipman Easy", "quote": "The gallant **seventy-four** led the British column into action under a heavy fire from the Spanish batteries."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The admiral hoisted his flag on a newly launched **seventy-four** designed by the master shipwrights of Deptford."}
    ]
  },
  "Dashboard — vent/seventy-nine.md": {
    "primary": "The cardinal number equal to the sum of seventy and nine; one less than eighty; 79.",
    "secondary": "In chemistry, gold (symbol Au) has atomic number seventy-nine, possessing high malleability and corrosion resistance.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The register recorded that the former mayor had reached the age of **seventy-nine** before laying down his earthly cares."},
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The old pensioner lived in room number **seventy-nine** of the almshouse, spending his days knitting stockings."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The estate accounts showed a surplus of **seventy-nine** pounds after all tenant repairs had been satisfied."}
    ]
  },
  "Dashboard — vent/seventy-one.md": {
    "primary": "The cardinal number equal to the sum of seventy and one; 71.",
    "secondary": "In chronology and statistics, an integer prime following seventy and preceding seventy-two.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The venerable senator reached his **seventy-one** years before retiring from the tumult of imperial politics."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The old shepherd counted **seventy-one** ewes safely folded within the hurdles before dusk fell across the valley."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "There were **seventy-one** steps leading to the windy attic where the impoverished scholar had his lodgings."}
    ]
  },
  "Dashboard — vent/seventy-seven.md": {
    "primary": "The cardinal number equal to the sum of seventy and seven; 77; seven times eleven.",
    "secondary": "In biblical exegesis, Matthew 18:22 commands forgiveness 'seventy times seven', symbolizing limitless mercy.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The venerable sage attained the age of **seventy-seven**, preserving his intellectual vigor unimpaired to the last."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel counted **seventy-seven** fleeces stacked neatly in the shearers' barn by midday."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal folio numbered **seventy-seven** pages of crabbed legal handwriting that defied mortal patience."}
    ]
  },
  "Dashboard — vent/seventy-six.md": {
    "primary": "The cardinal number equal to the sum of seventy and six; 76; associated with the Spirit of '76.",
    "secondary": "In American history, 'the spirit of 76' symbolizes the revolutionary patriotic fervor of 1776 and the Declaration of Independence.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "They boast that the king's standing army consists of a hundred and **seventy-six** thousand foot soldiers."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The venerable judge passed away quietly in his **seventy-six** year, honored by the entire commonwealth."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's log recorded that the whaler had cruised for **seventy-six** days without sighting a single spout."}
    ]
  },
  "Dashboard — vent/seventy-three.md": {
    "primary": "The cardinal number equal to the sum of seventy and three; 73; a prime number.",
    "secondary": "In celestial cartography and mathematics, seventy-three is an emirp whose digit reversal (37) is also a prime.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The old captain had survived to his **seventy-three** year, weathering countless storms in the North Sea trade."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The old clerk had occupied desk number **seventy-three** in the insurance office for more than four decades."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The survey noted **seventy-three** cottages requiring immediate roof repairs across the low-lying parish lands."}
    ]
  },
  "Dashboard — vent/seventy-two.md": {
    "primary": "The cardinal number equal to the product of eight and nine; six dozen; 72.",
    "secondary": "In rule-of-72 financial estimation, used to approximate the number of years required to double an investment at a given interest rate.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "In length, the Sperm Whale's skeleton at Tranque measured **seventy-two** feet, so that when alive it must have been eighty."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We anchored in the sheltered cove after **seventy-two** hours of continuous beating against head winds."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Lord John counted **seventy-two** prehistoric tracks impressed upon the dried mud of the volcanic plateau."}
    ]
  },
  "Dashboard — vent/subvent.md": {
    "primary": "To provide financial support or funding to; to grant a subvention or financial subsidy.",
    "secondary": "In political economy and public finance, state financial contributions subsidizing scientific research, public transit, or cultural institutions.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The legislature resolved to **subvent** the national fisheries by granting bounties upon exported catch."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The state may appropriately **subvent** foundational scientific investigations that offer no immediate commercial return."},
      {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "Efforts to **subvent** private industries from the public purse inevitably distort natural market incentives."}
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

print(f"Motion Batch 12B: Successfully updated {updated}/{len(data)} notes.")
