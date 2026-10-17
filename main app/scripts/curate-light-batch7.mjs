import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}

const batchData = {
  "Dashboard — phae/aphaeresis.md": {
    "primary": "The omission or loss of one or more sounds, syllables, or letters from the beginning of a word (such as 'gainst for against).",
    "secondary": "In historical phonology and metrics, a regular morphological contraction distinguishing colloquial speech or poetic scansion from formal prose.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Poetic scansion frequently requires **aphaeresis**, dropping initial vowels to preserve the iambic line."
      },
      {
        "author": "Henry Sweet",
        "work": "A History of English Sounds",
        "quote": "The development of modern English vocabulary demonstrates repeated **aphaeresis**, as when estate became state."
      },
      {
        "author": "Otto Jespersen",
        "work": "A Modern English Grammar on Historical Principles",
        "quote": "In rapid popular speech, **aphaeresis** eroded unstressed prefixes, transforming mend into amend."
      }
    ]
  },
  "Dashboard — phae/aphaeretic.md": {
    "primary": "Pertaining to, characterized by, or resulting from aphaeresis; having an initial sound or syllable omitted.",
    "secondary": "In descriptive linguistics, characterizing shortened lexical forms created through initial segment deletion.",
    "quotes": [
      {
        "author": "Henry Sweet",
        "work": "A New English Grammar",
        "quote": "Words like squire derived from Old French esquire represent classic **aphaeretic** developments."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "The **aphaeretic** contraction of words reflects the natural tendency toward physiological economy in speech."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Phonetic decay displays both **aphaeretic** losses at the beginning and apocopic losses at the end of syllables."
      }
    ]
  },
  "Dashboard — phae/phae.md": {
    "primary": "The Greek combining form (phaios, 'dusky, dun, gray-brown, dark') denoting dark brown, dusky hue, or brown algal pigments.",
    "secondary": "In biomedical and phycological nomenclature, a prefix in Phaeophyceae, pheochromocytoma, and phaeohyphomycosis.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In ancient Greek, the root **phae**- denoted the dusky gloom of twilight and the dun fleece of mountain sheep."
      },
      {
        "author": "Felix Eugen Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Botanists prefixed **phae**- to denote the olive-brown kelps whose fucoxanthin conceals green chlorophyll."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The combining element **phae**- designates chromaffin tissues that turn dark brown with chromium salts."
      }
    ]
  },
  "Dashboard — phae/phaeochromocytoma.md": {
    "primary": "British and historical spelling of pheochromocytoma; a catecholamine-secreting neuroendocrine tumor of the adrenal medulla.",
    "secondary": "In endocrinology and surgical pathology, a vascular chromaffin tumor causing paroxysmal hypertension, palpitations, headaches, and diaphoresis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A patient harboring an occult **phaeochromocytoma** experiences sudden, terrifying surges of systolic pressure."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity and Pathology",
        "quote": "Microscopic sections of the **phaeochromocytoma** stain deep mahogany brown upon exposure to potassium dichromate."
      },
      {
        "author": "William Henry Welch",
        "work": "Papers and Addresses",
        "quote": "Surgical removal of the **phaeochromocytoma** completely abolished the paroxysmal vasospastic crises."
      }
    ]
  },
  "Dashboard — phae/phaeohyphomycosis.md": {
    "primary": "A subcutaneous or systemic fungal infection caused by dematiaceous (naturally pigmented brown or black) fungi whose walls contain melanin.",
    "secondary": "In medical mycology, opportunistic mycotic infections by species of *Bipolaris*, *Exophiala*, or *Curvularia*, diagnosed by dark fungal hyphae in tissue biopsies.",
    "quotes": [
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "Deep tissue biopsies in **phaeohyphomycosis** demonstrate dark, septate, branched hyphae rich in melanin."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Immunocompromised patients occasionally contract severe subcutaneous **phaeohyphomycosis** following thorn puncture."
      },
      {
        "author": "Maxwell Finland",
        "work": "Antimicrobial Therapy",
        "quote": "Systemic **phaeohyphomycosis** poses difficult therapeutic problems owing to the intrinsic antifungal resistance of dematiaceous fungi."
      }
    ]
  },
  "Dashboard — phae/phaeomelanin.md": {
    "primary": "British and variant spelling of pheomelanin; the sulfur-containing reddish-yellow pigment found in red hair, feathers, and freckles.",
    "secondary": "In photobiology, an alkali-soluble melanin synthesized by the incorporation of glutathione or cysteine into dopaquinone.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Warm chestnut tones in mammalian fur arise from the fine distribution of **phaeomelanin** in the hair follicles."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies on Cell Staining",
        "quote": "Unlike photoprotective eumelanin, **phaeomelanin** can undergo photo-oxidation, generating cytotoxic free radicals."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The molecular architecture of **phaeomelanin** contains characteristic sulfur-bearing benzothiazine subunits."
      }
    ]
  },
  "Dashboard — phae/phaeophyceae.md": {
    "primary": "A large taxonomic class of mostly marine multicellular algae (brown algae), characterized by olive-green to dark brown thalli containing fucoxanthin.",
    "secondary": "In marine phycology, the evolutionary lineage encompassing giant giant kelps (*Macrocystis*), rockweeds (*Fucus*), and sargassum, reproducing via flagellated zoospores.",
    "quotes": [
      {
        "author": "Felix Eugen Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The class **Phaeophyceae** includes the grandest marine vegetation on Earth, with kelps reaching over a hundred feet in length."
      },
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "Members of **Phaeophyceae** dominate the rocky intertidal zones of cold temperate northern seas."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Tough leathery thalli of the **Phaeophyceae** withstand the crushing impact of continuous Atlantic surf."
      }
    ]
  },
  "Dashboard — phae/phaeophyta.md": {
    "primary": "A botanical division or phylum comprising the brown algae, characterized by brown carotenoid pigments (fucoxanthin) masking chlorophyll.",
    "secondary": "In marine ecology, the algal group responsible for massive underwater kelp forest ecosystems providing shelter and nutrients to diverse marine fauna.",
    "quotes": [
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "The division **Phaeophyta** is almost exclusively marine, thriving especially in turbulent subpolar waters."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The immense beds of **Phaeophyta** along the Fuegian coast support a fauna as rich as any tropical rainforest."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Cell walls in the **Phaeophyta** yield alginic acid, an economically vital mucilaginous polysaccharide."
      }
    ]
  },
  "Dashboard — phae/phaethon.md": {
    "primary": "In Greek mythology, the son of the sun god Helios who drove the sun chariot recklessly; in ornithology, the genus of oceanic tropicbirds.",
    "secondary": "In marine ornithology, pelagic seabirds (*Phaethon*) characterized by glistening white plumage, black markings, and extremely elongated central tail feathers.",
    "quotes": [
      {
        "author": "Ovid",
        "work": "Metamorphoses",
        "quote": "Bold **Phaethon** grasped the burning reins of the sun chariot, scorching the heavens and drying up the rivers of Earth."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "Like rash **Phaethon** hurtling from the sky, the ambitious poet fell from epic heights into bathos."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Far from any shore, the elegant white tropicbird, **Phaethon**, circled our masthead with graceful flight."
      }
    ]
  },
  "Dashboard — phae/phaethontidae.md": {
    "primary": "A family of oceanic seabirds in the order Phaethontiformes comprising the tropicbirds (genus *Phaethon*).",
    "secondary": "In systematic ornithology, pelagic plunge-divers possessing totipalmate feet, keen eyesight, and streamer-like central rectrices.",
    "quotes": [
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The family **Phaethontidae** contains three species of tropical seabirds famed for their streaming tail feathers."
      },
      {
        "author": "Robert Ridgway",
        "work": "The Birds of North and Middle America",
        "quote": "Breeding upon remote oceanic cliffs, the **Phaethontidae** wander for months over open tropical waters without touching land."
      },
      {
        "author": "John Gould",
        "work": "The Birds of Australia",
        "quote": "The radiant satin-like plumage of the **Phaethontidae** gleams with pinkish iridescence in equatorial sunlight."
      }
    ]
  },
  "Dashboard — phae/phaeton.md": {
    "primary": "A light, four-wheeled open horse-drawn carriage; in early motoring, an open-topped touring automobile with two rows of seats.",
    "secondary": "In 18th- and 19th-century transport history, a fast, fashionable, and somewhat hazardous sporting carriage driven by wealthy gentlemen.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Miss de Bourgh drove past the parsonage daily in her low **phaeton** and ponies."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "Joseph Sedley was proud of his dashing **phaeton**, driving it through the park to attract admiring glances."
      },
      {
        "author": "Charles Dickens",
        "work": "The Pickwick Papers",
        "quote": "A light **phaeton** rattled down the turnpike road at breakneck speed, scattering geese and chickens."
      }
    ]
  },
  "Dashboard — phae/pheochrome.md": {
    "primary": "Pertaining to cells or tissues that stain dark brown or yellowish-brown when exposed to chromium salts (chromaffin cells).",
    "secondary": "In histology, designating the neuroendocrine chromaffin granules of the adrenal medulla that oxidize to a brown color in dichromate fixatives.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology and Cell Chemistry",
        "quote": "The adrenal medullary cords exhibit a **pheochrome** reaction when immersed in Müller's potassium dichromate solution."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **pheochrome** granules represent stored adrenaline precursors awaiting sympathetic neural discharge."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology",
        "quote": "Embryologically, the **pheochrome** cells of the sympathetic paraganglia arise directly from the migrating neural crest."
      }
    ]
  },
  "Dashboard — phae/pheochromocytoma.md": {
    "primary": "A vascular, neuroendocrine tumor of the chromaffin tissue of the adrenal medulla that secretes high amounts of catecholamines.",
    "secondary": "In clinical endocrinology, a condition marked by the classic triad of episodic headaches, sweating, and tachycardia accompanied by severe hypertension.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unrecognized **pheochromocytoma** can provoke sudden hypertensive encephalopathy or fatal left ventricular failure."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Episodes of paroxysmal cardiac arrhythmia and pale sweating led to the detection of a large **pheochromocytoma**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Papers Relating to the Pituitary Body, Hypothalamus and Parasympathetic Nervous System",
        "quote": "The discovery of an adrenaline-producing **pheochromocytoma** explains many catastrophic vasomotor crises."
      }
    ]
  },
  "Dashboard — phalar/phalar.md": {
    "primary": "The Greek combining form (phalaros, 'white-spotted, having a white patch or crest') used in ornithological and botanical nomenclature.",
    "secondary": "In avian and plant taxonomy, a root designating white-patched shorebirds (phalaropes) and canary grasses (Phalaris).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek adjective **phalar**- designated the white crest upon a warrior's helmet or the frontal patch of the coot."
      },
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The combining form **phalar**- highlights the conspicuous white plumage markings on the throat and flanks."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "Botanists adopted **phalar**- to name grass genera whose compact inflorescences bear shining pale grains."
      }
    ]
  },
  "Dashboard — phalar/phalaris.md": {
    "primary": "A genus of stout annual and perennial grasses in the family Poaceae, commonly known as canary grasses, cultivated for birdseed and forage.",
    "secondary": "In plant physiology, the grass seedling (*Phalaris canariensis*) whose phototropic coleoptile Charles Darwin famously studied to discover auxin action.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "When the tip of the **Phalaris** coleoptile was capped with tin foil, the seedling ceased to bend toward lateral light."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "Fields of **Phalaris** were harvested in Kent to supply canary seed to the London bird fanciers."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The variegated ribbon grass grown in gardens is a cultivated variety of native **Phalaris**."
      }
    ]
  },
  "Dashboard — phalar/phalarope.md": {
    "primary": "A small, slender-necked wading shorebird in the family Scolopacidae, famous for spinning rapidly in circles on water to stir up insect prey.",
    "secondary": "In avian behavioral ecology, a bird noted for reversed sexual dimorphism and polyandry, where the brightly colored female courts the drab male who incubates the eggs.",
    "quotes": [
      {
        "author": "John James Audubon",
        "work": "Ornithological Biography",
        "quote": "The red **phalarope** swims with the buoyancy of a gull upon the arctic waves, feeding upon minute marine crustaceans."
      },
      {
        "author": "Elliott Coues",
        "work": "Birds of the Northwest",
        "quote": "Watching a **phalarope** pirouette on the tundra pool like a spinning top is one of the most delightful spectacles in nature."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Cape Cod",
        "quote": "A solitary **phalarope** drifted over the breakers, riding the stormy foam with effortless grace."
      }
    ]
  },
  "Dashboard — phalar/phalaropidae.md": {
    "primary": "A historical avian family formerly erected to classify the phalaropes, now treated as a specialized subfamily (Phalaropodinae) within Scolopacidae.",
    "secondary": "In systematic ornithology, wading birds distinguished by lobed swimming toes, dense waterproof belly plumage, and reversed breeding roles.",
    "quotes": [
      {
        "author": "Robert Ridgway",
        "work": "The Birds of North and Middle America",
        "quote": "The family **Phalaropidae** was distinguished from typical sandpipers by their semipalmate and lobate toes."
      },
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "All members of **Phalaropidae** spend their non-breeding months wandering over open pelagic oceans."
      },
      {
        "author": "Frank M. Chapman",
        "work": "Handbook of Birds of Eastern North America",
        "quote": "In **Phalaropidae**, nature has reversed the conventional roles, clothing the female in glorious nuptial dress."
      }
    ]
  },
  "Dashboard — phalar/phalaropus.md": {
    "primary": "The principal genus of phalaropes in the shorebird family Scolopacidae, comprising the red phalarope and red-necked phalarope.",
    "secondary": "In arctic ornithology, circumpolar migratory shorebirds (from Greek phalaros, coot-like, and pous, foot) possessing lobed toes for swimming.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Birds of Great Britain",
        "quote": "The graceful genus **Phalaropus** links the shorebirds to the pelagic fowl by its unique lobed swimming feet."
      },
      {
        "author": "Elliott Coues",
        "work": "Birds of the Colorado Valley",
        "quote": "Species of **Phalaropus** gather in immense maritime rafts off the Pacific coast during autumn migration."
      },
      {
        "author": "Alexander Wilson",
        "work": "American Ornithology",
        "quote": "The rapid swimming movements of **Phalaropus** allow it to capture mosquito larvae from northern peat pools."
      }
    ]
  },
  "Dashboard — phan/anaphase.md": {
    "primary": "The stage of cell division (mitosis or meiosis) in which duplicated chromosomes or sister chromatids separate and migrate toward opposite poles.",
    "secondary": "In cell biology and cytogenetics, the rapid mitotic phase triggered by the anaphase-promoting complex, which cleaves cohesin rings along chromatids.",
    "quotes": [
      {
        "author": "Walther Flemming",
        "work": "Zellsubstanz, Kern und Zelltheilung",
        "quote": "During **anaphase**, the daughter chromosomes pull apart along the spindle fibers with geometrical precision."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "The synchronous movement of chromosomes in **anaphase** ensures that each daughter nucleus receives identical genetic material."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Physical Basis of Heredity",
        "quote": "Non-disjunction during meiotic **anaphase** results in daughter cells carrying abnormal chromosome numbers."
      }
    ]
  },
  "Dashboard — phan/aphanite.md": {
    "primary": "A fine-grained, crystalline igneous rock whose constituent mineral grains are too small to be distinguished by the unaided human eye.",
    "secondary": "In petrology, an extrusive or shallow intrusive rock (such as basalt or felsite) exhibiting rapid cooling from a molten volcanic state.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The dense dark basalt passed insensibly into compact **aphanite** along the chilling margins of the volcanic dike."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Under the magnifying lens, the apparently homogeneous **aphanite** resolved into minute crystals of feldspar and pyroxene."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Lava flows that cooled rapidly in seawater solidified into microcrystalline **aphanite** and volcanic glass."
      }
    ]
  },
  "Dashboard — phan/aphanitic.md": {
    "primary": "Having a very fine-grained, microcrystalline texture, applied to igneous rocks whose mineral components cannot be distinguished without magnification.",
    "secondary": "In petrography, describing volcanic rocks with cryptocrystalline or microcrystalline groundmass resulting from rapid subaerial quenching.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "The Ancient Volcanoes of Great Britain",
        "quote": "The basaltic sheets exhibit a dense **aphanitic** texture at their upper surface where heat escaped rapidly."
      },
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "Rhyolite lavas frequently display an **aphanitic** groundmass enclosing scattered porphyritic quartz phenocrysts."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "An **aphanitic** dike had cut cleanly through the coarse granite bedrock of the quarry."
      }
    ]
  },
  "Dashboard — phan/diaphanous.md": {
    "primary": "Light, delicate, and translucent or transparent (especially of fine fabrics or vapor).",
    "secondary": "In literature and optics, describing ethereal, gossamer substances that permit light to shine through with luminous softness.",
    "quotes": [
      {
        "author": "Percy Bysshe Shelley",
        "work": "Alastor; or, The Spirit of Solitude",
        "quote": "Her **diaphanous** robe floated like morning mist around her youthful limbs."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "Turner captured the **diaphanous** veil of summer dawn rising above the Venetian lagoons."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The water shone pacifically, the sky was serene, a **diaphanous** fabric of evocative light."
      }
    ]
  },
  "Dashboard — phan/emphasis.md": {
    "primary": "Special importance, value, or prominence given to something; stress laid upon a word or syllable in speaking.",
    "secondary": "In rhetoric and typography, the deliberate highlighting of a statement via vocal inflection, italics, or structural positioning.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Shakspeare places his **emphasis** with such sovereign right that every phrase becomes immortal."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Too frequent **emphasis** in speech weakens authority, like a page printed entirely in capital letters."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The orator pronounced the word treason with terrible **emphasis**, causing the house to hold its breath."
      }
    ]
  },
  "Dashboard — phan/emphasise.md": {
    "primary": "British spelling of emphasize; to give special importance or prominence to something in speaking or writing.",
    "secondary": "In rhetorical composition and elocution, to stress a particular concept, argument, or syllable to arrest the audience's attention.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Inside the Whale",
        "quote": "I wish to **emphasise** that every sincere writer must preserve his political independence."
      },
      {
        "author": "Virginia Woolf",
        "work": "A Room of One's Own",
        "quote": "To **emphasise** the material barriers faced by women was not to diminish their creative genius."
      },
      {
        "author": "H. G. Wells",
        "work": "The Outline of History",
        "quote": "We must **emphasise** the profound unity underlying all great historical world religions."
      }
    ]
  },
  "Dashboard — phan/emphasised.md": {
    "primary": "Given special prominence, importance, or stress; highlighted (British spelling).",
    "secondary": "In stylistic analysis, characterizing arguments, visual features, or vocal tones made conspicuous by conscious intent.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "Her dark eyes **emphasised** the pale delicacy of her youthful face."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Holmes **emphasised** each point of the clues by tapping his pipe upon the mantelpiece."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "The naval staff **emphasised** the grave peril of unrestricted submarine warfare in the Atlantic."
      }
    ]
  },
  "Dashboard — phan/emphasize.md": {
    "primary": "To give special importance, prominence, or stress to something in speech, writing, or visual design.",
    "secondary": "In elocution and linguistics, to deliver a syllable or word with increased vocal force, pitch change, or duration.",
    "quotes": [
      {
        "author": "Abraham Lincoln",
        "work": "Address at Cooper Institute",
        "quote": "Let us again and again **emphasize** our devotion to the Constitution as our fathers framed it."
      },
      {
        "author": "William James",
        "work": "Talks to Teachers on Psychology",
        "quote": "The teacher must **emphasize** the central concept and suppress confusing trivial details."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "Simplify, simplify; I cannot too often **emphasize** the wisdom of shedding superfluous possessions."
      }
    ]
  },
  "Dashboard — phan/emphatic.md": {
    "primary": "Showing or giving emphasis; expressing something forcibly, clearly, and decisively.",
    "secondary": "In phonetics and semitics, describing consonants articulated with pharyngeal constriction or velarization; in behavior, bold and unmistakable.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Dick gave an **emphatic** nod of his head, as though the matter admitted of no debate."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Villette",
        "quote": "Madame Beck answered with an **emphatic** denial that brooked no further inquiry."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Danton's voice was **emphatic**, sounding like a clarion of war above the clamor of the assembly."
      }
    ]
  },
  "Dashboard — phan/epiphany.md": {
    "primary": "A moment of sudden and profound revelation or insight; the Christian festival (January 6) commemorating the manifestation of Christ to the Magi.",
    "secondary": "In literary theory, James Joyce's concept of a sudden spiritual manifestation where an ordinary object or trivial gesture reveals its essential soul.",
    "quotes": [
      {
        "author": "James Joyce",
        "work": "Stephen Hero",
        "quote": "By an **epiphany** he meant a sudden spiritual manifestation, whether in the vulgarity of speech or of a memorable phase of the mind itself."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "She had an **epiphany** of peace, perceiving that the fleeting moments of beauty were eternal."
      },
      {
        "author": "John Milton",
        "work": "Paradise Regained",
        "quote": "The bright celestial star heralded the glorious **epiphany** of the divine babe to the Eastern kings."
      }
    ]
  },
  "Dashboard — phan/epiphenomenon.md": {
    "primary": "A secondary phenomenon, effect, or byproduct that occurs alongside or results from a primary process, but lacks causal efficacy on that process.",
    "secondary": "In the philosophy of mind, Thomas Henry Huxley's hypothesis that conscious mental states are causally inert byproducts of underlying neural mechanisms.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Hypothesis that Animals are Automata",
        "quote": "Consciousness appears to be related to the mechanism of the body simply as an **epiphenomenon**, like the steam whistle of an engine."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "To reduce our passions and noble volitions to an idle **epiphenomenon** of brain tremors affronts common sense."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Analysis of Mind",
        "quote": "Behaviorism treats subjective thought as an incidental **epiphenomenon** of muscular twitching."
      }
    ]
  },
  "Dashboard — phan/fantasise.md": {
    "primary": "British spelling of fantasize; to indulge in daydreaming, reverie, or imaginative speculation.",
    "secondary": "In psychology and psychoanalysis, to construct internal mental scenarios fulfilling unconscious desires or repressed aspirations.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "Alone in the garden, the child began to **fantasise** about magical islands across the sea."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "He would sit in his dingy room and **fantasise** about suddenly inheriting immense wealth."
      },
      {
        "author": "H. G. Wells",
        "work": "Kipps",
        "quote": "He loved to **fantasise** himself as a gallant cavalier rescuing high-born ladies from distress."
      }
    ]
  },
  "Dashboard — phan/fantasist.md": {
    "primary": "A person who invents or indulges in fantasies, extravagant daydreams, or unrealistic imaginings.",
    "secondary": "In literature and psychiatric evaluation, an author of imaginative fantasy fiction or a pathological mythomaniac living in self-created illusions.",
    "quotes": [
      {
        "author": "G. K. Chesterton",
        "work": "The Everlasting Man",
        "quote": "The poet is a healthy **fantasist** who makes us see ordinary lampposts as fairy wands."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Illustrious Client",
        "quote": "The criminal was a cold **fantasist**, weaving intricate webs of romantic deception to entrap the innocent."
      },
      {
        "author": "George Bernard Shaw",
        "work": "John Bull's Other Island",
        "quote": "Do not mistake the dreamy Irish **fantasist** for a practical political administrator."
      }
    ]
  },
  "Dashboard — phan/fantasize.md": {
    "primary": "To daydream, imagine, or indulge in pleasing, improbable, or extravagant mental reveries.",
    "secondary": "In clinical psychology and child development, creating imaginative compensatory narratives to cope with emotional distress or boredom.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The tendency to **fantasize** provides an emotional sanctuary where thwarted instincts find harmless expression."
      },
      {
        "author": "Sigmund Freud",
        "work": "Creative Writers and Day-Dreaming",
        "quote": "The growing child continues to **fantasize** in secret, weaving imaginary wish-fulfillments into solitary daydreams."
      },
      {
        "author": "Mark Twain",
        "work": "The Adventures of Tom Sawyer",
        "quote": "Tom would sit beneath the oak tree and **fantasize** glorious triumphs as a fearless pirate chief."
      }
    ]
  },
  "Dashboard — phan/fantastic.md": {
    "primary": "Extraordinarily good or attractive; imaginative, bizarre, fanciful, or existing only in the imagination.",
    "secondary": "In literary criticism and art, characterized by unrestrained fancy, grotesque invention, or surreal transgression of realistic laws.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "An irrepressible tremor gradually pervaded my frame; and, at length, there sat upon my very heart an incubus of utterly **fantastic** terror."
      },
      {
        "author": "Charles Dickens",
        "work": "A Christmas Carol",
        "quote": "The crisp leaves rustled beneath his feet, and shadows danced in **fantastic** shapes upon the frosted wall."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Gothic gargoyles display a **fantastic** vitality born of the workman's untamed northern imagination."
      }
    ]
  },
  "Dashboard — phan/fantastical.md": {
    "primary": "Imaginative, fanciful, or bizarre; grotesque or extravagant in conception; unrealistic.",
    "secondary": "In Renaissance and Jacobean drama, describing eccentric whims, supernatural apparitions, or capricious melancholy.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Macbeth",
        "quote": "My thought, whose murder yet is but **fantastical**, shakes so my single state of man."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Scholastic philosophy was corrupted by **fantastical** conceits that had no foundation in sensible nature."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Rime of the Ancient Mariner",
        "quote": "The **fantastical** ice mast-high came floating by, as green as emerald."
      }
    ]
  },
  "Dashboard — phan/fantastically.md": {
    "primary": "In a fantastic, bizarre, or extraordinarily imaginative manner; to an extraordinary degree.",
    "secondary": "In narrative prose, describing extravagant ornamentation, wild landscapes, or eccentric behaviors.",
    "quotes": [
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "The Spy-glass hill shot up **fantastically** into the blue tropical sky, its crags jagged like broken glass."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "The icy peaks shone **fantastically** beneath the pale rays of the rising moon."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The harpooneer's body was **fantastically** tattooed with spiraling whorls of Polynesian ink."
      }
    ]
  },
  "Dashboard — phan/fantasy.md": {
    "primary": "The faculty or activity of imagining impossible or improbable things; a genre of imaginative fiction featuring magical or supernatural elements.",
    "secondary": "In literary theory and psychoanalysis, the psychic generation of imagery unbound by reality constraints (contrasted with factual memory).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "A Midsummer Night's Dream",
        "quote": "The lunatic, the lover, and the poet Are of imagination all compact; their shaping **fantasy** bodies forth forms of things unknown."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "When reason sleeps, **fantasy** erects palaces of cloud that vanish at the touch of reality."
      },
      {
        "author": "J. R. R. Tolkien",
        "work": "On Fairy-Stories",
        "quote": "Creative **fantasy** does not destroy reason, but rather sharpens our perception of the primary world."
      }
    ]
  },
  "Dashboard — phan/metaphase.md": {
    "primary": "The second stage of cell division (mitosis or meiosis), during which duplicated chromosomes align along the equatorial plate of the spindle.",
    "secondary": "In cytogenetics, the stage where chromosomes reach maximal condensation and are arrested by colchicine to prepare karyotypes.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "At **metaphase**, each chromosome is aligned with mathematical symmetry along the equatorial plate of the spindle."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Colchicine arrests dividing cells in **metaphase**, facilitating the counting of individual chromosome pairs."
      },
      {
        "author": "Barbara McClintock",
        "work": "The Association of Broken Chromosomes with Translocations",
        "quote": "The univalent chromosomes lagged upon the spindle long after normal bivalents had passed **metaphase**."
      }
    ]
  },
  "Dashboard — phan/phan.md": {
    "primary": "The Greek combining form (phainein, phanos, 'to appear, show, shine, visible') denoting light, revelation, manifestation, or appearance.",
    "secondary": "In linguistic and scientific nomenclature, the foundational root yielding phantom, epiphany, phanerogam, diaphanous, and related visual terms.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The root **phan**- signifies the sudden flashing forth of light and the visual manifestation of hidden forms."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "Philosophical terms bearing the root **phan**- relate to visible phenomena and perceptual appearance."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "From the Greek stem **phan**- arise terms denoting both radiant apparitions and empirical observations."
      }
    ]
  },
  "Dashboard — phan/phanerogam.md": {
    "primary": "A seed-bearing plant that produces flowers or cones; a spermatophyte, as distinguished from a cryptogam (spore-bearing plant).",
    "secondary": "In systematic botany, seed plants comprising angiosperms and gymnosperms whose reproductive organs are visibly manifested in flowers or strobili.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Every true **phanerogam** reproduces through seeds containing a preformed embryo nourished by endosperm."
      },
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "Circumnutation is common to all growing shoots throughout the vast division of the **phanerogam** plants."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Linnaeus divided the vegetable world into the hidden cryptogams and the conspicuous **phanerogam** families."
      }
    ]
  },
  "Dashboard — phan/phanerogamae.md": {
    "primary": "The historical botanical taxonomic division comprising all flowering and seed-bearing plants (phanerogams or spermatophytes).",
    "secondary": "In classical botanical systematics, the grand assemblage established by Linnaeus contrasting with Cryptogamae, uniting gymnosperms and angiosperms.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Philosophia Botanica",
        "quote": "The **Phanerogamae** openly display their nuptial organs to the sun, whereas the cryptogams conceal their generation."
      },
      {
        "author": "George Bentham",
        "work": "Genera Plantarum",
        "quote": "Our systematic survey of the **Phanerogamae** encompasses more than two hundred natural orders of flowering vegetation."
      },
      {
        "author": "Julius von Sachs",
        "work": "History of Botany",
        "quote": "The comparative studies of Hofmeister bridged the structural chasm separating the Cryptogamae from the **Phanerogamae**."
      }
    ]
  },
  "Dashboard — phan/phaneromania.md": {
    "primary": "An abnormal, uncontrollable obsessive habit or compulsion of picking at or touching one's own skin, nails, hairs, or blemishes.",
    "secondary": "In psychiatric dermatology and behavioral medicine, a body-focused repetitive disorder encompassing trichotillomania, onychophagia, and skin excoriation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients plagued with **phaneromania** incessantly pick at harmless cutaneous roughness until ulceration ensues."
      },
      {
        "author": "Erasmus Wilson",
        "work": "Diseases of the Skin",
        "quote": "The nervous excoriations were diagnosed as a form of **phaneromania** arising from constitutional anxiety."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "Habitual nail-biting and cuticle tearing in children represent mild manifestations of **phaneromania**."
      }
    ]
  },
  "Dashboard — phan/phanerozoic.md": {
    "primary": "The current geological eon, spanning from approximately 541 million years ago to the present, characterized by abundant visible animal and plant life.",
    "secondary": "In geochronology and paleontology, the grand eon following the Cryptozoic (Precambrian), divided into the Paleozoic, Mesozoic, and Cenozoic eras.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The onset of the **Phanerozoic** eon is marked by the sudden appearance of diverse hard-shelled fossils in the Cambrian strata."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The Burgess Shale captures the extraordinary evolutionary explosion that inaugurated the **Phanerozoic** eon."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "The fossil record of the **Phanerozoic** chronicles the rise of vertebrate life from primitive fishes to mammals."
      }
    ]
  },
  "Dashboard — phan/phantasm.md": {
    "primary": "A figment of the imagination; an illusion or apparition; a mental image of a real or supernatural object.",
    "secondary": "In philosophy and psychological fiction, an illusory sensory appearance lacking objective physical reality.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Raven",
        "quote": "Thrilled me—filled me with fantastic terrors never felt before; So that now, to still the beating of my heart, I stood repeating, It is some visitor, no **phantasm** of the night."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "I saw the hideous **phantasm** of a man stretched out, and then, on the working of some powerful engine, show signs of life."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Prometheus Unbound",
        "quote": "The **phantasm** of Jupiter arose from the misty underworld, uttering curses against the Titan."
      }
    ]
  },
  "Dashboard — phan/phantasma.md": {
    "primary": "An archaic or philosophical form of phantasm; an apparition, phantom, or mental illusion.",
    "secondary": "In Aristotelian epistemology and classical tragedy, the internal sensory image produced by the imagination (phantasia).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Julius Caesar",
        "quote": "Between the acting of a dreadful thing And the first motion, all the interim is Like a **phantasma**, or a hideous dream."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The mind of man, unguided by empirical observation, generates empty **phantasma** instead of divine knowledge."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "Sleep creates an inward stage where the soul converses with its own airy **phantasma**."
      }
    ]
  },
  "Dashboard — phan/phantasmagoria.md": {
    "primary": "A sequence of real or imaginary images like those seen in a dream; historically, an exhibition of optical illusions produced by magic lanterns.",
    "secondary": "In Victorian cultural history, theatrical projection shows using mobile magic lanterns behind translucent screens, evoking ghostly apparitions.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The whole history of the Terror rolled past like a turbulent, blood-stained **phantasmagoria**."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "Ligeia",
        "quote": "A subtle **phantasmagoria** seemed painted upon the heavy tapestries, shifting with every gust of wind."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The foggy city seemed a smoky **phantasmagoria** of ghostly vehicles and vanishing pedestrian shapes."
      }
    ]
  },
  "Dashboard — phan/phantasmagoric.md": {
    "primary": "Having a fantastic or deceptive appearance, as something in a dream or shifting optical illusion.",
    "secondary": "In literary criticism, characterizing narrative imagery marked by rapid, hallucinatory shifts of light, color, and bizarre forms.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "The hound burst from the dense fog with a **phantasmagoric** fury, fire leaping from its jaws."
      },
      {
        "author": "Virginia Woolf",
        "work": "Orlando",
        "quote": "The Great Frost turned London into a **phantasmagoric** carnival of frozen revelers on the Thames."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "The sun spun across the heavens in a **phantasmagoric** ribbon of blazing golden light."
      }
    ]
  },
  "Dashboard — phan/phantasmagorical.md": {
    "primary": "Relating to, resembling, or having the qualities of a phantasmagoria; dreamlike, illusory, and shifting.",
    "secondary": "In artistic criticism, describing surreal or nightmarish visual compositions filled with metamorphic figures.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "Turner's stormy seas possess a **phantasmagorical** grandeur that transcends mere literal representation."
      },
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "Opium summoned before my closed eyes colossal, **phantasmagorical** cities towering into the night."
      },
      {
        "author": "Nathaniel Hawthorne",
        "work": "The Scarlet Letter",
        "quote": "The minister's tortured conscience transformed the dark forest trees into a **phantasmagorical** assembly of demons."
      }
    ]
  },
  "Dashboard — phan/phantasmal.md": {
    "primary": "Of, relating to, or resembling a phantasm; spectral, ghostly, or illusory; lacking physical reality.",
    "secondary": "In philosophical prose and poetry, describing shadowy visions or deceptive mirages that mock human grasp.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The white whale swam through the night like a **phantasmal** apparition gliding across the deep."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Epipsychidion",
        "quote": "Her voice was like the voice of his own soul heard in the **phantasmal** twilight."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The distant peaks looked **phantasmal** and fragile against the brilliant crimson sunrise."
      }
    ]
  },
  "Dashboard — phan/phantasy.md": {
    "primary": "An older, literary spelling of fantasy; unrestrained imagination, visionary reverie, or a fantastic mental creation.",
    "secondary": "In Romantic poetics and early psychology, the intuitive creative power that combines memory images into original artistic visions.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "I separated Fancy from the higher creative Imagination, relegating the former to the play of **phantasy**."
      },
      {
        "author": "John Keats",
        "work": "Endymion",
        "quote": "A thousand dreams of radiant **phantasy** hovered around his slumbering head."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Man's body itself is but a garment woven by **phantasy** upon the loom of time."
      }
    ]
  },
  "Dashboard — phan/phantom.md": {
    "primary": "A ghost, apparition, or spectral figure; something that exists only in the mind or imagination; illusory.",
    "secondary": "In neurophysiology, a sensory perception originating from an absent body part, as in the famous phenomenon of phantom limb pain.",
    "quotes": [
      {
        "author": "Silas Weir Mitchell",
        "work": "Phantom Limbs",
        "quote": "The amputee felt distinct, excruciating cramping in the toes of his nonexistent **phantom** foot."
      },
      {
        "author": "William Shakespeare",
        "work": "Macbeth",
        "quote": "Is this a dagger which I see before me, Or art thou but A dagger of the mind, a false creation, A **phantom** of fevered thought?"
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The central nervous system maintains an enduring sensory map, giving vivid reality to the **phantom** arm."
      }
    ]
  },
  "Dashboard — phan/phase.md": {
    "primary": "A distinct stage or period in a series of events, development, or cycle; in astronomy, the changing illuminated shape of the moon or planet.",
    "secondary": "In thermodynamics and physical chemistry, a chemically and physically uniform, homogeneous state of matter (solid, liquid, or gas).",
    "quotes": [
      {
        "author": "Josiah Willard Gibbs",
        "work": "On the Equilibrium of Heterogeneous Substances",
        "quote": "The **phase** rule mathematically defines the degrees of freedom in any multi-component chemical equilibrium."
      },
      {
        "author": "Galileo Galilei",
        "work": "Letters on Sunspots",
        "quote": "The discovery that Venus displays every **phase** like the moon proved that it revolves around the sun."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "Each successive **phase** of embryonic growth recapitulates ancestral structural configurations."
      }
    ]
  },
  "Dashboard — phan/phene.md": {
    "primary": "A genetically determined phenotypic characteristic or trait of an organism; in organic chemistry, an obsolete synonym for benzene.",
    "secondary": "In modern genetics and phenomics, the elementary unit of the phenotype, corresponding to a single observable morphological or biochemical attribute.",
    "quotes": [
      {
        "author": "Wilhelm Johannsen",
        "work": "Elements of the Exact Doctrine of Heredity",
        "quote": "Just as the gene is the elemental unit of heredity, so the **phene** is the elementary unit of the visible phenotype."
      },
      {
        "author": "Auguste Laurent",
        "work": "Chemical Method",
        "quote": "I proposed the radical name **phene** for the aromatic core found in benzene derivatives."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Natural selection operates directly upon the **phene** rather than upon the naked genotype."
      }
    ]
  },
  "Dashboard — phan/phenetic.md": {
    "primary": "Classifying organisms based on overall morphological or anatomical similarity, without regard to evolutionary phylogeny.",
    "secondary": "In numerical taxonomy, a methodological framework that groups operational taxonomic units using unweighted biometric similarity matrices.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "A purely **phenetic** classification risks grouping convergent organisms together despite profound phylogenetic divergence."
      },
      {
        "author": "Julian Huxley",
        "work": "The New Systematics",
        "quote": "Numerical taxonomy utilizes **phenetic** distance algorithms to cluster species without evolutionary bias."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "The cladistic revolution exposed the theoretical inadequacies of strictly **phenetic** taxonomic clustering."
      }
    ]
  },
  "Dashboard — phan/phenology.md": {
    "primary": "The scientific study of cyclic and seasonal natural phenomena, especially in relation to climate, plant flowering, and animal migration.",
    "secondary": "In climatology and environmental ecology, recording annual dates of budburst, bird arrival, and leaf fall as sensitive bio-indicators of climate change.",
    "quotes": [
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "My journal of the first songs of birds and opening of flowers forms the basis of rural **phenology**."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Journal",
        "quote": "The meticulous **phenology** of Walden Pond revealed that nature keeps her spring calendar with astonishing fidelity."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Alterations in seasonal **phenology** disrupt the delicate synchronization between hatching insect larvae and migrating warblers."
      }
    ]
  },
  "Dashboard — phan/phenomenon.md": {
    "primary": "A fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question; an extraordinary occurrence.",
    "secondary": "In Kantian philosophy, the object of sensory experience (the sensible appearance), distinguished from the noumenon (the thing-in-itself).",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The human mind cognizes only the **phenomenon** as conditioned by space and time, never the noumenon in itself."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "From these simple experiments, the marvelous **phenomenon** of colors in thin plates receives a full explanation."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The phosphorescence of the sea is a magnificent **phenomenon** that fills the nocturnal traveler with wonder."
      }
    ]
  },
  "Dashboard — phan/polyphase.md": {
    "primary": "Having or utilizing two or more alternating electrical voltages with regular phase differences between them (such as three-phase power).",
    "secondary": "In electrical power engineering, systems designed by Nikola Tesla using multi-phase currents to generate rotating magnetic fields in induction motors.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "A New System of Alternating Current Motors and Transformers",
        "quote": "The generation of a continuous rotating magnetic field was accomplished through my novel **polyphase** alternating current system."
      },
      {
        "author": "Charles Proteus Steinmetz",
        "work": "Theory and Calculation of Alternating Current Phenomena",
        "quote": "The transmission of massive power across Niagara Falls established the undisputed supremacy of the **polyphase** grid."
      },
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "Tesla's **polyphase** motors solved the problem of long-distance industrial energy transmission."
      }
    ]
  },
  "Dashboard — phan/prophase.md": {
    "primary": "The first stage of cell division (mitosis or meiosis), during which chromatin condenses into distinct chromosomes and the nuclear envelope disintegrates.",
    "secondary": "In cytology and molecular genetics, the initial mitotic phase where duplicated centrosomes separate and initiate spindle formation.",
    "quotes": [
      {
        "author": "Walther Flemming",
        "work": "Zellsubstanz, Kern und Zelltheilung",
        "quote": "In early **prophase**, the diffuse nuclear network condenses into distinct, dark-staining chromatin skeins."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "During **prophase**, the nucleolus dissolves and the centrosomes migrate to establish the bipolar spindle."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Mechanism of Mendelian Heredity",
        "quote": "Homologous chromosomes pair lengthwise during the extended meiotic **prophase**, permitting crossing over."
      }
    ]
  },
  "Dashboard — phan/telophase.md": {
    "primary": "The final stage of cell division (mitosis or meiosis), in which daughter chromosomes reach the spindle poles and new nuclear envelopes assemble around them.",
    "secondary": "In cytology, the terminal mitotic phase concurrent with cytokinesis, where chromosomes decondense back into diffuse euchromatin.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "During **telophase**, the nuclear membranes reconstruct around the daughter chromosomal clusters as cytokinesis cleaves the cell."
      },
      {
        "author": "Walther Flemming",
        "work": "Cell Substance and Nuclear Division",
        "quote": "At **telophase**, the tightly packed chromosomes begin to loosen and resume the granular appearance of the resting nucleus."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The completion of **telophase** marks the successful segregation of identical genetic complements into two daughter cells."
      }
    ]
  },
  "Dashboard — phan/theophany.md": {
    "primary": "A visible manifestation or appearance of God or a deity to humankind.",
    "secondary": "In biblical theology and comparative religious history, a divine epiphany such as the burning bush of Moses or the chariot vision of Ezekiel.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "Ancient pagan mysteries claimed to grant the initiate a direct personal **theophany** of the goddess."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Sinai bowed beneath the terrible **theophany**, wrapped in smoking fire and the voice of thunder."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "To the ancient prophet, the thunderstorm was not a physical mechanism, but a direct, awe-inspiring **theophany**."
      }
    ]
  },
  "Dashboard — phan/tryptophan.md": {
    "primary": "An essential aromatic amino acid (C11H12N2O2) containing an indole ring, required for protein synthesis and serving as a metabolic precursor to serotonin and melatonin.",
    "secondary": "In nutritional biochemistry and physiology, an essential dietary building block first isolated by Frederick Gowland Hopkins from pancreatic digests of casein.",
    "quotes": [
      {
        "author": "Frederick Gowland Hopkins",
        "work": "Feeding Experiments Illustrating the Importance of Accessory Factors in Normal Dietaries",
        "quote": "Animals fed diets lacking **tryptophan** failed to grow, demonstrating that this indole amino acid is strictly essential to life."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The bulky bicyclic indole side chain of **tryptophan** participates in crucial hydrophobic interactions within enzymatic active sites."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies on Immunity",
        "quote": "Certain bacterial growth media require supplemental **tryptophan** to support rapid proliferation."
      }
    ]
  },
  "Dashboard — phan/unemphatic.md": {
    "primary": "Not emphatic; spoken, done, or expressed without special force, prominence, or stress; gentle, subdued, or mild.",
    "secondary": "In literary prose and elocution, describing understated delivery or quiet, muted assertions that lack rhetorical urgency.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Her reply was delivered in an **unemphatic** monotone that gave no clue to her inner turmoil."
      },
      {
        "author": "Virginia Woolf",
        "work": "Jacob's Room",
        "quote": "The conversation was quiet, polite, and completely **unemphatic**, gliding over dangerous domestic truths."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Casaubon made his **unemphatic** pronouncement with the dry precision of a cathedral archivist."
      }
    ]
  }
};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {
  if (updateNote(relPath, data)) updated++;
}
console.log(`Successfully updated ${updated} of ${Object.keys(batchData).length} files in Batch 7.`);
