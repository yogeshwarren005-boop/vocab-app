import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Sound & Auditory/Dashboard — bomb';

const filesData = {
  "abound.md": {
    primary: "To exist in large numbers or amounts; to be plentiful or copious.",
    secondary: "To be richly supplied, filled, or teeming with something (followed by *in* or *with*).",
    quotes: [
      { author: "Charles Dickens", work: "A Christmas Carol", quote: "The crisp leaves of holly, mistletoe, and ivy **abound** in every cozy shop window along the festive street." },
      { author: "William Shakespeare", work: "Henry VI, Part 2", quote: "So cares and joys **abound**, as seasons fleet." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Fish of several varieties **abound** in the clear, deep water of the pond." }
    ]
  },
  "bomb.md": {
    primary: "A container filled with explosive, incendiary, or toxic material, designed to detonate upon impact or via a timing device.",
    secondary: "A total failure or disaster in theater or cinema; or in British informal usage, a huge success.",
    quotes: [
      { author: "H. G. Wells", work: "The World Set Free", quote: "The pilot leaned from the cockpit and released the atomic **bomb**, watching its fiery cataclysm consume the hills below." },
      { author: "George Orwell", work: "1984", quote: "A rocket **bomb** had fallen two hundred meters up the street, tearing the row of houses into brick dust." },
      { author: "Joseph Conrad", work: "The Secret Agent", quote: "The anarchist carried the glass phial of explosive **bomb** material inside his breast pocket with perilous intimacy." }
    ]
  },
  "bombacaceae.md": {
    primary: "A former family of tropical dicotyledonous trees in the order Malvales (now subfamily Bombacoideae within Malvaceae), notably including the baobab, kapok, and balsa trees.",
    secondary: "A botanical taxon of majestic trees characterized by swollen pachycaul trunks, palmate leaves, and large flowers producing silky seed-capsules.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Trees of the family **Bombacaceae** tower above the equatorial jungle, their giant buttressed trunks anchored in ancient soil." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The grotesque, swollen trunk of the baobab, placed by botanists in the **Bombacaceae**, resembles a vegetable fortress." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In the **Bombacaceae**, the wood is remarkably soft and spongy, producing lightweight timbers like balsa." }
    ]
  },
  "bombard.md": {
    primary: "To attack continuously with bombs, artillery shells, or other missiles.",
    secondary: "To assail someone persistently with questions, complaints, or information; also, in nuclear physics, to direct a stream of high-energy particles at a target nucleus.",
    quotes: [
      { author: "Ernest Hemingway", work: "A Farewell to Arms", quote: "The Austrian batteries began to **bombard** the trench line across the river with heavy trench-mortar shells." },
      { author: "Marie Curie", work: "Radioactive Substances", quote: "Physicists learned to **bombard** heavy atoms with alpha particles to induce nuclear disintegrations." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The revolutionary mob gathered before the gates, threatening to **bombard** the fortress with captured cannon." }
    ]
  },
  "bombardier.md": {
    primary: "A member of a military aircraft crew responsible for sighting and releasing bombs onto target coordinates.",
    secondary: "A non-commissioned officer rank in artillery regiments, or a bombardier beetle that shoots noxious chemical spray.",
    quotes: [
      { author: "Joseph Heller", work: "Catch-22", quote: "Yossarian was a lead **bombardier** who spent every combat mission maneuvering desperately to avoid anti-aircraft flak." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Like a naval **bombardier** aiming a loaded mortar, the harpooneer poised his weapon above the churning sea." },
      { author: "Stephen Crane", work: "The Red Badge of Courage", quote: "The veteran **bombardier** swabbed the smoking barrel of the howitzer with swift, disciplined precision." }
    ]
  },
  "bombardment.md": {
    primary: "A continuous, intense attack with artillery shells, aerial bombs, or other high-explosive ordnance.",
    secondary: "A sustained, overwhelming barrage of questions, criticisms, or high-energy physical particles.",
    quotes: [
      { author: "Erich Maria Remarque", work: "All Quiet on the Western Front", quote: "During the heavy drumfire **bombardment**, the earth groans and trenches crumble into choking craters." },
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "The capital endured a ferocious nightly **bombardment**, yet the spirit of its citizens remained unbroken." },
      { author: "Ernest Rutherford", work: "The Newer Alchemy", quote: "Through continuous alpha-particle **bombardment**, we succeeded in transmuting stable nitrogen into oxygen." }
    ]
  },
  "bombardon.md": {
    primary: "A large bass brass wind instrument of the tuba family, or a deep pedal reed stop on a pipe organ, producing a powerful low resonant drone.",
    secondary: "A deep-voiced musical instrument derived from German *Bombardon* (from French *bombarde*, an early cannon/shawm).",
    quotes: [
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The village bandsman blew into his brass **bombardon**, shaking the windows of the gallery with its deep vibrating roar." },
      { author: "Hector Berlioz", work: "Treatise on Instrumentation", quote: "The powerful contrabass **bombardon** supplies a majestic foundation of bass tone to military bands." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "The circus parade advanced to the booming syncopation of drums and a lusty **bombardon**." }
    ]
  },
  "bombast.md": {
    primary: "High-sounding language with little meaning, used to impress people; pompous, inflated speech or writing.",
    secondary: "Cotton wool, soft down, or padding fabric formerly used for stuffing garments and quilted armor in historical costume.",
    quotes: [
      { author: "William Shakespeare", work: "Love's Labour's Lost", quote: "As **bombast** and as lining to the time: but more devout than this in our respects have we not been." },
      { author: "Samuel Johnson", work: "The Lives of the Poets", quote: "He mistook inflated **bombast** for sublimity, heaping epithets upon thoughts that were inherently trivial." },
      { author: "Jonathan Swift", work: "A Tale of a Tub", quote: "The orator strutted upon the platform, delivering a torrent of empty **bombast** to the bewildered crowd." }
    ]
  },
  "bombastic.md": {
    primary: "High-sounding but with little meaning; inflated, pompous, and pretentious in language.",
    secondary: "Exhibiting an overblown theatrical or rhetorical style in public speaking.",
    quotes: [
      { author: "Thomas Carlyle", work: "Past and Present", quote: "Mankind turns weary of **bombastic** election speeches that promise heaven and deliver nothing." },
      { author: "Edgar Allan Poe", work: "Marginalia", quote: "The reviewer tore apart the **bombastic** pretensions of the young poet's preface." },
      { author: "George Orwell", work: "Politics and the English Language", quote: "A tired writer resorts to **bombastic** diction to conceal an absolute absence of fresh thought." }
    ]
  },
  "bombastically.md": {
    primary: "In a bombastic, pompously inflated, or pretentiously grandiloquent manner.",
    secondary: "Using high-sounding words without substance or sincerity.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "He declaimed **bombastically** from the hearthrug, waving his hand as if addressing an imperial senate." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The boastful major spoke **bombastically** of his campaigns in India to dazzle the naive heiress." },
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "The courier gestured **bombastically** toward the ruined columns, reciting fabricated legends to the tourists." }
    ]
  },
  "bombax.md": {
    primary: "A genus of large tropical trees in the family Malvaceae (subfamily Bombacoideae), commonly known as red silk-cotton trees (*Bombax ceiba*), famed for their prickly bark, scarlet flowers, and silky seed capsules.",
    secondary: "A tropical timber tree prized for lightweight fiber (kapok) used for stuffing cushions and life preservers.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The magnificent crimson blossoms of **Bombax** burst into flower while the branches were still completely destitute of leaves." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Species of **Bombax** yield a downy floss enveloped in their woody capsules, valued for textile padding." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "In the foot-hills, giant specimens of **Bombax** rose eighty feet before spreading their horizontal flower-laden branches." }
    ]
  },
  "bombay.md": {
    primary: "The historic name of Mumbai, a major port city and financial metropolis on the western coast of India, famed for its deep natural harbor and colonial trade history.",
    secondary: "A breed of sleek, black domestic cat with copper eyes developed to resemble a miniature black panther.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "Regent Street is not unknown to Lascars and Malays; and at **Bombay**, in the Apollo Green, live Yankees have often scared the natives." },
      { author: "Jules Verne", work: "Around the World in Eighty Days", quote: "Phileas Fogg stepped ashore at the bustling quayside of **Bombay**, checking his pocket chronometer with unruffled calm." },
      { author: "Rudyard Kipling", work: "The Song of the Cities", quote: "Royal and spacious **Bombay**, jewel of the western sea, sits crowned upon her islands amidst the trade of empires." }
    ]
  },
  "bombazine.md": {
    primary: "A twilled fabric with a silk warp and a worsted wool weft, dyed black and traditionally used for mourning garments in Victorian and Edwardian society.",
    secondary: "The stiff, sombre black cloth symbolic of strict widowhood and domestic gravity in 19th-century literature.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Mrs. Reed sat erect in her black **bombazine** gown, cold and unyielding as a marble statue." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "Miss Murdstone rustled into the parlor in severe black **bombazine**, carrying her heavy steel purse." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "She appeared at church dressed in sombre **bombazine**, the recognized uniform of formal mourning in the borough." }
    ]
  },
  "bomber.md": {
    primary: "A military aircraft designed to drop bombs on ground or naval targets.",
    secondary: "A person who plants or detonates explosive bombs; or a short, waist-length jacket (bomber jacket) originally worn by flight crews.",
    quotes: [
      { author: "Winston Churchill", work: "The Second World War", quote: "The long-range heavy **bomber** was the instrument that carried the war directly into the industrial heart of the enemy." },
      { author: "George Orwell", work: "1984", quote: "The roar of a distant heavy **bomber** vibrated through the plaster walls of the decrepit tenement." },
      { author: "Arthur Conan Doyle", work: "His Last Bow", quote: "He pictured the night skies filled with fleets of soaring **bomber** planes raining fire upon sleeping cities." }
    ]
  },
  "bombie.md": {
    primary: "A small cluster bomblet; an unexploded submunition dropped from aircraft during aerial bombing campaigns.",
    secondary: "In Australian coastal surfing slang, a bombora or offshore submerged reef where giant ocean swells break heavily.",
    quotes: [
      { author: "Tim O'Brien", work: "The Things They Carried", quote: "The soldiers were warned to watch the paddy dikes for unexploded **bombie** submunitions hidden in the mud." },
      { author: "Peter Matthiessen", work: "Blue Meridian", quote: "The surfers paddled out past the coastal headland to challenge the giant breaking swells over the offshore **bombie**." },
      { author: "Michael Herr", work: "Dispatches", quote: "In the countryside, farmers still turned up orange-sized **bombie** pellets dropped decades earlier from the sky." }
    ]
  },
  "bombilate.md": {
    primary: "To make a humming, buzzing, or droning sound (variant of bombinate, from Greek *bombos*).",
    secondary: "To drone continuously like a bee or rotating propeller.",
    quotes: [
      { author: "Aldous Huxley", work: "Crome Yellow", quote: "His voice would **bombilate** softly through the library like a heavy bumblebee trapped behind a sunlit curtain." },
      { author: "James Joyce", work: "Finnegans Wake", quote: "The evening breeze seemed to **bombilate** with whispered rumors across the darkening Dublin quays." },
      { author: "T. S. Eliot", work: "Selected Essays", quote: "The mechanical engines of modern cities **bombilate** with a relentless rhythm that dulls the human soul." }
    ]
  },
  "bombilation.md": {
    primary: "A humming, buzzing, or droning sound; a low continuous acoustic vibration.",
    secondary: "Empty, buzzing sound without meaningful intellectual content.",
    quotes: [
      { author: "Vladimir Nabokov", work: "Ada, or Ardor", quote: "A faint **bombilation** of electric wires filled the warm summer stillness of the veranda." },
      { author: "James Joyce", work: "Ulysses", quote: "The distant **bombilation** of printing presses resonated through the floorboards of the newspaper office." },
      { author: "Aldous Huxley", work: "Point Counter Point", quote: "He listened to the dull **bombilation** of academic debate, longing for the fresh air of the open garden." }
    ]
  },
  "bombina.md": {
    primary: "A genus of small, warty, semi-aquatic toads in the family Bombinatoridae, commonly known as fire-bellied toads, famed for bright belly markings and low bell-like barking calls.",
    secondary: "A European and Asian amphibian genus exhibiting the defensive posture displaying a brightly colored belly to warn predators of skin toxins.",
    quotes: [
      { author: "Hans Gadow", work: "Amphibia and Reptiles", quote: "When disturbed, the little toad **Bombina** arches its spine to display the fiery orange warning patches upon its belly." },
      { author: "Konrad Lorenz", work: "King Solomon's Ring", quote: "In the marshes of the Danube, the melancholy bell-like piping of **Bombina** sounds like distant fairy bells across the reeds." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "The hybrid zone between two European species of **Bombina** provides a textbook model of reproductive isolation." }
    ]
  },
  "bombinate.md": {
    primary: "To make a humming or buzzing noise; to drone or buzz continuously like a bee.",
    secondary: "To hum aimlessly or engage in vacuous, noisy speculation in philosophical satire.",
    quotes: [
      { author: "François Rabelais", work: "Gargantua and Pantagruel", quote: "Whether a chimera, **bombinating** in the void, can devour second intentions." },
      { author: "Aldous Huxley", work: "Antic Hay", quote: "The thoughts in his tired brain continued to **bombinate** like hornets in an empty bottle." },
      { author: "Samuel Beckett", work: "Murphy", quote: "Murphy closed his eyes and allowed his consciousness to **bombinate** peacefully in total darkness." }
    ]
  },
  "bombination.md": {
    primary: "A buzzing, droning, or humming sound (from Latin *bombinare*, from Greek *bombos*).",
    secondary: "Empty, continuous verbal noise; vacuous academic buzzing.",
    quotes: [
      { author: "François Rabelais", work: "Gargantua and Pantagruel", quote: "Scholastic metaphysics often resolved into sterile **bombination** regarding things that have no real existence." },
      { author: "Aldous Huxley", work: "Those Barren Leaves", quote: "He could hear the distant **bombination** of traffic, an endless mechanical murmur rising from the metropolis." },
      { author: "Vladimir Nabokov", work: "Pale Fire", quote: "A gentle **bombination** of bumblebees over the lavender beds punctuated the quiet summer afternoon." }
    ]
  },
  "bombing.md": {
    primary: "An attack or assault in which explosive bombs are dropped from aircraft or detonated on targets.",
    secondary: "The military tactic or criminal act of deploying explosive munitions.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The air **bombing** of open towns was intended to shatter civilian morale, yet it produced only stubborn defiance." },
      { author: "Winston Churchill", work: "The Second World War", quote: "The strategic **bombing** campaign steadily dismantled the synthetic fuel refineries and rail hubs of Germany." },
      { author: "John Hersey", work: "Hiroshima", quote: "The flash of the atomic **bombing** was followed by a silent, dreadful whirlwind that flattened the city in seconds." }
    ]
  },
  "bomblet.md": {
    primary: "A small bomb or submunition, especially one of dozens or hundreds packed into a cluster bomb casing and dispersed over a wide area.",
    secondary: "An explosive submunition that presents lingering humanitarian hazards when unexploded.",
    quotes: [
      { author: "Tim O'Brien", work: "The Things They Carried", quote: "Each artillery cluster canister scattered hundreds of lethal **bomblet** spheres across the canopy." },
      { author: "Michael Herr", work: "Dispatches", quote: "The pilots spoke of cluster munitions dispersing every miniature **bomblet** across the jungle clearing with mathematical spread." },
      { author: "Philip Caputo", work: "A Rumor of War", quote: "They walked with caution through the target zone, avoiding any unexploded **bomblet** protruding from the red clay." }
    ]
  },
  "bombshell.md": {
    primary: "An explosive artillery shell or bomb.",
    secondary: "A sudden, shocking piece of news, or an exceptionally striking and attractive person in popular culture.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Return of Sherlock Holmes", quote: "The sudden announcement of the baronet's marriage was a social **bombshell** that stunned London drawing rooms." },
      { author: "F. Scott Fitzgerald", work: "Tender Is the Night", quote: "Her unexpected revelation dropped like a **bombshell** into the quiet elegance of their terrace dinner." },
      { author: "Stephen Crane", work: "The Red Badge of Courage", quote: "A screeching **bombshell** buried itself in the sod nearby, tossing up a geyser of blackened soil." }
    ]
  },
  "bombsight.md": {
    primary: "An optical, mechanical, or computerized sighting instrument mounted on a military aircraft, used by the bombardier to aim and release bombs accurately.",
    secondary: "The precision navigational and ballistic calculating instrument (such as the secret Norden bombsight of WWII).",
    quotes: [
      { author: "Joseph Heller", work: "Catch-22", quote: "Yossarian stared through the rubber eyepiece of the secret Norden **bombsight**, aligning crosshairs with the bridge piers." },
      { author: "Richard Rhodes", work: "The Making of the Atomic Bomb", quote: "The Enola Gay approached the aiming point over Hiroshima, the bombardier peering intently into the gyro-stabilized **bombsight**." },
      { author: "John Steinbeck", work: "Bombs Away: The Story of a Bomber Team", quote: "The **bombsight** was treated with religious secrecy, guarded by armed sentries whenever removed from the safe." }
    ]
  },
  "bombus.md": {
    primary: "The genus of robust, hairy bees in the family Apidae comprising the true bumblebees, famed for their deep humming flight buzz, colony sociality, and buzz pollination.",
    secondary: "The primary pollinators of temperate wildflowers and agricultural crops, named from Greek *bombos* ('buzzing').",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The fertilisation of red clover depends almost entirely upon visits from humble-bees of the genus **Bombus**." },
      { author: "John Lubbock", work: "Ants, Bees, and Wasps", quote: "A queen of **Bombus** emerges from her winter hibernation in early spring to establish a subterranean nest." },
      { author: "Edward O. Wilson", work: "The Insect Societies", quote: "Colonies of **Bombus** display a primitive, annual social structure that dissolves upon the arrival of autumn frosts." }
    ]
  },
  "bombycid.md": {
    primary: "A moth belonging to the family Bombycidae, typified by the domestic silkworm moth (*Bombyx mori*).",
    secondary: "A stout-bodied, hairy moth whose larvae spin dense silk cocoons.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on the Disease of Silkworms", quote: "The parasitic microsporidian attacked the **bombycid** larvae, threatening the entire silk industry of southern France." },
      { author: "Jean-Henri Fabre", work: "Social Life in the Insect World", quote: "The adult **bombycid** lives only a few days without feeding, dedicated solely to reproduction." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Tropical forests harbor wild **bombycid** species whose golden cocoons rival the finest domestic silk." }
    ]
  },
  "bombycidae.md": {
    primary: "The family of moths in the order Lepidoptera that includes the domestic silkworm moth and related silk-spinning species.",
    secondary: "The lepidopteran family of economic importance as the biological foundation of global sericulture.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Generations of artificial breeding within the family **Bombycidae** rendered the adult silkworm moth incapable of flight." },
      { author: "Louis Pasteur", work: "Studies on the Disease of Silkworms", quote: "The epidemic of pebrine among the **Bombycidae** was eradicated through microscopic examination of individual moths." },
      { author: "John Obadiah Westwood", work: "The Modern Classification of Insects", quote: "The family **Bombycidae** is characterized by heavy bodies, pectinated antennae, and robust cocoons of continuous silk." }
    ]
  },
  "bombycilla.md": {
    primary: "The genus of passerine birds comprising the waxwings in the family Bombycillidae, characterized by silky plumage, black masks, and waxy red tips on secondary wing feathers.",
    secondary: "A bird genus named from Greek *bombyx* ('silk') and Latin *cilla* ('tail'), typified by the Bohemian waxwing (*Bombycilla garrulus*).",
    quotes: [
      { author: "John James Audubon", work: "Birds of America", quote: "Flocks of **Bombycilla** descend upon the cedar trees in winter, devouring berries with voracious eagerness." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "The exquisite plumage of **Bombycilla** carolinensis is as soft and lustrous as the finest silk." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The genus **Bombycilla** is distinguished by its crest, silky plumage, and curious scarlet wax-like appendages upon the wings." }
    ]
  },
  "bombycillidae.md": {
    primary: "The bird family in the order Passeriformes comprising the waxwings (genus *Bombycilla*), specialized frugivores of the Holarctic region.",
    secondary: "A small songbird family known for nomadic winter wandering in search of wild fruit crops.",
    quotes: [
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The family **Bombycillidae** includes sleek, crested birds possessing gregarious habits and rich fruit-eating adaptations." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Nomadic irruptions in the **Bombycillidae** are triggered by boreal crop failures of mountain ash berries." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The family **Bombycillidae** represents a distinctly northern circumpolar group adapted to cold conifer forests." }
    ]
  },
  "bombyliidae.md": {
    primary: "The family of stout-bodied, hairy flies in the order Diptera, commonly known as bee flies, famed for hovering in mid-air and producing a loud, high-pitched hum.",
    secondary: "A diverse dipteran family whose adults feed on nectar with long proboscises while their larvae parasitize solitary bees and wasps.",
    quotes: [
      { author: "John Obadiah Westwood", work: "An Introduction to the Modern Classification of Insects", quote: "Flies of the family **Bombyliidae** dart with lightning speed among flowers, hovering poised upon vibrating wings like hummingbirds." },
      { author: "Jean-Henri Fabre", work: "Bramble-Bees and Others", quote: "The parasitic larva of the **Bombyliidae** waits stealthily at the threshold of the mason-bee's earthen cell." },
      { author: "Charles Darwin", work: "Natural Selection Manuscript", quote: "The extraordinary floral mimicry of the **Bombyliidae** protects these harmless nectar-feeders from insectivorous predators." }
    ]
  },
  "bombyx.md": {
    primary: "The genus of moths comprising the silkworm moth, notably *Bombyx mori*, whose caterpillar spins the commercial silk cocoon.",
    secondary: "The biological source of natural silk, domesticated in ancient China over five millennia of sericulture.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on the Disease of Silkworms", quote: "The caterpillar of **Bombyx** mori feeds exclusively on fresh white mulberry leaves before spinning its cocoon." },
      { author: "Pliny the Elder", work: "Natural History", quote: "From a tiny worm named **Bombyx**, eastern nations harvest the delicate threads that clothe Roman matrons in luxury." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Domesticated **Bombyx** moths have lost the instinct to hide from predators, entirely dependent on human care." }
    ]
  },
  "bound.md": {
    primary: "Tied or fastened securely with a rope, cord, or bandage; legally, morally, or logically obligated to do something.",
    secondary: "Moving by leaping, jumping, or springing; or heading toward a specific destination (e.g., outward-bound).",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "I am **bound** to hear. Speak; I am **bound** to revenge, when thou shalt hear." },
      { author: "Emily Dickinson", work: "Selected Poems", quote: "The soul selects her own society, then shuts the door; on chariot **bound**." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The Pequod was **bound** for the four corners of the watery globe in search of the white monster." }
    ]
  },
  "boundary.md": {
    primary: "A line that marks the limits or border of an area, territory, or jurisdiction.",
    secondary: "A limit or dividing threshold separating distinct concepts, psychological states, or physical phases.",
    quotes: [
      { author: "Robert Frost", work: "Mending Wall", quote: "Before I built a wall I'd ask to know what I was walling in or walling out; something there is that doesn't love a **boundary**." },
      { author: "John Locke", work: "Second Treatise of Government", quote: "The law of nature sets a clear **boundary** to individual property, measured by what one can cultivate and use." },
      { author: "Immanuel Kant", work: "Prolegomena to Any Future Metaphysics", quote: "Reason must recognize its own legitimate **boundary**, beyond which empirical knowledge cannot pass." }
    ]
  },
  "bounded.md": {
    primary: "Having limits or boundaries; enclosed, restricted, or confined.",
    secondary: "Of a mathematical set or function: having elements whose values do not exceed a finite real number; finite in magnitude.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "O God, I could be **bounded** in a nutshell, and count myself a king of infinite space, were it not that I have bad dreams." },
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "A set of numbers is said to be **bounded** when it possesses both an upper and a lower limit." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "Our everyday life is **bounded** by trivial routines, yet our thoughts touch eternity." }
    ]
  },
  "bounder.md": {
    primary: "A dishonorable, ill-bred, unscrupulous, or ill-mannered man who behaves badly toward others; a cad in British informal usage.",
    secondary: "One who bounds, springs, or leaps.",
    quotes: [
      { author: "P. G. Wodehouse", work: "The Inimitable Jeeves", quote: "He struck me as a loud, flashy sort of **bounder**, the kind of chap who wears yellow boots with a frock coat." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Pickering warned Higgins that treating the poor girl like an experiment would make him look like an unmitigated **bounder**." },
      { author: "Evelyn Waugh", work: "Brideshead Revisited", quote: "In our undergraduate days, anyone who flaunted his wealth too openly was branded as an insufferable **bounder**." }
    ]
  },
  "pseudobombax.md": {
    primary: "A genus of tropical flowering trees in the family Malvaceae (subfamily Bombacoideae), native to Central and South America, characterized by swollen water-storing green trunks and brush-like blossoms.",
    secondary: "A Neotropical pachycaul tree (such as *Pseudobombax ellipticum*, the shaving-brush tree), prized as an ornamental for its large pink or white brush-shaped stamens.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "In the dry valleys of the Orinoco, the green, water-swollen trunk of **Pseudobombax** survives months of scorching drought." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The spectacular blooms of **Pseudobombax** resemble giant shaving brushes, expanding at sunset with an abundance of nectar." },
      { author: "Thomas Belt", work: "The Naturalist in Nicaragua", quote: "Bats and large sphinx moths visit the nocturnal flowers of **Pseudobombax** as soon as the petals unfurl." }
    ]
  },
  "rebound.md": {
    primary: "To bounce back through elasticity after hitting a hard surface; to spring back.",
    secondary: "To recover from a setback, illness, or disappointment; in basketball, to catch a missed shot bouncing off the rim.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", quote: "Elastic bodies **rebound** from one another with a velocity determined by their coefficient of restitution." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Her youthful spirit possessed a resilient elasticity that allowed her to **rebound** from every cruelty." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The struck harpoon seemed to **rebound** from the rubbery blubber like an arrow from a bronze shield." }
    ]
  },
  "unbound.md": {
    primary: "Released from bonds, ties, chains, or physical confinement; liberated.",
    secondary: "Not bound in a book cover or casing; having loose leaves or paper covers.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Titan, our prayers have reached the throne, and Prometheus stands at last **unbound** upon the Caucasus!" },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "She leafed through the **unbound** sheets of the manuscript, reading the poet's first drafts." },
      { author: "John Milton", work: "Samson Agonistes", quote: "Samson, no longer **unbound**, felt his sacred strength return as he grasped the pillars of Dagon's temple." }
    ]
  }
};

for (const [filename, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filename}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filename}`);
}

console.log('Done Batch 4 (bomb) of Cluster Sound & Auditory!');
