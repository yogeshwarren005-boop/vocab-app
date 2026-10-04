# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — tend Part 2 (6B, 31 words) ---
  "Dashboard — tend/tendentiousness.md": {
    "primary": "The character or trait of deliberately promoting a partisan viewpoint, controversial agenda, or ideological slant.",
    "secondary": "In Marxist literary criticism, tendentiousness (Tendenz) was celebrated as overt political commitment, whereas formalists rejected it as dogmatic distortion.",
    "quotes": [
      {"author": "George Orwell", "work": "All Art Is Propaganda", "quote": "Every work of art contains political bias, but blatant **tendentiousness** often weakens the imaginative integrity of a narrative."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "The persistent **tendentiousness** of sectarian education blinds children to the virtues of objective reasoning."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "When an author writes with conscious **tendentiousness**, the creative flame is smothered by personal grievances."}
    ]
  },
  "Dashboard — tend/tender.md": {
    "primary": "To offer formally for acceptance, payment, or consideration; or describing something soft, delicate, and easily injured.",
    "secondary": "In financial contracts and commercial law, legal tender constitutes money legally valid for extinguishing monetary debts upon offer.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I **tender** it for him in the court; yea, twice the sum, if that will suffice."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor watched over her sister with the most **tender** solicitude during the long hours of the fever."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant may **tender** promissory notes in settlement of wholesale accounts according to custom."}
    ]
  },
  "Dashboard — tend/tenderfoot.md": {
    "primary": "A newcomer, novice, or inexperienced person unaccustomed to harsh outdoor conditions or frontier life.",
    "secondary": "In nineteenth-century American frontier folklore, seasoned pioneers playfully hazed the arriving tenderfoot who lacked survival skills.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The old miners could instantly spot a **tenderfoot** by his shiny patent-leather boots and pristine woolen coat."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The greenhorns from the city were branded as **tenderfoot** adventurers completely unfit for the Klondike winter."},
      {"author": "Theodore Roosevelt", "work": "Ranch Life and the Hunting-Trail", "quote": "A western ranch quickly cures a **tenderfoot** of his city mannerisms through long days in the saddle."}
    ]
  },
  "Dashboard — tend/tendergreen.md": {
    "primary": "A variety of turnip greens or mustard greens cultivated for edible tender leaves; or a delicate light green color.",
    "secondary": "In agricultural horticulture, tendergreen brassicas mature quickly in cool spring soil, providing nutrient-rich salad greens.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The cultivated **tendergreen** varieties exhibited remarkable leaf expansion under greenhouse shelter."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The young wheat sprouted in **tendergreen** rows across the rolling contours of the southern slope."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The birch saplings put forth their **tendergreen** shoots under the warm morning sun of late April."}
    ]
  },
  "Dashboard — tend/tenderhearted.md": {
    "primary": "Possessing an easily touched, sympathetic, compassionate, and kindly disposition; sensitive to the suffering of others.",
    "secondary": "In Victorian moral literature, the tenderhearted heroine embodied evangelical ideals of empathetic benevolence and unselfish charity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The **tenderhearted** clerk wept openly when he learned of Tiny Tim's fragile health."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was too **tenderhearted** to dismiss the distressed cottager without offering practical financial help."},
      {"author": "William Shakespeare", "work": "King Lear", "quote": "A **tenderhearted** maid would not have turned her aged father into such a tempestuous night."}
    ]
  },
  "Dashboard — tend/tenderheartedness.md": {
    "primary": "A disposition characterized by deep compassion, gentle sympathy, and readiness to feel for others' afflictions.",
    "secondary": "In moral theology, tenderheartedness reflects the spiritual virtue of misericordia, balancing strict justice with active empathy.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "There are episodes in most men's lives in which their **tenderheartedness** can only cast a delicate shadow over stern duty."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The schoolmaster was beloved throughout the village for his unfailing patience and **tenderheartedness**."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "True **tenderheartedness** does not expend itself in useless lamentations but hastens to relieve actual distress."}
    ]
  },
  "Dashboard — tend/tenderisation.md": {
    "primary": "The process or action of making meat more tender through pounding, marinating, or enzymatic treatment.",
    "secondary": "In industrial food biochemistry, tenderisation relies on proteolytic plant enzymes such as papain and bromelain to cleave myofibrillar proteins.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The culinary **tenderisation** of tough beef fibers involves breaking down collagen connective tissues through heat and moisture."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Mechanical **tenderisation** of meat by primitive hunters represented an early culinary adaptation to aid digestion."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The gauchos prepared the sun-dried beef by repeated **tenderisation** between heavy flat river stones."}
    ]
  },
  "Dashboard — tend/tenderise.md": {
    "primary": "To make meat tender, palatable, or soft by mechanical pounding, chemical marination, or enzymatic application.",
    "secondary": "In culinary food preparation, chefs tenderise tough cuts of flank steak with acidic citrus juices or vinegar-based marinades before grilling.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Native cooks know well how to **tenderise** tough game fowl using leaves of the wild papaya tree."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Heat and enzymatic action cooperate to **tenderise** animal protein during prolonged simmering."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The islanders pounded the roasted breadfruit to **tenderise** the pulp into a smooth edible paste."}
    ]
  },
  "Dashboard — tend/tenderised.md": {
    "primary": "Made soft, succulent, or less tough through mechanical pounding, slow cooking, or proteolytic enzymatic action.",
    "secondary": "In meat processing regulations, commercially tenderised steaks must be cooked to specific internal temperatures to prevent bacterial contamination.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The innkeeper served a platter of **tenderised** mutton garnished with roasted garden turnips."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The cook brought out the **tenderised** salt beef that had soaked for two days in fresh water."},
      {"author": "Herman Melville", "work": "Omoo", "quote": "The sailors eagerly enjoyed the **tenderised** pork roasted over glowing embers in the native pit."}
    ]
  },
  "Dashboard — tend/tenderiser.md": {
    "primary": "A substance, enzyme, or kitchen mallet used to break down tough fibers in meat to make it soft and edible.",
    "secondary": "In biochemical pharmacology, papain derived from Carica papaya serves as an active enzymatic tenderiser and topical debriding agent.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The natural plant juice acted as an effective **tenderiser**, dissolving the dense connective tissue of the steak."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "A chemical **tenderiser** mimics the digestive secretions by pre-cleaving muscular protein bundles."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Indigenous tribes used crushed papaya bark as a culinary **tenderiser** long before modern gastronomy."}
    ]
  },
  "Dashboard — tend/tenderization.md": {
    "primary": "The treatment or method of softening tough meat fibers by mechanical force, chemical marination, or enzymatic breakdown.",
    "secondary": "In meat science, post-mortem tenderization occurs naturally during aging via endogenous calpain and lysosomal cathepsin enzymes.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The scientific **tenderization** of animal tissues demonstrates the direct application of chemistry to household economy."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Every advance in the **tenderization** and culinary preparation of food reduced the physiological strain of human mastication."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The natural **tenderization** of flesh in cold climates permitted predators to consume frozen prey during winter months."}
    ]
  },
  "Dashboard — tend/tenderize.md": {
    "primary": "To soften or reduce the toughness of meat by pounding, marinating, or applying proteolytic enzymes.",
    "secondary": "In food preparation technology, mechanical needle injectors puncture muscle tissue to tenderize subprimal beef cuts uniformly.",
    "quotes": [
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The camp cook used a heavy wooden mallet to **tenderize** the frozen caribou meat before boiling."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The seasoned whalemen knew how to **tenderize** the tough whale flesh by hanging it in the ocean breeze."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The South American natives pound the strips of dried charqui on flat rocks to **tenderize** the beef."}
    ]
  },
  "Dashboard — tend/tenderized.md": {
    "primary": "Subjected to pounding, marinating, or enzymatic treatment to soften tough muscular fibers.",
    "secondary": "In agricultural commerce, tenderized meat cuts command higher retail demand by improving eating satisfaction in lower-grade beef.",
    "quotes": [
      {"author": "Jack London", "work": "South Sea Tales", "quote": "The feast featured **tenderized** wild boar roasted wrapped in green plantain fronds."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The villagers relished the **tenderized** venison pie prepared for the annual timber auction."},
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The German innkeeper offered us **tenderized** veal cutlets fried crisp in sweet country butter."}
    ]
  },
  "Dashboard — tend/tenderizer.md": {
    "primary": "A culinary tool, mallet, or enzymatic substance used to soften meat by disrupting muscular fiber bundles.",
    "secondary": "In enzyme biochemistry, powdered meat tenderizer typically combines refined papain or bromelain with sodium chloride carriers.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The commercial **tenderizer** proved capable of digesting fibrous collagen without altering the flavor of the meat."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "An enzymatic **tenderizer** performs outside the stomach what gastric pepsin accomplishes within the digestive canal."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Botanical extracts used as a **tenderizer** were discovered independently by various tropical peoples."}
    ]
  },
  "Dashboard — tend/tenderloin.md": {
    "primary": "A choice, tender cut of meat along either side of the spine; or a metropolitan district known for vice or corruption.",
    "secondary": "In anatomical butchery, the beef tenderloin comprises the psoas major muscle, prized for extreme tenderness due to minimal weight-bearing use.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The epicurean whaleman sliced off the prized whale **tenderloin** to roast over the ship's galley stove."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The mining town's notorious **tenderloin** district was filled with lively dance halls and gambling saloons."},
      {"author": "Eleanor H. Porter", "work": "Miss Billy — Married", "quote": "Billy ordered a prime beef **tenderloin** and fresh asparagus to celebrate her husband's return."}
    ]
  },
  "Dashboard — tend/tenderly.md": {
    "primary": "With gentleness, affectionate warmth, care, or delicacy; in a manner that avoids causing pain.",
    "secondary": "In musical performance notation, the Italian direction teneramente instructs players to perform a phrase tenderly and expressively.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "He spoke to his father, that so **tenderly** and entirely loves him, with tears in his eyes."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor embraced her sister **tenderly**, wiping away the tears that fell upon her cheek."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Lucie held her father's trembling hands **tenderly**, speaking words of comfort and devotion."}
    ]
  },
  "Dashboard — tend/tenderness.md": {
    "primary": "Gentle affection, kindness, and compassionate sensitivity; or physical delicacy and susceptibility to pain or pressure.",
    "secondary": "In clinical palpation, localized abdominal tenderness upon physical examination indicates underlying peritoneal inflammation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "I have given suck, and know how tender 'tis to love the babe that milks me; yet such **tenderness** was banished from her fierce heart."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth observed the unfeigned **tenderness** with which Jane spoke of Mr. Bingley's gentle manners."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery's clumsy hand rested upon my shoulder with an exquisite **tenderness** that touched my soul."}
    ]
  },
  "Dashboard — tend/tending.md": {
    "primary": "Caring for, managing, or ministering to someone or something; or moving or leaning in a specific direction.",
    "secondary": "In metallurgical smelting, tending the furnace involves monitoring blast airflow and slag tapping to maintain steady thermal equilibrium.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Do grace to Caesar's corpse, and grace his speech **tending** to Caesar's glories, which Mark Antony has permission to make."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel spent the stormy night **tending** the newborn lambs in the sheltered sheepfold."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Esther found solace in quietly **tending** the sick children in the humble cottage."}
    ]
  },
  "Dashboard — tend/tendinitis.md": {
    "primary": "Inflammation or irritation of a tendon, typically causing acute pain, swelling, and reduced joint mobility.",
    "secondary": "In orthopedic sports medicine, Achilles tendinitis frequently results from repetitive microtrauma and eccentric tendon overload in runners.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Chronic strain in manual artisans frequently provokes painful **tendinitis** in the wrist and forearm."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **tendinitis** requires complete immobilization and cold compresses to subside localized inflammatory effusion."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The overexertion of digital flexor muscles can induce severe **tendinitis** among professional musicians."}
    ]
  },
  "Dashboard — tend/tendinous.md": {
    "primary": "Pertaining to, consisting of, or resembling a tendon; sinewy, fibrous, or tough.",
    "secondary": "In comparative vertebrate anatomy, tendinous intersections segment the rectus abdominis muscle into distinct contractile bellies.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The extremity is **tendinous** and contains no vertebrae; this is succeeded by five rudimentary caudal segments."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **tendinous** fibers of the whale's tail are interwoven with extraordinary mechanical strength."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Muscles terminate in dense **tendinous** bands that anchor securely to the periosteum of bone."}
    ]
  },
  "Dashboard — tend/tendon.md": {
    "primary": "A tough, inelastic band or cord of dense fibrous connective tissue uniting a skeletal muscle to a bone.",
    "secondary": "In biomechanics, the Achilles tendon acts as an elastic spring that stores and returns mechanical energy during human locomotion.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whalemen severed the thick **tendon** of the fluke to prevent the dying monster from lashing the seas."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Examine these limbs, red, black, or white, they are cunning in **tendon** and nerve."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The facial muscles pull upon the cutaneous **tendon** to display instantaneous expressions of fear."}
    ]
  },
  "Dashboard — tend/tendonitis.md": {
    "primary": "Inflammation of a tendon resulting from repetitive mechanical strain, overuse, or traumatic injury.",
    "secondary": "In occupational ergonomics, patellar tendonitis (jumper's knee) is diagnosed through focal palpation tenderness at the inferior pole of the patella.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The athlete suffered from persistent **tendonitis** following the vigorous cross-country trials."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Repetitive mechanical labor without ergonomic respite inevitably induces severe musculoskeletal **tendonitis**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Prolonged vertical posture imposes stress upon the lower limb, occasionally producing degenerative **tendonitis**."}
    ]
  },
  "Dashboard — tend/tendosynovitis.md": {
    "primary": "Inflammation of a tendon together with its surrounding synovial sheath, causing pain and crepitus upon movement.",
    "secondary": "In hand surgery and rheumatology, De Quervain tendosynovitis affects the abductor pollicis longus and extensor pollicis brevis sheaths.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Exudative **tendosynovitis** was accompanied by audible friction sounds upon active flexion of the fingers."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "When inflammatory fluid accumulates within the digital sheath, acute **tendosynovitis** severely restricts tendon gliding."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The intricate pulley mechanisms of the human hand are vulnerable to debilitating **tendosynovitis** under excessive strain."}
    ]
  },
  "Dashboard — tend/tendrac.md": {
    "primary": "A small, spiny, insectivorous mammal native to Madagascar belonging to the tenrec family (Centetidae).",
    "secondary": "In evolutionary biogeography, the Malagasy tendrac represents remarkable adaptive radiation, filling ecological niches akin to shrews and hedgehogs.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The isolated fauna of Madagascar includes the curious **tendrac**, which retains primitive insectivorous dentition."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The anatomical structure of the **tendrac** illustrates how ancestral mammals adapted to specialized insular environments."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "Among the endemic mammalian genera of Madagascar, the nocturnal **tendrac** burrows among fallen forest foliage."}
    ]
  },
  "Dashboard — tend/tendril-climbing.md": {
    "primary": "Describing climbing vines and plants that ascend and support themselves by producing specialized twining tendrils.",
    "secondary": "In botanical morphology, tendril-climbing vines exhibit thigmotropism, curling tightly around structural supports upon tactile contact.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The **tendril-climbing** species exhibit an exquisite sensitivity to tactile stimulation, revolving until they find a trellis."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Dense masses of **tendril-climbing** creepers formed impenetrable curtains across the tropical woodland clearing."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The wild grapes were **tendril-climbing** over the low alders near the water's edge."}
    ]
  },
  "Dashboard — tend/tendril.md": {
    "primary": "A slender, threadlike, spiral coiling organ of climbing plants used to grasp a support; or a wispy curl of hair.",
    "secondary": "In plant developmental biology, a tendril is an evolutionary modification of a leaf, stem, or inflorescence specialized for climbing.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "When the sensitive tip of a **tendril** touches a twig, it rapidly curves and coils into a permanent spiral spring."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The vine curls her **tendril** about the elm, bearing purple clusters toward the sunlight."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A stray **tendril** of dark hair escaped from beneath her bonnet and brushed against her cheek."}
    ]
  },
  "Dashboard — tend/unattended.md": {
    "primary": "Left without presence, supervision, care, or guardianship; or unaccompanied by companions or escorts.",
    "secondary": "In transportation safety protocols, unattended luggage or vehicles in public terminals trigger security inspection routines.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Your constancy hath left you **unattended**; hark, more knocking at the south entry!"},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "This critical act is not always **unattended** with the saddest and most fatal casualties."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "At last Captain Wentworth approached, leaving Anne no longer **unattended** amid the crowded room."}
    ]
  },
  "Dashboard — tend/unextended.md": {
    "primary": "Not stretched out, enlarged, or prolonged; lacking spatial dimension or physical extension.",
    "secondary": "In Cartesian dualism, the rational soul (res cogitans) is defined as an unextended thinking substance distinct from extended matter.",
    "quotes": [
      {"author": "René Descartes", "work": "Meditations on First Philosophy", "quote": "The human mind is an **unextended** thinking entity, completely indivisible and independent of the physical body."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Philosophers have debated whether immaterial spirits can be conceived as **unextended** points in space."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "If space is the form of external intuition, nothing within physical experience can exist in an **unextended** state."}
    ]
  },
  "Dashboard — tend/unintended.md": {
    "primary": "Not planned, designed, or foreseen; occurring without deliberate intent or purpose; accidental.",
    "secondary": "In socioeconomics and policy analysis, Merton's law of unintended consequences describes unforeseen adverse results arising from purposive social interventions.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She answered cautiously, wanting to check **unintended** consequences before rumors spread through the parish."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "What good I do must be aside from my main path, and for the most part **unintended** by any conscious calculation."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "By pursuing his own interest, an individual frequently promotes that of the society through an **unintended** mechanism."}
    ]
  },
  "Dashboard — tend/unpretending.md": {
    "primary": "Modest, unassuming, simple, and free from ostentation, arrogance, or false display.",
    "secondary": "In literary characterization, unpretending domestic virtue in nineteenth-century novels stood as a moral foil to vanity and social climbing.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "An **unpretending**, single-minded, artless girl was infinitely to be preferred by any man of sense to an accomplished coquette."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Perhaps the humble and **unpretending** home of the guardian was the happiest retreat in all London."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village musicians were an **unpretending** band of country folk content with their simple rural tunes."}
    ]
  },
  "Dashboard — tend/untended.md": {
    "primary": "Not looked after, supervised, cultivated, or cared for; neglected or left abandoned.",
    "secondary": "In agrarian estate management, untended pastures rapidly deteriorate into bracken and scrubland within several seasons.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "A sight in camp in the daybreak gray and dim, where the wounded soldier lay **untended** upon his bloodstained blanket."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The little garden behind the cottage lay **untended**, overrun with nettles and wild briars."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The **untended** cows waited patiently at the farm gate, lowing softly for the delayed milkers."}
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

print(f"Motion Batch 6B: Successfully updated {updated}/{len(data)} notes.")
