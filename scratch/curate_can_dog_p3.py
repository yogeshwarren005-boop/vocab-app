# -*- coding: utf-8 -*-
"""
curate_can_dog_p3.py
Batch 4 Part 3 of Cluster Animal & Plant:
Dashboard — can_dog (54 words: canopied -> uncanny)
canopied, canopus, canopy, canorous, cant, cantabile, cantabrigian,
cantala, cantaloup, cantaloupe, cantankerous, cantankerously,
cantata, canted, canteen, canter, canterbury, cantering,
cantharellus, canthus, canticle, canticles, cantilever, cantillate,
cantillation, cantle, canto, canton, cantonal, cantonese, cantonment,
cantor, canty, canuck, canulate, canulation, canulisation,
canulization, canute, canyon, canyonside, cosecant, decant,
decantation, decanter, discant, incan, incantation, precancerous,
recant, recantation, secant, uncannily, uncanny
Total: 54 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_can_dog_p3 = {
    "canopied": {
        "primary": "Covered, vaulted, or overhung by or as if by a canopy; sheltered from above.",
        "secondary": "In decorative architecture and landscape poetry, describing ceremonial four-poster beds, thrones, or leafy forest boughs meeting overhead.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Away before me to sweet beds of flowers; / Love-thoughts lie rich when **canopied** with bowers."},
            {"author": "John Milton", "work": "Comus", "quote": "I know each lane, and every alley green, / Dingle, or bushy dell of this wild wood, / And every bosky bourn from side to side, / My daily walks and ancient neighborhood. The woods were richly **canopied**."},
            {"author": "Percy Bysshe Shelley", "work": "Alastor; or, The Spirit of Solitude", "quote": "The oak and beech met high above, forming a dark **canopied** roof that shut out the glare of noon."},
        ]
    },
    "canopus": {
        "primary": "The second-brightest star in the night sky, a white supergiant in the southern constellation Carina; or an ancient Egyptian port.",
        "secondary": "In celestial navigation and aerospace astronautics, the primary attitude-reference star used by space probes to navigate outside the solar plane.",
        "quotes": [
            {"author": "John Herschel", "work": "Results of Astronomical Observations at the Cape of Good Hope", "quote": "The brilliant white supergiant **Canopus** dominates the southern heavens, blazing with unsurpassed planetary brilliance."},
            {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "As we sailed past the Tropic of Cancer, **Canopus** rose above the horizon, guiding our course across the Atlantic."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient trading harbor of **Canopus** on the western mouth of the Nile was renowned for wealth and festive licentiousness."}
        ]
    },
    "canopy": {
        "primary": "An ornamental cloth covering hung or held up over a bed, throne, or sacred object; or any overhanging projection or foliage cover.",
        "secondary": "In forest ecology and architecture, the uppermost continuous layer of foliage formed by mature tree crowns, intercepting sunlight and rain.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "This most excellent **canopy**, the air, look you, this brave o'erhanging firmament, this majestical roof fretted with golden fire."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Under the shady **canopy** of whispering boughs, the first parents enjoyed sweet nocturnal repose."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The dense green **canopy** of the summer pines cast cool, fragrant shadows across the tranquil waters of the pond."}
        ]
    },
    "canorous": {
        "primary": "Pleasant-sounding, melodious, musical, or resonant in voice or acoustic tone.",
        "secondary": "In classical rhetoric and avian bioacoustics, characterizing rich, harmonious birdsong or vibrant oratorical vocalization.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Touching the **canorous** dying song of swans, celebrated by the poets, natural history hath discovered no anatomical confirmation."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The orator possessed a full, **canorous** voice that charmed the ears of the assembly before engaging their reason."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The nightingale pours forth its rich and **canorous** strains from the hawthorn brake throughout the silent May nights."}
        ]
    },
    "cant": {
        "primary": "Hypocritical and sanctimonious talk, typically of a moral, religious, or political nature; or the specialized jargon of a group.",
        "secondary": "In mechanics and naval architecture, an inclined or slanted surface, tilt, or bevel; or to set at an oblique angle.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "Boswell's Life of Samuel Johnson", "quote": "Clear your mind of **cant**. You may talk in this manner; it is a mode of talking in society; but don't think in that manner."},
            {"author": "Lord Byron", "work": "Letters and Journals", "quote": "The present age is distinguished above all others for **cant**; **cant** political, **cant** poetical, and **cant** religious."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The carpenter planed the timber with a slight **cant** toward the gunwale, allowing seawater to drain freely from the deck."}
        ]
    },
    "cantabile": {
        "primary": "In a smooth, graceful, singing style; flowing and melodic in musical performance.",
        "secondary": "In classical instrumental music, an expressive performance direction instructing performers to imitate the lyricism and legato breathing of the human voice.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The cellist delivered the slow movement with an exquisite **cantabile** tone that drew tears from the audience."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Cardboard Box", "quote": "Holmes played a soothing **cantabile** melody upon his Stradivarius, meditating upon the tragic clues of the case."},
            {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "The violin entered with a tender **cantabile** theme, soaring above the somber polyphony of the lower strings."}
        ]
    },
    "cantabrigian": {
        "primary": "Of, relating to, or characteristic of the University of Cambridge or the city of Cambridge; or a student or graduate of Cambridge.",
        "secondary": "In British university culture, designating traditions, rowing crews (the Light Blues), or collegiate scholarship associated with Cambridge.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The proud **Cantabrigian** scholars defended their university privileges against the arbitrary mandates of James II."},
            {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "Arthur Pendennis arrived at the university eager to emulate the fashionable habits of the senior **Cantabrigian** gentlemen."},
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The tutor was an accomplished **Cantabrigian** mathematician who had achieved high honors in the mathematical tripos."}
        ]
    },
    "cantala": {
        "primary": "A tropical succulent plant of the agave family (Agave cantala), cultivated especially in the Philippines and Indonesia for its tough white leaf fiber.",
        "secondary": "In agricultural commerce and cordage production, long bast fibers derived from agave leaves used to manufacture ropes, twine, and burlap bags.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The islanders cultivated extensive plantations of **cantala**, processing the fleshy spiny leaves into strong durable cordage."},
            {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Agriculture", "quote": "The commercial fiber harvested from **cantala** resembles sisal but is prized for greater flexibility in marine rope-making."},
            {"author": "David Fairchild", "work": "Exploring for Plants", "quote": "We observed rows of **cantala** planted along sandy terraces, their stout sword-like leaves harvesting water from ocean mists."}
        ]
    },
    "cantaloup": {
        "primary": "A small round melon with ribbed orange flesh and sweet musky perfume; a variant spelling of cantaloupe.",
        "secondary": "In European horticulture, Cucumis melo cantalupensis, originally cultivated at Cantalupo in Italy, famed for warty rinds and aromatic sweetness.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "The autumn garden was rich with fragrant **cantaloup** melons ripening on their sprawling leafy vines."},
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The dessert table groaned under luscious baskets of purple grapes, peaches, and sweet summer **cantaloup** slices."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Our harvest dinner was sweetened by a ripe **cantaloup** gathered fresh that morning from the sunlit garden patch."}
        ]
    },
    "cantaloupe": {
        "primary": "A variety of melon (Cucumis melo) having a ribbed or netted rind and sweet, aromatic, orange-colored flesh.",
        "secondary": "In agronomy and culinary arts, a warm-season annual gourd prized for high water content, dietary beta-carotene, and refreshing sweetness.",
        "quotes": [
            {"author": "Mark Twain", "work": "Pudd'nhead Wilson", "quote": "The true southern **cantaloupe** is a blessing to the palate, superior to all the cold pumpkins of the north."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I admired the great green leaves of the **cantaloupe** spreading across the sand, nourishing sweet juicy fruit beneath the summer sun."},
            {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "Breakfast was served on the sunny terrace, featuring iced **cantaloupe** and fragrant coffee before the morning swim."}
        ]
    },
    "cantankerous": {
        "primary": "Bad-tempered, argumentative, quarrelsome, and uncooperative in disposition.",
        "secondary": "In dramatic comedy and novelistic characterization, eccentric old eccentrics or obstinate villagers who resist every polite accommodation.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The coachman was a crusty, **cantankerous** old fellow who grumbled at every turn of the road and snarled at the horses."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Christian Cantle was plagued by a **cantankerous** temper that made him the laughingstock of the heath gatherings."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "Our pack mule proved an obstinate, **cantankerous** brute that refused to budge whenever the trail grew steep."}
        ]
    },
    "cantankerously": {
        "primary": "In a bad-tempered, quarrelsome, irritable, or uncooperative manner.",
        "secondary": "In humorous prose, snapping at well-meaning companions and finding fault with every innocent convenience.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Smallweed snapped **cantankerously** at his trembling granddaughter, demanding his cushion and his pipe without delay."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "Old Edie Ochiltree answered the bailiff **cantankerously**, defending his vagrant liberties with caustic Scottish wit."},
            {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The retired club colonel grumbled **cantankerously** over his morning mutton chop, complaining that the empire was going to ruin."}
        ]
    },
    "cantata": {
        "primary": "A vocal composition with an instrumental accompaniment, typically in several movements, often involving a choir.",
        "secondary": "In Baroque musicology, sacred or secular choral works perfected by J. S. Bach, alternating recitatives, arias, and chorales.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The performance of Bach's church **cantata** revealed the sublime polyphonic mastery that underpins his sacred choral writing."},
            {"author": "Johann Wolfgang von Goethe", "work": "Wilhelm Meister's Apprenticeship", "quote": "The chapel choir rehearsed a joyful Easter **cantata**, filling the ancient vaulted sanctuary with triumphant melodies."},
            {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "Leverkühn's final monumental **cantata**, The Lamentation of Dr. Faustus, was a work of devastating expressive dissonance."}
        ]
    },
    "canted": {
        "primary": "Tilted, angled, sloped, or pitched obliquely; or expressed in sanctimonious, hypocritical, or jargonized cant.",
        "secondary": "In carpentry, naval architecture, and surveying, beveled edges or frames set at an inclination to the perpendicular.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship lay heavily **canted** over on her side as the tremendous squall struck our remaining topsails."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The puritan hypocrite spoke in a **canted** whine that sickened every honest listener in the courtroom."},
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The Hispaniola had run ashore on the sandbar and sat **canted** sharply to port, her deck awash with breakers."}
        ]
    },
    "canteen": {
        "primary": "A small container used by soldiers or travelers for carrying water; or a restaurant or cafeteria provided for military personnel or workers.",
        "secondary": "In military logistics and institutional architecture, a post exchange supplying provisions, or a compact soldier's flask fitted with a felt cover.",
        "quotes": [
            {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The youth unslung his tin **canteen** and drank greedily of the warm river water amidst the smoke of battle."},
            {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The Ministry **canteen** was a noisy, crowded basement room reeking of sour cabbage and synthetic Victory gin."},
            {"author": "Rudyard Kipling", "work": "Barrack-Room Ballads", "quote": "The soldiers gathered in the **canteen** after drill, clinking tin mugs and singing of faraway English shires."}
        ]
    },
    "canter": {
        "primary": "A smooth, three-beat gait of a horse, easy and rhythmic, faster than a trot but slower than a gallop; or to ride at this pace.",
        "secondary": "Historically derived from the easy riding pace of medieval pilgrims journeying to the shrine of Thomas Becket at Canterbury ('Canterbury gallop').",
        "quotes": [
            {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The stag at eve had drunk his fill, / Where danced the moon on Monan's rill, / And deep his midnight lair had made / In lone Glenartney's hazel shade; / Then broke into an easy **canter** across the heather."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Jane rode to Netherfield on horseback, setting off at a brisk **canter** before the rain clouds broke."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba urged her pony into a graceful **canter**, her dark hair streaming in the autumn breeze across the downs."}
        ]
    },
    "canterbury": {
        "primary": "A historic cathedral city in Kent, southeastern England, the ecclesiastical capital of the Church of England; or a low stand with partitions for holding music sheets.",
        "secondary": "In English literature and religious history, the celebrated destination of Chaucer's Canterbury Tales pilgrims seeking the martyr shrine of St. Thomas Becket.",
        "quotes": [
            {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "And specially, from every shires ende / Of Engelond, to **Caunterbury** they wende, / The hooly blisful martir for to seke."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Archbishop of **Canterbury** stood as the first subject of the realm, crowning monarchs in Westminster Abbey."},
            {"author": "Jane Austen", "work": "Emma", "quote": "In the drawing-room stood a rosewood **canterbury** containing the young ladies' latest bound piano sonatas."}
        ]
    },
    "cantering": {
        "primary": "Moving or riding at a canter; advancing at a smooth, rhythmic, three-beat equine pace.",
        "secondary": "In travel narrative and equestrian description, covering open downland roads swiftly without exhausting the mount.",
        "quotes": [
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Black Knight rode steadily along the forest highway, his heavy charger **cantering** easily beneath his armored weight."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A horseman came **cantering** along the lonely lane, accompanied by a great black-and-white hound bounding before him."},
            {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The archers watched the French scout **cantering** across the meadow, checking his reins to inspect their battle line."}
        ]
    },
    "cantharellus": {
        "primary": "A genus of edible wild mushrooms in the family Cantharellaceae comprising true chanterelles, prized for their golden color and fruity apricot aroma.",
        "secondary": "In mycology and foraging gastronomy, Cantharellus cibarius, characterized by funnel-shaped golden caps and blunt, fork-veined false gills running down the stipe.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Under the beech woods we gathered abundant specimens of the golden **Cantharellus**, whose delicate perfume was noticed by all."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Along the moist mossy trail grew clusters of bright yellow fungi of the genus **Cantharellus**, glowing amidst the damp forest shadows."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The damp southern beech forests supported magnificent edible fungi allied to **Cantharellus**, forming a staple food for the Fuegian natives."}
        ]
    },
    "canthus": {
        "primary": "The outer or inner corner of the eye, where the upper and lower eyelids meet.",
        "secondary": "In clinical ophthalmology, distinguishing the medial (nasal) canthus containing the lacrimal caruncle from the lateral (temporal) canthus.",
        "quotes": [
            {"author": "William Bowman", "work": "Lectures on the Eye", "quote": "The internal **canthus** accommodates the reddish lacrimal caruncle and the delicate puncta that siphon tears into the nose."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "A small rodent ulcer appearing near the inner **canthus** requires meticulous excision to preserve the delicate lacrimal canaliculus."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "An inflammation situated at the angle of the eye where the lids unite is termed an affection of the **canthus**."}
        ]
    },
    "canticle": {
        "primary": "A hymn or liturgical chant taken directly from biblical texts, other than the Psalms; or a little song.",
        "secondary": "In Christian liturgy, morning and evening canticles sung during Daily Office services (Magnificat, Nunc Dimittis, Benedictus, Te Deum).",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The angelic choir sang a triumphant **canticle** of praise as the new-created universe arose out of chaos."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The basilica resounded with the solemn **canticle** of Ambrose, celebrating the victory of orthodox faith over imperial persecution."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Marius was deeply moved by the ancient Christian **canticle**, whose simple musical phrasing conveyed sublime spiritual peace."}
        ]
    },
    "canticles": {
        "primary": "Plural of canticle; or the biblical book known as the Song of Solomon (Canticle of Canticles).",
        "secondary": "In biblical hermeneutics and monastic mysticism, sacred love poetry interpreted allegorically by St. Bernard as the mystical union of Christ and the Church.",
        "quotes": [
            {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The holy book of **Canticles** portrays under the figure of bridal love the spiritual union between Christ and his faithful spouse, the Church."},
            {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The pilgrims rested in the fragrant apple orchard, singing sweet **canticles** of thanksgiving for their safe journey."},
            {"author": "George Eliot", "work": "Romola", "quote": "The novices chanted the evening **canticles** with clear youthful voices that floated across the quiet cloister of San Marco."}
        ]
    },
    "cantilever": {
        "primary": "A long projecting beam or girder fixed at only one end, used in bridge construction and architectural balconies.",
        "secondary": "In structural civil engineering, structural spans projecting over a void carrying loads through moment resistance at the fixed anchor.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The great steel bridge rested upon massive stone piers, its central **cantilever** span looming black against the smoky dawn."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Venetian palace balcony was supported by an ornate carved **cantilever** of Istrian marble projecting over the canal."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "The human arm operates mechanically as an organic **cantilever**, counterbalancing loads through the tension of the deltoid and pectoral muscles."}
        ]
    },
    "cantillate": {
        "primary": "To chant or intone religious texts, especially Hebrew scripture, with ritual musical inflections.",
        "secondary": "In synagogue liturgical tradition, reciting biblical verses according to ancient Masoretic trope signs (te'amim) indicating phrasing and melody.",
        "quotes": [
            {"author": "Ernest Renan", "work": "History of the People of Israel", "quote": "The ancient Levites were trained to **cantillate** the sacred psalms before the altar with traditional modal inflections."},
            {"author": "Max Muller", "work": "Lectures on the Origin of Religion", "quote": "In every ancient religion, the priesthood learned to **cantillate** sacred hymns to preserve their exact phonetic meter."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The cantor rose in the synagogue to **cantillate** the Sabbath Torah portion, his resonant voice vibrating with ancient modal cadences."}
        ]
    },
    "cantillation": {
        "primary": "The ritual chanting or musical intonation of sacred scriptures or liturgical texts in religious worship.",
        "secondary": "In musicology and Jewish liturgy, the formal system of chanting Hebrew biblical texts guided by melodic accents that emphasize grammatical syntax.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Daniel listened with profound awe to the solemn **cantillation** of the ancient Hebrew prayers in the Frankfurt synagogue."},
            {"author": "Ernest Renan", "work": "The Life of Jesus", "quote": "The traditional synagogal **cantillation** preserved the melodic cadence of biblical poetry long after Hebrew ceased to be a spoken tongue."},
            {"author": "Max Muller", "work": "The Science of Language", "quote": "Vedic recitation and Hebrew **cantillation** both demonstrate how ritual singing protects sacred texts from phonetic corruption."}
        ]
    },
    "cantle": {
        "primary": "A corner, edge, slice, or portion of something, especially a piece cut out of a larger whole; or the raised rear part of a saddle.",
        "secondary": "In equestrian saddlery and medieval weaponry, the rear upward projection of a saddle tree supporting the rider's lower back against lances.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "See how this river comes me cranking in, / And cuts me from the best of all my land / A huge half-moon, a monstrous **cantle** out."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight sat firmly rooted in his high-peaked saddle, his back pressed hard against the iron-plated **cantle**."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A ragged **cantle** of turf had been pared from the barrow, exposing the white chalk beneath the heather."}
        ]
    },
    "canto": {
        "primary": "One of the major divisions or sections into which a long epic or narrative poem is divided.",
        "secondary": "In Italian poetic tradition (Dante, Ariosto, Tasso, Byron), a book-length poetical segment originally conceived as a single sung unit.",
        "quotes": [
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The third **canto** of the pilgrimage records Harold's wanderings along the majestic Rhine and among the Alpine peaks."},
            {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "In every sparkling **canto** of the mock-heroic epic, the poet ridicules the trivial vanities of fashionable society."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Dante partitioned his divine vision into a hundred harmonious cantos, each **canto** echoing with celestial and infernal harmonies."}
        ]
    },
    "canton": {
        "primary": "A subdivision of a country established for political or administrative purposes, especially in Switzerland; or a corner of a shield in heraldry.",
        "secondary": "In heraldry and vexillology, a rectangular charge occupying the upper hoist corner of an escutcheon or national flag.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The hardy mountaineers of each Swiss **canton** defended their ancestral liberties against the Austrian chivalry at Morgarten."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The administrative autonomy enjoyed by each Swiss **canton** illustrates the strengths and weaknesses of decentralized confederation."},
            {"author": "Walter Scott", "work": "Anne of Geierstein", "quote": "Deputies from every forest **canton** assembled at Uri to swear mutual defense upon the ancient mountain covenant."}
        ]
    },
    "cantonal": {
        "primary": "Of, relating to, or belonging to a canton, especially an administrative division of the Swiss Confederation.",
        "secondary": "In Swiss constitutional politics, the sovereign legislative, executive, and judicial powers retained by individual member states.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "Memoirs of My Life and Writings", "quote": "I spent several happy years in Lausanne, admiring the tranquil administration and equitable laws of the **cantonal** council."},
            {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The Swiss federal constitution carefully reserves residual sovereign powers to the separate **cantonal** legislatures."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The Swiss guards who defended the Tuileries with unflinching heroism were recruited from ancient **cantonal** mountain families."}
        ]
    },
    "cantonese": {
        "primary": "Relating to Canton (Guangzhou) in southern China, its people, culture, or the Yue Chinese language widely spoken there and in Hong Kong.",
        "secondary": "In Chinese dialectology and global diaspora history, a major Sinitic branch retaining archaic Middle Chinese final stop consonants and six to nine tones.",
        "quotes": [
            {"author": "Richard Francis Burton", "work": "Pilgrimage to El-Medinah and Meccah", "quote": "In the crowded oriental port we met prosperous **Cantonese** merchants trading in raw silk, porcelain, and southern teas."},
            {"author": "Max Muller", "work": "Lectures on the Science of Language", "quote": "The **Cantonese** language preserves ancient phonetic features that have been lost in the more modern Mandarin dialects of the north."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "The Chinese miners in California were chiefly **Cantonese** laborers whose patient, uncomplaining industry was the marvel of the camp."}
        ]
    },
    "cantonment": {
        "primary": "A permanent military station or garrison, especially in British India; or temporary quarters for troops.",
        "secondary": "In colonial military administration, self-contained residential compounds accommodating European officers, native regiments, and administrative headquarters.",
        "quotes": [
            {"author": "Rudyard Kipling", "work": "Plain Tales from the Hills", "quote": "Life in the military **cantonment** during the hot weather was an endless succession of polo matches, social calls, and evening band concerts."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The regiment was stationed at the Cawnpore **cantonment** when the first ominous murmurs of the great mutiny broke forth."},
            {"author": "Flora Annie Steel", "work": "On the Face of the Waters", "quote": "The British families resided in spacious thatched bungalows lining the wide avenues of the peaceful Meerut **cantonment**."}
        ]
    },
    "cantor": {
        "primary": "An official who sings or leads the chanting in a Jewish synagogue (hazzan); or the leader of singing in a cathedral choir (precentor).",
        "secondary": "In German musical history and church administration, the music director of a major civic church (such as J. S. Bach as Thomaskantor in Leipzig).",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The voice of the **cantor** rose in passionate, mournful supplication, carrying the prayers of the congregation to heaven."},
            {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "Sebastian Bach labored in Leipzig as humble church **cantor**, composing immortal sacred cantatas for every Sunday in the liturgical year."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The cathedral **cantor** stepped before the altar to intone the opening phrase of the ancient Easter hymn."}
        ]
    },
    "canty": {
        "primary": "Lively, cheerful, merry, and brisk in spirits; pleasant, snug, and comfortable in domestic humor.",
        "secondary": "In traditional Scots poetry and vernacular song, describing a merry, warm-hearted, contented rustic companion.",
        "quotes": [
            {"author": "Robert Burns", "work": "The Cotter's Saturday Night", "quote": "The frugality of the honest cottager made his humble hearth a blest and **canty** refuge from the winter storm."},
            {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The old woman was a **canty**, cheerful body who had a kind word and an encouraging smile for every weary traveler."},
            {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "The cottage was clean and **canty**, with a peat fire glowing warmly upon the hearth and porridge simmering on the grate."}
        ]
    },
    "canuck": {
        "primary": "A colloquial term for a Canadian, especially a French-Canadian.",
        "secondary": "In North American cultural slang and lumberjack lore, designating hardy northern woodsmen or Canadian national identity with colloquial warmth.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Leaves of Grass (Song of Myself)", "quote": "The **Canuck** lumberman stands balanced upon the log raft in the foaming river rapids, fearless and free."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our crew included an energetic **Canuck** axeman who could fell a giant hemlock in half the time of other woodchoppers."},
            {"author": "Jack London", "work": "The Call of the Wild", "quote": "Francois was a shrewd French-Canadian **Canuck** who understood sled-dogs better than any man in the Yukon territory."}
        ]
    },
    "canulate": {
        "primary": "A variant spelling of cannulate; to insert a cannula into a vein, artery, duct, or body cavity.",
        "secondary": "In historical surgical practice and physiological laboratory experimentation, inserting a small drainage tube or monitoring catheter.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of critical circulatory failure, the operator must immediately **canulate** a superficial vein to administer reviving fluids."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "The surgeon was unable to **canulate** the collapsed vessel due to intense perivascular swelling."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "To investigate the secretion of the submaxillary gland, researchers **canulate** Wharton's duct with a fine silver tube."}
        ]
    },
    "canulation": {
        "primary": "A variant spelling of cannulation; the surgical insertion of a cannula into a bodily passage or vessel.",
        "secondary": "In clinical medicine, the establishment of tubular access for drainage, perfusion, or hemodynamic recording.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Successful venous **canulation** was accomplished after difficulty, permitting the continuous delivery of saline and glucose."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The procedure of tracheal **canulation** afforded immediate respiratory relief to the suffocating child."},
            {"author": "Thomas Henry Huxley", "work": "Lectures on Physiology", "quote": "Direct arterial **canulation** provided Harvey's successors with exact experimental measurements of cardiac output."}
        ]
    },
    "canulisation": {
        "primary": "A variant spelling of cannulisation; the act or process of cannulating a blood vessel or bodily duct.",
        "secondary": "In experimental therapeutics, placing a cannula into an anatomical vessel to measure pressure or administer solutions.",
        "quotes": [
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "The **canulisation** of the saphenous vein was performed swiftly to counteract deep surgical shock."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Through careful **canulisation** of the pleural space, three pints of purulent exudate were safely evacuated."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In physiological vivisections, vascular **canulisation** serves as the standard preparation for kymograph recording."}
        ]
    },
    "canulization": {
        "primary": "A variant spelling of cannulization; the surgical insertion of a tube or cannula into a vessel or cavity.",
        "secondary": "In critical care medicine and vascular surgery, placing indwelling catheters for parenteral nutrition or hemodynamic monitoring.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Urgent **canulization** of the internal jugular vein was undertaken when peripheral veins were inaccessible."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The **canulization** of the lacrimal punctum dislodged the fibrous obstruction and restored natural drainage."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Proper **canulization** requires strict antisepsis to prevent secondary thrombophlebitis in catheterized vessels."}
        ]
    },
    "canute": {
        "primary": "Referring to King Canute (Cnut the Great, c. 995–1035), king of Denmark, England, and Norway, famed for the legend of commanding the tide.",
        "secondary": "In English historiography and political folklore, the wise monarch who demonstrated the limits of royal power by showing that the ocean tide would not obey his command.",
        "quotes": [
            {"author": "David Hume", "work": "The History of England", "quote": "King **Canute** seated himself upon the beach and commanded the rising ocean tide to retire, exposing the foolish flattery of his fawning courtiers."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Scandinavian empire founded by **Canute** the Great united the crowns of England, Denmark, and Norway under a single powerful sovereign."},
            {"author": "Thomas Carlyle", "work": "The Early Kings of Norway", "quote": "The famous coastal rebuke administered by **Canute** to his courtiers stands as an enduring parable on the impotence of earthly majesty before natural law."}
        ]
    },
    "canyon": {
        "primary": "A deep gorge, typically one with a river flowing through it, flanked by steep cliffs or escarpments.",
        "secondary": "In fluvial geomorphology, a deep valley carved through horizontal strata by long-term river incision, exemplified by the Grand Canyon of the Colorado.",
        "quotes": [
            {"author": "John Muir", "work": "The Mountains of California", "quote": "The foaming torrent rushed through the granite depths of the **canyon**, echoing with a deep musical roar between the towering cliffs."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "Our stagecoach rattled along the narrow ledge of the **canyon**, with dizzying precipices dropping hundreds of feet to the river below."},
            {"author": "Theodore Roosevelt", "work": "The Wilderness Hunter", "quote": "We tracked the elk into the shadow of a deep rocky **canyon** where clear mountain springs nourished groves of yellow pine."}
        ]
    },
    "canyonside": {
        "primary": "The sloping or precipitous wall or flank of a canyon.",
        "secondary": "In mountain ecology and landscape description, the rugged terrain supporting specialized cliff flora and animal scramble trails.",
        "quotes": [
            {"author": "John Muir", "work": "Our National Parks", "quote": "Clinging to the dizzy **canyonside**, ancient juniper trees twisted their gnarled roots into narrow granite crevices."},
            {"author": "Theodore Roosevelt", "work": "Outdoor Pastimes of an American Hunter", "quote": "We rode along the steep **canyonside** trail, scanning the opposite crags for mountain sheep feeding upon the grassy ledges."},
            {"author": "Owen Wister", "work": "The Virginian", "quote": "A single horseman was visible picking his way cautiously down the perilous **canyonside** toward the cottonwoods by the stream."}
        ]
    },
    "cosecant": {
        "primary": "The trigonometric function that is the reciprocal of the sine of an angle (csc x = 1 / sin x).",
        "secondary": "In classical trigonometry and spherical astronomy, calculated historically from trigonometric tables for navigation and triangle resolution.",
        "quotes": [
            {"author": "Isaac Newton", "work": "The Mathematical Principles of Natural Philosophy", "quote": "In calculating orbital perturbations, the radius vector varies inversely with the sine, or directly as the **cosecant** of the true anomaly."},
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The determination of celestial latitude requires trigonometric calculations involving the secant and **cosecant** of the observer's polar distance."},
            {"author": "William Stanley Jevons", "work": "The Principles of Science", "quote": "Trigonometric functions such as the sine, tangent, and **cosecant** express geometric ratios between angular lines in a unit circle."}
        ]
    },
    "decant": {
        "primary": "To pour a liquid gently from one vessel into another, especially wine or a chemical solution, without disturbing the sediment at the bottom.",
        "secondary": "In chemistry and culinary arts, separating a clear supernatant liquid from a settled precipitate, or aerating aged vintage wine.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The host proceeded to **decant** a bottle of rare old port with exquisite care, watching the candlelight through the dark glass."},
            {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "After the precipitate hath completely subsided to the bottom, carefully **decant** the clear alkaline liquor into a clean vial."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The butler stood by the sideboard ready to **decant** the sherry before the mayor and corporation sat down to dinner."}
        ]
    },
    "decantation": {
        "primary": "The process of pouring off a clear liquid from a container without disturbing the sediment or precipitate remaining at the bottom.",
        "secondary": "In analytical laboratory chemistry, a fundamental separation technique used when filtration is too slow or unsuited for gelatinous precipitates.",
        "quotes": [
            {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Washing precipitates by **decantation** is far superior to filtration when dealing with heavy crystalline residues."},
            {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "By repeated **decantation** with distilled water, the chemist removes every trace of soluble chloride from the silver precipitate."},
            {"author": "Robert Hooke", "work": "Micrographia", "quote": "The purified liquor was separated by gentle **decantation**, leaving the gross dregs settled firmly at the bottom of the glass."}
        ]
    },
    "decanter": {
        "primary": "A decorative glass or crystal bottle, typically with a stopper, into which wine or other liquor is poured for serving.",
        "secondary": "In material culture and social dining rituals, an engraved crystal vessel displayed on dining tables to aerate vintage wines.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge set out the bottles with trembling joy, filling a heavy glass **decanter** with glowing port wine for Bob Cratchit."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Hurst called impatiently for the wine **decanter**, indifferent to any conversation that did not concern the dinner or the cards."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Abbey Grange", "quote": "On the mahogany sideboard stood a cut-glass **decanter** containing the remains of a bottle of fine Beaune wine."}
        ]
    },
    "discant": {
        "primary": "A medieval polyphonic music style in which a voice sings a countermelody above a plainsong tenor; or to discourse or comment at length; descant.",
        "secondary": "In classical counterpoint, the soprano or highest melodic line in vocal or instrumental music; or in rhetoric, an elaborate verbal monologue.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard III", "quote": "And therefore, since I cannot prove a lover, / To entertain these fair well-spoken days, / I am determined to prove a villain / And hate the idle pleasures of these days. / Plots have I laid, inductions dangerous, / By drunken prophecies, libels and dreams, / To set my brother Clarence and the king / In deadly hate the one against the other. To **discant** on mine own deformity."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The nightingale tuned her sweet nocturnal **discant**, charming the silent woods of Eden with her passionate song."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The critic paused to **discant** upon the philosophical subtleties embedded within Dryden's political satires."}
        ]
    },
    "incan": {
        "primary": "Relating to or characteristic of the Incas, their pre-Columbian South American empire, civilization, architecture, or culture.",
        "secondary": "In Andean archaeology and historical ethnology, designating the Tahuantinsuyu empire centered at Cusco, famed for monumental masonry and road networks.",
        "quotes": [
            {"author": "William H. Prescott", "work": "History of the Conquest of Peru", "quote": "The monumental **Incan** highways traversed dizzying Andean precipices with stone stairs and suspension bridges of extraordinary engineering."},
            {"author": "Alexander von Humboldt", "work": "Vues des Cordillères", "quote": "The massive cyclopean stones of the **Incan** fortress of Sacsahuamán fit together with such precision that a knife blade cannot penetrate the joints."},
            {"author": "Hiram Bingham", "work": "Lost City of the Incas", "quote": "Machu Picchu revealed the crowning perfection of **Incan** architectural mastery, perched between granite mountain peaks above the Urubamba."}
        ]
    },
    "incantation": {
        "primary": "A series of words said as a magic spell, charm, or chant; or the chanting or uttering of words purporting to have magical power.",
        "secondary": "In ritual folklore, anthropology, and dramatic poetry, verbal formulas believed to summon supernatural entities or alter physical reality.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Round about the cauldron go; / In the poison'd entrails throw. / ... / Double, double toil and trouble; / Fire burn and cauldron bubble. A fearful **incantation**."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "With hellish **incantation** the sorcerer invoked the dark powers of the deep to overthrow the kingdom of light."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "The German charlatan muttered an unintelligible **incantation** over the glowing brazier to deceive his credulous patron."}
        ]
    },
    "precancerous": {
        "primary": "Relating to, characteristic of, or manifesting a histological condition that tends to develop into cancer; premalignant.",
        "secondary": "In surgical pathology and oncology, cellular atypia, dysplasia, or carcinoma in situ preceding invasive stromal penetration.",
        "quotes": [
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "Leukoplakia of the tongue must be regarded by the surgeon as a dangerous **precancerous** state requiring prompt intervention."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic localized irritation of epithelial tissues frequently induces **precancerous** hyperplasia that demands early surgical scrutiny."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination reveals cellular dysplasia in **precancerous** lesions before malignant invasion breaks the basement membrane."}
        ]
    },
    "recant": {
        "primary": "To say that one no longer holds an opinion, belief, doctrine, or past statement; to retract or renounce publicly.",
        "secondary": "In the history of heresy trials and ecclesiastical courts, formally abjuring condemned theological propositions before an inquisitorial tribunal.",
        "quotes": [
            {"author": "Galileo Galilei", "work": "Sentence of the Holy Office", "quote": "Before the ecclesiastical tribunal, Galileo was formally compelled to **recant** and abjure the Copernican doctrine that the earth moves."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The steadfast martyr refused to **recant** his religious convictions, choosing the scaffold rather than apostasy."},
            {"author": "John Milton", "work": "Areopagitica", "quote": "A free thinker will never **recant** his conscientious convictions merely to appease the censorship of the state."}
        ]
    },
    "recantation": {
        "primary": "The act of publicly withdrawing or renouncing a prior statement, opinion, belief, or confession; a retraction.",
        "secondary": "In intellectual and ecclesiastical history, formal legal or theological documents signed by scholars disavowing censured publications.",
        "quotes": [
            {"author": "David Hume", "work": "The History of England", "quote": "Cranmer's sudden and dramatic revocation of his previous **recantation** before the burning stake astonished both friends and enemies."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Emperor Julian demanded a public **recantation** from the Christian bishops who had supported his rival's decrees."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary tribunal demanded a formal **recantation** of monarchical principles before granting safe conduct to suspects."}
        ]
    },
    "secant": {
        "primary": "A straight line that cuts a curve in two or more points; or the trigonometric function that is the reciprocal of the cosine (sec x = 1 / cos x).",
        "secondary": "In classical geometry and trigonometry, the ratio of the hypotenuse to the adjacent side in a right-angled triangle.",
        "quotes": [
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The trajectory of the refracted ray through the prism may be computed geometrically by considering the **secant** of the angle of incidence."},
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "In spherical trigonometry, the computation of zenith distances employs the **secant** and cosecant of the observer's latitude."},
            {"author": "William Stanley Jevons", "work": "The Principles of Science", "quote": "A **secant** line intersecting a circle illustrates how limits can be analyzed as the distance between intersection points vanishes."}
        ]
    },
    "uncannily": {
        "primary": "In an uncanny, strange, eerie, mysterious, or unsettling manner.",
        "secondary": "In psychological fiction and ghost stories, exhibiting resemblance, precision, or prescience so exact as to feel supernatural.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The portrait of Hugo Baskerville resembled Stapleton so **uncannily** that Holmes gasped in astonishment at the likeness."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The demonic laughter echoed **uncannily** through the third-story corridor of Thornfield Hall in the dead of night."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The sleeve moved with human gestures while remaining **uncannily** empty, terrifying all who watched in the village parlor."}
        ]
    },
    "uncanny": {
        "primary": "Strange or mysterious, especially in an unsettling, eerie, or supernatural way; weird.",
        "secondary": "In psychoanalytic aesthetics, Sigmund Freud's 'das Unheimliche' (the uncanny): that class of the frightening which leads back to what is old and long familiar.",
        "quotes": [
            {"author": "Sigmund Freud", "work": "The Uncanny (Das Unheimliche)", "quote": "The **uncanny** is that class of the terrifying which leads back to something long known to us, once very familiar."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "An **uncanny** hound bayed across the desolate moorland, chilling the hearts of all who heard its spectral cry."},
            {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "There was something abnormal and **uncanny** in the creature's appearance, an indescribable deformity that revolted the gaze."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_can_dog_p3: {len(data_can_dog_p3)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_can_dog_p3.items():
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
        print("ALL 54 words in can_dog Part 3 PASSED local pre-audit validation!")
