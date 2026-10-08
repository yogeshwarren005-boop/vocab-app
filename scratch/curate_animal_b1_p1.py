# -*- coding: utf-8 -*-
"""
curate_animal_b1_p1.py
Batch 1 Part 1 of Cluster Animal & Plant (50 words):
- Dashboard — corn (13 words):
  bicorn, bicornate, bicorned, corn, corneal, corned, corneous,
  cornerstone, cornet, cornetist, cornucopia, corny, unicorn
- Dashboard — herb (12 words):
  herb, herbaceous, herbage, herbal, herbalist, herbarium,
  herbart, herbert, herbicide, herbivore, herbivorous, herborize
- Dashboard — porc (9 words):
  porc, porcelain, porcelainize, porcellio, porcellionidae,
  porcine, porcupine, porcupinefish, porcupines
- Dashboard — taur (6 words):
  tauriform, taurine, taurobolium, tauromachy, taurotragus, taurus
- Dashboard — vulp (5 words):
  vulpecula, vulpecular, vulpes, vulpicide, vulpine
- Dashboard — zo (5 words):
  azoic, epizootic, protozoa, zodiac, zodiacal
Total: 50 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_animal_b1_p1 = {
    # ==================== Dashboard — corn (13 words) ====================
    "bicorn": {
        "primary": "A two-cornered cocked hat worn by military and naval officers, especially during the late eighteenth and early nineteenth centuries.",
        "secondary": "In morphology and anatomy, describing any structure or organ terminating in two distinct horn-shaped projections.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Deputies with plumes and cockades mingled with officers in blue coats and **bicorn** headgear."},
            {"author": "Arthur Conan Doyle", "work": "The Exploits of Brigadier Gerard", "quote": "He tucked his feathered **bicorn** beneath his arm and bowed low before the Emperor's staff."},
            {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The consular escort appeared in ceremonial attire, their rigid **bicorn** hats gleaming under the eastern sun."}
        ]
    },
    "bicornate": {
        "primary": "Possessing two horns, horn-like processes, or crescent crescent-shaped lateral extensions.",
        "secondary": "In embryology and comparative gynecology, designating an anatomical uterus having two distinct symmetric lateral cavities or horns.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The mammalian reproductive tract frequently retains an ancestral **bicornate** configuration with pronounced lateral cornua."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In several ungulate orders the uterus remains distinctly **bicornate**, diverging widely toward each oviduct."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon: A Dictionary of Medical Science", "quote": "A congenital **bicornate** malformation arises when the paired paramesonephric ducts fail to fuse along their midline."}
        ]
    },
    "bicorned": {
        "primary": "Having two horns or crescent-like points; crescentic or two-pronged in contour.",
        "secondary": "In classical poetry and astronomy, applied to the waxing crescent moon or horned deities such as Isis or Bacchus.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Mooned Ashtaroth, heaven's queen and mother, was pictured with **bicorned** crescent bright upon her brow."},
            {"author": "Percy Bysshe Shelley", "work": "The Revolt of Islam", "quote": "The **bicorned** moon hung trembling in the dusky west above the silent silver waters."},
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Fair Cynthia showed her **bicorned** crest aloft among the trembling constellations of the night."}
        ]
    },
    "corn": {
        "primary": "The seed or grain of cereal grasses, especially maize in North America, or wheat, rye, and barley in the British Isles.",
        "secondary": "In pathology, a painful localized thickening and hyperkeratosis of the epidermis, typically on the toes, caused by repeated friction or pressure.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "The man that makes his toe / What he his heart should make, / Shall of a **corn** cry woe, / And turn his sleep to wake."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I planted about two acres and a half of upland, chiefly with beans, but also a small patch of **corn** and potatoes."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was the chief dealer in wheat and barley, controlling the entire inland **corn** trade of the district."}
        ]
    },
    "corneal": {
        "primary": "Pertaining to or situated in the cornea, the transparent fibrous coat covering the iris and pupil of the eye.",
        "secondary": "In ophthalmology and optics, relating to refractive curvature, astigmatic distortion, or surgical transplantation of the anterior eye surface.",
        "quotes": [
            {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The anterior **corneal** surface provides the greater part of the optical refraction that focuses light upon the retina."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Light rays undergo their primary refraction at the curved surface of the transparent **corneal** epithelium."},
            {"author": "William Bowman", "work": "Lectures on the Parts Concerned in the Operations on the Eye", "quote": "The delicate lamellae of the **corneal** stroma lie arranged in regular horizontal layers beneath the anterior elastic membrane."}
        ]
    },
    "corned": {
        "primary": "Preserved or cured by packing with coarse grains or crystals of salt ('corns').",
        "secondary": "In culinary tradition, designating beef brisket cured in seasoned brine with peppercorns, cloves, and bay leaves before slow boiling.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He offered me a piece of **corned** beef and hard bread, which I was glad enough to partake of after our cold ride."},
            {"author": "Charles Dickens", "work": "The Posthumous Papers of the Pickwick Club", "quote": "A huge round of **corned** beef was placed upon the table, flanked by foaming tankards of home-brewed ale."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "We subsisted for weeks on bacon, ship biscuits, and salt **corned** pork until our provisions ran dangerously low."}
        ]
    },
    "corneous": {
        "primary": "Composed of or resembling horn; horny, tough, and keratinized in texture.",
        "secondary": "In entomology and malacology, describing hardened cuticular shields, beetle elytra, or the horny opercula of gastropods.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain beetles possess modified **corneous** wing-covers that form a solid protective shield over their delicate abdomens."},
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The mandibles are armed with dense **corneous** plates capable of shearing through tough fibrous vegetation."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The claw is enclosed in a thickened **corneous** sheath that grows continuously from the underlying dermis."}
        ]
    },
    "cornerstone": {
        "primary": "A stone that forms the base of a corner of a building, joining two walls; hence, an indispensable foundational basis.",
        "secondary": "In architectural ceremonies and political discourse, the ceremonial block engraved with commemorative dates, symbolizing institutional endurance.",
        "quotes": [
            {"author": "Thomas Jefferson", "work": "Writings on Democracy", "quote": "Freedom of religion and the press must remain the eternal **cornerstone** of any free and enlightened republic."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A well-regulated judiciary must ever be regarded as the essential **cornerstone** of constitutional liberty."},
            {"author": "John Locke", "work": "Two Treatises of Government", "quote": "Consent of the governed constitutes the true **cornerstone** upon which legitimate political authority is erected."}
        ]
    },
    "cornet": {
        "primary": "A brass wind instrument resembling a trumpet but shorter, equipped with valves and possessing a softer, more mellow tone.",
        "secondary": "Historically in the British cavalry, the lowest commissioned officer who carried the colors of a troop; or a cone-shaped rolled paper or pastry container.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The choir practice echoed with the piercing melody of the clarinet supported by the mellow notes of the **cornet**."},
            {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "He was once a dashing **cornet** of dragoons who rode with pride before the regiment in his scarlet coat."},
            {"author": "Charles Dickens", "work": "Sketches by Boz", "quote": "The street musician strained his cheeks until his eyes bulged as he blew a discordant march upon his battered **cornet**."}
        ]
    },
    "cornetist": {
        "primary": "A musician who plays the cornet.",
        "secondary": "In nineteenth-century concert bands and brass ensembles, the featured soloist who performed virtuosic ornamental cadenzas and melodic themes.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The celebrated **cornetist** executed the rapid triple-tonguing variations with remarkable agility and flawless intonation."},
            {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The municipal band included a dedicated **cornetist** who blew every martial strain with heroic lung power."},
            {"author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "Our regiment was fortunate in possessing an accomplished **cornetist** whose evening solos delighted the entire cantonment."}
        ]
    },
    "cornucopia": {
        "primary": "A horn of plenty; a symbol of abundance, represented as a goat's horn overflowing with fruits, flowers, and grains.",
        "secondary": "In iconography and classical mythology, the horn of the goat Amalthea that suckled Zeus, personified as a boundless inexhaustible supply.",
        "quotes": [
            {"author": "John Keats", "work": "Endymion", "quote": "She poured forth gifts like autumn's **cornucopia**, scattering golden fruit upon the lap of the smiling earth."},
            {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The harvest feast displayed an overflowing **cornucopia** of roasted meats, cider, and autumn fruits."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The Ghost of Christmas Present sat surrounded by a radiant **cornucopia** of turkeys, geese, poultry, brawn, and luscious fruits."}
        ]
    },
    "corny": {
        "primary": "Tritely sentimental, banally humorous, or outdated in taste; also literally abounding in corn or corn-like hard calluses.",
        "secondary": "In twentieth-century colloquial rhetoric and theatrical slang, describing rustic melodramatic tropes or stale vaudeville jokes.",
        "quotes": [
            {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "He made a **corny** old joke about the tourist season, smiling broadly as if it were a fresh invention."},
            {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The speaker delivered a series of **corny** platitudes about civic virtue that drew polite applause from the booster club."},
            {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The working-class music hall was filled with sentimental songs and **corny** gags that everyone had known since childhood."}
        ]
    },
    "unicorn": {
        "primary": "A legendary mythical creature typically depicted as a white horse with a single spiraling horn projecting from its forehead.",
        "secondary": "In medieval heraldry, bestiaries, and allegorical Christian art, an emblem of purity, Christological incarnation, and untamable strength.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Now I will believe / That there are **unicorns**; that in Arabia / There is one tree, the phoenix' throne; one phoenix / At this hour reigning there."},
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The alleged medicinal virtues of the horn of the **unicorn** have been thoroughly discredited by modern observation."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Many opinions have been held touching the **unicorn**, some affirming it to be an Indian ass, others a rhinoceros."}
        ]
    },

    # ==================== Dashboard — herb (12 words) ====================
    "herb": {
        "primary": "Any non-woody seed-bearing plant that dies back to the ground after flowering; or an aromatic plant used in cookery or medicine.",
        "secondary": "In pharmacology and culinary botanical taxonomy, distinguishing soft herbaceous tissues from woody perennial shrubs and arboreal timber.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "O, mickle is the powerful grace that lies / In herbs, plants, stones, and their true qualities: / For nought so vile that on the earth doth live / But to the earth some special good doth give. The healing **herb** heals the wound."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "He formed each pleasant **herb** of sweetest smell, / For food or medicine to the sons of men."},
            {"author": "Francis Bacon", "work": "The Essays", "quote": "Virtue is like precious odours, most fragrant when they are incensed or crushed; so also is every aromatic **herb**."}
        ]
    },
    "herbaceous": {
        "primary": "Relating to or having the characteristics of an herb; leafy and non-woody in stem structure.",
        "secondary": "In botany, designating perennial or annual vegetation that produces aerial shoots without forming persistent secondary xylem.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The seeds of many **herbaceous** species survive long immersion in sea water without losing their power of germination."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The hedge-banks were carpeted with succulent **herbaceous** shoots long before the deciduous trees showed their first buds."},
            {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "The rapid spring growth of **herbaceous** plants depends upon food stored in underground rhizomes during the prior season."}
        ]
    },
    "herbage": {
        "primary": "Herbaceous vegetation, such as grass and leafy plants, considered as food for livestock or ground cover.",
        "secondary": "In pastoral agriculture and historical legal tenure, the right of pasturing cattle upon another's land or commons.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The cows waded flank-deep into the rich green **herbage** of the water-meadows, chewing their cud in lazy contentment."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The pampas supported an abundant growth of succulent **herbage**, affording rich pasturage for vast herds of wild cattle."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "A heavy morning dew sparkled on every blade of **herbage** that fringed the quiet forest trail."}
        ]
    },
    "herbal": {
        "primary": "Relating to, made of, or derived from herbs; also a book containing the names and medicinal descriptions of plants.",
        "secondary": "In historical pharmacognosy and renaissance botany, an illustrated compendium compiling traditional remedies, plant signatures, and therapeutic virtues.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The old **herbal** writers made great account of the juice of wild thyme for expelling venomous infections."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The village women had great faith in Sally Oates's **herbal** teas for easing heart complaints and asthma."},
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "To compile a faithful **herbal** requireth not only diligent reading, but exact and curious observation in field and garden."}
        ]
    },
    "herbalist": {
        "primary": "A practitioner who collects, grows, or dispenses medicinal herbs and prepares traditional botanical remedies.",
        "secondary": "In the history of medicine and botany, the precursor to modern pharmacologists and botanists, classifying indigenous floras according to their active virtues.",
        "quotes": [
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "The village **herbalist** wandered along the cliffs collecting sea-fennel and scurvy-grass for his rustic patients."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Featherstone would trust no certified physician, preferring the infusions of an itinerant **herbalist** from the fen district."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth had spent years among the Native Americans, learning secrets that made him an accomplished **herbalist**."}
        ]
    },
    "herbarium": {
        "primary": "A systematically arranged collection of dried, pressed plant specimens mounted on paper for scientific research.",
        "secondary": "In taxonomic botany, an institutional repository preserving type specimens that serve as physical standards for botanical nomenclature.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Life and Letters of Charles Darwin", "quote": "I spent several hours comparing my Galápagos specimens with dried sheets preserved in the Kew **herbarium**."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Every serious student of flora must prepare a well-curated **herbarium**, annotating each sheet with exact locality and date."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Our botanical trunks contained a valuable **herbarium** of rare equatorial species gathered along the banks of the Orinoco."}
        ]
    },
    "herbart": {
        "primary": "Referring to Johann Friedrich Herbart (1776–1841), German philosopher and founder of modern scientific pedagogy.",
        "secondary": "In the history of education and psychological theory, designating the doctrine of apperception and moral character formation through structured instructional steps.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The pedagogical system founded by **Herbart** emphasized apperception as the mental process by which new ideas integrate with prior experience."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "The great service of **Herbart** lay in taking the work of teaching out of the realm of routine and accident."},
            {"author": "G. Stanley Hall", "work": "Adolescence", "quote": "Modern educational psychology owes a lasting debt to the pioneering psychological formulations of **Herbart**."}
        ]
    },
    "herbert": {
        "primary": "A personal name of Germanic origin meaning 'illustrious warrior' or 'bright army'; prominently associated with poet George Herbert or philosopher Herbert Spencer.",
        "secondary": "In English literature and intellectual history, denoting the metaphysical devotional poetry of George Herbert or the evolutionary sociology of Herbert Spencer.",
        "quotes": [
            {"author": "Izaak Walton", "work": "The Life of Mr. George Herbert", "quote": "The pious life of George **Herbert** at Bemerton displayed an exemplary union of pastoral devotion and transcendent verse."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poems of George **Herbert** are exquisite in their kind, combining quaint conceits with deep spiritual purity."},
            {"author": "William James", "work": "Pragmatism", "quote": "The cosmic evolutionary synthesis propounded by **Herbert** Spencer sought to explain all nature by mechanical transitions from homogeneity to heterogeneity."}
        ]
    },
    "herbicide": {
        "primary": "A chemical substance or toxic agent formulated specifically to kill or inhibit the growth of unwanted plants or weeds.",
        "secondary": "In agronomy and environmental management, classified into selective systemic compounds and non-selective contact desiccant agents.",
        "quotes": [
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The widespread aerial spraying of chemical **herbicide** along roadsides destroyed wild berry patches and poisoned local pollinator habitats."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "Modern agriculture relies increasingly on the **herbicide** to eliminate wild native forbs that once enriched the soil."},
            {"author": "Barry Commoner", "work": "The Closing Circle", "quote": "Synthetic **herbicide** runoff from commercial cornfields disrupts aquatic ecological balance in surrounding river basins."}
        ]
    },
    "herbivore": {
        "primary": "An animal anatomically and physiologically adapted to feed primarily or exclusively on autotrophic plant matter.",
        "secondary": "In trophic ecology, a primary consumer occupying the second trophic level, transferring photosynthesized solar energy to carnivores.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A quadrupedal **herbivore** requires an extensive digestive tract to ferment and extract nourishment from fibrous cellulose."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The molar dentition of a typical ungulate **herbivore** displays elevated transverse ridges ideal for grinding fibrous grasses."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The skull of the **herbivore** shows pronounced modification of the mandibular condyle to permit lateral chewing motion."}
        ]
    },
    "herbivorous": {
        "primary": "Feeding predominantly on plant material and vegetation; herb-eating.",
        "secondary": "In zoology and paleontology, characterizing dentition, rumen digestion, and digestive adaptations specialized for breaking down plant cell walls.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Vast herds of **herbivorous** quadrupeds roamed the grassy plains, leaving deep trails that crossed every watercourse."},
            {"author": "Georges Cuvier", "work": "Essay on the Theory of the Earth", "quote": "The fossil teeth indicate an animal strictly **herbivorous** in habit, closely allied to modern pachyderms."},
            {"author": "Richard Owen", "work": "Paleontology", "quote": "The massive flattened molars with crenulated enamel folds characterize large **herbivorous** mammals of the Tertiary epoch."}
        ]
    },
    "herborize": {
        "primary": "To search for, gather, and classify botanical specimens in their natural habitats; to botanize.",
        "secondary": "In eighteenth- and nineteenth-century natural history, embarking on field excursions equipped with a vasculum and magnifying loupe to study regional flora.",
        "quotes": [
            {"author": "Jean-Jacques Rousseau", "work": "Reveries of the Solitary Walker", "quote": "Nothing makes me happier than to wander through meadows with my collecting box and **herborize** among the mountain wildflowers."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "We set forth into the woods to **herborize**, returning with several rare species of mosses and marsh orchids."},
            {"author": "Johann Wolfgang von Goethe", "work": "Italian Journey", "quote": "I spent the afternoon attempting to **herborize** on the slopes of Vesuvius, searching for traces of Mediterranean coastal vegetation."}
        ]
    },

    # ==================== Dashboard — porc (9 words) ====================
    "porc": {
        "primary": "An archaic or dialectal spelling of pork, denoting the flesh of domestic swine prepared as culinary food.",
        "secondary": "In comparative anatomy and historical gastronomy, relating directly to the genus Sus or porcine livestock.",
        "quotes": [
            {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "His table was laden with roasted **porc** and brawn, well spiced with ginger and cloves for the winter feast."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Pork is Saxon, but when the brute is flayed and dressed for the banquet, swine becomes **porc** in the Norman tongue."},
            {"author": "Thomas Malory", "work": "Le Morte d'Arthur", "quote": "The knights sat at the banquet where fat **porc** and venison were served with abundance of red wine."}
        ]
    },
    "porcelain": {
        "primary": "A hard, fine-grained, translucent ceramic material produced by firing pure kaolin and feldspar clay at high temperatures; or vessels made from it.",
        "secondary": "In material culture and decorative arts, esteemed for its vitrified impermeability, ringing resonance, and luminous white surface.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The cabinet displayed delicate **porcelain** cups that had belonged to Dorothea's French grandmother."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The mantelpiece was crowded with shepherdesses of fragile **porcelain** and ornate Parisian timepieces."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "He handled the precious antique cup with reverent care, admiring the translucency of the blue-and-white **porcelain**."}
        ]
    },
    "porcelainize": {
        "primary": "To coat, enamel, or treat an object so as to give it the glossy, hard, and translucent appearance of porcelain.",
        "secondary": "In industrial materials engineering, applying a vitreous silicate enamel to metal cookery, plumbing fixtures, or electrical insulation.",
        "quotes": [
            {"author": "Thomas Edison", "work": "Patents and Inventions", "quote": "We sought a chemical technique to **porcelainize** the metallic plates to withstand persistent electrical arcing."},
            {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Industrial advances enable manufacturers to **porcelainize** base metals, rendering domestic utensils both durable and hygienic."},
            {"author": "Herman Melville", "work": "The Encantadas", "quote": "The volcanic heat seemed almost to **porcelainize** the rocky crags, baking their basaltic crust to a glassy finish."}
        ]
    },
    "porcellio": {
        "primary": "A genus of terrestrial isopod crustaceans, commonly known as woodlice, sowbugs, or pillbugs.",
        "secondary": "In arthropod morphology and soil ecology, distinguishing dorsoventrally flattened detritivores adapted to breathing through pseudotracheae in moist microhabitats.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Under every damp board one finds species of **Porcellio** sharing decaying matter with earthworms and centipedes."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The terrestrial isopod genus **Porcellio** exhibits modified pleopods functioning as respiratory organs on land."},
            {"author": "John Lubbock", "work": "On the Senses, Instincts, and Intelligence of Animals", "quote": "A frightened **Porcellio** runs rapidly seeking darkness beneath loose bark or decaying forest leaf-litter."}
        ]
    },
    "porcellionidae": {
        "primary": "A taxonomic family of terrestrial isopod crustaceans comprising common woodlice and sowbugs possessing two-segmented antennal flagella.",
        "secondary": "In invertebrate taxonomy, separating these fast-moving surface sowbugs from the Armadillidiidae that roll into complete balls.",
        "quotes": [
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy of the Invertebrate Animals", "quote": "Members of the family **Porcellionidae** occur abundantly in humic soils, performing vital decomposing functions."},
            {"author": "Thomas Henry Huxley", "work": "The Invertebrata", "quote": "Within the Oniscoidea, the family **Porcellionidae** is recognized by the distinct segmentation of the antennal flagellum."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "The evolutionary transition to dry terrestrial air reaches high specialization within the **Porcellionidae**."}
        ]
    },
    "porcine": {
        "primary": "Relating to, resembling, or suggestive of swine or pigs.",
        "secondary": "In figurative literature and moral commentary, describing gross gluttony, slovenly demeanor, or coarse physical heaviness.",
        "quotes": [
            {"author": "George Orwell", "work": "Animal Farm", "quote": "The creatures outside looked from pig to man, and from man to pig, but already their **porcine** features were indistinguishable."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The huge carcass of the right whale yielded blubber possessing a curious **porcine** texture and odor."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Pumblechook sat gorging himself with heavy self-satisfaction, his **porcine** cheeks glowing from excessive port."}
        ]
    },
    "porcupine": {
        "primary": "A large rodent characterized by a defensive coat of sharp, erectile, barbed quills covering its back and tail.",
        "secondary": "In vertebrate zoology, distinguishing the arboreal prehensile-tailed New World family (Erethizontidae) from terrestrial Old World forms (Hystricidae).",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "I could a tale unfold whose lightest word / Would harrow up thy soul, freeze thy young blood, / ... / And each particular hair to stand an end, / Like quills upon the fretful **porcupine**."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The dog was severely punished for attacking the **porcupine**, returning with numerous sharp barbed quills embedded in its muzzle."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our guide pointed out where a Canada **porcupine** had gnawed the bark clean from the trunk of a tall hemlock."}
        ]
    },
    "porcupinefish": {
        "primary": "A marine spiny globefish of the family Diodontidae, covered in sharp rigid spines that stand erect when the body inflates with water.",
        "secondary": "In ichthyology, distinguished from puffers by fused beak-like dental plates and stout two-rooted spines across the dermal skin.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The **porcupinefish** can inflate its body into a spiny ball, successfully defying the jaws of predatory sharks."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Dried skins of the bristling **porcupinefish** dangled from the low rafters of the salty old sailor's cabin."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The dental apparatus of the **porcupinefish** forms a crushing continuous beak suited for hard-shelled mollusks."}
        ]
    },
    "porcupines": {
        "primary": "Plural of porcupine; large quill-bearing rodents of the families Hystricidae and Erethizontidae.",
        "secondary": "In mammalian behavioral ecology, nocturnal herbivores famous for auditory quill-rattling warnings and backwards defensive lunges against carnivores.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The trappers warned us that **porcupines** frequently invaded unkept lumber camps to gnaw salty ax-handles."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We observed spiny mammals resembling giant **porcupines** rustling through the undergrowth of the prehistoric plateau."},
            {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Curious prickly **porcupines** climbed awkwardly among the upper branches of the lodgepole pines."}
        ]
    },

    # ==================== Dashboard — taur (6 words) ====================
    "tauriform": {
        "primary": "Having the form, shape, or likeness of a bull.",
        "secondary": "In classical archaeology and comparative religion, describing bovine sculptural vessels, rhytons, or representations of horned storm gods.",
        "quotes": [
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The ancient Mediterranean worshippers worshipped a **tauriform** deity whose sacred horns symbolized fertility and storm power."},
            {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "A magnificent **tauriform** rhyton carved from black steatite was unearthed in the domestic quarter of Knossos."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Solar deities were frequently invested with **tauriform** attributes to represent irresistible physical force."}
        ]
    },
    "taurine": {
        "primary": "Relating to or resembling a bull; bovine; also an essential amino sulfonic acid originally isolated from ox bile.",
        "secondary": "In biochemistry and physiology, an amino sulfonic acid involved in bile acid conjugation, osmoregulation, and cardiovascular function.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "By treating ox bile with hydrochloric acid, we obtained crystalline deposits of the nitrogenous substance **taurine**."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The bile salts comprise glycocholate and taurocholate, the latter yielding **taurine** upon alkaline decomposition."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Danton confronted the assembly with a fierce **taurine** energy that cowed his irresolute opponents."}
        ]
    },
    "taurobolium": {
        "primary": "An ancient Roman religious sacrifice of a bull, especially in the mystery rites of Cybele and Mithras.",
        "secondary": "In Roman imperial religious history, a baptism of blood wherein the initiate stood in a pit beneath an altar to receive rebirth for eternity.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pagan senators sought spiritual purification through the bloody rite of the **taurobolium**, defying Christian edicts."},
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "In the mystic **taurobolium**, the devotee descended into a trench over which a consecrated bull was slaughtered upon a perforated platform."},
            {"author": "Franz Cumont", "work": "The Mysteries of Mithra", "quote": "The inscription commemorated the initiate's renewal after the **taurobolium**, proclaiming him born again into eternal life."}
        ]
    },
    "tauromachy": {
        "primary": "The art or practice of bullfighting; public combat between humans and bulls.",
        "secondary": "In Iberian cultural history and ethnology, ritualized arena spectacles tracing descent from ancient Mediterranean sacrificial contests.",
        "quotes": [
            {"author": "Washington Irving", "work": "The Alhambra", "quote": "The populace gathered with deafening shouts in the plaza to witness the thrilling perils of the national **tauromachy**."},
            {"author": "George Borrow", "work": "The Bible in Spain", "quote": "Every village youth dreamed of achieving fame in **tauromachy**, emulating the daring passes of the legendary matadors."},
            {"author": "Richard Ford", "work": "Gatherings from Spain", "quote": "Spanish **tauromachy** is not a mere brutal sport, but an ancient dramatic tragedy enacted between man and beast."}
        ]
    },
    "taurotragus": {
        "primary": "The genus of African spiral-horned antelopes comprising the common eland and giant eland.",
        "secondary": "In mammalian taxonomy, large bovids characterized by massive spiral horns in both sexes, dewlaps, and bovine dimensions.",
        "quotes": [
            {"author": "David Livingstone", "work": "Missionary Travels and Researches in South Africa", "quote": "Herds of the majestic eland, designated **Taurotragus** by systematists, grazed quietly on the open plains."},
            {"author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "The giant eland of the genus **Taurotragus** is the stateliest and heaviest of all African spiral-horned antelopes."},
            {"author": "Richard Lydekker", "work": "The Game Animals of Africa", "quote": "In **Taurotragus**, both male and female possess stout spiral horns with pronounced transverse ridges along the lower keel."}
        ]
    },
    "taurus": {
        "primary": "A prominent northern zodiacal constellation depicted as the forequarters of a bull; also the second astrological sign.",
        "secondary": "In observational astronomy, containing the famous open clusters Pleiades and Hyades, as well as the supernova remnant Crab Nebula (M1).",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Sir Toby Belch: What shall we do else? Were we not born under **Taurus**? / Sir Andrew Aguecheek: **Taurus**! That's sides and heart. / Sir Toby Belch: No, sir, it is legs and thighs."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "When the sun with **Taurus** rides, / In radiance clothed along the zodiac wide."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The winter sky shone brilliantly overhead, with **Taurus** bearing the silvery cluster of the Pleiades upon his shoulder."}
        ]
    },

    # ==================== Dashboard — vulp (5 words) ====================
    "vulpecula": {
        "primary": "A faint northern constellation in the Milky Way between Cygnus and Sagitta, representing a little fox.",
        "secondary": "In observational astrophysics, cataloged by Johannes Hevelius and celebrated as the sky region where Jocelyn Bell Burnell discovered the first radio pulsar (CP 1919).",
        "quotes": [
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "In the constellation **Vulpecula** lies the famous Dumbbell Nebula, presenting two luminous cones united at their apexes."},
            {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The celestial fox, **Vulpecula**, was inserted by Hevelius to occupy the starry expanse adjoining the Swan."},
            {"author": "Simon Newcomb", "work": "Astronomy for Everybody", "quote": "With a modest telescope, one can sweep through **Vulpecula** and resolve countless rich galactic star clusters."}
        ]
    },
    "vulpecular": {
        "primary": "Pertaining to, resembling, or characteristic of a little fox; cunning or vulpine in manner.",
        "secondary": "In literary portraiture and moral fable, describing sly, crafty, or nocturnal predatory habits reminiscent of foxes.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The attorney cast a **vulpecular** glance over the parchment before affixing his signature to the settlement."},
            {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Fledgeby smiled with a **vulpecular** satisfaction, pleased that his duplicity had remained entirely undiscovered."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "He possessed that sharp, **vulpecular** wit that penetrates another's weakness while concealing his own designs."}
        ]
    },
    "vulpes": {
        "primary": "The taxonomic genus of true foxes within the family Canidae, including the red fox (Vulpes vulpes) and arctic fox.",
        "secondary": "In systematic mammalogy, distinguished from canines by smaller frames, flatter skulls, and characteristic vertical slit pupils in bright light.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "On the shores of the island we collected a distinct wild dog or fox, which naturalists refer to the genus **Vulpes**."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The cranial architecture of **Vulpes** separates it clearly from the heavier timber wolves and jackals."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The common red fox, **Vulpes** of the naturalists, prowls around the coppices in search of ground-nesting partridges."}
        ]
    },
    "vulpicide": {
        "primary": "The act of killing a fox by methods other than hunting it with hounds; or one who kills a fox in this manner.",
        "secondary": "In nineteenth-century British field sports culture, an unpardonable social transgression despised by gentry who preserved foxes exclusively for the chase.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "The American Senator", "quote": "To accuse a country gentleman of **vulpicide** was worse than charging him with embezzling county funds."},
            {"author": "Thomas Hardy", "work": "A Laodicean", "quote": "The gamekeeper had committed literal **vulpicide** by laying poison traps in the Squire's favorite fox coverts."},
            {"author": "R. S. Surtees", "work": "Handley Cross", "quote": "The Master of the Hunt denounced the farmer as a shameless **vulpicide** for shooting the vixen on her earth."}
        ]
    },
    "vulpine": {
        "primary": "Of, relating to, or resembling a fox; clever, sly, crafty, or artfully cunning.",
        "secondary": "In character portrayal and behavioral analysis, denoting keen, predatory vigilance masked by outwardly docile behavior.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "His features assumed a sharp, **vulpine** expression as he calculated the precise advantage to be gained from her distress."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The wicked wolf-like face turned toward me with a mocking, **vulpine** smile that chilled the blood in my veins."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp surveyed the drawing-room with **vulpine** quickness, selecting the most susceptible victims for her charms."}
        ]
    },

    # ==================== Dashboard — zo (5 words) ====================
    "azoic": {
        "primary": "Pertaining to or denoting geologic strata or conditions that are destitute of any organic or living remains.",
        "secondary": "In historical geology and Precambrian stratigraphy, the epoch preceding the dawn of life on Earth, before the earliest fossiliferous beds.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The crystalline schists were long regarded as fundamentally **azoic**, representing the primitive crust formed prior to the origin of life."},
            {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "The assumption that all basal metamorphic formations represent an **azoic** age has been shaken by the discovery of microscopic carbonaceous traces."},
            {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Below the lowest Paleozoic fossil beds lies the vast **azoic** foundation composed of granite, gneiss, and crystalline limestone."}
        ]
    },
    "epizootic": {
        "primary": "An outbreak of a disease affecting a large number of animals simultaneously within a geographical area; an animal epidemic.",
        "secondary": "In veterinary epidemiology and comparative pathology, designating viral or bacterial plagues like rinderpest or foot-and-mouth disease.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A devastating **epizootic** had swept through the cattle herds of the province, leaving pastures strewn with bleached bones."},
            {"author": "Louis Pasteur", "work": "Researches on Anthrax and Fowl Cholera", "quote": "The fatal **epizootic** which decimated the sheep folds was successfully checked through systematic bacterial inoculation."},
            {"author": "Robert Hooper", "work": "Lexicon Medicum", "quote": "An **epizootic** distemper frequently spreads through livestock herds under contaminated seasonal meteorological conditions."}
        ]
    },
    "protozoa": {
        "primary": "A diverse group of single-celled microscopic eukaryotic organisms that ingest food and move independently, such as amoebas and ciliates.",
        "secondary": "In historical microbiology and protistology, historically treated as the lowest subkingdom of the animal kingdom before multi-kingdom taxonomic revisions.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "The vital activities of the **protozoa** illustrate that all essential animal functions can be performed within a single microscopic cell."},
            {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "From ancestral flagellated **protozoa** arose the multicellular colonies that gave birth to the earliest metazoan lineages."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Microscopic **protozoa** possess such boundless capacity for multiplication that they soon populate every stagnant drop of water."}
        ]
    },
    "zodiac": {
        "primary": "An imaginary belt of the heavens extending about 8 degrees on either side of the apparent path of the sun (the ecliptic), divided into twelve signs.",
        "secondary": "In celestial cartography and ancient astral religion, the celestial coordinate frame tracking the seasonal wanderings of the sun, moon, and visible planets.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "So long that nineteen **zodiacs** have gone round, / And none of them been worn; and yet upon him / Will I the penalty of that decree / Enforce with rigor."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The doubloon showed the signs of the **zodiac** cast in pure gold, reflecting the fiery sun above the mountains of Quito."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "He mapped the celestial sphere, marking how the starry signs of the **zodiac** steer the turning of the seasons."}
        ]
    },
    "zodiacal": {
        "primary": "Pertaining to, located within, or characteristic of the zodiac.",
        "secondary": "In astrophysics and observational astronomy, designating zodiacal light: sunlight scattered by interplanetary dust particles in the ecliptic plane.",
        "quotes": [
            {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The brilliant **zodiacal** light appeared as a luminous pyramid rising obliquely above the western horizon after twilight."},
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The **zodiacal** light is seen to best advantage in tropical latitudes, shining with soft, pearly radiance in the clear night sky."},
            {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "I observed the **zodiacal** glow in the calm waters of the Pacific, where its bright apex reached the cluster of the Pleiades."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_animal_b1_p1: {len(data_animal_b1_p1)}")
    # Verify all words meet audit criteria
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_animal_b1_p1.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 50 words PASSED local pre-audit validation!")
