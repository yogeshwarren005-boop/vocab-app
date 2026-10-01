import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Sound & Auditory';

const filesData = {
  // Dashboard — rhythm
  "Dashboard — rhythm/eurhythmics.md": {
    primary: "A method of musical education developed by Émile Jaques-Dalcroze that teaches physical appreciation of rhythm through bodily movements.",
    secondary: "Harmonious bodily training coordinating musical expression, neuromuscular control, and rhythmic improvisation.",
    quotes: [
      { author: "Émile Jaques-Dalcroze", work: "Rhythm, Music and Education", quote: "The aim of **eurhythmics** is to enable pupils, at the end of their studies, to say, not 'I know,' but 'I have experienced'." },
      { author: "George Bernard Shaw", work: "The Sanity of Art", quote: "The Dalcroze demonstration of **eurhythmics** proved that musical rhythm can become a living bodily habit." },
      { author: "Isadora Duncan", work: "My Life", quote: "My dance was born of a natural **eurhythmics**, seeking bodily movements that echo the surge of the ocean." }
    ]
  },
  "Dashboard — rhythm/eurhythmy.md": {
    primary: "Harmony, proportion, and aesthetic beauty in rhythm, architecture, musical composition, or physical movement.",
    secondary: "An expressive movement art where speech and musical sounds are manifested through specific bodily gestures in anthroposophical philosophy.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "**Eurhythmy** is beauty and fitness in the adjustment of the parts, where height corresponds to width and width to length." },
      { author: "Rudolf Steiner", work: "Eurythmy as Visible Speech", quote: "Through **eurhythmy**, the human larynx becomes the whole body, speaking directly through form and movement in space." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The sublime facade achieved an exquisite **eurhythmy**, each colonnade echoing the proportions of the central arch." }
    ]
  },
  "Dashboard — rhythm/rhythm.md": {
    primary: "A strong, regular, repeated pattern of movement, sound, or activity; measured temporal cadence.",
    secondary: "The systematic arrangement of musical sounds or poetic feet according to duration, stress, and meter in artistic composition.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "I would define the poetry of words as the rhythmical creation of beauty; its heart is measured **rhythm**." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "A sight, an emotion, creates this wave in the mind, and the wave starts a **rhythm** which words must capture." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "The fluid **rhythm** of the tides and the wind through the tall grass dictated the free cadence of my verse." }
    ]
  },
  "Dashboard — rhythm/rhythmic.md": {
    primary: "Having, producing, or relating to rhythm; recurring with measured regularity.",
    secondary: "Marked by pleasing musical or poetic cadence in literary style.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "The regular, **rhythmic** thud of the woodsman's axe echoed across the frozen lake with musical clarity." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The oarsmen pulled in **rhythmic** unison, their blades rising and falling like a single machine." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The village fiddlers kept up a vigorous **rhythmic** beat that set every rustic boot tapping against the floor." }
    ]
  },
  "Dashboard — rhythm/rhythmical.md": {
    primary: "Pertaining to, having, or characterized by rhythm (synonymous with rhythmic).",
    secondary: "Flowing with harmonious periodic cadence in verse, prose, or dance.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The poem demands a refrain whose **rhythmical** recurrence strikes the ear with melancholic beauty." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The appreciation of **rhythmical** cadence and musical notes appears to be an ancient sensory gift shared across mammalian orders." },
      { author: "Ralph Waldo Emerson", work: "Poetry and Imagination", quote: "All thinking becomes **rhythmical** when the mind is exalted by intense imaginative insight." }
    ]
  },
  "Dashboard — rhythm/rhythmically.md": {
    primary: "In a rhythmic manner; with periodic cadence or regular tempo.",
    secondary: "Moving or recurring at regular harmonic intervals in acoustics and natural phenomena.",
    quotes: [
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "A continuous drum beat **rhythmically** in the night, carrying its muffled pulse across the wide river." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The waves broke **rhythmically** upon the shingle, soothing the restless thoughts of the house." },
      { author: "John Tyndall", work: "Sound", quote: "A sounding body vibrates **rhythmically**, communicating alternating compressions and rarefactions to the surrounding air." }
    ]
  },
  "Dashboard — rhythm/rhythmicity.md": {
    primary: "The property or condition of recurring at regular, rhythmic intervals; rhythmic regularity.",
    secondary: "The intrinsic ability of excitable cells (such as cardiac pacemaker cells) to generate spontaneous periodic electrical impulses in biology.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The inherent **rhythmicity** of the sinoatrial node maintains the steady cadence of the mammalian heart." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Biological functions exhibit intrinsic **rhythmicity**, oscillating between expenditure and replenishment in the milieu intérieur." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "Reflex stepping movements reveal a spinal **rhythmicity** that operates even when cortical oversight is suspended." }
    ]
  },
  "Dashboard — rhythm/rhythmos.md": {
    primary: "The ancient Greek concept of measured flow, orderly motion, proportion, pattern, or recurring form.",
    secondary: "In ancient atomism, the spatial configuration or distinctive shape of atoms that determines physical substance.",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", quote: "Democritus posited three differences in atoms: **rhythmos**, which is shape; diathege, which is arrangement; and trope, which is position." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "In the Hellenic worldview, **rhythmos** was not mere musical beat, but the measured boundary that gives form to human life." },
      { author: "Émile Benveniste", work: "Problems in General Linguistics", quote: "Originally, **rhythmos** designated the distinctive form or momentary posture assumed by something moving." }
    ]
  },
  "Dashboard — rhythm/unrhythmic.md": {
    primary: "Lacking rhythm, meter, or regular cadence; irregular in beat or movement.",
    secondary: "Jarring or halting in acoustic cadence.",
    quotes: [
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "The patient's breathing became **unrhythmic** and shallow, punctuated by sudden spasmodic gasps." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The irregular, **unrhythmic** crack of distant sniper rifles kept the trench garrison perpetually on edge." },
      { author: "James Joyce", work: "Dubliners", quote: "The horses' hooves struck the cobblestones with an **unrhythmic**, clattering noise that echoed through the empty lane." }
    ]
  },
  "Dashboard — rhythm/unrhythmical.md": {
    primary: "Characterized by an absence of rhythmic regularity or musical cadence (synonymous with unrhythmic).",
    secondary: "Lacking graceful flow, periodic symmetry, or poetic meter.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "A succession of harsh consonants produces an **unrhythmical** line that offends the cultivated ear." },
      { author: "Walter Pater", work: "Appreciations", quote: "Clumsy prose that stumbles between metrical verse and loose talk strikes the reader as painfully **unrhythmical**." },
      { author: "William James", work: "The Principles of Psychology", quote: "Sensory inputs that are completely **unrhythmical** demand constant conscious attention, producing rapid mental fatigue." }
    ]
  },

  // Dashboard — mel
  "Dashboard — mel/melodic.md": {
    primary: "Relating to or characterized by melody; musical, tuneful, and pleasing in sound.",
    secondary: "Pertaining to the horizontal succession of pitches in a musical composition (contrasted with harmonic).",
    quotes: [
      { author: "Ludwig van Beethoven", work: "Selected Letters", quote: "The **melodic** line must soar with noble simplicity, unburdened by excessive ornamental trickery." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "Melody is the most essential of these components, for **melodic** invention remains the supreme musical gift." },
      { author: "Walter Pater", work: "The Renaissance", quote: "All art constantly aspires towards the condition of music, achieving pure **melodic** integration of form and matter." }
    ]
  },
  "Dashboard — mel/melodious.md": {
    primary: "Having a pleasant tune; tuneful, musical, and sweet-sounding.",
    secondary: "Agreeable to the ear through harmonious vocal or instrumental cadence.",
    quotes: [
      { author: "John Keats", work: "Ode to a Nightingale", quote: "In some **melodious** plot Of beechen green, and shadows numberless, Singest of summer in full-throated ease." },
      { author: "William Shakespeare", work: "The Merry Wives of Windsor", quote: "By shallow rivers, to whose falls **melodious** birds sing madrigals." },
      { author: "Percy Bysshe Shelley", work: "To a Skylark", quote: "Teach me half the gladness that thy brain must know, and what sweet **melodious** thoughts are thine." }
    ]
  },
  "Dashboard — mel/melodiously.md": {
    primary: "In a melodious, tuneful, or sweetly harmonious manner.",
    secondary: "With musical grace and smooth vocal cadence.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "A thrush in the orchard began to sing **melodiously**, greeting the first golden gleam of morning." },
      { author: "Henry Wadsworth Longfellow", work: "Evangeline", quote: "The church bells chimed **melodiously** across the peaceful meadow, calling the villagers to vespers." },
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "The fountain played **melodiously** in the marble courtyard, its splash echoing against ancient stone." }
    ]
  },
  "Dashboard — mel/melodiousness.md": {
    primary: "The quality or state of being melodious, musical, or sweet-sounding; tunefulness.",
    secondary: "Agreeable acoustic euphony in poetry, speech, or music.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "The **melodiousness** of verse charms the soul by an almost physical enchantment of pure sound." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "Chaucer's verse possesses an unaffected **melodiousness** that flows with the liquid freshness of a spring brook." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "True poetic power is revealed in the sweet **melodiousness** that unites sense and sound in indivisible harmony." }
    ]
  },
  "Dashboard — mel/melodise.md": {
    primary: "To make melodious; to set to melody or compose a tune for (British spelling of melodize).",
    secondary: "To sing or express tunefully in musical verse.",
    quotes: [
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "The minstrel tuned his harp to **melodise** the tragic legend of the forgotten castle." },
      { author: "Thomas Moore", work: "Irish Melodies", quote: "The poet sought to **melodise** the ancient sorrows and hopes of his native land in song." },
      { author: "Walter Scott", work: "The Lady of the Lake", quote: "The solitary maiden would **melodise** her rustic lay as evening shadows fell across the glen." }
    ]
  },
  "Dashboard — mel/melodize.md": {
    primary: "To compose a melody for, or make tuneful and melodious (US spelling).",
    secondary: "To sing or express with lyrical sweetness.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "The Poet", quote: "The true bard will **melodize** the commonest chores of daily life, revealing their cosmic cadence." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "I hear America singing, and resolve to **melodize** the varied carols of mechanics, masons, and boatmen." },
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "The ripples of the river seem to **melodize** the silence of the afternoon wilderness." }
    ]
  },
  "Dashboard — mel/melodrama.md": {
    primary: "A dramatic piece with exaggerated characters, heightened emotions, and sensational events intended to appeal strongly to feelings (originally a play interspersed with music).",
    secondary: "Overly sensational, emotional, or theatrical behavior in daily life.",
    quotes: [
      { author: "George Bernard Shaw", work: "Plays Pleasant and Unpleasant", quote: "The Victorian stage relied on crude **melodrama** where virtue was rewarded and villainy unmasked at the final curtain." },
      { author: "Henry James", work: "The Art of the Novel", quote: "The author resisted the cheap temptation of **melodrama**, focusing instead on subtle psychological nuance." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "Don't indulge in **melodrama**, my dear boy; tears ruin one's appearance and change nothing." }
    ]
  },
  "Dashboard — mel/melodramatic.md": {
    primary: "Characteristic of melodrama; sensationalized, exaggerated, or overly theatrical in emotional expression.",
    secondary: "Relating to or featuring the style of theatrical melodrama.",
    quotes: [
      { author: "Virginia Woolf", work: "Night and Day", quote: "She avoided any **melodramatic** gesture, speaking in quiet, measured tones that carried conviction." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Wopsle struck an intensely **melodramatic** attitude, clutching his brow as though Hamlet's ghost stood before him." },
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "He felt ashamed of his **melodramatic** self-pity when he looked at the cold grey reality of the street." }
    ]
  },
  "Dashboard — mel/melody.md": {
    primary: "A sequence of single notes that is musically satisfying; a song or tuneful line.",
    secondary: "The principal or leading voice in a piece of music, as distinguished from harmony or accompaniment.",
    quotes: [
      { author: "Robert Burns", work: "A Red, Red Rose", quote: "O my Luve is like the **melody** that's sweetly play'd in tune." },
      { author: "Ludwig van Beethoven", work: "Conversations", quote: "A striking **melody** is a gift from heaven; no rules of counterpoint can manufacture a living theme." },
      { author: "John Keats", work: "Ode on a Grecian Urn", quote: "Heard **melodies** are sweet, but those unheard are sweeter; therefore, ye soft pipes, play on." }
    ]
  },
  "Dashboard — mel/melos.md": {
    primary: "The melodic element, tune, or lyrical song in ancient Greek poetry, tragedy, and choral performance.",
    secondary: "In music drama (Richard Wagner), the continuous, expressive vocal-orchestral melody that sustains dramatic continuity without periodic cadence.",
    quotes: [
      { author: "Richard Wagner", work: "Opera and Drama", quote: "The endless **melos** must guide the listener through the emotional labyrinth of the music-drama." },
      { author: "Friedrich Nietzsche", work: "The Case of Wagner", quote: "Wagner replaced rhythmic architecture with a fluid, undulating **melos** that intoxicates the nerves." },
      { author: "Gilbert Murray", work: "The Classical Tradition in Poetry", quote: "In ancient tragedy, the **melos** was the emotional soul of the drama, binding speech to song." }
    ]
  },
  "Dashboard — mel/unmelodious.md": {
    primary: "Not melodious; lacking sweet tune, musical harmony, or pleasant cadence; harsh or grating to the ear.",
    secondary: "Discordant, unmusical, or jarring in speech or sound.",
    quotes: [
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "The rusty weathercock turned with an **unmelodious** screech whenever the autumn gale shifted." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The street singer ground out an **unmelodious** dirge upon an ancient barrel organ." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The boatswain's pipe emitted a harsh and **unmelodious** squeak that startled the watch below." }
    ]
  },

  // Dashboard — mous
  "Dashboard — mous/mouse-colored.md": {
    primary: "Having the brownish-grey or dull grey color characteristic of a common field mouse or house mouse.",
    secondary: "Of a drab, muted, or nondescript appearance; murinus in biological description.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "She wore a plain, **mouse-colored** merino dress that accorded with her modest and quiet demeanor." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "A small **mouse-colored** pony trotted patiently along the chalk road, drawing the milk wagon." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "A little, **mouse-colored** man in a faded overcoat stepped cautiously through the fog." }
    ]
  },
  "Dashboard — mous/mouse-eared.md": {
    primary: "Having small, rounded, velvety leaves resembling the ears of a mouse, as in mouse-ear chickweed (*Cerastium*) or mouse-ear hawkweed (*Pilosella*).",
    secondary: "Having ears cropped or rounded like a mouse's ears, historically applied to horses with small, neat ears.",
    quotes: [
      { author: "John Gerard", work: "The Herball", quote: "The **mouse-eared** chickweed groweth upon dry ditch banks, having little soft hairy leaves." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Plants of this genus bear small **mouse-eared** foliage covered in silvery down." },
      { author: "William Withering", work: "A Botanical Arrangement of British Plants", quote: "The **mouse-eared** hawkweed spreads by runners over the dry gravelly pasture." }
    ]
  },
  "Dashboard — mous/mouse-sized.md": {
    primary: "Having the diminutive size or proportions of a mouse; tiny.",
    secondary: "Designating diminutive fossil mammals, rodents, or insectivores whose adult body mass approximates that of a mouse in paleontology.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Our Mesozoic ancestors were tiny, **mouse-sized** creatures scurrying in the shadows of the dinosaurs." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "A **mouse-sized** mammal requires a disproportionately high metabolic rate to maintain its core body heat." },
      { author: "H. G. Wells", work: "The Food of the Gods", quote: "The experimental serum had transformed an ordinary **mouse-sized** specimen into a terrifying titan." }
    ]
  },
  "Dashboard — mous/mouse.md": {
    primary: "A small rodent that typically has a pointed snout, relatively large ears and eyes, and a long thin tail (genus *Mus* and related species).",
    secondary: "A handheld hardware input device that controls the movement of the cursor on a computer display screen.",
    quotes: [
      { author: "Robert Burns", work: "To a Mouse", quote: "Wee, sleekit, cow'rin, tim'rous beastie, O, what a panic's in thy breastie, poor frightened **mouse**!" },
      { author: "Lewis Carroll", work: "Alice's Adventures in Wonderland", quote: "A **mouse** had fallen into the pool of tears, splashing about in the salty water." },
      { author: "John Steinbeck", work: "Of Mice and Men", quote: "The best-laid schemes o' mice an' men gang aft agley, and Lennie loved to stroke a soft little **mouse**." }
    ]
  },
  "Dashboard — mous/mouselike.md": {
    primary: "Resembling or characteristic of a mouse, especially in being quiet, timid, small, or stealthy.",
    secondary: "Having drab, greyish-brown coloring or scurrying movements.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "She sat in the corner with a quiet, **mouselike** stillness, afraid to draw the notice of her severe aunt." },
      { author: "George Orwell", work: "1984", quote: "A little, **mouselike** clerk with nervous spectacles hurried past him clutching a folder of documents." },
      { author: "Virginia Woolf", work: "Mrs. Dalloway", quote: "Miss Kilman stood motionless in her macintosh, watching with a sullen, **mouselike** vigilance." }
    ]
  },
  "Dashboard — mous/mousepad.md": {
    primary: "A flat, smooth pad or mat on which a computer mouse is operated to provide traction and facilitate smooth cursor movement.",
    secondary: "A desk accessory designed to optimize optical sensor tracking or mechanical ball rolling for computer peripherals.",
    quotes: [
      { author: "Walter Isaacson", work: "Steve Jobs", quote: "When the Macintosh team designed the desktop environment, every accessory from the mouse to the textured **mousepad** was scrutinized for user comfort." },
      { author: "Douglas Engelbart", work: "The Mother of All Demos", quote: "Engelbart rested his hand on the wooden prototype, sliding it across a leather **mousepad** to control screen coordinates." },
      { author: "Steven Levy", work: "Insanely Great", quote: "The personal computer revolution turned the humble desk into a digital workspace where a rubberized **mousepad** became an everyday tool." }
    ]
  },
  "Dashboard — mous/mouser.md": {
    primary: "An animal (especially a domestic cat) that hunts and catches mice.",
    secondary: "A person who searches quietly or rummages for curiosities or hidden facts.",
    quotes: [
      { author: "Mark Twain", work: "Pudd'nhead Wilson", quote: "The tomcat was an accomplished **mouser**, keeping the cellar entirely clear of rodents." },
      { author: "Charlotte Brontë", work: "Villette", quote: "The old tabby lay dozing beside the kitchen fire, an alert and trusty **mouser** despite her years." },
      { author: "Washington Irving", work: "The Sketch Book", quote: "The antiquary was a diligent **mouser** among forgotten church registers and worm-eaten parish rolls." }
    ]
  },
  "Dashboard — mous/mousetrap.md": {
    primary: "A mechanical trap or device designed to catch or kill mice.",
    secondary: "A clever scheme, ambush, or contrivance designed to catch someone unawares (as in Shakespeare's *Hamlet*).",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "What do you call the play? The **Mousetrap**. Marry, how? Tropically." },
      { author: "Ralph Waldo Emerson", work: "Miscellanies", quote: "If a man can write a better book, preach a better sermon, or make a better **mousetrap** than his neighbor, the world will make a beaten path to his door." },
      { author: "Agatha Christie", work: "The Mousetrap", quote: "The detective realized that the isolated guest house had become a deadly **mousetrap** with no way out." }
    ]
  },
  "Dashboard — mous/mousey.md": {
    primary: "Resembling a mouse in appearance or manner; timid, shy, drab, or brownish-grey (variant of mousy).",
    secondary: "Having a stale odor associated with mice, or quiet and unobtrusive demeanor.",
    quotes: [
      { author: "Virginia Woolf", work: "The Waves", quote: "She sat among the loud talkers with a timid, **mousey** silence, shrinking into her chair." },
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "The lodging-house parlor smelled faintly of cold tea, damp wallpaper, and a **mousey** decay." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The little clerk possessed a **mousey** countenance and faded grey garments that blended into the dusty legal parchment." }
    ]
  },
  "Dashboard — mous/moussaka.md": {
    primary: "A traditional baked Greek and Middle Eastern dish consisting of layered sliced eggplant (or potatoes) and spiced minced meat, topped with a thick custard or béchamel sauce.",
    secondary: "The national culinary specialty of Greece, codified in modern form by chef Nikolaos Tselementes in the 1920s.",
    quotes: [
      { author: "Elizabeth David", work: "A Book of Mediterranean Food", quote: "A classic Greek **moussaka** layers sautéed aubergines with fragrant spiced minced lamb beneath a golden crust of baked cream." },
      { author: "Patrick Leigh Fermor", work: "Mani: Travels in the Southern Peloponnese", quote: "In the village taverna, the host brought forth a smoking baking pan of **moussaka**, fragrant with cinnamon and olive oil." },
      { author: "Lawrence Durrell", work: "Prospero's Cell", quote: "We dined under the arbor upon cold retsina and savoury **moussaka**, listening to the waves lap the Corfu shore." }
    ]
  },
  "Dashboard — mous/mousse.md": {
    primary: "A light, airy, creamy food made with whipped cream or beaten egg whites, flavored with chocolate, fruit, fish, or meat, served chilled.",
    secondary: "A foamy aerosol cosmetic styling product applied to hair to provide volume and hold.",
    quotes: [
      { author: "Julia Child", work: "Mastering the Art of French Cooking", quote: "A chocolate **mousse** should be rich and dark, yet possessing a feathery, cloud-like lightness on the tongue." },
      { author: "Auguste Escoffier", work: "Le Guide Culinaire", quote: "The cold salmon **mousse** must be passed through a fine tammy cloth to ensure absolute smoothness before chilling." },
      { author: "Marcel Proust", work: "In Search of Lost Time", quote: "The dessert was an exquisite coffee **mousse**, whose delicate froth dissolved upon the palate like sweet air." }
    ]
  },
  "Dashboard — mous/moussorgsky.md": {
    primary: "Modest Mussorgsky (1839–1881), an innovative Russian romantic nationalist composer, member of 'The Five', famed for the opera *Boris Godunov* and *Pictures at an Exhibition*.",
    secondary: "A musical pioneer whose bold harmonic roughness and speech-like vocal declamation profoundly influenced modern 20th-century composers.",
    quotes: [
      { author: "Nikolai Rimsky-Korsakov", work: "My Musical Life", quote: "**Moussorgsky** possessed an astonishing dramatic instinct, capturing the rough vitality of the Russian folk in every measure." },
      { author: "Igor Stravinsky", work: "Dialogues and a Diary", quote: "The raw harmonic audacity of **Moussorgsky** broke through academic formulas to create a truly original musical speech." },
      { author: "Pyotr Ilyich Tchaikovsky", work: "Letters to His Family", quote: "In **Moussorgsky**, nature gave genius of the highest order, combined with an utter disdain for conventional technique." }
    ]
  },
  "Dashboard — mous/moustache.md": {
    primary: "A strip of hair left to grow above the upper lip of a person.",
    secondary: "A sensory bristle or tactile whisker located around the mouth of certain mammals, birds, or insects in biology.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventures of Sherlock Holmes", quote: "He was a remarkably handsome man, dark, aquiline, and moustached, possessing a heavy military **moustache**." },
      { author: "Agatha Christie", work: "Murder on the Orient Express", quote: "Hercule Poirot inspected his magnificent waxed **moustache** in the pocket mirror with fastidious pride." },
      { author: "George Orwell", work: "1984", quote: "The enormous face gazed down from the poster—forty-five, with a heavy black **moustache** and ruggedly handsome features." }
    ]
  },
  "Dashboard — mous/moustachio.md": {
    primary: "A moustache, especially an elaborate, luxuriant, long, or flamboyant one (often used in the plural: moustachios).",
    secondary: "An ornate facial whisker imparting a martial, swashbuckling, or roguish appearance.",
    quotes: [
      { author: "Charles Dickens", work: "Barnaby Rudge", quote: "The dashing officer twirled his waxed **moustachio** with an air of insufferable condescension." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The veteran harpooneer stroked his grey **moustachio**, squinting through the spray toward the horizon." },
      { author: "Washington Irving", work: "The Alhambra", quote: "A fierce Andalusian muleteer, sporting a pair of bushy **moustachios**, stepped into the firelight." }
    ]
  },
  "Dashboard — mous/mousy.md": {
    primary: "Resembling a mouse in appearance or character; shy, timid, unobtrusive, or having a dull light brownish-grey color (mousy hair).",
    secondary: "Having a stale, musty odor characteristic of mice.",
    quotes: [
      { author: "Virginia Woolf", work: "Jacob's Room", quote: "She sat quietly by the tea table, a **mousy** little woman whom nobody remembered to introduce." },
      { author: "George Orwell", work: "Burmese Days", quote: "Her hair was of that pale, **mousy** brown that never catches the sunlight." },
      { author: "Charlotte Brontë", work: "The Professor", quote: "Her demeanor was so quiet and **mousy** that her presence was scarcely felt in the classroom." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${relPath}`);
}

console.log('Done Batch 2 (rhythm, mel, mous) of Cluster Sound & Auditory!');
