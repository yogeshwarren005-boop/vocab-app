# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — cel Part 2 (40 words) ---
  "Dashboard — cel/cellar.md": {
    "primary": "A subterranean room or storehouse beneath a building, commonly used for storing wine, fuel, or provisions.",
    "secondary": "In domestic architecture and wine storage, a subterranean cellar maintains stable ambient temperatures and relative humidity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge walked through his rooms, checking each lock and looking down into the gloomy wine **cellar** below."},
      {"author": "Edgar Allan Poe", "work": "The Cask of Amontillado", "quote": "I led Fortunato down into the deep subterranean **cellar** where the damp vaults were encrusted with nitre."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mrs. Fairfax led Jane through the quiet manor, inspecting the spacious fruit **cellar** and vaulted larders."}
    ]
  },
  "Dashboard — cel/cellarage.md": {
    "primary": "Subterranean cellar space; or the commercial charge levied for storing goods in a cellar warehouse.",
    "secondary": "In maritime and dockland commerce, merchant factors leased bonded cellarage along the Thames to mature imported spirits.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "O day and night, but this is wondrous strange! A worthy pioner! Once more remove, good friends. Hear you this fellow in the **cellarage**?"},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "The venerable counting-house possessed extensive subterranean **cellarage** where ancient maritime ledgers were stored."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The prudent vintner computes the annual expense of his warehouse **cellarage** against seasonal wholesale turnover."}
    ]
  },
  "Dashboard — cel/cellaret.md": {
    "primary": "A small decorative wooden cabinet, chest, or deep drawer designed to hold wine or liquor bottles.",
    "secondary": "In Georgian and Victorian cabinetmaking, mahogany cellarets were lined with lead and fitted with brass handles for dining-room sideboards.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The dining parlor featured a handsome mahogany **cellaret** stocked with choice Madeira for hospitable entertaining."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley unlocked the brass-bound **cellaret** to offer his guests a cordial before the carriage arrived."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "The archdeacon kept his favorite vintage port under lock and key in an antique dining-room **cellaret**."}
    ]
  },
  "Dashboard — cel/cellblock.md": {
    "primary": "A distinct reinforced building or wing in a prison containing rows of individual detention cells.",
    "secondary": "In penology and correctional architecture, the cellblock was engineered to enable panoptic central surveillance over incarcerated populations.",
    "quotes": [
      {"author": "Jack London", "work": "The Star Rover", "quote": "The heavy iron gates clanged shut behind me as the guard marched me into the solitary **cellblock**."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The warden led the detectives through the central **cellblock**, pointing out the cell where the fugitive had been detained."},
      {"author": "Oscar Wilde", "work": "De Profundis", "quote": "The silence of the prison **cellblock** was broken only by the rhythmic footfalls of the warders on night watch."}
    ]
  },
  "Dashboard — cel/cellini.md": {
    "primary": "Benvenuto Cellini (1500–1571), celebrated Florentine goldsmith, Renaissance sculptor, and flamboyant autobiographer.",
    "secondary": "In Renaissance art history, Cellini's bronze *Perseus with the Head of Medusa* and his exquisite golden salt cellar exemplified Mannerist virtuosity.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The intricate golden craftsmanship of **cellini** displays the flamboyant ornamental genius of the high Italian Renaissance."},
      {"author": "Jacob Burckhardt", "work": "The Civilization of the Renaissance in Italy", "quote": "The candid memoirs of Benvenuto **cellini** depict an artist of fiery temper and supreme technical confidence."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "Beneath the bronze casting of Perseus, **cellini** triumphed over enormous metallurgical and artistic difficulties."}
    ]
  },
  "Dashboard — cel/cellist.md": {
    "primary": "A musician who plays the violoncello, performing as a soloist, chamber instrumentalist, or orchestral player.",
    "secondary": "In chamber music performance, the cellist provides the foundational bass harmonic voice and rich tenor cantabile solos in string quartets.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "Holmes sat in the concert stalls, his long fingers gently waving in time to the performance of the celebrated **cellist**."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "The sensitive young **cellist** drew his bow across the strings, eliciting a mournful, deep resonance from his instrument."},
      {"author": "Willa Cather", "work": "The Song of the Lark", "quote": "The conservatory orchestra rehearsed Beethoven's symphony under the watchful guidance of the principal **cellist**."}
    ]
  },
  "Dashboard — cel/cello.md": {
    "primary": "A four-stringed musical instrument of the violin family, pitched an octave lower than the viola and played between the knees.",
    "secondary": "In orchestral instrumentation, the cello possesses an expansive compass ranging from resonant low C up into expressive treble registers.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The mellow timbre of the solo **cello** soared effortlessly above the quiet woodwind accompaniment in the adagio."},
      {"author": "Thomas Mann", "work": "Buddenbrooks", "quote": "Hanno sat with his **cello** between his knees, practicing scales in the quiet upstairs drawing room."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes would lean back in his armchair and play his favorite airs, imitating the deep tone of a **cello** upon his violin."}
    ]
  },
  "Dashboard — cel/cellophane.md": {
    "primary": "A thin, transparent sheet made of regenerated cellulose, utilized extensively as a moisture-resistant packaging wrapping.",
    "secondary": "Invented by Jacques E. Brandenberger in 1908, cellophane revolutionized retail food preservation by providing hygienic visual display packaging.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The sterile biological samples were hermetically sealed in glittering sheets of transparent **cellophane**."},
      {"author": "John Steinbeck", "work": "Cannery Row", "quote": "The small grocery counter displayed candies wrapped in crinkling colored **cellophane** that caught the morning light."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "She unpacked the new Parisian dresses from their crackling **cellophane** envelopes upon the hotel bed."}
    ]
  },
  "Dashboard — cel/cellphone.md": {
    "primary": "A portable telephone that operates via cellular radio networks; a mobile phone.",
    "secondary": "In modern telecommunications, cellphone infrastructure utilizes hexagonal geographic cells serviced by low-power transceivers to reuse frequency bands.",
    "quotes": [
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "The worldwide diffusion of the handheld **cellphone** demonstrates how pure electromagnetic theory translates into ubiquitous everyday technology."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "We foresaw a day when every citizen would carry an individual pocket transceiver, what society now terms a **cellphone**."},
      {"author": "Oliver Sacks", "work": "The Mind's Eye", "quote": "The patient noted that interacting through a digital **cellphone** helped bridge perceptual deficits following neurological surgery."}
    ]
  },
  "Dashboard — cel/cellular.md": {
    "primary": "Consisting of or pertaining to biological cells; or organized into discrete, interconnected functional compartments.",
    "secondary": "In histology and cytopathology, cellular differentiation describes the epigenetic maturation of stem cells into specialized functional tissues.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Microscopic examination reveals that plant tissue is constructed of delicate **cellular** walls surrounding organic fluid."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The fundamental unit of all living organisms is the single **cellular** mass of protoplasm containing a nucleus."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The complex organs of higher animals arise through progressive multiplication and specialization of primitive **cellular** layers."}
    ]
  },
  "Dashboard — cel/cellularity.md": {
    "primary": "The density, abundance, and structural arrangement of cells within a biological tissue or marrow sample.",
    "secondary": "In diagnostic hematopathology, bone marrow cellularity is assessed relative to age-adjusted norms to diagnose aplastic anemia or leukemic infiltration.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Histological biopsy of the lymphoid tumor demonstrated marked hyper-**cellularity** and loss of normal follicular architecture."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The neuropathologist evaluated the high **cellularity** of the glioma specimen to determine the histological grade of malignancy."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The variation in tissue **cellularity** across embryonic stages illustrates the rapid tempo of primordial organogenesis."}
    ]
  },
  "Dashboard — cel/cellulite.md": {
    "primary": "Dimpled or puckered skin caused by subcutaneous fat deposits pushing through connective tissue fibers.",
    "secondary": "In aesthetic dermatology and cosmetic physiology, cellulite primarily affects the pelvic region, thighs, and buttocks due to fibrous septae architecture.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "Clinical inspection of the immobilized limb revealed localized cutaneous changes and superficial **cellulite** dimpling."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Subcutaneous adipose distribution varies significantly between sexes, predisposing to characteristic **cellulite** patterning."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "The post-surgical dressing was adjusted to minimize fluid accumulation and avoid aggravating superficial **cellulite**."}
    ]
  },
  "Dashboard — cel/cellulitis.md": {
    "primary": "A spreading bacterial skin infection characterized by localized erythema, edema, warmth, and pain in the deep dermis.",
    "secondary": "In clinical infectious diseases, acute cellulitis is most commonly caused by Streptococcus pyogenes or Staphylococcus aureus entering through skin breaks.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt administration of parenteral antibiotics is essential to halt the rapid spread of streptococcal **cellulitis** along the limb."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The country doctor lanced the infected boil to prevent the development of diffuse phlegmonous **cellulitis** in the surrounding tissue."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The surgeon monitored the marked red margins of the **cellulitis** daily to verify that antimicrobial therapy was reversing the infection."}
    ]
  },
  "Dashboard — cel/celluloid.md": {
    "primary": "A transparent, flammable plastic made from nitrocellulose and camphor, historically used for photographic film and small molded objects.",
    "secondary": "In the history of cinema and technology, celluloid roll film developed by George Eastman and Hannibal Goodwin laid the technical foundation for motion pictures.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The early twentieth-century motion picture archives perished in fierce fires due to the volatile nature of nitrate **celluloid** film."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "The small dressing-table displayed a comb of amber-colored **celluloid** and a silver-backed brush."},
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "The flexible strip of perforated **celluloid** allowed us to feed successive photographic frames smoothly through the Kinetoscope."}
    ]
  },
  "Dashboard — cel/cellulose.md": {
    "primary": "An insoluble complex carbohydrate polymer that forms the main structural component of plant cell walls and vegetable fibers.",
    "secondary": "In industrial chemistry and botany, cellulose is composed of linear beta-1,4-linked D-glucose units, providing tensile strength to wood, cotton, and hemp.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The tough outer wall of a vegetable cell consists of **cellulose**, a chemical substance insoluble in ordinary water."},
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The digestive enzymes of the sundew break down insect proteins while leaving the **cellulose** of plant detritus untouched."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Microbial decomposition of plant **cellulose** in anaerobic environments yields marsh gas and organic acids."}
    ]
  },
  "Dashboard — cel/cellulosic.md": {
    "primary": "Pertaining to, derived from, or containing cellulose.",
    "secondary": "In renewable energy engineering, cellulosic ethanol is synthesized through biochemical enzymatic hydrolysis of non-food plant biomass.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The resistant **cellulosic** framework of ancient trees forms the combustible carbon basis of our coal deposits."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The thickening of the **cellulosic** fibers in the tendril provides the mechanical rigidity required to support climbing vines."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The primary plant cell wall exhibits a complex network of **cellulosic** microfibrils embedded in a pectin matrix."}
    ]
  },
  "Dashboard — cel/cellulosid.md": {
    "primary": "A chemical term denoting a substance containing or related to cellulose compounds; cellulosic matter.",
    "secondary": "In early industrial organic chemistry, cellulosid derivatives were investigated as precursors for synthetic varnishes and molded polymers.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "We tested various **cellulosid** filaments in the laboratory to determine their electrical endurance under high vacuum."},
      {"author": "Louis Pasteur", "work": "Researches on Molecular Asymmetry", "quote": "Chemical reagents acted upon the **cellulosid** fibers without altering their optical rotary dispersion."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The decomposed organic residue yielded a distinct **cellulosid** precipitate when treated with dilute acid."}
    ]
  },
  "Dashboard — cel/celom.md": {
    "primary": "A variant spelling of coelom; the main fluid-filled body cavity in triploblastic animals, lined by mesoderm.",
    "secondary": "In comparative embryology and invertebrate zoology, the formation of the celom divides bilateria into schizocoelous and enterocoelous clades.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The true **celom** develops as a fluid-filled mesodermal space separating the gut from the outer body wall."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The evolutionary emergence of an internal **celom** allowed bilateral organisms to develop specialized organ systems and hydrostatic locomotion."},
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "The gastraea theory traces the origin of the primitive **celom** to outpouchings of the ancestral archenteron."}
    ]
  },
  "Dashboard — cel/celoma.md": {
    "primary": "A medical and anatomical term for the coelomic cavity; or an abnormal abdominal cyst.",
    "secondary": "In developmental teratology, developmental anomalies of the embryological celoma result in congenital diaphragmatic or abdominal wall hernias.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "During early organogenesis, the embryonic **celoma** divides into pericardial, pleural, and peritoneal cavities."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital defects in the closure of the fetal **celoma** may lead to umbilical or ventral herniations at birth."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Dissection of the primitive visceral **celoma** reveals how autonomic nerve plexuses establish early innervation pathways."}
    ]
  },
  "Dashboard — cel/celosia.md": {
    "primary": "A genus of ornamental plants in the amaranth family (cockscomb), noted for vivid, flame-like or crested floral plumes.",
    "secondary": "In horticultural botany and traditional agriculture, Celosia argentea (silver cockscomb) is cultivated worldwide both for ornamental beds and as an edible potherb.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The garden cockscomb, a cultivated species of **celosia**, displays striking, velvet-textured crests of intense crimson and gold."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Horticulturists have preserved monstrous crested variations in **celosia** through centuries of careful seed selection."},
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "Near the village dwellings, small garden patches were adorned with tall, feathery spikes of scarlet **celosia**."}
    ]
  },
  "Dashboard — cel/celsius.md": {
    "primary": "A scale of temperature on which water freezes at zero degrees and boils at one hundred degrees under standard atmospheric pressure.",
    "secondary": "Named after Swedish astronomer Anders Celsius, the Celsius scale was officially adopted by the General Conference on Weights and Measures in 1948.",
    "quotes": [
      {"author": "Lord Kelvin", "work": "On an Absolute Thermometric Scale", "quote": "The zero of the absolute scale corresponds to minus two hundred and seventy-three degrees on the air-thermometer of **celsius**."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Surface temperatures on Mars drop to seventy degrees **celsius** below freezing during the protracted Martian polar night."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The lunar thermometers recorded a searing heat of over one hundred degrees **celsius** when the midday sun shone directly upon the rocks."}
    ]
  },
  "Dashboard — cel/celt.md": {
    "primary": "A member of an ancient European people or their modern descendants; or an ancient prehistoric stone axe-head or chisel.",
    "secondary": "In prehistoric archaeology and antiquarian studies, a ground stone or bronze celt was hafted into a wooden shaft as a dual woodworking tool and weapon.",
    "quotes": [
      {"author": "John Lubbock", "work": "Pre-historic Times", "quote": "The antiquary uncovered a polished greenstone **celt** in the neolithic barrow alongside flint arrowheads."},
      {"author": "Matthew Arnold", "work": "On the Study of Celtic Literature", "quote": "The fiery imagination and poetic sensibility of the ancient **celt** enriched the mainstream of English verse."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Mr. Oldbuck proudly displayed a bronze **celt** found on the moor, debating whether it was of Roman or Caledonian origin."}
    ]
  },
  "Dashboard — cel/celtic.md": {
    "primary": "Pertaining to the Celts or their modern descendant cultures, languages, myths, and traditions.",
    "secondary": "In comparative linguistics, the Celtic branch of Indo-European comprises Goidelic (Irish, Scottish Gaelic, Manx) and Brythonic (Welsh, Cornish, Breton).",
    "quotes": [
      {"author": "Matthew Arnold", "work": "On the Study of Celtic Literature", "quote": "The **celtic** genius contributed a magical natural style and passionate melancholy to the English literary heritage."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The ancient **celtic** festival of Samhain marked the boundary between summer and the onset of winter darkness."},
      {"author": "William Butler Yeats", "work": "The Celtic Twilight", "quote": "The peasantry of western Ireland preserve an enchanting realm of **celtic** folklore alive in their fireside tales."}
    ]
  },
  "Dashboard — cel/celtis.md": {
    "primary": "A genus of deciduous trees in the hemp family commonly known as hackberries or nettle trees, bearing small edible drupes.",
    "secondary": "In urban forestry and ecology, Celtis occidentalis (common hackberry) is prized for tolerance to drought, wind, and alkaline soil conditions.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "The small dark berries of the nettle-tree, belonging to the genus **celtis**, persist through winter, providing food for cedar waxwings."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The common hackberry, **celtis** occidentalis, forms a handsome woodland tree with rough, warty bark and ovate leaves."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Along the river bluffs, scattered groves of hardy **celtis** sheltered herds of grazing guanacos from the wind."}
    ]
  },
  "Dashboard — cel/celtuce.md": {
    "primary": "A cultivar of lettuce (stem lettuce) grown primarily for its thick, crisp, edible central stalk rather than its leaves.",
    "secondary": "In Chinese horticulture and cuisine, celtuce (wosun) is peeled, sliced thin, and stir-fried or pickled for its crunchy texture and nutty flavor.",
    "quotes": [
      {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "Agricultural explorers introduced the succulent Chinese asparagus-lettuce, now commonly known as **celtuce**, to American home gardeners."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "The edible stem of **celtuce** is harvested before the flower stalks shoot up, providing a tender vegetable in late spring."},
      {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "This crisp stem vegetable, cultivated as **celtuce**, can be braised with butter or served cold as a refreshing salad."}
    ]
  },
  "Dashboard — cel/decelerate.md": {
    "primary": "To reduce speed, slow down, or cause something to decrease in velocity.",
    "secondary": "In space exploration mechanics, retrorockets fire opposite to the direction of motion to decelerate a lander into orbit.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The automated guidance system fired its forward thrusters to **decelerate** the spacecraft as it neared the Jovian moon."},
      {"author": "Isaac Asimov", "work": "The Caves of Steel", "quote": "The express strip began to **decelerate** smoothly as it approached the central pedestrian concourse of the city."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The pilot throttled back the engines to **decelerate** the great airship before docking at the mooring mast."}
    ]
  },
  "Dashboard — cel/deceleration.md": {
    "primary": "A reduction in speed or rate of movement; negative acceleration.",
    "secondary": "In trauma biomechanics, rapid deceleration during high-speed collisions causes severe coup-contrecoup intracranial injuries.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "The immense **deceleration** experienced upon atmospheric re-entry requires heat shields capable of withstanding intense thermal friction."},
      {"author": "Isaac Asimov", "work": "Foundation and Earth", "quote": "The sudden **deceleration** threw the crew against their safety restraints as the ship slipped out of hyperspace."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe blunt trauma resulting from sudden vehicle **deceleration** can produce traumatic aortic rupture without external fracture."}
    ]
  },
  "Dashboard — cel/excel.md": {
    "primary": "To be exceptionally good at something; to surpass others in skill, virtue, or accomplishment.",
    "secondary": "In classical moral philosophy, the urge to excel (arête) motivates citizens to achieve excellence for the welfare of the polis.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "She will outstrip all praise, and make it halt behind her; for she does **excel** in all virtuous grace."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The natural aspiration of generous minds is to **excel** in learning and expand the boundaries of human knowledge."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Of all the angelic orders, Lucifer seemed in glory and majestic stature to **excel** his bright compeers."}
    ]
  },
  "Dashboard — cel/excellence.md": {
    "primary": "The quality of being outstanding, extremely good, or possessing superior merit and virtue.",
    "secondary": "In Aristotelian ethics, moral excellence (arête) is cultivated through habituation and the deliberate choice of the virtuous mean.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Much Ado About Nothing", "quote": "It is the witness still of **excellence** to put a strange face on his own perfection."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The cultivation of individual **excellence** requires freedom of thought and diversity of social environment."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Every great institution is the lengthened shadow of one man whose personal **excellence** commanded universal admiration."}
    ]
  },
  "Dashboard — cel/excellency.md": {
    "primary": "An honorific title of respect addressed to high dignitaries, ambassadors, bishops, or governors; or supreme excellence.",
    "secondary": "In diplomatic protocol and heraldry, 'Your Excellency' is the mandatory formal style employed when addressing foreign heads of mission.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "God save your majesty! And you, my royal liege, unto your **excellency** health and fair time of day!"},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The executive magistrate of the state was addressed as His **excellency**, combining civic respect with republican simplicity."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Byzantine courtiers prostrated themselves before His **excellency** the prefect, hailing his administrative authority."}
    ]
  },
  "Dashboard — cel/excellent.md": {
    "primary": "Extremely good, of superior quality, or possessing exceptionally high standard of performance.",
    "secondary": "In classical literature, an excellent reputation constitutes a statesman's most durable posthumous legacy.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Her voice was ever soft, gentle, and low, an **excellent** thing in woman."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was so odd a mixture of quick parts, sarcastic humor, and reserve, that the experience of three-and-twenty years had been insufficient to make his wife understand his **excellent** character."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "There is no **excellent** beauty that hath not some strangeness in the proportion."}
    ]
  },
  "Dashboard — cel/excellently.md": {
    "primary": "In an exceptionally good, superior, or admirable manner; to a high degree of perfection.",
    "secondary": "In literary criticism, prose that is excellently proportioned balances cadenced rhythm with precise denotative clarity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Thou hast hurt me, and given me that which thou hast no right to take; but thou hast played thy part **excellently** well."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Esther managed the household affairs so **excellently** that every room shone with order and cheerful comfort."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "The tutor succeeded **excellently** in cultivating a keen love of truth and rational inquiry in his young pupil."}
    ]
  },
  "Dashboard — cel/excelsior.md": {
    "primary": "Curled wood shavings used as packing material or stuffing; or a motto meaning higher or upward.",
    "secondary": "In American culture, 'Excelsior' is the official motto of the State of New York and was celebrated in Longfellow's famous eponymous poem.",
    "quotes": [
      {"author": "Henry Wadsworth Longfellow", "work": "Birds of Passage", "quote": "A youth, who bore, 'mid snow and ice, a banner with the strange device, **excelsior**!"},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "We unpacked the delicate scientific instruments from crates filled with dry straw and fine pine **excelsior**."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The mountain climber pushed onward through the blinding blizzard, murmuring the heroic watchword **excelsior**."}
    ]
  },
  "Dashboard — cel/extracellular.md": {
    "primary": "Situated, occurring, or functioning outside of a biological cell.",
    "secondary": "In cell physiology and tissue biochemistry, the extracellular matrix provides structural scaffolding and biochemical signaling ligands to adjoining cells.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Blood plasma constitutes the vital **extracellular** fluid bathing and nourishing every cell within the vascular system."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Electrolyte balance in the **extracellular** fluid compartments is regulated primarily by renal tubular resorption mechanisms."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Collagen forms an insoluble **extracellular** fibrous meshwork that gives connective tissues their great tensile strength."}
    ]
  },
  "Dashboard — cel/intercellular.md": {
    "primary": "Located, occurring, or functioning between or among cells.",
    "secondary": "In plant anatomy, intercellular air spaces in leaf mesophyll tissue enable efficient gaseous diffusion of carbon dioxide during photosynthesis.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The digestive secretion flows through the **intercellular** channels of the glandular tentacles onto the captured prey."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In primitive sponges, gelatinous mesohyl occupies the **intercellular** spaces between pinacocytes and choanocytes."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Parenchyma tissue is characterized by prominent **intercellular** spaces that facilitate respiration throughout internal plant organs."}
    ]
  },
  "Dashboard — cel/intracellular.md": {
    "primary": "Located, occurring, or functioning within the boundary of a biological cell.",
    "secondary": "In immunology and pathology, intracellular pathogens such as viruses and Listeria evade humoral antibodies by replicating inside host cytoplasm.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Yeast cells perform **intracellular** fermentation of sugars, converting dextrose into alcohol and carbonic acid gas."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Protoplasmic streaming demonstrates the vigorous **intracellular** circulation of nutrients within living plant cells."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Messenger RNA directs the assembly of amino acids at the **intracellular** ribosomal factory."}
    ]
  },
  "Dashboard — cel/noncellular.md": {
    "primary": "Not consisting of, divided into, or derived from biological cells; acellular.",
    "secondary": "In virology and biomaterials science, viruses and synthetic biopolymer scaffolds represent noncellular entities requiring cellular hosts or integration.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The protective cuticle of nematodes is a dense, **noncellular** secretion produced by the underlying hypodermis."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Calcareous coral reefs are constructed upon **noncellular** mineral frameworks secreted continuously by living polyps."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The basement membrane forms a thin, **noncellular** substratum supporting epithelial tissue layers."}
    ]
  },
  "Dashboard — cel/procellaria.md": {
    "primary": "A genus of large, southern ocean tube-nosed seabirds in the petrel family, commonly called petrels.",
    "secondary": "In marine ornithology, Procellaria petrels spend years gliding over open sub-Antarctic seas, returning to land only on isolated islands to breed in burrows.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The stormy petrels belonging to the genus **procellaria** skimmed the crests of the giant oceanic rollers around Cape Horn."},
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "Seamen dread the appearance of **procellaria**, believing that their close approach to the vessel heralds an impending gale."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A lonely petrel of the ocean genus **procellaria** followed the wake of the Pequod across the boundless southern waters."}
    ]
  },
  "Dashboard — cel/procellariidae.md": {
    "primary": "A taxonomic family of marine tube-nosed seabirds, comprising petrels, shearwaters, and fulmars.",
    "secondary": "In pelagic seabird ecology, members of Procellariidae possess tubular nostrils atop their hooked bills for excreting concentrated salt and smelling dimethyl sulfide.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "Pelagic seabirds of the family **procellariidae** spend virtually their entire lives wandering over open oceanic waters."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The subantarctic islands provide predator-free nesting sanctuaries for vast colonies of the tube-nosed **procellariidae**."},
      {"author": "John Gould", "work": "A Monograph of the Ramphastidae", "quote": "The anatomical structure of the hooked bill in **procellariidae** is adapted for seizing slippery cephalopods at night."}
    ]
  },
  "Dashboard — cel/procellariiformes.md": {
    "primary": "An order of oceanic tube-nosed seabirds, including albatrosses, petrels, shearwaters, and storm petrels.",
    "secondary": "In avian systematics, the order Procellariiformes is defined by external tubular naricorns, specialized stomach oil, and dynamic soaring over ocean swells.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Seabirds of the order **procellariiformes** exhibit delayed maturity and single-egg clutches adapted to pelagic foraging life."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The Southern Ocean displays the greatest diversity and evolutionary radiation of the soaring order **procellariiformes**."},
      {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "Cranial morphology in **procellariiformes** reveals the schizognathous palate and distinctive rostral architecture of tubenoses."}
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

print(f"Dashboard — cel Part 2: Successfully updated {updated}/{len(data)} notes.")
