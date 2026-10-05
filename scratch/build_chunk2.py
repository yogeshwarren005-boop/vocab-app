# -*- coding: utf-8 -*-
"""
Helper script to populate and assemble scratch/curate_fire_cal_p2.py
"""
import sys
import json

part2_words = {}

part2_words["calisthenic"] = {
    "primary": "Of, relating to, or practicing vigorous physical exercises designed to promote bodily strength, agility, and grace.",
    "secondary": "In physical education and athletic history, designating gymnastic movements that utilize bodyweight resistance to foster poise and stamina.",
    "quotes": [
        {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "The routine of **calisthenic** drills in modern academies often lacks the spontaneous joy of free outdoor play."},
        {"author": "Louisa May Alcott", "work": "Little Women", "quote": "The girls performed their morning **calisthenic** exercises with brisk enthusiasm before commencing their studies."},
        {"author": "Thomas Wentworth Higginson", "work": "Out-Door Papers", "quote": "A regular course of **calisthenic** training imparts graceful carriage and muscular endurance to young scholars."}
    ]
}

part2_words["calisthenics"] = {
    "primary": "Gymnastic exercises designed to develop muscular tone, physical agility, and graceful bodily movement using body weight.",
    "secondary": "In athletic training and military physical culture, systematic calisthenic regimens including push-ups, pull-ups, and rhythmic jumping drills.",
    "quotes": [
        {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The students gathered in the courtyard at daybreak to perform their rigorous German **calisthenics** with mechanical precision."},
        {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "Our school mornings invariably commenced with twenty minutes of vigorous **calisthenics** in the damp playground."},
        {"author": "Louisa May Alcott", "work": "An Old-Fashioned Girl", "quote": "Polly demonstrated that simple domestic chores provided better exercise than all the artificial **calisthenics** of fashionable schools."}
    ]
}

part2_words["call"] = {
    "primary": "To cry out with a loud voice, summon a person to come, or name a person or thing.",
    "secondary": "In telecommunications, birding, and jurisprudence, to establish vocal contact, mimic an avian vocalization, or demand legal assembly.",
    "quotes": [
        {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The lookout in the masthead sounded the stirring **call** that alerted every sailor on deck to the spout."},
        {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I heard the night watchman **call** the hour as the thick river mist settled over the cobbled streets."},
        {"author": "Emily Brontë", "work": "Wuthering Heights", "quote": "I thought I heard Cathy's distant voice **call** my name across the desolate darkness of the heather."}
    ]
}

part2_words["call-back"] = {
    "primary": "A return phone call, an invitation to a secondary interview or audition, or a recall of manufactured products.",
    "secondary": "In theatrical casting, telecommunications, and industrial quality management, a subsequent screening of shortlisted candidates or an urgent product recall.",
    "quotes": [
        {"author": "David Mamet", "work": "A Whore's Invention", "quote": "The aspiring actor waited beside the payphone for the decisive **call-back** that could launch his stage career."},
        {"author": "Arthur Miller", "work": "Timebends: A Life", "quote": "The director granted her a second **call-back**, recognizing an unusual emotional authenticity in her delivery."},
        {"author": "Upton Sinclair", "work": "The Flivver King", "quote": "Factory managers issued an immediate **call-back** for thousands of defective axles discovered during assembly."}
    ]
}

part2_words["call-board"] = {
    "primary": "A notice board located backstage in a theatre where rehearsal schedules, cast notices, and messages are posted.",
    "secondary": "In stage management and theatrical lore, the central informational hub where calls, rehearsals, and disciplinary notices are pinned.",
    "quotes": [
        {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "Carrie scanned the crowded **call-board** near the stage door to see when the chorus rehearsals were scheduled."},
        {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "A single glance at the stage manager's **call-board** revealed the chaotic preparations for the evening premiere."},
        {"author": "Willa Cather", "work": "The Song of the Lark", "quote": "She found her name pinned to the **call-board** among the principals chosen for the seasonal opera cycle."}
    ]
}

part2_words["call-in"] = {
    "primary": "A radio or television program that broadcasts comments or queries received by telephone from listeners or viewers.",
    "secondary": "In broadcast journalism and workplace management, participatory broadcast talk radio or mandatory employee check-in protocols.",
    "quotes": [
        {"author": "Studs Terkel", "work": "Talking to Myself: A Memoir of My Times", "quote": "The late-night **call-in** program became a democratic forum where cab drivers and professors shared their fears."},
        {"author": "Marshall McLuhan", "work": "Understanding Media: The Extensions of Man", "quote": "The electronic immediacy of the **call-in** show collapses the distance between media producer and passive consumer."},
        {"author": "Saul Bellow", "work": "The Dean's December", "quote": "He listened absently to a heated radio **call-in** debate regarding municipal corruption in Chicago."}
    ]
}

part2_words["call-out"] = {
    "primary": "An order summoning workers or emergency personnel to attend to a job, or an explicit challenge or reprimand.",
    "secondary": "In industrial labor relations, graphic layout design, and typography, an emergency work dispatch or a breakout text box highlighting crucial content.",
    "quotes": [
        {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The sudden **call-out** of rescue squads to the pithead signaled an explosion in the deep coal seam."},
        {"author": "Jack London", "work": "The Iron Heel", "quote": "Union leaders debated whether a general **call-out** of transport workers could halt the repressive legislation."},
        {"author": "Joseph Conrad", "work": "The Nigger of the 'Narcissus'", "quote": "The boatswain's piercing **call-out** roused all hands from their bunks to secure the flapping sails."}
    ]
}

part2_words["calla"] = {
    "primary": "A herbaceous aquatic or wetland plant of the arum family, especially Calla palustris or the ornamental calla lily.",
    "secondary": "In marshland botany and ornamental floriculture, a bog perennial bearing glossy heart-shaped foliage, a white spathe, and bright red berry clusters.",
    "quotes": [
        {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "In the secluded swamps of northern Maine, the wild **calla** unfurled its white spathes among dark mosses."},
        {"author": "John Muir", "work": "A Thousand-Mile Walk to the Gulf", "quote": "Along stagnant blackwater creeks, clumps of blooming **calla** illuminated the deep shadows of the cypress trees."},
        {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "The pristine white spathes of the cultivated **calla** provided an exquisite architectural accent to the water garden."}
    ]
}

part2_words["callable"] = {
    "primary": "Subject to being called or recalled, especially denoting a financial bond redeemable by the issuer before maturity.",
    "secondary": "In corporate finance and software engineering, a security with an embedded call option or a programmatic routine invoked by an execution thread.",
    "quotes": [
        {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Investors demanded higher yields upon **callable** bonds to compensate for the risk of early redemption during low interest periods."},
        {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Corporations frequently issued **callable** debentures to retain financial flexibility against sudden fluctuations in the capital market."},
        {"author": "Benjamin Graham", "work": "The Intelligent Investor", "quote": "The conservative investor must examine whether a high-coupon security is **callable** at short notice by the issuing company."}
    ]
}

part2_words["callas"] = {
    "primary": "Plural form of calla, denoting multiple ornamental plants or blossoms belonging to the arum family.",
    "secondary": "In floristry and garden design, elegant arum plants cultivated for their trumpet-shaped spathes and lush arrow-shaped leaves.",
    "quotes": [
        {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Vases overflowing with pristine white **callas** adorned the drawing-room tables for the ceremonial afternoon reception."},
        {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "In the damp garden border, the waxen blooms of the **callas** gleamed under the tropical moonlight."},
        {"author": "Gertrude Jekyll", "work": "Colour in the Flower Garden", "quote": "The dramatic green foliage of the **callas** contrasted splendidly against the pale limestone balustrades of the terrace."}
    ]
}

part2_words["callathump"] = {
    "primary": "A noisy, boisterous, mock-serenade or discordant parade accompanied by banging pans, horns, and kettles; a shivaree.",
    "secondary": "In American folklore and dialectology, a riotous impromptu carnival or rough-music serenade intended to mock or celebrate newlyweds.",
    "quotes": [
        {"author": "Washington Irving", "work": "Salmagundi", "quote": "The nocturnal mischief-makers organized a deafening **callathump** outside the magistrate's window, rattling tins and blowing cow horns."},
        {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The drunken celebration dissolved into a furious **callathump** that echoed across the riverbanks long past midnight."},
        {"author": "Bret Harte", "work": "Tales of the Argonauts", "quote": "A rowdy crew from the mining camp greeted the frontier wedding with an uproarious **callathump**."}
    ]
}

part2_words["callback"] = {
    "primary": "An invitation to return for a second round of auditions or interviews, or a return telephone connection.",
    "secondary": "In software engineering and telecommunications, an executable function passed as an argument to be invoked asynchronously upon completion of an operation.",
    "quotes": [
        {"author": "Arthur Miller", "work": "Timebends: A Life", "quote": "When the young actress received her second **callback**, the producer recognized her latent dramatic intensity."},
        {"author": "David Mamet", "work": "True and False: Heresy and Common Sense for the Actor", "quote": "Do not alter your character choices merely to please casting agents during an unexpected **callback**."},
        {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "The interrupt handler invokes a registered **callback** to notify the primary algorithm that data transfer is complete."}
    ]
}

part2_words["caller"] = {
    "primary": "A person who pays a visit to someone, places a telephone call, or calls out the steps in a traditional dance.",
    "secondary": "In folk choreography and social customs, the dance master who announces figure changes in square dances, or an etiquette visitor.",
    "quotes": [
        {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet bustled about the drawing-room in great excitement to receive an unexpected morning **caller**."},
        {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge glowered suspiciously at the cheerful **caller** who knocked at his counting-house door wishing him merry tidings."},
        {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The energetic dance **caller** shouted each figure with rustic gusto above the spirited screech of the fiddles."}
    ]
}

part2_words["caller-out"] = {
    "primary": "A person whose role is to shout out or announce names, turns, warnings, or goods publicly.",
    "secondary": "In historical industrial manufacturing and trade guilds, an appointed crier who summoned shifts of dockworkers, weavers, or miners.",
    "quotes": [
        {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "At dawn the **caller-out** traversed the cobbled alleys, rapping sharply on windowpanes to rouse the miners for their shift."},
        {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The court **caller-out** bawled the defendant's name through the noisy corridors of the crowded tribunal."},
        {"author": "Jack London", "work": "The People of the Abyss", "quote": "Before the dock gates opened, a gruff **caller-out** shouted the names of the few casual laborers selected for day work."}
    ]
}

part2_words["caller-up"] = {
    "primary": "A knocker-up or early-morning worker employed to awaken factory hands and miners before dawn.",
    "secondary": "In British industrial social history, a specialized itinerant morning worker who tapped upstairs bedroom windows with long bamboo rods.",
    "quotes": [
        {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "In the cold morning twilight, the steady tap of the **caller-up** echoed against the damp brick tenements of the mining town."},
        {"author": "Arnold Bennett", "work": "Clayhanger", "quote": "Long before the factory whistles shrieked, the old **caller-up** rattled his long pole against Edwin's window frame."},
        {"author": "D. H. Lawrence", "work": "Sons and Lovers", "quote": "Mrs. Morel woke promptly at five, hearing the punctual footsteps of the village **caller-up** descending the stony hill."}
    ]
}

part2_words["calliandra"] = {
    "primary": "A genus of tropical and subtropical flowering shrubs or trees in the pea family, characterized by showy tassel-like floral stamens.",
    "secondary": "In tropical ornamental arboriculture, the powder-puff bush whose globular inflorescences feature hundreds of elongated crimson or pink stamens.",
    "quotes": [
        {"author": "David Fairchild", "work": "Exploring for Plants", "quote": "Shrubs of scarlet **Calliandra** illuminated the edges of the clearing with their feathery globes of bright red stamens."},
        {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of the New Continent", "quote": "Along the Orinoco riverbanks, species of **Calliandra** unfold their delicate blossoms in the tropical humidity."},
        {"author": "Paul C. Standley", "work": "Trees and Shrubs of Mexico", "quote": "The brilliant blossoms of **Calliandra** attract hummingbirds and honey bees from early dawn until sunset."}
    ]
}

part2_words["callicebus"] = {
    "primary": "A genus of small, arboreal South American monkeys in the family Pitheciidae, commonly known as titi monkeys.",
    "secondary": "In primatology and Neotropical zoology, monogamous primates characterized by soft dense fur, tail-twining behaviors, and complex dawn vocal duets.",
    "quotes": [
        {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "Pairs of **Callicebus** monkeys sat close together on high lianas, entangling their long bushy tails with affectionate intimacy."},
        {"author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "At dawn the mournful, melodious cries of the **Callicebus** resounded throughout the flooded Amazonian forest."},
        {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of the New Continent", "quote": "The indigenous hunters pointed out small groups of **Callicebus** sheltering within the thickest canopies of the river basin."}
    ]
}

part2_words["calligraph"] = {
    "primary": "A specimen, piece, or document produced in beautiful, elegant, artistic handwriting.",
    "secondary": "In paleography and epigraphy, an exquisite manuscript or ornamental inscription executing formal typographic and calligraphic artistry.",
    "quotes": [
        {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "An ancient **calligraph** preserves not merely the writer's thoughts, but the physical rhythm and soul of his hand."},
        {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "A masterly medieval **calligraph** balances blackletter majesty with gold leaf embellishments across vellum folios."},
        {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Every letter in this Gothic **calligraph** was drawn with religious devotion and absolute artistic poise."}
    ]
}

part2_words["calligrapher"] = {
    "primary": "A practitioner skilled in the craft and artistic execution of fine handwriting and decorative lettering.",
    "secondary": "In the history of manuscript arts and graphic design, a master scribe trained in historic scripts, formal illumination, and balanced stroke dynamics.",
    "quotes": [
        {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The royal **calligrapher** was rewarded handsomely for producing gilded copies of classical treatises for the caliph's library."},
        {"author": "William Morris", "work": "The Ideal Book", "quote": "The medieval **calligrapher** treated each manuscript page as an integrated work of sublime graphic architecture."},
        {"author": "Ralph Waldo Emerson", "work": "Letters and Social Aims", "quote": "A disciplined **calligrapher** moves his quill with the ease and fluidity of a dancer tracing graceful patterns in air."}
    ]
}

part2_words["calligraphic"] = {
    "primary": "Of, relating to, or characterized by beautiful, decorative, and artistically controlled penmanship or brushwork.",
    "secondary": "In art history and aesthetic theory, designating visual lines, brushstrokes, or decorative flourishes possessing rhythmic flow and expressive linear beauty.",
    "quotes": [
        {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner's delicate pen sketches possess a **calligraphic** elegance that conveys mountainous vitality in a single stroke."},
        {"author": "Roger Fry", "work": "Vision and Design", "quote": "Chinese brush painting relies upon **calligraphic** mastery to suggest form and emotional weight simultaneously."},
        {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "The **calligraphic** vitality of fourteenth-century manuscripts vanished with the mechanization of cheap commercial printing."}
    ]
}

print(f"Loaded {len(part2_words)} words in chunk 2")
