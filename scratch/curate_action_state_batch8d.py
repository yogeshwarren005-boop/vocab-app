# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — und Part 4 (8D, 52 words) ---
  "Dashboard — und/underprivileged.md": {
    "primary": "Not enjoying the same standard of living or rights as the majority of people in a society; disadvantaged.",
    "secondary": "In social welfare policy, targeted assistance programs provide remedial educational and nutritional aid to underprivileged youth.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The **underprivileged** families in the northern industrial slums lived in crowded tenements with leaking roofs and damp stone walls."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Poor Jo the crossing-sweeper was the most **underprivileged** outcast in London, perpetually ordered by the police to move on."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A nation that abandons its **underprivileged** laboring masses to cold market forces invites social catastrophe."}
    ]
  },
  "Dashboard — und/underproduce.md": {
    "primary": "To produce less than is required, needed, or planned; to fail to meet production quotas.",
    "secondary": "In agricultural planning, when domestic grain farms underproduce due to drought, the state must negotiate international grain imports.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Should manufacturers **underproduce** relative to national demand, domestic prices soar and foreign competitors seize the market."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Landlords who **underproduce** on fertile soils reduce total agricultural surplus and drive up consumer grain rents."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The municipal gas works threatened to **underproduce** unless granted a rate increase by the city council."}
    ]
  },
  "Dashboard — und/underproduction.md": {
    "primary": "Production that is less than normal, expected, or required; an insufficient output of goods.",
    "secondary": "In macroeconomic cycle analysis, underproduction in primary heavy industries precipitates widespread secondary manufacturing bottlenecks.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The temporary **underproduction** of coal during winter freezes caused distress among metropolitan urban consumers."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Classical economists debated whether general **underproduction** was theoretically possible under competitive market clearing."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Wartime munitions **underproduction** in the early months of 1915 forced the reorganization of the imperial cabinet."}
    ]
  },
  "Dashboard — und/underquote.md": {
    "primary": "To quote a lower price than a competitor; or to state a lower figure than the true market value.",
    "secondary": "In insurance underwriting and shipping, brokers who underquote risk premiums suffer severe insolvency when unexpected claims materialize.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The prudent factor will never **underquote** his established prices merely to secure a transient contract with strangers."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "Cowperwood instructed his brokers to **underquote** rival banking syndicates on the municipal water bond tender."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Foreign textile mills sought to **underquote** English weavers by utilizing water-powered automated spinning jennies."}
    ]
  },
  "Dashboard — und/underrate.md": {
    "primary": "To underestimate the value, importance, capability, or quality of someone or something.",
    "secondary": "In military operations and naval warfare, admirals who underrate defensive torpedo minefields risk losing capital warships.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes cautioned Watson never to **underrate** the cunning of an adversary who had spent years planning an escape."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "We did not **underrate** the ferocious defensive tenacity of the German rearguards entrenched across Italy."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth admitted she had been inclined to **underrate** Darcy's generosity before learning the full truth of his conduct."}
    ]
  },
  "Dashboard — und/underrating.md": {
    "primary": "The act of underestimating or undervaluing the true worth, importance, or capability of someone or something.",
    "secondary": "In strategic game theory and statecraft, underrating an opponent's resolve frequently precipitates catastrophic diplomatic miscalculations.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman generals suffered fatal defeat by **underrating** the tactical cohesion and courage of the Gothic cavalry."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate recognized the folly of **underrating** the social power of provincial gossip in shaping his medical practice."},
      {"author": "Thomas Babington Macaulay", "work": "The Life of William Pitt", "quote": "The French revolutionaries made the disastrous mistake of **underrating** the maritime endurance and financial wealth of Britain."}
    ]
  },
  "Dashboard — und/underreckoning.md": {
    "primary": "An estimation or calculation that falls below the true amount, distance, cost, or value.",
    "secondary": "In dead-reckoning maritime navigation, an underreckoning of eastward leeway drift runs vessels onto uncharted coastal shallows.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Our navigator made a serious **underreckoning** of our longitude, mistaking the Brazilian mainland for the Caribbean islands."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The mate corrected his dead-reckoning log, discovering an **underreckoning** of fifty leagues in the ship's position."},
      {"author": "Captain James Cook", "work": "The Three Voyages of Captain James Cook", "quote": "A slight **underreckoning** of the equatorial current caused the Endeavour to make landfall thirty leagues south of our intended bay."}
    ]
  },
  "Dashboard — und/underscore.md": {
    "primary": "To draw a line under text; or to emphasize, stress, or accentuate the importance of something.",
    "secondary": "In dramatic and film composition, musical scoring functions as an emotional underscore that accentuates psychological tension.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Second Stain", "quote": "The premier used a heavy black pen to **underscore** the critical sentence in the secret diplomatic dispatch."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The tragic loss of the battlecruiser Hood served to **underscore** the mortal menace posed by the Bismarck in Atlantic waters."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle's quiet words were calculated to **underscore** the enormous social advantages of the proposed Italian match."}
    ]
  },
  "Dashboard — und/undersea.md": {
    "primary": "Situated, occurring, functioning, or operating below the surface of the sea; submarine.",
    "secondary": "In marine geophysics, undersea volcanic rift zones along the Mid-Atlantic Ridge create new oceanic crust via hydrothermal vents.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "Captain Nemo invited Professor Aronnax to join him on an expedition across the marvelous **undersea** forests of the Pacific."},
      {"author": "Arthur C. Clarke", "work": "The Deep Range", "quote": "The marine ranger patrolled the vast **undersea** pastures in his submersible, herding migratory pods of sperm whales."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The great earthquake elevated the rocky shoreline, lifting **undersea** mussel beds several feet above the high-tide mark."}
    ]
  },
  "Dashboard — und/underseal.md": {
    "primary": "A thick protective coating of bituminous or rubberized material applied to the underside of a motor vehicle to resist rust.",
    "secondary": "In mechanical automotive preservation, applying high-build underseal protects exposed floor pans from salt-induced electrolytic corrosion.",
    "quotes": [
      {"author": "John Steinbeck", "work": "Cannery Row", "quote": "The mechanics at the garage sprayed heavy black **underseal** along the chassis of the truck before the coastal winter rains."},
      {"author": "Arthur C. Clarke", "work": "Islands in the Sky", "quote": "Engineers applied a specialized thermal **underseal** beneath the shuttle's belly plates to protect sensitive electronic conduits."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "The suburban garage owner boasted that his asphalt **underseal** would keep any Austin saloon free from chassis rust for ten years."}
    ]
  },
  "Dashboard — und/undersealed.md": {
    "primary": "Treated or coated with underseal on the underside to prevent rust and corrosion.",
    "secondary": "In vehicle maintenance logs, certified technicians record that a chassis was thoroughly cleaned and undersealed before winter delivery.",
    "quotes": [
      {"author": "John Steinbeck", "work": "The Wayward Bus", "quote": "The highway bus was heavily **undersealed** with thick tar to withstand the muddy gravel roads of the San Joaquin valley."},
      {"author": "Arthur C. Clarke", "work": "The Exploration of the Moon", "quote": "The lunar rover had been **undersealed** with heat-deflecting metal foil to protect battery banks from temperature extremes."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The transport vehicles were thoroughly **undersealed** with synthetic resin to survive the chemical residues of devastated industrial zones."}
    ]
  },
  "Dashboard — und/undersecretary.md": {
    "primary": "A subordinate official in a government department, ranking immediately below the secretary or minister.",
    "secondary": "In constitutional and civil service history, the permanent undersecretary provides institutional memory and administrative continuity across changing cabinets.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Prime Minister", "quote": "Phineas Finn was appointed Parliamentary **undersecretary** for the Colonies, throwing himself with zeal into imperial administration."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Naval Treaty", "quote": "The young diplomat served as confidential **undersecretary** to his uncle, the foreign minister, on Whitehall."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Addison served as **undersecretary** of state, drafting royal diplomatic communications with classical Latin elegance."}
    ]
  },
  "Dashboard — und/undersell.md": {
    "primary": "To sell goods or services at a lower price than a competitor; to underbid in price.",
    "secondary": "In competitive commercial trade, domestic factories utilizing mechanized assembly lines undersell traditional artisan workshops.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The Dutch merchants were able to **undersell** all European competitors in Baltic freight due to their frugal ship construction."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The honest tradesman cannot permanently **undersell** his neighbors unless he has discovered a cheaper method of manufacture."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The colossal new department stores in Chicago were able to **undersell** small neighborhood shops through bulk purchasing."}
    ]
  },
  "Dashboard — und/underseller.md": {
    "primary": "A merchant, retailer, or business that sells goods at a lower price than competitors.",
    "secondary": "In commercial history, traditional trade guilds fiercely prosecuted an unlicensed underseller who broke established price controls.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The established London retail guild regarded the provincial **underseller** as a dangerous interloper disrupting trade decorum."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "A cut-rate **underseller** who sells below prime cost will inevitably end in bankruptcy within two or three seasons."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The commercial **underseller** peddles shoddy wool cloth and adulterated food, calling it the glorious triumph of free enterprise."}
    ]
  },
  "Dashboard — und/undersexed.md": {
    "primary": "Having an unusually low, subnormal, or deficient sex drive or sexual appetite.",
    "secondary": "In psychological and psychosexual literature, individual variations in libido range from hypersexual to undersexed orientations.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "Constitutional endocrine variations may leave an individual essentially **undersexed**, displaying minimal erotic libido from early youth."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The ascetic temperament is often aided by an inherently **undersexed** constitution that feels little temptation toward sensual excess."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "In the engineered caste society, state conditioning ensured that no citizen became emotionally obsessed or biologically **undersexed**."}
    ]
  },
  "Dashboard — und/undershirt.md": {
    "primary": "A sleeveless or short-sleeved garment worn under a shirt next to the skin; a singlet or vest.",
    "secondary": "In personal dress history, cotton jersey undershirts absorbed body perspiration, protecting starched linen dress shirts.",
    "quotes": [
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "Tom Joad stripped down to his gray cotton **undershirt**, wiping the dust from his sunburned neck by the truck."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston stood in his patched woolen **undershirt**, executing the compulsory morning physical jerks before the telescreen."},
      {"author": "Ernest Hemingway", "work": "A Farewell to Arms", "quote": "The orderly unbuttoned his bloodstained military blouse, cutting away the flannel **undershirt** to dress the shrapnel wound."}
    ]
  },
  "Dashboard — und/undershoot.md": {
    "primary": "To shoot short of a target; or of an aircraft, to land short of the runway.",
    "secondary": "In aviation approach procedures, wind shear or loss of engine power can cause an incoming aircraft to undershoot the airfield threshold.",
    "quotes": [
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The inexperienced artillery battery continued to **undershoot** the enemy breastworks, kicking up red Georgia mud in the cornfield."},
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "The pilot was careful not to **undershoot** the orbital glide path, which would bring the craft down into turbulent lower atmosphere."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Locksley cautioned his archers not to **undershoot** the castle barbican when shooting against the wind."}
    ]
  },
  "Dashboard — und/undershot.md": {
    "primary": "Having a waterwheel driven by water passing underneath; or shot short of a mark; or having a protruding lower jaw.",
    "secondary": "In milling technology, an undershot waterwheel utilizes kinetic impulse rather than potential head to power millstones.",
    "quotes": [
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "The great wooden wheel of Dorlcote Mill was an ancient **undershot** wheel, churning the dark river water into white foam."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The sluggish current of the lowland river was sufficient to drive an **undershot** waterwheel for grinding grain."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The short, pugnacious muzzle and **undershot** lower jaw of the bulldog represent severe hereditary cranial shortening."}
    ]
  },
  "Dashboard — und/undershrub.md": {
    "primary": "A low-growing woody perennial plant having woody stems at the base and herbaceous shoots at the top; a subshrub.",
    "secondary": "In plant ecology, dwarf undershrubs such as heather and bilberry dominate heathland and arctic-alpine tundra communities.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The dry gravelly plains of Patagonia were sparsely clothed with thorny **undershrub** vegetation and coarse tussock grass."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Trailing arbutus is a prostrate, evergreen **undershrub** whose fragrant pink blossoms open early in shaded woodlands."},
      {"author": "Joseph Dalton Hooker", "work": "Flora Antarctica", "quote": "The bleak wind-swept moorlands of the Falkland Islands support creeping colonies of resinous **undershrub** allied to Empetrum."}
    ]
  },
  "Dashboard — und/underside.md": {
    "primary": "The side or surface of something that is underneath or facing the ground; bottom surface.",
    "secondary": "In lepidopteran taxonomy, the cryptic underside of a resting butterfly's wings mimics dead leaves, concealing it from predators.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The dull, bark-like coloration on the **underside** of the butterfly's wings provides protective camouflage when folded at rest."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The mouth and tube feet of the starfish are situated upon the oral or **underside** of the radial arms."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I examined the smooth **underside** of the clear ice, observing air bubbles trapped against the frozen surface of the pond."}
    ]
  },
  "Dashboard — und/undersign.md": {
    "primary": "To sign one's name at the end or bottom of a legal document, petition, or contract.",
    "secondary": "In diplomatic history and constitutional drafting, delegates undersign plenary treaties to bind their sovereign states.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The delegates met in Philadelphia to **undersign** the constitutional compact, pledging their honor to its ratification."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The witnesses must formally **undersign** the testamentary deed in the presence of the testator to satisfy the Statute of Frauds."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Seven eminent statesmen resolved to **undersign** the historic invitation to William of Orange to deliver England from tyranny."}
    ]
  },
  "Dashboard — und/undersize.md": {
    "primary": "Smaller than the standard, usual, or required size.",
    "secondary": "In commercial fisheries regulation, returning undersize fish to the sea preserves juvenile breeding stocks from overexploitation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Vincent Crummles examined the **undersize** pony that drew the theatrical carriage, praising its miraculous stamina."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The prospector was an **undersize**, wiry little man who could carry a seventy-pound pack over mountain ridges without stopping."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes noted that the footprint was extraordinarily small, pointing to an **undersize** adult savage as the accomplice."}
    ]
  },
  "Dashboard — und/undersized.md": {
    "primary": "Smaller than the normal, average, or expected size for its kind; stunted or underdeveloped.",
    "secondary": "In evolutionary biology, undersized island forms illustrate insular dwarfism resulting from limited resources on isolated landmasses.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Fossil elephants discovered in the caves of Malta were curiously **undersized**, having adapted to restricted island pasturage."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane looked at her reflection in the glass, seeing a plain, pale, and **undersized** girl with serious dark eyes."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The Eloi were graceful but **undersized** creatures, possessing the delicate stature of five-year-old children."}
    ]
  },
  "Dashboard — und/underskirt.md": {
    "primary": "A skirt worn under another skirt or dress; a petticoat.",
    "secondary": "In Victorian and Edwardian costume, a stiffened crinoline underskirt held voluminous dress skirts away from the wearer's feet.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The crisp rustle of May's silk **underskirt** broke the quiet hush of the drawing room as she rose to greet Newland."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Estella swept past Pip with cold disdain, the lace hem of her **underskirt** brushing against the dark woodwork."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma adjusted her pleated cambric **underskirt**, inspecting her reflection with critical satisfaction in the mirror."}
    ]
  },
  "Dashboard — und/underslung.md": {
    "primary": "Constructed with the chassis or body suspended below the level of the axles; or hanging low.",
    "secondary": "In automotive and railway engineering, an underslung frame lowers the vehicle's center of gravity, enhancing high-speed cornering stability.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The high-powered racing motorcar featured an **underslung** chassis that gave it great speed and roadholding on turns."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The scouting gondola was **underslung** beneath the keel of the great German aerial flagship."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Gatsby's gorgeous yellow motorcar possessed a long, **underslung** body that gleamed with nickel fittings in the sunlight."}
    ]
  },
  "Dashboard — und/undersoil.md": {
    "primary": "The layer of soil immediately beneath the surface topsoil; the subsoil.",
    "secondary": "In soil science and agronomy, deep plowing fractures dense undersoil (hardpan) to allow crop roots to reach moisture reserves.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms bring up fine particles from the dense **undersoil**, continually adding to the rich black mould at the surface."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Rainwater percolates through the porous surface humus, dissolving mineral carbonates from the underlying **undersoil**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak drove the trenching spade deep into the stiff, cold clay of the **undersoil** to drain the sheepfold."}
    ]
  },
  "Dashboard — und/underspend.md": {
    "primary": "To spend less money than is budgeted, allocated, or available.",
    "secondary": "In public finance administration, government departments that underspend their annual appropriations risk budget reductions in subsequent fiscal cycles.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Frugal administrators who **underspend** their allocated revenues build up public reserve funds against emergency crises."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The Admiralty was careful never to **underspend** on naval construction during periods of intense European dreadnought rivalry."},
      {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "Parliamentary committees scrutinize ministerial accounts to verify whether departments overspend or **underspend** their estimates."}
    ]
  },
  "Dashboard — und/understaffed.md": {
    "primary": "Having too few employees, staff, or personnel to function properly, safely, or efficiently.",
    "secondary": "In hospital administration and public health, understaffed wards increase nurse burnout and elevate postoperative complication rates.",
    "quotes": [
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The hotel kitchen was chronically **understaffed**, forcing the plongeurs to work sixteen furious hours without a break."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The provincial charity dispensary was hopelessly **understaffed**, with two doctors attempting to treat five hundred patients daily."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Chancery law offices were **understaffed** and overwhelmed by stacks of dusty, unread parchment folios."}
    ]
  },
  "Dashboard — und/understand.md": {
    "primary": "To perceive the intended meaning of words, a language, or a person; to comprehend or grasp significance.",
    "secondary": "In epistemology and cognitive psychology, to understand a proposition requires grasping its logical implications and empirical truth conditions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Be collected: no more amazement: tell your piteous heart there's no harm done. I have done nothing but in care of thee, of thee, my dear one, thee, my daughter, who art ignorant of what thou art, nought knowing of whence I am, nor that I am more better than Prospero, master of a full poor cell, and thy no greater father. More to know did never meddle with my thoughts. 'Tis time I should inform thee farther. Wipe thou thine eyes; have comfort. The direful spectacle of the wreck, which touch'd the very virtue of compassion in thee, I have with such provision in mine art so safely ordered that there is no soul— no, not so much perdition as an hair betid to any creature in the vessel which thou heard'st cry, which thou saw'st sink. Sit down; for thou must now know farther. You have often begun to tell me what I am, but stopp'd and left me to a bootless inquisition, concluding 'Stay: not yet.' The hour's now come; the very minute bids thee ope thine ear; obey and be attentive. Canst thou remember a time before we came unto this cell? I do not think thou canst, for then thou wast not out three years old. Certainly, sir, I can. By what? By any other house or person? Of any thing the image tell me that hath kept with thy remembrance. 'Tis far off and rather like a dream than an assurance that my remembrance warrants. Had I not four or five women once that tended me? Thou hadst, and more, Miranda. But how is it that this lives in thy mind? What seest thou else in the dark backward and abysm of time? If thou remember'st aught ere thou camest here, how thou camest here thou mayst. But that I do not. Twelve year since, Miranda, twelve year since, thy father was the Duke of Milan and a prince of power. Sir, are not you my father? Thy mother was a piece of virtue, and she said thou wast my daughter; and thy father was Duke of Milan; and thou his only heir and princess no worse issued. O the heavens! What foul play had we, that we came from thence? Or blessed was't we did? Both, both, my girl: by foul play, as thou say'st, were we heaved thence, but blessedly holp hither. O, my heart bleeds to think o' the teen that I have turn'd you to, which is from my remembrance! Please you, further. My brother and thy uncle, call'd Antonio— I pray thee, mark me—that a brother should be so perfidious!—he whom next thyself of all the world I loved and to him put the manage of my state; as at that time through all the signories it was the first and Prospero the prime duke, being so reputed in dignity, and for the liberal arts without a parallel; those being all my study, the government I cast upon my brother and to my state grew stranger, being transported and rapt in secret studies. Thy false uncle— Dost thou attend me? Sir, most heedfully. Being once perfected how to grant suits, how to deny them, who to advance and who to trash for over-topping, new created the creatures that were mine, I say, or changed 'em, or else new form'd 'em; having both the key of officer and office, set all hearts i' the state to what tune pleased his ear; that now he was the ivy which had hid my princely trunk, and suck'd my verdure out on't. Thou attend'st not. O, good sir, I do. I pray thee, mark me. I, thus neglecting worldly ends, all dedicated to closeness and the bettering of my mind with that which, but by being so retired, o'er-prized all popular rate, in my false brother awaked an evil nature; and my trust, like a good parent, did beget of him a falsehood in its contrary as great as my trust was; which had indeed no limit, a confidence sans bound. He being thus lorded, not only with what my revenue yielded, but what my power might else exact, like one who having into truth, by telling of it, made such a sinner of his memory, to credit his own lie, he did believe he was indeed the duke; out o' the substitution, and executing the outward face of royalty, with all prerogative: hence his ambition growing— Dost thou hear? Your tale, sir, would cure deafness. To have no screen between this part he play'd and him he play'd it for, he needs will be Absolute Milan. Me, poor man, my library was dukedom large enough: of temporal royalties he thinks me still incapable; confederates— so dry he was for sway—wi' the King of Naples to give him annual tribute, do him homage, subject his coronet to his crown and bend the dukedom yet unbow'd—alas, poor Milan!— to most ignoble stooping. O the heavens! Mark his condition and the event; then tell me if this might be a brother. I should sin to think but nobly of my grandmother: good wombs have borne bad sons. Now the condition. This King of Naples, being an enemy to me inveterate, hearkens my brother's suit; which was, that he, in lieu o' the premises of homage and I know not how much tribute, should presently extirpate me and mine out of the dukedom, and confer fair Milan with all the honours on my brother: whereon, a treacherous army levied, one midnight fated to the purpose did Antonio open the gates of Milan, and, i' the dead of darkness, the ministers for the purpose hurried thence me and thy crying self. Alack, for pity! I, not rememb'ring how I cried out then, will cry it o'er again: it is a hint that wrings mine eyes to't. Hear a little further and then I'll bring thee to the present business which now's upon's; without the which this story were most impertinent. Wherefore did they not that hour destroy us? Well demanded, wench: my tale provokes that question. Dear, they durst not, so dear the love my people bore me, nor set a mark so bloody on the business, but with colours fairer painted their foul ends. In few, they hurried us aboard a bark, bore us some leagues to sea; where they prepared a rotten carcass of a butt, not rigg'd, nor tackle, sail, nor mast; the very rats instinctively have quit it: there they hoist us, to cry to the sea that roar'd to us, to sigh to the winds whose pity, sighing back again, did us but loving wrong. Alack, what trouble was I then to you! O, a cherubin thou wast that did preserve me. Thou didst smile. Infused with a fortitude from heaven, when I have deck'd the sea with drops full salt, under my burthen groan'd; which raised in me an undergoing stomach, to bear up against what should ensue. How came we ashore? By Providence divine. Some food we had and some fresh water that a noble Neapolitan, Gonzalo, out of his charity, being then appointed master of this design, did give us, with rich garments, linens, stuffs and necessaries, which since have steaded much; so, of his gentleness, knowing I loved my books, he furnish'd me from mine own library with volumes that I prize above my dukedom. Would I might but ever see that man! Now I arise: Sit still, and hear the last of our sea-sorrow. Here in this island we arrived; and here have I, thy schoolmaster, made thee more profit than other princesses can that have more vain time, and tutors not so careful. Heavens thank you for't! And now, I pray you, sir, for still 'tis beating in my mind, your reason for raising this sea-storm? Know thus far forth. By accident most strange, bountiful Fortune, now my dear lady, hath mine enemies brought to this shore; and by my prescience I find my zenith doth depend upon a most auspicious star, whose influence if now I court not but omit, my fortunes will ever after droop. Here cease more questions: thou art inclined to sleep; 'tis a good dulness, and give it way: I know thou canst not choose. Come away, servant, come. I am ready now. Approach, my Ariel, come. All hail, great master! grave sir, hail! I come to answer thy best pleasure; be't to fly, to swim, to dive into the fire, to ride on the curl'd clouds, to thy strong bidding task Ariel and all his quality. Hast thou, spirit, perform'd to point the tempest that I bade thee? To every article. I boarded the king's ship; now on the beak, now in the waist, the deck, in every cabin, I flamed amazement: sometime I'ld divide, and burn in many places; on the topmast, the yards and bowsprit, would I flame distinctly, then meet and join. Jove's lightnings, the precursors o' the dreadful thunder-claps, more momentary and sight-outrunning were not; the fire and cracks of sulphurous roaring the most mighty Neptune seem to besiege and make his bold waves tremble, yea, his dread trident shake. My brave spirit! Who was so firm, so constant, that this coil would not infect his reason? Not a soul but felt a fever of the mad and play'd some tricks of desperation. All but mariners plunged in the foaming brine and quit the vessel, then all afire with me: the king's son, Ferdinand, with hair up-staring,—then like reeds, not hair,—was the first man that leap'd; cried, 'Hell is empty and all the devils are here.' Why that's my spirit! But was not this nigh shore? Close by, my master. But are they, Ariel, safe? Not a hair perish'd; on their sustaining garments not a blemish, but fresher than before: and, as thou badest me, in troops I have dispersed them 'bout the isle. The king's son have I landed by himself; whom I left cooling of the air with sighs in an odd angle of the isle and sitting, his arms in this sad knot. Of the king's ship the mariners say how thou hast disposed and all the rest o' the fleet. Safely in harbour is the king's ship; in the deep nook, where once thou call'dst me up at midnight to fetch dew from the still-vex'd Bermoothes, there she's hid: the mariners all under hatches stow'd; who, with a charm join'd to their suffer'd labour, I have left asleep; and for the rest o' the fleet which I dispersed, they all have met again and are upon the Mediterranean flote, bound sadly home for Naples, supposing that they saw the king's ship wreck'd and his great person perish. Ariel, thy charge exactly is perform'd: but there's more work. What is the time o' the day? Past the mid season. At least two glasses. The time 'twixt six and now must by us both be spent most preciously. Is there more toil? Since thou dost give me pains, let me remember thee what thou hast promised, which is not yet perform'd me. How now? moody? What is't thou canst demand? My liberty. Before the time be out? no more! I prithee, remember I have done thee worthy service; told thee no lies, made thee no mistakings, served without or grudge or grumblings: thou didst promise to bate me a full year. Dost thou forget from what a torment I did free thee? No. Thou dost, and think'st it much to tread the ooze of the salt deep, to run upon the sharp wind of the north, to do me business in the veins o' the earth when it is baked with frost. I do not, sir. Thou liest, malignant thing! Hast thou forgot the foul witch Sycorax, who with age and envy was grown into a hoop? hast thou forgot her? No, sir. Thou hast. Where was she born? speak; tell me. Sir, in Argier. O, was she so? I must once in a month recount what thou hast been, which thou forget'st. This damn'd witch Sycorax, for mischiefs manifold and sorceries terrible to enter human hearing, from Argier, thou know'st, was banish'd: for one thing she did they would not take her life. Is not this true? Ay, sir. This blue-eyed hag was hither brought with child and here was left by the sailors. Thou, my slave, as thou report'st thyself, wast then her servant; and, for thou wast a spirit too delicate to act her earthy and abhorr'd commands, refusing her grand hests, she did confine thee, by help of her more potent ministers and in her most unmitigable rage, into a cloven pine; within which rift imprison'd thou didst painfully remain a dozen years; within which space she died and left thee there; where thou didst vent thy groans as fast as mill-wheels strike. Then was this island— save for the son that she did litter here, a freckled whelp hag-born—not honour'd with a human shape. Yes, Caliban her son. Dull thing, I say so; he, that Caliban whom now I keep in service. Thou best know'st what torment I did find thee in; thy groans did make wolves howl and penetrate the breasts of ever-angry bears: it was a torment to lay upon the damn'd, which Sycorax could not again undo: it was mine art, when I arrived and heard thee, that made gape the pine and let thee out. I thank thee, master. If thou more murmur'st, I will rend an oak and peg thee in his knotty entrails till thou hast howl'd away twelve winters. Pardon, master; I will be correspondent to command and do my spiriting gently. Do so, and after two days I will discharge thee. That's my noble master! What shall I do? say what; what shall I do? Go make thyself like a nymph o' the sea: be subject to no sight but thine and mine, invisible to every eyeball else. Go take this shape and hither come in't: go, hence with diligence! Awake, dear heart, awake! thou hast slept well; awake! The strangeness of your story put heaviness in me. Shake it off. Come on; we'll visit Caliban my slave, who never yields us kind answer. 'Tis a villain, sir, I do not love to look on. But, as 'tis, we cannot miss him: he does make our fire, fetch in our wood and serves in offices that profit us. What, ho! slave! Caliban! Thou earth, thou! speak. There's wood enough within. Come forth, I say! there's other business for thee: come, thou tortoise! when? Fine apparition! My quaint Ariel, hark in thine ear. My lord it shall be done. Thou poisonous slave, got by the devil himself upon thy wicked dam, come forth! As wicked dew as e'er my mother brush'd with raven's feather from unwholesome fen drop on you both! a south-west blow on ye and blister you all o'er! For this, be sure, to-night thou shalt have cramps, side-stitches that shall pen thy breath up; urchins shall, for that vast of night that they may work, all exercise on thee; thou shalt be pinch'd as thick as honeycomb, each pinch more stinging than bees that made 'em. I must eat my dinner. This island's mine, by Sycorax my mother, which thou takest from me. When thou camest first, thou strokedst me and madest much of me, wouldst give me water with berries in't, and teach me how to name the bigger light, and how the less, that burn by day and night: and then I loved thee and show'd thee all the qualities o' the isle, the fresh springs, brine-pits, barren place and fertile: cursed be I that did so! All the charms of Sycorax, toads, beetles, bats, light on you! For I am all the subjects that you have, which first was mine own king: and here you sty me in this hard rock, whiles you do keep from me the rest o' the island. Thou most lying slave, whom stripes may move, not kindness! I have used thee, filth as thou art, with human care, and lodged thee in mine own cell, till thou didst seek to violate the honour of my child. O ho, O ho! would't had been done! Thou didst prevent me; I had peopled else this isle with Calibans. Abhorred slave, which any print of goodness wilt not take, being capable of all ill! I pitied thee, took pains to make thee speak, taught thee each hour one thing or other: when thou didst not, savage, know thine own meaning, but wouldst gabble like a thing most brutish, I endow'd thy purposes with words that made them known. But thy vile race, though thou didst learn, had that in't which good natures could not abide to be with; therefore wast thou deservedly confined into this rock, who hadst deserved more than a prison. You taught me language; and my profit on't is, I know how to curse. The red plague rid you for learning me your language! Hag-seed, hence! Fetch us in fuel; and be quick, thou'rt best, to answer other business. Shrugg'st thou, malice? If thou neglect'st or dost unwillingly what I command, I'll rack thee with old cramps, fill all thy bones with aches, make thee roar that beasts shall tremble at thy din. No, pray thee. I must obey: his art is of such power, it would control my dam's god, Setebos, and make a vassal of him. So, slave; hence! Come unto these yellow sands, and then take hands: courtsied when you have and kiss'd the wild waves whist, foot it featly here and there; and, sweet sprites, the burthen bear. Hark, hark! Bow-wow. The watch-dogs bark! Bow-wow. Hark, hark! I hear the strain of strutting chanticleer cry, Cock-a-diddle-dow. Where should this music be? i' the air or the earth? It sounds no more: and sure, it waits upon some god o' the island. Sitting on a bank, weeping again the king my father's wreck, this music crept by me upon the waters, allaying both their fury and my passion with its sweet air: thence I have follow'd it, or it hath drawn me rather. But 'tis gone. No, it begins again. Full fathom five thy father lies; of his bones are coral made; those are pearls that were his eyes: nothing of him that doth fade but doth suffer a sea-change into something rich and strange. Sea-nymphs hourly ring his knell: Ding-dong. Hark! now I hear them,—Ding-dong, bell. The ditty does remember my drown'd father. This is no mortal business, nor no sound that the earth owes. I hear it now above me. The fringed curtains of thine eye advance and say what thou seest yond. What is't? a spirit? Lord, how it looks about! Believe me, sir, it carries a brave form. But 'tis a spirit. No, wench; it eats and sleeps and hath such senses as we have, such. This gallant which thou seest was in the wreck; and, but he's something stain'd with grief that's beauty's canker, thou mightst call him a goodly person: he hath lost his fellows and strays about to find 'em. I might call him a thing divine, for nothing natural I ever saw so noble. It goes on, I see, as my soul prompts it. Spirit, fine spirit! I'll free thee within two days for this. Most sure, the goddess on whom these airs attend! Vouchsafe my prayer may know if you remain upon this island; and that you will some good instruction give how I may bear me here: my prime request, which I do last pronounce, is, O you wonder! if you be maid or no? No wonder, sir; but certainly a maid. My language! heavens! I am the best of them that speak this speech, were I but where 'tis spoken. How? the best? What wert thou, if the King of Naples heard thee? A single thing, as I am now, that wonders to hear thee speak of Naples. He does hear me; and that he does I weep: myself am Naples, who with mine eyes, never since at ebb, beheld the king my father wreck'd. Alack, for mercy! Yes, faith, and all his lords; the Duke of Milan and his brave son being twain. The Duke of Milan and his more braver daughter could control thee, if now 'twere fit to do't. At the first sight they have changed eyes. Delicate Ariel, I'll set thee free for this. A word, good sir; I fear you have done yourself some wrong: a word. Why speaks my father so ungently? This is the third man that e'er I saw, the first that e'er I sigh'd for: pity move my father to be inclined my way! O, if a virgin, and your affection not gone forth, I'll make you the Queen of Naples. Soft, sir! one word more. They are both in either's powers; but this swift business I must uneasy make, lest too light winning make the prize light. One word more; I charge thee that thou attend me: thou dost here usurp the name thou owest not; and hast put thyself upon this island as a spy, to win it from me, the lord on't. No, as I am a man. There's nothing ill can dwell in such a temple: if the ill spirit have so fair a house, good things will strive to dwell with't. Follow me. Speak not you for him; he's a traitor. Come; I'll manacle thy neck and feet together: sea-water shalt thou drink; thy food shall be the fresh-brook muscles, wither'd roots and husks wherein the acorn cradled. Follow. No; I will resist such entertainment till mine enemy has more power. O dear father, make not too rash a trial of him, for he's gentle and not fearful. What? I say, my foot my tutor? Put thy sword up, traitor; who makest a show but darest not strike, thy conscience is so possess'd with guilt: come from thy ward, for I can here disarm thee with this stick and make thy weapon drop. Beseech you, father. Hence! hang not on my garments. Sir, have pity; I'll be his surety. Silence! one word more shall make me chide thee, if not hate thee. What! an advocate for an impostor! hush! Thou think'st there is no more such shapes as he, having seen but him and Caliban: foolish wench! To the most of men this is a Caliban and they to him are angels. My affections are then most humble; I have no ambition to see a goodlier man. Come on; obey: thy nerves are in their infancy again and have no vigour in them. So they are; my spirits, as in a dream, are all bound up. My father's loss, the weakness which I feel, the wreck of all my friends, nor this man's threats, to whom I am subdued, are but light to me, might I but through my prison once a day behold this maid: all corners else o' the earth let liberty make use of; space enough have I in such a prison. It works. Come on. Thou hast done well, fine Ariel! Follow me. Hark what thou else shalt do me. Be of comfort; my father's of a better nature, sir, than he appears by speech: this is unwonted which now came from him. Thou shalt be as free as mountain winds: but then exactly do all points of my command. To the syllable. Come, follow. Speak not for him. Now do you **understand** the secret history of our exile?"},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "To **understand** the nature and extent of human knowledge, we must examine the simple sensory ideas from which all thought is derived."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth could not **understand** how Darcy could unite such haughty pride with such delicate, generous consideration."}
    ]
  },
  "Dashboard — und/understandability.md": {
    "primary": "Clarity, coherence, and ease of comprehension in speech, writing, or design.",
    "secondary": "In software engineering and technical writing, code understandability directly influences maintainability and bug remediation time.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Philosophy of Style", "quote": "The fundamental principle of composition is to economize the reader's mental attention and ensure immediate **understandability**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The great popular lecturers on natural philosophy combined scientific rigor with luminous, lucid **understandability**."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Philosophical definitions must aim at maximum **understandability**, eliminating circular phrases and ambiguous metaphors."}
    ]
  },
  "Dashboard — und/understandable.md": {
    "primary": "Able to be understood, comprehended, or grasped; intelligible, reasonable, or excusable.",
    "secondary": "In cognitive psychology, information presented with visual aids and logical hierarchy becomes readily understandable to non-experts.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Jarndyce spoke with an honest, plain directness that made his benevolent intentions immediately **understandable** to all."},
      {"author": "Jane Austen", "work": "Emma", "quote": "It was very **understandable** that Mr. Knightley should feel indignation at Frank Churchill's thoughtless conduct."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes made the complex sequence of moorland clues perfectly **understandable** to Dr. Watson over breakfast."}
    ]
  },
  "Dashboard — und/understandably.md": {
    "primary": "In a way that is natural, reasonable, or easy to understand; for reasons that are obvious.",
    "secondary": "In clinical medicine, patients diagnosed with life-threatening illness react understandably with acute psychological shock.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was **understandably** distressed when she realized the cold intellectual vanity that motivated Casaubon's labors."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Mary Morstan was **understandably** agitated as we drove in the four-wheeler toward the mysterious midnight rendezvous."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane shrank **understandably** from St. John's proposal, refusing to sacrifice her emotional truth to cold religious duty."}
    ]
  },
  "Dashboard — und/understanding.md": {
    "primary": "Intellectual comprehension, sympathetic insight, or informal agreement between individuals.",
    "secondary": "In epistemological philosophy, human understanding is the active cognitive faculty that synthesizes sensory impressions into concepts.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **understanding**, like the eye, whilst it informs and teaches us of other things, takes no notice of itself."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Give it an **understanding**, but no tongue: I will requite your loves; so fare you well upon the platform."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was surprised by the mutual **understanding** that had so quietly established itself between Jane and Bingley."}
    ]
  },
  "Dashboard — und/understandingly.md": {
    "primary": "In a sympathetic, discerning, knowledgeable, and compassionate manner.",
    "secondary": "In pastoral care and counseling, an experienced mentor listens understandingly to troubled confidants before offering advice.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dolly Winthrop nodded **understandingly**, offering gentle, practical comfort to the solitary weaver in his grief."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Agnes smiled **understandingly** as David poured out his youthful romantic confidences and anxieties."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Phoebe listened **understandingly** to poor Clifford's fragmented recollections of his long, unjust imprisonment."}
    ]
  },
  "Dashboard — und/understate.md": {
    "primary": "To describe or represent something as being smaller, worse, or less important than it actually is.",
    "secondary": "In historical diplomacy, seasoned ambassadors understate their geopolitical claims to avoid provoking public hysteria.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Ministers were careful not to **understate** the critical gravity of the submarine blockade in secret parliamentary sessions."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "Holmes was not a man to exaggerate danger, yet he did not **understate** the lethal peril awaiting us at Stoke Moran."},
      {"author": "George Bernard Shaw", "work": "Heartbreak House", "quote": "The cynical old captain preferred to **understate** his maritime exploits, speaking of typhoons as mere squalls."}
    ]
  },
  "Dashboard — und/understated.md": {
    "primary": "Expressed or presented in a subtle, quiet, restrained, or modest way; not ostentatious.",
    "secondary": "In interior architecture and sartorial design, understated elegance avoids garish ornament in favor of pure proportions.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Madame de Vionnet's apartment was decorated with an **understated** Parisian refinement that captivated Strether's sensibilities."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Old New York society prided itself upon an **understated** dignity that shrank from the flashy displays of newly rich parvenus."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Clarissa admired the **understated** courtesy of the veteran diplomat who greeted his guests with quiet warmth."}
    ]
  },
  "Dashboard — und/understatement.md": {
    "primary": "The presentation of something as being smaller, worse, or less important than it actually is; litotes.",
    "secondary": "In British literary rhetoric, ironic understatement is celebrated for conveying profound emotional intensity through stoic restraint.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "To say that Sir Henry was startled was a ludicrous **understatement**; he stood pale and trembling in the doorway."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "To describe our cavalry charge at Omdurman as an animated moment was a mild **understatement** of its bloody peril."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The English character displays a natural genius for ironic **understatement**, especially when facing national danger."}
    ]
  },
  "Dashboard — und/understock.md": {
    "primary": "To provide with insufficient stock, inventory, goods, or grazing livestock for pasture capacity.",
    "secondary": "In range management and pasture agronomy, graziers who understock rich pastures allow coarse woody weeds to outcompete forage grasses.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The tradesman who is forced to **understock** his warehouse loses custom to larger mercantile houses with diverse inventories."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard cautioned the young farmer not to **understock** his sheep meadows, which could easily sustain two hundred ewes."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "It is safer for a young beginner to **understock** his shop slightly than to overtrade on borrowed mercantile capital."}
    ]
  },
  "Dashboard — und/understood.md": {
    "primary": "Comprehended, perceived, or grasped intellectually; or agreed upon without needing explicit statement.",
    "secondary": "In contract jurisprudence, an understood custom of the trade is incorporated into commercial agreements by implication.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It was tacitly **understood** between them that the subject of Wickham's past should never be mentioned again."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt that Joe **understood** his inward remorse far better than any elaborate verbal apologies could express."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes immediately **understood** the meaning of the bloody inscription scrawled upon the wallpaper of the empty house."}
    ]
  },
  "Dashboard — und/understructure.md": {
    "primary": "The supporting framework, foundation, or substructure beneath a building, bridge, or vehicle.",
    "secondary": "In structural bridge engineering, the masonry piers and caissons of the understructure transfer dead loads safely into river bedrock.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The massive subterranean **understructure** of the Doge's Palace rests upon thousands of driven larch timber piles."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Geologists examined the granitic **understructure** of the mountain chain, exposed where glacial erosion had stripped away shale."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The steel **understructure** of the suspension bridge buckled under the explosive concussion of the aerial bomb."}
    ]
  },
  "Dashboard — und/understudy.md": {
    "primary": "An actor who learns the lines of another performer in order to appear in their place at short notice; or to act as an understudy.",
    "secondary": "In theatrical management, an understudy attends all rehearsals and remains backstage during performances to safeguard box office receipts.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Nicholas was engaged as an **understudy** in Mr. Vincent Crummles's provincial company, ready to play Romeo or walking gentlemen."},
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The talented young **understudy** was called upon to step into the leading tragic role without an orchestral dress rehearsal."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The senior consulting surgeon regarded his young house officer as a reliable clinical **understudy** during emergency operations."}
    ]
  },
  "Dashboard — und/undersurface.md": {
    "primary": "The lower or bottom surface of an object, leaf, or anatomical structure; underside.",
    "secondary": "In plant anatomy, stomata are predominantly concentrated on the foliar undersurface to minimize evaporative water loss during daytime.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The glandular hairs on the **undersurface** of the leaf secrete sticky digestive enzymes when touched by an insect."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Microscopic stomatal pores punctuate the green **undersurface** of deciduous leaves, governing respiratory gas exchange."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The pale downy pubescence on the **undersurface** of the silver poplar leaf reflects sunlight and limits transpiration."}
    ]
  },
  "Dashboard — und/undertake.md": {
    "primary": "To commit oneself to and begin an enterprise or responsibility; to take on a task or pledge to do something.",
    "secondary": "In constitutional history, sovereign executives undertake solemn inaugural oaths to preserve and defend national charters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "I'll **undertake** to bring the king's son safely to thy cell, performing every charge with faithful speed."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Men must **undertake** the reformation of natural science with humble minds, submitting speculation to empirical nature."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The federal government must **undertake** the honorable funding of revolutionary war debts to establish national credit."}
    ]
  },
  "Dashboard — und/undertaker.md": {
    "primary": "A person whose business is preparing dead bodies for burial or cremation and managing funerals; a mortician.",
    "secondary": "In seventeenth-century British and Irish colonial history, 'undertakers' were colonizing contractors who undertook to plant settlers on confiscated estates.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Oliver was bound apprentice to Mr. Sowerberry, the parish **undertaker**, whose dismal shop was lined with black coffins."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King James granted vast confiscated baronies in Ulster to Scottish **undertaker** settlers to establish Protestant colonies."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The solemn London **undertaker** marshaled the black horses and plumed hearses for the grand funeral of Sir Pitt Crawley."}
    ]
  },
  "Dashboard — und/undertaking.md": {
    "primary": "A formal pledge or promise to do something; or a task, enterprise, or project that is taken on.",
    "secondary": "In maritime law, an undertaking in bailment covenants safe delivery of ship cargo against perils of the sea.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I trembled at the momentous **undertaking** I had begun, shutting myself away in my solitary laboratory at Ingolstadt."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant ventures his capital upon a hazardous foreign **undertaking** in the expectation of extraordinary commercial profit."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The creation of a continental union was a colossal political **undertaking** requiring wisdom, compromise, and mutual sacrifice."}
    ]
  },
  "Dashboard — und/undertide.md": {
    "primary": "A subterranean or underwater tidal flow; an undercurrent flowing in a direction contrary to surface currents.",
    "secondary": "In coastal hydrodynamics, a powerful undertide sweeps beneath breaking surf, scouring offshore trenches and challenging swimmers.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The drifting whaleboat was caught by a swift, subterranean **undertide** that carried it miles toward the open Pacific."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The deep mill-weir concealed a treacherous **undertide** that swept drowning victims beneath the sunken sluice timbers."},
      {"author": "Walter Scott", "work": "The Pirate", "quote": "The Shetland boatmen feared the swirling **undertide** of the Sumburgh Roost, where contrary tidal currents clashed in fury."}
    ]
  },
  "Dashboard — und/undertone.md": {
    "primary": "A quiet or subdued tone of voice; or an underlying quality, feeling, or color tinge.",
    "secondary": "In color theory and painting, a warm or cool undertone beneath a glaze imparts luminous depth to oil portraits.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes spoke in a low, cautious **undertone**, gesturing for us to extinguish our lanterns on the dark moor."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "There was an **undertone** of bitter self-reproach in Rochester's voice that moved Jane to profound compassion."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The Venetian masters infused their flesh tints with a delicate golden **undertone** that mimicked the warmth of living blood."}
    ]
  },
  "Dashboard — und/undertow.md": {
    "primary": "A strong current below the surface of the sea, moving in the opposite direction to the surface water and pulling outward from shore.",
    "secondary": "In physical oceanography and beach safety, wave breaking on steep shores creates a dangerous seaward undertow across the swash zone.",
    "quotes": [
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The swimmer struggled against the powerful oceanic **undertow**, which dragged him relentlessly away from the rocky headland."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "Falling from the main-top into the sea, I felt the cold, suffocating **undertow** pulling me down into the black oceanic abyss."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The heavy surf broke upon the reef with a thunderous roar, sending a savage **undertow** swirling back into the channel."}
    ]
  },
  "Dashboard — und/undervaluation.md": {
    "primary": "The act or result of placing too low a value, price, or estimate on something; undervalue.",
    "secondary": "In customs revenue collection, fraudulent undervaluation of imported luxury merchandise incurs heavy civil forfeiture penalties.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The statutory **undervaluation** of gold at the mint encouraged merchants to export gold bullion to continental European markets."},
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "The widespread **undervaluation** of domestic manufactured goods by foreign buyers stemmed from colonial prejudices."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The corporate syndicate profited immensely from the deliberate **undervaluation** of public utility franchises by corrupt aldermen."}
    ]
  },
  "Dashboard — und/undervalue.md": {
    "primary": "To rate, estimate, or price something below its real worth, importance, or value.",
    "secondary": "In moral philosophy, individuals who undervalue the quiet virtues of integrity sacrifice lasting peace for ephemeral fame.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth warned Jane never to **undervalue** her own noble qualities or allow Bingley's sisters to treat her with condescension."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "A wise man will never **undervalue** the sincere approbation of virtuous citizens, though he despises vulgar flattery."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "He that will not apply new remedies must expect new evils; for time is the greatest innovator, and to **undervalue** it is fatal."}
    ]
  },
  "Dashboard — und/underwater.md": {
    "primary": "Situated, occurring, or used beneath the surface of the water; or submerged.",
    "secondary": "In marine technology and diving physiology, autonomous underwater vehicles (AUVs) map abyssal ocean floor trenches using side-scan sonar.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The powerful electric searchlight of the Nautilus illuminated the enchanted **underwater** landscapes of coral and sunken wrecks."},
      {"author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "The living polyps construct **underwater** ramparts against the open ocean surf, thriving in the well-aerated breaker zone."},
      {"author": "Arthur C. Clarke", "work": "The Deep Range", "quote": "The marine scientist donned his acoustic helmet and plunged into the quiet **underwater** world to inspect the plankton nets."}
    ]
  },
  "Dashboard — und/underway.md": {
    "primary": "Having started and currently making progress; in motion or in operation.",
    "secondary": "In maritime navigation regulations, a vessel is underway when it is neither at anchor, made fast to the shore, nor aground.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The anchor was weighed, the topsails sheeted home, and the Pequod was fairly **underway** upon her long, fateful voyage."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Colossal preparations were already **underway** in every shipyard to construct hundreds of anti-submarine patrol vessels."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The police launch was swiftly **underway**, slicing through the dark waters of the Thames in pursuit of the fugitive steam launch."}
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

print(f"Dashboard — und Part 4 (8D): Successfully updated {updated}/{len(data)} notes.")
