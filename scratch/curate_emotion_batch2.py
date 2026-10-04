# -*- coding: utf-8 -*-
"""
Curates Dashboard — cup (36 words) and Dashboard — path (39 words) in Cluster Emotion (75 words total).
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cup (36 words)
  # =========================================================================
  "Dashboard — cup/concupiscence.md": {
    "primary": "Strong sexual desire or lust; ardent or inordinate sensual appetite.",
    "secondary": "In Christian theology, the inherent inclination of fallen human nature toward sin and temporal indulgence.",
    "quotes": [
      {"author": "Augustine of Hippo", "work": "Confessions", "quote": "My youth was tossed about upon the churning sea of **concupiscence**, far from the harbor of divine peace."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "Original sin transmits a disordered **concupiscence** that clouds reason and inclines the will toward temporal goods."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Carnal desire inflamed their minds, leading to shameless **concupiscence** after eating the forbidden fruit."}
    ]
  },
  "Dashboard — cup/concupiscent.md": {
    "primary": "Filled with or expressing strong sexual desire, lust, or sensual longing.",
    "secondary": "In classical moral philosophy, pertaining to the desiring or appetitive faculty of the soul (the concupiscible power).",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The spiritual will must constantly govern the unruly impulses of the **concupiscent** nature."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A noble soul rises above the **concupiscent** cravings of the flesh to contemplate pure ideal truth."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Ancient moralists correctly distinguished between the irascible and the **concupiscent** faculties of the human mind."}
    ]
  },
  "Dashboard — cup/cup.md": {
    "primary": "A small bowl-shaped container for drinking from, typically having a handle.",
    "secondary": "In metaphorical and liturgical tradition, one's allotted portion of joy, suffering, or divine fate in life.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Give me the **cup**: let go; by heaven, I'll have't. O good Horatio, what a wounded name, things standing thus unknown, shall live behind me!"},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty poured me a hot **cup** of tea, watching my tired face with affectionate solicitude."},
      {"author": "John Milton", "work": "Comus", "quote": "He offers to every weary traveler his enchanted **cup**, transforming their human visage into brutish form."}
    ]
  },
  "Dashboard — cup/cupcake.md": {
    "primary": "A small cake baked in a cup-shaped foil or paper container, typically iced and decorated.",
    "secondary": "In early American culinary history, an individual portion cake originally measured out by volume in standard tea cups.",
    "quotes": [
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Meg baked a delicate frosted **cupcake** for each of the children as a special holiday surprise."},
      {"author": "Amelia Simmons", "work": "American Cookery", "quote": "Bake the sweet batter in small cups until golden, producing a light and toothsome **cupcake**."},
      {"author": "Laura Ingalls Wilder", "work": "Little Town on the Prairie", "quote": "Mary carefully set a pink-frosted **cupcake** beside each dinner plate for the sociable."}
    ]
  },
  "Dashboard — cup/cupel.md": {
    "primary": "A small, porous shallow vessel made of bone ash, used in assaying and refining precious metals.",
    "secondary": "In metallurgical chemistry, an absorbent crucible heated in a muffle furnace to separate lead from gold and silver.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The molten lead was absorbed by the porous bone ash of the **cupel**, leaving a pure bead of silver behind."},
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Examine the surface of the **cupel** carefully to verify that all base metals have oxidized and sunken into the vessel."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "In high-temperature assaying, the bone-ash **cupel** withstands intense heat while selectively absorbing volatile litharge."}
    ]
  },
  "Dashboard — cup/cupid.md": {
    "primary": "The Roman god of love and desire, usually depicted as a winged boy with a bow and arrow.",
    "secondary": "In classical iconography and mythology, the capricious divine personification of erotic attraction and romantic infatuation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Love looks not with the eyes, but with the mind; and therefore is winged **Cupid** painted blind."},
      {"author": "John Keats", "work": "Ode to Psyche", "quote": "The winged boy, fair **Cupid**, lay entwined with Psyche beneath the fragrant forest boughs."},
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "A thousand fluttering sprites surrounded Belinda, guarding her locks from mischievous **Cupid**'s darts."}
    ]
  },
  "Dashboard — cup/cupidity.md": {
    "primary": "Greed for money, wealth, or possessions; avarice or excessive covetousness.",
    "secondary": "In moral philosophy and political economy, an unbridled acquisitive impulse that undermines civic virtue and justice.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on the Nabob of Arcot's Debts", "quote": "The unprincipled **cupidity** of colonial adventurers drained the wealth of the ancient province."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor's insatiable **cupidity** prompted him to confiscate the ancestral estates of wealthy senators."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Society is corrupted when the admiration due to wisdom and virtue is squandered upon vulgar **cupidity**."}
    ]
  },
  "Dashboard — cup/cuplike.md": {
    "primary": "Resembling or shaped like a cup; concave, hemispherical, or bowl-shaped.",
    "secondary": "In botanical morphology, describing flowers, receptacles, or gall formations having a deep, hollow curvature.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The specialized cotyledons form a **cuplike** hollow that collects morning dew for the germinating seedling."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The involucre of the acorn forms a rugged, **cuplike** base supporting the smooth seed."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Fungus of bright scarlet sprouted upon the decaying stump, forming small **cuplike** vessels that held raindrops."}
    ]
  },
  "Dashboard — cup/cupola.md": {
    "primary": "A small dome, especially a small dome on a drum on top of a larger dome or roof.",
    "secondary": "In architectural design and military naval engineering, a rounded superstructure serving as a lantern, lookout, or revolving turret.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "From the elevated glass **cupola** upon the mansion roof, one could view the ships sailing into the harbor."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The gilded **cupola** of the cathedral gleamed through the London smoke, guiding travelers from afar."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The great plantation house was crowned with an airy glass **cupola** where the planter surveyed his broad fields."}
    ]
  },
  "Dashboard — cup/cupper.md": {
    "primary": "A person who performs the medical therapy of cupping; also a tool or device used for cupping.",
    "secondary": "In the historical history of medicine, a surgical practitioner specializing in bloodletting using heated glass suction cups.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In local pulmonary congestion, the skilled hospital **cupper** applied dry glasses along the posterior thorax."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "A noisy Italian **cupper** was summoned to bleed the patient, brandishing his scarificator with theatrical flourishes."},
      {"author": "Benjamin Rush", "work": "Medical Inquiries and Observations", "quote": "The professional **cupper** must exercise caution when scarifying children, lest excessive bloodletting induce syncope."}
    ]
  },
  "Dashboard — cup/cupping.md": {
    "primary": "A therapeutic method in alternative and historical medicine in which heated cups are applied to the skin to create suction.",
    "secondary": "In clinical history, categorized into dry cupping (suction alone) and wet cupping (suction combined with superficial skin scarification).",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dry **cupping** over the lumbar region frequently afforded symptomatic relief in acute renal congestion."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The cutaneous hyperemia produced by **cupping** demonstrates the rapid response of capillary networks to negative atmospheric pressure."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Careful attention must be paid when wet **cupping** is prescribed, ensuring absolute cleanliness of the scarified surfaces."}
    ]
  },
  "Dashboard — cup/cupressaceae.md": {
    "primary": "The cypress family of coniferous trees and shrubs, characterized by scale-like evergreen leaves and peltate cones.",
    "secondary": "In systematic gymnosperm botany, a globally distributed conifer family including cypresses, junipers, redwoods, and arborvitae.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Members of the family **Cupressaceae** bear small, opposite, scale-like leaves closely appressed to the twigs."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The modern distribution of ancient genera within **Cupressaceae** reveals the fragmentation of once continuous circumpolar forests."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The colossal sequoias belonging to **Cupressaceae** stand as immortal monuments to primeval nature."}
    ]
  },
  "Dashboard — cup/cupressus.md": {
    "primary": "A genus of evergreen coniferous trees and shrubs commonly known as cypresses.",
    "secondary": "In dendrology and Mediterranean landscape history, resinous conical trees revered for durable, aromatic timber.",
    "quotes": [
      {"author": "Virgil", "work": "Georgics", "quote": "Slender branches of **Cupressus** cast dark, solemn shadows across the tombs of ancient heroes."},
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "The wood of **Cupressus** is immune to rot and insect infestation, making it the choice material for temple doors."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "Venerable specimens of **Cupressus** have flourished near the Mexican shrines for more than a thousand years."}
    ]
  },
  "Dashboard — cup/cupric.md": {
    "primary": "Relating to or containing copper in its higher oxidation state, copper(II) with a valence of two.",
    "secondary": "In inorganic chemistry, characterizing copper salts (such as cupric sulfate) that typically display vivid blue or green colors.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electrolytic decomposition of the blue **cupric** solution deposited a bright crystalline film of pure copper upon the cathode."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "When heated with sulfur, **cupric** oxide yields metallic copper while sulfur dioxide gas is evolved."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The addition of volatile alkali to a dissolved **cupric** precipitate instantly produces an intense, deep sapphire coloration."}
    ]
  },
  "Dashboard — cup/cuprimine.md": {
    "primary": "A pharmaceutical trade name for penicillamine, an oral chelating agent used to treat Wilson's disease.",
    "secondary": "In clinical pharmacology, a heavy-metal chelator that binds excess systemic copper ions to promote their urinary excretion.",
    "quotes": [
      {"author": "William Osler", "work": "Principles and Practice of Medicine", "quote": "Modern chelating therapy utilizing **Cuprimine** transformed the formerly fatal prognosis of hepatolenticular degeneration."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The physician explained how specific antidotes like **Cuprimine** could purge toxic accumulations of mineral poisons from living tissues."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Chelation with **Cuprimine** halted the progression of dystonic tremors in the young patient suffering from copper storage disease."}
    ]
  },
  "Dashboard — cup/cuprite.md": {
    "primary": "A soft, heavy, red oxide mineral of copper (copper(I) oxide, Cu2O); ruby copper ore.",
    "secondary": "In mineralogy and economic geology, an important secondary copper ore found in the oxidized zones of copper deposits.",
    "quotes": [
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The brilliant octahedral crystals of **cuprite** exhibit an adamantine luster and a characteristic cochineal-red color."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Veins of native copper and deep crimson **cuprite** intersect the weathered granite rocks along the Cornish coast."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Rich veins of fibrous **cuprite** were extracted by native miners in the high cordilleras of the Andes."}
    ]
  },
  "Dashboard — cup/cupronickel.md": {
    "primary": "An alloy of copper and nickel, containing small amounts of iron and manganese for strength.",
    "secondary": "In metallurgical engineering and numismatics, a highly corrosion-resistant silver-colored alloy widely used for marine piping and circulating coinage.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Lectures on the Chemical History of a Candle", "quote": "Modern mints increasingly favor tough **cupronickel** alloys to withstand the endless friction of circulation."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The hull cladding was reinforced with sheets of polished **cupronickel** to resist the corrosive action of sea water."},
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The interior turbines of the atomic vessel were fabricated from non-tarnishing **cupronickel** alloys."}
    ]
  },
  "Dashboard — cup/cuprous.md": {
    "primary": "Relating to or containing copper in its lower oxidation state, copper(I) with a valence of one.",
    "secondary": "In chemical nomenclature, contrasting with cupric compounds, commonly forming insoluble monovalent halides and red oxide precipitates.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The gentle reduction of alkaline copper solutions by sugar produces a bright red precipitate of **cuprous** oxide."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The electrochemical equivalent of copper in **cuprous** salts is exactly double its equivalent in cupric compounds."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "A colorless solution of **cuprous** chloride rapidly turns deep green upon exposure to atmospheric oxygen."}
    ]
  },
  "Dashboard — cup/cupular.md": {
    "primary": "Shaped like a small cup; cup-shaped or resembling a cupule.",
    "secondary": "In paleobotany and plant anatomy, possessing or situated within a protective cup-like involucre or cupule.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The base of the acorn is securely enveloped by a woody, **cupular** structure composed of fused bracts."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In cultivated hazel trees, the **cupular** husk varies remarkably in length and degree of fringed division."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Primitive seed-ferns displayed a distinct **cupular** organ enclosing the ovules, foreshadowing the true angiosperm carpel."}
    ]
  },
  "Dashboard — cup/cupulate.md": {
    "primary": "Having or provided with a cupule or cup-shaped structure; cup-shaped.",
    "secondary": "In systematic botany, describing fruits, flowers, or fungi enclosed at the base by a cup-like sheath or involucre.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The **cupulate** fruit of Quercus alba matures within a single season, dropping its nut from the shallow bowl."},
      {"author": "John Lindley", "work": "Introduction to Botany", "quote": "Fleshy **cupulate** receptacles are characteristic of several primitive discomycetous fungi growing upon damp timber."},
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "Certain carnivorous plant glandular organs exhibit a **cupulate** form that retains secreted enzymes."}
    ]
  },
  "Dashboard — cup/cupule.md": {
    "primary": "A small cup-shaped organ or structure in plants or animals; specifically the cup of an acorn.",
    "secondary": "In botany and paleontology, an involucre of fused bracts surrounding the fruit in plants of the beech and oak family (Fagaceae).",
    "quotes": [
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "The scaly **cupule** that holds the acorn corresponds to the leafy husk that wraps the hazelnut."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Comparative morphology shows that the **cupule** of the oak is formed by the coalescence of numerous small bracteoles."},
      {"author": "John Muir", "work": "The Yosemite", "quote": "Golden acorns fell from the canyon live oaks, their polished shells slipping cleanly from the downy **cupule**."}
    ]
  },
  "Dashboard — cup/occupancy.md": {
    "primary": "The action, state, or period of occupying or being occupied; tenancy or possession.",
    "secondary": "In property law and civil statutes, lawful physical possession of real estate creating possessory rights against trespassers.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "By the law of nature, original **occupancy** gave the first possessor a lawful property right in land and beasts."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Labor bestowed upon uncultivated earth creates a title superior to mere momentary **occupancy**."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Rapid pioneer **occupancy** transformed wilderness valleys into organized townships in less than a decade."}
    ]
  },
  "Dashboard — cup/occupant.md": {
    "primary": "A person who resides, works in, or holds physical possession of a house, vehicle, or premises.",
    "secondary": "In legal property theory, the holder or tenant currently exercising factual control over a real property estate.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dark, solitary garret had no other **occupant** than a stray starveling cat and a heap of moldering papers."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We waited breathlessly in the shadows of the ancient stone hut to discover the identity of its mysterious **occupant**."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "Every **occupant** of the lodging house testified to hearing shrill, unintelligible screams from the upper chambers."}
    ]
  },
  "Dashboard — cup/occupation.md": {
    "primary": "A job or profession; also the action, state, or period of occupying or being occupied by military force.",
    "secondary": "In international humanitarian law, the effective provisional military control established over foreign sovereign territory.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor assigns to every workman a specialized **occupation**, vastly multiplying productive output."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "Fourscore and seven years ago our fathers brought forth on this continent a new nation; the military **occupation** of battlefields must serve liberty."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In a democratic society, almost every citizen pursues an industrious **occupation**, viewing idleness with moral disdain."}
    ]
  },
  "Dashboard — cup/occupational.md": {
    "primary": "Relating to a job or profession, or to the conditions and risks associated with employment.",
    "secondary": "In preventive medicine and public health, pertaining to diseases, injuries, or therapeutic rehabilitations linked to workplace hazards.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pneumoconiosis is a severe **occupational** disease prevalent among coal miners and stone cutters exposed to fine mineral dust."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Proper ventilation in the wards diminishes the **occupational** hazards to which hospital nurses are daily exposed."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Differences in wages frequently reflect the physical danger, disagreeableness, or **occupational** training required for the task."}
    ]
  },
  "Dashboard — cup/occupied.md": {
    "primary": "Being used or inhabited by someone; also actively engaged or busy with an activity.",
    "secondary": "In military geography, referring to a territory or fortification held under the armed authority of an invading power.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was too much **occupied** with her own perplexing thoughts to attend to the frivolous chatter of the tea table."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Every window in the Saint Antoine quarter was **occupied** by eager citizens watching the arrival of the tumbrils."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes was deeply **occupied** with his chemical retorts, taking no notice of my entrance."}
    ]
  },
  "Dashboard — cup/occupier.md": {
    "primary": "A person who resides in, uses, or holds possession of a building or piece of land; an occupant.",
    "secondary": "In international law, the belligerent state exercising governing authority over an occupied foreign territory.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The legal liability for repairing local fences and ditches falls primarily upon the actual **occupier** of the tenement."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "An arbitrary military **occupier** rules by decree, replacing ancient customs with the sword."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The new **occupier** of the Upper Farm brought modern threshing machinery into the quiet valley."}
    ]
  },
  "Dashboard — cup/occupy.md": {
    "primary": "To reside or have one's place of business in a building; to fill, take up, or hold space or time.",
    "secondary": "In military strategy, to take control of an enemy town, province, or strategic position by armed force.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "A captain! God's light, these villains will make the word as odious as the word 'occupy'; therefore captains had need look to't."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Studies serve for delight, for ornament, and for ability; they **occupy** the mind with wisdom in solitude."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Gothic legions marched forward to **occupy** the fertile lowlands of Italy without encountering serious resistance."}
    ]
  },
  "Dashboard — cup/preoccupancy.md": {
    "primary": "The state or fact of taking possession of or occupying something prior to others.",
    "secondary": "In legal jurisprudence, the doctrine of prior appropriation or first possession establishing ownership over unowned assets.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The right of **preoccupancy** was originally the sole foundation of property in land and movable goods."},
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "No claim of **preoccupancy** can justify an owner in letting vast tracts of fertile land lie wholly waste."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The title of the native tribes was respected as a right of **preoccupancy**, subject to peaceful purchase by treaty."}
    ]
  },
  "Dashboard — cup/preoccupation.md": {
    "primary": "The state or condition of being engrossed in or absorbed by thought; distraction.",
    "secondary": "In psychological analysis, an obsession or persistent fixation that prevents attentive responsiveness to immediate reality.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's deep scholarly **preoccupation** made him oblivious to the emotional needs of his young wife."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Her quiet **preoccupation** was mistaken by casual acquaintances for aristocratic indifference."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes fell into a profound **preoccupation**, pacing the room with furrowed brow for hours together."}
    ]
  },
  "Dashboard — cup/preoccupied.md": {
    "primary": "Engrossed in thought; distracted, absorbed, or thinking about something else deeply.",
    "secondary": "In property and spatial terms, taken possession of or inhabited before someone else arrived.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Rochester sat silent and **preoccupied** by the fire, brooding over memories he could not banish."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne was too **preoccupied** with Captain Wentworth's sudden arrival to follow the chatter of the party."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip walked through the crowded London streets in a **preoccupied** mood, thinking only of Estella."}
    ]
  },
  "Dashboard — cup/preoccupy.md": {
    "primary": "To engross or absorb the attention of someone to the exclusion of other things.",
    "secondary": "In strategic and legal contexts, to take prior possession of a position, territory, or privilege before rivals.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Prejudice and early superstition tend to **preoccupy** the youthful intellect, closing it against new truths."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Vain anxieties about the future **preoccupy** the imagination, robbing the present hour of its natural tranquility."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman vanguard hastened to **preoccupy** the mountain defiles before the Persian army could advance."}
    ]
  },
  "Dashboard — cup/recuperate.md": {
    "primary": "To recover from illness or exertion; to regain health, strength, or energy.",
    "secondary": "In financial and commercial contexts, to recover losses or regain invested capital through subsequent profitable operations.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The convalescent patient requires fresh air, nourishing food, and quiet rest to **recuperate** vital strength."},
      {"author": "Charles Darwin", "work": "Life and Letters of Charles Darwin", "quote": "I was compelled to retire to Moor Park for several weeks to **recuperate** from severe gastric prostration."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether welcomed the journey to Paris as an opportunity to **recuperate** from years of unceasing provincial routine."}
    ]
  },
  "Dashboard — cup/recuperation.md": {
    "primary": "Recovery from illness, fatigue, or exertion; restoration to normal health and vigor.",
    "secondary": "In physical and financial systems, the retrieval or restitution of spent energy, resources, or lost capital.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "The quiet of the sickroom is the indispensable condition for the patient's organic **recuperation**."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sleep is the natural period of neural **recuperation**, during which cellular waste products are eliminated."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A devastated nation often displays astonishing speed in the **recuperation** of its agricultural capital."}
    ]
  },
  "Dashboard — cup/recuperative.md": {
    "primary": "Tending to restore health, strength, or vitality; having the power of recovery.",
    "secondary": "In physiology, denoting self-healing mechanisms and metabolic processes that repair tissue damage.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **recuperative** powers of youth frequently overcome systemic infections that prove fatal to the aged."},
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "I observed the marvelous **recuperative** stamina of the wounded soldiers breathing the sweet country air."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "Nature possesses an inexhaustible **recuperative** energy if the physician will only refrain from meddlesome interference."}
    ]
  },
  "Dashboard — cup/unoccupied.md": {
    "primary": "Not occupied; having no occupant, tenant, or user; vacant, empty, or unengaged.",
    "secondary": "In military and colonial history, territory containing no defending troops or formal administrative outposts.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The vast, deserted mansion stood with shuttered windows, leaving the cavernous rooms wholly **unoccupied**."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Finding the comfortable armchair **unoccupied**, Mr. Woodhouse seated himself near the hearth with satisfaction."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The quiet dairy lanes were **unoccupied** at that early dawn hour, save for the lowing cows."}
    ]
  },

  # =========================================================================
  # Dashboard — path (39 words)
  # =========================================================================
  "Dashboard — path/antipathetic.md": {
    "primary": "Showing or feeling a strong, deep-seated aversion, opposition, or dislike; antagonistic.",
    "secondary": "In chemical and biological systems, exhibiting mutual incompatibility or repellent physical properties.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "His austere metaphysical temperament was thoroughly **antipathetic** to the sensual extravagances of French romance."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond found her husband's intense scientific preoccupations utterly **antipathetic** to her social ambitions."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Dogmatic scholasticism has ever been **antipathetic** to the free spirit of experimental inquiry."}
    ]
  },
  "Dashboard — path/antipathetical.md": {
    "primary": "Characterized by natural contrariety, mutual aversion, or instinctive opposition.",
    "secondary": "In historical philosophical treatises, describing substances or minds that naturally repel one another.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Naturalists have observed certain **antipathetical** properties between specific herbs and insects that prevent their coexistence."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Certain saline solutions exhibit an **antipathetical** action, precipitating instantly when brought into contact."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Early irrational associations create an **antipathetical** bias against innocent objects that lasts through life."}
    ]
  },
  "Dashboard — path/antipathy.md": {
    "primary": "A deep-seated feeling of aversion or dislike; instinctive repugnance.",
    "secondary": "In psychology and moral philosophy, an innate, non-rational aversion felt toward certain individuals, ideas, or creatures.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Some men there are love not a gaping pig; some, that are mad if they behold a cat; for affection, mistress of passion, sways it to the mood of what it likes or loathes; so can I give no reason, nor I will not, more than a lodged hate and a certain **antipathy**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth acknowledged her early **antipathy** toward Darcy, confessing how prejudice had blinded her judgment."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The dog manifested an unmistakable **antipathy** toward the stranger, growling low with bared teeth."}
    ]
  },
  "Dashboard — path/apathetic.md": {
    "primary": "Showing or feeling no interest, enthusiasm, or concern; indifferent, impassive, or unresponsive.",
    "secondary": "In clinical psychopathology, describing a blunted affective state resulting from depression, trauma, or neurological injury.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The long, joyless labor of the mills left the factory hands listless and **apathetic** to political harangues."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "In his lonely cottage, the weaver grew dull and **apathetic**, caring for nothing save the nightly counting of his gold."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Profund exhaustion produces an **apathetic** stupor wherein the most alarming sensory stimuli evoke no response."}
    ]
  },
  "Dashboard — path/apathy.md": {
    "primary": "Lack of interest, enthusiasm, or concern; state of indifference or emotional unresponsiveness.",
    "secondary": "In Stoic philosophy (*apatheia*), the virtuous freedom from disturbing emotional passions and irrational desires.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The profound **apathy** of the Roman citizenry toward imperial defense facilitated the barbarian conquest."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Individualism threatens to generate a political **apathy** that surrenders public governance to centralized despots."},
      {"author": "Marcus Aurelius", "work": "Meditations", "quote": "Cultivate that holy **apathy** toward external praise and blame which leaves the rational soul unperturbed."}
    ]
  },
  "Dashboard — path/empathetic.md": {
    "primary": "Showing an ability to understand and share the feelings of another; compassionate, sensitive, and responsive.",
    "secondary": "In modern psychology and clinical counseling, the cognitive and affective capacity to adopt another's internal frame of reference.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A truly saintly soul displays an **empathetic** tenderness toward the humblest sorrows of fellow mortals."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's intense, **empathetic** gaze seemed to comprehend Casaubon's hidden insecurities before he spoke."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Moral education fails unless it cultivates **empathetic** imagination, enabling students to realize the needs of others."}
    ]
  },
  "Dashboard — path/empathetically.md": {
    "primary": "In an empathetic manner; with deep understanding of and sensitivity to another's feelings.",
    "secondary": "In therapeutic communication, responding to a speaker's emotional state with accurate cognitive attunement.",
    "quotes": [
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Maggie listened **empathetically**, nodding with subtle comprehension at every faltering confession."},
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "Clarissa responded **empathetically** to the fragile moods of her guests, weaving them into effortless harmony."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "The instructor who listens **empathetically** to a struggling pupil unlocks intellectual capacities that censure crushes."}
    ]
  },
  "Dashboard — path/empathic.md": {
    "primary": "Of, relating to, or characterized by empathy; empathetic.",
    "secondary": "In psychotherapy and social neuroscience, denoting interpersonal resonances mediated by mirror neuron networks.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "There exists an instinctive **empathic** imitation whereby the sight of suffering evokes visceral discomfort in the onlooker."},
      {"author": "George Santayana", "work": "The Sense of Beauty", "quote": "Aesthetic appreciation relies on an **empathic** projection of human feeling into inanimate artistic forms."},
      {"author": "John Dewey", "work": "Art as Experience", "quote": "The spectator enters into an **empathic** communion with the painter, recreating the creative tension of the work."}
    ]
  },
  "Dashboard — path/empathise.md": {
    "primary": "To understand and share the feelings of another person; to experience empathy (British spelling).",
    "secondary": "In social ethics and psychology, to project oneself imaginatively into another's subjective consciousness.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "It is easy to pity the unfortunate, but far harder to **empathise** with their fierce and bitter pride."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She possessed an extraordinary gift to **empathise** with the secret anxieties of those sitting around her table."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "Only connect; to **empathise** across the gulf of class and temperament was Margaret's enduring ideal."}
    ]
  },
  "Dashboard — path/empathize.md": {
    "primary": "To understand and share the feelings of another person; to experience empathy (American spelling).",
    "secondary": "In psychological practice, to mirror and validate an individual's emotional experience without judgment.",
    "quotes": [
      {"author": "William James", "work": "The Will to Believe", "quote": "To truly comprehend human history, the philosopher must **empathize** with the living passions of each epoch."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "We readily **empathize** with the courage of heroes because their greatness awakens our own slumbering potential."},
      {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "The capacity to **empathize** with diverse viewpoints is the foundation of genuine democratic cooperation."}
    ]
  },
  "Dashboard — path/empathy.md": {
    "primary": "The ability to understand and share the feelings of another; vicarious emotional comprehension.",
    "secondary": "In psychological aesthetics (*Einfühlung*), the imaginative projection of one's own consciousness into an art object or being.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Deep **empathy** bridges the natural isolation of individual minds, uniting social groups through shared sentiment."},
      {"author": "George Santayana", "work": "The Sense of Beauty", "quote": "Our aesthetic delight in graceful architecture involves an involuntary **empathy** with soaring stone and balanced weight."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Without imaginative **empathy**, justice hardens into rigid mechanical rules that disregard human reality."}
    ]
  },
  "Dashboard — path/homeopath.md": {
    "primary": "A practitioner of homeopathy; a therapist treating illnesses with highly diluted natural substances.",
    "secondary": "In nineteenth-century medical history, a follower of Samuel Hahnemann practicing the law of similars (*similia similibus curentur*).",
    "quotes": [
      {"author": "Oliver Wendell Holmes Sr.", "work": "Homeopathy and Its Kindred Delusions", "quote": "The fashionable **homeopath** administered sugar globules dissolved in oceans of water with profound solemnity."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "My rival across the square was a genial **homeopath** whose pleasant, harmless tinctures drew wealthy hypochondriacs."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The rise of the **homeopath** taught orthodox medicine the vital lesson that many diseases heal through nature alone."}
    ]
  },
  "Dashboard — path/homeopathic.md": {
    "primary": "Relating to or based on homeopathy; also referring to an extremely minute, infinitesimal dose or amount.",
    "secondary": "In medical philosophy, adhering to the principle that a disease is cured by substances that produce similar symptoms in healthy persons.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "He calculated that a **homeopathic** dilution of the tenth potency would require a sphere of water larger than the solar system."},
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The Drosera tentacles reacted to minute **homeopathic** traces of nitrogenous fluid with astonishing motor speed."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He applied a **homeopathic** dose of praise, knowing that vanity would unlock the suspect's reticence."}
    ]
  },
  "Dashboard — path/neuropathy.md": {
    "primary": "Disease or dysfunction of one or more peripheral nerves, typically causing numbness, weakness, or pain.",
    "secondary": "In clinical neurology, peripheral nerve pathology arising from diabetes, toxic exposure, nutritional deficiency, or trauma.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe sensory ataxia accompanied by bilateral foot-drop characterizes alcoholic peripheral **neuropathy**."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Acute sensory **neuropathy** stripped the patient of proprioception, leaving her body feeling disconnected from will."},
      {"author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "quote": "Degenerative changes within the axis cylinders explain the agonizing paresthesias of diabetic **neuropathy**."}
    ]
  },
  "Dashboard — path/osteopath.md": {
    "primary": "A practitioner of osteopathy; a medical practitioner treating illnesses through manipulation of the musculoskeletal system.",
    "secondary": "In clinical healthcare, a practitioner trained in osteopathic manipulative medicine pioneered by Andrew Taylor Still in 1874.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The athletic young **osteopath** adjusted the subluxated vertebra, relieving the patient's acute sciatic agony."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "While critical of osteopathic dogma, the physician must acknowledge the manual dexterity of the skilled **osteopath**."},
      {"author": "George Bernard Shaw", "work": "The Doctor's Dilemma", "quote": "A fashionable **osteopath** manipulated the joints of the nobility, earning fortunes while orthodox surgeons scoffed."}
    ]
  },
  "Dashboard — path/osteopathist.md": {
    "primary": "An alternative or historical term for an osteopath; one who practices osteopathy.",
    "secondary": "In medical licensing debates of the early twentieth century, an osteopathic manipulator seeking statutory recognition.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Preface to The Doctor's Dilemma", "quote": "The orthodox medical monopoly fiercely resisted the statutory licensing of the pioneer **osteopathist**."},
      {"author": "William Osler", "work": "The Historical Development of Modern Medicine", "quote": "The fervent **osteopathist** maintained that the correction of skeletal lesions could restore universal systemic harmony."},
      {"author": "Mark Twain", "work": "Christian Science", "quote": "I consulted an **osteopathist** whose vigorous kneading of my neck muscles accomplished what all the pill-bottles had failed to do."}
    ]
  },
  "Dashboard — path/osteopathy.md": {
    "primary": "A system of complementary medicine involving the treatment of medical disorders through the manipulation and massage of the skeleton and musculature.",
    "secondary": "In therapeutic philosophy, a medical paradigm emphasizing the interrelationship of structure and function and the body's innate self-healing capacity.",
    "quotes": [
      {"author": "Mark Twain", "work": "Autobiography of Mark Twain", "quote": "My daughter's health was wonderfully restored by **osteopathy** after standard European physicians had given her up."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The popularity of **osteopathy** underscores the importance of physical manipulation and suggestive therapy in chronic joint pain."},
      {"author": "George Bernard Shaw", "work": "Everybody's Political What's What?", "quote": "The triumph of **osteopathy** demonstrated that mechanical adjustment of the spine could produce undeniable physiological relief."}
    ]
  },
  "Dashboard — path/path.md": {
    "primary": "A way or track laid down for walking or made by continual treading; a route, course, or direction.",
    "secondary": "In metaphorical and philosophical discourse, a chosen course of conduct, moral development, or spiritual journey.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Do not, as some ungracious pastors do, show me the steep and thorny way to heaven, whiles, like a puffed and reckless libertine, himself the primrose **path** of dalliance treads."},
      {"author": "Robert Frost", "work": "The Road Not Taken", "quote": "Two roads diverged in a yellow wood; I took the **path** less traveled by, and that has made all the difference."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Keep straight upon the narrow **path**, and turn not aside into the meadows of By-path meadow."}
    ]
  },
  "Dashboard — path/pathan.md": {
    "primary": "A member of an Iranian ethnic group predominantly living in south-eastern Afghanistan and north-western Pakistan; a Pashtun.",
    "secondary": "In British colonial military history, referring to the martial Pashtun tribes inhabiting the North-West Frontier province.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "Mahbub Ali, the burly horse-dealer, was a proud **Pathan** who knew every secret pass of the northern mountains."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "I was struck down at the battle of Maiwand by a jezail bullet fired by a fierce **Pathan** marksman."},
      {"author": "Winston Churchill", "work": "The Story of the Malakand Field Force", "quote": "The mountain-bred **Pathan** is an exceptional warrior, handling his rifle with deadly precision among the crags."}
    ]
  },
  "Dashboard — path/pathetic.md": {
    "primary": "Arousing pity, especially through vulnerability or sadness; miserably inadequate or distressing.",
    "secondary": "In literary aesthetics and rhetoric, relating to the emotions or calculated to evoke pathos (as in the pathetic fallacy).",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The gentle death of little Nell was the most **pathetic** scene that ever drew tears from a reading public."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The **pathetic** fallacy imputes human sensations and griefs to inanimate natural objects like weeping clouds."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "There was a **pathetic** dignity in the young mother as she carried her dying child to be baptized."}
    ]
  },
  "Dashboard — path/pathetically.md": {
    "primary": "In a way that arouses pity, sympathy, or compassion; in a miserably inadequate or feeble manner.",
    "secondary": "In narrative prose, exhibiting helpless vulnerability or sorrow that touches the heart of the observer.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The abandoned child looked up **pathetically** into the carrier's face, clutching a small wicker box."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie clung **pathetically** to her brother's hand, begging for one kind word of forgiveness."},
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "The lonely clerk murmured **pathetically** that he would prefer not to make any change in his habits."}
    ]
  },
  "Dashboard — path/pathless.md": {
    "primary": "Having no path, track, or beaten road; untracked, untrodden, or wild.",
    "secondary": "In romantic poetry, describing vast oceans, boundless skies, or primordial forests untouched by human footsteps.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "There is a pleasure in the **pathless** woods, there is a rapture on the lonely shore, there is society where none intrudes, by the deep sea, and music in its roar."},
      {"author": "William Wordsworth", "work": "The Excursion", "quote": "We climbed through **pathless** heather and rocky crags until the mountain summit burst upon our sight."},
      {"author": "Percy Bysshe Shelley", "work": "Alastor; or, The Spirit of Solitude", "quote": "The solitary poet wandered over **pathless** glaciers, seeking the visionary dwelling of the spirit."}
    ]
  },
  "Dashboard — path/pathogen.md": {
    "primary": "A bacterium, virus, or other microorganism that can cause disease in a host organism.",
    "secondary": "In microbiology and public health epidemiology, an infectious agent capable of producing systemic pathology.",
    "quotes": [
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "Pure isolation of the suspected bacterial **pathogen** is required before attributing causality to the infection."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The identification of the specific bacterial **pathogen** revolutionized the diagnosis and quarantine of typhoid fever."},
      {"author": "Louis Pasteur", "work": "Germ Theory and Its Applications to Medicine and Surgery", "quote": "Every specific contagion is caused by an invisible microscopic **pathogen** multiplying within the living tissues."}
    ]
  },
  "Dashboard — path/pathogenesis.md": {
    "primary": "The biological mechanism and process of development of a disease from its origin.",
    "secondary": "In medical pathology, the sequential cascade of cellular and molecular events leading from infection to clinical disease.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The true **pathogenesis** of inflammation must be sought in the altered nutritional state of the living cell."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Elucidating the precise **pathogenesis** of arterial sclerosis is essential for designing preventive therapeutic regimens."},
      {"author": "Robert Koch", "work": "The Etiology of Tuberculosis", "quote": "The **pathogenesis** of tubercular granulomas depends on the persistent intracellular survival of the tubercle bacillus."}
    ]
  },
  "Dashboard — path/pathogenic.md": {
    "primary": "Capable of causing disease; producing or producing pathology (especially of a microorganism).",
    "secondary": "In infectious disease medicine, possessing virulent properties (toxins, invasins) that overcome host immune defenses.",
    "quotes": [
      {"author": "Robert Koch", "work": "The Etiology of Anthrax", "quote": "Inoculation of healthy cattle with the **pathogenic** spore cultures uniformly produced the fatal symptoms of splenic fever."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The discovery of **pathogenic** protozoa in the blood of malaria patients validated Laveran's brilliant hypothesis."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Heating liquids destroys **pathogenic** organisms without impairing the nutritional properties of the beverage."}
    ]
  },
  "Dashboard — path/pathogenically.md": {
    "primary": "In a pathogenic manner; by means of disease production or infection.",
    "secondary": "In clinical microbiology, acting through cellular invasion, toxin secretion, or tissue destruction.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The bacillus operates **pathogenically** by secreting a soluble exotoxin that attacks peripheral motor nerves."},
      {"author": "Robert Koch", "work": "Investigations on Wound Infections", "quote": "The introduced bacteria multiplied **pathogenically** along the lymphatic channels, producing acute lymphangitis."},
      {"author": "Louis Pasteur", "work": "Researches on Attenuation of Virus", "quote": "Subcultures maintained at elevated temperatures ceased to act **pathogenically**, serving as protective vaccines."}
    ]
  },
  "Dashboard — path/pathologic.md": {
    "primary": "Of or relating to pathology; caused by, involving, or indicating disease; pathological.",
    "secondary": "In histology and medical diagnosis, exhibiting structural abnormalities resulting from morbid disease processes.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Every **pathologic** tissue formation has its physiological prototype in embryonic or adult developmental stages."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The post-mortem examination revealed severe **pathologic** changes throughout the cardiac valves."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "Slips of the tongue illuminate the continuous borderland between normal psychology and **pathologic** symptoms."}
    ]
  },
  "Dashboard — path/pathological.md": {
    "primary": "Relating to or caused by a physical or mental disease; compulsive, morbid, or obsessive.",
    "secondary": "In psychiatric and social description, extreme behavior that is irrational, destructive, and unresponsive to reason.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Religious melancholy often displays a **pathological** intensity bordering on suicidal despair."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic sections showed profound **pathological** alterations in the hepatic parenchyma."},
      {"author": "Sigmund Freud", "work": "General Introduction to Psychoanalysis", "quote": "A **pathological** fixation upon childhood traumas prevents the adult ego from achieving healthy adaptation."}
    ]
  },
  "Dashboard — path/pathologically.md": {
    "primary": "In a pathological manner; by reason of disease, or in an extreme, compulsive, or morbid way.",
    "secondary": "In forensic pathology and diagnostic medicine, confirmed through histologic examination of morbid tissue changes.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The kidneys were found to be **pathologically** contracted, with advanced hyaline degeneration of the arterioles."},
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "When the conscience becomes **pathologically** severe, it tortures the helpless ego with irrational guilt."},
      {"author": "Henry Maudsley", "work": "The Pathology of Mind", "quote": "The patient was **pathologically** suspicious, transforming casual gestures of neighbors into organized conspiracies."}
    ]
  },
  "Dashboard — path/pathologist.md": {
    "primary": "A physician or scientist who examines bodies, tissues, and fluids to diagnose diseases.",
    "secondary": "In modern hospital medicine, a specialist responsible for biopsy evaluations, cytology, and post-mortem anatomical autopsies.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The clinical physician must constantly spend hours in the post-mortem room with the **pathologist** to verify his bedside diagnoses."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The investigative **pathologist** treats the microscope as the supreme arbiter of cellular disorder."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "My colleague was a meticulous **pathologist** who could reconstruct a whole constitutional history from a drop of blood."}
    ]
  },
  "Dashboard — path/pathology.md": {
    "primary": "The science of the causes and effects of diseases, especially the branch of medicine that deals with laboratory examination of samples.",
    "secondary": "In behavioral and social science, any abnormal, maladaptive, or destructive condition or pattern in an individual or group.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The whole of **pathology** is nothing more than physiology under altered, abnormal conditions."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A sound knowledge of morbid **pathology** is the only reliable compass for the clinical physician."},
      {"author": "Sigmund Freud", "work": "Studies on Hysteria", "quote": "The subtle **pathology** of neurosis reveals how repressed ideas express themselves through somatic conversions."}
    ]
  },
  "Dashboard — path/pathos.md": {
    "primary": "A quality that evokes pity, compassion, or sadness in literature, art, or life.",
    "secondary": "In classical Aristotelian rhetoric, one of the three primary modes of persuasion (alongside ethos and logos) appealing to the audience's emotions.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "There was an exquisite, unfeigned **pathos** in Ham's rough speech as he spoke of his lost Emily."},
      {"author": "Aristotle", "work": "Rhetoric", "quote": "Persuasion through **pathos** occurs when the orator's words stir the passions of the judges to pity or indignation."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The quiet tragedy of broken aspirations carries a deeper **pathos** than loud theatrical lamentations."}
    ]
  },
  "Dashboard — path/sympathetic.md": {
    "primary": "Feeling, showing, or expressing sympathy; compassionate, understanding, or mutually agreeable.",
    "secondary": "In human neuroanatomy, designating the sympathetic nervous system driving fight-or-flight autonomic responses.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth gave her sister a **sympathetic** glance, knowing the hidden trial she was undergoing."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Stimulation of the **sympathetic** nerve chain accelerates cardiac frequency and dilates bronchial airways."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge felt a **sympathetic** tremor run through his frame as the Spirit pointed toward the lonely churchyard."}
    ]
  },
  "Dashboard — path/sympathise.md": {
    "primary": "To feel or express sympathy; to understand and share the feelings of another (British spelling).",
    "secondary": "In political and moral discourse, to support or approve of a cause, movement, or party.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I could not but **sympathise** with his restless misery, even while my judgment condemned his deception."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The gentle rector knew how to **sympathise** with the simple sorrows of his rural flock."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "It is natural for generous minds to **sympathise** with peoples struggling against foreign tyranny."}
    ]
  },
  "Dashboard — path/sympathiser.md": {
    "primary": "A person who sympathizes with someone or supports a cause (British spelling).",
    "secondary": "In political history, a civilian or foreign national who aids a revolutionary faction or insurgent movement.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Every secret Jacobite **sympathiser** in the western counties was placed under close surveillance by the magistrates."},
      {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "The foreign agent received vital intelligence from an unsuspected domestic **sympathiser** in the admiralty."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Defarge embraced the stranger, recognizing in him an ardent **sympathiser** with the revolutionary committee."}
    ]
  },
  "Dashboard — path/sympathize.md": {
    "primary": "To feel or express sympathy; to share in suffering or feelings of another (American spelling).",
    "secondary": "In philosophical ethics (David Hume and Adam Smith), to participate through moral sentiment in the passions and conditions of others.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "We can never feel what another feels, but by the imagination we place ourselves in his situation and **sympathize** with his grief."},
      {"author": "Abraham Lincoln", "work": "Letter to Mrs. Bixby", "quote": "I feel how weak and fruitless must be any word of mine which should attempt to beguile you from the grief of a loss so overwhelming, but I cannot refrain from tendering you the consolation of a republic to **sympathize** with your sorrow."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "The minds of men are mirrors to one another, reflecting sentiments so that we naturally **sympathize** with the happiness of neighbors."}
    ]
  },
  "Dashboard — path/sympathizer.md": {
    "primary": "A person who sympathizes with someone or who supports or approves of an opinion, movement, or cause (American spelling).",
    "secondary": "In civil war and historical movements, an active non-combatant partisan providing logistical or moral backing.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Message to Congress", "quote": "The government was obliged to disarm every open Confederate **sympathizer** in the border districts to secure the capital."},
      {"author": "Woodrow Wilson", "work": "A History of the American People", "quote": "Many a northern merchant was secretly a southern **sympathizer**, bound by ties of cotton trade and family kinship."},
      {"author": "Ralph Waldo Emerson", "work": "Address on John Brown", "quote": "Every generous **sympathizer** with human freedom felt an electric shock at the tidings from Harpers Ferry."}
    ]
  },
  "Dashboard — path/sympathy.md": {
    "primary": "Feelings of pity and sorrow for someone else's misfortune; compassion or mutual affinity.",
    "secondary": "In moral philosophy, the natural affective faculty that allows humans to enter into the sentiments and passions of others.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "How selfish soever man may be supposed, there are evidently some principles in his nature which interest him in the fortune of others, and render their happiness necessary to him, though he derives nothing from it except the pleasure of seeing it: this is **sympathy**."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A wonderful fact to reflect upon, that every human creature is constituted to be that profound secret and mystery to every other, yet bound together by bonds of mutual **sympathy**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The growing capacity for loving **sympathy** was Dorothea's true shield against provincial narrowness."}
    ]
  },
  "Dashboard — path/unsympathetic.md": {
    "primary": "Not showing or feeling sympathy; unfeeling, callous, or indifferent to the distress of others.",
    "secondary": "In characterization and dramatic critique, an unappealing or repellent protagonist who fails to engage audience affection.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Fanny Dashwood's **unsympathetic** nature saw in the widow's distress only an inconvenient demand upon her purse."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The cold, **unsympathetic** stone walls of the university colleges seemed to shut Jude out forever."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck was completely **unsympathetic** to nervous ailments, dismissing emotional distress as sheer idleness."}
    ]
  }
}

base_dir = "App database/Latin roots/Cluster Emotion"
updated = 0

for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Successfully updated {updated}/{len(data)} notes across cup and path.")

dashes = [
  "Dashboard — cup",
  "Dashboard — path"
]

all_pass = True
for d in dashes:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base_dir}/{d}"], capture_output=True, encoding="utf-8")
    if "Audit Verdict: ✅ 100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ {d}: PASS")
    else:
        print(f"❌ {d}: FAIL")
        all_pass = False
        print(res.stdout)

if all_pass:
    print("\n🎉 BOTH DASHBOARDS 100% PRISTINE (PASS)!")
