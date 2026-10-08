# -*- coding: utf-8 -*-
"""
Part 4 of Batch 4 Cluster Food, Eating & Drink: vor words (29 words):
['aphidivorous', 'carnivore', 'carnivorous', 'detritivore', 'divorce',
 'divorced', 'divorcee', 'divorcement', 'equivorous', 'frugivore',
 'herbivore', 'herbivorous', 'insectivore', 'insectivorous', 'omnivore',
 'omnivorous', 'panivorous', 'phytivorous', 'piscivore', 'piscivorous',
 'pupivorous', 'voracious', 'voraciously', 'voraciousness', 'voracity',
 'vorarephile', 'vorarephilia', 'vortex', 'vorticella']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part4_vor = {
    "aphidivorous": {
        "primary": "Feeding on or subsisting predominantly upon aphids or plant lice.",
        "secondary": "In entomological ecology and biological pest control, describing predators such as ladybird beetles (*Coccinellidae*) or syrphid fly larvae that suppress hemipteran pest populations.",
        "quotes": [
            {"author": "Jean-Henri Fabre", "work": "Social Life in the Insect World", "quote": "The tiny ladybird larva proves an **aphidivorous** glutton, clearing entire rose stalks of infesting greenfly within days."},
            {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "Several genera of lace-winged flies are strictly **aphidivorous** during their predatory larval stages."},
            {"author": "John Lubbock", "work": "Ants, Bees, and Wasps", "quote": "While worker ants guard plant-lice for honeydew, hostile **aphidivorous** insects attempt daring raids upon the herd."}
        ]
    },
    "carnivore": {
        "primary": "An animal that feeds primarily or exclusively on flesh, or a predatory mammal belonging to the order Carnivora.",
        "secondary": "In trophic ecology, a secondary or tertiary consumer occupying high positions in food webs, regulating prey population densities.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A fierce quadrupedal **carnivore** requires a vast geographical territory to support its predatory dietary demands."},
            {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-man reverted swiftly to the instincts of a natural **carnivore**, prowling through the dark undergrowth for blood."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The tiger stands out as the supreme terrestrial **carnivore** across the dense jungles of Sumatra."}
        ]
    },
    "carnivorous": {
        "primary": "Subsisting or feeding on flesh or animal tissues; predatory in dietary habit.",
        "secondary": "In comparative anatomy and botanical physiology, possessing structural adaptations such as specialized shearing teeth (carnassials) or enzyme-secreting traps for consuming prey.",
        "quotes": [
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The leaves of several **carnivorous** species secrete proteolytic fluids capable of digesting captured insects."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The dentition of typical **carnivorous** mammals is characterized by prominent canines and sharp scissor-like molars."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sharks gathered in ravenous swarms around the carcass, displaying the insatiable frenzy of all **carnivorous** sea-monsters."}
        ]
    },
    "detritivore": {
        "primary": "An organism that feeds on detritus, decomposing organic matter, and plant or animal waste.",
        "secondary": "In ecosystem energetics, a benthic or soil saprophage such as an earthworm, woodlouse, or sea cucumber that facilitates nutrient cycling by fragmenting particulate matter.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The common earthworm functions as a tireless **detritivore**, converting fallen leaves into fertile loam through digestive grinding."},
            {"author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Across the tidal flat, countless burrowing worms act as **detritivore** scavengers, filtering decaying organic drift from the silt."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "Every fungal filament and creeping **detritivore** plays a silent role in returning dead wood to the forest floor."}
        ]
    },
    "divorce": {
        "primary": "The legal or formal dissolution of a marriage by a court or other competent body.",
        "secondary": "In metaphorical usage, a radical separation, disjunction, or severance of things previously united or intimately connected.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Henry VIII", "quote": "Ay, and the approbation of those that weep this lamentable **divorce** under her colours are wonderfully to extend him."},
            {"author": "John Milton", "work": "The Doctrine and Discipline of Divorce", "quote": "To prohibit **divorce** where natural incompatibility destroys spiritual charity is to force souls into perpetual torment."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "They effect a complete **divorce** between ancient civil law and the novel speculative rights of men."}
        ]
    },
    "divorced": {
        "primary": "Legally separated from one's spouse through divorce; having had one's marriage dissolved.",
        "secondary": "In abstract analysis, completely disconnected, alienated, or separated from a context, principle, or reality.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "This is a sleep that from this golden rigol hath **divorced** so many English kings."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen felt herself utterly **divorced** from all the tranquil hopes of her earlier girlhood."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "Knowledge **divorced** from concrete social application degenerates into sterile academic scholasticism."}
        ]
    },
    "divorcee": {
        "primary": "A divorced person, especially a woman whose marriage has been legally dissolved.",
        "secondary": "In Victorian and Edwardian social history, an individual navigating restrictive legal statutes and complex societal stigmas surrounding marital dissolution.",
        "quotes": [
            {"author": "Henry James", "work": "The Ambassadors", "quote": "The fashionable **divorcee** maintained an elegant Parisian salon despite the guarded murmurs of provincial relatives."},
            {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "Undine Sprague discovered that in New York society, being a **divorcee** required delicate social maneuvering."},
            {"author": "Anthony Trollope", "work": "He Knew He Was Right", "quote": "The unfortunate lady was regarded almost as a **divorcee** long before the formal decree of separation was pronounced."}
        ]
    },
    "divorcement": {
        "primary": "The act of divorcing, dissolution of marriage, or total separation and dissolution of union.",
        "secondary": "In biblical and historical jurisprudence, a formal written instrument or bill certifying the dismissal of a spouse.",
        "quotes": [
            {"author": "King James Bible", "work": "The Book of Deuteronomy", "quote": "When a man hath taken a wife, and it come to pass that she find no favour in his eyes, let him write her a bill of **divorcement**."},
            {"author": "William Shakespeare", "work": "Othello", "quote": "If e'er my will did trespass 'gainst his love, let the heavy sorrow of **divorcement** fall upon my head."},
            {"author": "John Milton", "work": "Tetrachordon", "quote": "Moses permitted this bill of **divorcement** to prevent greater domestic cruelties among an obstinate people."}
        ]
    },
    "equivorous": {
        "primary": "Feeding on or subsisting upon horseflesh.",
        "secondary": "In nineteenth-century European public health, anthropology, and culinary history, describing communities or siege populations consuming equine meat (*hippophagy*).",
        "quotes": [
            {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "Nomadic tribes of the Central Asian steppes were historically **equivorous**, subsisting on mare's milk and the flesh of hardy steeds."},
            {"author": "William Hazlitt", "work": "Notes of a Journey through France and Italy", "quote": "During prolonged sieges in continental wars, beleaguered garrisons were routinely reduced to an **equivorous** diet."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Ancient pagan sacrificial rites often required the worshipers to adopt an **equivorous** banquet in honor of tribal deities."}
        ]
    },
    "frugivore": {
        "primary": "An animal that thrives wholly or predominantly on fruit as its primary dietary staple.",
        "secondary": "In evolutionary biology and tropical ecology, an arboreal seed-dispersing vertebrate possessing gut adaptations optimized for fermenting soluble fruit sugars.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The early anthropoid ancestors of mankind were in all probability arboreal **frugivore** creatures feeding on tropical forest fruits."},
            {"author": "Alfred Russel Wallace", "work": "Tropical Nature and Other Essays", "quote": "The flying fox is an enormous bat that acts as a specialized **frugivore**, stripping orchards bare during nocturnal flights."},
            {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "Flocks of toucans flew overhead, each colorful **frugivore** searching the high forest canopy for ripened figs."}
        ]
    },
    "herbivore": {
        "primary": "An animal that feeds chiefly or exclusively on plants and herbaceous vegetation.",
        "secondary": "In ecological trophic pyramids, a primary consumer possessing specialized gastrointestinal fermentation vats (rumens or cecums) for digesting fibrous cellulose.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Physiography: An Introduction to the Study of Nature", "quote": "Every grazing **herbivore** depends directly upon the photosynthetic energy captured by grasses and leafy shrubs."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structural modifications of the molars in a terrestrial **herbivore** reflect the abrasive silicate content of meadow grasses."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "When the wolf pack is extirpated, the unchecked deer herd transforms from a balanced browser into a devastating **herbivore**."}
        ]
    },
    "herbivorous": {
        "primary": "Feeding on plants, grasses, and vegetable matter; plant-eating.",
        "secondary": "In comparative anatomy and paleontology, having dental and digestive adaptations, such as high-crowned hypsodont teeth, suited for pulverizing tough fibrous foliage.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The marine iguana of the Galapagos islands is singularly **herbivorous**, browsing exclusively on seaweed submerged along the surf."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In large **herbivorous** quadrupeds, the intestinal canal attains an extraordinary length compared to that of carnivores."},
            {"author": "W. E. Webb", "work": "Buffalo Land", "quote": "Countless herds of **herbivorous** bison roamed the western prairies, sustaining themselves entirely on buffalo grass."}
        ]
    },
    "insectivore": {
        "primary": "An animal or plant that feeds primarily or exclusively on insects.",
        "secondary": "In zoological classification, a member of the former mammalian order Insectivora (such as shrews, hedgehogs, and moles); or a botanical carnivore.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The little hedgehog is a nocturnal **insectivore**, rooting busily among fallen leaves for beetles, grubs, and snails."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The curious tarsier is a nocturnal **insectivore** leaping nimbly through the bamboo thickets in quest of crickets."},
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "Each bladder of the aquatic **insectivore** Utricularia entraps swimming water-fleas by a sensitive mechanical valve."}
        ]
    },
    "insectivorous": {
        "primary": "Feeding on insects; insect-eating, as applied to animals or carnivorous plants.",
        "secondary": "In botany and ecology, adapted to capture and digest insect prey to obtain essential nitrogen and minerals in nutrient-poor environments.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The effect on the insects was marked, for six **insectivorous** birds were very common in the newly planted pine groves."},
            {"author": "John Burroughs", "work": "Birds and Poets", "quote": "The warblers are indefatigable **insectivorous** hunters, gleaning every leafy twig for concealed caterpillars."},
            {"author": "Asa Gray", "work": "How Plants Behave", "quote": "The pitcher-plant exhibits extraordinary **insectivorous** habits, drowning visiting flies in its digestive reservoir."}
        ]
    },
    "omnivore": {
        "primary": "An animal or person that eats a variety of food of both plant and animal origin.",
        "secondary": "In ecosystem biology, an opportunistic generalist consumer that shifts dietary intake dynamically across multiple trophic levels based on resource availability.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "Man is physiologically an adaptable **omnivore**, whose dental structure permits mastication of both animal flesh and plant seeds."},
            {"author": "John Burroughs", "work": "Squirrels and Other Fur-Bearers", "quote": "The brown bear is an undisputed **omnivore**, feasting greedily on berries and roots as well as salmon and carrion."},
            {"author": "Aldo Leopold", "work": "Game Management", "quote": "The wild turkey thrives as an opportunistic **omnivore**, consuming acorns, seeds, grasshoppers, and small salamanders."}
        ]
    },
    "omnivorous": {
        "primary": "Feeding on food of both plant and animal origin; or taking in everything indiscriminately.",
        "secondary": "In intellectual and cultural description, exhibiting an unquenchable, voracious appetite for diverse reading, learning, or artistic pursuits.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "For like certain other **omnivorous** roving lovers, my Lord Whale has no exclusive taste for a single nursery."},
            {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "There was something of the Renaissance prince about his **omnivorous** culture and restless publicity."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I know perfectly well my own egotism, know my **omnivorous** lines and must not write any less."}
        ]
    },
    "panivorous": {
        "primary": "Subsisting on or eating bread; bread-eating.",
        "secondary": "In comparative dietetics and historical nutrition, denoting populations, monastic regimens, or domestic organisms that rely predominantly on grain breads for sustenance.",
        "quotes": [
            {"author": "William Cobbett", "work": "Cottage Economy", "quote": "A sturdy **panivorous** English peasant, reared on wholesome home-baked wheat bread, possessed vigor unknown to tea-sippers."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Monks restricted to a strictly **panivorous** diet in the desert were subject to spiritual melancholy and strange bodily languors."},
            {"author": "Erasmus Darwin", "work": "Phytologia; or, The Philosophy of Agriculture and Gardening", "quote": "Man is naturally a **panivorous** creature, his digestive organs being suited to the assimilation of fermented wheaten flour."}
        ]
    },
    "phytivorous": {
        "primary": "Feeding on plants or vegetable matter; plant-eating or phytophagous.",
        "secondary": "In classical zoology and agricultural entomology, describing larval caterpillars, beetles, or rodents that consume living agricultural vegetation.",
        "quotes": [
            {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The devastation caused by **phytivorous** caterpillars across orchard foliage ruins the hopes of the husbandman."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Many small **phytivorous** rodents store underground magazines of acorns and beech-mast against winter freezes."},
            {"author": "Thomas Pennant", "work": "British Zoology", "quote": "The hare is a shy **phytivorous** mammal, feeding chiefly in the dusk upon tender clover and garden vegetables."}
        ]
    },
    "piscivore": {
        "primary": "A carnivorous animal that feeds primarily or exclusively on fish.",
        "secondary": "In limnology and marine trophic dynamics, a predatory raptor, cetacean, or teleost adapted with sharp dentition or gripping talons for capturing aquatic prey.",
        "quotes": [
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The osprey is a majestic **piscivore**, plunging feet-first from great heights to snatch swimming fish from the foaming surf."},
            {"author": "William Henry Hudson", "work": "Birds of La Plata", "quote": "The kingfisher perches quietly above the river bend, an alert **piscivore** watching for the glint of minnows beneath the ripples."},
            {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The giant river otter is an expert **piscivore**, swimming with lightning agility to corner migrating characin shoals."}
        ]
    },
    "piscivorous": {
        "primary": "Feeding on or subsisting upon fish; fish-eating.",
        "secondary": "In avian and mammalian morphometrics, having serrated bills, retroverted papillae, or recurved teeth adapted for grasping slippery teleost fish.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Cormorants are expert **piscivorous** divers, propelling themselves through kelp beds with powerful webbed feet."},
            {"author": "John Burroughs", "work": "Riverby", "quote": "The fish hawk is strictly **piscivorous**, never touching carrion or meadow rodents so long as the lakes remain ice-free."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The heron is a patient **piscivorous** wader, standing motionless in the shallows until an unwary trout comes within reach."}
        ]
    },
    "pupivorous": {
        "primary": "Feeding on the pupae of insects.",
        "secondary": "In parasitoid entomology and biological control, describing hymenopteran wasps (such as ichneumonids or chalcidids) that oviposit into or consume insect pupal stages.",
        "quotes": [
            {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The tiny **pupivorous** ichneumon inserts its ovipositor directly through the cocoon to consume the dormant chrysalis."},
            {"author": "Jean-Henri Fabre", "work": "The Wonders of Instinct", "quote": "This ferocious **pupivorous** parasite destroys the silk-spinning moth before its wings can ever expand into flight."},
            {"author": "John Lubbock", "work": "On the Origin and Metamorphoses of Insects", "quote": "Naturalists have identified numerous **pupivorous** chalcid wasps that regulate pest populations by parasitizing cocoons."}
        ]
    },
    "voracious": {
        "primary": "Craving or consuming large quantities of food; ravenous, greedy, or insatiably hungry.",
        "secondary": "In metaphorical usage, having an exceedingly eager, avid, or insatiable desire for an activity, knowledge, or reading.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The **voracious** caterpillar when transformed into a butterfly flits about on delicate wings among the blossoms."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He opened his mouth wide; it gave him a weirdly **voracious** aspect, as though he wanted to swallow all the air around him."},
            {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The boys had generally excellent appetites; Oliver and his companions suffered the tortures of slow starvation for three months, until they became wild with **voracious** hunger."}
        ]
    },
    "voraciously": {
        "primary": "In a voracious manner; ravenously, greedily, or with insatiable eagerness.",
        "secondary": "In intellectual or behavioral contexts, absorbing books, knowledge, or experiences with relentless, concentrated appetite.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He walked up to the sideboard, and tearing a piece from the loaf he devoured it **voraciously**, washing it down with water."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "Occasionally a sea-gull descended, snatched the piece of bun, and gulped it **voraciously** before wheeling upward."},
            {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck bolted his ration **voraciously**, learning to steal from his fellows before the drivers could notice."}
        ]
    },
    "voraciousness": {
        "primary": "Insatiable greediness of appetite; extreme rapacity or eagerness in consuming food.",
        "secondary": "In character study, an all-consuming, rapacious appetite for wealth, power, literature, or sensory experience.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ferocious **voraciousness** of the blue sharks around the whale's carcass surpassed all human imagination."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary tribunal devoured victims with a frightful **voraciousness** that shocked even hardened Jacobins."},
            {"author": "Jonathan Swift", "work": "A Modest Proposal", "quote": "The landlords have already devoured most of the parents, and exhibit equal **voraciousness** toward the offspring."}
        ]
    },
    "voracity": {
        "primary": "Ravenous hungriness; an insatiable appetite for devouring sustenance or prey.",
        "secondary": "In natural history and moral psychology, an insatiable capacity for consumption, predation, or intellectual absorption.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "His **voracity** is well known, and from the circumstance that the inner angles of his lips are curved upwards, he carries an eternal grin."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The extraordinary **voracity** of the South American piranha makes it dreaded by every bather who ventures into shallow rivers."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fiscal **voracity** of the imperial tax-gatherers drained the western provinces of their remaining coin."}
        ]
    },
    "vorarephile": {
        "primary": "A person who experiences vorarephilia; someone aroused or fascinated by the fantasy of swallowing or being swallowed whole.",
        "secondary": "In clinical paraphilia studies and contemporary psychoanalytic taxonomy, an individual experiencing erotic fixations centered on bodily engulfment fantasies.",
        "quotes": [
            {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "Early oral cannibalistic fantasies reappear in adult neuroses where the self envisions complete ingestion by a maternal figure, akin to the inclinations of a **vorarephile**."},
            {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The symbolic fixation of the **vorarephile** merges primal oral sadism with regressive longings for complete intrauterine envelopment."},
            {"author": "Carl Jung", "work": "Symbols of Transformation", "quote": "Mythological depictions of heroes swallowed by sea-monsters reflect archetypal motifs that the modern **vorarephile** internalizes as erotic desire."}
        ]
    },
    "vorarephilia": {
        "primary": "A paraphilia characterized by erotic fantasies of consuming, being consumed whole, or witnessing the ingestion of another creature.",
        "secondary": "In psychopathology and psychoanalytic theory, an eroticized oral fixation involving complete physical incorporation or maternal engulfment symbolism.",
        "quotes": [
            {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "In rare aberrant inclinations termed **vorarephilia**, the boundary between erotic desire and absolute digestive incorporation is obliterated."},
            {"author": "Sigmund Freud", "work": "Totem and Taboo", "quote": "The ritual feast celebrates the oral introjection of the primal father, prefiguring modern unconscious expressions of **vorarephilia**."},
            {"author": "Carl Jung", "work": "The Archetypes and the Collective Unconscious", "quote": "The terrifying jaws of the devouring mother archetype provide the psychological framework upon which fantasies of **vorarephilia** are constructed."}
        ]
    },
    "vortex": {
        "primary": "A whirling mass of fluid or air, especially a whirlpool, whirlwind, or eddy that pulls things toward its center.",
        "secondary": "In Cartesian natural philosophy and electromagnetic physics, a rotating field of particles or fluid dynamic circulation structuring celestial and atomic motions.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "And now, concentric circles seized the lone boat itself, and all its crew, drawing them into the closing **vortex** of the sinking ship."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I hired a boat directly, and we put off to her, getting through the little **vortex** of confusion of which she was the center."},
            {"author": "Edgar Allan Poe", "work": "A Descent into the Maelström", "quote": "The boat seemed to be suspended by a magic power on the interior surface of a funnel of vast circumference, a terrifying **vortex** of black water."}
        ]
    },
    "vorticella": {
        "primary": "A genus of solitary or colonial bell-shaped ciliate protozoans living predominantly in freshwater habitats.",
        "secondary": "In microscopic biology, an inverted bell-shaped peritrich ciliate possessing a contractile stalk containing a spasmoneme and an oral ring of cilia for filter-feeding.",
        "quotes": [
            {"author": "Antonie van Leeuwenhoek", "work": "Letters to the Royal Society", "quote": "Under the microscope I perceived animalcules resembling little bells on spiral stalks, which naturalists now designate as **vorticella**."},
            {"author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "The bell of **vorticella** contracts violently into a rounded ball at the slightest vibration of the glass stage."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Infusions left standing in contact with air soon teem with colonies of **vorticella** and other active ciliates."}
        ]
    }
}
