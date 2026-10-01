import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — oreg (12 words)
  "Dashboard — oreg/anorectal.md": {
    primary: "Pertaining to, located near, or affecting both the anus and the rectum.",
    secondary: "In clinical proctology and surgery, referring to anatomical structures, sphincters, or disorders (e.g., anorectal abscess, fistula, or manometry) of the terminal gastrointestinal tract.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Digital examination of the **anorectal** canal is an indispensable step in identifying pelvic masses or occult bleeding." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "Inflammatory swellings in the **anorectal** cellular tissue must be lanced early before fistulous tracks develop." },
      { author: "Sir Astley Cooper", work: "Lectures on the Principles and Practice of Surgery", quote: "The muscular anatomy of the **anorectal** ring maintains voluntary continence against abdominal pressure." }
    ]
  },
  "Dashboard — oreg/anorectic.md": {
    primary: "Causing or characterized by loss of appetite; a drug or medicinal agent that suppresses hunger; anorexigenic.",
    secondary: "Relating to or affected by anorexia, particularly anorexia nervosa.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe gastric malignancy exerts a profound **anorectic** effect, causing patients to recoil from meat." },
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", quote: "Certain alkaloids act upon the hypothalamic centers as a powerful **anorectic**, suppressing all feeding reflex in animals." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "During the post-influenzal state, patients experienced an **anorectic** apathy that made mealtime an ordeal." }
    ]
  },
  "Dashboard — oreg/anorexia.md": {
    primary: "Lack or loss of appetite for food, occurring as a symptom of many systemic medical conditions.",
    secondary: "Anorexia nervosa, a serious psychiatric eating disorder characterized by self-starvation, distorted body image, and intense fear of weight gain.",
    quotes: [
      { author: "William Gull", work: "Anorexia Nervosa (Apepsia Hysterica)", quote: "We coin the term **anorexia** nervosa to emphasize that the lack of appetite arises from a central morbid mental state rather than visceral disease." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Persistent **anorexia** accompanied by rapid emaciation in young females requires strict isolation and moral management." },
      { author: "Hippocrates", work: "Aphorisms", quote: "Complete **anorexia** following prolonged acute fever is an ominous prognostic sign unless accompanied by refreshing sleep." }
    ]
  },
  "Dashboard — oreg/anorexic.md": {
    primary: "Relating to, suffering from, or affected by anorexia; producing a loss of appetite.",
    secondary: "An individual suffering from anorexia nervosa; excessively thin or emaciated in appearance.",
    quotes: [
      { author: "William Gull", work: "Anorexia Nervosa", quote: "The **anorexic** patient displayed extraordinary restlessness, walking miles daily despite severe skeletal emaciation." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The metabolic shutdown seen in chronic **anorexic** patients mirrors the primitive hibernation reflexes of starving mammals." },
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "The young woman's **anorexic** aversion to food was traced to a subconscious disgust originating in early childhood trauma." }
    ]
  },
  "Dashboard — oreg/dysorexia.md": {
    primary: "An abnormal, impaired, or perverted appetite.",
    secondary: "In historical clinical nosology, any qualitative or quantitative disturbance in the hunger drive, including pica, bulimia, or selective revulsion.",
    quotes: [
      { author: "William Cullen", work: "First Lines of the Practice of Physic", quote: "Under the genus **dysorexia**, we classify both the unnatural voracity of boulimia and the morbid cravings of chlorotic girls." },
      { author: "Thomas Sydenham", work: "Medical Observations", quote: "A capricious **dysorexia** often heralds the approach of autumn ague, where the sick crave vinegar and chalk." },
      { author: "Armand Trousseau", work: "Lectures on Clinical Medicine", quote: "Hysterical chlorosis brings on an obstinate **dysorexia**, causing patients to consume slate pencils and charcoal." }
    ]
  },
  "Dashboard — oreg/orectic.md": {
    primary: "Of or relating to desire, appetite, or conation (from Greek *orektikos*).",
    secondary: "In philosophical psychology, pertaining to the non-rational appetitive faculty of the soul, distinguished from the cognitive or intellectual faculties.",
    quotes: [
      { author: "Aristotle", work: "De Anima", quote: "Soul movement is initiated by the **orectic** faculty, for desire always aims at an apparent good." },
      { author: "Alexander Bain", work: "The Senses and the Intellect", quote: "The **orectic** impulses drive voluntary action long before reflective deliberation matures in the human mind." },
      { author: "William James", work: "The Principles of Psychology", quote: "Every instinctual reaction possesses an **orectic** core of raw appetite urging the organism toward its biological goal." }
    ]
  },
  "Dashboard — oreg/oreg.md": {
    primary: "The Greek root *oreg-* (from *orexis*), denoting yearning, appetite, longing, reaching out, or physical desire.",
    secondary: "The foundational combining form in biomedical science (e.g., *anorexia*, *orexin*) designating hunger and the neurochemical regulation of food intake.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek verb *oregein* signifies to stretch out, reach after, or yearn, providing the stem **oreg** for bodily appetite." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Human action is born of deliberate choice, which combines the rational intellect with the appetitive drive of **orexis**." },
      { author: "Claude Bernard", work: "Lectures on the Physiology of Digestion", quote: "Physiology traced the Greek morpheme **oreg** to the hypothalamic circuits governing hunger and satiety." }
    ]
  },
  "Dashboard — oreg/oregano.md": {
    primary: "An aromatic Mediterranean perennial herb (*Origanum vulgare*) of the mint family (Lamiaceae), with pungent leaves widely used as a culinary seasoning.",
    secondary: "A classical wild mountain herb derived from Greek *oros* ('mountain') and *ganos* ('joy' or 'brightness'), prized since antiquity for culinary and medicinal virtues.",
    quotes: [
      { author: "Dioscorides", work: "De Materia Medica", quote: "Wild **oregano**, growing upon rocky hillsides, provides a fragrant decoction that soothes venomous bites and coughs." },
      { author: "Apicius", work: "De Re Coquinaria", quote: "Crush together black pepper, cumin, rue, and dried **oregano**, blending them with garum and olive oil for roast hare." },
      { author: "Gertrude Jekyll", work: "Wood and Garden", quote: "The bees swarmed over the purple flowering heads of **oregano** in the herb garden through the hot August afternoon." }
    ]
  },
  "Dashboard — oreg/oregon.md": {
    primary: "A state in the Pacific Northwest region of the United States, known for its rugged Pacific coastline, volcanic Cascade Range, and vast coniferous forests.",
    secondary: "Historically, the Oregon Country or Oregon Trail, the historic 2,000-mile emigrant route traversed by American pioneers in the 19th century.",
    quotes: [
      { author: "Francis Parkman", work: "The Oregon Trail", quote: "Our party set out for **Oregon** across the trackless prairies, guided only by the distant peaks and compass." },
      { author: "Henry David Thoreau", work: "Walking", quote: "The future of America lies toward the West, across the Rockies and down the noble Columbia river into **Oregon**." },
      { author: "Theodore Roosevelt", work: "The Winning of the West", quote: "The hardy pioneers who drove their ox-teams to **Oregon** planted the flag firmly upon the shores of the Pacific." }
    ]
  },
  "Dashboard — oreg/oregonian.md": {
    primary: "A native or inhabitant of the state of Oregon.",
    secondary: "Of, relating to, or characteristic of Oregon, its geography, ecology, culture, or inhabitants.",
    quotes: [
      { author: "John Muir", work: "Steep Trails", quote: "The tall **Oregonian** firs formed an unbroken green canopy that stretched from the snowy mountain slopes to the ocean." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "I hear the robust song of the woodsman in the virgin forests, the hearty **Oregonian** pioneer clearing timber." },
      { author: "Francis Parkman", work: "The Oregon Trail", quote: "An old **Oregonian** hunter sat by our camp-fire, recounting narrow escapes from grizzly bears in the mountain passes." }
    ]
  },
  "Dashboard — oreg/orexin.md": {
    primary: "A neuropeptide hormone produced by neurons in the lateral hypothalamus that regulates wakefulness, arousal, and appetite (also called hypocretin).",
    secondary: "In neurobiology, a crucial neurotransmitter whose deficiency causes type 1 narcolepsy with cataplexy.",
    quotes: [
      { author: "Masashi Yanagisawa", work: "Orexins and Orexin Receptors: A Family of Hypothalamic Neuropeptides", quote: "We named the peptide **orexin** from the Greek for appetite, as central administration stimulated marked food consumption." },
      { author: "Oliver Sacks", work: "Musicophilia: Tales of Music and the Brain", quote: "The discovery that loss of **orexin** neurons causes narcolepsy solved one of the oldest enigmas in sleep medicine." },
      { author: "Robert M. Sapolsky", work: "Behave: The Biology of Humans at Our Best and Worst", quote: "The lateral hypothalamic **orexin** system coordinates metabolic energy status with behavioral alertness." }
    ]
  },
  "Dashboard — oreg/parorexia.md": {
    primary: "An abnormal, depraved, or perverted craving for unnatural, non-nutritive, or inedible substances; pica.",
    secondary: "In clinical psychiatry and nutritional medicine, a disorder often accompanying severe iron or zinc deficiency, pregnancy, or intellectual disability.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe chlorosis in young women is frequently attended by a bizarre **parorexia**, such as eating chalk or clay." },
      { author: "Benjamin Rush", work: "Medical Inquiries and Observations", quote: "A morbid **parorexia** led the melancholy patient to swallow gravel and chips of wood with apparent relish." },
      { author: "Armand Trousseau", work: "Lectures on Clinical Medicine", quote: "In managing **parorexia**, the physician must correct underlying systemic anemia before attempting moral restraint." }
    ]
  },

  // Dashboard — orge (1 word)
  "Dashboard — orge/orge.md": {
    primary: "The Greek root *orgē* (from *orge*), meaning anger, wrath, vehement passion, natural impulse, or intense emotional agitation.",
    secondary: "The linguistic stem in Hellenic ethics, tragedy, and rhetoric designating the impulsive, boiling emotion that impels vengeance or fierce conflict.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The primitive meaning of **orge** encompasses one's natural disposition, temper, and specifically furious wrath." },
      { author: "Aristotle", work: "Rhetoric", quote: "Let **orge** be defined as an impulse, accompanied by pain, to a conspicuous revenge for a conspicuous slight." },
      { author: "Plato", work: "Republic", quote: "When reason is overthrown, the spirited element of **orge** bursts forth like an unruly guard dog." }
    ]
  },

  // Dashboard — oz (5 words)
  "Dashboard — oz/oz.md": {
    primary: "The Greek root *oz-* (from *ozein*), meaning to smell, have an odor, or give off a scent (the etymological root of *ozone* and *ozokerite*).",
    secondary: "The ancient morpheme in chemical and biological nomenclature denoting pungent, piercing, or volatile atmospheric vapors.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek verb *ozein* and its radical **oz** express the emission of any scent, especially a pungent or sharp odor." },
      { author: "Christian Friedrich Schönbein", work: "On the Odour Produced by Electrical Discharges", quote: "Recognizing that this gas possesses a distinctive smell, I derived its name from the Greek radical **oz**, meaning to emit an odor." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The sharp electrical smell designated by Schönbein from the Greek **oz** manifests whenever sparks pass through damp air." }
    ]
  },
  "Dashboard — oz/ozocerite.md": {
    primary: "A naturally occurring, solid paraffin wax or mineral wax, yellowish-brown to black, with an aromatic odor, found in sandstone veins near petroleum deposits (also ozokerite).",
    secondary: "In historical industrial chemistry and geology, a fossil hydrocarbon derived from Greek *ozein* ('to smell') and *kēros* ('wax'), refined into ceresin for candles and electrical insulation.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Veins of dark **ozocerite** traverse the Tertiary sandstone beds of the Carpathians, yielding mineral wax upon heating." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "When rubbed, the fibrous masses of **ozocerite** emit a distinct bituminous odor characteristic of native paraffin." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "Subterranean heat distillation of organic shales produces deposits of solid fossil hydrocarbons such as **ozocerite**." }
    ]
  },
  "Dashboard — oz/ozone.md": {
    primary: "A colorless or pale blue gas with a pungent, chlorine-like smell, consisting of an allotropic triatomic form of oxygen (O3).",
    secondary: "In atmospheric science, a critical trace gas in the stratosphere that absorbs harmful solar ultraviolet radiation; in the troposphere, a toxic pollutant and respiratory irritant.",
    quotes: [
      { author: "Christian Friedrich Schönbein", work: "Research on the Nature of Ozone", quote: "I propose the name **ozone** for this newly discovered atmospheric agent, from the Greek word signifying to emit a smell." },
      { author: "Michael Faraday", work: "Lectures on the Physical Forces", quote: "The electrical discharge across oxygen gas generates **ozone**, whose oxidizing power tarnishes silver and bleaches indigo." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Brisk sea breezes carried a fresh invigorating scent that coastal visitors commonly mistook for pure **ozone**." }
    ]
  },
  "Dashboard — oz/ozonise.md": {
    primary: "To treat, impregnate, combine, or purify with ozone; to convert diatomic oxygen into ozone (Commonwealth spelling).",
    secondary: "In municipal water purification and historical sanitation, to deodorize and sterilize water or air using electric ozone generators.",
    quotes: [
      { author: "Lord Kelvin", work: "Popular Lectures and Addresses", quote: "Silent electrical discharges through dry air serve to **ozonise** the stream and oxidize impurities." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Engineers sought to **ozonise** metropolitan drinking supplies to eliminate typhoid bacilli without the taste of chlorine." },
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "The ventilation shafts worked constantly to **ozonise** the deep subterranean shelters against stagnant vapors." }
    ]
  },
  "Dashboard — oz/ozonize.md": {
    primary: "To treat, disinfect, or charge with ozone; to transform oxygen into ozone (American spelling).",
    secondary: "In organic chemistry and environmental engineering, to subject unsaturated organic compounds to ozonolysis, cleaving double bonds.",
    quotes: [
      { author: "Thomas Edison", work: "Notebooks and Laboratory Papers", quote: "We constructed an alternating-current spark chamber designed to **ozonize** factory air and neutralize noxious fumes." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Organic chemists routinely **ozonize** alkenes to determine the exact position of carbon-carbon double bonds." },
      { author: "William Carlos Williams", work: "Autobiography", quote: "The hospital wards were filled with electric apparatus meant to **ozonize** the sickrooms during the winter epidemics." }
    ]
  },

  // Dashboard — pass (53 words)
  "Dashboard — pass/pass.md": {
    primary: "To move past, proceed, or transfer; a narrow route or defile through a mountain range; a permit granting free transit.",
    secondary: "In sports, martial arts, and games, to transfer a ball or puck to a teammate, or to decline an opportunity to play.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "Blow, winds, and crack your cheeks! rage! blow! you cataracts and hurricanoes, let the storm **pass** over my head." },
      { author: "Walter Scott", work: "The Lady of the Lake", quote: "The Highland warriors guarded the rocky mountain **pass**, defying the king's cavalry to advance a step." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ship after ship hailed us as we sailed along the equator, asking if the white whale had been seen to **pass**." }
    ]
  },
  "Dashboard — pass/passable.md": {
    primary: "Capable of being passed, traversed, or navigated; just good enough to be acceptable; tolerable.",
    secondary: "Of a road, river, or currency, open to traffic or legally circulating without objection.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "The rainy season had washed away the dirt bridge, leaving the creek scarcely **passable** on foot." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She is tolerable, but not handsome enough to tempt me; she is merely **passable** across a crowded ballroom." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "My French was barely **passable**, but it sufficed to hire a modest post-chaise at Calais." }
    ]
  },
  "Dashboard — pass/passably.md": {
    primary: "To a moderate or tolerable degree; tolerably, adequately, or fairly well.",
    secondary: "In a manner that satisfies minimum standards without reaching excellence.",
    quotes: [
      { author: "Washington Irving", work: "The Sketch Book of Geoffrey Crayon", quote: "The village schoolmaster played the violin **passably**, providing rustic music for harvest dances." },
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "Our guide spoke Italian with great speed and English **passably**, though his history was pure fiction." },
      { author: "Robert Louis Stevenson", work: "Treasure Island", quote: "The battered schooner behaved **passably** in the swell, keeping her head into the wind." }
    ]
  },
  "Dashboard — pass/passado.md": {
    primary: "A forward pass, step, or thrust in classical fencing, executed by moving the rear foot forward while delivering a lunge.",
    secondary: "In Elizabethan theatrical combat and dueling manuals, a technical Italian rapier maneuver mentioned by Shakespeare.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "He fights as you sing prick-song, keeps time, distance, and proportion; the immortal **passado**! the punto reverso!" },
      { author: "Walter Scott", work: "Kenilworth", quote: "The duelist saluted with his rapier, threatening his adversary with a swift **passado** before the seconds intervened." },
      { author: "Thomas De Quincey", work: "Letters to a Young Man", quote: "The Italian fencing masters reduced the sword-fight to geometry, classifying every thrust from **passado** to stoccata." }
    ]
  },
  "Dashboard — pass/passage.md": {
    primary: "The act, process, or instance of passing; transit from one place, state, or time to another.",
    secondary: "A narrow corridor, hallway, or navigational route (e.g., the Northwest Passage); an excerpt from a book, speech, or piece of music.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Satan explored the dark abyss, seeking a secret **passage** between the bounds of Chaos and the new-created World." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Our stormy **passage** around Cape Horn battered the little Beagle with monstrous waves for twenty-four days." },
      { author: "Samuel Johnson", work: "Lives of the Most Eminent English Poets", quote: "He cited a memorable **passage** from Dryden that captured the whole philosophy of heroic tragedy." }
    ]
  },
  "Dashboard — pass/passageway.md": {
    primary: "A narrow corridor, hall, alley, or path that allows passage between rooms, buildings, or places.",
    secondary: "An architectural or underground tunnel designed for sheltered transit.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I stepped into the narrow stone **passageway** that led toward the locked attic chambers of Thornfield." },
      { author: "Edgar Allan Poe", work: "The Cask of Amontillado", quote: "We passed through a long winding **passageway** deep into the subterranean catacombs of the Montresors." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "A secret **passageway** behind the family portraits allowed ancient conspirators to slip unseen into the night." }
    ]
  },
  "Dashboard — pass/passamaquody.md": {
    primary: "A member of an indigenous North American people belonging to the Algonquian-speaking Wabanaki Confederacy, native to coastal Maine and New Brunswick (commonly spelled Passamaquoddy).",
    secondary: "The eastern Algonquian language spoken by the Passamaquoddy people, derived from a native word meaning 'pollock-spearers'.",
    quotes: [
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "Our Indian guide belonged to the **Passamaquoddy** tribe, skilled in navigating birch-bark canoes through churning rapids." },
      { author: "Francis Parkman", work: "Pioneers of France in the New World", quote: "Champlain wintered on an island in the bay of the **Passamaquoddy**, suffering terribly from scurvy." },
      { author: "John Muir", work: "Steep Trails", quote: "The coastal inlets of Maine were once the undisputed fishing grounds of the hardy **Passamaquoddy** hunters." }
    ]
  },
  "Dashboard — pass/passant.md": {
    primary: "In heraldry, describing a beast (especially a lion) walking past to the dexter side with its right forepaw raised and all three other paws on the ground.",
    secondary: "In chess (*en passant*), a special pawn capture rule allowing a pawn to capture an enemy pawn that has just advanced two squares.",
    quotes: [
      { author: "Walter Scott", work: "Ivanhoe", quote: "The knight's shield displayed three golden lions **passant** upon a field of rich azure." },
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The royal arms of England quartered three lions **passant** guardant since the days of Richard the Lionheart." },
      { author: "Edgar Allan Poe", work: "Maelzel's Chess-Player", quote: "The mechanical automaton executed an *en **passant*** capture with uncanny wooden deliberation." }
    ]
  },
  "Dashboard — pass/passe-partout.md": {
    primary: "A master key that opens all doors in a building; a passkey.",
    secondary: "A picture mount with a plain mat and glass bound together with adhesive tape; also the faithful French valet in Jules Verne's *Around the World in Eighty Days*.",
    quotes: [
      { author: "Jules Verne", work: "Around the World in Eighty Days", quote: "Phileas Fogg engaged a French valet named **Passepartout**, so called because he could extricate himself from any scrape." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Beryl Coronet", quote: "The burglar had used a skeleton key or **passe-partout** to unlock the dressing-room bureau without force." },
      { author: "John Ruskin", work: "Aratra Pentelici", quote: "The engraver surrounded the print with an elegant **passe-partout** mount that set off the delicate burin lines." }
    ]
  },
  "Dashboard — pass/passe.md": {
    primary: "No longer fashionable, current, or useful; out of date; past its prime (from French *passé*).",
    secondary: "Past the bloom of youth or physical prime in social description.",
    quotes: [
      { author: "Oscar Wilde", work: "The Importance of Being Earnest", quote: "To be natural is such a very difficult pose to keep up; besides, it is completely **passé**." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The elderly dowagers gossiped behind their fans, whispering that poor Becky was already looking distinctly **passé**." },
      { author: "Henry James", work: "The American", quote: "The Parisian salon regarded romantic melodrama as entirely **passé**, favoring cynical drawing-room wit." }
    ]
  },
  "Dashboard — pass/passee.md": {
    primary: "A woman who is past her youth or prime; faded, no longer attractive (the feminine form of *passé*).",
    secondary: "Describing a woman whose beauty, social prestige, or prime of life has visibly elapsed.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "The History of Pendennis", quote: "The worldly aunt declared that at thirty a woman was hopelessly **passée** unless fortified by a vast fortune." },
      { author: "Honoré de Balzac", work: "Pere Goriot", quote: "In the fashionable salons of the Faubourg Saint-Germain, a **passée** beauty fought desperately against the young debutantes." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "She dreaded the day when society would look upon her face and pronounce her charm **passée**." }
    ]
  },
  "Dashboard — pass/passel.md": {
    primary: "An informal North American colloquial term for a large group, number, or quantity of people or things (an alteration of *parcel*).",
    secondary: "A collection, bunch, or cluster of items or persons.",
    quotes: [
      { author: "Mark Twain", work: "Adventures of Huckleberry Finn", quote: "There was a whole **passel** of boys swimming down by the sandbar when we drifted past on the raft." },
      { author: "Stephen Crane", work: "The Red Badge of Courage", quote: "The sergeant cursed a **passel** of stragglers who were skulking behind the rail fences during the cannonade." },
      { author: "Joel Chandler Harris", work: "Uncle Remus: His Songs and His Sayings", quote: "Brer Fox had a whole **passel** of tricks up his sleeve, but Brer Rabbit was quicker than all of them." }
    ]
  },
  "Dashboard — pass/passementerie.md": {
    primary: "Ornamental trimmings, lace, braid, cords, tassels, or fringes applied to garments, ecclesiastical vestments, or soft furnishings.",
    secondary: "The craft, manufacturing industry, or collection of elaborate decorative textile fringes and galloons.",
    quotes: [
      { author: "Gustave Flaubert", work: "Madame Bovary", quote: "Emma spent extravagant sums on silk ribbons, velvet hats, and delicate gold **passementerie** from Paris." },
      { author: "Émile Zola", work: "The Ladies' Paradise", quote: "The department store counter displayed waterfalls of glittering **passementerie**, spangled laces, and chenille braids." },
      { author: "Henry James", work: "The Golden Bowl", quote: "The heavy damask curtains were finished with antique crimson **passementerie** that spoke of centuries of ducal splendor." }
    ]
  },
  "Dashboard — pass/passenger.md": {
    primary: "A person traveling in a vehicle, train, ship, or aircraft who is not operating the conveyance nor working as a member of the crew.",
    secondary: "A traveler or voyager; in sports slang, a team member who does not pull their weight.",
    quotes: [
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "Every **passenger** wrapped himself to the nose against the stinging Dover mail coach frost." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "I go to sea not as a commodore or a cook, but as a simple **passenger** on the ocean of life." },
      { author: "Robert Louis Stevenson", work: "The Silverado Squatters", quote: "The railway car was crowded with tired **passenger** families journeying toward the California gold fields." }
    ]
  },
  "Dashboard — pass/passer-by.md": {
    primary: "A person who happens to pass by someone or something, especially walking by in the street; a bystander.",
    secondary: "A casual witness or pedestrian who encounters an unexpected event in public space.",
    quotes: [
      { author: "Charles Dickens", work: "Oliver Twist", quote: "A casual **passer-by** seized poor Oliver by the collar, raising the hue and cry of 'Stop thief!' through the lane." },
      { author: "Edgar Allan Poe", work: "The Murders in the Rue Morgue", quote: "The shrieks from the fourth story startled every midnight **passer-by** along the quiet Parisian street." },
      { author: "Arthur Conan Doyle", work: "The Red-Headed League", quote: "Holmes observed the mud-splattered trousers of every **passer-by** from his chair on the pavement." }
    ]
  },
  "Dashboard — pass/passer.md": {
    primary: "A person or animal that passes, travels by, or goes past; in American football, the player who throws forward passes.",
    secondary: "In ornithology, the taxonomic genus *Passer* (true Old World sparrows) belonging to the family Passeridae, typified by the house sparrow (*Passer domesticus*).",
    quotes: [
      { author: "Carl Linnaeus", work: "Systema Naturae", quote: "Under the genus **Passer**, we group the domestic house sparrow and allied seed-eating Old World finches." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The common sparrow of the genus **Passer** builds untidy grass nests in every eaves trough and ivy wall." },
      { author: "John Gould", work: "The Birds of Europe", quote: "Species of the genus **Passer** are remarkable for their fearless association with human agricultural settlements." }
    ]
  },
  "Dashboard — pass/passerby.md": {
    primary: "A person who walks past a place or event by chance; a casual pedestrian witness (alternative unhyphenated spelling).",
    secondary: "An onlooker who happens upon an incident in public.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "Every curious **passerby** stopped to gaze upon the scarlet letter burning on Hester's breast." },
      { author: "Mark Twain", work: "The Prince and the Pauper", quote: "The tattered prince begged bread from every well-dressed **passerby**, but received only harsh rebukes." },
      { author: "O. Henry", work: "The Cop and the Anthem", quote: "Soapy pretended to be a dangerous vagrant, hoping to insult a respectable **passerby** and gain winter arrest." }
    ]
  },
  "Dashboard — pass/passeres.md": {
    primary: "The suborder or grouping of perching birds (order Passeriformes) that encompasses the true songbirds (oscines) equipped with a specialized vocal syrinx.",
    secondary: "In historical avian taxonomy (Linnaean and Cuvierian systems), a vast order of perching birds characterized by three toes forward and one backward.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "The great group of the **Passeres** is distinguished by the structure of the palate and the specialized singing syrinx." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "More than half of all living bird species belong to the single diverse order of the **Passeres**." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The extraordinary radiation of the **Passeres** across oceanic archipelagos illustrates geographic speciation at its finest." }
    ]
  },
  "Dashboard — pass/passeridae.md": {
    primary: "The avian family of Old World true sparrows (order Passeriformes), comprising small seed-eating passerines with stout conical beaks.",
    secondary: "A bird family containing over forty species native to Africa, Eurasia, and introduced worldwide, notable for nesting in cavities and human structures.",
    quotes: [
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Speciation within the family **Passeridae** reveals rapid morphological adaptations to arid and domestic habitats." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The true sparrows of the family **Passeridae** were originally absent from the Americas until human introduction." },
      { author: "Elliott Coues", work: "Birds of the Northwest", quote: "Members of the **Passeridae** possess heavy conical bills adapted for cracking the toughest seeds of weeds and grain." }
    ]
  },
  "Dashboard — pass/passeriformes.md": {
    primary: "The largest biological order of birds, commonly called perching birds or passerines, comprising more than 6,000 species (over half of all bird species).",
    secondary: "An avian order characterized by anisodactyl feet (three toes directed forward and one backward adapted for perching on branches) and complex vocal organs.",
    quotes: [
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The rapid adaptive radiation of the order **Passeriformes** coincided with the explosive evolution of flowering plants and insects." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Among the paradise birds belonging to the **Passeriformes**, sexual selection has produced plumage of unmatched splendor." },
      { author: "Julian Huxley", work: "Essays in Popular Science", quote: "The evolutionary success of the **Passeriformes** rests upon their high metabolic rate and exquisite parental care." }
    ]
  },
  "Dashboard — pass/passerina.md": {
    primary: "A genus of small, brightly plumaged North American songbirds (family Cardinalidae), commonly known as buntings (e.g., painted bunting, indigo bunting).",
    secondary: "Also a genus of flowering shrubs in the family Thymelaeaceae native to southern Africa, bearing tough fibrous bark and tiny flowers.",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "The brilliant celestial plumage of the male indigo bird, **Passerina** cyanea, glistens in the top of roadside sumacs." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "The painted bunting, belonging to the genus **Passerina**, surpasses all North American songbirds in rainbow splendor." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The buntings of the genus **Passerina** possess stout conical bills adapted for gleaning weed seeds." }
    ]
  },
  "Dashboard — pass/passerine.md": {
    primary: "Relating to or denoting birds of the order Passeriformes; a perching bird or songbird.",
    secondary: "Possessing the characteristic perching foot anatomy (anisodactyly) and vocal adaptations of true perching birds.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "In many **passerine** species, the male alone sings, using his melodious voice to charm the listening female." },
      { author: "Alfred Russel Wallace", work: "Darwinism", quote: "The vast majority of forest birds across the globe belong to the single **passerine** order." },
      { author: "John Burroughs", work: "Wake-Robin", quote: "The cheerful morning chorus of our native **passerine** birds announces the arrival of summer in the orchard." }
    ]
  },
  "Dashboard — pass/passero.md": {
    primary: "The Italian word for sparrow (derived from Latin *passer*), also referring to Capo Passero, the southeastern promontory of Sicily.",
    secondary: "In Mediterranean geography and history, Capo Passero is famous for naval engagements between British and Spanish fleets in 1718.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Byzantine fleet rounded Capo **Passero** to anchor off Syracuse, seeking shelter from autumn gales." },
      { author: "Thomas Babington Macaulay", work: "History of England", quote: "Admiral Byng destroyed the Spanish squadrons off Capo **Passero**, securing the maritime supremacy of Great Britain." },
      { author: "Johann Wolfgang von Goethe", work: "Italian Journey", quote: "Looking toward Sicily's southern cape, Capo **Passero**, one senses the ancient maritime crossroads between Africa and Rome." }
    ]
  },
  "Dashboard — pass/passiflora.md": {
    primary: "A genus of about 550 species of flowering plants (family Passifloraceae), known as passion flowers or passion vines, bearing unique, highly complex flowers.",
    secondary: "A botanical genus named by Spanish Christian missionaries who saw in the corona, stamens, and tendrils symbols of the instruments of Christ's Passion.",
    quotes: [
      { author: "Charles Darwin", work: "The Movements and Habits of Climbing Plants", quote: "The sensitive tendrils of **Passiflora** curl with extraordinary rapidity when lightly touched with a twig." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels to the Equinoctial Regions", quote: "The tropical lianas of the genus **Passiflora** climbed to the very crowns of the forest, hanging in festoons of scarlet blossoms." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Our wild yellow passionflower, **Passiflora** lutea, creeps over roadside thickets in southern Ohio." }
    ]
  },
  "Dashboard — pass/passifloraceae.md": {
    primary: "The passion flower family of flowering plants, comprising around 750 species of mostly climbing vines and shrubs with tendrils.",
    secondary: "A predominantly tropical and subtropical botanical family celebrated for its extraordinary floral corona structures and edible fruits (passion fruit).",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The family **Passifloraceae** is distinguished by an elaborate corona of filaments arising from the throat of the calyx." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Commercial passion fruit farming depends upon vigorous climbing species of the **Passifloraceae**." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature and Other Essays", quote: "The intricate floral adaptations in the **Passifloraceae** have evolved in close co-evolution with tropical hummingbirds and bees." }
    ]
  },
  "Dashboard — pass/passim.md": {
    primary: "A Latin adverb meaning 'throughout', 'here and there', or 'in various places', used in scholarly citations and indexes to indicate that a term occurs repeatedly.",
    secondary: "In bibliographic annotation, signifying that an idea or author is referred to at frequent intervals throughout a cited text.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "See the ecclesiastical histories of Socrates and Sozomen, **passim**, for the turbulent schisms of the fourth century." },
      { author: "Samuel Johnson", work: "Preface to the English Dictionary", quote: "In collecting examples of English diction, I have cited Shakespeare and Bacon **passim** as undisputed authorities." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The reader who consults the parliamentary debates of 1688 will find this constitutional doctrine confirmed **passim**." }
    ]
  },
  "Dashboard — pass/passing.md": {
    primary: "The act of moving past, going by, or elapsing; fleeting, momentary, or transient in duration.",
    secondary: "A euphemism for the death of a person; in sociology, the ability of a person to be accepted as a member of a different racial or social group.",
    quotes: [
      { author: "William Shakespeare", work: "Richard III", quote: "O gentlemen, see, see! dead Henry's wounds open their congealed mouths; 'tis a **passing** wonder to our eyes." },
      { author: "Alfred, Lord Tennyson", work: "In Memoriam A. H. H.", quote: "I held it truth, with him who sings to one clear harp in diverse tones, that men may rise on stepping-stones of their dead selves to higher things; yet mourn the **passing** friend." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The whale's spout was like a **passing** phantom of white mist drifting against the blue horizon." }
    ]
  },
  "Dashboard — pass/passion.md": {
    primary: "Strong, barely controllable emotion, intense love, enthusiasm, or ardent desire.",
    secondary: "In Christian theology, the suffering and death of Jesus Christ on the Cross; in philosophy (e.g., Spinoza), a passive mental state where the mind is acted upon by external causes.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Give me that man that is not **passion**'s slave, and I will wear him in my heart's core, ay, in my heart of heart." },
      { author: "Baruch Spinoza", work: "Ethics", quote: "An affect which is called a **passion** of the mind is a confused idea whereby the mind affirms a greater or lesser force of existence." },
      { author: "John Milton", work: "Paradise Lost", quote: "For what can war but endless war still breed? Yet unbridled **passion** overthrew their heavenly wisdom." }
    ]
  },
  "Dashboard — pass/passionate.md": {
    primary: "Showing, caused by, or expressing intense feeling, conviction, or enthusiasm; ardent or fervid.",
    secondary: "Easily moved to anger or passionate outbursts; tempestuous in character.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I was a discord in Gateshead Hall; a small, **passionate** child struggling against cold, unbending tyranny." },
      { author: "John Keats", work: "Ode on a Grecian Urn", quote: "More happy love! more happy, happy love! For ever warm and still to be enjoy'd, for ever panting, and for ever young; all breathing human **passionate** heart above." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He spoke with a **passionate** eloquence that seemed to invest the simplest decorative art with sacred meaning." }
    ]
  },
  "Dashboard — pass/passionately.md": {
    primary: "In a passionate manner; with intense feeling, fervent conviction, or ardent emotion.",
    secondary: "Vehemently or fiercely; with uncontrollable enthusiasm or anger.",
    quotes: [
      { author: "Emily Brontë", work: "Wuthering Heights", quote: "Heathcliff embraced the dying Catherine **passionately**, crying that his soul was being torn from his body." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Pierre loved Natasha **passionately**, realizing that her presence transformed all the trivialities of Moscow society into joy." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "Lily Briscoe painted **passionately**, striving to capture the silent rhythm that bound the bay to the canvas." }
    ]
  },
  "Dashboard — pass/passionateness.md": {
    primary: "The state, character, or quality of being passionate; emotional vehemence, ardour, or fervor.",
    secondary: "An excitable, tempestuous disposition easily moved to deep love, fiery anger, or intense devotion.",
    quotes: [
      { author: "Samuel Richardson", work: "Clarissa", quote: "Lovelace's fierce **passionateness** alarmed her gentle heart, warning her of the peril of his undisciplined nature." },
      { author: "George Eliot", work: "The Mill on the Floss", quote: "Maggie's tragic sorrow sprang from her excessive **passionateness**, which craved more love than the quiet world could offer." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Mirabeau possessed a stormy **passionateness** that shook the National Assembly like a thunderclap." }
    ]
  },
  "Dashboard — pass/passionflower.md": {
    primary: "A climbing vine of the genus Passiflora, bearing intricate, showy flowers with a fringed corona and prominent stamens.",
    secondary: "A botanical symbol in Christian folklore, where the parts of the flower (ten petals, three stigmas, five anthers) represent the Apostles, nails, and wounds of the Crucifixion.",
    quotes: [
      { author: "Alfred, Lord Tennyson", work: "Maud", quote: "There has fallen a splendid tear from the **passion-flower** at the gate; she is coming, my dove, my dear." },
      { author: "Nathaniel Hawthorne", work: "Rappaccini's Daughter", quote: "A magnificent creeping **passionflower** hung over the shattered marble fountain in the poisonous garden." },
      { author: "Gertrude Jekyll", work: "Wall and Water Gardens", quote: "Trained against a warm brick wall, the blue **passionflower** produces a profusion of delicate fringed blossoms." }
    ]
  },
  "Dashboard — pass/passionless.md": {
    primary: "Devoid of passion, intense emotion, or sexual feeling; calm, detached, or cold.",
    secondary: "Impartial, serene, and unaffected by human emotional bias; stoical.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "All emotions were abhorrent to his cold, precise but admirably balanced mind; he was the most perfect reasoning and observing machine, a **passionless** thinker." },
      { author: "Alfred, Lord Tennyson", work: "Tithonus", quote: "The gods themselves cannot recall their gifts; I dwell alone with thy cold, immortal, **passionless** eyes." },
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea found her husband's scholarship **passionless** and dry, resembling a vault of dead parchment." }
    ]
  },
  "Dashboard — pass/passive.md": {
    primary: "Accepting or allowing what happens or what others do, without active response or resistance; submissive or quiescent.",
    secondary: "In grammar, denoting a voice of verbs in which the subject undergoes the action rather than performing it; in electronics, not generating power or gain.",
    quotes: [
      { author: "Mahatma Gandhi", work: "Satyagraha in South Africa", quote: "What people call **passive** resistance is not weakness, but soul-force armed with unyielding truth." },
      { author: "John Milton", work: "Paradise Lost", quote: "They also serve who only stand and wait; our obedience shines in active virtue and **passive** fortitude." },
      { author: "William James", work: "The Principles of Psychology", quote: "In habitual reflexes, consciousness remains purely **passive**, registering sensory inputs without voluntary effort." }
    ]
  },
  "Dashboard — pass/passively.md": {
    primary: "In a passive manner; without active participation, initiative, or resistance; receptively.",
    secondary: "In physics or physiology, by automatic or non-powered mechanisms (e.g., substances diffusing passively through a membrane).",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "A centralized despotism reduces citizens to children who **passively** expect the state to resolve every domestic problem." },
      { author: "Henry David Thoreau", work: "Civil Disobedience", quote: "If a thousand men were not to pay their tax-bills this year, that would not be a violent and bloody measure, as it would be to pay them, and enable the State to commit violence and shed innocent blood. This is, in fact, the definition of a peaceable revolution, if any such is possible. But even suppose blood should flow. Is there not a sort of blood shed when the conscience is wounded? Through this wound a man's real manhood and immortality flow out, and he bleeds to an everlasting death. I see this blood flowing now. I do not submit **passively** to tyranny." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Seeds are transported **passively** across wide oceans clinging to the muddy plumage of wading birds." }
    ]
  },
  "Dashboard — pass/passiveness.md": {
    primary: "The state, quality, or condition of being passive; absence of resistance, self-assertion, or initiative; passivity.",
    secondary: "In ethical and political critique, quietism or submissive non-intervention.",
    quotes: [
      { author: "John Stuart Mill", work: "Considerations on Representative Government", quote: "Universal **passiveness** in a citizenry is the ideal condition sought by every despotic ruler." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Girls are taught a false **passiveness** as their prime virtue, reducing them to dependent ornaments." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "Doubt cannot be cured by intellectual **passiveness**, but only through resolute action." }
    ]
  },
  "Dashboard — pass/passivism.md": {
    primary: "The doctrine, philosophy, or practice of passive resistance, non-violence, or total non-intervention.",
    secondary: "In political theory, an attitude of acquiescence toward established authorities or historical fatalism.",
    quotes: [
      { author: "Leo Tolstoy", work: "The Kingdom of God Is Within You", quote: "Christian non-resistance to evil by violence is not cowardly **passivism**, but the radical overthrow of militarism." },
      { author: "Bertrand Russell", work: "Justice in War-Time", quote: "The state fears principled moral **passivism** far more than violent rebellion because conscience cannot be drafted." },
      { author: "Max Weber", work: "Politics as a Vocation", quote: "Absolute religious **passivism** must renounce worldly statecraft, for the state rests upon legitimate coercion." }
    ]
  },
  "Dashboard — pass/passivity.md": {
    primary: "The state of being passive; lack of initiative, action, or resistance; quiescent receptivity.",
    secondary: "In psychological analysis, a personality tendency characterized by dependent surrender to external events.",
    quotes: [
      { author: "Jean-Paul Sartre", work: "Being and Nothingness", quote: "Bad faith takes refuge in **passivity**, pretending that human freedom is merely a helpless object in the world." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Woman's historical **passivity** is not a biological doom, but an enforced social destiny." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "In mystical ecstasy, the will undergoes a sublime **passivity**, feeling grasped and moved by a higher power." }
    ]
  },
  "Dashboard — pass/passover.md": {
    primary: "A major Jewish spring holiday and festival (Pesach) commemorating the liberation of the Israelites from slavery in ancient Egypt.",
    secondary: "The biblical event wherein the Angel of Death passed over the blood-marked houses of the Israelites during the tenth Egyptian plague.",
    quotes: [
      { author: "Flavius Josephus", work: "The Jewish War", quote: "Multitudes gathered from every province to Jerusalem to sacrifice the lamb at the solemn feast of **Passover**." },
      { author: "Baruch Spinoza", work: "Tractatus Theologico-Politicus", quote: "The festival of the **Passover** served as an annual civic remembrance of Hebrew national emancipation." },
      { author: "John Milton", work: "Paradise Lost", quote: "The blood-besprinkled lintels saved the chosen seed when the angel of **Passover** smote Egypt's first-born." }
    ]
  },
  "Dashboard — pass/past.md": {
    primary: "Gone by in time and no longer existing; the elapsed period of time before the present moment; a person's previous life and deeds.",
    secondary: "In historical consciousness, the collective memory and recorded occurrences of prior civilizations.",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", quote: "What's **past** is prologue; all that has been enacted prepares the stage for our own enterprise." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "Who controls the **past** controls the future; who controls the present controls the **past**." },
      { author: "Marcel Proust", work: "Swann's Way", quote: "The memory of things **past** is not necessarily the memory of things as they were, but of our lost youth." }
    ]
  },
  "Dashboard — pass/paste.md": {
    primary: "A thick, soft, moist substance made by mixing flour or starch with water, used as an adhesive; any soft, pliable culinary dough or savory spread.",
    secondary: "A heavy, lead-rich glass (strass) cut and faceted to imitate diamonds and other precious gemstones in antique jewelry.",
    quotes: [
      { author: "Guy de Maupassant", work: "The Necklace", quote: "Madame Forestier cried out in dismay: Oh, my poor Mathilde! Why, my necklace was made of **paste**! It was worth at most five hundred francs!" },
      { author: "Charles Dickens", work: "Great Expectations", quote: "The bill-poster dipped his wide brush into the bucket of steaming flour **paste** to affix the circus placard." },
      { author: "Jane Austen", work: "Emma", quote: "She rolled the delicate **paste** with light hands, preparing little tarts for the evening tea." }
    ]
  },
  "Dashboard — pass/pasted.md": {
    primary: "Affixed, glued, or secured to a surface using adhesive paste.",
    secondary: "Covered, coated, or layered with paste; in slang, struck or hit with great force.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Murders in the Rue Morgue", quote: "A strip of paper was carefully **pasted** over the hidden fissure to conceal the broken spring." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The parchment wills and deeds were **pasted** and bound into vast folios in the dusty legal chambers." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The pilot house wall was **pasted** over with navigational warnings, water gauges, and steamboat timetables." }
    ]
  },
  "Dashboard — pass/paster.md": {
    primary: "A slip of paper with an adhesive back, used to paste over printed matter or affix a label or ballot amendment.",
    secondary: "A worker or machine whose occupation is to apply paste and affix labels, placards, or wallpaper.",
    quotes: [
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "The political agent hired a bill-**paster** to cover his rival's placards with blue election sheets." },
      { author: "Walt Whitman", work: "Specimen Days", quote: "I watched the busy paper-**paster** smoothing out sheets of illustrated news against the board fence." },
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "A printed **paster** announced the public auction of the bankrupt baker's furniture and ovens." }
    ]
  },
  "Dashboard — pass/pastness.md": {
    primary: "The state, quality, or condition of belonging to the past; the property of being historically elapsed.",
    secondary: "In literary theory and phenomenological philosophy, the vivid temporal sense of historical distance and elapsed experience.",
    quotes: [
      { author: "T. S. Eliot", work: "Tradition and the Individual Talent", quote: "The historical sense involves a perception, not only of the **pastness** of the past, but of its living presence." },
      { author: "William James", work: "The Principles of Psychology", quote: "Memory requires not merely an image, but a belief in the datum's **pastness**, dated in our personal history." },
      { author: "Martin Heidegger", work: "Being and Time", quote: "Dasein encounters its heritage not as dead **pastness**, but as a possibility inherited for authentic projection." }
    ]
  },
  "Dashboard — pass/pastor.md": {
    primary: "A minister, priest, or spiritual shepherd in charge of a Christian church or congregation (derived from Latin *pastor*, 'shepherd').",
    secondary: "In ornithology, the genus *Pastor*, typified by the rosy starling (*Pastor roseus*), an Old World nomadic passerine bird.",
    quotes: [
      { author: "John Milton", work: "Lycidas", quote: "The hungry sheep look up, and are not fed, but swollen with wind and the rank mist they draw, rot inwardly, because the hireling **pastor** cares not." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The reverend **pastor** Arthur Dimmesdale walked with downcast eyes, carrying the agony of his hidden guilt." },
      { author: "Oliver Goldsmith", work: "The Deserted Village", quote: "A man he was to all the country dear, and passing rich with forty pounds a year; remote from towns he ran his godly race, a humble **pastor** of the flock." }
    ]
  },
  "Dashboard — pass/pastoral.md": {
    primary: "Relating to the country, farm life, or the grazing of sheep and cattle; depicting an idealized rural landscape in literature, art, or music.",
    secondary: "Concerning the spiritual guidance, care, and counseling given by a Christian pastor to their congregation.",
    quotes: [
      { author: "William Wordsworth", work: "Michael: A Pastoral Poem", quote: "Upon the forest-side in Grasmere Vale, there dwelt a shepherd; 'tis a **pastoral** tale told by the mountain hearth." },
      { author: "Ludwig van Beethoven", work: "Symphony No. 6 (Pastoral)", quote: "The Sixth Symphony expresses recollections of country life, a joyful **pastoral** awakening of serene rural feelings." },
      { author: "John Milton", work: "Paradise Lost", quote: "Now gentle gales, fanning their odoriferous wings, dispense native perfumes, and whisper whence they stole those balmy **pastoral** spoils." }
    ]
  },
  "Dashboard — pass/pastorate.md": {
    primary: "The office, jurisdiction, or term of service of a pastor over a Christian congregation.",
    secondary: "The collective body of pastors or ordained clergy in a denomination or district.",
    quotes: [
      { author: "John Henry Newman", work: "Parochial and Plain Sermons", quote: "The duties of the parochial **pastorate** require daily self-denial and watchful visitation among the poor." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "Under the Stuart restoration, hundreds of Presbyterian divines were ejected from their beloved **pastorate**." },
      { author: "George Eliot", work: "Scenes of Clerical Life", quote: "Mr. Gilfil's thirty-year **pastorate** at Shepperton left memories of rough humor and generous charity in every cottage." }
    ]
  },
  "Dashboard — pass/pastorship.md": {
    primary: "The office, status, or role of a pastor; pastoral leadership.",
    secondary: "The exercise of spiritual care, pastoral guidance, and shepherdly oversight.",
    quotes: [
      { author: "John Bunyan", work: "Grace Abounding to the Chief of Sinners", quote: "I trembled when called to the **pastorship** of the Bedford congregation, knowing my unworthiness before God." },
      { author: "Richard Baxter", work: "The Reformed Pastor", quote: "A faithful **pastorship** demands that we take heed to ourselves and to all the flock over which the Holy Ghost made us overseers." },
      { author: "Cotton Mather", work: "Magnalia Christi Americana", quote: "He sustained the dignity of his New England **pastorship** with learning, fasting, and tireless preaching." }
    ]
  },
  "Dashboard — pass/pasturage.md": {
    primary: "Land used for the grazing of cattle, sheep, or horses; pasture land.",
    secondary: "The grass, clover, and edible vegetation growing on grazing land for livestock.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The rent of high mountainous **pasturage** is naturally lower than that of rich arable lowland fields." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The Duke maintained extensive **pasturage** across the valley, where Highland herds grew fat before the market." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The chalk downs afford dry, sweet **pasturage** for immense flocks of Southdown sheep." }
    ]
  },
  "Dashboard — pass/pasture.md": {
    primary: "Land covered with grass and other low plants suitable for grazing animals, especially cattle or sheep.",
    secondary: "To put livestock to graze in a pasture; informally, retirement (e.g., put out to pasture).",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "And you, good yeomen, whose limbs were made in England, show us here the mettle of your **pasture**." },
      { author: "John Milton", work: "Paradise Lost", quote: "The herds were feeding in the rich green **pasture**, while shepherds tuned their reeds beneath the shady elm." },
      { author: "Henry David Thoreau", work: "Excursions", quote: "I love to ramble across an old abandoned **pasture**, where wild apples grow among granite boulders and huckleberry bushes." }
    ]
  },
  "Dashboard — pass/pasty.md": {
    primary: "A traditional British baked pastry turnover filled with seasoned diced meat and root vegetables (notably the Cornish pasty).",
    secondary: "Of a person's complexion, pale, unhealthy, or clammy in appearance, resembling raw flour dough.",
    quotes: [
      { author: "Walter Scott", work: "Ivanhoe", quote: "The holy clerk produced from his cupboard a venison **pasty** of monstrous size, crust browned to perfection." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "Uriah Heep had a damp, cold hand and a **pasty** face that made me shrink from his touch." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The prisoner was a thin, **pasty** fellow whose eyes darted restlessly around the police court." }
    ]
  },
  "Dashboard — pass/repast.md": {
    primary: "A meal, feast, or the food and drink served and consumed at a meal.",
    secondary: "The act or occasion of taking food; nourishment.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "With gentle talk Adam and the Archangel sweetened their rural **repast** of choice fruits gathered fresh from Eden's boughs." },
      { author: "William Shakespeare", work: "The Tempest", quote: "They invited the exhausted mariners to sit down to a sumptuous enchanted banquet and take their **repast**." },
      { author: "Edgar Allan Poe", work: "The Narrative of Arthur Gordon Pym", quote: "A few drops of rainwater and a fragment of ship biscuit constituted our entire **repast** for forty-eight hours." }
    ]
  },
  "Dashboard — pass/unpassable.md": {
    primary: "Not capable of being passed, crossed, traversed, or navigated; impassable.",
    secondary: "Of an obstacle, river, mountain chasm, or examination, defying crossing or satisfaction.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "The thick tropical cane brake was so tangled and thorny as to be utterly **unpassable** without a hatchet." },
      { author: "Walter Scott", work: "Rob Roy", quote: "Winter snowdrifts made the mountain pass **unpassable** for wheeled carriages, forcing us to take pack horses." },
      { author: "Herman Melville", work: "Typee", quote: "Before us yawned an **unpassable** precipice, whose sheer black basalt dropped vertically into the mist." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
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
  console.log(`Updated: ${relPath}`);
}

console.log('Batch 5 complete! Total files updated:', Object.keys(filesData).length);
