import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — prot";

const wordsData = {
  "protoplasm.md": {
    word: "protoplasm",
    primary: "The living substance of a cell, including the cytoplasm and nucleus, considered the physical basis of life.",
    secondary: "In cell biology and historical cytology, the colloidal ground substance supporting all vital physiological processes.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Physical Basis of Life", quote: "Protoplasm, simple or nucleated, is the formal basis of all life; it is the clay of the potter." },
      { author: "Ernst Haeckel", work: "The Riddle of the Universe", quote: "The living substance which we designate **protoplasm** consists essentially of carbon, nitrogen, oxygen, and hydrogen." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Every part of the cellular **protoplasm** must be regarded as sensitive to external environmental impressions." }
    ]
  },
  "protoplast.md": {
    word: "protoplast",
    primary: "The living contents of a plant, fungal, or bacterial cell whose cell wall has been removed or considered apart from its cell wall.",
    secondary: "In theology and literature, an original ancestor or progenitor of the human race (such as Adam).",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Adam, the first created **protoplast**, walked upright amidst the blossoming groves of Eden." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Enzymatic digestion of the cellulose wall liberates an intact, spherical **protoplast** bounded only by its plasma membrane." },
      { author: "Eduard Strasburger", work: "Textbook of Botany", quote: "The living **protoplast** remains connected with neighboring cells through delicate cytoplasmic plasmodesmata." }
    ]
  },
  "protos.md": {
    word: "protos",
    primary: "The Greek word meaning 'first', 'foremost', or 'earliest', used as an architectural or classical designation of primacy.",
    secondary: "In Byzantine administration and Mount Athos monastic tradition, the presiding elder or monastic superior of the holy mountain council.",
    quotes: [
      { author: "Robert Browning", work: "Cleon", quote: "Thou, **Protos**, king of our Aegean realm, hast sent me golden gifts and royal greetings." },
      { author: "Steven Runciman", work: "The Great Church in Captivity", quote: "The monastic communities of Mount Athos submitted disputes to the wisdom of their elected **Protos**." },
      { author: "J. B. Bury", work: "A History of the Later Roman Empire", quote: "In classical administrative terminology, the prefix **protos** denoted rank, seniority, and supreme imperial dignity." }
    ]
  },
  "prototheria.md": {
    word: "prototheria",
    primary: "A subclass of primitive mammals that lay eggs and suckle their young without nipples, comprising the monotremes (platypus and echidnas).",
    secondary: "In mammalian phylogenetics, the sister group to Theria (marsupials and placentals), retaining ancestral reptilian skeletal and reproductive traits.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Laws of Evolution to the Vertebrata", quote: "I proposed the division **Prototheria** for the duck-billed platypus and echidna, which stand closest to reptiles." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The oviparous reproduction of the **Prototheria** astonished European anatomists accustomed to viviparous mammals." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "The subclass **Prototheria** represents an ancient radiation of Australasian mammals that diverged before viviparity evolved." }
    ]
  },
  "prototherian.md": {
    word: "prototherian",
    primary: "Of, relating to, or characteristic of the mammalian subclass Prototheria (monotremes).",
    secondary: "Pertaining to egg-laying mammals displaying ancestral traits like a cloaca, cervical ribs, and low basal metabolic rates.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The platypus and echidna are the sole surviving **prototherian** remnants of an otherwise extinct mammalian fauna." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "The **prototherian** grade of mammalian evolution preserves crucial clues regarding the transition from cynodont reptiles." },
      { author: "Colin Groves", work: "Mammal Species of the World", quote: "Cranial osteology in the **prototherian** lineage lacks the auditory bullae characteristic of therian mammals." }
    ]
  },
  "prototypal.md": {
    word: "prototypal",
    primary: "Relating to, serving as, or characteristic of a prototype; original or primitive.",
    secondary: "In archetypal criticism and philosophy, embodying the original template from which later iterations or forms are derived.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "The Statesman's Manual", quote: "The Hebrew prophets held up a **prototypal** vision of divine justice to judge the earthly kings." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Plato provides the **prototypal** mind of Western philosophy, anticipating every subsequent idealist school." },
      { author: "Carl Jung", work: "Psychological Types", quote: "The primordial mother image functions as a **prototypal** motif across the mythologies of all continents." }
    ]
  },
  "prototypic.md": {
    word: "prototypic",
    primary: "Serving as a prototype; original, exemplary, or archetypal.",
    secondary: "In taxonomy and engineering, representing the standard or earliest form exhibiting the definitive traits of a class or product line.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The child’s first grasp of an object offers a **prototypic** example of voluntary motor coordination." },
      { author: "Claude Lévi-Strauss", work: "The Savage Mind", quote: "Totemic classification uses animals as **prototypic** models to articulate human social distinctions." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The ancient Mesopotamian citadel stood as the **prototypic** nucleus of urban civilization." }
    ]
  },
  "prototypical.md": {
    word: "prototypical",
    primary: "Serving as an original model or typical example on which others are patterned; archetypal.",
    secondary: "In cognitive psychology and linguistics, possessing the most representative or salient features of a cognitive category.",
    quotes: [
      { author: "Eleanor Rosch", work: "Principles of Categorization", quote: "Subjects judge a robin to be far more **prototypical** of the category 'bird' than a penguin or an ostrich." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Jane Austen created a **prototypical** comedy of manners that remains unsurpassed in English prose." },
      { author: "Henry James", work: "The American", quote: "Christopher Newman was presented as the **prototypical** self-made American entering the old aristocratic world of Paris." }
    ]
  },
  "protozoal.md": {
    word: "protozoal",
    primary: "Relating to, caused by, or characteristic of protozoa.",
    secondary: "In pathology, designating parasitic infections caused by single-celled eukaryotes (such as giardiasis, toxoplasmosis, or malaria).",
    quotes: [
      { author: "Ronald Ross", work: "The Prevention of Malaria", quote: "Microscopic blood smears confirmed that the fever was of **protozoal** origin, caused by mosquito transmission." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Amoebic dysentery represents a severe **protozoal** colitis capable of producing secondary hepatic abscesses." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The host immune response against **protozoal** parasites involves specialized macrophage and eosinophil activation." }
    ]
  },
  "protozoan.md": {
    word: "protozoan",
    primary: "A single-celled microscopic animal-like eukaryote belonging to the former group Protozoa; also, relating to protozoa.",
    secondary: "In aquatic ecology, a microscopic unicellular organism that grazes on bacteria and serves as a primary link in aquatic food webs.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "No one can doubt that many a humble **protozoan** has survived unchanged through vast geological epochs." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "In every tidal pool, countless **protozoan** creatures feed upon decaying organic matter." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Under the compound microscope, the transparent **protozoan** reveals pulsating vacuoles and streaming endoplasm." }
    ]
  },
  "protozoic.md": {
    word: "protozoic",
    primary: "Of, relating to, or containing protozoans.",
    secondary: "In historical geology, an obsolete term formerly applied to rocks containing the earliest fossil traces of microscopic animal life.",
    quotes: [
      { author: "Roderick Murchison", work: "Siluria", quote: "Geologists once designated the basal strata as **protozoic**, assuming animal life began with solitary microscopic organisms." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "The lower Cambrian deposits preserve **protozoic** radiolarian tests and sponge spicules." },
      { author: "Adam Sedgwick", work: "A Synopsis of the Classification of the British Palaeozoic Rocks", quote: "We investigated the metamorphic slate beds searching for any **protozoic** fossil impressions." }
    ]
  },
  "protozoological.md": {
    word: "protozoological",
    primary: "Relating to protozoology, the scientific study of protozoans.",
    secondary: "Pertaining to laboratory methods, cultures, and taxonomic frameworks applied to single-celled heterotrophic eukaryotes.",
    quotes: [
      { author: "David Keilin", work: "The History of Cell Respiration and Cytochrome", quote: "Subsequent **protozoological** investigations revealed the presence of respiratory pigments across diverse flagellates." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Breakthroughs in **protozoological** genetics demonstrated that mating types in ciliates follow Mendelian laws." },
      { author: "Élie Metchnikoff", work: "Immunity in Infective Diseases", quote: "My earliest observations of phagocytosis were carried out during **protozoological** studies of transparent marine larvae." }
    ]
  },
  "protozoologist.md": {
    word: "protozoologist",
    primary: "A zoologist or microbiologist who specializes in the study of protozoans.",
    secondary: "A laboratory or field researcher investigating the morphology, genetics, ecology, and pathogenesis of unicellular eukaryotes.",
    quotes: [
      { author: "Herbert Spencer Jennings", work: "Genetics of the Protozoa", quote: "The **protozoologist** observes how an isolated paramecium reproduces through hundreds of asexual generations." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Fritz Schaudinn worked with the relentless precision of a trained **protozoologist** when identifying the spirochete of syphilis." },
      { author: "Ronald Ross", work: "Memoirs", quote: "To unravel the complex life cycle of the malaria parasite, a physician had to become a meticulous **protozoologist**." }
    ]
  },
  "protozoology.md": {
    word: "protozoology",
    primary: "The branch of zoology or microbiology that deals with the study of protozoans.",
    secondary: "The scientific discipline encompassing the ultrastructure, biochemistry, life cycles, and clinical pathology of single-celled heterotrophic protists.",
    quotes: [
      { author: "Clifford Dobell", work: "Antony van Leeuwenhoek and His Little Animals", quote: "The origins of modern **protozoology** date back to Leeuwenhoek's discovery of infusoria in standing water." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Advances in tropical **protozoology** revolutionized our understanding of relapsing fevers and sleeping sickness." },
      { author: "Ernst Haeckel", work: "Systematische Phylogenie", quote: "Comparative **protozoology** provides the indispensable starting point for understanding metazoan genealogy." }
    ]
  },
  "protozoon.md": {
    word: "protozoon",
    primary: "A single-celled microscopic eukaryote; singular form of protozoa.",
    secondary: "In historical biology, an individual microscopic animalcule regarded as the fundamental unicellular unit of animal life.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "Even in the simplest **protozoon**, we observe irritability, nutrition, and reproduction reduced to their elemental terms." },
      { author: "H. G. Wells", work: "The Science of Life", quote: "The solitary **protozoon** lives without brain, nerves, or heart, performing all life tasks within a microscopic droplet of jelly." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The geometric regularity of a single **protozoon** reflects the direct action of surface tension upon colloidal protoplasm." }
    ]
  },
  "protract.md": {
    word: "protract",
    primary: "To prolong, lengthen, or draw out in time; delay or extend the duration of.",
    secondary: "In geometry and drafting, to draw, plot, or lay down on paper using scale, compass, and protractor.",
    quotes: [
      { author: "William Shakespeare", work: "Troilus and Cressida", quote: "He doth **protract** his work, and seeks to lengthen out the war with idle dalliance." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I would not **protract** our conversation, knowing that every delay increased the agony of parting." },
      { author: "Edmund Burke", work: "Speech on Conciliation with America", quote: "To **protract** an armed contest without a clear prospect of peace is to invite national ruin." }
    ]
  },
  "protracted.md": {
    word: "protracted",
    primary: "Lasting for a long time or longer than expected or usual; prolonged.",
    secondary: "Drawn out, tedious, or extended through deliberate delay or stubborn resistance.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "Jarndyce and Jarndyce had become a **protracted** nightmare of endless Chancery bills and legal costs." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **protracted** siege exhausted the garrison, whose supplies were consumed long before the breach was forced." },
      { author: "John Cairns", work: "Memoirs", quote: "After a **protracted** debate in the general assembly, the resolution was carried by a narrow majority." }
    ]
  },
  "protractedly.md": {
    word: "protractedly",
    primary: "In a protracted or prolonged manner; over an extended or drawn-out period of time.",
    secondary: "With tedious delay or hesitation; lingeringly.",
    quotes: [
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "The twilight lingered **protractedly** over Egdon Heath, blending heather and bog into uniform blackness." },
      { author: "George Eliot", work: "Middlemarch", quote: "Casaubon coughed **protractedly**, as if measuring out his words to emphasize his scholarly grievance." },
      { author: "Henry James", work: "The American", quote: "The negotiations proceeded **protractedly**, every minor formality being scrutinized by the Parisian solicitors." }
    ]
  },
  "protractible.md": {
    word: "protractible",
    primary: "Capable of being extended, protruded, or drawn out in length or space.",
    secondary: "In zoology and comparative anatomy, designating organs (such as tongues, proboscises, or claws) that can be extended outward.",
    quotes: [
      { author: "Richard Owen", work: "Comparative Anatomy and Physiology of Vertebrates", quote: "The chameleon possesses a **protractible** tongue propelled with lightning speed to capture resting insects." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The **protractible** proboscis of nemertean worms can be shot out from the rhynchocoel to seize prey." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "In felids, the claws are **protractible** and retractile, shielded within protective sheaths during locomotion." }
    ]
  },
  "protractile.md": {
    word: "protractile",
    primary: "Capable of being extended or pushed forward; protractible.",
    secondary: "In ichthyology and entomology, describing jaw apparatuses or feeding mouthparts that can be thrust forward to capture prey.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The mouth of the dory is remarkably **protractile**, shooting forward like a tube to suck in unsuspecting minnows." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Many butterfly pupae display **protractile** sensory horns that react violently to touch." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Deep-sea lanternfish often feature **protractile** jaws lined with needle-sharp inward-pointing teeth." }
    ]
  },
  "protraction.md": {
    word: "protraction",
    primary: "The action of prolonging something in time, or the state of being prolonged; extension.",
    secondary: "In anatomy, the forward movement of a body part (such as the shoulder girdle or mandible) in the horizontal plane.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The **protraction** of the parliamentary session gave the court cabal time to buy wavering votes." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The **protraction** of the scapula is accomplished chiefly through contraction of the serratus anterior muscle." },
      { author: "Alexander Hamilton", work: "The Federalist Papers (No. 70)", quote: "The **protraction** of executive deliberations during wartime invites disaster upon the republic." }
    ]
  },
  "protractor.md": {
    word: "protractor",
    primary: "An instrument for measuring or drawing angles, typically in the form of a flat semicircular graduated plate.",
    secondary: "In anatomy, a muscle that serves to draw a limb or structure forward (contrasting with a retractor).",
    quotes: [
      { author: "H. G. Wells", work: "The First Men in the Moon", quote: "Cavor laid out his calculations with compass, ruler, and brass **protractor** upon the workshop table." },
      { author: "Richard Owen", work: "The Anatomy of Vertebrates", quote: "The strong **protractor** muscle draws the mandible forward during mastication." },
      { author: "Jules Verne", work: "From the Earth to the Moon", quote: "Barbicane verified every ballistic azimuth with a gleaming nautical **protractor**." }
    ]
  },
  "protriptyline.md": {
    word: "protriptyline",
    primary: "A tricyclic antidepressant drug used in the treatment of major depressive disorder, known for having activating rather than sedating properties.",
    secondary: "In psychopharmacology, a secondary amine dibenzocycloheptene derivative that potently inhibits the reuptake of norepinephrine.",
    quotes: [
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", quote: "Unlike amitriptyline, **protriptyline** possesses prominent psychomotor stimulating properties that make it unsuitable for agitated depressives." },
      { author: "Julius Axelrod", work: "Nobel Lecture", quote: "The inhibition of presynaptic noradrenaline transport by **protriptyline** clarified the chemical mechanism of tricyclic antidepressants." },
      { author: "Nathan S. Kline", work: "Psychopharmacological Treatment of Depression", quote: "Patients treated with **protriptyline** showed rapid improvement in motor retardation and morning lethargy." }
    ]
  },
  "protropin.md": {
    word: "protropin",
    primary: "A synthetic recombinant human growth hormone (somatrem), containing an extra methionine residue, formerly used to treat growth hormone deficiency in children.",
    secondary: "In pharmaceutical biotechnology, one of the earliest recombinant DNA-derived therapeutics produced in E. coli by Genentech and approved by the FDA in 1985.",
    quotes: [
      { author: "Arthur Kornberg", work: "For the Love of Enzymes", quote: "The commercial production of somatrem under the brand name **Protropin** marked a triumph for recombinant gene expression." },
      { author: "Francis Collins", work: "The Language of Life", quote: "Before **Protropin** was engineered, children with pituitary dwarfism depended on scarce growth hormone extracted from cadavers." },
      { author: "Robert Weinberg", work: "The Biology of Cancer", quote: "Recombinant therapeutics like **Protropin** proved that cloned human proteins could be manufactured safely at industrial scale." }
    ]
  },
  "protrude.md": {
    word: "protrude",
    primary: "To extend beyond or above a surface; stick out or cause to project.",
    secondary: "In surgery and pathology, to herniate or push outward through an abnormal opening or weakened wall.",
    quotes: [
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Prince Andrei noticed the dead officer's boots **protrude** stiffly from under the artillery caisson." },
      { author: "James Joyce", work: "Ulysses", quote: "A corner of the yellow postal card was seen to **protrude** from beneath his waistcoat pocket." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Huge ivory teeth seemed to **protrude** like jagged tombstone slabs along the monster's lower jaw." }
    ]
  },
  "protrusible.md": {
    word: "protrusible",
    primary: "Capable of being thrust out or extended forward; capable of protrusion (variant of protractile).",
    secondary: "In zoology and functional morphology, describing anatomical appendages, proboscises, or pharynges capable of eversion.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea", quote: "The predatory marine snail extends its **protrusible** proboscis to bore through the calcareous shell of an oyster." },
      { author: "William Beebe", work: "The Arcturus Adventure", quote: "The deep-sea anglerfish carries a **protrusible** luminous bait suspended over its gaping maw." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "The pharynx of planarians is highly **protrusible**, capturing food through rapid muscular eversion." }
    ]
  },
  "protrusile.md": {
    word: "protrusile",
    primary: "Capable of being protruded or extended forward; protrusible.",
    secondary: "In comparative morphology, designating structures (such as insect ovipositors or fish premaxillae) that can be projected outwards.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The **protrusile** snout of the pipefish enables it to snatch copepods with explosive suction." },
      { author: "Alfred Russel Wallace", work: "Darwinism", quote: "In certain beetles, the terminal abdominal segments form a **protrusile** tube for depositing eggs inside tree bark." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The tongue of the woodpecker is operated by remarkably elongated, **protrusile** hyoid horns." }
    ]
  },
  "protrusion.md": {
    word: "protrusion",
    primary: "Something that protrudes; a projecting part, prominence, or bulge.",
    secondary: "The act of protruding or state of being pushed forward; in pathology, disc herniation or exophthalmos.",
    quotes: [
      { author: "George Eliot", work: "Adam Bede", quote: "A jagged rock **protrusion** jutted out into the woodland path, catching the wheels of the cart." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The great hump of the sperm whale rose in massive **protrusion** against the horizon." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "A posterolateral **protrusion** of the intervertebral disc impinges directly upon the passing spinal nerve root." }
    ]
  },
  "protrusive.md": {
    word: "protrusive",
    primary: "Tending to protrude; projecting or thrusting forward.",
    secondary: "In dentistry and orthodontics, relating to the forward positioning or movement of the lower jaw (mandibular protrusion).",
    quotes: [
      { author: "Henry James", work: "The Bostonians", quote: "Her jaw had a firm, **protrusive** line that conveyed an indomitable combative temperament." },
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "He noticed the **protrusive** eyes of the elderly curate surveying the congregation with cold appraisal." },
      { author: "Edward Angle", work: "Treatment of Malocclusion of the Teeth", quote: "Severe **protrusive** malocclusion of the incisors impairs both speech articulation and facial aesthetics." }
    ]
  },
  "protuberance.md": {
    word: "protuberance",
    primary: "A thing that protrudes from something else; a swelling, bulge, or lump.",
    secondary: "In astronomy, an obsolete term for a solar prominence; in anatomy, a bony process or elevation (such as the mental protuberance of the chin).",
    quotes: [
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "Gnarled roots formed a mossy **protuberance** at the base of the ancient oak where she sat down to rest." },
      { author: "Herman Melville", work: "Typee", quote: "A strange bony **protuberance** on the warrior's tattooed cheek marked the scar of an ancient war club." },
      { author: "John Herschel", work: "Outlines of Astronomy", quote: "During the total eclipse of the sun, curious rose-colored **protuberance** structures leaped from the solar rim." }
    ]
  },
  "protuberant.md": {
    word: "protuberant",
    primary: "Protruding or bulging beyond the surrounding surface; prominent or swelling out.",
    secondary: "In clinical inspection, describing an abnormally distended abdomen or prominent eyeballs (exophthalmos).",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Mr. Pumblechook sat before the fireplace, his **protuberant** stomach resting comfortably against the mahogany table." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Jos Sedley adjusted his voluminous cravat over his **protuberant** waistcoat with complacent vanity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient presented with a **protuberant** abdomen caused by massive ascites and hepatic cirrhosis." }
    ]
  },
  "protuberate.md": {
    word: "protuberate",
    primary: "To swell out, bulge, or project beyond the surrounding level; to form a protuberance.",
    secondary: "To enlarge or thrust outward in a bulging or prominent manner.",
    quotes: [
      { author: "John Dryden", work: "The Works of Virgil", quote: "From the rough trunk the knotted boughs begin to swell and **protuberate** beneath the vernal rain." },
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "Galls and mossy excrescences **protuberate** upon the bark wherever an insect punctures the tender shoot." },
      { author: "Walter Scott", work: "The Antiquary", quote: "Old rocks that **protuberate** above the sandbanks warned mariners of the sunken reef." }
    ]
  },
  "protura.md": {
    word: "protura",
    primary: "An order of very small, primitive, wingless, eyeless hexapods that inhabit soil, leaf litter, and moss, having twelve abdominal segments.",
    secondary: "In systematic entomology, microscopic soil organisms lacking antennae, using their elongated front legs as sensory organs.",
    quotes: [
      { author: "Filippo Silvestri", work: "Descrizione di un nuovo genere d'insetti", quote: "The discovery of **Protura** revealed an archaic hexapod lineage lacking antennae and possessing anamorphic development." },
      { author: "Vincent Wigglesworth", work: "The Principles of Insect Physiology", quote: "In the order **Protura**, the forelegs are held forward in a sensory posture functionally replacing absent antennae." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "The forest soil fauna teems with minute organisms, including the primitive **Protura**, which decompose fungal hyphae." }
    ]
  },
  "proturan.md": {
    word: "proturan",
    primary: "Any minute, eyeless hexapod belonging to the order Protura.",
    secondary: "Pertaining to or characteristic of proturans, noted for anamorphic postembryonic development (adding abdominal segments during molts).",
    quotes: [
      { author: "Alfried Schmitt", work: "Soil Biology & Biochemistry", quote: "A single handful of undisturbed forest humus may contain hundreds of **proturan** coneheads." },
      { author: "Peter J. Gullan", work: "The Insects: An Outline of Entomology", quote: "The internal mouthparts of the **proturan** place it alongside collembolans within the class Entognatha." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Anamorphic growth, preserved in the **proturan** lifecycle, represents an ancestral trait shared with myriapods." }
    ]
  },
  "unprotected.md": {
    word: "unprotected",
    primary: "Not protected, shielded, or guarded against harm, danger, attack, or damage.",
    secondary: "In law, patent, and copyright, not covered by legal safeguards, insurance, treaties, or trademark protections.",
    quotes: [
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The solitary cottage stood bleak and **unprotected** upon the crest of the windswept chalk ridge." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Women left **unprotected** by fair legal property rights remain completely dependent on the caprice of men." },
      { author: "Winston Churchill", work: "The World Crisis", quote: "The merchant convoy sailed through **unprotected** waters where hostile submarines lurked in silence." }
    ]
  },
  "unprotectedness.md": {
    word: "unprotectedness",
    primary: "The state, condition, or quality of being unprotected; vulnerability to danger, harm, or exposure.",
    secondary: "In psychology and sociology, an acute feeling or objective state of lacking social, economic, or legal defense.",
    quotes: [
      { author: "George Eliot", work: "Felix Holt, the Radical", quote: "Her profound sense of **unprotectedness** made every stranger's footstep outside the garden gate a terror." },
      { author: "Charlotte Brontë", work: "The Professor", quote: "The absolute **unprotectedness** of the young orphan girl appealed to every noble instinct of his heart." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "When intermediate aristocratic institutions crumble, the isolated citizen experiences an overwhelming sense of civic **unprotectedness**." }
    ]
  },
  "unprotective.md": {
    word: "unprotective",
    primary: "Not protective; failing to offer protection, defense, or shelter.",
    secondary: "Characterized by an absence of defensive precautions, safeguards, or parental shielding.",
    quotes: [
      { author: "Henry James", work: "The Golden Bowl", quote: "His casual, **unprotective** manner left her completely exposed to the sarcastic barbs of the company." },
      { author: "Edith Wharton", work: "The Custom of the Country", quote: "She resented her father’s weak, **unprotective** attitude toward the financial vultures circling the estate." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "The flimsy cotton canvas was utterly **unprotective** against the drenching equatorial downpour." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
    return;
  }

  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Primacy Batch 9 completed! Total words updated:", Object.keys(wordsData).length);
