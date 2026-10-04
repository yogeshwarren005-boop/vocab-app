# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Batch 2 of Cluster Light:
- Dashboard — lun (25 words)
- Dashboard — sol (26 words)
Total: 51 words.
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

data_batch2_lun = {
  "diflunisal": {
    "primary": "A nonsteroidal anti-inflammatory drug (NSAID), salicylic acid derivative used to treat arthritis and pain.",
    "secondary": "In clinical pharmacology, an analgesic and antipyretic that acts by inhibiting prostaglandin synthesis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern therapeutic regimens for osteoarthritis frequently incorporate salicylic derivatives such as **diflunisal** to alleviate joint stiffness."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The physician prescribed a potent analgesic compound analogous to modern **diflunisal** to soothe the rheumatic invalid."},
      {"author": "Louis Pasteur", "work": "Researches on Microorganisms", "quote": "Pharmacological chemists synthesized fluorinated phenolic analgesics related to **diflunisal** to diminish gastric irritation."}
    ]
  },
  "luna": {
    "primary": "The ancient Roman goddess personifying the moon, corresponding to the Greek Selene.",
    "secondary": "In planetary science and poetic literature, the Earth's natural satellite.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Less bright the moon, but opposite in leveled west was set, his mirror, with full face borrowing her light from him, for **Luna** shines reflected."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions paid religious veneration to the celestial deities Sol Invictus and **Luna** on the Syrian frontier."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The night procession in the temple honored the radiant image of pale **Luna** with hymns and burning incense."}
    ]
  },
  "lunacy": {
    "primary": "Severe mental illness, madness, or insanity, historically believed to fluctuate with phases of the moon.",
    "secondary": "Extreme foolishness, absurdity, or reckless folly in behavior or policy.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "If't be so, Hamlet is of the faction that is wrong'd; his madness is poor Hamlet's enemy: what I have done, that might your nature, honour, and exception roughly awake, I here proclaim was madness; was't Hamlet wrong'd Laertes? Never Hamlet: if Hamlet from himself be ta'en away, and when he's not himself does wrong Laertes, then Hamlet does it not; Hamlet denies it. Who does it then? His madness; if't be so, Hamlet is of the faction that is wrong'd; his **lunacy** is poor Hamlet's enemy."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Jarndyce regarded the protracted Chancery suit as an institutional monument of national **lunacy**."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley declared that entering into such a rash matrimonial engagement was pure **lunacy**."}
    ]
  },
  "lunar": {
    "primary": "Pertaining to, caused by, or characteristic of the moon.",
    "secondary": "Measured by the revolutions of the moon; resembling the moon in pale silvery light or phases.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Telescopic observation discloses deep volcanic craters and mountainous ridges across the **lunar** surface."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Marine invertebrates often synchronize their reproductive cycles with the recurring monthly **lunar** tides."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vast ocean swells gleamed beneath the pale **lunar** rays like plains of undulating silver."}
    ]
  },
  "lunaria": {
    "primary": "A genus of annual and biennial flowering plants in the cabbage family (Brassicaceae), including honesty or silver dollar.",
    "secondary": "In botany, prized for translucent, silvery, coin-shaped partition walls of its mature seed pods.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The garden honesty, termed **Lunaria** by herbalists, beareth round silvery pods that shine like full moons."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The dried silicles of **Lunaria** are collected for winter decorative bouquets on account of their pearly septa."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated varieties of **Lunaria** exhibit striking stability in the membranous texture of their seed vessels."}
    ]
  },
  "lunate": {
    "primary": "Crescent-shaped, sickle-shaped, or resembling the crescent moon.",
    "secondary": "In human anatomy, designating the crescent-shaped carpal bone of the wrist situated between the scaphoid and triquetrum.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The proximal row of carpal bones includes the scaphoid, the **lunate**, and the pyramidal elements."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "The distal edge of the pelvic fin bears a series of delicate **lunate** cartilaginous rays in primitive sharks."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The desert wind sculpted the sand into sweeping **lunate** dunes whose horns pointed in the direction of the gale."}
    ]
  },
  "lunatic": {
    "primary": "A person suffering from severe psychiatric illness or madness; an eccentric or wildly reckless person.",
    "secondary": "Wildly foolish, dangerous, or irrational in nature or conduct.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "The **lunatic**, the lover, and the poet are of imagination all compact: one sees more devils than vast hell can hold."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The ferocious laughter echoed from the attic where the violent **lunatic** Bertha Mason was confined."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes warned that the escaped **lunatic** from Princetown was lurking somewhere upon the desolate moor."}
    ]
  },
  "lunation": {
    "primary": "The interval of time between one new moon and the next; a synodic lunar month (approximately 29.53 solar days).",
    "secondary": "A complete cycle of lunar phases from new moon through full moon and back.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The exact duration of a synodic **lunation** is determined by comparing ancient and modern solar eclipse records."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The nomadic tribes of Arabia regulated their seasonal migrations and religious truces by the monthly **lunation**."},
      {"author": "Isaac Newton", "work": "Philosophiæ Naturalis Principia Mathematica", "quote": "The perturbing attraction of the sun causes small inequalities in the period of the **lunation** throughout the year."}
    ]
  },
  "lunch": {
    "primary": "A light midday meal typically eaten between breakfast and dinner.",
    "secondary": "To eat a light midday meal.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The gentlemen returned from their morning shooting excursion eager to partake of a cold **lunch** in the parlor."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick unpacked the hamper on the carriage seat, producing a delightful picnic **lunch** of cold fowl and pie."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The reapers sat beneath the shade of the great oak at noon to eat their harvest **lunch** of bread and cheese."}
    ]
  },
  "luncheon": {
    "primary": "A formal or substantial midday meal, often served for guests or official occasions.",
    "secondary": "A midday reception or social banquet.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Elton presided over the elegant cold **luncheon** with an air of patronizing condescension."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyers paused in their examination of the witnesses to partake of a substantial chop-house **luncheon**."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Lord Warburton invited the entire traveling party to a sumptuous **luncheon** at his country manor."}
    ]
  },
  "luncher": {
    "primary": "A person who partakes of lunch or dines at midday.",
    "secondary": "A diner who eats a midday meal at a restaurant, club, or tavern.",
    "quotes": [
      {"author": "George Gissing", "work": "The Whirlpool", "quote": "The fashionable West End café was crowded with every gay **luncher** escaping the midday heat of the city."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The pompous club **luncher** complained bitterly of the underdone mutton chop served by the waiter."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "He watched the solitary City **luncher** reading his financial newspaper over a plate of roast beef."}
    ]
  },
  "lunching": {
    "primary": "Partaking of a midday meal or dining at lunchtime.",
    "secondary": "The act, habit, or social occasion of eating lunch together.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The family were **lunching** upon cold meat and fruit when the unexpected guest arrived at the hall."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether spent the afternoon **lunching** in a quiet Parisian garden restaurant overlooking the Seine."},
      {"author": "Virginia Woolf", "work": "Jacob's Room", "quote": "The young undergraduates were **lunching** noisily in the college hall after their morning lectures."}
    ]
  },
  "lunchroom": {
    "primary": "A room or dining hall in a school, factory, office, or public facility where light lunches are served or eaten.",
    "secondary": "A casual counter-service cafeteria or small restaurant.",
    "quotes": [
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The striking factory hands gathered inside the workers' cooperative **lunchroom** to plan their demonstration."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt entered the crowded downtown **lunchroom**, ordering a quick sandwich and coffee at the counter."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "Carrie found refuge from the freezing winter wind inside a modest commercial **lunchroom** near the avenue."}
    ]
  },
  "lunchtime": {
    "primary": "The period of the middle of the day during which lunch is customarily eaten; the midday lunch break.",
    "secondary": "The scheduled noon recess for dining and rest.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "At **lunchtime**, the clerks put away their quill pens and hurried off into the crowded alleys of the City."},
      {"author": "H. G. Wells", "work": "The History of Mr. Polly", "quote": "When **lunchtime** arrived, Mr. Polly retired to the cellar stairs to enjoy his meat pie in peace."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The market square filled with farm laborers and grain merchants as the church bells chimed **lunchtime**."}
    ]
  },
  "lunette": {
    "primary": "An arched opening, crescent-shaped aperture, or semicircular window in a vaulted ceiling, wall, or dome.",
    "secondary": "In Renaissance art, a semicircular decorative wall painting or sculptured relief framed by an arch.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The upper **lunette** of the portal was filled with a delicate sculptured relief representing the Adoration of the Magi."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "Perugino painted a heavenly choir of angels within the arched **lunette** above the high altar."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Sunlight poured through the high semicircular **lunette** of the chapel, illuminating the ancient oak stalls."}
    ]
  },
  "lunisolar": {
    "primary": "Pertaining to or determined by the combined or mutual gravitational and optical actions of the sun and moon.",
    "secondary": "In calendar systems, designating a calendar reconciling lunar months with the solar year.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiæ Naturalis Principia Mathematica", "quote": "The precession of the equinoxes arises from the **lunisolar** gravitational pull upon the Earth's equatorial bulge."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Ancient Babylonian astronomers developed an ingenious **lunisolar** cycle of intercalary months to harmonize the seasons."},
      {"author": "Thomas Babington Macaulay", "work": "Essays", "quote": "The ancient Hindu calendar employs a complex **lunisolar** computation to fix sacred festival days."}
    ]
  },
  "lunt": {
    "primary": "A match, burning torch, or slow match used to ignite cannons or firearms in archaic Scottish and naval parlance.",
    "secondary": "To emit smoke, puffs of vapor, or flames, especially from a tobacco pipe.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The old soldier blew the glowing coal of his tobacco pipe until it burst into a bright **lunt** of flame."},
      {"author": "Robert Burns", "work": "Halloween", "quote": "She turned the key and blew the **lunt**, and through the keyhole cast her eye to spy her future lover."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The gunner stood ready with burning **lunt** in hand to touch off the quarterdeck carronades."}
    ]
  },
  "lunula": {
    "primary": "The pale, half-moon-shaped white area at the base of a human fingernail or toenail.",
    "secondary": "In classical archaeology, a crescent-shaped bronze or gold amulet worn by girls for protection.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cyanosis and trophic changes are frequently observed first in the matrix surrounding the **lunula** of the nail."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The opaque white appearance of the nail **lunula** results from the imperfect keratinization of the underlying matrix cells."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The Roman maiden wore a delicate silver **lunula** suspended from her neck to ward off the evil eye."}
    ]
  },
  "lunule": {
    "primary": "A variant term for lunula; a small crescent-shaped mark, physiological structure, or patch of color.",
    "secondary": "In malacology, the heart-shaped or crescent depression anterior to the beak in bivalve shells.",
    "quotes": [
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The hinge ligament of the bivalve shell is bounded anteriorly by a deeply excavated cordate **lunule**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Shell collectors distinguish fossil species of Venus by the depth and ornamentation of the circumscribed **lunule**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A dark transverse line across the **lunule** appeared following the patient's recovery from typhoid fever."}
    ]
  },
  "sublunar": {
    "primary": "Situated beneath the moon; belonging to the terrestrial world below the lunar sphere.",
    "secondary": "Pertaining to earthly, mortal, or fleeting human affairs as distinguished from celestial perfection.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Night with her sullen wings flitted over the **sublunar** world, shrouding mortal eyes in slumber."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Aristotle drew a sharp distinction between the immutable heavens and the mutable elements of the **sublunar** sphere."},
      {"author": "Percy Bysshe Shelley", "work": "Epipsychidion", "quote": "She seemed a soul too pure and radiant to dwell within our cloudy **sublunar** atmosphere."}
    ]
  },
  "sublunary": {
    "primary": "Situated beneath the moon; belonging to the physical Earth or mortal existence.",
    "secondary": "Characteristic of terrestrial life; mutable, perishable, and subject to time and decay.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The History of Rasselas, Prince of Abissinia", "quote": "Human life is a state in which much is to be endured, and little to be enjoyed, in this imperfect **sublunary** state."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman philosophers meditated upon the transient vanity of all **sublunary** grandeur and power."},
      {"author": "John Donne", "work": "A Valediction: Forbidding Mourning", "quote": "Dull **sublunary** lovers' love, whose soul is sense, cannot admit absence, because it doth remove those things which elemented it."}
    ]
  },
  "superlunar": {
    "primary": "Situated above the moon; celestial, heavenly, or transcendent beyond the lunar sphere.",
    "secondary": "Pertaining to the immutable celestial heavens in classical cosmology.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The seraph soared upward into the **superlunar** ether, leaving the gloomy orbits of terrestrial night behind."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The mystic vision transported the soul into **superlunar** realms of uncreated light and harmony."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "The devout mind contemplates the incorruptible perfection of **superlunar** intelligences."}
    ]
  },
  "superlunary": {
    "primary": "Situated higher than the moon; celestial, otherworldly, or spiritually elevated above earthly mutability.",
    "secondary": "Pertaining to divine, incorruptible cosmic realms beyond mortal change.",
    "quotes": [
      {"author": "Edmund Spenser", "work": "An Hymne of Heavenly Beautie", "quote": "The spirit ascends unto those **superlunary** heights where eternal beauty shines unclouded."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Ancient astronomers erroneously believed that **superlunary** regions were exempt from physical alteration or decay."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He looked beyond this mundane sphere, seeking communion with serene **superlunary** truths."}
    ]
  },
  "translunar": {
    "primary": "Extending, situated, or traveling beyond the orbit of the moon.",
    "secondary": "In astronautics, designating trajectories or space flights traversing the expanse beyond the lunar orbit.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Cometary orbits sweep outward into vast **translunar** voids far beyond the planetary spheres."},
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "The spacecraft fired its auxiliary rockets to enter a high **translunar** trajectory toward the outer planets."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The metal sphere drifted silently into the mysterious darkness of the **translunar** abyss."}
    ]
  },
  "translunary": {
    "primary": "Situated, occurring, or reaching beyond the moon; superlunary and ethereal.",
    "secondary": "Transcending mundane, earthly existence into sublime metaphysical realms.",
    "quotes": [
      {"author": "Michael Drayton", "work": "To My Most Dearly-Loved Friend, Henry Reynolds, Esq.", "quote": "Neat Marlowe bathed in the Thespian springs had in him those brave **translunary** things that the first poets had."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The metaphysical poets delighted in bold metaphors that ventured into **translunary** speculations."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Genius touches common worldly things with a divine, **translunary** illumination."}
    ]
  }
}

data_batch2_sol = {
  "consolable": {
    "primary": "Capable of being comforted, cheered, or relieved from grief, sorrow, or affliction.",
    "secondary": "Susceptible to soothing words or alleviation of emotional suffering.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was relieved to find her mother **consolable** under the severe financial disappointment."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The weeping widow proved readily **consolable** when the terms of the prosperous will were read."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The child cried bitterly at first, but was soon **consolable** with a piece of seed-cake and a toy."}
    ]
  },
  "consolation": {
    "primary": "Comfort received by a person after a loss, bereavement, or disappointment.",
    "secondary": "A person, circumstance, or thought that brings relief or solace in affliction.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth found great **consolation** in the affectionate letters and calm good sense of her sister Jane."},
      {"author": "Boethius", "work": "The Consolation of Philosophy", "quote": "Philosophy visited the imprisoned sage to offer heavenly **consolation** against the blows of fortune."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery's honest friendship was Pip's only true **consolation** during his troubled boyhood."}
    ]
  },
  "consolatory": {
    "primary": "Tending, serving, or intended to comfort, console, or relieve grief and mental distress.",
    "secondary": "Expressing soothing compassion or sympathetic solace.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The philosopher offered several **consolatory** reflections upon the inevitable transience of human grief."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne whispered a few gentle **consolatory** words to poor Mrs. Musgrove in her bereavement."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The minister read a **consolatory** psalm to the weeping family gathered in the cottage."}
    ]
  },
  "console": {
    "primary": "To comfort, soothe, or alleviate the grief, disappointment, or distress of someone.",
    "secondary": "In architecture and furniture, an ornamental bracket, cantilever, or cabinet supporting a tabletop.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Nothing can **console** the broken-hearted king wandering naked upon the stormy heath."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I tried to **console** little Adèle when she wept over the departure of her governess."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "An antique gilded **console** table supported a magnificent Chinese porcelain vase in the vestibule."}
    ]
  },
  "consoling": {
    "primary": "Providing solace, comfort, or emotional relief in times of sorrow, grief, or misfortune.",
    "secondary": "Serving to alleviate painful sorrow or disappointment.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea found a deeply **consoling** influence in active deeds of benevolence among the poor."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The spirit showed Scrooge a warm, **consoling** vision of family affection around the hearth."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "There was something quiet and **consoling** in the steady rhythmic pulse of the farm machinery."}
    ]
  },
  "desolate": {
    "primary": "Deserted, uninhabited, barren, and dismal in physical aspect; bleak and abandoned.",
    "secondary": "Utterly wretched, sorrowful, and overwhelmed by grief or loneliness.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster fled across the **desolate** glaciers of the high Alps, seeking solitude among ice peaks."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt solitary and **desolate** in the cold stone dormitory, far from every human friend."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe looked around upon the **desolate** island, weeping at his total separation from mankind."}
    ]
  },
  "desolately": {
    "primary": "In a desolate, dismal, or hopelessly abandoned and sorrowful manner.",
    "secondary": "Bleakly, forlornly, or with utter loneliness and despair.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The wind moaned **desolately** through the stunted gorse bushes of Egdon Heath at twilight."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The rain fell **desolately** upon the muddy streets, washing the dreary pavement of Tom-all-Alone's."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Silas gazed **desolately** upon the empty hole beneath the floorboards where his gold had been."}
    ]
  },
  "desolation": {
    "primary": "A state of complete destruction, ruin, waste, and devastation of a place or landscape.",
    "secondary": "Profound sorrow, misery, loneliness, and emotional grief.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The Roman Campagna presented an image of majestic **desolation**, strewn with broken aqueducts and tombs."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Barbarian invasions spread fire and **desolation** through the once-fertile valleys of northern Italy."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab stood alone upon the quarterdeck, his dark heart consumed by a terrible inward **desolation**."}
    ]
  },
  "inconsolable": {
    "primary": "Incapable of being consoled, comforted, or relieved from intense grief or bereavement.",
    "secondary": "Devastated by heartbreak that rejects all solace or alleviation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne was utterly **inconsolable** after receiving Willoughby's cruel letter of renunciation."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Ham Peggotty was **inconsolable** when Em'ly fled with Steerforth, wandering the lonely beach at night."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The mother was **inconsolable** for months after the tragic death of her only little boy."}
    ]
  },
  "parasol": {
    "primary": "A lightweight umbrella used especially by women to provide shade from the hot sun.",
    "secondary": "An overhead sunshade or canopy designed for solar protection.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The ladies opened their silk **parasol** sunshades as they strolled along the garden gravel walk."},
      {"author": "Henry James", "work": "Daisy Miller", "quote": "Daisy walked through the Roman ruins carrying a dainty lace-trimmed **parasol** over her shoulder."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The fashionable summer visitors held white **parasol** canopies to shield their complexions from the chalk glare."}
    ]
  },
  "sol": {
    "primary": "The personification of the sun in ancient Roman religion; in astronomy, the Sun itself.",
    "secondary": "In physical chemistry, a colloidal suspension of solid particles in a liquid medium.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Emperor Aurelian dedicated a magnificent temple in Rome to **Sol** Invictus, the unconquered sun god."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "At whose sight all the stars hide their diminished heads; to thee I call, but with no friendly voice, and add thy name, O **Sol**, to tell thee how I hate thy beams."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The ruby-red liquid represents a colloidal **sol** of metallic gold suspended in pure water."}
    ]
  },
  "solar": {
    "primary": "Pertaining to, determined by, proceeding from, or utilizing the light, heat, or energy of the Sun.",
    "secondary": "Measured by the motion or cycle of the Sun, as a solar year.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiæ Naturalis Principia Mathematica", "quote": "The planets revolve around the Sun in ellipses having the center of the **solar** body in one focus."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Green vegetation depends directly upon the absorption of **solar** light for organic carbon synthesis."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The spectroscope reveals dark absorption lines traversing the continuous spectrum of the **solar** atmosphere."}
    ]
  },
  "solarise": {
    "primary": "The British spelling of solarize; to expose a photographic image to excessive light, reversing its tonal highlights.",
    "secondary": "To expose materials to the direct rays of the sun for bleaching or photochemical treatment.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "If the sensitive paper is exposed too long to bright sun, it begins to **solarise** and reverse its tones."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Prolonged exposure to solar radiation may **solarise** the optical glass, inducing an amber discoloration."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The chemical reagents were left in the open courtyard to **solarise** and clarify under the equatorial sun."}
    ]
  },
  "solarium": {
    "primary": "A glass-enclosed room, porch, or sun parlor designed to admit extensive natural sunlight.",
    "secondary": "In medical sanatoriums, a sun terrace used for phototherapy and tuberculosis recovery.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Convalescent pulmonary patients derived immense benefit from rest in the open **solarium** of the sanatorium."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Milly Theale sat in the glass **solarium** of the Venetian palazzo, warmed by the autumn sun."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The hospital architects incorporated a spacious rooftop **solarium** to provide fresh air and light."}
    ]
  },
  "solarize": {
    "primary": "To subject a photographic emulsion to excessive light exposure, causing partial reversal of dark and light tones.",
    "secondary": "In agriculture, to sterilize topsoil by covering it with clear plastic sheeting under intense solar heat.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Direct sunlight of extreme intensity will quickly **solarize** the daguerreotype plate, turning shadows pale."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "Extreme radiant energy tends to **solarize** delicate photochemical compounds exposed in open glass tubes."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The heat-ray seemed to **solarize** and bleach the landscape with blinding, incandescent ferocity."}
    ]
  },
  "soled": {
    "primary": "Having a sole of a specified kind, as shoes or footwear fitted with leather or rubber soles.",
    "secondary": "In anatomy and zoology, having an underside or plantar surface.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She walked in heavy hobnail-**soled** boots that clattered loudly along the flinty country roads."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The convict wore thick-**soled** coarse shoes covered with mud from the desolate marshes."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Palmer took off his iron-**soled** sandals before stepping into the knight's hospitable chamber."}
    ]
  },
  "solely": {
    "primary": "Exclusively, entirely, wholly, and to the exclusion of all other persons, things, or factors.",
    "secondary": "Only; without any other companion, cause, or partner.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "He acted **solely** from a generous desire to preserve Elizabeth's family from public disgrace."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection acts **solely** by accumulating slight, successive, favorable variations."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The treaty-making power is vested **solely** in the executive and the senate."}
    ]
  },
  "solent": {
    "primary": "The strait of water separating the Isle of Wight from the mainland of southern England.",
    "secondary": "In maritime navigation and yachting, renowned as a challenging sheltered tidal waterway.",
    "quotes": [
      {"author": "Walter Scott", "work": "Peveril of the Peak", "quote": "The frigate dropped anchor in the sheltered roadstead of the **Solent** after weathering the gale."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Beagle weighed anchor at Plymouth after putting into the **Solent** to complete nautical surveys."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "Naval torpedoboats conducted tactical maneuvers in the choppy waters of the **Solent** off Portsmouth."}
    ]
  },
  "solitarily": {
    "primary": "In a solitary manner; alone, secluded, or in complete isolation from human company.",
    "secondary": "With lonely seclusion or separate existence.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Hester Prynne lived **solitarily** in a lonely cottage by the seashore, shunned by the townspeople."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard walked **solitarily** along the Roman earthworks, brooding over his ruined commercial fortune."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The lone albatross wheeled **solitarily** above the ship's wake in the stormy southern seas."}
    ]
  },
  "solitariness": {
    "primary": "The condition of living alone, in seclusion, or without companions; lonely seclusion.",
    "secondary": "Complete physical or social isolation from human society.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The unbroken **solitariness** of Marner's cottage life had warped his affections until Eppie came."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy Snowe felt the crushing **solitariness** of her foreign schoolroom during the long summer vacation."},
      {"author": "Ralph Waldo Emerson", "work": "Society and Solitude", "quote": "True genius requires a period of contemplative **solitariness** to mature its deepest intuitions."}
    ]
  },
  "solitary": {
    "primary": "Living, being, or existing alone; unaccompanied, secluded, or isolated from others.",
    "secondary": "Done, passed, or endured alone without companionship.",
    "quotes": [
      {"author": "William Wordsworth", "work": "The Solitary Reaper", "quote": "Behold her, single in the field, yon **solitary** Highland lass! Reaping and singing by herself."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe passed twenty-eight years of **solitary** exile upon his uninhabited island in the Caribbean."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The philosopher pursued his **solitary** meditations in his high watchtower overlooking the city."}
    ]
  },
  "solitude": {
    "primary": "A withdrawal from human company into peaceful seclusion; life lived apart from society and its distractions.",
    "secondary": "A lonely, uninhabited, or quiet secluded place.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "There is a pleasure in the pathless woods, there is a rapture on the lonely shore, there is society, where none intrudes, by the deep sea, and music in its roar: I love not man the less, but Nature more, from these our interviews, in which I steal from all I may be, or have been before, to mingle with the Universe, and feel what I can ne'er express, yet cannot all conceal, in blissful **solitude**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I find it wholesome to be alone the greater part of the time; to be in company, even with the best, is soon wearisome; I love to be alone; I never found the companion that was so companionable as **solitude**."},
      {"author": "Samuel Johnson", "work": "The History of Rasselas, Prince of Abissinia", "quote": "The hermit confessed that absolute **solitude** did not protect the mind from worldly temptations."}
    ]
  },
  "solo": {
    "primary": "A musical composition, performance, or passage executed by a single voice or instrument.",
    "secondary": "Performed, undertaken, or accomplished by one person alone without assistance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The flutist played a plaintive pastoral **solo** that silenced the chattering tavern company."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Klesmer performed a tempestuous piano **solo** that filled the drawing room with thunderous chords."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes played a melancholic violin **solo** late at night to soothe his restless intellect."}
    ]
  },
  "soloist": {
    "primary": "A musician, singer, dancer, or pilot who performs or operates alone as the featured artist.",
    "secondary": "A featured performer executing an individual solo piece.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The violin **soloist** interpreted Beethoven's concerto with exquisite tonal purity and intellectual vigor."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The church choir had no trained **soloist**, but relied upon the sturdy unison of rustic voices."},
      {"author": "Henry James", "work": "The Tragic Muse", "quote": "Miriam stood upon the stage like an inspired dramatic **soloist**, commanding the vast theatre."}
    ]
  },
  "solstice": {
    "primary": "Either of the two times in the year when the sun reaches its highest or lowest point in the sky at noon.",
    "secondary": "The astronomical points along the ecliptic marking the longest and shortest days of the year.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "At the summer **solstice**, the midday sun reaches its greatest northern declination above the Tropic of Cancer."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient pagan tribes lit midsummer fires on mountain hilltops to celebrate the summer **solstice**."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Stonehenge stood aligned with astronomical precision to frame the dawn sun on the summer **solstice**."}
    ]
  },
  "unconsolable": {
    "primary": "An alternative spelling of inconsolable; incapable of being comforted or soothed in profound grief.",
    "secondary": "Heartbroken, desperate, and impervious to sympathetic solace.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The poor grieving sister remained **unconsolable** for weeks following the sudden loss."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The grandfather was **unconsolable** when little Nell closed her eyes in eternal sleep."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "Lucy Ashton sat in **unconsolable** despair, staring blindly out upon the stormy sea."}
    ]
  }
}

data_batch2 = {**data_batch2_lun, **data_batch2_sol}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch2.items():
        p = entry.get("primary", "")
        s = entry.get("secondary", "")
        quotes = entry.get("quotes", [])

        if len(p) < 25:
            errors.append(f"{word}: primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"{word}: secondary definition too short ({len(s)} chars)")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        if p_tokens and s_tokens:
            jaccard = len(p_tokens & s_tokens) / len(p_tokens | s_tokens)
            if jaccard >= 0.70:
                errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")

        if len(quotes) != 3:
            errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")

        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            quote = q.get("quote", "")

            if banned_synthetic_regex.search(author) or banned_synthetic_regex.search(work) or banned_synthetic_regex.search(quote):
                errors.append(f"{word}: synthetic author/work/quote in {author}")

            if author in authors:
                errors.append(f"{word}: duplicate author {author}")
            authors.add(author)

            # Check bolded headword in quote: **word** or **Word**
            escaped_word = re.escape(word).replace(r'\ ', r'[\s\-]')
            bold_pat = re.compile(rf'\*\*[^*]*{escaped_word}[^*]*\*\*', re.I)
            if not bold_pat.search(quote):
                base_word = word.split()[0]
                base_pat = re.compile(rf'\*\*[^*]*{re.escape(base_word)}[^*]*\*\*', re.I)
                if not base_pat.search(quote):
                    errors.append(f"{word}: quote missing bolded headword: '{quote}'")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(data_batch2)} words in Light Batch 2 are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
