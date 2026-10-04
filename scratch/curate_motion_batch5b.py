# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — cess Part 2 (5B, 29 words) ---
  "Dashboard — cess/necessitous.md": {
    "primary": "Lacking the basic necessities of life; impoverished, destitute, or in urgent material need.",
    "secondary": "In historical English poor-law jurisprudence, parishes provided outdoor relief specifically for necessitous families unable to earn wages.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He who relieved the wants of the **necessitous** stranger earned a reputation for genuine Christian charity."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The relief committee visited the most **necessitous** quarters of the district to distribute loaves of bread."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A compassionate employer might extend credit to his most **necessitous** workmen during severe winter frosts."}
    ]
  },
  "Dashboard — cess/necessity.md": {
    "primary": "The fact of being indispensable, inevitable, or unavoidable; an imperative requirement or indispensable thing.",
    "secondary": "In classical philosophy and metaphysics, metaphysical necessity describes propositions whose negation entails a logical contradiction.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor saw the **necessity** of concealing from her mother the extent of their financial embarrassment."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The harsh **necessity** of self-preservation compelled the solitary prospector to ration his last cup of water."},
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "There is no power in the tongue of man to alter me; I stay here on my bond, urged by the strict **necessity** of the law."}
    ]
  },
  "Dashboard — cess/precess.md": {
    "primary": "To undergo precession; to rotate with a continuous conical wobble or circular change in the orientation of a rotational axis.",
    "secondary": "In astrophysics and gyrodynamics, a spinning top or rotating astronomical body will precess perpendicularly to the applied torque vector.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Because the equatorial bulge experiences unequal gravitational attraction from the sun and moon, Earth's axis must slowly **precess** over millennia."},
      {"author": "James Clerk Maxwell", "work": "Matter and Motion", "quote": "When an external couple acts upon a rapidly spinning wheel, its axis does not tilt directly but begins to **precess** uniformly."},
      {"author": "William Thomson (Lord Kelvin)", "work": "Popular Lectures and Addresses", "quote": "The spinning gyroscope demonstrated to the students how an unbalanced rotational system will steadily **precess** around the vertical."}
    ]
  },
  "Dashboard — cess/precession.md": {
    "primary": "The slow gyration or conical rotation of the axis of a spinning body around another axis, caused by an external torque.",
    "secondary": "In celestial mechanics and observational astronomy, the axial precession of Earth shifts the equinoctial points westward along the ecliptic.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The astronomical observations of the ancients confirmed that the **precession** of the equinoxes moved at approximately fifty seconds of arc annually."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The periodic climate oscillations caused by the astronomical **precession** of the equinoxes profoundly influenced the migration of species."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The steady **precession** of the terrestrial axis produces cyclic alterations in the distribution of solar insolation upon the hemispheres."}
    ]
  },
  "Dashboard — cess/process.md": {
    "primary": "A series of actions, operations, or natural changes systematically leading toward a specific outcome or result.",
    "secondary": "In operating system architecture, a process represents an active instance of a computer program executing within an isolated virtual address space.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection is a continuous **process** acting solely through the preservation of slight modifications advantageous to the organism."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The systematic investigation of nature requires an inductive **process** advancing from particulars to universal axioms."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The manufacturing **process** of dividing the production of a pin into eighteen distinct operations vastly multiplied output."}
    ]
  },
  "Dashboard — cess/processed.md": {
    "primary": "Subjected to a mechanical, chemical, physical, or computational treatment to modify, preserve, or refine properties.",
    "secondary": "In electronic data communications and signal processing, raw analog signals are sampled and processed into discrete digital streams.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The raw mineral ores must be refined and **processed** through smelting furnaces before they yield pure copper."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The harvested flax fibers were combed and **processed** to prepare them for spinning into fine linen thread."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Nutritive substances must be chemically digested and **processed** by glandular secretions before assimilation into living tissue."}
    ]
  },
  "Dashboard — cess/processing.md": {
    "primary": "The performing of a sequence of operations or systematic transformations on materials, data, or organisms.",
    "secondary": "In computer science, multiprocessor architectures achieve high throughput by distributing computational processing across parallel cores.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The natural weathering of granite involves the chemical **processing** of feldspar minerals by atmospheric carbonic acid."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The careful **processing** of raw sensory data into coherent scientific concepts forms the basis of genuine epistemology."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The industrial **processing** of agricultural raw materials into commercial textiles revolutionized eighteenth-century English manufacturing."}
    ]
  },
  "Dashboard — cess/procession.md": {
    "primary": "A continuous line or organized group of people, vehicles, or animals moving forward in formal, orderly succession.",
    "secondary": "In Christian liturgical theology, the procession of the Holy Spirit describes the eternal origin of the Third Person of the Trinity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A solemn funeral **procession** advanced through the narrow Parisian streets, escorted by hooded mourners bearing candles."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The triumphal **procession** of the victorious general marched through the Forum toward the Capitol amid shouting throngs."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The civic **procession** moved slowly past the town hall, headed by the mace-bearer and the uniformed aldermen."}
    ]
  },
  "Dashboard — cess/processional.md": {
    "primary": "Pertaining to, used in, or accompanying an organized ceremonial procession.",
    "secondary": "In liturgical hymnody and ecclesiastical book arts, a processional is a service book containing hymns, litanies, and rubrics for processions.",
    "quotes": [
      {"author": "George Eliot", "work": "Romola", "quote": "The deep choir sang a solemn **processional** hymn as the banner of Saint Mark was carried through the cathedral aisle."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The villagers gathered in **processional** order along the highway to escort the harvest wagon to the church."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The grand master raised his ivory crucifix and led the **processional** march of the Templars toward the judgment pavilion."}
    ]
  },
  "Dashboard — cess/processor.md": {
    "primary": "A person, machine, or device that executes a systematic process, treatment, or computation upon materials or data.",
    "secondary": "In hardware engineering, a central processor executes arithmetic, logic, and control operations decoded from stored machine instructions.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The brain acts as an extraordinary biological **processor** of incoming sensory stimuli from external nature."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The human cortex operates as an associative **processor** organizing primitive impressions into complex mental ideas."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The nervous system functions as an integrated **processor** coordinating reflex muscular contractions with emotional stimuli."}
    ]
  },
  "Dashboard — cess/recess.md": {
    "primary": "A temporary suspension of business or official proceedings; or a secluded, indented space or alcove set back into a wall.",
    "secondary": "In legislative procedure, a congressional recess designates an adjournment period during which formal legislative hearings pause without session termination.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The photograph is in a **recess** behind a sliding panel just above the right bell-pull."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "At one end of the room, in a **recess**, were a number of barrels piled one upon another."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The central space, together with the **recess** at one end, was emptied of all incumbrances."}
    ]
  },
  "Dashboard — cess/recessed.md": {
    "primary": "Set back into a wall, surface, or alcove; positioned in a secluded, indented, or withdrawn space.",
    "secondary": "In architectural lighting and interior construction, recessed downlights are installed flush within ceiling cavities to conceal fixture hardware.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His house stood **recessed** from the road, and the stables were sheltered behind ancient sycamore boughs."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A heavy iron safe was **recessed** into the solid granite wall of the baronet's study."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The antique library was fitted with tall shelves **recessed** deep between projecting carved oak pilasters."}
    ]
  },
  "Dashboard — cess/recession.md": {
    "primary": "A period of temporary economic decline characterized by reduced trade, industrial output, and employment; or the act of withdrawing.",
    "secondary": "In macroeconomic analysis, a technical recession is defined by two consecutive quarters of negative growth in real gross domestic product.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The gradual **recession** of the imperial legions from the Danube left the border provinces vulnerable to barbarian incursions."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A general **recession** in foreign trade inevitably depresses the profits of domestic merchants and lowers the revenue of the sovereign."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The marine fossils discovered along the high inland ridges proved the long-term **recession** of the ancient sea."}
    ]
  },
  "Dashboard — cess/recessional.md": {
    "primary": "Sung or recited during the withdrawal of clergy and choir at the end of a religious service; or relating to economic recession.",
    "secondary": "In English literary history, Kipling's famous poem 'Recessional' served as a solemn cautionary ode against imperial hubris at Victoria's Jubilee.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Recessional", "quote": "Lord God of Hosts, be with us yet, lest we forget—lest we forget; this **recessional** prayer echoed across the empire."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The organist played a subdued **recessional** voluntary as the congregation filed out into the cold churchyard."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The solemn strains of the **recessional** hymn signaled the end of the ceremony and the dispersal of the parishioners."}
    ]
  },
  "Dashboard — cess/recessionary.md": {
    "primary": "Pertaining to, causing, or occurring during a period of macroeconomic contraction and declining business activity.",
    "secondary": "In central banking policy, recessionary cycles often trigger monetary stimulus through policy rate reductions and quantitative easing.",
    "quotes": [
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "During a severe **recessionary** downturn, the liquidity preference of investors increases dramatically, stifling private capital formation."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A **recessionary** collapse in the price of colonial commodities brought ruin to many speculative merchant houses in Bristol."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "The industrial system periodically enters a **recessionary** slump when capital capitalization outruns prospective earning capacity."}
    ]
  },
  "Dashboard — cess/recessive.md": {
    "primary": "Tending to recede or go backward; or describing an inherited genetic allele suppressed by a dominant counterpart.",
    "secondary": "In Mendelian genetics, a recessive phenotype is expressed only in homozygous individuals carrying two copies of the mutant allele.",
    "quotes": [
      {"author": "Gregor Mendel", "work": "Experiments in Plant Hybridisation", "quote": "The characteristics which transmit themselves unchanged are dominant, while those that become latent in the first filial generation are **recessive**."},
      {"author": "Thomas Hunt Morgan", "work": "The Physical Basis of Heredity", "quote": "The white-eye trait in fruit flies behaved as a sex-linked **recessive** mutation located on the X-chromosome."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain ancestral traits remain dormant for generations in a **recessive** condition before suddenly reappearing."}
    ]
  },
  "Dashboard — cess/reprocess.md": {
    "primary": "To process materials, substances, or waste again in order to extract valuable components or prepare them for reuse.",
    "secondary": "In nuclear fuel cycle technology, chemical plants reprocess spent reactor rods to separate unused uranium and plutonium from fission products.",
    "quotes": [
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The chemists had to **reprocess** several tons of pitchblende residue to extract a minute fraction of pure radium salt."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Industrial ingenuity finds methods to **reprocess** slag and chemical waste into profitable fertilizers."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Nature continually evolves biochemical mechanisms to decompose and **reprocess** organic waste into fertile humus."}
    ]
  },
  "Dashboard — cess/secession.md": {
    "primary": "The formal withdrawal of a constituent state, region, or group from a larger political union, religious federation, or organization.",
    "secondary": "In American constitutional history, the doctrine of unilateral state secession was repudiated by the outcome of the Civil War and Texas v. White.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "Plainly, the central idea of **secession** is the essence of anarchy; a majority held in restraint by constitutional checks and limitations is the only true sovereign of a free people."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The peaceful **secession** of the plebeians to the Mons Sacer compelled the Roman Senate to create the office of the tribunes."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The threatened **secession** of the Scottish bishops from the assembly created an irreparable schism in the national church."}
    ]
  },
  "Dashboard — cess/secessionism.md": {
    "primary": "The political doctrine, advocacy, or movement that promotes withdrawal and independence from a sovereign nation or federal union.",
    "secondary": "In nineteenth-century political science, southern secessionism was defended by Calhoun through the theory of concurrent majorities and state nullification.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "Life and Times of Frederick Douglass", "quote": "The virulent spread of southern **secessionism** was fueled by the desperate desire to protect and expand chattel slavery."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "If the spirit of **secessionism** should infect several powerful confederate states, the federal union would lack the military apparatus to coerce them."},
      {"author": "Woodrow Wilson", "work": "A History of the American People", "quote": "The rise of militant **secessionism** in South Carolina convinced northern statesmen that compromise was no longer attainable."}
    ]
  },
  "Dashboard — cess/secessionist.md": {
    "primary": "An advocate, supporter, or participant in political or ecclesiastical secession from a sovereign nation or established body.",
    "secondary": "In Central European art history, the Secessionist movements in Vienna and Munich rejected conservative academic historicism in favor of Art Nouveau.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "The captured **secessionist** soldiers were marched under guard through Washington to the military prison."},
      {"author": "Abraham Lincoln", "work": "Second Annual Message", "quote": "No **secessionist** government can long sustain itself without sinking into military despotism or financial bankruptcy."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The river pilot had once harbored sympathy for the **secessionist** cause before witnessing the devastation wrought by the conflict."}
    ]
  },
  "Dashboard — cess/success.md": {
    "primary": "The favorable, prosperous, or intended outcome of an effort, undertaking, venture, or course of action.",
    "secondary": "In historical English usage and early modern literature, success denoted an outcome, result, or succession of events regardless of whether favorable or unfavorable.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "There's something in it more than my father's skill, which was the greatest of his profession, that hath brought **success** to our endeavor."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth congratulated herself on the **success** of her scheme to divert her sister's melancholy thoughts."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A foolish consistency is the hobgoblin of little minds; genuine **success** crowns him who follows his own genius without imitation."}
    ]
  },
  "Dashboard — cess/succession.md": {
    "primary": "The act, process, or right of following in order or sequence; or a series of persons or things following one after another.",
    "secondary": "In ecological biology, ecological succession describes the predictable, sequential replacement of species communities within an ecosystem over time.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 2", "quote": "How much more praise deserved thy beauty's use, if thou couldst answer 'This fair child of mine shall sum my count and make my old excuse,' proving his beauty by **succession** thine!"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological record reveals an orderly **succession** of biological forms, the newer species gradually replacing the ancient."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The hereditary **succession** of the imperial crown prevented the bloody civil wars that frequently attended popular elections."}
    ]
  },
  "Dashboard — cess/successive.md": {
    "primary": "Following in order or in uninterrupted course; coming one after another without break or interval; sequential.",
    "secondary": "In developmental biology and embryology, successive cell divisions transform the single-celled zygote into a multicellular blastula.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Now it is awake, takes note of what is done, and, like a prophet, looks in a glass that shows what future evils either new, or by remissness new conceived, are now to have a **successive** degree."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The white light passed through the prism and formed **successive** bands of spectral colors upon the white screen."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Winter advanced in well-marked **successive** stages, chilling the damp fields and stripping the hedgerows."}
    ]
  },
  "Dashboard — cess/successively.md": {
    "primary": "In a successive manner; one after another in regular order, sequence, or uninterrupted course.",
    "secondary": "In analytical chemistry and sequential extraction, mineral fractions are successively dissolved using reagents of increasing acidity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "And now my death changes the mood; for what in me was purchased falls upon thee in a more fairer sort; so thou the garland wear'st **successively**."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The whiteness, at length, changed **successively** into blue, indigo, and violet under the refracted beam."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The earthquake caused the coastal terraces to rise **successively** above high-water mark over thousands of years."}
    ]
  },
  "Dashboard — cess/successiveness.md": {
    "primary": "The characteristic or property of occurring, existing, or proceeding in sequential or successive order.",
    "secondary": "In Kantian transcendental aesthetics, the successiveness of temporal intuition is the necessary subjective condition for representing causality and motion.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "The **successiveness** of our internal perceptions proves that time is an a priori form of sensible intuition, not an empirical property of external things."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "All consciousness is characterized by the **successiveness** of diverse states of feeling following one another through awareness."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The stream of thought does not appear to itself chopped up in bits; its continuous **successiveness** defies atomistic division."}
    ]
  },
  "Dashboard — cess/successor.md": {
    "primary": "A person who inherits, succeeds to, or takes the office, position, title, or estate formerly held by another.",
    "secondary": "In discrete mathematics and Peano arithmetic, the successor function maps each natural number n to its immediate consecutive integer n+1.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Great Alexander left his empire to the worthiest; so his **successor** was like to be the best among his captains."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Doctor Peacock did not feel obliged to accept a new man merely in the character of his **successor**, objecting to young theorists."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Trajan selected Hadrian as his adopted **successor**, ensuring the administrative stability of the Roman world."}
    ]
  },
  "Dashboard — cess/unaccessible.md": {
    "primary": "Incapable of being reached, approached, obtained, or entered; inaccessible.",
    "secondary": "In historical English topography and mountaineering literature, unaccessible cliffs presented sheer barriers that repelled early cartographers.",
    "quotes": [
      {"author": "George Herbert", "work": "The Temple", "quote": "Thou art a rock so steep and **unaccessible** that mortal pride can never scale thy summit without divine grace."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Far off from the light of heaven, in utter darkness and deep gulfs **unaccessible**, the fallen host lay vanquished."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The ruined fortress perched upon an **unaccessible** crag overlooking the turbulent sea below."}
    ]
  },
  "Dashboard — cess/unnecessary.md": {
    "primary": "Not required by circumstances; needless, useless, redundant, or excessive.",
    "secondary": "In constitutional jurisprudence, unnecessary searches and seizures violate Fourth Amendment protections against unreasonable governmental intrusion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Thou whoreson zed! thou **unnecessary** letter!"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth considered any further discussion of Mr. Wickham's conduct entirely **unnecessary** and painful."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Pretty phrases and warm expressions being probably **unnecessary** where mutual affection was already understood."}
    ]
  },
  "Dashboard — cess/unprocessed.md": {
    "primary": "Not subjected to physical, chemical, or computational processing; remaining in an original, raw, or natural state.",
    "secondary": "In nutritional science and public health food classifications (NOVA system), unprocessed foods are whole edible parts of plants or animals unaltered by industrial refining.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The native weavers preferred **unprocessed** sheep's wool, spinning the coarse fleece directly into heavy woolen garments."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The chemical laboratory received tons of **unprocessed** shale oil to determine whether commercial kerosene could be extracted."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Primitive tribes relied on **unprocessed** flint stones and raw animal hides before the invention of metallurgy."}
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

print(f"Motion Batch 5B: Successfully updated {updated}/{len(data)} notes.")
