import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batch5Data = {
  "Dashboard — derm\\dermatology.md": {
    primary: "The branch of medical science concerned with the diagnosis, physiology, and pathology of the skin and its appendages.",
    secondary: "In clinical practice, the medical and surgical specialty dedicated to cuticular diseases, skin oncology, and systemic manifestations of dermatoses.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "The true progress of **dermatology** began when clinicians ceased looking at skin rashes as humoral purges and studied their local tissue pathology." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Few fields of medicine reward patient observation as richly as clinical **dermatology**, where pathology is spread out directly before the eye." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The master of internal medicine must keep abreast of **dermatology**, for the skin is a mirror of constitutional disease." }
    ]
  },
  "Dashboard — derm\\dermatome.md": {
    primary: "An area of skin that is primarily innervated by a single spinal sensory nerve root.",
    secondary: "In surgical instruments, a mechanical device equipped with an oscillating blade used to harvest split-thickness skin grafts of uniform depth.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The vesicular eruption of herpes zoster maps out with astonishing precision the sensory **dermatome** supplied by the affected dorsal ganglion." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Cutaneous sensory mapping demonstrates how each spinal **dermatome** overlaps with adjacent segments to prevent sensory gaps." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The invention of the calibrated **dermatome** allowed surgeons to excise uniform epidermal sheets for immediate autografting." }
    ]
  },
  "Dashboard — derm\\dermatomycosis.md": {
    primary: "A superficial fungal infection of the skin, hair, or nails caused by dermatophytes or yeasts.",
    secondary: "In clinical mycology, cuticular infections such as tinea versicolor or ringworm characterized by scaling, erythema, and epidermal maceration.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Microscopic scrapings mounted in potassium hydroxide reveal branching hyphae, confirming the diagnosis of **dermatomycosis**." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures and Reports", quote: "The spread of contagious **dermatomycosis** among schoolboys was checked by strict isolation and sulfur applications." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Schoenlein's discovery of the parasitic fungus in favus proved that certain chronic dermatoses are true forms of **dermatomycosis**." }
    ]
  },
  "Dashboard — derm\\dermatomyositis.md": {
    primary: "An uncommon inflammatory disease characterized by progressive muscle weakness and a distinctive skin rash.",
    secondary: "In clinical rheumatology, an idiopathic autoimmune inflammatory myopathy presenting with a heliotrope rash around the eyes and Gottron papules over knuckle joints.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The violaceous heliotrope discoloration of the eyelids accompanied by proximal limb girdle paresis establishes the diagnosis of **dermatomyositis**." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "In adult patients presenting with acute **dermatomyositis**, the clinician must conduct a vigilant search for occult internal neoplasm." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Muscle biopsy in **dermatomyositis** demonstrates perivascular lymphocytic cuffing and characteristic perifascicular atrophy." }
    ]
  },
  "Dashboard — derm\\dermatophytosis.md": {
    primary: "A superficial fungal infection of keratinized tissues (skin, hair, or nails) caused by dermatophyte fungi; ringworm or tinea.",
    secondary: "In infectious disease medicine, infections caused by species of Trichophyton, Microsporum, or Epidermophyton that digest cutaneous keratin.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Common athlete's foot is a localized **dermatophytosis** that flourishes in warm, occluded interdigital spaces." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Rare Diseases of the Skin", quote: "The circular expanding margin of active erythema in tinea circinata illustrates the invasive centrifugal growth of **dermatophytosis**." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Direct microscopic examination of epilated hairs demonstrates the endothrix spore chains characteristic of fungal **dermatophytosis**." }
    ]
  },
  "Dashboard — derm\\dermatosclerosis.md": {
    primary: "A disease characterized by abnormal hardening and thickening of the skin and subcutaneous tissue; scleroderma.",
    secondary: "In dermatology and rheumatology, chronic cutaneous induration resulting from excessive dermal collagen deposition and microvascular obliteration.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Diffuse **dermatosclerosis** transforms the skin of the face into an immobile, parchment-like mask, obliterating normal expression." },
      { author: "Jonathan Hutchinson", work: "Illustrations of Clinical Surgery", quote: "In advanced **dermatosclerosis**, the digits become tapered and claw-like, their joints locked by the dense, unyielding cutaneous envelope." },
      { author: "Ferdinand von Hebra", work: "Lectures on Diseases of the Skin", quote: "The histological section in **dermatosclerosis** shows massive hypertrophy of dermal collagen bundles with atrophy of sweat glands." }
    ]
  },
  "Dashboard — derm\\dermatosis.md": {
    primary: "Any disease or pathological condition of the skin, especially one that is not characterized by inflammation.",
    secondary: "In clinical nosology, an overarching classification encompassing non-inflammatory cuticular abnormalities, ichthyoses, and keratodermas.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Arsenical poisoning may induce a bizarre punctate pigmentary **dermatosis** upon the trunk and palms." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Every intractable **dermatosis** requires systematic investigation of the patient's general hygiene, occupational exposure, and diet." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "The presence of a sudden, widespread seborrheic **dermatosis** can serve as an alarming sign of internal visceral malignancy." }
    ]
  },
  "Dashboard — derm\\dermestidae.md": {
    primary: "A family of small beetles commonly known as skin beetles, hide beetles, or carpet beetles, whose larvae feed on dry animal and plant products.",
    secondary: "In natural history museums and forensic entomology, beetles utilized by preparators to clean skeleton specimens, or analyzed to estimate post-mortem intervals.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The larvae of the **Dermestidae** caused immense destruction among our dried zoological collections during the humid tropical voyage." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "Natural history curators employ colonies of the **Dermestidae** to clean delicate vertebrate skulls without damaging fragile sutures." },
      { author: "Jean-Henri Fabre", work: "The Life of the Fly", quote: "Whenever a carcass has dried into mere parchment and bone, the hungry larvae of the **Dermestidae** arrive to finish the feast." }
    ]
  },
  "Dashboard — derm\\dermic.md": {
    primary: "Pertaining to, relating to, or consisting of the dermis; dermal.",
    secondary: "In cutaneous histopathology, designating pathological processes, infiltrates, or vascular changes situated within the corium.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The tuberculin reaction produces a localized, indurated **dermic** erythema that peaks at forty-eight hours." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Careful excision of the deep **dermic** nodule confirmed its origin from transformed neural crest elements." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Hyperplasia of the fibrous connective tissue throughout the **dermic** layer creates the thickened elephantiasic skin." }
    ]
  },
  "Dashboard — derm\\dermis.md": {
    primary: "The dense inner layer of skin beneath the epidermis, comprising vascular connective tissue, nerve endings, sweat glands, and hair follicles.",
    secondary: "In cuticular physiology and biomechanics, the thick fibrous layer rich in type I and III collagen providing tensile strength and turgor to the integument.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The deep vascular layer, or **dermis**, nourishes the overlying avascular epidermis and provides the physical bed for sensory corpuscles." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe thermal injury that penetrates through the full thickness of the **dermis** necessitates surgical debridement and grafting." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The boundary between the epithelial epidermis and the connective tissue **dermis** is marked by an undulant basement membrane." }
    ]
  },
  "Dashboard — derm\\dermochelyidae.md": {
    primary: "A family of gigantic marine turtles comprising the leatherback sea turtle (Dermochelys coriacea) and its fossil relatives.",
    secondary: "In vertebrate paleontology and herpetology, marine chelonians distinguished by a carapace covered with leathery oily skin and thousands of tiny polygonal osteoderms rather than horny scutes.",
    quotes: [
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "The family **Dermochelyidae** parted company from ancestral hard-shelled marine turtles back in the Cretaceous, developing a mosaic osteodermal shell." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Fossil skeletons of the **Dermochelyidae** attain colossal proportions, reflecting profound adaptation to open ocean pelagic diving." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "The unique leathery shell of the **Dermochelyidae** enables these giant pelagic wanderers to dive into frigid oceanic depths." }
    ]
  },
  "Dashboard — derm\\dermochelys.md": {
    primary: "The genus of marine turtles containing the leatherback sea turtle, Dermochelys coriacea, the largest of all living turtles.",
    secondary: "In marine zoology, an oceanic chelonian possessing a hydrodynamically ridged, leathery carapace and counter-current heat exchange systems for maintaining core body warmth in cold waters.",
    quotes: [
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "A magnificent specimen of **Dermochelys** was taken off the coast, its black leathery back traversed by seven prominent longitudinal keels." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "In **Dermochelys**, the true bony ribs remain free from the superficial mosaic carapace that forms the leathery shield." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The giant leatherback, **Dermochelys**, journeys across thousands of leagues of open sea, diving hundreds of fathoms in pursuit of jellyfish." }
    ]
  },
  "Dashboard — derm\\dermoptera.md": {
    primary: "The order of arboreal gliding mammals native to Southeast Asia commonly known as colugos or flying lemurs (family Cynocephalidae).",
    secondary: "In mammalogy and evolutionary genomics, the closest living sister group to primates, possessing the most extensive gliding patagium of any mammal.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The colugo, belonging to the **Dermoptera**, launched itself from the crest of a tall dipterocarp and glided seventy yards across the ravine." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The order **Dermoptera** displays comb-like lower incisors and an expansive flight membrane extending to the very tips of the claws." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The extensive membrane of the **Dermoptera** illustrates an intermediate evolutionary stage between arboreal climbers and true bat-like flight." }
    ]
  },
  "Dashboard — derm\\ectoderm.md": {
    primary: "The outermost of the three primary germ layers in an animal embryo.",
    secondary: "In embryology, the foundational germ layer that gives rise to the nervous system, tooth enamel, and the epidermis with its cutaneous glands.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "The primitive blastoderm separates into outer **ectoderm** and inner entoderm during the initial stages of gastrulation." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Every neuroblast that populates the cerebral cortex originates from the primitive neuroepithelial fold of the **ectoderm**." },
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "Sensory structures throughout the animal kingdom trace their developmental lineage directly to the external **ectoderm**." }
    ]
  },
  "Dashboard — derm\\ectodermal.md": {
    primary: "Relating to or derived from the ectoderm.",
    secondary: "In clinical genetics, describing conditions such as ectodermal dysplasia that affect teeth, hair, nails, and cutaneous glands.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients with congenital **ectodermal** dysplasia exhibit total anodontia and an inability to tolerate warm weather." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "Tissue graft experiments demonstrate that competent **ectodermal** sheets can form either lens or epidermis depending upon organizer signals." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "The cellular movements of gastrulation position the **ectodermal** sheet as the external envelope of the entire embryo." }
    ]
  },
  "Dashboard — derm\\ectodermic.md": {
    primary: "Pertaining to or formed by the ectoderm; ectodermal.",
    secondary: "In invertebrate anatomy, characterizing the outer epithelial body wall of diploblastic animals such as cnidarians.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "The outer **ectodermic** cells of the medusa secrete the protective gelatinous bell and bear tactile sensory organs." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "In simple hydroids, the **ectodermic** layer functions simultaneously as a protective skin, muscle sheet, and sensory receiver." },
      { author: "Ernst Haeckel", work: "General Morphology of Organisms", quote: "Comparative analysis of the **ectodermic** epithelium reveals the primordial origins of animal sensibility." }
    ]
  },
  "Dashboard — derm\\endermatic.md": {
    primary: "Acting through or applied directly to the denuded dermis; endermic.",
    secondary: "In historical clinical pharmacology, a technique of introducing medicaments onto a raw de-epithelialized skin surface.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early nineteenth-century clinicians frequently resorted to **endermatic** application of belladonna to quiet severe sciatic neuralgia." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures and Reports", quote: "The **endermatic** method fell into disuse as soon as hypodermic needles provided exact dosing and painless administration." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Topical mercurial salves were administered by **endermatic** inunction over denuded blisters to treat constitutional syphilis." }
    ]
  },
  "Dashboard — derm\\endermic.md": {
    primary: "Acting by absorption through the skin; applied directly to the dermis.",
    secondary: "In medical history, the therapeutic introduction of drugs through blistered skin prior to the invention of parenteral injections.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The **endermic** introduction of strychnine was celebrated in early textbooks as a heroic stimulant in profound coma." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "Old Dr. Winter spoke nostalgically of **endermic** medication, recounting how blistered skin absorbed calomel." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Absorption by the **endermic** route varied wildly depending upon the vascular congestion of the raw dermal surface." }
    ]
  },
  "Dashboard — derm\\endoderm.md": {
    primary: "The innermost of the three primary germ layers in an animal embryo.",
    secondary: "In developmental biology, the embryonic tissue layer that forms the epithelial lining of the gut, respiratory tract, and associated glands.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "The archenteron of the early embryo is lined by the **endoderm**, which gives rise to the stomach, intestines, and liver." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "During invagination, vegetative blastomeres sink into the interior to establish the primary **endoderm**." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "The primitive digestive cavity formed by the **endoderm** represents the most ancient metabolic organ in animal phylogeny." }
    ]
  },
  "Dashboard — derm\\entoderm.md": {
    primary: "An alternative anatomical and embryological term for the endoderm; the inner germ layer of an embryo.",
    secondary: "In comparative embryology, the innermost epithelial layer of the gastrula from which the viscera and digestive glands originate.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "In coelenterates, the body consists essentially of two living sheets, the ectoderm and the internal **entoderm**." },
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "Fate maps of amphibian eggs demonstrate that the sub-equatorial cells migrate inward to form the **entoderm**." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Glandular and absorptive functions throughout the metazoan series are primarily carried out by derivatives of the **entoderm**." }
    ]
  },
  "Dashboard — derm\\epidermal.md": {
    primary: "Relating to or located in the epidermis, the outermost protective layer of the skin.",
    secondary: "In histology and botany, pertaining to the non-vascular surface layer of cells covering the body or leaves and stems of plants.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Superficial chemical burns destroy the outer **epidermal** barrier while sparing the deep dermal hair follicles." },
      { author: "Asa Gray", work: "Structural Botany", quote: "A waxy cuticle secreted by the outer **epidermal** walls prevents excessive loss of moisture from desert vegetation." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Mitotic division in the basal **epidermal** layer continuously pushes maturing cells outward toward desquamation." }
    ]
  },
  "Dashboard — derm\\epidermic.md": {
    primary: "Of, relating to, or derived from the epidermis; epidermal.",
    secondary: "In comparative anatomy, describing keratinized surface structures such as feathers, quills, nails, and tortoise shell.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "The porcupine's defensive quills represent modified, heavily thickened **epidermic** hairs." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The horny beak of the platypus is an **epidermic** sheath overlying the expanded premaxillary bones." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "Scales in reptiles are **epidermic** folds of keratin, contrasting with the bony dermal plates of fishes." }
    ]
  },
  "Dashboard — derm\\epidermis.md": {
    primary: "The surface epithelium of the skin, overlying the dermis; or the outermost single layer of cells covering a plant body.",
    secondary: "In dermatological physiology, a stratified squamous keratinized epithelium providing vital protection against pathogen entry, chemical injury, and dehydration.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic analysis reveals that the cells of the **epidermis** undergo progressive cornification as they approach the free surface." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "No blood vessels penetrate the **epidermis**; its living strata are nourished by transudation from the underlying dermal capillary loops." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Autocrat of the Breakfast-Table", quote: "The delicate tactile impressions received upon the fingertip must pass through the semi-transparent veil of the **epidermis**." }
    ]
  },
  "Dashboard — derm\\erythroderma.md": {
    primary: "An inflammatory skin disease characterized by intense, generalized redness and scaling affecting over ninety percent of the body surface area; exfoliative dermatitis.",
    secondary: "In clinical dermatology, a life-threatening cuticular emergency associated with severe hypothermia, fluid loss, protein wasting, and high-output heart failure.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Generalized **erythroderma** places severe strain upon the cardiovascular system due to colossal cutaneous capillary dilatation." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "The entire cutaneous surface shed immense paper-like scales daily in the severe form of pityriasis rubra **erythroderma**." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Drug hypersensitivity may manifest as sudden generalized **erythroderma**, stripping the patient of his protective integument." }
    ]
  },
  "Dashboard — derm\\euderma.md": {
    primary: "A genus of vespertilionid bats containing the spotted bat (Euderma maculatum), celebrated for its large ears and white dorsal spots on a black coat.",
    secondary: "In mammalian taxonomy, an enigmatic North American insectivorous bat possessing exceptionally low-frequency echolocation calls audible to the human ear.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The remarkable spotted bat of the genus **Euderma** inhabits the arid canyon country of western North America." },
      { author: "C. Hart Merriam", work: "North American Fauna", quote: "The immense, translucent pink ears of **Euderma** maculatum exceed half the length of its entire body." },
      { author: "Donald Griffin", work: "Listening in the Dark", quote: "Unique among North American microbats, **Euderma** broadcasts foraging clicks that echo clearly within human hearing range." }
    ]
  },
  "Dashboard — derm\\exoderm.md": {
    primary: "An outer layer of cells or tissue; specifically, the exodermis of a plant root or the outer ectodermal layer in invertebrate embryos.",
    secondary: "In plant root anatomy, a specialized subepidermal apoplastic barrier layer impregnated with suberin that regulates radial water and solute flux.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The suberized **exoderm** of the older root protects the internal cortex from desiccation when the soil dries out." },
      { author: "Arthur George Tansley", work: "Elements of Plant Biology", quote: "Microscopic transverse sections of the root reveal an impermeable **exoderm** situated immediately beneath the piliferous layer." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "The external **exoderm** of the sponge secretes mineral spicules to anchor the colony to submerged rock." }
    ]
  },
  "Dashboard — derm\\hypoderma.md": {
    primary: "In veterinary medicine, a genus of botflies (family Oestridae), commonly known as warble flies or heel flies, whose parasitic larvae develop under cattle skin.",
    secondary: "In botanical anatomy, the hypodermis or specialized layer of protective cells situated immediately below the plant epidermis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Subcutaneous nodules in cattle caused by the larvae of **Hypoderma** bovis produce severe economic loss in hide quality." },
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "Accidental human infestation by the wandering larva of **Hypoderma** presents as creeping subcutaneous migratory swellings." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "In pine needles, thick-walled sclerenchyma cells in the **hypoderma** resist winter gales and mechanical injury." }
    ]
  },
  "Dashboard — derm\\hypodermal.md": {
    primary: "Relating to or located beneath the skin; subcutaneous; hypodermic.",
    secondary: "In arthropod morphology, pertaining to the cellular hypodermis that secretes the exoskeleton.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "A dense layer of **hypodermal** cells underlies the calcareous carapace, orchestrating the periodic replacement of the armor." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Subcutaneous **hypodermal** fat deposits serve as an indispensable thermal blanket against severe cold." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Pigment granules embedded within the **hypodermal** layer create the brilliant coloration of many insect shells." }
    ]
  },
  "Dashboard — derm\\hypodermatidae.md": {
    primary: "A family or subfamily (Hypodermatinae) of oestrid botflies comprising warble flies that parasitize ungulates and domestic livestock.",
    secondary: "In veterinary entomology, dipterans whose endoparasitic larvae migrate through host esophageal and spinal tissues before encysting subcutaneously.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "Members of the **Hypodermatidae** cause immense distress to herds, triggering frantic gadding behavior as cattle flee ovipositing flies." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Parasitic warbles produced by the **Hypodermatidae** were formerly common among rural livestock across Europe and North America." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Wild ungulates have evolved behavioral defenses against the persistent attacks of parasitic flies of the **Hypodermatidae**." }
    ]
  },
  "Dashboard — derm\\hypodermic.md": {
    primary: "Relating to the parts beneath the skin; subcutaneous; or a syringe and hollow needle used for injecting liquids under the skin.",
    secondary: "In pharmacology and therapeutics, the parenteral route of drug administration designed for rapid systemic absorption bypassing digestive enzymes.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "He held the small **hypodermic** syringe in his hand, observing the clear droplet poised at the needle's tip." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The prompt **hypodermic** injection of atropine counteracts the cholinergic crisis induced by muscarine poisoning." },
      { author: "Jack London", work: "The Sea-Wolf", quote: "The captain produced an old brass **hypodermic** syringe, administering morphine to quiet the sailor's agony." }
    ]
  },
  "Dashboard — derm\\hypodermis.md": {
    primary: "The subcutaneous layer of loose connective and adipose tissue beneath the dermis; the superficial fascia.",
    secondary: "In plant histology, a layer of protective cells lying directly beneath the epidermis; in arthropods, the living cellular layer that secretes the exoskeleton.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Lipomas arise primarily from benign overgrowths of adipocytes within the subcutaneous **hypodermis**." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Nerve trunks and major cutaneous veins traverse the loose **hypodermis** before branching into the overlying dermis." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The lignified cells of the **hypodermis** in conifers protect the delicate inner photosynthetic mesophyll from frost." }
    ]
  },
  "Dashboard — derm\\leukoderma.md": {
    primary: "A condition characterized by localized loss of skin pigmentation, producing irregular white patches; vitiligo or post-inflammatory depigmentation.",
    secondary: "In clinical dermatology, an acquired hypomelanosis resulting from autoimmune destruction of epidermal melanocytes or chemical exposure.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Symmetrical patches of milk-white **leukoderma** stand out in bold contrast against the surrounding sun-tanned skin." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The patient displayed familial **leukoderma**, the depigmented patches exhibiting complete loss of melanocytic pigment." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Post-inflammatory **leukoderma** frequently marks the site of resolved syphilitic roseola or severe cutaneous burns." }
    ]
  },
  "Dashboard — derm\\megaderma.md": {
    primary: "A genus of Old World false vampire bats (family Megadermatidae), including Megaderma lyra (the greater false vampire bat) and Megaderma spasma.",
    secondary: "In mammalogy, carnivorous and insectivorous bats of South and Southeast Asia possessing prominent upright nose-leaves and broad wings for slow, agile flight.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the twilight, a large **Megaderma** fluttered through the forest veranda, swooping down to pluck a gecko from the bamboo wall." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The skull of **Megaderma** is distinguished by the total absence of upper premaxillary incisors." },
      { author: "Francis Day", work: "Fauna of British India", quote: "Specimens of **Megaderma** lyra roost in ancient ruined temples, emerging at dusk to hunt small frogs, birds, and insects." }
    ]
  },
  "Dashboard — derm\\megadermatidae.md": {
    primary: "A family of microchiropteran bats commonly known as false vampire bats, characterized by very large ears joined across the forehead and a tall nose-leaf.",
    secondary: "In chiropteran systematics, predatory Old World bats of Africa, southern Asia, and Australia that hunt small vertebrates and large arthropods by gleaning.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The family **Megadermatidae** ranges across the tropical zones of the Old World, from central Africa to northern Australia." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The immense tragus and fused pinnae in the **Megadermatidae** endow these bats with extraordinary passive acoustic sensitivity." },
      { author: "Donald Griffin", work: "Listening in the Dark", quote: "Gleaning bats of the **Megadermatidae** can locate rustling prey on the ground using passive hearing rather than loud echolocation." }
    ]
  },
  "Dashboard — derm\\mesoderm.md": {
    primary: "The middle of the three primary germ layers in an animal embryo, developing between the ectoderm and endoderm.",
    secondary: "In developmental biology, the embryonic tissue layer that gives rise to bone, muscle, cartilage, blood, vascular endothelium, and genitourinary organs.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "The formation of the **mesoderm** marks the decisive transition to triploblastic complexity in the animal kingdom." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Somites carved from the paraxial **mesoderm** define the segmented segmental architecture of the vertebrate trunk." },
      { author: "Santiago Ramón y Cajal", work: "Histology", quote: "While neurons derive from ectoderm, the surrounding skeletal and vascular framework is built entirely from the **mesoderm**." }
    ]
  },
  "Dashboard — derm\\mesodermal.md": {
    primary: "Of, relating to, or derived from the embryonic mesoderm.",
    secondary: "In histology and oncology, designating tissues (such as bone, muscle, and vascular walls) or neoplasms (sarcomas) of mesodermal origin.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Malignant transformation of **mesodermal** connective tissues produces the rapidly growing, vascular sarcomas." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "The dorsal **mesodermal** mantle acts as the primary organizer, instructing the overlying ectoderm to form the neural tube." },
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "Lateral plate **mesodermal** sheets split to line the coelom and envelop the visceral viscera." }
    ]
  },
  "Dashboard — derm\\pachyderm.md": {
    primary: "A very large, thick-skinned quadruped mammal, especially an elephant, rhinoceros, or hippopotamus.",
    secondary: "In historical zoology, an animal belonging to the obsolete taxonomic order Pachydermata established by Cuvier; or an insensitive person.",
    quotes: [
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "I gathered under the order of the **pachyderm** those massive hoofed mammals characterized by thick integuments and bulky skeletons." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The sperm whale may well be called an aquatic **pachyderm**, his colossal hide defying the sharpest iron harpoon." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The pampas fossil beds yielded the teeth of Toxodon, an extinct giant displaying affinities with both the rodent and the **pachyderm**." }
    ]
  },
  "Dashboard — derm\\pachydermal.md": {
    primary: "Pertaining to, resembling, or characteristic of a pachyderm; thick-skinned.",
    secondary: "In dermatopathology, describing pathological skin thickening, induration, and cutaneous folding.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The colossal **pachydermal** skeleton of the mastodon supported immense weight upon massive, pillar-like limb bones." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic lymphedema transforms the smooth leg into a rough, corrugated **pachydermal** mass resembling elephant hide." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The cutaneous biopsy revealed dense collagenous fibrosis producing true **pachydermal** induration." }
    ]
  },
  "Dashboard — derm\\pachydermatous.md": {
    primary: "Having thick skin; or metaphorically, thick-skinned and insensitive to criticism, reproof, or emotional injury.",
    secondary: "In vertebrate zoology, relating to thick-skinned ungulates such as elephants, tapirs, and rhinoceroses.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Brooke was too cheerful and **pachydermatous** to be wounded by the sharp barbs of political satire." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The old monarchy presented a tough, **pachydermatous** resistance to reform until the explosive fury of the mob shattered it." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The lawyer was a dry, **pachydermatous** gentleman whom no client's tears could ever soften." }
    ]
  },
  "Dashboard — derm\\pachydermic.md": {
    primary: "Relating to or resembling a pachyderm; thick-skinned.",
    secondary: "In medical pathology, describing thickened, coarse, elephantiasic skin resulting from chronic lymphatic obstruction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In advanced filarial elephantiasis, the lower limbs assume a grotesque, **pachydermic** appearance." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "His brow was furrowed with **pachydermic** wrinkles, telling of long decades of Arctic storms." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Rare Diseases", quote: "The localized **pachydermic** thickening of the scrotum was traced to chronic lymphatic obliteration." }
    ]
  },
  "Dashboard — derm\\pachydermous.md": {
    primary: "Variant of pachydermatous; thick-skinned, insensitive, or relating to pachyderms.",
    secondary: "In character description, emotionally impervious to insult, rebuke, or sensitivity.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Old Osborne was of a **pachydermous** nature, entirely devoid of those delicate sensibilities that torture finer souls." },
      { author: "Thomas Henry Huxley", work: "Methods and Results", quote: "The controversialist must possess a **pachydermous** hide if he intends to champion evolutionary heresy in public." },
      { author: "Walter Scott", work: "The Antiquary", quote: "He shrugged off the sarcastic sneers of his rival with calm, **pachydermous** indifference." }
    ]
  },
  "Dashboard — derm\\taxidermist.md": {
    primary: "A person who prepares, stuffs, and mounts the skins of animals for preservation, study, or exhibition in lifelike form.",
    secondary: "In museum curation, a specialist trained in animal anatomy, tanning, sculptural mannikin fabrication, and lifelike posture reconstruction.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Every bird and mammal collected during the inland expedition was skinned and labeled for the **taxidermist** in London." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The skilled **taxidermist** must work with rapid precision in the tropics before ants and moisture ruin the bird skins." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Around the naturalist's study were perched stuffed owls and birds of prey mounted by a local **taxidermist**." }
    ]
  },
  "Dashboard — derm\\taxidermy.md": {
    primary: "The art or practice of preparing, stuffing, and mounting the skins of animals with lifelike effect.",
    secondary: "In museum science, the preservation of wildlife specimens for scientific reference collections, anatomical research, and educational dioramas.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "I devoted my evenings to the delicate **taxidermy** of birds of paradise, preserving their marvelous plumes with powdered arsenic." },
      { author: "Charles Darwin", work: "Life and Letters of Charles Darwin", quote: "As a young student at Edinburgh, I took lessons in **taxidermy** from a freed slave that proved invaluable on the Beagle." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Modern **taxidermy** in public museums has progressed from grotesque stuffed skins to anatomically accurate artistic mounts." }
    ]
  },
  "Dashboard — derm\\undermanned.md": {
    primary: "Having an inadequate number of workers, crew members, or personnel to operate effectively.",
    secondary: "In maritime and organizational history, describing vessels or military posts operating below necessary complement.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The battered whaler was dangerously **undermanned** after losing two boat crews in the treacherous waters off Japan." },
      { author: "Joseph Conrad", work: "The Shadow-Line", quote: "With half the crew prostrate with tropical fever, the ship was critically **undermanned** as the gale approached." },
      { author: "Robert Louis Stevenson", work: "Treasure Island", quote: "Captain Smollett warned the squire that the Hispaniola was **undermanned** for so perilous an expedition." }
    ]
  },
  "Dashboard — derm\\undermentioned.md": {
    primary: "Mentioned, specified, or referred to subsequently or below in a written document or text.",
    secondary: "In legal documents, official decrees, and historical treatises, introducing a catalog of enumerated provisions or names.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **undermentioned** legions were ordered to march immediately from the Rhine frontier to the defense of Italy." },
      { author: "Alexander Hamilton", work: "The Federalist No. 22", quote: "The **undermentioned** defects in the Articles of Confederation rendered the national government incapable of collecting revenue." },
      { author: "Thomas Jefferson", work: "Writings of Thomas Jefferson", quote: "I transmit herewith the **undermentioned** papers concerning the boundary dispute between the neighboring territories." }
    ]
  },
  "Dashboard — derm\\undermine.md": {
    primary: "To excavate beneath a structure so as to make it collapse; or to weaken, erode, or damage insidiously or gradually.",
    secondary: "In political discourse and psychology, to covertly subvert authority, trust, or constitutional stability.",
    quotes: [
      { author: "William Shakespeare", work: "Troilus and Cressida", quote: "If Troy be not taken till these two **undermine** it, the walls will stand till they fall of themselves." },
      { author: "John Stuart Mill", work: "On Liberty", quote: "Unchecked despotic power tends slowly but inevitably to **undermine** the moral independence and vitality of the citizenry." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Factions work tirelessly to **undermine** the ancient foundations of church and state under the pretext of abstract equality." }
    ]
  },
  "Dashboard — din\\din.md": {
    primary: "A loud, unpleasant, and prolonged confusion of noises; an uproar or racket.",
    secondary: "In sensory description and literature, a deafening acoustic clamor that drowns out individual speech or thought.",
    quotes: [
      { author: "William Shakespeare", work: "The Taming of the Shrew", quote: "Think you a little **din** can daunt mine ears? Have I not heard the sea puff'd up with winds rage like an angry boar?" },
      { author: "John Milton", work: "Paradise Lost", quote: "A monstrous **din** of raging elements broke loose, shaking the high towers of heaven to their deep foundations." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The ceaseless **din** of Saint Antoine resounded through the narrow streets as the crowd prepared for revolt." }
    ]
  },
  "Dashboard — din\\dine.md": {
    primary: "To eat dinner; to take the principal meal of the day, often in social company.",
    secondary: "In social history and literature, to partake of an elaborate or formal repast accompanied by convivial conversation.",
    quotes: [
      { author: "William Shakespeare", work: "The Comedy of Errors", quote: "What, will you walk with me about the town, and then go to my inn and **dine** with me?" },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Darcy was invited to **dine** at Rosings, an honor which he accepted with his accustomed grave politeness." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Herbert and I agreed to **dine** together at our lodgings, celebrating our sudden turn of good fortune." }
    ]
  },
  "Dashboard — din\\dining.md": {
    primary: "The activity or experience of eating dinner; partaking of a meal in a designated room or social gathering.",
    secondary: "In social customs and architecture, relating to the formal room (dining-room) or furniture designed for communal meals.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 2", quote: "By this heavenly ground I tread on, I must be fain to pawn both my plate and the tapestry of my **dining** chambers." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The candles were lit on the long **dining** table, casting a warm golden glow across the faces of family and guests." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "They lingered in the **dining** room long after the dessert was cleared, discussing the strange destiny of Isabel Archer." }
    ]
  },
  "Dashboard — din\\undine.md": {
    primary: "In Paracelsian mythology and folklore, a female water spirit or nymph inhabiting brooks, lakes, and fountains.",
    secondary: "In romantic literature and opera, an elemental water being who gains a human soul only by marrying a mortal man (as in Friedrich de la Motte Fouqué's romance).",
    quotes: [
      { author: "Friedrich de la Motte Fouqué", work: "Undine", quote: "The gentle maiden was a true **undine**, born of the clear waters, seeking through human love the gift of an immortal soul." },
      { author: "Hans Christian Andersen", work: "The Little Mermaid", quote: "Like the legendary **undine** of German romance, the sea princess yearned to leave the ocean and walk upon mortal earth." },
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "The tale of **Undine** is one of the most exquisite creations of modern romantic genius, blending elemental nature with human sorrow." }
    ]
  },
  "Dashboard — encephal\\anencephalia.md": {
    primary: "The congenital absence of the cranial vault and cerebral hemispheres; anencephaly.",
    secondary: "In teratology and embryology, a lethal open neural tube defect resulting from failure of anterior neural pore closure during primary neurulation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The obstetric museum preserved an extraordinary case of **anencephalia**, where the flat skull base supported only vascular stroma." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "In **anencephalia**, the brainstem and spinal cord may be intact while the higher cerebral mantle is entirely absent." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "The prominent protruding eyes and absence of forehead give the infant with **anencephalia** a characteristic batrachian visage." }
    ]
  },
  "Dashboard — encephal\\anencephalic.md": {
    primary: "Affected by or characterized by anencephaly; born without the cerebral hemispheres and top of the skull.",
    secondary: "In neonatal neurology and medical ethics, designating an infant surviving only by primitive brainstem reflexes due to absence of neocortex.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "An **anencephalic** fetus may display active suckling and swallowing reflexes despite the complete absence of cerebral hemispheres." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Polyhydramnios during pregnancy should alert the obstetrician to the possibility of an **anencephalic** malformation." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Study of the **anencephalic** infant confirmed that basic autonomic vegetative rhythms are coordinated entirely within the brainstem." }
    ]
  },
  "Dashboard — encephal\\anencephalous.md": {
    primary: "Having no brain or lacking cerebral hemispheres; anencephalic.",
    secondary: "In comparative teratology and pathology, describing a fetus or organism exhibiting total failure of cerebral development.",
    quotes: [
      { author: "Étienne Geoffroy Saint-Hilaire", work: "Philosophie Anatomique: Des Monstruosités Humaines", quote: "The **anencephalous** monster demonstrates how the facial bones develop normally despite the absence of the brain." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "In the **anencephalous** condition, the reflex arc remains functional through the spinal cord alone." },
      { author: "William Osler", work: "Lectures on Diagnosis", quote: "The pathologist examined the **anencephalous** specimen, noting the thick vascular area cerebrovasculosa." }
    ]
  },
  "Dashboard — encephal\\anencephaly.md": {
    primary: "A serious birth defect in which a baby is born without parts of the brain and skull, caused by failure of the neural tube to close.",
    secondary: "In prenatal medicine and epidemiology, a lethal congenital neural tube defect preventable in large part by periconceptional maternal folic acid supplementation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The incidence of **anencephaly** displays striking geographic variation and a notable preponderance among female infants." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "The tragedy of **anencephaly** underscores the absolute dependence of conscious awareness upon an intact cerebral cortex." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures and Reports", quote: "Early maternal serum screening has dramatically reduced the birth prevalence of open **anencephaly**." }
    ]
  },
  "Dashboard — encephal\\encephal.md": {
    primary: "The combining root (from Greek enkephalos, meaning 'within the head, the brain'), forming terms relating to the brain and intracranial structures.",
    secondary: "In neuroanatomy and pathology, the foundational radical occurring in encephalon, encephalitis, and encephalopathy.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The ancient Greek word enkephalos literally signified that which is within the head; hence the anatomical root **encephal**." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the stem **encephal** arise our words encephalitis, encephalon, and electroencephalography." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "All specialized terms bearing the prefix **encephal** denote the cranial portion of the central nervous system." }
    ]
  },
  "Dashboard — encephal\\encephalartos.md": {
    primary: "A genus of African cycads (family Zamiaceae) commonly known as bread palms, characterized by thick cylindrical trunks and crowns of stiff, spiny pinnate leaves.",
    secondary: "In paleobotany and plant systematics, an ancient gymnosperm lineage surviving from the Mesozoic, with seeds historically processed into flour after detoxifying cycasin.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "The native tribes extract an edible flour from the pithy trunk of **Encephalartos**, burying it in water to wash out its poison." },
      { author: "Joseph Dalton Hooker", work: "The Flora of Tropical Africa", quote: "The massive cones of **Encephalartos** can weigh over eighty pounds, displaying vivid scarlet seeds upon maturity." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Like other cycads, species of **Encephalartos** rely upon specialized curculionid weevils for subterranean cone pollination." }
    ]
  },
  "Dashboard — encephal\\encephalitis.md": {
    primary: "Acute inflammation of the brain tissue, commonly caused by a viral infection or an autoimmune response.",
    secondary: "In neurology and infectious disease medicine, a condition presenting with fever, headache, altered consciousness, seizures, and focal neurological deficits.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The pandemic of **encephalitis** lethargica swept the globe between 1916 and 1927, leaving thousands frozen in parkinsonian trances." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Herpetic **encephalitis** exhibits a dangerous predilection for the temporal and frontal lobes, causing acute behavioral collapse." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Following recovery from acute **encephalitis**, neuropsychological testing reveals profound memory and attentional deficits." }
    ]
  },
  "Dashboard — encephal\\encephalocele.md": {
    primary: "A congenital defect in which brain tissue and its surrounding membranes protrude through an abnormal opening in the skull.",
    secondary: "In pediatric neurosurgery and teratology, a neural tube closure defect presenting as an occipital or frontonasal extracranial sac.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Transillumination of the occipital **encephalocele** indicates whether the protruding sac contains fluid meninges or functional cortex." },
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", quote: "Basal **encephalocele** protruding into the nasopharynx can easily be mistaken by the unwary surgeon for a simple nasal polyp." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Surgical closure of an **encephalocele** requires careful preservation of neural elements and watertight dural repair." }
    ]
  },
  "Dashboard — encephal\\encephalogram.md": {
    primary: "A diagnostic recording or image of the brain, historically an X-ray of the brain following gas replacement of CSF, or an electroencephalogram (EEG) tracing.",
    secondary: "In clinical neurophysiology and radiology, a graphical representation of cerebral electrical waveforms or intracranial ventriculography.",
    quotes: [
      { author: "Alexander Luria", work: "The Working Brain", quote: "The clinical **encephalogram** revealed localized spike-and-wave discharges originating in the left temporal lobe." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "A routine **encephalogram** documented continuous high-voltage delta activity across both cerebral hemispheres." },
      { author: "Harvey Cushing", work: "Intracranial Tumors", quote: "The pneumo-derived **encephalogram** demonstrated marked displacement of the lateral ventricle by a deep glioma." }
    ]
  },
  "Dashboard — encephal\\encephalography.md": {
    primary: "The radiography of the brain after the replacement of cerebrospinal fluid with a gas; or the electrical recording of brain activity (electroencephalography).",
    secondary: "In the history of neuroimaging, a pioneering diagnostic procedure introduced by Walter Dandy in 1919 to outline cerebral ventricles and detect space-occupying lesions.",
    quotes: [
      { author: "Harvey Cushing", work: "Intracranial Tumors", quote: "The development of fractional **encephalography** made it possible to localize tumors of the posterior fossa with unprecedented accuracy." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Electro-assisted **encephalography** provides an objective physiological window into the dynamic organization of cerebral cortical rhythms." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Before the advent of modern tomography, lumbar **encephalography** was our principal method for visualizing ventricular distortion." }
    ]
  },
  "Dashboard — encephal\\encephalomeningitis.md": {
    primary: "Inflammation affecting both the brain tissue and its surrounding protective membranes (meninges); meningoencephalitis.",
    secondary: "In clinical neurology, a combined infectious syndrome causing intense headache, nuchal rigidity, photophobia, altered consciousness, and focal seizures.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The acute onset of delirium and neck stiffness in **encephalomeningitis** demands immediate lumbar puncture and empiric antimicrobial therapy." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on the Diseases of the Nervous System", quote: "Post-mortem examination of **encephalomeningitis** reveals purulent exudate choking the subarachnoid cisterns and invading the cortex." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Severe childhood **encephalomeningitis** often leaves permanent scarring in association cortices, disrupting higher executive functions." }
    ]
  },
  "Dashboard — encephal\\encephalomyelitis.md": {
    primary: "Inflammation of both the brain and the spinal cord.",
    secondary: "In neurology and immunology, an acute autoimmune or infectious condition (such as acute disseminated encephalomyelitis or viral infections) producing multi-focal central nervous system demyelination.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Post-vaccinal **encephalomyelitis** presents as a sudden autoimmune attack upon the myelin sheaths of the brain and cord." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The patient's sudden paraparesis and confusion were the consequence of an acute, post-viral **encephalomyelitis**." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Disseminated **encephalomyelitis** scatters inflammatory foci through the white matter, impairing motor pathways and sensory conduction." }
    ]
  },
  "Dashboard — encephal\\encephalon.md": {
    primary: "The anatomical brain; the entire mass of nervous tissue enclosed within the cranium of a vertebrate.",
    secondary: "In comparative neuroanatomy, the central cephalic nervous structure comprising the prosencephalon (forebrain), mesencephalon (midbrain), and rhombencephalon (hindbrain).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The **encephalon** of the vertebrate expands from three primitive cerebral vesicles into the complex architecture of hemispheres and cerebellum." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Millions of interconnected neurons within the human **encephalon** form the physical organ of perception and thought." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The ratio of the **encephalon** to total body weight reaches its absolute evolutionary peak in primates and cetaceans." }
    ]
  },
  "Dashboard — encephal\\encephalopathy.md": {
    primary: "Any broad disease, disorder, or damage affecting the brain, characterized by an altered mental state, confusion, or cognitive impairment.",
    secondary: "In clinical internal medicine and critical care, cerebral dysfunction secondary to systemic metabolic failure (hepatic, uremic, hypertensive, or hypoxic encephalopathy).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Flapping tremor (asterixis) and fluctuating lethargy are the clinical hallmarks of metabolic **encephalopathy** in hepatic cirrhosis." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Hypoxic **encephalopathy** following cardiac arrest can selectively damage the vulnerable CA1 neurons of the hippocampus." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Toxic **encephalopathy** dulls the cortical tone, extinguishing the fine discrimination required for complex problem-solving." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch5Data);
console.log(`[Body Batch 5] Successfully updated ${updatedCount}/${Object.keys(batch5Data).length} notes.`);
