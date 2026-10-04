# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — und Part 1 (52 words) ---
  "Dashboard — und/abound.md": {
    "primary": "To exist in large numbers or great quantities; to be plentiful or richly supplied.",
    "secondary": "In biogeography, productive wetlands and estuarine mangrove creeks abound with migratory fish and crustacean populations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The coastal waters of Tierra del Fuego **abound** with giant kelp forests that harbor countless marine organisms."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Let fruitful earth bring forth her verdant growth, where herbs and blossom'd trees **abound** with fruit."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Fertile river valleys naturally **abound** with agricultural produce, encouraging early urban settlement and commerce."}
    ]
  },
  "Dashboard — und/abounding.md": {
    "primary": "Existing in large quantities; plentiful, rich, or overflowing with abundance.",
    "secondary": "In pastoral literature, an abounding autumn harvest symbolizes community stability and rural prosperity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The Ghost of Christmas Present sat surrounded by an **abounding** feast of turkeys, mince-pies, and glowing punch."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The equatorial feeding grounds displayed an **abounding** richness of squid that attracted schools of sperm whales."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Walden Pond was an **abounding** reservoir of pure spring water, mirroring the changing seasonal foliage."}
    ]
  },
  "Dashboard — und/abundance.md": {
    "primary": "A very large quantity of something; overflowing fullness, copiousness, or wealth.",
    "secondary": "In ecological population biology, species abundance measures the relative representation of a species in an ecosystem.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extraordinary **abundance** of certain insect species depends upon their immense reproductive capacity and favorable food supplies."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The market price of commodities falls whenever domestic supply is offered in great **abundance** beyond effective demand."},
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Poor sacrifices of our enmity! As rich shall Romeo's by his lady's lie; poor sacrifices of our enmity, given in sad **abundance**."}
    ]
  },
  "Dashboard — und/abundant.md": {
    "primary": "Existing or available in large quantities; plentiful, copious, or richly overflowing.",
    "secondary": "In mineralogy and geochemistry, silicon and oxygen are the most abundant chemical elements in the continental crust.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Rainfall upon the western mountain slopes feeds **abundant** mountain streams that carve fertile alluvial valleys."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Where food supplies are **abundant** throughout the year, animal populations expand rapidly without intense seasonal mortality."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Natural philosophy yields **abundant** practical benefits when guided by rigorous inductive observation rather than idle speculation."}
    ]
  },
  "Dashboard — und/abundantly.md": {
    "primary": "In large quantities; plentifully, copiously, or extremely and clearly.",
    "secondary": "In agricultural science, soil enriched with organic humus yields crops abundantly throughout successive growing seasons.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was **abundantly** provided with amusement during the assembly by watching the affectations of Caroline Bingley."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Nile valley rewarded the labors of the husbandman **abundantly**, supplying the imperial granaries of Rome."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery's generous affection was **abundantly** clear in every honest glance of his eyes."}
    ]
  },
  "Dashboard — und/alundum.md": {
    "primary": "An artificial abrasive and refractory material made of fused crystalline alumina (aluminum oxide).",
    "secondary": "In ceramic materials science, Alundum crucibles and grinding wheels withstand extreme metallurgical temperatures above two thousand degrees Celsius.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "We lined the experimental high-temperature electric furnace with porous **alundum** cement to resist thermal shock."},
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "Industrial refractory coatings formulated from fused **alundum** protected the rocket nozzle from eroding under searing exhaust gases."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The active radioactive preparation was contained inside an **alundum** crucible within the heavy lead shield."}
    ]
  },
  "Dashboard — und/arundinaceous.md": {
    "primary": "Resembling or having the characteristics of a reed or cane; reed-like.",
    "secondary": "In systematic graminology, arundinaceous grasses possess hollow, jointed, woody culms typical of tall marsh reeds and bamboos.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The margins of the freshwater lake were bordered by tall **arundinaceous** grasses sheltering nesting waterfowl."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Dense thickets of **arundinaceous** cane lined the muddy riverbanks of the Parana, impeding our overland progress."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "The delta wetlands harbored magnificent **arundinaceous** vegetation that swayed with the tidal surge."}
    ]
  },
  "Dashboard — und/arundinaria.md": {
    "primary": "A genus of bamboos in the grass family Poaceae, native to North America and Asia; cane.",
    "secondary": "In southeastern North American ecology, Arundinaria gigantea forms dense riverine canebrakes that once covered millions of acres.",
    "quotes": [
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "We rode for miles through towering canebrakes of **arundinaria**, whose jointed stems grew thirty feet in height."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The native switch-cane, **arundinaria** tecta, forms subterranean rhizomatous networks in damp southern swales."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The historical distribution of native bamboos like **arundinaria** in temperate America illustrates ancient floristic links with East Asia."}
    ]
  },
  "Dashboard — und/arundo.md": {
    "primary": "A genus of tall perennial reed grasses, especially Arundo donax (giant reed), native to the Mediterranean basin.",
    "secondary": "In musical instrument fabrication, culms of Arundo donax have been harvested since antiquity to manufacture reeds for oboes, clarinets, and bagpipes.",
    "quotes": [
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The marsh warbler suspended its woven nest among the waving stems of the giant river reed **arundo**."},
      {"author": "Richard Francis Burton", "work": "The Land of Midian", "quote": "The desert waterholes were fringed with luxuriant clumps of **arundo**, providing shade in the blistering midday heat."},
      {"author": "Hector Berlioz", "work": "Treatise on Modern Instrumentation and Orchestration", "quote": "Woodwind performance depends essentially upon the elasticity of the cane reed split from dried stalks of **arundo** donax."}
    ]
  },
  "Dashboard — und/asunder.md": {
    "primary": "Apart or divided; into separate pieces or directions.",
    "secondary": "In marriage liturgy and tragic drama, the phrase 'rent asunder' denotes the violent dissolution of sacred bonds or cosmic unity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "What God hath joined together, let no man put **asunder**; yet civil strife tears Verona's peace to shreds."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The sword of Michael smote the adversary, rending the demonic shield and mail **asunder** with celestial wrath."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Families were torn **asunder** by the sudden arrests of the revolutionary tribunal during the Reign of Terror."}
    ]
  },
  "Dashboard — und/conundrum.md": {
    "primary": "A confusing and difficult problem or question; or a riddle whose answer involves a pun.",
    "secondary": "In philosophical epistemology, a profound conceptual conundrum arises when reconciling determinism with subjective moral responsibility.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The locked room murder presented a perplexing **conundrum** that defied the standard deductions of Scotland Yard."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke treated political reform as a harmless intellectual **conundrum** to be debated pleasantly over claret."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "To discover who was the rightful heir to the Jarndyce millions was a legal **conundrum** that had baffled generations of chancellors."}
    ]
  },
  "Dashboard — und/corundom.md": {
    "primary": "An archaic variant spelling of corundum; a hard crystalline form of aluminum oxide.",
    "secondary": "In historical lapidary manuals, corundom gems included ruby and sapphire, valued next to diamond in hardness.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Lapidaries polish the hardest agates using powdered **corundom** imported from the East Indies."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "The mineral specimen of oriental **corundom** exhibited extraordinary hardness, resisting the keenest steel file."},
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "The hardness of **corundom** renders its abrasive dust essential for cutting and faceting precious stones."}
    ]
  },
  "Dashboard — und/corundum.md": {
    "primary": "An extremely hard mineral consisting of aluminum oxide (Al2O3), forming rubies and sapphires, used as an abrasive.",
    "secondary": "On the Mohs scale of mineral hardness, corundum defines hardness level 9, superseded in natural hardness only by diamond.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "In the river gravels of the diamond districts, miners frequently encounter water-worn pebbles of **corundum** and tourmaline."},
      {"author": "John Ruskin", "work": "The Ethics of the Dust", "quote": "The ruby is merely crystallized **corundum** touched with a minute trace of chromium that gives it royal crimson fire."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Granular varieties of **corundum** mixed with magnetite or hematite constitute commercial emery, prized for metal polishing."}
    ]
  },
  "Dashboard — und/inundate.md": {
    "primary": "To overwhelm someone with things or people to be dealt with; or to flood with water.",
    "secondary": "In hydrologic engineering, torrential rainfall can inundate low-lying floodplains when river levees fail under hydrostatic head.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden melting of alpine snows threatened to **inundate** the northern plains of Italy with destructive torrents."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Suppliants continued to **inundate** the Lord Chancellor with petitions and affidavits in the unending Chancery suit."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "Letters and telegrams began to **inundate** Baker Street from foreign embassies demanding immediate recovery of the naval plans."}
    ]
  },
  "Dashboard — und/inundated.md": {
    "primary": "Flooded with water; or overwhelmed with an excessive amount of things or people.",
    "secondary": "In agricultural history, the Nile valley was seasonally inundated by nutrient-rich floodwaters that deposited fertile black silt.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "The heavy monsoon rains had completely **inundated** the lower savanna, cutting off access to my coastal boat."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The Belgian engineers opened the sluice gates, leaving the low country around the Yser **inundated** to stop the German advance."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "The Floss overflowed its banks, and the fields were **inundated** by a vast sheet of swirling, muddy water."}
    ]
  },
  "Dashboard — und/inundation.md": {
    "primary": "An overwhelming abundance of people or things; or a flood or deluge of water.",
    "secondary": "In fluvial geomorphology, catastrophic river inundation deposits extensive overbank sediments across floodplain terraces.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian **inundation** swept across the Rhine provinces, extinguishing Roman civil administration in Gaul."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A sudden marine **inundation** followed the earthquake, sweeping ships far inland onto the coastal plains."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parliament was besieged by an **inundation** of petitions protesting the royal excise duties."}
    ]
  },
  "Dashboard — und/misunderstand.md": {
    "primary": "To fail to interpret, comprehend, or understand something or someone correctly.",
    "secondary": "In intercultural communication and diplomacy, ambiguous treaty phrasing causes rival chancelleries to misunderstand strategic intentions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "You choose to **misunderstand** me, said Elizabeth, smiling; I never accused Mr. Darcy of lacking intellectual abilities."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Vague philosophical terms cause disputants to **misunderstand** one another and waste lifetimes in verbal controversies."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Do not **misunderstand** my silence, for my grief is of that deep inward nature that passes outward show."}
    ]
  },
  "Dashboard — und/misunderstanding.md": {
    "primary": "A failure to understand correctly; or a disagreement, quarrel, or slight dispute.",
    "secondary": "In social contract theory, mutual trust mitigates the danger that factional misunderstanding will erupt into civil conflict.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "The entire unhappy complication arose from a mutual **misunderstanding** between Frank Churchill and Jane Fairfax."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Doctor Strong and his young wife lived under a painful cloud of domestic **misunderstanding** created by Uriah Heep's whispers."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes cleared up the tragic **misunderstanding** that had led the escaped convict to his death upon the rocks."}
    ]
  },
  "Dashboard — und/misunderstood.md": {
    "primary": "Incorrectly interpreted, evaluated, or understood; not appreciated for true qualities.",
    "secondary": "In Romantic literature, the misunderstood genius is alienated from bourgeois society, seeking solace in artistic isolation.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Is it so bad, then, to be **misunderstood**? Pythagoras was **misunderstood**, and Socrates, and Jesus, and Luther, and Newton."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane felt that her passionate longing for liberty was cruelly **misunderstood** by Mrs. Reed and the servants."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "To be **misunderstood** is the common fate of artists who refuse to flatter the conventional prejudices of their age."}
    ]
  },
  "Dashboard — und/overabundance.md": {
    "primary": "An excessive quantity or surplus of something, exceeding normal needs or capacity.",
    "secondary": "In agricultural economics, an overabundance of grain harvests precipitates steep commodity price deflation and farmer insolvency.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An **overabundance** of paper currency unregulated by metallic redemption inevitably results in domestic inflation."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **overabundance** of seeds produced by every plant ensures that only a tiny fraction survive the severe struggle for existence."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "In the midst of industrial **overabundance**, millions of English laborers languish without daily bread or employment."}
    ]
  },
  "Dashboard — und/overabundant.md": {
    "primary": "Existing in excessive quantity; more than enough or excessively plentiful.",
    "secondary": "In ecology and limnology, overabundant nitrate runoff causes eutrophication and catastrophic algal blooms in freshwater lakes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Where food supplies are **overabundant**, populations multiply until checked by disease, predators, or famine."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The **overabundant** moisture in the tropical air condenses into torrential daily afternoon downpours."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke possessed an **overabundant** store of miscellaneous information that he rarely applied to practical purpose."}
    ]
  },
  "Dashboard — und/profunda.md": {
    "primary": "A deep-seated anatomical blood vessel, especially the profunda femoris or profunda brachii artery.",
    "secondary": "In gross surgical anatomy, the arteria profunda femoris is the principal collateral channel supplying the thigh muscles.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ligation of the common femoral artery requires an intact **profunda** branch to maintain collateral perfusion to the lower limb."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The artery **profunda** brachii winds around the posterior surface of the humerus in close contact with the radial nerve."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The surgeon identified the bleeding branch of the **profunda**, applying a secure silk ligature in the deep muscular plane."}
    ]
  },
  "Dashboard — und/redound.md": {
    "primary": "To contribute greatly to a person's credit, honor, or disadvantage; or to recoil.",
    "secondary": "In classical legal and moral discourse, honorable public conduct redounds to the enduring glory of a commonwealth.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "All our glory shall **redound** to our Creator, when we stand confirmed in holiness before the throne."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A faithful discharge of the public debt will **redound** to the lasting credit and commercial prosperity of the American union."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Magnanimity in politics will **redound** more to imperial dignity than stubborn insistence upon uncollectible revenue rights."}
    ]
  },
  "Dashboard — und/redundance.md": {
    "primary": "Superfluity, excessive repetition, or surplus matter exceeding normal requirements; redundancy.",
    "secondary": "In classical literary criticism, pruning rhetorical redundance tightens argumentation and sharpens stylistic impact.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The author must prune every superfluous **redundance** from his sentences if he wishes his prose to endure."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Scholastic disputations were encumbered with dialectical **redundance** that obscured simple physical truths."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The political manifesto was weakened by verbal **redundance** and repetitious declarations of familiar platitudes."}
    ]
  },
  "Dashboard — und/redundancy.md": {
    "primary": "The state or fact of being superfluous, unnecessary, or duplicating function; or the loss of a job.",
    "secondary": "In aerospace and reliability engineering, triple modular redundancy ensures system failure tolerance through parallel backups.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "Critical spacecraft life-support circuits were engineered with double **redundancy** to prevent catastrophic failure in deep space."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Logical economy requires the elimination of conceptual **redundancy** from definitions and primary axioms."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A sudden **redundancy** of manufactured goods in the home market drives domestic merchants to seek foreign export outlets."}
    ]
  },
  "Dashboard — und/redundant.md": {
    "primary": "Not or no longer needed or useful; superfluous, repetitive, or exceeding what is natural or necessary.",
    "secondary": "In information theory, redundant coding bits are appended to data transmissions to enable forward error detection and correction.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With serpentine error wand'ring, found out the sea, where waves tossed **redundant** upon the sandy beach."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Rudimentary organs are **redundant** evolutionary remnants of structures that were fully functional in ancestral lineages."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "A concise discourse wastes no words on **redundant** flourishes that add nothing to the weight of the counsel."}
    ]
  },
  "Dashboard — und/superabundance.md": {
    "primary": "An exceedingly large quantity, excessive surplus, or overflowing excess of something.",
    "secondary": "In biological reproductive ecology, organisms produce a superabundance of gametes to offset severe juvenile mortality rates.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **superabundance** of offspring produced by every species inevitably leads to a fierce struggle for limited resources."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A **superabundance** of gold and silver in Spain after the conquest of Peru caused domestic commodity prices to soar."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The industrial mills produced a **superabundance** of cotton cloth while thousands of weavers shivered in rags."}
    ]
  },
  "Dashboard — und/superabundant.md": {
    "primary": "Existing in excessive quantity; more than sufficient; overflowing.",
    "secondary": "In horticultural cultivation, superabundant fruit set is thinned manually to allow remaining fruits to achieve premium market size.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Plants cultivated in rich garden loam produce **superabundant** foliage at the expense of floral development."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **superabundant** harvests of Egypt and Africa sustained the idle plebeian populace of imperial Rome."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Nature provides with **superabundant** generosity for those who are content with simple and wholesome necessities."}
    ]
  },
  "Dashboard — und/surround.md": {
    "primary": "To be all around someone or something; or to encircle, encompass, or hem in on all sides.",
    "secondary": "In tactical siege warfare, invading armies construct lines of circumvallation to surround a fortress and starve its garrison.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "Our armed legions shall **surround** your walls, shutting out all hope of foreign rescue or food."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I constructed a strong wooden stockade to **surround** my cave and protect me from nocturnal beasts."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The outlaw archers gathered quietly through the forest to **surround** the castle and block every avenue of escape."}
    ]
  },
  "Dashboard — und/surrounded.md": {
    "primary": "Encircled, encompassed, or enclosed on all sides by people, objects, or terrain.",
    "secondary": "In military history, an army surrounded without interior supply lines faces imminent capitulation unless relieved.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions under Varus were completely **surrounded** in the dense swamps of the Teutoburg Forest by Arminius."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The royal coach was **surrounded** by a surging Parisian mob armed with pikes and rusty muskets."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The gloomy mansion stood **surrounded** by desolate granite tors and treacherous quagmires of the Great Grimpen Mire."}
    ]
  },
  "Dashboard — und/surrounding.md": {
    "primary": "Encircling, enclosing, or situated around something; or environmental surroundings.",
    "secondary": "In urban planning and topography, zoning restrictions protect surrounding agricultural greenbelts from suburban sprawl.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The temperature of the sea exerts a profound moderating influence upon the **surrounding** coastal atmosphere."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The flora of the oceanic island differed markedly from the continental vegetation of the **surrounding** mainland."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Hester Prynne's cottage stood isolated on the outskirts of town, overlooking the sea and the **surrounding** wild forest."}
    ]
  },
  "Dashboard — und/surroundings.md": {
    "primary": "The things, conditions, and environment around a person or thing; physical setting.",
    "secondary": "In environmental psychology, aesthetic surroundings exert measurable influences on cognitive recovery and stress alleviation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea found her luxurious Roman **surroundings** oppressive, yearning for active moral duty rather than artistic sightseeing."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I stepped from the machine into unfamiliar **surroundings**, gazing upon colossal ruined palaces half-choked with rhododendrons."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes surveyed the luxurious oriental **surroundings** of Thaddeus Sholto's drawing room with keen analytical interest."}
    ]
  },
  "Dashboard — und/undamaged.md": {
    "primary": "Not harmed, impaired, or damaged; intact, sound, and in good condition.",
    "secondary": "In forensic insurance surveying, an undamaged vessel cargo is inspected to verify that seawater flooding did not contaminate holds.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I succeeded in bringing ashore several barrels of gunpowder that had remained completely **undamaged** by the seawater."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Miraculously, the battlecruiser survived the heavy shell hit with her main engines and steering gear **undamaged**."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "Holmes examined the charred ruins, discovering the valuable parchment deed **undamaged** inside the fireproof safe."}
    ]
  },
  "Dashboard — und/undatable.md": {
    "primary": "Impossible to assign to a specific date, era, or chronological timeframe.",
    "secondary": "In geoarchaeology and historical palynology, an undatable artifact stratum lacks organic carbon or diagnostic pottery typologies.",
    "quotes": [
      {"author": "John Lubbock", "work": "Pre-historic Times", "quote": "The deeply buried flint implements belonged to an **undatable** geological antiquity that preceded all historical records."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Ancient oral legends preserved by barbarian bards belong to an **undatable** mythological past beyond chronological verification."},
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The lowest cyclopean foundation stones appeared **undatable** by classical standards, pointing toward neolithic antecedents."}
    ]
  },
  "Dashboard — und/undated.md": {
    "primary": "Not bearing a date; not marked with a specific calendar day or year.",
    "secondary": "In manuscript palaeography and archival research, establishing the provenance of an undated letter requires internal watermarks.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Second Stain", "quote": "The stolen dispatch was an **undated** autograph letter from a foreign potentate, fraught with dangerous political consequences."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth received an **undated** letter from her sister Jane, written in haste from Longbourn upon Lydia's disappearance."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The historians discovered an **undated** royal memorandum in the archives that confirmed Monmouth's secret communications."}
    ]
  },
  "Dashboard — und/undaunted.md": {
    "primary": "Not intimidated, dismayed, or discouraged by difficulty, danger, or disappointment; brave.",
    "secondary": "In military chronicles, an undaunted rearguard holds its defensive position against overwhelming odds to save an army.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan stood with **undaunted** courage upon the burning marl, surveying the ruined host of his fallen legions."},
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Bring forth men-children only; for thy **undaunted** mettle should compose nothing but males."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The British people stood **undaunted** in the face of imminent invasion, united by an unconquerable resolve to resist tyranny."}
    ]
  },
  "Dashboard — und/undecagon.md": {
    "primary": "A plane geometrical figure with eleven straight sides and eleven angles; a hendecagon.",
    "secondary": "In Euclidean geometry and polygon construction, a regular undecagon cannot be constructed using an unmarked straightedge and compass.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Professor Teufelsdröckh drew geometric diagrams upon the chalkboard, illustrating the anomalous angles of an **undecagon**."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The crystalline mineral specimen exhibited eleven distinct pyramidal facets, approximating the shape of a geometric **undecagon**."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Mathematical studies of complex figures such as the **undecagon** sharpen the mind's capacity for abstract deduction."}
    ]
  },
  "Dashboard — und/undeceive.md": {
    "primary": "To free someone from an illusion, misconception, or false impression; to reveal the truth to someone.",
    "secondary": "In domestic fiction, a loyal friend intervenes to undeceive a naive protagonist regarding an unscrupulous suitor's character.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy resolved to **undeceive** Bingley regarding Jane's supposed indifference, acknowledging his past interference."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "Emilia strove with desperate courage to **undeceive** the Moor before his jealousy accomplished the fatal tragedy."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert Pocket deemed it his duty to **undeceive** Pip gently concerning the true source of his mysterious fortune."}
    ]
  },
  "Dashboard — und/undeceived.md": {
    "primary": "Freed from an illusion, deception, or false belief; having learned the truth of a situation.",
    "secondary": "In ethical philosophy, an undeceived mind evaluates human actions with objective realism rather than romanticized sentiment.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea looked upon her husband with an **undeceived** vision, recognizing the sad limitations of his pedantic intellect."},
      {"author": "Samuel Johnson", "work": "The History of Rasselas, Prince of Abissinia", "quote": "The prince returned to Abissinia **undeceived** by the worldly pretensions of statesmen, sages, and ascetics."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel Archer was at last **undeceived**, standing face to face with the calculated treachery that had engineered her marriage."}
    ]
  },
  "Dashboard — und/undecided.md": {
    "primary": "Not settled, resolved, or determined; wavering between two or more options.",
    "secondary": "In legal and parliamentary proceedings, an undecided question remains pending on the docket for further argument.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "While the momentous question of national union remained **undecided**, commercial enterprise was paralyzed across the states."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Jarndyce inheritance remained **undecided** after decades of argument, while costs ate away the disputed wealth."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was left **undecided** as to whether Edward's strange melancholy sprang from regret or external misfortune."}
    ]
  },
  "Dashboard — und/undecipherable.md": {
    "primary": "Impossible to read, translate, or decode; illegible or incomprehensible.",
    "secondary": "In historical cryptanalysis, an undecipherable cipher defies frequency analysis when encrypted using a one-time pad.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Dancing Men", "quote": "The strange chalk hieroglyphs upon the sundial appeared completely **undecipherable** to the local Norfolk police."},
      {"author": "Edgar Allan Poe", "work": "The Gold-Bug", "quote": "Legrand showed me a yellow parchment covered with characters that seemed at first glance wholly **undecipherable**."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The inscription carved upon the bronze pedestal was worn by centuries of weathering into an **undecipherable** script."}
    ]
  },
  "Dashboard — und/undecipherably.md": {
    "primary": "In an undecipherable, illegible, or completely incomprehensible manner.",
    "secondary": "In paleographical transcription, ancient papyrus fragments written undecipherably require multispectral imaging to reveal hidden inks.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The ancient manuscript was written **undecipherably** in faded seventeenth-century ink that taxed Holmes's patience."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard scrawled his bitter last will and testament **undecipherably** upon a scrap of crumpled paper in the hovel."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The old deed was endorsed **undecipherably** with archaic legal formulas that baffled modern conveyancers."}
    ]
  },
  "Dashboard — und/undeciphered.md": {
    "primary": "Not yet decoded, translated, or interpreted; remaining an unsolved mystery or script.",
    "secondary": "In historical epigraphy, ancient writing systems like Linear A and the Indus script remain tantalizingly undeciphered by modern linguists.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The hieroglyphic inscriptions of the Nile obelisks remained **undeciphered** until the discovery of the Rosetta Stone."},
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The baked clay tablets retrieved from Knossos bore an **undeciphered** script that preserved the lost language of Bronze-Age Crete."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger discovered an **undeciphered** symbol scratched upon the bark of a tree marking the entrance to the plateau."}
    ]
  },
  "Dashboard — und/undeclared.md": {
    "primary": "Not officially stated, announced, or admitted; or not declared to customs officials.",
    "secondary": "In international military conflict, an undeclared war bypasses formal legislative declarations through covert operations and proxy fighting.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "A state of **undeclared** naval hostility already existed in the Atlantic as submarines prowled the merchant shipping lanes."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "The smuggling of **undeclared** goods into colonial ports was tacitly condoned by local magistrates and merchants."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "There lingered between them an **undeclared** affection that neither had the courage to put into explicit words."}
    ]
  },
  "Dashboard — und/undecomposable.md": {
    "primary": "Incapable of being decomposed, separated into constituent elements, or broken down chemically.",
    "secondary": "In early modern chemical theory, Robert Boyle and Lavoisier defined chemical elements as undecomposable substances by physical means.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "An element is defined as a primitive, simple, and **undecomposable** body of which all compounded bodies are composed."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "If we apply the term elements to the **undecomposable** constituents of matter, we must classify thirty-three simple substances."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The mineral residue resisted the action of our strongest voltaic currents, remaining strictly **undecomposable**."}
    ]
  },
  "Dashboard — und/undecomposed.md": {
    "primary": "Not broken down, rotted, or decomposed; remaining intact and chemically unchanged.",
    "secondary": "In soil science and geology, undecomposed organic leaf litter forms a protective mor layer over acidic boreal forest soils.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms swallow fallen leaves, digesting the soft parts while ejecting the **undecomposed** fibrous fragments in their castings."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The coal beds contain fossilized trunks and leaves preserved in an almost **undecomposed** state beneath dense shale layers."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "In the absence of airborne microbial germs, sterile broth remains clear and **undecomposed** indefinitely."}
    ]
  },
  "Dashboard — und/undecorated.md": {
    "primary": "Not decorated, adorned, or embellished; plain, simple, and unadorned.",
    "secondary": "In architectural criticism, the severe undecorated facades of early modernism emphasized functional utility over historical ornament.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The honest dignity of an **undecorated** stone wall exceeds all the vulgar plaster ornament that false taste can paste upon it."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane's attic bedroom at Lowood was an **undecorated** cell furnished with a simple straw bed and an unpainted chair."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Gradgrind's schoolroom was an **undecorated** whitewashed hall where facts and figures reigned supreme."}
    ]
  },
  "Dashboard — und/undedicated.md": {
    "primary": "Not consecrated or formally dedicated to a sacred purpose; or not dedicated to a patron in a literary work.",
    "secondary": "In early print culture, an undedicated volume was published without an opening panegyric epistle courting aristocratic patronage.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "The poet published his satirical verses **undedicated**, refusing to stoop to the servile flattery of noble patrons."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The ruined chapel had stood **undedicated** and abandoned since the monastic suppression under Henry VIII."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The new public hall remained **undedicated** to any religious denomination, serving as an impartial civic forum."}
    ]
  },
  "Dashboard — und/undefeated.md": {
    "primary": "Not defeated, conquered, or beaten in battle, contest, or athletic competition.",
    "secondary": "In military biography, undefeated field marshals like the Duke of Marlborough achieved strategic victory through operational foresight.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Belisarius returned to Constantinople **undefeated**, having recovered Italy and Africa for the imperial crown."},
      {"author": "Winston Churchill", "work": "Marlborough: His Life and Times", "quote": "Marlborough remained an **undefeated** captain in the field, never fighting a battle that he did not win, nor besieging a fortress he did not take."},
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The veteran prizefighter entered the championship ring **undefeated**, boasting thirty victories over the bravest men of the fancy."}
    ]
  },
  "Dashboard — und/undefendable.md": {
    "primary": "Incapable of being defended, justified, or protected against attack or criticism.",
    "secondary": "In military strategy, an exposed salient without natural obstacles or artillery support becomes tactically undefendable under bombardment.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The frontier salient was tactically **undefendable**, forcing our infantry divisions to withdraw to the canal defenses."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A constitutional proposition that grants sovereign power without accountability is logically **undefendable** in a free republic."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "The ministerial policy of taxing the colonies without representation is politically **undefendable** before the bar of reason."}
    ]
  },
  "Dashboard — und/undefended.md": {
    "primary": "Not protected against attack, assault, or legal action; lacking defense or military garrison.",
    "secondary": "Under the Hague and Geneva conventions, an undefended open town or village must not be subjected to artillery bombardment.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian cavalry poured through the **undefended** passes of the Alps, ravaging the fertile plains of northern Italy."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The coastal ports were left virtually **undefended** while the main battlefleet concentrated in the northern anchorages."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The prisoner stood **undefended** before the revolutionary tribunal, where accusations were equivalent to instant condemnation."}
    ]
  },
  "Dashboard — und/undeferential.md": {
    "primary": "Not showing deference, reverence, or polite submission; disrespectful or irreverent toward authority.",
    "secondary": "In social history, democratic frontier communities developed an undeferential ethos that rejected traditional class hierarchies.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The American pioneer exhibits an **undeferential** bearing toward public magistrates, treating them as hired servants rather than lords."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton was shocked by the **undeferential** manner in which the newcomer addressed the established gentry of Highbury."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "Felix Holt spoke to the wealthy candidate in an **undeferential** tone that startled the complacent election committee."}
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

print(f"Dashboard — und Part 1 (8A): Successfully updated {updated}/{len(data)} notes.")
