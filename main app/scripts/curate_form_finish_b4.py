import json
import os
import subprocess

data = {
  "Dashboard \u2014 mycet\\endomycetales.md": {
    "primary": "An order of primitive ascomycetous fungi that multiply predominantly by budding and do not produce complex ascomata; true yeasts.",
    "secondary": "In fungal taxonomy and biotechnology, the Endomycetales (often classified as Saccharomycetales) include industrial fermenters like Saccharomyces cerevisiae.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The simple asci formed by members of the **Endomycetales** arise directly from single cells without preceding perithecial development."},
      {"author": "Bryce Kendrick", "work": "The Fifth Kingdom", "quote": "Yeasts grouped under **Endomycetales** have adapted their morphology to carbohydrate-rich liquid environments by reducing mycelial growth."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "Ascospore conjugation in the **Endomycetales** demonstrates an elemental form of sexual reproduction in higher fungi."}
    ]
  },
  "Dashboard \u2014 mycet\\eumycetes.md": {
    "primary": "The true fungi; a major taxonomic division or kingdom of non-photosynthetic eukaryotic organisms possessing chitinous cell walls and absorptive nutrition.",
    "secondary": "In systematic biology, the Eumycetes historically separated true mycelial fungi (Ascomycota, Basidiomycota, Zygomycota) from slime molds and fungal-like oomycetes.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The **Eumycetes** are characterized by a true vegetative mycelium whose cell walls contain fungal cellulose or chitin."},
      {"author": "Ernst Haeckel", "work": "Systematische Phylogenie", "quote": "Phylogenetic trees place the **Eumycetes** as an independent kingdom diverging early from ancestral protozoan flagellates."},
      {"author": "C. V. Subramanian", "work": "Hyphomycetes", "quote": "The remarkable morphological radiation of the **Eumycetes** reflects millions of years of adaptation to terrestrial organic decay."}
    ]
  },
  "Dashboard \u2014 mycet\\mycet.md": {
    "primary": "A Greek root and combining element derived from mykes, signifying fungus, mushroom, or fungal biological relationships.",
    "secondary": "In biological nomenclature and medicine, serves as a root in terms designating fungal structures, diseases (mycetoma), or fungal taxonomic groups.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek stem **mycet** derives from mykes, originally denoting a mushroom or fungal growth."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Linguistic evidence traces **mycet** back to ancient substrate terms describing spongy, moist forest organisms."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "Modern mycological taxonomy continually utilizes the root **mycet** to classify novel fungal divisions and reproductive structures."}
    ]
  },
  "Dashboard \u2014 mycet\\mycetophilidae.md": {
    "primary": "A family of small, slender dipteran nematoceran flies commonly known as fungus gnats, whose larvae feed upon fungal sporocarps or decaying vegetation.",
    "secondary": "In forest entomology and dipterology, Mycetophilidae are vital primary consumers of macrofungi, facilitating spore dispersal while developing in mushroom caps.",
    "quotes": [
      {"author": "J. O. Westwood", "work": "An Introduction to the Modern Classification of Insects", "quote": "The fragile, long-legged flies of the family **Mycetophilidae** congregate in damp woods where mushrooms flourish in autumn."},
      {"author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "Larvae of the **Mycetophilidae** spin delicate silken tubes across the gills of agarics, feeding upon the fleshy fungal tissue."},
      {"author": "Willi Hennig", "work": "Die Larvenformen der Dipteren", "quote": "Cephalic morphology in larval **Mycetophilidae** reveals specialized chewing mouthparts adapted for consuming tough fungal hyphae."}
    ]
  },
  "Dashboard \u2014 mycet\\mycologist.md": {
    "primary": "A biological scientist who specializes in the study, taxonomy, physiology, genetics, and ecology of fungi.",
    "secondary": "In agricultural and medical science, a mycologist investigates fungal plant pathogens, industrial fermentation processes, or clinical mycoses.",
    "quotes": [
      {"author": "Miles Joseph Berkeley", "work": "Outlines of British Fungology", "quote": "The aspiring **mycologist** must combine patient microscopic examination with meticulous observations of field habitats."},
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "By cultivating pure cultures on nutrient media, the modern **mycologist** unravels the enigmatic polymorphic life cycles of rusts."},
      {"author": "Pier Andrea Saccardo", "work": "Sylloge Fungorum", "quote": "A tireless **mycologist** cataloged tens of thousands of spore specimens to construct our foundational taxonomic system."}
    ]
  },
  "Dashboard \u2014 mycet\\mycology.md": {
    "primary": "The branch of biological science that studies fungi, including their genetic properties, taxonomy, biochemical traits, and ecological relationships.",
    "secondary": "In applied science, mycology encompasses both industrial applications (fermentation, pharmaceuticals) and medical disciplines treating pathogenic fungal infections.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The rise of experimental **mycology** transformed our understanding of parasitism and cellular symbiosis in plant disease."},
      {"author": "Pier Andrea Saccardo", "work": "Sylloge Fungorum", "quote": "Descriptive **mycology** requires standardized measurements of spore dimensions and precise descriptions of ascocarp anatomy."},
      {"author": "Bryce Kendrick", "work": "The Fifth Kingdom", "quote": "Modern molecular **mycology** has rewritten the fungal tree of life, demonstrating that fungi are more closely related to animals than to plants."}
    ]
  },
  "Dashboard \u2014 mycet\\Mycoplasma.md": {
    "primary": "A taxonomic genus of minute bacteria that naturally lack a rigid peptidoglycan cell wall, allowing them to assume pleomorphic shapes.",
    "secondary": "In medical microbiology and cell culture, Mycoplasma species (such as M. pneumoniae) are notorious contaminants and pathogens inherently resistant to beta-lactam antibiotics.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Certain filter-passing organisms, later classed as **Mycoplasma**, challenged the classic bacteriological doctrines of rigid cellular envelopes."},
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "The extreme delicacy of **Mycoplasma** colonies requires specialized serum-enriched agar plates for diagnostic isolation."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "With its tiny genome, **Mycoplasma** genitalium has become a premier model organism for synthetic biology and minimal cell design."}
    ]
  },
  "Dashboard \u2014 mycet\\zygomycete.md": {
    "primary": "Any fungus of the former phylum Zygomycota, characterized by sexual reproduction through the formation of thick-walled resting zygospores.",
    "secondary": "In food science and industrial biotechnology, zygomycetes (such as Rhizopus and Mucor) act as fast-growing sugar molds and essential agents in tempeh fermentation.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The conjugation of two copulating progametangia in a **zygomycete** yields a heavily pigmented and warted zygospore."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "The coenocytic hyphae of a typical **zygomycete** lack regular cross-walls, permitting rapid cytoplasmic streaming throughout the mycelium."},
      {"author": "Albert Francis Blakeslee", "work": "Sexual Reproduction in the Mucorineae", "quote": "Our experiments with a **zygomycete** mold revealed heterothallism, proving that sexual zygospore formation requires complementary mating strains."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmec.md": {
    "primary": "A Greek root and combining form derived from myrmex, signifying ant or relating to ants.",
    "secondary": "In zoology and ecological nomenclature, forms combining terms denoting ant-eating habits (myrmecophagy), ant dispersal of seeds (myrmecochory), or ant mimicry.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The ancient Greek noun myrmex forms the scientific base **myrmec**, denoting the ant in both myth and nature."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Indo-European cognates of **myrmec** exhibit diverse metathesized forms, all pointing to small social burrowing insects."},
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "Systematic biologists combine **myrmec** with diverse descriptive suffixes to name complex symbioses between ants and tropical plants."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecia.md": {
    "primary": "A taxonomic genus of large, aggressive ants native to Australia, commonly known as bull ants or bulldog ants, equipped with powerful stinging venom and large mandibles.",
    "secondary": "In myrmecology and evolutionary entomology, Myrmecia represents one of the most basal living ant lineages, displaying solitary foraging and primitive social behaviors.",
    "quotes": [
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The giant Australian bull ant **Myrmecia** retains primitive wasp-like traits, hunting by keen vision rather than chemical trails."},
      {"author": "E. O. Wilson", "work": "The Insect Societies", "quote": "Colonies of **Myrmecia** exhibit simple social structures with small worker populations and independent foraging strategies."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Naturalists in the southern continent quickly learn to respect the venomous sting and formidable jaws of **Myrmecia**."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecobius.md": {
    "primary": "A taxonomic genus of small marsupials endemic to Western Australia containing the numbat (*Myrmecobius fasciatus*), which feeds exclusively on termites.",
    "secondary": "In marsupial mammalogy, Myrmecobius is characterized by an extraordinarily long vermiform tongue, degenerate cheek teeth, and diurnal solitary foraging.",
    "quotes": [
      {"author": "George Robert Waterhouse", "work": "A Natural History of the Mammalia", "quote": "The genus **Myrmecobius** presents fifty-two teeth, an anomalously high dental formula among living terrestrial marsupials."},
      {"author": "John Gould", "work": "The Mammals of Australia", "quote": "With its transverse white dorsal bands and bushy tail, **Myrmecobius** runs with swift agility through hollow eucalyptus logs."},
      {"author": "Ronald Strahan", "work": "The Mammals of Australia", "quote": "Unlike most nocturnal marsupials, **Myrmecobius** searches for subsurface termite galleries during bright daylight hours."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecochory.md": {
    "primary": "The dispersal of plant seeds by ants, typically facilitated by specialized lipid- and protein-rich seed appendages called elaiosomes.",
    "secondary": "In plant ecology and mutualism biology, myrmecochory benefits plants by transporting seeds away from parent competition and burying them in nutrient-rich subterranean nests.",
    "quotes": [
      {"author": "F. E. Clements", "work": "Plant Succession", "quote": "Spring ephemerals in temperate deciduous forests rely heavily on **myrmecochory** to scatter their heavy seeds across the forest floor."},
      {"author": "E. O. Wilson", "work": "The Insect Societies", "quote": "In classical **myrmecochory**, the foraging ant consumes only the lipid-rich elaiosome, leaving the intact seed buried safely in underground refuse chambers."},
      {"author": "Daniel Janzen", "work": "Coevolution of Animals and Plants", "quote": "Seeds adapted for **myrmecochory** display smooth hard seed coats that resist mandibles while presenting irresistible nutritional rewards."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecoid.md": {
    "primary": "Resembling an ant in physical morphology, color patterning, posture, or movement; ant-like.",
    "secondary": "In evolutionary biology and entomology, myrmecoid mimicry (Batesian or Wasmannian) protects spiders, beetles, and hemipterans from visual predators that avoid stinging ants.",
    "quotes": [
      {"author": "Edward Bagnall Poulton", "work": "The Colours of Animals", "quote": "Certain salticid spiders develop a constricted abdomen and wave their anterior legs in the air, creating a striking **myrmecoid** illusion."},
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The selective pressure exerted by insectivorous birds has driven hundreds of tropical arthropods into exquisite **myrmecoid** camouflage."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism: An Exposition of the Theory of Natural Selection", "quote": "A harmless staphylinid beetle acquires immense protection by assuming a **myrmecoid** form within aggressive army ant columns."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecology.md": {
    "primary": "The scientific discipline that studies ants, encompassing their taxonomy, physiology, ecology, behavior, and social organization.",
    "secondary": "In evolutionary biology, myrmecology has provided pioneering insights into kin selection, chemical communication via pheromones, and superorganism theory.",
    "quotes": [
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The founding texts of modern **myrmecology** revealed that the ant colony functions as an integrated organic unit."},
      {"author": "E. O. Wilson", "work": "The Insect Societies", "quote": "Through field **myrmecology**, we discovered how glandular pheromone trails orchestrate complex division of labor among millions of nestmates."},
      {"author": "Auguste Forel", "work": "The Social World of the Ants", "quote": "Half a century of dedicated **myrmecology** convinced me that instinctive altruism reaches its supreme expression in the anthill."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophaga.md": {
    "primary": "A taxonomic genus of xenarthran mammals comprising the giant anteater (*Myrmecophaga tridactyla*), native to Central and South America.",
    "secondary": "In mammalogy and evolutionary anatomy, Myrmecophaga is characterized by an elongated tubular skull, complete absence of teeth, and a sticky two-foot tongue used to raid termite mounds.",
    "quotes": [
      {"author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "We describe the great toothless anteater under the genus **Myrmecophaga**, noting its extended snout and powerful clawed forefeet."},
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The salivary glands of **Myrmecophaga** secrete copious viscous mucus that covers the tongue during rapid extraction of insects."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The giant anteater **Myrmecophaga** wanders solitary over the South American savannas, ripping open termite mounds with immense claws."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophagidae.md": {
    "primary": "A mammalian family of xenarthrans comprising the true anteaters, including the giant anteater and the tamanduas.",
    "secondary": "In vertebrate paleontology and evolutionary morphology, Myrmecophagidae species are specialized for myrmecophagy through edentulous jaws, reduced zygomatic arches, and hyper-developed salivary glands.",
    "quotes": [
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The cranial architecture of the **Myrmecophagidae** shows extreme osseous remodeling correlated with an exclusively soft insectivorous diet."},
      {"author": "George Gaylord Simpson", "work": "The Principles of Classification and a Classification of Mammals", "quote": "Within the suborder Vermilingua, the **Myrmecophagidae** encompass both terrestrial giants and arboreal prehensile-tailed tamanduas."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The complete loss of functional dentition unites the living **Myrmecophagidae** in common evolutionary descent."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophagous.md": {
    "primary": "Feeding primarily or exclusively upon ants, termites, or related social insects; anteater-like in diet.",
    "secondary": "In mammalian ecology, myrmecophagous species (such as pangolins, anteaters, and aardvarks) exhibit convergent evolution with clawed digging forelimbs and vermiform tongues.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Animals belonging to distinct orders have acquired **myrmecophagous** adaptations, developing tubular jaws to prey upon social insects."},
      {"author": "Richard Owen", "work": "Odontography", "quote": "The **myrmecophagous** habit leads inevitably to tooth reduction, as demonstrated by pangolins and true anteaters."},
      {"author": "E. O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "A specialized **myrmecophagous** predator must tolerate painful chemical defenses and stings to exploit concentrated colonial biomass."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophile.md": {
    "primary": "An organism (such as an insect, mite, or spider) that lives in habitual symbiotic, commensal, or parasitic association with an ant colony.",
    "secondary": "In evolutionary entomology, a myrmecophile often produces specialized appeasement secretions from trichome glands to suppress worker aggression inside the nest.",
    "quotes": [
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The paussid beetle is an esteemed **myrmecophile**, pampered by host workers who greedily lick the golden secretions from its antennae."},
      {"author": "Auguste Forel", "work": "The Social World of the Ants", "quote": "Every flourishing anthill shelters a diverse community of guests, each **myrmecophile** exploiting nest warmth and food stores."},
      {"author": "E. O. Wilson", "work": "The Insect Societies", "quote": "Chemical mimicry allows an obligate **myrmecophile** to acquire the cuticular hydrocarbon signature of its host colony."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophilous.md": {
    "primary": "Living in, benefiting from, or exhibiting a mutualistic, commensal, or dependent relationship with ants.",
    "secondary": "In botanical ecology, myrmecophilous plants provide nesting hollows and nectar rewards in exchange for ant defense against herbivores.",
    "quotes": [
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The **myrmecophilous** lycaenid caterpillars pacify protective ant escorts by secreting drops of nutritious honey from dorsal glands."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Extrafloral nectaries attract swarms of **myrmecophilous** guards that drive destructive caterpillars from tender young shoots."},
      {"author": "Daniel Janzen", "work": "Coevolution of Mutualism Between Ants and Acacias", "quote": "In Central America, the **myrmecophilous** swollen-thorn acacias maintain resident ant colonies throughout all seasons."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophobia.md": {
    "primary": "An irrational, abnormal, and intense fear of ants, often accompanied by panic symptoms and compulsive avoidance.",
    "secondary": "In clinical psychology and psychiatric taxonomy, myrmecophobia is classified as a specific animal-type phobia that can produce severe anxiety even upon viewing images of ants.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "Analysis of a Phobia in a Five-Year-Old Boy", "quote": "Specific animal dreads, such as acute **myrmecophobia**, reflect repressed unconscious anxieties displaced onto teeming creatures."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A patient suffering from **myrmecophobia** reported that the mere sight of an ant on the garden path triggered trembling and dizziness."},
      {"author": "Pierre Janet", "work": "The Major Symptoms of Hysteria", "quote": "Phobic terrors of insects, whether arachnophobia or **myrmecophobia**, involve emotional overvaluation of harmless stimuli."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophyte.md": {
    "primary": "A plant that lives in an obligate or facultative mutualistic relationship with an ant colony, possessing specialized structures for housing and nourishing the ants.",
    "secondary": "In tropical ecology, a myrmecophyte provides domatia (hollow stems, thorns, or leaf pouches) and food bodies in exchange for defense against folivores and encroaching vines.",
    "quotes": [
      {"author": "Thomas Belt", "work": "The Naturalist in Nicaragua", "quote": "The bull's-horn acacia is a true **myrmecophyte**, offering hollow spines for nests and Beltian bodies on its leaflet tips as ant food."},
      {"author": "Daniel Janzen", "work": "Coevolution of Mutualism Between Ants and Acacias", "quote": "When ants were experimentally excluded from a **myrmecophyte**, the tree was rapidly defoliated and smothered by competing vegetation."},
      {"author": "E. O. Wilson", "work": "The Diversity of Life", "quote": "The tropical rainforest contains astonishing examples of the **myrmecophyte**, where plants cultivate fierce insect armies for protection."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmecophytic.md": {
    "primary": "Pertaining to, exhibiting, or characteristic of a myrmecophyte or a symbiotic ant-plant relationship.",
    "secondary": "In evolutionary botany, myrmecophytic traits include modified hollow petioles, extrafloral nectaries, and specialized nutrient-absorptive internal tissues.",
    "quotes": [
      {"author": "Thomas Belt", "work": "The Naturalist in Nicaragua", "quote": "The Cecropia tree displays **myrmecophytic** adaptations, producing sweet glycogen glands at the base of each leaf stalk."},
      {"author": "Daniel Janzen", "work": "Coevolution of Mutualism Between Ants and Acacias", "quote": "Obligate **myrmecophytic** species cannot survive in nature without the active clearing behavior of their resident ant colonies."},
      {"author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "In Southeast Asia, **myrmecophytic** ferns form bulbous hollow rhizomes that provide dry nesting galleries for arboreal ants."}
    ]
  },
  "Dashboard \u2014 myrmec\\Myrmidons.md": {
    "primary": "In Greek mythology and Homeric epic, a fierce Thessalian warrior tribe led by Achilles in the Trojan War, legendarily created from ants by Zeus.",
    "secondary": "In classical literature and common usage, applied figuratively to loyal, unquestioning, and ruthlessly obedient followers or subordinates who execute harsh orders.",
    "quotes": [
      {"author": "Homer", "work": "The Iliad", "quote": "Achilles went through the camp calling all his **Myrmidons** to arms, and they poured forth like ravening wolves."},
      {"author": "Ovid", "work": "Metamorphoses", "quote": "Zeus heard the prayer of King Aeacus and transformed the swarming ants upon the sacred oak into the warrior **Myrmidons**."},
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Strike, fellow **Myrmidons**, and close him round! So, Ilion, fall thou next! Now, Troy, sink down; here lies thy heart, thy sinews, and thy bone."}
    ]
  },
  "Dashboard \u2014 myrmec\\myrmomancy.md": {
    "primary": "An ancient form of divination or fortune-telling through the observation of the behavior, movements, or nesting habits of ants.",
    "secondary": "In classical folklore and anthropology, myrmomancy interpreted the sudden swarming of ants or their storage of grain as omens predicting severe winter storms, crop yields, or famines.",
    "quotes": [
      {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "Practitioners of **myrmomancy** watched the directional marching of ants across thresholds to foretell impending tribal wars or droughts."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Greek oracles occasionally practiced **myrmomancy**, seeking divine portents in the subterranean labors of ant mounds."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancient augurs relied upon **myrmomancy**, holding that ants carrying corn in haste presaged famine or sudden tempest."}
    ]
  },
  "Dashboard \u2014 mys\\mys.md": {
    "primary": "A Greek combining root derived from mys, meaning mouse or muscle, or alternatively related to pollution, defilement, or filth (mysos).",
    "secondary": "In systematic zoology and medical terminology, serves as a stem in names of rodents (Neomys, Notomys) and psychological conditions involving dread of dirt (mysophobia).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The root **mys** in classical Greek denotes both the mouse and the muscular tissue, mirroring the Latin mus."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Separate Greek roots share the form **mys**, one denoting a small rodent and another signifying ritual pollution or abominable filth."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Anatomists often utilize the Greek **mys** when classifying small rodent genera and their specialized masticatory musculature."}
    ]
  },
  "Dashboard \u2014 mys\\mysophilia.md": {
    "primary": "A psychological condition or paraphilia characterized by sexual attraction to or erotic arousal derived from dirt, filth, soiled clothing, or unwashed bodies.",
    "secondary": "In psychopathology and clinical sexology, mysophilia involves intense erotic preoccupation with soiled undergarments, mud, or personal excretions.",
    "quotes": [
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "Cases of **mysophilia** demonstrate how sensory associations with filth can become perversely linked to sexual gratification."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The fetishist afflicted with **mysophilia** finds alluring beauty in garments stained by sweat and street dust."},
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "Erotic fixations such as **mysophilia** represent unintegrated archaic components of infantile coprophilic curiosity."}
    ]
  },
  "Dashboard \u2014 mys\\mysophobia.md": {
    "primary": "An abnormal, irrational, and debilitating fear of germs, dirt, contamination, or defilement.",
    "secondary": "In clinical psychiatry, mysophobia is a hallmark symptom of obsessive-compulsive disorder (OCD), manifesting in compulsive handwashing and excessive disinfection rituals.",
    "quotes": [
      {"author": "William A. Hammond", "work": "Neurological Contributions", "quote": "I introduced the term **mysophobia** to describe an uncontrollable dread of contamination that compels patients to wash their hands hundreds of times daily."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In extreme **mysophobia**, touching a common doorknob induces overwhelming terror of invisible infectious grime."},
      {"author": "Emil Kraepelin", "work": "Psychiatry: A Text-Book for Students and Physicians", "quote": "The obsessive doubts in **mysophobia** trap the patient in agonizing cleaning rituals that consume every waking hour."}
    ]
  },
  "Dashboard \u2014 mys\\mysophobic.md": {
    "primary": "Afflicted with, characterized by, or pertaining to mysophobia; obsessively terrified of dirt, germs, or contamination.",
    "secondary": "In behavioral psychology, describing avoidance behaviors, barrier protocols, and compulsive cleaning routines exhibited by individuals with contamination obsessions.",
    "quotes": [
      {"author": "William A. Hammond", "work": "A Treatise on Insanity in Its Medical Relations", "quote": "The **mysophobic** subject avoided touching paper money or shaking hands, fearing lethal contamination from every stranger."},
      {"author": "Pierre Janet", "work": "Les Obsessions et la Psychasthénie", "quote": "Patients with **mysophobic** anxieties will scrub their skin with abrasive brushes until ulcerated wounds appear."},
      {"author": "Sigmund Freud", "work": "Notes Upon a Case of Obsessional Neurosis", "quote": "The Rat Man exhibited **mysophobic** defenses, attempting to ward off guilt by performing elaborate purifying washings."}
    ]
  },
  "Dashboard \u2014 mys\\neomys.md": {
    "primary": "A taxonomic genus of semi-aquatic Old World shrews in the family Soricidae, commonly known as Eurasian water shrews.",
    "secondary": "In mammalogy and ecological physiology, Neomys species (such as N. fodiens) possess stiff fringe hairs on their feet for swimming and slightly venomous saliva used to paralyze small fish and frogs.",
    "quotes": [
      {"author": "Johann Jakob Kaup", "work": "Das Thierreich in seinen Hauptformen", "quote": "We erect the genus **Neomys** for the water shrew, whose swimming habits are aided by stiff hairs fringing the paws."},
      {"author": "Thomas Bell", "work": "A History of British Quadrupeds", "quote": "The agile water shrew, **Neomys** fodiens, dives into clear chalk streams to hunt freshwater crustacea and minnows."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The submandibular salivary glands of **Neomys** secrete a paralyzing neurotoxin that subdues large aquatic prey."}
    ]
  },
  "Dashboard \u2014 ne\\anne.md": {
    "primary": "A variant root or combining form historically associated with spinning, thread-making, or weaving structures (derived from Greek nēma or nēein).",
    "secondary": "In classical philology and textile terminology, relates to terms designating spun filaments, thread skeins, or woven web foundations.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The verbal root meaning to spin or weave gave rise to various dialectal and poetic derivatives including **anne**."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Comparative linguists trace early Mediterranean terms for spun flax through morphological variants such as **anne**."},
      {"author": "John Ruskin", "work": "The Ethics of the Dust", "quote": "The ancient art of spinning thread and winding the **anne** skein symbolized feminine patience in traditional domestic arts."}
    ]
  },
  "Dashboard \u2014 ne\\axoneme.md": {
    "primary": "The central microtubular core and motility engine of a eukaryotic cilium or flagellum, classically exhibiting a conserved 9+2 arrangement of microtubule doublets.",
    "secondary": "In cell biology and biophysics, the sliding of adjacent doublet microtubules powered by dynein motor arms generates the rhythmic bending waves of the axoneme.",
    "quotes": [
      {"author": "Keith R. Porter", "work": "Fine Structure of Cells and Tissues", "quote": "Electron microscopy of ciliary cross-sections revealed the remarkable geometric regularity of the **axoneme** with its nine peripheral doublets."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "ATP-dependent dynein walking against adjacent microtubules causes the flexible **axoneme** to bend in rhythmic wave-like beats."},
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "The evolutionary origin of the eukaryotic **axoneme** remains one of the central puzzles in cellular morphogenesis."}
    ]
  },
  "Dashboard \u2014 ne\\diplonema.md": {
    "primary": "The diplotene stage of prophase I in meiosis, during which homologous chromosomes begin to desynapse and separate, remaining visibly joined at chiasmata.",
    "secondary": "In cytogenetics, diplonema is characterized by gene transcription in lampbrush chromosomes and prolonged developmental arrest in mammalian oocytes.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "At **diplonema**, the paired bivalents pull apart along their longitudinal axis except at points of genetic exchange called chiasmata."},
      {"author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "Chiasma terminalization during **diplonema** prepares the homologous chromosome pairs for orderly metaphase alignment."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Microscopic analysis at **diplonema** allows direct counting of crossover events across individual chromosome arms."}
    ]
  },
  "Dashboard \u2014 ne\\leptonema.md": {
    "primary": "The leptotene stage of prophase I in meiosis, during which chromatin condenses into fine, elongated, visible threadlike filaments within the nucleus.",
    "secondary": "In meiosis genetics, leptonema initiates meiotic chromosome remodeling as programmed double-strand breaks form along the chromosomes to guide pairing.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The meiotic prophase opens with **leptonema**, where chromosomes first become visible as delicate, unpolarized nuclear threads."},
      {"author": "Walther Flemming", "work": "Zellsubstanz, Kern und Zelltheilung", "quote": "During **leptonema**, dense chromatin beads called chromomeres appear like pearls upon a slender thread."},
      {"author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "The bouquet arrangement formed at the close of **leptonema** facilitates homologous recognition between chromosome telomeres."}
    ]
  },
  "Dashboard \u2014 ne\\ne.md": {
    "primary": "A combining root derived from Greek nema, meaning thread, filament, or spun fiber, or alternatively from neos, signifying new or recent.",
    "secondary": "In biological taxonomy and philology, ne- functions as a prefix in names of threadlike structures (nematodes, axoneme) or modern evolutionary epochs (Neolithic).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The root **ne** represents both the concept of spinning thread and the adjective for youth or newness."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "From the ancient Indo-European verbal stem for spinning comes the ubiquitous combining form **ne** in Greek anatomy."},
      {"author": "Benjamin Hall Kennedy", "work": "The Revised Latin Primer", "quote": "Students of classical compounding recognize **ne** in Greek borrowings describing fine filaments and novel forms."}
    ]
  },
  "Dashboard \u2014 ne\\Neolithic.md": {
    "primary": "Pertaining to or denoting the later part of the Stone Age, characterized by polished stone implements, agricultural cultivation, animal domestication, and pottery.",
    "secondary": "In archaeology and anthropology, the Neolithic Revolution marks the transformative transition from nomadic hunter-gatherer bands to sedentary farming communities.",
    "quotes": [
      {"author": "John Lubbock", "work": "Pre-historic Times", "quote": "I propose the term **Neolithic** for that polished stone age which witnessed the dawn of agriculture and pottery in Europe."},
      {"author": "Gordon Childe", "work": "Man Makes Himself", "quote": "The **Neolithic** revolution gave humankind control over its food supply through the domestication of cereals and sheep."},
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "The transition to **Neolithic** village settlements laid the material foundations for tribal confederacies and organized architecture."}
    ]
  },
  "Dashboard \u2014 ne\\pachynema.md": {
    "primary": "The pachytene stage of prophase I in meiosis, during which homologous chromosomes are fully synapsed into thick bivalents and crossing-over occurs.",
    "secondary": "In cytogenetics and reproductive biology, pachynema is the prolonged meiotic stage characterized by fully formed synaptonemal complexes and active genetic recombination.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "At **pachynema**, the pairing of homologous chromosomes is complete, each bivalent appearing as a thick, condensed double cord."},
      {"author": "Thomas Hunt Morgan", "work": "The Physical Basis of Heredity", "quote": "The physical exchange of chromosomal segments by crossing-over takes place precisely during **pachynema**."},
      {"author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "Electron micrographs of **pachynema** reveal the tripartite synaptonemal complex zippering the homologues from end to end."}
    ]
  },
  "Dashboard \u2014 ne\\synnema.md": {
    "primary": "A compact, erect bundle or column of conidiophores bearing asexual conidia at the apex, produced by certain anamorphic fungi.",
    "secondary": "In systematic mycology and plant pathology, the formation of a synnema (as in Dutch elm disease fungus Ophiostoma) aids in spore presentation to visiting insect vectors.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "In Stilbum, the fertile hyphae bundle together into an erect columnar **synnema** topped with a glistening drop of spores."},
      {"author": "Bryce Kendrick", "work": "The Fifth Kingdom", "quote": "An insect vector brushing against a mature **synnema** readily picks up sticky conidia produced on its elevated tip."},
      {"author": "C. V. Subramanian", "work": "Hyphomycetes", "quote": "Taxonomic keys differentiate coremium and **synnema** based on the structural compaction of the ascending conidiophore bundle."}
    ]
  },
  "Dashboard \u2014 ne\\treponema.md": {
    "primary": "A taxonomic genus of spiral-shaped, highly motile flagellated spirochete bacteria, notably including Treponema pallidum, the causative agent of syphilis.",
    "secondary": "In medical microbiology and infectious disease, Treponema species possess endoflagella within their periplasmic space, allowing corkscrew motility through mucous membranes.",
    "quotes": [
      {"author": "Fritz Schaudinn", "work": "Vorläufiger Bericht über das Vorkommen von Spirochaeten in syphilitischen Krankheitsprodukten", "quote": "Darkfield illumination revealed the delicate twisting movements of **Treponema** pallidum extracted from primary chancres."},
      {"author": "Paul Ehrlich", "work": "Experimental Chemotherapy of Spirilloses", "quote": "Our discovery of Salvarsan established that targeted arsenical compounds could selectively destroy **Treponema** without poisoning host cells."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The discovery of pathogenic spirochetes like **Treponema** extended the germ theory of disease to complex venereal contagions."}
    ]
  },
  "Dashboard \u2014 ne\\trine.md": {
    "primary": "Composed of three parts or units; threefold or triple; in astrology, an aspect of 120 degrees between two celestial bodies, historically viewed as harmonious.",
    "secondary": "In historical poetry and theology, trine describes triadic celestial harmonies, the Christian Trinity, or triangular geometric configurations.",
    "quotes": [
      {"author": "Johannes Kepler", "work": "Harmonices Mundi", "quote": "The **trine** aspect, dividing the celestial circle by three, establishes a harmonious resonance among planetary orbits."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "That glorious form, that light unsufferable, and that far-beaming blaze of majesty, wherewith he wont at Heaven's high council-table to sit the midst of **Trine** Unity into."},
      {"author": "John Dryden", "work": "Annus Mirabilis", "quote": "Whether in benign conjunction or in **trine**, the stars smiled down upon the restoring of English peace."}
    ]
  },
  "Dashboard \u2014 ne\\zygonema.md": {
    "primary": "The zygotene stage of prophase I in meiosis, during which homologous chromosomes recognize each other and initiate close lateral pairing via synaptonemal complexes.",
    "secondary": "In cytogenetics, zygonema represents the critical chromosomal pairing window that precedes genetic recombination in pachytene.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "During **zygonema**, the homologous maternal and paternal chromosomes approach and unite in parallel pairs point for point."},
      {"author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "The synapsis of homologues at **zygonema** is governed by precise molecular recognition along matching chromomeric bands."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Structural heterozygosity, such as an inversion, visibly forces chromosomes into diagnostic loops at **zygonema**."}
    ]
  },
  "Dashboard \u2014 neu\\neuo.md": {
    "primary": "A variant combining form derived from Greek neuron, meaning sinew, tendon, or nerve.",
    "secondary": "In historical anatomical literature and lexical surveys, neuo- appears in early compound descriptions of muscular-neural junctions and nervous system pathways.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The ancient Greek noun neuron, with dialectal variants like **neuo**, originally meant cord or bowstring before narrowing to nerve."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System of Man and Vertebrates", "quote": "Early anatomists combined stems related to **neuo** when cataloging the fibrous architecture of peripheral nerves."},
      {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The functional coordination of the motor unit reflects ancient linguistic roots that tied the concept of **neuo** to muscular tension."}
    ]
  },
  "Dashboard \u2014 neu\\neuroplasticity.md": {
    "primary": "The ability of the nervous system to dynamically modify its structural organization, synaptic connections, and functional pathways in response to experience or injury.",
    "secondary": "In cognitive neuroscience and rehabilitation medicine, neuroplasticity underlies memory formation, perceptual learning, and recovery of motor function after stroke.",
    "quotes": [
      {"author": "Donald Hebb", "work": "The Organization of Behavior", "quote": "When an axon of cell A repeatedly excites cell B, growth processes take place, providing the physical foundation for **neuroplasticity**."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Long-term potentiation demonstrates that synaptic connections are not hardwired circuits, but dynamic engines of lifelong **neuroplasticity**."},
      {"author": "Santiago Ramón y Cajal", "work": "Degeneration and Regeneration of the Nervous System", "quote": "While adult central pathways were long deemed immutable, modern experiments uncover an astonishing latent capacity for functional **neuroplasticity**."}
    ]
  },
  "Dashboard \u2014 neu\\neuroscience.md": {
    "primary": "The multidisciplinary scientific study of the nervous system, encompassing neuroanatomy, neurophysiology, molecular neurobiology, and cognitive neuroscience.",
    "secondary": "In contemporary science, neuroscience bridges molecular genetics and psychological behavior to explain consciousness, cognition, and neurological pathologies.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "The central mission of **neuroscience** is to understand the biological mechanisms that give rise to human thought, emotion, and action."},
      {"author": "Francis Crick", "work": "The Astonishing Hypothesis", "quote": "The astounding challenge facing twenty-first century **neuroscience** is to explain subjective conscious experience through neural firing patterns."},
      {"author": "Gerald Edelman", "work": "Neural Darwinism", "quote": "Theoretical **neuroscience** models the brain not as an engineered computer, but as a dynamic selective system operating via neuronal group selection."}
    ]
  },
  "Dashboard \u2014 neu\\neuroscientist.md": {
    "primary": "A scientific specialist who conducts empirical research into the structure, biochemistry, physiological function, development, or pathologies of the nervous system.",
    "secondary": "In clinical and experimental medicine, a neuroscientist develops pharmacological agents, neural implants, and behavioral therapies to treat brain disorders.",
    "quotes": [
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "As a young **neuroscientist**, I chose the marine snail Aplysia because its giant neurons offered an accessible window into synaptic memory."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The clinical neurologist must think like an empathetic novelist and observe with the rigorous precision of a dedicated **neuroscientist**."},
      {"author": "V. S. Ramachandran", "work": "Phantoms in the Brain", "quote": "Simple mirror therapy allowed the **neuroscientist** to relieve excruciating phantom limb pain by rewiring the patient's visual cortex feedback."}
    ]
  },
  "Dashboard \u2014 not\\not.md": {
    "primary": "A combining element derived from Greek notos, meaning the south wind, south, or southern; or alternatively from Latin nota, a mark or sign.",
    "secondary": "In biogeography and biological systematics, not- forms terms designating southern geographical regions (Notogaea) or southern taxonomic groups.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek noun notos denoted the warm, rain-bringing south wind, lending the combining form **not** to geographical nomenclature."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "The root **not** carries deep antiquity in Aegean nautical terminology, marking southern maritime bearing."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "Biogeographers frequently prefix **not** when designating unique floral and faunal realms confined to the southern hemisphere."}
    ]
  },
  "Dashboard \u2014 not\\notable.md": {
    "primary": "Worthy of notice, attention, or remark; distinguished, prominent, or memorable.",
    "secondary": "In public history and political science, designating persons of prominent social standing, wealth, or influence (an assembly of notables).",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is a **notable** thing to observe how scientific inquiries that appear barren of utility frequently yield the richest practical fruit."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The world readily applauds **notable** achievements, yet rare is the biographer who records the humble virtues of private life."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her arrival at the ball caused a **notable** sensation among the company, and her beauty was admired by all."}
    ]
  },
  "Dashboard \u2014 not\\notary.md": {
    "primary": "A public officer legally empowered to authenticate contracts, attest deeds, administer oaths, take affidavits, and certify legal documents.",
    "secondary": "In civil law traditions, a notary (notaire) is a specialized jurist who drafts binding conveyances, prenuptial agreements, and estate settlements.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Go with me to a **notary**, seal me there your single bond; and, in a merry sport, if you repay me not on such a day, let the forfeit be an equal pound of your fair flesh."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The fees paid to an official **notary** ensure that contracts can be executed with public certainty and enforceability across foreign markets."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In continental Europe, the **notary** preserves familial property archives and maintains legal order with traditional authority."}
    ]
  },
  "Dashboard \u2014 not\\notate.md": {
    "primary": "To record, set down, or represent information using a formal system of graphic symbols, musical marks, or mathematical characters.",
    "secondary": "In musicology and choreography, to notate a composition or dance sequence creates an enduring textual score enabling precise interpretation and performance.",
    "quotes": [
      {"author": "Igor Stravinsky", "work": "Poetics of Music in the Form of Six Lessons", "quote": "The composer must **notate** his musical thoughts with utmost precision to prevent performers from distorting his expressive intent."},
      {"author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "To **notate** rhythmic polyphony accurately, modern composers developed complex meters and unconventional time signatures."},
      {"author": "Willard Van Orman Quine", "work": "Mathematical Logic", "quote": "A transparent symbolic system enables logicians to **notate** quantified predicates without lexical ambiguity."}
    ]
  },
  "Dashboard \u2014 not\\noted.md": {
    "primary": "Well-known, celebrated, and widely recognized for particular virtues, accomplishments, or talents; famous.",
    "secondary": "Having been recorded, observed, or registered in writing or mental memory.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Galapagos archipelago was already **noted** among whalers for its extraordinary giant tortoises and desolate volcanic crater landscapes."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon, Gent.", "quote": "Sleepy Hollow was a place **noted** for its quiet atmosphere and the visionary propensities of its rustic inhabitants."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The city of London was then **noted** for its crowded guild halls, bustling docks, and fierce civic independence."}
    ]
  },
  "Dashboard \u2014 not\\notify.md": {
    "primary": "To give formal notice, announcement, or information to someone; to advise or report officially.",
    "secondary": "In legal jurisprudence and commercial contract law, to notify a party establishes formal constructive knowledge and triggers statutory limitation periods.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The sheriff is bound by law to **notify** the defendant of the impending writ through personal service or public proclamation."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "When magistrates fail to protect the commonwealth, citizens have the moral duty to **notify** their fellows and defend constitutional liberties."},
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "I took care to **notify** our subscribers whenever a new shipment of philosophical books arrived from London."}
    ]
  },
  "Dashboard \u2014 not\\Notogaea.md": {
    "primary": "In zoogeography and biogeography, the southern realm of the world comprising Australasia, New Zealand, and associated oceanic islands.",
    "secondary": "In evolutionary biogeography, Notogaea is distinguished by its prolonged geographic isolation from the northern landmasses, fostering endemic monotremes, marsupials, and ratites.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "On the Classification and Distribution of the Alectoromorphae and Heteromorphae", "quote": "I proposed the division of terrestrial faunas into **Notogaea** and Arctogaea, highlighting the archaic mammalian fauna of Australasia."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The profound mammalian divergence of **Notogaea** demonstrates that Australia separated from Asia before the radiation of placental carnivores."},
      {"author": "Philip Lutley Sclater", "work": "On the General Geographical Distribution of the Members of the Class Aves", "quote": "Avian families endemic to **Notogaea**, such as the birds-of-paradise and bowerbirds, reflect undisturbed insular radiation."}
    ]
  },
  "Dashboard \u2014 not\\Notomys.md": {
    "primary": "A taxonomic genus of nocturnal hopping mice endemic to arid regions of Australia, characterized by elongated hindlimbs and bipedal jumping locomotion.",
    "secondary": "In mammalogy and ecological physiology, Notomys species (such as the spinifex hopping mouse) possess highly concentrated urine and metabolize dry seeds without free water.",
    "quotes": [
      {"author": "John Gould", "work": "The Mammals of Australia", "quote": "The delicate hopping mouse **Notomys** bounds across sandy dunes like a miniature kangaroo, evading dingoes in the moonlight."},
      {"author": "Ronald Strahan", "work": "The Mammals of Australia", "quote": "The kidneys of **Notomys** alexis exhibit immense medullary thickness, enabling the animal to survive on dry grain without drinking."},
      {"author": "Tim Flannery", "work": "The Future Eaters", "quote": "Several species of **Notomys** went rapidly extinct in the twentieth century following the introduction of the European red fox and feral cat."}
    ]
  },
  "Dashboard \u2014 not\\Nototherium.md": {
    "primary": "A taxonomic genus of large, extinct Pleistocene diprotodontid marsupials from Australia, resembling heavily built rhinoceros-sized wombats.",
    "secondary": "In vertebrate paleontology, Nototherium fossils discovered in alluvial cave deposits provide critical evidence for megafaunal extinctions during the late Quaternary.",
    "quotes": [
      {"author": "Richard Owen", "work": "Description of the Teeth and Portions of the Jaws of Two Extinct Quadruped Animals: Nototherium and Diprotodon", "quote": "The fossil dentition of **Nototherium** presents robust bilophodont molars adapted for grinding tough scrub foliage and dry grasses."},
      {"author": "Thomas Henry Huxley", "work": "On the Osteology of the Genus Nototherium", "quote": "Cranial fragments of **Nototherium** demonstrate wide zygomatic arches that accommodated colossal masseter muscles in these extinct herbivores."},
      {"author": "Tim Flannery", "work": "The Future Eaters", "quote": "The extinction of giant browsers like **Nototherium** reshaped the Australian ecosystem, permanently altering fire regimes across the continent."}
    ]
  },
  "Dashboard \u2014 od\\anodal.md": {
    "primary": "Pertaining to, situated at, or directed toward the anode in an electrochemical cell, cathode-ray tube, or electronic circuit.",
    "secondary": "In electrochemistry and neurostimulation, anodal current depolarizes neuronal membranes beneath the positive electrode, increasing cellular excitability.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electrolytic decomposition releases chlorine and oxygen at the **anodal** surface of the platinum wire."},
      {"author": "J. J. Thomson", "work": "Conduction of Electricity through Gases", "quote": "Perforations in the cathode allow positive rays to stream away from the **anodal** region into the observation tube."},
      {"author": "Svante Arrhenius", "work": "Immunochemistry", "quote": "Positively charged metal ions migrate away from the **anodal** zone during continuous electrophoretic separation."}
    ]
  },
  "Dashboard \u2014 od\\anode.md": {
    "primary": "The positively charged electrode in an electrolytic cell through which electric current enters from an external circuit; the site where oxidation occurs.",
    "secondary": "In a galvanic cell or discharging battery, the anode acts as the negative terminal where spontaneous oxidation liberates electrons into the external circuit.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I propose to call that electrode the **anode** by which the positive electric current enters the electrolyte from the battery."},
      {"author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Faraday consulted classical philologists to construct the scientific terms **anode** and cathode from the Greek words for ascent and descent."},
      {"author": "J. J. Thomson", "work": "Rays of Positive Electricity and Their Application to Chemical Analyses", "quote": "The stream of canal rays accelerates through the electric field established between the perforated cathode and the metallic **anode**."}
    ]
  },
  "Dashboard \u2014 od\\anodic.md": {
    "primary": "Pertaining to, occurring at, or characteristic of an anode; relating to oxidation reactions occurring at the positive electrode.",
    "secondary": "In corrosion engineering, anodic protection applies a controlled positive potential to passive metals to form a protective oxide film against acid attack.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The chemical nature of the **anodic** reaction depends on the decomposition potential of the dissolved anions."},
      {"author": "Svante Arrhenius", "work": "Textbook of Electrochemistry", "quote": "During electrolysis of copper sulfate, copper dissolves at the **anodic** pole while depositing in metallic purity upon the cathode."},
      {"author": "Walther Nernst", "work": "Theoretical Chemistry from the Standpoint of Avogadro's Rule and Thermodynamics", "quote": "The electrode potential governing **anodic** dissolution is formulated mathematically using the Nernst equation."}
    ]
  },
  "Dashboard \u2014 od\\anodise.md": {
    "primary": "To electrochemically coat a metal (especially aluminum) with a durable, corrosion-resistant protective oxide layer by making it the anode in an acid bath (British spelling).",
    "secondary": "In materials engineering and surface metallurgy, to anodise metal parts allows organic dyes and pigments to be permanently absorbed into the porous oxide layer.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "When electric currents pass through dilute sulfuric acid, one can **anodise** aluminum sheets to form an impervious barrier coating."},
      {"author": "Ulick Evans", "work": "The Corrosion and Oxidation of Metals", "quote": "Engineers **anodise** aerospace structural alloys to improve fatigue life and prevent pitting corrosion in salt spray environments."},
      {"author": "Cyril Stanley Smith", "work": "A History of Metallography", "quote": "The industrial ability to **anodise** aluminum revolutionized architectural decoration and consumer product finishing in the twentieth century."}
    ]
  },
  "Dashboard \u2014 od\\anodize.md": {
    "primary": "To coat a metal (especially aluminum, titanium, or magnesium) with a protective, corrosion-resistant oxide film by making it the anode in an electrolytic solution.",
    "secondary": "In aerospace manufacturing and industrial materials science, to anodize components increases surface hardness, dielectric strength, and wear resistance.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Electrolytic oxidation can **anodize** the metallic plate, building an inert dielectric film that halts further chemical attack."},
      {"author": "Ulick Evans", "work": "Metallic Corrosion, Passivity and Protection", "quote": "To **anodize** an aircraft skin requires precise regulation of bath temperature, voltage, and sulfuric acid concentration."},
      {"author": "Cyril Stanley Smith", "work": "A History of Metallography", "quote": "Decorative fabricators **anodize** architectural panels to infuse vivid light-fast colors into microscopic oxide pores."}
    ]
  },
  "Dashboard \u2014 od\\diode.md": {
    "primary": "A two-terminal electronic semiconductor or thermionic vacuum device that conducts electric current primarily in one direction, acting as a rectifier.",
    "secondary": "In semiconductor physics and electronic engineering, a p-n junction diode blocks reverse voltage up to its breakdown limit while enabling low-resistance forward conduction.",
    "quotes": [
      {"author": "John Ambrose Fleming", "work": "The Thermionic Valve and Its Developments in Radiotelegraphy", "quote": "The thermionic **diode** converted alternating radiofrequency currents into direct impulses capable of actuating a telephone receiver."},
      {"author": "William Shockley", "work": "Electrons and Holes in Semiconductors", "quote": "The current-voltage relationship of an ideal p-n junction **diode** is governed by carrier injection across the potential barrier."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "A solid-state **diode** acts like a microscopic one-way turnstile for electrons traversing the crystal boundary."}
    ]
  },
  "Dashboard \u2014 od\\od.md": {
    "primary": "A Greek combining root derived from hodos, signifying a way, path, route, journey, or method.",
    "secondary": "In scientific terminology and classical compound words, serves as the base for terms denoting electrical paths (anode, cathode, diode) and vehicular travel meters (odometer).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek feminine noun hodos forms the combining root **od**, signifying a path, highway, or systematic route."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "From Proto-Indo-European *sod- comes the versatile Greek stem **od**, meaning journey, transit, or traveled way."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "We adopted the Greek **od** for 'way' when coining electrode, anode, and cathode to describe the pathways of current."}
    ]
  },
  "Dashboard \u2014 od\\odometer.md": {
    "primary": "An instrument mounted on a vehicle or carriage that measures and displays the linear distance traveled over ground.",
    "secondary": "In mechanical engineering and transportation history, mechanical odometers calculate distance via gear trains connected to wheel rotations, while modern odometers use electronic wheel speed sensors.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings of Thomas Jefferson", "quote": "I fixed an **odometer** to the axle of my carriage to measure the exact distance between post houses on my journey to Philadelphia."},
      {"author": "Benjamin Franklin", "work": "The Papers of Benjamin Franklin", "quote": "While serving as Postmaster General, I devised a simple **odometer** attached to a carriage wheel to survey post routes across the colonies."},
      {"author": "Vitruvius", "work": "The Ten Books on Architecture", "quote": "The Roman engineer mounted an **odometer** upon a chariot, dropping a small pebble into a bronze vessel at the completion of each mile."}
    ]
  },
  "Dashboard \u2014 od\\parodos.md": {
    "primary": "In classical Greek drama, the initial entrance song or choral ode sung by the chorus as it enters the orchestra of the theater.",
    "secondary": "In classical theater architecture, the parodos designates either of the two open side pathways between the skene and the auditorium through which the chorus and spectators entered.",
    "quotes": [
      {"author": "Aristotle", "work": "Poetics", "quote": "The **parodos** is the first whole utterance of the chorus as they enter the orchestra to take up their dramatic station."},
      {"author": "Aeschylus", "work": "The Persians", "quote": "In the solemn **parodos**, the elders of Susa chant their forebodings concerning the fate of the Persian host marching against Hellas."},
      {"author": "Gilbert Murray", "work": "A History of Ancient Greek Literature", "quote": "The rhythmic procession of the tragic chorus through the open **parodos** established the emotional key of the performance."}
    ]
  },
  "Dashboard \u2014 od\\period.md": {
    "primary": "A distinct interval or span of time characterized by particular events, conditions, or cultural cycles; in grammar, a punctuation mark (.) terminating a sentence.",
    "secondary": "In astronomy and physics, the time required for a recurring cyclic motion or wave to complete one full cycle, such as an orbital or pendulum period.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Kepler's third law demonstrates that the square of the orbital **period** of a planet is proportional to the cube of its mean distance from the Sun."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Each successive geological **period** left its characteristic fossil flora and fauna embedded within stratified sedimentary rocks."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A well-balanced prose **period** satisfies both the ear with musical cadence and the intellect with structural symmetry."}
    ]
  },
  "Dashboard \u2014 od\\synod.md": {
    "primary": "A formal council, convocation, or assembly of church clergy, bishops, and lay delegates convened to settle matters of doctrine, ecclesiastical administration, or canon law.",
    "secondary": "In church history and canon law, synods (diocesan, provincial, or general) establish authoritative disciplinary canons and confess theological creeds.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Emperor Constantine summoned a great **synod** of Christian bishops at Nicaea to establish doctrinal unity across the empire."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The decrees ratified by a legitimate general **synod** bind the faithful in matters touching orthodox faith and morals."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "Lords and Commons of England, consider what nation it is whereof ye are: a nation not slow and dull, nor easily coerced by any priestly **synod**."}
    ]
  }
}

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate_form_finish_b4.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Finish Slice 1 Batch 4.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} with {len(data)} words.")
res = subprocess.run(["node", mjs_path], capture_output=True, text=True)
print("Node output:", res.stdout)
if res.stderr:
    print("Node error:", res.stderr)
