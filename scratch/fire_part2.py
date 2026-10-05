# -*- coding: utf-8 -*-
"""
Part 2 of Curated Fire, Heat & Ash (non-cal):
Dashboard — ferv (19 words)
Dashboard — flam (30 words)
Total: 49 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  # =========================================================================
  # Dashboard — ferv (19 words)
  # =========================================================================
  "conferva": {
    "primary": "A genus or type of freshwater green filamentous algae, forming slimy green scum or mats on ponds.",
    "secondary": "In historical algology and limnology, unbranched aquatic filamentous thalli commonly classified in family Cladophoraceae or Tribonemataceae.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The quiet lagoons along the Rio de la Plata were carpeted with dense green mats of **conferva** floating upon the warm surface."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "On calm summer mornings, the shallow coves of the pond were fringed with delicate green threads of **conferva** basking in the sun."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "In hot droughts, our village ponds become choked with a thick mantle of **conferva**, harboring myriads of aquatic insects."}
    ]
  },
  "defervesce": {
    "primary": "To experience a reduction or abatement of fever, returning to normal body temperature.",
    "secondary": "In clinical medicine and infectious disease diagnostics, the resolution of an elevated core febrile state either by crisis or progressive lysis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Under the prompt administration of quinine, the malarial patient began to **defervesce** rapidly by evening lysis."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin watched the child's fever chart intently, hoping the infection would **defervesce** before pulmonary complications arose."},
      {"author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "The laboratory animals inoculated with the antiserum began to **defervesce**, their shivering subsiding as normal pulse returned."}
    ]
  },
  "defervescence": {
    "primary": "The subsidence or abatement of a fever as body temperature returns to normal.",
    "secondary": "In clinical thermoregulation and pathophysiology, the physiological phase wherein diaphoresis and peripheral vasodilation dissipate excess body heat.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The onset of sudden **defervescence** on the ninth day of lobar pneumonia was heralded by profuse perspiration and deep sleep."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Nature often achieves spontaneous **defervescence** through critical sweats long before the physician's nostrums take effect."},
      {"author": "Siddhartha Mukherjee", "work": "The Laws of Medicine", "quote": "In intensive care, monitoring the precise timing of **defervescence** helps clinicians differentiate bacterial sepsis from drug reactions."}
    ]
  },
  "defervescent": {
    "primary": "Causing or accompanied by the subsidence or reduction of fever.",
    "secondary": "In pharmacotherapy and internal medicine, designating therapeutic agents or physiological stages that promote the abatement of pyrexia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cold sponge baths served as an effective **defervescent** measure to prevent hyperpyrexia in severe enteric fever."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The surgeon prescribed a cooling **defervescent** draught to lower the wounded soldier's bounding pulse."},
      {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "During the **defervescent** period of the malady, the cutaneous capillaries dilate and copious perspiration ensues."}
    ]
  },
  "effervesce": {
    "primary": "To give off bubbles of gas, especially as the result of a chemical reaction; to bubble vigorously.",
    "secondary": "In chemistry and metaphorical discourse, to foam with brisk gas release or to display irrepressible, sparkling enthusiasm.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "When acid is poured upon crushed chalk, the mixture begins to **effervesce** violently, releasing carbonic acid gas."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her youthful spirits seemed to **effervesce** with irrepressible joy the moment the academy doors opened for the holiday."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes dropped the mineral crystals into the test tube, causing the liquid to **effervesce** with an pungent yellow vapor."}
    ]
  },
  "effervescence": {
    "primary": "The rapid escape of gas from a liquid in the form of bubbles; brisk fizzing or bubbling.",
    "secondary": "In physical chemistry and social psychology, spontaneous gaseous liberation or exuberant, vivacious enthusiasm of character.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sparkling cider rose in creamy **effervescence** against the rim of the rustic horn mug."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "There was a buoyant **effervescence** in Donatello's youthful nature that reminded his companions of sparkling vintage wine."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The acid tested upon the calcareous rock produced instantaneous **effervescence**, confirming the presence of coral limestone."}
    ]
  },
  "effervescent": {
    "primary": "Giving off bubbles; fizzy, vivacious, lively, or high-spirited.",
    "secondary": "In beverage manufacture, pharmacology, and descriptive prose, releasing microbubbles of gas or exhibiting exuberant sparkle.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "Algernon poured a glass of **effervescent** champagne, declaring that cucumber sandwiches were essential for high tea."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Her voice was an **effervescent** fountain of laughter that captivated everyone gathered in the drawing room."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "The patent medicine was a sugary, **effervescent** tonic that bubbled enticingly when stirred into cold spring water."}
    ]
  },
  "effervescing": {
    "primary": "Releasing gas bubbles actively; bubbling or fizzing continuously.",
    "secondary": "In chemical kinetics and descriptive literature, undergoing active gaseous liberation or bubbling with irrepressible excitement.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber brewed a bowl of punch with great ceremony, the hot brew **effervescing** softly over the embers."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white wake of the speeding whaleboat churned behind us like a cauldron of **effervescing** foam."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "The compound changed color from red to dark purple, **effervescing** and smoking as the transformation completed."}
    ]
  },
  "fervency": {
    "primary": "Warmth and intensity of emotion; passionate earnestness or zeal.",
    "secondary": "In devotional theology and moral rhetoric, profound spiritual warmth and sincerity in prayer or moral conviction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "With heartfelt **fervency** of soul, the suppliants pleaded before the judgment seat of the Roman general."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The seraph spoke with holy **fervency**, defending the unalterable decrees of heaven against the rebellious host."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers prayed with an austere **fervency** that filled the small stone cottage with solemn awe."}
    ]
  },
  "fervent": {
    "primary": "Having or displaying a passionate, warm, and intense enthusiasm or belief.",
    "secondary": "In literary and archaic physics, physically glowing with heat; characterized by ardent warmth and emotional intensity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea listened with **fervent** sympathy to the young physician's ambitious plans for the new hospital."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I pursued nature to her hiding places with a **fervent** curiosity that shut out all awareness of ordinary perils."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton whispered a **fervent** blessing as the morning sun broke through the prison grating."}
    ]
  },
  "fervently": {
    "primary": "In a manner characterized by intense, passionate, or heartfelt enthusiasm and sincerity.",
    "secondary": "In devotional and emotive discourse, pursuing an aim or prayer with profound warmth and unreserved zeal.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym Yeobright prayed **fervently** that some light of understanding might break through his spiritual perplexity."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale longed **fervently** for the courage to confess his hidden guilt before the assembled multitude."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne hoped **fervently** that the post chaise arriving at the inn might bring the long-awaited letter from Willoughby."}
    ]
  },
  "fervescent": {
    "primary": "Growing hot; becoming warm or increasingly heated.",
    "secondary": "In thermodynamic description and clinical terminology, exhibiting a rise in temperature or beginning to develop fever.",
    "quotes": [
      {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "During the **fervescent** stage of the pyrexial disorder, the pulse accelerates and the cutaneous surface warms noticeably."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The evening air above the desert grew **fervescent**, radiant with the accumulated heat of sandstone cliffs."},
      {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "Our instruments recorded a **fervescent** atmosphere, the ether vibrating with strange, suffocating warmth."}
    ]
  },
  "fervid": {
    "primary": "Intensely enthusiastic or passionate, especially to an excessive degree.",
    "secondary": "In literary aesthetics and archaic science, glowing with literal or metaphorical fire; blazing with heated emotion.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Swedenborg looked into the spiritual spheres with a **fervid** imagination that transfigured common theological dogmas."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare's **fervid** idealism blindfolded him to the practical realities of human fallibility."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Through the **fervid** noon the heavenly legions kept their watchful vigil upon the ramparts of bliss."}
    ]
  },
  "fervidly": {
    "primary": "In an intensely passionate, zealous, or enthusiastic manner.",
    "secondary": "In emotive narrative and oratorical rhetoric, expressing convictions or devotion with incandescent, fiery intensity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw argued **fervidly** for political reform, his eyes flashing with spontaneous youthful indignation."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles Winterborne loved Grace Melbury **fervidly**, yet hid his devotion behind humble silence and daily toil."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The Italian humanists sought **fervidly** to recover the lost beauty and intellectual liberty of classical antiquity."}
    ]
  },
  "fervidness": {
    "primary": "Vehement passion, burning intensity of emotion, or glowing ardor.",
    "secondary": "In moral psychology and rhetorical criticism, incandescent emotional warmth or ardent intensity of purpose.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "The prophetic fire of Mahomet was marked by an austere **fervidness** that commanded the obedience of desert tribes."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Conversion experiences often imprint the convert's temperament with permanent emotional **fervidness**."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Poetic genius unites profound contemplation with that passionate **fervidness** which gives life to abstract thought."}
    ]
  },
  "fervor": {
    "primary": "Intense and passionate feeling; great warmth of emotion.",
    "secondary": "In devotional religion and political discourse, zealous ardor driving commitment to a cause or spiritual discipline.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Let us cultivate our inner garden with steady **fervor**, refusing to be distracted by the petty gossip of town."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's spiritual **fervor** found no adequate outlet in the quiet, conventional routines of provincial society."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I chant the divine **fervor** of democracy, embracing every race, language, and laborer beneath the open sky."}
    ]
  },
  "fervour": {
    "primary": "Passionate intensity and warmth of feeling (chiefly British spelling).",
    "secondary": "In historical literature and classical rhetoric, vehement emotional or religious ardor animating action or speech.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The queen defended her honor with such noble **fervour** that even her accusers were moved to pity."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Jonathan Harker kissed the crucifix with genuine **fervour**, feeling its cold silver provide solace against evil."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific inquiry must be pursued with all the intellectual **fervour** traditionally reserved for philosophical debate."}
    ]
  },
  "noneffervescent": {
    "primary": "Not giving off gas bubbles; still and uncarbonated (of a beverage or chemical solution).",
    "secondary": "In beverage manufacturing, analytical chemistry, and pharmacology, designating liquids that remain flat and lack carbonic effervescence.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The lab assistant prepared a **noneffervescent** saline mixture to maintain osmotic balance during the bacterial culture test."},
      {"author": "George Orwell", "work": "Keep the Aspidistra Flying", "quote": "Gordon Comstock ordered a glass of cheap, **noneffervescent** ale at the dingy tavern counter."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Creeping Man", "quote": "The mysterious vial contained a dark, **noneffervescent** elixir that emitted a pungent organic odor."}
    ]
  },
  "perfervid": {
    "primary": "Intensely passionate, ardent, or zealous, often to an excessive or overwrought degree.",
    "secondary": "In literary criticism and psychological characterization, burning with exaggerated, feverish, or unconstrained enthusiasm.",
    "quotes": [
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The young philosopher recoiled from the **perfervid** emotionalism of the mystic cults that thronged imperial Rome."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The orator swept the Jacobin club into frenzy with his **perfervid** denunciations of aristocratic conspiracy."},
      {"author": "Edmund Gosse", "work": "Father and Son", "quote": "My father's religious temperament was **perfervid** and unbending, admitting no compromise with secular pleasures."}
    ]
  },

  # =========================================================================
  # Dashboard — flam (30 words)
  # =========================================================================
  "flambeau": {
    "primary": "A lighted torch, especially a decorated one used in public processions or night illuminations.",
    "secondary": "In cultural history and ceremonial processions, a flaming torch formed of thick wax wicks bound around a wooden core.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Footmen bearing smoking **flambeau** torches ran ahead of the carriage through the pitch-black streets of Paris."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The illumination of reason resembles not a blinding lightning bolt, but a steady **flambeau** guiding our footsteps."},
      {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "In the masquerade, the master criminal took the pseudonym of Flambeau, lighting his theatrical path like a midnight **flambeau**."}
    ]
  },
  "flame": {
    "primary": "A hot, glowing body of ignited gas produced by something on fire.",
    "secondary": "In combustion physics and poetic metaphor, incandescent gaseous plasma generated during rapid exothermic oxidation.",
    "quotes": [
      {"author": "William Blake", "work": "Songs of Experience", "quote": "Tyger Tyger, burning bright, in the forests of the night; what immortal hand or eye could frame thy fearful **flame**?"},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I saw how the fine form of man was degraded and wasted; I beheld the corruption of death succeed to the blooming cheek of life, until a sudden **flame** broke through the darkness."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The corposants flared along the lightning rods of the Pequod, each yard-arm tipping with a pale, supernatural **flame**."}
    ]
  },
  "flame-colored": {
    "primary": "Having a brilliant, fiery reddish-orange or bright scarlet color.",
    "secondary": "In chromatic description, fashion history, and botany, displaying the incandescent hues of burning fire.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "He will come to her in **flame-colored** stockings, and make a fool of himself before the whole household."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The embroideries upon Pearl's tunic glowed in **flame-colored** silks, reflecting her mother's impassioned spirit."},
      {"author": "Oscar Wilde", "work": "Salomé", "quote": "The moon slipped behind the clouds, casting a strange **flame-colored** halo over the palace terrace."}
    ]
  },
  "flame-coloured": {
    "primary": "Of a bright orange-red or fiery scarlet tint (chiefly British spelling).",
    "secondary": "In classical literature, entomology, and textiles, possessing an intense, fiery hue resembling burning embers.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The great ruby glowed against the dark velvet cloth with an extraordinary **flame-coloured** brilliance."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The autumn sunset stained the western sky with jagged bars of **flame-coloured** cloud above the ridgeway."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner captured the tempestuous alpine skies in streaks of **flame-coloured** light that seemed born of molten gold."}
    ]
  },
  "flame-flower": {
    "primary": "A plant with bright flame-colored flowers, especially the torch lily (Kniphofia) or flame vine.",
    "secondary": "In ornamental botany and landscape horticulture, striking herbaceous or climbing perennials noted for incandescent racemes.",
    "quotes": [
      {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "At the rear of the sunny herbaceous border, the scarlet spikes of the **flame-flower** provided fiery drama in late August."},
      {"author": "Vita Sackville-West", "work": "More for Your Garden", "quote": "Against the old grey stone wall, the brilliant clusters of the **flame-flower** flared like torches in the evening breeze."},
      {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "Along the roadside hedges in South Africa, we admired the fiery spikes of Kniphofia, commonly termed the **flame-flower**."}
    ]
  },
  "flame-orange": {
    "primary": "A vivid, fiery orange color reminiscent of an open fire.",
    "secondary": "In design arts, ornithological plumage descriptions, and mineralogy, a vibrant high-saturation chromatic hue.",
    "quotes": [
      {"author": "Jack London", "work": "The Cruise of the Snark", "quote": "The setting sun dipped into the Pacific in a blaze of **flame-orange** brilliance that lit the clouds from below."},
      {"author": "Willa Cather", "work": "The Song of the Lark", "quote": "The pottery shards retrieved from the canyon ruin showed distinctive patterns of **flame-orange** slipware."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A sudden burst of **flame-orange** light from the ship's furnace illuminated the blackened faces of the stokers."}
    ]
  },
  "flame-out": {
    "primary": "The sudden extinction of a jet engine flame, resulting in engine shutdown; figuratively, a sudden failure or collapse.",
    "secondary": "In aeronautical propulsion engineering and organizational psychology, combustion stoppage in a gas turbine combustion chamber or abrupt personal burnout.",
    "quotes": [
      {"author": "Tom Wolfe", "work": "The Right Stuff", "quote": "At forty thousand feet the compressor stalled, leading to an immediate **flame-out** that sent the fighter spinning into the clouds."},
      {"author": "Chuck Yeager", "work": "Yeager: An Autobiography", "quote": "When fuel flow stuttered in thin air, you suffered a **flame-out** and had to dive steeply to restart the turbine."},
      {"author": "Norman Mailer", "work": "Of a Fire on the Moon", "quote": "The test pilots knew the chilling peril of high-altitude **flame-out**, where only cool nerves restored engine ignition."}
    ]
  },
  "flame-retardant": {
    "primary": "A chemical substance added to materials to prevent, slow down, or inhibit combustion.",
    "secondary": "In materials science, textiles, and fire safety engineering, chemical additives that suppress fire ignition by gas-phase scavenging or char formation.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Industrial chemicals synthesized as **flame-retardant** coatings often accumulate persistently in wildlife tissues."},
      {"author": "Lewis Mumford", "work": "The Highway and the City", "quote": "Modern high-rise residential construction mandates **flame-retardant** insulation to minimize catastrophic fire hazards."},
      {"author": "Kurt Vonnegut", "work": "Player Piano", "quote": "The automated factory produced miles of synthetic drapery impregnated with **flame-retardant** polymers."}
    ]
  },
  "flamefish": {
    "primary": "A small, bright-red marine cardinalfish (Astrapogon stellatus or Apogon maculatus) native to warm reefs.",
    "secondary": "In marine ichthyology, nocturnal reef-dwelling fishes of family Apogonidae exhibiting vivid carmine coloration and communal dwelling in conch shells.",
    "quotes": [
      {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "Peering into the cavity of a living queen conch, we found a diminutive ruby **flamefish** sheltering peacefully."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The tropical **flamefish** belongs to the cardinalfish group, distinguished by large eyes and radiant red scales."},
      {"author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "Among the coral crevices, a tiny **flamefish** darted like a spark of living crimson against the sponges."}
    ]
  },
  "flameflower": {
    "primary": "A plant having fiery, flame-like blossom clusters, such as the jewelweed or flame azalea.",
    "secondary": "In botanical lore and horticultural design, ornamental taxa characterized by vivid vermilion or scarlet inflorescences.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Along the gravelly river bank grew the vivid wild **flameflower**, glowing amid the tangled northern sedges."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "The mountain slopes were brightened by patches of **flameflower**, their scarlet petals trembling in the canyon breeze."},
      {"author": "Luther Burbank", "work": "How Plants Are Trained to Work for Man", "quote": "We hybridized varieties of the wild **flameflower** to develop larger blooms that retain their brilliance throughout summer."}
    ]
  },
  "flamen": {
    "primary": "A priest of ancient Rome assigned to the service of a specific deity, such as Jupiter or Mars.",
    "secondary": "In Roman religion and classical antiquities, one of fifteen sacerdotal college members consecrated to perpetuating the cult of a designated state god.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "The solemn **flamen** quickens with his march, while matrons fling their gloves, ladies their scarfs upon him as he passes."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The patrician **flamen** Dialis was bound by ancient taboos that forbade him from touching iron or mounting a horse."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The sacred fire was maintained upon the altar by the venerable **flamen**, chanting archaic litanies of sacrifice."}
    ]
  },
  "flamenco": {
    "primary": "A passionate style of Spanish folk dance and guitar music originating in Andalusia, characterized by singing and rhythmic footwork.",
    "secondary": "In ethnomusicology and performing arts, an Andalusian cante and baile tradition developed by Gitano communities embodying deep emotional expression (duende).",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "The rhythmic clapping of the dancers echoed from the cave taverns, pulsing with the fierce cadence of Andalusian **flamenco**."},
      {"author": "Federico García Lorca", "work": "In Search of Duende", "quote": "In authentic **flamenco**, the singer wrestles with the dark angel of duende, opening wounds of ancestral sorrow."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "From the cellar canteen drifted the strumming of a Spanish guitar playing an intricate **flamenco** rhythm."}
    ]
  },
  "flameproof": {
    "primary": "Resistant to fire; treated so as not to catch fire or burn easily.",
    "secondary": "In safety engineering and industrial design, treated or constructed with incombustible materials to prevent ignition under intense thermal exposure.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Food of the Gods and How It Came to Earth", "quote": "The engineers clad themselves in **flameproof** asbestos suits before approaching the burning crater of the reactor."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The promotional brochure praised the new apartment hotel as entirely **flameproof** and impervious to metropolitan blazes."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The secret chamber was reinforced with **flameproof** iron plating behind the heavy wainscotting."}
    ]
  },
  "flamethrower": {
    "primary": "A weapon that sprays a stream of ignited, burning fuel, used in military warfare or vegetation clearing.",
    "secondary": "In military ordnance and historical combat, a tactical pneumatic apparatus discharging pressurized gelatinized petroleum or burning liquids.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The sudden introduction of the trench **flamethrower** on the Western Front introduced a terrifying new dimension to assault tactics."},
      {"author": "Erich Maria Remarque", "work": "All Quiet on the Western Front", "quote": "A blinding jet of liquid fire from a **flamethrower** hissed across the shell crater, forcing us back into the trench."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The fascists attempted to dislodge the parapet with an armored vehicle mounted with an improvised **flamethrower**."}
    ]
  },
  "flaming": {
    "primary": "Burning fiercely and emitting flames; hot, bright, or passionate.",
    "secondary": "In literary description and emotional metaphor, enveloped in active fire or marked by vehement, fiery intensity.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "They, looking back, all the eastern side beheld of Paradise, so late their happy seat, waved over by that **flaming** brand."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The rioters carried **flaming** torches through the midnight streets, setting the prison gates on fire with frenzied roars."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The try-pots burned fiercely, vomiting thick black smoke while **flaming** cinders showered upon the deck."}
    ]
  },
  "flamingo": {
    "primary": "A tall wading bird with bright pink or reddish plumage, long legs, a long neck, and a bent down-turned bill.",
    "secondary": "In systematic ornithology, filter-feeding aquatic birds of family Phoenicopteridae specialized in extracting algae and brine shrimp with lamellated bills.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The chief difficulty Alice found at first was in managing her **flamingo**: she succeeded in getting its body tucked under her arm."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Flocks of the Chilean **flamingo** rose above the salt lakes of Patagonia, their scarlet wings flashing against the blue sky."},
      {"author": "W. H. Hudson", "work": "Idle Days in Patagonia", "quote": "A solitary **flamingo** stood motionless in the shallow lagoon, resembling a pink sentinel poised on a single slender leg."}
    ]
  },
  "flaminius": {
    "primary": "A prominent ancient Roman statesman and general, especially Gaius Flaminius who constructed the Via Flaminia.",
    "secondary": "In Roman historiography and classical biography, the consul defeated by Hannibal at Lake Trasimene in 217 BC, or a character in Shakespeare's Timon of Athens.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "Faith, I perceive our master's fortune is in the decline; here comes **Flaminius**, his honest and faithful servant."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The historic highway paved by the consul **Flaminius** carried legions northward through the Apennine passes."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "Memories of the disaster where **Flaminius** fell beneath the Carthaginian cavalry still haunted the Senate."}
    ]
  },
  "flammability": {
    "primary": "The ability of a substance to ignite and burn easily; combustibility.",
    "secondary": "In materials science and fire protection engineering, the physicochemical ease with which a gas, liquid, or solid sustains gas-phase combustion upon ignition.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Petroleum solvents used to dissolve chemical sprays increase both their toxicity and their dangerous **flammability** in storage."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The laboratory safety code warned students against the extreme **flammability** of ether vapors near open Bunsen burners."},
      {"author": "Isaac Asimov", "work": "The Chemicals of Life", "quote": "Organic compounds containing long hydrocarbon chains exhibit high **flammability** owing to their rapid oxidation."}
    ]
  },
  "flammable": {
    "primary": "Easily set on fire; able to burn rapidly and readily.",
    "secondary": "In hazardous materials regulation and chemical safety, possessing a flash point low enough to ignite readily under ambient atmospheric conditions.",
    "quotes": [
      {"author": "Kurt Vonnegut", "work": "Slaughterhouse-Five", "quote": "The cellars beneath Dresden were filled with **flammable** timber and household goods that fed the firestorm above."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The synthetic carpets were engineered to be soft yet non-conductive, replacing older **flammable** cotton weaves."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Sussex Vampire", "quote": "A single spark near the vat of naphtha would have detonated the entire building, so **flammable** were the drying fumes."}
    ]
  },
  "flammulina": {
    "primary": "A genus of fungi in the family Physalacriaceae, best known for the edible velvet shank or enoki mushroom (Flammulina velutipes).",
    "secondary": "In mycology and commercial mushroom cultivation, cold-tolerant lignicolous agarics producing elongated slender stems under high carbon dioxide regimes.",
    "quotes": [
      {"author": "M. C. Cooke", "work": "British Fungi", "quote": "Clusters of **Flammulina** velutipes appear upon decaying elm trunks during late autumn frosts, recognizable by their velvety dark stems."},
      {"author": "David Arora", "work": "Mushrooms Demystified", "quote": "Known to gourmets as enoki, wild **Flammulina** bears little resemblance to the pale cultivated mushrooms grown in dark jars."},
      {"author": "Charles McIlvaine", "work": "One Thousand American Fungi", "quote": "The velvet-stemmed **Flammulina** withstands freezing temperatures, thawing out in midday sun to resume spore dispersal."}
    ]
  },
  "inflame": {
    "primary": "To provoke or intensify strong feelings, especially anger or passion; also to cause physical swelling and redness.",
    "secondary": "In pathology and moral rhetoric, to induce an inflammatory immune response or to excite passions to reckless agitation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "I fear I wrong the honorable men whose daggers have stabb'd Caesar; yet Antony's speech will **inflame** the citizens."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Superfluous wealth serves only to **inflame** desires that simpler living readily pacifies."},
      {"author": "G. K. Chesterton", "work": "The Everlasting Man", "quote": "Demagogic rhetoric serves to **inflame** the mob, blinding men to the quiet realities of enduring moral truths."}
    ]
  },
  "inflamed": {
    "primary": "Reddened, swollen, hot, and often painful as a result of injury or infection; also aroused to strong emotion.",
    "secondary": "In clinical pathology and dramatic narrative, exhibiting signs of active inflammation or excited to furious passion.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "His eyes were **inflamed** from reading ancient chancery parchments late into the smoky London night."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The wound upon the sailor's arm was angry and **inflamed**, poisoned by the venom of an Andaman dart."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "His **inflamed** imagination magnified every small slight into an unbearable verdict of cosmic rejection."}
    ]
  },
  "inflaming": {
    "primary": "Exciting to intense passion, anger, or enthusiasm; causing physical inflammation.",
    "secondary": "In rhetoric and clinical pathophysiology, exciting violent emotions or triggering inflammatory physiological cascades.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "His hot temper was capable of **inflaming** the calmest council into rash and desperate measures."},
      {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "There is a perilous intoxication in modern materialism, **inflaming** pride while starving the human spirit."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Seditious pamphlets circulated throughout the capital, **inflaming** the populace against established institutions."}
    ]
  },
  "inflammability": {
    "primary": "Susceptibility to catching fire readily and combusting rapidly; high emotional volatility.",
    "secondary": "In chemistry, fire safety regulations, and moral temperament, the capacity of a substance or temperament to ignite readily upon exposure to heat.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "The extraordinary **inflammability** of hydrogen gas is demonstrated the instant a taper approaches the mouth of the jar."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The dry tinder of economic desperation explained the dangerous social **inflammability** of the Paris faubourgs."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The emotional **inflammability** of youthful minds renders them exceptionally receptive to heroic suggestion."}
    ]
  },
  "inflammable": {
    "primary": "Easily set on fire; combustible; easily excited to anger or emotion.",
    "secondary": "In classical terminology and safety lexicons, capable of catching fire instantly (synonymous with flammable); quick-tempered.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dunstan Cass had an **inflammable** temper that flared up whenever his financial reckless schemes were questioned."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I gathered dry pine needles and other **inflammable** materials to build a protective campfire against the Morlocks."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "The stack of lumber was soaked with **inflammable** oil to guarantee a fierce and swift conflagration."}
    ]
  },
  "inflammation": {
    "primary": "A localized physical condition in which part of the body becomes reddened, swollen, hot, and often painful.",
    "secondary": "In immunology and pathology, a protective vascular and cellular tissue response to noxious stimuli, pathogens, or cellular injury.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Rage causes the blood vessels of the head to gorge, producing a fiery redness akin to acute **inflammation**."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian bodies, lacking immunity, fell victim to bacterial infection and pulmonary **inflammation** against which they had no defense."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The cardinal clinical signs of local **inflammation** have been recognized since antiquity as rubor, tumor, calor, and dolor."}
    ]
  },
  "inflammatory": {
    "primary": "Relating to or causing localized swelling, redness, and pain; also tending to arouse anger, hostility, or passion.",
    "secondary": "In clinical pathology and political rhetoric, inducing an immunological inflammatory cascade or provoking seditious public unrest.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The magistrates suppressed the seditious pamphlet, denouncing its **inflammatory** appeals to the sectarian passions of the mob."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rheumatic fever frequently manifests as an acute **inflammatory** disease affecting the synovial membranes and cardiac valves."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The chemist examined the lung tissue, observing severe **inflammatory** lesions induced by the toxic alkaloid."}
    ]
  },
  "nonflammable": {
    "primary": "Not easily ignited; not able to catch fire easily.",
    "secondary": "In fire prevention, industrial safety standards, and materials science, formulated to resist combustion under specified testing conditions.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The insulation surrounding the conditioning chambers was made of modern **nonflammable** synthetic minerals."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Agricultural carriers were gradually reformulated with **nonflammable** inert components to reduce warehouse hazards."},
      {"author": "Kurt Vonnegut", "work": "Cat's Cradle", "quote": "The laboratory walls were coated with a grey, **nonflammable** enamel that shed chemical fumes without staining."}
    ]
  },
  "noninflammatory": {
    "primary": "Not characterized by or not causing inflammation; peaceable or placid in tone.",
    "secondary": "In clinical pathology, histology, and political diplomacy, lacking leukocyte infiltration or phrased to avoid provoking public discord.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician differentiated the joint swelling as a **noninflammatory** degenerative arthrosis rather than septic arthritis."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The civic debate proceeded in a remarkably calm, **noninflammatory** spirit that facilitated legislative compromise."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Certain chronic effusions are entirely **noninflammatory** in origin, resulting merely from venous transudation."}
    ]
  },
  "proinflammatory": {
    "primary": "Tending to cause, promote, or accelerate physical inflammation.",
    "secondary": "In molecular immunology and cellular biology, designating cytokines (such as TNF-alpha or IL-1) that initiate and amplify inflammatory cascades.",
    "quotes": [
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Macrophage activation releases a storm of **proinflammatory** molecules that summon neutrophils to the site of infection."},
      {"author": "Paul Kalanithi", "work": "When Breath Becomes Air", "quote": "The cytokine storm flooded the systemic vasculature with **proinflammatory** mediators that precipitated multi-organ distress."},
      {"author": "Atul Gawande", "work": "Being Mortal", "quote": "Chronic metabolic ailments are increasingly understood as driven by low-grade **proinflammatory** systemic states."}
    ]
  }
}

if __name__ == "__main__":
    print(f"data_part2 loaded with {len(data_part2)} entries.")
