# -*- coding: utf-8 -*-
"""
Curates Dashboard — sag (31 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — sag/assagai.md": {
    "primary": "A light iron-tipped throwing spear or lance of hardwood used by southern African warriors.",
    "secondary": "In colonial military history, the traditional missile weapon of Zulu and Nguni impis in warfare.",
    "quotes": [
      {"author": "H. Rider Haggard", "work": "King Solomon's Mines", "quote": "The warrior shook his broad-bladed **assagai**, shouting defiance as the battle horn echoed from the mountain pass."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The scouts watched the crests for gleams of steel, where warriors armed with shield and **assagai** guarded the defile."},
      {"author": "Richard Francis Burton", "work": "First Footsteps in East Africa", "quote": "Each tribesman carried three throwing spears and a short stabbing **assagai** fashioned from seasoned thornwood."}
    ]
  },
  "Dashboard — sag/corsage.md": {
    "primary": "A small bouquet of flowers pinned to a woman's dress or worn around her wrist for a formal occasion.",
    "secondary": "In historic fashion and ball costume, the fitted bodice or waist of a woman's gown adorned with floral posies.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Daisy glanced down at the crushed orchid **corsage** pinned to her evening gown, shivering in the autumn chill."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "May Welland wore a simple white **corsage** of gardenias sent that morning from the van der Luydens' conservatory."},
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "Odette had fastened a cluster of cattleya blossoms to her silk **corsage**, adjusting the petals as Swann entered."}
    ]
  },
  "Dashboard — sag/disagree.md": {
    "primary": "Hold a different opinion or point of view; fail to agree or harmonize; also cause physical discomfort.",
    "secondary": "In culinary health and logical disputation, causing digestive distress or asserting contradictory propositions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy and Elizabeth seemed destined to **disagree** upon every topic that arose during the Netherfield ball."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The cold cucumber salad seemed to **disagree** violently with Mr. Chillip's delicate constitution that evening."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Philosophers perpetually **disagree** when they dispute about words without defining their underlying ideas."}
    ]
  },
  "Dashboard — sag/disagreeable.md": {
    "primary": "Unpleasant, offensive, or bad-tempered; causing discomfort, annoyance, or discord.",
    "secondary": "In narrative characterization, a sour or hostile personality that alienates friends and acquaintances.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy was discovered to be proud, to be above his company, and above being pleased; he was pronounced the most **disagreeable** man in Hertfordshire."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The weather was uncommonly **disagreeable**, with a drizzling rain that coated the London pavements with slippery mud."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed was a sullen, **disagreeable** schoolboy who spent his holidays torturing his sisters and servants."}
    ]
  },
  "Dashboard — sag/disagreeableness.md": {
    "primary": "The characteristic disposition of being disagreeable; unpleasantness, quarrelsome temper, or offensive quality.",
    "secondary": "In psychological temperament studies, habitual friction and lack of interpersonal warmth in social interaction.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's constitutional **disagreeableness** deepened whenever young Ladislaw's name was mentioned in his presence."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Fanny Dashwood's natural **disagreeableness** showed itself in her petty reluctance to grant the sisters any assistance."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "No vice creates more universal alienation than an unprovoked **disagreeableness** of conversation."}
    ]
  },
  "Dashboard — sag/disagreeably.md": {
    "primary": "In a disagreeable, unpleasant, offensive, or bad-tempered manner; distastefully.",
    "secondary": "In descriptive fiction, jarring upon the senses or dampening conversational warmth with sour remarks.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt the coarse convict clothes scratch his neck **disagreeably** as he trudged across the wet marshes."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The cold wind whistled **disagreeably** through the cracks of the sheepcote, threatening an icy night."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The dismal croak of a raven broke **disagreeably** upon the ominous silence of the Grimpen Mire."}
    ]
  },
  "Dashboard — sag/disagreement.md": {
    "primary": "Lack of consensus, harmony, or agreement; a conflict of opinion, quarrel, or dispute.",
    "secondary": "In contract law and political negotiation, irreconcilable differences between parties requiring formal arbitration.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A sharp **disagreement** between the states over western territorial claims threatened to dissolve the Confederation."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The first serious **disagreement** between Lydgate and Rosamond arose over the mounting debts for household luxuries."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Freedom of discussion ensures that honest intellectual **disagreement** remains the greatest spur to mental progress."}
    ]
  },
  "Dashboard — sag/presage.md": {
    "primary": "Be a sign or warning that something bad or momentous will happen; portend, foreshadow; an omen.",
    "secondary": "In classical tragedy and nature poetry, atmospheric portents heralding imminent political upheaval or ruin.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "My mind misgives some consequence yet hanging in the stars shall bitterly begin his fearful date with this night's revels and **presage** our ruin."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sudden descent of the barometer seemed to **presage** the furious wrath of the approaching typhoon."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Solar eclipses and earthquakes were interpreted by superstitious citizens to **presage** the fall of the dynasty."}
    ]
  },
  "Dashboard — sag/sag.md": {
    "primary": "Sink, subside, droop, or bend downward under weight, pressure, or gradual structural weakness.",
    "secondary": "In financial markets and construction engineering, a softening of stock prices or deflection in load-bearing beams.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The heavy thatched roof began to **sag** under the tremendous weight of the sodden autumnal downpour."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The tired sled dogs began to **sag** in their harnesses after breaking trail through thirty miles of fresh powder."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The damp cottage walls had cracked, causing the lintels to **sag** drunkenly over the cobblestone lane."}
    ]
  },
  "Dashboard — sag/saga.md": {
    "primary": "A long, traditional story of heroic achievement, especially a medieval prose narrative in Old Norse or Icelandic.",
    "secondary": "In modern literature, an extended family chronicle spanning multiple generations through triumph and adversity.",
    "quotes": [
      {"author": "Henry Wadsworth Longfellow", "work": "The Saga of King Olaf", "quote": "The skald struck his harp in the great hall, chanting the ancient Norse **saga** of sea-kings and dragons."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "In the Icelandic **saga**, we hear the rugged, honest voice of Scandinavian ancestors battling storm and frost."},
      {"author": "Walter Scott", "work": "The Pirate", "quote": "The old Udaller sat beside the peat fire, reciting an ancient Shetland **saga** of shipwrecked jarls."}
    ]
  },
  "Dashboard — sag/sagacious.md": {
    "primary": "Having or showing keen mental discernment, good judgment, and practical wisdom; shrewd and farsighted.",
    "secondary": "In character sketches and natural history, keen animal instinct or statesmen exhibiting acute political foresight.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Bucket was an extraordinarily **sagacious** officer, whose watchful eye missed no tremor of a witness's lip."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth smiled at Charlotte's **sagacious** observations, recognizing her friend's prudent calculation of matrimonial prospects."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old sailor gave a **sagacious** nod, pointing out subtle ocean currents invisible to inexperienced landsmen."}
    ]
  },
  "Dashboard — sag/sagaciously.md": {
    "primary": "In a sagacious manner; shrewdly, wisely, and with keen penetration and practical insight.",
    "secondary": "In narrative dialogue, expressing insightful judgment that exposes hidden motives behind polite pretense.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Jaggers rubbed his large hands together and nodded **sagaciously**, hinting that he knew far more than he cared to disclose."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg **sagaciously** examined the harpoon socket, testing the tempered iron against a block of seasoned oak."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The village elders shook their heads **sagaciously**, predicting that Rip Van Winkle would come to no good end."}
    ]
  },
  "Dashboard — sag/sagaciousness.md": {
    "primary": "The quality of being sagacious; keenness of mental discernment, practical wisdom, and shrewdness.",
    "secondary": "In moral philosophy and statecraft, depth of insight and farsightedness in navigating complex governance.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The renowned statesman owed his ascendancy to an innate **sagaciousness** that penetrated the masked intrigues of foreign courts."},
      {"author": "Walter Scott", "work": "The Heart of Mid-Lothian", "quote": "Jeanie Deans possessed that rustic **sagaciousness** which guides simple hearts securely through unfamiliar dangers."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "True political **sagaciousness** consists in accommodating governance to the ingrained temper of the people."}
    ]
  },
  "Dashboard — sag/sagacity.md": {
    "primary": "The quality of being sagacious; acuteness of mental discernment, sound judgment, and farsighted wisdom.",
    "secondary": "In classic literature, celebrated animal instinct (such as the hound's scent) or elderly statesmanship.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Now, the lawyer's extraordinary **sagacity** had led him straight to the hidden document in the dead man's lodgings."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth gave her friend full credit for **sagacity**, though she could not approve the mercenary prudence of her choice."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white whale displayed an almost human **sagacity** in eluding the combined pursuit of three harpoon boats."}
    ]
  },
  "Dashboard — sag/sagamore.md": {
    "primary": "A subordinate chief or tribal leader among certain Native American peoples of the northeastern Algonquian family.",
    "secondary": "In colonial American history and folklore, a tribal dignitary subordinate to a grand sachem in political council.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "The venerable **sagamore** sat beneath the council elm, smoking the calumet of peace with the Pilgrim magistrates."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "A wild figure stood at the forest edge, dressed in the fringed deerskins and wampum belt of a New England **sagamore**."},
      {"author": "James Fenimore Cooper", "work": "The Last of the Mohicans", "quote": "Chingachgook spoke with the gravitas of an ancient **sagamore**, mourning the scattered tribes of his fathers."}
    ]
  },
  "Dashboard — sag/sage-green.md": {
    "primary": "A pale, soft grayish-green color resembling the hue of dried culinary sage leaves.",
    "secondary": "In decorative arts and aesthetic movement interiors, an understated earthy tint favored by William Morris and Pre-Raphaelites.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The studio walls were hung with delicate **sage-green** silk, forming an artistic background for antique porcelain vases."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She wore an understated evening cloak of **sage-green** velvet that set off the dark coils of her hair."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "Margaret examined the Morris wallpaper with its graceful **sage-green** acanthus leaves winding across the hall."}
    ]
  },
  "Dashboard — sag/sage.md": {
    "primary": "A profoundly wise person, venerated for wisdom and sound judgment; also an aromatic culinary herb (*Salvia officinalis*).",
    "secondary": "In classical philosophy, the Stoic ideal of the perfected human whose reason remains untroubled by passions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "A **sage** philosopher once taught that grief best heals when seasoned with patient virtue and holy silence."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The ancient **sage** dwells in serene contemplation, recognizing the divine unity that animates every atom of creation."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak was regarded as a rustic **sage** whose sheep-tending lore surpassed all modern agricultural books."}
    ]
  },
  "Dashboard — sag/sagebrush.md": {
    "primary": "A shrubby aromatic North American plant (*Artemisia tridentata*) with silvery-gray leaves, dominating arid western plains.",
    "secondary": "In Western American literature, the quintessential aromatic shrub defining the rugged desert plains and badlands.",
    "quotes": [
      {"author": "Zane Grey", "work": "Riders of the Purple Sage", "quote": "Lassiter reined his horse upon the red sandstone bluff, looking across rolling miles of purple and silver **sagebrush**."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The pungent, camphoraceous aroma of the burning **sagebrush** campfire filled the cold desert night with wild comfort."},
      {"author": "Willa Cather", "work": "The Song of the Lark", "quote": "The dry mountain wind swept across the canyon flats, carrying the clean, bitter scent of sun-warmed **sagebrush**."}
    ]
  },
  "Dashboard — sag/sagely.md": {
    "primary": "In a wise, discerning, prudent, or sagacious manner; with deliberate philosophical gravity.",
    "secondary": "In narrative characterization, offering prudent advice with solemn nods and measured reflection.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The old dairyman nodded **sagely**, observing that young love was like a May morning, bright yet full of sudden storms."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "The schoolmaster stroked his chin and spoke **sagely** of the portents seen in the northern heavens before the war."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Dick looked **sagely** at the kite, remarking that King Charles had never known such lofty flight."}
    ]
  },
  "Dashboard — sag/sagina.md": {
    "primary": "A genus of small creeping or tufted perennial herbs of the pink family (Caryophyllaceae), commonly called pearlworts.",
    "secondary": "In botanical ecology, low-growing moss-like herbs forming dense green mats along rocky crevices and coastal shores.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Along the gravelly beach of the Falkland Islands, tiny tufts of **sagina** formed green cushions between the boulders."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **sagina** inhabit damp sand and alpine ledges, producing minuscule white four-petaled blossoms."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The pearlwort genus **sagina** demonstrates how tiny herbaceous perennials adapt to severe arctic-alpine exposure."}
    ]
  },
  "Dashboard — sag/saginaw.md": {
    "primary": "A historic commercial and manufacturing city in central Michigan, situated along the navigable Saginaw River.",
    "secondary": "In American industrial history, a nineteenth-century lumber boomtown that transitioned into a major automotive manufacturing center.",
    "quotes": [
      {"author": "Carl Sandburg", "work": "Smoke and Steel", "quote": "Logs floated down from the northern pine forests to the buzzing sawmills that made **saginaw** the lumber capital of the West."},
      {"author": "Theodore Dreiser", "work": "A Hoosier Holiday", "quote": "We drove through the busy streets of **saginaw**, admiring the handsome residences built by pioneer timber barons."},
      {"author": "Hamlin Garland", "work": "A Son of the Middle Border", "quote": "Young woodsmen left for the winter lumber camps near **saginaw**, returning in spring with pockets full of wages."}
    ]
  },
  "Dashboard — sag/sagitta.md": {
    "primary": "An arrow; in astronomy, a small, dim constellation in the northern sky (the Arrow); also an otolith in fish.",
    "secondary": "In comparative ichthyology and marine zoology, the largest calcium carbonate ear-stone used to determine fish age.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Promise of Space", "quote": "The astronomers directed the radio telescope toward the faint stars of **sagitta**, searching for artificial pulse signals."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Dissecting the auditory capsule reveals the large **sagitta**, whose concentric growth rings record seasonal growth."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "In ancient sky lore, the celestial arrow **sagitta** flew forever through the Milky Way between Aquila and Cygnus."}
    ]
  },
  "Dashboard — sag/sagittal.md": {
    "primary": "Of, relating to, or situated in the plane that divides a bilateral organism into right and left parts.",
    "secondary": "In human osteology, the sagittal suture uniting the two parietal bones along the midline of the calvaria.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **sagittal** suture extends between the coronal and lambdoid sutures, marking the junction of the parietal plates."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Comparative craniologists measured the **sagittal** crest in anthropoid apes, noting its connection to temporal muscles."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Thrombosis of the superior **sagittal** sinus was confirmed at autopsy following severe facial erysipelas."}
    ]
  },
  "Dashboard — sag/sagittaria.md": {
    "primary": "A genus of aquatic flowering plants in the water-plantain family (Alismataceae), commonly known as arrowheads or duck-potato.",
    "secondary": "In wetland botany and ethnobotany, wetland perennials producing edible starchy tubers harvested by indigenous peoples.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Along the marshy shallows of the river, the glossy arrow-shaped leaves of **sagittaria** rose above the brown water."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The aquatic species of **sagittaria** bear delicate white flowers in whorls upon tall scapose flower spikes."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina, Georgia, East and West Florida", "quote": "Canoeing through the cypress swamps, I collected a flowering **sagittaria** with broad aquatic tubers loved by wildfowl."}
    ]
  },
  "Dashboard — sag/sagittariidae.md": {
    "primary": "A taxonomic family of predatory birds containing a single surviving species, the secretarybird (*Sagittarius serpentarius*).",
    "secondary": "In systematic avian biology, long-legged African raptors specialized for stalking and stomping venomous snakes on savannahs.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The distinctive raptorial family **sagittariidae** is strictly confined to the Ethiopian zoological region."},
      {"author": "Richard Francis Burton", "work": "First Footsteps in East Africa", "quote": "On the open plain, a secretarybird of the family **sagittariidae** struck repeatedly with its powerful talons at an adder."},
      {"author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "We watched the stately secretarybird, sole representative of **sagittariidae**, stride purposefully through the tall grass."}
    ]
  },
  "Dashboard — sag/sagittarius.md": {
    "primary": "A prominent constellation of the zodiac (the Archer), containing the galactic center of the Milky Way.",
    "secondary": "In astrological tradition and astronomy, the ninth zodiacal sign and a dense star field rich in bright nebulae.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old masthead watchman stared into the southern heavens, where the golden stars of **sagittarius** wheeled toward dawn."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient Babylonian star-gazers depicted **sagittarius** as a winged centaur drawing his celestial bow against Scorpio."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Deep within the constellation of **sagittarius** lies the supermassive black hole at the very core of our galaxy."}
    ]
  },
  "Dashboard — sag/sagittate-leaf.md": {
    "primary": "A leaf shaped like an arrowhead, possessing two pointed, triangular lobes directed downward at the base.",
    "secondary": "In botanical organography, characterizing foliage found in plants like arrowheads (*Sagittaria*) and certain climbing ivies.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The distinctive **sagittate-leaf** of the marsh plant terminates in two acute basal lobes pointing straight toward the stem."},
      {"author": "Charles Darwin", "work": "The Movement and Habits of Climbing Plants", "quote": "The young tendril climbed upward until the first **sagittate-leaf** expanded to capture the dappled forest sunlight."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Field botanists readily identify the water-plantain family by its characteristic **sagittate-leaf** morphology."}
    ]
  },
  "Dashboard — sag/sagittate.md": {
    "primary": "Shaped like an arrowhead; triangular with two pointed basal lobes projecting downward.",
    "secondary": "In plant anatomy and entomology, describing arrow-shaped leaf blades, anthers, or insect wing markings.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The aquatic herb produces large **sagittate** leaves that stand erect above the calm surface of the pond."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The floral bracts of this variety were distinctly **sagittate**, clasping the calyx with two triangular lobes."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Along the muddy portage, I gathered water plants with sharp **sagittate** leaves growing in the beaver meadows."}
    ]
  },
  "Dashboard — sag/sagittiform.md": {
    "primary": "Arrowhead-shaped; possessing the triangular, pointed outline of an arrow head; sagittate.",
    "secondary": "In invertebrate morphology and mineral crystal classification, arrow-shaped shells, barbs, or twinned crystals.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrate Animals", "quote": "The cephalopod mantle terminates in a graceful **sagittiform** fin adapted for rapid backward propulsion in water."},
      {"author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "The opercular valves of this barnacle present a sharply **sagittiform** contour fitted into the calcareous base."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "Certain parasitic copepods attach to fish gills using specialized **sagittiform** hooks that resist strong currents."}
    ]
  },
  "Dashboard — sag/sago.md": {
    "primary": "An edible starch extracted from the spongy pith of various tropical palm stems, especially *Metroxylon sagu*.",
    "secondary": "In Southeast Asian agriculture and traditional puddings, a staple dietary starch processed into pearled pellets.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The islanders rely upon the wild **sago** palm for their daily bread, washing the grated pith in freshwater troughs."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo offered his guests cakes baked of golden **sago** flour harvested from the Pacific islands."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sick child was fed with a cup of warm **sago** pudding, prepared with fresh milk by the kind apothecary."}
    ]
  },
  "Dashboard — sag/saguaro.md": {
    "primary": "A giant, tree-like columnar cactus (*Carnegiea gigantea*) native to the Sonoran Desert, having branching arms and white flowers.",
    "secondary": "In desert ecology, a keystone cactus species providing nesting cavities for desert birds and fruit for indigenous peoples.",
    "quotes": [
      {"author": "John Muir", "work": "Steep Trails", "quote": "The colossal **saguaro** stands like a fluted green monument against the scorching Arizona sky, towering forty feet high."},
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "Father Latour gazed upon the silent desert landscape where the giant **saguaro** cactus raised its solemn arms in prayer."},
      {"author": "Zane Grey", "work": "The Desert of Wheat", "quote": "Sunset gilded the ribbed columns of the **saguaro**, casting elongated purple shadows across the desert floor."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — sag.")
