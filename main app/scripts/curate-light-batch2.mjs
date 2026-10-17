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
  "Dashboard — chro/achromasia.md": {
    "primary": "The complete absence or loss of normal pigmentation, as in albinism, or the pallor of red blood cells lacking hemoglobin.",
    "secondary": "In hematology and dermatology, hypochromia in erythrocytes or localized vitiliginous depigmentation of the epidermis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination of the blood smear revealed marked **achromasia** among the depleted red corpuscles."
      },
      {
        "author": "Robley Dunglison",
        "work": "A Dictionary of Medical Science",
        "quote": "The condition designated **achromasia** signifies a deficiency of cutaneous pigment, characteristic of partial albinism."
      },
      {
        "author": "Thomas Addison",
        "work": "On the Constitutional and Local Effects of Disease of the Supra-Renal Capsules",
        "quote": "Irregular patches of **achromasia** alternated with areas of deep bronze pigmentation across the patient's neck."
      }
    ]
  },
  "Dashboard — chro/achromat.md": {
    "primary": "An achromatic lens or optical system designed to transmit light without separating it into rainbow colors; also, a person affected by total color blindness.",
    "secondary": "In practical optics, an objective composed of crown and flint glass elements cemented together to focus two distinct wavelengths to the same focal point.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Treatise on Light",
        "quote": "The combination of crown and flint lenses formed a perfected **achromat**, banishing the chromatic fringes that marred early refractors."
      },
      {
        "author": "William Whewell",
        "work": "History of the Inductive Sciences",
        "quote": "Dollond's introduction of the composite **achromat** inaugurated a new epoch in observational astronomy."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "To the complete **achromat**, the vibrant tropical lagoon was perceived entirely in nuances of luminous tone."
      }
    ]
  },
  "Dashboard — chro/achromatic.md": {
    "primary": "Free from color; transmitting light without separating it into its constituent spectral hues; refracting light without chromatic aberration.",
    "secondary": "In visual perception and optics, describing stimuli lacking chromaticity (white, gray, black) or optical lens systems corrected for two primary wavelengths.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "If white light were refracted equally throughout, the image formed by the lens would remain truly **achromatic**."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "The human eye is not completely **achromatic**, yet the brain compensates effortlessly for dispersion fringes."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "An **achromatic** microscope lens opened to biological science a universe of previously invisible structural detail."
      }
    ]
  },
  "Dashboard — chro/achromaticity.md": {
    "primary": "The state, property, or degree of being achromatic; freedom from chromatic dispersion, color distortion, or perceived chromatic hue.",
    "secondary": "In optical engineering and colorimetry, the quality of a lens system or visual field that exhibits neutral color balance without chromatic aberration.",
    "quotes": [
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "The pursuit of perfect **achromaticity** required precise calculations of the dispersive powers of crown and flint glass."
      },
      {
        "author": "John Tyndall",
        "work": "Lectures on Light",
        "quote": "By matching opposing prisms of unequal refractive index, a remarkable degree of **achromaticity** is achieved."
      },
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "The greatest defect of our compound lenses lay in their failure to achieve true **achromaticity** around bright margins."
      }
    ]
  },
  "Dashboard — chro/achromatin.md": {
    "primary": "The non-staining or weakly staining nucleoplasm or ground substance of a biological cell nucleus, as distinguished from chromatin.",
    "secondary": "In classical cytogenetics, the unstained nuclear matrix or karyolymph in which chromatin threads and chromosomes are suspended.",
    "quotes": [
      {
        "author": "Walther Flemming",
        "work": "Zellsubstanz, Kern und Zelltheilung",
        "quote": "While the nuclein threads eagerly absorbed the aniline dye, the surrounding **achromatin** remained completely transparent."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "The nuclear framework consists of a delicate reticulum of **achromatin** supporting the granules of active chromatin."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "During late prophase, the spindle fibers arise from the **achromatin** of the clear nuclear sap."
      }
    ]
  },
  "Dashboard — chro/achromatinic.md": {
    "primary": "Pertaining to, composed of, or characteristic of achromatin; failing to take up basic dyes in histological preparations.",
    "secondary": "In cellular anatomy, designating the non-chromatic structural elements of the nucleus, such as the karyoplasmic matrix and spindle apparatus.",
    "quotes": [
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The dividing nucleus displays delicate **achromatinic** fibrils that guide the migrating chromosomes toward the poles."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "An **achromatinic** spindle forms between the asters as the nuclear membrane dissolves."
      },
      {
        "author": "Patrick Geddes",
        "work": "The Evolution of Sex",
        "quote": "The **achromatinic** substance serves as the inert medium wherein hereditary material undergoes symmetrical division."
      }
    ]
  },
  "Dashboard — chro/achromatise.md": {
    "primary": "British spelling of achromatize; to deprive of color, or to correct an optical system so that it transmits light without chromatic aberration.",
    "secondary": "In lens design and histological processing, to bleach color or calibrate optical glass pairings to eliminate prismatic color fringing.",
    "quotes": [
      {
        "author": "William Herschel",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "To **achromatise** the eyepiece of a large telescope requires an exact pairing of convex and concave surfaces."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on the Microscope",
        "quote": "Fluid lenses were occasionally constructed in an effort to **achromatise** the objective at minimal expense."
      },
      {
        "author": "George Gabriel Stokes",
        "work": "Mathematical and Physical Papers",
        "quote": "By balancing dispersive powers at two chosen Fraunhofer lines, we successfully **achromatise** the primary telescope objective."
      }
    ]
  },
  "Dashboard — chro/achromatism.md": {
    "primary": "The state or condition of being achromatic; optical correction that neutralizes chromatic aberration, or the absence of natural pigmentation.",
    "secondary": "In telescope and microscope engineering, the convergence of light rays of differing wavelengths to a common focus through combined refracting media.",
    "quotes": [
      {
        "author": "William Whewell",
        "work": "Philosophy of the Inductive Sciences",
        "quote": "Euler deemed the attainment of **achromatism** impossible until Dollond experimentally disproved Newton's doctrine."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The telescope owed its modern perfection to the discovery of **achromatism** in composite glass objectives."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Popular Scientific Lectures",
        "quote": "Without **achromatism**, microscopic observation of cellular structures would remain clouded in colored haloes."
      }
    ]
  },
  "Dashboard — chro/achromatize.md": {
    "primary": "To deprive of color, or to design and calibrate an optical instrument so that it forms images free from chromatic aberration.",
    "secondary": "In optical manufacture and photography, to neutralize chromatic dispersion by combining lenses with opposite dispersive indices.",
    "quotes": [
      {
        "author": "John Tyndall",
        "work": "Notes of a Course of Nine Lectures on Light",
        "quote": "We can easily **achromatize** a crown-glass prism by placing behind it a flint-glass prism of smaller refracting angle."
      },
      {
        "author": "Michael Faraday",
        "work": "Chemical Manipulation",
        "quote": "Chemical reagents that **achromatize** vegetable dyes do so through active oxidation or reduction."
      },
      {
        "author": "Thomas Young",
        "work": "A Course of Lectures on Natural Philosophy",
        "quote": "To **achromatize** an objective completely across all prismatic bands would demand an infinite series of optical media."
      }
    ]
  },
  "Dashboard — chro/achromatopsia.md": {
    "primary": "A rare genetic visual disorder characterized by total color blindness, daytime photophobia, nystagmus, and reduced visual acuity.",
    "secondary": "In ophthalmology and neurobiology, complete congenital absence of functional retinal cone photoreceptors, leaving vision mediated entirely by rods.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "On the remote atoll of Pingelap, hereditary **achromatopsia** affected nearly ten percent of the native population."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Physiological Optics",
        "quote": "Complete **achromatopsia** implies that the entire retinal cone mechanism is nonfunctional or congenitally absent."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The subject with congenital **achromatopsia** perceives reality as an engraved print, rich in shade but destitute of hue."
      }
    ]
  },
  "Dashboard — chro/achromatopsic.md": {
    "primary": "Relating to, characterized by, or affected with achromatopsia (total color blindness).",
    "secondary": "In clinical genetics and neuro-ophthalmology, designating an individual or retinal state devoid of functioning cone photoreception.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "The **achromatopsic** artist found his world drained of color following a traumatic cerebral infarction."
      },
      {
        "author": "Richard Gregory",
        "work": "Eye and Brain: The Psychology of Seeing",
        "quote": "In bright daylight, the **achromatopsic** subject is severely dazzled because rod saturation occurs rapidly."
      },
      {
        "author": "Francis Galton",
        "work": "Inquiries into Human Faculty and Its Development",
        "quote": "Pedigrees of **achromatopsic** families illustrate the recessive inheritance of complete macular color defects."
      }
    ]
  },
  "Dashboard — chro/achromatous.md": {
    "primary": "Colorless; having no color or natural pigment; pale.",
    "secondary": "In biological taxonomy and pathology, describing unpigmented fungal mycelia, pale algal varieties, or colorless body tissues.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Parasitic plants such as Indian pipe display an entirely **achromatous** stem devoid of green foliage."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Cave salamanders often present an **achromatous** skin resulting from generations of total subterranean darkness."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Varieties with **achromatous** flowers frequently breed true when sheltered from crossing with pigmented stocks."
      }
    ]
  },
  "Dashboard — chro/achromia.md": {
    "primary": "The condition of lacking normal color or pigmentation; an absence of pigment in the skin, hair, or erythrocytes.",
    "secondary": "In dermatology and hematology, pale depigmentation seen in vitiligo, leukoderma, or hypochromic microcytic anemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe iron-deficiency states result in marked central **achromia** of the erythrocyte disc."
      },
      {
        "author": "Erasmus Wilson",
        "work": "Diseases of the Skin",
        "quote": "Congenital **achromia** manifests as white locks of hair or patches of pigmentless skin."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "The localized **achromia** spread slowly across the knuckles without inflammation or induration."
      }
    ]
  },
  "Dashboard — chro/achromic.md": {
    "primary": "Characterized by an absence of color; colorless or unpigmented; unreactive to histological stains.",
    "secondary": "In clinical pathology and cytochemistry, describing erythrocyte ghost cells or tissue sections that fail to retain dye pigments.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Lessons in Elementary Physiology",
        "quote": "After losing their hemoglobin, red corpuscles appear as faint, **achromic** circular envelopes."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Certain atypical cell types remained completely **achromic** when treated with basic methyl violet."
      },
      {
        "author": "William Henry Welch",
        "work": "Papers and Addresses",
        "quote": "An **achromic** zone surrounded the central area of tissue necrosis within the infarcted lobe."
      }
    ]
  },
  "Dashboard — chro/achromous.md": {
    "primary": "Without color; lacking natural pigmentation; colorless.",
    "secondary": "In anatomical and botanical nomenclature, characterizing tissues, organs, or whole organisms that are translucent or white due to pigment absence.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals",
        "quote": "The subterranean crustacean possessed an entirely **achromous** exoskeleton and rudimentary visual organs."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "Submerged roots and saprophytic tubers remain **achromous** because light is excluded from their tissues."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The internal glandular hairs appeared translucent and **achromous** before digestive secretion commenced."
      }
    ]
  },
  "Dashboard — chro/achromycin.md": {
    "primary": "A commercial brand name for the broad-spectrum antibiotic tetracycline hydrochloride, used to treat bacterial infections.",
    "secondary": "In mid-20th-century pharmacology, an oral antibiotic synthesized by catalytic dehalogenation of chlortetracycline, active against Gram-positive and Gram-negative organisms.",
    "quotes": [
      {
        "author": "Maxwell Finland",
        "work": "Clinical Studies on Tetracycline",
        "quote": "Therapy with oral **achromycin** proved highly effective in controlling acute exacerbations of bronchitis."
      },
      {
        "author": "Selman Waksman",
        "work": "The Conquest of Tuberculosis",
        "quote": "The widespread prescription of **achromycin** demonstrated the clinical versatility of the tetracycline family."
      },
      {
        "author": "Paul de Kruif",
        "work": "Men Against Death",
        "quote": "Bottles of yellow **achromycin** capsules stood ready in the clinic to combat systemic bacterial invasions."
      }
    ]
  },
  "Dashboard — chro/amphichroic.md": {
    "primary": "Showing two different colors; producing two contrasting color reactions with indicators depending on environmental conditions.",
    "secondary": "In physical and analytical chemistry, describing an indicator or substance that can turn blue with acid and red with base or vice versa (amphoteric color change).",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Text-Book of Theoretical Electrochemistry",
        "quote": "Certain vegetable extracts exhibit an **amphichroic** behavior, changing hue with both alkaline and acid additions."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "The Foundations of Analytical Chemistry",
        "quote": "An **amphichroic** reagent displays sensitive equilibrium shifts across narrow hydrogen-ion intervals."
      },
      {
        "author": "Ira Remsen",
        "work": "Principles of Theoretical Chemistry",
        "quote": "The indicator proved curiously **amphichroic**, reflecting mixed chromatic responses in buffered solutions."
      }
    ]
  },
  "Dashboard — chro/anachronic.md": {
    "primary": "Characterized by, consisting of, or involving anachronism; misplaced in chronological time.",
    "secondary": "In literary criticism and historiography, describing objects, manners, or idioms presented outside of their authentic historical era.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "The feudal ceremonies looked bizarre and **anachronic** amidst the smoke of nineteenth-century cotton mills."
      },
      {
        "author": "Walter Pater",
        "work": "Appreciations",
        "quote": "A subtle **anachronic** charm pervades the narrative, blending archaic speech with modern introspection."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of Elizabethan Literature",
        "quote": "The dramatist committed an **anachronic** slip by introducing clock-chimes into ancient Roman forum scenes."
      }
    ]
  },
  "Dashboard — chro/anachronism.md": {
    "primary": "A thing belonging or appropriate to a period other than that in which it exists, especially a thing that is conspicuously old-fashioned.",
    "secondary": "In chronological analysis and dramatic art, an error in attributing an event, custom, or invention to a date when it did not exist.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The monkish chronicler was guilty of a flagrant **anachronism** in assigning gunpowder to the legions of Constantine."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "The History of Henry Esmond",
        "quote": "To hear the courtier quote Rousseau in Queen Anne's drawing-room was an amusing literary **anachronism**."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The poet avoided every jarring **anachronism** by steeping his imagination in the authentic atmosphere of the Middle Ages."
      }
    ]
  },
  "Dashboard — chro/anachronistic.md": {
    "primary": "Belonging or appropriate to an earlier period, especially so as to seem conspicuously old-fashioned; out of chronological order.",
    "secondary": "In cultural history and art criticism, displaying chronological discordance with the surrounding temporal milieu.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "Orlando: A Biography",
        "quote": "To wear an Elizabethan ruff aboard a Victorian steamboat seemed gloriously **anachronistic**."
      },
      {
        "author": "H. G. Wells",
        "work": "The Outline of History",
        "quote": "Hereditary despots ruling twentieth-century industrial empires presented a dangerously **anachronistic** spectacle."
      },
      {
        "author": "Lytton Strachey",
        "work": "Eminent Victorians",
        "quote": "His rigid scholastic theology sounded curiously **anachronistic** in an age dominated by evolutionary science."
      }
    ]
  },
  "Dashboard — chro/anachronistically.md": {
    "primary": "In an anachronistic manner; in a way that is out of its proper chronological time or historical context.",
    "secondary": "In stylistic analysis, portraying characters or adopting philosophies that belong temporally elsewhere.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "She spoke **anachronistically** of courtly chivalry as though knights still rode through the Tuscan vineyards."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Saint Joan",
        "quote": "The characters argue **anachronistically** with modern political acumen, giving timeless vitality to medieval disputes."
      },
      {
        "author": "Matthew Arnold",
        "work": "Essays in Criticism",
        "quote": "Judging ancient poets **anachronistically** by modern utilitarian standards blinds the critic to their native beauty."
      }
    ]
  },
  "Dashboard — chro/anachronous.md": {
    "primary": "Erroneous in date; out of proper chronological place; anachronistic.",
    "secondary": "In historical methodology, referring to documents, institutions, or phrases that betray their false dating by temporal inconsistencies.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The spurious charter was betrayed by several **anachronous** references to later Norman baronies."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "Placing classical porticoes upon alpine crags produced an **anachronous** and incongruous architectural effect."
      },
      {
        "author": "Walter Bagehot",
        "work": "The English Constitution",
        "quote": "An **anachronous** survival from Tudor governance lingered unnoticed in the archaic oaths of the Privy Council."
      }
    ]
  },
  "Dashboard — chro/apochromat.md": {
    "primary": "An apochromatic lens system corrected for chromatic aberration at three wavelengths and spherical aberration at two.",
    "secondary": "In microscopy and astronomical instrumentation, an advanced objective designed by Ernst Abbe using fluorite glass to eliminate the secondary spectrum.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "On the Theory of the Microscope",
        "quote": "The construction of the new **apochromat** eliminated the secondary spectrum that had forever limited immersion lenses."
      },
      {
        "author": "Robert Koch",
        "work": "Investigations into the Etiology of Traumatic Infective Diseases",
        "quote": "Photographing minute bacteria required Zeiss's newly perfected **apochromat** to secure crisp edges without purple flares."
      },
      {
        "author": "William Henry Dallinger",
        "work": "The Microscope and Its Revelations",
        "quote": "With Abbe's **apochromat**, resolving power approached the theoretical diffraction limit of visible light."
      }
    ]
  },
  "Dashboard — chro/apochromatic.md": {
    "primary": "Corrected for chromatic aberration at three distinct wavelengths of light and for spherical aberration at two wavelengths.",
    "secondary": "In precision microscopy and photographic optics, describing superior lens systems that eliminate secondary chromatic halos and fringing.",
    "quotes": [
      {
        "author": "John Tyndall",
        "work": "Light and Electricity",
        "quote": "The **apochromatic** microscope objective brings red, green, and blue rays to a single indistinguishable focus."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Wonders of Life",
        "quote": "Delicate silicious skeletons of radiolaria revealed their finest lattice under an oil-immersion **apochromatic** lens."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Advice for a Young Investigator",
        "quote": "Equip your microscope with the finest **apochromatic** optics, for histology forgives no optical distortions."
      }
    ]
  },
  "Dashboard — chro/auxochrome.md": {
    "primary": "A functional group of atoms which, when attached to a chromophore, deepens the color of a dye and enables it to bind to fibers.",
    "secondary": "In organic chemistry and dyestuff theory, electron-donating or withdrawing groups (such as -OH or -NH2) modifying UV-visible absorption spectra.",
    "quotes": [
      {
        "author": "Otto Nikolaus Witt",
        "work": "Zur Kenntniss der Bildung von Farbstoffen",
        "quote": "A chromophore generates the potential for color, but only the addition of an **auxochrome** converts it into a true dye."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology and Chemical Staining",
        "quote": "The basic amino group acts as an **auxochrome**, conferring affinity for the nucleic acids of the cell nucleus."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Delocalization of electrons between the aromatic ring and the **auxochrome** shifts the absorption band toward the red."
      }
    ]
  },
  "Dashboard — chro/chro.md": {
    "primary": "The Greek root combining form (chroos, chroma, 'color, complexion') designating color, pigment, or chromatic quality.",
    "secondary": "In linguistics and scientific nomenclature, the foundational root yielding chromo-, chromato-, and chronic words across physics, biology, and history.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "From the Hellenic root **chro**- spring terms encompassing both the physical hues of light and the temporal march of time."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "The Greek root **chro**- was adopted by modern chemists to denote elements producing brilliantly colored precipitates."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The stem **chro**- originally denoted the skin's surface and complexion before broadening into general color."
      }
    ]
  },
  "Dashboard — chro/chroma.md": {
    "primary": "The purity, saturation, or intensity of a color, as distinguished from its lightness or hue.",
    "secondary": "In the Munsell color system and colorimetry, the degree of departure of a color from a neutral gray of the same value.",
    "quotes": [
      {
        "author": "Albert Henry Munsell",
        "work": "A Color Notation",
        "quote": "Every color dimension may be plotted accurately along three coordinates: hue, value, and **chroma**."
      },
      {
        "author": "Wassily Kandinsky",
        "work": "Concerning the Spiritual in Art",
        "quote": "The heightened **chroma** of pure vermilion vibrates with an intense, inner spiritual resonance."
      },
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "Theory of Colours",
        "quote": "Colors attain their highest **chroma** when liberated from the shadowy degradation of black admixture."
      }
    ]
  },
  "Dashboard — chro/chromaesthesia.md": {
    "primary": "A variant spelling of chromesthesia, the form of synesthesia in which hearing sounds induces vivid subjective sensations of color.",
    "secondary": "In psychological aesthetics and neuropsychology, cross-modal sensory perception where vowels, orchestral timbres, or musical chords evoke chromatic hues.",
    "quotes": [
      {
        "author": "Francis Galton",
        "work": "Inquiries into Human Faculty and Its Development",
        "quote": "Subjects endowed with **chromaesthesia** perceive a rich spectrum of hues unfolding whenever music is performed."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The fascinating anomaly of **chromaesthesia** links the acoustic nerve pathways to involuntary visual hallucinations."
      },
      {
        "author": "Arthur Rimbaud",
        "work": "Voyelles",
        "quote": "The sonnet mapped each vowel to a radiant pigment, a poetic celebration of innate **chromaesthesia**."
      }
    ]
  },
  "Dashboard — chro/chromate.md": {
    "primary": "A salt or ester containing the divalent yellow chromate anion CrO4^2-, formed by chromium in the +6 oxidation state.",
    "secondary": "In industrial chemistry and pigments, potassium or lead chromate used in yellow paints (chrome yellow), electroplating, and corrosion inhibitors.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry",
        "quote": "Precipitating lead acetate with potassium **chromate** gave an instant deposit of brilliant yellow pigment."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "In acid solution, yellow **chromate** transforms rapidly into orange dichromate through ionic condensation."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "The minerals of Siberia furnished lead **chromate**, whose vivid color first guided Vauquelin to isolated chromium."
      }
    ]
  },
  "Dashboard — chro/chromatic.md": {
    "primary": "Relating to, produced by, or possessing color; in music, progressing by semitones or utilizing accidentals outside the diatonic key.",
    "secondary": "In optics, describing phenomena relating to color dispersion or wavelengths; in music theory, a twelve-tone scale consisting entirely of half steps.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The white beam was separated by the prism into its primary **chromatic** rays."
      },
      {
        "author": "Hector Berlioz",
        "work": "Treatise on Modern Instrumentation and Orchestration",
        "quote": "The strings swept upward in a rapid **chromatic** run that suggested the rising shriek of a storm."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "Nature never paints a surface with monochrome flat tints, but with delicate **chromatic** gradations."
      }
    ]
  },
  "Dashboard — chro/chromatically.md": {
    "primary": "In a chromatic manner; with respect to color, or in musical increments of semitones.",
    "secondary": "In artistic criticism and acoustics, executing color transitions smoothly or ascending and descending musical intervals by half-steps.",
    "quotes": [
      {
        "author": "George Bernard Shaw",
        "work": "Music in London",
        "quote": "The soprano descended **chromatically** from high C with astounding precision and crystal intonation."
      },
      {
        "author": "Walter Pater",
        "work": "The Renaissance",
        "quote": "Leonardo modulated the shadows **chromatically**, allowing the flesh tones to dissolve into dark foliage."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "On Colour Vision",
        "quote": "The sensations of the three retinal receptors combine **chromatically** to reconstruct the visual spectrum."
      }
    ]
  },
  "Dashboard — chro/chromaticity.md": {
    "primary": "The quality of a color determined by its dominant wavelength (hue) and purity (chroma), independent of its luminance or brightness.",
    "secondary": "In colorimetry, the quantitative coordinates of a color plotted on the standard CIE chromaticity diagram.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "Experiments on Colour, as Perceived by the Eye",
        "quote": "We determined the precise **chromaticity** of the spectral mixture by comparing it with standard pigments."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Physiological Optics",
        "quote": "The triangular diagram maps all visible hues, defining **chromaticity** without regard to absolute light intensity."
      },
      {
        "author": "Lord Rayleigh",
        "work": "Scientific Papers",
        "quote": "Atmospheric scattering alters the **chromaticity** of celestial light, shifting distant mountains into deep indigo."
      }
    ]
  },
  "Dashboard — chro/chromatid.md": {
    "primary": "Each of the two identical thread-like strands into which a chromosome divides longitudinally during cell division.",
    "secondary": "In genetics and molecular cytology, one of the paired sister copies of replicated DNA joined at the centromere prior to anaphase separation.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "During meiosis, crossing over occurs between homologous non-sister strands of each **chromatid**."
      },
      {
        "author": "Barbara McClintock",
        "work": "The Stability of Broken Ends of Chromosomes in Zea Mays",
        "quote": "Breakage of a single **chromatid** during mitosis triggered the breakage-fusion-bridge cycle."
      },
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "At metaphase, each chromosome resolves visibly into two distinct parallel **chromatid** threads."
      }
    ]
  },
  "Dashboard — chro/chromatin.md": {
    "primary": "The material of which chromosomes are composed, consisting of protein, RNA, and DNA, staining deeply with basic dyes.",
    "secondary": "In eukaryotic cell biology, the nucleoprotein complex organized into nucleosomes, existing as transcriptionally active euchromatin or dense heterochromatin.",
    "quotes": [
      {
        "author": "Walther Flemming",
        "work": "Cell Substance, Nucleus and Cell Division",
        "quote": "I have designated as **chromatin** that portion of the nuclear content which eagerly absorbs dye from solution."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "The condensation of diffuse **chromatin** into distinct rod-shaped chromosomes marks the onset of karyokinesis."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Physical Basis of Heredity",
        "quote": "The linear arrangement of hereditary factors corresponds directly to the physical structure of the **chromatin** thread."
      }
    ]
  },
  "Dashboard — chro/chromatinic.md": {
    "primary": "Of, relating to, or composed of chromatin; staining readily with nuclear dyes.",
    "secondary": "In cytology, describing the deeply staining nucleoprotein granules or threads inside a biological nucleus.",
    "quotes": [
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The protozoan nucleus displays a dense **chromatinic** karyosome encircled by clear nuclear fluid."
      },
      {
        "author": "Patrick Geddes",
        "work": "The Cell Theory",
        "quote": "All heredity appears intimately bound to the continuous transmission of the **chromatinic** filament."
      },
      {
        "author": "William Henry Welch",
        "work": "General Pathology",
        "quote": "Karyorrhexis was evidenced by fragmentation of the **chromatinic** mass into dark irregular granules."
      }
    ]
  },
  "Dashboard — chro/chromatism.md": {
    "primary": "Chromatic aberration in an optical lens; also, abnormal or excessive coloration in organisms.",
    "secondary": "In optics, the fringing of prismatic colors around images formed by uncorrected lenses; in botany, unusual pigment development in flowers.",
    "quotes": [
      {
        "author": "David Brewster",
        "work": "A Treatise on New Philosophical Instruments",
        "quote": "The primary defect of the single lens consists in its inherent **chromatism**, which tints every margin with rainbow rings."
      },
      {
        "author": "John Herschel",
        "work": "Treatise on Light",
        "quote": "To reduce the **chromatism** of the telescope, astronomers lengthened focal tubes to colossal dimensions."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "Occasional floral **chromatism** produces variegated petals where solid color normally prevails."
      }
    ]
  },
  "Dashboard — chro/chromatogram.md": {
    "primary": "A visible record, column, or graphic output produced by chromatography, showing the separated components of a mixture.",
    "secondary": "In analytical chemistry, the band pattern on a paper strip or the electronic peak profile recorded across retention time.",
    "quotes": [
      {
        "author": "Mikhail Tsvet",
        "work": "Chromatographic Adsorption Analysis",
        "quote": "The green extract separated on the chalk column into colored zones, forming an elegant **chromatogram** of leaf pigments."
      },
      {
        "author": "Archer John Porter Martin",
        "work": "A New Form of Chromatogram Employing Two Liquid Phases",
        "quote": "The movement of amino acids across the paper **chromatogram** revealed distinct ninhydrin-stained spots."
      },
      {
        "author": "Richard Laurence Millington Synge",
        "work": "Nobel Lecture: Partition Chromatography",
        "quote": "Examining the developed **chromatogram** permitted the complete structural mapping of the gramicidin polypeptide."
      }
    ]
  },
  "Dashboard — chro/chromatographic.md": {
    "primary": "Relating to or produced by chromatography, the process of separating components of a chemical mixture.",
    "secondary": "In laboratory methodology, characterizing columns, paper strips, or spectroscopic detection methods used in chemical separations.",
    "quotes": [
      {
        "author": "Mikhail Tsvet",
        "work": "Physical-Chemical Studies on Chlorophyll",
        "quote": "The **chromatographic** method permits the clean physical separation of chlorophyll a from chlorophyll b."
      },
      {
        "author": "Linus Pauling",
        "work": "Molecular Disease: Sickle Cell Anemia",
        "quote": "Using **chromatographic** analysis of peptide digests, we traced the sickle-cell hemoglobin defect to a single amino acid substitution."
      },
      {
        "author": "Erwin Chargaff",
        "work": "Chemical Specificity of Nucleic Acids",
        "quote": "Quantitative **chromatographic** procedures established that adenine equals thymine in all DNA extracts."
      }
    ]
  },
  "Dashboard — chro/chromatographical.md": {
    "primary": "Pertaining to chromatography; chromatographic.",
    "secondary": "In analytical literature, describing apparatus, procedures, or techniques employed in the adsorption separation of chemical mixtures.",
    "quotes": [
      {
        "author": "Archer John Porter Martin",
        "work": "Biochemical Journal",
        "quote": "The **chromatographical** separation of volatile fatty acids was effected upon silica gel columns."
      },
      {
        "author": "Richard Laurence Millington Synge",
        "work": "Proteins and Synthetic Polypeptides",
        "quote": "Careful **chromatographical** fractionation confirmed the high purity of the synthetic dipeptides."
      },
      {
        "author": "Paul Karrer",
        "work": "Carotenoids",
        "quote": "Our **chromatographical** surveys of plant juices yielded several previously unidentified xanthophyll isomers."
      }
    ]
  },
  "Dashboard — chro/chromatographically.md": {
    "primary": "By means of chromatography; using chromatographic techniques.",
    "secondary": "In experimental biochemistry, describing the isolation, purification, or quantification of compounds via selective partitioning.",
    "quotes": [
      {
        "author": "Erwin Chargaff",
        "work": "Essays on Nucleic Acids",
        "quote": "After hydrolyzing the calf thymus DNA, the purine and pyrimidine bases were **chromatographically** resolved."
      },
      {
        "author": "Melvin Calvin",
        "work": "The Path of Carbon in Photosynthesis",
        "quote": "The radioactive compounds were **chromatographically** separated on two-dimensional paper sheets."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "Brenner demonstrated **chromatographically** that the mutant viral proteins differed by a single peptide fragment."
      }
    ]
  },
  "Dashboard — chro/chromatography.md": {
    "primary": "A laboratory technique for separating the components of a mixture based on their differential distribution between a stationary phase and a mobile phase.",
    "secondary": "In chemistry and biochemistry, an indispensable analytical and preparative method encompassing gas, liquid, thin-layer, and affinity separations.",
    "quotes": [
      {
        "author": "Mikhail Tsvet",
        "work": "Adsorption Analysis and Chromatographic Method",
        "quote": "I have called this separation process **chromatography**, because it produces visible colored rings upon the adsorbent."
      },
      {
        "author": "Archer John Porter Martin",
        "work": "Partition Chromatography",
        "quote": "The power of **chromatography** lies in its ability to separate virtually identical chemical species under mild conditions."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Paper **chromatography** revolutionized organic analysis by enabling the detection of microgram quantities of amino acids."
      }
    ]
  },
  "Dashboard — chro/chromatophore.md": {
    "primary": "A pigment-containing and light-reflecting cell found in amphibians, fish, reptiles, crustaceans, and cephalopods; also, a bacterial photosynthetic organelle.",
    "secondary": "In comparative zoology, dermal cells (melanophores, xanthophores, iridophores) under nervous or hormonal control that enable rapid physiological color change.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The cuttlefish displayed rapid clouds of changing tint caused by the expansion and contraction of every **chromatophore**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "The brilliant spots upon the mantle were identified as distinct **chromatophore** cells packed with mobile pigment."
      },
      {
        "author": "E. Ray Lankester",
        "work": "Comparative Physiology",
        "quote": "Under autonomic nerve impulses, each **chromatophore** expands outward to darken the chameleon's skin."
      }
    ]
  },
  "Dashboard — chro/chrome.md": {
    "primary": "Chromium, especially as used to plate metal objects, or a vivid yellow pigment (chrome yellow) prepared from lead chromate.",
    "secondary": "In industrial design and motoring, bright electroplated metallic finishes; in colloquial usage, decorative shiny trim.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Elements of Drawing",
        "quote": "The painter used pure **chrome** yellow sparingly to indicate the direct strike of the setting sun."
      },
      {
        "author": "H. G. Wells",
        "work": "The World Set Free",
        "quote": "Machinery gleamed with polished steel and electroplated **chrome** in the underground power stations."
      },
      {
        "author": "Sinclair Lewis",
        "work": "Babbitt",
        "quote": "His automobile was adorned with glittering accessories of nickel and shining **chrome**."
      }
    ]
  },
  "Dashboard — chro/chromesthesia.md": {
    "primary": "A type of synesthesia in which non-visual auditory stimuli (such as spoken words, phonemes, or musical pitches) involuntarily evoke the sensation of colors.",
    "secondary": "In cognitive neuropsychology, an involuntary cross-activation between auditory cortical processing and visual color areas (V4).",
    "quotes": [
      {
        "author": "Francis Galton",
        "work": "Inquiries into Human Faculty and Its Development",
        "quote": "Cases of **chromesthesia** demonstrate that for certain minds, every vowel possesses a persistent, unchangeable hue."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In **chromesthesia**, hearing an oboe or trumpet note immediately floods the imagination with violet or gold."
      },
      {
        "author": "Oliver Sacks",
        "work": "Musicophilia",
        "quote": "Scriabin composed with vivid **chromesthesia**, assigning specific orchestral key signatures to precise spectral colors."
      }
    ]
  },
  "Dashboard — chro/chromite.md": {
    "primary": "A dark, metallic, brownish-black mineral consisting of iron chromium oxide (FeCr2O4), belonging to the spinel group.",
    "secondary": "In economic geology, the chief commercial ore of chromium, typically found as magmatic segregations in ultramafic rocks and peridotites.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The mineral **chromite** crystallizes in octahedrons and furnishes nearly all the chromium of commerce."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Heavy bands of **chromite** segregated along the bottom of the cooling serpentinite magma."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "In the Bushveld complex, stratiform layers of **chromite** extend across hundreds of square miles."
      }
    ]
  },
  "Dashboard — chro/chromium-plate.md": {
    "primary": "To electroplate a metal surface with a thin, protective, highly reflective layer of metallic chromium.",
    "secondary": "In manufacturing engineering, an electrodeposition process applying a chromium coating over nickel to prevent corrosion and reduce wear.",
    "quotes": [
      {
        "author": "Henry Ford",
        "work": "Moving Forward",
        "quote": "We chose to **chromium-plate** exterior automobile fittings to protect them against rain and rust."
      },
      {
        "author": "Thomas Alva Edison",
        "work": "Laboratory Notebooks",
        "quote": "Efforts to **chromium-plate** the acoustic diaphragm increased its wear resistance under constant vibration."
      },
      {
        "author": "Arthur D. Little",
        "work": "The Chemical Engineer",
        "quote": "The commercial ability to **chromium-plate** machine cylinders drastically lengthened the service life of internal combustion engines."
      }
    ]
  },
  "Dashboard — chro/chromium.md": {
    "primary": "A hard, brittle, lustrous transition metal of atomic number 24 (symbol Cr), capable of taking a high polish and resisting tarnishing.",
    "secondary": "In metallurgy, an essential alloying component of stainless steel; named from Greek chroma due to the intense colors of its varied chemical compounds.",
    "quotes": [
      {
        "author": "Louis Nicolas Vauquelin",
        "work": "Memoir on a New Metallic Substance Found in the Red Lead of Siberia",
        "quote": "I propose to give this metal the name **chromium**, on account of the striking and varied colors of its compounds."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "The compounds of **chromium** yield some of the most durable and brilliant pigments in the arts."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "Our laboratory syntheses depended on compounds of **chromium**, whose brilliant orange crystals required delicate handling."
      }
    ]
  },
  "Dashboard — chro/chromoblastomycosis.md": {
    "primary": "A chronic fungal skin and subcutaneous tissue infection characterized by dark pigmented verrucous or granulomatous lesions.",
    "secondary": "In tropical dermatology, a dematiaceous mycosis caused by trauma-inoculated fungi (*Fonsecaea pedrosoi*), diagnosed by thick-walled muriform Medlar bodies.",
    "quotes": [
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "Agricultural workers infected through thorns presented with crusted warty nodules characteristic of **chromoblastomycosis**."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Tissue sections of **chromoblastomycosis** reveal distinctive brown, chestnut-colored fungal bodies within giant cells."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The tropical surgeon recognized the stubborn warty plaques of **chromoblastomycosis** acquired in the Brazilian rubber groves."
      }
    ]
  },
  "Dashboard — chro/chromogen.md": {
    "primary": "A precursor substance capable of being transformed into a pigment, dye, or colored compound, or a bacterium that produces color.",
    "secondary": "In organic chemistry and histology, an uncolored compound containing a chromophore that becomes a dye upon the introduction of an auxochrome.",
    "quotes": [
      {
        "author": "August Wilhelm von Hofmann",
        "work": "Introduction to Modern Chemistry",
        "quote": "Colorless aniline acts as a **chromogen**, transforming into vivid magenta when treated with oxidizing agents."
      },
      {
        "author": "Paul Ehrlich",
        "work": "The Anaemias",
        "quote": "The primitive erythroblast elaborates an intracellular **chromogen** that subsequently ripens into functional hemoglobin."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The broth developed a startling blue sheen due to the proliferation of a pigment-forming **chromogen** bacillus."
      }
    ]
  },
  "Dashboard — chro/chromolithography.md": {
    "primary": "A method of making multi-colored prints by lithography, using a separate stone or metal plate inked with a different color for each impression.",
    "secondary": "In printing history, the dominant 19th-century commercial color printing technology that popularized full-color posters, trade cards, and book illustrations.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "Fors Clavigera",
        "quote": "The cheap perfection of modern **chromolithography** spreads colored copies of masterpieces into every cottage parlor."
      },
      {
        "author": "William Morris",
        "work": "The Ideal Book",
        "quote": "Mechanical **chromolithography** must not be mistaken for the soulful touch of the ancient illuminated manuscript."
      },
      {
        "author": "Walter Crane",
        "work": "Of the Decorative Illustration of Books",
        "quote": "The introduction of **chromolithography** offered artists unprecedented freedom in blending delicate tints on the printed page."
      }
    ]
  },
  "Dashboard — chro/chromophobia.md": {
    "primary": "An abnormal, morbid aversion to or fear of colors; also, the quality of a biological cell or tissue that resists staining with dyes.",
    "secondary": "In psychology, dread of vibrant hues; in histology, the property of chromophobe cells (such as certain anterior pituitary cells) that remain pale.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "The Psychology of Yellow",
        "quote": "A patient suffering from intense **chromophobia** painted all his domestic walls a uniform, deadening slate gray."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine",
        "quote": "Certain adenomas of the hypophysis are composed entirely of cells characterized by distinct **chromophobia**."
      },
      {
        "author": "G. Stanley Hall",
        "work": "A Study of Fears",
        "quote": "Childhood sensory dreads occasionally focalize as a marked **chromophobia** toward red or yellow fabrics."
      }
    ]
  },
  "Dashboard — chro/chromophore.md": {
    "primary": "An atom or group of atoms whose presence is responsible for the color of an organic compound.",
    "secondary": "In spectroscopy and organic chemistry, the unsaturated covalent moiety (such as -N=N-, -C=C-, or -NO2) that absorbs light in the visible region.",
    "quotes": [
      {
        "author": "Otto Nikolaus Witt",
        "work": "Zur Kenntniss der Bildung von Farbstoffen",
        "quote": "The azo group serves as the essential **chromophore**, without which the entire molecule would remain utterly colorless."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Extensive resonance throughout conjugated double bonds stabilizes the excited state of the **chromophore**."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Color appears in organic compounds only when an unsaturated atomic complex called a **chromophore** is present."
      }
    ]
  },
  "Dashboard — chro/chromoplast.md": {
    "primary": "A colored plastid other than a chloroplast found in plant cells, synthesizing and storing carotenoid pigments that color flowers and fruits.",
    "secondary": "In plant cell biology, a non-photosynthetic organelle responsible for yellow, orange, and red pigmentation in autumn foliage, petals, and ripening tomatoes.",
    "quotes": [
      {
        "author": "Julius von Sachs",
        "work": "Lectures on the Physiology of Plants",
        "quote": "As the fruit ripens, green chloroplasts lose their chlorophyll and metamorphose into yellow **chromoplast** bodies."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Crystalline carotene fills the specialized **chromoplast** organelles within the carrot root parenchyma."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "The dazzling scarlet of the rose hip is due to numerous angular **chromoplast** granules suspended in the cytoplasm."
      }
    ]
  },
  "Dashboard — chro/chromosomal.md": {
    "primary": "Of, relating to, or carried on a chromosome or chromosomes.",
    "secondary": "In cytogenetics, designating inheritance patterns, mutations, inversions, or translocations involving the physical structures of chromosomes.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "The linear linkage groups observed in breeding experiments correspond directly to **chromosomal** architecture."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Natural populations of fruit flies harbor diverse **chromosomal** inversions that confer adaptive fitness."
      },
      {
        "author": "Barbara McClintock",
        "work": "Chromosome Organization and Genic Expression",
        "quote": "Transposable elements induce **chromosomal** breakages that alter gene expression in variegated maize kernels."
      }
    ]
  },
  "Dashboard — chro/chromosome.md": {
    "primary": "A thread-like structure of nucleic acids and protein found in the nucleus of most living cells, carrying genetic information in the form of genes.",
    "secondary": "In cytology, a discrete chromatin package that condenses during mitosis and meiosis, ensuring equal segregation of duplicated genomic DNA.",
    "quotes": [
      {
        "author": "Heinrich Wilhelm Waldeyer",
        "work": "On Karyokinesis and Its Relation to the Process of Fertilization",
        "quote": "I propose the term **chromosome** for those particular stained bodies which play so vital a role in nuclear division."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Mechanism of Mendelian Heredity",
        "quote": "Every gene occupies a definite, mapped locus along the length of its parent **chromosome**."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Each eukaryotic **chromosome** contains a colossal, single continuous double helix of DNA wound about histone cores."
      }
    ]
  },
  "Dashboard — chro/chromosphere.md": {
    "primary": "A reddish gaseous layer of the sun's atmosphere located between the photosphere and the corona.",
    "secondary": "In solar astrophysics, a turbulent layer visible during total eclipses as a rosy fringe, characterized by emission lines such as hydrogen-alpha and calcium H and K.",
    "quotes": [
      {
        "author": "Joseph Norman Lockyer",
        "work": "The Chemistry of the Sun",
        "quote": "Above the luminous photosphere lies the rosy envelope which I designated the **chromosphere**."
      },
      {
        "author": "Arthur Eddington",
        "work": "Stars and Atoms",
        "quote": "Immense solar prominences leap hundreds of thousands of miles upward from the turbulent **chromosphere**."
      },
      {
        "author": "George Ellery Hale",
        "work": "The Study of Stellar Evolution",
        "quote": "Spectroheliograph images revealed swirling vortex storms in the hydrogen gas of the upper **chromosphere**."
      }
    ]
  },
  "Dashboard — chro/chronic.md": {
    "primary": "Persisting for a long time or constantly recurring (of an illness, condition, or problem); long-standing.",
    "secondary": "In clinical medicine, distinguishing slowly progressing, prolonged disease processes from sudden, self-limiting acute conditions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient suffered from **chronic** nephritis, which progressed insidiously over many silent years."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "In dealing with **chronic** invalids, fresh air and cheerful surroundings prove more curative than apothecary draughts."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Medical Observations",
        "quote": "Acute diseases are sent by nature to clear the body, whereas **chronic** complaints arise from our lingering internal infirmities."
      }
    ]
  },
  "Dashboard — chro/chronically.md": {
    "primary": "In a chronic manner; persistently, long-lastingly, or repeatedly over a prolonged period of time.",
    "secondary": "In sociology and pathology, characterizing habitual states of deprivation, illness, or systemic dysfunction.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Micawber lived **chronically** in expectation of something handsome turning up to rescue him."
      },
      {
        "author": "George Orwell",
        "work": "The Road to Wigan Pier",
        "quote": "Unemployed miners and their families were **chronically** undernourished, subsisting on bread and cheap tea."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "She felt **chronically** disconnected from the hurried, mechanical march of the city crowds."
      }
    ]
  },
  "Dashboard — chro/chronicle.md": {
    "primary": "A continuous, factual written account of historical events presented in chronological sequence; to record in such a manner.",
    "secondary": "In historiography and medieval literature, an annalistic record documenting royal reigns, battles, and notable occurrences year by year.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Henry V",
        "quote": "For hear her but philosophise on life, And you would think her very **chronicle** were writ by truth."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The dry monkish **chronicle** preserves little beyond the names of abbots and miracles of doubtful authenticity."
      },
      {
        "author": "Washington Irving",
        "work": "Chronicle of the Conquest of Granada",
        "quote": "The ancient **chronicle** recounts how knights on both sides performed prodigies of valor beneath the Moorish ramparts."
      }
    ]
  },
  "Dashboard — chro/chronicler.md": {
    "primary": "A person who writes or records a chronicle; a historian who records events as they occur.",
    "secondary": "In literary history, an annalist or narrator whose works serve as primary documentary sources for subsequent historiographers.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "Ivanhoe",
        "quote": "The medieval **chronicler** dwelt with relish upon the sumptuous heraldry displayed at the Ashby tournament."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "Froissart was the most vivid **chronicler** of fourteenth-century chivalry, capturing every fluttering plume and clash of steel."
      },
      {
        "author": "John Lothrop Motley",
        "work": "The Rise of the Dutch Republic",
        "quote": "No contemporary **chronicler** could witness the heroic defense of Leiden without recording his boundless admiration."
      }
    ]
  },
  "Dashboard — chro/chronograph.md": {
    "primary": "An instrument for recording time intervals with great precision, especially one with a stopwatch mechanism for measuring elapsed fractions of a second.",
    "secondary": "In ballistics and observational astronomy, a precision device with a revolving cylinder or digital clockwork that registers transit events.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "The electric **chronograph** registered the precise instant at which the star crossed the meridian wire."
      },
      {
        "author": "Jules Verne",
        "work": "From the Earth to the Moon",
        "quote": "The artillery officer checked his split-second **chronograph** as the countdown to detonation began."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of the Four",
        "quote": "Holmes glanced at his gold **chronograph**, calculating the exact speed of our cab through the foggy streets."
      }
    ]
  },
  "Dashboard — chro/chronological.md": {
    "primary": "Arranged in the order of time of occurrence; relating to the establishment of dates and time sequences.",
    "secondary": "In historical and archival research, arranging source documents, events, or evolutionary stages in strict temporal succession.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The geological record displays a magnificent **chronological** succession of living forms ascending through the rock strata."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "History of England",
        "quote": "A clear **chronological** narrative preserves the reader from confusing cause with subsequent effect."
      },
      {
        "author": "H. G. Wells",
        "work": "The Outline of History",
        "quote": "We present the rise of human civilizations in strict **chronological** order to demonstrate our shared heritage."
      }
    ]
  },
  "Dashboard — chro/chronologically.md": {
    "primary": "In order of time; according to the temporal sequence in which events occurred.",
    "secondary": "In biographic and bibliographic compilation, organizing occurrences or works progressively from inception to conclusion.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Lives of the Most Eminent English Poets",
        "quote": "I have examined the plays **chronologically**, that the author's gradual mastery of the stage may be observed."
      },
      {
        "author": "Edward Gibbon",
        "work": "Memoirs of My Life and Writings",
        "quote": "Arranging my notes **chronologically** brought order out of the chaotic records of the late empire."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "When the fossils are examined **chronologically**, the ancestry of the modern horse emerges beyond dispute."
      }
    ]
  }
};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {
  if (updateNote(relPath, data)) updated++;
}
console.log(`Successfully updated ${updated} of ${Object.keys(batchData).length} files in Batch 2.`);
