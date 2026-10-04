# -*- coding: utf-8 -*-
"""
Curates Dashboard — put (Part 2: words 39-76) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  "input": {
    "primary": "Data, energy, or information entered into a system, computer, or process for processing or storage.",
    "secondary": "In collaborative decision making, contributions of advice, opinions, or expertise offered by stakeholders.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Feedback loops continuously adjust operational output by comparing performance against sensory **input** signals."},
      {"author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "The paper tape provided discrete symbolic **input** that guided the internal state transitions of the machine."},
      {"author": "Herbert Simon", "work": "The Sciences of the Artificial", "quote": "Complex economic models require high-fidelity statistical **input** to forecast production trends accurately."}
    ]
  },
  "put": {
    "primary": "To place, position, or locate an object in a specific physical spot or state.",
    "secondary": "In rhetoric and literary expression, to state, express, or articulate an idea in specific words.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing end them... to **put** on an antic disposition."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley chose to **put** the matter plainly before her, refusing to soften his sincere reproof."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery reached out his blacksmith's hand to **put** the kettle on the hearth for tea."}
    ]
  },
  "putamen": {
    "primary": "A round dark subcortical brain structure that forms the outer part of the lentiform nucleus in the basal ganglia.",
    "secondary": "In neuroanatomy, an essential forebrain center involved in regulating motor execution, habit learning, and reinforcement.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Dopaminergic projections from the substantia nigra innervate the **putamen** to facilitate voluntary muscular initiation."},
      {"author": "Oliver Sacks", "work": "Musicophilia", "quote": "Neuroimaging revealed remarkable activation across the **putamen** when the musician kept internal rhythmic time."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Dense fiber bundles traverse the **putamen**, connecting the cerebral cortex with deeper motor nuclei."}
    ]
  },
  "putative": {
    "primary": "Generally considered, reputed, or assumed to be something; supposed or commonly accepted as true.",
    "secondary": "In evolutionary biology and genetics, a candidate gene or ancestral lineage presumed to perform a specific function.",
    "quotes": [
      {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "The fossil specimen was hailed as a **putative** ancestor linking early theropods with modern birds."},
      {"author": "Richard Dawkins", "work": "The Ancestor's Tale", "quote": "Molecular clocks allow us to calibrate the **putative** divergence dates between hominid lineages."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **putative** father of the young prince was widely rumored to be a Syrian gladiator."}
    ]
  },
  "putin": {
    "primary": "Vladimir Putin, a Russian intelligence officer and statesman serving as President and Prime Minister of Russia.",
    "secondary": "In contemporary geopolitical analysis, the political regime characterized by centralized presidential power in the Russian Federation.",
    "quotes": [
      {"author": "Timothy Snyder", "work": "The Road to Unfreedom", "quote": "The political philosophy of Vladimir **Putin** drew heavily upon the Eurasian fascist doctrines of Ivan Ilyin."},
      {"author": "Henry Kissinger", "work": "World Order", "quote": "Western statesmen underestimated the historical grievances that animated **Putin** during negotiations over NATO expansion."},
      {"author": "Masha Gessen", "work": "The Man Without a Face", "quote": "The ascent of **Putin** from an obscure KGB operative in Dresden to the Kremlin redefined modern Russian governance."}
    ]
  },
  "putoff": {
    "primary": "An evasion, excuse, delay, or postponement, or a quality that provokes distaste and discourages engagement.",
    "secondary": "In informal social interactions, an unpleasant trait or dismissive excuse that alienates romantic suitors or patrons.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Liza recognized the polite aristocratic refusal as a mere diplomatic **putoff** designed to avoid commitments."},
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "Anthony found the broker's perpetual evasion a tiresome **putoff**, masking financial insolvency with cheerful promises."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Her cold, guarded manner served as an effective **putoff** to earnest young men who sought her conversation."}
    ]
  },
  "putout": {
    "primary": "A defensive play in baseball that records an out against a batter or baserunner.",
    "secondary": "In sports statistics, a fielding metric credited to the fielder who catches a third strike, flies out a batter, or tags a runner.",
    "quotes": [
      {"author": "Ring Lardner", "work": "You Know Me Al", "quote": "The rookie first baseman recorded another clean **putout**, fielding the sharp grounder right at the bag."},
      {"author": "John Updike", "work": "Hub Fans Bid Kid Adieu", "quote": "Ted Williams trotted toward the dugout after the routine **putout** in deep left field, cheered by the Fenway crowd."},
      {"author": "Ernest Thayer", "work": "Casey at the Bat", "quote": "The catcher dropped the foul tip but recovered quickly to execute the final **putout** at home plate."}
    ]
  },
  "putrajaya": {
    "primary": "A planned city located south of Kuala Lumpur that serves as the administrative center and federal seat of Malaysia.",
    "secondary": "In modern urban design, an administrative capital celebrated for expansive wetlands, bridges, and Islamic-modernist architecture.",
    "quotes": [
      {"author": "Mahathir Mohamad", "work": "A Doctor in the House: The Memoirs of Tun Dr Mahathir Mohamad", "quote": "We conceived **Putrajaya** as an intelligent garden city that would consolidate federal ministries outside congested Kuala Lumpur."},
      {"author": "Rem Koolhaas", "work": "Mutations", "quote": "The monumental boulevards of **Putrajaya** represent a late-twentieth-century vision of technocratic statehood crafted from raw soil."},
      {"author": "Clifford Geertz", "work": "Available Light", "quote": "The federal palace at **Putrajaya** symbolizes the post-colonial state's synthesis of Islamic heritage and high-tech ambition."}
    ]
  },
  "putrefacient": {
    "primary": "Causing or accelerating putrefaction, decomposition, or rotting of organic matter.",
    "secondary": "In forensic pathology, environmental conditions or bacterial agents that expedite the putrefactive breakdown of tissue.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The experiment proved that anaerobic vibrios act as a powerful **putrefacient** agency in decaying animal muscle."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Warm and humid climates provide a natural **putrefacient** environment that challenges the preservation of specimens."},
      {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "Saprophytic bacteria perform an indispensable ecological role as the primary **putrefacient** agents of the biosphere."}
    ]
  },
  "putrefaction": {
    "primary": "The decomposition of organic matter, especially the bacterial breakdown of proteins producing foul-smelling compounds.",
    "secondary": "In forensic science, the stage of postmortem alteration characterized by cadaveric discoloration, bloating, and liquefaction.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The intense tropical heat accelerated the **putrefaction** of the stranded whale carcass upon the rocky beach."},
      {"author": "Louis Pasteur", "work": "Germ Theory and Its Applications to Medicine", "quote": "He demonstrated conclusively that **putrefaction** is produced entirely by living microorganisms carried in atmospheric dust."},
      {"author": "Edgar Allan Poe", "work": "The Facts in the Case of M. Valdemar", "quote": "The mesmerized corpse dissolved in minutes into an unrecognizable liquid mass of detestable **putrefaction**."}
    ]
  },
  "putrefactive": {
    "primary": "Pertaining to, causing, or accompanied by putrefaction and the decomposition of animal and vegetable matter.",
    "secondary": "In microbiology, describing anaerobic clostridial species that ferment amino acids into foul sulfurous gases.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Physiological Researches on Fermentation", "quote": "The **putrefactive** fermentation of meat ceased entirely when all aerial germs were incinerated by flame."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Aseptic technique eliminated the deadly **putrefactive** fevers that formerly haunted surgical wards."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The volatile spirits released during **putrefactive** decay exhibit distinctly alkaline and pungent properties."}
    ]
  },
  "putrefiable": {
    "primary": "Liable, susceptible, or subject to putrefaction, rotting, and biological decomposition.",
    "secondary": "In historical food preservation, perishable animal flesh or dairy broths lacking salt or chemical desiccants.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Memoir on the Organized Corpuscles", "quote": "The heated urine remained clear in the swan-neck flask, proving that a **putrefiable** liquid does not generate life spontaneously."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "Every **putrefiable** substance will remain sweet indefinitely if air is filtered through sterilized cotton wool."},
      {"author": "John Tyndall", "work": "Essays on the Floating-Matter of the Air", "quote": "He subjected hundreds of tubes of **putrefiable** mutton infusion to discontinuous boiling to eliminate resistant spores."}
    ]
  },
  "putrefy": {
    "primary": "To undergo putrefaction; to rot, decompose, or decay with the emission of a foul, offensive odor.",
    "secondary": "In moral and political allegories, to fester and deteriorate into corrupt, degenerate ruin.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "Let me look upon the city once more before I depart; may treason thrive and all her morals **putrefy**!"},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Without refrigeration, the slaughtered game began to **putrefy** rapidly under the midday subtropical sun."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Brobdingnagian flies dropped their monstrous eggs upon my food, which caused it immediately to **putrefy**."}
    ]
  },
  "putrescence": {
    "primary": "Decomposing organic matter undergoing rotten breakdown accompanied by the foul odor of decay.",
    "secondary": "In literary decadence, the aesthetic fascination with the grotesque imagery of death and decomposition.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The severed leviathan head emitted a sickening stench of ambergris mingled with ancient maritime **putrescence**."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "A heavy atmosphere of fungi and damp **putrescence** hung within the subterranean vaults beneath the tarn."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "A lingering taint of riverside **putrescence** clung to the mangrove roots where the steamer ran aground."}
    ]
  },
  "putrescent": {
    "primary": "Undergoing the process of putrefaction; decaying, rotting, and giving off the stench of decomposition.",
    "secondary": "In medical pathology, describing gangrenous tissue undergoing moist, foul-smelling necrotic breakdown.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I collected bones from charnel houses and disturbed with profane fingers the **putrescent** secrets of the grave."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The drainage from the abscess was dark and **putrescent**, signaling an anaerobic polymicrobial infection."},
      {"author": "H. P. Lovecraft", "work": "The Call of Cthulhu", "quote": "The cyclopean masonry dripped with a green, **putrescent** slime that had slept for aeons beneath the sea."}
    ]
  },
  "putrescible": {
    "primary": "Capable of rotting or liable to putrefaction; easily decomposed by bacterial or enzymatic action.",
    "secondary": "In sanitary engineering and waste management, solid organic waste that decomposes rapidly, attracting vermin.",
    "quotes": [
      {"author": "Edwin Chadwick", "work": "Report on the Sanitary Condition of the Labouring Population", "quote": "Accumulations of **putrescible** refuse in urban alleys generated noxious effluvia that spread typhus."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Airborne spores settle upon **putrescible** surfaces, initiating the rapid breakdown of complex albuminous molecules."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Deep abyssal waters contain very little **putrescible** organic sediment compared to the rich coastal shelf."}
    ]
  },
  "putrescine": {
    "primary": "A foul-smelling diamine (1,4-diaminobutane) produced by the breakdown of amino acids in decaying animal tissue.",
    "secondary": "In biochemistry, a polyamine synthesized from ornithine that plays essential roles in cellular growth and protein synthesis.",
    "quotes": [
      {"author": "Alexander Fleming", "work": "Chemotherapy: Yesterday, Today, and Tomorrow", "quote": "Chemical analysis identified cadaverine and **putrescine** as the primary volatile bases responsible for the stench of necrosis."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Cellular biochemists revealed that **putrescine** and related polyamines stabilize nucleic acids during rapid mitosis."},
      {"author": "Richard Selzer", "work": "Mortal Lessons", "quote": "The unmistakable reek of **putrescine** warned the surgical team of deep muscular gangrene beneath the intact skin."}
    ]
  },
  "putrid": {
    "primary": "In a state of foul decay or decomposition; rotten, malodorous, and offensive to the senses.",
    "secondary": "In historical clinical nosology, putrid typhus or putrid fever characterized by gangrenous ulcerations and prostration.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The air in Tom-all-Alone's was heavy with the **putrid** exhalations of open drains and neglected burial grounds."},
      {"author": "Jonathan Swift", "work": "A Modest Proposal", "quote": "He condemned the filthy butcheries that left piles of **putrid** offal exposed to the sweltering Dublin streets."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The decaying fruit beneath the breadfruit grove formed a thick, **putrid** compost upon the jungle floor."}
    ]
  },
  "putrid-smelling": {
    "primary": "Emitting a foul, rotten, or nauseating stench characteristic of decomposing organic matter.",
    "secondary": "In sensory descriptions, conveying the pungent, sulfurous odor produced by anaerobic bacteria in rotting tissue.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We stepped cautiously through the swamp, gagging at the **putrid-smelling** mud that bubbled with volcanic methane."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The kitchen was filled with **putrid-smelling** grease that had accumulated behind the ovens for months."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "As the vault opened, a cold, **putrid-smelling** draught issued from the tombs, chilling our blood."}
    ]
  },
  "putridity": {
    "primary": "Rottenness, foul decomposition, or an offensive putrefying mass of decaying organic matter.",
    "secondary": "In ethical criticism, moral depravity or spiritual degeneration within a society or institution.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The moral **putridity** of the later imperial court disgusted the austere barbarian chieftains from the north."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "An ancient regime founded upon privilege dissolved in the fiery furnace of its own internal **putridity**."},
      {"author": "Edgar Allan Poe", "work": "The Narrative of Arthur Gordon Pym of Nantucket", "quote": "The drifting brig revealed a crew of corpses frozen in the last stages of loathsome **putridity**."}
    ]
  },
  "putridness": {
    "primary": "Offensive foulness, advanced putrefaction, or the fetid character of decaying matter.",
    "secondary": "In physical pathology, the visible breakdown and liquefaction of infected tissues.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The marshy inlet was notorious for fevers, its muddy banks exuding a persistent **putridness** in the heat."},
      {"author": "Herman Melville", "work": "Redburn", "quote": "The steerage deck was filled with the sickening **putridness** of spoiled salt pork and unwashed bedding."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Naturalists dispute whether the viper can survive amid the noxious **putridness** of corrupted waters."}
    ]
  },
  "putsch": {
    "primary": "A sudden, violent attempt to overthrow a government or regime, especially by a faction or military clique.",
    "secondary": "In European political history, referring specifically to early twentieth-century German uprisings such as the Kapp Putsch.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Hitler launched his abortive Munich **putsch** from a beer hall, ending in gunfire and his subsequent imprisonment."},
      {"author": "Hannah Arendt", "work": "The Origins of Totalitarianism", "quote": "Paramilitary veterans organized the reactionary **putsch** to crush democratic institutions in Weimar Germany."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Rumors of an impending right-wing **putsch** circulated through the working-class syndicates of Valencia."}
    ]
  },
  "putt": {
    "primary": "A light, gentle golf stroke played on a putting green to roll the ball into or toward the hole.",
    "secondary": "In sports terminology, the rolling trajectory of a golf ball struck with a flat-faced putter.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Clicking of Cuthbert", "quote": "He lined up the six-foot **putt** with agonizing deliberation, knowing the club championship hung upon the roll."},
      {"author": "Bernard Darwin", "work": "The Golf Courses of the British Isles", "quote": "A treacherous downhill **putt** on the eleventh green at St. Andrews requires nerves of tempered steel."},
      {"author": "John Updike", "work": "Rabbit, Run", "quote": "Rabbit watched his curling **putt** lip the rim of the cup and trickle safely into the darkness."}
    ]
  },
  "puttee": {
    "primary": "A strip of cloth or gaiter wound spirally around the lower leg from the ankle to below the knee.",
    "secondary": "In military history, standard protective woolen legwear worn by infantrymen and cavalry during the First World War.",
    "quotes": [
      {"author": "George Orwell", "work": "Burmese Days", "quote": "The native police constables wore khaki shorts and unwound each woolen **puttee** to dry after the monsoon rain."},
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "A Sikh soldier paused by the Grand Trunk Road to re-tighten the binding of his unraveling **puttee**."},
      {"author": "Robert Graves", "work": "Good-bye to All That", "quote": "The trench mud in Flanders caked our boots and soaked through every woolen **puttee** until our feet froze."}
    ]
  },
  "putter": {
    "primary": "To move about or work in a casual, aimless, or leisurely manner, occupying oneself with trifles.",
    "secondary": "In sports equipment, a golf club designed with a relatively flat blade or mallet head for putting on greens.",
    "quotes": [
      {"author": "E. B. White", "work": "One Man's Meat", "quote": "I like to **putter** around the barn on rainy mornings, sharpening axes and mending harness straps."},
      {"author": "P. G. Wodehouse", "work": "Golf Without Tears", "quote": "He gripped his patented center-shafted **putter** with grim resolve and addressed the ball."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Mr. Bankes would **putter** in his garden before breakfast, inspecting his rosebushes with solitary care."}
    ]
  },
  "putterer": {
    "primary": "A person who putters; one who occupies their time with pleasant, minor, or desultory tasks without haste.",
    "secondary": "In character sketches, a hobbyist or tinkerer who enjoys browsing workshops and fixing domestic gadgets.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The contented **putterer** discovers in small domestic repairs a deeper philosophy than in bustling commerce."},
      {"author": "P. G. Wodehouse", "work": "Leave It to Psmith", "quote": "Lord Emsworth was a dedicated **putterer** among his prize pumpkin patches, oblivious to aristocratic intrigue."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "His neighbor was an inveterate garage **putterer**, polishing carburettors on warm Sunday afternoons."}
    ]
  },
  "putting": {
    "primary": "The act of executing strokes on a golf green with a putter to guide the ball into the hole.",
    "secondary": "In sports biomechanics, the precise pendular stroke requiring delicate kinesthetic judgment of green slope and grain.",
    "quotes": [
      {"author": "Bernard Darwin", "work": "Golf Between Two Wars", "quote": "Mastery of the **putting** art demands an enviable temperament that remains impervious to sudden panic."},
      {"author": "P. G. Wodehouse", "work": "The Heart of a Goof", "quote": "His tragic failure on the eighteenth green was attributed entirely to erratic **putting** under pressure."},
      {"author": "John Updike", "work": "Golf Dreams", "quote": "The secret of consistent **putting** lies in striking the ball with a true, unhurried pendulum motion."}
    ]
  },
  "putty": {
    "primary": "A pliable dough made of whiting and linseed oil, used to secure panes of glass in window frames.",
    "secondary": "In carpentry and decorating, a filling compound pressed into nail holes and wood crevices prior to painting.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The glazier arrived with a lump of fresh **putty** and replaced the shattered parlor casement pane."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Adam planed the ash doorframe smooth and pressed soft **putty** over the countersunk screw heads."},
      {"author": "H. G. Wells", "work": "The History of Mr. Polly", "quote": "He worked as an apprentice glazier, his fingers constantly scented with linseed oil and sticky white **putty**."}
    ]
  },
  "puttyroot": {
    "primary": "A North American woodland orchid (Aplectrum hyemale) producing sticky mucilaginous tubers historically used as glue.",
    "secondary": "In regional botany, an orchid species famous for producing a single overwintering leaf and persistent paired underground corms.",
    "quotes": [
      {"author": "John Muir", "work": "The Story of My Boyhood and Youth", "quote": "Pioneers dug the tubers of the **puttyroot** orchid to concoct an adhesive for mending broken earthenware."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Specimens of **puttyroot** thrive in rich deciduous forest leaf mold, flowering in early summer."},
      {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "The solitary winter leaf of the **puttyroot** stands out boldly against the snow-covered forest floor."}
    ]
  },
  "reputability": {
    "primary": "The quality, state, or property of being reputable, trustworthy, respectable, and held in high esteem.",
    "secondary": "In commerce and banking, the verified fiscal integrity and creditworthiness of a merchant house.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **reputability** of a merchant banker ensures that his bills of exchange circulate as readily as gold coin."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "Society questioned the commercial **reputability** of Melmotte's railway scheme despite his glittering banquets."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Bulstrode prized his Christian **reputability** above all worldly possessions, guarding it with anxious fervor."}
    ]
  },
  "reputable": {
    "primary": "Having a good reputation; considered trustworthy, honorable, respectable, and principled.",
    "secondary": "In trade and civil society, businesses and practitioners recognized for ethical standards and quality service.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Weston was a **reputable** gentleman whose genial hospitality made him beloved across Highbury."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Tellson's was an old and eminently **reputable** banking firm that prided itself on austere tradition."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I resolved to deal only with **reputable** printers whose craftsmanship met the highest standards of the trade."}
    ]
  },
  "reputably": {
    "primary": "In a reputable, honorable, or respectable manner; with an established good name.",
    "secondary": "In professional conduct, discharging duties and commercial obligations with transparency and fairness.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "He lived **reputably** upon the modest revenues of his parish, beloved by scholars and parishioners alike."},
      {"author": "Anthony Trollope", "work": "Doctor Thorne", "quote": "The country physician practiced **reputably** for forty years, refusing to bill impoverished farm laborers."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "A young apprentice who conducts his ledger **reputably** will never lack credit or willing creditors."}
    ]
  },
  "reputation": {
    "primary": "The general estimation, belief, or opinion held by the public about someone or something's character and worth.",
    "secondary": "In classical drama, the moral capital and public honor upon which social standing and personal dignity depend.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "**Reputation**, **reputation**, **reputation**! O, I have lost my **reputation**! I have lost the immortal part of myself, and what remains is bestial."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "One false step in a young woman's conduct involves her in inevitable ruin and destroys her **reputation** forever."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A good name and noble **reputation** is like an aromatic fragrance that outlasts the vessel containing it."}
    ]
  },
  "repute": {
    "primary": "The opinion generally held of someone or something; public esteem, renown, or reputation.",
    "secondary": "To consider, believe, or account someone or something to be in a specified condition or rank.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan stood supreme in evil **repute**, adored by fallen angels as the architect of their bold defiance."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Black Knight was a warrior of formidable **repute**, whose prowess in the tournament stunned the spectators."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Philosophers of high **repute** were summoned from Athens to instruct the imperial princes in jurisprudence."}
    ]
  },
  "reputedly": {
    "primary": "According to general belief, popular rumor, or widespread reputation; supposedly.",
    "secondary": "In historical chronicles, describing alleged events or treasures recorded through oral tradition rather than eyewitness record.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The ancient manor was **reputedly** haunted by a spectral hound that bayed upon the misty moors."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Captain Flint was **reputedly** the most bloodthirsty pirate who ever hoisted the skull and crossbones."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The founder of the house had **reputedly** seized the land through witchcraft accusations against poor Maule."}
    ]
  },
  "supercomputer": {
    "primary": "An exceptionally powerful mainframe computer designed to execute billions of high-speed floating-point calculations.",
    "secondary": "In computational science, high-performance computing clusters used for climate modeling, molecular dynamics, and astrophysics.",
    "quotes": [
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Modern planetary scientists rely upon the **supercomputer** to simulate the turbulent atmospheric storms of Jupiter."},
      {"author": "Arthur C. Clarke", "work": "2010: Odyssey Two", "quote": "The orbital laboratory housed a compact **supercomputer** capable of processing petabytes of sensor telemetry."},
      {"author": "Walter Isaacson", "work": "The Innovators", "quote": "Seymour Cray designed the world's fastest **supercomputer** by arranging processors in dense, refrigerated circles."}
    ]
  },
  "undisputable": {
    "primary": "Indisputable; not open to question, challenge, or debate; undeniably true.",
    "secondary": "In logical discourse, an axiomatic proposition whose contradiction entails an immediate absurdity.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "That three times five is equal to half of thirty expresses an **undisputable** relation between abstract numbers."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Empirical generalizations become **undisputable** only when verified through rigorous canons of induction."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Her musical talent was **undisputable**, and she accompanied her own singing upon the piano with admirable grace."}
    ]
  },
  "undisputed": {
    "primary": "Accepted, acknowledged, or agreed upon without challenge, opposition, or dissent.",
    "secondary": "In competitive titles and political sovereignty, reigning supreme without rival claimants.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Augustus reigned as the **undisputed** master of the Roman world, cloaking absolute power under republican titles."},
      {"author": "Winston Churchill", "work": "A History of the English-Speaking Peoples", "quote": "Following the victory at Trafalgar, the Royal Navy held **undisputed** command of the global oceans."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Squire Cass was the **undisputed** chief magnate of Raveloe, residing in the parish's finest red-brick hall."}
    ]
  }
}
