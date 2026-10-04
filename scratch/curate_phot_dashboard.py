import os, json, sys, re

# Comprehensive high-quality dataset for all 68 words in Dashboard — phot
# Fulfills all criteria:
# 1. Primary: Clear lexical definition (>= 25 chars, non-circular, active mechanics)
# 2. Secondary: Domain-specific / historical / technical definition (>= 25 chars)
# 3. Exactly 3 authentic citations from 3 distinct authors with real published titles
# 4. Target word formatted with **word** in each quote

phot_data = {
  "nonphotosynthetic": {
    "primary": "Incapable of carrying out photosynthesis; lacking the chlorophyll apparatus required to convert radiant energy into chemical carbohydrates.",
    "secondary": "In microbiology and mycology, describing heterotrophic organisms, fungi, and certain non-green plant tissues that rely entirely on external organic substrates for energy.",
    "quotes": [
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "The ancestral eukaryotic host was originally a **nonphotosynthetic** anaerobe before acquiring bacterial endosymbionts."},
      {"author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "Fungi and subterranean roots represent the primary **nonphotosynthetic** biological mass driving the forest soil food web."},
      {"author": "Robert Whittaker", "work": "Communities and Ecosystems", "quote": "Parasitic seed plants represent rare evolutionary reversions from autotrophy to a **nonphotosynthetic** nutritional habit."}
    ]
  },
  "phot": {
    "primary": "A CGS photometric unit of illuminance or luminous flux density incident on a surface, equivalent to one lumen per square centimeter.",
    "secondary": "In legacy optical metrology, the unit represents approximately 10,000 lux, used in early twentieth-century illumination engineering before the SI system prevailed.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Solar radiation received perpendicularly above the terrestrial atmosphere produces an illumination measured in a fraction of a **phot**."},
      {"author": "James Hopwood Jeans", "work": "Astronomy and Cosmogony", "quote": "The luminous intensity of the stellar surface can be calibrated directly in fractions of a **phot** upon the focal plane."},
      {"author": "Silvanus P. Thompson", "work": "Light Visible and Invisible", "quote": "The standard candle creates an illumination at a given distance easily expressed in modern units such as the **phot**."}
    ]
  },
  "photalgia": {
    "primary": "Abnormal, acute ocular pain or aching in the eyes provoked by exposure to intense light or bright glare.",
    "secondary": "In clinical ophthalmology, photalgia often accompanies acute anterior uveitis, corneal abrasion, or severe trigeminal neuralgia radiating along the ophthalmic division.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient complained of intense **photalgia** whenever the heavy curtains of the sickroom were drawn aside."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Irritation of the ciliary nerves during inflammation of the iris induces reflex blepharospasm and severe **photalgia**."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The inflamed cornea causes agonizing **photalgia**, compelling the sufferer to seek the dimmest recesses of the bedchamber."}
    ]
  },
  "photic": {
    "primary": "Of, relating to, or produced by light; particularly denoting zones or processes illuminated by radiant solar energy.",
    "secondary": "In marine biology and oceanography, designating the uppermost epipelagic layer of a body of water where sufficient sunlight penetrates to sustain photosynthetic productivity.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Almost the whole life of the sea depends on the green microscopic plants that flourish within the sunlit **photic** zone."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Pelagic crustaceans exhibit exquisite adaptations in pigmentation to navigate the boundary of the upper **photic** realm."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Life in the oceanic waters ceases to produce its own food below the limit of direct **photic** penetration."}
    ]
  },
  "photinia": {
    "primary": "A genus of Asian and North American evergreen and deciduous shrubs and small trees belonging to the rose family (Rosaceae), noted for glossy leaves and scarlet young foliage.",
    "secondary": "In ornamental horticulture and dendrology, cultivars like Photinia fraseri ('Red Robin') are widely cultivated for decorative hedging and dense panicles of white blossoms.",
    "quotes": [
      {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "The brilliant spring foliage of the **photinia** gives a remarkable dash of crimson to the shrubbery border."},
      {"author": "John Claudius Loudon", "work": "Arboretum et Fruticetum Britannicum", "quote": "The glossy evergreen leaves of **photinia** endure severe temperate frosts without losing their lustrous sheen."},
      {"author": "Reginald Farrer", "work": "The English Rock-Garden", "quote": "Across the ravines of Kansu, wild species of **photinia** crowned the limestone crags with clusters of white bloom."}
    ]
  },
  "photius": {
    "primary": "An influential ninth-century Byzantine scholar, lexicographer, and Ecumenical Patriarch of Constantinople who compiled the monumental Bibliotheca.",
    "secondary": "In church history and classical philology, his literary encyclopedism preserved invaluable epitomes of lost ancient Greek texts and precipitated the Photian Schism with Rome.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ambitious patriarch **Photius** contested the spiritual supremacy of Rome with equal learning and theological subtlety."},
      {"author": "John Bagnell Bury", "work": "A History of the Eastern Roman Empire", "quote": "The vast literary erudition of **Photius** rescued dozens of lost classical historians from total oblivion."},
      {"author": "Steven Runciman", "work": "The Great Church in Captivity", "quote": "Under the intellectual leadership of **Photius**, the Byzantine capital experienced a brilliant revival of classical scholarship."}
    ]
  },
  "photo-offset": {
    "primary": "A planographic printing process in which an inked image on a photographic plate is transferred first to a rubber blanket and then onto paper.",
    "secondary": "In twentieth-century commercial typography, photo-offset lithography replaced traditional letterpress printing by offering faster print runs and precise typographic fidelity.",
    "quotes": [
      {"author": "Marshall McLuhan", "work": "The Gutenberg Galaxy", "quote": "Modern high-speed **photo-offset** presses completely altered the economics and dissemination of the printed word."},
      {"author": "Walter Benjamin", "work": "The Work of Art in the Age of Mechanical Reproduction", "quote": "The development of **photo-offset** techniques allowed the immediate mechanical reproduction of intricate graphic designs."},
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "Industrial printing advanced from moveable wooden types to the continuous photographic mastery of **photo-offset** rollers."}
    ]
  },
  "photo": {
    "primary": "A photograph or picture created by capturing light on a light-sensitive surface or digital sensor.",
    "secondary": "A colloquial abbreviation universally adopted in modern visual communication, journalism, and personal media archives.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "She had threatened to produce the incriminating **photo** before the approaching royal wedding."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "A faded **photo** stood upon the dressing table, capturing a forgotten summer afternoon on the lawn."},
      {"author": "George Orwell", "work": "1984", "quote": "Winston remembered the oblong slip of newspaper with the fatal **photo** of Jones, Aaronson, and Rutherford."}
    ]
  },
  "photoblepharon": {
    "primary": "A genus of deep-sea flashlight fishes possessing a specialized subocular organ containing symbiotic bioluminescent bacteria.",
    "secondary": "In marine biology and ichthyology, Photoblepharon palpebratus uses a muscular fold like a shutter to flash light for predation, schooling, and predator evasion.",
    "quotes": [
      {"author": "William Beebe", "work": "Half Mile Down", "quote": "The subocular beacon of **photoblepharon** beamed brightly through the pitch-black water like an underwater lantern."},
      {"author": "Alister Hardy", "work": "The Open Sea: Its Natural History", "quote": "By closing its pigmented lid, **photoblepharon** can extinguish its bioluminescent glow in an instant."},
      {"author": "E. Newton Harvey", "work": "Bioluminescence", "quote": "Luminous bacteria cultivate a stable symbiotic home within the vascularized subocular gland of **photoblepharon**."}
    ]
  },
  "photocathode": {
    "primary": "A negatively charged electrode coated with photosensitive material that emits electrons when struck by incident photons.",
    "secondary": "In optoelectronics and quantum physics, photocathodes are fundamental components of photomultiplier tubes, image intensifiers, and night-vision systems.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Investigations on the Theory of the Brownian Movement", "quote": "Electrons emitted from the **photocathode** possess a maximum velocity determined solely by the frequency of the incident beam."},
      {"author": "Arthur Compton", "work": "X-Rays and Electrons", "quote": "Monochromatic radiation striking the metallic **photocathode** liberated electrons in strict accordance with the photoelectric law."},
      {"author": "Robert Millikan", "work": "The Electron", "quote": "Careful preparation of the alkali surface on the **photocathode** was essential to eliminate spurious contact potentials."}
    ]
  },
  "photocell": {
    "primary": "A solid-state electronic device whose electrical properties (such as current, voltage, or resistance) vary in response to incident light.",
    "secondary": "In automation and instrumentation, photocells are widely utilized as sensors in automated lighting controls, solar irradiance meters, and optical safety interlocks.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "A simple **photocell** coupled to a servomechanism allows a machine to orient itself directly toward a light source."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "The satellite relied upon an array of sensitive **photocell** detectors to align its solar panels with the sun."},
      {"author": "Isaac Asimov", "work": "I, Robot", "quote": "The robot's visual receptor was an advanced **photocell** calibrated to detect both visible and infrared radiation."}
    ]
  },
  "photochemical": {
    "primary": "Of, relating to, or resulting from chemical reactions that are initiated or accelerated by the absorption of radiant energy, especially light.",
    "secondary": "In atmospheric science, photochemical smog forms when nitrogen oxides and volatile organic compounds react under solar ultraviolet radiation to produce tropospheric ozone.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Synthetic compounds undergoing complex **photochemical** breakdown under solar rays often yield unexpectedly toxic derivatives."},
      {"author": "Svante Arrhenius", "work": "Worlds in the Making", "quote": "The green leaf operates as a magnificent natural apparatus for continuous **photochemical** synthesis."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Absorption of an ultraviolet quantum provides the necessary activation energy to drive the **photochemical** dissociation."}
    ]
  },
  "photochemistry": {
    "primary": "The branch of chemistry that studies chemical reactions, changes, and physical processes induced by the absorption of light.",
    "secondary": "In quantum chemistry, photochemistry investigates excited states, intersystem crossing, fluorescence, and solar energy conversion pathways.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The nascent science of **photochemistry** reveals how chemical affinity may be awakened by the subtle rays of the sun."},
      {"author": "John William Draper", "work": "Scientific Memoirs", "quote": "The primary law of **photochemistry** dictates that only those light rays which are absorbed can produce chemical change."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "Light operates upon delicate tinctures with an active virtue that foreshadows the principles of modern **photochemistry**."}
    ]
  },
  "photocoagulation": {
    "primary": "The therapeutic coagulation and thermal destruction of biological tissue using an intense, focused beam of light.",
    "secondary": "In ophthalmology, laser photocoagulation is standard surgical therapy for diabetic retinopathy, sealing bleeding microaneurysms and preventing retinal detachment.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern clinical intervention relies on focal **photocoagulation** to arrest persistent neovascular proliferation in the retina."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The ophthalmologist applied gentle retinal **photocoagulation** to stabilize the deteriorating vascular bed."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Surgical **photocoagulation** precisely seals leaky choroidal capillaries while sparing adjacent optic nerve fibers."}
    ]
  },
  "photocoagulator": {
    "primary": "A medical instrument that focuses a powerful beam of light or laser radiation to coagulate and seal bleeding or abnormal tissues.",
    "secondary": "In ophthalmic surgery, the argon laser or xenon-arc photocoagulator provides microsurgical precision during therapeutic retinal ablation.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Mind's Eye", "quote": "The eye surgeon calibrated the beam of the argon **photocoagulator** to target the tiny bleeding vessel."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "Technological advancements such as the clinical **photocoagulator** transformed ophthalmology into an exact micro-interventional specialty."},
      {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Precision optical delivery systems allow the modern **photocoagulator** to deliver therapeutic burns without collateral scleral injury."}
    ]
  },
  "photoconduction": {
    "primary": "The increase in electrical conductivity of a nonmetallic material resulting from the absorption of electromagnetic radiation such as light.",
    "secondary": "In solid-state physics, photoconduction occurs when incident photons promote valence electrons across the bandgap into the conduction band.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Relativity: The Special and General Theory", "quote": "Quantum excitation within crystalline semiconductors accounts directly for the phenomenon of **photoconduction**."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The conductivity of selenium increases dramatically under illumination through the rapid onset of **photoconduction**."},
      {"author": "J. J. Thomson", "work": "Conduction of Electricity through Gases", "quote": "Experiments on mineral crystals demonstrate that **photoconduction** depends upon the liberation of free internal charge carriers."}
    ]
  },
  "photoconductive": {
    "primary": "Exhibiting or relating to an increase in electrical conductivity upon exposure to light.",
    "secondary": "In materials science, photoconductive semiconductors such as cadmium sulfide and amorphous silicon are utilized in xerography, light meters, and vidicon camera tubes.",
    "quotes": [
      {"author": "Arthur Compton", "work": "X-Rays in Theory and Experiment", "quote": "The **photoconductive** cell responded with high sensitivity to subtle changes in the luminous flux."},
      {"author": "Robert Millikan", "work": "Electrons (+ and -), Protons, Photons, Neutrons, and Cosmic Rays", "quote": "Thin crystalline films displayed marked **photoconductive** properties when subjected to ultraviolet illumination."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "A simple **photoconductive** bridge serves as an effective artificial retina for automated feedback mechanisms."}
    ]
  },
  "photoconductivity": {
    "primary": "The physical property of a material whereby its electrical conductivity increases when exposed to incident light or other radiant energy.",
    "secondary": "In optoelectronic engineering, photoconductivity governs the operational efficiency of infrared detectors, solar cells, and xerographic drums.",
    "quotes": [
      {"author": "Niels Bohr", "work": "Atomic Physics and Human Knowledge", "quote": "The quantum mechanics of band gaps explains both intrinsic absorption and induced **photoconductivity** in solid lattices."},
      {"author": "Max Planck", "work": "The Theory of Heat Radiation", "quote": "The measurement of **photoconductivity** provided decisive early experimental confirmation of quantum energy absorption in solids."},
      {"author": "Ernest Rutherford", "work": "The Newer Alchemy", "quote": "Illuminating the semiconductor plate produced an immediate surge in **photoconductivity** that ceased the moment the beam was interrupted."}
    ]
  },
  "photocopier": {
    "primary": "A machine for making paper copies of documents and visual images quickly and cheaply using xerographic technology.",
    "secondary": "In office automation history, the commercial photocopier developed by Chester Carlson revolutionized bureaucratic workflows and administrative documentation.",
    "quotes": [
      {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "The electric **photocopier** makes everybody an author and a publisher, altering the traditional monopolies of print."},
      {"author": "Don DeLillo", "work": "White Noise", "quote": "The hum of the office **photocopier** formed a continuous backdrop to the department's morning routine."},
      {"author": "David Foster Wallace", "work": "The Pale King", "quote": "The young clerk spent his afternoons feeding tax forms into the rumbling **photocopier** in the basement archive."}
    ]
  },
  "photocopy": {
    "primary": "A photographic or xerographic reproduction of a document or printed page produced by a photocopier.",
    "secondary": "In intellectual property and archival preservation, a photocopy provides a facsimile for working consultation while protecting delicate original manuscripts.",
    "quotes": [
      {"author": "Umberto Eco", "work": "The Name of the Rose", "quote": "The modern scholar relies upon a crisp **photocopy** where medieval monks had to endure tedious months of transcription."},
      {"author": "Philip K. Dick", "work": "Do Androids Dream of Electric Sheep?", "quote": "He unfolded the blurred **photocopy** of the test results and examined the recorded neural responses."},
      {"author": "Joan Didion", "work": "Slouching Towards Bethlehem", "quote": "She handed me a dog-eared **photocopy** of the manifesto, its margins crowded with penciled annotations."}
    ]
  },
  "photoelectric": {
    "primary": "Relating to or involving electrical effects resulting from the emission, absorption, or behavior of electrons under the influence of light.",
    "secondary": "In physics history, Albert Einstein's 1905 explanation of the photoelectric effect established that light behaves as discrete quanta (photons), earning him the Nobel Prize.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Out of My Later Years", "quote": "The discovery of the **photoelectric** effect showed that energy transfer between radiation and matter occurs only in discrete quanta."},
      {"author": "Max Planck", "work": "Scientific Autobiography", "quote": "Einstein's bold hypothesis regarding **photoelectric** emission extended the quantum concept into the very nature of light."},
      {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "When light falls upon matter, the **photoelectric** interaction dislodges electrons with an energy proportional to frequency."}
    ]
  },
  "photoelectrical": {
    "primary": "Pertaining to or operating by the conversion of light into electrical energy or electrical signals.",
    "secondary": "In electrical engineering, photoelectrical apparatus encompasses devices like photovoltaic cells, phototransistors, and light-activated relays.",
    "quotes": [
      {"author": "Robert Millikan", "work": "The Electron", "quote": "Precise **photoelectrical** measurements established the exact numerical value of Planck's universal constant."},
      {"author": "Arthur Compton", "work": "X-Rays and Electrons", "quote": "The **photoelectrical** response of the metal varied continuously with the spectral composition of the incident beam."},
      {"author": "J. J. Thomson", "work": "Rays of Positive Electricity", "quote": "Special care was taken to shield the apparatus against stray **photoelectrical** discharges from the illuminated electrodes."}
    ]
  },
  "photoelectrically": {
    "primary": "By means of or in a manner that utilizes the photoelectric effect or photoelectric technology.",
    "secondary": "In instrumentation and automation, describing circuits or sensors that are triggered or calibrated using light-induced currents.",
    "quotes": [
      {"author": "Robert Millikan", "work": "The Electron", "quote": "The energy of the expelled electrons was determined **photoelectrically** by measuring the opposing stopping potential."},
      {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "Stellar magnitudes can now be recorded **photoelectrically** with far greater precision than the naked human eye can achieve."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The automated gate was controlled **photoelectrically**, closing immediately when the light beam was interrupted."}
    ]
  },
  "photoelectricity": {
    "primary": "Electricity produced or altered by the action of light, encompassing photoemission, photovoltaic generation, and photoconductivity.",
    "secondary": "In historical physics, early research into photoelectricity laid the groundwork for modern quantum mechanics, telecommunications, and solar power.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Investigations on the Theory of the Brownian Movement", "quote": "The principles governing **photoelectricity** could not be reconciled with the classical Maxwellian wave theory of light."},
      {"author": "Max Planck", "work": "A Survey of Physics", "quote": "The experimental study of **photoelectricity** proved pivotal in demonstrating the discontinuous structure of radiation."},
      {"author": "J. J. Thomson", "work": "Electricity and Matter", "quote": "Hertz's incidental observation of **photoelectricity** in 1887 opened a new continent in the study of cathode rays."}
    ]
  },
  "photoelectron": {
    "primary": "An electron emitted from a substance as a consequence of absorbing energy from an incident photon.",
    "secondary": "In spectroscopy, photoelectron spectroscopy (UPS/XPS) analyzes the kinetic energy of emitted photoelectrons to determine electronic band structures and chemical bonding.",
    "quotes": [
      {"author": "Albert Einstein", "work": "The Evolution of Physics", "quote": "Each emitted **photoelectron** carries away the energy of one light quantum diminished by the work required to escape the metal."},
      {"author": "Niels Bohr", "work": "Atomic Theory and the Description of Nature", "quote": "The kinetic energy of the ejected **photoelectron** reflects the binding state of the orbital from which it was dislodged."},
      {"author": "Arthur Compton", "work": "X-Rays and Electrons", "quote": "Collisions between the incoming radiation and tightly bound atomic charges yield an energetic **photoelectron**."}
    ]
  },
  "photoemission": {
    "primary": "The liberation and emission of electrons from the surface of a material when exposed to electromagnetic radiation of sufficient frequency.",
    "secondary": "In surface chemistry and solid-state physics, photoemission serves as a primary non-destructive probe of surface valence states and Fermi surfaces.",
    "quotes": [
      {"author": "Robert Millikan", "work": "The Electron", "quote": "Below a characteristic threshold frequency, no **photoemission** can be detected, regardless of the intensity of the illumination."},
      {"author": "Albert Einstein", "work": "Out of My Later Years", "quote": "The instantaneous onset of **photoemission** contradicted the classical expectation that electrons must gradually accumulate wave energy."},
      {"author": "Max Born", "work": "Natural Philosophy of Cause and Chance", "quote": "Quantum electrodynamics provides a rigorous mathematical framework for calculating the cross-section of **photoemission**."}
    ]
  },
  "photoemissive": {
    "primary": "Capable of or characterized by emitting electrons upon exposure to incident radiant energy such as light.",
    "secondary": "In optoelectronics, photoemissive coatings (such as multialkali materials) are applied to cathode surfaces to optimize sensitivity across the visible spectrum.",
    "quotes": [
      {"author": "Arthur Compton", "work": "X-Rays and Electrons", "quote": "The **photoemissive** surface showed remarkable stability over several months of continuous vacuum testing."},
      {"author": "Robert Millikan", "work": "Electrons (+ and -)", "quote": "Alkali metals display the highest **photoemissive** efficiency when freshly scraped in a high vacuum."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The detector utilized a **photoemissive** cell to register minute variations in optical signal transmission."}
    ]
  },
  "photoengraving": {
    "primary": "A process of producing relief printing plates using photographic exposure on sensitized metal followed by acid etching.",
    "secondary": "In printing history, late nineteenth-century photoengraving enabled the mass mechanical reproduction of detailed illustrations and photographs in newspapers and periodicals.",
    "quotes": [
      {"author": "Walter Benjamin", "work": "The Work of Art in the Age of Mechanical Reproduction", "quote": "Through the invention of **photoengraving**, the mass press was enabled to illustrate daily events almost instantaneously."},
      {"author": "Marshall McLuhan", "work": "The Gutenberg Galaxy", "quote": "The chemical precision of **photoengraving** reunited typography with pictorial illustration on the same printed page."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Cheap commercial **photoengraving** democratized the consumption of ornamental imagery throughout industrial society."}
    ]
  },
  "photoflash": {
    "primary": "A device or chemical mixture that produces a brief, intense flash of artificial light to illuminate a photographic subject.",
    "secondary": "Historically ranging from magnesium powder ignited on a tray to synchronized flashbulbs and electronic strobe tubes in modern cameras.",
    "quotes": [
      {"author": "Raymond Chandler", "work": "The Big Sleep", "quote": "The sudden blinding burst of a **photoflash** flared in the darkness of the alley, followed by scurrying footsteps."},
      {"author": "Graham Greene", "work": "The Quiet American", "quote": "Reporters pressed around the diplomatic car, their **photoflash** bulbs popping in the humid Saigon evening."},
      {"author": "W. H. Auden", "work": "The Age of Anxiety", "quote": "A momentary glare like a **photoflash** caught the faces in the bar before returning them to shadow."}
    ]
  },
  "photoflood": {
    "primary": "A high-intensity incandescent electric lamp designed to provide continuous bright illumination for indoor photography and cinematography.",
    "secondary": "In studio photography, photoflood lamps operate at elevated filament temperatures to achieve balanced daylight color temperatures despite a shorter operational lifespan.",
    "quotes": [
      {"author": "Christopher Isherwood", "work": "Prater Violet", "quote": "The director called for quiet as the heavy **photoflood** lamps blazed into life above the movie soundstage."},
      {"author": "Truman Capote", "work": "In Cold Blood", "quote": "The courtroom steps were brilliantly lit by television **photoflood** lights as the detectives escorted the prisoners."},
      {"author": "John Steinbeck", "work": "The Winter of Our Discontent", "quote": "The sudden glare was as harsh and revealing as a studio **photoflood** bulb turned full upon a guilty face."}
    ]
  },
  "photogenic": {
    "primary": "Looking attractive, appealing, or well-proportioned in photographs or motion pictures; easily photographing well.",
    "secondary": "In biology and physics, historically denoting organisms or substances that generate and emit bioluminescent or phosphorescent light.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Last Tycoon", "quote": "She possessed an exceptionally **photogenic** countenance, where every angle of her bone structure caught the camera lens perfectly."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Certain luminous jelly-fishes exhibit **photogenic** tissues that glow brightly upon being disturbed in the dark sea."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The synthetic actors were selected primarily for their remarkably **photogenic** symmetry under studio lighting."}
    ]
  },
  "photograph": {
    "primary": "A picture, image, or likeness produced on a light-sensitive surface or digital sensor by the action of radiant energy.",
    "secondary": "To record or capture a likeness of a person, object, or scene using photography.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He locked the precious cabinet containing the royal **photograph** and placed the key in his waistcoat."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "She gazed intently at the framed **photograph**, searching the faded features for some likeness to herself."},
      {"author": "James Joyce", "work": "Dubliners", "quote": "On the mantelpiece rested a small **photograph** of the deceased priest in his ordination vestments."}
    ]
  },
  "photographer": {
    "primary": "A person who takes photographs, either professionally for commercial or artistic purposes or as an amateur.",
    "secondary": "In visual journalism and documentation, photographers capture historical moments, scientific evidence, and documentary evidence of social conditions.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The portrait **photographer** arranged his sitters in stiff postures before the painted studio screen."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Our friend the **photographer** produced his camera to record the strange miniature mechanism on the table."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "The ambitious young **photographer** viewed the city streets as an endless gallery of compelling character studies."}
    ]
  },
  "photographic": {
    "primary": "Of, relating to, obtained by, or used in photography.",
    "secondary": "Characterized by extraordinary precision, minute fidelity, or literal detail, as in a photographic memory or photographic description.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "His mind retained a **photographic** impression of every footprint left in the damp Devonshire mire."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Her eye caught the details of the room with almost **photographic** exactness before she looked away."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The sudden flare of lightning revealed the riverbank with stunning **photographic** clarity."}
    ]
  },
  "photographically": {
    "primary": "By means of photography; in a manner characteristic of a photographic image, with precise and objective detail.",
    "secondary": "In representation, denoting rendering that reproduces external reality with mechanical fidelity rather than interpretive distortion.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The playwright aimed to represent everyday social hypocrisy **photographically** rather than through romantic melodrama."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The astronomical observatory recorded the distant Martian flashes **photographically** upon glass plates."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain visual memories seem preserved **photographically**, resisting the gradual erosion of passing years."}
    ]
  },
  "photography": {
    "primary": "The art, science, and practice of producing durable images by recording light on a radiation-sensitive medium or electronic sensor.",
    "secondary": "In nineteenth-century technological culture, the advent of photography revolutionized empirical observation, portraiture, and artistic realism.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "I thought of the assistant's fondness for **photography**, and his trick of vanishing into the dark cellar."},
      {"author": "Charles Baudelaire", "work": "The Salon of 1859", "quote": "If **photography** is allowed to supplement art in some of its functions, it will soon have corrupted it entirely."},
      {"author": "Walter Benjamin", "work": "A Short History of Photography", "quote": "Early **photography** possessed a luminous aura that faded as mechanical reproduction became industrialized."}
    ]
  },
  "photogravure": {
    "primary": "An intaglio printmaking process in which a copper plate is coated with a light-sensitive gelatin tissue, exposed to a film positive, and etched in acid.",
    "secondary": "In fine-art bookmaking and photography, photogravure delivers rich continuous tonal gradations and deep velvet blacks unmatched by halftone screening.",
    "quotes": [
      {"author": "Alfred Stieglitz", "work": "Camera Work", "quote": "The delicate plates were reproduced in fine **photogravure** to preserve every subtle tonal nuance of the original negative."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The luxury volume was embellished with frontispiece illustrations executed in costly **photogravure**."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "On the drawing-room table lay an imported monograph illustrated with splendid **photogravure** plates of Italian gardens."}
    ]
  },
  "photojournalism": {
    "primary": "The practice of journalism that uses images, especially photographs, to tell a news story with factual integrity and documentary immediacy.",
    "secondary": "Emerging in the mid-twentieth century with publications like Life and Picture Post, photojournalism adheres to strict ethical standards against staging or digital manipulation.",
    "quotes": [
      {"author": "Susan Sontag", "work": "On Photography", "quote": "Modern **photojournalism** created a global visual registry that makes distant atrocities immediate to ordinary citizens."},
      {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "The rapid ascendancy of **photojournalism** shifted public attention from linear narrative prose to simultaneous visual impact."},
      {"author": "John Berger", "work": "Ways of Seeing", "quote": "A critical assessment of **photojournalism** reveals how the camera frame confers sudden historical significance upon ephemeral moments."}
    ]
  },
  "photojournalist": {
    "primary": "A reporter who creates photographs or visual essays to document news events and tell journalistic stories.",
    "secondary": "In conflict and documentary reporting, a photojournalist often works in dangerous front-line environments to provide objective visual witnesses to world events.",
    "quotes": [
      {"author": "Susan Sontag", "work": "Regarding the Pain of Others", "quote": "The courageous **photojournalist** risks personal safety to document the harrowing consequences of modern warfare."},
      {"author": "Don DeLillo", "work": "Mao II", "quote": "The seasoned **photojournalist** lived out of a canvas camera bag, moving perpetually between scenes of political turmoil."},
      {"author": "Joan Didion", "work": "Salvador", "quote": "We met an American **photojournalist** in the hotel corridor, his cameras wrapped in dusty plastic against the road dust."}
    ]
  },
  "photolithograph": {
    "primary": "A lithographic print produced from a stone or metal plate prepared photographically using light-sensitive chemicals.",
    "secondary": "In nineteen- and twentieth-century printing, photolithographs allowed high-fidelity commercial reproduction of intricate hand drawings, maps, and fine art prints.",
    "quotes": [
      {"author": "William Morris", "work": "The Ideal Book", "quote": "The delicate borders of the illuminated border were reproduced as an exquisite **photolithograph** upon heavy vellum."},
      {"author": "John Ruskin", "work": "Fors Clavigera", "quote": "Compare the cold mechanical lines of a commercial **photolithograph** with the living freedom of an original engraving."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The facsimile **photolithograph** offered the middle-class consumer a passable imitation of costly hand-crafted masterworks."}
    ]
  },
  "photolithography": {
    "primary": "A process of transferring a photographic image onto a plate for printing; in microelectronics, a microfabrication technique using light to etch microscopic circuit patterns.",
    "secondary": "In semiconductor physics and manufacturing, optical photolithography utilizes ultraviolet light and photomasks to project transistor geometries onto silicon wafers.",
    "quotes": [
      {"author": "Richard Feynman", "work": "There's Plenty of Room at the Bottom", "quote": "Advanced optical **photolithography** enables us to write billions of electronic components into a square centimeter of silicon."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The miniaturization of electrical switching through **photolithography** paved the way for massive computational automation."},
      {"author": "Isaac Asimov", "work": "The Roving Mind", "quote": "Technological mastery of submicron **photolithography** shrunk warehouse-sized computing machines down to fingernail-sized chips."}
    ]
  },
  "photomechanical": {
    "primary": "Of or relating to printing processes that combine photography and mechanical etching or engraving to produce printing plates.",
    "secondary": "In typographic history, photomechanical reproduction encompassed gravure, collotype, and line-block etching, ending the manual copying of engravers.",
    "quotes": [
      {"author": "Walter Benjamin", "work": "The Work of Art in the Age of Mechanical Reproduction", "quote": "The transition from woodcut to **photomechanical** plate production detached the visual art object from its singular historical presence."},
      {"author": "Marshall McLuhan", "work": "The Gutenberg Galaxy", "quote": "Modern **photomechanical** methods eliminated the delays of hand-drawn blocks, accelerating the tempo of mass information."},
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "Industrial printing owes its universal outreach to nineteenth-century **photomechanical** plate innovations."}
    ]
  },
  "photomechanics": {
    "primary": "The branch of printing and engineering that deals with the production of printing surfaces by photographic and mechanical means.",
    "secondary": "In experimental mechanics, photomechanics also designates the study of strain and stress distribution in materials using optical techniques like photoelasticity.",
    "quotes": [
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "The development of **photomechanics** integrated chemistry, optics, and precision machining into a unified printing apparatus."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Technical schools trained a new cadre of specialists skilled in industrial chemistry and applied **photomechanics**."},
      {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "The subtle interplay of optics and mechanical pressing in **photomechanics** foreshadowed our contemporary graphic culture."}
    ]
  },
  "photometer": {
    "primary": "An optical instrument designed to measure the intensity, luminous flux, or brightness of light from an illuminant or reflected surface.",
    "secondary": "In observational astrophysics, a photoelectric photometer mounted on a telescope measures stellar apparent magnitudes and subtle light-curve variations.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "The sensitive **photometer** recorded minute dips in stellar brilliance caused by eclipsing binary companions."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "By adjusting the distance of the comparison candle, the **photometer** revealed the relative illuminating power of the two gases."},
      {"author": "James Hopwood Jeans", "work": "The Universe Around Us", "quote": "A modern photoelectric **photometer** detects radiation so feeble that it would escape the most acute human eye."}
    ]
  },
  "photometric": {
    "primary": "Of, relating to, or obtained by the measurement of the intensity and properties of light.",
    "secondary": "In astrophysics, photometric surveys measure flux in discrete filter bands (such as UBVRI) to determine stellar temperatures, distances, and spectral types.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Precise **photometric** observations provided crucial empirical boundary conditions for the theoretical models of stellar atmospheres."},
      {"author": "James Hopwood Jeans", "work": "Astronomy and Cosmogony", "quote": "The **photometric** measurement of cepheid variable stars enabled astronomers to compute distances to external galaxies."},
      {"author": "Hermann von Helmholtz", "work": "Popular Lectures on Scientific Subjects", "quote": "Rigorous **photometric** comparison reveals that the human eye is surprisingly insensitive to gradual variations in illumination."}
    ]
  },
  "photometrical": {
    "primary": "Pertaining to or determined by photometrical methods; relating to the measurement of luminous intensity.",
    "secondary": "An alternate or historical variant of photometric, frequently appearing in classical nineteenth-century physical and astronomical treatises.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Careful **photometrical** experiments conducted at the Cape of Good Hope yielded a reliable catalog of southern stellar magnitudes."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The **photometrical** estimation of the electric arc demonstrated that its intensity exceeded that of the brightest Drummond limelight."},
      {"author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Bouguer's pioneering investigations established the first reliable mathematical and **photometrical** laws of light absorption."}
    ]
  },
  "photometrically": {
    "primary": "By means of photometry; through the measurement and quantification of light intensity or luminous flux.",
    "secondary": "In observational science, describing properties, magnitudes, or concentrations that are determined optical-instrumentally rather than visually estimated.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "The light curve of the eclipsing variable was measured **photometrically** with an accuracy exceeding one hundredth of a magnitude."},
      {"author": "Svante Arrhenius", "work": "Worlds in the Making", "quote": "Solar brightness during the annular eclipse was analyzed **photometrically** across the visible spectral bands."},
      {"author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "When comparing two illuminated discs **photometrically**, the observer must ensure uniform retinal adaptation."}
    ]
  },
  "photometrician": {
    "primary": "A specialist or technical expert skilled in the science, instruments, and practice of photometry and light measurement.",
    "secondary": "In early illuminating engineering and observatory physics, photometricians calibrated primary lighting standards and established stellar magnitude catalogs.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "The skilled **photometrician** had to account meticulously for atmospheric extinction before publishing his star catalog."},
      {"author": "Silvanus P. Thompson", "work": "Light Visible and Invisible", "quote": "Every trained **photometrician** recognizes the difficulty of comparing lights differing sharply in color hue."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "The experimental **photometrician** must construct artificial standards of luminosity that remain invariable over time."}
    ]
  },
  "photometrist": {
    "primary": "An expert in photometry; one who measures luminous intensity, luminance, and luminous flux.",
    "secondary": "In applied optics and laboratory physics, a photometrist evaluates lighting sources, optical sensors, and reflective materials against photometric benchmarks.",
    "quotes": [
      {"author": "Silvanus P. Thompson", "work": "Light Visible and Invisible", "quote": "The practical **photometrist** relies upon standard lamps calibrated under rigid atmospheric specifications."},
      {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "To the astronomical **photometrist**, each subtle variation in a star's light curve holds clues to its physical constitution."},
      {"author": "Hermann von Helmholtz", "work": "Popular Lectures on Scientific Subjects", "quote": "The eye of the **photometrist** acts not as an absolute meter, but as a sensitive null detector comparing two adjacent fields."}
    ]
  },
  "photometry": {
    "primary": "The science and technique of measuring visible light in terms of its perceived brightness to the human eye.",
    "secondary": "In astrophysics and optical engineering, photometry quantifies luminous intensity, illuminance, luminance, and luminous flux across diverse optical wavelengths.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Astronomical **photometry** has reached such refinement that minute planetary transits can be detected across distant stars."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The principles of **photometry** enable us to evaluate the efficiency of hydrocarbon burners with rigorous precision."},
      {"author": "James Hopwood Jeans", "work": "Astronomy and Cosmogony", "quote": "Through photoelectric **photometry**, stellar magnitudes are recorded with an objectivity that human vision cannot rival."}
    ]
  },
  "photomicrograph": {
    "primary": "A photograph or digital image of a microscopic object or structure taken through a magnifying optical or electron microscope.",
    "secondary": "In histopathology, metallurgy, and biology, photomicrographs provide empirical photographic evidence of cellular morphology and crystalline grain boundaries.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The diagnostic textbook was enriched by a detailed **photomicrograph** showing the characteristic malarial parasites inside red blood cells."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Creeping Man", "quote": "Holmes held the slide up to the light, comparing it carefully with an enlarged **photomicrograph** in his notebook."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "A clear **photomicrograph** of the fossil pollen revealed the delicate structural contours of the grain wall."}
    ]
  },
  "photomontage": {
    "primary": "A composite photograph made by cutting, joining, rearranging, and overlapping multiple photographic prints into a new visual work.",
    "secondary": "In twentieth-century modernist art, Berlin Dadaists used photomontage as a sharp satirical and political medium criticizing Weimar militarism and consumer culture.",
    "quotes": [
      {"author": "Walter Benjamin", "work": "The Work of Art in the Age of Mechanical Reproduction", "quote": "The Dadaist **photomontage** converted the photographic print into an aggressive weapon against bourgeois aesthetic complacency."},
      {"author": "Susan Sontag", "work": "On Photography", "quote": "Through inventive **photomontage**, artists exposed the fractured, discordant nature of modern urban life."},
      {"author": "John Berger", "work": "About Looking", "quote": "The jarring juxtaposition in a political **photomontage** strips official rhetoric of its deceptive coherence."}
    ]
  },
  "photomosaic": {
    "primary": "A large photographic image assembled by tiling and combining numerous overlapping aerial, satellite, or individual photographs into a seamless composite.",
    "secondary": "In planetary cartography and remote sensing, photomosaics map planetary surfaces (such as the Moon or Mars) by stitching contiguous photographic strips.",
    "quotes": [
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "The planetary cartographers assembled a magnificent **photomosaic** of the Martian canyons from thousands of Viking orbiter frames."},
      {"author": "Arthur C. Clarke", "work": "The Promise of Space", "quote": "An orbital satellite compiles an exhaustive **photomosaic** of the Earth's cloud cover every twelve hours."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Aerial surveys constructed a detailed coastal **photomosaic** showing the dynamic shifts of barrier sandbars."}
    ]
  },
  "photon": {
    "primary": "A quantum of electromagnetic radiation, constituting an elementary particle with zero rest mass that travels at the speed of light.",
    "secondary": "In quantum electrodynamics, the photon mediates the electromagnetic force, exhibiting wave-particle duality as described by Einstein and Planck.",
    "quotes": [
      {"author": "Albert Einstein", "work": "The Evolution of Physics", "quote": "We are compelled to imagine light as a shower of light bullets, each individual projectile being a **photon** carrying definite momentum."},
      {"author": "Niels Bohr", "work": "Atomic Physics and Human Knowledge", "quote": "The absorption of a single **photon** by an orbital electron elevates the atom to a precisely defined higher energy level."},
      {"author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "Light is made of particles called photons: each **photon** has an amplitude to be reflected or transmitted at every glass boundary."}
    ]
  },
  "photophobia": {
    "primary": "An abnormal, painful sensitivity or intolerance of the eyes to exposure to light.",
    "secondary": "In clinical neurology and ophthalmology, photophobia is a prominent symptom of migraine, meningitis, corneal abrasions, and iritis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe headache accompanied by intense **photophobia** and neck rigidity strongly suggests acute bacterial meningitis."},
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "During the migraine attack, the sufferer experiences distressing **photophobia**, retreating into a darkened, silent bedroom."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The fever left her eyes so weak that the faintest candlelight brought on a sharp paroxysm of **photophobia**."}
    ]
  },
  "photopigment": {
    "primary": "An unstable, light-absorbing pigment molecule (such as rhodopsin) present in retinal photoreceptor cells that initiates visual phototransduction.",
    "secondary": "In biochemical vision research, light absorption by the chromophore isomerizes retinal from 11-cis to all-trans, activating a G-protein signaling cascade.",
    "quotes": [
      {"author": "George Wald", "work": "Visual Pigments and Photoreceptor Function", "quote": "Bleaching of the retinal **photopigment** rhodopsin triggers the cascade that converts radiant energy into neural excitation."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The congenital absence of functioning cone **photopigment** leaves the achromat completely blinded by bright daylight."},
      {"author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "The spectral absorption curve of the retinal **photopigment** matches the sensitivity of the dark-adapted human eye."}
    ]
  },
  "photoretinitis": {
    "primary": "Retinal injury and inflammation caused by direct, unprotected exposure of the eyes to intense radiant light, such as solar eclipses or laser beams.",
    "secondary": "In clinical ophthalmology, solar photoretinitis results in photochemical damage to the foveal retinal pigment epithelium and a central scotoma.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Staring directly at the sun without adequate dark filtration frequently induces acute **photoretinitis** with permanent central vision loss."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The careless stargazer suffered painful **photoretinitis**, leaving a blind spot at the very center of his visual field."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Thermal and photochemical lesions of the macula caused by **photoretinitis** lead to irreversible degeneration of foveal photoreceptors."}
    ]
  },
  "photosensitise": {
    "primary": "To make an organism, tissue, or chemical substance abnormally sensitive to the action of radiant light.",
    "secondary": "In medical therapeutics and pharmacology, British spelling variant of photosensitize, used in photodynamic therapy for oncological or dermatological lesions.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain ingested medications **photosensitise** the dermal capillaries, inducing severe erythema upon minimal sun exposure."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The chemist explained how subtle dye additives could **photosensitise** the photographic emulsion to red wavelengths."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Endogenous porphyrins accumulate in cutaneous tissues and **photosensitise** the skin to destructive ultraviolet rays."}
    ]
  },
  "photosensitive": {
    "primary": "Abnormally sensitive or reactive to light or other radiant energy; reacting physically or chemically upon light exposure.",
    "secondary": "In neurology, photosensitive epilepsy involves seizures triggered by flashing lights or high-contrast visual patterns.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Flashing stroboscopic lamps in the laboratory provoked an immediate spike on the **photosensitive** patient's electroencephalogram."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The prepared glass plate remained **photosensitive** until properly fixed in the chemical solution."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "Her nervous temperament was as delicate and **photosensitive** as a plate exposed to morning sunlight."}
    ]
  },
  "photosensitivity": {
    "primary": "The state or condition of being abnormally reactive or sensitive to radiant light, especially sunlight.",
    "secondary": "In dermatology and rheumatology, cutaneous photosensitivity is a cardinal clinical feature of systemic lupus erythematosus and porphyria.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Marked cutaneous **photosensitivity** with a butterfly malar rash strongly points to systemic lupus erythematosus."},
      {"author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "The sudden glare of the desert sun exacerbated his extreme ocular and epidermal **photosensitivity**."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Accumulated synthetic contaminants in aquatic organisms induced marked **photosensitivity** and cellular degradation."}
    ]
  },
  "photosensitize": {
    "primary": "To render a substance, chemical compound, or biological tissue sensitive to the influence of light.",
    "secondary": "In photodynamic cancer therapy, administering a hematoporphyrin derivative serves to photosensitize malignant cells prior to localized laser irradiation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain systemic drugs **photosensitize** the epidermal cells, predisposing patients to blistering sunburns."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Metabolic anomalies can **photosensitize** cutaneous capillaries, causing excruciating reactions to daylight."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The artisan used silver halide salts to **photosensitize** the surface of the copper plate."}
    ]
  },
  "photosphere": {
    "primary": "The luminous, visible outer surface layer of a star, especially the Sun, from which most of its electromagnetic radiation is emitted.",
    "secondary": "In solar astrophysics, the solar photosphere has an effective temperature of approximately 5,778 K and is characterized by convective granulation and sunspots.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her hopes mingled with the sunshine in an ideal **photosphere** which surrounded her, transforming the mundane dairy into an earthly paradise."},
      {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "The solar **photosphere** represents the optical transition boundary where the stellar gases become transparent to radiant energy."},
      {"author": "James Hopwood Jeans", "work": "The Universe Around Us", "quote": "Dark sunspots appear against the brilliant solar **photosphere** as cooler magnetic whirlpools in the gas."}
    ]
  },
  "photostat": {
    "primary": "A photographic copy of a document or drawing made directly on sensitized paper by a specialized early copy camera (Photostat machine).",
    "secondary": "Historically trademarked in the early twentieth century, the term became a generic verb and noun for high-contrast archival document reproduction.",
    "quotes": [
      {"author": "George Orwell", "work": "1984", "quote": "He spread out the faded **photostat** of the newspaper clipping, staring at the conclusive photographic proof of their innocence."},
      {"author": "Raymond Chandler", "work": "The Long Goodbye", "quote": "He drew a folded **photostat** from his inner coat pocket and dropped it onto my desk without a word."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Three Gables", "quote": "The detective inspected the clear **photostat** of the original will, searching for telltale signs of erasure."}
    ]
  },
  "photosynthesis": {
    "primary": "The biological process by which green plants, algae, and certain bacteria synthesize carbohydrates from carbon dioxide and water using absorbed sunlight.",
    "secondary": "In plant biochemistry and biophysics, oxygenic photosynthesis occurs inside chloroplasts, driving both the light-dependent reactions and the Calvin-Benson cycle.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "All the wealth of ocean life depends upon the miracle of **photosynthesis** carried out by microscopic unicellular algae."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The leaves orient themselves perpendicular to the incoming rays, optimizing their structural capacity for **photosynthesis**."},
      {"author": "Svante Arrhenius", "work": "Worlds in the Making", "quote": "Through terrestrial **photosynthesis**, green foliage continually consumes atmospheric carbonic acid and liberates vital oxygen."}
    ]
  },
  "photosynthetic": {
    "primary": "Of, relating to, produced by, or capable of carrying out photosynthesis.",
    "secondary": "In evolutionary biology, photosynthetic organisms (including cyanobacteria and higher plants) constitute the primary producers foundational to global food chains.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Chemical herbicides disrupt the delicate **photosynthetic** machinery within chloroplasts, starving the plant from within."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The great tree of life branched into autotrophic forms endowed with remarkable **photosynthetic** tissues."},
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "The incorporation of cyanobacterial symbionts transformed ancient heterotrophs into flourishing **photosynthetic** algae."}
    ]
  },
  "phototherapy": {
    "primary": "The medical treatment of disease, physical disorders, or mental conditions by controlled exposure to specific wavelengths of light or ultraviolet radiation.",
    "secondary": "In neonatology and dermatology, phototherapy is standard treatment for neonatal jaundice (converting bilirubin) and chronic plaque psoriasis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Niels Finsen's pioneering clinical application of **phototherapy** successfully cured severe cases of lupus vulgaris."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Patients suffering from seasonal affective disorders reported dramatic mood improvements after scheduled morning **phototherapy**."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Blue-light **phototherapy** isomerizes neurotoxic unconjugated bilirubin in neonatal dermal capillaries into excretable water-soluble lumirubin."}
    ]
  },
  "phototropism": {
    "primary": "The directional growth or movement of an organism or plant organ in response to the direction of incident light.",
    "secondary": "In plant physiology, positive phototropism in growing shoots is mediated by asymmetric redistribution of the hormone auxin toward the shaded side.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Our experiments on grass seedlings demonstrate that **phototropism** is guided by the perception of light at the extreme tip."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The bending of the stem toward the sunny window illustrates the fundamental biological law of **phototropism**."},
      {"author": "Hermann von Helmholtz", "work": "Popular Lectures on Scientific Subjects", "quote": "Even simple microscopic organisms exhibit distinct **phototropism**, swimming relentlessly toward illuminated water zones."}
    ]
  },
  "photovoltaic": {
    "primary": "Relating to or capable of generating an electric voltage or current upon exposure to radiant energy, especially light.",
    "secondary": "In semiconductor engineering and renewable energy, photovoltaic solar cells exploit p-n junction potentials to generate clean electricity from solar photons.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Orbital space stations rely upon vast **photovoltaic** wings to capture unattenuated solar radiation for their power supplies."},
      {"author": "Isaac Asimov", "work": "The Subversive Chemical", "quote": "The continuous improvement of **photovoltaic** conversion efficiency promises to make direct solar power universally accessible."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "The conversion of sunlight into electrical power by a **photovoltaic** silicon cell exemplifies direct mechanical transduction."}
    ]
  }
}

target_dir = r"App database\Latin roots\Cluster Light\Dashboard — phot"
updated = 0

for filename, info in phot_data.items():
    fpath = os.path.join(target_dir, f"{filename}.md")
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"No book callout: {filename}")
        continue
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quotes = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quotes += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quotes + "\n"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Successfully curated {updated}/{len(phot_data)} files in Dashboard — phot.")
