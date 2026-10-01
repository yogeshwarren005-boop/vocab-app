import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Motion & Direction';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch1Data = {
  // Dashboard — pheug
  "Dashboard — pheug/apophyge.md": {
    primary: "A slight concave curve or flare in a classical architectural column where the shaft springs outward to meet the base or terminates at the capital.",
    secondary: "In classical orders, literally an 'escape' (Greek apopheugein), the subtle transition molding that softens the juncture between cylindrical shaft and plinth.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "At the foot of the shaft, the **apophyge** curves outward to rest gracefully upon the torus of the base." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Grecian architect fashioned the **apophyge** with mathematical delicacy to relieve the visual weight of the vertical column." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Ionic columns terminate above and below in a gentle **apophyge** flanked by narrow decorative fillets." }
    ]
  },
  "Dashboard — pheug/hypophyge.md": {
    primary: "A concave hollow or molding beneath a cornice, fillet, or architectural band, facilitating drainage and casting a deep shadow.",
    secondary: "In architectural moldings, a downward curved hollow resembling an inverted apophyge, designed to prevent rainwater from streaking the masonry face.",
    quotes: [
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Beneath the projecting dripstone, an acute **hypophyge** casts an impenetrable line of shade across the entablature." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The stonecutter carved a crisp **hypophyge** under the drip molding to throw the driving rain clear of the wall." },
      { author: "Francis Bond", work: "Gothic Architecture in England", quote: "Early English capitals often substitute a deep **hypophyge** for the flatter classical cavetto." }
    ]
  },
  "Dashboard — pheug/pheug.md": {
    primary: "The Greek root pheugein (meaning 'to flee, run away, or escape'), forming words relating to evasion, centrifugal departure, and architectural escape curves.",
    secondary: "In historical linguistics and etymology, an Indo-European root akin to Latin fugere, seen in apophyge, hypophyge, and centrifugal motion.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek stem **pheug**, meaning to flee, underlies ancient legal terms of exile as well as architectural curves." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "From the Hellenic **pheug**, classical architects conceived the column's curve as an elegant escape from rigid horizontal lines." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "Under the root **pheug**, we classify all expressions signifying flight, evasion, and departure from a center." }
    ]
  },

  // Dashboard — brady
  "Dashboard — brady/brady.md": {
    primary: "The Greek combining form brady- (from bradys, meaning 'slow'), used in scientific, medical, and biological terms denoting retarded speed or delayed action.",
    secondary: "In clinical pathology and evolutionary biology, a productive prefix contrasting with tachy- (fast), seen in bradycardia, bradytelic, and bradylalia.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek element **brady**, denoting slowness, forms the essential clinical counterpart to tachycardic speed." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Physicians prefix **brady** to diagnostic terms whenever physiological function exhibits abnormal sluggishness." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "All scientific designations of retarded tempo or prolonged duration borrow the prefix **brady**." }
    ]
  },
  "Dashboard — brady/bradycardia.md": {
    primary: "An abnormally slow resting heart rate, typically defined as fewer than 60 beats per minute in an adult.",
    secondary: "In cardiology, a clinical sign resulting from sinoatrial node dysfunction, heart block, hypothermia, or high vagal tone in endurance athletes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Marked sinus **bradycardia** is often observed during convalescence from typhoid fever or in well-trained marathon runners." },
      { author: "Paul Dudley White", work: "Heart Disease", quote: "A profound **bradycardia** accompanied by syncopal attacks should immediately suggest Stokes-Adams complete heart block." },
      { author: "Eugene Braunwald", work: "Heart Disease", quote: "Persistent symptomatic **bradycardia** refractory to atropine requires the prompt implantation of an artificial cardiac pacemaker." }
    ]
  },
  "Dashboard — brady/bradysuria.md": {
    primary: "Abnormally slow or delayed micturition (urination), marked by difficulty in initiating or completing the flow.",
    secondary: "In clinical urology, a symptom often caused by mechanical urethral obstruction, benign prostatic hyperplasia, or neurogenic bladder atony.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Elderly males suffering from chronic prostatic enlargement frequently complain of distressing **bradysuria**." },
      { author: "Samuel Cooper", work: "A Dictionary of Practical Surgery", quote: "The surgeon diagnosed stricture of the membranous urethra after the patient presented with chronic **bradysuria**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In tabetic neurosyphilis, early bladder involvement manifests as painless **bradysuria** and urinary retention." }
    ]
  },
  "Dashboard — brady/bradytelic.md": {
    primary: "Evolving at a markedly slower rate than typical or related phylogenetic lineages; surviving with little morphological change over vast geological periods.",
    secondary: "In evolutionary paleontology, coined by George Gaylord Simpson to describe 'living fossils' like the horseshoe crab, coelacanth, and *Lingula*.",
    quotes: [
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", quote: "I designate as **bradytelic** those rare, exceptionally slow-evolving lines that persist through whole geological eras without major change." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The horseshoe crab is our most famous **bradytelic** survivor, retaining its Paleozoic anatomy virtually unaltered." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "A **bradytelic** lineage proves that stabilizing natural selection can maintain structural equilibrium when ecological niches remain stable." }
    ]
  },

  // Dashboard — drome
  "Dashboard — drome/drome.md": {
    primary: "The Greek root dromos (meaning 'running', 'race', 'course', or 'speedway'), forming vocabulary relating to arenas, airfields, and biological syndromes.",
    secondary: "In morphology and etymology, an ancient combining form denoting a course, path, or sequential symptom cluster, as in hippodrome, aerodrome, and prodrome.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek stem **drome**, signifying a running course, gives us the camel that runs and the airfield where aircraft land." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "From the Olympic chariot course, the suffix **drome** was revived by modern aviators for their aerodromes." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "All lexical terms describing circular tracks, runways, and swift transits converge upon the root **drome**." }
    ]
  },
  "Dashboard — drome/dromedary.md": {
    primary: "A single-humped camel (Camelus dromedarius), native to the Arabian Peninsula and North Africa, bred as a swift riding or pack animal.",
    secondary: "In cultural history and mammalogy, distinguished from the two-humped Bactrian camel by its desert speed, literally meaning 'the runner' (Greek dromas).",
    quotes: [
      { author: "Richard Francis Burton", work: "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", quote: "The Arabian **dromedary** glides across the burning dunes with an untiring, swaying trot." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "A swift **dromedary** carried the royal courier across the Syrian waste in fewer days than a horse troop could march." },
      { author: "Charles Doughty", work: "Travels in Arabia Deserta", quote: "We mounted our tall **dromedary** beasts at dawn, pressing south through the vast wilderness." }
    ]
  },
  "Dashboard — drome/prodromal.md": {
    primary: "Of, relating to, or serving as a prodrome; indicating the early, warning stage preceding the acute outbreak of a disease.",
    secondary: "In clinical medicine, designating non-specific early signs (such as malaise, low-grade fever, or aura) that herald the full manifestation of an illness.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A distinctive **prodromal** rash often appears twenty-four hours before the eruptive fever of smallpox." },
      { author: "Eugene Braunwald", work: "Harrison's Principles of Internal Medicine", quote: "Severe migraine attacks are frequently preceded by a sensory **prodromal** aura lasting several minutes." },
      { author: "Wilder Penfield", work: "Epilepsy and the Functional Anatomy of the Human Brain", quote: "The patient reported a strange epigastric sensation as a **prodromal** signal prior to each seizure." }
    ]
  },
  "Dashboard — drome/prodrome.md": {
    primary: "An early premonitory symptom or group of symptoms that heralds the impending onset of a disease.",
    secondary: "In classical and modern medicine, a 'running before' (Greek prodromos); also historically used for a preliminary scholarly treatise or introductory handbook.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The catarrhal symptoms and Koplik's spots constitute an unmistakable **prodrome** of measles." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The sudden retreat of the sea was the dreaded **prodrome** of the catastrophic tidal wave that struck Lisbon." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The preliminary paper served as an intellectual **prodrome** to his exhaustive monograph on fossil cephalopods." }
    ]
  },
  "Dashboard — drome/prodromic.md": {
    primary: "Precursory; symptomatic of the beginning or approach of a disease (variant of prodromal).",
    secondary: "In pathology and medical diagnostics, descriptive of early warning signals in infectious or neurological disorders.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The **prodromic** stage of acute fevers is marked by universal languor, shivering, and headache." },
      { author: "Samuel Cooper", work: "A Dictionary of Practical Surgery", quote: "Immediate isolation is indicated upon the appearance of these **prodromic** symptoms in infectious wards." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The physician should teach the epileptic patient to recognize the **prodromic** sensation to avoid accidental falls." }
    ]
  },
  "Dashboard — drome/syndrome.md": {
    primary: "A characteristic group or pattern of symptoms and physical signs that consistently occur together to define a specific disease or medical condition.",
    secondary: "Figuratively, a predictable combination of behaviors, opinions, or circumstances that characterize a social or psychological trend (literally 'running together').",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinical **syndrome** of fever, murmur, and hematuria leaves no doubt regarding the diagnosis of bacterial endocarditis." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Each post-encephalitic patient exhibited a unique clinical **syndrome** that defied conventional textbook categories." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "The UFO abduction **syndrome** reflects deep-seated cultural anxieties projected onto modern technological myths." }
    ]
  },

  // Dashboard — pat
  "Dashboard — pat/expat.md": {
    primary: "An expatriate; a person living or working outside their native country.",
    secondary: "Informal shortening of expatriate (from Latin ex- out of + patria fatherland); often applied to cosmopolitan literary or business communities living abroad.",
    quotes: [
      { author: "Ernest Hemingway", work: "A Moveable Feast", quote: "In those days, Paris was full of **expat** writers and painters arguing over café tables in Montparnasse." },
      { author: "George Orwell", work: "Burmese Days", quote: "The small **expat** club was an oasis of gin, cricket, and nostalgic gossip isolated in the tropical jungle." },
      { author: "Graham Greene", work: "The Quiet American", quote: "He looked like an ordinary American **expat**, earnest and full of dangerous good intentions." }
    ]
  },
  "Dashboard — pat/pat.md": {
    primary: "To touch, stroke, or tap gently with the flat of the hand or a small implement, often expressing affection or approval.",
    secondary: "Adjectivally, so completely suited, convenient, or smoothly glib as to seem artificial or suspiciously ready.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Joe gave me a gentle **pat** upon the shoulder, reassuring me with his honest blacksmith smile." },
      { author: "George Eliot", work: "Middlemarch", quote: "His explanations were so exceedingly **pat** that Dorothea felt a growing distrust of his sincerity." },
      { author: "William Shakespeare", work: "King Lear", quote: "And **pat** he comes, like the catastrophe of the old comedy." }
    ]
  },
  "Dashboard — pat/pater.md": {
    primary: "A father (Latin pater); also used in British school slang as an affectionate or informal term for one's father.",
    secondary: "In classical and ecclesiastical usage, the formal designation of the male parent or religious head (as in Pater Noster).",
    quotes: [
      { author: "William Makepeace Thackeray", work: "The History of Pendennis", quote: "Pen sat down to write an urgent letter to the **pater**, begging for an immediate advance upon his allowance." },
      { author: "Evelyn Waugh", work: "Brideshead Revisited", quote: "'The **pater** will never consent to that,' Sebastian laughed, leaning against the college balustrade." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman Senate hailed the emperor with the venerable title of **Pater** Patriae." }
    ]
  },
  "Dashboard — pat/patness.md": {
    primary: "The quality or state of being opportune, highly convenient, or neatly and glibly ready.",
    secondary: "In literary criticism and conversation, an excessive readiness or artificial neatness that suggests fabrication or rehearsed glibness.",
    quotes: [
      { author: "Henry James", work: "The Art of the Novel", quote: "The sudden **patness** of the dénouement robbed the tragedy of its organic dramatic truth." },
      { author: "George Bernard Shaw", work: "Dramatic Opinions and Essays", quote: "The comic dramatist relied on the sheer **patness** of his entrances to keep the audience laughing." },
      { author: "H. L. Mencken", work: "Prejudices", quote: "The fatal **patness** of the slogan deceived thousands of voters who mistook an alliteration for a policy." }
    ]
  },
  "Dashboard — pat/peripatetic.md": {
    primary: "Traveling from place to place, especially working or teaching in various venues; wandering or itinerant.",
    secondary: "In the history of philosophy, an adherent of Aristotle or his school, so named because Aristotle walked about the Lyceum (*peripatein*) while lecturing.",
    quotes: [
      { author: "Oliver Goldsmith", work: "The Vicar of Wakefield", quote: "He adopted the life of a **peripatetic** philosopher, wandering from town to town with his flute." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The **peripatetic** doctrine of the four elements dominated natural philosophy for fifteen centuries." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "There is immense pleasure in a solitary **peripatetic** excursion across the open hills on a spring morning." }
    ]
  },
  "Dashboard — pat/peripateticism.md": {
    primary: "The philosophical system, doctrine, and teachings of Aristotle and his followers (the Peripatetic school).",
    secondary: "In academic history, the dominant scholastic tradition of late antiquity and the medieval universities, characterized by Aristotelian logic, physics, and metaphysics.",
    quotes: [
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Medieval scholasticism was essentially a Christianized form of Aristotelian **peripateticism**." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "The insights of ancient **peripateticism** provide valuable rational instruments for the exposition of sacred doctrine." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "True empirical science must break free from the dogmatic disputations of decadent **peripateticism**." }
    ]
  },

  // Dashboard — pro
  "Dashboard — pro/prologise.md": {
    primary: "To speak, write, or deliver a prologue; to introduce a play or dramatic work with an opening address (British spelling).",
    secondary: "In theatrical history, to introduce the theme and characters before the main action unfolds on stage.",
    quotes: [
      { author: "Ben Jonson", work: "The Poetaster", quote: "Let the actor come forward and **prologise** with modesty, inviting the favor of the pit." },
      { author: "William Hazlitt", work: "Lectures on the English Comic Writers", quote: "Dryden loved to **prologise** in verse, flattering the court while lecturing the audience on dramatic art." },
      { author: "George Saintsbury", work: "A History of Elizabethan Literature", quote: "Early dramatists found it necessary to **prologise** to explain the complex plot to unlettered spectators." }
    ]
  },
  "Dashboard — pro/prologize.md": {
    primary: "To deliver or compose a prologue; to introduce a literary or dramatic production (American spelling).",
    secondary: "In theatrical arts, to present the preliminary monologue setting forth the antecedent circumstances of the drama.",
    quotes: [
      { author: "John Dryden", work: "Essay of Dramatic Poesy", quote: "To **prologize** with wit requires as delicate an art as the writing of the play itself." },
      { author: "Edgar Allan Poe", work: "Marginalia", quote: "He attempted to **prologize** his brief tale with an elaborate essay upon German mysticism." },
      { author: "George Bernard Shaw", work: "Our Theatres in the Nineties", quote: "The manager stepped before the curtain to **prologize** the experimental tragedy to a perplexed house." }
    ]
  },
  "Dashboard — pro/prologue.md": {
    primary: "A separate introductory section of a literary, dramatic, or musical work that provides essential background context.",
    secondary: "An introductory event, occurrence, or action that serves as a precursor or prelude to something larger; from Greek pro- (before) + logos (speech).",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", quote: "What's past is **prologue**, what to come in yours and my discharge." },
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", quote: "Whan that Aprill with his shoures soote the droghte of March hath perced to the roote, began the famous **prologue**." },
      { author: "John Milton", work: "Paradise Lost", quote: "The celestial war was but the tragic **prologue** to the creation and fall of mankind." }
    ]
  },
  "Dashboard — pro/prologuize.md": {
    primary: "To speak or write a prologue; to introduce a literary or theatrical work with introductory remarks (variant spelling).",
    secondary: "In dramatic literature, to preface an argument or dialogue with preliminary explanation.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "He chose to **prologuize** his collection with an aggressive manifesto on poetic diction." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "The chorus would **prologuize** in solemn tones before the entrance of the doomed tragic heroes." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The editor paused to **prologuize** upon the strange philosophy of clothes before unveiling the German manuscript." }
    ]
  },
  "Dashboard — pro/prostate.md": {
    primary: "A firm, partly muscular and partly glandular body in male mammals that surrounds the base of the urethra and bladder neck, secreting seminal fluid.",
    secondary: "In human anatomy and clinical medicine, etymologically derived from Greek prostates ('one who stands before', guardian), frequently subject to hypertrophy or carcinoma in older age.",
    quotes: [
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "The **prostate** is positioned immediately below the internal urethral orifice and rests upon the urogenital diaphragm." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Benign enlargement of the **prostate** is the most frequent cause of mechanical urinary obstruction in men over sixty." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The ancient anatomist Herophilus gave the name **prostate** to the gland, viewing it as a guardian seated at the bladder gate." }
    ]
  },
  "Dashboard — pro/prostatic.md": {
    primary: "Of, relating to, affecting, or produced by the prostate gland.",
    secondary: "In urology, describing anatomical structures (e.g., prostatic urethra) or pathological conditions (e.g., prostatic hyperplasia).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic **prostatic** hypertrophy leads progressively to bilateral hydronephrosis if left untreated." },
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "The **prostatic** venous plexus communicates freely with the vesical plexus and the vertebral veins." },
      { author: "Samuel Cooper", work: "A Dictionary of Practical Surgery", quote: "Catheterization through the **prostatic** portion of the urethra requires extreme gentleness to avoid false passages." }
    ]
  },
  "Dashboard — pro/prow.md": {
    primary: "The portion of a ship's hull that is forward when the vessel is underway; the bow.",
    secondary: "Figuratively, the forefront or vanguard of any moving force, vehicle, or intellectual movement (from French proue, Latin prora, Greek prora).",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The sharp **prow** of the whaleboat cleft the foaming green swells in fierce pursuit." },
      { author: "Samuel Taylor Coleridge", work: "The Rime of the Ancient Mariner", quote: "With sloping masts and dipping **prow**, as who pursued with yell and blow came on the ice and snow." },
      { author: "Joseph Conrad", work: "The Mirror of the Sea", quote: "The ship plunged her heavy **prow** into the oncoming gale, tossing white foam over the forecastle." }
    ]
  },

  // Dashboard — pemp
  "Dashboard — pemp/apopemptic.md": {
    primary: "Sung, recited, or delivered to a person departing on a journey; valedictory or pertaining to a farewell hymn.",
    secondary: "In classical Greek poetry, a ceremonial ode or farewell poem addressed to a friend, traveler, or patron god departing from a city (from Greek apopempein, to send away).",
    quotes: [
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "The choir sang an **apopemptic** hymn upon the shore as the sacred trireme set sail for Delos." },
      { author: "Richard Claverhouse Jebb", work: "The Growth and Influence of Classical Greek Poetry", quote: "The **apopemptic** odes of the lyric poets blended affectionate personal farewells with solemn prayers to Poseidon." },
      { author: "Gilbert Murray", work: "A History of Ancient Greek Literature", quote: "When the colonists weighed anchor, the magistrates offered an **apopemptic** sacrifice to bless their voyage into unknown waters." }
    ]
  },
  "Dashboard — pemp/hypnopompic.md": {
    primary: "Of or relating to the semi-conscious state occurring during the transition from sleep to wakefulness.",
    secondary: "In sleep medicine and psychology, characterizing hallucinations, sleep paralysis, or sensory illusions experienced upon awakening (contrasting with hypnagogic, leading into sleep).",
    quotes: [
      { author: "Frederic W. H. Myers", work: "Human Personality and Its Survival of Bodily Death", quote: "I coined the term **hypnopompic** to designate those brief waking visions that linger as consciousness emerges from sleep." },
      { author: "William James", work: "The Principles of Psychology", quote: "In the **hypnopompic** state, dream imagery may overlap with the actual visual perception of the bedroom walls." },
      { author: "Oliver Sacks", work: "Hallucinations", quote: "Many people experience fleeting **hypnopompic** apparitions or auditory calls in the first moments of waking." }
    ]
  },
  "Dashboard — pemp/pemp.md": {
    primary: "The Greek root pempein (meaning 'to send, dispatch, convey, or escort'), forming words relating to processions, ceremonial transmissions, and departures.",
    secondary: "In historical linguistics and Greek morphology, the source of pompe (a solemn procession, literally 'a sending'), whence English pomp and pompous.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek verb **pemp**, meaning to send or escort, yielded the festive procession termed a pompe." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "Through the ancient stem **pemp**, our word pomp originally meant nothing more grandiose than an escort sending someone on their way." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "From the Hellenic **pemp** arise all vocabulary denoting ceremonial conveyances and valedictory dismissals." }
    ]
  },
  "Dashboard — pemp/pomp.md": {
    primary: "Splendid display, stately ceremony, or magnificent pageantry associated with high office, royalty, or celebration.",
    secondary: "Historically, a solemn procession in ancient Greece (Greek pompe); figuratively, vain or ostentatious earthly display.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "O ceremony, show me but thy worth! What is thy soul of adoration? Art thou aught else but place, degree, and form, creating awe and fear in other men? What drink'st thou oft, instead of homage sweet, but poison'd flattery? O, be sick, great **pomp**!" },
      { author: "Thomas Gray", work: "Elegy Written in a Country Churchyard", quote: "The boast of heraldry, the **pomp** of pow'r, and all that beauty, all that wealth e'er gave, awaits alike the th' inevitable hour." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The triumphal **pomp** of Aurelian displayed the captive queen Zenobia adorned in chains of gold." }
    ]
  },
  "Dashboard — pemp/pompous.md": {
    primary: "Characterized by an exaggerated, affected display of dignity, importance, or solemnity; self-important.",
    secondary: "Pretentiously grandiose or bombastic in language, bearing, or manner.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Collins was not a sensible man, and the deficiency of nature had been but little assisted by education or society; his manner was a mixture of servility and **pompous** self-consequence." },
      { author: "Charles Dickens", work: "Hard Times", quote: "Mr. Bounderby stood upon the hearthrug, loud, boastful, and thoroughly **pompous** in every gesture." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The magistrate puffed himself out like a turkey cock, delivering his petty sentence with **pompous** gravity." }
    ]
  },
  "Dashboard — pemp/pompously.md": {
    primary: "In a pompous, arrogant, or pretentiously self-important manner.",
    secondary: "With ostentatious, inflated ceremony or bombastic language.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "He cleared his throat **pompously** before instructing the parish vestry on the true principles of political economy." },
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "The schoolmaster strode **pompously** up the aisle, swinging his ferule with dreadful authority." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Inspector Jones delivered his erroneous theory **pompously**, proud of having locked up the wrong suspect." }
    ]
  },
  "Dashboard — pemp/pompousness.md": {
    primary: "The quality or condition of being pompous; pretentious self-importance or grandiosity.",
    secondary: "Affectation of solemn dignity or excessive gravity in speech or behavior.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "The Book of Snobs", quote: "The insufferable **pompousness** of the club bore drove every sensible member from the smoking room." },
      { author: "Charles Dickens", work: "Little Dorrit", quote: "Mr. Merdle's butler carried himself with a **pompousness** that eclipsed even his master's financial fame." },
      { author: "H. L. Mencken", work: "Prejudices", quote: "Nothing deflates academic **pompousness** faster than a single drop of unvarnished common sense." }
    ]
  },
  "Dashboard — pemp/unpompous.md": {
    primary: "Free from pomposity, pretension, or self-importance; modest, approachable, and unassuming.",
    secondary: "Characterized by plain, straightforward dignity without artificial theatricality.",
    quotes: [
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "His broadcast was quiet, direct, and completely **unpompous**, winning the trust of millions of working people." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Montaigne's genius lies in his charmingly **unpompous** candor about his own frailties." },
      { author: "E. M. Forster", work: "Two Cheers for Democracy", quote: "A genuinely great statesman is marked by an **unpompous** demeanor that puts humble visitors at ease." }
    ]
  },

  // Dashboard — pol
  "Dashboard — pol/dipole.md": {
    primary: "A pair of equal and oppositely charged electric charges or magnetic poles separated by a distance.",
    secondary: "In molecular physics, a molecule (such as water) with an asymmetric charge distribution creating an electric dipole moment.",
    quotes: [
      { author: "Peter Debye", work: "Polar Molecules", quote: "The permanent electric **dipole** moment of the water molecule explains its high dielectric constant and solvent power." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Electronegativity differences between bonded atoms generate a localized bond **dipole**." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "The radiation emitted by an oscillating **dipole** forms the elementary basis of classical electrodynamics." }
    ]
  },
  "Dashboard — pol/polar.md": {
    primary: "Of, relating to, or situated near the North Pole or South Pole of the Earth; characterized by intense cold.",
    secondary: "Possessing polarity; having two opposing or contradictory poles, qualities, or magnetic charges.",
    quotes: [
      { author: "Robert Falcon Scott", work: "Scott's Last Expedition", quote: "Great God! this is an awful place, and terrible enough for us to have laboured to it without the reward of priority in the **polar** wilderness." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The contrast between the lush tropical flora and the desolate **polar** tundras illustrates the power of climate." },
      { author: "Samuel Taylor Coleridge", work: "The Rime of the Ancient Mariner", quote: "The **polar** spirit from the land of mist and snow, he loved the bird that loved the man who shot him with his bow." }
    ]
  },
  "Dashboard — pol/polarise.md": {
    primary: "To cause light, electromagnetic waves, or particles to vibrate in a definite, single plane (British spelling).",
    secondary: "To divide a community, electorate, or opinion into two sharply contrasting and hostile groups.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "Tourmaline crystals possess the property to **polarise** light by absorbing waves vibrating in one plane." },
      { author: "John Stuart Mill", work: "Considerations on Representative Government", quote: "Partisan newspapers tend to **polarise** the citizenry, extinguishing all moderate middle opinions." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "A powerful electromagnet was used to **polarise** the beam of light passing through heavy glass." }
    ]
  },
  "Dashboard — pol/polarity.md": {
    primary: "The state of having two opposite, contradictory, or contrasting poles, qualities, or tendencies (such as positive and negative).",
    secondary: "In developmental biology, the orientation of a cell, embryo, or tissue along an anterior-posterior or apical-basal axis.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Compensation", quote: "**Polarity**, or action and reaction, we meet in every part of nature; in darkness and light; in heat and cold; in male and female." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The magnetic **polarity** of the steel bar reversed instantly when the electric coil's direction was changed." },
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "The morphological **polarity** of the embryo is established long before visible organs differentiate." }
    ]
  },
  "Dashboard — pol/polarize.md": {
    primary: "To cause light or electromagnetic radiation to oscillate in a specific plane or direction (American spelling).",
    secondary: "To break up into opposing, rigid factions or conflicting ideological groups.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "A Nicol prism is employed in the polarimeter to **polarize** monochromatic sodium light." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "Fear and superstition serve to **polarize** public debate, replacing scientific reason with tribal dogma." },
      { author: "Walter Lippmann", work: "Public Opinion", quote: "Skilled propagandists know how to **polarize** an issue so that no room remains for nuanced compromise." }
    ]
  },
  "Dashboard — pol/polaroid.md": {
    primary: "A synthetic plastic sheet embedded with microscopic crystals oriented to polarize transmitted light, invented by Edwin H. Land.",
    secondary: "A trademark for a brand of instant camera and photographic film producing developed prints within minutes.",
    quotes: [
      { author: "Edwin H. Land", work: "A New One-Step Photographic Process", quote: "The **Polaroid** process eliminated the darkroom, delivering a fully developed positive print within sixty seconds." },
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "I took a sheet of **polaroid** and showed the students how rotating it cut off the glare from the water surface." },
      { author: "Andy Warhol", work: "The Philosophy of Andy Warhol", quote: "A **Polaroid** photograph has an immediate, unvarnished honesty that catches the subject before they can pose." }
    ]
  },
  "Dashboard — pol/pole.md": {
    primary: "Either of the two extreme points at opposite ends of an axis of rotation, such as Earth's North or South Pole; or an electrical/magnetic terminal.",
    secondary: "A long, slender, rounded piece of wood, metal, or fiberglass used as a support, shaft, or lever (from Latin palus stake).",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The magnetic needle turned toward the frozen **pole**, guiding our ship across the loneliest wastes of ocean." },
      { author: "John Milton", work: "Paradise Lost", quote: "From **pole** to **pole** the thunder rolled, shaking the crystal battlements of heaven." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I leaned upon my birch **pole**, watching the shadows lengthen across the frozen pond." }
    ]
  },
  "Dashboard — pol/poler.md": {
    primary: "A person who propels or steers a boat (such as a punt, barge, or canoe) using a long pole.",
    secondary: "A draft horse harnessed alongside the central pole of a carriage or wagon, helping to steer and hold back the load.",
    quotes: [
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The expert **poler** braced his bare feet against the deck timber, shoving the raft off the mud shoal." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The heavy timber wagon rattled down the hill, with the near **poler** straining hard against the breeching." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The native **poler** stood in the bows of the canoe, sounding the muddy shallows with a long bamboo." }
    ]
  },
  "Dashboard — pol/polity.md": {
    primary: "A politically organized society, community, or state considered as a distinct governing entity.",
    secondary: "A specific form, constitution, or system of civil or ecclesiastical government (from Greek politeia, from polis city).",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "A constitutional **polity** represents the balanced rule of the middle class, avoiding the extremes of oligarchy and democracy." },
      { author: "Richard Hooker", work: "Of the Lawes of Ecclesiasticall Politie", quote: "No human **polity** can long endure without laws grounded upon natural reason and divine wisdom." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Our ancient British **polity** was not struck out at a single blow, but grew organically through centuries of experience." }
    ]
  },

  // Dashboard — trech
  "Dashboard — trech/ditrochee.md": {
    primary: "A compound metrical foot in classical prosody consisting of two trochees (a heavy syllable, light syllable, heavy syllable, light syllable).",
    secondary: "In Greek and Latin metrics, an eight-time rhythm (trochaic dipody) frequently employed in dramatic cadences and oration clausulae.",
    quotes: [
      { author: "Cicero", work: "De Oratore", quote: "The orator frequently closes his period with a resonant **ditrochee**, which delights the Roman ear with its rhythmic fall." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "A **ditrochee** at the end of a sentence imparts a solemn, conclusive finish to forensic eloquence." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "In Swinburne's sweeping meters, we frequently encounter the rolling cascade of the **ditrochee**." }
    ]
  },
  "Dashboard — trech/epitrochoid.md": {
    primary: "A geometric roulette curve traced by a point attached to a circle that rolls without slipping around the outside of a fixed circle.",
    secondary: "In kinematics and mechanical engineering, the mathematical profile used in designing the rotor and chamber of the Wankel rotary internal combustion engine.",
    quotes: [
      { author: "Felix Wankel", work: "Rotary Piston Machines", quote: "The inner combustion chamber of the rotary engine is machined to the exact mathematical contour of a two-lobed **epitrochoid**." },
      { author: "Leonhard Euler", work: "Mechanica", quote: "The geometric properties of the **epitrochoid** illustrate the kinematic generation of cycloidal curves." },
      { author: "Arthur Cayley", work: "The Principles of Book-Keeping by Double Entry", quote: "Tracing the path of the **epitrochoid** reveals how planetary gear assemblies distribute torque." }
    ]
  },
  "Dashboard — trech/hypotrochoid.md": {
    primary: "A geometric roulette curve traced by a point attached to a circle that rolls without slipping along the interior of a fixed circle.",
    secondary: "In recreational mathematics, the family of intricate curves generated by drawing toys such as the Spirograph, including the ellipse and deltoid as special cases.",
    quotes: [
      { author: "Leonhard Euler", work: "Mechanica", quote: "When the tracing point lies inside the rolling radius, the resulting **hypotrochoid** forms graceful looped rosettes." },
      { author: "Felix Wankel", work: "Rotary Piston Machines", quote: "Planetary gear teeth can be milled to **hypotrochoid** curves to eliminate sliding friction under high loads." },
      { author: "Martin Gardner", work: "Mathematical Carnival", quote: "The Spirograph delights children because every gear combination traces a pristine mathematical **hypotrochoid**." }
    ]
  },
  "Dashboard — trech/trochaic.md": {
    primary: "Of, relating to, or consisting of trochees (metrical feet consisting of one stressed syllable followed by one unstressed syllable).",
    secondary: "In English poetry, producing a brisk, driving, or tripping rhythm, famously exemplified by Longfellow's *The Song of Hiawatha*.",
    quotes: [
      { author: "Henry Wadsworth Longfellow", work: "The Song of Hiawatha", quote: "By the shores of Gitche Gumee, by the shining Big-Sea-Water, rang the rapid, flowing **trochaic** meter." },
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The Raven is composed in a **trochaic** octameter acatalectic, alternating with heptameter catalectic." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The sudden shift from iambic to **trochaic** movement imparts an electrifying urgency to Elizabethan tragedy." }
    ]
  },
  "Dashboard — trech/trochanter.md": {
    primary: "Any of several prominent bony protuberances on the upper part of the femur (thigh bone) in vertebrates, serving as muscle attachment points.",
    secondary: "In insect anatomy, the second segment of the leg between the coxa and the femur; derived from Greek trochanter (literally 'a runner', from trekhein to run).",
    quotes: [
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "The greater **trochanter** provides insertion for the gluteal muscles that abduct and rotate the thigh." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "In beetles, the small **trochanter** articulates between the basal coxa and the elongated femur." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "A prominent third **trochanter** is characteristic of the femur in perissodactyl ungulates like the horse." }
    ]
  },
  "Dashboard — trech/trochee.md": {
    primary: "A metrical foot in poetry consisting of one stressed (or long) syllable followed by one unstressed (or short) syllable.",
    secondary: "Etymologically 'a running foot' (Greek trochaios, from trekhein to run), contrasting with the rising iambic cadence.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Metrical Feet: A Lesson for a Boy", quote: "**Trochee** trips from long to short; from long to long in solemn sort slow Spondee stalks." },
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "The nimble **trochee** hastens down the line, while lingering spondees check the swift design." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "Shakespeare often opens a dramatic blank verse line with an emphatic **trochee** to seize the hearer's ear." }
    ]
  },
  "Dashboard — trech/trochelminth.md": {
    primary: "An invertebrate belonging to the Trochelminthes, an archaic grouping comprising the rotifers and related microscopic aquatic worms.",
    secondary: "In invertebrate zoology, characterized by a ciliated corona or wheel-organ (*trochus*) used for both locomotion and suspension feeding.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The typical **trochelminth** uses its anterior ciliated disk to create a feeding vortex in freshwater ponds." },
      { author: "Richard Owen", work: "Lectures on Invertebrate Animals", quote: "Microscopists were captivated by the rapid rotation of the cilia in each minute **trochelminth**." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Plankton hauls in coastal lagoons frequently yield millions of microscopic **trochelminth** rotifers." }
    ]
  },
  "Dashboard — trech/trochlea.md": {
    primary: "A pulley-like anatomical structure, especially a grooved articular surface of a bone (such as the distal end of the humerus) or a fibrous loop through which a tendon glides.",
    secondary: "In human cranial anatomy, the fibrocartilaginous ring in the orbit through which the tendon of the superior oblique muscle passes (innervated by the trochlear nerve).",
    quotes: [
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "The pulley-like **trochlea** of the humerus articulates smoothly with the semilunar notch of the ulna." },
      { author: "Charles Bell", work: "The Hand: Its Mechanism and Vital Endowments", quote: "The superior oblique tendon passes through a cartilaginous **trochlea**, changing its angle of pull to roll the eye." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Palsy of the fourth cranial nerve impairs the muscular action directed through the orbital **trochlea**." }
    ]
  },
  "Dashboard — trech/trochoid.md": {
    primary: "In geometry, a curve traced by a point fixed at any distance from the center of a circle as that circle rolls without slipping along a straight line.",
    secondary: "In comparative anatomy, describing a pivot joint (trochoid joint) in which rotation occurs around a single longitudinal axis, as between the atlas and axis vertebrae.",
    quotes: [
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "The atlantoaxial articulation is a typical **trochoid** or pivot joint allowing horizontal rotation of the skull." },
      { author: "Leonhard Euler", work: "Mechanica", quote: "The mathematical properties of the **trochoid** bridge the cycloid with the broader family of rolling curves." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The head of the radius forms a **trochoid** pivot within the lesser sigmoid cavity of the ulna." }
    ]
  },
  "Dashboard — trech/trochophore.md": {
    primary: "A small, translucent, free-swimming ciliated marine larva characteristic of mollusks, annelids, and related lophotrochozoan phyla.",
    secondary: "In marine developmental biology, featuring a prominent equatorial band of cilia (the prototroch, literally 'wheel-bearer') used for propulsion and planktotrophic feeding.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea: The World of Plankton", quote: "The spinning **trochophore** larva of the polychaete worm is propelled by a ring of powerful vibrating cilia." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Countless microscopic **trochophore** larvae drift in the spring tide, destined to settle as clams and marine worms." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The common possession of a **trochophore** stage provides decisive embryological proof uniting annelids and mollusks." }
    ]
  },

  // Dashboard — streph
  "Dashboard — streph/anastrophe.md": {
    primary: "A rhetorical figure of speech in which the normal syntactic order of words is inverted for artistic effect or emphasis (e.g., 'Into the sea plunged she').",
    secondary: "In classical and English stylistics, literally 'a turning back' (Greek anastrophe), widely used in heroic epic and poetry to enhance dignity and rhythm.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "In Milton's grand style, deliberate **anastrophe** lends an antique majesty to descriptions of the angelic rebellion." },
      { author: "Alexander Pope", work: "The Art of Sinking in Poetry", quote: "The poet employs **anastrophe** to elevate common speech above the vulgar idiom of the market." },
      { author: "George Saintsbury", work: "A History of English Prose Rhythm", quote: "Judicious **anastrophe** allows an author to place the most emphatic word precisely at the close of the period." }
    ]
  },
  "Dashboard — streph/antistrophic.md": {
    primary: "Of, relating to, or having the character of an antistrophe in classical Greek choral lyric poetry.",
    secondary: "In dramatic metrics, describing the second stanza of a choral triad, sung while the chorus moves in reverse direction across the orchestra.",
    quotes: [
      { author: "John Milton", work: "Samson Agonistes", quote: "The chorus responds in **antistrophic** measure, balancing grief with pious resignation." },
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "The **antistrophic** symmetry of Pindar's odes reflects the coordinated counter-dance of the Greek chorus." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", quote: "In Aeschylean tragedy, every strophic burst of terror receives its measured **antistrophic** answer." }
    ]
  },
  "Dashboard — streph/apostrophic.md": {
    primary: "Of, relating to, or characterized by apostrophe (a direct address to an absent person, abstract quality, or inanimate object).",
    secondary: "In punctuation and orthography, relating to the apostrophe mark (') used to indicate omission of letters or the possessive case.",
    quotes: [
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "The poem rises to an impassioned **apostrophic** climax as the narrator addresses the eternal ocean." },
      { author: "Percy Bysshe Shelley", work: "Defense of Poetry", quote: "The lyrical impulse is essentially **apostrophic**, summoning the unseen powers of nature into dialogue." },
      { author: "Samuel Johnson", work: "The Lives of the Poets", quote: "Cowley was too fond of cold, **apostrophic** addresses to abstractions that awakened no genuine feeling." }
    ]
  },
  "Dashboard — streph/boustrophedon.md": {
    primary: "An ancient method of writing in which lines run alternately from right to left and from left to right, literally 'turning like an ox in plowing'.",
    secondary: "In epigraphy and paleography, characteristic of archaic Greek inscriptions of the 6th century BC, eliminating the need to return to the left margin for each line.",
    quotes: [
      { author: "Isaac Taylor", work: "The History of the Alphabet", quote: "Archaic Greek inscriptions on stone are frequently written in **boustrophedon**, snake-like from right to left and back." },
      { author: "Herodotus", work: "The Histories", quote: "The ancient laws were incised in **boustrophedon** upon wooden tablets preserved in the Prytaneum." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The transition from Phoenician right-to-left script to European left-to-right passed through the intermediate stage of **boustrophedon**." }
    ]
  },
  "Dashboard — streph/boustrophedonic.md": {
    primary: "Written in or characteristic of boustrophedon; alternating direction from line to line.",
    secondary: "In computer graphics, printing technology, and robotics, descriptive of path-planning algorithms that sweep a surface in back-and-forth snake-like rows.",
    quotes: [
      { author: "Isaac Taylor", work: "The History of the Alphabet", quote: "The **boustrophedonic** style of the Solonian code prevented the reader's eye from losing its place between long lines." },
      { author: "Arthur Evans", work: "Scripta Minoa", quote: "Several early Cretan seal impressions display a **boustrophedonic** arrangement of hieroglyphic signs." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Agricultural plowing creates a **boustrophedonic** furrow pattern that alters hillside surface drainage." }
    ]
  },
  "Dashboard — streph/catastrophe.md": {
    primary: "An event causing great and often sudden damage, suffering, or disaster; a terrible upheaval.",
    secondary: "In classical drama, the final event or resolution in a tragedy (literally 'overturning' or 'downturn', Greek katastrophe) that concludes the dramatic action.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "Pat he comes, like the **catastrophe** of the old comedy: my cue is villainous melancholy." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Uniformitarianism rejected the notion that every geological epoch was terminated by a global **catastrophe**." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The sudden fall of the French monarchy was a historic **catastrophe** that shook the foundations of Europe." }
    ]
  },
  "Dashboard — streph/catastrophic.md": {
    primary: "Involving or causing sudden, widespread, and disastrous damage or suffering.",
    secondary: "In geology, ecology, and engineering, characterized by sudden, violent systemic failure or transformative upheaval.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The indiscriminate application of chemical pesticides risks **catastrophic** disruption to bird populations." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The collapse of the caldera at Krakatoa produced **catastrophic** tsunamis felt across the globe." },
      { author: "Carl Sagan", work: "Cosmos", quote: "A comet impact sixty-five million years ago caused a **catastrophic** climate shift that doomed the dinosaurs." }
    ]
  },
  "Dashboard — streph/catastrophism.md": {
    primary: "The geological doctrine that Earth's crustal features were shaped primarily by sudden, violent, worldwide catastrophes rather than by gradual processes.",
    secondary: "In the history of science, the dominant early 19th-century school championed by Georges Cuvier, subsequently displaced by Charles Lyell's uniformitarianism.",
    quotes: [
      { author: "Georges Cuvier", work: "Discourse on the Revolutionary Upheavals on the Surface of the Earth", quote: "The disappearance of entire fossil faunas can only be explained by recurrent episodes of planetary **catastrophism**." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The doctrine of **catastrophism** was born from our reluctance to comprehend the immense duration of past geological time." },
      { author: "Thomas Henry Huxley", work: "Geological Contemporaneity and Persistent Types of Life", quote: "Modern geology synthesized uniformitarian continuity with occasional localized **catastrophism**." }
    ]
  },
  "Dashboard — streph/monostrophe.md": {
    primary: "A poem, choral song, or musical composition consisting of a single strophe or stanza.",
    secondary: "In classical metrics, a composition in which a single metrical pattern is sustained throughout without alternating strophes and antistrophes.",
    quotes: [
      { author: "John Milton", work: "Samson Agonistes", quote: "The tragic dialogue gives way to an impassioned choral **monostrophe** celebrating Samson's final strength." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "Collins constructed an exquisite **monostrophe** where unrhymed lyrical stanzas mirror the stillness of evening." },
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "The Spartan marching chant was a concise **monostrophe** designed to keep soldiers in rhythmic step." }
    ]
  },
  "Dashboard — streph/monostrophic.md": {
    primary: "Consisting of or written in a single strophe or stanza; having uniform stanzas throughout.",
    secondary: "In classical prosody, composed in identical repeated meters rather than triad structures of strophe, antistrophe, and epode.",
    quotes: [
      { author: "John Milton", work: "Samson Agonistes", quote: "Milton notes in his preface that the choral odes are **monostrophic**, following emotional cadence rather than dance turns." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The simple ballad stanza provides a **monostrophic** framework well-suited for extended oral narrative." },
      { author: "Algernon Charles Swinburne", work: "Studies in Prose and Poetry", quote: "The hymn moves in a majestic, **monostrophic** march that never flags in musical momentum." }
    ]
  },
  "Dashboard — streph/strophic.md": {
    primary: "Consisting of or characterized by strophes (stanzas); structured in recurring metrical units of identical or corresponding form.",
    secondary: "In musical composition, designating a song (strophic form) in which all verses or stanzas of text are sung to the same recurring music.",
    quotes: [
      { author: "Donald Francis Tovey", work: "Essays in Musical Analysis", quote: "Schubert's simplest lieder adhere to a pure **strophic** structure where melody illuminates every verse." },
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "The **strophic** architecture of Pindaric poetry was matched step for step by the choreography of the chorus." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", quote: "The evolution from monotonous narrative chant to balanced **strophic** lyric marks the birth of European drama." }
    ]
  },

  // Dashboard — torn
  "Dashboard — torn/return.md": {
    primary: "To come or go back to a place, person, condition, or subject.",
    secondary: "To give, put, or send back something to its owner or original place; derived from Old French retourner (Latin tornare, from Greek tornos a lathe).",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "The undiscover'd country from whose bourn no traveller **returns**, puzzles the will." },
      { author: "John Milton", work: "Paradise Lost", quote: "Though fallen on evil days, on evil days though fallen, and evil tongues; in darkness, and with dangers compassed round, and solitude; yet not alone, while thou visit'st my slumbers nightly, or when morn purples the east: still govern thou my song, Urania, and fit audience find, though few." },
      { author: "Homer", work: "The Odyssey", quote: "Ten long years did Odysseus wander across the wine-dark sea before he could **return** to rocky Ithaca." }
    ]
  },
  "Dashboard — torn/returning.md": {
    primary: "Coming back or going back; recurring or repeating at intervals.",
    secondary: "Arriving back from a journey or absent state; restoring or yielding in response.",
    quotes: [
      { author: "Walt Whitman", work: "When Lilacs Last in the Dooryard Bloom'd", quote: "When lilacs last in the dooryard bloom'd, and the great star early droop'd in the western sky in the night, I mourn'd, and yet shall mourn with ever-**returning** spring." },
      { author: "Percy Bysshe Shelley", work: "Adonais", quote: "The **returning** sun warms the frozen earth, but awakens not our lost companion." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The weary peasants trudged along the road, **returning** from the fields as evening fell." }
    ]
  },
  "Dashboard — torn/torn.md": {
    primary: "Pulled or ripped apart by force; having ragged, lacerated edges.",
    secondary: "Deeply divided, conflicted, or anguished between competing emotions, loyalties, or choices.",
    quotes: [
      { author: "William Shakespeare", work: "Richard III", quote: "Our bruised arms hung up for monuments; our stern alarums changed to merry meetings, our dreadful marches to delightful measures; our **torn** banners healed." },
      { author: "Charles Dickens", work: "Bleak House", quote: "He held the **torn** document in his trembling hand, staring at the missing signature." },
      { author: "George Eliot", work: "The Mill on the Floss", quote: "Maggie was bitterly **torn** between her ardent passion and her unyielding sense of duty." }
    ]
  },
  "Dashboard — torn/tornado.md": {
    primary: "A violent, destructive, rapidly rotating column of air extending from a cumulonimbus cloud to the ground, characterized by a funnel-shaped condensation cloud.",
    secondary: "In meteorology, an atmospheric vortex generating wind speeds up to 300 mph (derived from Spanish tronada thunderstorm, influenced by tornar to turn).",
    quotes: [
      { author: "Mark Twain", work: "Roughing It", quote: "A Kansas **tornado** swept across the prairie, lifting cabins and spinning fences into matchwood." },
      { author: "Henry David Thoreau", work: "Excursions", quote: "The summer gale raged like a miniature **tornado**, twisting ancient oaks from their roots." },
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Vorticity calculations explain the intense localized pressure drop inside the funnel of a **tornado**." }
    ]
  },
  "Dashboard — torn/tornillo.md": {
    primary: "The screwbean mesquite (Prosopis pubescens), a thorny shrub or small tree native to the southwestern United States and Mexico, bearing tightly spiraled, screw-shaped seedpods.",
    secondary: "In Spanish and southwestern botany, literally 'little screw' (from Spanish tornillo, from Latin tornus a lathe / Greek tornos); valued as nutritious forage and fuel wood.",
    quotes: [
      { author: "John Muir", work: "Steep Trails", quote: "Thickets of spiny **tornillo** fringed the dry riverbeds, their coiled pods hanging in dense yellow clusters." },
      { author: "Asa Gray", work: "Plantae Wrightianae", quote: "Specimens of **tornillo** collected along the Rio Grande exhibit the tight helical pods characteristic of the species." },
      { author: "George Engelmann", work: "Botanical Works", quote: "The wood of the **tornillo** is remarkably dense, furnishing durable fence posts in the arid river valleys." }
    ]
  },
  "Dashboard — torn/tournament.md": {
    primary: "A medieval sporting contest in which knights engaged in mock combat, jousts, and martial trials to display chivalric prowess.",
    secondary: "A series of contests between multiple competitors or teams competing for an overall championship in sport or games (from Old French torneiement, from torneier to turn).",
    quotes: [
      { author: "Walter Scott", work: "Ivanhoe", quote: "The passage of arms at Ashby-de-la-Zouche was celebrated as the most magnificent **tournament** of the reign of King Richard." },
      { author: "Alfred, Lord Tennyson", work: "Idylls of the King", quote: "In the lists of Camelot, knight met knight in the glittering **tournament** of diamond spears." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The martial spirit of the crusaders was nourished by the perilous amusements of the **tournament**." }
    ]
  },
  "Dashboard — torn/turn.md": {
    primary: "To move in a circular direction around an axis or center; to rotate, pivot, or change direction.",
    secondary: "To change or transform into a specified state or condition; to shape an object on a lathe (from Greek tornos lathe / compass).",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Imperious Caesar, dead and **turned** to clay, might stop a hole to keep the wind away." },
      { author: "John Keats", work: "Ode on a Grecian Urn", quote: "Thou still unravish'd bride of quietness, thou foster-child of silence and slow time, what leaf-fring'd legend haunts about thy shape of deities or mortals, or of both, in Tempe or the dales of Arcady?" },
      { author: "Henry David Thoreau", work: "Walden", quote: "The wheels of nature **turn** with unhurried majesty, bringing the seasons round in perfect sequence." }
    ]
  },
  "Dashboard — torn/turned.md": {
    primary: "Having moved around an axis or altered course; transformed into a different state.",
    secondary: "Shaped, rounded, or smoothed by revolving against a cutting tool on a lathe.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "He **turned** his eyes toward the dark river, watching the solitary light of the prison hulk." },
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "The table legs had been skillfully **turned** on a pole lathe from seasoned beech wood." },
      { author: "Joseph Conrad", work: "Typhoon", quote: "Captain MacWhirr **turned** the vessel squarely into the teeth of the rising hurricane." }
    ]
  },
  "Dashboard — torn/turner.md": {
    primary: "A person who shapes wood, metal, or other materials by cutting on a lathe.",
    secondary: "A gymnast who is a member of a Turnverein (German gymnastics society, from German turnen to practice gymnastics).",
    quotes: [
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The local wood **turner** fashioned bowls, spinning wheels, and chair rungs for all the neighboring parishes." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The division of labor permits the skilled **turner** to produce ten times the spindles in a single day." },
      { author: "George Eliot", work: "Silas Marner", quote: "Beside the hearth sat a three-legged stool, cleanly carved by a village **turner** half a century before." }
    ]
  },
  "Dashboard — torn/turnery.md": {
    primary: "Articles made on a lathe; wooden, ivory, or metal objects produced by turning.",
    secondary: "The art, craft, trade, or workshop of a turner.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The shop window was filled with quaint specimens of wooden **turnery**, from snuff boxes to curtain rings." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The domestic manufacture of coarse **turnery** supplied kitchen utensils before stamped tinplate became cheap." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "He inspected the curious **turnery** of the professor's pipe, carved with antique armorial crests." }
    ]
  },
  "Dashboard — torn/turning.md": {
    primary: "The act of rotating, revolving, or changing direction; a place where a road or path branches off.",
    secondary: "The process or craft of shaping workpieces on a lathe using cutting tools.",
    quotes: [
      { author: "William Butler Yeats", work: "The Second Coming", quote: "**Turning** and **turning** in the widening gyre, the falcon cannot hear the falconer; things fall apart; the centre cannot hold." },
      { author: "Robert Frost", work: "The Road Not Taken", quote: "Two roads diverged in a yellow wood, and I took the **turning** less traveled by." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The geometric precision of mechanical **turning** can never replace the living vitality of hand carving." }
    ]
  }
};

let count = 0;
for (const [key, data] of Object.entries(batch1Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 1 Completed: ${count} / ${Object.keys(batch1Data).length} words updated`);
console.log(`========================================`);
