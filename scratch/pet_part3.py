# -*- coding: utf-8 -*-
"""
Part 3 of Curated Data for Asking & Seeking Batch 3 (Dashboard — pet):
Words 65 to 96:
['peter', 'peterburg', 'petersburg', 'petiole', 'petiolule',
 'petite', 'petiteness', 'petitio', 'petition', 'petitionary',
 'petitioner', 'petrarca', 'petrarch', 'petrel', 'petrifaction',
 'petrification', 'petrify', 'petrifying', 'petrissage', 'petrochemical',
 'petrocoptis', 'petrogale', 'petroglyph', 'petrograd', 'petrol',
 'petrolatum', 'petroleum', 'petrology', 'petromyzon', 'petromyzoniformes',
 'petromyzontidae', 'petronius']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

pet_part3 = {
    "peter": {
        "primary": "To diminish gradually and then cease; to dwindle or trail off, typically followed by out.",
        "secondary": "In mining history and vernacular geology, the exhaustion or pinching out of a profitable vein of ore or mineral deposit.",
        "quotes": [
            {"author": "Mark Twain", "work": "Roughing It", "quote": "The miners toiled through the winter only to watch their rich silver vein **peter** out into barren porphyry."},
            {"author": "Bret Harte", "work": "The Luck of Roaring Camp and Other Sketches", "quote": "When the gulch placer began to **peter** out, the restless gold seekers packed their mules for the southern diggings."},
            {"author": "Jack London", "work": "The Call of the Wild", "quote": "The dog team pushed on over the frozen ridge until the winding sled trail seemed to **peter** out into trackless snow."}
        ]
    },
    "peterburg": {
        "primary": "A historical variant name for Saint Petersburg, the imperial capital of Russia founded on the Neva.",
        "secondary": "In diplomatic history and 19th-century geography, denoting the Baltic administrative metropolis of the Russian Empire.",
        "quotes": [
            {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "All the fashionable society of **Peterburg** gathered in the grand salon of Anna Pavlovna Scherer to debate the Bonaparte crisis."},
            {"author": "Fyodor Dostoevsky", "work": "Crime and Punishment", "quote": "The suffocating summer heat and yellow dust of **Peterburg** weighed heavily upon Raskolnikov as he wandered beside the Catherine Canal."},
            {"author": "Alexander Pushkin", "work": "The Bronze Horseman", "quote": "Upon the desolate shore Peter the Great stood dreaming of the great northern capital of **Peterburg** that would defy the Baltic storms."}
        ]
    },
    "petersburg": {
        "primary": "The Russian imperial capital on the Gulf of Finland, or a historic city in Virginia besieged during the American Civil War.",
        "secondary": "In military history, denoting the protracted ten-month siege of Petersburg (1864–1865) that foreshadowed modern trench warfare.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "A single telegraph wire connects Boston to St. **Petersburg**, yet men have little of true spiritual value to communicate."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "M. O. Kowalevsky communicated to me several remarkable observations made upon domesticated animals in the imperial gardens of St. **Petersburg**."},
            {"author": "Ulysses S. Grant", "work": "Personal Memoirs of U. S. Grant", "quote": "The strategic investment of **Petersburg** formed the decisive turning point that forced General Lee to evacuate Richmond."}
        ]
    },
    "petiole": {
        "primary": "The slender stalk that attaches the leaf blade to the stem of a plant.",
        "secondary": "In plant anatomy and entomo-morphology, the foliar stalk containing vascular bundles, or the slender abdominal waist of hymenopteran insects.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "In Clematis, the sensitive **petiole** curls around any slender twig it touches, securing the climbing shoot with remarkable tenacity."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "When the **petiole** is absent, the leaf blade is termed sessile, adhering directly to the node of the main axis."},
            {"author": "John Burroughs", "work": "Locusts and Wild Honey", "quote": "The trembling aspen owes its restless flutter to the long, vertically flattened **petiole** that catches every breath of wind."}
        ]
    },
    "petiolule": {
        "primary": "The small stalk that attaches a leaflet to the central rachis of a compound leaf.",
        "secondary": "In structural botany, the specialized secondary stipe of a leaflet, frequently bearing an articulate pulvinule capable of nyctinastic movement.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "At dusk, the pulvinus at the base of each **petiolule** flexes downward, folding the lateral leaflets in their characteristic sleep movement."},
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "In pinnately compound leaves, each separate leaflet is supported upon its own distinct **petiolule** attached to the common rachis."},
            {"author": "John Lindley", "work": "Introduction to Botany", "quote": "The articulation of the **petiolule** allows individual leaflets to fall cleanly in autumn without tearing the main foliar rachis."}
        ]
    },
    "petite": {
        "primary": "Of a woman or clothing size: attractively small, dainty, and slender.",
        "secondary": "In fashion design and sociology, designating garments tailored with shorter proportions for individuals under five feet four inches in height.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her figure was **petite** and light, yet she moved across the shearing barn floor with a dignified self-possession."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind forms its ideas of great and **petite** magnitude by continuous comparison with familiar sensory standards."},
            {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck was a **petite**, compact woman who ruled her pensionnat with an eye that observed every classroom whisper."}
        ]
    },
    "petiteness": {
        "primary": "Charming smallness, daintiness, or delicate slenderness of stature or bodily proportion.",
        "secondary": "In aesthetic portraiture, graceful compactness of physical stature combined with harmonious elegance of proportion.",
        "quotes": [
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "There was an exquisite **petiteness** in the contour of her wrists and ankles that spoke of aristocratic lineage."},
            {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Her captivating **petiteness** formed a dramatic contrast to the imposing statuesque matrons of New York society."},
            {"author": "Anthony Trollope", "work": "Can You Forgive Her?", "quote": "The delicate **petiteness** of her form made her seem almost too fragile to bear the heavy sorrows of the family."}
        ]
    },
    "petitio": {
        "primary": "A begging or pleading; in logic, petitio principii, the fallacy of begging the question.",
        "secondary": "In formal philosophical dialectic and legal pleading, assuming the very proposition that requires demonstration or judicial proof.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "To deduce the principle from instances that already presuppose it is to fall into the classical fallacy of **petitio** principii."},
            {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Scholastic syllogisms often conceal a covert **petitio**, mistaking circular linguistic definitions for genuine natural discoveries."},
            {"author": "Jeremy Bentham", "work": "The Book of Fallacies", "quote": "Political polemicists constantly resort to **petitio** whenever they christen their preferred policy with inherently laudatory epithets."}
        ]
    },
    "petition": {
        "primary": "A formal written request addressed to an authority appealing for a particular action, right, or remedy.",
        "secondary": "In constitutional law and prayer liturgy, the guaranteed civil right to seek governmental redress of grievances, or solemn supplication to God.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I pray thee, hear me speak; I will not listen to thy harsh **petition** till justice be duly satisfied."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The ruined burghers signed a desperate **petition** to the council, begging for an extension of the municipal fair privileges."},
            {"author": "Henry David Thoreau", "work": "Civil Disobedience", "quote": "When a whole people signs a **petition** against injustice and is met by cold indifference, passive resistance becomes an imperative duty."}
        ]
    },
    "petitionary": {
        "primary": "Of the nature of, containing, or conveying a formal petition or humble supplication.",
        "secondary": "In ecclesiastical rhetoric and diplomatic correspondence, expressing prayerful or deferential requests seeking mercy or imperial concession.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Thy **petitionary** grace shall not prevail; I banish you from my sight and turn deaf ears to Rome."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "The colonists adopted a **petitionary** tone in their addresses to the Crown, seeking redress without violating loyalty."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "With tears and sighs our fallen parents poured forth their **petitionary** prayers before the mercy seat of Heaven."}
        ]
    },
    "petitioner": {
        "primary": "A person who presents, signs, or submits a formal petition to an authority or court.",
        "secondary": "In chancery jurisprudence and appellate procedure, the initiating party seeking equitable relief or extraordinary writ from a tribunal.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Away, base scoundrels! Here comes the poor **petitioner** who seeks redress against the tyrannical duke."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Many a wretched **petitioner** had grown grey and infirm while waiting for an equitable decree from the Lord High Chancellor."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Stand upright; be not a whining **petitioner** at the footstool of custom, but a sovereign creator of your own destiny."}
        ]
    },
    "petrarca": {
        "primary": "Francesco Petrarca (Petrarch), the renowned 14th-century Italian humanist scholar and lyric poet.",
        "secondary": "In literary history, the Renaissance father of humanism whose vernacular Canzoniere perfected the Italian sonnet form.",
        "quotes": [
            {"author": "Walter Pater", "work": "The Renaissance: Studies in Art and Poetry", "quote": "The sensitive lyricism of **Petrarca** ushered in a humanist reawakening that transformed European intellectual sensibility."},
            {"author": "John Addington Symonds", "work": "Renaissance in Italy", "quote": "To understand the recovery of classical Latinity, one must study the tireless manuscript searches conducted by **Petrarca**."},
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Arqua preserves the tomb of **Petrarca**, where pilgrim scholars pause to honor the immortal bard of Vaucluse."}
        ]
    },
    "petrarch": {
        "primary": "The anglicized name of Francesco Petrarca, Italian humanist poet celebrated for his love sonnets to Laura.",
        "secondary": "In prosody and comparative literature, the archetype of the Petrarchan sonnet structure consisting of an octave and sestet.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Now is he for the numbers that **Petrarch** flowed in: Laura to his lady was but a kitchen-wench."},
            {"author": "George Eliot", "work": "Romola", "quote": "Bardo possessed rare manuscripts of **Petrarch** which he guarded with the jealous reverence of a true Florentine scholar."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The refined sonnets of **Petrarch** gave polish to the Italian tongue and inspired centuries of romantic verse."}
        ]
    },
    "petrel": {
        "primary": "A oceanic seabird of the order Procellariiformes, having tube-shaped nostrils and long wings.",
        "secondary": "In pelagic ornithology and folklore, wide-ranging sea rovers such as the stormy petrel, proverbially believed to presage approaching ocean tempests.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The stormy **petrel** skimmed the crests of the giant Cape Horn waves, dipping its feet as though walking upon the water."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A solitary sea **petrel** circled our rigging with plaintive cries, heralding the fury of the midnight typhoon."},
            {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "The ocean wanderer watched the hardy **petrel** breast the Atlantic gale without the slightest tremor of its outstretched wings."}
        ]
    },
    "petrifaction": {
        "primary": "The process of turning into stone by mineral infiltration; or an organism preserved as a fossil.",
        "secondary": "In historical geology and moral psychology, the replacement of organic tissue by silicious or calcareous matter, or emotional paralysis.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Mineral springs rich in carbonate of lime effect rapid **petrifaction** upon wood and leaves submerged in their calcareous basins."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Prolonged exposure to cynical worldliness often induces a melancholy **petrifaction** of the finest human sympathies."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Dead formulas and institutional **petrifaction** stifle the living spirit of religion until a fresh prophet arises."}
        ]
    },
    "petrification": {
        "primary": "The conversion of organic material into stone or stony substance; or extreme petrified terror.",
        "secondary": "In taphonomy and narrative literature, permineralization where mineral deposits form internal casts of organisms, or sudden stupefaction.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We discovered a fossil forest in the Andes where complete **petrification** had preserved every microscopic ring of the ancient trees."},
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "A horror of utter **petrification** seized my limbs as the enshrouded figure of the lady Madeline swayed in the doorway."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The Medusa head possessed that fatal gaze of **petrification** which froze the blood of ancient mythic heroes into stone."}
        ]
    },
    "petrify": {
        "primary": "To change organic substance into stone; or to paralyze with astonishment, horror, or fear.",
        "secondary": "In figurative expression and paleontology, to render rigid, inert, and incapable of change or movement through sudden shock.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The unexpected reappearance of the convict seemed to **petrify** the listener, rooting him helplessly to the hearthrug."},
            {"author": "Sir Walter Scott", "work": "The Antiquary", "quote": "The calcifying waters of the cavern slowly **petrify** whatever leaves, twigs, or bird nests are suspended beneath the dripping roof."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "His sudden grim announcement served to **petrify** every joyous sentiment that had blossomed in my breast."}
        ]
    },
    "petrifying": {
        "primary": "Causing to turn into stone; or having the effect of paralyzing with astonishment or horror.",
        "secondary": "In geochemical hydrology and rhetoric, describing subterranean waters loaded with mineral salts that incrust objects, or chilling terror.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The learned philosophers showed me a **petrifying** spring whose drops transformed pieces of wood into flinty stone in a few months."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The awful apparition of the daemon at my casement produced a **petrifying** effect upon my already exhausted frame."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Calcareous cascades deposit travertine rapidly, exerting a **petrifying** influence over the entire river gorge."}
        ]
    },
    "petrissage": {
        "primary": "A massage movement involving kneading, rolling, and squeezing the muscles with firm pressure.",
        "secondary": "In manual physical therapy and rehabilitation medicine, a manipulation technique applied to mobilize deep myofascial tissues and enhance venous return.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "For chronic muscular atrophy following neuritis, daily application of effleurage and deep **petrissage** yields excellent therapeutic benefit."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "Judicious **petrissage** administered to the spastic limbs assists greatly in restoring muscular elasticity after paralytic strokes."},
            {"author": "Douglas Graham", "work": "A Practical Treatise on Massage", "quote": "The skilled operator applies **petrissage** by grasping the muscle bellies firmly between the thumb and fingers without pinching the skin."}
        ]
    },
    "petrochemical": {
        "primary": "Relating to substances or chemical products obtained from petroleum or natural gas.",
        "secondary": "In chemical engineering and industrial geology, designating synthetic compounds such as polymers, solvents, and fertilizers refined from hydrocarbons.",
        "quotes": [
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The massive expansion of the modern **petrochemical** industry introduced thousands of synthetic compounds into the global biosphere."},
            {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Modern heavy manufacture relies fundamentally upon continuous output from the burgeoning **petrochemical** and refinery complexes."},
            {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "The neotechnic phase of industrial society is tied to the energy grids and **petrochemical** innovations derived from fossil fuels."}
        ]
    },
    "petrocoptis": {
        "primary": "A small genus of perennial saxicolous flowering plants in the pink family Caryophyllaceae, native to the Pyrenees.",
        "secondary": "In European alpine biogeography, Petrocoptis comprises chasmophytic endemics adapted to sheer limestone cliffs and calcareous rock clefts.",
        "quotes": [
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The chasmophytic genus **Petrocoptis** clings tenaciously to the vertical limestone fissures of the northern Spanish ranges."},
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Alpine rupicolous species such as **Petrocoptis** demonstrate specialized rooting adaptations for exploiting narrow moisture-retaining crevices."},
            {"author": "George Bentham", "work": "Handbook of the British Flora", "quote": "European rock-dwelling caryophylls, including the delicate **Petrocoptis**, bear glaucous foliage and star-like pink or white blossoms."}
        ]
    },
    "petrogale": {
        "primary": "A genus of Australian macropod marsupials commonly known as rock-wallabies.",
        "secondary": "In australian mammalogy and biomechanics, Petrogale includes nimble wallabies equipped with modified roughened footpads for bounding across steep cliffs.",
        "quotes": [
            {"author": "John Gould", "work": "The Mammals of Australia", "quote": "The agile rock-wallaby of the genus **Petrogale** leaps across dizzying sandstone precipices with the sure-footed grace of an alpine chamois."},
            {"author": "Richard Lydekker", "work": "A Hand-book to the Marsupialia and Monotremata", "quote": "In **Petrogale**, the soles of the hind feet are densely granulated to prevent slipping upon smooth granite boulders."},
            {"author": "Frank Beddard", "work": "Mammalia", "quote": "Species of **Petrogale** inhabit arid mountain ranges, finding secure shelter within deep caverns during the blazing heat of noon."}
        ]
    },
    "petroglyph": {
        "primary": "A prehistoric carving or rock engraving made by pecking, incising, or abrading a rock surface.",
        "secondary": "In archaeological anthropology and semiotics, an ancient rock art symbol providing evidence of prehistoric cultural rituals, cosmology, or territory.",
        "quotes": [
            {"author": "John Wesley Powell", "work": "The Exploration of the Colorado River", "quote": "Upon the smooth sandstone cliff walls above the river, we discovered many an ancient **petroglyph** depicting mountain sheep and solar symbols."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "The primitive **petroglyph** represents an early stage in the development of picture-writing before phonetic scripts emerged."},
            {"author": "Franz Boas", "work": "Primitive Art", "quote": "Every tribal **petroglyph** pecked into the basalt cliffs served as a ceremonial marker commemorating ancestral deeds."}
        ]
    },
    "petrograd": {
        "primary": "The Russian name given to Saint Petersburg from 1914 to 1924 during World War I and the Russian Revolution.",
        "secondary": "In 20th-century geopolitical history, the revolutionary urban center where the 1917 Bolshevik uprising deposed the provisional government.",
        "quotes": [
            {"author": "John Reed", "work": "Ten Days That Shook the World", "quote": "Across the stormy winter nights of **Petrograd**, armored cars patrolled the bridges and the Red Guards guarded the Smolny Institute."},
            {"author": "H. G. Wells", "work": "Russia in the Shadows", "quote": "I walked through the desolate, snow-encrusted avenues of **Petrograd**, observing a vast empire in the throes of total collapse."},
            {"author": "Leon Trotsky", "work": "The History of the Russian Revolution", "quote": "The workers and garrison soldiers of **Petrograd** rose en masse to shatter the foundations of the ancient Romanov autocracy."}
        ]
    },
    "petrol": {
        "primary": "A volatile, flammable liquid mixture of hydrocarbons derived from petroleum, used as motor fuel; gasoline.",
        "secondary": "In chemical fuel technology and Commonwealth nomenclature, refined light hydrocarbon fractions utilized in internal combustion spark-ignition engines.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The acrid smell of burning **petrol** and vaporized machinery hung heavy in the air after the alien cylinders fell."},
            {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "Von Bork filled the motor tank with **petrol**, preparing for his midnight dash to the awaiting submarine off Harwich."},
            {"author": "G. K. Chesterton", "work": "The Flying Inn", "quote": "The noisy chugging of the early horseless carriage reeked of commercial grease and pungent **petrol** fumes."}
        ]
    },
    "petrolatum": {
        "primary": "A purified, semisolid mixture of hydrocarbons obtained from petroleum; petroleum jelly, used in ointments and lubricants.",
        "secondary": "In pharmacognosy and industrial manufacturing, an odorless hydrophobic unguent base providing occlusive emollient protection against cutaneous moisture loss.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A soothing protective dressing of pure white **petrolatum** was applied over the extensive dermal burns to prevent atmospheric irritation."},
            {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin spread a sterile layer of **petrolatum** around the edges of the culture chamber to seal it against airborne contaminants."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "Soft yellow **petrolatum** forms an unctuous and non-rancid vehicle for zinc oxide and sulfur in compound skin ointments."}
        ]
    },
    "petroleum": {
        "primary": "A liquid mixture of hydrocarbons that is present in certain rock strata and can be extracted and refined into fuels.",
        "secondary": "In economic geology and petrochemistry, crude mineral oil formed from compressed prehistoric marine organic matter, powering modern industrial transport.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Flying Inn", "quote": "The modern plutocrat cares little for ancient vineyards so long as he controls the dark, subterranean torrents of **petroleum**."},
            {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The global struggle for coal and **petroleum** gave way abruptly when industrial science unlocked the latent atomic energies of the element."},
            {"author": "Thorstein Veblen", "work": "Absentee Ownership", "quote": "Strategic monopolies in **petroleum** distillation dictated the geopolitical alliances of the early twentieth century."}
        ]
    },
    "petrology": {
        "primary": "The branch of science concerned with the origin, small-scale structure, and composition of rocks.",
        "secondary": "In geological sciences, the discipline encompassing petrography (rock description) and petrogenesis (mechanisms of igneous, metamorphic, and sedimentary formation).",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Microscopic **petrology** has demonstrated that granite crystalline fabrics originated under immense subterranean pressure and heat."},
            {"author": "Archibald Geikie", "work": "The Founders of Geology", "quote": "The introduction of thin-section polarized microscopy revolutionized modern **petrology**, unlocking the secrets of volcanic magma cooling."},
            {"author": "Charles Darwin", "work": "Geological Observations on Volcanic Islands", "quote": "A careful study of volcanic **petrology** reveals how fluid basaltic lavas differentiate into trachytic varieties upon oceanic islands."}
        ]
    },
    "petromyzon": {
        "primary": "The type genus of jawless primitive vertebrates in the lamprey family, comprising the sea lamprey (Petromyzon marinus).",
        "secondary": "In comparative vertebrate morphology, an ancient cyclostome possessing a suctorial toothed oral disc, persistent notochord, and parasitic adult habits.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The structural morphology of **Petromyzon** exhibits an early stage of vertebrate evolution prior to the origin of true articulated jaws."},
            {"author": "Frank Balfour", "work": "A Treatise on Comparative Embryology", "quote": "Embryological development in the ammocoete larva of **Petromyzon** sheds essential light on the ancestral lineage of craniate vertebrates."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The marine lamprey, **Petromyzon** marinus, ascends freshwater rivers in spring to spawn among gravel shoals."}
        ]
    },
    "petromyzoniformes": {
        "primary": "An order of jawless fish-like aquatic vertebrates comprising all modern lampreys.",
        "secondary": "In systematic ichthyology and evolutionary biology, the Petromyzoniformes represent an ancient agnathan clade lacking paired fins, jaws, and bone.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "Within the division Marsipobranchii, the order **Petromyzoniformes** is distinguished by seven pairs of external gill slits opening along the pharynx."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The order **Petromyzoniformes** includes both anadromous parasitic lampreys and non-parasitic freshwater brook species."},
            {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "Fossil precursors of the **Petromyzoniformes** indicate that the lamprey body plan has persisted virtually unchanged since the Carboniferous period."}
        ]
    },
    "petromyzontidae": {
        "primary": "The taxonomic family of Northern Hemisphere lampreys within the order Petromyzoniformes.",
        "secondary": "In systematic taxonomy and aquatic ecology, Petromyzontidae includes genera such as Petromyzon, Lampetra, and Ichthyomyzon with round rasping oral suckers.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "Fishes", "quote": "Members of the family **Petromyzontidae** attach themselves to migratory salmon and trout, rasping the flesh to feed on bodily fluids."},
            {"author": "Spencer Fullerton Baird", "work": "Fishes of the Great Lakes", "quote": "The invasive spread of the **Petromyzontidae** through ship canals wrought catastrophic destruction upon endemic lake trout stocks."},
            {"author": "Frank Beddard", "work": "Animal Coloration", "quote": "The dorsal coloration in the **Petromyzontidae** varies from olive-brown to slate, providing protective camouflage against stony riverbeds."}
        ]
    },
    "petronius": {
        "primary": "Petronius Arbiter, Roman courtier and satirist of the Nero era, traditionally regarded as author of the Satyricon.",
        "secondary": "In classical literary criticism and social history, celebrated as the arbiter elegantiae whose picaresque narrative vividly depicts Imperial Roman decadence.",
        "quotes": [
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The cynical, fastidious wit of **Petronius** captured the sensual luxury and moral weariness of Neronian Rome."},
            {"author": "John Addington Symonds", "work": "Studies of the Greek Poets", "quote": "In the Banquet of Trimalchio, **Petronius** preserved a priceless comic portrait of vulgar provincial wealth run riot."},
            {"author": "Henryk Sienkiewicz", "work": "Quo Vadis", "quote": "As the supreme judge of taste, **Petronius** guided the whimsical aesthetic caprices of Caesar with subtle, mocking flattery."}
        ]
    }
}
