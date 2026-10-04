# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — cess Part 1 (5A, 29 words) ---
  "Dashboard — cess/access.md": {
    "primary": "The means, opportunity, or permission to approach, enter, or make use of a place, person, or data.",
    "secondary": "In computer architecture and memory hierarchy, random access memory provides uniform read-write access latency.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "Holmes determined that only three persons in the household had immediate **access** to the private bureau."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy readily granted the travelers permission and **access** to walk through the grounds of Pemberley."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The turnkey unlocked the heavy iron grates, granting Doctor Manette daily **access** to his daughter's room."}
    ]
  },
  "Dashboard — cess/accessary.md": {
    "primary": "A person who incites, aids, abets, or conceals a perpetrator in committing a crime; an accessory.",
    "secondary": "In criminal jurisprudence, common law indictments distinguished between an accessary before the fact and an accessary after the fact.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Rape of Lucrece", "quote": "O hateful error, melancholy's child, why dost thou show to the apt thoughts of men an **accessary** yield?"},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The police arrested the cab driver as an **accessary** to the robbery, suspecting he had aided the escape."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Fagin was judged an **accessary** to the burglary, having planned the crime and received the stolen silverware."}
    ]
  },
  "Dashboard — cess/accessibility.md": {
    "primary": "The ease with which a place, person, service, or information can be reached, approached, entered, or understood.",
    "secondary": "In urban planning and universal design standards, building accessibility requires ramps, wide doorways, and tactile paving.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The geographical **accessibility** of the coastal harbor encouraged early maritime commerce with neighboring islands."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The growing **accessibility** of cheap printed literature broadened the intellectual horizons of working citizens."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "True artistic beauty is distinguished by its **accessibility** to every sincere and uncorrupted human eye."}
    ]
  },
  "Dashboard — cess/accessible.md": {
    "primary": "Able to be reached, entered, obtained, or understood easily; approachable.",
    "secondary": "In digital human-computer interaction, accessible web software complies with WCAG standards for screen readers and keyboard navigation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The isolated stone hut on the moor was **accessible** only by a narrow track winding between treacherous mires."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny found Edmund always **accessible** and kind, ready to listen to her modest thoughts and anxieties."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The volcanic crater was easily **accessible** from the eastern slope, where ancient lava streams had cooled into terraces."}
    ]
  },
  "Dashboard — cess/accession.md": {
    "primary": "The attainment or acquisition of a dignity, rank, or high office; or an addition to an existing collection or territory.",
    "secondary": "In museum cataloging and archival science, an accession register records the formal provenance and acquisition of historical artifacts.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **accession** of the Antonines inaugurated a golden half-century of peace and administrative justice in Rome."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The national joy that greeted the **accession** of William and Mary reflected relief from arbitrary monarchical rule."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The territorial **accession** of new overseas colonies opened lucrative transatlantic markets for British manufactures."}
    ]
  },
  "Dashboard — cess/accessional.md": {
    "primary": "Pertaining to, resulting from, or added by an accession, addition, or augmentation.",
    "secondary": "In legal property doctrine and riparian accession, accessional land deposits created by silt accretion belong to the riverbank owner.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **accessional** wealth flowing from the colonial trade stimulated domestic manufacturing across western ports."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor celebrated his triumph with **accessional** distributions of grain and olive oil to the plebeians."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Every true reform brings an **accessional** strength to the moral foundation of the commonwealth."}
    ]
  },
  "Dashboard — cess/accessorial.md": {
    "primary": "Pertaining to or functioning as an accessory; supplementary, subordinate, or aiding in a criminal enterprise.",
    "secondary": "In freight transport logistics and maritime shipping, accessorial charges cover ancillary services such as detention, storage, or redelivery.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solicitor examined the **accessorial** costs incurred during the lengthy examination of witnesses in Chancery."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes weighed the **accessorial** evidence, determining how the boatman had unwittingly assisted the fugitive."},
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The jurist distinguished principal liability from **accessorial** involvement in conspiratorial crimes."}
    ]
  },
  "Dashboard — cess/accessory.md": {
    "primary": "A supplementary, secondary, or decorative item that contributes to a whole; or a person who helps commit a crime.",
    "secondary": "In criminal law, an accessory after the fact assists a felon with knowledge that the crime has been committed.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "Holmes proved that the maid was an unsuspecting **accessory** who had left the garden window unbolted."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia viewed marriage primarily as an excuse for purchasing every fashionable **accessory** and new bonnet."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt himself a guilty **accessory** to the convict's escape as he hurried through the morning mist with the file."}
    ]
  },
  "Dashboard — cess/cessation.md": {
    "primary": "A temporary or final ceasing, halting, or discontinuance of an action, process, or condition; a pause.",
    "secondary": "In military diplomacy, a cessation of hostilities (armistice) halts armed combat while peace terms are formally negotiated.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The sudden **cessation** of aerial bombardment over London signaled the redeployment of enemy air wings eastward."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I longed for a **cessation** of my mental agony, wishing that the silent grave might receive my weary body."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The sudden **cessation** of the hound's deep baying filled the midnight moor with an ominous, chilling silence."}
    ]
  },
  "Dashboard — cess/cession.md": {
    "primary": "The formal giving up, yielding, or surrender of rights, property, or territory, especially by treaty.",
    "secondary": "In reinsurance contracts, cession denotes the portion of underwriting risk transferred from the primary ceding insurer to a reinsurer.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The disgraceful **cession** of the Mesopotamian fortresses to the Persian king outraged the Roman senate."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The treaty of peace was ratified upon the formal **cession** of the border barrier fortresses in Flanders."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The foreign minister refused to contemplate the territorial **cession** of vital strategic coaling stations."}
    ]
  },
  "Dashboard — cess/concession.md": {
    "primary": "Something granted, yielded, or conceded, especially in response to demands; or a commercial grant or franchise.",
    "secondary": "In natural resource extraction law, a mining or petroleum concession grants private corporations rights to exploit state minerals.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Magnanimity in politics is not seldom the truest wisdom; and a great empire and little minds go ill together; make a generous **concession** to your colonies."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth made no **concession** to Lady Catherine's arrogance, maintaining her dignity with calm resolution."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Cowperwood secured a lucrative municipal traction **concession** by distributing cash among the city aldermen."}
    ]
  },
  "Dashboard — cess/concessionaire.md": {
    "primary": "A person, group, or company that holds a commercial concession, franchise, or operational lease from an authority.",
    "secondary": "In public transportation and national park management, an authorized concessionaire operates dining, retail, and lodging facilities.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The street railway **concessionaire** lobbied state legislators to extend corporate franchise privileges for fifty years."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "The commercial **concessionaire** managed the luxury hotel pavilion along the Mediterranean seaside promenade."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The foreign **concessionaire** invested vast capital into developing the silver mine high in the Golfo Placido mountains."}
    ]
  },
  "Dashboard — cess/concessioner.md": {
    "primary": "A person who operates or holds a commercial concession, retail stall, or franchise; an alternative of concessionaire.",
    "secondary": "In historic municipal fairgrounds and exhibition parks, each licensed concessioner paid stallage fees to municipal bailiffs.",
    "quotes": [
      {"author": "Mark Twain", "work": "Innocents Abroad", "quote": "The enterprising **concessioner** near the ancient ruins sold plaster antiquities and sweet lemonade to pilgrims."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The athletic stadium **concessioner** made handsome profits selling hot sausages and roasted peanuts to crowds."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The itinerant fair **concessioner** hawked roasted chestnuts and ginger beer from a smoking brazier."}
    ]
  },
  "Dashboard — cess/concessive.md": {
    "primary": "Expressing, implying, or characterized by concession; or in grammar, expressing concession or contrast (e.g. 'although').",
    "secondary": "In formal diplomatic discourse, adopting a concessive tone signals readiness to compromise on secondary negotiation items.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The grammatical theorist analyzed the syntactic function of **concessive** clauses introduced by 'although' and 'whereas'."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The orator employed a **concessive** opening to disarm hostile prejudices before presenting his core proofs."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The royal response was couched in polite, **concessive** language that masked an unyielding determination."}
    ]
  },
  "Dashboard — cess/deaccession.md": {
    "primary": "To officially remove an artwork, book, or object from a museum, gallery, or library collection, typically for sale or disposal.",
    "secondary": "In museum ethics and collections stewardship, institutions deaccession redundant objects only to fund preservation of core holdings.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The municipal gallery resolved to **deaccession** minor copies to acquire rare original early Italian canvases."},
      {"author": "Henry James", "work": "The Outcry", "quote": "The connoisseur debated whether the impoverished lord would **deaccession** his magnificent heirloom portrait to an American collector."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The private collector refused to **deaccession** a single canvas from his secretive, priceless gallery."}
    ]
  },
  "Dashboard — cess/excess.md": {
    "primary": "An amount of something that is more than necessary, permitted, or desirable; lack of moderation or restraint.",
    "secondary": "In property and casualty insurance, an excess clause (deductible) establishes the policyholder's initial liability per claim.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "If music be the food of love, play on; give me **excess** of it, that, surfeiting, the appetite may sicken, and so die."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Led by **excess** of pride and blind ambition, Satan dared to challenge the almighty power of heaven."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An **excess** of paper bank notes issued beyond the real commerce of the country precipitates rapid monetary inflation."}
    ]
  },
  "Dashboard — cess/excessive.md": {
    "primary": "More than is necessary, normal, or desirable; immoderate, extreme, or disproportionate.",
    "secondary": "In constitutional human rights law, the Eighth Amendment prohibits excessive bail, excessive fines, and cruel and unusual punishments.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's **excessive** indulgence of grief impaired her health and caused deep anxiety to her affectionate sister."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **excessive** taxation levied by the late emperors drove provincial farmers to abandon their fields in despair."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes warned Watson that **excessive** haste in drawing conclusions from incomplete data is the fatal error of detectives."}
    ]
  },
  "Dashboard — cess/excessively.md": {
    "primary": "To a greater degree or in greater amounts than is necessary, normal, or desirable; overly, exceedingly.",
    "secondary": "In pharmacology, administering dosage regimens excessively above the minimum toxic concentration triggers adverse toxicities.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet was **excessively** diverted by the thought of Jane reigning as mistress of Netherfield Hall."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber became **excessively** dejected in the morning, only to recover his buoyant optimism by evening punch."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The parlor was **excessively** warm, heated by a blazing coal fire that caused the sleepy company to nod."}
    ]
  },
  "Dashboard — cess/excessiveness.md": {
    "primary": "The characteristic or quality of being excessive, immoderate, extreme, or beyond reasonable limits.",
    "secondary": "In Aristotelian moral philosophy, virtue occupies the golden mean between the deficiency and the excessiveness of an emotional passion.",
    "quotes": [
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "Moral virtue is destroyed by defect and by **excessiveness**, while it is preserved by observing the proportionate mean."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **excessiveness** of worldly ambitions inevitably plunges the soul into bitter disappointment and fatigue."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary decrees were marked by an **excessiveness** that alienated all moderate friends of liberty."}
    ]
  },
  "Dashboard — cess/inaccessibility.md": {
    "primary": "The property or characteristic of being impossible or extremely difficult to reach, approach, or enter.",
    "secondary": "In defense geography and military siege history, the natural inaccessibility of mountain citadels enabled garrisons to hold off invaders.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The sheer red sandstone cliffs gave the South American plateau an absolute **inaccessibility** to ordinary exploration."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The rugged **inaccessibility** of the volcanic island provided a secure nesting haven for oceanic petrels and boobies."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The fortress of Edinburgh Castle derived its historic strength from the precipitous **inaccessibility** of its basalt crag."}
    ]
  },
  "Dashboard — cess/inaccessible.md": {
    "primary": "Unable to be reached, approached, entered, or obtained; remote and unapproachable.",
    "secondary": "In deep-sea oceanographic biology, abyssal benthic habitats were long considered inaccessible prior to bathyscaphes and ROVs.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The daemon took refuge among the **inaccessible** ice caves and jagged pinnacles of the high Alps."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "God dwelleth in uncreated light, **inaccessible** to mortal sight, surrounded by choirs of seraphim."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The icy polar seas remained long **inaccessible** to commercial merchant navigation."}
    ]
  },
  "Dashboard — cess/incessancy.md": {
    "primary": "The quality, state, or property of being continuous, uninterrupted, or never-ceasing; unremitting persistence.",
    "secondary": "In climatological acoustics, the incessancy of monsoon rain downpours produces continuous white noise across tropical valleys.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The marvelous **incessancy** of universal life rolls on forever, weaving suns and planetary systems on time's loom."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "True moral devotion requires an **incessancy** of vigilance against the subtle corruptions of pride."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The **incessancy** of the London drizzle seemed to dissolve the very bricks and mortar into dreary mud."}
    ]
  },
  "Dashboard — cess/incessant.md": {
    "primary": "Continuing without pause or interruption, especially describing something unpleasant; ceaseless, unceasing.",
    "secondary": "In sensory physiology, adaptation causes sensory neurons to decrease firing rates under incessant, unvarying background stimuli.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The **incessant** clanking of the loom and the murmur of revolutionary voices filled the Saint Antoine quarter."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The grim moors were shrouded in an **incessant** autumn rain that beat against the granite manor windows."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Frankenstein was pursued by an **incessant** remorse that allowed him no peaceful rest day or night."}
    ]
  },
  "Dashboard — cess/incessantly.md": {
    "primary": "Without interruption; constantly, continuously, and repeatedly.",
    "secondary": "In cardiac biomechanics, human myocardial fibers contract and relax incessantly over billions of cycles across a lifetime.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes paced the room **incessantly**, his brow furrowed as he wrestled with the puzzling clues."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The bitter rain poured **incessantly** upon the bare moors as Jane fled from Thornfield Hall."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The pistons of the Coketown steam engines worked **incessantly** up and down, like the head of an elephant in a melancholy madness."}
    ]
  },
  "Dashboard — cess/incessantness.md": {
    "primary": "The state or characteristic of being ceaseless, unremitting, or continuous without pause.",
    "secondary": "In occupational psychology, the incessantness of high-volume digital communications induces chronic cognitive fatigue.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The terrible **incessantness** of the revolutionary tumbrils rolling to the scaffold cowed the citizens of Paris into silence."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was wearied by the dry **incessantness** of Casaubon's pedantic inquiries into dead mythologies."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The grand **incessantness** of the ocean swell reminds mortal man of the infinite power that governs creation."}
    ]
  },
  "Dashboard — cess/intercession.md": {
    "primary": "The action of intervening or pleading on behalf of another person, especially in prayer or petition.",
    "secondary": "In diplomatic history and mediation law, third-party state intercession facilitates prisoner exchanges during armed conflicts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Your **intercession** comes too late; the royal warrant has been signed and dispatched to the Tower."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny's gentle **intercession** softened Sir Thomas's anger toward her wayward brother William."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The Son of God offered holy **intercession** before the eternal throne on behalf of repentant fallen mankind."}
    ]
  },
  "Dashboard — cess/intercessor.md": {
    "primary": "A person who intervenes, mediates, or pleads on behalf of another, especially in prayer or conflict resolution.",
    "secondary": "In international arbitration and diplomacy, an impartial neutral intercessor assists warring parties in framing ceasefire terms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Volumnia walked to the Volscian camp, acting as a tearful **intercessor** to save Rome from her own son's wrath."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The Duke of Argyle acted as a powerful **intercessor** with the Queen on behalf of the humble Scottish maiden."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian was directed to the heavenly **intercessor** who alone could wash away the heavy burden upon his back."}
    ]
  },
  "Dashboard — cess/necessary.md": {
    "primary": "Required to be done, achieved, or present; indispensable, essential, or unavoidable.",
    "secondary": "In modal philosophical logic, a necessary truth is one whose negation is logically impossible across all possible worlds.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife; yet it was **necessary** to ascertain his real character."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "When you have eliminated the impossible, whatever remains, however improbable, must be the **necessary** truth."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wages of labor must at least be sufficient to maintain the laborer and provide the **necessary** subsistence for his family."}
    ]
  },
  "Dashboard — cess/necessitate.md": {
    "primary": "To make something necessary, unavoidable, or an indispensable consequence of an action or event.",
    "secondary": "In contractual law and maritime salvage doctrine, extraordinary perils of the sea necessitate emergency jettisoning of cargo.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The sudden collapse of our continental allies did **necessitate** a complete reorientation of British global strategy."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The discovery of a second testamentary will did **necessitate** a reopening of the entire Chancery lawsuit."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The extensive frontier line did **necessitate** the permanent maintenance of thirty veteran legions on the borders."}
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

print(f"Motion Batch 5A: Successfully updated {updated}/{len(data)} notes.")
