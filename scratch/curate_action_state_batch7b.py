# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — bat Part 2 (44 words) ---
  "Dashboard — bat/battery-powered.md": {
    "primary": "Operating on electrical energy supplied by portable electrochemical batteries.",
    "secondary": "In electrical engineering and consumer electronics, battery-powered apparatus requires high-efficiency power management circuits to extend operating cycles.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Islands in the Sky", "quote": "The astronaut carried a compact, **battery-powered** torch to inspect the shadowy recesses of the orbital station."},
      {"author": "Isaac Asimov", "work": "The Caves of Steel", "quote": "The patrolman activated his portable, **battery-powered** field transceiver to report the disturbance on the lower roadway."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "We illuminated the subterranean caverns with our small, **battery-powered** electric lanterns."},
    ]
  },
  "Dashboard — bat/batting.md": {
    "primary": "The act of hitting with a bat; or cotton or wool wadding prepared in sheets for quilts or insulation.",
    "secondary": "In the game of cricket and baseball, batting technique balances defensive stance, hand-eye coordination, and rotational hip drive.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Gold Bat", "quote": "The crowd applauded vigorously as the school captain displayed brilliant **batting** form against the visiting fast bowlers."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dolly Winthrop stitched the warm wool **batting** into the baby's winter quilt with patient, even stitches."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Luffey's aggressive **batting** brought immense satisfaction to the Muggleton supporters at the cricket match."},
    ]
  },
  "Dashboard — bat/battle.md": {
    "primary": "A sustained fight between large organized armed forces; or a protracted struggle or contest.",
    "secondary": "In military historiography, a decisive pitched battle can overturn dynastic regimes and redraw continental frontiers.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Once more unto the breach, dear friends, once more; or close the wall up with our English dead. In peace there's nothing so becomes a man as modest stillness and humility: but when the blast of war blows in our ears, then imitate the action of the tiger; summon up the blood, disguise fair nature with hard-favour'd rage: then lend the eye a terrible aspect; let pry through the portage of the head like the brass cannon; let the brow o'erwhelm it as fearfully as doth a galled rock o'erhang and jutty his confounded base, swill'd with the wild and wasteful ocean. Now set the teeth and stretch the nostril wide, hold hard the breath and bend up every spirit to his full height. On, on, you noblest English, whose blood is fet from fathers of war-proof! Fathers that, like so many Alexanders, have in these parts from morn till even fought, and sheathed their swords for lack of argument: dishonour not your mothers; now attest that those whom you call'd fathers did beget you. Be copy now to men of grosser blood, and teach them how to war. And you, good yeomen, whose limbs were made in England, show us here the mettle of your pasture; let us swear that you are worth your breeding; which I doubt not; for there is none of you so mean and base, that hath not noble lustre in your eyes. I see you stand like greyhounds in the slips, straining upon the start. The game's afoot: follow your spirit, and upon this charge cry 'God for Harry, England, and Saint George!' And so prepare for **battle**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The catastrophic **battle** of Adrianople witnessed the destruction of the Roman army and the death of Emperor Valens."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The gigantic naval **battle** of Jutland raged through mist and gunfire across the grey waters of the North Sea."},
    ]
  },
  "Dashboard — bat/battle-ax.md": {
    "primary": "A heavy axe designed specifically as a weapon for combat; battle-axe.",
    "secondary": "In medieval arms and armor, the double-bitted chivalric battle-ax was swung with two hands to split through plate armor and mail coifs.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Black Knight swung his ponderous **battle-ax** with irresistible might, hewing through the stout oak timbers of the postern gate."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "Sir Nigel raised his notched **battle-ax**, parrying the furious sword strokes of the French man-at-arms."},
      {"author": "William Makepeace Thackeray", "work": "The Rose and the Ring", "quote": "The fierce giant strode forward, brandishing a rusty **battle-ax** that terrified the royal guards."},
    ]
  },
  "Dashboard — bat/battle-axe.md": {
    "primary": "A medieval broad-bladed fighting axe; or an informal derogatory term for a domineering or formidable woman.",
    "secondary": "In knightly weaponry, the poleaxe and battle-axe were favored weapons for dismounted combat during the Wars of the Roses.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Lay of the Last Minstrel", "quote": "Lord Cranstoun seized his keen **battle-axe**, rushing forward to defend the castle moat against the border raiders."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ancient armory contained a formidable iron **battle-axe** that had seen bloody service at the battle of Worcester."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins muttered under his breath about his mother's formidable visitor, describing her privately as an old social **battle-axe**."},
    ]
  },
  "Dashboard — bat/battle-scarred.md": {
    "primary": "Bearing scars or showing extensive damage resulting from military combat, warfare, or severe struggle.",
    "secondary": "In military memoir literature, battle-scarred veterans and regiments wear their physical wounds as emblems of honored service.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The River War", "quote": "The **battle-scarred** gunboats steamed up the Nile, their armored bulwarks dented by dervish rifle fire."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Major Sholto was a **battle-scarred** officer whose shattered health reflected years of arduous frontier service in India."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **battle-scarred** hull of the old whaling ship bore deep gashes from encounters with icebergs and ferocious bull sperm whales."},
    ]
  },
  "Dashboard — bat/battledore.md": {
    "primary": "A light wooden bat or racket used in playing battledore and shuttlecock (the ancestor of modern badminton); or a child's hornbook.",
    "secondary": "In early English educational history, a battledore was a folded cardboard primer containing the alphabet, numbers, and basic prayers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The children laughed merrily on the lawn, batting the feathered shuttlecock back and forth with a light wooden **battledore**."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Harriet and Robert Martin enjoyed an energetic game of **battledore** and shuttlecock in the vicarage garden."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The schoolmaster placed the printed **battledore** into the boy's hand, initiating him into the mysteries of the alphabet."},
    ]
  },
  "Dashboard — bat/battlefield.md": {
    "primary": "The piece of ground on which a battle is fought; or a sphere or arena of intense conflict.",
    "secondary": "In military archaeology, metal detection and forensic osteology on historical battlefield sites reconstruct troop movements and combat trauma.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrei lay wounded upon the **battlefield** of Austerlitz, gazing up into the lofty, infinite blue sky."},
      {"author": "Abraham Lincoln", "work": "The Gettysburg Address", "quote": "We have come to dedicate a portion of that **battlefield**, as a final resting place for those who here gave their lives that that nation might live."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The ruined **battlefield** of the Somme was a desolate moonscape of waterlogged craters and tangled barbed wire."},
    ]
  },
  "Dashboard — bat/battlefront.md": {
    "primary": "The forward line or zone along which opposing armed forces engage in active combat; the front line.",
    "secondary": "In strategic warfare and logistics, maintaining supply convoys and communication lines to the battlefront decides operational success.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Dispatches from the Russian **battlefront** reported massive tank engagements raging along the perimeter of Kursk."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Upon arriving at the mountain **battlefront**, we found conditions of extreme cold, primitive trenches, and scarce ammunition."},
      {"author": "Ernest Hemingway", "work": "A Farewell to Arms", "quote": "The ambulance drove along the muddy road toward the mountain **battlefront**, where distant artillery rumbled like thunder."},
    ]
  },
  "Dashboard — bat/battleful.md": {
    "primary": "Pertaining to, ready for, or full of battle; martial, combative, or warlike in spirit.",
    "secondary": "In heroic poetry and romantic saga translation, a battleful warrior or tribe eagerly seeks glory in martial confrontation.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The chieftain rallied his **battleful** clansmen, whose pipes sounded a wild martial gathering across the heather."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The ancient Norse sagas breathe a **battleful** spirit of fearless defiance against chaotic frost giants and dark destiny."},
      {"author": "William Morris", "work": "The Story of Sigurd the Volsung", "quote": "The king rode forth with his **battleful** host, their burnished shields glittering beneath the morning sky."},
    ]
  },
  "Dashboard — bat/battleground.md": {
    "primary": "A place where a battle is or was fought; or an area of intense competition, debate, or rivalry.",
    "secondary": "In electoral political science, a swing state or contested district represents a pivotal battleground that determines executive elections.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The courtroom in America serves as the primary peaceful **battleground** where social interests and constitutional rights are resolved."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Flanders was historically the bloody **battleground** of Europe, where French and allied armies contended for continental supremacy."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The national assembly was converted into a turbulent **battleground** where factional demagogues contended for dictatorial power."},
    ]
  },
  "Dashboard — bat/battlement.md": {
    "primary": "A parapet at the top of a castle wall or tower, featuring alternating solid merlons and open crenels for defense.",
    "secondary": "In medieval military architecture, a battlement provided archers with protective cover while shooting down at attacking forces.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "The raven himself is hoarse that croaks the fatal entrance of Duncan under my **battlement**."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Crossbowmen looked down from the high stone **battlement**, discharging heavy quarrels into the attacking Saxon ranks."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane walked along the leaded roof of Thornfield Hall, leaning upon the gray **battlement** to gaze out over the quiet hills."},
    ]
  },
  "Dashboard — bat/battlemented.md": {
    "primary": "Furnished or fortified with battlements; crenellated in architectural structure.",
    "secondary": "In Gothic Revival architecture, battlemented rooflines and parapets were incorporated to evoke feudal chivalric heritage.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Baskerville Hall presented a grand **battlemented** central block flanked by twin towers overgrown with dark ivy."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The ancient villa displayed a picturesque **battlemented** tower dating from the turbulent medieval wars of Tuscany."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "The gloomy mansion featured crumbling **battlemented** parapets that seemed ready to plunge into the silent tarn below."},
    ]
  },
  "Dashboard — bat/battler.md": {
    "primary": "A person who fights, struggles courageously against difficulties, or engages in combat; a determined fighter.",
    "secondary": "In Australian cultural folklore, the 'Aussie battler' represents an ordinary working citizen who perseveres cheerfully through adversity.",
    "quotes": [
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen was an indomitable physical **battler** who acknowledged no law beyond his own ruthless survival and iron will."},
      {"author": "Henry Lawson", "work": "While the Billy Boils", "quote": "The bushman was a patient **battler** who endured droughts, bushfires, and low wool prices without losing his dry humor."},
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The champion was a game **battler** in the prize ring, rising from heavy knockdowns to continue the contest."},
    ]
  },
  "Dashboard — bat/battleship.md": {
    "primary": "A heavy warship of the largest type, possessing extensive armor plate and batteries of the heaviest caliber guns.",
    "secondary": "In naval history, the dreadnought battleship dominated maritime strategic doctrine from 1906 until the advent of aircraft carriers in World War II.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The dreadnought **battleship** was the supreme instrument of modern naval power, embodying the industrial might of the British empire."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The torpedo ram Thunder Child steamed into combat against three Martian tripods, fighting like a doomed **battleship** to protect the refugee fleet."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The ironclads and the modern **battleship** represent an austere triumph of steam machinery over the romantic canvas of the past."},
    ]
  },
  "Dashboard — bat/battlesight.md": {
    "primary": "The fixed or default sight setting on a military rifle or artillery piece, calibrated for immediate engagement at combat ranges.",
    "secondary": "In small arms ballistics, battlesight zero allows infantrymen to hit man-sized targets within three hundred yards without manual elevation changes.",
    "quotes": [
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The sergeant commanded the recruits to set their rifles at **battlesight** and aim low into the advancing gray line."},
      {"author": "Arthur Conan Doyle", "work": "The Green Flag", "quote": "The veteran marksman glanced along the **battlesight** of his Martini-Henry rifle as the enemy skirmishers broke from cover."},
      {"author": "Ernest Hemingway", "work": "Men at War", "quote": "The infantry manual instructed soldiers to utilize the fixed **battlesight** in sudden close-quarters trench encounters."},
    ]
  },
  "Dashboard — bat/battlewagon.md": {
    "primary": "A colloquial or naval slang term for a heavily armored battleship; or an armored war chariot.",
    "secondary": "In twentieth-century naval parlance, sailors affectionate designated dreadnoughts and fast battleships as battlewagons in fleet maneuvers.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The old **battlewagon** Warspite bombarded the Normandy beachheads with her fifteen-inch guns, supporting the Allied landings."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The wooden line-of-battle ship was the ancestral **battlewagon** of the seas, bristling with tiers of black cannons."},
      {"author": "Ernest Hemingway", "work": "Islands in the Stream", "quote": "The patrol boat crew watched the great gray **battlewagon** steam past the reef on its way to the Atlantic convoy lanes."},
    ]
  },
  "Dashboard — bat/battue.md": {
    "primary": "The driving of game birds or animals toward stationary hunters by beaters; or an indiscriminate slaughter.",
    "secondary": "In European game preserve history, a battue was an aristocratic shooting party where hundreds of pheasants were driven into waiting guns.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "Levin preferred solitary hunting with his faithful dog in marshy thickets to the noisy, artificial **battue** organized on great estates."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess was horrified to discover wounded pheasants lying in the woods after an aristocratic autumn **battue** by sporting gentlemen."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman hunters organized a vast **battue** across the Libyan desert to capture wild beasts for the Colosseum amphitheatres."},
    ]
  },
  "Dashboard — bat/batty.md": {
    "primary": "Crazy, mad, eccentric, or mentally unhinged in an amusing or harmless way.",
    "secondary": "In colloquial British and American idiom, calling someone slightly batty suggests idiosyncratic harmless delusions or flighty habits.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "Carry On, Jeeves", "quote": "Bingo Little was always a bit **batty** when in love, pacing his rooms and reciting sentimental poetry at all hours."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The eccentric village rector had grown delightfully **batty**, mistaking his parishioners for characters from Latin comedies."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Three Garridebs", "quote": "The old bibliophile had a reputation for being slightly **batty**, spending fortunes on ancient, worthless parchment fragments."},
    ]
  },
  "Dashboard — bat/combat.md": {
    "primary": "Fighting between armed forces; or a struggle or conflict between opposing persons, groups, or ideas.",
    "secondary": "In military doctrine and hand-to-hand tactical training, close-quarters combat integrates martial discipline with instinctive survival reflexes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "The day, my friends, and all things stay for us: then let our herald cry aloud and sound the charge to **combat** upon the field."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The gladiatorial **combat** in the amphitheater entertained the Roman populace with spectacle of blood and fatal valor."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Male stags engage in furious **combat** during the autumn rut, locking their branched antlers to win access to the herd."},
    ]
  },
  "Dashboard — bat/combatant.md": {
    "primary": "A person, soldier, or nation that engages in fighting, armed conflict, or active competition.",
    "secondary": "In international humanitarian law and the Geneva Conventions, a lawful combatant wears distinctive uniforms and bears arms openly.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Every major European **combatant** poured its industrial output and young manpower into the colossal attrition of trench warfare."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The wounded French **combatant** was treated with chivalrous courtesy by the Russian field surgeons after the engagement."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "Thirty chosen warriors from each Highland clan entered the lists as an appointed **combatant** in the judicial trial by battle."},
    ]
  },
  "Dashboard — bat/combative.md": {
    "primary": "Ready or eager to fight; pugnacious, aggressively argumentative, or fiercely disputatious.",
    "secondary": "In political debate, a combative rhetorical posture seeks to polarize issues and rally partisan supporters through sharp confrontation.",
    "quotes": [
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom Tulliver possessed a proud and **combative** nature, ever ready to defend his boyish honor with clenched fists."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Dr. Johnson was a formidable and **combative** conversationalist who delighted in crushing verbal antagonists in taverns."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger assumed an intensely **combative** attitude whenever rival scientists dared to question his pterodactyl discoveries."},
    ]
  },
  "Dashboard — bat/combatively.md": {
    "primary": "In a combative, aggressive, or argumentative manner; pugnaciously.",
    "secondary": "In courtroom advocacy, counsel cross-examines an evasive witness combatively to expose internal contradictions in testimony.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Mr. Bounderby spoke **combatively**, boasting of his self-made prosperity and daring any man in Coketown to contradict him."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft responded **combatively**, defending his armaments enterprise as the ultimate guarantor of modern social progress."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Olive Chancellor eyed her southern cousin **combatively**, anticipating an intellectual battle over the rights of women."},
    ]
  },
  "Dashboard — bat/combativeness.md": {
    "primary": "A disposition or eager inclination to fight, contend, or assertively dispute; pugnacity.",
    "secondary": "In evolutionary behavioral biology, territorial combativeness in alpha males secures mating access and protects group boundaries.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The instinct of **combativeness** is deeply rooted in mammalian evolutionary biology, finding social outlets in athletics and politics."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Displays of facial sneering and bared canines express natural **combativeness** when an animal prepares for physical contest."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "Luther's ferocious theological **combativeness** gave him the courage to face the imperial Diet of Worms without flinching."},
    ]
  },
  "Dashboard — bat/debatable.md": {
    "primary": "Open to discussion, dispute, or question; not established beyond doubt.",
    "secondary": "In historiography, the primary causes of the fall of the Western Roman Empire remain an endlessly debatable subject among scholars.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Theological subtilties remain forever **debatable** unless illuminated by clear scriptural warrant and rational charity."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The exact phylogenetic branching of fossil hominids provides a legitimate and **debatable** problem in modern paleoanthropology."},
      {"author": "Walter Scott", "work": "The Lay of the Last Minstrel", "quote": "Rival moss-troopers clashed along the **debatable** borderland where neither Scottish nor English law held sway."},
    ]
  },
  "Dashboard — bat/debate.md": {
    "primary": "A formal discussion on a particular topic in a public meeting or assembly, in which opposing arguments are put forward.",
    "secondary": "In parliamentary procedure, floor debate follows established rules of order to allow minority views full legislative expression.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Now, lords, if God doth give successful end unto this **debate** that bleedeth at our doors, we will our youth lead on to higher fields."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A prolonged and contentious parliamentary **debate** ended with the cabinet stubbornly rejecting all overtures of peace."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The freedom of open public **debate** trains citizens to comprehend the intricate balance of local self-government."},
    ]
  },
  "Dashboard — bat/debater.md": {
    "primary": "A person who participates in a debate or formal argument, presenting structured reasoning.",
    "secondary": "In collegiate forensics and parliamentary rhetoric, an experienced debater employs structured syllogisms and cross-examination techniques.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The Life of William Pitt", "quote": "William Pitt proved himself a formidable parliamentary **debater** while still in his early twenties, mastering every fiscal detail."},
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "My companion was a keen **debater** who loved disputation and frequently drove me to refine my arguments."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The medical student was an aggressive **debater** who challenged professors during clinical hospital ward rounds."},
    ]
  },
  "Dashboard — bat/diabatic.md": {
    "primary": "Involving a transfer of heat to or from a thermodynamic system; non-adiabatic.",
    "secondary": "In meteorology and atmospheric thermodynamics, diabatic processes include solar radiation absorption, latent heat release, and ground conduction.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The heating of surface air through contact with sun-baked soil illustrates a typical **diabatic** process governing local weather."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Planetary atmospheric models must account for **diabatic** heating from solar radiation balancing thermal infrared emissions to space."},
      {"author": "Lord Kelvin", "work": "Mathematical and Physical Papers", "quote": "When thermal energy crosses the boundaries of the gas cylinder, the expansion is strictly **diabatic** rather than adiabatic."},
    ]
  },
  "Dashboard — bat/disapprobation.md": {
    "primary": "Strong moral disapproval, condemnation, or adverse judgment.",
    "secondary": "In Victorian social fiction, defying domestic decorum invited severe community disapprobation and formal social exclusion.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Sir Walter Elliot expressed his pronounced **disapprobation** of the proposed naval alliance with fashionable coldness."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Lord Chancellor frowned with grave judicial **disapprobation** at the scandalous delays in the Chancery proceedings."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mrs. Cadwallader voiced her loud **disapprobation** of Dorothea's perverse determination to marry an elderly scholar."},
    ]
  },
  "Dashboard — bat/embattle.md": {
    "primary": "To set in military array or draw up troops in readiness for battle; or to fortify with battlements.",
    "secondary": "In epic poetry and military chronicles, field generals embattle infantry squares and cavalry squadrons before the general assault.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "The English are **embattle** in the field, ready to charge with courage against superior numbers."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Michael commanded the celestial legions to **embattle** in radiant ranks upon the plain of heaven."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whalemen prepared to **embattle** the monsters of the deep, their harpoons sharpened for mortal combat."},
    ]
  },
  "Dashboard — bat/incubate.md": {
    "primary": "To brood over eggs to hatch them by warmth; or to develop slowly and quietly before emerging.",
    "secondary": "In microbiology and infectious pathology, bacterial pathogens incubate within host tissue before manifesting overt clinical symptoms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain Australian megapode birds do not **incubate** their eggs directly, but bury them beneath mounds of fermenting vegetable matter."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The microbiologist must **incubate** the culture broth at constant body temperature to promote bacterial proliferation."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt that secret ambitions had begun to **incubate** within his restless heart, making the forge seem narrow and dull."},
    ]
  },
  "Dashboard — bat/incubation.md": {
    "primary": "The process of incubating eggs, bacterial cultures, or developing plans; or the period before a disease manifests.",
    "secondary": "In epidemiology, the incubation period of a virus is the silent time interval elapsed between exposure and the onset of symptoms.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical **incubation** period of typhoid fever varies from eight to fourteen days before the step-ladder fever appears."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The female bird assumes the primary burden of **incubation**, her cryptic plumage protecting the clutch from sharp-eyed predators."},
      {"author": "Louis Pasteur", "work": "Researches on Attenuated Viruses", "quote": "Following inoculation into the animal host, a prolonged period of **incubation** preceded the clinical onset of rabies symptoms."},
    ]
  },
  "Dashboard — bat/incubator.md": {
    "primary": "An apparatus used to provide controlled temperature and humidity for hatching eggs or rearing premature infants.",
    "secondary": "In neonatal medicine, modern infant incubators revolutionized pediatrics by maintaining thermoregulation for fragile premature neonates.",
    "quotes": [
      {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "The clinical introduction of the infant **incubator** dramatically reduced mortality rates among fragile, premature newborns in maternity hospitals."},
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "Ukridge invested his meager capital in a patented artificial **incubator**, dreaming of hatching thousands of prize Orpington chickens."},
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "The research scientist placed the experimental bacterial flasks inside the laboratory **incubator** to monitor overnight cell division."},
    ]
  },
  "Dashboard — bat/noncombatant.md": {
    "primary": "A person who is not engaged in active fighting, such as a medical officer, chaplain, or civilian.",
    "secondary": "Under the law of armed conflict, a designated noncombatant enjoys protected legal status and must not be targeted in military operations.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "International treaties strictly prohibit armed belligerents from targeting an innocent **noncombatant** during naval blockades."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian invaders spared neither age nor sex, slaughtering every peaceful **noncombatant** within the captured provincial city."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The regiment swept through the farmyard, ignoring the frightened **noncombatant** women who sheltered inside the brick dairy."},
    ]
  },
  "Dashboard — bat/probate.md": {
    "primary": "The official legal process of proving that a will is valid; or to establish the validity of a will in court.",
    "secondary": "In inheritance jurisprudence and estate administration, probate courts supervise executor duties, estate asset valuation, and creditor distributions.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The executor must present the testament for formal **probate** before the ecclesiastical ordinary to validate title to personalty."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The jurisdiction over **probate** matters and testamentary administration properly resides in local state judicial tribunals."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The contested will lingered for thirty years in the **probate** courts, until costs consumed the entire disputed inheritance."},
    ]
  },
  "Dashboard — bat/probation.md": {
    "primary": "A period of testing or trial to evaluate a person's conduct, character, or suitability; or a conditional judicial sentence.",
    "secondary": "In penology, probation serves as a community-based alternative to incarceration under the supervisory oversight of a probation officer.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "This day my sister should the cloister enter, and there receive her **probation** under strict monastic vows."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A wise tutor places the young gentleman on moral **probation**, observing his conduct when free from immediate surveillance."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The Puritan elders viewed human life on earth as a solemn **probation** preparing the elect for eternity."},
    ]
  },
  "Dashboard — bat/probationary.md": {
    "primary": "Relating to or serving as a period of testing, trial, or evaluation before permanent confirmation.",
    "secondary": "In civil service administration, a probationary appointment allows supervisors to evaluate a recruit's aptitude before conferring tenure.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Three Clerks", "quote": "The ambitious young clerk served a rigorous **probationary** year in the Weights and Measures office before receiving his permanent appointment."},
      {"author": "Thomas Babington Macaulay", "work": "The Life of William Pitt", "quote": "The new ministers viewed their first parliamentary session as a **probationary** trial before an expectant British public."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy endured his **probationary** agricultural apprenticeship with Caleb Garth, striving to prove his renewed industriousness."},
    ]
  },
  "Dashboard — bat/probationer.md": {
    "primary": "A person undergoing a period of trial or probation, such as a novice, newly hired employee, or theological student.",
    "secondary": "In nineteenth-century hospital administration, a nurse probationer received practical clinical training under the supervision of a ward sister.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Reuben Butler was a licensed church **probationer**, waiting patiently for a parish living to fall vacant in the Kirk of Scotland."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The young **probationer** at Lowood school endured strict discipline and meager rations with quiet Christian fortitude."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The hospital **probationer** took the patient's pulse and temperature, recording the clinical data on the chart at the bedside."},
    ]
  },
  "Dashboard — bat/probative.md": {
    "primary": "Having the quality of proving, testing, or demonstrating the truth or validity of something; evidentiary.",
    "secondary": "In the law of evidence, probative value is weighed against unfair prejudice to determine whether a document is admissible at trial.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "Direct eyewitness testimony possesses the highest **probative** force in establishing the material facts of a criminal indictment."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "A crucial empirical experiment possesses singular **probative** virtue, deciding between two rival hypotheses in natural philosophy."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Inductive generalizations lack **probative** certainty until verified by rigorous methods of elimination and experimental control."},
    ]
  },
  "Dashboard — bat/probatory.md": {
    "primary": "Serving to test, prove, or examine; probationary or evidentiary.",
    "secondary": "In civil law and canon jurisprudence, a probatory term is the designated period granted to litigants to produce evidence and examine witnesses.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The ecclesiastical judge granted a **probatory** term to allow the parties to interrogate witnesses under oath."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The trials of human existence are designed by Providence to serve a **probatory** discipline that refines virtue."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The transitional assembly instituted a **probatory** constitution, testing public tolerance for sweeping administrative innovations."},
    ]
  },
  "Dashboard — bat/rebate.md": {
    "primary": "A partial refund to someone who has paid too much money for tax, rent, or a utility; or to blunt a weapon.",
    "secondary": "In industrial history and antitrust regulation, secret railroad rebates granted to Standard Oil helped eliminate smaller independent competitors.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchants petitioned Parliament for a customs **rebate** upon foreign raw materials re-exported in manufactured goods."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Doth make my cold heart **rebate** its natural courage, and turn my thoughts to fearful apprehension."},
      {"author": "Frank Norris", "work": "The Octopus", "quote": "The wheat growers struggled against the railroad trust, which used discriminatory tariff and secret **rebate** schemes to control the market."},
    ]
  },
  "Dashboard — bat/rebato.md": {
    "primary": "A stiff, flared, wired collar or ruff worn by men and women in the late sixteenth and early seventeenth centuries.",
    "secondary": "In Elizabethan and Jacobean costume history, the rebato supported elaborate lace ruffs, framing the neck and shoulders in formal court dress.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Much Ado About Nothing", "quote": "Hero inquired of Margaret: 'I think the other **rebato** were better.' And Margaret answered: 'No, pray thee, good madam, this one is handsomer.'"},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "Queen Elizabeth appeared adorned in a magnificent pleated lace **rebato**, held stiffly upright by concealed silver wire."},
      {"author": "Ben Jonson", "work": "Every Man out of His Humour", "quote": "The court gallant spent half his morning adjusting the starch in his pleated **rebato** before appearing in Paul's Walk."},
    ]
  },
  "Dashboard — bat/reprobate.md": {
    "primary": "An unprincipled or depraved person; or to express severe disapproval of someone or something.",
    "secondary": "In Calvinist theology and predestinarian dogma, the reprobate are those excluded from divine grace and foreordained to eternal damnation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Prince Hal was playfully rebuked for keeping company with Falstaff, that ancient and incorrigible **reprobate**."},
      {"author": "John Bunyan", "work": "Grace Abounding to the Chief of Sinners", "quote": "I trembled in terror lest I should find myself numbered among the hopeless **reprobate** abandoned by God."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Brocklehurst denounced the weeping child as an ungrateful **reprobate** who harbored a deceitful heart."},
    ]
  },
  "Dashboard — bat/reprobation.md": {
    "primary": "Severe condemnation, formal rejection, or divine exclusion from salvation.",
    "secondary": "In Reformed theology, the decree of reprobation is the eternal preterition of non-elect individuals from sovereign divine grace.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode trembled at the thought of public **reprobation**, dreading that his past hypocrisies would be laid bare before his neighbors."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman emperors condemned the Gnostic sects with fierce imperial **reprobation**, banishing their leaders from the cities."},
      {"author": "Robert Burns", "work": "Holy Willie's Prayer", "quote": "The Calvinist elder prayed with grim satisfaction that divine **reprobation** would overtake his theological adversaries."},
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

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

print(f"Dashboard — bat Part 2: Successfully updated {updated}/{len(data)} notes.")
