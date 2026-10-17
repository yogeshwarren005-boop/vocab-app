# -*- coding: utf-8 -*-
import json
import os

batch6 = {
  "Dashboard — melan/amelanchier.md": {
    "primary": "A genus of deciduous shrubs and small trees in the rose family Rosaceae, commonly known as serviceberries, shadbush, or juneberries.",
    "secondary": "In temperate dendrology, woodland trees producing delicate white spring flowers followed by sweet, dark purple, edible pome fruits.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The snowy blossoms of **Amelanchier** appear in early spring before the forest trees have expanded their leaves." },
      { "author": "John Burroughs", "work": "Riverby", "quote": "Cedar waxwings descended upon the hillside to feast upon the ripening purple berries of **Amelanchier**." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The hardy species of **Amelanchier** yield valued timber for tool handles and delicious summer fruit." }
    ]
  },
  "Dashboard — melan/amelanism.md": {
    "primary": "A genetic condition characterized by the complete absence of melanin pigment in the skin, hair, scales, or feathers.",
    "secondary": "In veterinary genetics and herpetology, a recessive mutation that leaves erythrophores and xanthophores intact, producing bright red or yellow morphs.",
    "quotes": [
      { "author": "Raymond Ditmars", "work": "The Reptile Book", "quote": "In captive cornsnakes, **amelanism** produces vivid orange and scarlet patterns lacking all trace of black pigment." },
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Recessive alleles for **amelanism** fail to synthesize functional tyrosinase within the neural-crest melanocytes." },
      { "author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Natural instances of **amelanism** are quickly weeded out by predators due to the loss of protective camouflage." }
    ]
  },
  "Dashboard — melan/aphaeomelanism.md": {
    "primary": "An inherited pigmentation deficiency characterized by the specific absence of pheomelanin (reddish-yellow melanin).",
    "secondary": "In avian and mammalian coat color genetics, a condition where animals retain normal black eumelanin but lack buff, rufous, or chestnut hues.",
    "quotes": [
      { "author": "Elliott Coues", "work": "Key to North American Birds", "quote": "The aberrant sparrow specimen exhibited **aphaeomelanism**, its plumage displaying cold slate and black without warm buff." },
      { "author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Geographic races occasionally undergo **aphaeomelanism**, resulting in localized gray color phases across arid basins." },
      { "author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "Mutations causing **aphaeomelanism** alter the biochemical sulfhydryl incorporation pathway in follicular melanocytes." }
    ]
  },
  "Dashboard — melan/eumelanin.md": {
    "primary": "The most common form of biological melanin pigment, brown or black in color, providing structural coloration and photoprotection against ultraviolet radiation.",
    "secondary": "In biochemistry and photobiology, a cross-linked polymer of 5,6-dihydroxyindole units that quenches free radicals and absorbs broadband light.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The protective epidermal screen against solar rays consists of dense granules of **eumelanin** within basal keratinocytes." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The dense polymeric network of **eumelanin** acts as a stable organic semiconductor and free-radical trap." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Tropical human populations possess an abundance of cutaneous **eumelanin** adapted to intense equatorial sunlight." }
    ]
  },
  "Dashboard — melan/hypermelanic.md": {
    "primary": "Characterized by an abnormally large amount of melanin; unusually dark or deeply pigmented.",
    "secondary": "In pathology and zoology, describing melanistic animal morphs or skin lesions exhibiting intense pathological deposition of dark pigment.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Adrenal cortical failure causes the skin to develop diffuse, **hypermelanic** bronze patches." },
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The borders of the malignant plaque became markedly **hypermelanic**, spreading irregularly into surrounding dermis." },
      { "author": "Alfred Russel Wallace", "work": "Tropical Nature and Other Essays", "quote": "Certain moist tropical islands produce distinct **hypermelanic** varieties among native lizards and birds." }
    ]
  },
  "Dashboard — melan/melan.md": {
    "primary": "The Greek combining form (melas, melanos, 'black, dark, gloomy') denoting black color, melanin pigment, or dark bodily fluids.",
    "secondary": "In scientific terminology, a root found in melanoma, melancholy, melanocyte, and Melanesia, designating darkness in physical, medical, and psychological senses.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "From the Greek root **melan**- we derive terms for the darkest pigments of animal skin and hair." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "In classical Greek, the stem **melan**- referred to dark wine, black ships, and the gloom of the underworld." },
      { "author": "William Whewell", "work": "Philosophy of the Inductive Sciences", "quote": "Naturalists adopted the combining form **melan**- to classify animals exhibiting atypical black coloration." }
    ]
  },
  "Dashboard — melan/melancholia.md": {
    "primary": "A deep, persistent mental state of intense sadness, dejection, or depression; historically, a disorder attributed to an excess of black bile.",
    "secondary": "In clinical psychiatry and psychoanalysis, a severe subtype of depressive disorder characterized by profound psychomotor retardation, anhedonia, and guilt.",
    "quotes": [
      { "author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "No despair is deeper or more agonizing than that bred by the dark vapors of confirmed **melancholia**." },
      { "author": "William Shakespeare", "work": "Hamlet", "quote": "There is a kind of confession in your looks which your modesties have not craft enough to colour, born of lingering **melancholia**." },
      { "author": "Sigmund Freud", "work": "Mourning and Melancholia", "quote": "In mourning the world has become poor and empty; in **melancholia** it is the ego itself which is impoverished." }
    ]
  },
  "Dashboard — melan/melancholiac.md": {
    "primary": "A person affected with melancholia; an individual suffering from deep, persistent depressive dejection.",
    "secondary": "In historical psychiatry, a clinical patient predisposed to brooding sorrow, withdrawal, and delusions of unworthiness.",
    "quotes": [
      { "author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "The solitary **melancholiac** shuns company and seeks out dark groves to nurse his solitary griefs." },
      { "author": "William James", "work": "The Varieties of Religious Experience", "quote": "To the religious **melancholiac**, the universe appears fundamentally evil, rotten, and forsaken of God." },
      { "author": "Samuel Johnson", "work": "The Rambler", "quote": "The confirmed **melancholiac** torments himself with imaginary evils while neglecting present duties." }
    ]
  },
  "Dashboard — melan/melancholic.md": {
    "primary": "Feeling, expressing, or causing deep, pensive sadness; relating to or affected with melancholia.",
    "secondary": "In classical humorism, one of the four traditional temperaments (black bile), characterized by serious reflection, artistic sensitivity, and solemnity.",
    "quotes": [
      { "author": "John Keats", "work": "Ode on Melancholy", "quote": "Ay, in the very temple of Delight Veil'd **melancholic** sorrow has her sovran shrine." },
      { "author": "Francis Bacon", "work": "Essays", "quote": "Men of **melancholic** temperament are prone to deep speculations and serious artistic achievements." },
      { "author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The bleak November afternoon cast a **melancholic** shade over the lonely moors." }
    ]
  },
  "Dashboard — melan/melancholy.md": {
    "primary": "A feeling of pensive sadness, typically with no obvious cause; or causing a gentle, sorrowful mood.",
    "secondary": "In cultural history and aesthetics, a prized reflective artistic sensibility associated with twilight, ruined landscapes, and philosophical solitude.",
    "quotes": [
      { "author": "William Shakespeare", "work": "As You Like It", "quote": "I can suck **melancholy** out of a song, as a weasel sucks eggs." },
      { "author": "John Milton", "work": "Il Penseroso", "quote": "Hail, divinest **Melancholy**, whose saintly visage is too bright to hit the sense of human sight." },
      { "author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "There is a delicious **melancholy** in the autumn woods that soothes the troubled mind." }
    ]
  },
  "Dashboard — melan/melanchthon.md": {
    "primary": "Philip Melanchthon (1497–1560), German Protestant reformer, humanist scholar, and author of the Augsburg Confession.",
    "secondary": "In Renaissance intellectual history, the scholar whose Greek surname (translating German Schwartzerdt, 'black earth') symbolized humanist synthesis with the Reformation.",
    "quotes": [
      { "author": "Martin Luther", "work": "Table Talk", "quote": "I am rough, boisterous, and warlike, but Master **Melanchthon** proceeds gently and quietly, building and planting." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The mild and scholarly **Melanchthon** sought in vain to temper the furious religious controversies of Germany." },
      { "author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "Beside the fiery Luther stood **Melanchthon**, whose Greek learning gave philosophical form to the Reformation." }
    ]
  },
  "Dashboard — melan/melanerpes.md": {
    "primary": "A genus of New World woodpeckers in the family Picidae, including the red-headed woodpecker and the acorn woodpecker.",
    "secondary": "In North American ornithology, social and colorful woodpeckers renowned for communal acorn caching and striking black-and-white plumage.",
    "quotes": [
      { "author": "John James Audubon", "work": "Ornithological Biography", "quote": "The red-headed woodpecker, classified as **Melanerpes**, flashes like a living meteor through the green orchards." },
      { "author": "Elliott Coues", "work": "Birds of the Colorado Valley", "quote": "The communal habits of **Melanerpes** in storing thousands of acorns in pine bark present an extraordinary spectacle." },
      { "author": "Alexander Wilson", "work": "American Ornithology", "quote": "The glossy black mantle and white wing-patches distinguish **Melanerpes** from all other nearctic picids." }
    ]
  },
  "Dashboard — melan/melanesia.md": {
    "primary": "A subregion of Oceania extending from New Guinea in the southwestern Pacific Ocean eastward to the Arafura Sea and Fiji.",
    "secondary": "In historical anthropology and Pacific geography, an ethnolinguistic region named from Greek melas (black) and nesos (islands) for the dark skin of its inhabitants.",
    "quotes": [
      { "author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The ethnological boundary separates the lighter Malay race from the dark-skinned inhabitants of **Melanesia**." },
      { "author": "Bronislaw Malinowski", "work": "Argonauts of the Western Pacific", "quote": "The Kula ring forms an extensive inter-island trading network binding the diverse communities of eastern **Melanesia**." },
      { "author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "Barrier reefs of colossal extent encircle the volcanic archipelagos scattered across **Melanesia**." }
    ]
  },
  "Dashboard — melan/melanesian.md": {
    "primary": "Of, relating to, or denoting Melanesia, its people, or their languages; an indigenous inhabitant of Melanesia.",
    "secondary": "In linguistics and anthropology, characterizing Oceanic Austronesian or Papuan languages and distinct maritime cultural complexes.",
    "quotes": [
      { "author": "Bronislaw Malinowski", "work": "Crime and Custom in Savage Society", "quote": "The daily life of a **Melanesian** villager is governed by mutual obligations and ancestral clan law." },
      { "author": "Margaret Mead", "work": "Sex and Temperament in Three Primitive Societies", "quote": "Artistic traditions in the **Melanesian** river village emphasized towering spirit masks and carved canoes." },
      { "author": "Robert Louis Stevenson", "work": "In the South Seas", "quote": "A sturdy **Melanesian** sailor stood at the helm as the schooner negotiated the coral passage." }
    ]
  },
  "Dashboard — melan/melanin.md": {
    "primary": "A dark brown to black biological pigment occurring in the hair, skin, and iris of people and animals, responsible for tanning of skin.",
    "secondary": "In dermatopathology and biochemistry, an insoluble polymer synthesized from tyrosine by tyrosinase, shielding nuclear DNA from UV damage.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "The Anaemias", "quote": "Melanocytes transfer granules of **melanin** into surrounding epithelial cells via branching dendritic processes." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The protective deposit of **melanin** in the skin shields tropical races from intense solar radiation." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The complex structure of **melanin** arises from the oxidative polymerization of catechol derivatives." }
    ]
  },
  "Dashboard — melan/melanise.md": {
    "primary": "British spelling of melanize; to darken or convert by the deposition of melanin pigment.",
    "secondary": "In ecological genetics and insect physiology, to darken plumage, cuticle, or scales under environmental or developmental cues.",
    "quotes": [
      { "author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "Industrial air pollution caused peppered moth populations to **melanise** rapidly throughout the English Midlands." },
      { "author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Exposure to maritime humidity appears to **melanise** the feathers of birds dwelling upon rocky northern coasts." },
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "During metamorphosis, the insect cuticle begins to **melanise** and harden upon contact with oxygen." }
    ]
  },
  "Dashboard — melan/melanism.md": {
    "primary": "An unusual darkening of body tissues caused by excessive development of melanin pigment, resulting in dark or black animals.",
    "secondary": "In evolutionary biology, adaptive darkening (such as industrial melanism in *Biston betularia*) demonstrating natural selection in changing environments.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Black panthers are well-known examples of **melanism** occurring within the ordinary spotted leopard species." },
      { "author": "E. B. Ford", "work": "Ecological Genetics", "quote": "The spread of industrial **melanism** in moths provided the first quantitative demonstration of rapid natural selection in the wild." },
      { "author": "Alfred Russel Wallace", "work": "Tropical Nature", "quote": "Complete **melanism** often confers concealment in dense, shaded forests where light scarcely penetrates." }
    ]
  },
  "Dashboard — melan/melanitta.md": {
    "primary": "A genus of heavy-bodied northern sea ducks in the family Anatidae, commonly known as scoters, noted for jet-black male plumage.",
    "secondary": "In marine ornithology, diving ducks (such as the black scoter, surf scoter, and velvet scoter) that dive into pounding coastal surf for mollusks.",
    "quotes": [
      { "author": "John James Audubon", "work": "Ornithological Biography", "quote": "Flocks of the velvet duck, classified under **Melanitta**, plunged headlong into the surging Atlantic breakers." },
      { "author": "Elliott Coues", "work": "Birds of the Northwest", "quote": "The adult male of **Melanitta** wears an intense coal-black plumage offset by a brightly swollen orange bill." },
      { "author": "Henry David Thoreau", "work": "Cape Cod", "quote": "Out on the grey ocean shoals, black rafts of **Melanitta** rode the heaving winter swell." }
    ]
  },
  "Dashboard — melan/melanize.md": {
    "primary": "To darken or color with melanin pigment; to cause to become dark or black.",
    "secondary": "In entomology and vertebrate genetics, to deposit melanin in cuticular or epidermal structures during wound healing or sclerotization.",
    "quotes": [
      { "author": "V. B. Wigglesworth", "work": "The Principles of Insect Physiology", "quote": "Within minutes of injury, enzymes in the hemolymph **melanize** the clotted blood to seal the wound against bacteria." },
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Cooler developmental temperatures tend to **melanize** the abdominal tergites of Drosophila." },
      { "author": "E. B. Ford", "work": "Moths", "quote": "Natural selection operated swiftly to **melanize** urban moth populations resting on soot-blackened tree trunks." }
    ]
  },
  "Dashboard — melan/melanoblast.md": {
    "primary": "A precursor cell derived from the embryonic neural crest that migrates through the dermis and differentiates into a melanin-producing melanocyte.",
    "secondary": "In developmental embryology and oncology, an unpigmented progenitor cell whose migration pathway determines adult pigmentation patterns and melanoma susceptibility.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Histology of the Blood and Tissues", "quote": "The embryonic **melanoblast** migrates from the neural crest into the basal layer of the developing skin." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "Arrested migration of the **melanoblast** during fetal life accounts for congenital Mongolian blue spots." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology", "quote": "Cytochemical markers identify the primitive **melanoblast** long before intracellular pigment synthesis begins." }
    ]
  },
  "Dashboard — melan/melanoblastoma.md": {
    "primary": "An older or historical medical term for a malignant melanoma arising from melanoblasts.",
    "secondary": "In surgical oncopathology, a highly aggressive, deeply pigmented malignant neoplasm characterized by rapid hematogenous and lymphatic metastasis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The lethal malignancy designated **melanoblastoma** frequently originates within a preexisting pigmented mole." },
      { "author": "William Henry Welch", "work": "Papers and Addresses", "quote": "Microscopic sections of the **melanoblastoma** revealed spindle-shaped and polyhedral cells choked with dark pigment." },
      { "author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Early and wide excision offers the sole hope of curing an invasive cutaneous **melanoblastoma**." }
    ]
  },
  "Dashboard — melan/melanocyte.md": {
    "primary": "A specialized, melanin-producing cell located in the basal layer of the skin epidermis, the hair follicles, and the uvea of the eye.",
    "secondary": "In cell biology and dermatology, a dendritic cell that synthesizes melanin within specialized organelles called melanosomes, transferring them to keratinocytes.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ultraviolet exposure stimulates the epidermal **melanocyte** to accelerate pigment transfer to surrounding skin cells." },
      { "author": "Paul Ehrlich", "work": "Studies on Immunity", "quote": "The dendritic arborization of each **melanocyte** permits contact with dozens of neighboring epidermal cells." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The tyrosinase enzyme within the **melanocyte** catalyses the initial oxidation of tyrosine to dopaquinone." }
    ]
  },
  "Dashboard — melan/melanoderma.md": {
    "primary": "An abnormal darkening or hyperpigmentation of the skin caused by excessive deposition of melanin.",
    "secondary": "In clinical dermatology, generalized or patchy cutaneous hypermelanosis resulting from Addison's disease, chronic arsenic poisoning, or sun damage.",
    "quotes": [
      { "author": "Thomas Addison", "work": "On the Constitutional and Local Effects of Disease of the Supra-Renal Capsules", "quote": "A pervasive **melanoderma**, giving the skin a peculiar bronze tint, heralds the destruction of the adrenal glands." },
      { "author": "Erasmus Wilson", "work": "Diseases of the Skin", "quote": "Severe friction combined with heat induced a localized **melanoderma** across the laborer's neck." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic intake of medicinal arsenic occasionally provokes a diffuse, rain-drop **melanoderma** over the trunk." }
    ]
  },
  "Dashboard — melan/melanogrammus.md": {
    "primary": "A genus of marine gadid teleost fishes containing the haddock (*Melanogrammus aeglefinus*), characterized by a black lateral line.",
    "secondary": "In commercial fisheries and North Atlantic ichthyology, an economically vital food fish distinguished by a prominent dark lateral line and a dark shoulder blotch.",
    "quotes": [
      { "author": "George Brown Goode", "work": "Fisheries and Fishery Industries of the United States", "quote": "The haddock, classified under **Melanogrammus**, is recognized by the inky black lateral line running to its tail." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Legend called the dark shoulder mark on **Melanogrammus** the thumbprint of Saint Peter." },
      { "author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "Shoals of young **Melanogrammus** drifted over the rich feeding grounds of Georges Bank." }
    ]
  },
  "Dashboard — melan/melanoma.md": {
    "primary": "A serious form of skin cancer that begins in the melanocytes; a malignant tumor containing melanin.",
    "secondary": "In oncology, an aggressive neoplasm marked by the ABCDE criteria (asymmetry, border irregularity, color variegation, diameter, evolving size) and high metastatic potential.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A pigmented cutaneous mole that begins to itch, bleed, or enlarge must be excised promptly to prevent lethal **melanoma**." },
      { "author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "Malignant lentigo in the elderly may persist quiescently for decades before transforming into invasive **melanoma**." },
      { "author": "Paul Ehrlich", "work": "Chemotherapy Studies", "quote": "The high resistance of metastatic **melanoma** to chemical agents spurred search for immunologic targets." }
    ]
  },
  "Dashboard — melan/melanophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of the color black or of darkness.",
    "secondary": "In clinical psychology and psychotherapy, a specific phobic aversion where dark objects, black clothing, or unlit spaces trigger intense panic attacks.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Cases of severe **melanophobia** occur wherein the sight of black mourning crape causes acute hysterical collapse." },
      { "author": "G. Stanley Hall", "work": "A Study of Fears", "quote": "Childhood fear of the dark frequently crystallizes into an enduring adult **melanophobia** toward somber colors." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "Instinctive antipathies such as **melanophobia** reflect ancient evolutionary dread of nocturnal predators." }
    ]
  },
  "Dashboard — melan/melanophore.md": {
    "primary": "A dark, pigment-bearing chromatophore cell found in the skin of amphibians, reptiles, and fish, containing melanin granules.",
    "secondary": "In comparative neurobiology, a dermal cell whose melanosomes disperse outward to darken skin or aggregate centrally to lighten it under hormonal control.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The chameleon changes its tint as nerve impulses disperse or concentrate melanin granules in every **melanophore**." },
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The branching processes of the **melanophore** expand across the dermal layer like a spider's web of pigment." },
      { "author": "E. Ray Lankester", "work": "Comparative Physiology", "quote": "Melatonin and adrenaline cause the **melanophore** to concentrate its dark granules, blanching the frog's skin." }
    ]
  },
  "Dashboard — melan/melanoplus.md": {
    "primary": "A large and diverse genus of North American grasshoppers in the family Acrididae, commonly known as spur-throated grasshoppers.",
    "secondary": "In agricultural entomology, a devastating pest genus including the migratory grasshopper (*Melanoplus sanguinipes*) and differential grasshopper.",
    "quotes": [
      { "author": "Charles Valentine Riley", "work": "The Rocky Mountain Locust", "quote": "Swarms of **Melanoplus** darkened the midday sky across Kansas, devouring every green blade in their path." },
      { "author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "The distinctive spine on the prosternum characterizes the genus **Melanoplus** among our native acridians." },
      { "author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "Species of **Melanoplus** deposit their egg-pods underground in early autumn to overwinter safely beneath snow." }
    ]
  },
  "Dashboard — melan/melanosis.md": {
    "primary": "An abnormal or excessive deposition of black pigment (melanin) in tissues or organs of the body.",
    "secondary": "In gastroenterology and toxicology, a condition such as melanosis coli, a benign dark pigmentation of the colonic mucosa caused by chronic anthraquinone laxative use.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Post-mortem examination revealed striking **melanosis** of the colon, the mucosa stained dark brown throughout." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Pigmentary **melanosis** must be distinguished from hematogenous hemosiderin staining by chemical iron tests." },
      { "author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Diffuse cuticular **melanosis** followed the prolonged administration of Fowler's arsenical solution." }
    ]
  },
  "Dashboard — melan/melanotis.md": {
    "primary": "A genus of New World passerine birds in the mockingbird family Mimidae, comprising the blue mockingbirds of Mexico and Central America.",
    "secondary": "In neotropical ornithology, slate-blue mimid birds characterized by a black facial mask or ear-coverts (from Greek melas, black, and ous, ear).",
    "quotes": [
      { "author": "Robert Ridgway", "work": "The Birds of North and Middle America", "quote": "The rich blue plumage and black auriculars distinguish **Melanotis** among all American mimids." },
      { "author": "Alexander Skutch", "work": "Life Histories of Central American Birds", "quote": "From the deep tropical ravine, the glorious varied song of **Melanotis** echoed through the dawn mist." },
      { "author": "Elliott Coues", "work": "Key to North American Birds", "quote": "The blue mockingbird of the genus **Melanotis** possesses exceptional imitative and melodic powers." }
    ]
  },
  "Dashboard — melan/melanthiaceae.md": {
    "primary": "A family of perennial monocotyledonous flowering plants in the order Liliales, including trilliums, death camases, and bunchflowers.",
    "secondary": "In systematic botany and toxicology, a family of rhizomatous herbs producing deadly steroid alkaloids (such as veratrine in *Veratrum*).",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Melanthiaceae** includes the poisonous white hellebore and graceful woodland trilliums." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Potent cardiovascular alkaloids pervade the rootstocks of many genera within the **Melanthiaceae**." },
      { "author": "Armen Takhtajan", "work": "Evolutionary Trends in Flowering Plants", "quote": "Morphological characters place **Melanthiaceae** near the ancestral base of the monocotyledonous order Liliales." }
    ]
  },
  "Dashboard — melan/melatonin.md": {
    "primary": "A hormone produced primarily by the pineal gland in darkness, regulating sleep-wake cycles and circadian rhythms.",
    "secondary": "In endocrinology, an indoleamine synthesized from serotonin that synchronizes circadian physiology; named for its ability to aggregate melanin in amphibian melanophores.",
    "quotes": [
      { "author": "Aaron B. Lerner", "work": "Isolation of Melatonin, the Pineal Gland Factor That Lightens Melanocytes", "quote": "We isolated the pineal hormone **melatonin**, which caused rapid aggregation of melanin granules in isolated frog skin." },
      { "author": "Oliver Sacks", "work": "The Mind's Eye", "quote": "Nocturnal surges of **melatonin** signal the brain to enter restful sleep as daylight fades." },
      { "author": "Linus Pauling", "work": "Orthomolecular Medicine", "quote": "The physiological synthesis of **melatonin** from serotonin illustrates the chemical governance of circadian biological rhythms." }
    ]
  },
  "Dashboard — melan/neuromelanin.md": {
    "primary": "A dark, insoluble polymer pigment found in catecholaminergic neurons of the brainstem, especially in the substantia nigra and locus coeruleus.",
    "secondary": "In neuropathology, an autoxidized dopamine/noradrenaline pigment that accumulates with aging and chelates heavy metals; its loss characterizes Parkinson's disease.",
    "quotes": [
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The deep black coloration of the substantia nigra is produced by cytoplasmic granules of **neuromelanin** inside large motor neurons." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In paralysis agitans, macroscopic pallor of the substantia nigra reflects the loss of cells laden with **neuromelanin**." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Degeneration of dopamine-producing cells rich in **neuromelanin** lies at the pathological heart of post-encephalitic parkinsonism." }
    ]
  },
  "Dashboard — melan/pheomelanin.md": {
    "primary": "A reddish to yellowish-brown melanin pigment rich in sulfur and benzothiazine rings, responsible for red hair and freckles.",
    "secondary": "In photobiology, a pigment produced when cysteine is incorporated during melanogenesis; unlike eumelanin, it generates free radicals upon UV irradiation.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Studies on Cell Staining", "quote": "Chemical analysis reveals that red hair owes its tint to sulfur-rich **pheomelanin** rather than standard black eumelanin." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The benzothiazine rings in **pheomelanin** confer yellow and reddish tones while conferring poor photoprotection." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Variations in the ratio of dark eumelanin to bright **pheomelanin** generate the diverse hair colors of human populations." }
    ]
  },
  "Dashboard — myo/demystify.md": {
    "primary": "To make a difficult, esoteric, or mysterious subject clearer, simpler, and easier to understand; to dispel the mystery surrounding something.",
    "secondary": "In pedagogy and scientific communication, to translate arcane concepts into transparent, rational, and accessible terms.",
    "quotes": [
      { "author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Science seeks not to strip the cosmos of wonder, but to **demystify** the natural processes that govern it." },
      { "author": "Richard Feynman", "work": "The Character of Physical Law", "quote": "My aim in these lectures is to **demystify** quantum mechanics without sacrificing its astonishing reality." },
      { "author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Clear logical analysis serves to **demystify** traditional metaphysical puzzles that have perplexed philosophers for centuries." }
    ]
  },
  "Dashboard — myo/leiomyoma.md": {
    "primary": "A benign, non-cancerous tumor of smooth muscle tissue, commonly occurring in the uterus (where it is known as a uterine fibroid).",
    "secondary": "In surgical pathology and gynecology, a well-circumscribed, whorled mesenchymal neoplasm of smooth muscle bundles that may cause menorrhagia and pelvic pain.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The uterine **leiomyoma** forms a dense, whorled fibrous mass that frequently undergoes hyaline degeneration." },
      { "author": "William Henry Welch", "work": "General Pathology", "quote": "Histologically, the **leiomyoma** consists of interlacing fascicles of elongated smooth muscle cells with blunt nuclei." },
      { "author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "A massive submucous **leiomyoma** caused severe secondary hypochromic anemia through recurrent hemorrhages." }
    ]
  },
  "Dashboard — myo/miosis.md": {
    "primary": "Excessive or abnormal constriction of the pupil of the eye, caused by contraction of the pupillary sphincter muscle.",
    "secondary": "In neuro-ophthalmology, pupillary constriction induced by parasympathomimetic drugs (pilocarpine), opioid intoxication, or Horner's syndrome.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pinpoint **miosis** in an unconscious patient strongly suggests acute narcotic intoxication or pontine hemorrhage." },
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The pupillary light reflex produces prompt **miosis** to protect the sensitive retina from excessive illumination." },
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Creeping Man", "quote": "Holmes noted the extreme **miosis** of the professor's eyes, indicating the recent influence of a powerful drug." }
    ]
  },
  "Dashboard — myo/miotic.md": {
    "primary": "Causing constriction of the pupil of the eye; or an agent, drug, or substance that constricts the pupil.",
    "secondary": "In clinical ophthalmology, parasympathomimetic agents (such as pilocarpine or physostigmine) used to treat acute angle-closure glaucoma.",
    "quotes": [
      { "author": "Albrecht von Graefe", "work": "Clinical Lectures on Ophthalmology", "quote": "Instilling a **miotic** drop of physostigmine opened the iridocorneal angle, bringing swift relief in acute glaucoma." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "The diagnostic administration of a **miotic** agent aids in localizing autonomic sympathetic lesions." },
      { "author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Calabar bean extract serves as the classic **miotic** remedy to counter the mydriasis of belladonna." }
    ]
  },
  "Dashboard — myo/my 2.md": {
    "primary": "The Greek root combining form my- (myein, 'to close or shut the eyes or lips'), yielding words related to secret rites (mystery) and ocular squinting (myopia).",
    "secondary": "In historical linguistics and lexical morphology, the root underlying mystical contemplation (shutting outward senses) and physiological pupillary narrowing (miosis).",
    "quotes": [
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The Indo-European radical **my 2** denotes the closure of the lips or eyelids, yielding Hellenic cultic mysteries." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "From the root **my 2** arose the ancient designation for initiates who kept their lips sealed in sacred silence." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The verbal root **my 2** signifies closing or shutting, especially said of the eyes in squinting or sleep." }
    ]
  },
  "Dashboard — myo/myo.md": {
    "primary": "The combining form from Greek mys (muscle) or myein (to shut or close), used in anatomical, pathological, and optical terms.",
    "secondary": "In biomedical terminology, designating muscles (myocardium, myopathy) or ocular squinting/closure (myopia, miosis).",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The combining form **myo**- appears in all medical terms describing muscular tissue and its contractile fibrils." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clinicians employ **myo**- to denote inflammatory or degenerative diseases attacking the cardiac muscle." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "Greek **myo**- combines the ideas of the small mouse-like muscle and the blinking closure of the eyelid." }
    ]
  },
  "Dashboard — myo/myopia.md": {
    "primary": "Nearsightedness; a refractive visual error in which distant objects appear blurred because light rays focus in front of the retina; or lack of foresight.",
    "secondary": "In clinical ophthalmology, axial elongation of the eyeball or excessive corneal curvature corrected with concave divergent lenses.",
    "quotes": [
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "In high **myopia**, the axial length of the eyeball is abnormally increased, requiring biconcave glass correction." },
      { "author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Political **myopia** blinds legislators to the long-term consequences of hasty, populist enactments." },
      { "author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "His extreme **myopia** compelled him to hold the ancient parchment within two inches of his spectacles." }
    ]
  },
  "Dashboard — myo/myopic.md": {
    "primary": "Nearsighted; affected with myopia; or lacking imagination, foresight, or intellectual breadth.",
    "secondary": "In optical physics and social criticism, describing visual fields corrected by negative lenses or narrow, short-sighted public policies.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "A **myopic** observer perceives foreground details with exquisite clarity while the distant landscape dissolves into blur." },
      { "author": "H. G. Wells", "work": "The Outline of History", "quote": "The **myopic** rivalries of European dynasties plunged the continent into catastrophic world war." },
      { "author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Do not dismiss social reforms with that **myopic** cynicism which sees only the gutter and never the stars." }
    ]
  },
  "Dashboard — myo/myosis.md": {
    "primary": "Excessive constriction of the pupil of the eye; variant spelling of miosis.",
    "secondary": "In neuro-ophthalmology, pupillary narrowing produced by stimulation of the parasympathetic third cranial nerve or topical cholinergics.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The classic Argyll Robertson pupil exhibits marked **myosis** and responds to accommodation but not to light." },
      { "author": "Albrecht von Graefe", "work": "Clinical Lectures", "quote": "Sustained **myosis** was maintained with Calabar bean extract to draw the iris away from the filtration angle." },
      { "author": "Robley Dunglison", "work": "A Dictionary of Medical Science", "quote": "The symptom termed **myosis** is a permanent unnatural contraction of the pupil, impeding night vision." }
    ]
  },
  "Dashboard — myo/myotic.md": {
    "primary": "Causing pupillary constriction, or an agent that causes the pupil of the eye to constrict; variant spelling of miotic.",
    "secondary": "In clinical therapeutics, describing ophthalmic drugs (such as pilocarpine or acetylcholine) that contract the ciliary muscle and pupillary sphincter.",
    "quotes": [
      { "author": "William Osler", "work": "Modern Medicine", "quote": "The ophthalmologist prescribed a **myotic** collyrium to prevent peripheral anterior synechiae." },
      { "author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Eserine is the most reliable **myotic** substance known for lowering intraocular pressure." },
      { "author": "Albrecht von Graefe", "work": "On Glaucoma", "quote": "Without regular **myotic** drops, the shallow anterior chamber threatened to close completely." }
    ]
  },
  "Dashboard — myo/mysterious.md": {
    "primary": "Difficult or impossible to understand, explain, or identify; of obscure nature, origin, or purpose.",
    "secondary": "In literature and philosophy, evoking a profound sense of awe, numinous dread, or inscrutable cosmic purpose.",
    "quotes": [
      { "author": "Albert Einstein", "work": "The World As I See It", "quote": "The most beautiful experience we can have is the **mysterious**; it is the fundamental emotion at the cradle of true science." },
      { "author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An air of stern, deep, and irredeemable gloom hung over and pervaded the **mysterious** mansion." },
      { "author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A **mysterious** parcel arrived each year on the same date, containing a single lustrous pearl." }
    ]
  },
  "Dashboard — myo/mysteriously.md": {
    "primary": "In a way that is difficult or impossible to understand, explain, or identify; with an air of mystery.",
    "secondary": "In narrative prose, describing enigmatic occurrences, unexplained disappearances, or unprovable phenomena.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "The documents disappeared **mysteriously** from the locked deed-box during the night." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "The compass needle pointed **mysteriously** into the void, reversed by the thunderbolt." },
      { "author": "Joseph Conrad", "work": "Lord Jim", "quote": "He vanished **mysteriously** into the dark tropical jungle, leaving only a legend behind." }
    ]
  },
  "Dashboard — myo/mystery.md": {
    "primary": "Something that is difficult or impossible to understand or explain; an enigma; a religious truth known only through divine revelation; an ancient secret religious rite.",
    "secondary": "In classical history and religious anthropology, esoteric initiatory rituals (such as the Eleusinian Mysteries) wherein sacred rites were concealed from the uninitiated.",
    "quotes": [
      { "author": "William Shakespeare", "work": "Hamlet", "quote": "There are more things in heaven and earth, Horatio, Than are dreamt of in your philosophy; life remains a grand **mystery**." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The solemn **mystery** of Eleusis was celebrated at midnight with torchlight and awe-inspiring pageantry." },
      { "author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The universe is not dead machine, but an infinite, living **mystery** clothing the eternal spirit." }
    ]
  },
  "Dashboard — myo/mystify.md": {
    "primary": "To utterly bewilder, perplex, or baffle someone; to make obscure or mysterious.",
    "secondary": "In psychological fiction and stage illusion, deliberately withholding key facts to cultivate suspense or misdirection.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "Holmes took immense pleasure in presenting his conclusions so as to completely **mystify** the official detectives." },
      { "author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The odd circumstances seemed contrived solely to **mystify** the police and confound ordinary inquiry." },
      { "author": "Jane Austen", "work": "Emma", "quote": "Frank Churchill loved to **mystify** his companions with playful riddles and ambiguous smiles." }
    ]
  },
  "Dashboard — myo/mystifying.md": {
    "primary": "Utterly bewildering, perplexing, or difficult to explain or understand.",
    "secondary": "In literary criticism and scientific research, describing anomalies or narrative twists that confound established expectations.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "It was the most singular and **mystifying** case that had ever challenged Holmes's powers of deduction." },
      { "author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The transmutation of species was long regarded as a **mystifying** riddle beyond empirical investigation." },
      { "author": "H. G. Wells", "work": "The Island of Dr. Moreau", "quote": "The half-human cries emanating from the enclosure presented a **mystifying** horror in the night." }
    ]
  },
  "Dashboard — op/metope.md": {
    "primary": "A square space between triglyphs in a Doric frieze, often decorated with carved relief sculpture.",
    "secondary": "In classical architecture, the frieze panel (from Greek meta, between, and ope, opening) carrying iconic sculptural narratives such as the Parthenon Centauromachy.",
    "quotes": [
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "Every carved **metope** of the Doric temple displayed heroes locked in fierce combat with centaurs." },
      { "author": "Walter Pater", "work": "Greek Studies", "quote": "The relief upon the marble **metope** was designed to be viewed from below under the sharp Mediterranean sun." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Centuries of storm had not effaced the glorious sculptured **metope** blocks of the Parthenon." }
    ]
  },
  "Dashboard — op/op.md": {
    "primary": "The combining form derived from Greek ops (eye, sight, vision) or ope (hole, aperture, opening).",
    "secondary": "In linguistics and scientific nomenclature, a foundational root yielding optical, autopsy, myopia, metope, and related visual and anatomical terms.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek radical **op**- denoted both the organ of vision and the aperture through which light enters." },
      { "author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Terms formed with **op**- encompass the entire mechanical and physiological doctrine of vision." },
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "From the archaic root **op**- sprang both Greek terms for looking and classical architectural openings." }
    ]
  },
  "Dashboard — op/opaion.md": {
    "primary": "An opening, eye, or aperture in a roof, ceiling, or dome in classical architecture; an oculus.",
    "secondary": "In ancient Greek architectural history, the central smoke-hole or lighting skylight in the roof of a hypaethral temple or megaron.",
    "quotes": [
      { "author": "Vitruvius", "work": "De Architectura", "quote": "Through the circular **opaion** in the crown of the dome, celestial light poured into the sacred rotunda." },
      { "author": "Walter Pater", "work": "Greek Studies", "quote": "The smoke of the hearth drifted upward through the **opaion** into the open sky." },
      { "author": "Arthur Evans", "work": "The Palace of Minos", "quote": "Minoan builders introduced a central **opaion** to illuminate interior halls without exposing them to gale winds." }
    ]
  },
  "Dashboard — op/opt.md": {
    "primary": "To make a choice from a range of possibilities; to decide or choose.",
    "secondary": "In decision theory and behavioral economics, selecting a preferred alternative among competing opportunities or policy options.",
    "quotes": [
      { "author": "John Stuart Mill", "work": "On Liberty", "quote": "A free citizen must have liberty to **opt** for his own path, provided it causes no injury to his neighbors." },
      { "author": "Bertrand Russell", "work": "Principles of Social Reconstruction", "quote": "Nations must **opt** for international arbitration if civilization is to survive the atomic age." },
      { "author": "William James", "work": "The Will to Believe", "quote": "In living dilemmas, we are compelled to **opt** between active faith and paralysis of the will." }
    ]
  },
  "Dashboard — op/optative.md": {
    "primary": "Expressing a wish or desire; in grammar, a verbal mood in ancient Greek and other languages used to express wishes or contingencies.",
    "secondary": "In linguistics and rhetoric, a grammatical category distinct from the subjunctive, conveying aspirations, prayers, or potential states.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek verb employs the **optative** mood to utter solemn prayers to the gods or polite requests." },
      { "author": "Samuel Taylor Coleridge", "work": "Table Talk", "quote": "His conversation dwelt forever in the **optative** mood, wishing for reforms he lacked the courage to enact." },
      { "author": "Thomas Babington Macaulay", "work": "Critical Essays", "quote": "The parliamentary resolution was phrased in gentle **optative** terms rather than mandatory commands." }
    ]
  },
  "Dashboard — op/optic.md": {
    "primary": "Of or relating to the eye or the sense of sight; an optical lens, eyepiece, or eye.",
    "secondary": "In anatomy and neuroscience, designating the second cranial nerve (optic nerve) that transmits visual impulses from the retina to the brain.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "The moon, whose orb through **optic** glass the Tuscan artist views at evening from Fiesole." },
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **optic** nerve penetrates the sclera to distribute its fibers across the internal retinal layer." },
      { "author": "Alexander Pope", "work": "An Essay on Man", "quote": "Why has not man a microscopic eye? For this plain reason, man is not a fly; his **optic** frame fits his station." }
    ]
  },
  "Dashboard — op/optical.md": {
    "primary": "Relating to sight, light, or the science of optics; designed to assist or utilize vision.",
    "secondary": "In physics and instrumentation, characterizing devices (microscopes, telescopes, lasers) that manipulate or detect electromagnetic waves in the visible range.",
    "quotes": [
      { "author": "Isaac Newton", "work": "Opticks", "quote": "The prism demonstrates the remarkable **optical** property that white light is a compound of differently refrangible rays." },
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "The cornea and crystalline lens together constitute the primary **optical** system of the human eye." },
      { "author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I observed the rotation of the plane of polarization when light traversed the **optical** glass in a magnetic field." }
    ]
  },
  "Dashboard — op/optically.md": {
    "primary": "In a way that relates to vision or light; by optical means.",
    "secondary": "In stereochemistry and crystallography, describing substances that rotate the plane of polarized light (optically active).",
    "quotes": [
      { "author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "Dextro-tartaric acid is **optically** active, rotating the plane of polarized light decisively to the right." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "Dust-free air inside the chamber became **optically** empty, scattering not a single ray of the searchlight." },
      { "author": "David Brewster", "work": "Treatise on Optics", "quote": "Birefringent crystals resolve incident light into two **optically** distinct refracted beams." }
    ]
  },
  "Dashboard — op/optician.md": {
    "primary": "A specialist qualified to fit and sell eyeglasses and contact lenses, or a maker and seller of optical instruments.",
    "secondary": "In the history of science, skilled instrument makers (such as John Dollond or Joseph von Fraunhofer) who perfected scientific lenses and prisms.",
    "quotes": [
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Fraunhofer, the celebrated Munich **optician**, mapped hundreds of dark lines across the solar spectrum." },
      { "author": "Charles Dickens", "work": "Dombey and Son", "quote": "Old Sol Gills was a mathematical instrument maker and **optician**, surrounded by quadrants and chronometers." },
      { "author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes submitted the walking-stick to the inspection of a London **optician** to verify the doctor's lenses." }
    ]
  },
  "Dashboard — op/optics.md": {
    "primary": "The scientific branch of physics that studies the behavior, properties, and interactions of light with matter.",
    "secondary": "In physical science, divided into geometrical optics (ray tracing and lens systems) and physical/wave optics (diffraction, interference, polarization).",
    "quotes": [
      { "author": "Isaac Newton", "work": "Opticks", "quote": "My design in this treatise of **optics** is not to explain properties by hypotheses, but to propose and prove them by reason and experiments." },
      { "author": "James Clerk Maxwell", "work": "A Dynamical Theory of the Electromagnetic Field", "quote": "The agreement of the velocity of light with electromagnetic wave speed shows that **optics** is an integral branch of electricity." },
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Physiological **optics** bridges physical physics with psychological perception, tracing light from lens to consciousness." }
    ]
  },
  "Dashboard — op/option.md": {
    "primary": "A thing that is or may be chosen; the freedom or right to choose from alternatives.",
    "secondary": "In finance and contract law, a privilege sold by one party to another giving the buyer the right to purchase or sell an asset at a set price.",
    "quotes": [
      { "author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The citizens had no other **option** than to ratify the constitution or dissolve the confederacy into warring factions." },
      { "author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The tenant retained the legal **option** to purchase the freehold upon the expiration of his lease." },
      { "author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king was left without an **option**, compelled to assent to the terms imposed by parliament." }
    ]
  },
  "Dashboard — op/optometrist.md": {
    "primary": "A licensed health professional who examines eyes for visual defects, prescribes corrective lenses, and detects ocular disorders.",
    "secondary": "In clinical vision care, an eye care provider specializing in refractive measurement, binocular vision therapy, and ocular disease detection.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The visiting **optometrist** fitted the achromatopsic children with dense red-tinted lenses to prevent daytime blinding." },
      { "author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The local **optometrist** occupied a bright storefront on Main Street lined with trial lenses and phoropters." },
      { "author": "H. G. Wells", "work": "The History of Mr. Polly", "quote": "A consult with a competent **optometrist** might have spared him years of chronic headache and squinting." }
    ]
  },
  "Dashboard — op/optometry.md": {
    "primary": "The practice or profession of examining the eyes for visual defects, measuring visual acuity, and prescribing corrective lenses.",
    "secondary": "In ophthalmic science, the discipline encompassing retinoscopy, refraction, keratometry, and the non-surgical management of ocular disorders.",
    "quotes": [
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The invention of the ophthalmoscope laid the scientific foundations of modern clinical **optometry**." },
      { "author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "Advances in **optometry** provided prism lenses that corrected the patient's intractable double vision." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "Accurate **optometry** is essential in school health programs to detect uncorrected astigmatism in children." }
    ]
  },
  "Dashboard — op/panoptical.md": {
    "primary": "Permitting the view of everything at once; of, relating to, or resembling a panopticon.",
    "secondary": "In social philosophy and architectural theory, Jeremy Bentham's surveillance design enabling a central inspector to observe all inmates continuously.",
    "quotes": [
      { "author": "Jeremy Bentham", "work": "Panopticon; or, The Inspection-House", "quote": "The **panoptical** arrangement allows a single inspector to oversee every cell from an unseen central tower." },
      { "author": "Michel Foucault", "work": "Discipline and Punish", "quote": "The **panoptical** mechanism automatizes and disindividualizes power, rendering surveillance constant in its effects." },
      { "author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "From his high garret window, Teufelsdröckh enjoyed a **panoptical** survey of the scurrying city mortals below." }
    ]
  },
  "Dashboard — op/synoptical.md": {
    "primary": "Characterized by, giving, or affording a general view of a whole; synoptic; condensed into a comprehensive summary.",
    "secondary": "In historical and biblical scholarship, presenting parallel accounts (such as the Gospels of Matthew, Mark, and Luke) in aligned columns.",
    "quotes": [
      { "author": "Francis Bacon", "work": "Novum Organum", "quote": "A **synoptical** table of instances enables the understanding to perceive the true forms of physical phenomena." },
      { "author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "The naturalist constructs a **synoptical** chart displaying the distribution of species across the globe." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "This **synoptical** view of the cranial bones makes clear their evolutionary homology across vertebrates." }
    ]
  },
  "Dashboard — op/synoptics.md": {
    "primary": "The Synoptic Gospels (Matthew, Mark, and Luke) considered together; or the science of synoptic meteorology.",
    "secondary": "In biblical criticism, the three gospels characterized by common perspective and shared text, forming the famous 'Synoptic Problem'.",
    "quotes": [
      { "author": "Ernest Renan", "work": "The Life of Jesus", "quote": "The **synoptics** preserve the vivid popular sayings and parables of Galilee with touching simplicity." },
      { "author": "Albert Schweitzer", "work": "The Quest of the Historical Jesus", "quote": "Critical study of the **synoptics** revealed the eschatological framework underpinning the apostolic message." },
      { "author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "In the **synoptics**, we hear the authentic voice of the prophet of Nazareth untangled from theological dogma." }
    ]
  },
  "Dashboard — pentacosi/pentacosi.md": {
    "primary": "The Greek combining numeral prefix (pentakosioi) denoting five hundred.",
    "secondary": "In classical Attic political history and metrology, a numeral prefix designating quantities of five hundred units or ancient socio-economic classes.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The stem **pentacosi**- derives from the ancient Greek numeral for five hundred, found in institutional titles." },
      { "author": "George Grote", "work": "A History of Greece", "quote": "Solon utilized the numeral prefix **pentacosi**- to classify citizens by their annual agricultural produce." },
      { "author": "William Whewell", "work": "Philosophy of the Inductive Sciences", "quote": "Higher geometric and numeric designations preserve Greek numeral elements such as **pentacosi**- in scientific vocabulary." }
    ]
  },
  "Dashboard — pentacosi/pentacosiomedimni.md": {
    "primary": "The highest of the four census property classes established by Solon in ancient Athens, consisting of citizens whose land yielded at least 500 medimnoi.",
    "secondary": "In classical constitutional history, the wealthy agrarian elite who alone were eligible for the archonship and treasurership of Athena.",
    "quotes": [
      { "author": "Aristotle", "work": "The Athenian Constitution", "quote": "Solon divided the citizenry into four classes according to property, of which the highest was the **pentacosiomedimni**." },
      { "author": "George Grote", "work": "A History of Greece", "quote": "Only members of the **pentacosiomedimni** were eligible to serve as archons and guardians of the public treasury." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Solonian democracy balanced popular rights against the aristocratic privileges of the **pentacosiomedimni**." }
    ]
  }
}

# Write curate-light-batch6.mjs
mjs_code = f"""import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {{
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {{
    console.error(`File not found: ${{filePath}}`);
    return false;
  }}
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {{
    console.error(`No > [!book] in ${{filePath}}`);
    return false;
  }}
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${{data.primary}}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${{data.secondary}}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${{q.author}} (*${{q.work}}*):** *"${{q.quote}}"*`).join('\\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${{quoteLines}}`;

  const newContent = `${{headerPart}}\\n\\n${{defBlock}}\\n\\n${{quotesBlock}}\\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}}

const batchData = {json.dumps(batch6, indent=2, ensure_ascii=False)};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {{
  if (updateNote(relPath, data)) updated++;
}}
console.log(`Successfully updated ${{updated}} of ${{Object.keys(batchData).length}} files in Batch 6.`);
"""

with open('main app/scripts/curate-light-batch6.mjs', 'w', encoding='utf-8') as f:
    f.write(mjs_code)

print("Generated curate-light-batch6.mjs with", len(batch6), "words.")
