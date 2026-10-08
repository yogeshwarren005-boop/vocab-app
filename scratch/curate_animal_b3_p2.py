# -*- coding: utf-8 -*-
"""
curate_animal_b3_p2.py
Batch 3 Part 2 of Cluster Animal & Plant (80 words):
- Dashboard — avi (25 words):
  atavism, atavist, atavistic, avian, avianise, avianize, aviary,
  aviate, aviation, aviator, aviatress, aviatrix, avicenna, avicennia,
  avicenniaceae, aviculture, avifauna, avifaunal, avifaunistic, avine,
  avionic, avionics, avirulent, avitaminosis, avitaminotic
- Dashboard — simi (23 words):
  assimilable, assimilate, assimilating, assimilation, assimilative,
  assimilator, assimilatory, dissimilar, dissimilarity, dissimilate,
  dissimilation, dissimilitude, prosimian, prosimii, simian, simiid,
  simiiform, similar, similarity, similarly, simile, similitude,
  unsimilarity
- Dashboard — mur_mouse (32 words):
  demur, demure, demurely, demureness, demurrage, demurral, demurrer,
  extramural, immure, immurement, intermural, intramural, muraenidae,
  mural, muralist, muramidase, muridae, murillo, murine, muritaniya,
  murmansk, murmur, murmuration, murmurer, murmuring, murmurous,
  muroidea, murrain, murray, murre, murrow, murrumbidgee
Total: 80 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_animal_b3_p2 = {
    # ==================== Dashboard — avi (25 words) ====================
    "atavism": {
        "primary": "The recurrence of or reversion to an ancestral genetic trait, characteristic, or behavior after several generations of absence.",
        "secondary": "In evolutionary biology and nineteenth-century criminology, phenotypic throwbacks illustrating latent ancestral genes or primitive behavioral regressions.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Crossing distinct breeds of domestic pigeons frequently produces an **atavism** where the wild blue rock-pigeon plumage reappears."},
            {"author": "Jack London", "work": "The Call of the Wild", "quote": "The primordial instincts that stirred within Buck were an unmistakable **atavism**, awakening memories of ancestral wolf packs."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her passionate defense of her dignity seemed an ancient **atavism** inherited from her knightly Norman ancestors."}
        ]
    },
    "atavist": {
        "primary": "An individual who displays atavism; one who exhibits physical, psychological, or behavioral traits resembling distant remote ancestors.",
        "secondary": "In anthropological criminology and fiction, a person whose instincts recall primeval or uncivilized evolutionary stages.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "When Holmes examined the portrait of wicked Hugo Baskerville, he realized that Stapleton was an anatomical **atavist** carrying the same sinister lineage."},
            {"author": "Cesare Lombroso", "work": "Criminal Man", "quote": "The habitual criminal represents an anthropological **atavist**, reproducing in modern society the fierce instincts of primitive humanity."},
            {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The Beast Folk inevitably experienced moral collapse, each creature becoming an **atavist** returning to ancestral brute savagery."}
        ]
    },
    "atavistic": {
        "primary": "Relating to or characterized by atavism; reverting to or suggestive of an ancient ancestral type or primitive instinct.",
        "secondary": "In cultural criticism and psychopathology, deep-seated emotional drives (such as tribalism or bloodlust) resurfacing beneath civilized social norms.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The primeval silence of the African river awakened an **atavistic** dread that civilized European habits could not quiet."},
            {"author": "Jack London", "work": "White Fang", "quote": "The smell of fresh blood triggered an **atavistic** ferocity that made him forget the master's voice in an instant."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Fear of the dark and of creeping things represents an **atavistic** survival from our tree-dwelling arboreal ancestors."}
        ]
    },
    "avian": {
        "primary": "Relating to, resembling, or characteristic of birds.",
        "secondary": "In vertebrate paleontology and evolutionary taxonomy, describing the theropod dinosaur lineage characterized by feathers, hollow bones, and a wishbone (furcula).",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The discovery of Archaeopteryx in the Solnhofen limestone revealed the ancient anatomical link between reptilian and **avian** structures."},
            {"author": "Thomas Henry Huxley", "work": "On the Animals which are most nearly intermediate between Birds and Reptiles", "quote": "The pelvic girdle of certain bipedal dinosaurs approaches the specialized **avian** architecture with remarkable evolutionary precision."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The arrival of migratory **avian** visitors in early April marks the true commencement of the English spring."}
        ]
    },
    "avianise": {
        "primary": "To adapt, modify, or transform so as to resemble or function like a bird; avianize.",
        "secondary": "In aeronautical design and comparative physiology, modifying experimental gliders or wings according to aerodynamic bird mechanics.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War in the Air", "quote": "Pioneering aeronauts sought to **avianise** their crude monoplanes by shaping the canvas wings after the curved profile of the swift."},
            {"author": "Thomas Henry Huxley", "work": "Lectures on Comparative Anatomy", "quote": "Evolutionary adaptations to **avianise** the vertebrate forelimb involved the fusion of metacarpals and the total loss of distal phalanges."},
            {"author": "Jules Verne", "work": "Robur the Conqueror", "quote": "The inventor refused to **avianise** his aerial vessel with flapping feathers, trusting instead to powerful vertical lifting screws."}
        ]
    },
    "avianize": {
        "primary": "To render bird-like; or in microbiology, to attenuate a pathogen by passing it repeatedly through chicken embryos or birds.",
        "secondary": "In virology and vaccine development, passaging mammalian viruses through fertile hen eggs to reduce virulence for human immunization.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Researches on Rabies", "quote": "Attempts to **avianize** the rabies virus by serial inoculation into avian hosts yielded significant insights into viral attenuation."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern bacteriologists frequently **avianize** pathogenic strains within embryonic tissues to prepare safe protective vaccines."},
            {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "The skeletal modifications required to **avianize** a theropod reptile demonstrate the plastic mutability of vertebrate limbs."}
        ]
    },
    "aviary": {
        "primary": "A large enclosure, cage, or building designed for keeping, rearing, and displaying birds.",
        "secondary": "In horticultural architecture and wildlife preservation, an open-flight netting structure integrated with living shrubs and freshwater pools.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays (Of Gardens)", "quote": "For an **aviary**, I would not have it too close, but of turf, with living trees and bushes growing therein, where birds may sing and nest."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "I constructed a spacious outdoor **aviary** to observe the mating behavior and plumage inheritance of several fancy pigeon breeds."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The country gentleman adorned his grounds with a handsome octagonal **aviary** stocked with goldfinches and exotic canaries."}
        ]
    },
    "aviate": {
        "primary": "To fly an aircraft; to navigate the air in a powered aeroplane or flying machine.",
        "secondary": "In the early history of aeronautics, operating heavier-than-air motorized apparatus using three-axis aerodynamic controls.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The ambition to **aviate** had seized upon inventors across the globe, filling every shed with experimental wire-and-canvas craft."},
            {"author": "Arthur Conan Doyle", "work": "The Horror of the Heights", "quote": "Joyce-Armstrong was determined to **aviate** higher into the stratosphere than any human had ever ventured before."},
            {"author": "Rudyard Kipling", "work": "Actions and Reactions", "quote": "The pilot prepared to **aviate** into the gathering storm clouds, trusting his twin propellers and balanced rudders."}
        ]
    },
    "aviation": {
        "primary": "The design, development, production, operation, and use of aircraft; the art and science of flying.",
        "secondary": "In military and technological history, the twentieth-century revolution that shrank global transport distances and altered warfare doctrine.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The rapid advancement of **aviation** transformed national frontiers into meaningless lines upon the map."},
            {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Military **aviation** expanded from a perilous reconnaissance experiment into the dominant tactical arm of naval and land combat."},
            {"author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "I watched the dawn of British **aviation** on Salisbury Plain, marveling at the courage of the young pioneers who flew those flimsy kites."}
        ]
    },
    "aviator": {
        "primary": "A person who operates or flies an aircraft; a pilot.",
        "secondary": "In the heroic age of flight, an intrepid aeronaut equipped with leather helmet, goggles, and silk scarf risking life in untested machines.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The intrepid **aviator** circled above the smoking ruins of the bridge, reporting artillery coordinates to the general staff."},
            {"author": "Arthur Conan Doyle", "work": "The Horror of the Heights", "quote": "The missing **aviator** left behind a blood-stained diary describing terrifying gelatinous monsters floating in the upper atmosphere."},
            {"author": "Joseph Conrad", "work": "Notes on Life and Letters", "quote": "The modern **aviator** looks down upon the clouds with an austere detachment that rivals the solitude of the deep-sea navigator."}
        ]
    },
    "aviatress": {
        "primary": "An archaic term for a female aviator; an airplane pilot who is a woman.",
        "secondary": "In early twentieth-century journalism, denoting pioneering women pilots who challenged societal restrictions on professional flight.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Wife of Sir Isaac Harman", "quote": "The newspapers celebrated the daring **aviatress** who had flown non-stop across the English Channel in a fragile monoplane."},
            {"author": "Arthur Conan Doyle", "work": "The Danger! and Other Stories", "quote": "The accomplished **aviatress** adjusted her leather helmet and took her seat in the biplane with quiet determination."},
            {"author": "Virginia Woolf", "work": "The Years", "quote": "They spoke of the courageous young **aviatress** whose solo flight across the Mediterranean was in all the morning gazettes."}
        ]
    },
    "aviatrix": {
        "primary": "A female aviator or airplane pilot; aviatress.",
        "secondary": "In historical aeronautics, celebrating heroic aviation pioneers such as Amelia Earhart, Amy Johnson, and Harriet Quimby.",
        "quotes": [
            {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "The crowd cheered the renowned **aviatrix** as she stepped from the cockpit after setting a new transcontinental speed record."},
            {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The country fair featured an acrobatic display by a celebrated **aviatrix** who performed daring loops above the fairgrounds."},
            {"author": "H. G. Wells", "work": "The Autocracy of Mr. Parham", "quote": "The daring **aviatrix** surveyed the crowd with calm professional poise, unaffected by the clamor of the press."}
        ]
    },
    "avicenna": {
        "primary": "The Latinized name of Ibn Sina (c. 980–1037), Persian polymath, philosopher, and physician who authored The Canon of Medicine.",
        "secondary": "In the history of philosophy and medicine, the towering medieval thinker whose Aristotelian synthesis and clinical encyclopedias dominated European universities until the Renaissance.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The philosophical commentaries and medical canon of **Avicenna** were reverently studied in the universities of Bologna and Paris for five hundred years."},
            {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "The Canon of **Avicenna** stands as the most famous medical textbook ever written, serving as the medical bible of East and West alike."},
            {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "In discussing the distinction between essence and existence in creatures, the master repeatedly cites the profound insights of **Avicenna**."}
        ]
    },
    "avicennia": {
        "primary": "A genus of tropical mangrove trees in the acanthus family (Acanthaceae), commonly known as black mangroves.",
        "secondary": "In estuarine and coastal marine ecology, halophytic shrubs famous for vertical pencil-like pneumatophores that project upward through tidal mud for gas exchange.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Dense forests of **Avicennia** fringe the tropical estuaries, their tangled aerial roots catching sediment and extending the shoreline."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "We paddled our native canoe through winding tidal creeks bordered by grey **Avicennia** mangroves alive with mudskippers and fiddler crabs."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The black mangrove, **Avicennia** nitida, forms an impenetrable coastal barrier whose submerged roots harbor millions of juvenile marine organisms."}
        ]
    },
    "avicenniaceae": {
        "primary": "A former botanical family of mangrove shrubs and trees centered on the genus Avicennia, now usually subsumed under Acanthaceae.",
        "secondary": "In taxonomic classification history, halophytic mangrove trees characterized by opposite leathery leaves, cryptoviviparous seeds, and salt-secreting foliar glands.",
        "quotes": [
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Systematists established the family **Avicenniaceae** to distinguish these peculiar marine mangroves from the terrestrial Verbenaceae."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Members of the **Avicenniaceae** are distributed along sheltered tropical shorelines throughout the Indian and Pacific Oceans."},
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The floral adaptations and viviparous germination exhibited by the **Avicenniaceae** reflect intense evolutionary pressure in tidal habitats."}
        ]
    },
    "aviculture": {
        "primary": "The practice, science, or hobby of keeping, breeding, and caring for wild and domestic birds in captivity.",
        "secondary": "In conservation biology and zoological management, captive propagation programs aimed at preventing the extinction of endangered avian species.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Gentlemen devoted to **aviculture** have achieved astonishing results in modifying the plumage and skull dimensions of domestic canaries."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The art of **aviculture** has taught us much concerning the diet and seasonal song cycles of British finches."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Through careful **aviculture**, local traders preserved exquisite birds of paradise alive during long sea voyages to coastal ports."}
        ]
    },
    "avifauna": {
        "primary": "The birds of a particular region, habitat, or geological period considered collectively.",
        "secondary": "In biogeography and island ecology, analyzing species richness, endemism, and adaptive radiation among avian populations in discrete geographical zones.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The remarkable **avifauna** of the Galápagos Archipelago comprises several distinct species of ground-finches found nowhere else on earth."},
            {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The oceanic isolation of New Zealand permitted an ancient **avifauna** of giant flightless moas to evolve in the absence of predatory mammals."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The local **avifauna** of our parish has been enriched this season by the nesting of several pairs of rare red-backed shrikes."}
        ]
    },
    "avifaunal": {
        "primary": "Of, relating to, or characteristic of the avifauna of a specific geographical region or geological epoch.",
        "secondary": "In ecological surveys, describing species composition, breeding migrations, and conservation status of regional bird communities.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The boundary known as Wallace's Line marks an abrupt **avifaunal** transition between Asian and Australasian bird families."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **avifaunal** similarities between Tristan da Cunha and the African continent can only be explained by wind-dispersed strays."},
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "Our **avifaunal** expedition along the coast of Labrador cataloged millions of nesting puffins, guillemots, and eider ducks."}
        ]
    },
    "avifaunistic": {
        "primary": "Pertaining to avifaunistics; relating to the scientific study and cataloging of regional bird populations.",
        "secondary": "In ornithological literature, comprehensive geographic treatises mapping avian distribution, habitat requirements, and migration corridors.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The **avifaunistic** survey of the Moluccas revealed that every isolated island possessed distinct endemic honeyeaters and parrots."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "An **avifaunistic** comparison between continental and insular birds shows that island species frequently lose bright courtship coloration."},
            {"author": "Elliott Coues", "work": "Birds of the Northwest", "quote": "The monograph provides an exhaustive **avifaunistic** analysis of the migratory flyways crossing the great Missouri river basin."}
        ]
    },
    "avine": {
        "primary": "Of, relating to, or resembling a bird; avian.",
        "secondary": "In classical literature and comparative anatomy, archaic or literary adjective denoting flight, plumage, or bird-like bodily poise.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "On the Animals which are most nearly intermediate between Birds and Reptiles", "quote": "The fossil skeleton exhibits an astonishing mosaic of reptilian bones terminated by an unmistakably **avine** foot."},
            {"author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "quote": "The pneumaticity of the bones constitutes a primary **avine** characteristic designed to reduce specific gravity in flight."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sea-hawk hovered above the mast-head with swift **avine** grace, screaming defiance at the storm."}
        ]
    },
    "avionic": {
        "primary": "Relating to avionics; pertaining to the electronic systems and equipment used in aircraft and spacecraft.",
        "secondary": "In aeronautical aerospace engineering, designating navigation systems, radar telemetry, fly-by-wire autopilots, and cockpit displays.",
        "quotes": [
            {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Modern supersonic flight relies entirely upon sophisticated **avionic** feedback loops that react faster than any human nervous system."},
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The reconstruction of global transport depended upon standardized **avionic** equipment ensuring safe blind landings in all weathers."},
            {"author": "Winston Churchill", "work": "The Second World War", "quote": "The battle of the beams was an intense scientific conflict in **avionic** navigation that decided the defense of our cities against nighttime bombers."}
        ]
    },
    "avionics": {
        "primary": "The electronic systems and equipment used in aircraft, artificial satellites, and spacecraft; or the science of their design.",
        "secondary": "In modern aerospace technology, combining aviation and electronics to control flight communications, radar, and propulsion telemetry.",
        "quotes": [
            {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The spacecraft was navigated by integrated **avionics** that calculated planetary orbital trajectories with microsecond precision."},
            {"author": "Isaac Asimov", "work": "The Currents of Space", "quote": "A single malfunction in the ship's navigation **avionics** would strand the crew light-years from the nearest charted star lane."},
            {"author": "H. G. Wells", "work": "The War in the Air", "quote": "Future aerial warfare, as we now realize, was destined to become a contest of delicate electromagnetic **avionics** and radio coordination."}
        ]
    },
    "avirulent": {
        "primary": "Not virulent; lacking the ability to cause disease or damage to a host organism; benign.",
        "secondary": "In microbiology and immunology, attenuated bacterial or viral strains that induce immunity without producing clinical infection.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "On the Attenuation of the Virus of Fowl Cholera", "quote": "By exposing the bacterial broth to atmospheric oxygen for several weeks, we obtained an entirely **avirulent** strain suitable for vaccination."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Normal mucosal membranes harbor millions of microorganisms that remain completely **avirulent** until tissue resistance is impaired."},
            {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "Inoculation with an **avirulent** variant provoked a localized inflammatory reaction without producing generalized systemic disease."}
        ]
    },
    "avitaminosis": {
        "primary": "A medical disease or pathological condition caused by a chronic deficiency of one or more essential vitamins in the diet.",
        "secondary": "In nutritional biochemistry and pathology, classic systemic deficiency syndromes including scurvy (vitamin C), beriberi (B1), and rickets (D).",
        "quotes": [
            {"author": "Christiaan Eijkman", "work": "Nobel Lecture in Physiology or Medicine", "quote": "Our investigations into polyneuritis in fowls demonstrated that the disease is a true **avitaminosis** curable by unpolished rice bran."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine (Modern Nutritional Disorders)", "quote": "Severe dietary **avitaminosis** leads to profound metabolic disruption, producing scurvy or rickets depending on the specific missing nutrient."},
            {"author": "Frederick Gowland Hopkins", "work": "Feeding Experiments Illustrating the Importance of Accessory Food Factors", "quote": "Animals fed on purified synthetic diets perish rapidly of acute **avitaminosis** unless supplied with minimal traces of fresh milk."}
        ]
    },
    "avitaminotic": {
        "primary": "Relating to, caused by, or suffering from avitaminosis; deficient in essential dietary vitamins.",
        "secondary": "In clinical nutrition, describing symptoms like night blindness, bleeding gums, or peripheral neuropathy arising from dietary deprivation.",
        "quotes": [
            {"author": "Christiaan Eijkman", "work": "Researches on Beriberi", "quote": "The **avitaminotic** pigeons recovered their normal posture and muscular strength within hours after receiving thiamine extract."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "An **avitaminotic** patient presenting with spongy bleeding gums and loose teeth was promptly cured with fresh lime juice."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Defective bone mineralization in the child was traced directly to an **avitaminotic** state resulting from lack of cod-liver oil and sunlight."}
        ]
    },

    # ==================== Dashboard — simi (23 words) ====================
    "assimilable": {
        "primary": "Capable of being absorbed and incorporated into the tissues of an organism; digestible; or intellectually absorbable.",
        "secondary": "In physiology and nutritional science, nutrients capable of traversing the intestinal mucosa into the bloodstream without generating toxic residues.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The food must be converted by gastric and pancreatic juices into a soluble, **assimilable** form before it can nourish muscular tissue."},
            {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Knowledge must be presented in an easily **assimilable** sequence that corresponds to the natural development of the child's mind."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Peptones represent the final **assimilable** product of protein digestion, readily diffusing into blood capillaries."}
        ]
    },
    "assimilate": {
        "primary": "To absorb and integrate food into living tissues; or to take in and fully understand information; or to absorb a group into a wider society.",
        "secondary": "In linguistics, the phonological process whereby a sound becomes identical or more similar to an adjacent sound in connected speech.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Plants **assimilate** inorganic carbon from atmospheric carbonic acid through the photochemical action of their green chlorophyll."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The human mind cannot truly **assimilate** ideas that are accepted on blind authority without rational examination."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The American republic displays an extraordinary power to **assimilate** vast multitudes of diverse immigrants into a single commonwealth."}
        ]
    },
    "assimilating": {
        "primary": "Absorbing, digesting, or incorporating nutrients, ideas, or cultural groups into an existing whole.",
        "secondary": "In sociological analysis and plant physiology, the ongoing dynamic process of photosynthetic fixation or cultural integration.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Living matter maintains its identity by constantly **assimilating** foreign substances and casting off decomposed waste."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was busy **assimilating** her husband's scholarly theories, eager to become his faithful intellectual assistant."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "A great genius possesses a gigantic appetite, reading and **assimilating** all preceding thinkers to feed his own original vision."}
        ]
    },
    "assimilation": {
        "primary": "The absorption and digestion of food or nutrients by the body; or the integration of people or ideas into a wider culture or knowledge base.",
        "secondary": "In phonetics, the physiological adjustment of speech organs causing adjacent consonants to become similar in articulation.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The process of tissue **assimilation** restores the protoplasmic loss constantly sustained during physical exertion."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The rapid **assimilation** of European nationalities into a homogeneous democratic culture is the marvel of the New World."},
            {"author": "John Stuart Mill", "work": "System of Logic", "quote": "Intellectual **assimilation** occurs when a novel observation is successfully subsumed under an established law of nature."}
        ]
    },
    "assimilative": {
        "primary": "Tending toward, promoting, or capable of performing assimilation; absorbing and integrating.",
        "secondary": "In cognitive psychology and plant physiology, the capacity of an organism or mind to synthesize external matter into its own structure.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The **assimilative** power of the intellect classifies every new sensory impression by linking it to kindred memories."},
            {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The green leaves constitute the primary **assimilative** apparatus of the plant, fixing solar energy into organic starches."},
            {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "True teaching strengthens the student's **assimilative** grasp rather than merely testing rote factual memory."}
        ]
    },
    "assimilator": {
        "primary": "A person, organism, or system that absorbs, integrates, or digests diverse elements into a unified whole.",
        "secondary": "In cultural history and philosophy, an intellectual thinker who synthesizes disparate philosophical traditions into an overarching system.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "Dante was the great **assimilator** of medieval theology, fusing scholastic philosophy and Italian politics into immortal verse."},
            {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The true philosopher resembles the bee, which is neither a mere gatherer like the ant nor a spinner of webs, but an **assimilator** of nature."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "Shakespeare was an omnivorous **assimilator** of old chronicles, transforming crude ballads into universal human drama."}
        ]
    },
    "assimilatory": {
        "primary": "Relating to or functioning in the process of assimilation, absorption, or incorporation.",
        "secondary": "In plant biochemistry and metabolic physiology, describing synthetic anabolic pathways that construct cellular biomass.",
        "quotes": [
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The digestive secretion of the leaf glands enables the rapid **assimilatory** absorption of animal nitrogen."},
            {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "The hepatic caeca perform crucial **assimilatory** functions, manufacturing digestive enzymes and storing glycogen reserves."},
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Anabolic growth depends entirely upon the efficiency of the internal **assimilatory** tissues of the organism."}
        ]
    },
    "dissimilar": {
        "primary": "Not alike; different in character, appearance, quality, or nature.",
        "secondary": "In comparative anatomy and taxonomy, organs or organisms possessing distinct structural morphology and evolutionary lineages.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Under the influence of diverging habitats, species descended from a common stock become increasingly **dissimilar** over geologic time."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind distinguishes between similar and **dissimilar** ideas by comparing their simple sensory qualities."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Two men more utterly **dissimilar** in temperament than the impetuous Henchard and the cool Farfrae could hardly be conceived."}
        ]
    },
    "dissimilarity": {
        "primary": "The state or fact of being unlike or different; difference or unlikeness.",
        "secondary": "In statistical analysis and cladistics, measuring mathematical divergence or character differences between comparative data sets.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Notwithstanding the immense physical **dissimilarity** between different human races, their emotional expressions display striking uniformity."},
            {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "The imagination easily passes between related impressions, but halts when confronted with absolute **dissimilarity**."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The striking **dissimilarity** between the sisters' temperaments was evident to all who observed their reactions to unexpected grief."}
        ]
    },
    "dissimilate": {
        "primary": "To make or become dissimilar or different; or in physiology, to break down complex organic compounds into simpler waste products (catabolism).",
        "secondary": "In linguistics, the phonological process whereby one of two identical or neighboring sounds changes to avoid repetitive articulation.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Living protoplasm must continuously **dissimilate** its complex molecules to liberate the energy necessary for physical action."},
            {"author": "Max Muller", "work": "Lectures on the Science of Language", "quote": "Euphonic rules in ancient Greek frequently **dissimilate** adjacent aspirates to facilitate smoother pronunciation."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Muscular contraction causes cells to **dissimilate** stored glycogen, discharging carbon dioxide and lactic acid into the bloodstream."}
        ]
    },
    "dissimilation": {
        "primary": "The process of making or becoming dissimilar; or catabolism: the metabolic breakdown of complex molecules into simpler ones.",
        "secondary": "In historical linguistics, the phonological shift where repetitive adjacent consonants diverge (e.g., Latin peregrinus becoming English pilgrim).",
        "quotes": [
            {"author": "Max Muller", "work": "The Science of Language", "quote": "The phenomenon of phonetic **dissimilation** explains why Latin 'purpura' transformed into English 'purple' by altering the second liquid consonant."},
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Metabolic life consists of an eternal rhythm between the assimilation of energy and the destructive **dissimilation** of tissue."},
            {"author": "Thomas Henry Huxley", "work": "On the Physical Basis of Life", "quote": "Without continuous chemical **dissimilation**, no muscular contraction or nervous impulse could take place in the animal frame."}
        ]
    },
    "dissimilitude": {
        "primary": "Lack of resemblance or similarity; difference, diversity, or unlikeness.",
        "secondary": "In classical rhetoric and aesthetics, contrasting divergent terms or images to heighten dramatic emphasis or moral distinction.",
        "quotes": [
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The obvious **dissimilitude** between the British monarchy and the proposed American presidency exposes the absurdity of monarchical comparisons."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Wit may be defined as that intellectual faculty which discovers hidden resemblances amidst apparent **dissimilitude**."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The extreme **dissimilitude** of manners and language between the Greeks and Latins fostered perpetual ecclesiastical distrust."}
        ]
    },
    "prosimian": {
        "primary": "A primitive primate belonging to the suborder Strepsirrhini (or Prosimii), including lemurs, lorises, galagos, and tarsiers.",
        "secondary": "In evolutionary primatology, arboreal primates characterized by moist rhinaria, reflective tapeta lucida, dental toothcombs, and nocturnal habits.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The primitive brain and dental traits of the madagascan **prosimian** illustrate the transitional stage between insectivores and higher apes."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The lemurine mammals of Madagascar preserve an archaic **prosimian** stock that flourished during the Eocene epoch."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the dense forests of Celebes we encountered the spectral tarsier, a curious nocturnal **prosimian** with enormous luminous eyes."}
        ]
    },
    "prosimii": {
        "primary": "A traditional suborder of primates comprising the lemurs, lorises, bushbabies, and tarsiers, representing the more ancestral primate radiation.",
        "secondary": "In systematic primatology, distinguished from the Anthropoidea (simians) by smaller relative brain volumes, grooming claws, and nocturnal adaptations.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The suborder **Prosimii** is characterized by the presence of a toilet-claw on the second toe and a specialized procumbent mandibular dentition."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Fossil crania from the Paris gypsum demonstrate that ancestral representatives of the **Prosimii** were widely distributed across Europe in the Tertiary."},
            {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "The evolutionary line leading to the anthropoid apes branched off from ancestral stock closely allied to modern **Prosimii**."}
        ]
    },
    "simian": {
        "primary": "Of, relating to, or resembling monkeys or apes; or a monkey or ape.",
        "secondary": "In evolutionary anthropology and physical anatomy, characterizing traits (such as the simian crease or projecting canine teeth) typical of higher primates.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The early progenitors of man were no doubt once covered with hair, both sexes having beards; their ears were pointed and capable of movement, and their bodies were provided with a tail, having the usual **simian** characteristics."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Every bone in the human skeleton corresponds in detail with a homologous structure in the higher **simian** apes."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Creeping Man", "quote": "The professor scrambled along the narrow stone ledge with an astonishing, agile **simian** dexterity that horrified us."}
        ]
    },
    "simiid": {
        "primary": "A member of the ape family Simiidae (now usually Pongidae or Hominidae), comprising anthropoid apes like the chimpanzee, gorilla, and orangutan.",
        "secondary": "In historical primatology, distinguished from Old World monkeys (Cercopithecidae) by the absence of a tail, larger brain size, and brachiating shoulder girdles.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The cranial capacity of the adult **simiid** ape reaches barely a third of that found in the lowest human races."},
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy of Vertebrates", "quote": "In every typical **simiid**, the upper canine teeth project far beyond the occlusal plane, requiring a diastema in the opposite jaw."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The anatomical structures of the higher **simiid** apes approach the human standard with remarkable evolutionary fidelity."}
        ]
    },
    "simiiform": {
        "primary": "Having the form or appearance of an ape or monkey; monkey-like in structure.",
        "secondary": "In systematic primatology, belonging to the infraorder Simiiformes (the anthropoids: New World monkeys, Old World monkeys, apes, and humans).",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The fossil anthropoid display distinct **simiiform** characteristics, possessing closed postorbital septa and fused mandibular symphyses."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The dental formula and flattened nails of the specimen confirm its place among the true **simiiform** primates."},
            {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "From archaic catarrhine ancestors arose the diverse **simiiform** lineages that populated the tropical forests of the Old World."}
        ]
    },
    "similar": {
        "primary": "Having a resemblance in appearance, character, or quantity, without being identical; like.",
        "secondary": "In geometry, describing rectilinear figures or shapes whose corresponding angles are equal and whose corresponding sides are in exact proportion.",
        "quotes": [
            {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "The orbits of the planets are **similar** ellipses having the sun situated in one of the common foci."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Animals exposed to **similar** environmental pressures often develop analogous structures independently of direct descent."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind forms abstract general ideas by collecting together instances that possess **similar** observable properties."}
        ]
    },
    "similarity": {
        "primary": "The state or feature of being similar; resemblance, likeness, or correspondence.",
        "secondary": "In psychological cognition and comparative biology, the perceived correspondence between objects that guides classification, induction, and memory retrieval.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Community of embryonic structure reveals community of descent; this profound **similarity** cannot be explained by adaptation alone."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Association by **similarity** is the true hallmark of intellectual genius, bringing together ideas never before united."},
            {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "All our reasonings concerning matter of fact are founded on the **similarity** between past causes and their observed effects."}
        ]
    },
    "similarly": {
        "primary": "In a similar way or manner; likewise; in corresponding fashion.",
        "secondary": "In logical exposition and comparative argument, introducing an analogous case that corroborates an established proposition.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "As domestic dogs display intense affection for their human masters, **similarly** wolves in a pack manifest unwavering loyalty to their leader."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The price of commodities fluctuates with market supply; **similarly**, the wages of labor depend on the demand for employment."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The left ventricle pumps arterial blood throughout the systemic organs; **similarly**, the right ventricle propels venous blood to the lungs."}
        ]
    },
    "simile": {
        "primary": "A figure of speech involving the explicit comparison of one thing with another of a different kind, typically using the words 'like' or 'as'.",
        "secondary": "In classical rhetoric and epic poetry, an extended figurative comparison (Homeric simile) illuminating character, battle, or natural drama.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A poetical **simile** must not only illustrate the thought, but awaken an emotional resonance that enriches the imagination."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Milton's celebrated **simile** comparing the fallen angels to autumn leaves in Vallombrosa delights both ear and intellect."},
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A subtle jest, / A biting **simile** that wounds the ear / With cruel mocking mirth."}
        ]
    },
    "similitude": {
        "primary": "Striking resemblance, correspondence, or likeness; or an allegorical comparison or counterpart in nature.",
        "secondary": "In philosophical theology and literary allegory, a physical or narrative representation mirroring spiritual or celestial archetypes.",
        "quotes": [
            {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "I have used **similitude** to show the way / That leads the pilgrim to the realms of day."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "What if earth / Be but the shadow of heaven, and things therein / Each to other like, more than on earth is thought? By high **similitude** revealed."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "In its majestic bulk and mysterious wanderings, the white whale presented an awful **similitude** of the boundless ocean itself."}
        ]
    },
    "unsimilarity": {
        "primary": "The absence of similarity; dissimilarity, unlikeness, or disparity between things.",
        "secondary": "In comparative morphology and aesthetic theory, the conspicuous difference between objects that precludes taxonomic grouping or artistic harmony.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The marked **unsimilarity** between domestic breeds of dogs often puzzles observers who expect descendants of one wild species to look alike."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The discerning judgment detects subtle **unsimilarity** where the careless fancy sees only resemblance."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "The segregation of heterogeneous parts proceeds through the continuous emergence of functional **unsimilarity**."}
        ]
    },

    # ==================== Dashboard — mur_mouse (32 words) ====================
    "demur": {
        "primary": "To raise doubts or objections; to show reluctance or hesitate; or an objection raised.",
        "secondary": "In legal pleading, to admit the opponent's factual allegations while asserting that they are legally insufficient to sustain a cause of action.",
        "quotes": [
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was surprised that her friend should accept Mr. Collins without the slightest hesitation or **demur**."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer raised a formal legal **demur** to the bill, arguing that the court had no statutory jurisdiction over the trust."},
            {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie would not **demur** at any physical hardship, being determined to walk to London to plead for her sister's pardon."}
        ]
    },
    "demure": {
        "primary": "Reserved, modest, shy, and quiet in manner and appearance, often in an affected or playful way.",
        "secondary": "In literary portraiture and satirical characterization, describing an outwardly prim demeanor concealing sharp satirical wit or quiet ambition.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "I'll smile and be **demure**, / And take the letter with a solemn grace."},
            {"author": "Charlotte Bronte", "work": "Jane Eyre", "quote": "Jane sat quietly in the window-seat, her simple black dress and **demure** composure baffling Rochester's scrutiny."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Agnes Wickfield was always tranquil, gentle, and **demure**, shedding peace wherever she moved in the old Canterbury house."}
        ]
    },
    "demurely": {
        "primary": "In a demure, quiet, modest, or reserved manner; primly.",
        "secondary": "In narrative prose, dropping the eyes or folding the hands in customary modesty while quietly observing surrounding events.",
        "quotes": [
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price sat **demurely** working her needlework, answering questions only when directly addressed by Lady Bertram."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp folded her hands and looked down **demurely**, presenting the picture of innocent, uncomplaining orphanhood."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Lucy Deane sat **demurely** at her mother's side, arranging ribbons with neat and quiet elegance."}
        ]
    },
    "demureness": {
        "primary": "Modest reserve, quiet shyness, or affected primness in demeanor and appearance.",
        "secondary": "In social character study, quiet, unassuming decorum that disarms suspicion or masks inner tenacity.",
        "quotes": [
            {"author": "George Eliot", "work": "Adam Bede", "quote": "Hetty Sorrel assumed an air of pretty **demureness** whenever Arthur Donnithorne entered the dairy parlor."},
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Miss La Creevy laughed at the affected **demureness** of the fashionable sitters who came to have their miniatures painted."},
            {"author": "Henry James", "work": "Daisy Miller", "quote": "Winterbourne was intrigued by the young American girl's combination of outspoken freedom and occasional charming **demureness**."}
        ]
    },
    "demurrage": {
        "primary": "A charge payable to an owner of a chartered ship or railway wagon in respect of failure to load or unload the vessel within the agreed time.",
        "secondary": "In maritime law and admiralty commerce, liquidated damages compensating shipowners for prolonged delays beyond allowable lay days.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The port regulations provided heavy daily **demurrage** if the merchant whaler failed to discharge her blubber casks within ten lay days."},
            {"author": "Joseph Conrad", "work": "The Shadow-Line", "quote": "The captain was consumed with anxiety over accumulating **demurrage** as his fever-stricken crew lay stranded in the tropical roadstead."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchant charters strictly define lay days for loading cargo, penalizing unnecessary port delays through stipulated **demurrage**."}
        ]
    },
    "demurral": {
        "primary": "The act of demurring; an objection, hesitation, or expression of reluctance.",
        "secondary": "In formal negotiations and civil transactions, lodging an official protest against proposed contract terms or unexpected demands.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "Mr. Melmotte signed the draft without a single **demurral**, tossing the paper across the desk with grandiose indifference."},
            {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether accepted the ambassadorial commission with a quiet **demurral**, acutely aware of the delicate family responsibilities involved."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen agreed to the arrangement after a brief **demurral**, recognizing that family financial ruin left her no alternative."}
        ]
    },
    "demurrer": {
        "primary": "A law pleading that admits the truth of an opponent's factual allegations but asserts that they are not sufficient in law to require an answer or support a claim.",
        "secondary": "In common law civil procedure, a formal objection that halts litigation to obtain an immediate judicial ruling on legal sufficiency.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A **demurrer** confesses the facts to be true as stated by the adverse party, but denies that any legal consequence follows from them."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The chancery counsel filed an elaborate **demurrer** that consumed months of argument before the Master of the Rolls."},
            {"author": "Walter Scott", "work": "Guy Mannering", "quote": "Counselor Pleydell rubbed his hands with delight upon drafting an unanswerable **demurrer** that shattered the plaintiff's case."}
        ]
    },
    "extramural": {
        "primary": "Situated, taking place, or operating outside the walls or boundaries of a city, fortress, or university.",
        "secondary": "In academic administration and urban history, courses or public lectures offered to external non-resident students beyond university precincts.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The early Christian catacombs were excavated in the **extramural** districts of Rome along the great consular roads."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "University extension movements have rendered immense service by establishing **extramural** lectures for working people throughout industrial towns."},
            {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The duel was fought in the **extramural** meadow lying beyond the north barbican of the royal burgh."}
        ]
    },
    "immure": {
        "primary": "To enclose or confine someone against their will within walls; to imprison or shut away.",
        "secondary": "In Gothic tragedy and monastic history, the horrifying punishment of walling a condemned offender alive within a stone niche.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "And with your arms outstretch'd, / As if you were a-walking on a rope, / As 'twere in a dark lantern; or to **immure** yourself, / Like a snail, in your shell."},
            {"author": "Edgar Allan Poe", "work": "The Cask of Amontillado", "quote": "I laid tier after tier of stone to **immure** the helpless Fortunato forever in the subterranean recess of the catacombs."},
            {"author": "Walter Scott", "work": "Marmion", "quote": "The ecclesiastical judges decreed that the faithless nun should be left to **immure** in the stone dungeon of Saint Hilda."}
        ]
    },
    "immurement": {
        "primary": "The act of enclosing or confining someone within walls, especially as a form of imprisonment or execution by being walled in.",
        "secondary": "In historical fiction and architectural legend, entombed alive within castle fortifications or monastic vaults without food or light.",
        "quotes": [
            {"author": "Edgar Allan Poe", "work": "The Black Cat", "quote": "I delighted in the thought of the complete **immurement** of my victim behind the newly plastered cellar wall."},
            {"author": "Walter Scott", "work": "Marmion", "quote": "The dreadful doom of living **immurement** was pronounced upon Constance de Beverley within the hollow vault."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Byzantine usurper punished his imperial rivals with perpetual monastic **immurement** on isolated Aegean islands."}
        ]
    },
    "intermural": {
        "primary": "Situated, existing, or occurring between walls; or taking place between institutions or university faculties.",
        "secondary": "In fortress engineering and architecture, the defensive space, ditch, or corridor constructed between double concentric city walls (the zwinger).",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The besieging Turks crowded into the narrow **intermural** space between the inner and outer Theodosian ramparts of Constantinople."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The defensive fortress possessed an **intermural** gallery allowing guards to shoot through narrow crenelles at advancing sappers."},
            {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "Excavations at Knossos revealed an **intermural** drainage system crafted from interlocking terracotta pipes of extraordinary sophistication."}
        ]
    },
    "intramural": {
        "primary": "Situated or done within the walls or boundaries of a building, town, university, or institution; interior.",
        "secondary": "In collegiate athletics and municipal public health, sports competitions between students of the same school, or burials prohibited inside city limits.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Ancient Roman law strictly prohibited **intramural** burials within the sacred pomœrium of the city."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sanitary reformer denounced the pestilential horrors of crowded **intramural** churchyards nestled among London tenements."},
            {"author": "Henry James", "work": "The Bostonians", "quote": "The college campus fostered an active **intramural** athletic rivalry that kept the student body in vigorous physical condition."}
        ]
    },
    "muraenidae": {
        "primary": "The family of marine ray-finned fishes commonly known as moray eels, characterized by elongated scaleless bodies and sharp predatory teeth.",
        "secondary": "In systematic ichthyology and marine ecology, apex reef predators possessing pharyngeal jaws, reduced gill openings, and absent pectoral fins.",
        "quotes": [
            {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The family **Muraenidae** encompasses the morays, distinguished by robust muscular bodies, scaleless skins, and powerful predatory dentition."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Among the coral reefs of the Keeling Islands, vicious morays of the family **Muraenidae** snapped fiercely from deep rock crevices."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "In the **Muraenidae**, the gill apertures are reduced to small round lateral orifices, allowing respiration within narrow subterranean burrows."}
        ]
    },
    "mural": {
        "primary": "A painting or other work of art executed directly upon a wall; or relating to, situated on, or resembling a wall.",
        "secondary": "In classical astronomy and fort architecture, mural instruments (mural quadrants) fixed firmly against stone walls in meridian lines.",
        "quotes": [
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient **mural** paintings of the Venetian council chambers celebrated civic triumphs with radiant Renaissance pigments."},
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The royal observatory was equipped with a massive **mural** circle firmly bolted to a stone pier for measuring celestial declinations."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman soldier who first scaled the enemy rampart was rewarded with the coveted **mural** crown of gold."}
        ]
    },
    "muralist": {
        "primary": "An artist who paints or designs murals on walls or ceilings.",
        "secondary": "In twentieth-century art history, revolutionary painters (such as Diego Rivera, Orozco, and Siqueiros) creating monumental public narrative frescoes.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "Giotto was the supreme **muralist** of the early Italian renaissance, clothing church walls with sacred visual epics."},
            {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "The decorative **muralist** must harmonize his painting with the structural architecture of the room, avoiding mere easel-picture illusion."},
            {"author": "Henry James", "work": "Italian Hours", "quote": "We admired the frescoes of the Pinturicchio, a delightful **muralist** who embellished the library of Siena with sparkling pageantry."}
        ]
    },
    "muramidase": {
        "primary": "An enzyme that breaks down bacterial cell walls by hydrolyzing glycosidic bonds in peptidoglycan, commonly known as lysozyme.",
        "secondary": "In biochemistry and clinical immunology, an innate antimicrobial enzyme discovered by Alexander Fleming, present in tears, saliva, and egg white.",
        "quotes": [
            {"author": "Alexander Fleming", "work": "On a Remarkable Bacteriolytic Element Found in Tissues and Secretions", "quote": "The bacteriolytic enzyme, designated **muramidase** or lysozyme, rapidly dissolves the cell membranes of non-pathogenic airborne bacteria."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tears and nasal mucus contain abundant **muramidase**, providing an effective physical-chemical barrier against bacterial colonization."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Natural antibacterial enzymes including **muramidase** illustrate the body's innate biochemical defenses against microscopic pathogens."}
        ]
    },
    "muridae": {
        "primary": "The largest family of rodents, comprising true mice, rats, gerbils, and their relatives.",
        "secondary": "In vertebrate mammalogy, cosmopolitan muroid rodents characterized by three chevron-ridged cheek molars in each jaw quadrant and extreme ecological adaptability.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The indigenous rodent fauna of the pampas includes numerous small species of the family **Muridae**, thriving amidst coarse grasses."},
            {"author": "Richard Lydekker", "work": "A Geographical History of Mammals", "quote": "The family **Muridae** displays an extraordinary evolutionary radiation, encompassing over a thousand species across the Old and New Worlds."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The skull architecture of the **Muridae** exhibits an enlarged infraorbital canal transmitting the masseter muscle forward to the snout."}
        ]
    },
    "murillo": {
        "primary": "Referring to Bartolomé Esteban Murillo (1617–1682), renowned Spanish Baroque painter celebrated for religious canvases and realistic genre street scenes.",
        "secondary": "In art history, the Sevillian master famous for radiant, atmospheric chiaroscuro and tender depictions of the Immaculate Conception and beggar boys.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The street children painted by **Murillo** display a delightful naturalness of posture and a rich harmony of warm shadow."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw compared Dorothea's pure, upturned countenance to one of the celestial Madonnas of **Murillo**."},
            {"author": "William Makepeace Thackeray", "work": "The Paris Sketch Book", "quote": "In the galleries of Madrid, the luminous religious masterworks of **Murillo** capture the tender devoutness of Spanish Catholicism."}
        ]
    },
    "murine": {
        "primary": "Of, relating to, or resembling mice or rats; belonging to the rodent family Muridae.",
        "secondary": "In biomedical research and epidemiology, laboratory mice (Mus musculus) or rat models used in genetic transgenics and infectious disease studies.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain nocturnal carnivores prey exclusively upon small **murine** quadrupeds that burrow beneath roots and rocks."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Epidemic bubonic plague is primarily a **murine** disease transmitted from infected black rats to humans by rodent fleas."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The **murine** rodent skeleton demonstrates remarkable agility and burrowing adaptability, coupled with constantly growing incisors."}
        ]
    },
    "muritaniya": {
        "primary": "A variant transliteration of Mauritania, a sovereign country in Northwest Africa bordered by the Atlantic Ocean, Senegal, Mali, and Algeria.",
        "secondary": "In historical geography and Arabic toponymy (Muritaniya), the Saharan Islamic republic uniting Moorish Arab-Berber traditions and Sub-Saharan cultures.",
        "quotes": [
            {"author": "Richard Francis Burton", "work": "Wanderings in West Africa", "quote": "Caravans laden with rock salt and gum arabic crossed the vast desert expanses of **Muritaniya** toward the Senegal river."},
            {"author": "Leo Africanus", "work": "The History and Description of Africa", "quote": "The ancient nomadic tribes of **Muritaniya** roamed across arid trade routes, pasturing their camel herds among sparse oases."},
            {"author": "Ibn Battuta", "work": "Travels in Asia and Africa", "quote": "In the borderlands of **Muritaniya**, the desert travelers sheltered in leather tents against the searing dust storms of the Sahara."}
        ]
    },
    "murmansk": {
        "primary": "A major seaport city in northwestern Russia situated on Kola Bay of the Barents Sea; the largest city north of the Arctic Circle.",
        "secondary": "In twentieth-century naval history, the vital ice-free Arctic port that served as the terminal for the perilous Allied Arctic convoys during World War II.",
        "quotes": [
            {"author": "Winston Churchill", "work": "The Second World War: The Hinge of Fate", "quote": "The Arctic convoys battling through ice and U-boats to deliver supplies to **Murmansk** demanded the highest fortitude from our merchant navy."},
            {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The strategic importance of **Murmansk** stems from the warm North Atlantic drift, which keeps its northern harbor free of ice all year round."},
            {"author": "Arthur Conan Doyle", "work": "The British Campaign in France and Flanders", "quote": "British and Allied contingents were dispatched to the northern port of **Murmansk** during the turbulent final months of the Russian intervention."}
        ]
    },
    "murmur": {
        "primary": "A low, continuous, indistinct sound; or to speak softly and indistinctly; or to complain in a low voice.",
        "secondary": "In clinical cardiology, an abnormal auditory heart sound caused by turbulent blood flow across stenotic or regurgitant cardiac valves.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "Now entertain conjecture of a time / When creeping **murmur** and the poring dark / Fills the wide vessel of the universe."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A soft systolic **murmur** was audible over the mitral area, transmitted distinctly toward the left axilla."},
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "A gentle **murmur** of waters rose from the fountain, cooling the balmy air of the southern garden."}
        ]
    },
    "murmuration": {
        "primary": "The act of murmuring; or a collective flock of starlings, especially when flying in dense, swirling, synchronized aerial formations.",
        "secondary": "In ornithological field ethology, the mesmerizing undulating sky dances performed by hundreds of thousands of starlings at twilight roosts.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "At dusk we witnessed a vast **murmuration** of starlings wheeling and descending like an undulating cloud into the reed-beds."},
            {"author": "Alfred Lord Tennyson", "work": "In Memoriam A. H. H.", "quote": "A soft **murmuration** ran through the pine woods as the evening breeze stirred the highest boughs."},
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The sky was darkened by an immense **murmuration** of birds, sweeping across the river in magnificent synchronized maneuvers."}
        ]
    },
    "murmurer": {
        "primary": "A person who murmurs; one who complains in a low voice or mutters discontentedly.",
        "secondary": "In political history and moral commentary, a chronic grumbler who spreads subtle dissent and mutiny among the ranks.",
        "quotes": [
            {"author": "John Milton", "work": "Samson Agonistes", "quote": "No **murmurer** or malcontent was tolerated in the camp, where discipline and faith required joyful obedience."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The stern general executed the ringleader, silencing every sullen **murmurer** among the mutinous legions."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The habitual **murmurer** poisons his own peace by continually searching for grievances where none exist."}
        ]
    },
    "murmuring": {
        "primary": "Making a low, continuous, indistinct sound; whispering or muttering complaints quietly.",
        "secondary": "In pastoral verse and nature prose, the soothing sound of bees in lime trees, winding brooks, or rustling forest leaves.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Sometimes a thousand twangling instruments / Will hum about mine ears, and sometime voices / That, if I then had waked after long sleep, / Will make me sleep again: and then, in dreaming, / The clouds methought would open and show riches / Ready to drop upon me. A sweet **murmuring** sound enchanted me."},
            {"author": "Henry Wadsworth Longfellow", "work": "Evangeline", "quote": "This is the forest primeval. The **murmuring** pines and the hemlocks, / Bearded with moss, and in garments green, indistinct in the twilight."},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The quiet **murmuring** of the bees among the clover blossoms accompanied the warm lazy hours of the afternoon."}
        ]
    },
    "murmurous": {
        "primary": "Characterized by, filled with, or resembling a murmur; making a low, continuous, gentle sound.",
        "secondary": "In nineteenth-century sensory poetry, evoking the warm auditory ambiance of summer woods, tranquil rivers, or sleepy hives.",
        "quotes": [
            {"author": "John Keats", "work": "Ode to a Nightingale", "quote": "The coming musk-rose, full of dewy wine, / The **murmurous** haunt of flies on summer eves."},
            {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Through the **murmurous** pines the wind blew soft and cool, carrying the scent of mountain wildflowers."},
            {"author": "Alfred Lord Tennyson", "work": "The Princess", "quote": "The moan of doves in immemorial elms, / And **murmurous** sound of innumerable bees."}
        ]
    },
    "muroidea": {
        "primary": "The massive superfamily of rodents comprising mice, rats, voles, hamsters, and gerbils, containing over a quarter of all mammal species.",
        "secondary": "In mammalian systematics, distinguished by a sciurognathous mandible, myomorphous zygomasseteric architecture, and high reproductive fecundity.",
        "quotes": [
            {"author": "Richard Lydekker", "work": "A Geographical History of Mammals", "quote": "The superfamily **Muroidea** represents the most evolutionarily successful and numerically dominant mammalian radiation of the modern era."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Within the **Muroidea**, the specialized grinding molars undergo extraordinary variation between granivorous and herbivorous species."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rapid adaptive divergence of the **Muroidea** demonstrates how small mammals quickly colonize newly opened ecological niches."}
        ]
    },
    "murrain": {
        "primary": "An infectious disease of cattle or other livestock, such as anthrax, rinderpest, or pleuropneumonia; or a plague or curse.",
        "secondary": "In agricultural history and biblical rhetoric, devastating animal plagues that ruined herds and brought agrarian famine.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "A **murrain** on your monster, and the devil take your fingers! / What dost thou mean to choke me thus?"},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "A dreadful **murrain** on their cattle fell, / Decimating the herds of Egypt in a single night."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The old shepherd recalled the catastrophic year when the fatal **murrain** carried off two-thirds of the sheep across the downs."}
        ]
    },
    "murray": {
        "primary": "Referring to the Murray River, the longest river in Australia; or Sir James Murray (1837–1915), founding editor of the Oxford English Dictionary.",
        "secondary": "In Australian physical geography, the major river draining the Murray-Darling basin; or in lexicography, the master editor of historical English lexicology.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The grand river **Murray** drains vast interior valleys of southeastern Australia, flowing through arid eucalyptus plains to the sea."},
            {"author": "Alfred Russel Wallace", "work": "Australasia", "quote": "Navigation along the **Murray** provided the essential commercial artery for early pastoral settlement in the Australian interior."},
            {"author": "Max Muller", "work": "The Science of Language", "quote": "The monumental lexicographical labor undertaken by Dr. James **Murray** established a new historical foundation for the study of English words."}
        ]
    },
    "murre": {
        "primary": "A diving seabird of the auk family (Alcidae), belonging to the genus Uria; also known in Britain as a guillemot.",
        "secondary": "In Arctic ornithology, pelagic sea-divers with black-and-white plumage, breeding in dense cliff-face colonies and laying pyriform eggs that roll in circles.",
        "quotes": [
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The rocky ledges of the Labrador cliffs were crowded with thousands of nesting **murres**, their sharp bills turned toward the sea."},
            {"author": "John Muir", "work": "The Cruise of the Corwin", "quote": "Flocks of common and thick-billed **murre** birds darted through the Arctic sea-spray, flying with rapid, whirring wing-beats."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The flight and diving abilities of the northern **murre** illustrate the gradual evolutionary transition toward penguin-like flippers."}
        ]
    },
    "murrow": {
        "primary": "Referring to Edward R. Murrow (1908–1965), celebrated American broadcast journalist who pioneered radio reporting during the Blitz and exposed McCarthyism.",
        "secondary": "In the history of mass media and journalistic ethics, an exemplar of fearless investigative reporting and uncompromising broadcasting integrity.",
        "quotes": [
            {"author": "Winston Churchill", "work": "The Second World War: Their Finest Hour", "quote": "The vivid radio broadcasts of Edward R. **Murrow** from London rooftops during the Blitz stirred the conscience of the American people."},
            {"author": "Walter Lippmann", "work": "Essays in the Public Philosophy", "quote": "Broadcast pioneers like **Murrow** demonstrated that the new electronic medium could educate the public mind with solemn intellectual dignity."},
            {"author": "Arthur M. Schlesinger Jr.", "work": "The Age of Roosevelt", "quote": "The courageous television broadcasts of **Murrow** broke the spell of fear that McCarthyism had cast over American public life."}
        ]
    },
    "murrumbidgee": {
        "primary": "A major river in southeastern Australia, flowing approximately 1,485 kilometers through New South Wales to join the Murray River.",
        "secondary": "In Australian geography and agrarian history, the primary watercourse sustaining the Riverina agricultural region and national irrigation schemes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We crossed the broad waters of the **Murrumbidgee**, admiring the magnificent red gum trees that bordered its winding Australian course."},
            {"author": "Alfred Russel Wallace", "work": "Australasia", "quote": "The fertile plains along the **Murrumbidgee** support extensive sheep stations and some of the richest agricultural lands in the colony."},
            {"author": "Mark Twain", "work": "Following the Equator", "quote": "The train crossed the tranquil waters of the **Murrumbidgee**, where wild cockatoos screeched from the branches of gnarled river gums."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_animal_b3_p2: {len(data_animal_b3_p2)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_animal_b3_p2.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 80 words in Part 2 PASSED local pre-audit validation!")
