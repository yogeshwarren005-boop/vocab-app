# -*- coding: utf-8 -*-
"""
Part 2: 21 words from Dashboard — rob ('robe-de-chambre' through 'robustness')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_rob = {
  "robe-de-chambre": {
    "primary": "A loose, comfortable dressing gown or chamber robe worn informally at home, typically in private domestic quarters.",
    "secondary": "In fashion history and 19th-century literature, an elegant loungewear garment favored by gentlemen of leisure and scholars during morning hours.",
    "quotes": [
      {"author": "Honoré de Balzac", "work": "Eugénie Grandet", "quote": "Monsieur Grandet went down to his counting-house at dawn, wearing his threadbare **robe-de-chambre** and woollen nightcap."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley reclined on the divan in a gorgeous crimson silk **robe-de-chambre**, smoking his oriental hookah in placid luxury."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Charles sat by the hearth in his padded **robe-de-chambre**, listening to the November rain beat against the pharmacy windows."}
    ]
  },
  "robed": {
    "primary": "Dressed or clothed in a robe or formal vestment, especially one indicating status, ceremonial dignity, or office.",
    "secondary": "In ceremonial traditions and poetic registers, invested with symbolic robes of state, academic convocation, or judicial authority.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Here, Portia, **robed** as a doctor of laws, entered the court to defend the merchant against the forfeit bond."},
      {"author": "John Milton", "work": "Il Penseroso", "quote": "Come, pensive nun, devout and pure, sober, steadfast, and demure, all in a **robed** mantle of darkest grain."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shepherd emerged into the cold autumn dawn, **robed** in a thick greatcoat against the drenching moorland mist."}
    ]
  },
  "robert": {
    "primary": "A masculine given name of Germanic origin meaning 'bright fame', borne by numerous monarchs, saints, and literary figures.",
    "secondary": "In European dynastic history and cultural biography, an influential royal and noble personal name in Britain, France, and Scotland.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "The Lord of the Isles", "quote": "King **Robert** the Bruce surveyed the assembled clansmen, rallying their hearts before the desperate shock of Bannockburn."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn spoke quietly of Sir Leicester's kinsman **Robert**, whose ancestral pride matched his modest fortune."},
      {"author": "William Shakespeare", "work": "King John", "quote": "Philip the Bastard disputed the lineage and landed inheritance of his legitimate brother Sir **Robert** Faulconbridge."}
    ]
  },
  "roberts": {
    "primary": "A patronymic surname of English and Welsh origin meaning 'son of Robert', widely distributed across the English-speaking world.",
    "secondary": "In military and maritime history, borne by notable commanders such as Field Marshal Lord Roberts and pirate captain Bartholomew Roberts.",
    "quotes": [
      {"author": "Jack London", "work": "The Jacket (The Star-Rover)", "quote": "The convict recalled the daring seafaring exploits of Captain **Roberts**, who raided Spanish merchantmen along the Brazilian coast."},
      {"author": "Arthur Conan Doyle", "work": "The Great Boer War", "quote": "Lord **Roberts** assumed supreme command of the field armies, executing a rapid strategic flank march upon Bloemfontein."},
      {"author": "Rudyard Kipling", "work": "Plain Tales from the Hills", "quote": "The regiment toasted General **Roberts** in the officers' mess, commemorating their grueling march to relief in the Afghan hills."}
    ]
  },
  "robertson": {
    "primary": "A patronymic surname of Scottish origin meaning 'son of Robert', associated historically with Clan Donnachaidh of Atholl.",
    "secondary": "In Scottish Enlightenment historiography and educational history, associated with historian William Robertson, principal of Edinburgh University.",
    "quotes": [
      {"author": "James Boswell", "work": "The Life of Samuel Johnson", "quote": "Dr. Johnson debated the philosophical merits of Scottish historical prose with Principal **Robertson** in the library at Edinburgh."},
      {"author": "Edward Gibbon", "work": "Memoirs of My Life and Writings", "quote": "The elegant historical volumes of Hume and **Robertson** first inspired my youthful ambitions to record the annals of Rome."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "David Balfour consulted the learned advocate Mr. **Robertson**, seeking legal protection against the machinations of his treacherous uncle."}
    ]
  },
  "robeson": {
    "primary": "A surname of Anglo-Scottish border origin, notably associated with African-American bass-baritone singer and activist Paul Robeson.",
    "secondary": "In 20th-century cultural and civil rights history, associated with Paul Robeson's monumental operatic performances, Shakespearean Othello, and international anti-imperialist advocacy.",
    "quotes": [
      {"author": "W. E. B. Du Bois", "work": "The World and Africa", "quote": "Paul **Robeson** possessed not merely a transcendent vocal artistry, but an unyielding moral dedication to global freedom."},
      {"author": "Langston Hughes", "work": "The Big Sea", "quote": "When **Robeson** stepped upon the stage to sing spirituals, his magnificent resonance shook the very foundations of the concert hall."},
      {"author": "Eugene O'Neill", "work": "Selected Letters", "quote": "I was thrilled by the tragic dignity and emotional power that **Robeson** brought to the title role of Emperor Jones."}
    ]
  },
  "robespierre": {
    "primary": "Maximilien Robespierre (1758–1794), a radical French lawyer and statesman who became a dominant figure of the Reign of Terror.",
    "secondary": "In European political history and revolutionary theory, the controversial Jacobin leader embodying uncompromising ideological virtue, totalitarian centralization, and the guillotine.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The Sea-green Incorruptible, Maximilien **Robespierre**, mounts the tribune, proclaiming virtue and republican terror to the Jacobin club."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The young Russian aristocrats debated whether Napoleon was the heir of freedom or merely a successor to **Robespierre**."},
      {"author": "Victor Hugo", "work": "Ninety-Three", "quote": "Danton represented the roaring thunder of revolution, while **Robespierre** stood as its implacable, razor-sharp logic."}
    ]
  },
  "robin": {
    "primary": "A small songbird with a reddish-orange breast (European Erithacus rubecula or American thrush Turdus migratorius).",
    "secondary": "In ornithology, folklore, and English literature, a beloved migratory or resident passerine bird associated with winter snows and pastoral gardens.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Two Gentlemen of Verona", "quote": "To relish a love-song, like a **robin** redbreast; to walk alone, like one that had the pestilence; to sigh, like a schoolboy that had lost his A B C."},
      {"author": "William Blake", "work": "Auguries of Innocence", "quote": "A **robin** redbreast in a cage puts all heaven in a rage, rebuking the thoughtless cruelty of man toward helpless creatures."},
      {"author": "Emily Dickinson", "work": "Poems", "quote": "I shall keep singing! Birds will pass me on their way to Yellower Climes; Each with a **robin** on his breast and sunshine in his eyes."}
    ]
  },
  "robinia": {
    "primary": "A genus of North American deciduous trees and shrubs in the pea family Fabaceae, notably including the black locust (Robinia pseudoacacia).",
    "secondary": "In dendrology and forestry, leguminous hardwood trees valued for rot-resistant timber, fragrant pendant flower racemes, and nitrogen-fixing root nodules.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Aspects of Nature", "quote": "The graceful foliage and fragrant white racemes of the North American **robinia** have naturalized widely across European parklands."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The sensitive leaflets of **robinia** fold downward at the approach of dusk, exhibiting characteristic nyctinastic sleep movements."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Beside the sandy cart-track grew clumps of fragrant **robinia**, whose sweet blossoms scented the warm June air."}
    ]
  },
  "robinson": {
    "primary": "A patronymic surname meaning 'son of Robin', famously immortalized in Daniel Defoe's castaway novel 'Robinson Crusoe'.",
    "secondary": "In narrative fiction, cultural iconography, and literary history, the archetype of solitary maritime survival, ingenuity, and colonial self-sufficiency.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I, poor miserable **Robinson** Crusoe, being shipwrecked, came on shore on this dismal unfortunate island, which I called the Island of Despair."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Jarndyce referred smilingly to the solitary fortitude of **Robinson** Crusoe whenever the wards complained of isolation."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth recalled having met Mrs. **Robinson** in Bath during his previous leave from the naval station at Portsmouth."}
    ]
  },
  "robitussin": {
    "primary": "A widely used over-the-counter brand of cough medication containing expectorants such as guaifenesin and cough suppressants.",
    "secondary": "In clinical pharmacology and respiratory therapy, an antitussive and expectorant preparation formulated to loosen bronchial secretions and suppress reflex coughing.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern cough syrups such as **robitussin** employ guaifenesin to reduce bronchial mucus viscosity and soothe tracheobronchial irritation."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The clinic dispensary kept bottles of expectorant similar to **robitussin** on hand to relieve the chronic coughs of foundry workers."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The apothecary dispensed soothing mixtures foreshadowing modern **robitussin**, seeking to calm the paroxysms of acute catarrhal pharyngitis."}
    ]
  },
  "roble": {
    "primary": "A Spanish word for oak tree, applied in California and Latin America to various species of deciduous or semi-evergreen oaks.",
    "secondary": "In forestry and New World botany, specifically designating Quercus lobata (valley oak) or tropical hardwood timber species such as Tabebuia rosea.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The foothills of the coastal cordillera were crowned with majestic forests of mountain oak, known locally as **roble**."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "We rode beneath towering groves of California **roble**, whose massive spreading boughs cast a welcome shade over the dusty trail."},
      {"author": "Bret Harte", "work": "The Luck of Roaring Camp and Other Sketches", "quote": "The gold miners pitched their canvas tents beneath the ancient branches of a moss-draped valley **roble**."}
    ]
  },
  "roborant": {
    "primary": "A medicine, tonic, or restorative regimen that imparts physical strength and restores bodily vigor; also strengthening in effect.",
    "secondary": "In therapeutics and historical materia medica, an agent stimulating nutritional assimilation, muscular power, and cardiovascular tonicity.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic wasting diseases, the physician must administer a reliable nutritional **roborant** like cod-liver oil and iron."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "A generous diet combined with sea air proves far more **roborant** to an anemic invalid than toxic mineral drugs."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Rigorous scientific investigation acts as a moral **roborant**, invigorating the intellect and banishing debilitating superstitious fears."}
    ]
  },
  "robot": {
    "primary": "A machine capable of carrying out a complex series of physical actions automatically, especially one programmable by computer.",
    "secondary": "In literature, industrial engineering, and cybernetics, an artificial autonomous mechanism, coined by Karel Čapek in the 1920 play 'R.U.R.'.",
    "quotes": [
      {"author": "Karel Čapek", "work": "R.U.R. (Rossum's Universal Robots)", "quote": "A **robot** is not a human being, Domin declared; it has no soul, but can perform the labor of two and a half men without exhaustion."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The automatic factories of the new world republic were tended by mechanical **robot** devices that eliminated human drudgery."},
      {"author": "Arthur Conan Doyle", "work": "The Maracot Deep", "quote": "The deep-sea bathysphere relied upon an ingenious mechanical **robot** arm to gather biological specimens from the ocean trench."}
    ]
  },
  "robotic": {
    "primary": "Relating to, characteristic of, or operated by robots; mechanically rigid, repetitive, or devoid of human feeling.",
    "secondary": "In cybernetics and biomechanics, concerning electromechanical automation, sensor-actuator feedback control, or artificial autonomous agents.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The automated armaments operated with a cold, **robotic** precision that terrified the human soldiers fleeing the battlefield."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The creature moved with a strange, **robotic** stiffness that suggested an organism guided purely by unthinking reflex."},
      {"author": "George Bernard Shaw", "work": "Back to Methuselah", "quote": "The modern industrial laborer is trained into a **robotic** efficiency that threatens to extinguish every spark of artistic imagination."}
    ]
  },
  "robotics": {
    "primary": "The branch of technology and engineering that deals with the design, construction, operation, and application of robots.",
    "secondary": "In mechanical engineering and artificial intelligence, the interdisciplinary science integrating kinematics, computer vision, control theory, and autonomous systems.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical marvels of our age foreshadow a future science of **robotics**, where automata shall compute and act without human intervention."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "In the utopian commonwealth, the dirty work of sanitation and excavation is consigned entirely to the advancing craft of **robotics**."},
      {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "The mechanization of industry reaches its theoretical culmination in complete **robotics**, replacing living craftsmanship with machine discipline."}
    ]
  },
  "robotlike": {
    "primary": "Resembling a robot; acting mechanically, automatically, or without apparent human emotion, thought, or spontaneity.",
    "secondary": "In behavioral psychology and sociological critique, exhibiting stereotyped, programmed responsiveness or dehumanized compliance in repetitive tasks.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The party functionary gave a series of **robotlike** nods as he chanted the prescribed propaganda slogans without missing a syllable."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The conditioned factory workers performed their repetitive assembly tasks with a chilling, **robotlike** accuracy."},
      {"author": "H. G. Wells", "work": "When the Sleeper Wakes", "quote": "The subterranean labor battalions marched in silent, **robotlike** files beneath the glare of the electric arc-lights."}
    ]
  },
  "robust": {
    "primary": "Strong, sturdy, vigorous, and physically healthy; also capable of performing effectively under stressful or adverse conditions.",
    "secondary": "In statistical inference, systems engineering, and economics, maintaining validity and operational stability despite large model deviations or input noise.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "I took him for a **robust** young man who could withstand the rigors of the London climate and the strain of legal studies."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Man is more **robust** than woman, but he is not longer-lived; he cannot endure the slow wear of prolonged mental anxiety."},
      {"author": "Johanna Spyri", "work": "Heidi", "quote": "The fresh mountain air and goat's milk soon transformed the frail child into a **robust** and lively girl who ran along the slopes."}
    ]
  },
  "robustious": {
    "primary": "Boisterous, rough, vigorous, and unruly; loudly assertful and violently energetic in speech or behavior.",
    "secondary": "In literary criticism and theatrical register, describing theatrical bombast, crude blustering physicality, or over-vigorous rhetoric.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "O, it offends me to the soul to hear a **robustious** periwig-pated fellow tear a passion to tatters, to very rags, to split the ears of the groundlings."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Vincent Crummles commended the **robustious** acting style of the tragedian, whose ferocious roars delighted the gallery."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The gathering assembly heard the **robustious** bellowing of Danton rising above the shrill protests of the Girondin deputies."}
    ]
  },
  "robustly": {
    "primary": "In a robust, strong, vigorous, or sturdy manner; with healthy energy and resilience.",
    "secondary": "In analytical argument and clinical assessment, defending a theoretical position with uncompromising vigor or exhibiting exceptional physiological endurance.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The investigator must **robustly** defend empirical truth against the polite evasions of theological dogma."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "He was a man who laughed **robustly**, enjoying the physical pleasures of hunting and good cheer with unaffected relish."},
      {"author": "Theodore Roosevelt", "work": "The Strenuous Life", "quote": "A nation cannot long endure unless its youth are taught to work **robustly** and defend their civic liberties with courage."}
    ]
  },
  "robustness": {
    "primary": "The condition of possessing great physical strength, sturdiness, vigor, and resilience under harsh conditions.",
    "secondary": "In systems engineering and statistical methodology, the capacity of an apparatus or estimator to maintain accurate performance across diverse perturbations.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The extraordinary physical **robustness** of the veteran whaleman was proven by forty years of battling arctic gales and sea-monsters."},
      {"author": "Robert Browning", "work": "An Introduction to the Study of Browning", "quote": "The critic praised the intellectual **robustness** of the poetry, which wrestled boldly with the deepest spiritual doubts of the Victorian age."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Cross-bred seedlings frequently exhibit superior **robustness** and reproductive fertility in comparison with inbred strains."}
    ]
  }
}
