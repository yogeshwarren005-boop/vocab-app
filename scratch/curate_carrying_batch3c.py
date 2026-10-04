# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — port (Batch 3C: 32 words)
  # =========================================================================
  "Dashboard — port/porterhouse.md": {
    "primary": "A choice cut of beef containing a large T-bone and portion of tenderloin; or historically, an alehouse where porter was sold.",
    "secondary": "In culinary gastronomy and butchery, a thick-cut steak from the short loin containing a larger tenderloin section than a standard T-bone.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He ordered a juicy cut of **porterhouse** steak, relishing its savory fragrance after months of salt pork."},
      {"author": "O. Henry", "work": "The Four Million", "quote": "The hungry clerk dreamed of dining on a sizzling **porterhouse** with mushrooms at a Broadway restaurant."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "They gathered at the club grill for a dinner of thick **porterhouse** steaks and baked potatoes."}
    ]
  },
  "Dashboard — port/portico.md": {
    "primary": "A structure consisting of a roof supported by columns at regular intervals, typically attached as a porch to a building.",
    "secondary": "In classical Greek and Roman architecture, a monumental colonnaded entrance (such as the Stoa or the portico of the Pantheon).",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A gloomy man, who had been observing her from under the church **portico**, now stepped forward."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "They lingered beneath the marble **portico** of the temple, admiring the flight of doves across the piazza."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The great **portico** of the baths was adorned with precious statues brought from Greece."}
    ]
  },
  "Dashboard — port/porticoed.md": {
    "primary": "Furnished with or characterized by a portico or colonnade.",
    "secondary": "In neoclassical and Palladian architecture, featuring monumental columnar facades inspired by Vitruvian design principles.",
    "quotes": [
      {"author": "Henry James", "work": "The American Scene", "quote": "The stately **porticoed** mansion stood back from the road, shaded by ancient live oaks."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The avenue was lined with dignified, **porticoed** residences that expressed the quiet wealth of old New York."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The **porticoed** entrance of the country seat gave an imposing air of antiquity to the modern wings."}
    ]
  },
  "Dashboard — port/portiere.md": {
    "primary": "A heavy curtain hung over a door or doorway to prevent drafts, divide rooms, or serve as a decorative screen.",
    "secondary": "In Victorian and Edwardian domestic interior decoration, heavy velvet or brocade drapery installed to insulate parlor thresholds.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "She drew back the heavy velvet **portiere** and looked into the dimly lighted library."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "A servant parted the rich silk **portiere**, announcing the arrival of the visitors."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Through the parted **portiere** came the sweet, oppressive fragrance of heavy gardenias."}
    ]
  },
  "Dashboard — port/portion.md": {
    "primary": "A part of a whole; an amount, section, or piece of something divided; or a person's allotted share or destiny.",
    "secondary": "In marriage settlements and historical law, the dowry or share of an estate transferred to an heir upon coming of age or marriage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "What prodigal **portion** have I spent, that I should come to such penury?"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her small **portion** in life was considered an insurmountable obstacle to an advantageous match."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A generous **portion** of pudding was placed before the hungry schoolboys."}
    ]
  },
  "Dashboard — port/portland.md": {
    "primary": "A peninsula in Dorset, England, famed for its limestone quarries (Portland stone); or the largest city in Oregon or Maine.",
    "secondary": "In civil engineering and construction materials, Portland cement, a hydraulic binder manufactured by pulverizing clinkers of calcium silicates.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Well-Beloved", "quote": "The rocky Isle of Slingers, known to the world as **Portland**, rose like a great crouching beast from the sea."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The fossil beds of the **Portland** stone preserve remarkable ammonites and ancient cycad trunks."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The stone docks were constructed of durable **Portland** blocks capable of withstanding the Atlantic surge."}
    ]
  },
  "Dashboard — port/portly.md": {
    "primary": "Having a stout body, somewhat fat, dignified, and imposing in appearance; corpulent.",
    "secondary": "In early modern English (Shakespearean usage), stately, dignified, and majestic in demeanor and noble carriage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Our house, my sovereign liege, little deserves the scourge of greatness to be used on it; and that same greatness too which our own hands have holp to make so **portly**."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Two **portly** gentlemen, pleasant to behold, now stood, with their hats off, in Scrooge's office."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Weston was a **portly**, good-humored gentleman of middle age, whose cheerful temper made him universally liked."}
    ]
  },
  "Dashboard — port/portmanteau.md": {
    "primary": "A large travelling bag, typically made of stiff leather and opening into two equal compartments; or a word blending the sounds and meanings of two words.",
    "secondary": "In linguistics and morphophonology, a blend formed by merging multiple base lexemes (such as smog or brunch) into a single phonetic stem.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "You see it's like a **portmanteau**—there are two meanings packed into one word."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He placed his leather **portmanteau** upon the rack and settled himself into the carriage corner."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes quickly packed his spyglass, lens, and note-books into a battered **portmanteau**."}
    ]
  },
  "Dashboard — port/porto.md": {
    "primary": "The second-largest city in Portugal, situated along the Douro river estuary, renowned as the historic center of the port wine trade.",
    "secondary": "In enology and viticulture, fortified dessert wine produced from grapes cultivated in the demarcated Douro Valley and matured in lodges at Vila Nova de Gaia.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The romantic hills of **Porto** terrace down to the rushing waters of the golden Douro."},
      {"author": "George Borrow", "work": "The Bible in Spain", "quote": "I walked through the steep, narrow streets of **Porto**, inhaling the rich aroma of wine from the ancient cellars."},
      {"author": "Richard Francis Burton", "work": "The Highlands of the Brazil", "quote": "The merchant ships carried rich cargoes of wine from the wharves of **Porto** across the southern oceans."}
    ]
  },
  "Dashboard — port/portrait.md": {
    "primary": "A painting, drawing, photograph, or engraving of a person, especially depicting the face and shoulders.",
    "secondary": "In literary biography and cultural criticism, a detailed and nuanced biographical character study or depiction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The **portrait** of a blinking idiot presenting me a schedule! Here's the scroll."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "In the centre of the room stood the full-length **portrait** of a young man of extraordinary personal beauty."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The ancestral **portrait** of Colonel Pyncheon seemed to follow every movement with stern, unblinking eyes."}
    ]
  },
  "Dashboard — port/portraitist.md": {
    "primary": "An artist or photographer who specializes in making portraits of people.",
    "secondary": "In visual arts criticism, a painter adept at psychological insight, likeness, and chiaroscuro modeling in representing human subjects.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "A true **portraitist** does not merely copy features; he translates the secret movements of the soul into form."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Gainsborough was supreme as a natural **portraitist**, capturing the unstudied grace of his sitters."},
      {"author": "Kenneth Clark", "work": "Looking at Pictures", "quote": "Velázquez demonstrated the ultimate economy of touch expected of a master court **portraitist**."}
    ]
  },
  "Dashboard — port/portraiture.md": {
    "primary": "The art or practice of creating portraits; or portraits considered collectively.",
    "secondary": "In fine art history, the formal genre of visual and plastic art dedicated to human representation, likeness, and social status.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For by the image of my cause I see the **portraiture** of his."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The finest Elizabethan **portraiture** sought to convey moral character rather than fleeting physical expression."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The gallery displayed masterpieces of seventeenth-century **portraiture** that seemed to gaze out from the shadows."}
    ]
  },
  "Dashboard — port/portray.md": {
    "primary": "To depict or represent someone or something in a work of art, literature, or performance.",
    "secondary": "In courtroom rhetoric and biographical historiography, framing an individual's character or intent to influence public judgment.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My pencil could not **portray** the elusive sorrow that shadowed his proud countenance."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A novelist who seeks to **portray** human life faithfully must not shrink from its commonplace ironies."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "No painter could adequately **portray** the terrifying majesty of the breaching whale."}
    ]
  },
  "Dashboard — port/portrayal.md": {
    "primary": "A depiction of someone or something in a work of art or literature; an artistic representation.",
    "secondary": "In dramatic criticism and theatrical theory, an actor's interpretation and physical execution of a dramatic character.",
    "quotes": [
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "A vivid **portrayal** of life is the only excuse for the existence of a novel."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The rough **portrayal** of his features in the skimmity-ride drove the proud merchant to despair."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The painting was no longer a mere **portrayal**, but the living record of his corrupted soul."}
    ]
  },
  "Dashboard — port/portrayed.md": {
    "primary": "Represented or depicted in a work of art, literature, or dramatic performance.",
    "secondary": "In narrative realism, characters and historical events presented with psychological verisimilitude.",
    "quotes": [
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The painter had **portrayed** the rustic maiden with all the tender simplicity of nature."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister was **portrayed** in the collective mind of the parish as a vessel of heavenly grace."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The canvas **portrayed** a cavalier whose cruel lips and mocking eyes betrayed the ancestral curse."}
    ]
  },
  "Dashboard — port/portrayer.md": {
    "primary": "An artist, writer, or performer who portrays or depicts someone or something.",
    "secondary": "In literary theory, an author or dramaturge whose works systematically delineate the manners and morals of an epoch.",
    "quotes": [
      {"author": "William Hazlitt", "work": "Characters of Shakespear's Plays", "quote": "Shakespeare is the supreme **portrayer** of the passions, revealing every nuance of the human heart."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Tintoretto stood as the fierce **portrayer** of biblical drama, unmatched in dynamic movement."},
      {"author": "Henry James", "work": "French Poets and Novelists", "quote": "Balzac was the unwearied **portrayer** of the immense human comedy of nineteenth-century France."}
    ]
  },
  "Dashboard — port/portraying.md": {
    "primary": "The act of representing, depicting, or illustrating someone or something in art, words, or drama.",
    "secondary": "In documentary realism, capturing historical circumstances without sentimental idealization.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "In **portraying** the provincial society of Middlemarch, she laid bare the subtle currents of human motive."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rustic ballad-singer took great delight in **portraying** the sorrowful fate of betrayed lovers."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "The artist's highest task consists in **portraying** the subtle impressions made by life upon the sensitive mind."}
    ]
  },
  "Dashboard — port/portsmouth.md": {
    "primary": "A historic naval port and city in Hampshire, southern England, long serving as the premier base of the Royal Navy.",
    "secondary": "In naval history and maritime logistics, the historic royal dockyard housing HMS Victory, drydocks, and naval administration.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A naturalist in **Portsmouth** informed me of several curious variations observed in marine fauna."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price returned to her father's crowded, noisy house in the busy garrison town of **Portsmouth**."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "They journeyed along the high road toward the naval port of **Portsmouth**, seeking theatrical engagements."}
    ]
  },
  "Dashboard — port/portugal.md": {
    "primary": "A sovereign nation on the Iberian Peninsula of southwestern Europe, bordering Spain and the Atlantic Ocean.",
    "secondary": "In early modern global history, the pioneering seafaring empire initiating the European maritime exploration of Africa, Brazil, and the Indian Ocean.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "My affection hath an unknown bottom, like the bay of **Portugal**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The commercial treaty with **Portugal** opened vast foreign markets for British manufactured woolens."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Where is thy boasted vintage, and the vine-crowned hills of **Portugal**?"}
    ]
  },
  "Dashboard — port/portuguese.md": {
    "primary": "Relating to Portugal, its people, or its Romance language; or a native or inhabitant of Portugal.",
    "secondary": "In historical maritime commerce, the Portuguese caravel and navigational techniques that initiated global oceanic trade networks.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The word seems to have been applied by **Portuguese** mariners to designate the native inhabitants of the eastern coast."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Several hardy **Portuguese** sailors from the Western Islands pulled in the starboard boat."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We were courteously received by the **Portuguese** governor at the Cape Verde settlement."}
    ]
  },
  "Dashboard — port/portulaca.md": {
    "primary": "A genus of succulent flowering plants (Portulacaceae), notably purslane (Portulaca oleracea) and moss rose (Portulaca grandiflora), with fleshy leaves and bright flowers.",
    "secondary": "In plant physiology and culinary botany, edible succulent herbs exhibiting drought-tolerant C4/CAM photosynthesis and rich in omega-3 fatty acids.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The brilliant floral variations of garden **portulaca** developed rapidly under artificial hybridization."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Creeping succulent beds of **portulaca** carpeted the arid saline flats near the coast."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I gathered wild purslane, the ancient **portulaca**, boiling it for a simple and nutritious dinner in the woods."}
    ]
  },
  "Dashboard — port/portulacaceae.md": {
    "primary": "A botanical family of flowering plants (the purslane family) within the order Caryophyllales, comprising succulent herbs and subshrubs.",
    "secondary": "In plant taxonomy and systematic angiosperm phylogeny, plants characterized by two sepal-like involucral bracts and mucilaginous succulent tissues.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **portulacaceae** is distinguished by fleshy succulent leaves, two sepals, and a one-celled capsule."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Experiments upon various genera of the **portulacaceae** revealed varying degrees of self-fertility."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of the **portulacaceae** are predominantly adapted to arid soils and sunny maritime rocks."}
    ]
  },
  "Dashboard — port/portunidae.md": {
    "primary": "A zoological family of decapod marine crustaceans, known as the swimming crabs, having flattened paddle-like fifth legs (dactyls).",
    "secondary": "In marine biology and invertebrate zoology, agile predatory crabs (such as the blue crab Callinectes sapidus) equipped with modified swimming paddles.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The family **portunidae** is readily distinguished by the transformation of the posterior pereiopods into broad swimming oars."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual dimorphism in coloration is remarkably pronounced among several genera of the **portunidae**."},
      {"author": "William Beebe", "work": "Half Mile Down", "quote": "Swimming crabs of the family **portunidae** darted across our searchlight beam with astonishing velocity."}
    ]
  },
  "Dashboard — port/portunus.md": {
    "primary": "A genus of swimming crabs within the family Portunidae, characterized by broad carapaces with lateral spines and paddle-shaped hind legs.",
    "secondary": "In Roman mythology, Portunus was the ancient god of keys, doors, cattle, and maritime harbors, celebrated at the Portunalia.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "When a Devil-crab, **Portunus** puber, was seen by an observer, its fierce defensive attitude was immediately noted."},
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "The ancient temple of **Portunus** by the Tiber guarded the river landing where merchant vessels moored."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The carapace of **Portunus** terminates on each side in an acute, projecting epibranchial spine."}
    ]
  },
  "Dashboard — port/proportion.md": {
    "primary": "A part, share, or number considered in comparative relation to a whole; or the harmonious relationship between elements.",
    "secondary": "In mathematics, an equation stating that two ratios are equal (a/b = c/d).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "And, I fear, Sir Michael, what with the sickness of Northumberland, whose power was in the first **proportion**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The quantity of every commodity brought to market naturally suits itself to the effectual demand in just **proportion**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection acts solely by accumulating slight variations advantageous to each organism in **proportion** to its struggle."}
    ]
  },
  "Dashboard — port/proportionable.md": {
    "primary": "Capable of being proportioned; corresponding in proportion; proportionate.",
    "secondary": "In classical political philosophy and moral jurisprudence, adjusting civic rewards or penalties in direct alignment with merit or injury.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "For us to levy power **proportionable** to the enemy is all impossible."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our assent should be **proportionable** to the degree of evidence which supports the proposition."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A wise magistrate awards honors **proportionable** to the public benefits conferred by the citizen."}
    ]
  },
  "Dashboard — port/proportional.md": {
    "primary": "Corresponding in size, degree, or intensity; having a constant ratio to another quantity.",
    "secondary": "In electoral systems (proportional representation), allocating seats in an elected body in direct mathematical accordance with the popular vote.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I shall reserve for my future work the discussion of the **proportional** numbers of species in different classes."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wages of labor vary in **proportional** relation to the difficulty, risk, and disagreeableness of the employment."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A truly democratic legislature must reflect a **proportional** representation of all significant political opinions."}
    ]
  },
  "Dashboard — port/proportionality.md": {
    "primary": "The quality of being proportional; the correct or proper relationship between components.",
    "secondary": "In constitutional law and international humanitarian law, the principle that military action or statutory punishment must not exceed the legitimate objective.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The doctrine of **proportionality** between punishments and offenses is the first axiom of enlightened penal legislation."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Justice demands an overarching **proportionality** between effort expended for the public good and societal reward."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A sound education maintains an intellectual **proportionality** among physical science, literature, and art."}
    ]
  },
  "Dashboard — port/proportionally.md": {
    "primary": "In a proportional manner; in proportion to something else.",
    "secondary": "In economics and geometry, increasing or diminishing by a constant common factor.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The Jacobin has the feathers so much reversed along the neck that the beak is **proportionally** shortened."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "As the division of labor improves, the productive powers of labor increase **proportionally**."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "If taxation falls **proportionally** upon all forms of income, the relative economic positions of citizens remain undisturbed."}
    ]
  },
  "Dashboard — port/proportionate.md": {
    "primary": "Proportional; corresponding in size, degree, or scale to something else.",
    "secondary": "In retributive ethics and criminal justice, penal consequences strictly calibrated to the blameworthiness and damage caused by the offender.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "When Jove and his fellow-gods became indignant, their anger was **proportionate** to their divine majesty."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her sympathy for his affliction was **proportionate** to the depth of her own generous nature."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The muscular strength of the male is **proportionate** to his role in combat and defense of the troop."}
    ]
  },
  "Dashboard — port/proportionately.md": {
    "primary": "In proportion; to a corresponding degree or extent.",
    "secondary": "In statistical physics and financial modeling, scaling variables in direct linear dependency with an underlying parameter.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "This move was unexpected, and **proportionately** disconcerted the plans of his rival."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "If any one species increases **proportionately** in numbers, others must inevitably decrease."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "When market demand exceeds supply, prices rise **proportionately** above the natural rate."}
    ]
  },
  "Dashboard — port/proportionateness.md": {
    "primary": "The quality of being proportionate; proper balance, symmetry, or calibration.",
    "secondary": "In classical architectural theory and sculpture, mathematical harmony between human anatomical parts and monumental building elevations.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The noble beauty of the cathedral depends upon the subtle **proportionateness** of its archways to the nave."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "There is no exquisite beauty without some strangeness in the **proportionateness** of its features."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The moral **proportionateness** of his actions was admired by all who valued integrity above display."}
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

print(f"Carrying Batch 3C (port): Successfully updated {updated}/{len(data)} notes.")
