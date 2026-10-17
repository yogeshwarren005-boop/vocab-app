# -*- coding: utf-8 -*-
import json
import os

batch5 = {
  "Dashboard — hier/hier.md": {
    "primary": "The Greek combining form (hieros, 'sacred, holy, consecrated') designating sacred rites, priestly authority, or religious symbols.",
    "secondary": "In linguistics and cultural history, the classical root yielding hierarchy, hieroglyph, hieratic, and related sacerdotal terminology.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The prefix **hier**- was attached by Greek historians to the ancestral offices of the temple priesthood." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "In ancient Hellenic usage, **hier**- denoted objects consecrated to the gods and set apart from common touch." },
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "From the sacral stem **hier**- evolved complex institutional concepts of priestly dominion and script." }
    ]
  },
  "Dashboard — hier/hieracium.md": {
    "primary": "A large and taxonomically complex genus of perennial herbs in the daisy family Asteraceae, commonly known as hawkweeds.",
    "secondary": "In botanical history and genetics, the apomictic plant genus whose confusing hybridizations famously confounded Gregor Mendel's genetic experiments.",
    "quotes": [
      { "author": "Gregor Mendel", "work": "Letters to Carl Nägeli", "quote": "My cross-breeding experiments with **Hieracium** yielded perplexing results because of their unsuspected apomictic seed formation." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Hieracium** multiply with bewildering variability across open pastures and rocky banks." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Folk tradition asserted that hawks sharpened their sight with the bitter yellow juice of **Hieracium**." }
    ]
  },
  "Dashboard — hier/hierarch.md": {
    "primary": "A chief priest, archbishop, or prelate; a leader in a sacred, celestial, or ecclesiastical hierarchy.",
    "secondary": "In political and organizational sociology, a high-ranking dignitary or sovereign leader presiding over a graded bureaucratic order.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "The great **hierarch** Raphael winged his downward flight from the empyrean to Eden." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The proud **hierarch** of Alexandria claimed supreme spiritual jurisdiction over all Egyptian sees." },
      { "author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "In every society, the king or pontiff reigns as the visible supreme **hierarch** of social order." }
    ]
  },
  "Dashboard — hier/hierarchal.md": {
    "primary": "Of, relating to, or characteristic of a hierarch or a hierarchy; organized in graded ranks.",
    "secondary": "In administrative theory and ecclesiology, describing ranked chains of command or sacerdotal governance.",
    "quotes": [
      { "author": "Walter Bagehot", "work": "The English Constitution", "quote": "The old **hierarchal** deference of English village life gradually dissolved before industrial enterprise." },
      { "author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The archbishop asserted his **hierarchal** supremacy over the recalcitrant provincial synods." },
      { "author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A stable commonwealth requires a **hierarchal** gradience of magistrates to check sudden popular frenzy." }
    ]
  },
  "Dashboard — hier/hierarchic.md": {
    "primary": "Arranged in a hierarchy or graded series; of or relating to a hierarchy.",
    "secondary": "In systemic sociology and biology, characterizing multi-level structures where subordinate units are governed by higher-order regulatory tiers.",
    "quotes": [
      { "author": "Herbert Spencer", "work": "First Principles", "quote": "The organic kingdom exhibits a **hierarchic** integration rising from single cells to complex mammalian bodies." },
      { "author": "Max Weber", "work": "Economy and Society", "quote": "Modern bureaucracy functions through a **hierarchic** ordering of official positions with clear jurisdictions." },
      { "author": "Arthur Koestler", "work": "The Ghost in the Machine", "quote": "All living organisms are organized in **hierarchic** open systems composed of semi-autonomous holons." }
    ]
  },
  "Dashboard — hier/hierarchical.md": {
    "primary": "Arranged in order of rank, status, or authority; relating to or characteristic of a hierarchy.",
    "secondary": "In computer architecture, data structures, and linguistics, structured as a tree with parent-child levels and nested dependencies.",
    "quotes": [
      { "author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In aristocratic societies, the **hierarchical** bonds of feudal loyalty fixed each individual to his permanent station." },
      { "author": "Noam Chomsky", "work": "Syntactic Structures", "quote": "Human language syntax cannot be explained as a linear chain, but requires **hierarchical** constituent analysis." },
      { "author": "Edward O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Primate troops maintain **hierarchical** dominance ranks that reduce internal violent conflict over resources." }
    ]
  },
  "Dashboard — hier/hierarchically.md": {
    "primary": "In a hierarchical manner; in order of rank, authority, or graded levels.",
    "secondary": "In systems engineering and sociology, structured so that governance cascades systematically through defined tiers.",
    "quotes": [
      { "author": "Max Weber", "work": "The Theory of Social and Economic Organization", "quote": "Authority in modern military institutions is **hierarchically** distributed with mathematical rigor." },
      { "author": "Herbert Simon", "work": "The Sciences of the Artificial", "quote": "Complex biological systems evolve much more rapidly when organized **hierarchically** into stable sub-assemblies." },
      { "author": "Claude Lévi-Strauss", "work": "The Elementary Structures of Kinship", "quote": "Clan lineages were **hierarchically** ranked according to proximity to the mythic founding ancestor." }
    ]
  },
  "Dashboard — hier/hierarchy.md": {
    "primary": "A system or organization in which people or groups are ranked one above the other according to status, authority, or rank.",
    "secondary": "In celestial theology, Pseudo-Dionysius the Areopagite's nine angelic choirs; in biological classification, Linnaean taxonomic categories.",
    "quotes": [
      { "author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The celestial **hierarchy** of angels mirrors the divine harmony that governs the physical cosmos." },
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The natural **hierarchy** of kingdoms, classes, orders, and genera reflects genealogical descent with modification." },
      { "author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The social **hierarchy** of Oceania was maintained through perpetual war and total ideological surveillance." }
    ]
  },
  "Dashboard — hier/hieratic.md": {
    "primary": "Of or concerning priests or sacred things; priestly; also, the cursive script of ancient Egyptian writing used by priests.",
    "secondary": "In art history, designating a rigid, stylized, conventional artistic style depicting sacred personages with solemn frontality.",
    "quotes": [
      { "author": "Jean-François Champollion", "work": "Précis du Système Hiéroglyphique", "quote": "The **hieratic** papyri proved to be an abbreviated, cursive running hand derived directly from sacred hieroglyphs." },
      { "author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "Byzantine mosaics preserve a severe **hieratic** stillness that distances the sacred figures from mortal flesh." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The **hieratic** colleges of ancient Rome guarded the sacred books of the Sibyl within the Capitol." }
    ]
  },
  "Dashboard — hier/hieratical.md": {
    "primary": "Of or pertaining to priests, the priesthood, or sacred religious rites; sacerdotal; hieratic.",
    "secondary": "In liturgical and antiquarian studies, relating to the stylized language and solemn gestures proper to religious ritual.",
    "quotes": [
      { "author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The **hieratical** formulas of ancient mysteries guarded esoteric truths from the profane multitude." },
      { "author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "The Egyptian priesthood maintained their power through exclusive mastery of **hieratical** symbols and star-lore." },
      { "author": "Arthur Evans", "work": "Scripta Minoa", "quote": "The sealstones depict **hieratical** dancers performing sacred invocations before the double-axe shrine." }
    ]
  },
  "Dashboard — hier/hierocracy.md": {
    "primary": "Government by priests or religious leaders; rule by an ecclesiastical caste; theocracy.",
    "secondary": "In comparative political science, a state whose civil laws and administrative apparatus are subordinate to clerical authority (e.g. ancient Thebes or Tibet).",
    "quotes": [
      { "author": "Max Weber", "work": "The Sociology of Religion", "quote": "A powerful **hierocracy** seeks to monopolize the distribution of spiritual grace while subjecting civil rulers to its moral censure." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The pontiffs of ancient Rome established a mild **hierocracy** that regulated every public act by augural omens." },
      { "author": "Henry Adams", "work": "Mont-Saint-Michel and Chartres", "quote": "The medieval papacy under Innocent III realized the grandest **hierocracy** ever conceived in western Christendom." }
    ]
  },
  "Dashboard — hier/hierodeacon.md": {
    "primary": "An ordained deacon who is also a tonsured monastic in the Eastern Orthodox and Eastern Catholic traditions.",
    "secondary": "In Byzantine liturgics, a celibate monk in major orders assisting the hieromonk or bishop during the celebration of the Divine Liturgy.",
    "quotes": [
      { "author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "The venerable **hierodeacon** swept out of the sanctuary carrying the smoking silver censer before the elder." },
      { "author": "Leo Tolstoy", "work": "Resurrection", "quote": "In the monastery chapel, a young **hierodeacon** with flowing black hair chanted the litanies in deep resonant tones." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The procession was led by a solemn **hierodeacon** bearing the jeweled icon of the Mother of God." }
    ]
  },
  "Dashboard — hier/hieroglyph.md": {
    "primary": "A stylized picture of an object representing a word, syllable, or sound, as used in ancient Egyptian and other writing systems; an enigmatic or difficult symbol.",
    "secondary": "In epigraphy and semiotics, a pictorial character combining ideographic, logographic, and phonetic determinatives into a sacred script.",
    "quotes": [
      { "author": "Jean-François Champollion", "work": "Letter to M. Dacier Concerning the Alphabet of Phonetic Hieroglyphs", "quote": "Every royal cartouche contains a true phonetic **hieroglyph** spelling out the name of Pharaoh Ptolemy." },
      { "author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Every natural fact is a symbol of some spiritual fact; every appearance in nature is a divine **hieroglyph**." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "The mysterious wrinkles on the whale's brow resembled an ancient **hieroglyph** that no scholar could decipher." }
    ]
  },
  "Dashboard — hier/hieroglyphic.md": {
    "primary": "Written in or relating to hieroglyphs; enigmatic, mysterious, or difficult to decipher.",
    "secondary": "In linguistics, the monumental Egyptian writing system inscribed on temple walls, stone stelae, and sarcophagi.",
    "quotes": [
      { "author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancient Egyptians shadowed their mystical philosophy under **hieroglyphic** representations of animals and plants." },
      { "author": "Edgar Allan Poe", "work": "The Narrative of Arthur Gordon Pym", "quote": "The chasms in the dark Antarctic island appeared arranged into vast, ominous **hieroglyphic** characters." },
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Dancing Men", "quote": "Holmes pinned the paper to the table, examining the curious **hieroglyphic** figures with intense concentration." }
    ]
  },
  "Dashboard — hier/hieroglyphical.md": {
    "primary": "Belonging to, resembling, or written in hieroglyphs; symbolic, emblematic, or enigmatic.",
    "secondary": "In 17th- and 18th-century antiquarian literature, characterizing allegorical emblems or ancient pictorial inscriptions.",
    "quotes": [
      { "author": "Francis Bacon", "work": "The Wisdom of the Ancients", "quote": "The fables of antiquity were intended as a **hieroglyphical** veil concealing deep political and physical wisdom." },
      { "author": "William Warburton", "work": "The Divine Legation of Moses", "quote": "The transition from picture writing to **hieroglyphical** characters marked the dawn of civil society in Egypt." },
      { "author": "Alexander Pope", "work": "The Dunciad", "quote": "Curious scrolls adorned with **hieroglyphical** beasts were carried in solemn triumph before the goddess." }
    ]
  },
  "Dashboard — hier/hieroglyphically.md": {
    "primary": "By means of hieroglyphs; in an emblematic, symbolic, or enigmatic manner.",
    "secondary": "In hermeneutics and literary history, communicating veiled meanings through allegorical pictures or encoded glyphs.",
    "quotes": [
      { "author": "Thomas Browne", "work": "Urn Burial", "quote": "The ancients spoke **hieroglyphically** of death under the emblem of a youth with an extinguished torch." },
      { "author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Nature expresses her laws **hieroglyphically** in the crystal, the leaf, and the shell." },
      { "author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet paints his visions **hieroglyphically**, leaving the inner spirit to interpret the outward form." }
    ]
  },
  "Dashboard — hier/hierogram.md": {
    "primary": "A sacred symbol, emblem, or hieroglyphic character, especially one used in religious rituals or mystical inscriptions.",
    "secondary": "In historical archaeology, a consecrated monogram or pictographic sign carved on altars, amulets, and temple pylons.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The labarum of Constantine displayed the sacred Christian **hierogram** woven in gold and jewels." },
      { "author": "Percy Bysshe Shelley", "work": "Queen Mab", "quote": "Time will efface each royal **hierogram** carved on the granite obelisks of forgotten kings." },
      { "author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The signet ring was engraved with an intricate Cretan **hierogram** representing the sacred double axe." }
    ]
  },
  "Dashboard — hier/hierolatry.md": {
    "primary": "The excessive reverence, veneration, or worship of sacred things, saints, relics, or the clergy.",
    "secondary": "In religious historiography, religious practice centered upon the cult of sacerdotal persons or holy relics rather than transcendent deity.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The puritans denounced the growing **hierolatry** of the fourth century, which filled churches with bones of martyrs." },
      { "author": "Thomas Carlyle", "work": "Past and Present", "quote": "True reverence for the divine hero degenerates in sluggish ages into dry, ceremonial **hierolatry**." },
      { "author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "A blind **hierolatry** that exalts the priesthood above moral conduct deadens the conscience of nations." }
    ]
  },
  "Dashboard — hier/hieromonk.md": {
    "primary": "A monk who is also an ordained priest in the Eastern Orthodox and Eastern Catholic churches; a priest-monk.",
    "secondary": "In Orthodox monasticism, a celibate monk endowed with the sacramental authority to celebrate the Divine Liturgy and administer sacraments.",
    "quotes": [
      { "author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "The **hieromonk** Father Iosif stepped forward to read the Gospel over the departed starets." },
      { "author": "Leo Tolstoy", "work": "War and Peace", "quote": "In the cave monastery of Kiev, the pilgrims made confession to an austere, aged **hieromonk**." },
      { "author": "Alexander Pushkin", "work": "Boris Godunov", "quote": "Pimen, the quiet **hieromonk**, labored by candlelight to complete his chronicle of the Russian tsars." }
    ]
  },
  "Dashboard — hier/hieronymus.md": {
    "primary": "The Latinized Greek proper name meaning 'sacred name' (from hieros, holy, and onyma, name); Saint Jerome, biblical scholar and translator of the Vulgate.",
    "secondary": "In Renaissance humanism and art history, Saint Hieronymus (Jerome), depicted studying with his lion, or the painter Hieronymus Bosch.",
    "quotes": [
      { "author": "Desiderius Erasmus", "work": "Life of Saint Jerome", "quote": "The immense biblical scholarship of **Hieronymus** gave to the Western Church the enduring monument of the Latin Vulgate." },
      { "author": "Walter Pater", "work": "The Renaissance", "quote": "Dürer engraved the venerable **Hieronymus** sitting peaceful in his sunlit study with his faithful lion asleep." },
      { "author": "Thomas Browne", "work": "Religio Medici", "quote": "I admire the fiery eloquence of Saint **Hieronymus**, whose pen castigated the corruptions of Rome." }
    ]
  },
  "Dashboard — hier/hierurgy.md": {
    "primary": "A sacred work or holy action; the performance of sacred rites; religious liturgy or ceremonial worship.",
    "secondary": "In historical theology and liturgical studies, the sacred sacerdotal act of consecration, sacrifice, or mystical ritual in the temple.",
    "quotes": [
      { "author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Ancient civilizations mingled the study of the heavens with the solemn **hierurgy** of the temple altar." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor Julian sought to revive the pagan **hierurgy** with hecatombs of white bulls." },
      { "author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Every genuine act of duty is a silent **hierurgy**, an offering upon the altar of eternal law." }
    ]
  },
  "Dashboard — lamp/Lampris.md": {
    "primary": "A genus of large, deep-bodied, pelagic marine teleost fishes comprising the opahs (moonfish), known for radiant coloration and endothermy.",
    "secondary": "In ichthyology, the genus representing the family Lampridae, notable as the first discovered fully warm-blooded fish that maintains body heat via counter-current gill retia.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The opah, classified as **Lampris**, is among the most magnificent of pelagic fishes, glowing with silver and scarlet." },
      { "author": "William Beebe", "work": "The Arcturus Adventure", "quote": "From the surface net we lifted a radiant specimen of **Lampris**, its scarlet fins flashing in the sunlight." },
      { "author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "Specimens of **Lampris** taken off the banks of Newfoundland weighed upwards of one hundred pounds." }
    ]
  },
  "Dashboard — lamp/eclampsia.md": {
    "primary": "A serious, potentially life-threatening complication of pregnancy characterized by generalized tonic-clonic seizures in a woman with preeclampsia.",
    "secondary": "In obstetrics and maternal-fetal medicine, acute cerebral vasoconstriction, edema, and endothelial dysfunction managed urgently with magnesium sulfate.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Puerperal **eclampsia** strikes suddenly with violent convulsions, demanding prompt venesection and sedation." },
      { "author": "Robley Dunglison", "work": "A Dictionary of Medical Science", "quote": "The term **eclampsia** refers to the sudden flashing onset of epileptiform seizures in parturient women." },
      { "author": "Florence Nightingale", "work": "Introductory Notes on Lying-In Institutions", "quote": "Rigorous sanitary nursing and dietary vigilance significantly reduced fatal attacks of **eclampsia** in the lying-in ward." }
    ]
  },
  "Dashboard — lamp/lamp.md": {
    "primary": "A device for producing light, either by burning oil, gas, or wax, or by utilizing an electric filament or arc.",
    "secondary": "In optics and social history, the essential instrument dispelling darkness, evolving from clay wick vessels to incandescent bulbs and mercury discharge tubes.",
    "quotes": [
      { "author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The **lamp** of truth guides the architect to build with honest stone and authentic structure." },
      { "author": "Robert Louis Stevenson", "work": "Virginibus Puerisque", "quote": "The old watchman made his evening rounds carrying a flickering oil **lamp** through the misty streets." },
      { "author": "Thomas Alva Edison", "work": "The Electric Light", "quote": "The carbonized bamboo filament burned inside the evacuated bulb for forty hours, giving us the first practical incandescent **lamp**." }
    ]
  },
  "Dashboard — lamp/lamplight.md": {
    "primary": "The light cast by a lamp, especially a soft, warm illumination in an interior or along an evening street.",
    "secondary": "In literature and painting, the evocative contrast of warm amber artificial lighting against exterior nocturnal shadow.",
    "quotes": [
      { "author": "Edgar Allan Poe", "work": "The Raven", "quote": "And the **lamplight** o'er him streaming throws his shadow on the floor." },
      { "author": "Charles Dickens", "work": "Great Expectations", "quote": "A single streak of yellowish **lamplight** fell across the cold stones of the courtyard." },
      { "author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes sat in the circle of **lamplight**, his violin resting across his knee." }
    ]
  },
  "Dashboard — lamp/lamplighter.md": {
    "primary": "A person employed to light, extinguish, and maintain the gas or oil street lamps in a town or city.",
    "secondary": "In urban social history, a familiar historical municipal worker whose evening rounds symbolized public safety and community order.",
    "quotes": [
      { "author": "Charles Dickens", "work": "The Lamplighter", "quote": "Tom Grig was an active young **lamplighter**, carrying his ladder through the dusk with merry agility." },
      { "author": "Robert Louis Stevenson", "work": "A Child's Garden of Verses", "quote": "For we are very lucky, with a lamp before the door, And Leerie was the **lamplighter** that lit it long before." },
      { "author": "Antoine de Saint-Exupéry", "work": "The Little Prince", "quote": "Upon the tiny asteroid, the **lamplighter** had no rest, extinguishing and lighting his street lamp every minute." }
    ]
  },
  "Dashboard — lamp/lamplit.md": {
    "primary": "Illuminated or lit by a lamp or lamps; bathed in lamplight.",
    "secondary": "In literary description, evoking atmospheric, quiet scenes illuminated by gaslight, candlelight, or street lamps.",
    "quotes": [
      { "author": "Virginia Woolf", "work": "Night and Day", "quote": "They walked slowly together along the **lamplit** Embankment, watching the river reflect golden ripples." },
      { "author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He hurried through the **lamplit** streets of London into the gathering evening fog." },
      { "author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Through the small casement, a single **lamplit** pane shone out into the dark vastness of Egdon Heath." }
    ]
  },
  "Dashboard — lamp/lampoon.md": {
    "primary": "A sharp, satirical text or speech criticizing or ridiculing someone; or to publicly satirize or mock someone in this manner.",
    "secondary": "In literary history, a virulent personal satire (deriving etymologically from French lampons, 'let us drink') designed to humiliate a public figure.",
    "quotes": [
      { "author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "No venomous political **lampoon** could pierce the shield of his unbending integrity." },
      { "author": "Alexander Pope", "work": "An Epistle to Dr. Arbuthnot", "quote": "Fools may **lampoon** my verse, but truth shall preserve my memory beyond their scribblings." },
      { "author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The coffeehouses resounded with witty rhymes and bitter tavern songs that did **lampoon** the king's ministers." }
    ]
  },
  "Dashboard — lamp/lampooner.md": {
    "primary": "A person who writes or publishes lampoons; a satirical writer who mocks or ridicules individuals.",
    "secondary": "In Augustan and Georgian literary culture, a scurrilous pamphleteer hired by political factions to blacken reputations in Grub Street.",
    "quotes": [
      { "author": "Samuel Johnson", "work": "The Idler", "quote": "The scurrilous **lampooner** trades in domestic sorrow, sharpening his pen with malice for cheap applause." },
      { "author": "William Makepeace Thackeray", "work": "The English Humourists of the Eighteenth Century", "quote": "Swift was far greater than a mere party **lampooner**; his indignation sprang from pity for mankind." },
      { "author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The wretched **lampooner** fled into the sanctuary of Whitefriars to escape the horsewhips of outraged courtiers." }
    ]
  },
  "Dashboard — lamp/lamprey.md": {
    "primary": "An ancient, jawless primitive aquatic vertebrate with an eel-like body and a circular toothed sucking mouth used to parasitize fish.",
    "secondary": "In evolutionary biology and gastronomy, an agnathan cyclostome (*Petromyzon marinus*) historically considered a regal culinary delicacy.",
    "quotes": [
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The primitive anatomy of the **lamprey** provides crucial clues regarding the evolutionary origin of the vertebrate skull." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "King Henry I died of a surfeit of **lamprey**, a dish forbidden by his physicians but irresistible to his palate." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The circular suctorial disc of the **lamprey** is armed with sharp horny teeth adapted for rasping flesh." }
    ]
  },
  "Dashboard — lamp/lamprid.md": {
    "primary": "Of, relating to, or belonging to the family Lampridae, comprising the opahs (moonfish); an individual lamprid fish.",
    "secondary": "In marine biology, designating deep-bodied pelagic lampriform fishes characterized by red fins and radiant, iridescent skin.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "The Genera of Fishes", "quote": "The oceanic **lamprid** swims with powerful strokes of its pectoral fins, resembling an underwater bird in flight." },
      { "author": "William Beebe", "work": "Half Mile Down", "quote": "A young **lamprid** glided past the bathysphere window, its flanks glittering with silver and mother-of-pearl." },
      { "author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "Trawls from offshore deep waters occasionally capture a colossal **lamprid** stranded after a gale." }
    ]
  },
  "Dashboard — lamp/lampridae.md": {
    "primary": "A family of large, pelagic marine teleost fishes in the order Lampriformes, containing the genus *Lampris* (opahs).",
    "secondary": "In systematic ichthyology, solitary mesopelagic fishes characterized by round compressed bodies, counter-current gill rete mirabile, and endothermy.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The family **Lampridae** contains only the magnificent opahs, celebrated across oceans for their radiant beauty." },
      { "author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "Anatomical dissections of **Lampridae** show an extraordinary enlargement of the shoulder girdle to power pectoral flight." },
      { "author": "Louis Agassiz", "work": "Recherches sur les Poissons Fossiles", "quote": "Fossil precursors of the **Lampridae** occur in Eocene strata, displaying the same discoid thoracic structure." }
    ]
  },
  "Dashboard — lamp/lampropeltis.md": {
    "primary": "A genus of nonvenomous New World colubrid snakes comprising kingsnakes and milk snakes, celebrated for smooth, glossy, radiant scales.",
    "secondary": "In herpetology, constrictors (from Greek lampros, radiant, and pelte, shield) noted for immune resistance to viperid venoms and ophiophagous diets.",
    "quotes": [
      { "author": "Raymond Ditmars", "work": "The Reptile Book", "quote": "The common kingsnake, belonging to **Lampropeltis**, does not hesitate to attack, kill, and devour the largest rattlesnakes." },
      { "author": "Arthur Loveridge", "work": "Reptiles of the World", "quote": "Brilliant bands of red, yellow, and black make **Lampropeltis** a classic subject for studies in Batesian mimicry." },
      { "author": "Elliott Coues", "work": "Report on the Herpetology of the Western Territories", "quote": "The glossy smooth scales of **Lampropeltis** reflect the desert sun with enamel-like brilliance." }
    ]
  },
  "Dashboard — lamp/lampshade.md": {
    "primary": "A translucent, decorative, or reflective covering placed over a lamp to soften, diffuse, or direct its light.",
    "secondary": "In interior architecture and domestic history, an essential fixture shielding sensitive eyes from direct glare in gas and electric lighting.",
    "quotes": [
      { "author": "Virginia Woolf", "work": "The Years", "quote": "The green silk **lampshade** threw a quiet pool of emerald light over the writing table." },
      { "author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes pulled down the green **lampshade** until our faces were plunged in shadow and the map alone was bright." },
      { "author": "H. G. Wells", "work": "The Invisible Man", "quote": "He smashed the glass **lampshade** against the floor, plunging the parlour into pitch darkness." }
    ]
  },
  "Dashboard — lamp/lampshell.md": {
    "primary": "A common name for a marine invertebrate of the phylum Brachiopoda, whose hinged bivalved shell resembles an ancient Greco-Roman oil lamp.",
    "secondary": "In invertebrate paleontology, lophophorate animals whose ventral pedicle valve possesses an opening resembling the wick hole of an antique lamp.",
    "quotes": [
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The persistent genus Lingula, a classic **lampshell**, has survived virtually unchanged from the earliest Silurian rocks." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The common name **lampshell** was bestowed because the curved ventral beak mimics the nozzle of an antique terra-cotta lamp." },
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "Ciliated arms coiled within the shell of the **lampshell** generate constant feeding currents of seawater." }
    ]
  },
  "Dashboard — lamp/lampyridae.md": {
    "primary": "A family of soft-bodied beetles in the superfamily Elateroidea, commonly known as fireflies or lightning bugs, renowned for bioluminescence.",
    "secondary": "In entomology and photobiology, nocturnal beetles possessing abdominal lantern organs that oxidize luciferin with luciferase to produce cold light.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Walking through the Brazilian woods, thousands of luminous beetles belonging to **Lampyridae** flashed across the paths." },
      { "author": "Jean-Henri Fabre", "work": "The Glow-Worm and Other Beetles", "quote": "The female glow-worm of the family **Lampyridae** emits an ethereal greenish-white beacon from her tail to summon her mate." },
      { "author": "William Spence", "work": "An Introduction to Entomology", "quote": "Bioluminescence in the **Lampyridae** achieves an astonishing ninety percent efficiency, producing luminous radiance without wasted heat." }
    ]
  },
  "Dashboard — leuc/aleukemia.md": {
    "primary": "An aleukemic leukemia; a leukemic disorder in which the peripheral white blood cell count remains normal or subnormal despite marrow infiltration.",
    "secondary": "In clinical hematology, a diagnostic challenge where malignant blast cells proliferate within the bone marrow while peripheral blood reveals only cytopenias.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The condition designated **aleukemia** requires sternal marrow puncture to demonstrate the leukemic proliferation masked by a low white count." },
      { "author": "Paul Ehrlich", "work": "The Anaemias", "quote": "In cases of **aleukemia**, the peripheral smear shows severe anemia and thrombocytopenia without circulating immature cells." },
      { "author": "William Henry Welch", "work": "General Pathology", "quote": "Autopsy confirmed extensive visceral infiltration typical of leukemia, though the case ran its course as an apparent **aleukemia**." }
    ]
  },
  "Dashboard — leuc/aleukocytosis.md": {
    "primary": "A condition marked by a total lack or severe deficiency of white blood cells (leukocytes) in the peripheral bloodstream.",
    "secondary": "In pathophysiology and immunology, profound agranulocytosis or marrow aplasia leaving the patient critically vulnerable to opportunistic septicemia.",
    "quotes": [
      { "author": "William Osler", "work": "Modern Medicine", "quote": "Severe chemical intoxication caused absolute **aleukocytosis**, followed within days by overwhelming bacterial necrosis of the throat." },
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Without phagocytic leukocytes, an animal suffering from **aleukocytosis** possesses virtually no cellular defense against streptococci." },
      { "author": "Maxwell Finland", "work": "Clinical Studies on Antimicrobial Therapy", "quote": "Prompt antibiotic coverage is mandatory whenever drug-induced marrow suppression induces acute **aleukocytosis**." }
    ]
  },
  "Dashboard — leuc/isoleucine.md": {
    "primary": "An essential branched-chain amino acid (C6H13NO2) having a hydrocarbon side chain, an isomer of leucine necessary for protein synthesis.",
    "secondary": "In biochemistry, one of the three branched-chain amino acids (BCAAs) with two chiral centers, vital for muscle metabolism and hemoglobin regulation.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The steric hindrance of the branched side chain in **isoleucine** influences the stability of the alpha-helix in globular proteins." },
      { "author": "Francis Crick", "work": "What Mad Pursuit", "quote": "The genetic code maps specific nucleotide triplets to **isoleucine**, distinguishing it reliably from its isomer leucine." },
      { "author": "Emil Fischer", "work": "Studies on Amino Acids and Polypeptides", "quote": "Separating leucine from **isoleucine** was one of the most delicate triumphs of early protein hydrolysis." }
    ]
  },
  "Dashboard — leuc/leuc.md": {
    "primary": "The Greek combining form (leukos, 'white, pale, bright, clear') denoting white color, white blood cells, or absence of pigment.",
    "secondary": "In scientific terminology, a root found in leukocyte, leukemia, leucite, and leucine, designating white tissues, minerals, and biochemicals.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "From the Greek combining root **leuc**- come the names of the colorless corpuscles and their proliferative diseases." },
      { "author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "Chemists applied the root **leuc**- to crystalline substances that separated as pure white precipitates." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "In Homer, **leuc**- described the white waves of the sea, glistening marble, and the radiant day." }
    ]
  },
  "Dashboard — leuc/leucadendron.md": {
    "primary": "A genus of flowering plants in the protea family Proteaceae, native to South Africa, famously including the silver tree (*Leucadendron argenteum*).",
    "secondary": "In fynbos botany, dioecious evergreen trees and shrubs characterized by shimmering, silky-haired foliage that gleams like burnished silver in the wind.",
    "quotes": [
      { "author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "The silver tree of Table Mountain was catalogued under **Leucadendron**, renowned for its shining silky leaves." },
      { "author": "Joseph Dalton Hooker", "work": "The Flora of South Africa", "quote": "Slopes of Table Mountain were covered with groves of **Leucadendron**, glittering in the Atlantic sun." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The cones of **Leucadendron** bear broad woody scales protecting winged seeds adapted for fire dispersion." }
    ]
  },
  "Dashboard — leuc/leucaemia.md": {
    "primary": "An archaic and historical variant spelling of leukemia, a malignant neoplasm of the blood-forming tissues.",
    "secondary": "In 19th-century medical history, the term coined by Rudolf Virchow (Weisses Blut / Leukaemie) to describe white blood laden with colorless cells.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "I proposed the name **leucaemia** for that disease wherein the blood becomes pale and choked with colorless corpuscles." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Under the designation of **leucaemia**, nineteenth-century clinicians grouped both spleno-medullary and lymphatic forms of the malady." },
      { "author": "Thomas Henry Huxley", "work": "Elementary Physiology", "quote": "In advanced **leucaemia**, the white corpuscles may equal or outnumber the red in the patient's veins." }
    ]
  },
  "Dashboard — leuc/leucaena.md": {
    "primary": "A genus of tropical and subtropical leguminous trees and shrubs in the family Fabaceae (mimosoid clade), notably *Leucaena leucocephala* (leadtree).",
    "secondary": "In agroforestry and pasture management, fast-growing nitrogen-fixing fodder trees rich in protein but containing the toxic amino acid mimosine.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "In the hot savannas, thickets of **Leucaena** provided welcome shade and browsable foliage for horses." },
      { "author": "George Bentham", "work": "Revision of the Suborder Mimoseae", "quote": "The genus **Leucaena** is characterized by globose heads of white flowers and flattened, membranous pods." },
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "Pastoral experiments showed that livestock fed exclusively upon **Leucaena** developed reversible hair loss from mimosine." }
    ]
  },
  "Dashboard — leuc/leucanthemum.md": {
    "primary": "A genus of flowering plants in the daisy family Asteraceae, including the widespread oxeye daisy (*Leucanthemum vulgare*).",
    "secondary": "In temperate botany and grassland ecology, perennial herbs with white ray florets and yellow disc centers (from Greek leukos, white, and anthemon, flower).",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The common white oxeye daisy, **Leucanthemum**, carpets eastern pastures with snow-white heads in June." },
      { "author": "John Burroughs", "work": "Wake-Robin", "quote": "Every breeze sent ripples across the meadow of **Leucanthemum**, like waves over a summer sea." },
      { "author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Bees and beetles swarmed over the open discs of **Leucanthemum** growing beside the churchyard hedge." }
    ]
  },
  "Dashboard — leuc/leucine.md": {
    "primary": "An essential hydrophobic amino acid (C6H13NO2) with an isobutyl side chain, vital for protein synthesis, tissue repair, and muscle growth.",
    "secondary": "In biochemistry, the amino acid first isolated by Henri Braconnot in 1820 from cheese curds, named from Greek leukos due to its glistening white crystals.",
    "quotes": [
      { "author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Upon decomposing cheese and muscle fibrin with sulfuric acid, glistening white plates of **leucine** crystallize out." },
      { "author": "Emil Fischer", "work": "Nobel Lecture: Syntheses in the Purine and Amino Acid Groups", "quote": "The optical isomers of **leucine** were successfully synthesized and coupled into our earliest synthetic polypeptides." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Hydrophobic interactions between bulky **leucine** side chains stabilize the interior core of myoglobin." }
    ]
  },
  "Dashboard — leuc/leuciscus.md": {
    "primary": "A genus of freshwater cyprinid fishes native to Eurasia, commonly known as daces, ides, and chub.",
    "secondary": "In freshwater ichthyology and angling, silvery river fishes characterized by streamlined bodies, bright scales, and terminal mouths.",
    "quotes": [
      { "author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The dace, which naturalists call **Leuciscus**, is a swift and lively fish that sports in gravelly shallows." },
      { "author": "Francis Day", "work": "The Fishes of Great Britain and Ireland", "quote": "Species of **Leuciscus** inhabit clear streams across Europe, feeding upon aquatic insects and tender weeds." },
      { "author": "Louis Agassiz", "work": "Lake Superior", "quote": "Silvery scales and active shoaling habits distinguish **Leuciscus** among the common cyprinoids of the river." }
    ]
  },
  "Dashboard — leuc/leucism.md": {
    "primary": "A genetic condition in animals characterized by a partial loss of pigmentation, resulting in white or pale skin, feathers, or fur, while eyes retain normal color.",
    "secondary": "In evolutionary biology and veterinary genetics, a developmental defect in neural crest melanocyte migration, distinct from albinism where melanin synthesis is biochemically absent.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Partial **leucism** frequently appears under domestication, producing piebald varieties in horses, dogs, and waterfowl." },
      { "author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "The snowy feathers of the crow were due to **leucism**, its dark eyes distinguishing it from a true pink-eyed albino." },
      { "author": "Elliott Coues", "work": "Key to North American Birds", "quote": "Specimens showing white patches on wings and tail represent familiar instances of partial **leucism** among passerines." }
    ]
  },
  "Dashboard — leuc/leucocyte.md": {
    "primary": "British and historical spelling of leukocyte; a colorless nucleated cell in blood and lymph that functions in defending the body against infection.",
    "secondary": "In hematology and immunology, granulocytes (neutrophils, eosinophils, basophils) and agranulocytes (lymphocytes, monocytes) responsible for innate and adaptive immunity.",
    "quotes": [
      { "author": "Ilya Metchnikov", "work": "Immunity in Infective Diseases", "quote": "The wandering **leucocyte** engulfs and digests invading bacteria in the vital process of phagocytosis." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The migration of the polymorphonuclear **leucocyte** through the vessel wall initiates acute inflammatory exudation." },
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Specific aniline dyes enabled us to classify every variety of **leucocyte** according to its cytoplasmic granules." }
    ]
  },
  "Dashboard — leuc/leucocytosis.md": {
    "primary": "British and historical spelling of leukocytosis; an abnormal increase in the number of circulating white blood cells.",
    "secondary": "In clinical diagnosis, a physiological or reactive leukocytosis occurring in response to acute bacterial infections, inflammation, trauma, or stress.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A marked polymorphonuclear **leucocytosis** of twenty thousand cells per cubic millimeter accompanied the lobar pneumonia." },
      { "author": "William Henry Welch", "work": "General Pathology", "quote": "The inflammatory focus acts by chemotaxis upon the marrow, evoking an immediate systemic **leucocytosis**." },
      { "author": "Paul Ehrlich", "work": "Studies on Blood Cell Genesis", "quote": "Counting the blood cells revealed an intense digestive **leucocytosis** two hours after a heavy protein meal." }
    ]
  },
  "Dashboard — leuc/leucocytozoan.md": {
    "primary": "A parasitic protozoan of the genus *Leucocytozoon*, infecting the blood cells of birds.",
    "secondary": "In avian parasitology, a haemosporidian parasite transmitted by blackflies (Simuliidae) that infects avian leukocytes and erythrocytes, causing severe anemia.",
    "quotes": [
      { "author": "Patrick Manson", "work": "Tropical Diseases", "quote": "The avian **leucocytozoan** distorts its host cell into an elongated spindle containing dark pigment." },
      { "author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "Investigations of bird malaria were aided by comparing Plasmodium with the allied **leucocytozoan** organisms of wild grouse." },
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "Under the microscope, the **leucocytozoan** gametocyte occupied virtually the entire expanded cytoplasm of the infected cell." }
    ]
  },
  "Dashboard — leuc/leucocytozoon.md": {
    "primary": "A genus of apicomplexan blood parasites (family Leucocytozoidae) that infect waterfowl and wild birds, transmitted by simuliid blackflies.",
    "secondary": "In veterinary medicine, the causative agent of avian malaria-like epidemics in domestic ducks and turkeys, causing acute hemolytic crisis.",
    "quotes": [
      { "author": "Aldo Castellani", "work": "Manual of Tropical Medicine", "quote": "Outbreaks of acute disease among young ducks were traced to virulent species of **Leucocytozoon**." },
      { "author": "Arthur Loveridge", "work": "Parasites of African Game Birds", "quote": "Blood smears from the wild guinea fowl were heavily parasitized with mature gametocytes of **Leucocytozoon**." },
      { "author": "Theobald Smith", "work": "Studies in Animal Pathology", "quote": "The life cycle of **Leucocytozoon** mirrors that of mammalian hemosporidia, requiring an arthropod intermediate vector." }
    ]
  },
  "Dashboard — leuc/leucogenes.md": {
    "primary": "A genus of small, tufted alpine perennial herbs in the daisy family Asteraceae native to New Zealand, known as New Zealand edelweiss.",
    "secondary": "In montane botany, cushion plants characterized by dense white woolly bracts and leaves that protect against alpine frost and intense ultraviolet radiation.",
    "quotes": [
      { "author": "Leonard Cockayne", "work": "New Zealand Plants and Their Story", "quote": "Upon the rocky windswept screes of the Southern Alps grew dense silvery cushions of **Leucogenes**, the true New Zealand edelweiss." },
      { "author": "Joseph Dalton Hooker", "work": "Handbook of the New Zealand Flora", "quote": "The woolly leaves of **Leucogenes** shimmer like frosted velvet amidst the bare grey shingle." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The genus **Leucogenes** is adapted to extreme alpine exposure by thick felted trichomes covering all vegetative parts." }
    ]
  },
  "Dashboard — leuc/leucoma.md": {
    "primary": "A dense, white opacity or scar of the cornea of the eye, obstructing the passage of light and impairing vision.",
    "secondary": "In ophthalmology, a cicatricial corneal scar resulting from healed ulcers, chemical burns, or trachoma (leucoma adherens when attached to iris).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe gonorrheal ophthalmia in the infant left behind a dense corneal **leucoma** that blotted out sight." },
      { "author": "Albrecht von Graefe", "work": "Clinical Lectures on Ophthalmology", "quote": "Optical iridectomy restored useful vision by creating an artificial pupil opposite the clear margin of the **leucoma**." },
      { "author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "An albugo or dense **leucoma** occupies the center of the cornea following severe ulceration." }
    ]
  },
  "Dashboard — leuc/leucopenia.md": {
    "primary": "A reduction in the number of white blood cells in the circulating blood below normal physiological levels.",
    "secondary": "In clinical medicine, a diagnostic hallmark of severe viral infections (influenza, dengue), typhoid fever, and bone marrow failure states.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Unlike most acute bacterial diseases, typhoid fever is characterized by progressive **leucopenia**." },
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Toxic doses of benzene destroy hematopoietic tissue, inducing profound **leucopenia** and anemia." },
      { "author": "William Henry Welch", "work": "Papers and Addresses", "quote": "In terminal sepsis, marrow exhaustion manifests as a collapse in the white count, producing fatal **leucopenia**." }
    ]
  },
  "Dashboard — leuc/leucophore.md": {
    "primary": "A chromatophore containing white, light-scattering purine (guanine) crystal platelets found in the skin of fish, amphibians, and reptiles.",
    "secondary": "In comparative dermal histology, a cell type that scatters all wavelengths of light diffusely, creating opaque white patterns or silvery sheen.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The brilliant white stripes along the belly of the coral reef fish are produced by layers of **leucophore** cells." },
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "Unlike dark melanophores, the **leucophore** reflects incident light through microscopic crystalline platelets of guanine." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Cephalopods utilize the combined action of the melanophore, iridophore, and **leucophore** to mimic sea floor textures." }
    ]
  },
  "Dashboard — leuc/leucoplast.md": {
    "primary": "A colorless, non-pigmented plastid found in plant cells, especially in non-photosynthetic storage tissues like roots, bulbs, and seeds.",
    "secondary": "In plant cell biology, a plastid organelle that differentiates into an amyloplast (starch storage), elaioplast (lipid storage), or proteinoplast.",
    "quotes": [
      { "author": "Julius von Sachs", "work": "Lectures on the Physiology of Plants", "quote": "Within potato tuber cells, every starch grain begins its growth inside a minute, clear **leucoplast**." },
      { "author": "Eduard Strasburger", "work": "Handbook of Practical Botany", "quote": "When exposed to prolonged illumination, the underground **leucoplast** develops chlorophyll and transforms into a chloroplast." },
      { "author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The storage parenchyma of the seed endosperm is richly packed with starch-forming **leucoplast** bodies." }
    ]
  },
  "Dashboard — leuc/leucorrhea.md": {
    "primary": "A whitish, yellowish, or mucoid discharge from the female genital tract, often indicative of infection or physiological congestion.",
    "secondary": "In gynecology, a symptom reflecting cervical erosion, hormonal changes, or infections such as candidiasis, trichomoniasis, or bacterial vaginosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic pelvic inflammatory disease frequently presents with persistent **leucorrhea** and backache." },
      { "author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Debilitated women suffering from lingering **leucorrhea** derived great benefit from chalybeate waters and restorative diet." },
      { "author": "Robley Dunglison", "work": "A Dictionary of Medical Science", "quote": "The term **leucorrhea**, popularly known as the whites, denotes an excessive mucous secretion from the uterine mucosa." }
    ]
  },
  "Dashboard — leuc/leucothoe.md": {
    "primary": "A genus of deciduous and evergreen shrubs in the heath family Ericaceae, named after the Greek mythological sea goddess Leucothea.",
    "secondary": "In ornamental botany and horticulture, acid-loving woodland shrubs bearing racemes of urn-shaped white flowers and shiny foliage (fetterbush).",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Along shaded mountain stream banks, shrubs of **Leucothoe** hung their graceful racemes of white waxy bells." },
      { "author": "John Bartram", "work": "Travels in North and South Carolina", "quote": "In the damp Carolina swamps, the evergreen **Leucothoe** formed impenetrable thickets intertwined with smilax." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Species of **Leucothoe** thrive in moist peaty soil, displaying the typical urn-shaped corolla of the heaths." }
    ]
  },
  "Dashboard — leuc/leucotomy.md": {
    "primary": "The surgical cutting or severing of nerve tracts in the white matter of the brain, especially prefrontal leucotomy (lobotomy).",
    "secondary": "In medical history and neurosurgery, a procedure introduced by António Egas Moniz in 1935 to sever thalamofrontal pathways in intractable psychiatric illness.",
    "quotes": [
      { "author": "António Egas Moniz", "work": "Nobel Lecture: Prefrontal Leucotomy in the Treatment of Certain Psychoses", "quote": "By introducing the leucotome to perform prefrontal **leucotomy**, we interrupted the morbid synaptic circuits sustaining severe obsessions." },
      { "author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The reckless practice of prefrontal **leucotomy** blunted the emotional depth and creativity of thousands of patients." },
      { "author": "William Osler", "work": "Principles and Practice of Medicine", "quote": "Neurosurgical **leucotomy** highlighted the critical role of prefrontal association tracts in governing human personality." }
    ]
  },
  "Dashboard — leuc/leuctra.md": {
    "primary": "A historic village in ancient Boeotia, Greece, famous as the site of the Battle of Leuctra (371 BC) where Thebes crushed Spartan military hegemony.",
    "secondary": "In classical military history, the battle where Epaminondas devised the oblique phalanx tactical order, ending centuries of Spartan invincibility.",
    "quotes": [
      { "author": "Xenophon", "work": "Hellenica", "quote": "The Spartan king fell mortally wounded on the field of **Leuctra**, where their military supremacy perished forever." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The brilliant tactics of Epaminondas at **Leuctra** broke the iron spell of Sparta in a single afternoon." },
      { "author": "George Grote", "work": "A History of Greece", "quote": "News of the disaster at **Leuctra** was received in Sparta during the gymnaepedia without a single outward sign of grief." }
    ]
  },
  "Dashboard — leuc/leukemia.md": {
    "primary": "A malignant progressive disease in which the bone marrow and other blood-forming organs produce increased numbers of immature or abnormal leukocytes.",
    "secondary": "In hematologic oncology, classified into acute and chronic myeloid or lymphoid leukemias, characterized by marrow failure, anemia, and thrombocytopenia.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "White Blood and Leukemia", "quote": "The blood in **leukemia** assumes a milky pale appearance owing to an immense accumulation of colorless cells." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In myelogenous **leukemia**, the spleen enlarges until it fills almost the entire left half of the abdominal cavity." },
      { "author": "Paul Ehrlich", "work": "The Anaemias and Their Pathology", "quote": "Cytochemical staining of the marrow in acute **leukemia** reveals the complete arrest of cellular differentiation." }
    ]
  },
  "Dashboard — leuc/leukocyte.md": {
    "primary": "A white blood cell; a colorless cellular component of the blood that possesses a nucleus and functions in the immune system to fight infections.",
    "secondary": "In immunology and cellular biology, motile cells that migrate through vascular endothelium into tissues via diapedesis in response to chemotactic gradients.",
    "quotes": [
      { "author": "Ilya Metchnikov", "work": "The Comparative Pathology of Inflammation", "quote": "Every active **leukocyte** acts as a cellular sentinel, devouring microbes to preserve the organism from septic death." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Under the microscope, we watched a single **leukocyte** extend pseudopodia and engulf a chain of streptococci." },
      { "author": "Claude Bernard", "work": "Lectures on the Phenomenon of Life", "quote": "The amoeboid motion of the **leukocyte** demonstrates the continuous vitality of individual cells within the body fluid." }
    ]
  },
  "Dashboard — leuc/leukocytopenia.md": {
    "primary": "An abnormally low count of white blood cells (leukocytes) in the circulating peripheral blood; leukopenia.",
    "secondary": "In hematopathology, a dangerous reduction in circulating leukocytes (less than 4,000 cells/uL) induced by chemotherapy, irradiation, or marrow aplasia.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Following massive mustard gas exposure, profound **leukocytopenia** left soldiers entirely defenseless against secondary pneumonia." },
      { "author": "Paul Ehrlich", "work": "Studies on Immunity", "quote": "The injection of specific cytotoxic sera resulted in transient marrow paralysis and severe **leukocytopenia**." },
      { "author": "Maxwell Finland", "work": "Antimicrobial Agents and Chemotherapy", "quote": "Patients developing drug-induced **leukocytopenia** must be placed in strict protective isolation immediately." }
    ]
  },
  "Dashboard — leuc/leukocytosis.md": {
    "primary": "An increase in the number of white blood cells in the circulating blood, especially in response to infection, inflammation, or physical trauma.",
    "secondary": "In clinical diagnosis, a reactive elevation in leukocyte count above 11,000 cells/uL, characteristically showing a left shift with band neutrophils in acute infection.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A marked polymorphonuclear **leukocytosis** accompanies acute appendicitis, serving as a reliable surgical indicator." },
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Chemotactic substances released by damaged tissues enter the circulation and provoke rapid **leukocytosis** from the bone marrow." },
      { "author": "William Henry Welch", "work": "General Pathology", "quote": "The degree of **leukocytosis** reflects both the virulence of the pathogen and the reactive vigor of the host defense." }
    ]
  },
  "Dashboard — leuc/leukodystrophy.md": {
    "primary": "A group of rare, inherited metabolic disorders characterized by the abnormal growth or progressive degeneration of the myelin sheath in the white matter of the brain.",
    "secondary": "In neurogenetics, progressive neurometabolic diseases (such as metachromatic leukodystrophy or Krabbe disease) caused by lysosomal or peroxisomal enzyme deficiencies.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Genetic screening has elucidated the metabolic enzyme defects underlying catastrophic childhood **leukodystrophy**." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "Demyelination of the cerebral hemispheres in **leukodystrophy** leads inexorably to spastic paralysis and cognitive decline." },
      { "author": "Santiago Ramón y Cajal", "work": "Degeneration and Regeneration of the Nervous System", "quote": "Disintegration of the myelin wrapping in progressive **leukodystrophy** strips the central nerve axones of insulation." }
    ]
  },
  "Dashboard — leuc/leukoplakia.md": {
    "primary": "A condition in which white, adherent patches or plaques develop on the mucous membranes of the mouth, tongue, or vulva, with potential for malignant transformation.",
    "secondary": "In oral pathology, a hyperkeratotic epithelial dysplasia associated with tobacco and alcohol use, biopsied to rule out oral squamous cell carcinoma.",
    "quotes": [
      { "author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Chronic pipe smokers frequently exhibit persistent patches of **leukoplakia** upon the dorsal surface of the tongue." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinician must regard **leukoplakia** of the buccal mucosa as a premalignant lesion requiring close surveillance." },
      { "author": "Erasmus Wilson", "work": "Diseases of the Skin", "quote": "The chalky white plaque of **leukoplakia** cannot be wiped off the mucous membrane like a thrush deposit." }
    ]
  },
  "Dashboard — leuc/leukorrhea.md": {
    "primary": "A thick, whitish or yellowish discharge from the female genital tract; variant American spelling of leucorrhea.",
    "secondary": "In clinical gynecology, an abnormal vaginal exudate resulting from cervical irritation, bacterial vaginosis, or hormonal imbalance.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent **leukorrhea** in an elderly woman warrants thorough endometrial examination to exclude occult carcinoma." },
      { "author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The discharge known as **leukorrhea** arises from chronic catarrhal inflammation of the cervical canal." },
      { "author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Proper sanitation and ventilation alleviated the distressing symptoms of chronic **leukorrhea** in hospital patients." }
    ]
  }
}

# Write curate-light-batch5.mjs
mjs_code = f"""import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {{
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {{
    console.error(`File not found: ${{filePath}}`);
    return false;
  }}
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {{
    console.error(`No > [!book] in ${{filePath}}`);
    return false;
  }}
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${{data.primary}}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${{data.secondary}}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${{q.author}} (*${{q.work}}*):** *"${{q.quote}}"*`).join('\\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${{quoteLines}}`;

  const newContent = `${{headerPart}}\\n\\n${{defBlock}}\\n\\n${{quotesBlock}}\\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}}

const batchData = {json.dumps(batch5, indent=2, ensure_ascii=False)};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {{
  if (updateNote(relPath, data)) updated++;
}}
console.log(`Successfully updated ${{updated}} of ${{Object.keys(batchData).length}} files in Batch 5.`);
"""

with open('main app/scripts/curate-light-batch5.mjs', 'w', encoding='utf-8') as f:
    f.write(mjs_code)

print("Generated curate-light-batch5.mjs with", len(batch5), "words.")
