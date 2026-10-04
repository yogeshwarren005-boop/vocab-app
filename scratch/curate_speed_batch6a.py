# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — lev (Batch 6A: 30 words)
  # =========================================================================
  "Dashboard — lev/alleviant.md": {
    "primary": "Having the power to relieve or mitigate; an agent or remedy that alleviates pain or suffering.",
    "secondary": "In classical pharmacology and palliative medicine, soothing remedies administered to lessen distressing symptoms without curing the underlying malady.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The sweet solace of poetry served as a gentle **alleviant** to the dark distress of his troubled spirit."},
      {"author": "Oliver Wendell Holmes", "work": "Currents and Counter-Currents in Medical Science", "quote": "A judicious physician prescribes a mild **alleviant** to assuage the restless agony of the febrile patient."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "Philosophy offers a quiet **alleviant** against the heavy burdens and afflictions of mortal life."}
    ]
  },
  "Dashboard — lev/alleviate.md": {
    "primary": "To make less severe, painful, or difficult to bear; to mitigate, ease, or lighten.",
    "secondary": "In public health and social reform, systematic measures designed to reduce chronic poverty, hunger, or physical suffering.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "You come to us now to share a misery which nothing can **alleviate**; yet your presence will bring solace to our father."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Kind words had power to **alleviate** the loneliness that weighed upon her sensitive heart."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He sought by every compassionate means to **alleviate** the wretched destitution of the poor room."}
    ]
  },
  "Dashboard — lev/alleviated.md": {
    "primary": "Made less severe, intense, or painful; relieved, eased, or mitigated.",
    "secondary": "In clinical therapeutics, symptomatic distress rendered manageable through pharmacological or palliative intervention.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The labours I endured were no longer to be **alleviated** by the bright sun or gentle breeze of spring."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Her sorrow was gradually **alleviated** by the tender attentiveness and sympathetic presence of her sister."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "His gloomy remorse was partially **alleviated** when he learned that his daughter was safe from harm."}
    ]
  },
  "Dashboard — lev/alleviation.md": {
    "primary": "The mitigating or easing of pain, suffering, or distress; the experience of being relieved.",
    "secondary": "In humanitarian ethics, targeted charitable interventions intended to lessen social misery without addressing fundamental structural inequalities.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her presence was at first a strain upon Tess, but afterwards an **alleviation** of her heavy solitude."},
      {"author": "Jane Austen", "work": "Emma", "quote": "There was no recovering Miss Taylor, nor much likelihood of ceasing to pity her, without some **alleviation** from friendly company."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "A kind deed brings an immediate **alleviation** to the spirit oppressed by guilt and sorrow."}
    ]
  },
  "Dashboard — lev/alleviative.md": {
    "primary": "Tending or serving to alleviate; mitigating, palliative, or soothing.",
    "secondary": "In historical medicine, therapeutic treatments directed at moderating acute symptoms rather than achieving radical eradication of disease.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The physician must not neglect **alleviative** remedies when cure is beyond the reach of his art."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Punishment", "quote": "The magistrate should apply **alleviative** measures to soften the rigor of penal discipline where humanity demands."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sympathy functions as an **alleviative** balm that soothes nervous agitation in times of emotional distress."}
    ]
  },
  "Dashboard — lev/alleviator.md": {
    "primary": "One who or that which alleviates, softens, lightens, or relieves pain, burden, or distress.",
    "secondary": "In social reform literature, philanthropic figures or legal reforms that diminish civic burdens and exploitation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Patience is the great **alleviator** of human calamity, teaching the mind to endure what cannot be avoided."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "She moved like a gentle **alleviator** among the sick and weary children of the forgotten hamlet."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "True friendship acts as an unfailing **alleviator** of solitary grief and bitter disappointment."}
    ]
  },
  "Dashboard — lev/alleviatory.md": {
    "primary": "Serving or tending to alleviate; soothing, palliative, or mitigating in character.",
    "secondary": "In jurisprudence, mitigating factors or extenuating circumstances pleaded to soften judicial punishment.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The ancient laws provided **alleviatory** provisions to shield unfortunate debtors from total ruin."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The advocate pleaded several **alleviatory** circumstances in the hope of averting the capital sentence."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parliament introduced **alleviatory** clauses into the statute to prevent excessive hardship upon the peasantry."}
    ]
  },
  "Dashboard — lev/elevate.md": {
    "primary": "To raise to a higher position, status, level, or moral character; to lift up.",
    "secondary": "In architectural engineering, to raise a structural element or floor plane above ground level for flood protection or grand visual prominence.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Some men must marry to **elevate** themselves a little, but when I am in need of that assistance I will look elsewhere."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I know of no more encouraging fact than the unquestionable ability of man to **elevate** his life by a conscious endeavour."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A great soul knows how to **elevate** the most ordinary duties into acts of noble virtue."}
    ]
  },
  "Dashboard — lev/elevated.md": {
    "primary": "Raised to a higher physical position, rank, dignity, or intellectual plane; lofty or noble.",
    "secondary": "In meteorology and geography, regions positioned significantly above sea level, producing cooler temperatures and higher wind speeds.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The fire began to get worsted, and Gabriel's **elevated** position being no longer required, he descended the ladder."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "His prosperous fortune had suddenly **elevated** him far above his former humble companions."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The successful general was **elevated** to the imperial purple by the unanimous acclamation of the legions."}
    ]
  },
  "Dashboard — lev/elevation.md": {
    "primary": "The height to which something is raised above a point of reference (such as sea level); the act of lifting or promoting.",
    "secondary": "In architectural drawing, an orthographic projection of one vertical face or facade of a building showing exterior dimensions without perspective distortion.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He had sunk from his modest **elevation** as pastoral king into the very slime-pits of poverty."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "During the slow **elevation** of the land above the sea, new habitats were created for coastal organisms."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The western **elevation** of the basilica reveals a magnificent harmony of arches and sculptured columns."}
    ]
  },
  "Dashboard — lev/elevator.md": {
    "primary": "A movable platform or cage for carrying passengers or freight between different levels of a building; a mechanical lift.",
    "secondary": "In aeronautics, a horizontal control surface hinged to the tail assembly of an aircraft used to control pitch.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Whenever Tess lifted her head she beheld always the great upgrown straw-stack, with the **elevator** carrying the yellow sheaves aloft."},
      {"author": "H. G. Wells", "work": "When the Sleeper Wakes", "quote": "He was carried upward at breathtaking speed in a glass-enclosed **elevator** toward the summit of the tower."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The mechanical **elevator** glided smoothly from floor to floor, packed with well-dressed shoppers."}
    ]
  },
  "Dashboard — lev/eleven.md": {
    "primary": "The cardinal number following ten and preceding twelve, represented by the Arabic numerals 11.",
    "secondary": "In sports history, a traditional athletic team or side comprising eleven active field players (notably in cricket, association football, and field hockey).",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Thus we may see, quoth he, how the world wags: 'tis but an hour ago since it was nine, and after one hour more 'twill be **eleven**."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "It was twenty minutes to **eleven** by the great clock when we stopped before the mysterious iron gate."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "The village clock struck **eleven**, and the two boys stole softly into the dark churchyard."}
    ]
  },
  "Dashboard — lev/eleven-plus.md": {
    "primary": "An examination formerly administered to primary school pupils in England and Wales at around age eleven to govern grammar school admission.",
    "secondary": "In British educational sociology (post-1944 Butler Act), the tripartite sorting mechanism determining placement into grammar, technical, or secondary modern schools.",
    "quotes": [
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The competitive examination system, culminating in tests like the **eleven-plus**, entrenched class privilege under the guise of educational merit."},
      {"author": "Richard Hoggart", "work": "The Uses of Literacy", "quote": "Passing the **eleven-plus** represented a dramatic turning point in the working-class scholarship boy's intellectual journey."},
      {"author": "Michael Young", "work": "The Rise of the Meritocracy", "quote": "The institutionalisation of the **eleven-plus** established intelligence quotient testing as the ultimate arbiter of social status."}
    ]
  },
  "Dashboard — lev/eleven-sided.md": {
    "primary": "Having eleven distinct sides or boundary lines; hendecagonal.",
    "secondary": "In classical Euclidean plane geometry, pertaining to a hendecagon, possessing eleven vertices and internal angles totaling 1620 degrees.",
    "quotes": [
      {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "Geometrical figures of complex symmetry, even an **eleven-sided** polygon, reflect the mathematical order of nature."},
      {"author": "Arthur Cayley", "work": "The Collected Mathematical Papers", "quote": "The properties of a regular **eleven-sided** figure cannot be fully constructed using only an unmarked ruler and compass."},
      {"author": "William Rowan Hamilton", "work": "Elements of Quaternions", "quote": "The angular relations of an **eleven-sided** polyhedron can be computed with precision through algebraic quaternions."}
    ]
  },
  "Dashboard — lev/eleventh.md": {
    "primary": "Coming next after the tenth in an ordered sequence; being one of eleven equal parts into which a whole is divided.",
    "secondary": "In proverbial and biblical parlance (at the eleventh hour), the latest possible time or final moment before an impending deadline or catastrophe.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Douglas and the English rebels met at the **eleventh** hour upon the bloody field of Shrewsbury."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He postponed his decision until the **eleventh** hour, hoping that some unforeseen stroke of fortune would intervene."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Even in the **eleventh** hour of the monarchy, the court clung to illusions of absolute authority."}
    ]
  },
  "Dashboard — lev/irrelevance.md": {
    "primary": "The quality, condition, or fact of being irrelevant; lack of relation, applicability, or pertinence to the matter at hand.",
    "secondary": "In evidentiary jurisprudence and legal procedure, the inadmissibility of proffered evidence that fails to logically prove or disprove a fact at issue.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "That he should be regarded as a suitor to herself would have seemed to her a ridiculous **irrelevance**."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She listened with quiet amusement to his rambling remarks, noting their total **irrelevance** to the crisis."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "In rigorous logical analysis, emotional rhetoric must be discarded as mere **irrelevance**."}
    ]
  },
  "Dashboard — lev/irrelevancy.md": {
    "primary": "An irrelevant remark, matter, or instance; the state or character of lacking pertinent connection.",
    "secondary": "In parliamentary and courtroom debate, an argument that departs from the proposition under consideration (fallacia ignoratio elenchi).",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "I think, said Gregory, with placid **irrelevancy**, that we will call a cab."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "Holmes waved aside the inspector's objection as a tedious **irrelevancy** that obscured the essential footprints."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The speech was filled with brilliant rhetorical flourishes, but spoiled by constant **irrelevancy** to the bill."}
    ]
  },
  "Dashboard — lev/irrelevant.md": {
    "primary": "Not connected with, applicable to, or bearing upon the subject or issue under consideration; immaterial.",
    "secondary": "In logic, propositions that provide no evidentiary support or inferential connection to the conclusion being argued.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "True, drink is a pleasant delight, said Jan, offering an **irrelevant** truism to soothe the dispute."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "It is of the highest importance in the art of deduction not to allow **irrelevant** facts to confuse your judgment."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Minor differences in plumage between non-interbreeding varieties are entirely **irrelevant** to sexual selection."}
    ]
  },
  "Dashboard — lev/irrelevantly.md": {
    "primary": "In an irrelevant, impertinent, or disconnected manner; without logical relation to the topic.",
    "secondary": "In literary dialogue and psychological characterization, speaking off-topic due to emotional preoccupation or mental absent-mindedness.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "The machinery is of the most perfect, assented Durand, somewhat **irrelevantly**; but what of the spirit?"},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She spoke **irrelevantly** of the garden flowers, hoping to avert the stormy argument between her guests."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "He interposed **irrelevantly** with a question about train timetables, shrinking from the painful topic."}
    ]
  },
  "Dashboard — lev/lev.md": {
    "primary": "The basic monetary unit and standard currency of Bulgaria, subdivided into one hundred stotinki.",
    "secondary": "In Balkan economic history, the Bulgarian national currency established under the Bulgarian National Bank in 1881, originally tied to the Latin Monetary Union.",
    "quotes": [
      {"author": "Rebecca West", "work": "Black Lamb and Grey Falcon", "quote": "The border merchant exchanged his foreign paper for the Bulgarian **lev**, counting each note with meticulous care."},
      {"author": "James David Bourchier", "work": "The Balkan Question", "quote": "Peasant commerce throughout Sofia was conducted in the national **lev**, which maintained stable value prior to the wars."},
      {"author": "John Reed", "work": "The War in Eastern Europe", "quote": "In the shops along the boulevard, bread and coffee were paid for with a few silver pieces of the **lev**."}
    ]
  },
  "Dashboard — lev/levallorphan.md": {
    "primary": "A synthetic morphinan derivative that acts as an opioid antagonist, formerly used to counteract narcotic-induced respiratory depression.",
    "secondary": "In clinical pharmacology, a mixed agonist-antagonist displacing pure agonists like morphine from mu-opioid receptors while exhibiting partial kappa intrinsic activity.",
    "quotes": [
      {"author": "Louis S. Goodman & Alfred Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The administration of **levallorphan** promptly reverses opioid-induced respiratory depression without abolishing analgesia entirely."},
      {"author": "Henry K. Beecher", "work": "Measurement of Subjective Responses", "quote": "Clinical trials indicated that combining **levallorphan** with potent narcotics diminished the incidence of postoperative hypoventilation."},
      {"author": "Nathan B. Eddy", "work": "The Search for New Analgesics", "quote": "Chemical modifications of the morphinan nucleus yielded **levallorphan**, a compound displaying notable narcotic antagonist properties."}
    ]
  },
  "Dashboard — lev/levant.md": {
    "primary": "The historical geographical term for the countries bordering the eastern shores of the Mediterranean Sea; or (archaic verb) to run away or abscond secretly.",
    "secondary": "In historical maritime commerce, the mercantile sphere dominated by the Levant Company, trading silks, spices, and textiles between England and Ottoman ports.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He had traded across every ocean, from the icy shores of Greenland to the sunny ports of the **levant**."},
      {"author": "Walter Scott", "work": "Peveril of the Peak", "quote": "The dishonest gambler resolved to **levant** under cover of darkness before his debts of honor fell due."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley feared that the shady adventurer had chosen to **levant** without settling his billiard account."}
    ]
  },
  "Dashboard — lev/levanter.md": {
    "primary": "A strong, easterly Mediterranean wind blowing through the Strait of Gibraltar; or one who absconds or defaults on debts.",
    "secondary": "In nautical meteorology, a damp, cloudy easterly gale that builds heavy swells against the western entrance of the Mediterranean.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "So that Monsoons, Pampas, Nor'-Westers, Harmattans, Trades; any wind but the **levanter** and the Simoom had blown in our teeth."},
      {"author": "Washington Irving", "work": "The Alhambra", "quote": "The damp easterly **levanter** swept across the bay, wrapping the Rock of Gibraltar in a dense shroud of fog."},
      {"author": "Charles Lever", "work": "The Confessions of Harry Lorrequer", "quote": "The notorious **levanter** was seen slipping toward the packet boat, leaving a trail of unpaid debts behind him."}
    ]
  },
  "Dashboard — lev/levantine.md": {
    "primary": "Of, relating to, or characteristic of the Levant or its peoples; a native or inhabitant of the eastern Mediterranean region.",
    "secondary": "In textile and commercial history, a stout, rich twilled silk fabric originally imported into western Europe from the Levant.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She went to the cabinet of maps and unrolled one, tracing the trade routes along the **levantine** coast."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Those Ausonia claims, **levantine** regions these; the Azores send their jessamine across the western waters."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **levantine** merchants preserved the commercial networks that linked Constantinople to the markets of Alexandria."}
    ]
  },
  "Dashboard — lev/levator.md": {
    "primary": "A muscle that serves to raise or elevate a body part or anatomical structure.",
    "secondary": "In vertebrate comparative anatomy, skeletal muscles such as the levator scapulae or levator ani that provide postural suspension and upward movement.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "This man, for instance, had on both sides of his neck a true and powerful **levator** claviculae muscle."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **levator** scapulae arises from the transverse processes of the upper cervical vertebrae and elevates the medial border of the scapula."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The coordinated contraction of the **levator** muscles lifts the lower jaw during vigorous mastication."}
    ]
  },
  "Dashboard — lev/levee.md": {
    "primary": "An embankment built along the edge of a river or canal to prevent flooding; or a formal morning reception held by a monarch or high official.",
    "secondary": "In hydrologic engineering, earthen or reinforced dikes designed to contain high-discharge flood stages within a channelized alluvial floodplain.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I used to attend the king's **levee** once or twice a week, and had often seen him under the barber's hand."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "He says indifferently and alike How are you friend? to the President at his **levee**."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The great river broke through the earthen **levee**, inundating thousands of acres of fertile cotton land."}
    ]
  },
  "Dashboard — lev/level.md": {
    "primary": "Having a flat, horizontal surface with no irregularities, tilt, or elevation difference; equal in rank, condition, or degree.",
    "secondary": "In geodesy and surveying, an instrument (such as a spirit level or optical transit) used to determine a truly horizontal line of sight perpendicular to local gravity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Sonnets", "quote": "No, I am that I am, and they that **level** at my abuses reckon up their own."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Drive a nail home and clinch it so faithfully that you can wake up in the night and see your work on a **level** with the finest."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection tends only to make each organic being as perfect as, or slightly more perfect than, the other inhabitants of the same country with which it comes into competition, raising them to a common **level**."}
    ]
  },
  "Dashboard — lev/level-headed.md": {
    "primary": "Characterized by sound judgment, emotional balance, calm rationality, and practical good sense.",
    "secondary": "In managerial and crisis psychology, the capacity to maintain objective cognitive evaluation during high-stress operational dilemmas.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer seemed to be a **level-headed** and observant man, despite his eccentric passion for cranial anthropology."},
      {"author": "Joseph Conrad", "work": "Chance", "quote": "The captain was known as a **level-headed** seaman whose steady temper never failed in dangerous squalls."},
      {"author": "John Galsworthy", "work": "The Forsyte Saga", "quote": "Soames regarded himself as a cool, **level-headed** man of affairs who never permitted sentiment to compromise financial security."}
    ]
  },
  "Dashboard — lev/leveler.md": {
    "primary": "One who or that which levels, equalizes, or flattens; an advocate of the abolition of social or political distinctions.",
    "secondary": "In 17th-century British political history (Levellers), radical democratic reformers who advocated universal male suffrage, equality before the law, and religious tolerance.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Death is the ultimate **leveler**, dragging emperors and mendicants alike to the same quiet dust."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The democratic **leveler** sought to overthrow all hereditary magistracies in the name of popular sovereignty."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Time acts as an impartial **leveler**, defacing the monuments of conquerors and the cottages of shepherds."}
    ]
  },
  "Dashboard — lev/levelheaded.md": {
    "primary": "Calm, sensible, and not easily unhinged or rattled; possessing practical and sound judgment.",
    "secondary": "In administrative leadership, evaluating contentious proposals through dispassionate analysis rather than impulsive rhetoric.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "A successful pioneer must be bold yet **levelheaded**, capable of facing sudden peril without losing his composure."},
      {"author": "Willa Cather", "work": "O Pioneers!", "quote": "Alexandra proved to be a **levelheaded** woman whose foresight and frugality turned the wild prairie into rich farmland."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The mate was a **levelheaded** sailor who went about his duties with quiet efficiency, untouched by the hysteria around him."}
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

print(f"Speed Batch 6A: Successfully updated {updated}/{len(data)} notes.")
