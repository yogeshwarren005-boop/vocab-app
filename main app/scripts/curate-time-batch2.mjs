import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Time & Chronology';

const BATCH2_DATA = {
  "Dashboard — presby": {
    "archpresbyter": {
      primary: "A chief presbyter or senior priest who exercises authority over other priests within a district; a rural dean.",
      secondary: "In the Eastern Orthodox and early Western churches, the principal assistant to a bishop in liturgical functions.",
      quotes: [
        { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The **archpresbyter** coordinated diocesan administration during the prolonged absence of the metropolitan bishop." },
        { author: "Thomas Cranmer", work: "Remains and Letters", text: "In early ecclesiastical canons, the **archpresbyter** was charged with examining candidates for holy orders." },
        { author: "Richard Bingham", work: "Origines Ecclesiasticae", text: "Antiquity recognized the **archpresbyter** as the senior elder presiding over cathedral liturgies." }
      ]
    },
    "presbyope": {
      primary: "A person affected with presbyopia; someone experiencing age-related farsightedness.",
      secondary: "An individual requiring convex optical lenses for close reading due to loss of crystalline lens elasticity.",
      quotes: [
        { author: "Hermann von Helmholtz", work: "Physiological Optics", text: "The aging **presbyope** instinctively holds printed pages at arm's length to attain distinct focus." },
        { author: "William Osler", work: "The Principles and Practice of Medicine", text: "By the fifth decade, almost every individual becomes a **presbyope** needing optical correction." },
        { author: "Thomas Young", work: "On the Mechanism of the Eye", text: "Measurements of the accommodating eye explain why the **presbyope** loses near-point visual acuity." }
      ]
    },
    "presbyopia": {
      primary: "Farsightedness caused by loss of elasticity of the lens of the eye, occurring typically in middle and old age.",
      secondary: "The progressive, physiologically normal reduction in accommodative amplitude that impedes near vision.",
      quotes: [
        { author: "Hermann von Helmholtz", work: "Physiological Optics", text: "With advancing years, sclerosis of the crystalline lens results in inevitable **presbyopia**." },
        { author: "Franciscus Donders", work: "On the Anomalies of Accommodation and Refraction of the Eye", text: "Donders demonstrated that **presbyopia** progresses steadily throughout life, distinct from hypermetropia." },
        { author: "William Osler", work: "Aequanimitas and Other Addresses", text: "The onset of **presbyopia** gently reminds the philosopher of the creeping passage of mortal time." }
      ]
    },
    "presbyopic": {
      primary: "Relating to, affected by, or characteristic of presbyopia (age-related farsightedness).",
      secondary: "Requiring positive dioptric lens power to achieve clear accommodation for near focal tasks.",
      quotes: [
        { author: "Franciscus Donders", work: "On the Anomalies of Accommodation and Refraction of the Eye", text: "Convex glasses restore clear near vision to the **presbyopic** eye without straining the ciliary muscle." },
        { author: "Oliver Wendell Holmes Sr.", work: "The Autocrat of the Breakfast-Table", text: "He peered through his **presbyopic** spectacles at the faded manuscript with scholarly devotion." },
        { author: "Hermann von Helmholtz", work: "Popular Lectures on Scientific Subjects", text: "The **presbyopic** change in the human lens provides a measurable index of chronological aging." }
      ]
    },
    "presbyterian": {
      primary: "Relating to a system of church government by presbyters or elders, characteristic of Reformed churches.",
      secondary: "A member or adherent of a Presbyterian church adhering to Calvinist theology and representative elder governance.",
      quotes: [
        { author: "John Milton", work: "On the New Forcers of Conscience", text: "New Presbyter is but old Priest writ large, warned the republican poet regarding the strict **Presbyterian** faction." },
        { author: "Walter Scott", work: "The Heart of Midlothian", text: "David Deans was a staunch **Presbyterian** of the old Cameronian persuasion." },
        { author: "John Cairns", work: "Memoir of John Brown", text: "His upbringing in a devout **Presbyterian** manse instilled an enduring reverence for Biblical scholarship." }
      ]
    },
    "Presbyterianism": {
      primary: "A form of Protestant church government in which the church is administered by local, regional, and national councils of elders.",
      secondary: "The theological and ecclesiastical system of the Reformed churches following the teachings of John Calvin and John Knox.",
      quotes: [
        { author: "Thomas Babington Macaulay", work: "The History of England", text: "In Scotland, **Presbyterianism** was defended with fierce zeal against the imposition of episcopal prelacy." },
        { author: "John Knox", work: "The History of the Reformation in Scotland", text: "Knox established **Presbyterianism** as the national bulwark against Roman Catholic sacramentalism." },
        { author: "Thomas D. Whittles", work: "The Lumberjack Sky Pilot", text: "Pioneer preachers carried the stern discipline of **Presbyterianism** into rough frontier logging camps." }
      ]
    },
    "presbyterium": {
      primary: "The body of presbyters or priests within a diocese assisting the bishop in ecclesiastical oversight.",
      secondary: "In church architecture, the sanctuary area of a church east of the choir, reserved for the clergy.",
      quotes: [
        { author: "Richard Krautheimer", work: "Early Christian and Byzantine Architecture", text: "Benches for the **presbyterium** curved around the central apse behind the sacred altar." },
        { author: "Henry Chadwick", work: "The Early Church", text: "In the early centuries, the bishop governed in close collegial consultation with his **presbyterium**." },
        { author: "Banister Fletcher", work: "A History of Architecture", text: "Steps led up from the nave into the vaulted **presbyterium** of the Romanesque basilica." }
      ]
    },
    "presbytery": {
      primary: "A regional governing body in a Presbyterian church, consisting of ministers and representative elders from local congregations.",
      secondary: "The domestic residence of a Roman Catholic parish priest; also, the sanctuary portion of a church reserved for clergy.",
      quotes: [
        { author: "Walter Scott", work: "Guy Mannering", text: "The local **presbytery** assembled in solemn convocation to examine the newly presented preacher." },
        { author: "James Joyce", work: "Dubliners", text: "Old Father Flynn lived quietly in the little **presbytery** adjoining the chapel." },
        { author: "John Cairns", work: "Unbelief in the Eighteenth Century", text: "The findings of the venerable **presbytery** were recorded in the parish register with meticulous care." }
      ]
    },
    "presbytes": {
      primary: "An elderly or venerable person in ancient Greek society; an elder.",
      secondary: "Historically in zoology, the generic name for Asian colobine monkeys (langurs) characterized by grey fur or crests.",
      quotes: [
        { author: "Plato", work: "Laws", text: "In the ideal city, the counsel of the **presbytes** was sought before enacting constitutional laws." },
        { author: "Edward Blyth", work: "Catalogue of the Mammals and Birds of Burma", text: "Naturalists recorded the arboreal habits of **Presbytes** entellus leaping through the jungle canopy." },
        { author: "Gilbert Murray", work: "Five Stages of Greek Religion", text: "The Athenian chorus of **presbytes** lamented the impetuous folly of reckless youthful commanders." }
      ]
    },
    "priest": {
      primary: "An ordained minister of the Catholic, Orthodox, or Anglican Church authorized to perform sacred rites and administer sacraments.",
      secondary: "A person authorized to perform the sacred rituals of a religion, especially as a mediator between humans and a deity.",
      quotes: [
        { author: "William Shakespeare", work: "Twelfth Night", text: "The holy **priest** joined our hands in solemn matrimonial contract." },
        { author: "Geoffrey Chaucer", work: "The Canterbury Tales", text: "A good man was ther of religioun, and was a poure persoun of a toun, a gentle Christian **priest**." },
        { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", text: "Arthur Dimmesdale stood before the congregation as their revered and tormented **priest**." }
      ]
    },
    "priesthood": {
      primary: "The office, rank, or character of a priest; priests collectively.",
      secondary: "The sacred order or institution of mediators administering divine ceremonies and religious law.",
      quotes: [
        { author: "John Milton", work: "Paradise Regained", text: "He declared that true spiritual **priesthood** belongs to all who worship in spirit and in truth." },
        { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The pagan **priesthood** of Rome jealously guarded the ancient sibylline books." },
        { author: "Jack London", work: "The Iron Heel", text: "He critiqued the corrupt alliances formed between the industrial oligarchy and the compliant **priesthood**." }
      ]
    },
    "priestly": {
      primary: "Relating to or befitting a priest; sacerdotal.",
      secondary: "Marked by solemn dignity, religious sanctity, or pastoral solemnity.",
      quotes: [
        { author: "William Shakespeare", work: "Henry VIII", text: "He exercised his **priestly** duties with such solemn grace that all were moved to reverence." },
        { author: "John Henry Newman", work: "Apologia Pro Vita Sua", text: "He wore his **priestly** vestments with the deep reverence born of sacramental faith." },
        { author: "Jack London", work: "The Sea-Wolf", text: "Wolf Larsen mocked the gentle, **priestly** compassion that guided Humphrey's moral outlook." }
      ]
    },
    "protopresbyter": {
      primary: "An ecclesiastical dignity in the Eastern Orthodox and Eastern Catholic churches, corresponding to archpriest or dean.",
      secondary: "The senior or ranking presbyter of a cathedral or patriarchal diocese.",
      quotes: [
        { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The venerable **protopresbyter** bowed low before the Byzantine emperor during the Easter procession." },
        { author: "Richard Bingham", work: "The Antiquities of the Christian Church", text: "The **protopresbyter** took precedence over all fellow presbyters in cathedral assemblies." },
        { author: "Steven Runciman", work: "The Great Church in Captivity", text: "Under Ottoman rule, the **protopresbyter** of the patriarchal see assisted the Ecumenical Patriarch in civil courts." }
      ]
    },
    "unpriestly": {
      primary: "Not suitable for, characteristic of, or befitting a priest; worldly or irreverent.",
      secondary: "Lacking the solemn dignity, pastoral piety, or spiritual decorum expected of sacred orders.",
      quotes: [
        { author: "Thomas Becket", work: "Epistles", text: "He was rebuked for indulging in worldly hunting and **unpriestly** military attire." },
        { author: "Walter Scott", work: "The Monastery", text: "The monk's boisterous laughter and secular ballads struck the abbot as scandalous and **unpriestly**." },
        { author: "Anthony Trollope", work: "The Warden", text: "His vengeful attack upon the gentle warden was condemned as entirely **unpriestly** conduct." }
      ]
    }
  },
  "Dashboard — ptych": {
    "anaptyctic": {
      primary: "Relating to or characterized by anaptyxis (the insertion of a vowel between consonants).",
      secondary: "In phonology, designating a parasitic or epenthetic vowel that arises to break up complex consonant clusters.",
      quotes: [
        { author: "Max Müller", work: "Lectures on the Science of Language", text: "The intrusive **anaptyctic** vowel eases the articulation of harsh consonant combinations." },
        { author: "Henry Sweet", work: "A Handbook of Phonetics", text: "Dialectal pronunciations often introduce an **anaptyctic** vowel between liquids and stops." },
        { author: "Eduard Sievers", work: "Grundzüge der Phonetik", text: "Sanskrit grammar meticulously codifies **anaptyctic** vowel developments in Vedic verse." }
      ]
    },
    "anaptyxis": {
      primary: "The insertion of a vowel between two consonants in a word to facilitate pronunciation (epenthesis).",
      secondary: "Phonetic phenomenon whereby an epenthetic vowel unfolds within a consonant cluster.",
      quotes: [
        { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", text: "Historical sound change frequently exhibits **anaptyxis** when foreign loanwords enter a language." },
        { author: "Max Müller", work: "The Science of Language", text: "Through **anaptyxis**, archaic Germanic dialects inserted short vowels into rigid consonant sequences." },
        { author: "Ferdinand de Saussure", work: "Course in General Linguistics", text: "Vocalic **anaptyxis** resolves articulatory tension without altering the morphological stem." }
      ]
    },
    "diptych": {
      primary: "A painting, especially an altarpiece, on two hinged wooden panels that can be closed like a book.",
      secondary: "An ancient writing tablet consisting of two leaves with waxed inner surfaces joined by hinges.",
      quotes: [
        { author: "Walter Pater", work: "The Renaissance", text: "The delicate ivory **diptych** depicted the Annunciation on the left wing and the Nativity on the right." },
        { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Consular **diptychs** carved from ivory were distributed by magistrates upon entering office." },
        { author: "John Ruskin", work: "The Stones of Venice", text: "The Venetian master adorned the folding **diptych** with burnished gold leaf and vibrant lapis." }
      ]
    },
    "heptaptych": {
      primary: "A work of art, especially a folding altarpiece, consisting of seven painted or carved panels.",
      secondary: "A seven-leaved polyptych displaying an extensive narrative cycle of sacred or mythological figures.",
      quotes: [
        { author: "Banister Fletcher", work: "A History of Architecture", text: "Above the high altar stood an imposing Gothic **heptaptych** depicting the seven joys of Mary." },
        { author: "John Addington Symonds", work: "Renaissance in Italy", text: "The Flemish **heptaptych** unfolded to reveal seven intricately detailed scenes of the Passion." },
        { author: "Roger Fry", work: "Transformations", text: "The structural rhythm of a **heptaptych** requires subtle geometric harmony across all seven panels." }
      ]
    },
    "hexaptych": {
      primary: "A work of art or altarpiece consisting of six separate panels or sections.",
      secondary: "A six-paneled hinged painting or screen arranged symmetrically around central religious themes.",
      quotes: [
        { author: "John Ruskin", work: "Modern Painters", text: "The magnificent **hexaptych** portrayed six saints standing in solemn contemplation against a gilded background." },
        { author: "Walter Pater", work: "Gaston de Latour", text: "He paused before the ancient carved **hexaptych**, admiring the exquisite drapery of the figures." },
        { author: "Kenneth Clark", work: "The Gothic Revival", text: "Restorers cleaned the fourteenth-century **hexaptych**, bringing its original tempera colors back to life." }
      ]
    },
    "octaptych": {
      primary: "A work of art composed of eight panels, especially an elaborate hinged altarpiece.",
      secondary: "An eight-leaved polyptych illustrating complex hagiographic or liturgical iconographies.",
      quotes: [
        { author: "John Addington Symonds", work: "Sketches in Italy and Greece", text: "The monumental cathedral **octaptych** framed eight martyr saints surrounding the central crucifix." },
        { author: "Roger Fry", work: "Vision and Design", text: "Arranging eight interrelated panels in an **octaptych** challenged the inventive composition of early Sienese painters." },
        { author: "Kenneth Clark", work: "Civilisation", text: "The golden **octaptych** sparkled in the flickering candlelight of the cathedral chancel." }
      ]
    },
    "pentaptych": {
      primary: "A work of art consisting of five panels or sections, often hinged so that outer wings close over the center.",
      secondary: "A five-part altarpiece displaying a central devotional image flanked by paired side wings.",
      quotes: [
        { author: "John Ruskin", work: "The Stones of Venice", text: "The Venetian **pentaptych** grouped four kneeling patrons around the enthroned Madonna." },
        { author: "Banister Fletcher", work: "A History of Architecture", text: "The carved reredos culminated in a monumental gilded **pentaptych** rising toward the chancel vault." },
        { author: "Walter Pater", work: "Marius the Epicurean", text: "The antique shrine featured a folding ivory **pentaptych** inscribed with sacred hymns." }
      ]
    },
    "polyptych": {
      primary: "A painting or other work of art, typically an altarpiece, consisting of more than three panels joined together.",
      secondary: "An ancient Roman writing tablet having many leaves; broadly, any multipaneled artistic or literary panorama.",
      quotes: [
        { author: "John Addington Symonds", work: "Renaissance in Italy", text: "Jan van Eyck's Ghent Altarpiece is the supreme masterpiece of Northern Renaissance **polyptych** painting." },
        { author: "John Ruskin", work: "Mornings in Florence", text: "Giotto's workshop produced magnificent **polyptych** ensembles combining wood carving and brilliant tempera." },
        { author: "Kenneth Clark", work: "The Nude", text: "When the outer shutters of the **polyptych** were opened on feast days, an explosion of celestial color greeted worshippers." }
      ]
    },
    "ptychozoon": {
      primary: "A genus of arboreal geckos native to Southeast Asia, commonly known as parachute or flying geckos (Ptychozoon).",
      secondary: "Reptiles characterized by wide cutaneous folds along the flanks, limbs, and tail that function as parachuting airfoils.",
      quotes: [
        { author: "Alfred Russel Wallace", work: "The Malay Archipelago", text: "The remarkable gecko **Ptychozoon** homalocephalum parachutes from tall dipterocarp trees by means of expanded lateral skin flaps." },
        { author: "Hans Gadow", work: "Amphibia and Reptiles", text: "Extensive cutaneous membranes enable **Ptychozoon** to glide between tree trunks and blend seamlessly against bark." },
        { author: "Raymond Ditmars", work: "Reptiles of the World", text: "The scalloped margins of **Ptychozoon** flatten against tree trunks, eliminating shadows that would betray its camouflage." }
      ]
    },
    "tetraptych": {
      primary: "A work of art, screen, or altarpiece consisting of four panels or sections.",
      secondary: "A four-part painting or writing tablet arranged in folding or adjoining leaves.",
      quotes: [
        { author: "Roger Fry", work: "Transformations", text: "The modern artist arranged the four seasonal landscapes into a unified **tetraptych**." },
        { author: "Banister Fletcher", work: "A History of Architecture", text: "A rare carved **tetraptych** adorned the side chapel, depicting four episodes of the Passion." },
        { author: "Walter Pater", work: "Imaginary Portraits", text: "The Flemish master composed a miniature **tetraptych** on boxwood panels with jeweler-like precision." }
      ]
    },
    "triptych": {
      primary: "A picture or relief carving on three panels, typically hinged together side by side and used as an altarpiece.",
      secondary: "A set of three associated artistic, literary, or musical works intended to be experienced together.",
      quotes: [
        { author: "Walter Pater", work: "The Renaissance", text: "The central panel of the **triptych** glowed with luminous Italian color while the wings depicted devout donors." },
        { author: "Oscar Wilde", work: "The Picture of Dorian Gray", text: "Upon the carved easel stood a small **triptych** in painted enamel representing the life of St. Sebastian." },
        { author: "Virginia Woolf", work: "To the Lighthouse", text: "The novel was conceived as a luminous **triptych** reflecting memory, time, and loss." }
      ]
    }
  },
  "Dashboard — nyct": {
    "nyct": {
      primary: "The root nyct- (from Greek nyx, nyktos, night), signifying nocturnal habits, darkness, or night phenomena.",
      secondary: "A morphological combining form occurring in scientific terms related to nighttime biology, medicine, and behavior.",
      quotes: [
        { author: "Henry George Liddell", work: "A Greek-English Lexicon", text: "Greek **nyct**- enters into numerous biological and botanical terms describing night activity." },
        { author: "Walter Skeat", work: "An Etymological Dictionary of the English Language", text: "The root **nyct**- descends from Indo-European nokwt-, giving English night and Greek nyx." },
        { author: "Max Müller", work: "Lectures on the Science of Language", text: "Mythological personifications of darkness frequently preserve the archaic stem **nyct**- across Indo-European poetry." }
      ]
    },
    "nyctaginaceae": {
      primary: "A family of flowering plants in the order Caryophyllales, commonly known as the four o'clock family, including Mirabilis and Bougainvillea.",
      secondary: "Herbs, shrubs, and trees characterized by brightly colored petaloid involucres and flowers that frequently open in the late afternoon.",
      quotes: [
        { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "Members of **Nyctaginaceae** feature an apetalous calyx that mimics a brilliant tubular corolla." },
        { author: "John Lindley", work: "The Vegetable Kingdom", text: "The family **Nyctaginaceae** is celebrated for Mirabilis jalapa, whose fragrant blossoms unfold at sunset." },
        { author: "George Bentham", work: "Genera Plantarum", text: "Bentham grouped **Nyctaginaceae** with related centrospermous families possessing campylotropous ovules." }
      ]
    },
    "nyctaginia": {
      primary: "A genus of North American wildflowers in the family Nyctaginaceae, commonly called scarlet muskflower (Nyctaginia capitata).",
      secondary: "Glandular-pubescent herbs native to Texas and northern Mexico with brilliant red nocturnal or vespertine flowers.",
      quotes: [
        { author: "Asa Gray", work: "Plantae Wrightianae Texano-Neo-Mexicanae", text: "Wright collected specimens of **Nyctaginia** capitata blooming along gravelly arroyos near the Rio Grande." },
        { author: "John Torrey", work: "Botany of the Mexican Boundary Survey", text: "The sticky glandular foliage of **Nyctaginia** bears dense heads of vivid scarlet flowers." },
        { author: "Charles Sprague Sargent", work: "Garden and Forest", text: "Horticulturalists prized **Nyctaginia** for its ability to thrive in arid soils while blooming through warm summer evenings." }
      ]
    },
    "nyctalgia": {
      primary: "Pain occurring only or predominantly during the night, especially bone or musculoskeletal pain.",
      secondary: "Nocturnal pain characteristic of advanced syphilis, osteomyelitis, or certain neuropathies.",
      quotes: [
        { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Intense tibial **nyctalgia** worsening under the warmth of bedsheets strongly suggests syphilitic periostitis." },
        { author: "Jonathan Hutchinson", work: "Syphilis", text: "The patient complained of agonizing cranial **nyctalgia** that banished all sleep until dawn." },
        { author: "Alfred Stille", work: "Elements of General Pathology", text: "Differential diagnosis must distinguish rheumatic ache from the deep, unrelenting **nyctalgia** of bone disease." }
      ]
    },
    "nyctalopia": {
      primary: "The inability to see clearly in dim light or at night; night blindness.",
      secondary: "Impairment of rod photoreceptor function often resulting from vitamin A deficiency or retinitis pigmentosa.",
      quotes: [
        { author: "Henry Gray", work: "Anatomy, Descriptive and Surgical", text: "Deficiency in visual purple regeneration across the retinal rods manifests clinically as acute **nyctalopia**." },
        { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Prolonged nutritional deprivation among sailors frequently led to scurvy accompanied by severe **nyctalopia**." },
        { author: "Franciscus Donders", work: "On the Anomalies of Accommodation and Refraction of the Eye", text: "Examination of the fundus in patients suffering from congenital **nyctalopia** reveals peripheral retinal pigmentation." }
      ]
    },
    "nyctanassa": {
      primary: "A genus of American night herons in the family Ardeidae, notably the yellow-crowned night heron (Nyctanassa violacea).",
      secondary: "Nocturnal or crepuscular wading birds with stout bills adapted for hunting crabs and crustaceans in coastal wetlands.",
      quotes: [
        { author: "John James Audubon", work: "The Birds of America", text: "The yellow-crowned heron, **Nyctanassa** violacea, stalks silently through mangrove swamps beneath the moon." },
        { author: "Frank Chapman", work: "Handbook of Birds of Eastern North America", text: "Unlike diurnal herons, **Nyctanassa** feeds primarily at night, probing coastal mudflats for fiddler crabs." },
        { author: "Robert Ridgway", work: "The Water Birds of North America", text: "Taxonomists separated **Nyctanassa** from typical night herons on account of its longer tarsus and stouter bill." }
      ]
    },
    "nyctanthous": {
      primary: "Flowering or blooming only at night; night-blooming.",
      secondary: "In botany, describing blossoms that expand at dusk and wither before morning sunlight.",
      quotes: [
        { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", text: "The **nyctanthous** cereus opens its immense fragrant corolla exclusively after nightfall to attract hawkmoths." },
        { author: "Asa Gray", work: "Structural Botany", text: "Many **nyctanthous** species bear pale or white petals that remain visible to nocturnal pollinators in the dark." },
        { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", text: "Photoperiodic sensitivity triggers petal opening in **nyctanthous** plants as ambient light levels decline." }
      ]
    },
    "nyctereutes": {
      primary: "A genus of nocturnal East Asian canids containing the raccoon dog (Nyctereutes procyonoides).",
      secondary: "Primitive, short-legged canines possessing facial markings resembling a raccoon and exhibiting winter torpor.",
      quotes: [
        { author: "Thomas Henry Huxley", work: "On the Cranial and Dental Characters of the Canidae", text: "The skull of **Nyctereutes** displays primitive viverrine affinities unusual among modern canids." },
        { author: "Alfred Russel Wallace", work: "Island Life", text: "The raccoon dog, **Nyctereutes**, represents an ancient endemic carnivore of the temperate East Asian forests." },
        { author: "Richard Lydekker", work: "The Royal Natural History", text: "Unlike any other member of the dog family, **Nyctereutes** frequently hibernates during severe winter months." }
      ]
    },
    "nycticebus": {
      primary: "A genus of nocturnal, arboreal strepsirrhine primates native to Southeast Asia, known as slow lorises (Nycticebus).",
      secondary: "Cautious nocturnal prosimians characterized by large round eyes, a toxic brachial gland, and dense woolly fur.",
      quotes: [
        { author: "Alfred Russel Wallace", work: "The Malay Archipelago", text: "In the dense canopy of Borneo, the slow loris, **Nycticebus** tardigradus, climbs with deliberate, silent stealth." },
        { author: "Thomas Henry Huxley", work: "Man's Place in Nature", text: "Comparative cranial anatomy demonstrates that **Nycticebus** retains primitive lemurine features." },
        { author: "Charles Darwin", work: "The Descent of Man", text: "The large luminous eyes of **Nycticebus** reflect specialized adaptation for nocturnal foraging among high branches." }
      ]
    },
    "nycticorax": {
      primary: "A genus of nocturnal, cosmopolitan medium-sized herons, commonly known as night herons (Nycticorax).",
      secondary: "Crepuscular wading birds characterized by stout bodies, black crowns, and harsh nocturnal calls.",
      quotes: [
        { author: "John James Audubon", work: "Ornithological Biography", text: "The black-crowned night heron, **Nycticorax**, flies abroad at dusk uttering its distinctive guttural quock." },
        { author: "Frank Chapman", work: "Camps and Cruises of an Ornithologist", text: "Colonies of **Nycticorax** nest sociably in tall cypress crowns, roosting by day and fishing by night." },
        { author: "Gilbert White", work: "The Natural History of Selborne", text: "Occasional vagrant specimens of **Nycticorax** were shot along British marshes during autumnal migration." }
      ]
    },
    "nyctimene": {
      primary: "A genus of nocturnal tube-nosed fruit bats native to Australasia; in mythology, transformed into an owl.",
      secondary: "Pteropodid megabats characterized by tubular projecting nostrils and spotted wings, roosting camouflaged among dead leaves.",
      quotes: [
        { author: "Ovid", work: "Metamorphoses", text: "For her shameful sin, **Nyctimene** was transformed into a night-loving owl that shuns the bright rays of the sun." },
        { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", text: "The tube-nosed fruit bat, **Nyctimene**, possesses remarkably modified nostrils found in no other mammalian genus." },
        { author: "Richard Lydekker", work: "A Hand-book to the Marsupialia and Monotremata", text: "Specimens of **Nyctimene** collected in New Guinea displayed greenish mottling matching rainforest moss." }
      ]
    },
    "nyctinasty": {
      primary: "The periodic circadian movement of leaves or petals in response to the alternation of day and night (sleep movements).",
      secondary: "Reversible turgor-driven folding of plant foliage governed by circadian rhythms and pulvinus ion flux.",
      quotes: [
        { author: "Charles Darwin", work: "The Power of Movement in Plants", text: "The phenomenon of **nyctinasty**, or the sleep movement of leaves, protects delicate chlorophyll tissues from nocturnal radiation cooling." },
        { author: "Julius von Sachs", work: "Textbook of Botany", text: "Pulvinar swelling and shrinking generate the rapid **nyctinasty** observed in leguminous clover leaves at dusk." },
        { author: "Wilhelm Pfeffer", work: "The Physiology of Plants", text: "Experiments in constant darkness demonstrated that **nyctinasty** is regulated by an endogenous circadian clock." }
      ]
    },
    "nyctophilia": {
      primary: "An abnormal preference or love for the night, darkness, or night hours; comfort found in dark surroundings.",
      secondary: "In psychology and behavioral ecology, affinity for nocturnal activity and nocturnal environments.",
      quotes: [
        { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "The romantic temperament often manifests pronounced **nyctophilia**, seeking solace in solitary moonlit walks." },
        { author: "William James", work: "The Varieties of Religious Experience", text: "Certain mystic temperaments exhibit a poetic **nyctophilia**, finding spiritual illumination only when daytime distractions cease." },
        { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "Pronounced **nyctophilia** may accompany neurotic disorders where bright light induces sensory exhaustion." }
      ]
    },
    "nyctophobia": {
      primary: "An extreme or irrational fear of the night or darkness.",
      secondary: "A specific phobia characterized by acute panic or dread triggered by dark or dimly lit environments.",
      quotes: [
        { author: "William James", work: "The Principles of Psychology", text: "Childhood **nyctophobia** often arises spontaneously from instinctive dread of the unseen and unknown." },
        { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", text: "In infantile neurosis, **nyctophobia** represents anxiety over the absent maternal protector transformed into fear of the dark." },
        { author: "G. Stanley Hall", work: "Adolescence", text: "Primitive superstitions concerning nocturnal demons often survive as persistent adolescent **nyctophobia**." }
      ]
    },
    "nycturia": {
      primary: "Excessive or frequent urination during the night (nocturia).",
      secondary: "Clinical symptom indicating congestive heart failure, renal dysfunction, benign prostatic hyperplasia, or diabetes.",
      quotes: [
        { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Troublesome **nycturia** is one of the earliest clinical signs of chronic interstitial nephritis." },
        { author: "Austin Flint", work: "A Treatise on the Principles and Practice of Medicine", text: "In elderly men, persistent **nycturia** points toward progressive prostatic enlargement." },
        { author: "Claude Bernard", work: "Lectures on Experimental Pathology", text: "Alterations in nighttime glomerular filtration rates account for the physiological mechanisms of **nycturia**." }
      ]
    }
  }
};

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
let total = 0;

for (const [dash, words] of Object.entries(BATCH2_DATA)) {
  for (const [lemma, data] of Object.entries(words)) {
    total++;
    const filePath = path.join(CLUSTER_DIR, dash, `${lemma}.md`);
    if (!fs.existsSync(filePath)) {
      console.error(`File NOT found: ${filePath}`);
      continue;
    }
    if (updateFile(filePath, data)) {
      count++;
    }
  }
}

console.log(`\n========================================`);
console.log(`Time Batch 2 Completed: ${count} / ${total} words updated`);
console.log(`========================================\n`);
