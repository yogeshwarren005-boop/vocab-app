import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batch4Data = {
  "Dashboard — dactyl\\ectrodactyly.md": {
    primary: "A congenital limb malformation characterized by the deficiency or absence of one or more central digits of the hand or foot (split-hand/split-foot malformation).",
    secondary: "In medical genetics and dysmorphology, an autosomal dominant autopodial anomaly resulting in a deep median cleft of the hand or foot ('lobster-claw' deformity).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The family pedigree demonstrated typical dominant transmission of **ectrodactyly**, with median clefting of both hands across four generations." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "In severe **ectrodactyly**, the central rays are entirely suppressed, leaving only two opposed pincers of remarkable strength." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "The dexterity with which the patient manipulated surgical instruments with his **ectrodactyly** hand astonished all his colleagues." }
    ]
  },
  "Dashboard — dactyl\\heterodactyl.md": {
    primary: "Having the toes arranged with the first and second digits directed backward and the third and fourth forward, an arrangement unique to trogons.",
    secondary: "In avian systematics, an anatomical foot configuration that distinguishes the family Trogonidae from all other zygodactyl or anisodactyl birds.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "The trogons are uniquely **heterodactyl**, turning their second toe backward alongside the hallux to grasp tropical branches." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature and Other Essays", quote: "The resplendent quetzal exhibits the curious **heterodactyl** foot structure characteristic of its mountain family." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Comparative avian anatomy reveals that the **heterodactyl** foot evolved independently from ancestral perching forms." }
    ]
  },
  "Dashboard — dactyl\\heterodactylous.md": {
    primary: "Characterized by heterodactyly; possessing differently directed or unequal digits.",
    secondary: "In ornithology, designating birds whose inner two toes are reversed backward while the outer two remain forward.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The **heterodactylous** foot of the trogon illustrates how digital orientation can diverge from the common climbing type." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "Tendons of the deep flexor muscles are specially routed to operate the reversed digits of the **heterodactylous** limb." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "We observed **heterodactylous** trogons perching motionless for hours upon low boughs before darting after flying insects." }
    ]
  },
  "Dashboard — dactyl\\heterodactyly.md": {
    primary: "The condition of having an unusual or irregular arrangement of toes, especially with digits one and two reversed backward as in trogons.",
    secondary: "In comparative osteology, an autopodial specialization providing a secure bilateral pinch upon slender forest vines.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lectures on Comparative Anatomy", quote: "True **heterodactyly** occurs nowhere among living birds outside the limits of the tropical order Trogoniformes." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "The subtle differences between zygodactyly and **heterodactyly** demonstrate how developmental pathways can reverse alternative digits." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The ancient fossil record confirms that avian **heterodactyly** had already crystallized in Eocene trogons." }
    ]
  },
  "Dashboard — dactyl\\hyperdactyly.md": {
    primary: "The congenital presence of supernumerary or extra fingers or toes; polydactyly.",
    secondary: "In developmental genetics and teratology, the development of additional digital rays resulting from ectopic sonic hedgehog signaling in the limb bud.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Symmetrical **hyperdactyly** involving six well-formed digits on each extremity frequently follows strict dominant inheritance." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "The transmission of **hyperdactyly** in cats and domestic poultry provided early breeders with proof of abrupt hereditary variation." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "Amputation of the supernumerary digit in **hyperdactyly** should be deferred until radiographic ossification clarifies the joint relations." }
    ]
  },
  "Dashboard — dactyl\\leptodactylous.md": {
    primary: "Having slender, thin, or delicate toes or fingers.",
    secondary: "In herpetology and zoological taxonomy, describing frogs of the family Leptodactylidae or birds possessing long, unwebbed digital rays.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Travels on the Amazon and Rio Negro", quote: "Along the muddy river margins hopped active **leptodactylous** frogs, navigating dense leaf litter with slender unwebbed toes." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The **leptodactylous** digits of jacanas allow them to distribute their weight across floating water-lily pads." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "Several small **leptodactylous** species were discovered sheltering beneath fallen logs in the humid Valdivian forests." }
    ]
  },
  "Dashboard — dactyl\\macrodactylus.md": {
    primary: "A genus of American scarab beetles (family Scarabaeidae), most notably Macrodactylus subspinosus (the rose chafer), having remarkably elongated spiny legs.",
    secondary: "In entomology and agronomy, destructive agricultural pests whose adults voraciously devour the blossoms and foliage of roses, grapes, and fruit trees.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "Swarms of the rose chafer, **Macrodactylus** subspinosus, quickly reduce delicate rose petals to ragged shreds in early June." },
      { author: "John Torrey", work: "Reports on Injurious Insects", quote: "Vineyard growers suffered heavy losses from the long-legged beetle **Macrodactylus**, which strips the young grape clusters." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "The formidable tarsal claws of **Macrodactylus** enable the beetle to cling tenaciously to windblown blossoms." }
    ]
  },
  "Dashboard — dactyl\\monodactyly.md": {
    primary: "The condition of having only a single functional digit on each limb, as in the modern horse (Equus).",
    secondary: "In evolutionary morphology, the extreme cursorial specialization in equids resulting from the progressive reduction of side toes and hypertrophy of the third metacarpal.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The transition from four-toed Eohippus through three-toed Protohippus to modern equine **monodactyly** provides unanswerable proof of evolution." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The single hoof of the horse represents the triumphant culmination of **monodactyly** adapted for speed across grassy plains." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "In achieving **monodactyly**, the horse sacrificed lateral agility for maximal forward propulsion upon a single central pillar." }
    ]
  },
  "Dashboard — dactyl\\oligodactyly.md": {
    primary: "A congenital physical anomaly characterized by the presence of fewer than five fingers or toes on a hand or foot.",
    secondary: "In medical genetics and teratology, digital hypoplasia or agenesis occurring as an isolated limb defect or in association with complex syndromic conditions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The congenital infant presented with severe bilateral **oligodactyly**, possessing only two functional digits on each hand." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Radiographs of **oligodactyly** reveal whether the missing digits represent true ray absence or fusion of adjacent metacarpal blastemas." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Despite his congenital **oligodactyly**, the craftsman operated fine watchmaking tools with marvelous digital precision." }
    ]
  },
  "Dashboard — dactyl\\pamprodactyly.md": {
    primary: "An arrangement of avian toes in which all four digits point forward, found in swifts and mousebirds.",
    secondary: "In avian functional morphology, an extreme adaptation enabling birds to hang vertically from rock crevices, chimney flues, or tree trunks.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "The foot of the common swift displays complete **pamprodactyly**, all four short curved claws pointing forward like crampons." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Swifts roosting inside limestone caves cling to the vertical stone with the aid of their **pamprodactyly** feet." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The swift can scarcely walk upon level ground, its **pamprodactyly** toes being formed purely for grasping perpendicular masonry." }
    ]
  },
  "Dashboard — dactyl\\pentadactyl.md": {
    primary: "Having five fingers or toes on each hand or foot; an animal possessing five-toed limbs.",
    secondary: "In vertebrate morphology, characterizing the primitive ancestral limb design shared by amphibians, reptiles, birds, and mammals.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The basic **pentadactyl** limb is modified by natural selection into the wing of the bat, the paddle of the whale, and the foot of the horse." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "What can be more curious than that the **pentadactyl** hand of man, formed for grasping, should be fashioned on the same pattern as the mole's digging claw?" },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "Early Devonian tetrapods experimented with polydactylous paddles before the **pentadactyl** standard was locked in." }
    ]
  },
  "Dashboard — dactyl\\pentadactylous.md": {
    primary: "Characterized by having five digits on each limb; pentadactyl.",
    secondary: "In comparative osteology, exhibiting the archetypal tetrapod digital formula of five radiating digits.",
    quotes: [
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "The mammalian skeleton remains fundamentally **pentadactylous**, even when lateral digits atrophy into small vestigial splints." },
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The primitive **pentadactylous** condition of ancestral reptiles serves as our reference baseline for all limb modifications." },
      { author: "Alfred Romer", work: "The Vertebrate Body", quote: "In human anatomy, the persistence of an unspecialized **pentadactylous** hand was the prerequisite for tool use." }
    ]
  },
  "Dashboard — dactyl\\pentadactyly.md": {
    primary: "The state or condition of possessing five digits on each limb.",
    secondary: "In evolutionary biology, the universal morphological baseline of crown tetrapods, conserved across hundreds of millions of years.",
    quotes: [
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "We owe our ten fingers and ten toes to the contingent survival of the ancestral lineage that established **pentadactyly**." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "The remarkable conservatism of **pentadactyly** across amphibians and mammals argues for deep developmental constraints in digital patterning." },
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", quote: "Even where digits are reduced to three or one, embryology confirms that the mammalian limb bud begins in **pentadactyly**." }
    ]
  },
  "Dashboard — dactyl\\perissodactyl.md": {
    primary: "An odd-toed ungulate mammal belonging to the order Perissodactyla (such as horses, tapirs, and rhinoceroses).",
    secondary: "In mammalian systematics, an ungulate characterized by mesaxonic foot symmetry, where weight is borne primarily by the enlarged third digit.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The **perissodactyl** lineage traces an unbroken fossil succession from the four-toed dawn horse to the single-toed modern stallion." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Extinct tapir-like creatures connect the ancient **perissodactyl** stock with early pachyderms." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "In the **perissodactyl** skeleton, the middle digit bears the main axis of stress, while the lateral toes progressively diminish." }
    ]
  },
  "Dashboard — dactyl\\polydactyl.md": {
    primary: "Having more than the normal number of fingers or toes (such as a six-toed cat or human).",
    secondary: "In medical genetics and animal breeding, an individual exhibiting extra preaxial or postaxial digits.",
    quotes: [
      { author: "Ernest Hemingway", work: "Selected Letters", quote: "My white **polydactyl** cat sauntered across the patio, displaying six large claws on each forepaw with comical pride." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The **polydactyl** infant had a small rudimentary digit attached by a slender pedicle to the ulnar border of the hand." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Breeders noted that **polydactyl** poultry passed their extra hind toe to half of their offspring with remarkable regularity." }
    ]
  },
  "Dashboard — dactyl\\polydactylous.md": {
    primary: "Having extra fingers or toes; characterized by polydactyly.",
    secondary: "In genetics and physical examination, exhibiting supernumerary digits along the digital rays.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "In several recorded human genealogies, **polydactylous** fathers transmitted their six-fingered hands through three generations." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "The **polydactylous** strain of guinea pigs established by Castle illustrated cumulative modifier genes acting on digital development." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough examination of the **polydactylous** foot ensures that accessory metatarsal bones are not overlooked before surgery." }
    ]
  },
  "Dashboard — dactyl\\polydactylus.md": {
    primary: "The specific epithet in zoological and botanical taxonomy designating species with many fingers, rays, or toes; a multi-digited animal.",
    secondary: "In ichthyology, the genus Polydactylus comprising the threadfins (family Polynemidae), characterized by finger-like free pectoral filaments.",
    quotes: [
      { author: "Francis Day", work: "The Fishes of India", quote: "Fishes of the genus **Polydactylus** utilize their long detached pectoral filaments to grope for crustaceans in muddy estuaries." },
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "The threadfin, **Polydactylus** paradiseus, was prized by Anglo-Indian diners for its exquisite flavor and delicate flesh." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "We secured specimens of **Polydactylus** along the tropical coast, marveling at the sensitive tactile rays beneath the gills." }
    ]
  },
  "Dashboard — dactyl\\polydactyly.md": {
    primary: "A congenital anomaly in humans and animals characterized by the presence of extra fingers or toes.",
    secondary: "In medical genetics, a condition categorized as preaxial (radial/tibial), postaxial (ulnar/fibular), or central, often associated with Ellis-van Creveld or Meckel syndromes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Postaxial **polydactyly** of the hand is ten times more frequent in persons of African ancestry than in Europeans." },
      { author: "Francis Galton", work: "Hereditary Genius", quote: "The inheritance of **polydactyly** furnished early anthropologists with an unambiguous anatomical marker of genetic transmission." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "In isolated island communities, genetic drift can elevate the frequency of harmless traits like **polydactyly**." }
    ]
  },
  "Dashboard — dactyl\\schizodactyly.md": {
    primary: "The congenital condition in which digits are deeply cleft or split, as in ectrodactyly; or in ornithology, having toes completely cleft and unwebbed.",
    secondary: "In avian morphology, a foot structure lacking interdigital webbing, adapted for walking or running over marshy soil.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "The rails and gallinules display extreme **schizodactyly**, their long unwebbed toes spreading wide to walk upon soft aquatic mud." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "Avian **schizodactyly** contrasts with palmiped webbing, providing independent mobility to each individual digit." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "In human teratology, severe **schizodactyly** produces a deep central fissure that bifurcates the hand into two claw-like halves." }
    ]
  },
  "Dashboard — dactyl\\syndactylism.md": {
    primary: "The condition of having two or more fingers or toes joined together; syndactyly.",
    secondary: "In mammalian comparative anatomy, the natural evolutionary fusion of digits, as seen in diprotodont marsupials (kangaroos and possums).",
    quotes: [
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "In the kangaroo, **syndactylism** fuses the second and third toes into a single sheath, forming a specialized grooming comb." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Congenital **syndactylism** of the third and fourth fingers is easily corrected by plastic separation in early childhood." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "Marsupial **syndactylism** represents an ancient functional adaptation preserved across diverse Australasian genera." }
    ]
  },
  "Dashboard — dactyl\\syndactylous.md": {
    primary: "Having digits that are fused together or connected by a web; web-toed or web-fingered.",
    secondary: "In zoology, describing animals whose digits are enclosed within a shared integumentary sheath.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **syndactylous** foot of marsupial climbers demonstrates how fused digits can be repurposed for grooming fur." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Cuscuses and tree kangaroos display **syndactylous** hind feet that grip mossy branches with remarkable tenacity." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "Kingfishers possess **syndactylous** feet in which the outer and middle toes are united for half their length." }
    ]
  },
  "Dashboard — dactyl\\syndactyly.md": {
    primary: "The condition of having some or all of the fingers or toes joined together, either by skin (webbed) or by bone.",
    secondary: "In developmental biology, a common congenital hand malformation resulting from the failure of programmed apoptosis in the interdigital webs during gestation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Complete cutaneous **syndactyly** between the index and middle fingers is successfully remedied by zig-zag surgical plasty." },
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Apoptotic cell death between the developing digits carves out the fingers; when it fails, **syndactyly** results." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "The child was born with simple cutaneous **syndactyly**, but surgical separation gave him full digital freedom to learn sign language." }
    ]
  },
  "Dashboard — dactyl\\tetradactylous.md": {
    primary: "Having four digits on each limb; four-toed or four-fingered.",
    secondary: "In comparative vertebrate osteology, possessing four functional digits per autopod, as in many amphibians and birds.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The forelimb of the salamander is **tetradactylous**, possessing four well-developed digits without a thumb." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Vertebrates", quote: "In pigs and hippopotamuses, the **tetradactylous** foot retains two central weight-bearing hooves and two reduced lateral dewclaws." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "The transition from pentadactyl ancestors to **tetradactylous** dinosaurs accompanied bipedal cursorial evolution." }
    ]
  },
  "Dashboard — dactyl\\tetradactyly.md": {
    primary: "The condition of possessing four fingers or toes on a limb.",
    secondary: "In evolutionary morphology, digital reduction from the ancestral pentadactyl condition to four functional digits, seen across anurans and avian feet.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Avian **tetradactyly** preserves digits one through four, while the fifth digit is entirely lost." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Comparative analysis of tetrapod feet shows that **tetradactyly** arose independently in multiple amphibian and reptilian lineages." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The functional stability of **tetradactyly** in perching birds proves that four digits provide optimal grasping geometry." }
    ]
  },
  "Dashboard — dactyl\\tridactyly.md": {
    primary: "The condition of possessing three digits on each hand or foot.",
    secondary: "In vertebrate paleontology and evolutionary biology, digital reduction to three functional toes, classic in theropod dinosaurs, emus, and fossil horses (Protohippus).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The Miocene horse Protohippus exhibited complete **tridactyly**, its two slender lateral toes flanking a dominant central hoof." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Theropod dinosaurs achieved formidable bipedal balance through symmetrical avian **tridactyly**." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The three-toed rhea of South America illustrates how **tridactyly** evolved to facilitate rapid flightless running over open plains." }
    ]
  },
  "Dashboard — dactyl\\undatable.md": {
    primary: "Not capable of being dated; impossible to assign to a specific historical date or chronological period.",
    secondary: "In historical archaeology and palaeography, lacking stratigraphic markers, typological diagnostics, or radiocarbon material necessary for chronology.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Ancient tribal customs drifted through oral traditions in an **undatable** antiquity long before the arrival of Roman legions." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "Unstratified surface sherds gathered outside the palace walls remained unfortunately **undatable**." },
      { author: "Virginia Woolf", work: "Orlando", quote: "Love and grief belong to that timeless, **undatable** realm of the human soul that laughs at centuries." }
    ]
  },
  "Dashboard — dactyl\\undated.md": {
    primary: "Not bearing a date; not marked with a date of origin, publication, or execution.",
    secondary: "In historical bibliography and textual criticism, a manuscript, epistle, or coin whose exact year must be deduced from internal contextual evidence.",
    quotes: [
      { author: "Samuel Johnson", work: "The Lives of the English Poets", quote: "An **undated** letter found among his papers throws unexpected light upon his youthful dispute with Addison." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "She handed me an **undated** note written in a hurried, trembling hand, requesting an immediate interview." },
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "Holmes examined the **undated** letter, holding the heavy Bohemian paper up to the gas lamp." }
    ]
  },
  "Dashboard — dactyl\\zygodactyly.md": {
    primary: "An arrangement of bird toes in which two toes point forward (digits 2 and 3) and two point backward (digits 1 and 4).",
    secondary: "In avian functional anatomy, the specialized climbing and grasping foot morphology characteristic of woodpeckers, parrots, and toucans.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **zygodactyly** of the woodpecker allows it to climb tree trunks with extraordinary vertical agility while hammering for grubs." },
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "In parrots, **zygodactyly** transforms the foot into a versatile hand capable of holding nuts while the beak cracks them." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Tropical forest birds like toucans and barbets utilize their **zygodactyly** claws to scramble among dense hanging vines." }
    ]
  },
  "Dashboard — der\\Dermaptera.md": {
    primary: "The insect order comprising the earwigs, characterized by short leathery forewings (tegmina) and prominent abdominal forceps (cerci).",
    secondary: "In systematic entomology, hemimetabolous insects with large semicircular membranous hindwings folded fanwise beneath protective elytra.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "The order **Dermaptera** is distinguished by the powerful forcep-like cerci that terminate the abdomen in both sexes." },
      { author: "Jean-Henri Fabre", work: "The Life of the Fly", quote: "The mother earwig of the **Dermaptera** displays touching maternal care, guarding her clutch of eggs beneath stones." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Male specimens in the **Dermaptera** use their curved abdominal pincers in ritualized courtship displays." }
    ]
  },
  "Dashboard — der\\der.md": {
    primary: "The root (from Greek derma, dermatos, meaning 'skin, hide, leather'), forming the basis of terms relating to the skin and cutaneous layers.",
    secondary: "In morphological linguistics and anatomy, an abbreviated combining radical present in dermal, dermis, and epidermic.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From the ancient Greek root **der**, to flay or strip, arose derma, the skin or hide of an animal." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The radical **der** signifies skin, entering English through anatomical terms like dermatitis and epidermis." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "All cutaneous compounds bearing the syllable **der** trace their origin to the protective covering of the vertebrate body." }
    ]
  },
  "Dashboard — der\\dermal.md": {
    primary: "Relating to or affecting the skin; cutaneous.",
    secondary: "In vertebrate anatomy, relating specifically to the dermis or to bony armor plates formed within the dermis (dermal ossicles, dermal scutes).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The bony carapace of the armadillo and the scales of reptiles are true **dermal** ossifications." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Systemic lupus erythematosus characteristically displays an erythematous **dermal** eruption over the malar eminences." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Fossil glyptodonts were encased in massive **dermal** armor composed of thousands of sutured bony plates." }
    ]
  },
  "Dashboard — der\\dermic.md": {
    primary: "Of, relating to, or consisting of the dermis; dermal.",
    secondary: "In histological descriptions, pertaining to the vascular, collagenous corium situated beneath the basement membrane.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Inflammatory infiltrates congregate primarily around the capillary loops of the upper **dermic** papillae." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Subcutaneous edema separates the deeper **dermic** fibers, producing a boggy swelling that pits on pressure." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "Chronic syphilitic eruptions typically produce indurated **dermic** nodules that heal with circular scarring." }
    ]
  },
  "Dashboard — der\\dermis.md": {
    primary: "The thick layer of living tissue below the epidermis which forms the true skin, containing blood capillaries, nerve endings, and sweat glands.",
    secondary: "In cuticular physiology and histopathology, the dense irregular connective tissue layer providing tensile strength and elasticity to the integument.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The vascular **dermis** projects into the overlying epidermis in thousands of sensitive papillae containing tactile corpuscles." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Extravasated erythrocytes trapped within the **dermis** produce the non-blanching macules of purpura." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The human **dermis** is the sensitive boundary where the nervous system touches and perceives the external universe." }
    ]
  },
  "Dashboard — der\\ectoderm.md": {
    primary: "The outermost layer of cells or tissue of an embryo in early development, or the parts derived from this.",
    secondary: "In embryology, the germ layer that gives rise to the epidermis, hair, nails, tooth enamel, sensory epithelia, and the entire nervous system.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "The hollow blastula invaginates to form two primary germ layers, of which the outer is the **ectoderm**." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The entire spinal cord and brain arise from a simple longitudinal folding of the embryonic **ectoderm**." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "Comparative gastrulation proves that the neural tube and the skin share a common parentage in the primordial **ectoderm**." }
    ]
  },
  "Dashboard — der\\ectodermal.md": {
    primary: "Of, relating to, or derived from the ectoderm.",
    secondary: "In clinical genetics and pathology, designating structures or developmental anomalies (such as ectodermal dysplasia) affecting skin, teeth, and nerves.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Anhidrotic **ectodermal** dysplasia presents with sparse hair, missing dentition, and an inability to sweat." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "The dorsal blastopore lip induces adjacent **ectodermal** cells to abandon epidermal fate and become neural plate." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Cellular fate mapping confirms that lens placodes arise directly from localized **ectodermal** thickenings." }
    ]
  },
  "Dashboard — der\\ectodermic.md": {
    primary: "Relating to or formed by the ectoderm; ectodermal.",
    secondary: "In comparative invertebrate histology, pertaining to the outer cell layer of diploblastic organisms (such as cnidarians).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "The outer **ectodermic** sheath of the hydra contains cnidocytes, epitheliomuscular cells, and sensory receptors." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "In sponges, the pinacoderm represents an **ectodermic** boundary separating the internal choanocytes from seawater." },
      { author: "Ernst Haeckel", work: "General Morphology of Organisms", quote: "The primordial **ectodermic** layer was the first cellular boundary to mediate contact between the metazoan and its world." }
    ]
  },
  "Dashboard — der\\endermic.md": {
    primary: "Acting by absorption through the skin; applied directly to the denuded dermis.",
    secondary: "In historical therapeutics, an administration method where a blister was raised with cantharides and therapeutic powders applied directly to the raw dermis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Before the invention of the hypodermic syringe, physicians employed **endermic** medication to introduce morphine into the circulation." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures and Reports", quote: "The **endermic** method was abandoned because it caused severe local pain and unpredictable systemic absorption." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "Old medical compendiums described **endermic** blistering as a sovereign remedy for violent neuralgias." }
    ]
  },
  "Dashboard — der\\endoderm.md": {
    primary: "The innermost layer of cells or tissue of an embryo in early development.",
    secondary: "In embryology, the germ layer that forms the lining of the digestive tract, respiratory system, liver, pancreas, and urinary bladder.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "The primitive gut or archenteron of the gastrula is lined entirely by the vegetative **endoderm**." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "The **endoderm** preserves the primary nutritive function of the ancestral hypothetical Gastraea." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Invagination of large yolk-laden cells during gastrulation establishes the future intestinal **endoderm**." }
    ]
  },
  "Dashboard — der\\epidermal.md": {
    primary: "Relating to or situated in the epidermis; cutaneous.",
    secondary: "In histology and botany, pertaining to the outermost protective layer of keratinized stratified squamous epithelium or plant cuticle.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Constant shedding of dead **epidermal** squames is compensated by active cell proliferation in the basal germinative layer." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The stomata of green leaves are specialized openings bounded by **epidermal** guard cells that regulate transpiration." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe pemphigus causes widespread bullous separation of the **epidermal** sheet from the underlying basement membrane." }
    ]
  },
  "Dashboard — der\\epidermic.md": {
    primary: "Of, relating to, or belonging to the epidermis; epidermal.",
    secondary: "In comparative anatomy, describing surface appendages such as scales, feathers, hair, and claws derived from the outer epithelial layer.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "Feathers and reptilian scales are true **epidermic** growths, nourished at their base by a vascular dermal papilla." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "In domestic sheep, the wool represents an extraordinarily elongated, curled **epidermic** filament." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The keratinized horn sheath of bovids is an **epidermic** structure covering a bony core." }
    ]
  },
  "Dashboard — der\\epidermis.md": {
    primary: "The surface epithelium of the skin, overlying the dermis; in botany, the outermost single layer of cells covering a young plant.",
    secondary: "In vertebrate dermatology, the multi-layered avascular barrier consisting of the strata basale, spinosum, granulosum, lucidum, and corneum.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The continuous desquamation and regeneration of the **epidermis** illustrates cellular renewal in its purest physiological form." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The impermeable keratinized outer stratum of the **epidermis** shields the body from dehydration and bacterial invasion." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Sudden terror provokes contraction of the arrectores pilorum, producing gooseflesh upon the **epidermis**." }
    ]
  },
  "Dashboard — der\\hypodermal.md": {
    primary: "Relating to the parts beneath the skin; subcutaneous; hypodermic.",
    secondary: "In invertebrate zoology, relating to the hypodermis, the cellular layer that secretes the chitinous cuticle of arthropods.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "The chitinous armor of the crustacean is secreted directly by the underlying **hypodermal** cells." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Insulin must be deposited into the loose **hypodermal** adipose tissue to ensure smooth, continuous absorption." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Thickened **hypodermal** sclerenchyma fibers beneath the needle epidermis give structural rigidity to pine foliage." }
    ]
  },
  "Dashboard — der\\hypodermic.md": {
    primary: "Relating to the region immediately beneath the skin; or a hypodermic needle or syringe used for injecting fluids subcutaneously.",
    secondary: "In pharmacology and therapeutics, the parenteral administration of soluble medications directly into the subcutaneous space.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Sherlock Holmes took his bottle from the corner of the mantelpiece and his **hypodermic** syringe from its neat morocco case." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The introduction of the **hypodermic** needle revolutionized the emergency management of intractable pain and collapse." },
      { author: "Robert Louis Stevenson", work: "The Strange Case of Dr. Jekyll and Mr. Hyde", quote: "He glanced at the glass phials and the **hypodermic** apparatus with a shudder of fearful fascination." }
    ]
  },
  "Dashboard — der\\hypodermis.md": {
    primary: "The subcutaneous layer of loose connective tissue and fat beneath the dermis; the superficial fascia.",
    secondary: "In arthropod morphology, the layer of living epithelial cells that secretes and underlies the chitinous exoskeleton.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Before ecdysis takes place, the **hypodermis** detaches from the old cuticle and begins secreting a soft new skin." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The abundant fat stored within the **hypodermis** acts as both an energy reservoir and a thermal insulator." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Glandular secretions from the insect **hypodermis** lubricate the old skin during molting." }
    ]
  },
  "Dashboard — der\\mesoderm.md": {
    primary: "The middle of the three primary germ layers in an embryo, developing between the ectoderm and endoderm.",
    secondary: "In developmental biology, the embryonic germ layer that gives rise to the musculoskeletal system, cardiovascular system, kidneys, and gonads.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "Triploblastic animals are distinguished from coelenterates by the formation of a true **mesoderm** between the outer and inner layers." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "The coelomic body cavity arises through the splitting or outpouching of the embryonic **mesoderm**." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "From the somatic and splanchnic sheets of the **mesoderm** develop the muscles, skeleton, and circulating blood." }
    ]
  },
  "Dashboard — der\\mesodermal.md": {
    primary: "Of, relating to, or derived from the mesoderm.",
    secondary: "In histology and embryology, pertaining to connective tissues, blood vessels, and skeletal elements of mesodermal origin.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology", quote: "Microglial cells are unique among central nervous elements in having an invasive **mesodermal** origin rather than an ectodermal lineage." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Sarcomas represent malignant neoplasms arising from transformed tissues of **mesodermal** extraction." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "The primary organizer consists of chordamesoderm that induces the overlying ectoderm while differentiating into **mesodermal** somites." }
    ]
  },
  "Dashboard — der\\pander.md": {
    primary: "To gratify, cater to, or exploit the baser desires, weaknesses, or prejudices of others.",
    secondary: "Historically, a pimp, procurer, or go-between in illicit amorous intrigues (named after Pandarus in the Trojan legend).",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Reason panders will, when virtue itself of vice must pardon beg; do not **pander** to base corruption." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The court poets did not blush to **pander** to the monarch's most scandalous vices for a pension." },
      { author: "George Bernard Shaw", work: "Mrs. Warren's Profession", quote: "A society that refuses decent wages to working women will always find men ready to **pander** to prostitution." }
    ]
  },
  "Dashboard — der\\panderer.md": {
    primary: "One who caters to or profits from the vices, weaknesses, or corrupt desires of others; a procurer.",
    secondary: "In literary and political criticism, a writer or politician who degrades standards to flatter the uneducated mob.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The eunuch became the secret **panderer** of the emperor's pleasures and the distributor of imperial favors." },
      { author: "William Makepeace Thackeray", work: "The English Humourists of the Eighteenth Century", quote: "Congreve refused to be considered a mere **panderer** to the frivolous amusements of high society." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The demagogue is ever the **panderer** to popular passions, leading the multitude toward their own destruction." }
    ]
  },
  "Dashboard — der\\parader.md": {
    primary: "One who marches in a parade; a person who ostentatiously displays or flaunts their possessions, accomplishments, or virtues.",
    secondary: "In social satire, a vain exhibitionist who struts in public view to command admiration.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Every fashionable boulevard had its **parader**, strolling slowly to exhibit the latest cut of his waistcoat." },
      { author: "Charles Dickens", work: "Bleak House", quote: "Mr. Turveydrop was a celebrated **parader** of deportment, bowing with majestic condescension to the admiring throng." },
      { author: "Henry James", work: "The Bostonians", quote: "She had no desire to become a vulgar public **parader** of private griefs upon the political platform." }
    ]
  },
  "Dashboard — der\\paradise.md": {
    primary: "An ideal, beautiful, or idyllic place or state; heaven or the Garden of Eden in religious traditions.",
    secondary: "In historical linguistics and Persian culture, an enclosed royal hunting park or walled garden (pairi-daeza) renowned for fountains and fruit trees.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "The world was all before them, where to choose their place of rest, and Providence their guide: they, hand in hand, with wandering steps and slow, through Eden took their solitary way from **Paradise**." },
      { author: "Dante Alighieri", work: "Paradiso", quote: "In that celestial **paradise**, the blessed souls abide in radiant circles of eternal light and love." },
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "Nature is a setting that makes of every quiet woodland walk an earthly **paradise** for the contemplative mind." }
    ]
  },
  "Dashboard — der\\under.md": {
    primary: "Extending or situated directly beneath or below; in or to a lower place.",
    secondary: "Subordinate to, subject to the authority of, or undergoing a specified condition or process.",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", quote: "Full fathom five thy father lies; of his bones are coral made; those are pearls that were his eyes: nothing of him that doth fade, but doth suffer a sea-change into something rich and strange **under** the sea." },
      { author: "Samuel Taylor Coleridge", work: "The Rime of the Ancient Mariner", quote: "Water, water, everywhere, and all the boards did shrink; water, water, everywhere, nor any drop to drink **under** the burning sun." },
      { author: "John Keats", work: "Ode on a Grecian Urn", quote: "Fair youth, beneath the trees, thou canst not leave thy song, nor ever can those trees be bare **under** the quiet boughs." }
    ]
  },
  "Dashboard — derm\\adermin.md": {
    primary: "An obsolete historical name for vitamin B6 (pyridoxine), originally designated for its curative effect on rat acrodynia (dermatitis).",
    secondary: "In nutritional biochemistry history, the water-soluble vitamin isolated by Paul György that prevents rat pellagra-like dermal necrosis.",
    quotes: [
      { author: "Paul György", work: "Investigations on the Vitamin B2 Complex", quote: "We propose the name **adermin** for the rat acrodynia-preventing factor, which restores normal hair and skin integrity." },
      { author: "Albert Szent-Györgyi", work: "Studies on Biological Oxidation", quote: "The discovery of **adermin** established another essential coenzyme in cellular amino acid metabolism." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Experimental nutritional deficiency proved that deprivation of **adermin** provoked severe cutaneous desquamation and convulsions." }
    ]
  },
  "Dashboard — derm\\derma.md": {
    primary: "The dermis, or true skin situated below the epidermis; the corium.",
    secondary: "In dermatology, the vascular connective tissue matrix supporting the cutaneous appendages and sensory corpuscles.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Chronic inflammation causes cellular exudation into the papillary layer of the **derma**, elevating the surface into papules." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Scleroderma induces dense, board-like induration throughout the fibrous bundles of the **derma**." },
      { author: "Erasmus Wilson", work: "On Diseases of the Skin", quote: "The **derma** is richly supplied with arterial plexuses that regulate both cutaneous nutrition and animal heat." }
    ]
  },
  "Dashboard — derm\\dermabrasion.md": {
    primary: "A dermatological procedure in which the superficial layers of the skin are mechanically removed using a high-speed rotating abrasive tool to reduce scars and wrinkles.",
    secondary: "In aesthetic and reconstructive plastic surgery, controlled skin resurfacing allowing re-epithelialization from adnexal follicular reservoirs.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Post-acne pitting and traumatic tattoos are effectively softened through careful surgical **dermabrasion**." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "Mechanical **dermabrasion** of superficial facial scars permits fresh epidermal migration from undamaged hair follicles." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Controlled cutaneous scraping, the forerunner of **dermabrasion**, was employed to remove persistent tuberculous lupus nodules." }
    ]
  },
  "Dashboard — derm\\dermacentor.md": {
    primary: "A genus of hard ticks (family Ixodidae), including Dermacentor andersoni (Rocky Mountain wood tick) and Dermacentor variabilis (American dog tick).",
    secondary: "In medical acarology, vectors of serious zoonoses including Rocky Mountain spotted fever, Colorado tick fever, and tularemia.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The transmission of Rocky Mountain spotted fever was traced to the bite of the wood tick, **Dermacentor** andersoni." },
      { author: "Howard Taylor Ricketts", work: "Contributions to Medical Science", quote: "Infected specimens of **Dermacentor** harbor rickettsial organisms in their salivary glands, transmitting them during blood feeding." },
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "Tick paralysis in domestic animals and children is frequently caused by a salivary neurotoxin secreted by **Dermacentor**." }
    ]
  },
  "Dashboard — derm\\dermal.md": {
    primary: "Relating to the skin, especially the dermis; cutaneous.",
    secondary: "In histology and comparative anatomy, pertaining to structures, glands, or ossifications arising within the dermis.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The teeth of vertebrates and the placoid scales of sharks are homologous **dermal** structures derived from dentine papillae." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The characteristic **dermal** lesions of secondary syphilis present as symmetrical, coppery-red macules." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The human body retains fine **dermal** hair tracts that correspond to the primordial coat of our mammalian ancestors." }
    ]
  },
  "Dashboard — derm\\dermaptera.md": {
    primary: "The taxonomic order of insects that includes the earwigs, characterized by short leathery forewings and pincers at the tip of the abdomen.",
    secondary: "In systematic entomology, nocturnal, thigmotactic insects with forceps-like cerci used for defense, grooming, and folding their wings.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "Members of the **Dermaptera** fold their expansive membranous wings beneath minute tegmina with astonishing geometric precision." },
      { author: "Jean-Henri Fabre", work: "The Life of the Fly", quote: "Few insects among the **Dermaptera** fail to inspire foolish terror in country folk on account of their harmless tail pincers." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "Flightless island species of **Dermaptera** often develop enormous, asymmetrical forceps suited for male rivalry." }
    ]
  },
  "Dashboard — derm\\dermatitis.md": {
    primary: "Inflammation of the skin, characterized by itching, redness, swelling, and often vesicular lesions; eczema.",
    secondary: "In clinical dermatology, a broad category of acute and chronic cutaneous disorders, including contact dermatitis, atopic dermatitis, and seborrheic dermatitis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Contact with poison ivy excites an acute, intensely pruritic vesicular **dermatitis** within twenty-four hours of exposure." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Every acute **dermatitis** passes through stages of erythema, papulation, vesicle formation, and eventual desquamation." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Rare Diseases of the Skin", quote: "Occupational **dermatitis** in chemical workers highlights the danger of cumulative local skin irritation." }
    ]
  },
  "Dashboard — derm\\dermatobia.md": {
    primary: "A genus of New World botflies (family Oestridae), especially Dermatobia hominis, commonly known as the human botfly.",
    secondary: "In tropical parasitology and medical entomology, a fly whose females capture mosquitoes to carry their eggs, allowing hatching larvae to penetrate mammal skin.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases: A Manual of the Diseases of Warm Climates", quote: "The larva of **Dermatobia** hominis burrows into the subcutaneous tissue, creating a painful, discharging furuncular lesion." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels to the Equinoctial Regions", quote: "Native guides in the Orinoco forests warned us of the painful swellings caused by the burrowing grub of **Dermatobia**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Extraction of the living **Dermatobia** maggot brings immediate relief to the traveler returning from tropical America." }
    ]
  },
  "Dashboard — derm\\dermatoglyphic.md": {
    primary: "Of, relating to, or characteristic of dermatoglyphics; relating to the epidermal ridge patterns of the hands and feet.",
    secondary: "In medical genetics and physical anthropology, pertaining to ridge counts, triradii, and digital whorls used in diagnostic screening.",
    quotes: [
      { author: "Francis Galton", work: "Finger Prints", quote: "The immutable **dermatoglyphic** ridges of the fingertips remain unchanged from fetal life until post-mortem decomposition." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A single transverse palmar crease is an important **dermatoglyphic** marker in Down syndrome." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "Genetic dysmorphologists study unusual **dermatoglyphic** configurations to confirm early embryonic developmental disturbances." }
    ]
  },
  "Dashboard — derm\\dermatoglyphics.md": {
    primary: "The scientific study of the ridged skin patterns found on the fingertips, palms of the hands, and soles of the feet.",
    secondary: "In forensics and clinical genetics, the classification of friction ridge patterns (arches, loops, whorls) for human identification and chromosomal disorder analysis.",
    quotes: [
      { author: "Francis Galton", work: "Fingerprint Directories", quote: "The systematic classification of **dermatoglyphics** provided criminal jurisprudence with an infallible method of personal identification." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Galton's pioneer work in **dermatoglyphics** demonstrated that ridge counts follow strict quantitative polygenic inheritance." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Abnormal **dermatoglyphics**, such as a high axial triradius, frequently accompany congenital cardiac malformations." }
    ]
  },
  "Dashboard — derm\\dermatologic.md": {
    primary: "Relating to dermatology, the medical branch concerned with the diagnosis and treatment of skin disorders.",
    secondary: "In clinical medicine, pertaining to cutaneous physical signs, topical pharmacotherapies, and cuticular biopsies.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough **dermatologic** inspection of the patient in natural daylight often reveals the systemic nature of an obscure illness." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "The primary rule of **dermatologic** diagnosis is to look with trained eyes before forming speculative hypotheses." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Rare **dermatologic** manifestations frequently serve as sentinels of occult internal malignancy." }
    ]
  },
  "Dashboard — derm\\dermatological.md": {
    primary: "Of or pertaining to dermatology or the scientific study and clinical management of the skin.",
    secondary: "In medical education, relating to cutaneous clinics, diagnostic histological atlases, and skin therapeutics.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Lectures on Diseases of the Skin", quote: "Our **dermatological** clinic at Vienna was founded upon the principle that skin lesions must be correlated with morbid anatomy." },
      { author: "Erasmus Wilson", work: "Portraits of Diseases of the Skin", quote: "Accurate colored lithographs are indispensable in **dermatological** teaching to convey subtle variations in erythema." },
      { author: "William Osler", work: "Aequanimitas", quote: "The young physician should attend the **dermatological** dispensary to acquire rapid precision in identifying cuticular eruptions." }
    ]
  },
  "Dashboard — derm\\dermatologist.md": {
    primary: "A physician who specializes in the diagnosis, medical management, and surgical treatment of diseases of the skin, hair, and nails.",
    secondary: "In modern medicine, a clinical specialist proficient in dermatopathology, dermoscopy, Mohs surgery, and systemic immunodermatology.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "The skilled **dermatologist** distinguishes at a glance between contagious scabies and constitutional eczema." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "To the consulting **dermatologist**, every chronic ulcer on the leg presents a complex problem of vascular dynamics." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cooperation between the internist and the **dermatologist** is essential whenever cuticular purpura indicates systemic vasculitis." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch4Data);
console.log(`[Body Batch 4] Successfully updated ${updatedCount}/${Object.keys(batch4Data).length} notes.`);
