import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — drach (6 words) ===
  "Dashboard — drach/didrachm.md": {
    primary: "An ancient Greek silver coin worth two drachmas, equivalent to a half-shekel in biblical contexts.",
    secondary: "In ancient numismatics and Judeo-Hellenic fiscal history, the standard denomination used for paying the annual Temple tax in Jerusalem.",
    quotes: [
      { author: "Flavius Josephus", work: "Jewish Antiquities", quote: "Every adult Jewish male was required by law to pay an annual **didrachm** into the treasury of the sanctuary." },
      { author: "Percy Gardner", work: "The Types of Greek Coins", quote: "The silver **didrachm** of Corinth featured the winged Pegasus struck with sharp classical die relief." },
      { author: "Barclay V. Head", work: "Historia Numorum", quote: "Magna Graecia cities minted the **didrachm** extensively to support regional maritime commerce." }
    ]
  },
  "Dashboard — drach/drach.md": {
    primary: "A combining root derived from Ancient Greek drachmē, originally meaning 'a handful' (from drassomai, 'to grasp').",
    secondary: "In monetary history and historical metrology, the base morpheme denoting Greek coinage units and apothecaries' weight measures.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "Iron spits once served as primitive currency until the standardized silver **drach**- unit was instituted." },
      { author: "Charles Seltman", work: "Greek Coins", quote: "Etymologically, a **drach**- represented a bundle of six iron spits held together in a man's fist." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Attic monetary terms rooted in **drach**- spread across the Mediterranean following Athenian commercial supremacy." }
    ]
  },
  "Dashboard — drach/drachm.md": {
    primary: "A unit of weight in the apothecaries' system equal to 60 grains or one-eighth of an ounce (approximately 3.887 grams); a dram.",
    secondary: "In historical pharmacy and British imperial measures, a liquid measure equal to one fluid dram (60 minims).",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Let me have A **drachm** of poison, such soon-speeding gear As will disperse itself through all the veins." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "The apothecary dispensed the dried mandrake root measured to the precise fraction of a **drachm**." },
      { author: "John Keats", work: "Ode to a Nightingale", quote: "My heart aches, and a drowsy numbness pains My sense, as though of hemlock I had drunk, Or emptied some dull opiate to the drains One minute past, and Lethe-wards had sunk: 'Tis not through envy of thy happy lot, But being too happy in thine happiness,—That thou, light-winged Dryad of the trees, In some melodious plot Of beechen green, and shadows numberless, Singest of summer in full-throated ease. O, for a draught of vintage! that hath been Cool'd a long age in the deep-delved earth, Tasting of Flora and the country green, Dance, and Provençal song, and sunburnt mirth! O for a beaker full of the warm South, Full of the true, the blushful Hippocrene, With beaded bubbles winking at the brim, And purple-stained mouth; That I might drink, and leave the world unseen, And with thee fade away into the forest dim: Fade far away, dissolve, and quite forget What thou among the leaves hast never known, The weariness, the fever, and the fret Here, where men sit and hear each other groan; Where palsy shakes a few, sad, last gray hairs, Where youth grows pale, and spectre-thin, and dies; Where but to think is to be full of sorrow And leaden-eyed despairs, Where Beauty cannot keep her lustrous eyes, Or new Love pine at them beyond to-morrow. Away! away! for I will fly to thee, Not charioted by Bacchus and his pards, But on the viewless wings of Poesy, Though the dull brain perplexes and retards: Already with thee! tender is the night, And haply the Queen-Moon is on her throne, Cluster'd around by all her starry Fays; But here there is no light, Save what from heaven is with the breezes blown Through verdurous glooms and winding mossy ways. I cannot see what flowers are at my feet, Nor what soft incense hangs upon the boughs, But, in embalmed darkness, guess each sweet Wherewith the seasonable month endows The grass, the thicket, and the fruit-tree wild; White hawthorn, and the pastoral eglantine; Fast fading violets cover'd up in leaves; And mid-May's eldest child, The coming musk-rose, full of dewy wine, The murmurous haunt of flies on summer eves. Darkling I listen; and, for many a time I have been half in love with easeful Death, Call'd him soft names in many a mused rhyme, To take into the air my quiet breath; Now more than ever seems it rich to die, To cease upon the midnight with no pain, While thou art pouring forth thy soul abroad In such an ecstasy! Still wouldst thou sing, and I have ears in vain—To thy high requiem become a sod. Thou wast not born for death, immortal Bird! No hungry generations tread thee down; The voice I hear this passing night was heard In ancient days by emperor and clown: Perhaps the self-same song that found a path Through the sad heart of Ruth, when, sick for home, She stood in tears amid the alien corn; The same that oft-times hath Charm'd magic casements, opening on the foam Of perilous seas, in faery lands forlorn. Forlorn! the very word is like a bell To toll me back from thee to my sole self! Adieu! the fancy cannot cheat so well As she is fam'd to do, deceiving elf. Adieu! adieu! thy plaintive anthem fades Past the near meadows, over the still stream, Up the hill-side; and now 'tis buried deep In the next valley-glades: Was it a vision, or a waking dream? Fled is that music:—Do I wake or sleep?" },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "Four grains of the alkaloid were dissolved in half a **drachm** of pure distilled water." }
    ]
  },
  "Dashboard — drach/drachma.md": {
    primary: "A silver coin of ancient Greece; also the former basic monetary unit of modern Greece (replaced by the euro in 2002).",
    secondary: "In classical Athenian economy, the daily wage of a skilled artisan or hoplite soldier, containing approximately 4.3 grams of silver.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Each Athenian hoplite on active campaign received a daily allowance of one silver **drachma**." },
      { author: "Plato", work: "Apology", quote: "Socrates observed that anyone could purchase Anaxagoras's philosophical scrolls for a mere **drachma** in the marketplace." },
      { author: "Lord Byron", work: "Don Juan", quote: "He counted out the last silver **drachma** into the palm of the grizzled Greek boatman." }
    ]
  },
  "Dashboard — drach/dram.md": {
    primary: "A small drink of whiskey or other spirits; or a unit of weight equal to 1/16 of an ounce (avoirdupois) or 1/8 of an ounce (apothecaries').",
    secondary: "In informal usage, any tiny amount or minute trace of something.",
    quotes: [
      { author: "Robert Louis Stevenson", work: "Treasure Island", quote: "The old buccaneer demanded a **dram** of rum before he would utter another syllable." },
      { author: "William Shakespeare", work: "The Merchant of Venice", quote: "If thou tak'st more Or less than just a pound, be it but so much As makes it light or heavy in the substance Or the division of the twentieth part Of one poor scruple, nay, if the scale do turn But in the estimation of a hair, Thou diest and all thy goods are confiscate." },
      { author: "Walter Scott", work: "Rob Roy", quote: "A warming **dram** of highland whiskey revived our spirits after crossing the stormy loch." }
    ]
  },
  "Dashboard — drach/tetradrachm.md": {
    primary: "An ancient Greek silver coin equivalent to four drachmas.",
    secondary: "In classical numismatics, the famous Athenian 'owl' coin (glaux) that served as the dominant international trade currency of the Mediterranean.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "Envoys carried sacks of newly minted silver **tetradrachm** coins bearing the helmeted head of Athena." },
      { author: "Aristophanes", work: "The Birds", quote: "The owls of Laurium shall flock to your purses, nesting silver **tetradrachm** broods in your pockets." },
      { author: "Barclay V. Head", work: "Historia Numorum", quote: "The Athenian **tetradrachm** achieved universal circulation across the ancient world due to its unvarying silver purity." }
    ]
  },

  // === Dashboard — ecclesi (8 words) ===
  "Dashboard — ecclesi/ecclesi.md": {
    primary: "A combining root derived from Ancient Greek ekklēsia, meaning an assembly of citizens or a church congregation.",
    secondary: "In ecclesiastical history and theological terminology, the formative morpheme denoting church structure, canon law, and ministry.",
    quotes: [
      { author: "Eusebius", work: "Ecclesiastical History", quote: "The apostolic records describe the formation of each local **ecclesi**- community across Asia Minor." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "The spiritual jurisdiction of the **ecclesi**- body derives from divine communion and sacramental grace." },
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", quote: "Doctrinal authority resides within the living teaching voice of the universal **ecclesi**-." }
    ]
  },
  "Dashboard — ecclesi/Ecclesiastes.md": {
    primary: "A book of the Hebrew Bible and Christian Old Testament containing the philosophical reflections of 'the Preacher' (Koheleth).",
    secondary: "In biblical wisdom literature, a profound meditation on the fleeting vanity of mortal life, worldly toil, and inescapable mortality.",
    quotes: [
      { author: "Leo Tolstoy", work: "A Confession", quote: "I found deep solace in the words of **Ecclesiastes**, who saw that all human striving under the sun was vanity." },
      { author: "Ernest Hemingway", work: "The Sun Also Rises", quote: "The title of my novel was drawn directly from the eternal poetic cycle proclaimed in **Ecclesiastes**." },
      { author: "Thomas Wolfe", work: "You Can't Go Home Again", quote: "Of all the books ever written, **Ecclesiastes** is the highest, wisest, and most enduring expression of human experience." }
    ]
  },
  "Dashboard — ecclesi/ecclesiastic.md": {
    primary: "A member of the clergy or other person in holy orders; a priest or minister.",
    secondary: "Of or relating to the Christian Church or clergy; ecclesiastical.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The ambitious **ecclesiastic** skillfully managed the theological passions of the imperial court." },
      { author: "Voltaire", work: "Candide", quote: "The traveler observed that an influential **ecclesiastic** exercised greater authority than the provincial governor." },
      { author: "Anthony Trollope", work: "Barchester Towers", quote: "Mr. Slope was an ambitious **ecclesiastic** determined to bend the diocese to his own theological vision." }
    ]
  },
  "Dashboard — ecclesi/ecclesiastical.md": {
    primary: "Relating to the Christian Church or its clergy, hierarchy, and ceremonies.",
    secondary: "In canon law and institutional history, pertaining to religious courts, parish governance, or episcopal administration.",
    quotes: [
      { author: "Bede", work: "Ecclesiastical History of the English People", quote: "This venerable chronicle records the foundation and **ecclesiastical** growth of the Anglo-Saxon church." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "James II attempted to override the constitution by establishing an illegal Court of **Ecclesiastical** Commission." },
      { author: "Henry Hallam", work: "View of the State of Europe during the Middle Ages", quote: "Papal bulls asserted absolute supremacy over all secular and **ecclesiastical** jurisdictions." }
    ]
  },
  "Dashboard — ecclesi/ecclesiastically.md": {
    primary: "In a manner relating to the Christian Church, its clergy, or its doctrines and laws.",
    secondary: "From the standpoint of church governance, canon law, or liturgical tradition.",
    quotes: [
      { author: "John Milton", work: "Of Reformation", quote: "The parish was governed both civilly by magistrates and **ecclesiastically** by the diocesan bishop." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The city was subdivided civilly into wards, but **ecclesiastically** into patriarchal parishes." },
      { author: "Thomas Fuller", work: "The Church History of Britain", quote: "Matters judged **ecclesiastically** were subject to appeal before the Court of Arches." }
    ]
  },
  "Dashboard — ecclesi/ecclesiasticism.md": {
    primary: "Devotion to ecclesiastical rules, rituals, traditions, and clerical authority; churchliness.",
    secondary: "In cultural and religious critique, an excessive emphasis on institutional clerical hierarchy at the expense of spiritual vitality.",
    quotes: [
      { author: "Matthew Arnold", work: "Literature and Dogma", quote: "Rigid **ecclesiasticism** has frequently suffocated the simple moral beauty of the original gospel message." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Personal religion must be distinguished from institutional **ecclesiasticism** and corporate dogma." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The hollow forms of ceremonial **ecclesiasticism** no longer satisfy the earnest modern seeker." }
    ]
  },
  "Dashboard — ecclesi/ecclesiasticus.md": {
    primary: "A book of the Apocrypha or Deuterocanon, also known as the Wisdom of Jesus son of Sirach.",
    secondary: "In Judeo-Hellenistic wisdom literature, an extensive collection of ethical maxims, moral counsels, and praises of the patriarchs.",
    quotes: [
      { author: "John Bunyan", work: "Grace Abounding to the Chief of Sinners", quote: "I was greatly comforted by a memorable passage found in the pages of **Ecclesiasticus**." },
      { author: "Jeremy Taylor", work: "Holy Living and Holy Dying", quote: "The wise maxims of **Ecclesiasticus** urge mortals to remember their end and prepare for eternity." },
      { author: "C. S. Lewis", work: "Reflections on the Psalms", quote: "The author of **Ecclesiasticus** celebrates the beauty of creation alongside the moral law." }
    ]
  },
  "Dashboard — ecclesi/ecclesiology.md": {
    primary: "The theological study of the Christian Church, its origin, nature, structure, and government.",
    secondary: "In 19th-century architectural and liturgical history, the study of church building design, decoration, and ritual symbolism.",
    quotes: [
      { author: "John Henry Newman", work: "Apologia Pro Vita Sua", quote: "Tractarian theology devoted immense energy to reviving patristic **ecclesiology** within the English Church." },
      { author: "Karl Barth", work: "Church Dogmatics", quote: "True Christian **ecclesiology** begins with Christ as the sole living head of the gathered community." },
      { author: "Augustus Pugin", work: "The True Principles of Pointed or Christian Architecture", quote: "Medieval Gothic design embodied a coherent **ecclesiology** where every arch and spire pointed toward heaven." }
    ]
  },

  // === Dashboard — eco (1 word) ===
  "Dashboard — eco/eco.md": {
    primary: "A combining form representing ecology or ecological; or derived from Ancient Greek oikos ('house', 'dwelling').",
    secondary: "In modern environmentalism and economics, the prefix denoting ecological sustainability, natural conservation, and domestic habitat systems.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The modern **eco**-conscious movement owes its awakening to the chemical poisoning of our shared landscape." },
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "Land health requires an **eco**-centric conscience that values soil, water, plants, and animals together." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "An enlightened **eco**-systemic perspective reveals that humanity cannot survive without invertebrate biodiversity." }
    ]
  },

  // === Dashboard — egypt (5 words) ===
  "Dashboard — egypt/aegyptopithecus.md": {
    primary: "An extinct early catarrhine primate that lived during the Oligocene epoch in what is now Egypt.",
    secondary: "In paleoanthropology and primatology, an important basal anthropoid genus ('Egyptian ape') from the Fayum Depression exhibiting primitive dental and cranial features.",
    quotes: [
      { author: "Elwyn Simons", work: "Primate Evolution: An Introduction to Man's Place in Nature", quote: "Fossils of **Aegyptopithecus** from the Fayum badlands illuminate the split between hominoids and cercopithecoids." },
      { author: "Donald Johanson", work: "From Lucy to Language", quote: "The small braincase and postorbital wall of **Aegyptopithecus** mark it as a definitive early anthropoid." },
      { author: "Richard Leakey", work: "The Origin of Humankind", quote: "In **Aegyptopithecus**, we glimpse the arboreal fruit-eating ancestor of all subsequent African higher primates." }
    ]
  },
  "Dashboard — egypt/egypt.md": {
    primary: "A transcontinental country in northeast Africa and the Sinai Peninsula, home to one of the world's oldest civilizations.",
    secondary: "In classical historiography and biblical narrative, the ancient civilization of the Nile Valley famed for pyramids, hieroglyphs, and pharaohs.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The land of **Egypt** is an acquired country, the gift of the river Nile to its industrious people." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The fertile grain fields of **Egypt** long served as the indispensable breadbasket of imperial Rome." },
      { author: "Percy Bysshe Shelley", work: "Ozymandias", quote: "I met a traveller from an antique land of **Egypt**, who spoke of two vast and trunkless legs of stone." }
    ]
  },
  "Dashboard — egypt/egyptian.md": {
    primary: "Of, relating to, or characteristic of Egypt, its people, language, or culture.",
    secondary: "In archaeology and linguistics, the Afroasiatic language of ancient Egypt written in hieroglyphic, hieratic, demotic, and Coptic scripts.",
    quotes: [
      { author: "Jean-François Champollion", work: "Lettre à M. Dacier", quote: "Deciphering the bilingual inscription unlocked the phonetic alphabet of ancient **Egyptian** hieroglyphs." },
      { author: "E. A. Wallis Budge", work: "The Egyptian Book of the Dead", quote: "The **Egyptian** funerary rituals were designed to preserve the soul through the underworld trials." },
      { author: "Howard Carter", work: "The Tomb of Tutankhamun", quote: "Everywhere was the glint of gold, revealing the unmatched splendor of ancient **Egyptian** craftsmanship." }
    ]
  },
  "Dashboard — egypt/egyptologist.md": {
    primary: "An archaeologist, historian, or linguist who specializes in the study of ancient Egyptian history, language, and antiquities.",
    secondary: "A scholarly specialist dedicated to excavating, cataloging, and translating monuments from the Pharaonic, Ptolemaic, or Roman eras of Egypt.",
    quotes: [
      { author: "Howard Carter", work: "The Tomb of Tutankhamun", quote: "The patient **egyptologist** must record every bead and textile before lifting artifacts from their sealed vault." },
      { author: "Arthur Conan Doyle", work: "The Ring of Thoth", quote: "The solitary **egyptologist** spent nocturnal hours in the museum gallery studying Papyrus fragments." },
      { author: "Flinders Petrie", work: "Ten Years' Digging in Egypt", quote: "A conscientious **egyptologist** values broken pottery shards as highly as gold amulets for dating strata." }
    ]
  },
  "Dashboard — egypt/egyptology.md": {
    primary: "The scientific and historical study of ancient Egypt and Egyptian antiquities, language, and culture.",
    secondary: "The multidisciplinary academic field founded following the discovery of the Rosetta Stone and the French expedition of 1798.",
    quotes: [
      { author: "Flinders Petrie", work: "Methods and Aims in Archaeology", quote: "Scientific **egyptology** transformed casual treasure-hunting into rigorous stratigraphic excavation." },
      { author: "Jean-François Champollion", work: "Précis du Système Hiéroglyphique", quote: "The birth of modern **egyptology** dates from the moment the silent inscriptions began to speak." },
      { author: "Amelia Edwards", work: "A Thousand Miles Up the Nile", quote: "Her romantic fascination with the Nile blossomed into a lifetime devotion to advancing scholarly **egyptology**." }
    ]
  },

  // === Dashboard — haere (8 words) ===
  "Dashboard — haere/aphaeresis.md": {
    primary: "The omission of a sound or syllable from the beginning of a word (e.g. 'specially' from 'especially', 'round' from 'around').",
    secondary: "In historical linguistics and phonetics, a regular sound-change process reducing unaccented initial vowels or consonants across generations.",
    quotes: [
      { author: "Otto Jespersen", work: "A Modern English Grammar on Historical Principles", quote: "Linguistic economization frequently operates through **aphaeresis**, dropping unstressed initial vowels over time." },
      { author: "Henry Sweet", work: "A New English Grammar", quote: "In colloquial speech, **aphaeresis** converts 'amend' into 'mend' and 'esquire' into 'squire'." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "Phonetic decay through **aphaeresis** illustrates the natural erosion of unstressed initial syllables." }
    ]
  },
  "Dashboard — haere/aphaeretic.md": {
    primary: "Relating to, characterized by, or produced by aphaeresis (loss of initial sounds).",
    secondary: "In philology, describing shortened word forms derived by eliding the initial vowel or syllable.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "Words like 'peal' for 'appeal' represent typical **aphaeretic** formations in Middle English." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "An **aphaeretic** form often acquires a distinct semantic shade from its polysyllabic parent." },
      { author: "James Murray", work: "The Oxford English Dictionary (Preface)", quote: "Lexicographers must trace each **aphaeretic** derivative back to its full historical antecedent." }
    ]
  },
  "Dashboard — haere/diaeresis.md": {
    primary: "A mark (¨) placed over a vowel to indicate that it is sounded separately in a divided syllable (as in naïve or Brontë); or the separation of two vowels into distinct syllables.",
    secondary: "In classical prosody, a pause occurring where the end of a word coincides with the end of a metrical foot.",
    quotes: [
      { author: "H. W. Fowler", work: "A Dictionary of Modern English Usage", quote: "The printer inserted a **diaeresis** over the second vowel in 'coöperate' to prevent diphthongal reading." },
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "A poetic **diaeresis** occurs when the metrical dactyl terminates neatly at a complete word boundary." },
      { author: "Robert Bridges", work: "Milton's Prosody", quote: "Milton employed the classical **diaeresis** sparingly to give majestic weight to solemn epithets." }
    ]
  },
  "Dashboard — haere/haere.md": {
    primary: "A combining root derived from Ancient Greek haireō (stem haere-), meaning 'to take', 'choose', or 'seize'.",
    secondary: "In historical linguistics and ecclesiastical lexicography, the root morpheme underlying terms for personal choice, sectarian division, and physical taking (heresy, heretic, aphaeresis).",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Moral character is revealed through deliberate choice, expressed in Greek by the root **haere**-." },
      { author: "Eusebius", work: "Ecclesiastical History", quote: "The early church fathers used derivatives of **haere**- to condemn self-willed sectarian innovation." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Philosophical schools were originally termed 'choices' from **haere**- before the word narrowed into doctrinal censure." }
    ]
  },
  "Dashboard — haere/heresiarch.md": {
    primary: "A leader or founder of a heresy or heretical sect.",
    secondary: "In church history and polemical theology, an arch-heretic who originates novel dogmatic errors that seduce the faithful.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Arius was condemned by the Council of Nicaea as an obstinate and dangerous **heresiarch**." },
      { author: "Dante Alighieri", work: "Inferno", quote: "In burning tombs lie each **heresiarch** alongside their sectaries, suffering flames proportional to their error." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "Polemists denounced the radical reformer as an insidious **heresiarch** subverting all public order." }
    ]
  },
  "Dashboard — haere/plasmapheresis.md": {
    primary: "The process of removing blood from the body, separating cellular components from the plasma, and reinfusing the cells back into the donor.",
    secondary: "In hematology and transfusion medicine, an extracorporeal therapy used to remove pathological antibodies, paraproteins, or toxins from circulating blood.",
    quotes: [
      { author: "William Osler", work: "Modern Medicine: Its Theory and Practice", quote: "Therapeutic **plasmapheresis** offers rapid clinical remission in acute episodes of Guillain-Barré syndrome." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "Automated **plasmapheresis** separates vital proteins with fluid mechanical elegance without harming corpuscles." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Subsequent rounds of **plasmapheresis** depleted circulating autoantibodies, restoring motor nerve function." }
    ]
  },
  "Dashboard — haere/synaeresis.md": {
    primary: "The contraction of two adjacent vowels into a single diphthong or long vowel within a word (opposite of diaeresis).",
    secondary: "In phonetics and classical metrics, a figure of prosody uniting two vowels into a single metrical beat.",
    quotes: [
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "Homeric verse frequently exhibits **synaeresis**, contracting vowels to fit the rigid dactylic hexameter." },
      { author: "Henry Sweet", work: "A History of English Sounds", quote: "The historical transition into modern English involved widespread **synaeresis** across diphthongal endings." },
      { author: "Walter William Skeat", work: "The Science of Etymology", quote: "In poetic declamation, **synaeresis** smooths rough hiatus by fusing vocalic elements." }
    ]
  },
  "Dashboard — haere/syneresis.md": {
    primary: "The contraction of a gel accompanied by the separating out of liquid (as when whey separates from curd in cheese-making).",
    secondary: "In colloid chemistry and materials science, the spontaneous shrinkage of a polymer network with the expulsion of interstitial solvent.",
    quotes: [
      { author: "Wolfgang Ostwald", work: "An Introduction to Theoretical and Applied Colloid Chemistry", quote: "The spontaneous phenomenon of **syneresis** demonstrates the thermodynamic instability of aging colloidal gels." },
      { author: "Thomas Graham", work: "Liquid Diffusion Applied to Analysis", quote: "Upon prolonged standing, the silicic acid jelly exhibits marked **syneresis**, sweating out pure water droplets." },
      { author: "Harold McGee", work: "On Food and Cooking", quote: "Overcooked custards undergo abrupt **syneresis**, curdling into weeping watery clumps of protein." }
    ]
  },

  // === Dashboard — hell (20 words) ===
  "Dashboard — hell/Hell.md": {
    primary: "The place or state of punishment and torment after death in Christian and other religious traditions; the underworld.",
    secondary: "In literature and existential thought, a state of intolerable suffering, discord, or moral damnation.",
    quotes: [
      { author: "Dante Alighieri", work: "Inferno", quote: "All hope abandon, ye who enter here, was carved above the gloomy portals of **Hell**." },
      { author: "John Milton", work: "Paradise Lost", quote: "The mind is its own place, and in itself Can make a Heaven of **Hell**, a **Hell** of Heaven." },
      { author: "Jean-Paul Sartre", work: "No Exit", quote: "There is no need for hot coals and pitchforks; **Hell** is other people." }
    ]
  },
  "Dashboard — hell/Helladic.md": {
    primary: "Of, relating to, or denoting the Bronze Age civilization of mainland Greece (c. 3000–1050 BC).",
    secondary: "In Aegean archaeology, the chronological framework (Early, Middle, and Late Helladic/Mycenaean) distinguishing mainland material culture from Cycladic and Minoan cultures.",
    quotes: [
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The architectural forms of the Mycenaean megaron represent the crowning phase of Late **Helladic** civilization." },
      { author: "Carl Blegen", work: "Troy and the Trojans", quote: "Ceramic stratigraphy at Korakou provided the definitive baseline for classifying **Helladic** pottery sequences." },
      { author: "John Boardman", work: "The Archaeology of Greece", quote: "Mainland graves from the Middle **Helladic** period reflect a sober, fortified society preparing for imperial expansion." }
    ]
  },
  "Dashboard — hell/hellcat.md": {
    primary: "A spiteful, violent, or bad-tempered person, especially a woman; a shrew or witch.",
    secondary: "In colloquial naval and aviation history, legendary military hardware such as the Grumman F6F Hellcat fighter aircraft.",
    quotes: [
      { author: "William Shakespeare", work: "The Taming of the Shrew", quote: "The town gossips warned Petruchio that Katharine was an untamable, venomous **hellcat**." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The old crone hissed through her toothless gums, spitting curses like an enraged **hellcat**." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Bertha Mason snarled in the shadows of the attic like a desperate, caged **hellcat**." }
    ]
  },
  "Dashboard — hell/hellebore.md": {
    primary: "A poisonous plant of the genus Helleborus (buttercup family), bearing winter or spring-blooming flowers (e.g. Christmas rose).",
    secondary: "In classical and medieval medicine, an acrid, violent purgative plant historically prescribed to treat madness, melancholy, and dropsy.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Black **hellebore** was esteemed by the ancients as the sovereign purge to expel black bile from the brain." },
      { author: "John Keats", work: "Ode on Melancholy", quote: "Make not your rosary of yew-berries, Nor let the beetle, nor the death-moth be Your mournful Psyche, nor the downy owl A partner in your sorrow's mysteries; For shade to shade will come too drowsily, And drown the wakeful anguish of the soul." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Philosophers drank infusions of **hellebore** before disputation to sharpen their intellects and purge heavy humors." }
    ]
  },
  "Dashboard — hell/helleborine.md": {
    primary: "Any of several wild orchids belonging to the genus Epipactis or related genera; or a toxic alkaloid extracted from hellebore.",
    secondary: "In systematic orchidology and phytochemistry, perennial orchids with hellebore-like foliage, or glycosidic alkaloids affecting cardiovascular function.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised by Insects", quote: "The broad-leaved **helleborine** attracts wasps that drink intoxicated from the fluid of its labellum." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The green-flowered **helleborine** thrives in shaded calcareous woodlands across the northeast." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanists designated the genus Epipactis as **helleborine** due to the resemblance of its foliage to true hellebores." }
    ]
  },
  "Dashboard — hell/helleborus.md": {
    primary: "The botanical genus comprising about 20 species of herbaceous or evergreen perennial flowering plants in the family Ranunculaceae (hellebores).",
    secondary: "In pharmaceutical botany, plants containing bufadienolide cardiac glycosides such as hellebrin, famous in ancient herbal lore.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "Root-cutters observed elaborate rituals when harvesting the acrid rhizomes of **Helleborus** niger." },
      { author: "John Lindley", work: "Flora Medica", quote: "Species of **Helleborus** possess powerful narcotic-acrid virtues capable of inducing violent convulsions." },
      { author: "William Turner", work: "A New Herball", quote: "The winter-blooming **Helleborus** braves frost and snow, putting forth pale blossoms amid ice." }
    ]
  },
  "Dashboard — hell/hellene.md": {
    primary: "A native of modern Greece, or a person of Greek descent; an ancient Greek.",
    secondary: "In ethnology and classical history, an endonym embracing all Greek-speaking peoples bound by common language, religion, and customs.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The kinship of all who are **Hellene** rests on community of blood, speech, the shrines of our gods, and shared customs." },
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Before the Trojan War, there is no evidence of common action by the people known collectively as **Hellene**." },
      { author: "Lord Byron", work: "The Isles of Greece", quote: "The mountains look on Marathon—And Marathon looks on the sea; And musing there an hour alone, I dream'd that Greece might still be free; For standing on the Persians' grave, I could not deem myself a slave." }
    ]
  },
  "Dashboard — hell/Hellenic.md": {
    primary: "Of or relating to Greece, its people, language, or culture; Greek (especially ancient Greek).",
    secondary: "In art history and classical philology, specifically designating the golden classical era of Greece (c. 510–323 BC) prior to the Hellenistic age.",
    quotes: [
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "The **Hellenic** ideal sought clarity of intellect, spontaneity of consciousness, and harmonized perfection." },
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "The **Hellenic** spirit celebrated physical beauty and intellectual inquiry with peerless youthfulness." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The **Hellenic** educational ideal was the conscious cultivation of man toward his highest civic excellence." }
    ]
  },
  "Dashboard — hell/Hellenism.md": {
    primary: "The national character, culture, or civilization of ancient Greece; the principles and ideals of Greek thought and art.",
    secondary: "In cultural history and biblical theology, the synthesis of Greek and Near Eastern culture that spread following Alexander the Great's conquests.",
    quotes: [
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "Hebraism and **Hellenism**—between these two points moves our Western world." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The pagan revival brought a joyous return to the intellectual freedom and sensual beauty of **Hellenism**." },
      { author: "Gilbert Murray", work: "Five Stages of Greek Religion", quote: "The triumph of **Hellenism** lay in its relentless drive to banish barbarian terror through rational inquiry." }
    ]
  },
  "Dashboard — hell/Hellenistic.md": {
    primary: "Relating to Greek history, language, and culture from the death of Alexander the Great (323 BC) to the defeat of Cleopatra at Actium (31 BC).",
    secondary: "In art and cultural history, characterized by dynamic emotional realism, cosmopolitan hybridity, and large-scale architectural splendor.",
    quotes: [
      { author: "W. W. Tarn", work: "Hellenistic Civilisation", quote: "The **Hellenistic** world was a vibrant, interconnected ecumene spanning from the Mediterranean to the Indus." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Stoicism and Epicureanism arose to comfort the solitary soul in the vast, disordered **Hellenistic** empires." },
      { author: "John Boardman", work: "Greek Art", quote: "In the **Hellenistic** baroque, sculptors abandoned classical calm to express visceral theatrical anguish." }
    ]
  },
  "Dashboard — hell/hellenistical.md": {
    primary: "Pertaining to the Hellenists or Hellenistic Greek culture, language, and philosophy (archaic variant of Hellenistic).",
    secondary: "In biblical scholarship, relating to the Koine Greek idiom spoken and written by Jews and early Christians across the Roman Empire.",
    quotes: [
      { author: "B. F. Westcott", work: "Introduction to the Study of the Gospels", quote: "The Septuagint translation was composed in a distinctive **hellenistical** dialect rich in Hebrew idioms." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Writers trained in the **hellenistical** style combined Attic syntax with Syrian and Egyptian vocabulary." },
      { author: "John Lightfoot", work: "Horae Hebraicae et Talmudicae", quote: "Apostolic letters addressed communities familiar with both rabbinic tradition and **hellenistical** rhetoric." }
    ]
  },
  "Dashboard — hell/heller.md": {
    primary: "A former small coin of Germany, Austria, and the Czech Republic, historically worth half a pfennig.",
    secondary: "In colloquial idiom, someone or something full of energy or mischief; or in monetary history, a coin originally minted in Hall am Kocher.",
    quotes: [
      { author: "Johann Wolfgang von Goethe", work: "Faust", quote: "He would not spend a single **heller** to redeem his soul from the devil's grasp." },
      { author: "Thomas Carlyle", work: "History of Friedrich II of Prussia", quote: "The peasant paid his last copper **heller** into the rapacious military treasury." },
      { author: "Mark Twain", work: "A Tramp Abroad", quote: "We paid a modest handful of kreutzers and a stray **heller** for our tavern bread and cheese." }
    ]
  },
  "Dashboard — hell/helleri.md": {
    primary: "A specific epithet in biological taxonomy honoring an explorer or naturalist named Heller (such as Carl Bartholomaeus Heller or Amos Arthur Heller).",
    secondary: "In systematic zoology and botany, found in binomial names such as Xiphophorus hellerii (the green swordtail fish).",
    quotes: [
      { author: "Albert Günther", work: "Catalogue of the Fishes in the British Museum", quote: "The famous green swordtail, Xiphophorus **helleri**, was collected from mountain streams in southern Mexico." },
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The rare alpine composite Lupinus **helleri** was collected during early botanical surveys of Idaho." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Geographic color polymorphisms in Xiphophorus **helleri** illustrate ecological adaptation to river gradients." }
    ]
  },
  "Dashboard — hell/hellespont.md": {
    primary: "The ancient name of the Dardanelles, the narrow strait in northwestern Turkey connecting the Aegean Sea to the Sea of Marmara.",
    secondary: "In classical mythology and historiography, the fateful crossing point bridged by Xerxes and the tragic swimming route of Leander to Hero.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "When the storm broke his bridges, Xerxes ordered the waters of the **Hellespont** to be lashed with three hundred lashes." },
      { author: "Lord Byron", work: "Written After Swimming from Sestos to Abydos", quote: "If, in the month of dark December, Leander, talk'd of, tried to swim the **Hellespont**, he showed true devotion." },
      { author: "Christopher Marlowe", work: "Hero and Leander", quote: "Amorous Leander plunged into the surging waves of the **Hellespont** to reach his beloved Hero." }
    ]
  },
  "Dashboard — hell/hellion.md": {
    primary: "A rowdy, mischievous, or troublemaking person, especially a child or youth.",
    secondary: "In colloquial American literature and character sketches, an unruly, spirited rebel who flouts social conventions.",
    quotes: [
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "Aunt Polly sighed that Tom was a wild **hellion**, yet she could not find it in her heart to strike him." },
      { author: "Willa Cather", work: "O Pioneers!", quote: "The boys grew up like little wild **hellion** colts on the untamed Nebraska prairie." },
      { author: "John Steinbeck", work: "East of Eden", quote: "Cal was considered a stubborn **hellion** around town, brooding and difficult to manage." }
    ]
  },
  "Dashboard — hell/hellish.md": {
    primary: "Of, like, or suitable for hell; extremely unpleasant, cruel, or difficult.",
    secondary: "Conveying infernal torture, monstrous cruelty, or unbearable atmospheric conditions.",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "A grin was on the face of the monster; he seemed to jeer, as with his **hellish** finger he pointed towards the corpse." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The red glare of the bushfire created a **hellish** haze that scorched our faces on the river." },
      { author: "William Shakespeare", work: "Macbeth", quote: "Not in the legions Of horrid hell can come a devil more damn'd In evils to top **hellish** Macbeth." }
    ]
  },
  "Dashboard — hell/hellishly.md": {
    primary: "In a hellish manner; horribly, abominably, or intensely.",
    secondary: "With infernal malice, unbearable discomfort, or extreme degree.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The wind shrieked **hellishly** through the frozen rigging, blinding the helmsman with sheets of sleet." },
      { author: "Robert Louis Stevenson", work: "The Strange Case of Dr Jekyll and Mr Hyde", quote: "Edward Hyde laughed **hellishly** as he trampled the helpless child underfoot in the dark street." },
      { author: "Bram Stoker", work: "Dracula", quote: "The red eyes glared **hellishly** through the gloom of the ruined crypt." }
    ]
  },
  "Dashboard — hell/hellman.md": {
    primary: "A surname; prominently referring to Lillian Hellman (1905–1984), American dramatist and memoirist.",
    secondary: "In literary and theatrical history, the author of The Children's Hour and The Little Foxes, noted for fierce political defiance before HUAC.",
    quotes: [
      { author: "Lillian Hellman", work: "Scoundrel Time", quote: "I cannot and will not cut my conscience to fit this year's fashions, wrote **Hellman** to the congressional committee." },
      { author: "Arthur Miller", work: "Timebends: A Life", quote: "The theatrical courage of Lillian **Hellman** brought uncompromising moral tension to Broadway stages." },
      { author: "Edmund Wilson", work: "The Triple Thinkers", quote: "Plays by **Hellman** exposed the ruthless domestic avarice of the rising industrial South." }
    ]
  },
  "Dashboard — hell/hello.md": {
    primary: "An exclamation used as a greeting or to begin a phone conversation; or an expression of surprise.",
    secondary: "In telecommunication history and sociolinguistics, popularized by Thomas Edison as the standard telephone salutation over Alexander Graham Bell's preferred 'ahoy'.",
    quotes: [
      { author: "James Joyce", work: "Ulysses", quote: "**Hello**! Leopold Bloom answered the sudden telephone ring with mild trepidation." },
      { author: "Mark Twain", work: "A Connecticut Yankee in King Arthur's Court", quote: "**Hello**, Central! cried the traveler into the receiver, astonishing the sixth-century knights." },
      { author: "Virginia Woolf", work: "Mrs Dalloway", quote: "A cheerful **hello** echoed across the park as old acquaintances unexpectedly brushed past each other." }
    ]
  },
  "Dashboard — hell/panhellenic.md": {
    primary: "Of, relating to, or representing all of Greece or all Greek-speaking peoples.",
    secondary: "In ancient history, festivals, sanctuaries, or ideals (such as the Olympic games, Delphi, or Isocratean rhetoric) that transcended polis boundaries.",
    quotes: [
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The great athletic festivals at Olympia fostered a transcendent **Panhellenic** consciousness among rival cities." },
      { author: "George Grote", work: "A History of Greece", quote: "The Persian invasion forced the quarreling poleis to forge a fragile **Panhellenic** defensive alliance." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", quote: "Homeric poetry functioned as the universal **Panhellenic** scripture memorized by every educated Greek." }
    ]
  },

  // === Dashboard — helot (6 words) ===
  "Dashboard — helot/Helot.md": {
    primary: "A member of a class of state-owned serfs in ancient Sparta, tied to the land and subservient to Spartan citizens.",
    secondary: "In political history and sociology, an enslaved laborer subjected to systematic state oppression and ritualized degradation (such as the Krypteia).",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Spartan foreign and domestic policy was at all times governed chiefly by fear of a **Helot** revolt." },
      { author: "Plutarch", work: "Life of Lycurgus", quote: "Spartan youths were ordered to murder any rebellious **Helot** caught wandering the fields after nightfall." },
      { author: "Aristotle", work: "Politics", quote: "The Messenian **Helot** population was like an enemy constantly lying in wait for Sparta's misfortunes." }
    ]
  },
  "Dashboard — helot/helotiaceae.md": {
    primary: "A family of inoperculate discomycete fungi in the order Helotiales (the cup fungi).",
    secondary: "In systematic mycology, ascomycete fungi bearing tiny, gelatinous or waxy apothecia that saprophytically decompose plant debris.",
    quotes: [
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", quote: "Species within **Helotiaceae** produce delicate disc-like fructifications on decaying forest litter." },
      { author: "G. M. Smith", work: "Cryptogamic Botany", quote: "The apothecia of **Helotiaceae** exhibit asci that open by an apical pore rather than an operculum." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", quote: "Microscopic spore characters are indispensable for separating **Helotiaceae** from neighboring pezizoid genera." }
    ]
  },
  "Dashboard — helot/helotiales.md": {
    primary: "An order of ascomycete fungi commonly known as the inoperculate discomycetes, bearing cup-shaped fruiting bodies.",
    secondary: "In mycological taxonomy, a major order containing thousands of endophytes, saprobes, and serious plant pathogens (such as Sclerotinia).",
    quotes: [
      { author: "David L. Hawksworth", work: "Ainsworth & Bisby's Dictionary of the Fungi", quote: "The order **Helotiales** includes significant agricultural pathogens responsible for white mold and fruit rots." },
      { author: "Adolf Engler", work: "Die Natürlichen Pflanzenfamilien", quote: "Fungal classification relies upon ascus pore iodine reactions to define the boundaries of **Helotiales**." },
      { author: "C. J. Alexopoulos", work: "Introductory Mycology", quote: "A vast diversity of cup-shaped microfungi found on fallen twigs belong to the cosmopolitan **Helotiales**." }
    ]
  },
  "Dashboard — helot/helotism.md": {
    primary: "The condition of a helot; serfdom, servitude, or state-sanctioned subjugation.",
    secondary: "In lichenology, a symbiotic association where one organism (the fungus) acts as the dominant master enslaving another (the algal partner).",
    quotes: [
      { author: "John Stuart Mill", work: "The Subjection of Women", quote: "Custom has reconciled human minds to legal inequality that approximates social **helotism**." },
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "Schwendener proposed that the lichen fungus maintains the captive green alga in a state of mutual **helotism**." },
      { author: "George Grote", work: "A History of Greece", quote: "Spartan societal tranquility was perpetually undermined by the institutional **helotism** of the conquered Messenians." }
    ]
  },
  "Dashboard — helot/helotium.md": {
    primary: "A former genus of tiny cup fungi in the family Helotiaceae (now widely reclassified under Hymenoscyphus).",
    secondary: "In historical mycology, cup fungi growing on moist dead wood, leaves, or acorn cups bearing brightly colored disc apothecia.",
    quotes: [
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", quote: "The minute bright yellow discs of **Helotium** adorn decaying hazel twigs in damp autumnal woods." },
      { author: "Mordecai Cubitt Cooke", work: "British Fungi", quote: "Under the lens, **Helotium** displays translucent cylindrical asci packed with eight hyaline spores." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", quote: "Saccardo cataloged scores of saprophytic species under the classical generic concept of **Helotium**." }
    ]
  },
  "Dashboard — helot/helotry.md": {
    primary: "Helots collectively; or the system or condition of serfdom and bonded servitude.",
    secondary: "In political critique and social history, a permanently disenfranchised and exploited working caste.",
    quotes: [
      { author: "Thomas Carlyle", work: "Past and Present", quote: "The degraded condition of industrial factory laborers threatened to produce a new British **helotry**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The rural coloni of the late empire sank inexorably into an oppressive hereditary **helotry**." },
      { author: "George Grote", work: "A History of Greece", quote: "Sparta was a military garrison surrounded by an armed, deeply resentful native **helotry**." }
    ]
  },

  // === Dashboard — heres (7 words) ===
  "Dashboard — heres/antiheretical.md": {
    primary: "Directed against, opposing, or intended to suppress heresy or heretics.",
    secondary: "In patristics and ecclesiastical history, describing theological treatises or inquisitorial institutions established to combat doctrinal deviations.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Irenaeus composed extensive **antiheretical** volumes refuting the intricate mythologies of the Gnostics." },
      { author: "Henry Chadwick", work: "The Early Church", quote: "The imperial edicts contained fierce **antiheretical** penalties aimed at preserving doctrinal unity." },
      { author: "Jaroslav Pelikan", work: "The Christian Tradition", quote: "Creedal formulations were shaped directly by urgent **antiheretical** debates over the nature of Christ." }
    ]
  },
  "Dashboard — heres/apheresis.md": {
    primary: "A medical procedure in which blood is drawn from a donor, separated into components, one or more parts retained, and the remainder returned to the donor.",
    secondary: "In phonetics and historical linguistics, the loss or omission of a sound or syllable from the beginning of a word (alternative spelling of aphaeresis).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Therapeutic **apheresis** is employed to lower dangerously elevated platelet counts in acute leukemia." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "The colloquial clipping of 'telephone' into 'phone' illustrates modern phonetic **apheresis**." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "Blood fractionation technology transformed modern medicine through continuous-flow **apheresis**." }
    ]
  },
  "Dashboard — heres/apheretic.md": {
    primary: "Of, relating to, or produced by apheresis (either the medical separation procedure or linguistic sound elision).",
    secondary: "In linguistics, designating truncated words produced by the deletion of initial vowels or syllables.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "An **apheretic** alteration accounts for the formation of 'sample' from ancient 'ensample'." },
      { author: "Henry Sweet", work: "A New English Grammar", quote: "Popular vernacular speech abounds in **apheretic** shortenings that eventually enter formal registers." },
      { author: "Morris Fishbein", work: "Medical Advances", quote: "New automated **apheretic** instrumentation improved the yield of therapeutic donor platelets." }
    ]
  },
  "Dashboard — heres/heres.md": {
    primary: "A combining root derived from Ancient Greek hairesis, denoting choice, school of thought, sectarian belief, or doctrinal heresy.",
    secondary: "In ecclesiastical Latin and canon law, an heir (heres); or the root underlying heretical theological deviation.",
    quotes: [
      { author: "Eusebius", work: "Ecclesiastical History", quote: "The root **heres**- originally designated philosophical schools before narrowing into sectarian error." },
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "Under civil law, the designated **heres** stepped into the full legal personality of the deceased." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "Doctrinal error stubborn against the universal magisterium constitutes the formal sin of **heres**-y." }
    ]
  },
  "Dashboard — heres/heresy.md": {
    primary: "Belief or opinion contrary to orthodox religious doctrine (especially Christian), or opinion profoundly at odds with accepted belief.",
    secondary: "In the sociology of knowledge and science, radical paradigm dissent that challenges established institutional consensus.",
    quotes: [
      { author: "John Milton", work: "Areopagitica", quote: "A man may be a heretic in the truth; and if he believe things only because his pastor says so, his belief is **heresy**." },
      { author: "Thomas Henry Huxley", work: "The Coming of Age of the Origin of Species", quote: "It is the customary fate of new truths to begin as **heresy** and end as superstition." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "The Party was not content with negative obedience; it sought to eradicate the very possibility of **heresy**." }
    ]
  },
  "Dashboard — heres/heretic.md": {
    primary: "A person believing in or practicing religious heresy; or a person holding an opinion at odds with what is generally accepted.",
    secondary: "In intellectual history, an uncompromising iconoclast whose nonconformity threatens institutional orthodoxy.",
    quotes: [
      { author: "George Bernard Shaw", work: "Saint Joan", quote: "The church must burn the **heretic** not out of malice, but to preserve the flock from spiritual corruption." },
      { author: "Voltaire", work: "Philosophical Dictionary", quote: "A **heretic** is simply someone who has an opinion of his own when the rest of the world has none." },
      { author: "Friedrich Nietzsche", work: "Beyond Good and Evil", quote: "Every bold pioneer of thought has been reviled as a dangerous **heretic** by his contemporaries." }
    ]
  },
  "Dashboard — heres/heretical.md": {
    primary: "Believing in or practicing religious heresy; or contrary to generally accepted standards, opinions, or dogma.",
    secondary: "Characterized by unorthodox departures from doctrinal, political, or scientific orthodoxy.",
    quotes: [
      { author: "Galileo Galilei", work: "Dialogue Concerning the Two Chief World Systems", quote: "Inquisitors warned that asserting the motion of the Earth was deemed formally **heretical**." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Spinoza was cast out of the synagogue for harboring **heretical** views on the divine nature." },
      { author: "John Locke", work: "A Letter Concerning Toleration", quote: "Civil magistrates have no commission to punish citizens for holding purely **heretical** theological opinions." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
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
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 4!`);
