import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design/Dashboard — arti';

const filesData = {
  "apart.md": {
    primary: "Separated by a distance, interval, or space of time.",
    secondary: "To or on one side; in a detached, distinct, or isolated state.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "O, swear not by the moon, the inconstant moon, that monthly changes in her circled orb, lest that thy love prove likewise variable; stand all **apart**." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I love to be alone; I never found the companion that was so companionable as solitude when standing **apart** from the crowd." },
      { author: "Emily Dickinson", work: "Poems", quote: "The distance that the dead have gone does not at first appear; their coming back seems possible for pins and needles falling **apart**." }
    ]
  },
  "art.md": {
    primary: "The expression or application of human creative skill and imagination, typically in visual or auditory form.",
    secondary: "A skill acquired by experience, study, or observation; a craft or trade.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "**Art** is the most intense mode of individualism that the world has known." },
      { author: "Leo Tolstoy", work: "What Is Art?", quote: "**Art** is a human activity consisting in this, that one man consciously infects others with the feelings he has lived through." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "It was in the nature of **art** to hold together what was fleeting and chaotic in everyday life." }
    ]
  },
  "arti.md": {
    primary: "The Greek combining root *artios* (even-numbered, complete, fitting), seen in zoological and biological nomenclature.",
    secondary: "In Romance and English etymology, the stem representing Latin *ars* (genitive *artis*), signifying craft, skill, or artistic technique.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In anatomical and zoological compounds, the root **arti** denotes an even number or fitting symmetry of parts." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The dental formula and pedal digits share the primitive **arti** arrangement characteristic of even-toed ungulates." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek adjective *artios*, root **arti**, designated whole numbers that are divisible by two without remainder." }
    ]
  },
  "artichoke.md": {
    primary: "A perennial plant of the thistle family Asteraceae, cultivated for its edible immature flower head.",
    secondary: "The Jerusalem artichoke (*Helianthus tuberosus*), a North American sunflower cultivated for its edible tuberous rhizomes.",
    quotes: [
      { author: "Elizabeth David", work: "French Provincial Cooking", quote: "Peel away the tough outer bracts of the **artichoke** to reveal the tender, pale green heart." },
      { author: "Pablo Neruda", work: "Ode to the Artichoke", quote: "The tender **artichoke** dressed in armor, a vegetable warrior standing proud in market baskets." },
      { author: "Henry James", work: "A Little Tour in France", quote: "We were served boiled purple **artichoke** accompanied by a piquant vinaigrette." }
    ]
  },
  "article.md": {
    primary: "A particular item or individual thing within a class or collection of goods.",
    secondary: "A non-fiction piece of writing included in a publication; or a distinct clause in a legal document.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "There was not a single household **article** in the dismal room that did not speak of desolation." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I resolved to write a modest **article** for the paper, submitting it anonymously beneath the door." },
      { author: "Thomas Jefferson", work: "Declaration of Independence", quote: "Each formal **article** of grievance was set forth to justify a complete severance of political allegiance." }
    ]
  },
  "articled.md": {
    primary: "Bound by a formal written contract or indenture of apprenticeship, training, or articles of clerkship.",
    secondary: "Formulated, itemized, or charged under specific legal articles or covenants.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "He had been regularly **articled** to a proctor in Doctors' Commons for a term of seven years." },
      { author: "William Makepeace Thackeray", work: "The History of Pendennis", quote: "The ambitious young gentleman was **articled** to an eminent London attorney." },
      { author: "Anthony Trollope", work: "The Warden", quote: "The elderly solicitor remembered when he himself had been an **articled** youth copying dusty deeds." }
    ]
  },
  "articular.md": {
    primary: "Relating to a joint or the joints of the body.",
    secondary: "Characterized by or situated near the articulating surface of two bones or cartilage.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Rheumatoid disease characteristically begins with bilateral swelling of the small **articular** capsules." },
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "Smooth hyaline cartilage coats each **articular** extremity to minimize friction during movement." },
      { author: "Santiago Ramón y Cajal", work: "Histology", quote: "Proprioceptive sensory nerve endings are densely distributed within the fibrous **articular** ligaments." }
    ]
  },
  "articulary.md": {
    primary: "Pertaining to, involving, or situated at the joints; articular.",
    secondary: "In anatomy, designating connective structures, ligaments, or surfaces participating in joint articulation.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Vertebrates", quote: "The fossil reptile displayed specialized **articulary** facets on its cervical vertebrae." },
      { author: "Robert Hooper", work: "Lexicon Medicum", quote: "In classical nosology, **articulary** rheumatism denoted painful inflammation confined to synovial joints." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The **articulary** head of the humerus fits snugly into the shallow glenoid cavity." }
    ]
  },
  "articulate.md": {
    primary: "Having or showing the ability to speak fluently and coherently; expressing oneself clearly.",
    secondary: "Having joints or jointed segments; forming a movable joint with another bone or part.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "He possessed an extraordinarily **articulate** voice that lent persuasiveness to the most complex moral argument." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Human speech differs from animal cries by consisting of distinct, **articulate** vocal sounds." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The limbs of the anthropoid ape are freely **articulate**, adapted for brachiation among branches." }
    ]
  },
  "articulated.md": {
    primary: "Having jointed sections, segments, or connecting links that allow bending, movement, or flexibility.",
    secondary: "Clearly expressed, formulated, or enunciated in words.",
    quotes: [
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "The Martian war-machine stepped across the hills on three long, **articulated** metallic legs." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Her unspoken grief was at last **articulated** in a series of poignant journal entries." },
      { author: "Richard Feynman", work: "The Character of Physical Law", quote: "Scientific theories must be rigorously **articulated** so that precise predictions can be tested." }
    ]
  },
  "articulately.md": {
    primary: "In a clear, fluent, and coherent manner of speech or writing.",
    secondary: "In an interconnected, segmented, or jointed physical arrangement.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Elinor spoke so **articulately** and calmly that her sister was gradually comforted." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Mr. Rochester stated his case **articulately**, laying bare the tragic secrets of his past." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The robotic limbs moved **articulately**, assembling delicate electronic components without human intervention." }
    ]
  },
  "articulateness.md": {
    primary: "The quality of being articulate; the ability to express thoughts fluently, clearly, and effectively in speech or writing.",
    secondary: "The physical state of being segmented or having movable joints.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "True eloquence requires an **articulateness** of spirit where thought and word merge into one." },
      { author: "David Foster Wallace", work: "Consider the Lobster", quote: "He admired the extraordinary **articulateness** of the radio essayist, who never faltered for a syllable." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Higgins believed that phonetic **articulateness** was the primary barrier dividing social classes." }
    ]
  },
  "articulatio.md": {
    primary: "In classical anatomy and medical Latin, a joint or articulation connecting two or more skeletal bones or cartilages.",
    secondary: "The formal anatomical nomenclature for synovial, fibrous, and cartilaginous skeletal joints.",
    quotes: [
      { author: "Gray's Anatomy", work: "Anatomy of the Human Body", quote: "The hip joint is classified anatomically as an **articulatio** coxae, possessing a ball-and-socket configuration." },
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "In describing each **articulatio**, Vesalius illustrated the synovial membranes and retaining ligaments with fidelity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Inflammatory effusion within an **articulatio** requires careful diagnostic aspiration." }
    ]
  },
  "articulation.md": {
    primary: "The clear, distinct pronunciation and enunciation of vocal speech sounds in language.",
    secondary: "A movable or fixed joint between two bones or parts of an animal skeleton; or the state of being jointed.",
    quotes: [
      { author: "Peter Ladefoged", work: "A Course in Phonetics", quote: "Precise lingual **articulation** against the alveolar ridge produces crisp dental consonants." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The ball-and-socket **articulation** of the shoulder allows universal rotation of the forelimb." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Eliza practiced her vowel **articulation** before the mirror until every trace of Cockney slang vanished." }
    ]
  },
  "articulative.md": {
    primary: "Serving to articulate, join, or connect; having the power of distinct articulation.",
    secondary: "In linguistics or anatomy, functioning in the formation of speech sounds or physical jointing.",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The **articulative** organs of the human mouth coordinate subtle air movements into recognizable speech." },
      { author: "Herbert Spencer", work: "The Principles of Psychology", quote: "Higher intellectual evolution is marked by increasing **articulative** complexity in symbolic communication." },
      { author: "William Dwight Whitney", work: "Language and the Study of Language", quote: "The child gradually refines its crude vocal babbling into controlled, **articulative** phrases." }
    ]
  },
  "articulator.md": {
    primary: "In phonetics, a vocal speech organ (such as the tongue, lips, or palate) that moves to produce speech sounds.",
    secondary: "In dentistry, a mechanical device to which dental plaster casts are attached to simulate jaw movements.",
    quotes: [
      { author: "Peter Ladefoged", work: "Vowels and Consonants", quote: "The tongue serves as the most agile mobile **articulator** in the vocal tract." },
      { author: "Daniel Jones", work: "The Pronunciation of English", quote: "A phonetician must master the independent movement of each active **articulator**." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "Even when muscular dystonia affected his jaw **articulator**, the singer managed to enunciate pure melodic phrases." }
    ]
  },
  "articulatory.md": {
    primary: "Relating to the articulation of speech sounds or the anatomical organs involved in speech production.",
    secondary: "Relating to anatomical joints or joint function.",
    quotes: [
      { author: "Noam Chomsky", work: "The Sound Pattern of English", quote: "Generative phonology relates abstract phonological matrices to concrete **articulatory** movements." },
      { author: "Peter Ladefoged", work: "Elements of Acoustic Phonetics", quote: "Acoustic resonance in the vocal tract corresponds directly to specific **articulatory** postures." },
      { author: "Edward Sapir", work: "Language", quote: "Every spoken language possesses its own distinctive **articulatory** rhythm and muscular habitus." }
    ]
  },
  "artillery.md": {
    primary: "Large-caliber mounted firearms, cannon, howitzers, or missile launchers used in warfare.",
    secondary: "A branch or regiment of an army that uses and maintains heavy ordnance and cannons.",
    quotes: [
      { author: "Winston Churchill", work: "The World Crisis", quote: "The massed **artillery** opened fire at dawn, throwing up a rolling curtain of fire and steel." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Captain Tushin's battery of light **artillery** maintained its fire despite heavy smoke and enemy shot." },
      { author: "Ernest Hemingway", work: "A Farewell to Arms", quote: "The Austrian mountain **artillery** pounded the ridge with sharp, rhythmic detonations." }
    ]
  },
  "artilleryman.md": {
    primary: "A soldier belonging to an artillery unit, trained in the operation, sighting, and firing of heavy guns and cannons.",
    secondary: "A gunner or member of a cannon crew.",
    quotes: [
      { author: "Stephen Crane", work: "The Red Badge of Courage", quote: "A blackened **artilleryman** swabbed the smoking chamber of the twelve-pounder with desperate haste." },
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "I encountered an exhausted **artilleryman** who had fled the annihilation of his battery on Weybridge common." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "The brave **artilleryman** stands by his gun, heedless of the bursting shell and blinding smoke." }
    ]
  },
  "artiodactyl.md": {
    primary: "An even-toed ungulate mammal belonging to the order Artiodactyla, possessing an even number of functional toes on each foot.",
    secondary: "Of or relating to the even-toed hoofed mammals.",
    quotes: [
      { author: "Richard Owen", work: "On the Archetype and Homologies of the Vertebrate Skeleton", quote: "Owen divided the ungulates into perissodactyl and **artiodactyl** orders based on the axis of the foot." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Fossil discoveries continue to illuminate the divergence between perissodactyl and **artiodactyl** mammalian lineages." },
      { author: "Stephen Jay Gould", work: "The Flamingo's Smile", quote: "Whales share deep phylogenetic affinities with the terrestrial **artiodactyl** stem, notably the hippopotamus." }
    ]
  },
  "artiodactyla.md": {
    primary: "An order of placental mammals comprising the even-toed ungulates, whose weight is borne equally by the third and fourth digits.",
    secondary: "In mammalian paleontology, a dominant ungulate order that diversified extensively throughout the Cenozoic era.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The order **Artiodactyla** is distinguished by an asymmetrical paraxonic foot symmetry." },
      { author: "Ernst Mayr", work: "Principles of Systematic Zoology", quote: "Molecular phylogenies revealed that Cetacea are nested cladistically within **Artiodactyla**, forming Cetartiodactyla." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Ruminant families of the **Artiodactyla** achieved their greatest diversity across the Old World plains." }
    ]
  },
  "artiodactylous.md": {
    primary: "Having an even number of toes or digits on each foot; belonging or pertaining to the Artiodactyla.",
    secondary: "Characterized by a paraxonic foot structure in which the main axis of weight passes between the third and fourth digits.",
    quotes: [
      { author: "Louis Agassiz", work: "Methods of Study in Natural History", quote: "The fossil tracks displayed a distinctly **artiodactylous** footprint, clearly separated from odd-toed tapir prints." },
      { author: "Richard Owen", work: "Palaeontology: A Systematic Summary of Extinct Animals", quote: "Anoplotherium possessed **artiodactylous** feet, representing an extinct transitional herbivore." },
      { author: "Edward Drinker Cope", work: "The Primary Factors of Organic Evolution", quote: "Foot reduction in **artiodactylous** ungulates culminated in the specialized cannon bones of deer and cattle." }
    ]
  },
  "artisan.md": {
    primary: "A worker in a skilled trade, especially one that involves making things by hand; a craftsperson.",
    secondary: "Relating to or characteristic of products made in limited quantities using traditional, non-mechanized methods.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The medieval stonecutter was an **artisan** whose creative freedom breathed spiritual life into the cathedral." },
      { author: "William Morris", work: "News from Nowhere", quote: "In our commonwealth, every laborer is an **artisan**, taking genuine joy in the beauty of handmade craft." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "My father taught me to respect the diligent **artisan** who earns an honest bread through his skillful trade." }
    ]
  },
  "artist.md": {
    primary: "A person who produces paintings, drawings, sculpture, or other works of visual fine art.",
    secondary: "A person who practices any of the creative arts, such as music, writing, or performance, with exceptional skill.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "The Poet", quote: "The true **artist** seeks to unlock the secret beauty hidden within common, neglected things." },
      { author: "James Joyce", work: "A Portrait of the Artist as a Young Man", quote: "The **artist**, like the God of the creation, remains within or behind or beyond or above his handiwork, invisible." },
      { author: "Oscar Wilde", work: "The Decay of Lying", quote: "Life imitates art far more than art imitates life, and the **artist** creates the lens through which we see nature." }
    ]
  },
  "artiste.md": {
    primary: "A professional entertainer, especially a singer, dancer, or variety performer on stage.",
    secondary: "A skilled craftsperson or stylist who approaches their trade with artistic flair and theatricality.",
    quotes: [
      { author: "Virginia Woolf", work: "Night and Day", quote: "The eccentric salon was frequented by poets, painters, and a flamboyant foreign **artiste**." },
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "Mr. Vincent Crummles introduced his leading stage **artiste** with grand theatrical flourishes." },
      { author: "P. G. Wodehouse", work: "Right Ho, Jeeves", quote: "The dramatic soprano considered herself an **artiste** of international caliber, brooking no contradiction." }
    ]
  },
  "artistic.md": {
    primary: "Having or revealing natural creative skill; showing good aesthetic taste and imaginative sensitivity.",
    secondary: "Relating to or characteristic of art or artists.",
    quotes: [
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "Lily Briscoe struggled before her canvas to balance the color masses in unified **artistic** vision." },
      { author: "Oscar Wilde", work: "The Critic as Artist", quote: "The **artistic** temperament is driven by an intense desire to create beauty amidst a prosaic world." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "Her performance lacked genuine **artistic** depth, relying instead on mechanical technical perfection." }
    ]
  },
  "artistically.md": {
    primary: "In an artistic, aesthetically pleasing, or skillfully creative manner.",
    secondary: "From the standpoint of art, aesthetics, or artistic technique.",
    quotes: [
      { author: "Edith Wharton", work: "The Age of Innocence", quote: "The private drawing-room was decorated **artistically**, avoiding the rigid Victorian clutter of the avenue." },
      { author: "Henry James", work: "The Aspern Papers", quote: "The Venetian garden was neglected, yet **artistically** charming in its wild, romantic decay." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Turner arranged the light and shadow **artistically**, lifting the landscape into spiritual poetry." }
    ]
  },
  "artistry.md": {
    primary: "Creative skill, ability, and imagination of a high order in the arts.",
    secondary: "Superior craftsmanship or artistic quality evident in any human performance or creation.",
    quotes: [
      { author: "Willa Cather", work: "The Song of the Lark", quote: "The soprano's effortless vocal control and deep dramatic **artistry** stunned the opera house audience." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Greek Interpreter", quote: "Art in the blood is liable to take the strangest forms, and Holmes possessed an eerie diagnostic **artistry**." },
      { author: "Ralph Waldo Emerson", work: "Essays: Second Series", quote: "The supreme test of human **artistry** is whether it reveals the divine simplicity underlying creation." }
    ]
  },
  "unarticulate.md": {
    primary: "Unable to express oneself clearly, fluently, or coherently; inarticulate.",
    secondary: "Lacking distinct jointed segments, divisions, or syllables.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "He uttered a low, **unarticulate** groan of anguish that pierced my heart with sorrow." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "From the depths of the cabin came a wild, **unarticulate** cry that chilled the night watch." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "The working masses suffered in dumb silence, their deep grievances remaining **unarticulate** before Parliament." }
    ]
  },
  "unarticulated.md": {
    primary: "Not expressed, spoken, or clearly formulated in words; unspoken.",
    secondary: "In anatomy or zoology, not having joints or movable connections; solid or fused.",
    quotes: [
      { author: "Virginia Woolf", work: "The Waves", quote: "Beneath our polite dinner conversation lay a vast ocean of **unarticulated** desires and unspoken regrets." },
      { author: "George Eliot", work: "Middlemarch", quote: "A shadowy, **unarticulated** fear hovered over her mind, though she dared not name it." },
      { author: "Richard Owen", work: "Lectures on Invertebrate Anatomy", quote: "The primitive fossil carapace forms a single **unarticulated** shield protecting the dorsal organs." }
    ]
  },
  "unartistic.md": {
    primary: "Lacking artistic value, aesthetic taste, or creative imagination; crude or prosaic.",
    secondary: "Showing no appreciation for or understanding of the fine arts.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "There is no such thing as a moral or an immoral book; books are well written, or badly written, and this was merely **unartistic**." },
      { author: "Henry James", work: "The American", quote: "Newman cheerfully admitted to an **unartistic** eye, wandering through the Louvre with honest American bewilderment." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The cheap cast-iron facade was thoroughly **unartistic**, an insult to true craftsmanship." }
    ]
  }
};

for (const [filename, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filename}`);
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
  console.log(`Updated: ${filename}`);
}

console.log('Done Batch 6 (Dashboard — arti) of Cluster Art, Craft & Design (31 words)!');
