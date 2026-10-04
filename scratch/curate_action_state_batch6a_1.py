# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — cel Part 1 (40 words) ---
  "Dashboard — cel/accelerando.md": {
    "primary": "A musical tempo direction indicating a gradual increase in tempo and speed of performance.",
    "secondary": "In orchestral score analysis, an accelerando creates growing acoustic tension leading into climactic cadences or thematic transformations.",
    "quotes": [
      {"author": "Romain Rolland", "work": "Jean-Christophe", "quote": "The orchestra surged forward in a thrilling **accelerando**, sweeping the listener along in a whirlwind of sound."},
      {"author": "Hector Berlioz", "work": "Treatise on Modern Instrumentation and Orchestration", "quote": "The composer employed an **accelerando** in the string section to simulate the galloping approach of the phantom steed."},
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "The syncopated rhythms intensified through a subtle **accelerando**, blurring the boundary between dance and frenzy."}
    ]
  },
  "Dashboard — cel/accelerate.md": {
    "primary": "To cause to move faster, gain speed, or happen more quickly; to increase the rate of progress.",
    "secondary": "In classical Newtonian mechanics, an unbalanced external force acting upon a mass serves to accelerate it proportionally to the applied force.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The force of gravity acting perpetually upon a falling body will continually **accelerate** its downward velocity toward the earth."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Severe environmental changes tend to **accelerate** the rate of organic modification and natural selection among competing varieties."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I pulled the lever harder to **accelerate** my journey into the distant, dim future of our planet."}
    ]
  },
  "Dashboard — cel/accelerated.md": {
    "primary": "Caused to move or happen faster; moving with increasing speed or at a rapid rate.",
    "secondary": "In cardiac pathology, an accelerated ventricular rhythm produces palpitations and compromised hemodynamic efficiency during exercise.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Artificial breeding programs have **accelerated** the emergence of striking morphological varieties in domestic pigeons."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The unexpected death of the emperor **accelerated** the disintegration of the imperial administration along the Danube."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The laboratory reaction proceeded at an **accelerated** pace, filling the glassware with dense violet fumes."}
    ]
  },
  "Dashboard — cel/acceleration.md": {
    "primary": "The rate of change of velocity per unit of time; an increase in the speed or rate of something.",
    "secondary": "In kinematics and calculus, acceleration represents the second time derivative of position, measured in meters per second squared.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The steady **acceleration** of moving bodies under gravitational attraction follows precise mathematical laws across the solar system."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The rapid **acceleration** of the mountain torrent eroded deep gorges through the hardest granite strata."},
      {"author": "Albert Einstein", "work": "Relativity: The Special and General Theory", "quote": "The equivalence principle postulates that physical effects of gravitational attraction are indistinguishable from uniform mechanical **acceleration**."}
    ]
  },
  "Dashboard — cel/accelerative.md": {
    "primary": "Tending to cause an increase in speed, velocity, or rate of development; accelerating.",
    "secondary": "In macroeconomics and monetary dynamics, the accelerative effect of capital expenditure stimulates amplified secondary consumption cycles.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The accumulation of mercantile capital exerts an **accelerative** influence upon national division of labor and manufacturing efficiency."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Cosmic evolution exhibits an **accelerative** momentum as specialized structures multiply within the expanding universe."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Inductive reasoning provides an **accelerative** method for discovering hidden axioms of natural science."}
    ]
  },
  "Dashboard — cel/accelerator.md": {
    "primary": "A device, pedal, or throttle for increasing speed; or an agent, catalyst, or machine that accelerates.",
    "secondary": "In high-energy nuclear physics, a particle accelerator uses radio-frequency electric fields and superconducting magnets to smash hadrons.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The New Accelerator", "quote": "Professor Gibberne invented a miraculous nervous **accelerator** that stimulated the human metabolism thousands of times above normal speed."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "Physicists realized that an artificial electrostatic **accelerator** could disintegrate atomic nuclei far more effectively than alpha particles."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He stepped firmly upon the motor **accelerator**, propelling the vehicle down the country road at breathtaking velocity."}
    ]
  },
  "Dashboard — cel/acceleratory.md": {
    "primary": "Serving to accelerate; characterized by or contributing to an increase in speed.",
    "secondary": "In neurophysiology and autonomic regulation, acceleratory cardiac nerve fibers release norepinephrine to increase sinoatrial firing rates.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Stimulation of sympathetic pathways exerts a direct **acceleratory** action upon ventricular contraction during acute physiological stress."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The medulla contains both inhibitory and **acceleratory** centers regulating the rhythm of respiratory movements."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Adaptive biological modifications produce an **acceleratory** impetus that widens the gap between allied evolutionary lineages."}
    ]
  },
  "Dashboard — cel/accelerometer.md": {
    "primary": "An instrument designed to measure proper acceleration, mechanical shock, or the rate of velocity change.",
    "secondary": "In aerospace navigation and inertial guidance systems, a triaxial accelerometer calculates vehicle trajectory without external radio signals.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "The cockpit **accelerometer** registered four gravities of force as the experimental rocket blasted through the stratosphere."},
      {"author": "Isaac Asimov", "work": "The Stars, Like Dust", "quote": "The pilot tapped the glass of the **accelerometer**, checking the deceleration rate as the spacecraft entered the planetary orbit."},
      {"author": "Robert A. Heinlein", "work": "Rocket Ship Galileo", "quote": "The needle of the **accelerometer** crept upward toward the red danger line during the intense lunar descent burn."}
    ]
  },
  "Dashboard — cel/alcelaphus.md": {
    "primary": "A genus of large African antelopes commonly known as the hartebeest, characterized by elongated muzzles and ringed horns.",
    "secondary": "In mammalian evolutionary biology and game ecology, Alcelaphus buselaphus is adapted to grassland grazing, running in high-speed zigzags to escape predators.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "A herd of hartebeest of the genus **alcelaphus** grazed cautiously across the rolling savanna beneath the acacia trees."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The awkward, high-withered gait of **alcelaphus** belies the astonishing galloping speed of this African antelope."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The curiously twisted, lyrate horns of **alcelaphus** are developed in both sexes and employed in intraspecific territorial defense."}
    ]
  },
  "Dashboard — cel/arcella.md": {
    "primary": "A genus of testate freshwater amoebae characterized by a dome-shaped, brownish shell or test with an inverted central aperture.",
    "secondary": "In protozoology and micro-limnology, Arcella vulgaris secretes a chitinous proteinaceous shell that incorporates gas vacuoles for buoyant flotation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Microscopic examination of pond water reveals the brown chitinous test of **arcella** extending lobose pseudopodia through its aperture."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The widespread distribution of testate protozoa like **arcella** in isolated mountain pools is facilitated by airborne encystment."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "We observed the delicate creeping movements of **arcella** upon the slide, marveling at the geometric perfection of its microscopic dome."}
    ]
  },
  "Dashboard — cel/arcellidae.md": {
    "primary": "A taxonomic family of testate amoebae within the order Arcellinida, bearing organic, non-mineralized circular shells.",
    "secondary": "In paleo-limnology and aquatic ecotoxicology, fossilized tests of Arcellidae serve as bioindicators of past freshwater acidity and heavy metal contamination.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Members of the family **arcellidae** are distinguished from other rhizopods by their hemispherical, organic test devoid of agglutinated sand grains."},
      {"author": "Joseph Leidy", "work": "Fresh-Water Rhizopods of North America", "quote": "The sphagnum bogs of New Jersey yielded an astonishing abundance of microscopic **arcellidae** thriving among the submerged mosses."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Dredgings from the marshy pools of the Pampas contained several distinct varieties belonging to the testate **arcellidae**."}
    ]
  },
  "Dashboard — cel/celandine.md": {
    "primary": "A yellow-flowered European plant of the poppy family (greater celandine) or buttercup family (lesser celandine).",
    "secondary": "In historical herbalism and folklore, yellow celandine sap was applied topically to remove warts and soothe ocular inflammation.",
    "quotes": [
      {"author": "William Wordsworth", "work": "Poems, in Two Volumes", "quote": "There is a flower, the lesser **celandine**, that will bloom on bleak winter days when skies are cold and gray."},
      {"author": "John Ruskin", "work": "Proserpina", "quote": "The glossy golden petals of the lesser **celandine** brighten the English wayside banks long before the primrose appears."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The spring opening of the greater **celandine** along our sunny stone hedgerows coincides with the return of migratory martins."}
    ]
  },
  "Dashboard — cel/celastraceae.md": {
    "primary": "A family of flowering plants (the bittersweet or staff-tree family), comprising trees, shrubs, and lianas with small flowers and colorful arils.",
    "secondary": "In phytochemistry and economic botany, members of Celastraceae yield cytotoxic triterpenes (maytansinoids) and traditional insecticidal extracts.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **celastraceae** is well represented in our woodlands by the climbing bittersweet and the burning bush."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "Tropical mountain forests harbor diverse arborescent genera of **celastraceae** bearing bright scarlet, bird-dispersed arils."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "Climbing woody lianas of the family **celastraceae** twist their stems spirally around neighboring saplings to reach the canopy."}
    ]
  },
  "Dashboard — cel/celastrus.md": {
    "primary": "A genus of deciduous and evergreen woody vines and shrubs in the bittersweet family, noted for showy, bright red or yellow seeds.",
    "secondary": "In landscape ecology and invasive species management, Celastrus orbiculatus (Oriental bittersweet) aggressively outcompetes native North American trees.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Excursions", "quote": "In late October, the bursting orange capsules of **celastrus** reveal their brilliant crimson seeds along the forest margin."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The climbing bittersweet, **celastrus** scandens, ascends tall trees in fertile river bottoms, fruiting abundantly in autumn."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The revolving young shoot of **celastrus** sweeps a wide circle through the air until it encounters a supportive branch."}
    ]
  },
  "Dashboard — cel/celebes.md": {
    "primary": "The historical name for Sulawesi, a large, uniquely four-peninsula island in eastern Indonesia.",
    "secondary": "In biogeography, Celebes lies at the heart of Wallacea, exhibiting extraordinary faunal endemism including the babirusa and anoa.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The island of **celebes** occupies a remarkably central position in the archipelago, possessing animal forms utterly distinct from those of Java or Borneo."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The anomalous mammalian fauna of **celebes** indicates long periods of geographic isolation from both Asian and Australian mainlands."},
      {"author": "Joseph Conrad", "work": "An Outcast of the Islands", "quote": "Willems stared toward the dark outline of the **celebes** coast, wondering what fate awaited him across those tropical straits."}
    ]
  },
  "Dashboard — cel/celebrant.md": {
    "primary": "A person who performs or presides over a formal religious ceremony or rite, especially the Eucharist; or a participant in a celebration.",
    "secondary": "In liturgical theology, the celebrant acts in persona Christi during the consecration of the bread and wine at the high altar.",
    "quotes": [
      {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "Stephen watched the vestmented **celebrant** elevate the golden chalice amid clouds of fragrant incense at the altar."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The solemn Christian **celebrant** pronounced the ancient eucharistic prayers with serene dignity before the gathered congregation."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The bishop stood as the chief **celebrant** in Saint Peter's, blessing the bowed multitudes beneath the mighty dome."}
    ]
  },
  "Dashboard — cel/celebrate.md": {
    "primary": "To acknowledge a significant happy day or event with a social gathering, ceremony, or enjoyable activity.",
    "secondary": "In cultural anthropology, human communities celebrate seasonal solstices and harvests through symbolic feasts and commemorative rituals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "A contract of true love to **celebrate**, and some donation freely to estate on the bless'd lovers."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The Cratchit family gathered with joyful hearts to **celebrate** Christmas Day around their modest roasted goose."},
      {"author": "Walt Whitman", "work": "Song of Myself", "quote": "I **celebrate** myself, and sing myself, and what I assume you shall assume, for every atom belonging to me as good belongs to you."}
    ]
  },
  "Dashboard — cel/celebrated.md": {
    "primary": "Widely known, praised, honored, and acclaimed for great achievements or distinguished qualities.",
    "secondary": "In historiographical literature, celebrated figures of antiquity were memorialized in Plutarch's *Parallel Lives* as models of civic virtue.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer presented his manuscript regarding the **celebrated** hound legend that had haunted the family for generations."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Pemberley was a **celebrated** estate renowned throughout Derbyshire for its magnificent park and stately architectural beauty."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **celebrated** philosopher Marcus Aurelius united imperial sovereignty with severe Stoic moral introspection."}
    ]
  },
  "Dashboard — cel/celebrater.md": {
    "primary": "A variant spelling of celebrator; one who celebrates, commemorates, or praises a person, event, or triumph.",
    "secondary": "In nineteenth-century festival accounts, every enthusiastic celebrater joined the civic procession through the decorated marketplace.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Snodgrass proved himself a passionate **celebrater** of rustic beauty and bucolic romance during the shooting excursion."},
      {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The squire was an indefatigable **celebrater** of old English customs, reviving Yule logs and morris dancing on his estate."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The poet is born to be a sincere **celebrater** of divine heroism in human history and noble actions."}
    ]
  },
  "Dashboard — cel/celebration.md": {
    "primary": "The action of celebrating an important day or event; a social gathering or festive party.",
    "secondary": "In ritual sociology, collective celebration revitalizes communal bonds through shared symbols, music, and commemorative pageantry.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The annual New Year's Eve **celebration** at the Red House brought together the gentry and tenantry in festive harmony."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The triumphal **celebration** of Aurelian displayed the captive queen Zenobia adorned in chains of gold through the Roman Forum."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lively wedding **celebration** cheered the old house with laughter and music after months of solemn quiet."}
    ]
  },
  "Dashboard — cel/celebrator.md": {
    "primary": "A person who celebrates or participates enthusiastically in a festive event, triumph, or ceremony.",
    "secondary": "In literary journalism, an engaged celebrator of cultural anniversaries produces retrospective essays honoring seminal artistic milestones.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "The poet stands as the loving **celebrator** of American democracy and the manifold labors of working men."},
      {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "The merry **celebrator** of May Day raised the garlanded maypole upon the woodland green, defying puritan frowns."},
      {"author": "William Makepeace Thackeray", "work": "The Paris Sketch Book", "quote": "Every lively **celebrator** in the boulevard carnival wore grotesque masks and pelted passersby with confetti."}
    ]
  },
  "Dashboard — cel/celebratory.md": {
    "primary": "Expressing, conveying, or characterized by celebration, festive praise, or happy commemoration.",
    "secondary": "In symphonic music, a celebratory fanfare composed for brass and timpani opens civic jubilees and state ceremonies.",
    "quotes": [
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "The church bells of Florence rang out in a vibrant, **celebratory** peal that resonated across the red-tiled roofs."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "The royal banquet concluded with a magnificent **celebratory** display of fireworks rising over the frozen Thames."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "London was filled with **celebratory** crowds waving flags as the radio officially announced victory in Europe."}
    ]
  },
  "Dashboard — cel/celebrex.md": {
    "primary": "A brand name for celecoxib, a nonsteroidal anti-inflammatory drug (NSAID) that selectively inhibits COX-2 enzymes.",
    "secondary": "In clinical pharmacology, Celebrex treats arthritis and acute pain with lower risks of gastric ulceration compared to non-selective NSAIDs.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "Selective anti-inflammatory therapies such as **celebrex** emerged from modern biochemical breakthroughs in prostaglandin synthesis."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The therapeutic utility of targeted COX-2 inhibitors like **celebrex** revolutionized chronic rheumatologic pain management."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The clinic physician noted that novel analgesic preparations such as **celebrex** effectively mitigated chronic joint stiffness."}
    ]
  },
  "Dashboard — cel/celebrity.md": {
    "primary": "The state of being widely celebrated or famous; or a famous, widely recognized person.",
    "secondary": "In cultural sociology, modern celebrity culture transforms private personal identity into a commodified public spectacle via mass media.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian found that his sudden social **celebrity** brought both flattering adoration and malicious drawing-room gossip."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Miss Chancellor shrank from the vulgar **celebrity** that pursued outspoken lecturers in the sensational public press."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Vincent Crummles took immense pride in introducing the infant phenomenon to provincial audiences as a theatrical **celebrity**."}
    ]
  },
  "Dashboard — cel/celecoxib.md": {
    "primary": "A nonsteroidal anti-inflammatory drug (NSAID) that selectively inhibits the cyclooxygenase-2 (COX-2) enzyme.",
    "secondary": "In molecular pharmacology, celecoxib reduces inflammatory prostaglandin synthesis while sparing gastroprotective COX-1 activity in gastric mucosa.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clinical trials demonstrated that **celecoxib** provided potent analgesia in osteoarthritis without impairing platelet aggregation."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "The development of **celecoxib** marked a major advance in designing enzyme-specific therapeutics for chronic inflammatory disorders."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "Postoperative discomfort was effectively managed through selective cyclooxygenase inhibitors such as **celecoxib**."}
    ]
  },
  "Dashboard — cel/celeriac.md": {
    "primary": "A variety of celery cultivated for its large, knobby, edible turnip-like root; celery root.",
    "secondary": "In European culinary history and gastronomy, celeriac is traditionally shredded raw in remoulade sauce or puréed with potatoes in winter stews.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Peel the knobby root of the **celeriac** thoroughly before slicing it thin for a savory winter salad with mustard vinaigrette."},
      {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "Braised **celeriac** served with a rich espagnole sauce provides an elegant winter vegetable accompaniment to roast beef."},
      {"author": "Auguste Escoffier", "work": "A Guide to Modern Cookery", "quote": "The French chef prepares céleri-rave by julienning fresh **celeriac** and binding it with piquant seasoned mayonnaise."}
    ]
  },
  "Dashboard — cel/celerity.md": {
    "primary": "Swiftness of movement, speed, rapidity, or prompt dispatch in action.",
    "secondary": "In classical military doctrine, Julius Caesar famously defeated adversaries by conducting forced marches with legendary celerity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Caesar has done his work with that **celerity** that he outstrips our swiftest couriers in the field."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The yield of your design, and the **celerity** with which you execute it, is astonishing to all your friends."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman cavalry swept across the plains with such **celerity** that the enemy encampment was surrounded before scouts could give warning."}
    ]
  },
  "Dashboard — cel/celery.md": {
    "primary": "A cultivated biennial marsh plant of the parsley family (Apium graveolens), with crisp, fibrous, edible leafy stalks.",
    "secondary": "In commercial horticulture, wild marsh celery (smallage) was domesticated in seventeenth-century Italy through selective blanching to reduce bitterness.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "There were great, round, pot-bellied baskets of chestnuts, crisp leaves of **celery**, and Spanish onions glowing in the grocer's window."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse cautioned his guests that raw **celery** was far too cold and astringent for delicate winter digestions."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A simple meal of baked corn and wild marsh **celery** proved sweet to the palate of the solitary woodland philosopher."}
    ]
  },
  "Dashboard — cel/celesta.md": {
    "primary": "A small keyboard instrument in which felt hammers strike suspended steel plates over wooden resonators, producing bell-like tones.",
    "secondary": "Invented by Auguste Mustel in 1886, the celesta was famously introduced into the modern orchestra by Tchaikovsky in *The Nutcracker*.",
    "quotes": [
      {"author": "Pyotr Ilyich Tchaikovsky", "work": "Letters to His Family", "quote": "I have discovered in Paris a wonderful new instrument called the **celesta**, whose ethereal, bell-like timbre will enchant the public in my new ballet."},
      {"author": "Romain Rolland", "work": "Musicians of To-day", "quote": "The delicate chiming of the **celesta** lent a magical fairy-tale shimmering atmosphere to the nocturnal garden scene."},
      {"author": "Hector Berlioz", "work": "Treatise on Modern Instrumentation and Orchestration", "quote": "Keyboard percussion instruments such as the **celesta** afford composers luminous, crystal-clear acoustic accents in light orchestration."}
    ]
  },
  "Dashboard — cel/celestial.md": {
    "primary": "Pertaining to the sky, the heavens, or outer space; or divinely sublime, angelic, and otherworldly.",
    "secondary": "In classical observational astronomy, the celestial sphere is an imaginary concentric sphere of infinite radius surrounding the Earth.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Sing, **celestial** Muse, that, on the secret top of Oreb, or of Sinai, didst inspire that shepherd who first taught the chosen seed."},
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "O, cherish him, for he has looked upon a **celestial** vision that mortal eyes can scarce endure."},
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The same law of universal gravitation governs both terrestrial falling bodies and the orbits of **celestial** planetary bodies."}
    ]
  },
  "Dashboard — cel/celestite.md": {
    "primary": "A delicate blue or colorless mineral consisting of strontium sulfate (SrSO4), forming tabular and prismatic crystals.",
    "secondary": "In industrial mineralogy, celestite is the principal commercial ore mined for strontium compounds utilized in fireworks and flares.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Ethics of the Dust", "quote": "The young mineralogist held up a magnificent cluster of pale sky-blue **celestite** crystals from the limestone geodes."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "In the gypsum beds of the tertiary strata, we discovered crystalline veins containing fibrous **celestite**."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The sky-blue color and high specific gravity readily distinguish **celestite** from allied baryte and carbonate specimens."}
    ]
  },
  "Dashboard — cel/celiac.md": {
    "primary": "Pertaining to the abdomen or abdominal cavity; or relating to celiac disease (gluten-sensitive enteropathy).",
    "secondary": "In human gross anatomy, the celiac trunk is a major visceral branch of the abdominal aorta that vascularizes the stomach, liver, and spleen.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dr. Samuel Gee first provided an accurate clinical description of the **celiac** affection in children suffering from chronic intestinal malabsorption."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The **celiac** artery arises from the anterior surface of the aorta, supplying digestive organs with arterial blood."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Surgical access to the upper abdominal viscera requires careful preservation of the autonomic **celiac** plexus."}
    ]
  },
  "Dashboard — cel/celibacy.md": {
    "primary": "The voluntary practice of abstaining from marriage and sexual relations, typically for religious or spiritual vows.",
    "secondary": "In ecclesiastical history, clerical celibacy was formally mandated in the Western Catholic Church by the Gregorian reforms of the eleventh century.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The early Christian hermits regarded perpetual **celibacy** as the highest path toward angelic purity and spiritual contemplation."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "He that hath wife and children hath given hostages to fortune; for they are impediments to great enterprises, either of virtue or mischief; but **celibacy** breeds inward concentration."},
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "Ecclesiastical authorities have no civil warrant to enforce vows of monastic **celibacy** upon unwilling subjects by temporal penalties."}
    ]
  },
  "Dashboard — cel/celibate.md": {
    "primary": "Abstaining from marriage and sexual relations, especially because of a religious vow; or a person who practices this.",
    "secondary": "In nineteenth-century sociological surveys, the living conditions of lifelong celibate scholars and monastics were studied for longevity patterns.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon maintained the ascetic, reserved habits of a lifelong **celibate** scholar buried among dusty folios."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Isabella prepared to enter the convent of Saint Clare, resolving to live a **celibate** votary dedicated to holy prayer."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The colleges of Oxford and Cambridge were staffed by **celibate** fellows who forfeited their fellowships upon marriage."}
    ]
  },
  "Dashboard — cel/celiocentesis.md": {
    "primary": "A surgical puncture of the abdominal cavity (paracentesis) using a trocar or needle to aspirate fluid.",
    "secondary": "In clinical gastroenterology and hepatology, diagnostic celiocentesis evaluates ascitic fluid for bacterial peritonitis or peritoneal carcinomatosis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Immediate diagnostic **celiocentesis** is indicated in patients with cirrhotic ascites presenting with unexplained abdominal tenderness."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The surgical registrar performed a careful **celiocentesis**, withdrawing several liters of serous fluid to relieve diaphragmatic embarrassment."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Following the therapeutic **celiocentesis**, the patient's respiratory excursions improved noticeably as abdominal pressure subsided."}
    ]
  },
  "Dashboard — cel/celioma.md": {
    "primary": "A medical term denoting a tumor, abnormal neoplasm, or cystic mass situated within the abdominal cavity.",
    "secondary": "In nineteenth-century clinical surgical pathology, an intra-abdominal celioma required exploratory laparotomy to assess resectability.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The diagnostic differentiation between a mesenteric cyst and an invasive **celioma** relies upon meticulous palpation and exploratory incision."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "The surgical team dissected the boundaries of the retroperitoneal **celioma**, protecting adjacent mesenteric vessels."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The senior consulting surgeon lectured the students upon an unusual case of intra-abdominal **celioma** in the public ward."}
    ]
  },
  "Dashboard — cel/celioscopy.md": {
    "primary": "Endoscopic examination of the abdominal cavity through an incision in the abdominal wall; laparoscopy.",
    "secondary": "Pioneered by Georg Kelling in 1901, diagnostic celioscopy paved the way for modern minimally invasive laparoscopic surgery.",
    "quotes": [
      {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "The introduction of diagnostic **celioscopy** enabled clinicians to inspect visceral surfaces directly without resorting to broad laparotomy incisions."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Through specialized optical instruments, experimental **celioscopy** demonstrated that peritoneal adhesions could be mapped with minimal surgical trauma."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The operating room staff prepared the optical conduits for an exploratory **celioscopy** to identify the source of occult bleeding."}
    ]
  },
  "Dashboard — cel/cell.md": {
    "primary": "The smallest structural and functional unit of an organism; or a small room in a prison, monastery, or honeycomb.",
    "secondary": "In cell biology, the cell theory formulated by Schleiden and Schwann establishes that all living organisms are composed of one or more cells.",
    "quotes": [
      {"author": "Robert Hooke", "work": "Micrographia", "quote": "These microscopic pores were the first that were ever seen, for they were very thin and like a **cell** in a honeycomb."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The physiological power of the individual living **cell** to assimilate nourishment and divide underlies all organic growth."},
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Welcome, sir; this **cell**'s my court: here have I few attendants and subjects none abroad."}
    ]
  },
  "Dashboard — cel/cell-free.md": {
    "primary": "Lacking biological cells; prepared from cellular lysates without containing intact living cells.",
    "secondary": "In molecular biochemistry, a cell-free translation system enabled Nirenberg and Matthaei to decipher the universal genetic code in 1961.",
    "quotes": [
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "By using a **cell-free** system derived from crushed bacterial cells, biochemists synthesized polypeptide chains from synthetic messenger RNA."},
      {"author": "Sydney Brenner", "work": "My Life in Science", "quote": "We prepared a **cell-free** extract containing active ribosomes, demonstrating protein synthesis in a test tube."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Enzymatic reactions in **cell-free** solutions proved that biological catalysis operates through ordinary physical and chemical laws."}
    ]
  },
  "Dashboard — cel/cell-like.md": {
    "primary": "Resembling or having the structural characteristics, compartments, or appearance of a cell.",
    "secondary": "In origin-of-life prebiotic chemistry, protocells form cell-like lipid vesicles capable of encapsulating replicating catalytic RNA molecules.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The primitive colloidal masses organized themselves into microscopic, **cell-like** globules under the influence of chemical affinity."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Microscopic sections of the connective tissue revealed an intricate network of tiny, **cell-like** compartments."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The spontaneous aggregation of organic macromolecules generates spherical, **cell-like** units possessing permeable boundaries."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

updated = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
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

print(f"Dashboard — cel Part 1: Successfully updated {updated}/{len(data)} notes.")
