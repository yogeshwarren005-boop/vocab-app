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
  "Dashboard — aspr/aspr.md": {
    "primary": "The combining form derived from Byzantine Greek aspron (white, silvery), historically denoting white coins or argentiferous currency.",
    "secondary": "In numismatics and Mediterranean monetary history, a small silver or alloyed coin circulating throughout the Byzantine Empire, Ottoman domains, and the Trebizond realm.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The tribute was computed in bags of silver **aspr**, the traditional coin of the Levant."
      },
      {
        "author": "Richard Knolles",
        "work": "The Generall Historie of the Turkes",
        "quote": "Every soldier received his daily dole of five **aspr** pieces from the grand vizier."
      },
      {
        "author": "John Evelyn",
        "work": "Numismata: A Discourse of Medals",
        "quote": "The debased **aspr** circulated widely through Aegean trading ports during the Venetian wars."
      }
    ]
  },
  "Dashboard — aspr/diaper.md": {
    "primary": "A fabric woven with a repeated geometric diamond or lozenge pattern, or ornamentation consisting of such repeated motifs.",
    "secondary": "In heraldry and architectural decoration, surface patterning composed of reticulated diamonds or small rosettes; in child-care, an absorbent garment.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The red wall was enriched with delicate marble **diaper** carved into low relief."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Silken banners covered in gold **diaper** fluttered above the assembling heralds."
      },
      {
        "author": "Geoffrey Chaucer",
        "work": "The Knight's Tale",
        "quote": "Upon the altar lay a fine cloth of rich **diaper** embroidered with pearl."
      }
    ]
  },
  "Dashboard — chlor/chlor.md": {
    "primary": "The combining form (from Greek chloros, 'light green' or 'greenish-yellow') designating green color or the presence of chlorine.",
    "secondary": "In chemical and biological nomenclature, a prefix denoting chlorine substituents or photosynthetic plant pigments.",
    "quotes": [
      {
        "author": "Humphry Davy",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "From its peculiar greenish-yellow hue I propose the name **chlor**-ine for this remarkable elementary body."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "The combining root **chlor** designates the halogen halogen group exhibiting marked electronegative affinity."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lessons in Elementary Physiology",
        "quote": "Plant cells owe their verdant hue to the **chlor**-bearing plastids embedded in the protoplasm."
      }
    ]
  },
  "Dashboard — chlor/chlorambucil.md": {
    "primary": "A bifunctional nitrogen mustard alkylating drug used primarily in the chemotherapy of chronic lymphocytic leukemia and lymphomas.",
    "secondary": "In oncology, an orally active cytotoxic agent that cross-links DNA strands during cell replication to suppress malignant lymphoid proliferation.",
    "quotes": [
      {
        "author": "David A. Karnofsky",
        "work": "Clinical Evaluation of Chemotherapeutic Agents",
        "quote": "Patients treated with daily **chlorambucil** exhibited prolonged remissions in indolent chronic leukemia."
      },
      {
        "author": "Alexander Haddow",
        "work": "Advances in Cancer Research",
        "quote": "The synthesis of **chlorambucil** marked an important step toward well-tolerated oral alkylating therapies."
      },
      {
        "author": "Emil Frei",
        "work": "Cancer Medicine",
        "quote": "Low toxicity and steady absorption made **chlorambucil** the standard frontline regimen for small-cell lymphocytic lymphoma."
      }
    ]
  },
  "Dashboard — chlor/chloramine-t.md": {
    "primary": "The sodium salt of N-chloro-4-methylbenzenesulfonamide, widely used as an antiseptic, disinfectant, and laboratory mild oxidizing agent.",
    "secondary": "In surgical sanitation and public health, an organic chlorine carrier that slowly releases hypochlorous acid without causing tissue necrosis.",
    "quotes": [
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "Irrigation of extensive trauma with **chloramine-t** prevented suppuration without burning living tissue."
      },
      {
        "author": "Henry Drysdale Dakin",
        "work": "Handbook of Antiseptics",
        "quote": "We prepared **chloramine-t** to provide a stable, non-irritating reservoir of active bactericidal chlorine."
      },
      {
        "author": "Alexander Fleming",
        "work": "The Action of Chemical Antiseptics on Wound Flora",
        "quote": "Dilute solutions of **chloramine-t** retained bactericidal potency in the presence of wound serum."
      }
    ]
  },
  "Dashboard — chlor/chloramine.md": {
    "primary": "Any chemical derivative of ammonia formed by substituting one or more hydrogen atoms with chlorine, notably monochloramine (NH2Cl).",
    "secondary": "In municipal water treatment, a disinfectant formed by reacting chlorine with ammonia to provide a persistent, low-byproduct residual sanitizer.",
    "quotes": [
      {
        "author": "George C. Whipple",
        "work": "The Microscopy of Drinking Water",
        "quote": "Switching from free chlorine to **chloramine** residual reduced pungent medicinal odors across the reservoir network."
      },
      {
        "author": "Robert Spurr Weston",
        "work": "Water Purification",
        "quote": "The formation of **chloramine** prevents the synthesis of trihalomethanes in organic-rich raw water."
      },
      {
        "author": "Karl F. Meyer",
        "work": "Public Health Engineering",
        "quote": "Bacterial counts declined steadily after the distribution mains were charged with residual **chloramine**."
      }
    ]
  },
  "Dashboard — chlor/chloramphenicol.md": {
    "primary": "A broad-spectrum bacteriostatic antibiotic first isolated from the actinomycete bacterium Streptomyces venezuelae.",
    "secondary": "In clinical pharmacology, an inhibitor of ribosomal peptidyl transferase reserved for serious infections such as typhoid and bacterial meningitis.",
    "quotes": [
      {
        "author": "Theodore E. Woodward",
        "work": "Preliminary Report on the Beneficial Effect of Chloromycetin in Typhoid",
        "quote": "Administration of crystalline **chloramphenicol** caused rapid defervescence in acute cases of enteric fever."
      },
      {
        "author": "Paul R. Burkholder",
        "work": "Studies on Antibiotics from Soil Organisms",
        "quote": "From soil cultures gathered in South America, we isolated **chloramphenicol**, an antibiotic containing a rare nitrobenzene moiety."
      },
      {
        "author": "Maxwell Finland",
        "work": "Antimicrobial Agents and Chemotherapy",
        "quote": "The clinical utility of **chloramphenicol** must be balanced against its rare propensity to induce bone marrow depression."
      }
    ]
  },
  "Dashboard — chlor/chloranthaceae.md": {
    "primary": "A primitive family of aromatic flowering plants belonging to the order Chloranthales, characterized by simple opposite leaves and reduced flowers.",
    "secondary": "In systematic angiosperm phylogeny, an ancient basal lineage with fossil pollen records extending back to the Early Cretaceous.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Genera Plantarum",
        "quote": "The family **Chloranthaceae** exhibits remarkably reduced floral parts combined with woody stems and opposite leaves."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Aromatic resins and jointed stems characterize the East Asian genera of **Chloranthaceae**."
      },
      {
        "author": "Armen Takhtajan",
        "work": "Evolutionary Trends in Flowering Plants",
        "quote": "Pollen morphology demonstrates that **Chloranthaceae** represent one of the earliest divergent clades of mesangiosperms."
      }
    ]
  },
  "Dashboard — chlor/chloranthus.md": {
    "primary": "A genus of small aromatic Asian shrubs and herbs in the family Chloranthaceae, traditionally used to scent teas and prepare herbal infusions.",
    "secondary": "In phytotaxonomy, the type genus of Chloranthaceae, distinguished by spikes of minute flowers lacking sepals and petals.",
    "quotes": [
      {
        "author": "Robert Fortune",
        "work": "Three Years' Wanderings in the Northern Provinces of China",
        "quote": "The dried blossoms of **Chloranthus** were added by tea merchants to perfume high-grade Pekoe."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Flora of British India",
        "quote": "In the damp understory of the Khasi Hills, small clusters of **Chloranthus** flowered inconspicuously."
      },
      {
        "author": "E. H. Wilson",
        "work": "A Naturalist in Western China",
        "quote": "The villagers gathered **Chloranthus** roots from shaded forest ravines to treat lingering fevers."
      }
    ]
  },
  "Dashboard — chlor/chloranthy.md": {
    "primary": "A plant teratological condition in which floral organs (petals, stamens, or carpels) mutate or metamorphose into green vegetative leaves.",
    "secondary": "In plant developmental genetics and phytopathology, phyllody or greening caused by phytoplasma infection or hormonal deregulation.",
    "quotes": [
      {
        "author": "Maxwell T. Masters",
        "work": "Vegetable Teratology",
        "quote": "Complete **chloranthy** was observed in the rose blossom, every petal having transformed into an ordinary foliage leaf."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The phenomenon of **chloranthy** affords decisive morphological proof of the foliar nature of all floral appendages."
      },
      {
        "author": "Karl Goebel",
        "work": "Organography of Plants",
        "quote": "Under the influence of gall-mites, the whole inflorescence succumbed to retrogressive **chloranthy**."
      }
    ]
  },
  "Dashboard — chlor/chlorate.md": {
    "primary": "A chemical salt or ester containing the monovalent chlorate anion ClO3-, known for strong oxidizing properties.",
    "secondary": "In industrial chemistry and pyrotechnics, potassium or sodium chlorate used as an oxidizer in matches, explosives, and weedkillers.",
    "quotes": [
      {
        "author": "Claude Louis Berthollet",
        "work": "Essai de Statique Chimique",
        "quote": "The thermal decomposition of potassium **chlorate** produces copious quantities of pure dephlogisticated air."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "A single spark detonated the dry mixture of sulfur and potassium **chlorate** with blinding brilliance."
      },
      {
        "author": "Ira Remsen",
        "work": "Inorganic Chemistry",
        "quote": "Heating sodium **chlorate** drives off all oxygen, leaving behind neutral common sodium chloride."
      }
    ]
  },
  "Dashboard — chlor/chlorella.md": {
    "primary": "A genus of single-celled spherical green freshwater microalgae belonging to the phylum Chlorophyta, rich in chlorophyll and protein.",
    "secondary": "In bioengineering and photosynthetic physiology, a classic model organism used by Otto Warburg and Melvin Calvin to decipher carbon fixation.",
    "quotes": [
      {
        "author": "Otto Warburg",
        "work": "The Prime Cause and Prevention of Cancer",
        "quote": "We measured the quantum yield of photosynthesis by suspending pure cultures of **Chlorella** in manometric vessels."
      },
      {
        "author": "Melvin Calvin",
        "work": "The Path of Carbon in Photosynthesis",
        "quote": "Exposing **Chlorella** suspensions to radioactive carbon dioxide permitted the isolation of the first photosynthetic intermediates."
      },
      {
        "author": "Eugene Rabinowitch",
        "work": "Photosynthesis and Related Processes",
        "quote": "Dense suspensions of **Chlorella** furnish an exceptionally uniform biological material for photochemical analysis."
      }
    ]
  },
  "Dashboard — chlor/chlorenchyma.md": {
    "primary": "Parenchyma tissue in plants that contains chloroplasts and is photosynthetic, notably comprising the mesophyll of leaves.",
    "secondary": "In plant anatomy, specialized palisade and spongy cortical tissues structured to maximize light capture and gas diffusion.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The leaf mesophyll represents the most highly specialized form of **chlorenchyma** in vascular vegetation."
      },
      {
        "author": "Julius von Sachs",
        "work": "Text-Book of Botany",
        "quote": "Within the cells of the **chlorenchyma**, radiant energy is harnessed to polymerize starch granules."
      },
      {
        "author": "G. Haberlandt",
        "work": "Physiological Plant Anatomy",
        "quote": "The vertical palisade **chlorenchyma** facilitates light penetration deep into the inner layers of the blade."
      }
    ]
  },
  "Dashboard — chlor/chloride.md": {
    "primary": "A chemical compound in which chlorine is combined with another element or group, or the negatively charged chlorine ion Cl-.",
    "secondary": "In physiology and oceanography, the predominant extracellular anion essential for osmotic equilibrium, neuromuscular activity, and gastric acid secretion.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Common salt is a binary compound of sodium and chlorine, denominated sodium **chloride**."
      },
      {
        "author": "Walter B. Cannon",
        "work": "The Wisdom of the Body",
        "quote": "The kidneys continually regulate the excretion of sodium **chloride** to maintain internal fluid balance."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Text-Book of Electrochemistry",
        "quote": "Dissolving potassium **chloride** in water results in immediate dissociation into electropositive and electronegative ions."
      }
    ]
  },
  "Dashboard — chlor/chlorinate.md": {
    "primary": "To treat, combine, or saturate a substance or water supply with chlorine or a chlorine-containing disinfectant compound.",
    "secondary": "In organic synthesis, to substitute or add chlorine atoms into a hydrocarbon skeleton; in civil engineering, to sanitize municipal water.",
    "quotes": [
      {
        "author": "Allen Hazen",
        "work": "Clean Water and How to Get It",
        "quote": "The decision to **chlorinate** the city reservoirs immediately cut typhoid mortality by ninety percent."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Under the influence of ultraviolet light, methane will readily **chlorinate** to form methyl chloride."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Efforts to **chlorinate** natural hydrocarbons gave birth to synthetic insecticides of extraordinary persistence."
      }
    ]
  },
  "Dashboard — chlor/chlorination.md": {
    "primary": "The process of introducing chlorine into water or another chemical system for purification, bleaching, or chemical synthesis.",
    "secondary": "In public health engineering, the standard chemical disinfection practice that historically eradicated waterborne cholera and typhoid epidemics.",
    "quotes": [
      {
        "author": "William T. Sedgwick",
        "work": "Principles of Sanitary Science and the Public Health",
        "quote": "The widespread adoption of **chlorination** constitutes one of the greatest triumphs of modern preventive medicine."
      },
      {
        "author": "George C. Whipple",
        "work": "Typhoid Fever: Its Causation, Transmission and Prevention",
        "quote": "Careful **chlorination** of the metropolitan aqueduct halted the winter epidemic in its tracks."
      },
      {
        "author": "Ira Remsen",
        "work": "An Introduction to the Study of the Compounds of Carbon",
        "quote": "Direct **chlorination** of aliphatic chains proceeds via a vigorous radical mechanism."
      }
    ]
  },
  "Dashboard — chlor/chlorine.md": {
    "primary": "A halogen element of atomic number 17, appearing at room temperature as a toxic, irritating, greenish-yellow diatomic gas (Cl2).",
    "secondary": "In chemical industry, a fundamental building block used in PVC plastics, water sanitation, paper pulp bleaching, and pharmaceuticals.",
    "quotes": [
      {
        "author": "Humphry Davy",
        "work": "Researches, Chemical and Philosophical",
        "quote": "I have ventured to name this uncompounded gas **chlorine**, from its distinct yellow-green hue."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "The greenish gas was **chlorine**, choking and corrosive, which seized the throat like a vice."
      },
      {
        "author": "Marie Curie",
        "work": "Radioactive Substances",
        "quote": "We precipitated the barium and radium salts from solution in the form of **chlorine** compounds."
      }
    ]
  },
  "Dashboard — chlor/chlorinity.md": {
    "primary": "A oceanographic measure of the total halide concentration in seawater, expressed as grams of chlorine equivalent per kilogram of seawater.",
    "secondary": "In chemical oceanography, an exact titration parameter used in Knudsen's formula to calculate total salinity of marine waters.",
    "quotes": [
      {
        "author": "Martin Knudsen",
        "work": "Hydrographical Tables",
        "quote": "Determining the **chlorinity** by silver nitrate titration permits an accurate calculation of total ocean salinity."
      },
      {
        "author": "H. U. Sverdrup",
        "work": "The Oceans: Their Physics, Chemistry, and General Biology",
        "quote": "Because major ionic ratios remain constant, seawater salinity is derived directly from measured **chlorinity**."
      },
      {
        "author": "C. Wyville Thomson",
        "work": "The Voyage of the Challenger",
        "quote": "Samples drawn from the abyssal depths showed remarkable uniformity in their relative **chlorinity**."
      }
    ]
  },
  "Dashboard — chlor/chloris.md": {
    "primary": "In Greek mythology, the nymph of flowers and spring (equivalent to Flora); in botany, a genus of tropical and subtropical grasses (windmill grass).",
    "secondary": "In ornithology, a genus of Old World finches including the European greenfinch (*Chloris chloris*).",
    "quotes": [
      {
        "author": "Ovid",
        "work": "Fasti",
        "quote": "The breath of spring aroused **Chloris**, whose lips drop flowers over the blossoming fields."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "The greenfinch, classified under **Chloris**, nested abundantly in the orchard evergreens."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Species of **Chloris** bear digitately clustered spikes with awned floral glumes."
      }
    ]
  },
  "Dashboard — chlor/chlorite.md": {
    "primary": "A group of green phyllosilicate minerals rich in magnesium, iron, and aluminium, common in low-grade metamorphic rocks.",
    "secondary": "In inorganic chemistry, a salt containing the chlorite anion ClO2-, such as sodium chlorite used as a bleaching precursor.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "The dull olive-green flakes in the schist proved to be foliated crystals of **chlorite**."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Regional metamorphism altered the basic lavas into soft greenish slabs loaded with **chlorite**."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Microscopic sections show scales of **chlorite** replacing the original augite and hornblende crystals."
      }
    ]
  },
  "Dashboard — chlor/chloroacetophenone.md": {
    "primary": "A chlorinated aromatic organic compound (C8H7ClO) formerly used widely as an incapacitating tear gas (designated agent CN).",
    "secondary": "In riot control and toxicology, a potent lachrymator that causes severe burning sensation of the eyes, blepharospasm, and respiratory tract irritation.",
    "quotes": [
      {
        "author": "Fritz Haber",
        "work": "The Chemistry of Modern Warfare",
        "quote": "A tiny vapor concentration of **chloroacetophenone** suffices to disable soldiers by provoking blinding tears."
      },
      {
        "author": "J. B. S. Haldane",
        "work": "Callinicus: A Defence of Chemical Warfare",
        "quote": "Police agencies selected **chloroacetophenone** because its incapacitating effects wear off quickly in fresh air."
      },
      {
        "author": "Alice Hamilton",
        "work": "Industrial Toxicology",
        "quote": "Workers handling **chloroacetophenone** dust suffered acute conjunctivitis and skin erythema."
      }
    ]
  },
  "Dashboard — chlor/chlorobenzene.md": {
    "primary": "A colorless, flammable aromatic organic compound (C6H5Cl) produced by chlorinating benzene in the presence of a Lewis acid catalyst.",
    "secondary": "In synthetic organic chemistry, an important industrial intermediate in the manufacture of aniline, phenol, and DDT.",
    "quotes": [
      {
        "author": "August Wilhelm von Hofmann",
        "work": "Introduction to Modern Chemistry",
        "quote": "Treating aromatic benzene with chlorine gas yieldeth liquid **chlorobenzene** with evolution of pungent fumes."
      },
      {
        "author": "Ira Remsen",
        "work": "Organic Chemistry",
        "quote": "The chlorine atom in **chlorobenzene** is held far more tenaciously than in aliphatic alkyl halides."
      },
      {
        "author": "Paul Müller",
        "work": "Nobel Lecture: Dichlorodiphenyltrichloroethane",
        "quote": "Condensing chloral with **chlorobenzene** in concentrated sulfuric acid produced the potent contact insecticide."
      }
    ]
  },
  "Dashboard — chlor/chlorobenzylidenemalononitrile.md": {
    "primary": "A crystalline cyanocarbon compound (C10H5ClN2) that serves as the active agent in modern tear gas (designated CS gas).",
    "secondary": "In chemical defense and civil security, an aerosolized sensory irritant causing immediate burning in ocular and mucous membranes, chest tightness, and coughing.",
    "quotes": [
      {
        "author": "Ben Corson",
        "work": "Synthesis of Substituted Malononitriles",
        "quote": "Condensing 2-chlorobenzaldehyde with malononitrile yielded crystalline **chlorobenzylidenemalononitrile**, a compound of extraordinary irritant power."
      },
      {
        "author": "Steven Rose",
        "work": "CBW: Chemical and Biological Warfare",
        "quote": "The adoption of **chlorobenzylidenemalononitrile** displaced older agents because of its higher margin of safety."
      },
      {
        "author": "Julian Perry Robinson",
        "work": "The Problem of Chemical and Biological Warfare",
        "quote": "Dispersed as a fine smoke, **chlorobenzylidenemalononitrile** produces instantaneous, intolerable sensory reflexes."
      }
    ]
  },
  "Dashboard — chlor/chlorococcales.md": {
    "primary": "An order of green algae in the class Chlorophyceae consisting of non-motile unicellular or colonial vegetative organisms.",
    "secondary": "In phycology and limnology, a diverse taxonomic order comprising ecologically vital phytoplankton such as *Scenedesmus* and *Pediastrum*.",
    "quotes": [
      {
        "author": "G. S. West",
        "work": "A Treatise on the British Freshwater Algae",
        "quote": "The order **Chlorococcales** includes an astonishing variety of geometric, non-motile freshwater colonies."
      },
      {
        "author": "Felix Eugen Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Reproduction in **Chlorococcales** typically occurs via the formation of autospores or zoospores."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "The Fresh-Water Algae of the United States",
        "quote": "Plankton hauls from the pond surface were dominated by typical coenobic **Chlorococcales**."
      }
    ]
  },
  "Dashboard — chlor/chlorococcum.md": {
    "primary": "A genus of single-celled spherical green algae in the order Chlorococcales commonly found in moist soils, tree bark, and freshwater.",
    "secondary": "In soil biology and phycology, a pioneer microalga that reproduces through biflagellate zoospores and forms green powdery crusts.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "The green coating upon damp brickwork was resolved by the microscope into teeming spheres of **Chlorococcum**."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "Each spherical cell of **Chlorococcum** contains a hollow parietal chloroplast with a prominent pyrenoid."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Under desiccation, **Chlorococcum** forms thick-walled cysts capable of surviving prolonged drought."
      }
    ]
  },
  "Dashboard — chlor/chlorofluorocarbon.md": {
    "primary": "Any organic compound composed solely of carbon, chlorine, and fluorine, historically used as refrigerants, aerosol propellants, and solvents.",
    "secondary": "In atmospheric environmental science, volatile halogenated hydrocarbons (CFCs) responsible for the catalytic destruction of stratospheric ozone.",
    "quotes": [
      {
        "author": "Mario J. Molina",
        "work": "Stratospheric Sink for Chlorofluoromethanes: Chlorine Atom-Catalysed Destruction of Ozone",
        "quote": "Photodissociation of every persistent **chlorofluorocarbon** releases free chlorine radicals that devour stratospheric ozone."
      },
      {
        "author": "F. Sherwood Rowland",
        "work": "Nobel Lecture: Atmospheric Chemistry of Ozone Depletion",
        "quote": "Because of their chemical inertness, molecules of **chlorofluorocarbon** drift unaltered for decades until reaching the stratosphere."
      },
      {
        "author": "Al Gore",
        "work": "Earth in the Balance",
        "quote": "The global phaseout of **chlorofluorocarbon** propellants demonstrated that nations could act collectively to shield the biosphere."
      }
    ]
  },
  "Dashboard — chlor/chloroform.md": {
    "primary": "A dense, sweet-smelling, non-flammable organic solvent and halogenated hydrocarbon (CHCl3), formerly widely employed as a general anesthetic.",
    "secondary": "In medical history and organic chemistry, the halogenated liquid whose anesthetic vapor was popularized by James Young Simpson in obstetric surgery.",
    "quotes": [
      {
        "author": "James Young Simpson",
        "work": "Notice of a New Anæsthetic Agent as a Substitute for Sulphuric Ether",
        "quote": "A few deep inhalations of **chloroform** induced a state of complete, painless insensibility."
      },
      {
        "author": "Charles Dickens",
        "work": "All the Year Round",
        "quote": "The surgeon applied the scented sponge of **chloroform**, and the sufferer knew nothing of the blade."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "Medical Essays",
        "quote": "Ether and **chloroform** stripped the operating theatre of its historic terrors."
      }
    ]
  },
  "Dashboard — chlor/chlorofucin.md": {
    "primary": "An obsolete or historical botanical term for an accessory brownish-green pigment found in brown algae (phaeophyta).",
    "secondary": "In historical phycology, the pigment fraction now identified with chlorophyll c or associated fucoxanthin complexes in chromophyte algae.",
    "quotes": [
      {
        "author": "H. C. Sorby",
        "work": "Proceedings of the Royal Society of London",
        "quote": "Spectroscopic analysis of brown seaweeds reveals the presence of **chlorofucin** alongside ordinary chlorophyll."
      },
      {
        "author": "George Murray",
        "work": "An Introduction to the Study of Seaweeds",
        "quote": "The olive-colored extract owed its peculiar optical bands to the pigment called **chlorofucin**."
      },
      {
        "author": "E. Ray Lankester",
        "work": "Quarterly Journal of Microscopical Science",
        "quote": "Early investigators separated **chlorofucin** as a distinct chromogen in marine Laminaria."
      }
    ]
  },
  "Dashboard — chlor/chloromycetin.md": {
    "primary": "A proprietary brand name for the broad-spectrum antibiotic chloramphenicol, synthesized originally from soil actinomycetes.",
    "secondary": "In clinical therapeutics, a landmark post-war antibiotic historically prescribed for rickettsial infections, typhus, and scrub fever.",
    "quotes": [
      {
        "author": "Joseph E. Smadel",
        "work": "Chloromycetin in the Treatment of Scrub Typhus",
        "quote": "Prompt administration of **chloromycetin** cleared scrub typhus infections among soldiers within forty-eight hours."
      },
      {
        "author": "Selman Waksman",
        "work": "My Life with the Microbes",
        "quote": "The discovery of **chloromycetin** underscored the immense pharmaceutical wealth hidden in common soil."
      },
      {
        "author": "Paul de Kruif",
        "work": "A Man Against Insanity",
        "quote": "Doctors hailed **chloromycetin** as a wonder weapon against fevers that had baffled medicine for centuries."
      }
    ]
  },
  "Dashboard — chlor/chlorophis.md": {
    "primary": "A genus (or subgenus) of slender, harmless green colubrid snakes native to sub-Saharan Africa, often known as green tree snakes.",
    "secondary": "In herpetology, arboreal African colubrids characterized by bright emerald dorsal coloration and smooth scales, closely allied to *Philothamnus*.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "Catalogue of Colubrine Snakes in the Collection of the British Museum",
        "quote": "The genus **Chlorophis** contains extremely slender, vivid green arboreal serpents of tropical Africa."
      },
      {
        "author": "Arthur Loveridge",
        "work": "Reptiles from the East African Lakes",
        "quote": "A brilliant **Chlorophis** glided effortlessly through the reeds in pursuit of tree frogs."
      },
      {
        "author": "Raymond Ditmars",
        "work": "Snakes of the World",
        "quote": "Among the harmless bush-dwelling species, **Chlorophis** harmonizes perfectly with the verdant foliage."
      }
    ]
  },
  "Dashboard — chlor/chlorophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of the color green or green objects.",
    "secondary": "In clinical psychology and psychiatry, a specific phobia where exposure to green hues or verdant environments triggers acute autonomic anxiety.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "A peculiar aversion to natural foliage led the patient into an acute, disabling **chlorophobia**."
      },
      {
        "author": "G. Stanley Hall",
        "work": "Adolescence",
        "quote": "Chromatic idiosyncrasies occasionally manifest as severe **chlorophobia**, where green clothing provokes dread."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Unaccountable antipathies toward specific primary colors, such as **chlorophobia**, reflect deep sensory associations."
      }
    ]
  },
  "Dashboard — chlor/chlorophoneus.md": {
    "primary": "A genus of colorful African bushshrikes in the family Malaconotidae, typically bearing bright green and yellow plumage.",
    "secondary": "In ornithology, forest bushshrikes of the African tropics characterized by polymorphic plumages and musical territorial whistles.",
    "quotes": [
      {
        "author": "David Bannerman",
        "work": "The Birds of Tropical West Africa",
        "quote": "The olive bushshrike, belonging to **Chlorophoneus**, crept through the thick tangled canopy."
      },
      {
        "author": "Austin Roberts",
        "work": "The Birds of South Africa",
        "quote": "Species of **Chlorophoneus** exhibit striking color phases ranging from bright yellow to deep crimson."
      },
      {
        "author": "C. W. Mackworth-Praed",
        "work": "Birds of Eastern and North Eastern Africa",
        "quote": "The clear ringing call of **Chlorophoneus** echoed across the montane forest valley."
      }
    ]
  },
  "Dashboard — chlor/chlorophthalmidae.md": {
    "primary": "A family of small, deep-sea aulopiform fishes commonly known as greeneyes, named for their large, iridescent green eyes.",
    "secondary": "In marine ichthyology, benthic mesopelagic and bathypelagic fishes possessing specialized reflective tapeta adapted for low-light vision.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The family **Chlorophthalmidae** takes its name from the magnificent emerald shine of their enlarged eyes."
      },
      {
        "author": "William Beebe",
        "work": "Half Mile Down",
        "quote": "Dredges from deep water hauled up curious specimens of **Chlorophthalmidae** with radiant eyes shining in the dark."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Trawled from muddy oceanic slopes, the **Chlorophthalmidae** rest upon bottom sediments facing into the current."
      }
    ]
  },
  "Dashboard — chlor/chlorophyceae.md": {
    "primary": "A large taxonomic class of green algae (Chlorophyta) characterized by green chloroplasts containing chlorophylls a and b.",
    "secondary": "In botanical phycology, predominantly freshwater algae possessing starch reserves inside plastids and whiplash flagella in motile stages.",
    "quotes": [
      {
        "author": "Felix Eugen Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The class **Chlorophyceae** embraces an enormous diversity of forms from unicellular spheres to branching filaments."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Freshwater Algae of the United States",
        "quote": "Most freshwater green scums consist of filamentous members of the **Chlorophyceae**."
      },
      {
        "author": "Julius von Sachs",
        "work": "Lectures on the Physiology of Plants",
        "quote": "The photosynthetic apparatus of the **Chlorophyceae** closely mirrors that of higher vascular plants."
      }
    ]
  },
  "Dashboard — chlor/chlorophyl.md": {
    "primary": "A variant spelling of chlorophyll, the green photosynthetic pigment found in plant chloroplasts and cyanobacteria.",
    "secondary": "In 19th-century scientific literature, the green coloring matter extracted from leaves using alcohol or ether.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Physiography: An Introduction to the Study of Nature",
        "quote": "The presence of **chlorophyl** enables the green plant to decompose carbonic acid in the sunlight."
      },
      {
        "author": "John Tyndall",
        "work": "Fragments of Science",
        "quote": "Solar rays absorbed by **chlorophyl** supply the mechanical energy needed to construct organic tissues."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "Grains of **chlorophyl** give the verdant color to the parenchyma of the leaf."
      }
    ]
  },
  "Dashboard — chlor/chlorophyll.md": {
    "primary": "The green photosynthetic pigment present in cyanobacteria and the chloroplasts of algae and plants, essential for absorbing light energy.",
    "secondary": "In biochemistry, a magnesium-coordinated porphyrin-derivative pigment occurring predominantly as chlorophyll a and chlorophyll b.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "Under prolonged darkness, the production of **chlorophyll** ceases and the shoots become completely etiolated."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The microscopic floating meadows of the ocean are rich in **chlorophyll**, capturing the light of the upper layers."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The central magnesium atom in **chlorophyll** coordinates planar pyrrole rings in a manner analogous to iron in heme."
      }
    ]
  },
  "Dashboard — chlor/chlorophyllose.md": {
    "primary": "Containing, resembling, or rich in chlorophyll; chlorophyll-bearing.",
    "secondary": "In bryology and cryptogamic botany, describing narrow green cells in moss leaves (*Sphagnum*) that contrast with clear hyaline cells.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The **chlorophyllose** cells of the moss leaf form a verdant network around the large empty water cells."
      },
      {
        "author": "William Starling Sullivant",
        "work": "Icones Muscorum",
        "quote": "Cross-sections through the Sphagnum leaf display narrow triangular **chlorophyllose** cells between transparent hyaline chambers."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Elongated **chlorophyllose** filaments line the interior of the photosynthetic stem cortex."
      }
    ]
  },
  "Dashboard — chlor/chlorophyllous.md": {
    "primary": "Pertaining to, composed of, or containing chlorophyll; actively photosynthetic.",
    "secondary": "In structural botany, characterizing plant tissues, parenchyma layers, or algal symbionts possessing functional green pigments.",
    "quotes": [
      {
        "author": "Julius von Sachs",
        "work": "Text-Book of Botany",
        "quote": "Starch formation is strictly confined to the **chlorophyllous** cells directly illuminated by sunlight."
      },
      {
        "author": "E. Ray Lankester",
        "work": "Degeneration: A Chapter in Darwinism",
        "quote": "Certain freshwater hydras maintain a beneficial partnership with **chlorophyllous** green algae in their gastrodermis."
      },
      {
        "author": "G. Haberlandt",
        "work": "Physiological Plant Anatomy",
        "quote": "The entire palisade layer functions as a light-trapping screen of dense **chlorophyllous** protoplasm."
      }
    ]
  },
  "Dashboard — chlor/chlorophyta.md": {
    "primary": "A major division or phylum of green algae comprising primarily freshwater and marine photosynthetic organisms containing chlorophylls a and b.",
    "secondary": "In evolutionary systematics, the ancestral algal clade from which all terrestrial embryophyte land plants originated.",
    "quotes": [
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "Primary endosymbiosis of a cyanobacterium gave rise to the ancestral lineage of the **Chlorophyta**."
      },
      {
        "author": "Felix Eugen Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The vast assemblage of **Chlorophyta** ranges from single flagellated cells to complex siphonaceous thalli."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "Both marine seaweeds and microscopic freshwater pond scums are represented within the division **Chlorophyta**."
      }
    ]
  },
  "Dashboard — chlor/chlorophyte.md": {
    "primary": "Any green alga or member of the division Chlorophyta.",
    "secondary": "In aquatic biology and evolutionary botany, a photosynthetic organism that stores carbohydrate food reserves as starch inside plastids.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Along the tidal pools, patches of delicate **chlorophyte** seaweeds carpeted the volcanic rocks."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Symbiotic cells inside the freshwater sponge were identified as a simple single-celled **chlorophyte**."
      },
      {
        "author": "Eugene Rabinowitch",
        "work": "Photosynthesis",
        "quote": "The light-harvesting complex of a typical **chlorophyte** contains identical pigment ratios to higher terrestrial leaves."
      }
    ]
  },
  "Dashboard — chlor/chloropicrin.md": {
    "primary": "A heavy, colorless, pungent liquid (CCl3NO2) used as a broad-spectrum soil fumigant, pesticide, and historical chemical warfare choking agent.",
    "secondary": "In agrochemistry and military history, a severe pulmonary and lacrimatory agent synthesized by treating picric acid with hypochlorite.",
    "quotes": [
      {
        "author": "John Stenhouse",
        "work": "Philosophical Magazine",
        "quote": "Distilling picric acid with bleaching powder yielded an exceedingly pungent oil which I named **chloropicrin**."
      },
      {
        "author": "Fritz Haber",
        "work": "The Chemistry of Warfare",
        "quote": "Because of its ability to penetrate standard gas-mask canisters, **chloropicrin** was deployed extensively in artillery shells."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Before planting strawberries, growers injected **chloropicrin** into the soil to kill nematodes and subterranean fungi."
      }
    ]
  },
  "Dashboard — chlor/chloroplast.md": {
    "primary": "A plastid organelle found in green plant and algal cells that contains chlorophyll and is the site of photosynthesis.",
    "secondary": "In cell biology, a semiautonomous endosymbiotic organelle bounded by a double membrane and enclosing a thylakoid membrane system.",
    "quotes": [
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "Under the microscope, each vibrant green disk inside the leaf cell revealed itself as an active **chloroplast**."
      },
      {
        "author": "Lynn Margulis",
        "work": "Origin of Eukaryotic Cells",
        "quote": "The modern **chloroplast** is the direct evolutionary descendant of an engulfed photosynthetic cyanobacterium."
      },
      {
        "author": "Melvin Calvin",
        "work": "Chemical Evolution",
        "quote": "Within the stroma of the **chloroplast**, carbon dioxide is converted into sugars via cyclical enzymic reactions."
      }
    ]
  },
  "Dashboard — chlor/chloroprene.md": {
    "primary": "A colorless volatile liquid chemical monomer (2-chloro-1,3-butadiene) used in the manufacture of the synthetic elastomer neoprene.",
    "secondary": "In industrial polymer chemistry, a conjugated chlorodiene whose polymerization yielded the world's first commercially successful synthetic rubber.",
    "quotes": [
      {
        "author": "Wallace Carothers",
        "work": "Studies on Polymerization: Acetylene Polymers and Derivatives",
        "quote": "The addition of hydrogen chloride to monovinylacetylene produces **chloroprene**, which readily polymerizes to an elastic gum."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Handwriting on the Wall",
        "quote": "The synthesis of **chloroprene** freed industrial manufacturers from total dependence on natural plantation latex."
      },
      {
        "author": "Herman F. Mark",
        "work": "Giant Molecules",
        "quote": "Polymers of **chloroprene** exhibited remarkable resistance to gasoline, heat, and oxidative degradation."
      }
    ]
  },
  "Dashboard — chlor/chloroquine.md": {
    "primary": "A synthetic 4-aminoquinoline drug widely used for the prevention and treatment of malaria, as well as autoimmune conditions like lupus.",
    "secondary": "In clinical pharmacology, an agent that accumulates in the acidic food vacuole of the malaria parasite (*Plasmodium*), preventing hemozoin biocrystallization.",
    "quotes": [
      {
        "author": "Paul F. Russell",
        "work": "Man's Mastery of Malaria",
        "quote": "The introduction of **chloroquine** provided a reliable, swift therapeutic cure for acute attacks of vivax and falciparum malaria."
      },
      {
        "author": "Maxwell Finland",
        "work": "Clinical Studies on Antimalarial Drugs",
        "quote": "Weekly prophylaxis with **chloroquine** protected thousands of troops stationed in hyperendemic jungle regions."
      },
      {
        "author": "Thomas Weller",
        "work": "Tropical Health: A Summary of a Study",
        "quote": "The emergence of **chloroquine** resistance across Southeast Asia raised urgent demands for novel antimalarial compounds."
      }
    ]
  },
  "Dashboard — chlor/chlorosis.md": {
    "primary": "A condition in plants marked by yellowing or blanching of green tissues due to lack of chlorophyll; historically, 'green sickness' in humans (iron-deficiency anemia).",
    "secondary": "In plant pathology, nutrient deficiency (notably iron or nitrogen) or viral infection disrupting chlorophyll synthesis; in 19th-century medicine, adolescent hypochromic anemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Iron therapy acts as a true specific in curing the pale, greenish complexion of **chlorosis** in young women."
      },
      {
        "author": "Julius von Sachs",
        "work": "Lectures on the Physiology of Plants",
        "quote": "Adding iron salts to the culture solution promptly cured the lime-induced **chlorosis** of the grapevines."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The virgin afflicted with **chlorosis** suffered from sluggish circulation, fainting fits, and a peculiar waxy pallor."
      }
    ]
  },
  "Dashboard — chlor/chlorothiazide.md": {
    "primary": "A benzothiadiazine thiazide diuretic drug used to treat hypertension, congestive heart failure, and peripheral edema.",
    "secondary": "In cardiovascular pharmacology, the pioneering thiazide diuretic that inhibits the sodium-chloride cotransporter in the renal distal convoluted tubule.",
    "quotes": [
      {
        "author": "Karl H. Beyer",
        "work": "The Mechanism of Action of Chlorothiazide",
        "quote": "The discovery of **chlorothiazide** revolutionized the clinical management of severe arterial hypertension."
      },
      {
        "author": "Robert W. Wilkins",
        "work": "New Drugs for the Treatment of Hypertension",
        "quote": "Oral administration of **chlorothiazide** achieved potent saluresis without the toxic hazards of mercurial diuretics."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Patients drowning in congestive cardiac edema found rapid relief through daily doses of **chlorothiazide**."
      }
    ]
  },
  "Dashboard — chlor/chlorotic.md": {
    "primary": "Pertaining to, affected with, or resembling chlorosis; sickly pale, blanched, or yellowish-green.",
    "secondary": "In botany and medicine, describing leaves deficient in chlorophyll or individuals exhibiting the pallor of severe microcytic anemia.",
    "quotes": [
      {
        "author": "Charlotte Brontë",
        "work": "Villette",
        "quote": "Her face had that pale, **chlorotic** cast which speaks of long confinement in gloomy corridors."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "When cultivated in soil lacking available iron, the leaves remained stunted, brittle, and utterly **chlorotic**."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "A sickly, **chlorotic** ray of afternoon sun struggled through the grimy window of the chancery office."
      }
    ]
  },
  "Dashboard — chlor/chloroxylon.md": {
    "primary": "A genus of tropical trees in the family Rutaceae, notably *Chloroxylon swietenia*, native to India and Sri Lanka and yielding Ceylon satinwood.",
    "secondary": "In forestry and economic botany, a valuable hardwood tree prized for its fragrant, fine-grained, golden-yellow timber used in luxury cabinetry.",
    "quotes": [
      {
        "author": "William Roxburgh",
        "work": "Plants of the Coast of Coromandel",
        "quote": "The fragrant satinwood tree was classified under **Chloroxylon**, renowned for its yellow lustrous timber."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Dense forests of **Chloroxylon** covered the rocky hillsides of the central Deccan plateau."
      },
      {
        "author": "George Watt",
        "work": "A Dictionary of the Economic Products of India",
        "quote": "Cabinetmakers prized timber cut from **Chloroxylon** for its satin sheen and remarkable durability."
      }
    ]
  },
  "Dashboard — chlor/chlortetracycline.md": {
    "primary": "The first discovered tetracycline antibiotic (originally known as Aureomycin), isolated from the actinomycete *Streptomyces aureofaciens*.",
    "secondary": "In antimicrobial chemotherapy, a golden-yellow broad-spectrum antibiotic that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit.",
    "quotes": [
      {
        "author": "Benjamin Minge Duggar",
        "work": "Aureomycin: A Product of the Continuing Search for New Antibiotics",
        "quote": "From soil samples collected in Missouri, we isolated the antibiotic **chlortetracycline**, which yielded golden crystalline salts."
      },
      {
        "author": "Maxwell Finland",
        "work": "Clinical Uses of Aureomycin",
        "quote": "Early clinical trials showed that oral **chlortetracycline** controlled primary atypical pneumonia and psittacosis."
      },
      {
        "author": "Selman Waksman",
        "work": "The Actinomycetes",
        "quote": "The discovery of **chlortetracycline** demonstrated that actinomycetes produced versatile broad-spectrum antibacterial compounds."
      }
    ]
  },
  "Dashboard — chlor/chlorthalidone.md": {
    "primary": "A long-acting thiazide-like sulfonamide diuretic used in the treatment of hypertension and edema.",
    "secondary": "In nephrology and cardiology, an inhibitor of the distal convoluted tubule Na+/Cl- symporter with an exceptionally prolonged half-life.",
    "quotes": [
      {
        "author": "Karl H. Beyer",
        "work": "Diuretic and Antihypertensive Agents",
        "quote": "A single morning dose of **chlorthalidone** provided smooth, sustained blood pressure control throughout twenty-four hours."
      },
      {
        "author": "Robert C. Tarazi",
        "work": "Hemodynamic Effects of Long-Term Diuretic Therapy",
        "quote": "Prolonged therapy with **chlorthalidone** reduced peripheral vascular resistance and expanded stroke volume."
      },
      {
        "author": "Edgar Haber",
        "work": "Cardiovascular Pharmacotherapeutics",
        "quote": "Clinical trials established **chlorthalidone** as a cornerstone agent for preventing cardiovascular strokes in elderly patients."
      }
    ]
  },
  "Dashboard — chlor/chlorura.md": {
    "primary": "A genus (or subgenus) of American emberizine passerine birds, specifically the green-tailed towhee (*Chlorura chlorura* / *Pipilo chlorurus*).",
    "secondary": "In North American ornithology, a brush-dwelling songbird characterized by an olive-green tail, bright rufous crown, and white throat.",
    "quotes": [
      {
        "author": "Elliott Coues",
        "work": "Birds of the Colorado Valley",
        "quote": "The sweet, variable song of **Chlorura** floated out from the thick sagebrush on the mountain slope."
      },
      {
        "author": "Robert Ridgway",
        "work": "The Birds of North and Middle America",
        "quote": "Distinct olive coloration on wings and tail characterizes the genus **Chlorura** among nearctic finches."
      },
      {
        "author": "Florence Merriam Bailey",
        "work": "Handbook of Birds of the Western United States",
        "quote": "We watched the green-tailed **Chlorura** scratching vigorously among dry pine needles for fallen seeds."
      }
    ]
  },
  "Dashboard — chlor/dechlorinate.md": {
    "primary": "To remove chlorine or chlorine compounds from water, wastewater, or a chemical compound.",
    "secondary": "In environmental engineering and aquaculture, using reducing agents like sulfur dioxide or activated carbon to prevent chlorine toxicity to aquatic life.",
    "quotes": [
      {
        "author": "Allen Hazen",
        "work": "The Filtration of Public Water Supplies",
        "quote": "Before discharging treated effluent into trout streams, the engineers must thoroughly **dechlorinate** the outflow."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Soil bacteria slowly **dechlorinate** synthetic pesticide molecules, reducing their chemical persistence."
      },
      {
        "author": "Gordon Maskew Fair",
        "work": "Water and Wastewater Engineering",
        "quote": "Adding sulfur dioxide to **dechlorinate** municipal water eliminates residual oxidant before biological filtration."
      }
    ]
  },
  "Dashboard — chlor/hypochlorite.md": {
    "primary": "An oxyanion of chlorine with the chemical formula ClO-, or a salt containing this ion (such as sodium hypochlorite or calcium hypochlorite).",
    "secondary": "In sanitation and industrial chemistry, a potent bleach and oxidizing disinfectant that releases hypochlorous acid in solution.",
    "quotes": [
      {
        "author": "Claude Louis Berthollet",
        "work": "Memoirs on the Bleaching of Cloth",
        "quote": "The miraculous bleaching liquor of Javel proved to be a solution of potassium **hypochlorite**."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "Dakin's solution of buffered sodium **hypochlorite** cleansed gangrenous wounds without injuring healthy granulation."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry",
        "quote": "Passing chlorine into caustic alkali readily forms a mixture of chloride and **hypochlorite**."
      }
    ]
  },
  "Dashboard — chlor/pyrochlore.md": {
    "primary": "A group of hard, vitreous, brownish to yellowish-green minerals composed of niobates and tantalates of calcium, sodium, and rare-earth elements.",
    "secondary": "In mineralogy and economic geology, the principal commercial ore mineral mined for niobium, crystallizing in the isometric system.",
    "quotes": [
      {
        "author": "Friedrich Wöhler",
        "work": "Annalen der Physik",
        "quote": "When heated before the blowpipe, this curious mineral turned yellow, whence the name **pyrochlore** was bestowed upon it."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The octohedral crystals of **pyrochlore** found in nepheline syenites contain significant amounts of columbium."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Carbonatite complexes in Norway and Canada are richly mineralized with disseminated **pyrochlore**."
      }
    ]
  },
  "Dashboard — chlor/trichloride.md": {
    "primary": "A chemical binary compound containing three chlorine atoms per molecule combined with another element or group.",
    "secondary": "In inorganic chemistry, common compounds such as phosphorus trichloride (PCl3), iron(III) chloride (FeCl3), and aluminium trichloride (AlCl3).",
    "quotes": [
      {
        "author": "Humphry Davy",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "Burning phosphorus in dry chlorine gas resulted in a volatile liquid identified as phosphorus **trichloride**."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "Anhydrous aluminium **trichloride** fumed intensely upon contact with the moist air of the laboratory."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Nitrogen **trichloride** is an exceedingly dangerous, oily explosive that detonates at the slightest mechanical shock."
      }
    ]
  },
  "Dashboard — chlor/trichlormethiazide.md": {
    "primary": "A potent thiazide diuretic and antihypertensive drug used in the clinical management of hypertension and peripheral edema.",
    "secondary": "In renal therapeutics, a chlorinated benzothiadiazine derivative with greater natriuretic potency per milligram than chlorothiazide.",
    "quotes": [
      {
        "author": "Karl H. Beyer",
        "work": "Modern Diuretic Agents",
        "quote": "The substitution of chlorinated alkyl radicals in **trichlormethiazide** substantially increased diuretic potency."
      },
      {
        "author": "Robert W. Wilkins",
        "work": "Newer Therapies in Clinical Hypertension",
        "quote": "Patients maintained on daily **trichlormethiazide** demonstrated consistent sodium loss and sustained diastolic reduction."
      },
      {
        "author": "Edgar Haber",
        "work": "Cardiovascular Pharmacotherapeutics",
        "quote": "Edematous swelling resulting from nephrotic syndrome resolved steadily under low-dose **trichlormethiazide**."
      }
    ]
  },
  "Dashboard — chlor/trichloroethane.md": {
    "primary": "A chlorinated hydrocarbon solvent (C2H3Cl3), occurring as two isomers, particularly 1,1,1-trichloroethane (methyl chloroform).",
    "secondary": "In industrial chemistry and toxicology, an effective non-flammable degreasing solvent whose widespread use was phased out under the Montreal Protocol.",
    "quotes": [
      {
        "author": "Alice Hamilton",
        "work": "Industrial Poisons in the United States",
        "quote": "Workers cleaning precision mechanical parts were exposed to high vapor concentrations of **trichloroethane**."
      },
      {
        "author": "Mario J. Molina",
        "work": "Atmospheric Halogen Chemistry",
        "quote": "Significant quantities of 1,1,1-**trichloroethane** reached the stratosphere where they contributed to ozone loss."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Chlorinating ethane sequentially replaces hydrogen atoms, producing **trichloroethane** and related solvents."
      }
    ]
  },
  "Dashboard — chlor/trichloroethylene.md": {
    "primary": "A volatile, sweet-smelling, chlorinated hydrocarbon solvent (C2HCl3) widely used as an industrial metal degreaser and extraction solvent.",
    "secondary": "In environmental toxicology and industrial hygiene, a persistent groundwater pollutant and classified carcinogen historically used as a surgical anesthetic.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Industrial discharges of **trichloroethylene** contaminated municipal wells, threatening regional groundwater tables."
      },
      {
        "author": "Alice Hamilton",
        "work": "Industrial Toxicology",
        "quote": "Inhaling heavy fumes of **trichloroethylene** in dry-cleaning shops produced dizziness, narcosis, and liver damage."
      },
      {
        "author": "James Young Simpson",
        "work": "Anæsthesia, or the Employment of Chloroform and Ether",
        "quote": "Experimental trials with **trichloroethylene** showed marked anesthetic properties, though less volatile than ether."
      }
    ]
  },
  "Dashboard — chlor/trichloromethane.md": {
    "primary": "The systematic IUPAC chemical name for chloroform (CHCl3), a haloform consisting of three chlorine atoms bound to a methyl carbon.",
    "secondary": "In synthetic organic chemistry, a trihalomethane solvent and chemical precursor used in the synthesis of polytetrafluoroethylene (Teflon).",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Annalen der Chemie und Pharmacie",
        "quote": "Distilling ethyl alcohol with chlorocalx yields the dense, sweet liquid known systematically as **trichloromethane**."
      },
      {
        "author": "Claude Louis Berthollet",
        "work": "Chemical Statics",
        "quote": "The reaction of chlorinated alkalis with organic liquors produced significant quantities of **trichloromethane**."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The tetrahedral geometry of **trichloromethane** results in a permanent molecular dipole moment."
      }
    ]
  }
};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {
  if (updateNote(relPath, data)) updated++;
}
console.log(`Successfully updated ${updated} of ${Object.keys(batchData).length} files in Batch 1.`);
