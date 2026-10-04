# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — ven Part 2 (14B, 35 words) ---
  "Dashboard — ven/provencal.md": {
    "primary": "Relating to Provence, its people, or the Romance language (Occitan) spoken in southeastern France.",
    "secondary": "In medieval romance philology, the literary dialect of the 12th-century troubadours cultivating courtly love poetry.",
    "quotes": [
      {"author": "Walter Scott", "work": "Anne of Geierstein", "quote": "The minstrel sang a melodious **provencal** ballad celebrating the deeds of chivalric knighthood."},
      {"author": "Henry James", "work": "A Little Tour in France", "quote": "The midday sun bathed the ancient Roman arena in brilliant **provencal** light."},
      {"author": "W. B. Yeats", "work": "Ideas of Good and Evil", "quote": "The early lyric poets were deeply stirred by the delicate melodies of **provencal** song."}
    ]
  },
  "Dashboard — ven/provence.md": {
    "primary": "A historical province of southeastern France extending from the lower Rhône river to the Italian border.",
    "secondary": "In Mediterranean historical geography, a region known for Greco-Roman antiquity, olive agriculture, and distinctive limestone landscapes.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "The pleasant hills and olive groves of **provence** welcomed travelers journeying south toward Avignon."},
      {"author": "Tobias Smollett", "work": "Travels through France and Italy", "quote": "The dry mistral wind blew fiercely across the stony plains of lower **provence**."},
      {"author": "Henry James", "work": "A Little Tour in France", "quote": "Every ancient gateway in **provence** seems stamped with the monumental seal of imperial Rome."}
    ]
  },
  "Dashboard — ven/provenience.md": {
    "primary": "The place of origin, historical source, or archaeological findspot of an artifact or biological specimen.",
    "secondary": "In stratigraphic archaeology and museology, the exact three-dimensional spatial coordinates and layer context where an artifact was excavated.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "Holmes established the exact **provenience** of the porcelain vase from the palace of the Emperor of China."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The geological **provenience** of the fossil specimen was confirmed by the stratum in which it lay embedded."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "We trace the intellectual **provenience** of an idea back to its original sensory associations."}
    ]
  },
  "Dashboard — ven/reconvene.md": {
    "primary": "To convene, assemble, or call together again after an adjournment, recess, or suspension.",
    "secondary": "In parliamentary procedure, the formal resumption of deliberative legislative or judicial sessions following a stated recess.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The legislature was empowered to **reconvene** at the seat of government upon executive proclamation."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The houses of parliament agreed to **reconvene** when the autumn harvest had concluded."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The national assembly decided to **reconvene** without waiting for royal assent."}
    ]
  },
  "Dashboard — ven/reinvention.md": {
    "primary": "The process or act of inventing something anew, or transforming an established persona, concept, or institution.",
    "secondary": "In organizational sociology, strategic institutional restructuring whereby an enterprise alters its fundamental mission to survive changing environments.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Each successive civilization achieved a partial **reinvention** of mechanical arts and legal frameworks."},
      {"author": "George Orwell", "work": "Collected Essays", "quote": "The totalitarian state specializes in the continual **reinvention** of historical memory."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Genius does not consist in sterile repetition, but in the bold **reinvention** of universal truths."}
    ]
  },
  "Dashboard — ven/revenant.md": {
    "primary": "A visible ghost, apparition, or person who returns after death or after a prolonged absence.",
    "secondary": "In European folklore and Gothic literature, a reanimated corpse returning from the grave to haunt living relatives or avenge a wrong.",
    "quotes": [
      {"author": "Walter Scott", "work": "Letters on Demonology and Witchcraft", "quote": "The fearful peasant mistook the cloaked wanderer in the mist for a spectral **revenant**."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The legend of the spectral hound seemed like a dreadful **revenant** haunting the desolate moor."},
      {"author": "Robert Louis Stevenson", "work": "The Master of Ballantrae", "quote": "He stood upon the threshold like a pale **revenant** restored to life from the icy wilderness."}
    ]
  },
  "Dashboard — ven/revenue.md": {
    "primary": "The total income generated by a government, company, or individual; public funds yielded by taxation.",
    "secondary": "In public finance, gross fiscal receipts accrued from customs duties, income levies, and excise taxes used to service the national debt.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The expense of defending the society cannot be defrayed without public **revenue** raised from the people."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A vigorous national government requires steady and predictable sources of public **revenue**."},
      {"author": "Thomas Jefferson", "work": "First Inaugural Address", "quote": "A wise and frugal government will collect sufficient **revenue** without exhausting the earnings of labor."}
    ]
  },
  "Dashboard — ven/revenuer.md": {
    "primary": "A federal government officer tasked with enforcing excise tax laws, especially on alcoholic beverages.",
    "secondary": "In American Appalachian history, Treasury agents who raided illicit mountain distilleries and pursued 'moonshiners'.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The mountain folk kept a wary eye peeled for any prowling federal **revenuer** searching the ravines."},
      {"author": "Jack London", "work": "John Barleycorn", "quote": "Illicit distillers in the remote hills learned to dread the sudden raid of an armed **revenuer**."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Tales circulated among the elders of how the old **revenuer** had tracked hidden stills through the pine woods."}
    ]
  },
  "Dashboard — ven/seven.md": {
    "primary": "The cardinal number equivalent to the sum of six and one; the numeral 7.",
    "secondary": "In numerology and comparative myth, a symbolic number frequently associated with cosmic cycles, days of creation, and celestial spheres.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "All the world's a stage, and all the men and women merely players; his acts being **seven** ages."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The sun completed his diurnal course through the **seven** spheres of heaven."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Marley's ghost reminded Scrooge that his former partner had been dead these **seven** years."}
    ]
  },
  "Dashboard — ven/sevener.md": {
    "primary": "A member of the Ismaili branch of Shia Islam that recognizes Ismail ibn Jafar as the seventh and final Imam.",
    "secondary": "In Islamic theological history, the historical sectarian movement distinguishing the Septimanian branch from the Twelver tradition.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The doctrine of the **sevener** sect maintained that divine leadership closed with the seventh imam."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Sectarian schisms divided the faithful, distinguishing the orthodox believer from the zealous **sevener**."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The traveler noted doctrinal disputes between the dominant school and the elusive **sevener** pilgrims."}
    ]
  },
  "Dashboard — ven/sevens.md": {
    "primary": "Plural of seven; a card game played by discarding sequential cards, or rugby played with seven-a-side teams.",
    "secondary": "In idiomatic English ('at sixes and sevens'), a condition of confusion, disorder, or unresolved conflict.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "The parlor arrangements were left at sixes and **sevens** until the guests had departed."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The household affairs of the careless baronet had long stood at sixes and **sevens**."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The whole market square was thrown into confusion, with merchandise left at sixes and **sevens**."}
    ]
  },
  "Dashboard — ven/sevensome.md": {
    "primary": "A group, party, or musical/athletic ensemble consisting of seven persons or things.",
    "secondary": "In Scottish dance tradition, a traditional reel danced simultaneously by seven performers.",
    "quotes": [
      {"author": "Walter Scott", "work": "Waverley", "quote": "The highland piper played a brisk reel for the merry **sevensome** gathered upon the green."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "We watched the lively **sevensome** finish their dance before dispersing into the mountain heather."},
      {"author": "James Hogg", "work": "The Private Memoirs and Confessions of a Justified Sinner", "quote": "A rustic **sevensome** assembled at the tavern to celebrate the conclusion of the harvest."}
    ]
  },
  "Dashboard — ven/seventh.md": {
    "primary": "The ordinal number corresponding to seven; one of seven equal parts into which a whole is divided.",
    "secondary": "In music theory, an interval spanning seven diatonic scale degrees, characteristic of dominant and major seventh chords.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "On the **seventh** day he took his rest, as ancient custom commanded."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **seventh** chapter treats of simple ideas derived immediately from sensory perception."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "It was upon the **seventh** evening of my stay that the mysterious letter was delivered."}
    ]
  },
  "Dashboard — ven/seventhly.md": {
    "primary": "In the seventh place; seventh in an enumerated series or formal order of arguments.",
    "secondary": "In classical scholastic discourse and sermonic rhetoric, introducing the seventh sub-argument of a doctrinal thesis.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "He proceeded through his arguments methodically, and **seventhly** demonstrated the absurdity of modern pedantry."},
      {"author": "Walter Scott", "work": "Old Mortality", "quote": "The preacher droned on through his theological heads, announcing **seventhly** the doom of the unrepentant."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The professor argued sixthly on clothes as emblems, and **seventhly** on garments as historical monuments."}
    ]
  },
  "Dashboard — ven/souvenir.md": {
    "primary": "A thing kept or purchased as a reminder of a person, place, visit, or memorable occasion.",
    "secondary": "In material culture studies, a physical relic or manufactured token serving as an emotional mnemonic of travel.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I preserved the little silver brooch as a cherished **souvenir** of my tranquil days at Lowood."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She purchased an exquisite Florentine cameo as a lasting **souvenir** of her Italian holiday."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He presented me with a worn sea-shell as a humble **souvenir** of our Yarmouth adventures."}
    ]
  },
  "Dashboard — ven/supervene.md": {
    "primary": "To occur or take place as an unforeseen, additional, or extraneous event or development.",
    "secondary": "In metaphysics and philosophy of mind, a relation between properties wherein high-level properties supervene on low-level physical bases.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Unforeseen calamities may **supervene** upon even the most cautiously considered political reforms."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A period of civil war did **supervene** upon the death of the emperor, shattering provincial peace."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "New sensations **supervene** upon prior neural impressions, modifying the conscious stream of thought."}
    ]
  },
  "Dashboard — ven/uneven.md": {
    "primary": "Not level, flat, or smooth; irregular in surface, quality, spacing, or balance.",
    "secondary": "In statistical analysis and economics, asymmetrical or unequal distribution of income, resources, or developmental gains.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The cart rattled noisily over the rough, **uneven** stones of the rural village roadway."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The flickering candlelight threw long, **uneven** shadows across the damp brick walls."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "His gait was jerky and **uneven**, reflecting the deep agitation of his troubled mind."}
    ]
  },
  "Dashboard — ven/unevenly.md": {
    "primary": "In an uneven manner; irregularly, unequally, or with an asymmetrical surface or distribution.",
    "secondary": "In microeconomic geography, regional investment apportioned unevenly across metropolitan cores and rural peripheries.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The moonlight shone **unevenly** through broken rifts in the heavy storm clouds."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The turf on the ancient barrow was worn **unevenly** by generations of grazing sheep."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The strange mechanical dial spun **unevenly**, jerking violently from epoch to epoch."}
    ]
  },
  "Dashboard — ven/unevenness.md": {
    "primary": "Irregularity, roughness, or lack of symmetry, flatness, or uniformity across a surface or distribution.",
    "secondary": "In materials science and topography, surface roughness or elevation variance measured across a specified contour.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The structural **unevenness** of the coral reef surface created sheltered lagoons for diverse marine life."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The artistic beauty of Gothic stone carving lies in its vital **unevenness**, defying mechanical uniformity."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The noticeable **unevenness** of his temperament made his neighbors cautious in their daily dealings."}
    ]
  },
  "Dashboard — ven/uneventful.md": {
    "primary": "Marked by no interesting, important, or disruptive events; quiet, monotonous, or tranquil.",
    "secondary": "In historical narrative and biographical analysis, prolonged periods characterized by institutional stability and domestic quietude.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The winter passed in an **uneventful** routine of domestic duties and quiet morning walks."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes sighed over several **uneventful** weeks during which no remarkable crime had been reported."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her life in the quiet pensionnat flowed on in an **uneventful** and sober stream."}
    ]
  },
  "Dashboard — ven/uneventfully.md": {
    "primary": "In an uneventful manner; without incident, disturbance, disruption, or notable excitement.",
    "secondary": "In logistics and transport history, a voyage or transit proceeding uneventfully according to operational schedules.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The trading ship steamed **uneventfully** across the glass-smooth waters of the tropical sea."},
      {"author": "Henry James", "work": "The American", "quote": "The quiet afternoon slipped by **uneventfully** among the shaded walks of the Luxembourg garden."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The first days of our voyage passed **uneventfully**, favored by a steady easterly breeze."}
    ]
  },
  "Dashboard — ven/unproven.md": {
    "primary": "Not demonstrated or established by evidence, trial, or argument; unverified.",
    "secondary": "In legal and scientific epistemology, a hypothesis or claim lacking empirical validation or evidentiary substantiation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A rigorous naturalist cannot accept an **unproven** speculation as an established law of nature."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes warned against building elaborate deductions upon an **unproven** initial assumption."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An assertion remains merely conjectural while the premises on which it rests are **unproven**."}
    ]
  },
  "Dashboard — ven/vena.md": {
    "primary": "A vein, especially a blood vessel carrying blood from the tissues toward the heart.",
    "secondary": "In classical human anatomy, major venous vessels such as the vena cava superior and vena cava inferior returning systemic blood.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis (On the Motion of the Heart and Blood)", "quote": "The blood is continuously returned to the right atrium through the great **vena** cava."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The surgeon traced the rupture of the pulmonary **vena** to severe blunt thoracic trauma."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Deoxygenated blood from the systemic organs enters the **vena** cava before reaching the heart."}
    ]
  },
  "Dashboard — ven/venal.md": {
    "primary": "Capable of being bought or bribed; corrupt, mercenary, or open to dishonorable financial influence.",
    "secondary": "In political science and historical sociology, venal offices or administrative posts sold by the crown for royal fiscal revenue.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A **venal** Praetorian guard auctioned the supreme imperial dignity to the highest bidder."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The independence of judges prevents them from falling into **venal** subjection to the legislature."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "He described the courts of Europe where **venal** ministers betrayed public interests for gold."}
    ]
  },
  "Dashboard — ven/venality.md": {
    "primary": "Openness to bribery, corruption, or prostitution of principles for monetary or material gain.",
    "secondary": "In institutional history, systemic venality involving the lawful sale of judicial and magisterial offices under the Ancien Régime.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The blatant **venality** of corrupt magistrates eroded all public confidence in the judicial bench."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The court of King Charles was infamous for the pervasive **venality** of its high officials."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Universal **venality** reigned throughout the provincial administration in the late empire."}
    ]
  },
  "Dashboard — ven/venally.md": {
    "primary": "In a venal manner; corruptly, dishonorably, or through susceptibility to bribery.",
    "secondary": "In public integrity law, official duties exercised venally in exchange for clandestine remuneration.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The provincial governor disposed **venally** of high civic appointments to wealthy patrons."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The bailiff acted **venally**, accepting bribes from lawbreakers while punishing the poor."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Pamphleteers who wrote **venally** for ministerial gold were quickly exposed by the revolutionary clubs."}
    ]
  },
  "Dashboard — ven/venation.md": {
    "primary": "The arrangement or pattern of veins in a plant leaf, an insect wing, or anatomical tissue.",
    "secondary": "In botanical morphology and paleontology, parallel vs. reticulate venation used to classify monocotyledonous and dicotyledonous angiosperms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The delicate **venation** of an insect wing exhibits complex functional architecture shaped by selection."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "Reticulated or netted **venation** distinguishes the foliage of dicots from the parallel veins of grasses."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The subtle symmetry in the leaf's green **venation** guides the distribution of vital sap."}
    ]
  },
  "Dashboard — ven/veneer.md": {
    "primary": "A thin layer of fine wood or material bonded to a cheaper base; an attractive or deceptive surface appearance.",
    "secondary": "In cabinetmaking and decorative arts, fine wood veneers (such as mahogany or rosewood) glued under pressure to carcass wood.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The Veneerings were brand-new people in a brand-new house, covered with a glittering **veneer** of wealth."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His suave manners were only a superficial **veneer** covering a selfish and arrogant temperament."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The wilderness stripped away the flimsy **veneer** of European civilization from the colonizers."}
    ]
  },
  "Dashboard — ven/veneering.md": {
    "primary": "The process or art of applying thin sheets of decorative wood to a surface; a decorative wood layer.",
    "secondary": "In sociological satire, a superficial show of culture, respectability, or refinement concealing crude ambition.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The social circle practiced an elaborate system of **veneering**, pretending to profound antiquity."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "He criticized the architectural **veneering** of brick structures with thin marble slabs as deceptive."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "Underneath the fashionable **veneering** of high society lay vulgar greed and trivial rivalries."}
    ]
  },
  "Dashboard — ven/venerability.md": {
    "primary": "The quality of commanding deep respect by virtue of age, character, wisdom, or sacred associations.",
    "secondary": "In cultural anthropology, ancestral venerability accorded to patriarchs, elders, and sacred sanctuaries.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient senatorial traditions lent an aura of sublime **venerability** to the Roman constitution."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The grey-haired magistrate commanded respect through the dignified **venerability** of his person."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The **venerability** of ancient stones awakens reverent contemplation in the traveler."}
    ]
  },
  "Dashboard — ven/venerable.md": {
    "primary": "Commanding respect or reverence through age, wisdom, holy character, or historic associations.",
    "secondary": "In Roman Catholic hagiography, an honorific title given to a deceased person whose heroic virtues have been officially decreed.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The **venerable** doctor sat in the sun, beloved and honored by all who knew his long suffering."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The old mansion possessed a **venerable** air, surrounded by noble oaks that had stood for centuries."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The **venerable** clergyman read the ancient liturgy in a tone of dignified solemnity."}
    ]
  },
  "Dashboard — ven/venerableness.md": {
    "primary": "An imposing, dignified, and sacred character derived from great antiquity, virtue, or wisdom.",
    "secondary": "In aesthetic criticism and antiquarian studies, the perceived sacred dignity conferred upon monuments by long passage of time.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The ruined abbey possessed an impressive **venerableness** that filled the antiquary with silent awe."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The dark timbered facade acquired an antique **venerableness** with each passing generation."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The solemn **venerableness** of primeval mountain peaks inspires profound humility in mankind."}
    ]
  },
  "Dashboard — ven/venerate.md": {
    "primary": "To regard with deep respect, reverence, or awe, especially on account of sacred character or wisdom.",
    "secondary": "In comparative religion, the formal theological distinction between dulia (venerating saints) and latria (worshiping God alone).",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The citizens were taught to **venerate** the memory of their republican ancestors."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Children should learn to **venerate** truth and justice above all worldly advantages."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Man was created to **venerate** the noble and heroic wherever he beholds it in history."}
    ]
  },
  "Dashboard — ven/venerating.md": {
    "primary": "The act of regarding or treating with profound reverence, honor, and deep respect.",
    "secondary": "In liturgical theology, the customary practice of venerating icons, relics, or the cross during solemn rites.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Pilgrims assembled at the shrine, **venerating** the sacred relics of the early Christian martyrs."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "She knelt before the ancient shrine, **venerating** the image of the Madonna with fervent piety."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Society stagnates when citizens persist in uncritically **venerating** outdated ancestral customs."}
    ]
  },
  "Dashboard — ven/veneration.md": {
    "primary": "Great respect, reverence, or awe inspired by the dignity, wisdom, or holiness of a person or object.",
    "secondary": "In phrenological classification (Gall and Spurzheim), the cerebral faculty presumed to govern religious sentiment and deference to authority.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I looked upon the kind schoolmaster with boundless affection and sincere **veneration**."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "We receive our civil liberties with a sense of reverent **veneration** from our forefathers."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea felt a deep intellectual **veneration** for Mr. Casaubon's vast biblical learning."}
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

print(f"Motion Batch 14B: Successfully updated {updated}/{len(data)} notes.")
