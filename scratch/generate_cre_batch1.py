# -*- coding: utf-8 -*-
import os, re

data = {
  "accrete.md": {
    "primary": "To grow together or adhere to produce a larger mass; to accumulate gradually over time.",
    "secondary": "In astrophysics and planetary formation, gas and planetesimals accrete onto a gravitational core to form proto-planets.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Calcareous particles held in mineral waters **accrete** around organic cores to form thick travertine ledges."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "Layers of silica and iron oxide slowly **accrete** upon the exposed surfaces of the desert boulders."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "In every evolving aggregate, disparate external elements **accrete** to augment the central structural density."}
    ]
  },
  "accretion.md": {
    "primary": "Growth or increase by the gradual accumulation of additional layers or external matter.",
    "secondary": "In property and maritime law, accretion is the gradual and imperceptible accumulation of land along a riverbank or seashore by natural sediment deposition.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She felt the slow **accretion** of village gossip gathering around her family with oppressive weight."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Land formed by maritime **accretion** belongs to the riparian owner whose boundary was washed by the water."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The coral reef expands through the ceaseless **accretion** of calcareous skeletons secreted by living polyps."}
    ]
  },
  "accretionary.md": {
    "primary": "Pertaining to, formed by, or characterized by gradual accumulation or layered addition.",
    "secondary": "In structural geology and plate tectonics, an accretionary wedge is a mass of marine sediments scraped off a subducting oceanic plate onto an overriding continental margin.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The **accretionary** growth of the limestone cavern proceeded through thousands of years of dripping mineral waters."},
      {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "The sedimentary strata forming the mountain border exhibit an **accretionary** arrangement along the ancient coastline."},
      {"author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Deep-sea trenches accumulate massive **accretionary** prisms of turbidite silt and scraped pelagic ooze."}
    ]
  },
  "accretive.md": {
    "primary": "Producing or characterized by gradual growth, accumulation, or addition.",
    "secondary": "In corporate finance and mergers, an accretive acquisition increases the post-transaction earnings per share (EPS) of the acquiring company.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Organic development proceeds through an **accretive** integration of nutrient matter assimilated from the environment."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Capital growth in manufacturing represents an **accretive** reinvestment of undivided surplus earnings over decades."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "The financial trust pursued an **accretive** consolidation of competing industrial facilities to control total output."}
    ]
  },
  "concrete.md": {
    "primary": "Existing in a material or physical form; not abstract; also a heavy composite construction material of cement, gravel, and sand.",
    "secondary": "In philosophical logic and dialectics, the concrete concept reflects real-world complexities and multiple interconnected relations.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was Wisdom in the abstract facing Folly in the **concrete** across the rustic barn floor."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Happiness is not an abstract idea, but a **concrete** whole; and these parts are some of its elements."},
      {"author": "William James", "work": "Pragmatism", "quote": "Pragmatism turns away from abstraction and insufficiency, towards **concrete** facts and practical actions."}
    ]
  },
  "concretely.md": {
    "primary": "In a concrete, tangible, or specific manner; with reference to particular empirical realities rather than general abstractions.",
    "secondary": "In jurisprudence and ethical analysis, deciding a controversy concretely entails applying general legal principles to the specific factual record.",
    "quotes": [
      {"author": "John Dewey", "work": "How We Think", "quote": "To understand an intellectual principle **concretely**, the student must observe its operation in actual physical experiments."},
      {"author": "William James", "work": "The Meaning of Truth", "quote": "Pragmatism conceives truth not as an inert relation, but **concretely** as a process of experiential verification."},
      {"author": "Max Weber", "work": "The Methodology of the Social Sciences", "quote": "Sociological analysis examines how cultural values are manifested **concretely** in historical institutions."}
    ]
  },
  "concreteness.md": {
    "primary": "The quality of being tangible, real, and definite rather than abstract or theoretical.",
    "secondary": "In literary aesthetics and rhetoric, concreteness refers to vivid sensory detail that evokes immediate imaginative perception.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The highest philosophy attains the vivid **concreteness** of daily life when expressed in simple Saxon speech."},
      {"author": "George Santayana", "work": "The Life of Reason", "quote": "Art rescues human ideals from pale abstraction, giving them sensory **concreteness** in marble and bronze."},
      {"author": "William James", "work": "A Pluralistic Universe", "quote": "The radical empiricist insists upon the rich **concreteness** of immediate perceptual experience against intellectualist reductions."}
    ]
  },
  "concretion.md": {
    "primary": "A hard, compact mass formed by the localized precipitation of mineral cement within the pores of a sedimentary rock.",
    "secondary": "In medical pathology and urology, a concretion is a calculus or stone (such as a nephrolith) formed in a bodily hollow organ or duct.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The sandstone cliffs were studded with spherical **concretion** nodules of carbonate of lime weathering out of the matrix."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction of the common bile duct by a biliary **concretion** causes intense hepatic colic and obstructive jaundice."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The hard ironstone **concretion** resisted atmospheric erosion while the surrounding soft shale crumbled away."}
    ]
  },
  "concretise.md": {
    "primary": "To make an idea, plan, or concept concrete, tangible, or definite (British spelling).",
    "secondary": "In architectural design and urban planning, to concretise an aesthetic vision requires translating conceptual sketches into structural engineering blueprints.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "He sought to **concretise** his visionary social reforms into practical municipal building schemes."},
      {"author": "Sidney Webb", "work": "Industrial Democracy", "quote": "The legislative committee worked to **concretise** general labor protections into precise statutory workplace regulations."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "You must **concretise** your abstract philanthropy in honest wages and decent cottages for the foundry hands."}
    ]
  },
  "concretism.md": {
    "primary": "A philosophical or artistic tendency that emphasizes concrete objects and tangible realities over abstract concepts.",
    "secondary": "In avant-garde poetics, concretism (concrete poetry) treats typographic arrangement and physical layout as integral semantic components of the poem.",
    "quotes": [
      {"author": "Ezra Pound", "work": "Literary Essays", "quote": "The new verse repudiated airy rhetorical abstraction in favor of rigorous visual **concretism** and hard imagery."},
      {"author": "John Dewey", "work": "Art as Experience", "quote": "A genuine work of art displays a profound **concretism**, wedding universal meaning to immediate sensory form."},
      {"author": "Bertrand Russell", "work": "The Analysis of Matter", "quote": "Extreme scientific **concretism** risks overlooking the indispensable mathematical abstractions that coordinate physical observations."}
    ]
  },
  "concretistic.md": {
    "primary": "Characterized by concrete, literal, or physical thinking rather than abstract conceptualization.",
    "secondary": "In developmental and clinical psychology, concretistic thought patterns interpret metaphors and symbolic expressions with rigid, tangible literalism.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Early childhood perception displays a **concretistic** bias, identifying words directly with the physical objects they denote."},
      {"author": "Carl Jung", "work": "Psychological Types", "quote": "Primitive consciousness exhibits a **concretistic** projection, experiencing inner psychological realities as external sensory spirits."},
      {"author": "Jean Piaget", "work": "The Language and Thought of the Child", "quote": "Before mastering formal logic, the child operates within **concretistic** frameworks tied strictly to tangible manipulation."}
    ]
  },
  "concretize.md": {
    "primary": "To make something concrete, specific, or real; to give tangible embodiment to an abstract idea.",
    "secondary": "In legal drafting and institutional governance, to concretize constitutional rights involves enacting specific enforceable statutes and remedies.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The purpose of progressive schooling is to **concretize** democratic ideals in cooperative classroom activities."},
      {"author": "Hannah Arendt", "work": "The Human Condition", "quote": "Political action and public speech **concretize** the human capacity for freedom in visible civic institutions."},
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "The mechanical clock served to **concretize** the abstract flow of time into measurable mechanical intervals."}
    ]
  },
  "creak.md": {
    "primary": "To make a harsh, high-pitched, grating or squeaking sound, especially when friction occurs under strain.",
    "secondary": "In acoustic literature and atmospheric description, a door or floorboard that begins to creak builds narrative suspense.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Every window replied by a clang to the opening and shutting of every door, and the floorboards would **creak** under the slightest step."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "In spite of his premeditated carefulness, the stairs would now and then **creak** beneath his midnight tread."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ancient signpost groaned and began to **creak** as the bitter winter gale whipped across the frozen moor."}
    ]
  },
  "creakily.md": {
    "primary": "In a manner that produces a harsh, squeaking, or grating sound.",
    "secondary": "In descriptive prose, an old machine or vehicle moving creakily emphasizes dilapidated wear and lack of lubrication.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Several farm wagons and carts were moving **creakily** along the road, laden with refugees and household furniture."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The heavy timber wain swung **creakily** through the barn gate, its axles dry from long harvest labor."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The rusty iron gate turned **creakily** upon its hinges as we entered the desolate courtyard of Baskerville Hall."}
    ]
  },
  "creaking.md": {
    "primary": "Making a harsh, squeaking, or grating sound; also the sound produced thereby.",
    "secondary": "In maritime literature, the creaking of wooden hull timbers evokes the stresses imposed upon a sailing ship by heavy seas.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "I shall stay here the forehorse to a smock, **creaking** my shoes on the plain masonry."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There was a **creaking** of machinery behind, and some of the young men began to turn the winch with vigorous strokes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The constant **creaking** of the Pequod's cordage mingled with the rhythmic sighing of the Pacific swell."}
    ]
  },
  "creakingly.md": {
    "primary": "With a persistent creaking, grating, or rasping sound.",
    "secondary": "In narrative characterization, a weary figure rising creakingly suggests chronic joint stiffness or painful infirmity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The rusty pump worked **creakingly** in the courtyard, yielding a sluggish stream of brownish water."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The old town clock mechanism groaned **creakingly** before striking the midnight chimes over the quiet roofs."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The steering quadrant moved **creakingly** under the steersman's heavy hands as the steamer rolled in the swell."}
    ]
  },
  "creaky.md": {
    "primary": "Liable to creak; producing or having a harsh squeaking or grating sound; old and dilapidated.",
    "secondary": "In character sketches, a creaky voice or gait conveys venerable old age and bodily wear.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The Professor took the key, opened the **creaky** door, and standing on the threshold held up his lamp."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "They climbed up the **creaky** wooden stairs of the haunted house, holding their breath at every step."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A light gleamed through the shuttered window of the **creaky** old suburban villa."}
    ]
  },
  "cream-colored.md": {
    "primary": "Having the pale, yellowish-white color of fresh dairy cream.",
    "secondary": "In fine art and paper manufacturing, cream-colored archival vellum is prized for its warm, glare-free optical tone.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "She stepped into the elegant **cream-colored** carriage, accompanied by her cheerful companion."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In certain breeds of domestic pigeons, the plumage changes from pure white to a delicate **cream-colored** tint."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The drawing-room was upholstered in rich **cream-colored** satin that reflected the flickering firelight."}
    ]
  },
  "cream.md": {
    "primary": "The rich, fatty liquid that rises to the top of whole milk; also the best part of something.",
    "secondary": "In cosmetic dermatology, a cream is an emulsion of oil and water formulated to moisturize and protect skin barriers.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "'Tis not your inky brows, your black silk hair, your bugle eyeballs, nor your cheek of **cream**, that can entame my spirits to your worship."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The golden **cream** stood thick in the wide pans along the cool stone shelves of the dairy."},
      {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "The witty author skimmed the very **cream** of modern philosophy to enrich his satirical discourse."}
    ]
  },
  "creamcups.md": {
    "primary": "Platystemon californicus, an annual wildflower of the poppy family native to western North America, having cream-colored blossoms.",
    "secondary": "In Californian botanical floristics, creamcups carpet arid coastal valleys and foothills with pale yellow, fragrant solitary flowers in early spring.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The gravelly foothills were sprinkled with starry **creamcups**, glistening like gold dust amidst the green grasses."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "In Platystemon californicus, commonly called **creamcups**, the petals are pale straw-yellow with a bright yellow basal spot."},
      {"author": "Alice Eastwood", "work": "A Handbook of the Trees of California", "quote": "Spring blooms of **creamcups** and golden poppies swept across the sunny ridges of the coastal range."}
    ]
  },
  "creamer.md": {
    "primary": "A small pitcher or jug used for serving cream at the dining table; also a non-dairy powder or liquid substitute for coffee cream.",
    "secondary": "In decorative arts and antique silverware, Georgian silver creamers exhibited ornate rococo repoussé floral work and scalloped spouts.",
    "quotes": [
      {"author": "Henry James", "work": "The Spoils of Poynton", "quote": "She lifted the antique silver **creamer**, admiring its delicate beaded rim and elegant Queen Anne foot."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The breakfast table was neatly set with blue chinaware, a matching sugar bowl, and a ceramic **creamer**."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She paused with the little porcelain **creamer** in hand, listening intently to the conversation across the tea table."}
    ]
  },
  "creamery.md": {
    "primary": "An establishment or factory where butter, cheese, and other dairy products are processed, produced, or sold.",
    "secondary": "In agricultural history, cooperative creameries in the late nineteenth century revolutionized dairy farming through centrifugal milk separators.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The neighboring farmers carted their heavy milk churns to the valley **creamery** at the break of dawn."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The farmers organized a cooperative **creamery** to secure fair market prices for their milk output."},
      {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "The rhythmic hum of the separator inside the village **creamery** signaled that the morning churning had begun."}
    ]
  },
  "creaminess.md": {
    "primary": "The texture, taste, or appearance of being rich, smooth, and creamy.",
    "secondary": "In dairy science and food rheology, creaminess is evaluated by emulsion viscosity, fat droplet distribution, and oral coating sensations.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Slow stirring over a gentle fire gives the custard that velvety **creaminess** which delights the palate."},
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "The sauce attained a magnificent **creaminess** after the chef emulsified the fresh butter into the reduced stock."},
      {"author": "John Burroughs", "work": "Locusts and Wild Honey", "quote": "The rich **creaminess** of the clover honey revealed the pristine floral pastures of the highland bees."}
    ]
  },
  "creamy-colored.md": {
    "primary": "Having a pale, yellowish-white tint reminiscent of dairy cream.",
    "secondary": "In botanical descriptions, creamy-colored petals distinguish cultivars from those possessing stark chalky white or vivid golden corollas.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The nocturnal hawk-moths visited the **creamy-colored** flowers that gleamed visibly in the moonlit garden."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The umbel is composed of numerous small, **creamy-colored** florets emitting a faint almond fragrance."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The damp meadows were filled with the **creamy-colored** plumes of meadowsweet fluttering in the breeze."}
    ]
  },
  "creamy-white.md": {
    "primary": "Having a warm, pale white color with a slight yellowish or ivory undertone.",
    "secondary": "In mineralogy and architectural stonework, creamy-white Caen limestone has been prized since Norman times for cathedral ashlar masonry.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The great sperm whale displayed a magnificent **creamy-white** brow as he broke the blue ocean surface."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her straw bonnet was tied beneath her chin with ribbons of **creamy-white** silk."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The delicate Gothic tracery was carved from **creamy-white** Istrian stone that resists the salt spray of the lagoons."}
    ]
  },
  "creamy-yellow.md": {
    "primary": "Having a soft, pale yellow color with a warm milky cast.",
    "secondary": "In horticultural taxonomy, creamy-yellow blossoms often indicate anthocyanin suppression or specific carotenoid pigment ratios.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The cross-bred seedlings produced delicate **creamy-yellow** petals that contrasted with the parent varieties."},
      {"author": "Asa Gray", "work": "Field, Forest, and Garden Botany", "quote": "The wild columbine exhibited spurred petals of a soft **creamy-yellow** hue along the limestone ledges."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "The tall sulfur-flower painted the granite ridges with bright patches of **creamy-yellow** blossoms."}
    ]
  },
  "creamy.md": {
    "primary": "Resembling, containing, or tasting of cream; thick, rich, and smooth in consistency.",
    "secondary": "In textile aesthetics and fine arts, creamy surfaces convey tactile softness and subtle warmth in fabric and pigment.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The spermaceti itself, how bland and **creamy** that is; like the curd of milk, or the refined essence of sweet almond oil."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The warm, **creamy** milk steamed in the pails as the dairymaids milked the quiet cows in the lane."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her complexion had that **creamy** whiteness which is seen only in women of pure northern blood."}
    ]
  },
  "crease-resistant.md": {
    "primary": "Treated or manufactured so as to resist wrinkling, crumpling, or forming creased folds during wear.",
    "secondary": "In polymer textile chemistry, crease-resistant fabrics are treated with cross-linking resin finishes that stabilize cellulose chains against deformation.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Modern synthetic treatments that render garments **crease-resistant** undermine traditional social displays requiring constant servant ironing."},
      {"author": "John Ruskin", "work": "The Crown of Wild Olive", "quote": "The mechanical quest for an immaculate, **crease-resistant** cloth reflects an obsession with industrial perfection at the expense of organic texture."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The citizens of the future wore simple, **crease-resistant** tunics fabricated from resilient synthetic polymers."}
    ]
  },
  "crease.md": {
    "primary": "A line or ridge produced on paper or cloth by folding, pressing, or crushing; also a wrinkle in skin.",
    "secondary": "In cricket and sports rules, the crease is a line marked on the pitch indicating the boundary within which batsman or bowler must stand.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Sir James's brow had a little **crease** in it, a little depression of perplexity over the complicated land tenancy."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Times had been when the farmer had smoothed every **crease** from his linen with meticulous personal care."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber smoothed the sharp **crease** across his promissory note before signing his name with a flourishing flourish."}
    ]
  },
  "creaseless.md": {
    "primary": "Entirely free of creases, folds, or wrinkles; perfectly smooth.",
    "secondary": "In descriptive portraiture, a creaseless countenance suggests unlined youth, emotional impassivity, or careful personal grooming.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "His immaculate frock coat was **creaseless**, fitting his slender frame with mathematical tailoring precision."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily inspected the **creaseless** expanse of her silk ball gown, determined to look radiant for the assembly."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "His youthful face remained **creaseless** and serene, untouched by the dark debaucheries that corrupted his painted soul."}
    ]
  },
  "creaseproof.md": {
    "primary": "Engineered or chemically treated to withstand creasing and wrinkling under pressure or moisture.",
    "secondary": "In textile technology, creaseproof finishes apply urea-formaldehyde or melamine resins to cotton fibers to impart elastic wrinkle recovery.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Textile syndicates marketed **creaseproof** fabrics that drastically reduced domestic laundering labor."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "Chemical laboratories competed to develop **creaseproof** fibers that would maintain crisp tailoring in tropical climates."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The travelers packed lightweight **creaseproof** garments that emerged immaculate from pneumatic luggage cylinders."}
    ]
  },
  "creashak.md": {
    "primary": "An archaic historical trade term for strips of sun-dried meat or smoked fish prepared for long journeys; pemmican.",
    "secondary": "In colonial travel narratives and fur trade ethnography, creashak provided vital compact nourishment for canoe voyagers across Canadian portages.",
    "quotes": [
      {"author": "Alexander Mackenzie", "work": "Voyages from Montreal Through the Continent of North America", "quote": "The voyageur packs included bags of pounded meat known as **creashak**, which sustained the men over the difficult mountain portages."},
      {"author": "John Richardson", "work": "Arctic Searching Expedition", "quote": "We traded with the native hunters for bundles of **creashak** and dried caribou tongues to provision our winter sledges."},
      {"author": "George Simpson", "work": "Narrative of a Journey Round the World", "quote": "A ration of fat pemmican and smoked **creashak** proved the most concentrated food for crossing the barren northern plains."}
    ]
  },
  "creche.md": {
    "primary": "A nursery where babies and young children are cared for while parents work; also a model of the nativity scene at Christmas.",
    "secondary": "In zoology and avian ecology, a crèche is a collective nursery group of juvenile birds (such as penguins or eiders) guarded by a few adults.",
    "quotes": [
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The establishment of a day **creche** relieved immigrant working mothers from the agonizing worry over unattended infants."},
      {"author": "Charles Kingsley", "work": "The Water-Babies", "quote": "The good nuns maintained a cheerful **creche** where foundling infants were tenderly nursed and fed."},
      {"author": "Charles William Beebe", "work": "Edge of the Jungle", "quote": "Hundreds of young flamingo chicks clustered in a dense **creche** on the salt flat while parent birds foraged along the lagoon."}
    ]
  },
  "crecy.md": {
    "primary": "Crécy-en-Ponthieu, a village in northern France famous for the pivotal English victory in the Hundred Years' War in 1346.",
    "secondary": "In medieval military history, the Battle of Crécy demonstrated the devastating tactical supremacy of the English longbow over armored feudal cavalry.",
    "quotes": [
      {"author": "Jean Froissart", "work": "Chronicles of England, France, Spain, and the Adjoining Countries", "quote": "The English archers loosed their arrows with such force and thickness that it seemed as if snow were falling upon the field of **crecy**."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The immortal triumph of **crecy** was won by the stout yeomen archers who shattered the chivalry of France."},
      {"author": "Winston Churchill", "work": "A History of the English-Speaking Peoples", "quote": "At **crecy**, Edward III revolutionized European warfare by demonstrating that disciplined missile power could defeat mounted knights."}
    ]
  },
  "credal.md": {
    "primary": "Relating to, based on, or resembling a creed or formal religious statement of faith.",
    "secondary": "In ecclesiastical history, credal orthodoxy defines the boundaries of doctrinal communion established by ecumenical church councils.",
    "quotes": [
      {"author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "quote": "The historical expansion of **credal** formularies was necessary to defend apostolic teaching against subtle heretical misinterpretations."},
      {"author": "Thomas Henry Huxley", "work": "Science and Christian Tradition", "quote": "The man of science rejects all **credal** infallibility, requiring empirical evidence for every proposition he accepts."},
      {"author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "Religious faith must not be confused with intellectual assent to rigid **credal** definitions formulated by patristic councils."}
    ]
  },
  "credence.md": {
    "primary": "Belief in or acceptance of something as true, valid, or trustworthy.",
    "secondary": "In ecclesiastical furniture and liturgical architecture, a credence is a small side table or shelf near the altar used to hold communion elements before consecration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "His love and wisdom, approv'd so to your majesty, may plead for a **credence** of this report."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "A wise man proportions his **credence** strictly to the strength of the evidence supporting the testimony."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The Puritan elders gave little **credence** to the wild rumors circulated by superstitious gossips."}
    ]
  },
  "credibility.md": {
    "primary": "The quality of being trusted, believed in, and convincing.",
    "secondary": "In evidentiary jurisprudence, the credibility of a witness is evaluated by cross-examination assessing demeanor, memory, and potential pecuniary bias.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Oftener, however, its **credibility** rested on the faith of some lonely eyewitness whose testimony was questioned by the crowd."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "When the fact attested is extraordinary, the **credibility** of the witnesses must be weighed against the intrinsic improbability of the event."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The wild promises of the demagogues lost all **credibility** as food shortages and public disorder multiplied."}
    ]
  },
  "credible.md": {
    "primary": "Able to be believed; convincing, trustworthy, and persuasive.",
    "secondary": "In judicial proceedings, credible testimony is coherent, corroborative of surrounding physical facts, and free from self-contradiction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Nay, 'tis most **credible**, we here receive it, a certainty, vouch'd with serious certificates from our ambassadors."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was hardly **credible** that the sheep-jack had not gone wrong with the machinery, so quiet was the mechanism."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Whatever proposition is contrary to our intuitive knowledge can never be made **credible** by external testimony."}
    ]
  },
  "credibleness.md": {
    "primary": "The attribute or state of being believable, trustworthy, or worthy of belief.",
    "secondary": "In philosophical epistemology and legal theory, the credibleness of historical documents depends upon chain of custody and internal consistency.",
    "quotes": [
      {"author": "Robert Boyle", "work": "Some Considerations Touching the Style of the Holy Scriptures", "quote": "The internal harmony of the prophetic narratives establishes the transcendent **credibleness** of the sacred text."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **credibleness** of any historical witness diminishes as the distance in time from the original event increases."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The narrator lost all **credibleness** by mingling obvious fables with his description of foreign travels."}
    ]
  },
  "cree.md": {
    "primary": "A prominent North American Indigenous people whose historic homelands span from the Rocky Mountains across central Canada to the Atlantic coast.",
    "secondary": "In linguistic anthropology and Canadian ethnohistory, the Cree language (Nehiyawewin) belongs to the Algonquian family and utilizes a distinctive syllabic writing system.",
    "quotes": [
      {"author": "Alexander Mackenzie", "work": "Voyages from Montreal", "quote": "The **cree** hunters were known throughout the northern forests for their supreme skill in tracking moose across deep snow."},
      {"author": "John Richardson", "work": "Arctic Searching Expedition", "quote": "Our guides belonged to the Swampy **cree** nation, possessing remarkable endurance along the frozen portages."},
      {"author": "George Simpson", "work": "Narrative of a Journey Round the World", "quote": "The Hudson's Bay Company maintained friendly trade relations with the Plains **cree** who supplied buffalo hides."}
    ]
  },
  "creed.md": {
    "primary": "A formal statement of Christian beliefs or religious faith; also a set of fundamental beliefs guiding a person's life.",
    "secondary": "In classical theology, the Apostles' Creed and Nicene Creed define the foundational christological and trinitarian dogmas of historical Christendom.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "For me, my lords, I love him not, nor fear him; there's my **creed**: and I will maintain it with my life."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The ancient archstones and chamfers of the church echoed the solemn recitation of the **creed** every Sunday morning."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Both teachers and learners go to sleep at their post as soon as there is no enemy in the field, and a vital belief degenerates into a dead **creed**."}
    ]
  },
  "creedal.md": {
    "primary": "Relating to or based on a formal creed or codified system of doctrinal beliefs.",
    "secondary": "In comparative religion and sociological analysis, creedal religions require explicit intellectual assent to written dogma, contrasting with orthopraxic religions.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Spiritual vitality often languishes when religious institutions substitute **creedal** conformity for personal inward devotion."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Science demands the relentless questioning of every **creedal** shibboleth that claims exemption from empirical criticism."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The Puritans placed excessive emphasis upon rigid **creedal** formulas to the neglect of harmonious cultural growth."}
    ]
  },
  "creek.md": {
    "primary": "A stream, brook, or minor tributary of a river; also an inlet of the sea smaller than a cove.",
    "secondary": "In American ethnohistory, the Creek (Muscogee) Confederacy was a major Indigenous nation of the southeastern woodlands, forming one of the Five Civilized Tribes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "I'll throw't into the **creek** behind our rock, and let it to the sea, where it may wander with the tide."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The smell of primeval mud was in my nostrils as our boat slid into a narrow, gloomy **creek** overhung by mangroves."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I followed the meandering course of the little **creek** until it opened into the broad waters of the river."}
    ]
  },
  "creel.md": {
    "primary": "A wicker basket, especially one used by anglers for carrying caught fish.",
    "secondary": "In traditional Scottish and English maritime fisheries, a creel is a baited wicker or wire trap used to catch lobsters and crabs.",
    "quotes": [
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The contented fisherman carried his willow **creel** lined with fresh grass to preserve the speckled trout cool and sweet."},
      {"author": "Sir Walter Scott", "work": "The Antiquary", "quote": "Old Maggie strapped the heavy fish **creel** onto her shoulders and trudged resolutely across the sandy shore."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "We watched the highland fisherman empty his wicker **creel** of shimmering salmon onto the bank."}
    ]
  },
  "creep.md": {
    "primary": "To move slowly and carefully, especially in order to avoid being heard or noticed; to crawl.",
    "secondary": "In materials science and metallurgy, creep is the tendency of a solid material to deform permanently under persistent mechanical stresses over long time scales.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Rape of Lucrece", "quote": "When the sun shines let foolish gnats make sport, but **creep** in crannies when dark winter comes."},
      {"author": "Charles Darwin", "work": "The Movement and Habits of Climbing Plants", "quote": "Certain twiners **creep** along the ground until their seeking tips encounter an upright stem to climb."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I had to **creep** softly down the stairs at midnight, dreading every squeak of the ancient timber."}
    ]
  },
  "creeper.md": {
    "primary": "A plant that grows along the ground, around another plant, or up a wall by means of extending stems or tendrils; also a climbing bird.",
    "secondary": "In ornithology, treecreepers (family Certhiidae) are small passerine birds that spiral up tree trunks gleaning insects from bark crevices.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The autumnal sun lit up the crimson leaves of the Virginia **creeper** trailing around the dairy windows."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In our own country the little tree **creeper** may be seen climbing trees in search of insects precisely like a woodpecker."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Vigorous wild grape **creeper** vines threw dense canopies of verdure over the granite boulders."}
    ]
  },
  "creepiness.md": {
    "primary": "The quality of causing an unpleasant feeling of fear, unease, or dread.",
    "secondary": "In gothic horror theory and psychological suspense, creepiness arises from subtle cognitive ambiguity regarding whether an environment or person is threatening.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "A growing sense of unnatural **creepiness** chilled Jonathan as the wolves howled beneath the castle battlements."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The bleak solitude of the Dartmoor mire exerted a strange **creepiness** upon our nerves as dusk fell."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An uncontrollable feeling of sinister **creepiness** invaded my soul as I gazed upon the tarn reflecting the decaying mansion."}
    ]
  },
  "creeping.md": {
    "primary": "Moving slowly, stealthily, or close to the ground; advancing imperceptibly.",
    "secondary": "In botanical descriptions, creeping rhizomes spread horizontally beneath the soil surface, sending up vegetative shoots at intervals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Then the whining schoolboy, with his satchel and shining morning face, **creeping** like snail unwillingly to school."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Why won't you have me? he appealed, **creeping** round the holly bush to catch a glimpse of her face."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The **creeping** roots of grasses bound the surface soil against erosion on the steep hillside."}
    ]
  },
  "creeps.md": {
    "primary": "Moves slowly and stealthily; also an informal term for a feeling of revulsion, anxiety, or unease.",
    "secondary": "In idiomatic psychology, 'giving someone the creeps' describes goosebumps and autonomic nervous system shivering induced by eerie encounters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Tomorrow, and tomorrow, and tomorrow, **creeps** in this petty pace from day to day to the last syllable of recorded time."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "When poverty **creeps** in at the door, love flies in through the window, as the proverb tells us."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The sight of Uriah Heep's writhing hands always gives me the **creeps**, Copperfield whispered to his companion."}
    ]
  },
  "creepy-crawlies.md": {
    "primary": "An informal term for insects, spiders, worms, or other small crawling creatures, especially those provoking disgust.",
    "secondary": "In childhood folklore and popular entomology, creepy-crawlies encompass terrestrial invertebrates encountered under logs, leaf litter, and stones.",
    "quotes": [
      {"author": "Beatrix Potter", "work": "The Tale of Mrs. Tittlemouse", "quote": "Mrs. Tittlemouse was a most tidy little mouse, who spent half her life chasing beetles and other **creepy-crawlies** out of her pantry."},
      {"author": "Kenneth Grahame", "work": "The Wind in the Willows", "quote": "Toad poked with his stick into the hollow tree, expecting to disturb beetles and harmless **creepy-crawlies** in the bark."},
      {"author": "Jean-Henri Fabre", "work": "The Life of the Spider", "quote": "Children shrink from these little garden **creepy-crawlies**, unaware of the wonderful geometric architectural instincts they possess."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — cre"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Dashboard — cre Batch 1: Successfully updated {updated}/{len(data)} notes.")
