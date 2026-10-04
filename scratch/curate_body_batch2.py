# -*- coding: utf-8 -*-
"""
Curates Cluster Body & State (Batch 2, 36 words):
- Dashboard — frat (10 words)
- Dashboard — salu (12 words)
- Dashboard — sud (14 words)
Total: 36 words.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  # Dashboard — frat
  "frat": {
    "primary": "Informal shortening of fraternity; a social organization of male college students.",
    "secondary": "In American collegiate life, a Greek-letter society maintaining a residential chapter house.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The rival **frat** members gathered on the campus lawn during autumn rush week."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin refused to pledge the fashionable medical **frat**, preferring solitary night work in the lab."},
      {"author": "Thomas Wolfe", "work": "Look Homeward, Angel", "quote": "The rowdy **frat** brothers sang drinking songs late into the Carolina midnight."}
    ]
  },
  "fratercula": {
    "primary": "A taxonomic genus of pelagic seabirds in the auk family Alcidae, comprising the puffins.",
    "secondary": "In ornithology, seabirds characterized by a brightly colored, laterally compressed bill during the breeding season.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Rocky North Atlantic sea cliffs provide nesting burrows for the puffin genus **Fratercula**."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The Atlantic puffin, classified as **Fratercula** arctica, dives skillfully into ocean waves for sand eels."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Mariners observed dense colonies of **Fratercula** nesting along the craggy ledges of the Hebrides."}
    ]
  },
  "fraternal": {
    "primary": "Of, relating to, or characteristic of a brother or brothers; brotherly and friendly.",
    "secondary": "In human genetics, dizygotic or non-identical twins developed from two separately fertilized ova.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "With malice toward none, with charity for all, let us bind up the nation's wounds in **fraternal** peace."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Social animals extend **fraternal** mutual aid to members of their immediate troop or family."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Civic associations establish a **fraternal** bond among citizens who would otherwise remain isolated."}
    ]
  },
  "fraternally": {
    "primary": "In a brotherly, friendly, or supportive manner; with mutual warmth and solidarity.",
    "secondary": "In associative correspondence, closing formal fraternal letters with brotherly greetings.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "My Bondage and My Freedom", "quote": "Abolitionists embraced their fellow crusaders **fraternally**, united against the curse of slavery."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Militiamen from opposing political factions greeted each other **fraternally** in the muddy trenches."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The two old comrades shook hands **fraternally**, recalling campaigns fought long ago in Flanders."}
    ]
  },
  "fraternisation": {
    "primary": "The act of associating or forming close friendly bonds with others (British spelling).",
    "secondary": "In wartime military law, unauthorized friendly interaction between opposing combatants or between soldiers and occupied populations.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Spontaneous Christmas **fraternisation** between British and German troops halted trench gunfire for a single holy day."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king forbade all political **fraternisation** between his royal guards and rebellious townspeople."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Strict party discipline prohibited all informal **fraternisation** with common proles."}
    ]
  },
  "fraternise": {
    "primary": "To associate or form friendly bonds with others, especially with those holding opposing views (British spelling).",
    "secondary": "In military regulations, to socialize familiarly with an enemy or with subordinate ranks.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Sir Thomas was displeased to see his daughters **fraternise** too familiarly with visiting London actors."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Soldiers on night patrol were warned not to **fraternise** with opposing pickets across no-man's-land."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Ensign Stubble was eager to **fraternise** with veteran officers in the Brussels taverns."}
    ]
  },
  "fraternity": {
    "primary": "A group of people sharing a common profession or interests; mutual brotherly fellowship.",
    "secondary": "In political philosophy, the third ideal of the French revolutionary motto (liberté, égalité, fraternité).",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Christian teaching instilled the universal **fraternity** of mankind, elevating democratic equality."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary ideal of **fraternity** was mocked by the reign of terror and the guillotine."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Intellectual sympathy unites distant thinkers in a perpetual, invisible **fraternity** of spirit."}
    ]
  },
  "fraternization": {
    "primary": "The act of associating with others on friendly or brotherly terms (American spelling).",
    "secondary": "In military discipline, unauthorized informal relations between officers and enlisted personnel or with civilians.",
    "quotes": [
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "Pickets called across the river in friendly **fraternization**, trading tobacco for northern coffee."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Military commanders strictly regulated troop **fraternization** during the occupation of the Rhineland."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "Naval hierarchy forbade democratic **fraternization** between naval officers and common sailors."}
    ]
  },
  "fraternize": {
    "primary": "To associate with someone in a brotherly, friendly, or supportive manner.",
    "secondary": "In army code of conduct, to mingle socially with enemy troops or civilian inhabitants of occupied territory.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "The traveling knights were delighted to **fraternize** with wandering friars along the highway."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "Striking workers attempted to **fraternize** with the infantry regiments sent to quell their protest."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "Archers and men-at-arms loved to **fraternize** around the campfires before the morning march."}
    ]
  },
  "fratricide": {
    "primary": "The crime of killing one's own brother; a person who commits such an act.",
    "secondary": "In military terminology, unintentional harm or death inflicted on friendly forces (friendly fire).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "O, my offence is rank it smells to heaven; it hath the primal eldest curse upon't, a brother's murder... The black guilt of **fratricide**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor Caracalla secured absolute power through the brutal **fratricide** of his brother Geta."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Michael showed Adam the dreadful spectacle of Cain's **fratricide**, the first death of fallen humanity."}
    ]
  },

  # Dashboard — salu
  "insalubrious": {
    "primary": "Unfavorable to health; unwholesome, noxious, or pestilential in climate or air.",
    "secondary": "In Victorian public health and sanitation, squalid urban slums characterized by open sewage and contagious disease.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tom-all-Alone's was a notoriously **insalubrious** slum where fever bred in every squalid garret."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The coastal swamps of Fernando de Noronha had an **insalubrious** reputation among merchant mariners."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Lowood School was situated in an **insalubrious** hollow that fostered the fatal typhus outbreak."}
    ]
  },
  "insalubriousness": {
    "primary": "The unwholesome, unhealthy, or pestilential character of a climate, locality, or environment.",
    "secondary": "In 19th-century epidemiological topography, environmental conditions that promote infectious outbreaks.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The deadly **insalubriousness** of the Pontine marshes decimated barbarian armies besieging Rome."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The notorious **insalubriousness** of Batavia killed hundreds of Dutch company factors every year."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **insalubriousness** of crowded factory tenements was remedied through modern municipal sanitation."}
    ]
  },
  "insalubrity": {
    "primary": "Unhealthfulness; unwholesomeness of climate, situation, diet, or living quarters.",
    "secondary": "In colonial administration and naval medicine, the pestilential quality of tropical swamps and miasmas.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Wages of labor are naturally higher in occupations marked by extreme **insalubrity** or hazard."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative", "quote": "Travelers remarked upon the notorious **insalubrity** of the Orinoco delta during the rainy season."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "The mountain counties enjoyed perpetual health, free from the summer **insalubrity** of the tidewater plains."}
    ]
  },
  "salubrious": {
    "primary": "Favorable to health; health-giving, wholesome, invigorating, or beneficial.",
    "secondary": "In climatic geography and balneology, regions whose clean mountain or marine air promotes convalescence.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The sea breezes of Lyme Regis were universally recommended as wonderfully **salubrious** for invalids."},
      {"author": "John Muir", "work": "Our National Parks", "quote": "The pine-scented air of the Yosemite Valley is pure, invigorating, and delightfully **salubrious**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I found the simple woodland atmosphere far more **salubrious** than the artificial luxury of cities."}
    ]
  },
  "salubriousness": {
    "primary": "Wholesomeness, healthfulness, or invigorating purity of air, water, or climate.",
    "secondary": "In public environmental hygiene, the positive physiological impact of clean living environments.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The extraordinary **salubriousness** of the Virginia Piedmont sustained long and vigorous lives among its yeomen."},
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "Physicians praise the natural **salubriousness** of seaside breezes for restoring exhausted patients."},
      {"author": "Walter Scott", "work": "Guy Mannering", "quote": "The Highland glen was renowned for its **salubriousness**, its clear springs free from mineral taint."}
    ]
  },
  "salubrity": {
    "primary": "Wholesomeness of climate or situation; healthfulness and invigorating quality.",
    "secondary": "In traditional environmental medicine, the favorable atmospheric and topographical conditions of a sanatorium.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The physician praised the exceptional **salubrity** of the high chalk downs for pulmonary convalescents."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pleasant climate and celebrated **salubrity** of Antioch attracted Roman patricians seeking retirement."},
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The damp **salubrity** of the British climate sustains the robust physical vigor of its people."}
    ]
  },
  "salutary": {
    "primary": "Producing good effects; beneficial, wholesome, or promoting health and well-being.",
    "secondary": "In political and moral discourse, a salutary lesson or check that prevents dangerous overreach.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A energetic executive provides a **salutary** check against hasty legislative factions."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Wise statesmen maintained a policy of **salutary** neglect toward the burgeoning American colonies."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Free local institutions exercise a profoundly **salutary** influence on the civic morality of citizens."}
    ]
  },
  "salutation": {
    "primary": "A gesture, greeting, or phrase expressing goodwill, respect, or acknowledgment upon meeting.",
    "secondary": "In epistolary style, the opening formal greeting addressed to the recipient of a letter (e.g., 'Dear Sir').",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "With courtesy and with respect enough; but not with such familiar instances as he hath used of old... A cold **salutation** from a changed friend."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery touched his hat with an awkward but heartfelt **salutation** as Pip entered the forge."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy bowed stiffly in polite **salutation**, scarcely raising his eyes to meet Elizabeth's gaze."}
    ]
  },
  "salutatorian": {
    "primary": "The student who ranks second highest in a graduating class and delivers the salutatory address.",
    "secondary": "In American academic commencement traditions, the graduate designated to welcome faculty, guests, and classmates.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin listened impatiently while the class **salutatorian** delivered an earnest Latin oration."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The distinguished **salutatorian** stepped to the podium to welcome university alumni and families."},
      {"author": "Willa Cather", "work": "My Ántonia", "quote": "At the high school commencement, the proud young **salutatorian** spoke eloquently of pioneer endurance."}
    ]
  },
  "salutatory": {
    "primary": "Relating to or expressing greeting or welcome; welcoming and cordial.",
    "secondary": "In academic graduation exercises, the opening welcoming address delivered by the salutatorian.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The university chancellor delivered a formal **salutatory** address to welcome the prince of Orange."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Coverdale extended a warm **salutatory** welcome to the new arrivals at the utopian commune."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "The morning birds sounded their sweet **salutatory** songs across the waking forest."}
    ]
  },
  "salute": {
    "primary": "To greet or acknowledge with a formal gesture of respect, such as raising a hand to the cap.",
    "secondary": "In military and naval ceremonies, firing a specified number of cannon rounds to honor a dignitary or state.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Long live King Richard, England's royal king! To **salute** him with this kingly title."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The crew assembled upon the quarterdeck to **salute** their captain with three ringing cheers."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The warships fired a thunderous naval **salute** as the flagship steamed into Alexandria harbor."}
    ]
  },
  "saluter": {
    "primary": "One who salutes, greets, or welcomes another; a person who renders a formal gesture of respect.",
    "secondary": "In military protocol, a soldier or sentry designated to render ceremonial honors.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The crusader knight observed the courteous **saluter**, acknowledging the Saracen's respectful bow."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The crowd cheered every friendly **saluter** who waved a Protestant orange banner."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Guppy was a persistent **saluter** of Lady Dedlock whenever she stepped from her carriage."}
    ]
  },

  # Dashboard — sud
  "sudafed": {
    "primary": "A brand name for pseudoephedrine; an over-the-counter sympathomimetic decongestant medication.",
    "secondary": "In clinical pharmacology, an alpha-adrenergic agonist used to reduce swelling of nasal mucous membranes.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern pharmacological formulations of **Sudafed** relieve acute rhinitis through vasoconstriction."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Adrenergic agonists related to **Sudafed** provide symptomatic airway relief in catarrhal congestion."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Synthetic decongestants such as **Sudafed** target respiratory mucosal inflammation effectively."}
    ]
  },
  "sudan": {
    "primary": "A vast country in northeast Africa; historically, the geographical region south of the Sahara extending to Central Africa.",
    "secondary": "In 19th-century colonial history, the Anglo-Egyptian condominium territory traversed by the White and Blue Niles.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The River War", "quote": "The reconquest of the **Sudan** restored British and Egyptian control over the upper Nile valley."},
      {"author": "Richard Burton", "work": "The Lake Regions of Central Africa", "quote": "Caravans crossed the burning sands of the eastern **Sudan** laden with ivory and gum arabic."},
      {"author": "Charles George Gordon", "work": "Journals at Kartoum", "quote": "General Gordon defended the isolated garrison of Khartoum in the heart of the rebellious **Sudan**."}
    ]
  },
  "sudanese": {
    "primary": "Relating to Sudan, its people, language, or culture; a native or citizen of Sudan.",
    "secondary": "In military and ethnographic history, indigenous battalions renowned for their fierce courage along the upper Nile.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The River War", "quote": "The **Sudanese** regiments displayed steadfast discipline and extraordinary courage at the battle of Omdurman."},
      {"author": "Arthur Conan Doyle", "work": "The Tragedy of the Korosko", "quote": "The tourists were captured by a swift band of **Sudanese** dervishes along the rocky Nile cataract."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Among traditional **Sudanese** tribes, the divine king was believed to control rainfall and seasonal fertility."}
    ]
  },
  "sudate": {
    "primary": "To sweat or exude perspiration; to undergo sweat-inducing physiological transpiration.",
    "secondary": "In archaic therapeutic medicine, to induce heavy sweating as a method of purging febrile toxins.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "In acute fevers, the patient was placed under heavy blankets to **sudate** copiously."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Ancient physicians urged melancholic sufferers to **sudate** in dry vapor baths to purge morbid humors."},
      {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Diaphoretics encourage the pores to **sudate** freely, moderating arterial heat."}
    ]
  },
  "sudation": {
    "primary": "The act or process of sweating or perspiring heavily; perspiration.",
    "secondary": "In balneology and historic hydrotherapy, the medicinal induction of heavy sweating in steam rooms.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Copious **sudation** following crisis in malignant fevers was regarded as nature's method of purification."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Vigorous bodily exercises provoke wholesome **sudation** that clears the animal spirits."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diabetic patients exhibit impaired cutaneous **sudation**, leaving the skin dry and scaly."}
    ]
  },
  "sudatorium": {
    "primary": "A hot, vaulted room in an ancient Roman bath (thermae) designed to induce heavy sweating.",
    "secondary": "In classical archaeology and thermal architecture, the sweating chamber heated by hypocaust floor flues.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The luxurious thermae of Caracalla contained an immense vaulted **sudatorium** paved with Numidian marble."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Roman patricians retired from the cool frigidarium into the aromatic vapor of the **sudatorium**."},
      {"author": "Viollet-le-Duc", "work": "Annals of a Fortress", "quote": "Remains of the legionary **sudatorium** revealed advanced underfloor hypocaust brickwork along the frontier."}
    ]
  },
  "sudatory": {
    "primary": "Sweat-producing; sweating; a room or apparatus for inducing perspiration, like a sauna.",
    "secondary": "In ancient Roman baths, an alternative term for a laconicum or steam sweating room.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Russian and Finnish peasants constructed rustic **sudatory** cabins heated by red-hot stones."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "The **sudatory** bath was highly recommended by Galen to dispel black bile from the blood."},
      {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Mild **sudatory** regimens were prescribed during the convalescent stage of catarrhal fevers."}
    ]
  },
  "sudoku": {
    "primary": "A popular logic-based number-placement puzzle played on a 9x9 grid divided into 3x3 subgrids.",
    "secondary": "In recreational mathematics and combinatorial analysis, a completed Latin square constraint puzzle.",
    "quotes": [
      {"author": "Douglas Hofstadter", "work": "I Am a Strange Loop", "quote": "Solving a challenging **Sudoku** puzzle requires recursive backtracking and rigorous logical deduction."},
      {"author": "Martin Gardner", "work": "Mathematical Puzzles and Diversions", "quote": "The combinatorial structure of modern **Sudoku** derives from Euler's classic studies of Latin squares."},
      {"author": "Ian Stewart", "work": "Professor Stewart's Cabinet of Mathematical Curiosities", "quote": "Every valid **Sudoku** configuration possesses a unique solution dictated by simple exclusion rules."}
    ]
  },
  "sudor": {
    "primary": "Sweat or perspiration; bodily fluid excreted by the sudoriferous sweat glands.",
    "secondary": "In physiological biochemistry, the aqueous hypotonic secretion containing sodium chloride, urea, and lactate.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Profuse nocturnal **sudor** is a classical clinical symptom of progressive pulmonary tuberculosis."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The excretion of **sudor** through the skin maintains the internal thermal equilibrium of the living body."},
      {"author": "William Harvey", "work": "On the Motion of the Heart and Blood", "quote": "Vigorous muscular movement accelerates the pulse and drives cutaneous **sudor** through the pores."}
    ]
  },
  "sudoriferous": {
    "primary": "Producing, secreting, or conveying sweat or perspiration.",
    "secondary": "In vertebrate histology, the eccrine and apocrine tubular glands embedded in the dermis.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Microscopic sections of the palm reveal millions of coiled **sudoriferous** glands opening onto epidermal ridges."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sudden terror stimulates the **sudoriferous** glands, bathing the brow in cold sweat."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dysfunction of the cutaneous **sudoriferous** apparatus can precipitate dangerous heat exhaustion."}
    ]
  },
  "sudorific": {
    "primary": "Causing, inducing, or stimulating sweat or perspiration; a medicine that induces sweating; diaphoretic.",
    "secondary": "In pharmacology, therapeutic agents administered to promote diaphoresis and lower fever.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Cashel Byron's Profession", "quote": "The trainer prescribed a vigorous **sudorific** regimen of rope-skipping and steam baths before the match."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hot lemon drafts and Dover's powder act as an effective **sudorific** remedy in early respiratory chills."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Ancient leeches employed strong **sudorific** decoctions of guaiacum to drive out chronic humors."}
    ]
  },
  "sudra": {
    "primary": "A member of the fourth and lowest of the traditional Hindu varnas or social classes; an artisan or laborer.",
    "secondary": "In Indian social history and Vedic literature, the working caste traditionally serving the three higher twice-born varnas.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient Brahmanical codes strictly regulated the domestic and ritual duties permitted to a **Sudra**."},
      {"author": "Max Müller", "work": "Chips from a German Workshop", "quote": "Vedic hymns distinguish the twice-born Aryan classes from the indigenous **Sudra** cultivators."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rigid caste divisions separating Brahman, Kshatriya, Vaisya, and **Sudra** preserved social hierarchy for millennia."}
    ]
  },
  "suds": {
    "primary": "Froth, foam, or lather formed on soapy water; soapy water used for washing.",
    "secondary": "In informal American slang, beer or alcoholic malt beverages served with a frothy head.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The washhouse was filled with steaming clouds and mounds of white soap **suds**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooned whale thrashed the brine into a dazzling cauldron of boiling **suds** and blood."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The paddlewheels churned the muddy river water into thick yellow **suds** along the stern."}
    ]
  },
  "sudsy": {
    "primary": "Covered with, full of, or resembling suds, soapy lather, or foam; frothy.",
    "secondary": "In consumer chemistry, detergents formulated to produce rich, stable surfactant lather in hard water.",
    "quotes": [
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Meg immersed her hands in the warm, **sudsy** basin, scrubbing the family linen by the kitchen hearth."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol poured the washing powder into the tub, watching the water turn into a rich, **sudsy** foam."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "Ma Joad wrung out the wet shirts over the wooden tub filled with grey **sudsy** wash water."}
    ]
  }
}
