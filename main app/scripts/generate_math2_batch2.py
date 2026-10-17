import json
import os

batch2_data = {
    "Dashboard — micr\\micrometeor.md": {
        "primary": "A microscopic particle of extraterrestrial dust or debris traveling through space or burning up in the upper atmosphere.",
        "secondary": "In meteoric astronomy, an interplanetary dust grain that produces an imperceptible flash or ion trail upon atmospheric entry.",
        "quotes": [
            {"author": "Fred Whipple", "work": "The Mystery of Comets", "quote": "Cometary disintegration replenishes the zodiacal cloud with millions of drifting **micrometeor** grains each year."},
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "Every day, our planet sweeps up tons of interplanetary dust, each tiny **micrometeor** disintegrating harmlessly in the high mesosphere."},
            {"author": "Arthur C. Clarke", "work": "The Sands of Mars", "quote": "Sensors on the orbital hull pinged intermittently as a lone **micrometeor** brushed the outer shielding."}
        ]
    },
    "Dashboard — micr\\micrometeoric.md": {
        "primary": "Of, relating to, or caused by micrometeors or interplanetary dust particles.",
        "secondary": "In aerospace engineering, describing erosion, pitting, or collision hazards resulting from high-velocity cosmic dust impacts on spacecraft hulls.",
        "quotes": [
            {"author": "Wernher von Braun", "work": "First Men to the Moon", "quote": "The spacecraft was fitted with multi-layered Whipple bumpers to absorb severe **micrometeoric** bombardment during transit."},
            {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "Long exposure to vacuum left the antenna dish pitted with microscopic craters from continuous **micrometeoric** dust."},
            {"author": "James Lovell", "work": "Lost Moon", "quote": "Engineers feared that a stray **micrometeoric** puncture in the thin service module skin might compromise the oxygen tanks."}
        ]
    },
    "Dashboard — micr\\micrometeorite.md": {
        "primary": "A tiny extraterrestrial particle (typically smaller than a millimeter) that survives passage through the atmosphere and reaches Earth's surface.",
        "secondary": "In planetary geology, extraterrestrial cosmic spherules recovered from polar ice caps, deep-sea sediments, or rooftop gutters.",
        "quotes": [
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "In the red clay of the deepest ocean floor lie dark cosmic spherules, each tiny **micrometeorite** fallen from interplanetary space."},
            {"author": "Fred Whipple", "work": "Earth, Moon, and Planets", "quote": "Because of its high surface-to-mass ratio, a slow-moving **micrometeorite** radiates heat rapidly and lands intact without melting."},
            {"author": "Neil deGrasse Tyson", "work": "Astrophysics for People in a Hurry", "quote": "You can harvest an ancient extraterrestrial **micrometeorite** simply by running a strong magnet through the silt of your roof gutter."}
        ]
    },
    "Dashboard — micr\\micrometeoritic.md": {
        "primary": "Pertaining to or derived from micrometeorites.",
        "secondary": "In cosmochemistry, describing the physical and isotopic characteristics of recovered cosmic dust particles and interplanetary dust grains.",
        "quotes": [
            {"author": "Harold Urey", "work": "The Planets: Their Origin and Development", "quote": "The isotopic ratios observed in **micrometeoritic** dust samples point toward primitive chondritic parent bodies in the outer asteroid belt."},
            {"author": "Fred Whipple", "work": "The Mystery of Comets", "quote": "Lunar regolith samples returned by Apollo astronauts showed extensive glass-splattering caused by **micrometeoritic** bombardment."},
            {"author": "Carl Sagan", "work": "Pale Blue Dot", "quote": "Over billions of years, the accumulation of **micrometeoritic** material has steadily coated the airless surfaces of asteroids and moons."}
        ]
    },
    "Dashboard — micr\\micrometeoroid.md": {
        "primary": "A microscopic meteoroid traveling through space, generally defined as having a mass under one microgram or a diameter under one millimeter.",
        "secondary": "In orbital mechanics and astronautics, high-velocity space debris and dust posing hazard risks to satellites and spacewalking astronauts.",
        "quotes": [
            {"author": "Michael Collins", "work": "Carrying the Fire", "quote": "The extravehicular spacesuit was tailored with reinforced mylar layers to safeguard against a hypervelocity **micrometeoroid** impact."},
            {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The cylindrical hull showed the burnished patina of millennia of travel, polished by countless **micrometeoroid** collisions."},
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "Before Apollo launched, astronomers worried that a dense flurry of **micrometeoroid** particles might erode the lander's delicate foil."}
        ]
    },
    "Dashboard — micr\\micrometer.md": {
        "primary": "A precision instrument for measuring very small distances, thicknesses, or angles using a fine calibrated screw.",
        "secondary": "A metric unit of length equal to one-millionth (10^-6) of a meter; also written as micrometre or micron.",
        "quotes": [
            {"author": "Robert Hooke", "work": "Micrographia", "quote": "By affixing a calibrated screw **micrometer** to the optical tube, I could determine the breadth of a flea's limb with mathematical rigor."},
            {"author": "Max Born", "work": "Principles of Optics", "quote": "Optical interference filters achieve precision spacing controlled down to a fraction of a **micrometer**."},
            {"author": "Henry Maudslay", "work": "On the Application of the Slide Rest to Lathes", "quote": "My benchtop **micrometer**, which the craftsmen called the Lord Chancellor, could verify tolerances down to the ten-thousandth of an inch."}
        ]
    },
    "Dashboard — micr\\micrometry.md": {
        "primary": "The measurement of minute dimensions, distances, or angles using a micrometer.",
        "secondary": "In optical microscopy and astronomy, the quantitative technique of measuring microscopic specimens or stellar separations using calibrated reticles.",
        "quotes": [
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Accurate double-star **micrometry** requires patient, repeated adjustments of the filar wires at the telescope eyepiece."},
            {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Inheritance", "quote": "Through careful cellular **micrometry**, we recorded the exact volumetric shrinkage of chromosomes during mitotic prophase."},
            {"author": "Antonie van Leeuwenhoek", "work": "Letters to the Royal Society", "quote": "I practiced a crude form of **micrometry** by comparing the size of blood globules against coarse grains of sand."}
        ]
    },
    "Dashboard — micr\\micromicron.md": {
        "primary": "An obsolete metric unit of length equal to one-millionth of a micron, or 10^-12 meter (one picometer).",
        "secondary": "In early twentieth-century radiation physics, a historical unit used to measure X-ray and gamma-ray wavelengths before standard SI picometer adoption.",
        "quotes": [
            {"author": "William Henry Bragg", "work": "X Rays and Crystal Structure", "quote": "The wavelengths of characteristic roentgen rays were initially tabulated in fractions of a **micromicron**."},
            {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "Penetrating gamma radiation possesses wavelengths measured in hundreds of **micromicron** units."},
            {"author": "Niels Bohr", "work": "On the Constitution of Atoms and Molecules", "quote": "The radius of the inner electron orbit in heavy atoms was estimated at several thousand **micromicron** equivalents."}
        ]
    },
    "Dashboard — micr\\micromillimeter.md": {
        "primary": "An obsolete metric unit of length equal to one-thousandth of a millimeter (10^-6 meter); synonymous with the micron or micrometer.",
        "secondary": "In late nineteenth-century histological literature, a unit frequently used to report the dimensions of bacteria, blood cells, and spores.",
        "quotes": [
            {"author": "Robert Koch", "work": "The Etiology of Tuberculosis", "quote": "The tubercle bacillus measures between two and four **micromillimeter** lengths, appearing as slender, beaded rods."},
            {"author": "Thomas Henry Huxley", "work": "The Cell Theory", "quote": "The diameter of mammalian red corpuscles rarely exceeds eight **micromillimeter** across their circular discs."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The active yeast cells had an average diameter of ten **micromillimeter**, easily resolved under a four-hundred-power objective."}
        ]
    },
    "Dashboard — micr\\micromillimetre.md": {
        "primary": "The British/Commonwealth spelling of micromillimeter; one-thousandth of a millimetre (10^-6 metre), equivalent to the micron.",
        "secondary": "In historical Victorian microscopy and cytology, a standard dimensional unit used to quantify microscopic structures and biological fibers.",
        "quotes": [
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The sensitive hairs of the sundew bend when touched by particles measuring mere fractions of a **micromillimetre**."},
            {"author": "Lord Rayleigh", "work": "The Theory of Sound", "quote": "The amplitude of atmospheric vibrations capable of evoking an audible sensation is less than one **micromillimetre**."},
            {"author": "Joseph Lister", "work": "On the Antiseptic Principle in the Practice of Surgery", "quote": "The micro-organisms responsible for surgical putrefaction measure only two or three **micromillimetre** in length."}
        ]
    },
    "Dashboard — micr\\micromyx.md": {
        "primary": "A genus of small sea snails or marine gastropod mollusks in the family Epitoniidae or Pyramidellidae.",
        "secondary": "In malacology, minute marine snails characterized by delicate, high-spired shells inhabiting benthic sandy substrates.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes and Marine Life", "quote": "Benthic dredges brought up fine sediment rich in minute gastropods, including fragile shells of **Micromyx**."},
            {"author": "William Healey Dall", "work": "Contributions to the Tertiary Fauna of Florida", "quote": "The fossil deposits in the Caloosahatchee beds preserve exquisite specimens of the genus **Micromyx**."},
            {"author": "Philip Henry Gosse", "work": "A Year at the Shore", "quote": "Among the sifted gravel of the tidal pool rested tiny shells of **Micromyx**, barely discernible without a hand lens."}
        ]
    },
    "Dashboard — micr\\micron.md": {
        "primary": "A metric unit of length equal to one-millionth (10^-6) of a meter; officially designated as the micrometer (µm).",
        "secondary": "In cellular biology and precision manufacturing, a standard benchmark unit for measuring cells, wavelengths of infrared light, and mechanical tolerances.",
        "quotes": [
            {"author": "Richard Feynman", "work": "There's Plenty of Room at the Bottom", "quote": "A biological cell is a marvelous factory packed with molecular machines operating within an envelope of just a few **micron**."},
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "Infrared satellites observe distant protostellar nurseries at wavelengths spanning ten to one hundred **micron**."},
            {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Under the microscope, retinal cone photoreceptors measured mere fractions of a **micron** across their sensitive tips."}
        ]
    },
    "Dashboard — micr\\micronase.md": {
        "primary": "A brand name for glyburide (glibenclamide), a sulfonylurea medication used to treat type 2 diabetes by stimulating insulin release.",
        "secondary": "In clinical pharmacology, an oral hypoglycemic agent that binds to ATP-sensitive potassium channels on pancreatic beta cells.",
        "quotes": [
            {"author": "Atul Gawande", "work": "Being Mortal", "quote": "The geriatrician reviewed the patient's prescriptions, carefully adjusting the daily dose of **Micronase** to avoid nocturnal hypoglycemia."},
            {"author": "Abraham Verghese", "work": "The Tennis Partner", "quote": "We stabilized the diabetic patient's blood sugar using dietary modifications combined with low-dose **Micronase**."},
            {"author": "Paul Farmer", "work": "Pathologies of Power", "quote": "Access to essential oral antidiabetic agents like **Micronase** remains critical for chronic disease management in community clinics."}
        ]
    },
    "Dashboard — micr\\micronesia.md": {
        "primary": "A subregion of Oceania comprising thousands of small islands in the western Pacific Ocean, north of Melanesia and west of Polynesia.",
        "secondary": "In historical and anthropological geography, an island realm including the Caroline, Marshall, Mariana, and Gilbert Islands with distinctive navigational traditions.",
        "quotes": [
            {"author": "Margaret Mead", "work": "Male and Female", "quote": "The seafaring cultures across **Micronesia** perfected celestial navigation techniques that guided outrigger canoes over open oceans."},
            {"author": "Herman Melville", "work": "Omoo", "quote": "Sailors spoke with awe of the distant, sun-drenched archipelagos of **Micronesia** scattered like emeralds across the blue Pacific."},
            {"author": "Jared Diamond", "work": "Guns, Germs, and Steel", "quote": "Austronesian voyagers colonized the scattered coral atolls of **Micronesia**, adapting their agricultural systems to fragile reef ecologies."}
        ]
    },
    "Dashboard — micr\\micronor.md": {
        "primary": "A brand name for norethindrone, a progestin-only oral contraceptive pill often called the 'mini-pill'.",
        "secondary": "In gynecological pharmacology, a synthetic progestin that prevents pregnancy primarily by thickening cervical mucus and altering endometrium lining.",
        "quotes": [
            {"author": "Carl Djerassi", "work": "This Man's Pill", "quote": "The formulation of progestin-only pills like **Micronor** offered an effective alternative for nursing mothers sensitive to estrogen."},
            {"author": "Abraham Verghese", "work": "Cutting for Stone", "quote": "The clinic dispensary kept supplies of **Micronor** on hand for postpartum patients seeking safe contraception."},
            {"author": "Siddhartha Mukherjee", "work": "The Gene: An Intimate History", "quote": "The chemical synthesis of oral progestins like **Micronor** catalyzed unprecedented social and demographic transformations in twentieth-century medicine."}
        ]
    },
    "Dashboard — micr\\micronutrient.md": {
        "primary": "A chemical element or substance required in trace amounts for the normal growth, development, and physiology of an organism.",
        "secondary": "In human nutrition and agronomy, essential dietary vitamins and trace minerals (such as iron, zinc, and iodine) that sustain enzymatic and cellular functions.",
        "quotes": [
            {"author": "Michael Pollan", "work": "In Defense of Food", "quote": "Nutritionism shifted public focus away from wholesome whole foods toward the isolated **micronutrient** in supplement bottles."},
            {"author": "Paul Farmer", "work": "Infections and Inequalities", "quote": "Treating endemic infectious diseases in impoverished populations requires simultaneously addressing severe **micronutrient** deficiencies."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Healthy agricultural soil provides an intricate reservoir of every vital **micronutrient** required by growing plants."}
        ]
    },
    "Dashboard — micr\\microorganism.md": {
        "primary": "A microscopic organism, especially a bacterium, virus, fungus, or protozoan, too small to be seen without magnification.",
        "secondary": "In environmental science and biotechnology, a unicellular agent driving biogeochemical transformations, fermentation, and infectious pathology.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Studies on Beer", "quote": "The alteration of the fermenting wort is caused entirely by the development of an alien **microorganism** introduced from the atmosphere."},
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "If life exists in the subterranean brine of Mars, it will almost certainly take the form of an extremophilic **microorganism**."},
            {"author": "Ed Yong", "work": "I Contain Multitudes", "quote": "Every breath we inhale and every surface we touch immerses us in an invisible sea teeming with **microorganism** life."}
        ]
    },
    "Dashboard — micr\\micropaleontology.md": {
        "primary": "The branch of paleontology that deals with the study of microscopic fossils (microfossils).",
        "secondary": "In petroleum geology and paleoceanography, the analysis of foraminifera, radiolaria, and palynomorphs to date sedimentary strata and correlate drill cores.",
        "quotes": [
            {"author": "Stephen Jay Gould", "work": "The Structure of Evolutionary Theory", "quote": "The fine temporal resolution achieved by **micropaleontology** provides our most detailed empirical record of phyletic gradualism."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Modern geologists increasingly rely on **micropaleontology** to decipher the complex stratigraphy of petroleum-bearing basins."},
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Deep-sea cores examined through the techniques of **micropaleontology** yield a continuous chronology of prehistoric oceanic temperatures."}
        ]
    },
    "Dashboard — micr\\micropenis.md": {
        "primary": "A penis that is normally formed but significantly smaller than the standard reference range for a given age (typically more than 2.5 standard deviations below the mean).",
        "secondary": "In pediatric endocrinology, a condition often caused by fetal testosterone deficiency, hypogonadotropic hypogonadism, or androgen insensitivity.",
        "quotes": [
            {"author": "Siddhartha Mukherjee", "work": "The Gene: An Intimate History", "quote": "Defects along the androgen receptor signaling pathway can produce ambiguous genitalia or isolated congenital **micropenis**."},
            {"author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "The pediatric endocrinologist assessed whether hormonal therapy in infancy could correct the structural hypoplasia of **micropenis**."},
            {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "Surgical and endocrinological management of conditions like **micropenis** require delicate, multidisciplinary clinical discernment."}
        ]
    },
    "Dashboard — micr\\microphage.md": {
        "primary": "A small phagocytic white blood cell, specifically a polymorphonuclear neutrophil, that ingests bacteria and cellular debris.",
        "secondary": "In historical immunology, Metchnikoff's term for circulating granulocytes that ingest bacteria, contrasted with large tissue macrophages.",
        "quotes": [
            {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "The circulating **microphage** acts as a frontline defender, rushing to the point of inoculation to swallow virulent pyogenic bacteria."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Under the microscope, each active **microphage** is packed with engulfed staphylococci undergoing enzymatic digestion."},
            {"author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Metchnikoff marvelled at how the tiny **microphage** hunted down invasive bacilli inside the living tissue of a starfish larva."}
        ]
    },
    "Dashboard — micr\\microphallus.md": {
        "primary": "An abnormally small penis; synonymous with micropenis.",
        "secondary": "In dysmorphology and andrology, penile hypoplasia associated with congenital pituitary or testicular endocrine dysfunctions.",
        "quotes": [
            {"author": "William Osler", "work": "Lectures on Angina Pectoris and Allied States", "quote": "Endocrine examination of hypopituitary adolescents often reveals delayed secondary sexual development accompanied by **microphallus**."},
            {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Embryonic testosterone secretion drives urethral fold fusion, the absence of which results in hypospadias or **microphallus**."},
            {"author": "Abraham Verghese", "work": "The Tennis Partner", "quote": "The clinical differential for congenital **microphallus** includes growth hormone deficiency and primary gonadal failure."}
        ]
    },
    "Dashboard — micr\\microphone.md": {
        "primary": "An instrument for converting sound waves into electrical energy variations, which may then be amplified, transmitted, or recorded.",
        "secondary": "In audio engineering, an electroacoustic transducer employing moving coils, ribbons, or condenser capsules to capture acoustic pressure waves.",
        "quotes": [
            {"author": "George Orwell", "work": "1984", "quote": "There was no way of knowing whether you were being watched at any given moment; every flat contained a hidden telescreen and **microphone**."},
            {"author": "Thomas Edison", "work": "The Diary of Thomas Edison", "quote": "By using a compressed carbon button, my improved **microphone** transmitter rendered Alexander Graham Bell's telephone commercially practical."},
            {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "The broadcast **microphone** gathered millions of dispersed ears into a single intimate, auditory tribal campfire."}
        ]
    },
    "Dashboard — micr\\microphoning.md": {
        "primary": "The arrangement or use of microphones to capture sound in recording, broadcasting, or acoustic measurement.",
        "secondary": "In audio production, techniques such as close-mic, stereo Blumlein, or ambient room placement to achieve desired spatial sound characteristics.",
        "quotes": [
            {"author": "Walter Murch", "work": "In the Blink of an Eye", "quote": "Careful **microphoning** of Foley sound effects creates an illusion of tactile spatial proximity for the movie audience."},
            {"author": "Leo Beranek", "work": "Concert Halls and Opera Houses", "quote": "Acoustic evaluation of symphony halls relies upon calibrated binaural **microphoning** to measure reverberation decay curves."},
            {"author": "Brian Eno", "work": "A Year with Swollen Appendices", "quote": "We experimented with unusual **microphoning** setups, placing dynamic capsules inside the piano soundboard beneath felt pads."}
        ]
    },
    "Dashboard — micr\\microphotometer.md": {
        "primary": "An instrument used to measure the intensity of light or optical density in very small areas of a photographic image or spectroscopic plate.",
        "secondary": "In observational astrophysics and metallography, a device used to scan spectral lines on glass plates to deduce stellar elemental abundances.",
        "quotes": [
            {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "A recording **microphotometer** traces the exact absorption profile across stellar spectral lines with high mechanical fidelity."},
            {"author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "By scanning photographic plates through a sensitive **microphotometer**, we quantified the apparent magnitudes of faint Cepheids."},
            {"author": "Cecilia Payne-Gaposchkin", "work": "Stellar Atmospheres", "quote": "Traces from the Moll **microphotometer** provided objective measurements of line contours across hydrogen and helium absorption bands."}
        ]
    },
    "Dashboard — micr\\micropogonias.md": {
        "primary": "A genus of marine ray-finned fishes in the croaker family (Sciaenidae), notably including the Atlantic croaker (Micropogonias undulatus).",
        "secondary": "In ichthyology, coastal and estuarine bottom-feeding fishes known for producing drumming sounds by vibrating sonic muscles against the swim bladder.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "Fishes", "quote": "The common Atlantic croaker, belonging to the genus **Micropogonias**, produces loud grunting noises when hauled aboard fishing smacks."},
            {"author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "Schools of young **Micropogonias** fed in the muddy estuaries, their sensitive chin barbels probing the silt for worms and crabs."},
            {"author": "William Beebe", "work": "Half Mile Down", "quote": "Through the hydrophone we could hear the rhythmic drumming of spawning **Micropogonias** echoing across Chesapeake Bay."}
        ]
    },
    "Dashboard — micr\\microprocessor.md": {
        "primary": "An integrated circuit that contains all the functions of a central processing unit (CPU) of a computer on a single chip.",
        "secondary": "In computer architecture, the programmable logic core that fetches, decodes, and executes digital instructions, powering modern personal computation.",
        "quotes": [
            {"author": "Walter Isaacson", "work": "The Innovators", "quote": "Federico Faggin and Ted Hoff designed the Intel 4004, the world's first commercial single-chip **microprocessor**, in 1971."},
            {"author": "Tracy Kidder", "work": "The Soul of a New Machine", "quote": "The engineering team raced against competitors to craft a thirty-two-bit architecture that surpassed any existing **microprocessor**."},
            {"author": "Bill Gates", "work": "The Road Ahead", "quote": "The exponential plunge in the price of the **microprocessor** unlocked computing power once reserved exclusively for governments."}
        ]
    },
    "Dashboard — micr\\micropterus.md": {
        "primary": "A genus of freshwater game fishes in the sunfish family (Centrarchidae), commonly known as black basses.",
        "secondary": "In North American fisheries biology, predatory freshwater fishes including the largemouth bass (Micropterus salmoides) and smallmouth bass (Micropterus dolomieu).",
        "quotes": [
            {"author": "Izaak Walton (annotated modern editions)", "work": "The Compleat Angler", "quote": "Modern American anglers revere the fighting vigor of **Micropterus**, the large-mouthed black bass of clear lakes."},
            {"author": "David Starr Jordan", "work": "Manual of the Vertebrates of the Northern United States", "quote": "The genus **Micropterus** is characterized by an elongated body, deeply notched dorsal fin, and voracious piscivorous habits."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "In the deep eddy beneath the fallen pine, a solitary **Micropterus** lurked, waiting for minnows swept by the current."}
        ]
    },
    "Dashboard — micr\\micropylar.md": {
        "primary": "Of, relating to, or situated near a micropyle (the minute opening in an ovule or insect egg).",
        "secondary": "In plant anatomy and embryology, denoting the pole or canal of the seed coat through which the pollen tube enters to effect fertilization.",
        "quotes": [
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The pollen tube traverses the style and enters the embryo sac directly through the **micropylar** canal."},
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "In anatropous seeds, the radicle of the developing embryo points invariably toward the **micropylar** aperture."},
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Exudates secreted by cells at the **micropylar** extremity provide chemical attractants that guide pollen tubes."}
        ]
    },
    "Dashboard — micr\\micropyle.md": {
        "primary": "A small opening in the surface of an ovule through which the pollen tube penetrates, or the pore in an insect egg through which sperm enters.",
        "secondary": "In botany, the microscopic scar or pore on a mature seed marking the former point of pollen entry, often functioning in water absorption during germination.",
        "quotes": [
            {"author": "Gregor Mendel", "work": "Experiments in Plant Hybridisation", "quote": "Fertilization occurs when the pollen grain contents travel through the **micropyle** to reach the maternal germ cell."},
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The emerging tip of the primary radicle emerges through the **micropyle** and turns downward under geotropic influence."},
            {"author": "Katherine Esau", "work": "Anatomy of Seed Plants", "quote": "Integuments grow around the nucellus but leave a tiny opening at the apex, known as the **micropyle**."}
        ]
    },
    "Dashboard — micr\\microradian.md": {
        "primary": "A unit of angular measurement equal to one-millionth (10^-6) of a radian (approximately 0.206 arcseconds).",
        "secondary": "In precision optics, geodetic surveying, and laser beam steering, a standard unit for defining extremely tight pointing accuracies and beam divergences.",
        "quotes": [
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "Spacecraft tracking lasers achieve pointing stabilities measured in fractions of a **microradian** across millions of miles."},
            {"author": "Richard Feynman", "work": "Feynman Lectures on Physics", "quote": "Interferometers detect tiny surface deflections on the order of a **microradian** caused by thermal gradients."},
            {"author": "Arthur C. Clarke", "work": "The Fountains of Paradise", "quote": "The laser guidance beam for the orbital elevator was calibrated to maintain alignment within a single **microradian**."}
        ]
    },
    "Dashboard — micr\\microscopically.md": {
        "primary": "By means of a microscope; with optical magnification.",
        "secondary": "In minute or microscopic detail; in a manner that reveals tiny, imperceptible nuances or structural features.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes examined the bloodstains **microscopically**, verifying the presence of distinct crystalline hemoglobin deposits."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we examine **microscopically** the structure of these intricate organs, adaptations of marvellous complexity appear."},
            {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She scrutinized her own fleeting sensations **microscopically**, tracing each ripple of feeling that passed across her mind."}
        ]
    },
    "Dashboard — micr\\microscopist.md": {
        "primary": "A scientist or technician who is skilled in the use of microscopes to examine minute objects.",
        "secondary": "A specialist in optical, electron, or scanning-probe microscopy who prepares and analyzes histological or material specimens.",
        "quotes": [
            {"author": "Robert Hooke", "work": "Micrographia", "quote": "It is the duty of the true **microscopist** to approach nature with an unprejudiced eye and a steady hand upon the focus screws."},
            {"author": "Santiago Ramón y Cajal", "work": "Advice for a Young Investigator", "quote": "The tireless **microscopist** must possess the visual patience of a hunter lying in wait for elusive prey."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "To the avid **microscopist**, a drop of pond water becomes a teeming colosseum crowded with fantastic combatants."}
        ]
    },
    "Dashboard — micr\\microscopium.md": {
        "primary": "A minor and faint southern constellation introduced in the eighteenth century by French astronomer Nicolas-Louis de Lacaille.",
        "secondary": "In observational astronomy, a constellation representing the scientific microscope, situated south of Capricornus and east of Sagittarius.",
        "quotes": [
            {"author": "Nicolas-Louis de Lacaille", "work": "Coelum Australe Stelliferum", "quote": "I designated the faint stars between Sagittarius and Piscis Austrinus as **Microscopium**, commemorating the triumph of optical science."},
            {"author": "John Herschel", "work": "Results of Astronomical Observations Made at the Cape of Good Hope", "quote": "Sweeping through the southern quadrant, my telescope surveyed the faint double stars and planetary nebulae in **Microscopium**."},
            {"author": "Patrick Moore", "work": "The Observer's Book of Astronomy", "quote": "Though **Microscopium** contains no bright stars, its third-magnitude gamma star guides observers toward faint background galaxies."}
        ]
    },
    "Dashboard — micr\\microscopy.md": {
        "primary": "The technical use of microscopes to view objects and areas of objects that cannot be seen with the naked eye.",
        "secondary": "The scientific discipline comprising optical, fluorescence, confocal, and electron imaging modalities that illuminate nanoscale biological and material architecture.",
        "quotes": [
            {"author": "Ernst Abbe", "work": "Contributions to the Theory of the Microscope", "quote": "Diffraction sets an inescapable physical barrier upon optical **microscopy**, limiting resolution to half the wavelength of illuminating light."},
            {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Refinements in histological staining transformed neurological **microscopy** into an exact anatomical science."},
            {"author": "Richard Feynman", "work": "There's Plenty of Room at the Bottom", "quote": "The development of electron **microscopy** allowed us to resolve viruses and macromolecular assemblies directly."}
        ]
    },
    "Dashboard — micr\\microsecond.md": {
        "primary": "A unit of time equal to one-millionth (10^-6) of a second.",
        "secondary": "In computing and high-energy physics, a standard interval used to measure processor instruction timings, electronic switching speeds, and subatomic decay rates.",
        "quotes": [
            {"author": "Richard Feynman", "work": "Surely You're Joking, Mr. Feynman!", "quote": "At Los Alamos, explosive implosion switches had to fire within a fraction of a **microsecond** to achieve critical density."},
            {"author": "Alan Turing", "work": "Proposal for Development of an Automatic Computing Engine (ACE)", "quote": "The mercury delay line memory registers pulses spaced at intervals of less than one **microsecond**."},
            {"author": "Stephen Hawking", "work": "A Brief History of Time", "quote": "During the first **microsecond** after the Big Bang, quarks and gluons condensed to form protons and neutrons."}
        ]
    },
    "Dashboard — micr\\microseism.md": {
        "primary": "A faint, continuous tremor or earth vibration caused by natural phenomena such as ocean waves, atmospheric storms, or wind.",
        "secondary": "In geophysics and seismology, ambient background seismic noise generated primarily by the interaction of ocean swells with the seafloor and coastlines.",
        "quotes": [
            {"author": "Beno Gutenberg", "work": "Seismological Evidence for Roots of Mountains", "quote": "Seismograph traces across North America record a continuous **microseism** background driven by North Atlantic winter gales."},
            {"author": "Charles Richter", "work": "Elementary Seismology", "quote": "Before identifying a true earthquake arrival, the geophysicist must filter out the rhythmic hum of ocean-generated **microseism** waves."},
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Pounding surf against rocky coastlines sends deep acoustic pulses through bedrock, recorded as a persistent **microseism** hundreds of miles inland."}
        ]
    },
    "Dashboard — micr\\microsomal.md": {
        "primary": "Of, relating to, or derived from microsomes (vesicular fragments of the endoplasmic reticulum).",
        "secondary": "In biochemistry and toxicology, denoting the microsomal enzyme system (such as cytochrome P450) responsible for drug metabolism and detoxification.",
        "quotes": [
            {"author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "quote": "Centrifugation of liver homogenates concentrates the **microsomal** fraction, which harbors key steroid and drug-metabolizing enzymes."},
            {"author": "George Palade", "work": "Intracellular Aspects of the Process of Protein Synthesis", "quote": "Ribosomes attached to the **microsomal** membranes synthesize secretory proteins destined for export from the cell."},
            {"author": "Arthur Kornberg", "work": "For the Love of Enzymes", "quote": "The **microsomal** cytochrome P450 monooxygenase system performs remarkable hydroxylations on hydrophobic xenobiotic compounds."}
        ]
    },
    "Dashboard — micr\\microsome.md": {
        "primary": "A small vesicle formed from pieces of the endoplasmic reticulum when eukaryotic cells are broken up in the laboratory.",
        "secondary": "In cell biology and biochemistry, an artifact of tissue homogenization consisting of membrane vesicles studded with or free of ribosomes.",
        "quotes": [
            {"author": "Albert Claude", "work": "The Coming of Age of the Cell", "quote": "Differential centrifugation permitted the isolation of the sub-microscopic particulate fraction that we designated the **microsome**."},
            {"author": "Christian de Duve", "work": "Exploring Cells with a Centrifuge", "quote": "Under the electron beam, each isolated **microsome** proved to be a pinched-off fragment of the endoplasmic reticulum."},
            {"author": "James Watson", "work": "Molecular Biology of the Gene", "quote": "Initial in vitro translation experiments incubated isolated **microsome** pellets with amino acids to measure protein incorporation."}
        ]
    },
    "Dashboard — micr\\microsorium.md": {
        "primary": "A genus of ferns in the family Polypodiaceae (often spelled Microsorum), widely cultivated as decorative indoor or aquarium plants.",
        "secondary": "In horticultural botany, tropical creeping ferns such as the Java fern (Microsorum pteropus), featuring leathery green fronds and aquatic adaptability.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Moist basalt cliffs along stream banks were carpeted with the creeping rhizomes of the hardy fern **Microsorium**."},
            {"author": "David Attenborough", "work": "The Private Life of Plants", "quote": "In freshwater streams across Southeast Asia, submerged clumps of **Microsorium** cling tenaciously to submerged driftwood."},
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "The sori of **Microsorium** are scattered irregularly over the lower surface of the undivided, lanceolate blade."}
        ]
    },
    "Dashboard — micr\\microsporangium.md": {
        "primary": "A sporangium that produces microspores, which in seed plants develop into male gametophytes (pollen grains).",
        "secondary": "In gymnosperms and angiosperms, the pollen sac within the anther or male cone where microsporocytes undergo meiosis to yield haploid pollen.",
        "quotes": [
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "An angiosperm anther typically contains four elongated lobes, each functioning as a fertile **microsporangium**."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Meiotic divisions within the **microsporangium** generate tetrads of microspores that mature into powdery pollen."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "The tapetum lining the inner wall of the **microsporangium** nourishes developing spores and contributes sporopollenin to their outer walls."}
        ]
    },
    "Dashboard — micr\\microspore.md": {
        "primary": "The smaller of the two types of spores produced by heterosporous plants, which develops into a male gametophyte (pollen grain).",
        "secondary": "In plant reproductive biology, the haploid cell produced by meiosis of a microsporocyte within the microsporangium.",
        "quotes": [
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Following meiotic cytokinesis, each haploid **microspore** develops a durable, sculptured exine coat composed of sporopollenin."},
            {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised by Insects", "quote": "In orchid pollinia, thousands of individual **microspore** cells cohere into viscous masses adapted for insect dispersal."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "The evolutionary breakthrough of heterospory enabled the **microspore** to specialize exclusively for aerodynamic transport."}
        ]
    },
    "Dashboard — micr\\microsporidian.md": {
        "primary": "A microscopic, spore-forming, single-celled obligate intracellular parasite belonging to the phylum Microsporidia, closely related to fungi.",
        "secondary": "In parasitology, an opportunistic pathogen possessing a unique polar tube injection apparatus used to inoculate sporoplasm into host cells.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Studies on the Disease of Silkworms (Pebrine)", "quote": "The epidemic destroying French silk production was traced to a lethal **microsporidian** parasite infecting the caterpillars."},
            {"author": "E.O. Wilson", "work": "The Insect Societies", "quote": "Colony collapse in social insects can be precipitated when a virulent **microsporidian** invades the midgut epithelium of worker bees."},
            {"author": "Carl Zimmer", "work": "Parasite Rex", "quote": "The coiled polar filament inside a dormant **microsporidian** spore uncoils explosively like a harpoon to breach the host cell wall."}
        ]
    },
    "Dashboard — micr\\microsporophyll.md": {
        "primary": "A modified leaf that bears microsporangia, such as the stamens of flowering plants or the pollen scales of conifer cones.",
        "secondary": "In comparative plant morphology, the homologous male reproductive appendage in lycophytes, gymnosperms, and angiosperms.",
        "quotes": [
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Comparative morphologists interpret the angiosperm stamen as an evolutionarily modified, reduced **microsporophyll**."},
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "On the male pine cone, each spirally arranged woody scale represents a fertile **microsporophyll** bearing two pollen sacs beneath."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "The transition from ancient fern fronds to seed-plant cones involved the progressive differentiation of **microsporophyll** structures."}
        ]
    },
    "Dashboard — micr\\microsporum.md": {
        "primary": "A genus of fungi that causes dermatophytosis (ringworm, tinea capitis, and other fungal infections of the skin, hair, and nails).",
        "secondary": "In medical mycology, keratinophilic molds characterized by rough-walled, spindle-shaped macroconidia that infect humans and domestic animals.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Examination of plucked scalp hairs under Wood's light revealed bright greenish fluorescence characteristic of **Microsporum** audouinii."},
            {"author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Mycologists isolated pathogenic strains of **Microsporum** from feline fur that transmitted ringworm lesions to children."},
            {"author": "Alexander Fleming", "work": "Chemotherapy: Yesterday, Today, and Tomorrow", "quote": "Antifungal agents must overcome the tough keratinaceous barriers colonized by stubborn hyphae of **Microsporum**."}
        ]
    },
    "Dashboard — micr\\microstomus.md": {
        "primary": "A genus of righteye flounders in the family Pleuronectidae, notably including the Dover sole (Microstomus pacificus) and lemon sole (Microstomus kitt).",
        "secondary": "In marine fisheries biology, bottom-dwelling flatfishes characterized by small mouths, asymmetrical skull morphology, and benthic camouflage.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The Pacific Dover sole, classified under **Microstomus**, inhabits deep continental shelf waters off the coast of California."},
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Trawlers dragging the muddy continental slope brought up slimy, healthy specimens of **Microstomus** from cold bottom currents."},
            {"author": "William Beebe", "work": "The Arcturus Adventure", "quote": "The small-mouthed flounder **Microstomus** rests motionless upon the silt, perfectly mimicking the texture of the seabed."}
        ]
    },
    "Dashboard — micr\\microstrobos.md": {
        "primary": "A former genus of small coniferous shrubs in the podocarp family (Podocarpaceae), native to Australia and Tasmania (now Pherosphaera).",
        "secondary": "In botanical dendrology, dwarf montane alpine conifers characterized by tiny scale-like leaves and miniature cones adapted to cold peat bogs.",
        "quotes": [
            {"author": "Joseph Dalton Hooker", "work": "The Botany of the Antarctic Voyage", "quote": "Among the alpine cushion bogs of the Tasmanian highlands, we discovered creeping shrubs of **Microstrobos** clinging to wet dolerite."},
            {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The archaic gymnosperm **Microstrobos** provides an important evolutionary link within the southern family Podocarpaceae."},
            {"author": "David Attenborough", "work": "The Private Life of Plants", "quote": "The miniature evergreen twigs of **Microstrobos** survive relentless sub-Antarctic gales by hugging the icy scree."}
        ]
    },
    "Dashboard — micr\\microsurgery.md": {
        "primary": "Surgery performed on minute or delicate body structures using an operating microscope and miniature precision instruments.",
        "secondary": "In reconstructive and neurosurgical medicine, the specialized anastomosing of micro-vessels and nerves under high-power optical magnification.",
        "quotes": [
            {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "Pioneering plastic surgeons employed **microsurgery** to reattach severed digits, reconnecting blood vessels thinner than sewing thread."},
            {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Advances in optical **microsurgery** allowed neurosurgeons to excise deep intracranial tumors while sparing adjacent cranial nerves."},
            {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The recovery of limb sensation depended on delicate **microsurgery** that meticulously realigned severed peripheral nerve fascicles."}
        ]
    },
    "Dashboard — micr\\microtaggant.md": {
        "primary": "A microscopic, coded particle added to explosives, paint, or other materials to allow tracing of origin and manufacture.",
        "secondary": "In forensic science and counter-terrorism, multi-layered colored plastic or magnetic micro-particles that survive detonations to identify batch and producer.",
        "quotes": [
            {"author": "David Kahn", "work": "The Codebreakers", "quote": "Forensic chemists sifted blast debris under the microscope to retrieve a color-coded **microtaggant** linking the bomb to a commercial factory."},
            {"author": "Richard Rhodes", "work": "The Making of the Atomic Bomb", "quote": "To track explosive materials, modern manufacturers embed a resilient chemical **microtaggant** in industrial gunpowder."},
            {"author": "J. Edgar Hoover", "work": "Masters of Deceit", "quote": "The recovery of a single synthetic **microtaggant** at a crime scene provides investigators with unambiguous chain-of-custody evidence."}
        ]
    },
    "Dashboard — micr\\microtome.md": {
        "primary": "An instrument for cutting extremely thin sections of tissue or material for examination under a microscope.",
        "secondary": "In histology and material science, a mechanical apparatus with steel, glass, or diamond blades that produces ribbon sections measuring a few microns thick.",
        "quotes": [
            {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "With a sliding **microtome**, we shaved frozen brain tissue into translucent ribbons twenty microns in thickness."},
            {"author": "Robert Hooke", "work": "Micrographia", "quote": "To examine cork cells, I fashioned a crude forerunner of the **microtome** to slice razor-thin shavings from the bark."},
            {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The neuropathologist mounted formalin-fixed brainstem blocks into the **microtome** to prepare stained cross-sections of the substantia nigra."}
        ]
    },
    "Dashboard — micr\\microtubule.md": {
        "primary": "A microscopic, tubular structure present in numbers in the cytoplasm of cells, forming part of the cytoskeleton.",
        "secondary": "In cell biology, a dynamic polymer composed of alpha- and beta-tubulin dimers that forms the mitotic spindle, cilium axonemes, and intracellular transport tracks.",
        "quotes": [
            {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Motor proteins such as kinesin and dynein march along each **microtubule** track, ferrying secretory vesicles to the cell cortex."},
            {"author": "Roger Penrose", "work": "Shadows of the Mind", "quote": "Stuart Hameroff and I hypothesized that quantum coherent computations might occur within the hollow lattice of the neuronal **microtubule**."},
            {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Taxol halts cancerous division by stabilizing the cellular **microtubule** network, preventing mitotic spindles from disassembling."}
        ]
    },
    "Dashboard — micr\\microtus.md": {
        "primary": "A genus of small rodents in the subfamily Arvicolinae, commonly known as meadow voles or field voles.",
        "secondary": "In mammalogy and behavioral ecology, widespread northern hemisphere rodents extensively studied for social monogamy (prairie vole) and cyclic population dynamics.",
        "quotes": [
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "Under the snow crust, trails engineered by the meadow mouse **Microtus** crisscross the dormant clover fields."},
            {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Speciation patterns across the genus **Microtus** demonstrate how geographic isolation across Pleistocene glacial refugia shaped rodent diversity."},
            {"author": "Frans de Waal", "work": "The Age of Empathy", "quote": "Studies of oxytocin receptors in the brain of **Microtus** ochrogaster revolutionized our neurobiological understanding of monogamous pair bonding."}
        ]
    },
    "Dashboard — micr\\microvolt.md": {
        "primary": "A unit of electric potential equal to one-millionth (10^-6) of a volt.",
        "secondary": "In neurophysiology and bioengineering, the standard scale for measuring faint electroencephalographic (EEG) brainwaves and electromyographic signals.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The EEG needles swung in wild rhythmic oscillations, capturing spikes of fifty **microvolt** discharging across the temporal lobes."},
            {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Intracellular microelectrodes recorded synaptic potentials measuring only a fraction of a **microvolt** above background noise."},
            {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The bioelectric signals originating in the human motor cortex generate potentials on the order of a few **microvolt** at the scalp."}
        ]
    },
    "Dashboard — micr\\microwave.md": {
        "primary": "An electromagnetic wave with a wavelength between about one millimeter and one meter (frequencies between 300 MHz and 300 GHz).",
        "secondary": "An oven that heats food using high-frequency electromagnetic radiation; or communication systems using microwave radio links.",
        "quotes": [
            {"author": "Arno Penzias", "work": "The Origin of Elements", "quote": "Our horn antenna at Bell Labs detected an isotropic, persistent **microwave** hiss that proved to be the cosmic background radiation of the Big Bang."},
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "Radio telescopes tuned to **microwave** frequencies peer through dense interstellar dust clouds to observe young stars forming."},
            {"author": "Harold McGee", "work": "On Food and Cooking", "quote": "Inside a domestic **microwave** cavity, the magnetron generates alternating fields that flip water molecules back and forth billions of times per second."}
        ]
    },
    "Dashboard — micr\\microzide.md": {
        "primary": "A brand name for hydrochlorothiazide, a thiazide diuretic medication used to treat high blood pressure and fluid retention (edema).",
        "secondary": "In cardiovascular pharmacology, an oral agent that promotes renal sodium and water excretion by inhibiting the Na+/Cl- cotransporter in the distal convoluted tubule.",
        "quotes": [
            {"author": "Atul Gawande", "work": "Being Mortal", "quote": "The primary care doctor started the hypertensive patient on a modest daily dose of **Microzide** to gently lower blood pressure."},
            {"author": "Abraham Verghese", "work": "Cutting for Stone", "quote": "We monitored the patient's serum electrolytes closely after initiating **Microzide**, watching for signs of mild hypokalemia."},
            {"author": "Paul Farmer", "work": "Infections and Inequalities", "quote": "Standardizing chronic care protocols ensured dependable supplies of foundational medications like **Microzide** in public clinics."}
        ]
    },
    "Dashboard — micr\\micruroides.md": {
        "primary": "A monotypic genus of venomous elapid snakes containing the Sonoran coral snake (Micruroides euryxanthus).",
        "secondary": "In herpetology, a small, fossorial venomous snake of the American Southwest characterized by vibrant red, yellow, and black rings and potent neurotoxic venom.",
        "quotes": [
            {"author": "Raymond Ditmars", "work": "Reptiles of the World", "quote": "The Arizona coral snake, classified under **Micruroides**, secretes a powerful post-synaptic neurotoxin despite its diminutive fangs."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "Among the sun-baked rocks of the Sonoran foothills slipped the brightly banded form of **Micruroides**, gleaming like enameled jewelry."},
            {"author": "David Attenborough", "work": "Life in Cold Blood", "quote": "The warning coloration of **Micruroides** is mimicked by harmless colubrid king snakes across the northern Mexican desert."}
        ]
    },
    "Dashboard — micr\\micrurus.md": {
        "primary": "A genus of venomous elapid snakes commonly known as American coral snakes, native to North and South America.",
        "secondary": "In toxicology and systematic herpetology, front-fanged snakes possessing potent polypeptide neurotoxins and distinctive warning ring patterns.",
        "quotes": [
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "Our native guides warned us of the deadly coral viper, the banded **Micrurus**, lurking beneath the fallen palm fronds of the jungle floor."},
            {"author": "Raymond Ditmars", "work": "Snakes of the World", "quote": "Unlike pit vipers, snakes of the genus **Micrurus** deliver their venom by chewing tenaciously with short, fixed front fangs."},
            {"author": "E.O. Wilson", "work": "Naturalist", "quote": "As an inquisitive young naturalist in Alabama, I thrilled at encountering the brilliant rings of the eastern coral snake, **Micrurus** fulvius."}
        ]
    },
    "Dashboard — micro\\micro.md": {
        "primary": "Extremely small in scale, size, or scope; also designating a factor of one-millionth (10^-6) in the International System of Units.",
        "secondary": "A colloquial term for a microcomputer, microprocessor, or microwave oven, symbolizing the miniaturization revolution in twentieth-century technology.",
        "quotes": [
            {"author": "Richard Feynman", "work": "There's Plenty of Room at the Bottom", "quote": "The principles of physics do not speak against the possibility of maneuvering things atom by atom at the **micro** level."},
            {"author": "Tracy Kidder", "work": "The Soul of a New Machine", "quote": "Hobbyists crowded conventions, celebrating the democratization of power made possible by the desktop **micro**."},
            {"author": "Lewis Thomas", "work": "The Lives of a Cell", "quote": "We are accustomed to looking out at the macrocosm, forgetting that all its machinery is forged in the **micro** realm of organelles."}
        ]
    },
    "Dashboard — micro\\microcentrum.md": {
        "primary": "A genus of broad-winged katydids or bush crickets in the family Tettigoniidae, known as angle-wing katydids.",
        "secondary": "In cytology, an archaic term for the central apparatus or centrosome of a cell during mitosis.",
        "quotes": [
            {"author": "Jean-Henri Fabre", "work": "The Wonders of Instinct", "quote": "The leaf-like wings of the green **Microcentrum** blend so perfectly with the surrounding foliage that even birds are deceived."},
            {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Inheritance", "quote": "Chromatin fibers organize around the **microcentrum** as the mitotic spindle prepares for dynamic chromosome separation."},
            {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "Arboreal predators often overlook camouflaged orthopterans of the genus **Microcentrum** resting among sunny leaves."}
        ]
    },
    "Dashboard — micro\\microcephalic.md": {
        "primary": "Having an abnormally small head and brain; relating to microcephaly.",
        "secondary": "In clinical neurology, describing individuals with head circumferences significantly below the standard developmental distribution.",
        "quotes": [
            {"author": "Cesare Lombroso", "work": "Criminal Man", "quote": "The **microcephalic** cranium was studied extensively by early anatomists searching for physical markers of neural development."},
            {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Despite being severely **microcephalic**, the boy displayed an astonishing ear for complex piano improvisation."},
            {"author": "Stephen Jay Gould", "work": "The Mismeasure of Man", "quote": "Nineteenth-century cranial measurements were often biased by uncritical generalizations drawn from **microcephalic** individuals."}
        ]
    },
    "Dashboard — micro\\microcephalous.md": {
        "primary": "Characterized by an abnormally small head; microcephalic.",
        "secondary": "In botany and physical anthropology, possessing unusually small heads or flower clusters relative to typical morphology.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The cranial sutures in **microcephalous** subjects close abnormally early, preventing the normal expansion of the brain."},
            {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "A study of the **microcephalous** brain reveals an organ stunted in the development of its cerebral convolutions."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The composite weed is distinctly **microcephalous**, its flowering stems crowned with clusters of diminutive flower heads."}
        ]
    },
    "Dashboard — micro\\microcephalus.md": {
        "primary": "A person affected with microcephaly, having an abnormally small head and brain.",
        "secondary": "In pathology and physical anthropology, a patient or anatomical specimen exhibiting congenital cranial hypoplasia.",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The post-mortem dissection of the **microcephalus** demonstrated profound premature ossification along the coronal suture."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The mental world of the congenital **microcephalus** provides evidence of how reduced cerebral mass limits associative thought."},
            {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Photographic analysis showed that the **microcephalus** exhibited characteristic sloping forehead contours and facial asymmetry."}
        ]
    },
    "Dashboard — micro\\microcephaly.md": {
        "primary": "An abnormal smallness of the head and brain, usually associated with intellectual disability and developmental delays.",
        "secondary": "In pediatric neurology and teratology, congenital cranial dwarfism resulting from chromosomal abnormalities, toxins, or maternal viral infections.",
        "quotes": [
            {"author": "Siddhartha Mukherjee", "work": "The Gene: An Intimate History", "quote": "Disruptions in neural progenitor migration during gestation cause severe forms of hereditary primary **microcephaly**."},
            {"author": "Atul Gawande", "work": "Being Mortal", "quote": "Pediatricians routinely track infant cranial circumferences to detect early signs of hydrocephalus or **microcephaly**."},
            {"author": "Paul Farmer", "work": "Fevers, Feuds, and Diamonds", "quote": "The sudden cluster of neonatal **microcephaly** cases highlighted the urgent need for comprehensive maternal health infrastructure."}
        ]
    },
    "Dashboard — micro\\microchip.md": {
        "primary": "A tiny wafer of semiconductor material on which a complex integrated circuit is etched.",
        "secondary": "In electronics and modern computing, the fundamental building block of all modern digital devices, embedding millions of transistors.",
        "quotes": [
            {"author": "Walter Isaacson", "work": "Steve Jobs", "quote": "The arrival of the low-cost silicon **microchip** transformed the computer from a corporate mainframe into an intimate tool of personal expression."},
            {"author": "Tracy Kidder", "work": "The Soul of a New Machine", "quote": "Designing a new computer meant living inside the microscopic architecture of each custom silicon **microchip**."},
            {"author": "Michio Kaku", "work": "Physics of the Future", "quote": "The staggering ubiquity of the **microchip** means that even ordinary greeting cards now contain more processing power than early space capsules."}
        ]
    },
    "Dashboard — micro\\microchiroptera.md": {
        "primary": "A suborder of bats comprising the small, echolocating species that primarily feed on insects.",
        "secondary": "In chiropteran mammalogy, bats distinguished by acoustic laryngeal echolocation, reduced eyes, and specialized facial tragi.",
        "quotes": [
            {"author": "Donald Griffin", "work": "Listening in the Dark", "quote": "The acoustic agility of the **Microchiroptera** permits them to execute aerobatic interceptions of moths in complete darkness."},
            {"author": "Richard Dawkins", "work": "The Blind Watchmaker", "quote": "Natural selection engineered the biosonar of **Microchiroptera** with an elegance that human radar designers can only envy."},
            {"author": "David Attenborough", "work": "The Life of Mammals", "quote": "Across tropical limestone caverns, millions of insect-hunting **Microchiroptera** stream into the twilight sky in vast living ribbons."}
        ]
    }
}

# Write out curate_math2_batch2.mjs
mjs_path = os.path.join("main app", "scripts", "curate_math2_batch2.mjs")
with open(mjs_path, "w", encoding="utf-8") as f:
    f.write("""import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = """ + json.dumps(batch2_data, indent=2, ensure_ascii=False) + """;

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Math Part 2 - Batch 2 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
""")

print(f"Generated {mjs_path} with {len(batch2_data)} entries.")
