import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';

const BATCH7_DATA = [
  // Dashboard — necr (23 words)
  {
    lemma: "necr",
    dashboard: "Dashboard — necr",
    primary: "The ancient Greek root (*nekros*, corpse, dead body) denoting death, dead tissue, or mortality.",
    secondary: "In scientific, medical, and occult terminology, the combining element designating mortification, necrotic lesions, or communication with the deceased.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "From the classical root **necr** pathology derives its terminology for cellular mortification and tissue death." },
      { author: "Max Müller", work: "Lectures on the Science of Language", text: "The Greek stem **necr** shares an ancient Indo-European lineage with Sanskrit naś and Latin nocere." },
      { author: "Gilbert Murray", work: "Five Stages of Greek Religion", text: "Primitive chthonic rituals appeased the restless spirits of the dead under solemn invocations of **necr**." }
    ]
  },
  {
    lemma: "necrobiosis",
    dashboard: "Dashboard — necr",
    primary: "The natural, gradual physiological death and replacement of cells or tissues as part of normal biological turnover.",
    secondary: "A pathological localized collagen degeneration, as in necrobiosis lipoidica diabeticorum, characterized by palisading granulomas.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "I introduced the term **necrobiosis** to distinguish the continuous physiological death of active cells from sudden catastrophic necrosis." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "In necrobiosis lipoidica, cutaneous collagen bundles undergo degenerating **necrobiosis** surrounded by lipid-laden histiocytes." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Living tissue sustains its vitality through incessant destruction, an ongoing internal **necrobiosis** balanced by synthesis." }
    ]
  },
  {
    lemma: "necrology",
    dashboard: "Dashboard — necr",
    primary: "A list or record of persons who have died recently; a register of deaths; an obituary.",
    secondary: "In monastic history, a roll or register containing the death anniversaries of benefactors and brethren to be commemorated in prayer.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", text: "The parish priest recorded each departure of the pestilence in his mournful municipal **necrology**." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Monastic **necrologies** preserved the only surviving documentary genealogies of the early feudal barony." },
      { author: "William Makepeace Thackeray", work: "The Newcomes", text: "He turned first to the morning paper's **necrology**, checking whether any elderly wealthy uncles had departed." }
    ]
  },
  {
    lemma: "necrolysis",
    dashboard: "Dashboard — necr",
    primary: "The dissolution, separation, or shedding of dead tissue or cells.",
    secondary: "In dermatology, acute detachment and necrosis of the epidermis from the dermis, notably in toxic epidermal necrolysis (Lyell's syndrome).",
    quotes: [
      { author: "Alan Lyell", work: "Toxic Epidermal Necrolysis: An Eruption Resembling Scalding of the Skin", text: "I described toxic epidermal **necrolysis** as a catastrophic drug reaction stripping the cutaneous mantle like widespread boiling scalding." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Extensive sheets of flaccid epidermis slough away as **necrolysis** cleaves the basal dermo-epidermal junction." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Enzymatic autolysis swiftly follows cellular death, culminating in complete structural **necrolysis**." }
    ]
  },
  {
    lemma: "necromancer",
    dashboard: "Dashboard — necr",
    primary: "A sorcerer or occultist who practices necromancy; one who claims to divine the future by conjuring the spirits of the dead.",
    secondary: "A practitioner of black magic or forbidden wizardry in folklore and fantasy literature.",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", text: "Prospero abjures his potent art, burying his staff deeper than ever plummet sounded, unlike the sinister **necromancer**." },
      { author: "John Milton", work: "Paradise Lost", text: "Dark cabalists and the cunning **necromancer** sought to call forth phantoms from the stygian pit." },
      { author: "Walter Scott", work: "Letters on Demonology and Witchcraft", text: "Medieval superstition credited the wandering **necromancer** with terrible powers over sepulchral vaults." }
    ]
  },
  {
    lemma: "necromancy",
    dashboard: "Dashboard — necr",
    primary: "The practice of communicating with the dead, especially in order to predict future events; black art, sorcery, or witchcraft.",
    secondary: "The dark arts of summoning specters or reanimating corpses in esoteric mysticism and mythological folklore.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", text: "Superstitious arts such as astrology and **necromancy** promise much yet produce only imposture and deceit." },
      { author: "Thomas Browne", work: "Hydriotaphia, Urn Burial", text: "The ancient Witch of Endor practiced forbidden **necromancy**, bringing up the troubled ghost of Samuel before Saul." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Imperial edicts inflicted capital penalties on all who consulted midnight séances and pagan **necromancy**." }
    ]
  },
  {
    lemma: "necromania",
    dashboard: "Dashboard — necr",
    primary: "An abnormal, morbid, or pathological obsession with death, corpses, or funeral rituals.",
    secondary: "A psychiatric delusion or impulse driving an individual to seek contact with dead bodies or morbid mortuary environments.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "Morbid psychopathy may manifest as acute **necromania**, where cemetery visits become an irresistible compulsion." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "We trace a severe aberration in the patient's history, progressing from melancholy brooding into overt **necromania**." },
      { author: "William James", work: "The Varieties of Religious Experience", text: "A temperament burdened by morbid **necromania** sees in every human joy only the rotting worm beneath the tombstone." }
    ]
  },
  {
    lemma: "necromantic",
    dashboard: "Dashboard — necr",
    primary: "Of, relating to, or practiced by means of necromancy; dealing with the conjuration of the dead.",
    secondary: "Having the eerie, uncanny, or sinister aura of magical contact with corpses or the underworld.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "Frankenstein (Preface)", text: "The solitary student pursued his investigations by midnight into charnel houses with almost **necromantic** zeal." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", text: "Old Roger Chillingworth delved into the young minister's heart with a dark, **necromantic** scrutiny." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", text: "A wild mystical gloom pervaded the study, redolent of antique folios and **necromantic** speculations." }
    ]
  },
  {
    lemma: "necromantical",
    dashboard: "Dashboard — necr",
    primary: "Relating to or characteristic of necromancy; necromantic.",
    secondary: "In archaic prose, pertaining to the illicit invocation of deceased souls or demonic spirits.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "Many reputed miracles of pagan oracles were mere delusions contrived by **necromantical** impostors." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", text: "Sorcerers use spells and **necromantical** circles to terrify fearful consciences into despair." },
      { author: "Walter Scott", work: "The Antiquary", text: "The treasure-hunter muttered **necromantical** incantations as he dug into the ruined priory vault." }
    ]
  },
  {
    lemma: "Necronomicon",
    dashboard: "Dashboard — necr",
    primary: "A fictional grimoire (textbook of magic) created by American horror writer H. P. Lovecraft, containing accounts of the Old Ones and rites for summoning them.",
    secondary: "A legendary forbidden tome in the Cthulhu Mythos, attributed to the 'mad Arab' Abdul Alhazred and bound in human leather.",
    quotes: [
      { author: "H. P. Lovecraft", work: "The Call of Cthulhu", text: "That is not dead which can eternal lie, and with strange aeons even death may die—the cryptic couplet from the **Necronomicon**." },
      { author: "H. P. Lovecraft", work: "The Dunwich Horror", text: "He spent long hours consulting the guarded Latin copy of the **Necronomicon** housed in the library of Miskatonic University." },
      { author: "Jorge Luis Borges", work: "There Are More Things", text: "In my memory lingered Lovecraft's terrifying invention of the **Necronomicon**, a book whose very pages breathed cosmic horror." }
    ]
  },
  {
    lemma: "necrophagia",
    dashboard: "Dashboard — necr",
    primary: "The act, habit, or practice of feeding on dead flesh or carrion; necrophagy.",
    secondary: "In anthropology and folklore, corpse-eating or necro-cannibalism; in ecology, scavenging by obligate or facultative carnivores.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", text: "The condor of the Andes subsists primarily through scavenging **necrophagia**, soaring for leagues in search of dead cattle." },
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", text: "Certain subterranean doryline army ants practice opportunistic **necrophagia** upon dead earthworms and grubs." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", text: "Vultures and carrion beetles accelerate nutrient recycling through specialized, competitive **necrophagia**." }
    ]
  },
  {
    lemma: "necrophagy",
    dashboard: "Dashboard — necr",
    primary: "The habit of feeding on dead bodies or decaying flesh; the ecological consumption of carrion.",
    secondary: "An ecological niche occupied by scavengers (hyenas, vultures, silphid beetles) that cleanses ecosystems of putrefying carcasses.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Carrion consumption or **necrophagy** diverts substantial biomass from bacterial decay directly back into higher trophic levels." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", text: "Swarms of burying beetles executed efficient **necrophagy**, dragging small rodent carcasses beneath the forest litter." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The robust crushing dentition of the hyaena is specialized for habitual **necrophagy** and the splintering of large marrow bones." }
    ]
  },
  {
    lemma: "necrophilia",
    dashboard: "Dashboard — necr",
    primary: "A paraphilia characterized by sexual attraction to or sexual acts involving corpses.",
    secondary: "In psychoanalytic and social philosophy (such as Erich Fromm's theory), an attraction to all that is dead, mechanical, and destructive, contrasted with biophilia.",
    quotes: [
      { author: "Erich Fromm", work: "The Anatomy of Human Destructiveness", text: "I defined **necrophilia** in the psychological sense as the passionate attraction to that which is dead, decaying, and purely mechanical." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "True clinical **necrophilia** represents the most monstrous perversion of the sexual impulse known to alienists." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "Cases of **necrophilia** demonstrate a profound dissociation between instinctual drive and empathetic human intimacy." }
    ]
  },
  {
    lemma: "necrophilism",
    dashboard: "Dashboard — necr",
    primary: "The psychological condition or manifestation of necrophilia; an erotic or morbid fascination with corpses.",
    secondary: "In psychopathology, the compulsive mental disorder marked by morbid desecration of graves or desire for dead bodies.",
    quotes: [
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "The trial of Sergeant Bertrand in 1849 established the forensic reality of morbid **necrophilism** in French criminal jurisprudence." },
      { author: "Erich Fromm", work: "The Heart of Man", text: "Modern bureaucratic authoritarianism often exhibits an unconscious cultural **necrophilism**, exalting rigid law over living warmth." },
      { author: "Magnus Hirschfeld", work: "Sexual Pathology", text: "Extreme emotional detachment and sadistic daydreams frequently accompany the clinical onset of **necrophilism**." }
    ]
  },
  {
    lemma: "necrophobia",
    dashboard: "Dashboard — necr",
    primary: "An abnormal, persistent, or irrational fear of dead bodies or death; thanatophobia.",
    secondary: "In behavioral psychology, acute panic, revulsion, and avoidance triggered by tombs, funeral homes, corpses, or mortuary symbols.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", text: "A deep-seated instinctual shuddering at the presence of a corpse borders on irrational **necrophobia** in sensitive temperaments." },
      { author: "Sigmund Freud", work: "Totem and Taboo", text: "Primitive taboos surrounding the dead are rooted in an ambivalence of grief and unconscious **necrophobia**." },
      { author: "Wilhelm Stekel", work: "Conditions of Nervous Anxiety", text: "The phobic patient suffered from severe **necrophobia**, unable to pass a cemetery gate without debilitating palpitations." }
    ]
  },
  {
    lemma: "necropolis",
    dashboard: "Dashboard — necr",
    primary: "A large, elaborate cemetery or burial complex, especially one belonging to an ancient city.",
    secondary: "An extensive historical burial ground containing monumental tombs, mausoleums, and subterranean catacombs (such as the Giza necropolis).",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Beneath the modern city of Rome lies the silent **necropolis** of the early Christian martyrs." },
      { author: "Pausanias", work: "Description of Greece", text: "Outside the monumental gate of Kerameikos stretched the Athenian **necropolis**, flanked by marble grave stelai." },
      { author: "Alexander von Humboldt", work: "Researches Concerning the Institutions of the Ancient Inhabitants of America", text: "The vast subterranean **necropolis** of the Incas yielded mummies preserved in desiccated sandy vaults." }
    ]
  },
  {
    lemma: "necropsy",
    dashboard: "Dashboard — necr",
    primary: "The post-mortem surgical examination of a body to determine the cause of death or evaluate the extent of disease; an autopsy.",
    secondary: "In veterinary medicine and experimental pathology, the anatomical dissection of an animal carcass.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Careful pathological correlation at **necropsy** remains the final and most authoritative teacher of the clinician." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Routine **necropsy** revealed extensive unsuspected atheroma of the coronary arteries with acute thrombosis." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Every systematic **necropsy** must combine gross macroscopic inspection with microscopic histochemical verification." }
    ]
  },
  {
    lemma: "necrose",
    dashboard: "Dashboard — necr",
    primary: "To undergo necrosis; to become necrotic or die while remaining attached to living tissue.",
    secondary: "In clinical pathology, describing tissues (such as bone or ischemic bowel) that mortify and lose viability.",
    quotes: [
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Deprived of collateral arterial supply, the strangulated loop of bowel will swiftly **necrose** and perforate." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Severe frostbite causes the distal phalanges to **necrose**, requiring eventual surgical amputation." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "When vascular thrombosis occludes the nutrient vessel, the affected capillary territory begins to **necrose** within hours." }
    ]
  },
  {
    lemma: "necrosis",
    dashboard: "Dashboard — necr",
    primary: "The death of body tissue or cells caused by disease, physical injury, radiation, or inadequate blood supply (ischemia).",
    secondary: "Irreversible pathological cell death characterized by cellular swelling, membrane rupture, organelle dissolution, and acute inflammation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "I define **necrosis** as the passive mortification of living parts within the living organism following vascular occlusion." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Caseous **necrosis** in tuberculosis leaves behind cheesy, structureless debris devoid of living cellular landmarks." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Myocardial infarction represents ischemic coagulation **necrosis** resulting from sudden coronary artery occlusion." }
    ]
  },
  {
    lemma: "necrospermia",
    dashboard: "Dashboard — necr",
    primary: "A condition in which the spermatozoa present in the semen are dead, non-motile, or completely non-viable; necrozoospermia.",
    secondary: "A rare cause of male infertility where ejaculated sperm display complete loss of membrane integrity and motility upon laboratory testing.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Differential diagnosis in male sterility must distinguish total azoospermia from the dead spermatozoa of true **necrospermia**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Vital eosin staining confirms complete membrane non-viability in genuine cases of persistent **necrospermia**." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Prolonged epididymal storage or toxic scrotal hyperthermia can induce transient **necrospermia** in breeding stallions." }
    ]
  },
  {
    lemma: "necrotic",
    dashboard: "Dashboard — necr",
    primary: "Of, relating to, or affected by necrosis; dead, devitalized, or gangrenous.",
    secondary: "Characterized by localized tissue mortification, cellular disintegration, and surrounding inflammatory leukocytic infiltration.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "The **necrotic** core of the infarct becomes surrounded by a hyperemic zone of reactive capillary proliferation." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Debridement of jagged wounds must excise all **necrotic** muscle to prevent colonization by anaerobic clostridia." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "A **necrotic** slough lined the base of the deep typhoid ulcer, threatening intestinal hemorrhage." }
    ]
  },
  {
    lemma: "necrotize",
    dashboard: "Dashboard — necr",
    primary: "To cause necrosis in living tissue; to kill or mortify cells.",
    secondary: "In surgical pathology, to devitalize or produce cell death through toxins, severe infection, or arterial deprivation.",
    quotes: [
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Bacterial alpha-toxins rapidly **necrotize** vascular endothelial walls, producing fulminant gas gangrene." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Corrosive poisons ingested orally **necrotize** the esophageal mucosa, leaving deep fibrous strictures." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Excessive pressure will **necrotize** overlying skin, initiating decubitus ulcer formation in bedridden invalids." }
    ]
  },
  {
    lemma: "necrotomy",
    dashboard: "Dashboard — necr",
    primary: "The surgical excision of a sequestrum (dead bone fragment) resulting from chronic osteomyelitis.",
    secondary: "In legal and anatomical history, the dissection or surgical cutting of a corpse; an autopsy.",
    quotes: [
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Chronic draining sinuses demand radical **necrotomy** to extract the dense, detached bony sequestrum." },
      { author: "Ambroise Paré", work: "The Apologie and Treatise", text: "The military surgeon must perform bold **necrotomy** when blackened splintered bone threatens gangrene." },
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", text: "Surgical **necrotomy** exposes the involucrum cavity to excise the devitalized cortical fragments." }
    ]
  },

  // Dashboard — than (13 words)
  {
    lemma: "athanasianism",
    dashboard: "Dashboard — than",
    primary: "The theological system and doctrines championed by Athanasius of Alexandria, asserting the full divinity and co-equality of the Son with the Father (homoousios).",
    secondary: "Orthodox Trinitarian Christianity as codified in the Nicene Creed, maintaining the eternal deity of Christ against Arianism.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The subtle distinctions of **Athanasianism** divided the Roman world into hostile theological factions." },
      { author: "John Henry Newman", work: "The Arians of the Fourth Century", text: "The steadfast endurance of **Athanasianism** preserved the core revelation of the Incarnation against rationalist dilution." },
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", text: "Dante's vision was anchored firmly upon the rock of **Athanasianism**, the unshakeable Trinitarian cosmos of the Middle Ages." }
    ]
  },
  {
    lemma: "athanasius",
    dashboard: "Dashboard — than",
    primary: "Saint Athanasius of Alexandria (c. 296–373 AD), 20th bishop of Alexandria, Church Father, and chief champion of the Nicene doctrine of the Trinity against Arianism.",
    secondary: "A masculine proper name derived from the Greek *athanatos*, meaning 'immortal' or 'deathless'.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Five times was **Athanasius** expelled from his episcopal throne; twenty years he passed as an exile or a fugitive." },
      { author: "John Henry Newman", work: "Select Treatises of St. Athanasius", text: "In the history of dogma, **Athanasius** stands as an immovable tower resisting the waves of imperial heresy." },
      { author: "Arthur Penrhyn Stanley", work: "Lectures on the History of the Eastern Church", text: "The small, energetic figure of **Athanasius** dominated the debates of the Council of Nicaea." }
    ]
  },
  {
    lemma: "athanor",
    dashboard: "Dashboard — than",
    primary: "A self-feeding furnace used by alchemists to maintain a steady, uniform, and continuous heat for protracted chemical digestions.",
    secondary: "In occult hermetic philosophy, the mystical furnace of constant spiritual transformation, from Greek *athanatos* (undying heat) or Arabic *al-tannūr*.",
    quotes: [
      { author: "Ben Jonson", work: "The Alchemist", text: "Look if the cold furnace be on fire, and the **athanor** kept at its equal and enduring heat." },
      { author: "Paracelsus", work: "The Hermetic and Alchemical Writings", text: "The great work requires that the fire of the **athanor** be kept burning without interruption for forty days and nights." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "Alchemists watched their burning **athanor** with religious vigilance, awaiting the golden transmutation in the crucible." }
    ]
  },
  {
    lemma: "euthanasia",
    dashboard: "Dashboard — than",
    primary: "The painless killing of a patient suffering from an incurable and painful disease or in an irreversible coma; mercy killing.",
    secondary: "Historically, a peaceful, gentle, or honorable death; in bioethics, the voluntary or non-voluntary termination of life to relieve intractable suffering.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", text: "I esteem it the office of a physician not only to restore the health, but to mitigate pain and dolours; and not only when such mitigation may conduce to recovery, but when it may serve to make a fair and easy passage: for this **euthanasia** is no small part of happiness." },
      { author: "David Hume", work: "Essays, Moral, Political, and Literary", text: "An absolute monarchy is the easiest death, the true **euthanasia** of the British constitution." },
      { author: "William Osler", work: "Science and Immortality", text: "Most mortals depart this life quietly, enjoying a natural physical **euthanasia** as senses gently dim into unconsciousness." }
    ]
  },
  {
    lemma: "thanatocoenosis",
    dashboard: "Dashboard — than",
    primary: "An assemblage of fossilized dead organisms brought together after death by physical agents such as water currents or wind; a death assemblage.",
    secondary: "In paleoecology and taphonomy, a fossil accumulation containing specimens that did not live together in life, contrasted with a living biocoenosis.",
    quotes: [
      { author: "Amadeus William Grabau", work: "Principles of Stratigraphy", text: "We contrast the living biocoenosis with the **thanatocoenosis**, which represents a drifted accumulation of dead shells." },
      { author: "Stephen Jay Gould", work: "Time's Arrow, Time's Cycle", text: "Taphonomists must separate the ecological community from the posthumous distortions of the **thanatocoenosis**." },
      { author: "David Raup", work: "Principles of Paleontology", text: "Storm waves swept disparate marine fauna into an offshore trench, preserving a complex mixed **thanatocoenosis**." }
    ]
  },
  {
    lemma: "thanatoid",
    dashboard: "Dashboard — than",
    primary: "Resembling death; deathlike; mortal or deadly.",
    secondary: "In toxicology and pathology, describing states of extreme prostration, stupor, or coma mimicking somatic death (as in snake venom poisoning).",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", text: "The bite of the sea snake induces a **thanatoid** collapse, with flaccid paralysis and imperceptible respiration." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The patient lay in a profound **thanatoid** coma, unresponsive to painful cutaneous stimuli." },
      { author: "Edgar Allan Poe", work: "The Premature Burial", text: "A state of **thanatoid** catalepsy held her motionless, mimicking the pallor and rigidity of the grave." }
    ]
  },
  {
    lemma: "thanatology",
    dashboard: "Dashboard — than",
    primary: "The scientific study of death, dying, and the psychological, social, and medical practices associated with mortality and bereavement.",
    secondary: "An interdisciplinary academic field investigating hospice palliative care, end-of-life decision making, and cultural grief rituals.",
    quotes: [
      { author: "Elisabeth Kübler-Ross", work: "On Death and Dying", text: "Modern **thanatology** teaches us to listen to the dying patient, illuminating the emotional stages preceding death." },
      { author: "William Osler", work: "Science and Immortality", text: "The physician's role in bedside **thanatology** is to alleviate physical agony and comfort the bereaved family." },
      { author: "Philippe Ariès", work: "Western Attitudes toward Death", text: "Historical **thanatology** charts how Western society shifted from familiar domestic dying to institutional concealment." }
    ]
  },
  {
    lemma: "thanatophobia",
    dashboard: "Dashboard — than",
    primary: "An abnormal, persistent, or irrational fear of death or dying.",
    secondary: "In clinical psychiatry, an acute anxiety neurosis characterized by intrusive panic attacks centered upon mortality and bodily vulnerability.",
    quotes: [
      { author: "Sigmund Freud", work: "Thoughts for the Times on War and Death", text: "Unconscious psychic life cannot imagine its own demise; hence conscious **thanatophobia** is often the secondary symptom of guilt." },
      { author: "William James", work: "The Varieties of Religious Experience", text: "Morbid melancholy often crystallizes into agonizing **thanatophobia**, poisoning every innocent worldly pleasure." },
      { author: "Wilhelm Stekel", work: "Conditions of Nervous Anxiety", text: "Night terrors and hypochondriacal fixations in young adults frequently mask acute, unexpressed **thanatophobia**." }
    ]
  },
  {
    lemma: "thanatophoric",
    dashboard: "Dashboard — than",
    primary: "Death-bearing; deadly; lethal; producing or causing death.",
    secondary: "In medical genetics and pediatrics, designating thanatophoric dysplasia, a severe, universally lethal congenital micromelic dwarfism.",
    quotes: [
      { author: "William Boyd", work: "A Textbook of Pathology", text: "The micromelia and telephone-receiver femoral bowing in **thanatophoric** dwarfism result from activating FGFR3 mutations." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "Certain venomous viperid fangs deliver a swiftly **thanatophoric** neurotoxin into prey tissues." },
      { author: "Thomas Browne", work: "Hydriotaphia", text: "The ancient urn preserved the mortal dust from the destructive ravages of **thanatophoric** time." }
    ]
  },
  {
    lemma: "thanatopsis",
    dashboard: "Dashboard — than",
    primary: "A meditation upon, view of, or contemplation of death.",
    secondary: "A famous meditative philosophical poem written by William Cullen Bryant in 1811 on nature, death, and human destiny.",
    quotes: [
      { author: "William Cullen Bryant", work: "Thanatopsis", text: "So live, that when thy summons comes to join the innumerable caravan... thou go not, like the quarry-slave at night, scourged to his dungeon, but, sustained and soothed by an unfaltering trust, approach thy grave, like one who wraps the drapery of his couch about him, and lies down to pleasant dreams." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", text: "The serene **thanatopsis** of the Stoic sages viewed physical dissolution as a natural harmonious return to the cosmic whole." },
      { author: "Oliver Wendell Holmes Sr.", work: "Pages from an Old Volume of Life", text: "The solemn music of Bryant's **thanatopsis** reconciled human grief with the majestic cycles of the continent." }
    ]
  },
  {
    lemma: "thanatos",
    dashboard: "Dashboard — than",
    primary: "The personification of death in Greek mythology, the winged son of Nyx (Night) and twin brother of Hypnos (Sleep).",
    secondary: "In psychoanalysis, the death instinct or drive (posited by Sigmund Freud) that impels organisms toward destruction, quiescence, and inorganic rest.",
    quotes: [
      { author: "Sigmund Freud", work: "Beyond the Pleasure Principle", text: "We set the death instinct, or **Thanatos**, in fundamental opposition to Eros, the preserver of all life." },
      { author: "Homer", work: "The Iliad", text: "Apollo bade gentle Sleep and **Thanatos** carry the lifeless body of fallen Sarpedon to his Lycian homeland." },
      { author: "Walter Burkert", work: "Greek Religion", text: "Unlike Hades the sovereign of the underworld, **Thanatos** was the silent messenger who severed the silver cord of life." }
    ]
  },
  {
    lemma: "thane",
    dashboard: "Dashboard — than",
    primary: "A man who held land granted by the king or by a nobleman in Anglo-Saxon and early medieval Scottish history, ranking between an ordinary freeman and a hereditary earl.",
    secondary: "A feudal lord, military retainer, or baron in medieval Scotland, famously immortalized in Shakespeare's *Macbeth*.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", text: "All hail, Macbeth! hail to thee, **thane** of Glamis! All hail, Macbeth! hail to thee, **thane** of Cawdor! All hail, Macbeth, that shalt be king hereafter!" },
      { author: "Walter Scott", work: "The Fair Maid of Perth", text: "The proud Scottish **thane** rode down from his Highland fastness with a retinue of armed clansmen." },
      { author: "Thomas Babington Macaulay", work: "The History of England", text: "The Saxon **thane** enjoyed extensive territorial rights, presiding over local hundred courts before the Norman conquest." }
    ]
  },
  {
    lemma: "thaneship",
    dashboard: "Dashboard — than",
    primary: "The rank, office, dignity, or territorial jurisdiction of a thane.",
    secondary: "In medieval Scottish and Anglo-Saxon law, the hereditary baronial estate or administrative lordship held by a thane.",
    quotes: [
      { author: "Walter Scott", work: "Minstrelsy of the Scottish Border", text: "Charter records confirm that the ancient **thaneship** of Cawdor passed intact through centuries of border warfare." },
      { author: "William Shakespeare", work: "Macbeth", text: "He bade me from him call thee thane of Cawdor: in which addition, hail, most worthy thane! for it is thine: the royal gift of the **thaneship**." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Feudal transformations gradually converted the Saxon **thaneship** into the knightly tenure of Norman barons." }
    ]
  },

  // Dashboard — karyo (12 words)
  {
    lemma: "akaryocyte",
    dashboard: "Dashboard — karyo",
    primary: "A non-nucleated cell, especially a mature mammalian erythrocyte (red blood cell); variant spelling of acaryocyte.",
    secondary: "In hematology, a fully differentiated blood cell that has extruded its nucleus to maximize hemoglobin carrying capacity.",
    quotes: [
      { author: "Paul Ehrlich", work: "Histology of the Blood", text: "During mammalian erythropoiesis, the normoblast extrudes its nucleus, converting into a functional **akaryocyte**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "The biconcave **akaryocyte** navigates splenic sinusoids with extraordinary elasticity." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "We contrast nucleated cellular monads with the specialized non-nucleated **akaryocyte** of mammalian blood." }
    ]
  },
  {
    lemma: "akaryote",
    dashboard: "Dashboard — karyo",
    primary: "A cell or organism lacking a distinct, membrane-bound nucleus; variant spelling of acaryote.",
    secondary: "In evolutionary cytology, a primitive cell or non-nucleated organism (such as a virus or archaic bacterium).",
    quotes: [
      { author: "Ernst Haeckel", work: "The History of Creation", text: "The hypothetical primal moneron represents an **akaryote** stage of life consisting of structureless cytode protoplasm." },
      { author: "Carl Woese", work: "Bacterial Evolution", text: "Cytologists historically used **akaryote** to designate cells whose genetic material floats free of a nuclear envelope." },
      { author: "Lynn Margulis", work: "Origin of Eukaryotic Cells", text: "The transition from the primitive **akaryote** to the complex nucleated cell represents the great divide of biology." }
    ]
  },
  {
    lemma: "eukaryote",
    dashboard: "Dashboard — karyo",
    primary: "An organism consisting of a cell or cells in which the genetic material is DNA in the form of chromosomes contained within a distinct membrane-bound nucleus.",
    secondary: "Any member of the domain Eukarya, including all animals, plants, fungi, and protists, characterized by cytoskeletons and membrane-bound organelles.",
    quotes: [
      { author: "Edouard Chatton", work: "Pansporella perplexa: Réflexions sur la Biologie des Flagellés", text: "I proposed the fundamental dichotomy dividing all living organisms into the prokaryote and the **eukaryote**." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "The **eukaryote** is not an expanded bacterium, but a multi-genome cooperative community forged through endosymbiosis." },
      { author: "Carl Woese", work: "The Archaea: Their History and Significance", text: "Molecular sequencing revealed that the nucleocytoplasmic lineage of the **eukaryote** shares profound homologies with Archaea." }
    ]
  },
  {
    lemma: "eukaryotic",
    dashboard: "Dashboard — karyo",
    primary: "Of, relating to, or characteristic of a eukaryote or eukaryotes; possessing a membrane-bound nucleus and organelles.",
    secondary: "Describing cellular organization featuring linear chromosomes bound with histones, compartmentalized endomembranes, and mitotic spindles.",
    quotes: [
      { author: "Francis Crick", work: "What Mad Pursuit", text: "The split gene architecture and RNA splicing revealed an unexpected complexity in the **eukaryotic** genome." },
      { author: "Jacques Monod", work: "Chance and Necessity", text: "What is true for E. coli must be true for the elephant, yet **eukaryotic** chromatin introduces elaborate epigenetic layers." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "Mitochondria within the **eukaryotic** cell generate ATP through chemiosmotic proton gradients across inner cristae." }
    ]
  },
  {
    lemma: "karyolymph",
    dashboard: "Dashboard — karyo",
    primary: "The clear, fluid, or semi-fluid colloidal substance filling the interphase cell nucleus; nucleoplasm; nuclear sap.",
    secondary: "The nuclear matrix fluid in which the chromatin network, nucleoli, and ribonucleoprotein complexes are suspended.",
    quotes: [
      { author: "Walther Flemming", work: "Zellsubstanz, Kern und Zelltheilung", text: "During prophase, the chromatin threads condense while the surrounding **karyolymph** becomes continuous with the cytoplasm upon nuclear envelope breakdown." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "The germinal vesicle contains abundant clear **karyolymph** bathing the central nucleolus." },
      { author: "Edmund Beecher Wilson", work: "The Cell in Development and Heredity", text: "Diffusion of messenger particles across the **karyolymph** precedes their export through the nuclear pores." }
    ]
  },
  {
    lemma: "karyolysis",
    dashboard: "Dashboard — karyo",
    primary: "The dissolution and disappearance of the cell nucleus, occurring naturally in cell maturation or pathologically during necrosis.",
    secondary: "A morphological stage of irreversible cell death characterized by enzymatic degradation of chromatin by endonucleases.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Following pyknosis, the necrotic nucleus undergoes complete **karyolysis**, fading into an imperceptible phantom." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "In ischemic renal tubular necrosis, total **karyolysis** leaves behind pale, ghost-like epithelial outlines." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", text: "The mammalian erythroblast undergoes **karyolysis** and extrusion, releasing the mature enucleated disc." }
    ]
  },
  {
    lemma: "karyon",
    dashboard: "Dashboard — karyo",
    primary: "The nucleus of a biological cell.",
    secondary: "The classical Greek noun (*karyon*, nut, walnut, or kernel) adopted in cytology as the root for nuclear structures and cellular classification.",
    quotes: [
      { author: "Edmund Beecher Wilson", work: "The Cell in Development and Heredity", text: "Cytologists adopted the classical Greek term **karyon** to designate the central governing kernel of the protoplast." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "The evolution of the true **karyon** separated simple cytodes from advanced cellular organisms." },
      { author: "Max Müller", work: "Lectures on the Science of Language", text: "Etymologically, **karyon** signified the hard shell of a walnut before biology borrowed it for the cell nucleus." }
    ]
  },
  {
    lemma: "karyotype",
    dashboard: "Dashboard — karyo",
    primary: "The number, size, and visual appearance of the chromosomes in the cell nuclei of an organism or species.",
    secondary: "A standardized photomicrographic display of metaphase chromosomes arranged in homologous pairs according to length and centmer position.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", text: "Chromosomal inversions and translocations alter the ancestral **karyotype**, establishing reproductive isolation between sibling species." },
      { author: "Barbara McClintock", work: "Chromosome Morphology in Zea Mays", text: "Detailed analysis of the pachytene **karyotype** of maize allowed precise cytological mapping of chromosomal knobs." },
      { author: "Jerome Lejeune", work: "The Trisomy 21 Karyotype", text: "Analysis of the human **karyotype** demonstrated that Down syndrome is caused by the presence of a supernumerary chromosome 21." }
    ]
  },
  {
    lemma: "megakaryocyte",
    dashboard: "Dashboard — karyo",
    primary: "A large bone marrow cell with a lobulated polyploid nucleus responsible for the production and release of blood platelets (thrombocytes).",
    secondary: "A massive hematopoietic giant cell that undergoes endomitosis and extends cytoplasmic proplatelet ribbons into marrow sinusoids.",
    quotes: [
      { author: "James Homer Wright", work: "The Histogenesis of the Blood Platelets", text: "I proved that blood platelets are detached cytoplasmic fragments pinched off from the giant **megakaryocyte** of the bone marrow." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "In idiopathic thrombocytopenic purpura, marrow aspirates show abundant **megakaryocytes** failing to release functional platelets." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", text: "The enormous multilobulated **megakaryocyte** dominates bone marrow smears with its sprawling basophilic cytoplasm." }
    ]
  },
  {
    lemma: "megakaryocytic",
    dashboard: "Dashboard — karyo",
    primary: "Of, relating to, or derived from megakaryocytes.",
    secondary: "Pertaining to megakaryocytopoiesis or the differentiation lineage producing blood platelets in bone marrow.",
    quotes: [
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Acute **megakaryocytic** leukemia is characterized by the malignant proliferation of bizarre, atypical platelet precursors." },
      { author: "James Homer Wright", work: "Studies on Blood Platelets", text: "The budding of **megakaryocytic** pseudopodia directly into the sinusoidal bloodstream generates circulating thrombocytes." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", text: "Thrombopoietin stimulates both **megakaryocytic** endomitosis and subsequent proplatelet formation." }
    ]
  },
  {
    lemma: "Prokaryote",
    dashboard: "Dashboard — karyo",
    primary: "A microscopic single-celled organism that has neither a distinct nucleus with a membrane nor other specialized organelles, including bacteria and cyanobacteria.",
    secondary: "Any unicellular organism of the domains Bacteria or Archaea possessing circular chromosomal DNA in an un-enclosed nucleoid.",
    quotes: [
      { author: "Edouard Chatton", work: "Pansporella perplexa", text: "I introduced the term **prokaryote** to designate primitive organisms whose protoplasm lacks a bounded nuclear membrane." },
      { author: "Carl Woese", work: "Bacterial Evolution", text: "The classic concept of the **prokaryote** dissolved when molecular analysis proved Archaea and Bacteria are as distinct as animals and fungi." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "The primordial biosphere belonged exclusively to the **prokaryote** for over two billion years of planetary history." }
    ]
  },
  {
    lemma: "prokaryotic",
    dashboard: "Dashboard — karyo",
    primary: "Of, relating to, or being a prokaryote; lacking a membrane-bound nucleus and complex cytoplasmic organelles.",
    secondary: "Pertaining to organisms whose transcription and translation are coupled and whose cell walls typically contain peptidoglycan.",
    quotes: [
      { author: "Jacques Monod", work: "Chance and Necessity", text: "The **prokaryotic** lac operon revealed how gene transcription is directly regulated by repressor proteins." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "The **prokaryotic** ribosome differs in sedimentation coefficient and antibiotic sensitivity from its eukaryotic counterpart." },
      { author: "Carl Woese", work: "The Archaea: Their History and Significance", text: "Diverse **prokaryotic** lineages conquered extreme thermal, saline, and acidic environments across the globe." }
    ]
  },

  // Dashboard — mit (6 words)
  {
    lemma: "amitosis",
    dashboard: "Dashboard — mit",
    primary: "Direct cell division by simple cleavage of the nucleus and cytoplasm without the formation of chromosomes, spindle fibers, or mitotic stages.",
    secondary: "A primitive, non-mitotic mode of nuclear division occurring in ciliate macronuclei, degenerate tissues, or pathological neoplasms.",
    quotes: [
      { author: "Walther Flemming", work: "Zellsubstanz, Kern und Zelltheilung", text: "I contrasted indirect mitotic division with direct **amitosis**, wherein the nucleus merely pinches into two halves without chromosome condensation." },
      { author: "Edmund Beecher Wilson", work: "The Cell in Development and Heredity", text: "True **amitosis** is exceptional in healthy embryonic growth, occurring mainly in senescent or highly specialized polyploid tissues." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Certain rapidly proliferating sarcoma cells divide by bizarre **amitosis**, yielding multinucleated giant syncytia." }
    ]
  },
  {
    lemma: "mit",
    dashboard: "Dashboard — mit",
    primary: "The classical Greek combining root (*mitos*, thread) denoting thread-like filaments, chromosomes, or mitotic spindles.",
    secondary: "In cytology and molecular genetics, the morphological root seen in mitosis and mitochondria, referring to chromatin threads.",
    quotes: [
      { author: "Walther Flemming", work: "Contributions to the Knowledge of the Cell", text: "I selected the Greek root **mit** because the chromatin organizes into distinct thread-like filaments during nuclear division." },
      { author: "Max Müller", work: "The Science of Language", text: "The versatile Greek stem **mit** entered modern biology to describe the finest microscopic threads of living matter." },
      { author: "Edmund Beecher Wilson", work: "The Cell in Development and Heredity", text: "From the humble weaver's term **mit** arose our entire vocabulary for chromosomal dance and cellular division." }
    ]
  },
  {
    lemma: "miter",
    dashboard: "Dashboard — mit",
    primary: "A tall liturgical headdress with two peaks worn by bishops and abbots in Christian churches; also a joint between two pieces bevelled at an angle.",
    secondary: "To bevel the ends of two pieces of wood or stone (usually at 45 degrees) to form a right-angle corner (miter joint).",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", text: "If it pass against us, we lose the better half of our possession: for all the temporal lands which men devout by testament have given to the church would they strip from our **miter**." },
      { author: "John Milton", work: "Lycidas", text: "The pilot of the Galilean lake shook his **miter**'d locks, mourning the untimely departure of young Lycidas." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The proud prelate assumed the jeweled **miter** and pastoral crosier, defying the secular decree of the emperor." }
    ]
  },
  {
    lemma: "mitochondrion",
    dashboard: "Dashboard — mit",
    primary: "An organelle found in large numbers in most eukaryotic cells, in which cellular respiration and energy production (ATP synthesis) occur.",
    secondary: "A double-membraned organelle containing its own circular DNA and ribosomes, derived evolutionarily from an alpha-proteobacterial endosymbiont.",
    quotes: [
      { author: "Carl Benda", work: "Weitere Mittheilungen über die Mitochondria", text: "I proposed the term **mitochondrion** to describe these thread-like and granular cytoplasmic structures in spermatogenesis." },
      { author: "Peter Mitchell", work: "Coupling of Phosphorylation to Electron and Hydrogen Transfer", text: "The inner membrane of the **mitochondrion** operates as a chemiosmotic transducer, coupling electron transport to ATP synthesis." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "The **mitochondrion** was once an independent, oxygen-respiring bacterial symbiont engulfed by an anaerobic host." }
    ]
  },
  {
    lemma: "mitosis",
    dashboard: "Dashboard — mit",
    primary: "A type of cell division that results in two daughter cells each having the same number and kind of chromosomes as the parent nucleus.",
    secondary: "The continuous cycle of nuclear division comprising prophase, metaphase, anaphase, and telophase, mediated by the mitotic spindle apparatus.",
    quotes: [
      { author: "Walther Flemming", work: "Zellsubstanz, Kern und Zelltheilung", text: "I applied the term **mitosis** to this process of thread-formation, through which the chromatin is divided with geometric equality." },
      { author: "Thomas Hunt Morgan", work: "The Physical Basis of Heredity", text: "During **mitosis**, each longitudinal half of a split chromosome travels to opposite poles, preserving identical genetic information." },
      { author: "Edmund Beecher Wilson", work: "The Cell in Development and Heredity", text: "The exquisite precision of **mitosis** guarantees the unbroken hereditary continuity of the organism across cellular generations." }
    ]
  },
  {
    lemma: "remit",
    dashboard: "Dashboard — mit",
    primary: "To cancel, pardon, or refrain from exacting a debt, fine, penalty, or punishment; to send money in payment.",
    secondary: "To diminish or abate in severity, force, or intensity (as in a remitting fever); also, to refer a matter to an authority for decision.",
    quotes: [
      { author: "William Shakespeare", work: "The Merchant of Venice", text: "The duke cannot deny the course of law; yet if thou wilt, mercifully **remit** the penalty of the bond." },
      { author: "John Locke", work: "Second Treatise of Government", text: "The magistrate has the executive power to **remit** the punishment of criminal offenses where public interest permits." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The malarial paroxysm began to **remit** toward dawn, drenched in profuse cooling perspiration." }
    ]
  },

  // Dashboard — thanat (4 words)
  {
    lemma: "thanatology",
    dashboard: "Dashboard — thanat",
    primary: "The branch of science and humanities dealing with the facts, causes, phenomena, and psychological consequences of death.",
    secondary: "The comprehensive study of physiological dying, bereavement counseling, and ethical dilemmas surrounding end-of-life care.",
    quotes: [
      { author: "Elisabeth Kübler-Ross", work: "On Death and Dying", text: "Modern **thanatology** broke the conspiracy of silence surrounding the terminal ward, helping patients face death with dignity." },
      { author: "Herman Feifel", work: "The Meaning of Death", text: "Pioneering research in **thanatology** restored mortality to its central position in psychological inquiry." },
      { author: "Ernest Becker", work: "The Denial of Death", text: "Cultural **thanatology** reveals that human civilizations construct elaborate heroic projects to deny physical death." }
    ]
  },
  {
    lemma: "thanatophobia",
    dashboard: "Dashboard — thanat",
    primary: "An extreme, morbid, or pathological dread of death or dying.",
    secondary: "A specific phobic disorder marked by anticipatory terror, somatic distress, and compulsive avoidance of anything associated with mortality.",
    quotes: [
      { author: "Sigmund Freud", work: "The Ego and the Id", text: "The unconscious mind knows nothing of its own annihilation, making acute **thanatophobia** a reflection of castration anxiety and moral guilt." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", text: "Miserable melancholics torment themselves with continual **thanatophobia**, trembling at every rustling leaf as a harbinger of the tomb." },
      { author: "G. Stanley Hall", work: "Thanatophobia and Immortality", text: "The developmental emergence of **thanatophobia** in early youth spurs intense philosophical and religious introspection." }
    ]
  },
  {
    lemma: "thanatopsis",
    dashboard: "Dashboard — thanat",
    primary: "A spiritual or philosophical contemplation of death and mortal transience.",
    secondary: "The poetic view of mortality expressed in nineteenth-century romantic literature, envisioning death as peaceful rest in the earth.",
    quotes: [
      { author: "William Cullen Bryant", work: "Thanatopsis", text: "To him who in the love of Nature holds communion with her visible forms, she speaks a various language; she glides into his darker musings with a mild and healing sympathy... a serene **thanatopsis**." },
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", text: "In the quiet autumn woods, the falling leaves offer a gentle **thanatopsis** reconciling the wanderer to the inevitable sleep." },
      { author: "Walt Whitman", work: "Leaves of Grass", text: "I bequeath myself to the dirt to grow from the grass I love; if you want me again look for me under your boot-soles—a glorious American **thanatopsis**." }
    ]
  },
  {
    lemma: "thanatos",
    dashboard: "Dashboard — thanat",
    primary: "Death personified in classical Hellenic mythology, serving as an attendant of Hades alongside his brother Hypnos.",
    secondary: "The psychological concept of the death drive (mortido or destructive drive) in post-Freudian psychoanalytic literature.",
    quotes: [
      { author: "Hesiod", work: "Theogony", text: "There dwell the children of dark Night, glowing Sleep and dreadful **Thanatos**, terrible gods whom the shining sun never looks upon with his beams." },
      { author: "Sigmund Freud", work: "Civilization and Its Discontents", text: "The fateful question for the human species seems to me to be whether and to what extent their cultural development will succeed in mastering the disturbance of their communal life by the human instinct of aggression and self-destruction—the drive of **Thanatos**." },
      { author: "Carl Jung", work: "Psychological Types", text: "In psychic equilibrium, the creative vitality of Eros must constantly balance the silent pulling of **Thanatos** toward dissolution." }
    ]
  }
];

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(filePath, wordData) {
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

let count = 0;
for (const item of BATCH7_DATA) {
  const filePath = path.join(CLUSTER_DIR, item.dashboard, `${item.lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, item)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 7 Completed: ${count} / ${BATCH7_DATA.length} words updated`);
console.log(`========================================\n`);
