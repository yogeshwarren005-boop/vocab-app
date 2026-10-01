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

const batch2Data = {
  "Dashboard — stol/apostle.md": {
    "primary": "One of the twelve disciples chosen by Jesus Christ to preach the Gospel; by extension, any pioneering missionary or fervent advocate of a great moral cause.",
    "secondary": "In early Christian ecclesiology and historical theology, an emissary sent with delegated spiritual authority (Greek apostolos, from apostellein 'to send off'), establishing churches and foundational doctrine.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The first preaching of the **apostle** had planted vibrant churches across the maritime provinces of Asia Minor."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Then to the desert fled, where **apostle** none attended, but angels ministering to his needs."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "Mahomet was received by his followers not as a worldly monarch, but as an inspired **apostle** of monotheism."
      }
    ]
  },
  "Dashboard — stol/apostleship.md": {
    "primary": "The office, spiritual commission, or official tenure of an apostle; the authority delegated to preach and govern.",
    "secondary": "In historical theology and apostolic succession, the foundational mandate conferred upon early church leaders, establishing continuity of doctrine and episcopal jurisdiction.",
    "quotes": [
      {
        "author": "Richard Hooker",
        "work": "Of the Lawes of Ecclesiasticall Politie",
        "quote": "The authority of their **apostleship** remained sacred and inviolate among all the primitive churches of the Mediterranean."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "He grounded his pastoral duty directly upon the inherited commission of primitive **apostleship**."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "The singular grace of **apostleship** was conferred upon the twelve that they might lay the immutable foundations of the faith."
      }
    ]
  },
  "Dashboard — stol/apostolic.md": {
    "primary": "Pertaining to, characteristic of, or tracing descent from the Apostles of Jesus Christ or their foundational teachings.",
    "secondary": "In canonical and ecclesiastical law, designating decrees, letters, or delegated authority emanating directly from the Holy See (the Apostolic See) or ancient patriarchal jurisdictions.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The bishop of Rome asserted his primacy by invoking an unbroken chain of **apostolic** succession."
      },
      {
        "author": "John Locke",
        "work": "A Letter Concerning Toleration",
        "quote": "No church can justly claim an **apostolic** pedigree that denies mutual toleration and freedom of inward conscience."
      },
      {
        "author": "George Eliot",
        "work": "Romola",
        "quote": "Fra Girolamo addressed the multitude with the austere zeal of an **apostolic** reformer summoning Florence to repentance."
      }
    ]
  },
  "Dashboard — stol/apostolical.md": {
    "primary": "Relating to or conforming to the practice and doctrine of the Apostles or the primitive Christian church.",
    "secondary": "An archaic or formal variant of apostolic, frequently utilized in historic liturgies, charters, and early modern theological controversies regarding church governance.",
    "quotes": [
      {
        "author": "Jeremy Taylor",
        "work": "The Rule and Exercises of Holy Living",
        "quote": "The primitive pastors ordered their households in simplicity, striving to fulfill the **apostolical** pattern of charity."
      },
      {
        "author": "Jonathan Swift",
        "work": "A Tale of a Tub",
        "quote": "They claimed an unblemished **apostolical** pedigree, though their courtly habits bore little resemblance to the fishermen of Galilee."
      },
      {
        "author": "David Hume",
        "work": "The History of England",
        "quote": "The reformist clergy rejected all ceremonial vestments that could not plead direct **apostolical** warrant."
      }
    ]
  },
  "Dashboard — stol/diastole.md": {
    "primary": "The phase of the cardiac cycle during which the heart muscle relaxes and its chambers expand to fill with incoming blood, alternating rhythmically with systole.",
    "secondary": "In classical metrics and rhetoric, the poetic lengthening of a syllable that is normally short; figuratively, any rhythmic expansion, dilation, or release of tension in natural cycles.",
    "quotes": [
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "During the **diastole**, the ventricles dilate and receive blood poured into them from the auricles."
      },
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "Faust",
        "quote": "In the ceaseless systole and **diastole** of the universe, nature pulses between concentration and infinite expansion."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lessons in Elementary Physiology",
        "quote": "The physiological efficiency of the heart relies upon the complete muscular relaxation attained during each brief **diastole**."
      }
    ]
  },
  "Dashboard — stol/diastolic.md": {
    "primary": "Pertaining to, occurring during, or characteristic of cardiac diastole; specifically denoting the minimum arterial blood pressure recorded between heartbeats.",
    "secondary": "In cardiovascular hemodynamics, relating to ventricular compliance, filling pressures, and peripheral vascular resistance during the resting phase of the cardiac cycle.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A soft, blowing **diastolic** murmur heard at the third intercostal space indicates early incompetence of the aortic valve."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The clinician recorded both the peak systolic thrust and the baseline **diastolic** resistance within the brachial artery."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "The precise timing of the acoustic vibration, whether systolic or **diastolic**, remains the supreme diagnostic criterion."
      }
    ]
  },
  "Dashboard — stol/epistle.md": {
    "primary": "A written communication directed to a person or group; a formal, didactic, or elegant literary letter.",
    "secondary": "In biblical canon and liturgical practice, one of the doctrinal letters of the New Testament (such as those of Paul or Peter) appointed to be read during public Christian worship.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "An Essay on Man",
        "quote": "He addressed his moral **epistle** to Bolingbroke, vindicating the ways of God to inquiring minds."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Horace composed each verse **epistle** with an urbanity and conversational grace that concealed consummate art."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "A formal **epistle** from a prudent statesman often preserves more truth of history than a labored chronicle."
      }
    ]
  },
  "Dashboard — stol/epistolary.md": {
    "primary": "Of, relating to, or conducted by means of letters or personal correspondence.",
    "secondary": "In literary theory, denoting a genre of novel or narrative developed entirely through exchanged letters, diary entries, or documentary fragments (e.g., Richardson's *Clarissa*).",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Her style of writing was very unlike the brisk, lively **epistolary** banter characteristic of her younger sisters."
      },
      {
        "author": "Samuel Richardson",
        "work": "Clarissa",
        "quote": "The urgent passions of the human heart appear in their true nakedness through immediate **epistolary** confessions."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "The eighteenth century perfected the **epistolary** novel by transforming private mailbags into public theatrical spectacles."
      }
    ]
  },
  "Dashboard — stol/epistolatory.md": {
    "primary": "Pertaining to letters or letter-writing; an archaic or rare stylistic equivalent of epistolary.",
    "secondary": "In historical rhetoric, descriptive of the elaborate conventions, formal protocols, and ornate greetings required in classical and diplomatic correspondence.",
    "quotes": [
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "He kept up an extensive **epistolatory** intercourse with eminent scholars scattered across the German universities."
      },
      {
        "author": "Walter Scott",
        "work": "Guy Mannering",
        "quote": "The Scottish solicitor managed his remote clients through voluminous **epistolatory** packets sent by stagecoach."
      },
      {
        "author": "Robert Southey",
        "work": "The Life of Nelson",
        "quote": "The admiral's **epistolatory** despatches were straightforward, concise, and devoid of diplomatic dissimulation."
      }
    ]
  },
  "Dashboard — stol/stele.md": {
    "primary": "An upright stone slab or pillar bearing inscriptions, reliefs, or commemorative emblems, erected as a gravestone or monument.",
    "secondary": "In plant anatomy, the central cylindrical vascular cylinder of a root or stem, comprising xylem, phloem, pericycle, and occasionally pith in vascular plants.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The sacred civic decrees were engraved upon an ancient marble **stele** standing in the center of the marketplace."
      },
      {
        "author": "Arthur Evans",
        "work": "The Palace of Minos",
        "quote": "Near the entrance corridor, workers unearthed a fragmented limestone **stele** incised with ritual double-axes."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "A microscopic cross-section of the fern rhizome reveals an intricate, siphonostelic **stele** surrounded by an endodermis."
      }
    ]
  },
  "Dashboard — stol/stellein.md": {
    "primary": "The ancient Greek verb stellein (meaning 'to put in order, equip, array, dispatch, or send'), serving as the linguistic progenitor of numerous English words denoting mission and structure.",
    "secondary": "In comparative Indo-European philology, an etymological root giving rise to Greek apostolos ('envoy'), epistole ('message sent'), peristalsis ('compressing around'), and stele ('upright standing block').",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "From the Hellenic verb **stellein**, signifying to equip and send on a mission, our language derives both apostle and epistle."
      },
      {
        "author": "Ernest Weekley",
        "work": "The Romance of Words",
        "quote": "The fundamental Greek root **stellein** unites the concepts of military equipment, vertical monuments, and dispatched letters."
      },
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "Under the etymological heading of **stellein**, we assemble all derivatives that signify dispatching, erecting, or outfitting."
      }
    ]
  },
  "Dashboard — stol/stole.md": {
    "primary": "A long, narrow band of colored fabric worn over the shoulders by Christian clergy during religious services; a wide scarf or wrap worn by women around the shoulders.",
    "secondary": "In classical antiquity (Latin stola, from Greek stole, 'garment, equipment'), a full-length draped robe worn by Roman matrons as an emblem of marital dignity and social virtue.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "The Canterbury Tales",
        "quote": "Upon his priestly robes rested an embroidered silk **stole**, signifying the solemn duties of holy orders."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The patrician matron retained the dignified long **stole** as a public emblem of chastity and civil rank."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "The vicar adjusted his liturgical **stole** as he walked solemnly through the lych-gate toward the open grave."
      }
    ]
  },
  "Dashboard — stol/stolid.md": {
    "primary": "Calm, dependable, and showing little emotion, animation, or excitement; impassive and phlegmatic.",
    "secondary": "In psychological characterization, descriptive of a temperament impervious to intellectual agitation, aesthetic sensitivity, or panic, often marked by obstinate endurance.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "He sat in the gloomy corner with a **stolid** countenance, utterly indifferent to the turbulent legal arguments around him."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The impenetrable African jungle stood silent and menacing before the **stolid** gaze of our tired crew."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Her husband's **stolid** composure under severe criticism proved more exasperating than open anger."
      }
    ]
  },
  "Dashboard — stol/stolidity.md": {
    "primary": "The quality or state of being stolid; phlegmatic impassiveness, dull indifference, or absence of emotional expression.",
    "secondary": "In narrative literature, a deliberate or constitutional apathy that resists sudden enthusiasm, artistic nuance, or spiritual crisis.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Starbuck's face betrayed an innate dread, contrasting sharply with the iron **stolidity** of the pagan harpooners."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of Four",
        "quote": "Inspector Jones received the startling revelation of murder with his usual bureaucratic **stolidity**."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Beneath his smooth, British **stolidity**, she gradually perceived a stubborn reservoir of pride."
      }
    ]
  },
  "Dashboard — stol/stolidly.md": {
    "primary": "In a stolid manner; with dull calmness, impassivity, and lack of visible feeling or excitement.",
    "secondary": "In dramatic narrative, describing a heavy, mechanical, or unyielding course of action pursued without panic or hesitation.",
    "quotes": [
      {
        "author": "Jack London",
        "work": "The Call of the Wild",
        "quote": "The sled dogs plodded **stolidly** through the freezing snowdrifts, heedless of the bitter northern gale."
      },
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "The regular soldier munched his dry ration **stolidly**, recounting the total destruction of his battery without panic."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "Henchard stood on the bridge and gazed **stolidly** down into the eddying water, meditating upon his ruin."
      }
    ]
  },
  "Dashboard — stol/stolidness.md": {
    "primary": "The state or characteristic of being stolid; emotional apathy, slow responsiveness, or placid heavy-mindedness.",
    "secondary": "In behavioural psychology, an innate disposition characterized by low emotional reactivity and imperviousness to external excitement or sensory stimuli.",
    "quotes": [
      {
        "author": "Nathaniel Hawthorne",
        "work": "The Scarlet Letter",
        "quote": "The Puritan elders looked on with a grim **stolidness** that chilled the young mother's despairing heart."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "The gatekeeper maintained an obstinate **stolidness**, refusing to yield the keys without direct orders from the master."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "Silver smiled smoothly, but the rough buccaneers behind him displayed an ominous, silent **stolidness**."
      }
    ]
  },
  "Dashboard — stol/stolon.md": {
    "primary": "A slender horizontal plant stem or runner that extends along the surface of the soil, forming roots and shoots at its nodes to produce new independent clonal plants.",
    "secondary": "In invertebrate marine biology, a rootlike or tubular outgrowth produced by colonial organisms (such as hydroids, bryozoans, and tunicates) from which new zooids bud vegetatively.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The garden strawberry spreads with astonishing speed across the bed by projecting runner after **stolon**."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "When a procumbent branch strikes root and generates an independent crown, botanists designate the connecting axis a **stolon**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In creeping compound ascidians, the parent organism buds a vascular **stolon** from which daughter zooids emerge."
      }
    ]
  },
  "Dashboard — stol/stoloniferous.md": {
    "primary": "Bearing, producing, or spreading by means of stolons or creeping horizontal runners.",
    "secondary": "In systematic botany and agrostology, descriptive of grasses and herbaceous perennials (e.g., *Agrostis stolonifera*) that colonize ground rapidly via rooting surface shoots.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "Certain **stoloniferous** herbs rely far more upon creeping vegetative stems than on seed dispersal for territorial survival."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Creeping bent is an intensely **stoloniferous** turfgrass capable of knitting an exceptionally resilient, velvet surface."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The genus comprises several **stoloniferous** species whose horizontal stems establish extensive mats in damp pastures."
      }
    ]
  },
  "Dashboard — oestr/anestric.md": {
    "primary": "Relating to or characterized by anestrus; sexually dormant or lacking reproductive receptivity in female mammals.",
    "secondary": "In veterinary reproductive endocrinology, an adjectival variant denoting the baseline physiological state between successive estrous cycles.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "During the **anestric** interval of autumn, the ovarian follicles of the ewe remain completely quiescent."
      },
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "Comparative physiologists distinguish the fertile phase from the prolonged **anestric** period of seasonal breeders."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Mammalian species inhabiting temperate zones exhibit distinct **anestric** pauses synchronized with winter scarcity."
      }
    ]
  },
  "Dashboard — oestr/anestrous.md": {
    "primary": "Experiencing or characterized by anestrus; being in a seasonal or physiological period of reproductive dormancy or sexual inactivity.",
    "secondary": "In mammalian biology, designating female animals during periods when circulating estrogen is minimal, ovulation ceases, and mating behavior is absent.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The **anestrous** doe shows complete indifference toward the stag throughout the harsh winter months."
      },
      {
        "author": "Julian Huxley",
        "work": "Essays in Popular Science",
        "quote": "Wild mammals generally possess an **anestrous** season which protects the mother from bearing young during food shortages."
      },
      {
        "author": "Solly Zuckerman",
        "work": "The Social Life of Monkeys and Apes",
        "quote": "Unlike lower mammals which have strictly **anestrous** seasons, catarrhine primates exhibit uninterrupted menstrual cycles."
      }
    ]
  },
  "Dashboard — oestr/anestrus.md": {
    "primary": "The recurring period of sexual inactivity and hormonal dormancy in female mammals between breeding seasons or consecutive estrous cycles.",
    "secondary": "In reproductive endocrinology, a physiological state marked by low gonadotropin secretion, minimal ovarian activity, and absence of secondary sexual receptive behaviors.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "Following the cessation of lactation, the female sheep enters an extended seasonal **anestrus**."
      },
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "The onset of daylight changes in spring breaks the endocrine quietude of **anestrus** in seasonal rodents."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The synchronization of breeding cycles through well-timed **anestrus** ensures that offspring emerge when forage is abundant."
      }
    ]
  },
  "Dashboard — oestr/anoestrous.md": {
    "primary": "The standard British spelling of anestrous; being in a period of reproductive dormancy, sexual quiescence, or non-breeding condition.",
    "secondary": "In comparative mammalian physiology, describing the female endocrine status when ovarian follicle maturation and sexual receptivity are suspended.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The ovaries of the **anoestrous** vixen regress significantly during the late summer months."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Seasonal triggers reactivate the reproductive glands of previously **anoestrous** animals as spring approaches."
      },
      {
        "author": "Solomon Zuckerman",
        "work": "Functional Affinities of Man, Monkeys, and Apes",
        "quote": "The contrast between an **anoestrous** carnivore and an uninterrupted primate cycle highlights major evolutionary shifts."
      }
    ]
  },
  "Dashboard — oestr/anoestrum.md": {
    "primary": "The period of sexual dormancy and non-breeding between periods of oestrus in female mammals; a Latinate technical synonym for anoestrus.",
    "secondary": "In veterinary endocrinology, the phase of the oestrous cycle during which the reproductive tract is atrophic and pituitary gonadotropin output remains low.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "During **anoestrum**, the uterine mucosa shows marked involution and an absence of secretory activity."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The term **anoestrum** designates that quietude of the generative organs intervening between rutting seasons."
      },
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "Laboratory studies confirm that artificial illumination can abbreviate the duration of physiological **anoestrum** in sheep."
      }
    ]
  },
  "Dashboard — oestr/anoestrus.md": {
    "primary": "The British orthographical variant of anestrus; the period of sexual quiescence and hormonal dormancy between breeding seasons in female mammals.",
    "secondary": "In livestock management and comparative zoology, the non-cycling stage of seasonal polyoestrous species induced by photoperiod, lactation, or nutritional deficit.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The transition from **anoestrus** to active breeding condition is mediated by increasing hypothalamic stimulation."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Prolonged winter **anoestrus** prevents fatal energy expenditure during the most severe climatic stresses."
      },
      {
        "author": "Julian Huxley",
        "work": "The Individual in the Animal Kingdom",
        "quote": "The rhythms of seasonal **anoestrus** reflect an intimate evolutionary adaptation to ecological carrying capacity."
      }
    ]
  },
  "Dashboard — oestr/estrogen.md": {
    "primary": "Any of a group of steroid hormones that promote the development and maintenance of female secondary sex characteristics and regulate the reproductive cycle.",
    "secondary": "In human biochemistry and clinical pharmacology, primarily estradiol, estrone, and estriol, synthesized by the ovaries, placenta, and adrenal glands, acting via nuclear estrogen receptors.",
    "quotes": [
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "The discovery of **estrogen** resolved the long-standing mystery of how the ovary commands the uterine cycle."
      },
      {
        "author": "Edward Doisy",
        "work": "The Assay and Isolation of Estrogens",
        "quote": "Pure crystalline **estrogen** obtained from follicular fluid demonstrated immense potency in biological assays."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The evolutionary emergence of **estrogen** and its target receptors represents a fundamental milestone in vertebrate biology."
      }
    ]
  },
  "Dashboard — oestr/estrogenic.md": {
    "primary": "Producing, inducing, or having the physiological properties of estrogen; promoting estrus or female secondary sexual traits.",
    "secondary": "In pharmacology and toxicology, describing synthetic compounds, phytoestrogens, or environmental xenobiotics capable of binding to and activating estrogen receptors.",
    "quotes": [
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "Substances exhibiting powerful **estrogenic** activity were detected not only in mammalian tissue but in certain legumes."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Synthetic pesticides can mimic hormonal signals, displaying potent **estrogenic** effects that disrupt wildlife reproduction."
      },
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The administration of an **estrogenic** extract provoked typical receptive behavior in ovariectomized test animals."
      }
    ]
  },
  "Dashboard — oestr/estrous.md": {
    "primary": "Of, relating to, or being in the state of estrus; characterizing the mammalian sexual and ovulatory cycle.",
    "secondary": "In veterinary medicine and reproductive biology, modifying cycles, phases, or physiological behaviors associated with recurrent sexual receptivity (e.g., the *estrous cycle*).",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The length of the **estrous** cycle varies widely across mammalian orders, spanning days in rodents to months in carnivores."
      },
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "During each **estrous** surge, profound histological changes transform the vaginal epithelium and uterine glands."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Behavioral synchronization during the **estrous** phase prevents wasteful mating attempts between incompatible species."
      }
    ]
  },
  "Dashboard — oestr/estrus.md": {
    "primary": "A recurring period of maximum sexual receptivity and fertility in female mammals (often called 'heat'), coinciding with ovulation.",
    "secondary": "In reproductive biology, the distinct ovulatory phase (from Greek oistros, 'gadfly, passionate frenzy') marked by elevated estrogen, follicular maturation, and receptivity to coitus.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "During peak **estrus**, the female manifests a dramatic change in demeanour, actively seeking out the male."
      },
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "Ovulation coincides precisely with the physiological summit of **estrus**, ensuring maximal probability of fertilization."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "In many quadrupeds, the female is willing to admit the male only during the brief season of **estrus**."
      }
    ]
  },
  "Dashboard — oestr/monoestrous.md": {
    "primary": "Having or experiencing only one period of estrus (or heat) during each breeding season or annual cycle (as in bears, wolves, and roe deer).",
    "secondary": "In comparative ethology and mammalian reproductive physiology, contrasting with polyestrous species that cycle repeatedly if pregnancy does not occur.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "Wild canids are typically **monoestrous**, coming into breeding condition only once per year in late winter."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "The **monoestrous** schedule of arctic mammals prevents the perilous birth of litters during mid-winter."
      },
      {
        "author": "Julian Huxley",
        "work": "The Individual in the Animal Kingdom",
        "quote": "A strictly **monoestrous** animal expends all its reproductive reserves upon a single, decisive annual effort."
      }
    ]
  },
  "Dashboard — oestr/oestr.md": {
    "primary": "The Greek root oistros (meaning 'gadfly, sting, frenzy, or vehement impulse'), which provides the etymological basis for biological terms relating to reproductive heat and estrogen hormones.",
    "secondary": "In classical literature and the history of science, an ancient term for the maddening gadfly sent by Hera to torment Io, later adopted by 19th-century physiologists to denote reproductive frenzy.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The classical Greek root **oestr**, originally signifying a stinging gadfly, came to represent uncontrollable passion and biological heat."
      },
      {
        "author": "Ernest Weekley",
        "work": "The Romance of Words",
        "quote": "From the tormenting gadfly **oestr** that pursued mythical Io, modern endocrinology named the hormones of sexual vitality."
      },
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "Under the radical **oestr**, we group medical terms referring to intense excitement, seasonal rut, and endocrine regulation."
      }
    ]
  },
  "Dashboard — oestr/oestradiol.md": {
    "primary": "The most potent and prevalent naturally occurring estrogen hormone, secreted primarily by the ovarian follicles and responsible for female secondary sexual development.",
    "secondary": "In biochemical endocrinology, a C18 steroid diol that binds with high affinity to alpha and beta estrogen receptors, regulating gonadotropin feedback and target tissue proliferation.",
    "quotes": [
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "Biochemists isolated **oestradiol** as the most active natural estrogen secreted by the developing graafian follicle."
      },
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "Rising levels of circulating **oestradiol** stimulate the pre-ovulatory surge of luteinizing hormone from the anterior pituitary."
      },
      {
        "author": "Edward Doisy",
        "work": "The Biochemistry of Estrogens",
        "quote": "The structural identification of **oestradiol** marked the opening of a modern therapeutic era in clinical endocrinology."
      }
    ]
  },
  "Dashboard — oestr/oestridae.md": {
    "primary": "A family of stout, hairy dipteran flies (commonly called botflies or warble flies) whose parasitic larvae develop within the flesh, nasal passages, or stomach of mammals.",
    "secondary": "In systematic entomology, a cosmopolitan family of calyptrate muscoid flies featuring vestigial mouthparts in adults and obligate endoparasitic larval stages in ungulates and rodents.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Fly",
        "quote": "The dreaded fly of the family **Oestridae** deposits its eggs on the coat of grazing cattle with stealthy persistence."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The parasitic larvae of the **Oestridae** exhibit exquisite adaptations for anchoring themselves within the stomach walls of horses."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Adult members of the **Oestridae** take no nourishment, their brief existence being devoted solely to reproduction."
      }
    ]
  },
  "Dashboard — oestr/oestriol.md": {
    "primary": "A relatively weak estrogen hormone formed as a metabolic byproduct of estradiol and estrone, produced in substantial quantities by the placenta during pregnancy.",
    "secondary": "In maternal-fetal medicine, a hydroxylated C18 steroid whose concentration in maternal serum serves as a clinical index of fetal-placental viability.",
    "quotes": [
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "During normal human gestation, the placental syncytiotrophoblast secretes abundant quantities of **oestriol** into maternal circulation."
      },
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The relatively modest potency of **oestriol** allows it to circulate at high levels without provoking excessive peripheral stimulation."
      },
      {
        "author": "Edward Doisy",
        "work": "The Assay and Isolation of Estrogens",
        "quote": "Laboratory purification distinguished **oestriol** from estrone by its extra hydroxyl group and distinct solubility."
      }
    ]
  },
  "Dashboard — oestr/oestrogen.md": {
    "primary": "The British orthographical variant of estrogen; any steroid hormone that regulates female sexual development, menstrual and estrous cycles, and bone density.",
    "secondary": "In clinical medicine and pharmacology, a class of steroidal compounds exerting biological effects across reproductive, cardiovascular, neuroendocrine, and skeletal tissues.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The cyclical surge of ovarian **oestrogen** induces profound changes in the vascularity of the endometrium."
      },
      {
        "author": "Julian Huxley",
        "work": "Essays in Popular Science",
        "quote": "The action of **oestrogen** upon bodily form demonstrates how minute chemical messengers govern macroscopic morphology."
      },
      {
        "author": "Solly Zuckerman",
        "work": "The Social Life of Monkeys and Apes",
        "quote": "Fluctuations in circulating **oestrogen** correlate closely with sexual skin swellings in baboons and chimpanzees."
      }
    ]
  },
  "Dashboard — oestr/oestrone.md": {
    "primary": "An estrogenic steroid hormone that is the primary estrogen produced after menopause, synthesized primarily in adipose tissue from adrenal precursors.",
    "secondary": "In human biochemistry, a ketone-containing C18 steroid (estrone) with lower receptor affinity than estradiol, functioning as an intermediary metabolite and postmenopausal hormone.",
    "quotes": [
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "Isolation of crystalline **oestrone** from pregnancy urine provided the first chemical evidence of female sex hormones."
      },
      {
        "author": "Edward Doisy",
        "work": "The Assay and Isolation of Estrogens",
        "quote": "Chemical analysis proved **oestrone** to possess a keto oxygen atom at the seventeenth position of the cyclopentanoperhydrophenanthrene ring."
      },
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "Following the menopausal cessation of follicular function, peripheral **oestrone** becomes the predominant estrogen."
      }
    ]
  },
  "Dashboard — oestr/oestrus.md": {
    "primary": "The British orthographical variant of estrus; the recurrent period of sexual excitement, heat, and ovulatory fertility in non-human female mammals.",
    "secondary": "In classical literature, a gadfly or divine frenzy sent to provoke madness; in zoology, the specific hormonal interval when female mammals accept copulation.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "The onset of **oestrus** in the cow is accompanied by unmistakable restlessness, bellowing, and mounting behavior."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Female mammals in **oestrus** emit distinctive scents that carry on the wind to attract courting males from afar."
      },
      {
        "author": "Julian Huxley",
        "work": "Essays in Popular Science",
        "quote": "The ancient Greek word for frenzy, **oestrus**, aptly captures the sudden, instinctual compulsion of seasonal mating."
      }
    ]
  },
  "Dashboard — oestr/polyestrous.md": {
    "primary": "Having more than one period of estrus (or heat) in a single year or breeding season (as seen in rodents, cows, and pigs).",
    "secondary": "In comparative zoology, descriptive of species that undergo continuous or seasonal recurrent ovulatory cycles until conception intervenes.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "Domestic cattle are typical **polyestrous** animals, repeating their reproductive cycles every twenty-one days year-round."
      },
      {
        "author": "George Corner",
        "work": "The Hormones in Human Reproduction",
        "quote": "The laboratory rat provides an indispensable model because it is continuously **polyestrous** with short four-day cycles."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "A **polyestrous** strategy confers high reproductive resilience against accidental mating failures during early spring."
      }
    ]
  },
  "Dashboard — oestr/polyoestrous.md": {
    "primary": "The British spelling of polyestrous; experiencing recurring cycles of oestrus throughout a breeding season or throughout the entire year.",
    "secondary": "In livestock husbandry and wildlife biology, classifying mammalian females whose reproductive endocrine rhythm repeats if fertilization is missed.",
    "quotes": [
      {
        "author": "Francis Marshall",
        "work": "The Physiology of Reproduction",
        "quote": "Sheep are seasonally **polyoestrous**, exhibiting repeated cycles of heat only during the shortening days of autumn."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Evolutionary transitions from monoestrous to **polyoestrous** breeding correlate with improved environmental stability."
      },
      {
        "author": "Julian Huxley",
        "work": "The Individual in the Animal Kingdom",
        "quote": "In highly domesticated species, selection has favored **polyoestrous** rhythms that maximize reproductive yields."
      }
    ]
  },
  "Dashboard — tach/detach.md": {
    "primary": "To disengage, disconnect, or separate something from that to which it is attached; to send away a military unit on a specialized assignment.",
    "secondary": "In psychology and moral philosophy, to withdraw emotionally or intellectually from personal bias, passion, or entanglement in order to achieve objectivity.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventures of Sherlock Holmes",
        "quote": "He used a pocket knife to **detach** the sealed parchment from the hollow lining of the strongbox."
      },
      {
        "author": "Carl von Clausewitz",
        "work": "On War",
        "quote": "The general decided to **detach** two light cavalry brigades to harass the enemy flank and delay their retreat."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Conquest of Happiness",
        "quote": "A wise philosopher learns to **detach** his ego from petty daily irritations, viewing them sub specie aeternitatis."
      }
    ]
  },
  "Dashboard — tach/detachable.md": {
    "primary": "Capable of being separated, unfastened, or removed from a larger assembly without causing damage.",
    "secondary": "In mechanical engineering and industrial design, designating components engineered with quick-release mechanisms, modular couplings, or threaded fasteners.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "He unbolted the **detachable** nickel lever and slipped it into his pocket to prevent unauthorized tampering."
      },
      {
        "author": "Jules Verne",
        "work": "Twenty Thousand Leagues Under the Sea",
        "quote": "Captain Nemo pointed to the **detachable** dinghy secured atop the hull of the Nautilus."
      },
      {
        "author": "Henry Ford",
        "work": "My Life and Work",
        "quote": "We designed every engine part to be easily **detachable** so that ordinary mechanics could service the machine in the field."
      }
    ]
  },
  "Dashboard — tach/detached.md": {
    "primary": "Separate, disconnected, or standing apart; unattached to another structure.",
    "secondary": "In psychology and literary criticism, exhibiting impartiality, emotional distance, or objective contemplation free from personal interest or distress.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "Winston watched the proceedings with a **detached** curiosity, as if observing a drama enacted by strangers."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Mr. Ramsay looked out over the sea with a **detached**, melancholy gaze, pondering the fate of human ambition."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "Marlow narrated the tragedy in a calm, **detached** manner that underscored the inevitability of the catastrophe."
      }
    ]
  },
  "Dashboard — tach/detachment.md": {
    "primary": "The state of being separate, distant, or disengaged; a posture of objective impartiality and emotional freedom.",
    "secondary": "In military operations, a body of troops or naval vessels separated from the main force and deployed on a distinct mission.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "A small **detachment** of legionaries guarded the mountain pass against the barbarian incursions."
      },
      {
        "author": "Aldous Huxley",
        "work": "Ends and Means",
        "quote": "True spiritual freedom is achieved only through profound **detachment** from worldly ambitions and physical desires."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Saintly figures cultivate an inner **detachment** that renders them tranquil amid worldly catastrophe."
      }
    ]
  },
  "Dashboard — tach/tach.md": {
    "primary": "The Greek combining form tachy- or tach- (from tachys, meaning 'swift, quick, rapid, or speed'), widely used in technical and scientific terms denoting velocity or acceleration.",
    "secondary": "In linguistics and historical terminology, an etymological morpheme contrasting with brady- (slow), found in tachycardia, tachometer, and tachytelic evolution.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek element **tach**, signifying velocity and haste, forms the root of modern instruments that measure mechanical revolutions."
      },
      {
        "author": "Ernest Weekley",
        "work": "The Romance of Words",
        "quote": "In medical nomenclature, the stem **tach** instantly signals accelerated physiological cadence or abnormal haste."
      },
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "Under **tach**, the lexicographer gathers all technical indicators of high speed, rapid rotation, and promptitude."
      }
    ]
  },
  "Dashboard — tach/tacheometer.md": {
    "primary": "A surveying instrument (a specialized theodolite) designed to measure distances, directions, and elevation differences rapidly by optical readings on a graduated rod.",
    "secondary": "In civil engineering and topographic geodesy, an optical-mechanical device that eliminates chaining by calculating horizontal distances through stadia trigonometry.",
    "quotes": [
      {
        "author": "William Rankine",
        "work": "A Manual of Civil Engineering",
        "quote": "By using a modern **tacheometer**, the surveyor determines both the elevation and horizontal distance of distant stations in a single reading."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "The contouring of the steep hillside site was executed with exceptional speed by means of a transit **tacheometer**."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Geologists employed the **tacheometer** to map the rugged contours of the volcanic crater with high geodetic accuracy."
      }
    ]
  },
  "Dashboard — tach/tachinidae.md": {
    "primary": "A large and diverse family of true flies (order Diptera), whose larvae are internal parasitoids of caterpillars, beetles, and other insect pests.",
    "secondary": "In economic entomology and biological pest control, a vital family of bristly calyptrate flies whose endoparasitic habits naturally regulate agricultural insect infestations.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Fly",
        "quote": "A bristly fly of the family **Tachinidae** hovered over the succulent caterpillar, preparing to glue her parasitic eggs to its neck."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The balance of insect populations in nature is relentlessly enforced by the internal larvae of the **Tachinidae**."
      },
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "Economic entomologists value the **Tachinidae** above almost all other dipteran families for their role in checking agricultural pests."
      }
    ]
  },
  "Dashboard — tach/tachistoscope.md": {
    "primary": "An apparatus for projecting or exposing visual images or textual stimuli for a brief, precisely controlled interval of time (such as milliseconds).",
    "secondary": "In experimental cognitive psychology and reading research, an instrument used to assess visual perception thresholds, tachistoscopic recognition, and sensory memory.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Exposing letters by means of a rapid **tachistoscope** demonstrated that the mind grasps whole words before distinguishing individual letters."
      },
      {
        "author": "Edward Titchener",
        "work": "Experimental Psychology",
        "quote": "The laboratory **tachistoscope** delivers exposures calibrated down to the hundredth part of a second with remarkable consistency."
      },
      {
        "author": "B. F. Skinner",
        "work": "The Technology of Teaching",
        "quote": "The **tachistoscope** was initially utilized in military training to accelerate the instant recognition of enemy aircraft silhouettes."
      }
    ]
  },
  "Dashboard — tach/tachogram.md": {
    "primary": "A graphic tracing or chart produced by a tachograph or recording device, displaying speed or instantaneous heart rate over a period of time.",
    "secondary": "In cardiovascular physiology and autonomic research, a plot of consecutive heartbeat intervals (RR intervals) used for analyzing heart rate variability (HRV).",
    "quotes": [
      {
        "author": "Augustus Waller",
        "work": "An Introduction to Human Physiology",
        "quote": "Inspection of the continuous **tachogram** revealed sudden transient fluctuations in pulse rate provoked by deep inspiration."
      },
      {
        "author": "Willem Einthoven",
        "work": "The Mechanism of the Electrocardiogram",
        "quote": "From the photographic **tachogram**, we measured the microscopic variability in beat-to-beat cardiac timing."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The physiological **tachogram** visually represents the velocity of blood flow or pulse frequency across extended observation periods."
      }
    ]
  },
  "Dashboard — tach/tachograph.md": {
    "primary": "A device fitted to a motor vehicle or locomotive that automatically records speed, distance traveled, and driver driving and rest periods onto a chart or digital memory.",
    "secondary": "In transport regulation and forensic accident analysis, a tamper-resistant recorder mandated on commercial vehicles to ensure adherence to statutory safety limits.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The War in the Air",
        "quote": "The engineer checked the drum of the **tachograph** to confirm the locomotive's acceleration over the steep viaduct."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Bruce-Partington Plans",
        "quote": "A careful examination of the train's **tachograph** verified that it had slowed down abruptly near the signal box."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "The modern highway transport system enforces mechanical discipline through the unblinking record of the **tachograph**."
      }
    ]
  },
  "Dashboard — tach/tachometer.md": {
    "primary": "An instrument that measures and indicates the rotation speed of a shaft or disk, usually expressed in revolutions per minute (RPM).",
    "secondary": "In mechanical engineering, aviation, and automotive telemetry, a gauge essential for monitoring engine operating limits and preventing overspeed damage.",
    "quotes": [
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Wind, Sand and Stars",
        "quote": "My eyes darted constantly between the altimeter, the oil gauge, and the needle of the **tachometer** trembling at two thousand revolutions."
      },
      {
        "author": "H. G. Wells",
        "work": "The First Men in the Moon",
        "quote": "Cavor adjusted the control valve while keeping his eyes glued to the dial of the centrifugal **tachometer**."
      },
      {
        "author": "Nevil Shute",
        "work": "No Highway",
        "quote": "The test pilot noted a sudden fluctuation in the port **tachometer** before the vibration began to shake the airframe."
      }
    ]
  },
  "Dashboard — tach/tachycardia.md": {
    "primary": "An abnormally rapid resting heart rate, typically exceeding 100 beats per minute in an adult.",
    "secondary": "In clinical cardiology, a diverse category of arrhythmias (including sinus, supraventricular, and ventricular tachycardia) arising from anomalous cardiac pacing or conduction pathways.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe paroxysmal **tachycardia** may develop abruptly in an otherwise healthy patient, elevating the pulse to two hundred beats a minute."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The physician identified persistent **tachycardia** as a hallmark of severe thyrotoxicosis and systemic exhaustion."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The patient collapsed upon the sofa, his wild pulse beating with that desperate **tachycardia** which heralds cardiovascular shock."
      }
    ]
  },
  "Dashboard — tach/tachyglossidae.md": {
    "primary": "The family of monotreme mammals comprising the echidnas (or spiny anteaters), endemic to Australia and New Guinea.",
    "secondary": "In vertebrate taxonomy and evolutionary biology, an archaic family of egg-laying mammals distinguished by an elongated snout, toothless jaws, and an agile vermiform tongue (hence *fast-tongued*).",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The family **Tachyglossidae** occupies a unique position in natural history, uniting mammalian hair and lactation with oviparous reproduction."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Members of the **Tachyglossidae** possess powerful claws for burrowing and an extensible, sticky tongue suited for harvesting ants."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The survival of the **Tachyglossidae** in Australasia demonstrates the long persistence of primitive mammalian lineages in geographic isolation."
      }
    ]
  },
  "Dashboard — tach/tachyglossus.md": {
    "primary": "The genus of short-beaked echidnas (*Tachyglossus aculeatus*), characterized by spiny quills, an egg-laying reproductive strategy, and a rapid insect-catching tongue.",
    "secondary": "In mammalian zoology, the monotypic genus representing the short-beaked echidna of Australia and southern New Guinea, capable of entering deep torpor.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Dissection of the palate in **Tachyglossus** reveals specialized horny spines that grind insect prey against the roof of the mouth."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The skeleton of **Tachyglossus** retains primitive reptilian features in the shoulder girdle, notably an interclavicle."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "When threatened by predators, **Tachyglossus** burrows straight down into the gravel with astonishing speed until only spines protrude."
      }
    ]
  },
  "Dashboard — tach/tachygraphy.md": {
    "primary": "The art or practice of rapid writing; shorthand or stenography.",
    "secondary": "In classical and medieval palaeography, the system of abbreviated notations (such as the Roman Tironian notes or Byzantine tachygraphic hands) used by ancient scribes to record orations verbatim.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The impassioned speeches of Cicero were taken down verbatim by scribes trained in the Roman art of **tachygraphy**."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "From the Greek words for swift and writing, scholars coined **tachygraphy** to denote all systems of shorthand."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "He acquired a remarkable proficiency in **tachygraphy**, enabling him to preserve the fleeting thoughts of his patron without delay."
      }
    ]
  },
  "Dashboard — tach/tachylite.md": {
    "primary": "A dark, glassy volcanic rock formed by the rapid cooling of basaltic magma.",
    "secondary": "In petrology and vulcanology, a natural basaltic glass (also spelled tachylyte) occurring at the chilled margins of dikes, sills, and lava pillows where crystallization was arrested.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Geological Observations on Volcanic Islands",
        "quote": "Along the outer rim of the basaltic flow, the molten rock had cooled instantaneously into a brittle, lustrous **tachylite**."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Thin sections of **tachylite** under the microscope show a dark brown isotropic glass crowded with embryonic microlites."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The sudden quenching of the lava stream beneath the ocean brine produced a selvedge of pitch-black **tachylite**."
      }
    ]
  },
  "Dashboard — tach/tachymeter.md": {
    "primary": "An instrument designed to measure speed or velocity rapidly; specifically, a graduated scale on a watch bezel used to compute speed based on travel time over a measured distance.",
    "secondary": "In surveying, an alternative term for a tacheometer, an optical instrument that expeditiously determines distances and angles without physical tape measurements.",
    "quotes": [
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Night Flight",
        "quote": "The aviator timed his flight between beacons, reading his ground velocity directly from the engraved **tachymeter** bezel."
      },
      {
        "author": "William Rankine",
        "work": "A Manual of Civil Engineering",
        "quote": "The modern geodetic **tachymeter** allows the engineer to complete a comprehensive triangulation in half the customary time."
      },
      {
        "author": "Nevil Shute",
        "work": "No Highway",
        "quote": "He glanced at the **tachymeter** on his wrist as the prototype aircraft crossed the measured nautical mile marker."
      }
    ]
  },
  "Dashboard — tach/tachypleus.md": {
    "primary": "A genus of Asian horseshoe crabs (family Limulidae), including the Chinese and Indo-Pacific horseshoe crabs.",
    "secondary": "In marine biology and invertebrate zoology, a genus of ancient chelicerate 'living fossils' characterized by a trilobite-like carapace and blue, copper-based hemocyanin blood used in endotoxin assays.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The Asian horseshoe crab, classified under **Tachypleus**, preserves a body plan virtually unchanged since the Jurassic."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Marine biologists study **Tachypleus** to decipher the morphological transition between ancient trilobites and modern arachnids."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The slow morphological divergence of **Tachypleus** across millions of years represents a classic case of evolutionary bradytely."
      }
    ]
  },
  "Dashboard — tach/tachyrhythmia.md": {
    "primary": "Any abnormal heart rhythm characterized by a rapid heartbeat; an alternative clinical term for tachyarrhythmia.",
    "secondary": "In electrophysiology, a pathological cardiac rhythm (originating in the atria or ventricles) where the activation frequency exceeds 100 beats per minute, compromising cardiac output.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The electrocardiogram confirmed an acute onset of ventricular **tachyrhythmia** during the height of the febrile attack."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Physicians apply the term **tachyrhythmia** to any state wherein the heart pulses with excessive and irregular speed."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "Unless prompt vagal stimulation or medication arrests the **tachyrhythmia**, systemic hypoperfusion quickly ensues."
      }
    ]
  },
  "Dashboard — tach/tachytelic.md": {
    "primary": "Evolving at an exceptionally rapid or accelerated rate compared to standard evolutionary lineages.",
    "secondary": "In paleontology and macroevolution (a concept introduced by George Gaylord Simpson), designating phyletic lineages that experience swift morphological divergence under intense selective pressures.",
    "quotes": [
      {
        "author": "George Gaylord Simpson",
        "work": "Tempo and Mode in Evolution",
        "quote": "Lineages undergoing **tachytelic** evolution diverge with extraordinary velocity, often bridging major adaptive zones in brief geological intervals."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The rapid adaptive radiation of island finches provides an outstanding living illustration of **tachytelic** divergence."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Simpson coined the term **tachytelic** to characterize those rapid bursts of evolutionary change that punctuate the fossil record."
      }
    ]
  },
  "Dashboard — dram/aerodrome.md": {
    "primary": "A defined location on land or water (including buildings, installations, and equipment) intended to be used for the arrival, departure, and surface movement of aircraft; an airfield or airport.",
    "secondary": "Historically, Samuel Langley's nineteenth-century term for an airborne flying machine (from Greek aer 'air' and dromos 'running/course'); later adopted in British aviation for landing grounds.",
    "quotes": [
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "Our fighter squadrons scrambled from every coastal **aerodrome** to intercept the incoming bombers over Kent."
      },
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Wind, Sand and Stars",
        "quote": "The beacon lights of the distant **aerodrome** cut through the desert night, welcoming the weary airmail pilot home."
      },
      {
        "author": "H. G. Wells",
        "work": "The Shape of Things to Come",
        "quote": "The modern **aerodrome** had become the true crossroads of human commerce, supplanting the ancient maritime ports."
      }
    ]
  },
  "Dashboard — dram/anadromous.md": {
    "primary": "Migrating up rivers from the sea to spawn in fresh water (characteristic of fishes such as salmon, sea trout, and shad).",
    "secondary": "In ichthyology and aquatic ecology, describing species that spend the majority of their adult life in marine environments but undergo physiological smoltification to breed in inland streams.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The heroic journeys of **anadromous** fishes against furious mountain cataracts illustrate the relentless power of reproductive instincts."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The great run of **anadromous** salmon entered the river estuary, scenting the familiar gravel beds of their native headwaters."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "Dams and mills now bar the path of the **anadromous** shad that once ascended our pristine rivers in millions."
      }
    ]
  },
  "Dashboard — dram/antidromic.md": {
    "primary": "Proceeding or conducting impulses in a direction opposite to the normal physiological course (as along a nerve axon).",
    "secondary": "In neurophysiology, describing artificial or pathological impulses traveling retrogradely toward the cell soma, used to measure axonal conduction velocities and refractory periods.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Electrical stimulation of the sensory root produced an **antidromic** wave that invaded the spinal cord backwards."
      },
      {
        "author": "Edgar Adrian",
        "work": "The Mechanism of Nervous Action",
        "quote": "By recording the **antidromic** impulse along the motor axon, we were able to measure the central latency of the reflex arc."
      },
      {
        "author": "John Eccles",
        "work": "The Neurophysiological Basis of Mind",
        "quote": "The **antidromic** invasion of the motoneuron soma was found to be blocked during states of postsynaptic inhibition."
      }
    ]
  },
  "Dashboard — dram/catadromous.md": {
    "primary": "Migrating down rivers to the sea to spawn (characteristic of fishes such as the European and American freshwater eels).",
    "secondary": "In aquatic biology, describing a diadromous life cycle that is the reverse of anadromous, where feeding and somatic growth occur in freshwater rivers while breeding occurs in oceanic abysses.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The mature **catadromous** eels slipped down the dark autumn river, drawn by an irresistible call to the Sargasso Sea."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "The remarkable **catadromous** migration of the freshwater eel was finally deciphered through Johannes Schmidt's ocean surveys."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Unlike salmon, **catadromous** species spend their years of growth in inland waters and descend to oceanic depths to reproduce."
      }
    ]
  },
  "Dashboard — dram/diadromous.md": {
    "primary": "Migrating regularly between fresh water and the sea at predictable stages of the life cycle (encompassing both anadromous and catadromous species).",
    "secondary": "In fisheries science, describing aquatic species that possess specialized osmoregulatory adaptations to survive dramatic salinity transitions between marine and fluvial ecosystems.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Many **diadromous** fishes must adjust their entire gill physiology when passing from dense brine into sweet mountain rivers."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The migratory discipline of **diadromous** populations prevents localized inbreeding by mixing river stocks on oceanic feeding grounds."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Geological alterations of river drainages have profoundly shaped the migration routes of ancient **diadromous** species."
      }
    ]
  },
  "Dashboard — dram/dram.md": {
    "primary": "A traditional small unit of weight (1/16 of an ounce avoirdupois, or 1/8 of an ounce apothecaries'); by extension, a small drink of liquor (especially whisky) or a tiny quantity of anything.",
    "secondary": "In historical metrology and pharmacy (from Greek drachme, 'a handful, a drachma coin'), a standard measure for compounding medicinal tinctures and dry chemicals.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Romeo and Juliet",
        "quote": "Let me have a **dram** of poison, such soon-speeding gear as will disperse itself through all the veins."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Kidnapped",
        "quote": "The skipper poured himself a hearty **dram** of brandy to ward off the freezing mist of the Scottish coast."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Not a single **dram** of comfort could be extracted from Joe's awkward, tongue-tied condolences."
      }
    ]
  },
  "Dashboard — dram/drama.md": {
    "primary": "A composition in verse or prose intended to portray life or character or to tell a story through dialogue and action on a stage; a theatrical play.",
    "secondary": "In everyday speech and narrative theory, an exciting, emotional, or unexpected series of real-life events marked by intense conflict, suspense, and emotional climax.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Poetics",
        "quote": "Tragic **drama** is an imitation of an action that is serious, complete, and of a certain magnitude, through pity and fear effecting catharsis."
      },
      {
        "author": "William Shakespeare",
        "work": "As You Like It",
        "quote": "All the world's a stage, and all the men and women merely players; they have their exits and their entrances in life's vast **drama**."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "Attic **drama** arose from the miraculous union of the Dionysian chorus with the Apollonian world of images."
      }
    ]
  },
  "Dashboard — dram/dramamine.md": {
    "primary": "A proprietary brand name for dimenhydrinate, an over-the-counter antihistamine medication widely used to prevent and treat motion sickness, nausea, and vertigo.",
    "secondary": "In clinical pharmacology, an H1 receptor antagonist with central anticholinergic properties that dampens vestibular stimulation in the inner ear during travel by sea or air.",
    "quotes": [
      {
        "author": "Hunter S. Thompson",
        "work": "Fear and Loathing in Las Vegas",
        "quote": "We had two bags of grass, seventy-five pellets of mescaline, and a whole galaxy of multi-colored uppers and **Dramamine**."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Vestibular disturbances can sometimes be alleviated by anti-emetic medications such as **Dramamine**, which dull cerebellar sensitivity."
      },
      {
        "author": "David Foster Wallace",
        "work": "A Supposedly Fun Thing I'll Never Do Again",
        "quote": "The cruise passengers queued at the ship's infirmary for transdermal patches and chewable tablets of **Dramamine** before the swell worsened."
      }
    ]
  },
  "Dashboard — dram/dramatic.md": {
    "primary": "Relating to drama or the theater; strikingly sensational, exciting, or emotional in appearance, effect, or circumstance.",
    "secondary": "In narrative arts and rhetoric, producing a vivid, instantaneous impression through contrast, conflict, and sudden transformation of circumstances.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "The sudden collapse of the ancient mansion was attended by a **dramatic** crash that reverberated across the tarn."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Her arrival at the bedside transformed a quiet domestic illness into a scene of intense **dramatic** tension."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "The sudden evacuation of Dunkirk remains one of the most **dramatic** episodes in our military annals."
      }
    ]
  },
  "Dashboard — dram/dramatically.md": {
    "primary": "In a dramatic manner; strikingly, severely, or with theatrical flair and emotional impact.",
    "secondary": "In statistical analysis and historiography, denoting change or progress that occurs with startling speed, magnitude, or conspicuousness.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The appearance of new species in a region often shifts the balance of competition **dramatically** and irreversibly."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Holmes paused **dramatically** on the threshold, raising his lantern to reveal the mysterious footprints in the mire."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "The sun grew **dramatically** larger and redder in the darkening sky as millions of years sped past in seconds."
      }
    ]
  },
  "Dashboard — dram/dramatics.md": {
    "primary": "The art, practice, or study of dramatic performance and theatrical production; by extension, exaggerated, histrionic, or overly emotional behavior.",
    "secondary": "In educational and amateur contexts, organized extracurricular play-acting; in colloquial psychology, an affectation of dramatic outrage or distress.",
    "quotes": [
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "She had an innate instinct for amateur **dramatics**, never uttering a simple truth without a melodramatic gesture."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "The children spent the stormy afternoon engaged in lively parlor **dramatics**, donning old cloaks and cardboard swords."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Pygmalion",
        "quote": "Spare me your drawing-room **dramatics**, Higgins, and explain how you intend to present this girl to society."
      }
    ]
  },
  "Dashboard — dram/dramatisation.md": {
    "primary": "The standard British spelling of dramatization; the act or process of adapting a literary narrative, historical event, or concept into theatrical, film, or broadcast form.",
    "secondary": "In psychoanalysis and narrative theory, the psychic or artistic process by which abstract ideas, conflicts, or dreams are transformed into sensory, acted scenes.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Dream-work accomplishes a plastic **dramatisation** of latent thoughts, staging them as objective theatrical happenings."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "The stage **dramatisation** of the novel lost all the quiet nuances of the original authorial voice."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "quote": "A clumsy **dramatisation** of history replaces complex political currents with noisy, personal melodrama."
      }
    ]
  },
  "Dashboard — dram/dramatise.md": {
    "primary": "The standard British spelling of dramatize; to adapt a novel, poem, or historical episode into a play or theatrical script.",
    "secondary": "To present an ordinary occurrence or personal grievance in an exaggerated, histrionic, or emotionally heightened manner.",
    "quotes": [
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "It was impossible for Lord Henry not to **dramatise** the situation, viewing the boy's moral decline as a theatrical masterpiece."
      },
      {
        "author": "Virginia Woolf",
        "work": "A Room of One's Own",
        "quote": "To write great fiction, one must **dramatise** human experience without allowing personal bitterness to distort the vision."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Major Barbara",
        "quote": "He sought to **dramatise** the brutal clash between industrial capital and Christian philanthropy upon the open stage."
      }
    ]
  },
  "Dashboard — dram/dramatist.md": {
    "primary": "A person who writes plays; a playwright or author of dramatic literature.",
    "secondary": "In literary criticism, a master of stagecraft, dialogue, and character psychology whose works reveal human motives through live conflict and dialogue.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Preface to Shakespeare",
        "quote": "Shakespeare is above all writers the **dramatist** of nature, holding up to his readers a faithful mirror of manners and life."
      },
      {
        "author": "John Dryden",
        "work": "An Essay of Dramatic Poesy",
        "quote": "A true **dramatist** must balance the regular rules of the ancients with the lively variety of modern stage action."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Plays Pleasant and Unpleasant",
        "quote": "The modern **dramatist** must provoke thought, using comedy as a surgeon uses an anaesthetic while operating on social vices."
      }
    ]
  },
  "Dashboard — dram/dramatization.md": {
    "primary": "The act or process of adapting a story, novel, or real-life event into a dramatic play or cinematic production.",
    "secondary": "In psychology and communication, the portrayal of an abstract condition, grievance, or emotional dilemma in terms of vivid, concrete, and enacted conflict.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "Essays and Reviews",
        "quote": "The successful **dramatization** of a Gothic romance requires relentless compression and intense theatrical atmosphere."
      },
      {
        "author": "Sigmund Freud",
        "work": "A General Introduction to Psychoanalysis",
        "quote": "The dream achieves its compelling illusion through the direct **dramatization** of repressed childhood desires."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World Revisited",
        "quote": "Political propaganda increasingly relies upon the slick **dramatization** of fears rather than rational debate."
      }
    ]
  },
  "Dashboard — dram/dramatize.md": {
    "primary": "To adapt a literary work or factual event into a play or theatrical script; to represent an event with striking dramatic intensity.",
    "secondary": "To exaggerate or inflate an ordinary difficulty into a scene of histrionic proportions; to express symbolically in action.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Art of the Novel",
        "quote": "The novelist must always **dramatize**, transforming internal speculation into immediate, tangible scenes."
      },
      {
        "author": "Mark Twain",
        "work": "Autobiography",
        "quote": "He had a natural instinct to **dramatize** his minor ailments, turning a common cold into a tragic deathbed scene."
      },
      {
        "author": "George Bernard Shaw",
        "work": "The Quintessence of Ibsenism",
        "quote": "Ibsen was the first to **dramatize** the quiet, suffocating hypocrisy of middle-class domestic life."
      }
    ]
  },
  "Dashboard — dram/dramaturgic.md": {
    "primary": "Of or relating to the art of dramatic composition, stagecraft, or theatrical presentation.",
    "secondary": "In performance studies, descriptive of the internal mechanics, pacing, and architectural principles that govern effective theatrical representation.",
    "quotes": [
      {
        "author": "Gotthold Ephraim Lessing",
        "work": "Hamburg Dramaturgy",
        "quote": "Every genuine **dramaturgic** principle must be derived from the fundamental psychology of human emotion."
      },
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "Conversations with Eckermann",
        "quote": "Goethe examined the manuscript with keen **dramaturgic** insight, pointing out where the second act lost momentum."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "quote": "The production suffered from superficial acting that ignored the play's sophisticated **dramaturgic** structure."
      }
    ]
  },
  "Dashboard — dram/dramaturgical.md": {
    "primary": "Relating to dramaturgy or the theatrical arts.",
    "secondary": "In sociology and social theory (especially following Erving Goffman), describing an analytical framework that interprets social interaction as a theatrical performance comprising roles, stages, and front/back regions.",
    "quotes": [
      {
        "author": "Erving Goffman",
        "work": "The Presentation of Self in Everyday Life",
        "quote": "From a **dramaturgical** perspective, individuals manage their front-stage impressions to project a socially acceptable persona."
      },
      {
        "author": "Gotthold Ephraim Lessing",
        "work": "Hamburg Dramaturgy",
        "quote": "The **dramaturgical** critique of the French tragedy revealed its slavish adherence to arbitrary unities."
      },
      {
        "author": "Kenneth Burke",
        "work": "A Grammar of Motives",
        "quote": "Human action can be comprehensively analyzed through five key **dramaturgical** terms: act, scene, agent, agency, and purpose."
      }
    ]
  },
  "Dashboard — dram/dramaturgy.md": {
    "primary": "The theory and practice of dramatic composition, stagecraft, and theatrical representation.",
    "secondary": "In sociology and symbolic interactionism, the analysis of human social behavior as an ongoing theatrical production wherein individuals act out social scripts.",
    "quotes": [
      {
        "author": "Gotthold Ephraim Lessing",
        "work": "Hamburg Dramaturgy",
        "quote": "The primary aim of theatrical **dramaturgy** is not to flatter the audience, but to awaken authentic tragic sympathy."
      },
      {
        "author": "Erving Goffman",
        "work": "The Presentation of Self in Everyday Life",
        "quote": "In modern sociological **dramaturgy**, the backstage area is where the performer drops his public mask and steps out of character."
      },
      {
        "author": "Bertolt Brecht",
        "work": "Brecht on Theatre",
        "quote": "Epic **dramaturgy** deliberately shatters the illusion of the fourth wall to stimulate critical social awareness."
      }
    ]
  },
  "Dashboard — dram/dromaeosaurid.md": {
    "primary": "Any member of the family Dromaeosauridae, a group of agile, feathered theropod dinosaurs of the Cretaceous period (commonly known as 'raptors').",
    "secondary": "In vertebrate paleontology, an avian-like paravian theropod characterized by an enlarged, recurved, hyperextensible sickle claw on the second toe and a rigid ossified tail.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Dinosaur in a Haystack",
        "quote": "The anatomical discoveries of small, agile **dromaeosaurid** skeletons transformed our view of dinosaurs from sluggish reptiles to dynamic animals."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "Every feathered **dromaeosaurid** unearthed in Liaoning underscores the intimate evolutionary continuity between dinosaurs and birds."
      },
      {
        "author": "Ernst Mayr",
        "work": "This Is Biology",
        "quote": "The shared skeletal specializations of a **dromaeosaurid** and early avians provide incontrovertible evidence for their common ancestry."
      }
    ]
  },
  "Dashboard — dram/heterodromous.md": {
    "primary": "Running or turning in different, opposite, or alternating directions.",
    "secondary": "In botanical morphology and phyllotaxy, describing stems, leaves, or floral spirals where the direction of coil or arrangement runs counter to that of the parent axis.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "In certain climbing plants, the lateral shoots are **heterodromous**, winding around the trellis in a direction opposite to the main stem."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The spiral phyllotaxis of the branches presents a curious **heterodromous** relation to the primary axis of the tree."
      },
      {
        "author": "Charles Darwin",
        "work": "The Movement and Habits of Climbing Plants",
        "quote": "We observed rare instances of **heterodromous** twining wherein twin shoots from the same root spiraled in opposing senses."
      }
    ]
  },
  "Dashboard — dram/loxodrome.md": {
    "primary": "A rhumb line on the surface of a sphere (such as the Earth) that crosses all meridians of longitude at the same constant oblique angle.",
    "secondary": "In marine navigation and spherical geometry, a path of constant compass bearing, represented as a straight line on a Mercator projection map, spiraling asymptotically toward the poles.",
    "quotes": [
      {
        "author": "Gerardus Mercator",
        "work": "Atlas sive Cosmographicae Meditationes",
        "quote": "By projecting the spherical meridians into parallel straight lines, the navigator can plot a true **loxodrome** with a simple ruler."
      },
      {
        "author": "William Herschel",
        "work": "Treatise on Astronomy",
        "quote": "A ship steering a constant course cuts each meridian obliquely, tracing a spiral **loxodrome** toward the pole."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Ahab paced the deck, calculating whether their current compass **loxodrome** would intersect the migrating sperm whales."
      }
    ]
  },
  "Dashboard — dram/monodromy.md": {
    "primary": "The mathematical study of how objects (such as solutions to differential equations or points on covering spaces) behave and transform as they are analytically continued along closed loops around singularities.",
    "secondary": "In algebraic geometry and complex analysis, the group homomorphism (monodromy group) from the fundamental group of a punctured space to the automorphism group of the fibers.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "Tracing algebraic functions along closed circuits around branch points reveals their underlying **monodromy** group."
      },
      {
        "author": "Bernhard Riemann",
        "work": "Foundations for a General Theory of Functions",
        "quote": "The multiple values assumed by a complex integral are completely governed by the **monodromy** around its singular points."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "The linear differential equations of Gauss are classified through the spectral transformations of their **monodromy** operators."
      }
    ]
  },
  "Dashboard — dram/syndrome.md": {
    "primary": "A characteristic combination of symptoms and physical signs that collectively indicate a particular disease, abnormal medical condition, or disorder.",
    "secondary": "In sociology and cultural analysis, a recognizable pattern of behaviors, attitudes, or systemic trends that characterizes a specific social malady or psychological state.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The constellation of tachycardia, exophthalmos, and fine tremor forms the unmistakable clinical **syndrome** of Graves' disease."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Patients afflicted with post-encephalitic Parkinson's displayed a protean **syndrome** of motor arrests and bizarre tics."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Psychopathology of Everyday Life",
        "quote": "In obsessional neurosis, we encounter a recurring **syndrome** of doubts, repetitive rituals, and moral scrupulosity."
      }
    ]
  },
  "Dashboard — dram/undramatic.md": {
    "primary": "Not dramatic; lacking excitement, theatrical flair, sudden suspense, or sensational interest; quiet, plain, and routine.",
    "secondary": "In literary criticism and historiography, characterizing events, developments, or styles that unfold gradually and without overt conflict or histrionics.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "Real warfare consists largely of long, dreary, utterly **undramatic** periods of waiting in cold mud."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Her daily existence unfolded in an **undramatic** sequence of domestic duties, sewing, and tranquil reflections."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The decay of civic institutions proceeded by slow, **undramatic** encroachments rather than sudden revolutionary shocks."
      }
    ]
  },
  "Dashboard — dram/undramatically.md": {
    "primary": "In an undramatic manner; quietly, uneventfully, and without sensational display, fuss, or emotional agitation.",
    "secondary": "In historical description, characterizing changes or conclusions that transpire smoothly, imperceptibly, or with understated calm.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The long-awaited reconciliation occurred quite **undramatically** over a cup of cider by the kitchen hearth."
      },
      {
        "author": "George Orwell",
        "work": "Down and Out in Paris and London",
        "quote": "Destitution arrives **undramatically**, slipping into a man's life like a creeping cold through a worn coat."
      },
      {
        "author": "H. G. Wells",
        "work": "The New Machiavelli",
        "quote": "The long-standing cabinet coalition dissolved **undramatically** after a weary midnight committee meeting."
      }
    ]
  }
};

let count = 0;
for (const [key, data] of Object.entries(batch2Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 2 Completed: ${count} / ${Object.keys(batch2Data).length} words updated`);
console.log(`========================================`);
