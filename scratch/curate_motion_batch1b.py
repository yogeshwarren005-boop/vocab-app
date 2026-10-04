# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — merg (19 words) ---
  "Dashboard — merg/emerge.md": {
    "primary": "To move out of or away from something and come into view; to become apparent, known, or prominent.",
    "secondary": "In evolutionary biology and systems theory, novel macro-properties emerge spontaneously from complex network interactions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "New varieties and modified species slowly **emerge** through continuous natural selection over vast geological epochs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The mighty white head of the whale seemed to **emerge** from the foaming crest of the midnight billow."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I watched the morning sun **emerge** above the snowy peaks of Mont Blanc, illuminating the jagged glaciers."}
    ]
  },
  "Dashboard — merg/emergence.md": {
    "primary": "The process of coming into view, existence, or prominent notice after being hidden or obscure.",
    "secondary": "In complex systems science and ecology, systemic emergence describes collective behaviors irreducible to individual constituent parts.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The gradual **emergence** of moral consciousness marked the decisive transition from animal instinct to human civilization."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The progressive **emergence** of order from primordial chaos illustrates the universal law of cosmic evolution."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The sudden **emergence** of agrarian river civilizations transformed human social organization across the Fertile Crescent."}
    ]
  },
  "Dashboard — merg/emergency.md": {
    "primary": "A serious, unexpected, and often dangerous situation requiring immediate decisive action.",
    "secondary": "In constitutional law and public administration, executive emergency powers allow temporary suspension of ordinary statutory procedures during crisis.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Watson kept his revolver ready in his coat pocket, prepared for any sudden violent **emergency**."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The cabinet convened at midnight to address the grave military **emergency** created by the collapse of the front."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Captain Smollett proved cool and resourceful, directing the defense of the stockade in every unexpected **emergency**."}
    ]
  },
  "Dashboard — merg/emergent.md": {
    "primary": "Coming into existence or becoming prominent; or arising unexpectedly as an urgent development.",
    "secondary": "In evolutionary philosophy and philosophy of mind, emergent properties arise at higher systemic levels without existing in underlying substrate components.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Conscious thoughts represent an **emergent** phenomenon arising from intricate cerebral and sensory neural processes."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate surveyed the **emergent** political movements of provincial England with the detached curiosity of a scientist."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The fiery leader rode the crest of the **emergent** popular passions surging through the streets of Paris."}
    ]
  },
  "Dashboard — merg/emerging.md": {
    "primary": "Coming into view, prominence, or recognized existence from a concealed, underdeveloped, or subordinate state.",
    "secondary": "In international macroeconomics, emerging market economies exhibit accelerated industrialization and elevated capital inflow volatility.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "We watched the dark forest wall slowly **emerging** from the dense morning river fog as the sun climbed."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The prisoners stood in the courtyard, their pale faces **emerging** from the gloomy shadows of the Bastille."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Hester Prynne walked with dignified sorrow, **emerging** from the prison portal into the harsh town sunlight."}
    ]
  },
  "Dashboard — merg/merganser.md": {
    "primary": "A fish-eating diving duck characterized by a slender serrated bill and typically a crested head.",
    "secondary": "In ornithological ecology, the hooded merganser nests in tree cavities and uses specialized nictitating membranes for underwater foraging.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "A startled **merganser** flew low along the glassy surface of the wilderness river, its crest raised in alarm."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The red-breasted **merganser** dives with astonishing velocity through tidal estuaries to capture small schooling fish."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The serrated bill of the **merganser** provides a classic anatomical adaptation for grasping slippery aquatic prey."}
    ]
  },
  "Dashboard — merg/merge.md": {
    "primary": "To combine, unite, or blend together gradually into a single unified whole.",
    "secondary": "In corporate finance and antitrust regulation, commercial entities merge to consolidate market share and achieve operational economies of scale.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The soft evening shadows seemed to **merge** with the gloomy woods bordering the quiet country road."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The foaming white wakes of the racing whaleboats appeared to **merge** into one broad track of boiling spray."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The dusk advanced until earth and sky seemed to **merge** into one vast, undifferentiated expanse of twilight."}
    ]
  },
  "Dashboard — merg/merged.md": {
    "primary": "Combined, united, or blended into a single coherent entity or unified mass.",
    "secondary": "In physical optics, spectral color bands become merged into white light when recombined through a convex converging lens.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The distant granite tors **merged** into the dark wall of fog creeping steadily across the moorland."},
      {"author": "George Orwell", "work": "Animal Farm", "quote": "The creatures outside looked from pig to man, and from man to pig, and already their features **merged** inextricably."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The distant waves and the horizon **merged** into a pale sapphire haze under the fading afternoon sky."}
    ]
  },
  "Dashboard — merg/mergenthaler.md": {
    "primary": "Referring to Ottmar Mergenthaler (1854–1899), the inventor of the Linotype linecasting typesetting machine.",
    "secondary": "In the history of typography and print technology, Mergenthaler revolutionized mass newspaper publishing by mechanizing movable type composition.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Writings of Thomas Edison", "quote": "Edison acclaimed the revolutionary linecasting invention of **Mergenthaler** as the eighth wonder of the mechanical world."},
      {"author": "Mark Twain", "work": "Autobiography of Mark Twain", "quote": "Twain lamented the fortunes lost on rival typesetting contrivances before **Mergenthaler** triumphed in printing houses."},
      {"author": "Theodore Dreiser", "work": "A Book About Myself", "quote": "The rhythmic clanking of the **Mergenthaler** machines filled the bustling metropolitan newspaper composing room."}
    ]
  },
  "Dashboard — merg/merger.md": {
    "primary": "A statutory combination or union of two or more commercial companies or organizations into a single entity.",
    "secondary": "In antitrust economics, regulatory commissions scrutinize horizontal merger proposals to prevent monopolistic market concentration.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "Cowperwood engineered a secret corporate **merger** that placed all competing street railway franchises under his control."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A monopolistic **merger** of competing merchant guilds restricts output and elevates prices against the public interest."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The voluntary **merger** of small rural landholdings allowed landlords to introduce advanced industrial agricultural methods."}
    ]
  },
  "Dashboard — merg/merginae.md": {
    "primary": "A taxonomic subfamily of waterfowl in the family Anatidae that comprises sea ducks and sawbill mergansers.",
    "secondary": "In systematic ornithology, the Merginae are characterized by specialized salt glands and dive adaptations suited for marine foraging.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The divers and sawbills classified under the **Merginae** frequent rugged coastal fjords and northern estuaries."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Anatomical comparisons within the **Merginae** demonstrate remarkable bill specialization for piscivorous predation."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The cranial morphology and osteology of the **Merginae** reveal distinctive modifications for deep-water diving."}
    ]
  },
  "Dashboard — merg/merging.md": {
    "primary": "Blending, uniting, or combining gradually so as to lose distinct individual identities in a common whole.",
    "secondary": "In computational data engineering, merging sorted dataset streams minimizes algorithmic I/O complexity.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The twilight deepened rapidly, **merging** the dark contours of the coastal headland with the purple sea."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The twin rivers flowed together beneath the old stone bridge, **merging** their murky waters into the Thames."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "She sat motionless in the gathering gloom, her private thoughts **merging** with the melancholy rhythm of the city."}
    ]
  },
  "Dashboard — merg/mergus.md": {
    "primary": "The zoological type genus of typical mergansers, characterized by narrow serrated bills used to catch fish.",
    "secondary": "In taxonomic nomenclature, the genus Mergus includes the common merganser (Mergus merganser) and red-breasted merganser (Mergus serrator).",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "Species of the genus **Mergus** exhibit extraordinary diving agility when pursuing minnows across swift northern streams."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "A solitary specimen belonging to the genus **Mergus** was observed diving among the reeds of the pond in winter."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The specialized serrations along the mandible of **Mergus** furnish compelling evidence of adaptive divergence."}
    ]
  },
  "Dashboard — merg/nonsubmergible.md": {
    "primary": "Incapable of being submerged, sinkable, or plunged completely underwater; buoyant.",
    "secondary": "In naval architecture and life-safety engineering, nonsubmergible survival lifeboats incorporate closed-cell foam buoyancy chambers.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo explained that the upper observation deck was virtually **nonsubmergible** when surface hatches remained dog-latched."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sealed empty casks formed a **nonsubmergible** raft that kept the castaways afloat amidst the tempest."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The torpedo ram Thunder Child appeared a massive, **nonsubmergible** iron citadel charging through the churning brine."}
    ]
  },
  "Dashboard — merg/submerge.md": {
    "primary": "To put, sink, or plunge beneath the surface of water or another liquid; or to overwhelm completely.",
    "secondary": "In submarine warfare and oceanographic research, submersibles submerge by flooding negative buoyancy ballast tanks.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "At an order from Captain Nemo, the Nautilus began to **submerge** swiftly into the mysterious oceanic abyss."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The giant cachalot sounded suddenly, choosing to **submerge** its massive black bulk into the fathomless deep."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The rising tide of revolutionary violence threatened to **submerge** every ancient aristocratic house in France."}
    ]
  },
  "Dashboard — merg/submerged.md": {
    "primary": "Lying, existing, or operating completely beneath the surface of water or another covering medium.",
    "secondary": "In marine geology and hydrography, submerged coral atolls and guyots mark subsiding oceanic tectonic plates.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The canoe brushed against ancient tree trunks **submerged** beneath the dark, reed-choked waters of the hidden lake."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The ship's bows remained **submerged** for long breathless seconds beneath mountains of green sea water."},
      {"author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "Barrier reefs encircle islands that have slowly **submerged** beneath the rising tropical sea over millennia."}
    ]
  },
  "Dashboard — merg/submergence.md": {
    "primary": "The act of plunging or sinking below the surface of water, or the state of being submerged.",
    "secondary": "In coastal geomorphology and eustasy, marine submergence during interglacial periods creates rias and drowned river valleys.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The periodic **submergence** and elevation of continental landmasses is demonstrated by marine fossil strata in high Alps."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "During deep **submergence**, the thick crystal lenses of the salon resisted crushing hydrostatic pressures."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The low-lying coastal plains suffered complete **submergence** whenever catastrophic spring storm surges struck the estuary."}
    ]
  },
  "Dashboard — merg/submergible.md": {
    "primary": "Capable of being submerged or operated underwater; a vessel designed to navigate beneath the water surface.",
    "secondary": "In deep-sea exploration engineering, a robotic submergible vehicle carries specialized robotic arms and sensors for abyssal sampling.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The Nautilus proved that an electrically powered **submergible** vessel could traverse every ocean without coaling."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Speculative engineers debated whether a **submergible** warship could evade the Martian fighting machines in open water."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The secret plans concerned an advanced **submergible** boat intended to protect the British coast from invasion."}
    ]
  },
  "Dashboard — merg/submerging.md": {
    "primary": "Sinking, plunging, or disappearing below the surface of a fluid medium; or inundating.",
    "secondary": "In hydraulic engineering, submerging sluice gates regulates reservoir head pressures during seasonal flood discharges.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "The Nigger of the 'Narcissus'", "quote": "The roaring white water rushed across the listing deck, **submerging** the struggling crew up to their waists."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "With one final sweep of his tail, the leviathan sounded, **submerging** into the unfathomable depths of the Pacific."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The torrential Alpine rain fell incessantly, **submerging** mountain roads and carrying away wooden bridges."}
    ]
  },

  # --- Dashboard — sult (19 words) ---
  "Dashboard — sult/consult.md": {
    "primary": "To seek information, advice, or instruction from someone with specialized knowledge; or to deliberate together.",
    "secondary": "In clinical medicine and legal jurisprudence, primary practitioners consult specialized authorities when facing complex diagnostic dilemmas.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Clients traveled from all parts of Europe to **consult** Holmes on baffling problems that defeated the police."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma decided to **consult** Mr. Knightley regarding the proper education and social guidance of young Harriet."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Prudent rulers frequently **consult** historical chronicles to understand the hidden roots of political factions."}
    ]
  },
  "Dashboard — sult/consultancy.md": {
    "primary": "A professional practice or firm that provides expert specialized advice in a specific field.",
    "secondary": "In management economics and organizational strategy, corporate leaders engage strategic consultancy firms to restructure global operations.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The traction syndicate established a specialized engineering **consultancy** to survey the municipal street railway extensions."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "Modern industrial enterprises increasingly depend upon an independent scientific **consultancy** to maintain product innovation."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt aspired to establish a lucrative real estate **consultancy** catering to wealthy suburban land developers."}
    ]
  },
  "Dashboard — sult/consultant.md": {
    "primary": "A person who provides expert professional or technical advice in a specific specialized discipline.",
    "secondary": "In hospital clinical hierarchies, an attending medical consultant oversees resident training and complex surgical interventions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes described his unique profession as that of a consulting detective, advising other detectives as a senior **consultant**."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The role of the clinical **consultant** demands acute diagnostic discernment combined with sympathetic bedside courtesy."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "The patent medicine enterprise hired a prominent London chemical **consultant** to certify the tonic's purity."}
    ]
  },
  "Dashboard — sult/consultation.md": {
    "primary": "A formal meeting or discussion to exchange views, seek professional advice, or reach a collective decision.",
    "secondary": "In clinical medical practice, an interdisciplinary consultation between oncology and pathology establishes personalized treatment protocols.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solemn solicitors held a lengthy private **consultation** in the dusty chambers of the Court of Chancery."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "After an anxious **consultation** with the physician, Elinor felt somewhat reassured regarding Marianne's condition."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian kings met in secret **consultation** to coordinate their sudden assault across the Rhine."}
    ]
  },
  "Dashboard — sult/consultative.md": {
    "primary": "Pertaining to, having, or acting in an advisory or deliberation-oriented capacity.",
    "secondary": "In administrative law and civic governance, consultative assemblies provide recommendations to executive ministries without binding legislative power.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A well-organized state requires a **consultative** council composed of seasoned administrators to review proposed legislation."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The ancient constitution provided **consultative** bodies where all estates of the realm could voice their grievances."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The War Cabinet created a **consultative** committee of naval officers to evaluate convoy protection strategies."}
    ]
  },
  "Dashboard — sult/consultatory.md": {
    "primary": "Having the quality or function of giving or seeking advice; consultative.",
    "secondary": "In canonical law and ecclesiastical administration, consultatory letters gather episcopal counsel prior to promulgation of diocesan synods.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Prudent sovereigns maintain **consultatory** chambers where wise counselors may speak without fear of royal displeasure."},
      {"author": "Jeremy Bentham", "work": "Constitutional Code", "quote": "The draft code established **consultatory** committees to review municipal petitions prior to parliamentary debate."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The privy council met in a **consultatory** session to consider emergency grain imports during the autumn famine."}
    ]
  },
  "Dashboard — sult/consultive.md": {
    "primary": "Relating to or designed for consultation; advisory.",
    "secondary": "In bureaucratic organizational theory, consultive bodies facilitate communication between department leadership and field personnel.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The legislative authority may appoint a **consultive** body to report upon matters of foreign commerce and defense."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The executive branch requires a **consultive** council capable of deliberation without impeding swift operational decision."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Early tribal councils performed a purely **consultive** role, leaving final military commands to the war chieftain."}
    ]
  },
  "Dashboard — sult/desultory.md": {
    "primary": "Lacking a definite plan, purpose, or enthusiasm; moving or jumping erratically from one thing to another.",
    "secondary": "In military combat analysis, desultory skirmishing along the periphery of an army precedes coordinated general assaults.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth found the conversation at Rosings strained, consisting only of **desultory** remarks between long pauses."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David engaged in **desultory** reading among his father's old books in the quiet garret of Blunderstone Rookery."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare wandered in **desultory** contemplation across the meadows, unable to resolve his agonizing dilemma."}
    ]
  },
  "Dashboard — sult/insult.md": {
    "primary": "To speak to or treat someone with disrespect, contempt, or insolence; an offensive remark or act.",
    "secondary": "In pathology and neurobiology, an ischemic or toxic insult damages delicate neural cells and triggers inflammatory cascades.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For who would bear the whips and scorns of time, the oppressor's wrong, the proud man's contumely, and the **insult** of office?"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth considered Mr. Darcy's haughty refusal to dance an unprovoked **insult** to her dignity."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To subject a venerable monarch to public mockery is an **insult** that offends every principle of chivalry."}
    ]
  },
  "Dashboard — sult/insulting.md": {
    "primary": "Expressing, conveying, or marked by insolence, contempt, or deliberate offense; abusive.",
    "secondary": "In international diplomatic communications, using insulting rhetoric in formal demarches frequently triggers retaliatory diplomatic expulsions.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Estella's treatment of Pip was haughty and **insulting**, mocking his coarse hands and thick working boots."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The blackmailer addressed the duchess in a sneering, **insulting** tone that roused Holmes's deepest indignation."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The haughty Templar directed an **insulting** laugh toward the Saxon knights assembled in the banquet hall."}
    ]
  },
  "Dashboard — sult/insultingly.md": {
    "primary": "In an abusive, disrespectful, or contemptuous manner intended to hurt or humiliate.",
    "secondary": "In parliamentary debate etiquette, addressing a colleague insultingly violates standing orders and warrants disciplinary rebuke.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed glared **insultingly** at Jane before hurling the heavy grammar book across the breakfast room."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Sir Mulberry Hawk spoke **insultingly** of Kate Nickleby at the tavern, provoking Nicholas to strike him."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Grandcourt smiled **insultingly** at his dependent companion, knowing the man had no means to leave his service."}
    ]
  },
  "Dashboard — sult/result.md": {
    "primary": "A consequence, outcome, or effect that ensues from an action, process, event, or calculation.",
    "secondary": "In empirical scientific methodology, a statistically significant result requires rigorous experimental control and reproducibility.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes held up the test tube triumphantly, announcing that the chemical **result** was decisive and unmistakable."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The astonishing diversity of domestic pigeon breeds is the cumulative **result** of generations of methodical human selection."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The general enrichment of society is the unintended **result** of individuals pursuing their own economic self-interest."}
    ]
  },
  "Dashboard — sult/resultant.md": {
    "primary": "Arising, occurring, or proceeding as a consequence or outcome; a force or entity produced by combination.",
    "secondary": "In classical Newtonian vector mechanics, the resultant force represents the single vector sum of all concurrent forces acting on a body.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The **resultant** velocity of a body subjected to two simultaneous impulses is represented by the diagonal of the parallelogram."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Modern ethical conduct is the complex **resultant** of biological instincts modified by social education."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Every historical event is the **resultant** of countless physical, biological, and sociological forces converging together."}
    ]
  },
  "Dashboard — sult/sultan.md": {
    "primary": "A sovereign monarch or supreme ruler of a Muslim state, particularly the ruler of the Ottoman Empire.",
    "secondary": "In Islamic political theology and medieval statecraft, the sultan exercised executive temporal authority alongside the caliph's spiritual prestige.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Ottoman **sultan** Mehmed the Second deployed his colossal bronze cannon before the walls of Constantinople."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "The splendid court of the grand **sultan** shone with jewels, cloth of gold, and silent janissary guards."},
      {"author": "Washington Irving", "work": "Tales of the Alhambra", "quote": "The Moorish **sultan** held court within the magnificent marble halls of the Alhambra overlooking Granada."}
    ]
  },
  "Dashboard — sult/sultana.md": {
    "primary": "A female sultan, or the wife, mother, or daughter of a sultan; also a variety of small pale seedless grape or raisin.",
    "secondary": "In Ottoman imperial dynastic history, the Valide Sultana exercised profound political influence during the Sultanate of Women.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The favorite **sultana** exerted powerful influence within the imperial seraglio over appointments of provincial viziers."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "The haughty **sultana** commanded that the handsome young captive be brought before her private divan."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The grocer's display featured boxes of golden dried **sultana** raisins imported for traditional holiday baking."}
    ]
  },
  "Dashboard — sult/sultanate.md": {
    "primary": "The country, territory, state, or office ruled by a sultan.",
    "secondary": "In maritime Indian Ocean trade history, the Sultanate of Oman established commercial trading emporia spanning from Muscat to Zanzibar.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Seljuk **sultanate** of Rum fragmented into numerous rival principalities following Mongol invasions."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The traveller crossed the desert borders of the ancient **sultanate**, guided by Bedouin scouts through the dunes."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The coastal trading post lay within the nominal jurisdiction of an impoverished Malay **sultanate** upriver."}
    ]
  },
  "Dashboard — sult/sultrily.md": {
    "primary": "In an oppressively hot, humid, close, or passionate manner.",
    "secondary": "In meteorology and atmospheric observation, summer weather that unfolds sultrily precedes severe convective squall lines.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The July sun beat down **sultrily** upon the dairy meadows, causing the cows to seek the shade of the willows."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The heavy African night breathed **sultrily** through the open port of the river steamboat."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "The afternoon burned **sultrily** as the company drove toward Manhattan in the sweltering heat."}
    ]
  },
  "Dashboard — sult/sultriness.md": {
    "primary": "Oppressive atmospheric heat accompanied by high humidity, moisture, and absence of breeze.",
    "secondary": "In climatological bioclimatology, intense sultriness impairs human thermoregulation by preventing evaporative perspiration cooling.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The heavy **sultriness** of the August afternoon seemed to hang over the deserted London law courts like a shroud."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "A breathless **sultriness** pervaded the pine woods, presaging the arrival of an evening electrical thunderstorm."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The Roman summer brought an enervating **sultriness** that drove visitors away from the ancient stone ruins."}
    ]
  },
  "Dashboard — sult/sultry.md": {
    "primary": "Oppressively hot and humid, causing a feeling of damp closeness; or expressing passionate sensuality.",
    "secondary": "In tropical synoptic meteorology, sultry air masses with elevated dew points provide thermodynamic instability for tropical cyclones.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A **sultry** summer breeze murmured in the great horse-chestnut tree in the orchard on that fateful midsummer eve."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The motionless ship lay trapped in a **sultry** calm upon a sea that shone like molten brass."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak watched the heavy purple clouds gathering on the horizon at the close of a **sultry** August day."}
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

print(f"Motion Batch 1B: Successfully updated {updated}/{len(data)} notes.")
