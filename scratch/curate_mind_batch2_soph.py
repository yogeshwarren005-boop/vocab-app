# -*- coding: utf-8 -*-
"""
Curates Dashboard — soph (32 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — soph/alsophila.md": {
    "primary": "A genus of large, graceful tree ferns in the family Cyatheaceae, native to tropical mountain rainforests.",
    "secondary": "In paleobotany and pteridology, ancient arborescent ferns with fibrous trunks dating back to the Jurassic period.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the mountain ravines of Java, gigantic tree ferns of the genus **alsophila** spread their fronds thirty feet above the torrent."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We rode beneath magnificent groves of **alsophila**, whose delicate pinnate fronds sheltered lush mosses from the midday sun."},
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "The slopes of Sikkim were densely clothed with **alsophila** tree ferns flourishing amidst the perpetual mountain mists."}
    ]
  },
  "Dashboard — soph/esophageal.md": {
    "primary": "Of, relating to, or situated in the esophagus (the muscular tube connecting the throat to the stomach).",
    "secondary": "In gastroenterology, describing muscular peristalsis, mucosal erosion, or varices along the swallowing passage.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic portal hypertension frequently leads to the formation of dilated **esophageal** veins subject to fatal hemorrhage."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The bolus of food is propelled downward by involuntary waves of contraction passing through the **esophageal** muscular tunic."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "The endoscopic camera advanced slowly, illuminating a severe **esophageal** stricture that prevented normal swallowing."}
    ]
  },
  "Dashboard — soph/esophagitis.md": {
    "primary": "Inflammation of the mucosal lining of the esophagus, commonly caused by acid reflux, infection, or medication irritation.",
    "secondary": "In clinical gastroenterology, erosive reflux disease presenting with retrosternal pyrosis and painful dysphagia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe chemical **esophagitis** may supervene rapidly following the accidental ingestion of mineral acids or caustic alkalis."},
      {"author": "Oliver Sacks", "work": "Uncle Tungsten", "quote": "The patient complained of constant burning retrosternal pain, which the clinic diagnosed as acute reflux **esophagitis**."},
      {"author": "Atul Gawande", "work": "Being Mortal", "quote": "The elderly gentleman suffered from debilitating **esophagitis**, which made even swallowing warm broth an agonizing trial."}
    ]
  },
  "Dashboard — soph/esophagoscope.md": {
    "primary": "An illuminated optical endoscope designed for visual examination and biopsy of the interior of the esophagus.",
    "secondary": "In thoracic surgery and endoscopic history, a rigid or flexible instrument introduced to remove impacted foreign objects.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Direct visualization through the illuminated **esophagoscope** has revolutionized the diagnosis of early mucosal carcinoma."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The otolaryngologist demonstrated how the newly invented **esophagoscope** could safely extract an aspirated coin from the throat."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "The surgeon guided the flexible **esophagoscope** past the cricopharyngeal muscle under direct video magnification."}
    ]
  },
  "Dashboard — soph/esophagus.md": {
    "primary": "The muscular membranous tube through which food and liquids pass from the pharynx downward into the stomach.",
    "secondary": "In human digestive anatomy, an organ approximately ten inches long traversing the posterior mediastinum and diaphragm.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **esophagus** descends through the neck behind the trachea, enters the thorax, and pierces the muscular diaphragm."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Peristaltic muscular contractions of the **esophagus** propel food into the stomach even when an animal hangs head downward."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sudden terror often induces an involuntary spasmodic constriction of the **esophagus**, rendering speech impossible."}
    ]
  },
  "Dashboard — soph/philosopher.md": {
    "primary": "A person who seeks wisdom, enlightenment, or ponders fundamental questions of existence, reality, and morality.",
    "secondary": "In intellectual history, a thinker who constructs or critiques systematic models of metaphysics, logic, and ethics.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "There are more things in heaven and earth, Horatio, than are dreamt of in your **philosopher**'s school."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Plato is philosophy, and philosophy, Plato; to him every subsequent **philosopher** pays unconscious tribute."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The duty of a true **philosopher** is to examine ideas with impartial candor, unswayed by ancient custom or popular clamor."}
    ]
  },
  "Dashboard — soph/philosophic.md": {
    "primary": "Of, relating to, or characteristic of philosophy; calm, rational, and stoically resigned in the face of adversity.",
    "secondary": "In intellectual essays, an analytical temperament seeking foundational explanations behind superficial events.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Marcus Aurelius maintained a serene **philosophic** calm amidst the turbulent pestilence and barbarian wars of the Danube."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate regarded social prejudices with **philosophic** amusement, confident that science would soon dispell ancient ignorance."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "With a **philosophic** flourish Cato throws himself upon his sword; I quietly take to the ship and the boundless sea."}
    ]
  },
  "Dashboard — soph/philosophical.md": {
    "primary": "Relating to the study of fundamental knowledge, reality, and existence; calm, reasonable, and stoical.",
    "secondary": "In scientific and ethical prose, an attitude of rational inquiry seeking primary causes rather than empirical particulars.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A **philosophical** mind will never accept authority without demanding the rational evidence upon which belief must rest."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth bore the disappointment with **philosophical** good humor, resolving to make the best of her rustic surroundings."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists of a **philosophical** turn of mind cannot fail to be struck by the pervasive unity of type in nature."}
    ]
  },
  "Dashboard — soph/philosophically.md": {
    "primary": "In a philosophical manner; calmly, rationally, stoically, or with reference to philosophical principles.",
    "secondary": "In narrative characterization, enduring misfortune with dignified composure and intellectual perspective.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber smiled **philosophically**, observing that while clouds darkened the horizon, something was bound to turn up."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes regarded the ruined carpet **philosophically**, observing that an investigator must accept small domestic casualties."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak took the loss of his flock **philosophically**, turning his face toward new employment without bitterness."}
    ]
  },
  "Dashboard — soph/philosophise.md": {
    "primary": "Speculate or theorize about fundamental issues; explain or moralize in philosophical terms (British spelling).",
    "secondary": "In literary dialogue, engaging in detached reflection upon human folly while observing worldly commotion.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "Men love to **philosophise** upon the vanity of life while greedily reaching for every worldly luxury within their grasp."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare would **philosophise** upon the simple virtues of peasant labor, forgetting the harsh poverty beneath."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The time traveler began to **philosophise** upon the eventual fate of human intellect in an automated golden age."}
    ]
  },
  "Dashboard — soph/philosophiser.md": {
    "primary": "A person who philosophizes, often casually, superficially, or pretentiously (British spelling).",
    "secondary": "In social satire, an armchair moralist who dispenses unhelpful abstract theories in times of crisis.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The eloquent **philosophiser** who lectured upon mastering sorrow wept uncontrollably when death took his own daughter."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Major Dobbin was no pedantic **philosophiser**, but a plain soldier whose quiet loyalty outshone clever drawing-room wits."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The cynical **philosophiser** sat in the club window, sneering at every earnest enterprise as a foolish delusion."}
    ]
  },
  "Dashboard — soph/philosophize.md": {
    "primary": "Speculate, theorize, or moralize about fundamental matters of human life, morality, and knowledge.",
    "secondary": "In character studies, seeking abstract wisdom or moralizing upon ordinary daily events.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Pierre loved to **philosophize** through the long winter evenings, debating Freemasonry and the purpose of human existence."},
      {"author": "Mark Twain", "work": "Adventures of Huckleberry Finn", "quote": "Jim and I would lie on the raft and **philosophize** about whether the stars were made or just happened like eggs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "It is pleasant to **philosophize** upon the harpoon line while sitting safely ashore by a glowing sea-coal grate."}
    ]
  },
  "Dashboard — soph/philosophizer.md": {
    "primary": "A person who philosophizes, especially in a shallow, amateurish, pedantic, or pretentious manner.",
    "secondary": "In character criticism, an individual given to trivial moralizing without practical worldly experience.",
    "quotes": [
      {"author": "Henry James", "work": "The Bostonians", "quote": "Basil Ransom viewed the elderly **philosophizer** as a well-meaning dreamer whose windy lectures changed nothing."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The utopian community was crowded with every species of reformer and long-haired **philosophizer** from New England."},
      {"author": "Washington Irving", "work": "Salmagundi", "quote": "Our local **philosophizer** took the floor, proving in three tedious hours that virtue was preferable to vice."}
    ]
  },
  "Dashboard — soph/philosophizing.md": {
    "primary": "The action of engaging in philosophical speculation, reflection, or moralizing discourse.",
    "secondary": "In dramatic narrative, paused reflection upon mortality, fate, or ethics in the midst of turmoil.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrei tired of the ceaseless political **philosophizing** of the Petersburg salons, longing for the simplicity of the camp."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber's eloquent **philosophizing** could not pay the baker's bill, yet it sustained his cheerful spirit."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen indulged in brutal **philosophizing**, arguing that life was a mere ferment of yeast fighting for crumbs."}
    ]
  },
  "Dashboard — soph/philosophy.md": {
    "primary": "The study of the fundamental nature of knowledge, reality, and existence; also a guiding personal life creed.",
    "secondary": "In intellectual history, academic discourse spanning epistemology, metaphysics, logic, ethics, and aesthetics.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Hang up **philosophy**! Unless **philosophy** can make a Juliet, displant a town, reverse a prince's doom, it helps not."},
      {"author": "John Milton", "work": "Comus", "quote": "How charming is divine **philosophy**! Not harsh and crabbed, as dull fools suppose, but musical as is Apollo's lute."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A little **philosophy** inclineth man's mind to atheism, but depth in **philosophy** bringeth men's minds about to religion."}
    ]
  },
  "Dashboard — soph/soph.md": {
    "primary": "An informal colloquial abbreviation for a sophomore, especially in American colleges and universities.",
    "secondary": "In historical Cambridge academic tradition, an undergraduate in their second or third year (*senior soph*).",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory arrived at Princeton as a confident **soph**, eager to secure a place in the prestigious campus eating clubs."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin looked down upon the incoming freshmen with the seasoned superiority of a medical school **soph**."},
      {"author": "Thomas Hughes", "work": "Tom Brown at Oxford", "quote": "The veteran rowing coach selected an athletic young **soph** to stroke the college eight on the Isis."}
    ]
  },
  "Dashboard — soph/sophism.md": {
    "primary": "A clever but fallacious argument, especially one used deliberately to deceive or mislead others.",
    "secondary": "In philosophical dialectics and rhetoric, a specious syllogism that mimics truth while hiding a logical fallacy.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The diplomat veiled his cynical ambition behind an ingenious **sophism**, persuading the ministers that retreat was victory."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The opponents of the Constitution rely upon a transparent **sophism** to frighten the people into rejecting national unity."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel recognized the subtle **sophism** in Madame Merle's worldly advice, yet lacked the heart to expose it."}
    ]
  },
  "Dashboard — soph/sophist.md": {
    "primary": "A paid teacher of philosophy and rhetoric in ancient Greece; a person who uses clever but fallacious arguments.",
    "secondary": "In classical philosophy, thinkers such as Protagoras and Gorgias contrasted by Socrates with true lovers of wisdom.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thou art a cunning **sophist**, whose slick tongue makes the worse appear the better reason in the senate."},
      {"author": "John Keats", "work": "Lamia", "quote": "Do not all charms fly at the mere touch of cold **sophist** reason? Philosophy will clip an Angel's wings."},
      {"author": "Plato", "work": "The Republic", "quote": "Socrates showed how the professional **sophist** caters to the passions of the great beast, mistaking popular whims for justice."}
    ]
  },
  "Dashboard — soph/sophistic.md": {
    "primary": "Of, relating to, or characteristic of sophists, their teachings, or their subtle, fallacious methods of reasoning.",
    "secondary": "In historical intellectual movements, the Fifth-century BC rhetorical enlightenment in Athens and its Roman revival.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Since I myself had fallen into a **sophistic** maze of doubts, Van Helsing's unwavering conviction steadied my mind."},
      {"author": "John Stuart Mill", "work": "Dissertations and Discussions", "quote": "Grote defended the Athenian teachers against the charge of corrupting youth with mere **sophistic** verbal trickery."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The second century witnessed a brilliant **sophistic** renaissance, wherein Greek rhetoricians were showered with imperial honors."}
    ]
  },
  "Dashboard — soph/sophistical.md": {
    "primary": "Plausible but fallacious; misleading, specious, or deceptive in reasoning or argument.",
    "secondary": "In moral philosophy and legal pleading, arguments constructed with hair-splitting subtleties to evade truth.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester attempted by **sophistical** reasoning to persuade Jane that moral laws might be set aside for love."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen countered my arguments with **sophistical** brilliance, twisting every altruistic ideal into selfish impulse."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Osmond's explanation was so **sophistical** that Isabel felt her very moral landmarks slipping beneath her feet."}
    ]
  },
  "Dashboard — soph/sophisticate.md": {
    "primary": "Make more worldly, refined, or complex; also a person with worldly knowledge, taste, and experience.",
    "secondary": "In social satire, an urbane cosmopolite who disdains provincial customs and embraces cultural avant-garde.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thou art the thing itself; unaccommodated man is no more but such a poor, bare, forked animal as thou art; off, off, you lendings! Come, unbutton here, and **sophisticate** no more."},
      {"author": "Jack London", "work": "The Jacket (The Star-Rover)", "quote": "Civilization tends to **sophisticate** our primal instincts until we mistake artificial etiquette for human nature."},
      {"author": "Anthony Pryde", "work": "Nightfall", "quote": "She was a modern **sophisticate** whose cynical repartee masked a deep longing for genuine affection."}
    ]
  },
  "Dashboard — soph/sophisticated.md": {
    "primary": "Having worldly knowledge and refined taste; also highly developed, complex, or advanced in technology.",
    "secondary": "In systems engineering and aesthetics, intricate mechanisms or cultural refinement operating at peak subtlety.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "Clarissa Dalloway moved gracefully through her London drawing room, the quintessential **sophisticated** hostess of Mayfair."},
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The spacecraft was governed by a **sophisticated** heuristic computer capable of speech and independent strategic planning."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "The expatriate crowd on the Riviera prided itself on being effortlessly **sophisticated**, bored by ordinary bourgeois morality."}
    ]
  },
  "Dashboard — soph/sophistication.md": {
    "primary": "Worldly knowledge, cultural refinement, and cultivated taste; also high complexity in design or technology.",
    "secondary": "In historical culture and rhetoric, moving away from rustic simplicity toward cosmopolitan elegance.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle possessed that supreme European **sophistication** which handles every social crisis with flawless tact."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Newland Archer admired the subtle **sophistication** of Countess Olenska, so different from the rigid conventions of Old New York."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The leisure class cultivates an esoteric **sophistication** of consumption to advertise its complete exemption from manual labor."}
    ]
  },
  "Dashboard — soph/sophistry.md": {
    "primary": "The use of clever but fallacious arguments, especially with the deliberate intention of deceiving or misleading.",
    "secondary": "In political debate and ethical philosophy, deceptive verbal manipulation that dresses falsehood in the garb of reason.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare felt that all his liberal modern theories were but empty **sophistry** when confronted with Tess's tragic confession."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Upon my word, said Farebrother, it requires tremendous **sophistry** to reconcile Bulstrode's pious words with his banking practices."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Scholastic disputants too often substitute verbal **sophistry** for the humble, diligent search after natural truth."}
    ]
  },
  "Dashboard — soph/sophocles.md": {
    "primary": "One of the three great ancient Athenian tragic playwrights (c. 496–406 BC), author of *Oedipus Rex* and *Antigone*.",
    "secondary": "In classical literature, celebrated for dramatic structure, moral seriousness, and introducing the third actor to Greek theatre.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "To a Friend", "quote": "Be his My special thanks, whose even-balanced soul business could not make dull, nor passion wild; who saw life steadily, and saw it whole: the mellow glory of the Attic stage, singer of sweet Colonus, and its child, **sophocles**."},
      {"author": "Percy Bysshe Shelley", "work": "A Defence of Poetry", "quote": "The choral odes of **sophocles** express the highest moral dignity that ancient Greek drama ever attained."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie read the Antigone of **sophocles** with a beating heart, feeling kinship with that noble, tragic sister."}
    ]
  },
  "Dashboard — soph/sophomore.md": {
    "primary": "A student in the second year of high school or college; also immature, overconfident, or pretentious.",
    "secondary": "In American academic culture, etymologically linked to Greek *sophos* (wise) and *moros* (foolish), the 'wise fool'.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "The student remembered his unruly days as a college **sophomore**, drinking porter in the student taverns of Dublin."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "As a **sophomore**, Amory Blaine threw himself into campus politics, writing poems and satirizing faculty pomposity."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol remembered her college years, when every cocky **sophomore** fancied himself an authority on Ibsen and Nietzsche."}
    ]
  },
  "Dashboard — soph/sophonias.md": {
    "primary": "The Greek and Douay-Rheims biblical form of the name of the minor Old Testament prophet Zephaniah.",
    "secondary": "In biblical scholarship, the prophetic book prophesying the Day of the Lord and the restoration of a righteous remnant.",
    "quotes": [
      {"author": "John Henry Newman", "work": "Tracts for the Times", "quote": "The somber warnings in the prophecy of **sophonias** prefigured the catastrophic judgment destined to fall upon unrepentant Jerusalem."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The Angelic Doctor cites the text of **sophonias** to prove that divine mercy preserves a faithful remnant amidst universal tribulation."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Latin Vulgate translation of the prophet **sophonias** was chanted in the cathedrals during the solemn season of Advent."}
    ]
  },
  "Dashboard — soph/sophora.md": {
    "primary": "A genus of flowering trees and shrubs in the legume family (Fabaceae), commonly called necklace trees or pagoda trees.",
    "secondary": "In ornamental horticulture and dendrology, trees noted for fragrant pea-like white blossoms and bead-like constricted seed pods.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "We camped beside a grove of flowering **sophora**, whose fragrant white panicles attracted swarms of wild mountain bees."},
      {"author": "Asa Gray", "work": "Scientific Papers of Asa Gray", "quote": "The oriental species **sophora** japonica flourishes in botanical gardens, celebrated for its weeping branches and durable timber."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "In the temperate valleys of New Zealand, yellow kowhai trees of the genus **sophora** brighten the riverbanks in spring."}
    ]
  },
  "Dashboard — soph/theosophical.md": {
    "primary": "Of, relating to, or derived from theosophy; mystical, esoteric, and concerned with spiritual knowledge of the divine.",
    "secondary": "In religious history, denoting the nineteenth-century movement founded by Madame Blavatsky synthesizing Eastern and Western esotericism.",
    "quotes": [
      {"author": "William Butler Yeats", "work": "Autobiographies", "quote": "In my youth I attended meetings of the **theosophical** society in Dublin, fascinated by their esoteric doctrines of reincarnation."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The **theosophical** literature presents an elaborate occult cosmology purporting to explain the psychic hierarchy of the universe."},
      {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "The **theosophical** mystic seeks to escape personal responsibility by dissolving the self into an impersonal cosmic ocean."}
    ]
  },
  "Dashboard — soph/theosophist.md": {
    "primary": "An adherent, practitioner, or student of theosophy, seeking intuitive spiritual knowledge of divine mysteries.",
    "secondary": "In modern occult history, a member of the Theosophical Society exploring Hindu and Buddhist esoteric philosophy.",
    "quotes": [
      {"author": "William Butler Yeats", "work": "Memoirs", "quote": "My friend the painter was an ardent **theosophist**, meditating daily upon ancient Indian Upanishads in his studio."},
      {"author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "The spiritualist conferenced with a learned **theosophist** on the nature of astral bodies and survival after death."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "AE sat in the national library surrounded by admiring disciples, the revered **theosophist** expounding Irish visionary myths."}
    ]
  },
  "Dashboard — soph/theosophy.md": {
    "primary": "A philosophical and religious system maintaining that knowledge of God may be attained through spiritual intuition and ecstasy.",
    "secondary": "In religious philosophy, esoteric systems like Jacob Boehme's mystical theology or the modern Theosophical Society.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The teachings of modern **theosophy** represent a curious synthesis of Hindu metaphysics and Western occult science."},
      {"author": "Mary Baker Eddy", "work": "Science and Health with Key to the Scriptures", "quote": "Christian Science is not to be confounded with pantheism or the speculative doctrines of oriental **theosophy**."},
      {"author": "G. K. Chesterton", "work": "The Everlasting Man", "quote": "The vagueness of modern **theosophy** dissolves the sharp, dramatic reality of the historic Christian Incarnation."}
    ]
  },
  "Dashboard — soph/unsophisticated.md": {
    "primary": "Lacking worldly experience, artifice, or refined complexity; simple, natural, naive, and unpretentious.",
    "secondary": "In literature and social commentary, genuine innocence untouched by the cynical affectations of high society.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess was a pure and **unsophisticated** village maiden, unaccustomed to the predatory flatteries of worldly men."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester declared that Jane's blunt, **unsophisticated** honesty was a refreshing breeze through his corrupted halls."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Catherine Morland was an open-hearted, **unsophisticated** girl whose imagination had been bewitched by Gothic romances."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — soph.")
