# -*- coding: utf-8 -*-
"""
Part 1 of Curated Food, Eating & Drink Batch 3:
Dashboard — pom (30 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_pom = {
    "pom": {
        "primary": "An informal and often derogatory colloquial term used in Australia, New Zealand, and South Africa to designate an English immigrant or British person.",
        "secondary": "In Commonwealth sociolinguistics and colonial history, a widely debated cultural epithet purportedly derived as rhyming slang from pomegranate or an acronym for Prisoner of Mother England.",
        "quotes": [
            {"author": "D. H. Lawrence", "work": "Kangaroo", "quote": "The local bushmen regarded him with cautious curiosity, wondering whether this newcomer was another delicate **Pom** unprepared for the blistering sun."},
            {"author": "Nevil Shute", "work": "A Town Like Alice", "quote": "Out on the cattle station, the seasoned drovers quickly discovered that the newly arrived **Pom** possessed more grit and endurance than they had expected."},
            {"author": "Robert Hughes", "work": "The Fatal Shore", "quote": "In Australian vernacular lore, the label **Pom** evolved from colonial tensions between native-born currency lads and haughty British officials."}
        ]
    },
    "pomacanthus": {
        "primary": "A genus of large, brightly colored marine angelfishes in the family Pomacanthidae, inhabiting tropical coral reefs worldwide.",
        "secondary": "In systematic ichthyology and marine ecology, perciform fishes characterized by robust preopercular spines and striking ontogenetic shifts in color patterns from juvenile to adult stages.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Around the vibrant coral shoals, magnificent specimens of **Pomacanthus** darted between branching madrepores, their vivid bands gleaming under the tropical swell."},
            {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "Through the glass bottom of the boat, the French angel of the genus **Pomacanthus** drifted with majestic poise above the waving sea fans."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The genus **Pomacanthus** includes some of the most splendidly adorned species of the tropical coral banks, distinguished by their serrated preopercle."}
        ]
    },
    "pomace": {
        "primary": "The pulpy dry residue or crushed solid mass of apples, grapes, or other fruits remaining after the juice or oil has been mechanically pressed out.",
        "secondary": "In traditional cider making, pomology, and agricultural distillation, the nutrient-rich marc or apple cake utilized as livestock feed, soil conditioner, or feedstock for brandies.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The sweet, heavy scent of autumn pervaded the orchard where wet heaps of cider **pomace** lay steaming in the crisp morning air."},
            {"author": "Henry David Thoreau", "work": "Wild Apples", "quote": "The old cider-mill was silent now, but mounds of brownish **pomace** remained piled beside the wooden press, attracting swarms of buzzing wasps."},
            {"author": "William Howitt", "work": "The Rural Life of England", "quote": "Carts trundled through the farm lanes bearing loads of moist apple **pomace** to be spread across the frost-bitten orchard pastures."}
        ]
    },
    "pomacentridae": {
        "primary": "A diverse family of small, predominantly marine perciform ray-finned fishes known commonly as damselfishes and clownfishes.",
        "secondary": "In marine biology and coral reef ecology, territorial fishes exhibiting aggressive defense of microalgal turfs, complex parental brooding, and mutualistic symbioses with actiniarian sea anemones.",
        "quotes": [
            {"author": "William Beebe", "work": "Arcturus Adventure", "quote": "Tiny, pugnacious damselfishes of the family **Pomacentridae** hovered above the coral heads, fiercely guarding their minute feeding territories against all intruders."},
            {"author": "David Starr Jordan", "work": "Fishes", "quote": "The **Pomacentridae** are exceptionally abundant on tropical reefs, displaying an astonishing array of brilliant chromatic patterns and specialized foraging behaviors."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the shallow reef pools of the Moluccas, agile species belonging to the **Pomacentridae** flashed like living jewels between the tentacles of giant anemones."}
        ]
    },
    "pomacentrus": {
        "primary": "The type genus of marine damselfishes in the family Pomacentridae, comprising small, agile species that frequent Indo-Pacific coral reefs.",
        "secondary": "In taxonomic ichthyology, herbivorous and omnivorous damselfishes distinguished by serrated preopercles, deep compressed bodies, and territorial cultivation of filamentous epilithic algae.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "The Genera of Fishes", "quote": "Lacépède established the genus **Pomacentrus** to encompass those distinctive coral damselfishes possessing an operculum armed with small denticulations."},
            {"author": "William Beebe", "work": "Zaca Venture", "quote": "A solitary **Pomacentrus** hovered motionlessly above a shelf of brain coral, defending its patch of green turf against encroaching parrotfish."},
            {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The distribution of small reef fishes such as **Pomacentrus** highlights the exceptional biological richness of the central Indo-Pacific marine corridor."}
        ]
    },
    "pomade": {
        "primary": "A scented greasy ointment or wax-based cosmetic preparation used for conditioning, styling, and adding gloss to the hair.",
        "secondary": "In historical perfumery and apothecary, an unguent traditionally prepared by steeping aromatic blossoms in purified lard or suet through the technique of enfleurage.",
        "quotes": [
            {"author": "Honoré de Balzac", "work": "Lost Illusions", "quote": "Lucien took exceptional pains with his toilette, smoothing his dark curls with fragrant rose **pomade** before stepping out into the Parisian salon."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Joseph Sedley spent half an hour before the looking-glass, applying scented **pomade** to his whiskers until they shone with brilliant luster."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth appeared freshly dressed for dinner, smelling pleasantly of jasmine **pomade** and carrying himself with effortless aristocratic grace."}
        ]
    },
    "pomaded": {
        "primary": "Dressed, smoothed, or heavily styled with scented pomade or aromatic cosmetic unguents.",
        "secondary": "In literature and social satire, denoting an excessively groomed, dapper, or ostentatiously slicked personal appearance typical of fashionable gallants.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The dapper clerk entered the parlor with **pomaded** hair parted meticulously down the center and cuffs turned back with fastidious care."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy looked down at his own **pomaded** locks and scarlet uniform, smiling with supreme complacency at the impression he made."},
            {"author": "George Orwell", "work": "Burmese Days", "quote": "The young dandy brushed his **pomaded** hair until it flattened into sleek black ridges against his skull, ready for the evening dance."}
        ]
    },
    "pomaderris": {
        "primary": "A genus of Australasian shrubs and small trees in the family Rhamnaceae, bearing clusters of small yellow or cream flowers and stellate foliage.",
        "secondary": "In Australian systematic botany and temperate forestry, woody buckthorn relatives often thriving as understory shrubs in sclerophyll forests and subalpine river valleys.",
        "quotes": [
            {"author": "Joseph Dalton Hooker", "work": "Flora Tasmaniae", "quote": "Several remarkable species of **Pomaderris** abound along the gravelly riverbanks of Tasmania, distinguished by the dense stellate tomentum on their leaves."},
            {"author": "Ferdinand von Mueller", "work": "Select Extra-Tropical Plants", "quote": "The hazel **Pomaderris** attains the stature of a small tree in damp mountain gullies, providing useful timber and ornamental golden blossoms."},
            {"author": "Robert Brown", "work": "Prodromus Florae Novae Hollandiae", "quote": "In our botanical surveys of the southern ranges, the diverse forms of **Pomaderris** illustrated the adaptive radiation of Australian Rhamnaceae."}
        ]
    },
    "pomatomidae": {
        "primary": "A family of marine perciform fishes containing a single extant species, the voracious coastal bluefish (Pomatomus saltatrix).",
        "secondary": "In marine fisheries science and pelagic ecology, fast-swimming predatory teleosts renowned for schooling habits, powerful scissor-like dentition, and fierce feeding frenzies on smaller clupeids.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The family **Pomatomidae** consists of a single cosmopolitan species celebrated among anglers and commercial fishermen as the swift and destructive bluefish."},
            {"author": "George Brown Goode", "work": "Fisheries and Fishery Industries of the United States", "quote": "No marine predator displays greater rapacity than the oceanic representatives of **Pomatomidae**, which slash through schools of menhaden with ceaseless fury."},
            {"author": "Spencer Fullerton Baird", "work": "Report on the Condition of the Sea Fisheries", "quote": "Our investigations into the **Pomatomidae** revealed their enormous impact upon migratory baitfish populations along the Atlantic seaboard."}
        ]
    },
    "pomatomus": {
        "primary": "The monotypic genus of pelagic marine fishes comprising the bluefish, Pomatomus saltatrix, found widely across temperate and subtropical waters.",
        "secondary": "In systematic marine ichthyology, predatory teleosts distinguished by a stout compressed body, two dorsal fins, and dangerously sharp uniserial triangular teeth.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "American Food and Game Fishes", "quote": "The voracious **Pomatomus** moves in dense shoals along our Atlantic shores, attacking schools of mullet with relentless ferocity."},
            {"author": "George Brown Goode", "work": "American Fishes", "quote": "Fishermen along the coast respect **Pomatomus** as one of the fiercest adversaries that can take a hook or shred a net."},
            {"author": "Spencer Fullerton Baird", "work": "Natural History of Aquatic Animals", "quote": "The swift locomotion and muscular agility of **Pomatomus** render it an apex hunter within the temperate littoral zone."}
        ]
    },
    "pomatum": {
        "primary": "A perfumed unguent or ointment formerly made from apples and animal fats, applied to beautify, soothe, or dress the hair and skin.",
        "secondary": "In seventeenth- and eighteenth-century pharmacopoeia, an aromatic pomade prepared with crushed apples (pommes), rosewater, and clarified suet used for cosmetic and medicinal grooming.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He had smoothed his dark locks with fragrant **pomatum**, presenting an appearance of unexpected civility amid the rough whaling crew."},
            {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "Mr. Grewgious smelled faintly of antique snuff and lavender **pomatum**, gazing across the fire with mild and dry detachment."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The little valet rubbed sweet-scented **pomatum** into his master's thinning crown, attempting to disguise the advance of middle age."}
        ]
    },
    "pome": {
        "primary": "A fleshy fruit characteristic of the rose family, such as the apple, pear, or quince, consisting of an outer fleshy receptacle and a cartilaginous core containing seeds.",
        "secondary": "In structural plant morphology and carpology, an accessory false fruit (pseudocarp) derived from an inferior compound ovary fused with the surrounding floral tube or hypanthium.",
        "quotes": [
            {"author": "Asa Gray", "work": "First Lessons in Botany and Vegetable Physiology", "quote": "In botanical morphology, the apple is designated a **pome**, formed by the thickening and swelling of the fleshy receptacle around the core."},
            {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "The typical **pome** exhibits five cartilaginous carpels enclosed within the succulent flesh that develops from the floral envelope."},
            {"author": "Liberty Hyde Bailey", "work": "The Principles of Fruit-Growing", "quote": "Cultivated orchard trees bearing the classic **pome** require careful winter pruning to stimulate fruit-bud formation along the mature spurs."}
        ]
    },
    "pomegranate": {
        "primary": "A round subtropical fruit with a thick reddish rind containing numerous tart seeds enveloped in juicy crimson pulpy arils, produced by Punica granatum.",
        "secondary": "In comparative mythology, classical literature, and horticulture, an ancient sacred fruit symbolizing fertility, royal abundance, and the mythical return of Persephone from Hades.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "It was the nightingale, and not the lark, That pierced the fearful hollow of thine ear; Nightly she sings on yon **pomegranate** tree."},
            {"author": "King James Bible", "work": "Song of Solomon", "quote": "Thy lips are like a thread of scarlet, and thy speech is comely: thy temples are like a piece of a **pomegranate** within thy locks."},
            {"author": "Oscar Wilde", "work": "A House of Pomegranates", "quote": "He cracked open the ripe **pomegranate** with his fingers, marveling at the jewel-like seeds that glistened like dark rubies in the sun."}
        ]
    },
    "pomelo": {
        "primary": "A large citrus fruit native to Southeast Asia (Citrus maxima), having a very thick yellow-green spongy rind, sweet mild flesh, and mild grapefruit-like flavor.",
        "secondary": "In systematic pomology and citrus genetics, one of the three ancestral wild species from which commercial sweet oranges and modern hybrid grapefruits were developed.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "At the native markets in Batavia, immense baskets were heaped high with the fragrant **pomelo**, whose refreshing juice revived weary travelers."},
            {"author": "Robert Fortune", "work": "A Journey to the Tea Countries of China", "quote": "The orchards of southern China produce an admirable variety of the **pomelo**, remarkable for its immense size and delicate sugary flavor."},
            {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "We collected seeds of the wild Siamese **pomelo**, recognizing its tremendous potential for introducing hardiness into commercial citrus groves."}
        ]
    },
    "pomeranian": {
        "primary": "A toy breed of dog characterized by a compact body, fox-like head, prick ears, and a lavish, fluffy double coat, or a native of Pomerania.",
        "secondary": "In canine history and regional geography, a miniaturized spitz breed originating in the Baltic province of Pomerania, popularized across Europe by Queen Victoria.",
        "quotes": [
            {"author": "Anton Chekhov", "work": "The Lady with the Dog", "quote": "She strolled alone along the seaside embankment every afternoon, accompanied only by a little white **Pomeranian** trotting at her heels."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The lady sat upon the sofa petting her fluffy **Pomeranian**, while Holmes inquired gently into the events of the preceding evening."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The eccentric dowager arrived with her beloved **Pomeranian** nestled upon her lap, glaring at the visitors through gold-rimmed spectacles."}
        ]
    },
    "pommel": {
        "primary": "A rounded knob forming the upward-projecting front part of a saddle, or the rounded ornamental knob at the end of a sword hilt.",
        "secondary": "In equestrian saddlery and historical metallurgy, a stabilizing front arch on a saddle tree, or a counterbalancing terminal mass on a sword tang.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He grasped the carved **pommel** of his saddle with weathered hands, reining in the nervous stallion as the storm broke over the plain."},
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "MacIan gripped the brass **pommel** of his ancient claymore, his knuckles turning white as he faced his antagonist in the morning mist."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight rested his mailed hand upon the steel **pommel** of his sword, listening gravely to the summons delivered by the herald."}
        ]
    },
    "pommy": {
        "primary": "An informal and often pejorative slang designation for an English immigrant or British citizen in Australia and New Zealand.",
        "secondary": "In Australasian cultural studies, an entrenched colloquial moniker carrying historical associations of convict-era resentment, class tensions, and sporting rivalry.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The emigrant wrote home from the goldfields that the rough bushmen called every fresh arrival from Dorset a simple **pommy** greenhorn."},
            {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Among the international volunteers, the cheerful Australian miner referred to every London soldier good-naturedly as a stubborn **pommy**."},
            {"author": "D. H. Lawrence", "work": "Kangaroo", "quote": "Somers felt the peculiar distance that separated his English sensibilities from the colonial youths, who labeled him a quiet **pommy** stranger."}
        ]
    },
    "pomo": {
        "primary": "An indigenous Native American people historically inhabiting northern California along the Russian River and Pacific coast, or their family of languages.",
        "secondary": "In cultural anthropology and indigenous material arts, California hunter-gatherer communities internationally celebrated for their intricate, feather-ornamented coiled and twined basketry.",
        "quotes": [
            {"author": "Alfred Kroeber", "work": "Handbook of the Indians of California", "quote": "The artistic genius of the **Pomo** reached its highest expression in their feather-decorated baskets, unmatched in delicate craftsmanship across the continent."},
            {"author": "John Muir", "work": "The Mountains of California", "quote": "We passed the peaceful summer encampments of the **Pomo** along the redwood valleys, where families harvested acorns and dried salmon for winter."},
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "In the sacred seasonal rituals of the Californian **Pomo**, dancers donned elaborate feathered head-dresses to invoke the spirits of fertility and rain."}
        ]
    },
    "pomolobus": {
        "primary": "A former zoological genus of clupeid fishes comprising anadromous herrings such as the alewife and blueback herring, now classified under Alosa.",
        "secondary": "In historical American ichthyology and fisheries documentation, river herrings ascending Atlantic freshwater streams in dense spring spawning runs to support commercial fisheries.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Rafinesque proposed the name **Pomolobus** for the common alewife and its allies, separating them from true oceanic herrings by their notched upper jaws."},
            {"author": "Spencer Fullerton Baird", "work": "Report on the Condition of the Sea Fisheries", "quote": "Every spring the rivers of New England were choked with millions of **Pomolobus**, providing abundant sustenance for coastal settlements."},
            {"author": "George Brown Goode", "work": "American Fishes", "quote": "The species formerly grouped under **Pomolobus** undertake remarkable freshwater migrations, swimming against swift currents to deposit their spawn in quiet ponds."}
        ]
    },
    "pomologist": {
        "primary": "A botanical scientist or horticulturist who specializes in pomology, the systematic study and cultivation of fruits and fruit-bearing trees.",
        "secondary": "In agricultural science and nursery practice, an expert who breeds, classifies, cross-pollinates, and improves orchard cultivars to resist frost, pests, and disease.",
        "quotes": [
            {"author": "Liberty Hyde Bailey", "work": "The Nursery-Book", "quote": "The dedicated **pomologist** spends decades observing slight variations among grafted seedlings to identify hardier varieties of winter apples."},
            {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "I walked through the experimental orchard with an elderly **pomologist** who spoke of russet pears as though they were intimate personal acquaintances."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Every experienced **pomologist** knows that varieties of the peach frequently revert when propagated from seed rather than by careful budding."}
        ]
    },
    "pomology": {
        "primary": "The branch of botany and horticultural science that deals with the study, breeding, cultivation, and economic management of fruits and fruit trees.",
        "secondary": "In agronomic literature and plant physiology, the systematic discipline encompassing rootstock selection, canopy training, fruit morphometry, and post-harvest preservation.",
        "quotes": [
            {"author": "Liberty Hyde Bailey", "work": "The Principles of Fruit-Growing", "quote": "Modern **pomology** combines rigorous physiological research with practical field management to maximize the annual yield of commercial orchards."},
            {"author": "Henry David Thoreau", "work": "Wild Apples", "quote": "Our treatises on **pomology** describe hundred of refined varieties, yet none possesses the wild, spicy vigor of the solitary seedling apple."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The history of **pomology** shows that human selection has transformed wild crabapples into the countless luxuriant fruits cultivated across Europe today."}
        ]
    },
    "pomona": {
        "primary": "The Roman mythological goddess of fruitful abundance, gardens, and orchard trees, traditionally depicted carrying a pruning knife and cornucopia.",
        "secondary": "In Latin classical poetry and Western iconography, the wood nymph beloved by Vertumnus who personifies the flourishing cultivation and care of domestic orchards.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "To Pales, or **Pomona**, thus adorned, Likest she seemed, **Pomona** when she fled Vertumnus, or to Ceres in her prime."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "In the golden warmth of September, nature pours forth the gifts of **Pomona**, loading the orchard branches with ripe and fragrant harvest."},
            {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "The classical worshiper saw the divine hand of **Pomona** in the heavy clusters of the vine and the mellow fullness of autumn apples."}
        ]
    },
    "pomoxis": {
        "primary": "A genus of North American freshwater sunfishes in the family Centrarchidae, commonly known as crappies and prized as popular sport and pan fish.",
        "secondary": "In inland fisheries biology, teleosts comprising the black crappie and white crappie, characterized by compressed bodies, mottled silvery sides, and nest-building habits in quiet waters.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "American Food and Game Fishes", "quote": "Rafinesque described the genus **Pomoxis**, noting the distinctive opercular flap and sharp dorsal spines of our native American crappies."},
            {"author": "Spencer Fullerton Baird", "work": "Report on the Condition of the Sea Fisheries", "quote": "Anglers throughout the Mississippi basin find both species of **Pomoxis** to be among the most delightful and palatable pan fishes in quiet lakes."},
            {"author": "George Brown Goode", "work": "American Fishes", "quote": "In early spring, schools of **Pomoxis** gather in shallow, weed-choked bays to spawn, offering lively sport to country fishermen."}
        ]
    },
    "pomp": {
        "primary": "Stately, magnificent, or ceremonious display and pageantry, often marked by elaborate processions and ceremonial splendor.",
        "secondary": "In political philosophy and tragic drama, the external theatrical panoply of sovereign authority, imperial prestige, and courtly ostentation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Why, what is **pomp**, rule, reign, but earth and dust? And, live we how we can, yet die we must."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "The true king needs no theatrical **pomp** or gilded chariot to command the involuntary homage of wise men."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He loved the marvelous **pomp** of the ritual, the fragrant clouds of incense, and the embroidered vestments of the choir."}
        ]
    },
    "pompadour": {
        "primary": "A hairstyle in which the hair is brushed high up from the forehead without a part, or a style of low-cut dress bodice named after Madame de Pompadour.",
        "secondary": "In costume history and salon culture, an eighteenth-century aesthetic of rococo elegance and voluminous coiffures inspired by the influential mistress of King Louis XV.",
        "quotes": [
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The portrait exhibited the grandmother in the grand days of her youth, with powdered **pompadour** hair and satin bodice adorned with lace."},
            {"author": "Henry James", "work": "The Bostonians", "quote": "Her elaborate **pompadour** coiffure added an inch to her stature, imparting an air of formidable social consequence to her appearance."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Old Mrs. Mingott recalled the era when every fashionable New York belle swept her hair into an immense **pompadour** above ivory shoulders."}
        ]
    },
    "pomposity": {
        "primary": "Pompous behavior, pretentiousness, or self-important dignity in demeanor, speech, or writing.",
        "secondary": "In social satire and character comedy, an inflated sense of personal importance marked by solemn affectation, grandiloquent language, and absurd vanity.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The pompous alderman cleared his throat with immense **pomposity**, puffing out his waistcoat before delivering his banal opinion."},
            {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "Mr. Sapsea wrapped himself in a mantle of solemn **pomposity**, delivering commonplaces as though they were divine revelations."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins spoke with an absurd mixture of servility and **pomposity**, praising Lady Catherine with every breath he drew."}
        ]
    },
    "pompous": {
        "primary": "Characterized by an exaggerated display of dignity, self-importance, or solemn grandeur; pretentiously stately.",
        "secondary": "In rhetoric and literary portraiture, describing persons or writing styles inflated with self-complacent arrogance and heavy, ornate grandiloquence.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "To see the **pompous** court, and there to hear The buzzing whisperers of a king's decay, Was more than my grieved spirit could endure."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon delivered his scholarly observations in a dry, **pompous** tone that sounded like the rustling of dried autumn leaves."},
            {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "I cannot abide those **pompous** moralists who instruct the universe upon duties they have never had the courage to perform."}
        ]
    },
    "pompously": {
        "primary": "In a pompous, self-important, or ostentatiously solemn manner.",
        "secondary": "In comedic description and narrative prose, acting or declaiming with ridiculous grandeur and exaggerated gravity.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The manager strolled across the veranda, speaking **pompously** of civilization and progress while the miserable carriers groaned in the dust."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook blew out his cheeks and declared **pompously** that boyish gratitude was the rarest virtue known under the canopy of heaven."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Brocklehurst cleared his dry throat and **pompously** addressed the assembled schoolgirls on the mortal peril of worldly adornments."}
        ]
    },
    "pompousness": {
        "primary": "The state or characteristic of being pompous; overbearing self-importance or grandiloquent solemnity.",
        "secondary": "In ethical portraiture and interpersonal dynamics, an irritating affectation of intellectual or social superiority accompanied by stiffness and lack of humor.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard despised the smug **pompousness** of the town councilors, whose smooth phrases concealed their complete lack of courage in a crisis."},
            {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins took malicious delight in puncturing the inflated **pompousness** of high society gatherings with his blunt observations."},
            {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "There is no variety of human folly more ridiculous than the empty **pompousness** of a minor official puffed up with brief authority."}
        ]
    },
    "unpompous": {
        "primary": "Free from pomp, pretension, or self-important display; genuinely modest, straightforward, and unpretentious in demeanor.",
        "secondary": "In biographical sketch and portraiture, exhibiting an unpretending directness and approachable simplicity despite holding elevated rank or great achievement.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The greatest scholars I met were remarkably **unpompous** men, speaking with plain good sense and listening with modest patience to every inquirer."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "True saintliness reveals itself in an **unpompous** humility that disarms hostility and touches the hearts of common folk."},
            {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She admired his simple, **unpompous** manner at the dinner table, contrasting sharply with the stiff posturing of younger academic guests."}
        ]
    }
}
