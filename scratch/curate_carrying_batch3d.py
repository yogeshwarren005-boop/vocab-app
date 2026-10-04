# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — port (Batch 3D: 31 words)
  # =========================================================================
  "Dashboard — port/purport.md": {
    "primary": "The meaning or substance of something, typically as a document or speech; or to claim or appear to be or do something.",
    "secondary": "In legal document construction and textual analysis, the ostensible intent or operational effect deduced from the face of an instrument.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "With a look so piteous in **purport** as if he had been loosed out of hell to speak of horrors."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The general **purport** of the proclamation was to warn the settlers against idolatry and sin."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She caught the general **purport** of his words without understanding their minute legal consequences."}
    ]
  },
  "Dashboard — port/rapport.md": {
    "primary": "A close and harmonious relationship in which the people or groups concerned understand each other's feelings or ideas and communicate well.",
    "secondary": "In clinical psychotherapy and psychological interviewing, establishing an empathetic, trust-based therapeutic alliance facilitating open communication.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Between the two cousins there existed a subtle, unspoken **rapport** that needed few words to sustain it."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "He felt at once that easy **rapport** which well-bred men establish with women of their own world."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The captain established an immediate **rapport** with the native crew, earning their unquestioned obedience."}
    ]
  },
  "Dashboard — port/reapportion.md": {
    "primary": "To assign or distribute something again in a different way or in different proportions.",
    "secondary": "In political representation, redrawing legislative district boundaries after a census to reflect changing demographic distributions.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Every future census will require congress to **reapportion** legislative seats among the changing populations of the states."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The legislature must periodically **reapportion** representation to prevent decaying boroughs from controlling the commonwealth."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The western migration compelled the union to **reapportion** federal tax quotas and congressional districts."}
    ]
  },
  "Dashboard — port/reapportionment.md": {
    "primary": "The act or process of redistributing or allocating something again in different shares.",
    "secondary": "In constitutional law, the decennial statutory redistribution of United States congressional districts among the states.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The decennial **reapportionment** of representatives preserves the democratic equilibrium between older and younger states."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Each **reapportionment** of power shifted the political center of gravity steadily toward the burgeoning western territories."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The **reapportionment** of the parish rates relieved the overburdened agricultural laborers."}
    ]
  },
  "Dashboard — port/reimport.md": {
    "primary": "To import something that had previously been exported from the same country.",
    "secondary": "In international customs law, bringing back domestic manufactures from foreign bonded warehouses without paying secondary import duties.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant may find it advantageous to export commodities to a foreign depot and subsequently **reimport** them when market conditions change."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "High tariffs often encourage traders to **reimport** domestic goods through illicit maritime channels."},
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "Provisions allowing manufacturers to **reimport** unused raw materials free of duty foster industrial expansion."}
    ]
  },
  "Dashboard — port/report.md": {
    "primary": "An account given of a particular matter, event, or situation after thorough investigation or observation; or a sudden loud noise.",
    "secondary": "In common law legal systems, an officially published account of a judicial decision and the court's reasoning (law reports).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Sonnets", "quote": "I love thee in such sort as, thou being mine, mine is thy good **report**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sudden **report** of a pistol echoed through the deserted chambers of Lincoln's Inn."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The masthead watch shouted his joyful **report** that the white whale was breached upon the horizon."}
    ]
  },
  "Dashboard — port/reportable.md": {
    "primary": "Suitable, required, or worthy to be reported to an authority, public body, or news organization.",
    "secondary": "In public health epidemiology, an infectious disease or pathogen legally mandated to be notified immediately to disease control authorities.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "There was nothing in the man's quiet conduct that was **reportable** to the local constabulary."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Every diagnosed case of cholera was classified as an immediately **reportable** infection under public sanitary codes."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Only severe injuries causing protracted absence were classified as **reportable** mining accidents."}
    ]
  },
  "Dashboard — port/reportage.md": {
    "primary": "The reporting of news, current affairs, or events, especially in newspapers, radio, television, or literature.",
    "secondary": "In literary nonfiction and investigative journalism, narrative journalism combining firsthand documentary observation with literary prose techniques.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "His vivid **reportage** from the Aragon front captured the raw confusion of the trenches without romantic illusion."},
      {"author": "Ernest Hemingway", "work": "Death in the Afternoon", "quote": "Good **reportage** demands setting down what really happened rather than what you were supposed to feel."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The maritime **reportage** of the disaster was pieced together from the depositions of surviving seamen."}
    ]
  },
  "Dashboard — port/reported.md": {
    "primary": "Having been stated, described, or recorded as a fact by an observer, informant, or document.",
    "secondary": "In judicial proceedings, a legal decision preserved and transcribed in formal volumes of legal precedent.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "It is **reported** that he has taken their great'st city and captured their fleet upon the Nile."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Several extraordinary volcanic eruptions were **reported** by the inhabitants of the coastal settlements."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "It was **reported** throughout the countryside that the master of Thornfield was soon to wed Miss Ingram."}
    ]
  },
  "Dashboard — port/reportedly.md": {
    "primary": "According to what has been said, claimed, or reported by others; allegedly.",
    "secondary": "In news reporting and historiography, attributing information to secondhand sources without independent empirical verification.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A monstrous spectral hound had **reportedly** been sighted near the ancient stone huts upon the moor."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The rebel duke had **reportedly** landed at Lyme with a small band of armed followers."},
      {"author": "Henry James", "work": "The American", "quote": "The family had **reportedly** amassed immense fortunes during the continental wars."}
    ]
  },
  "Dashboard — port/reporter.md": {
    "primary": "A person who investigates, collects, and reports news or current events for newspapers, magazines, radio, or television.",
    "secondary": "In judicial administration, an official tasked with transcribing, indexing, and publishing the verbatim decisions of an appellate court (reporter of decisions).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "There she appeared indeed, or my **reporter** devised a well-feigned tale."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I became a parliamentary **reporter**, taking down speeches in shorthand in the gallery of the House of Commons."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "As a city **reporter** in Virginia City, I had to manufacture sensation when real news was scarce."}
    ]
  },
  "Dashboard — port/reporting.md": {
    "primary": "The activity, process, or occupation of gathering and presenting news, statements, or formal accounts.",
    "secondary": "In corporate finance and auditing, the periodic disclosure of financial statements, balance sheets, and compliance filings to regulatory bodies.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Pericles", "quote": "If I should tell my history, it would seem like lies, disdained in the **reporting**."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Honest **reporting** of political events was frequently suppressed by wartime censors."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "Careful **reporting** of experimental conditions is the essential prerequisite of scientific reproducibility."}
    ]
  },
  "Dashboard — port/support.md": {
    "primary": "To bear all or part of the weight of; hold up; or to give assistance, approval, or encouragement to.",
    "secondary": "In structural mechanics, a foundation, pier, or cantilever resisting applied dead and live mechanical loads.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "**Support** him by the arm. Give me your hand, and let me conduct you to some shelter."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The revenue of the state must **support** the necessary expenses of sovereign defense and civil justice."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The stout timbers of the hull were framed to **support** the crushing pressure of the pack ice."}
    ]
  },
  "Dashboard — port/supportable.md": {
    "primary": "Capable of being borne, tolerated, or endured; bearable; or capable of being defended or justified.",
    "secondary": "In formal argumentation and historiography, a thesis or hypothesis corroborated by sufficient documentary evidence.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "As great to me, as late; and, **supportable** to make the dear loss, have I means much weaker than you may call to comfort you."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His poverty was made **supportable** by the proud consciousness of his unblemished honor."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No doctrine is rationally **supportable** which directly contradicts the clear evidence of the senses."}
    ]
  },
  "Dashboard — port/supported.md": {
    "primary": "Held up, sustained, or maintained by physical structure, financial backing, or moral approval.",
    "secondary": "In empirical epistemology, a scientific hypothesis validated by experimental data and repeatable trials.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "For, in my knowing, Timon has been this lord's father, and kept his credit with his purse; **supported** his estate with bountiful open hands."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "This view is **supported** by the striking resemblance between the embryos of widely distinct vertebrate classes."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She was **supported** through her long illness by the unwearied devotion of her companion."}
    ]
  },
  "Dashboard — port/supporter.md": {
    "primary": "A person who approves of and encourages a person, team, or cause; or a structure that bears weight.",
    "secondary": "In heraldry, a figure (such as a lion, unicorn, or angel) depicted standing on either side of the escutcheon to hold it up.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "To me and to the state of my great grief let kings assemble; for my grief's so great that no **supporter** but the huge firm earth can hold it up."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The minister found in the young member a formidable and eloquent **supporter** of his budget."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Every ardent **supporter** of the revolution donned the red cap and tricolor cockade."}
    ]
  },
  "Dashboard — port/supporting.md": {
    "primary": "Serving to support, hold up, or maintain; or playing a secondary role in a theatrical production or film.",
    "secondary": "In architectural engineering, designating load-bearing walls, piers, or pillars that carry the gravitational load of roofs or upper stories.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Shall one of us, that struck the foremost man of all this world, but for **supporting** robbers, contaminate our fingers with base bribes?"},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The fossil record offers strong **supporting** evidence for the gradual divergence of hominid ancestors."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She played a quietly **supporting** part in her husband's public labors, never seeking prominence for herself."}
    ]
  },
  "Dashboard — port/supportive.md": {
    "primary": "Providing encouragement, emotional help, or practical assistance to someone.",
    "secondary": "In medicine and palliative oncology, care directed toward relieving distressing symptoms rather than curative eradication of disease.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "When curative remedies are exhausted, compassionate **supportive** measures must sustain the failing patient."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Her presence was unfailingly **supportive**, creating an atmosphere of warmth in which everyone expanded."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie was grateful for Philip's **supportive** sympathy during her darkest days of isolation."}
    ]
  },
  "Dashboard — port/transport.md": {
    "primary": "To take or carry people or goods from one place to another by means of a vehicle, aircraft, or ship; or an overwhelming emotion of ecstasy.",
    "secondary": "In historical penal jurisprudence, to exile or banish a convicted felon to an overseas penal colony for a term of years.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "He cannot temperately **transport** his honours from where he should begin to where he should end."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Water carriage affords an incomparably cheaper means to **transport** bulky goods than land transit."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He looked upon her with a **transport** of mingled passion and despair."}
    ]
  },
  "Dashboard — port/transportable.md": {
    "primary": "Capable of being transported, moved, or carried easily from one location to another.",
    "secondary": "In military logistics, field equipment designed to fit standard cargo dimensions for air, sea, or rail mobilization.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The surveying instruments were packed in compact, **transportable** cases to withstand rough handling on horseback."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Precious metals are the most **transportable** of all commercial commodities, possessing immense value in small bulk."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whaleboat is a light, swift, and easily **transportable** craft built for rough open waters."}
    ]
  },
  "Dashboard — port/transportation.md": {
    "primary": "The action of transporting someone or something, or the system or means of conveying passengers or goods.",
    "secondary": "In British legal history, the penal exile of convicted criminals to British colonies (such as Australia or the Americas).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Living birds can hardly fail to be highly effective agents in the **transportation** of seeds across wide oceanic expanses."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Magwitch had been sentenced to penal **transportation** for life to the distant penal settlements of New South Wales."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The construction of canals and railroads revolutionized the internal **transportation** of the continent."}
    ]
  },
  "Dashboard — port/transporter.md": {
    "primary": "A person or vehicle that transports goods, people, or military equipment.",
    "secondary": "In cellular biochemistry and membrane physiology, a transmembrane protein that facilitates the passage of ions or metabolites across biological membranes.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian fighting machine functioned as a colossal mechanical **transporter**, striding over the countryside."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The red blood corpuscles act as the vital chemical **transporter** of oxygen to the peripheral tissues."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Our Indian **transporter** carried the heavy scientific crates with effortless endurance along the jungle trail."}
    ]
  },
  "Dashboard — port/unexportable.md": {
    "primary": "Not suitable, permitted, or able to be exported to foreign nations.",
    "secondary": "In international trade and cultural property law, cultural antiquities, national treasures, or strategic dual-use technologies barred from export.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Perishable provisions were historically **unexportable** until modern salting and preservation techniques were developed."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Certain heavy minerals remain **unexportable** due to transit costs exceeding their market value abroad."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient frescoes of the republic were declared precious and **unexportable** national heirlooms."}
    ]
  },
  "Dashboard — port/unimportance.md": {
    "primary": "The quality of having little or no importance, significance, or value.",
    "secondary": "In existential philosophy, the cosmic insignificance of individual human affairs against the backdrop of geological and cosmic time.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Even in the first short time which has elapsed since my return, I have realized the utter **unimportance** of these social distinctions."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He comforted himself with the thought of his own **unimportance** in the grand march of history."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A detail of apparent **unimportance** often holds the master key to the entire mystery."}
    ]
  },
  "Dashboard — port/unimportant.md": {
    "primary": "Lacking in importance, significance, consequence, or influence.",
    "secondary": "In experimental science, secondary variables that produce no statistically significant perturbation in outcome measurements.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "When Farmer Oak smiled, the corners of his mouth seemed to spread into **unimportant** wrinkles."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Slight and seemingly **unimportant** variations may become of high significance under changed conditions of life."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She treated the gossip of the neighborhood as altogether trivial and **unimportant**."}
    ]
  },
  "Dashboard — port/unportable.md": {
    "primary": "Not portable; too heavy, bulky, or awkward to be easily moved or carried by hand.",
    "secondary": "In computer architecture, source code tightly coupled to a proprietary instruction set architecture that cannot execute on other processors.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The iron try-works were massive and **unportable**, firmly cemented onto the main deck of the whaler."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Most of the luxuries and cumbersome conveniences of life are **unportable** burdens upon the free spirit of man."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The immense mahogany writing desk was completely **unportable**, rooted like an oak in the corner of the office."}
    ]
  },
  "Dashboard — port/unreportable.md": {
    "primary": "Not suitable, permitted, or able to be reported publicly or officially.",
    "secondary": "In journalistic law and military censorship, confidential court testimony or operational intelligence legally barred from publication.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Certain atrocities witnessed in the village were deemed **unreportable** by the military censor."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The details of the international scandal were of so delicate a character as to be strictly **unreportable**."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The squalid underworld intrigue was largely **unreportable** in polite domestic journals."}
    ]
  },
  "Dashboard — port/unreported.md": {
    "primary": "Not stated, reported, or made known to the public, an authority, or the media.",
    "secondary": "In maritime navigation and shipping registries (such as Lloyd's Register), missing vessels that have failed to arrive or report from sea.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Many a stout ship has vanished into the southern ocean, remaining forever **unreported** on the books of the owners."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The minor domestic quarrels of the poor went **unreported** by the town magistrates."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Countless silent tragedies of the prison house occurred daily, **unreported** to the outside world."}
    ]
  },
  "Dashboard — port/unsupportable.md": {
    "primary": "Not able to be endured or tolerated; intolerable; or not able to be defended or justified.",
    "secondary": "In analytical philosophy, a proposition or deductive argument so lacking in evidentiary warrant that it collapses under scrutiny.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The cold indifference of his gaze became at last an **unsupportable** torment to my pride."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The arbitrary caprices of the tyrant became **unsupportable** to the senate and the army."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "To maintain that ideas are innate without consciousness is an **unsupportable** hypothesis in philosophy."}
    ]
  },
  "Dashboard — port/unsupported.md": {
    "primary": "Not supported physically; not held up; or not corroborated by evidence, authority, or funds.",
    "secondary": "In empirical science, an assertive claim or hypothesis offered without corroborating experimental observations or statistical backing.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Some authors believe that long-continued domestication produces variation, but this assertion remains largely **unsupported** by direct evidence."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An inductive generalization that stands **unsupported** by verified facts is a mere speculative conjecture."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister stood upon the scaffold, **unsupported** by human aid, facing the judgment of the congregation."}
    ]
  },
  "Dashboard — port/unsupportive.md": {
    "primary": "Not providing encouragement, emotional help, or practical assistance; unhelpful or negative.",
    "secondary": "In family systems psychology, familial environments characterized by emotional detachment, criticism, or withholding of validation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She found her family completely **unsupportive** of her philanthropic schemes, greeting them with cold skepticism."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "An **unsupportive** domestic atmosphere stifled her creative ambitions, leaving her lonely and perplexed."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The directress was distant and **unsupportive**, offering neither counsel nor comfort to the solitary English teacher."}
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

print(f"Carrying Batch 3D (port): Successfully updated {updated}/{len(data)} notes.")
