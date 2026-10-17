import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — thel\\thelypteris.md": {
    "primary": "A genus of terrestrial ferns known as marsh ferns, belonging to the family Thelypteridaceae.",
    "secondary": "In botanical taxonomy, *Thelypteris* is characterized by creeping rhizomes, bipinnatifid fronds with prominent acicular hairs, and round sori protected by kidney-shaped indusia.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Linnaeus originally described the marsh fern *Acrostichum thelypteris*, later designated as the type of **Thelypteris**."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Along shaded boggy margins, the delicate pale green fronds of **Thelypteris** form dense clonal colonies."
      },
      {
        "author": "William Jackson Hooker",
        "work": "British Ferns",
        "quote": "The creeping black rhizome of **Thelypteris** spreads rapidly through acidic marshland soils."
      }
    ]
  },
  "Dashboard — top\\atopic.md": {
    "primary": "Pertaining to, affected by, or characteristic of atopy; predisposed to localized hypersensitivity reactions (such as eczema, asthma, or hay fever).",
    "secondary": "In clinical immunology, atopic disorders are mediated by hyper-responsiveness of T-helper 2 cells and elevated serum immunoglobulin E (IgE) against common environmental antigens.",
    "quotes": [
      {
        "author": "Arthur F. Coca",
        "work": "On the Classification of the Phenomena of Hypersensitiveness",
        "quote": "We propose the term **atopic** to describe familial hereditary hypersensitivities peculiar to the human species."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Infantile eczema frequently serves as the opening clinical episode in the lifelong **atopic** diathesis."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Cellular mast-cell degranulation accounts for the rapid cutaneous flare seen in **atopic** sensitivity tests."
      }
    ]
  },
  "Dashboard — top\\atopy.md": {
    "primary": "A genetic predisposition to develop allergic diseases, such as allergic rhinitis, bronchial asthma, and atopic dermatitis.",
    "secondary": "Coined in 1923 by Coca and Cooke from Greek *atopia* (placelessness, strangeness), atopy reflects abnormal IgE antibody synthesis upon contact with benign airborne or dietary allergens.",
    "quotes": [
      {
        "author": "Arthur F. Coca",
        "work": "The Journal of Immunology",
        "quote": "The condition of **atopy** is characterized by reagins that can be transferred passively to healthy skin."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Family pedigrees demonstrate that **atopy** transmits a general allergic irritability rather than specific antigen sensitivity."
      },
      {
        "author": "Alexis Carrel",
        "work": "Man, The Unknown",
        "quote": "The modern rise of **atopy** and autoimmune complaints reflects altered interactions between industrialized environments and human physiology."
      }
    ]
  },
  "Dashboard — top\\dystopia.md": {
    "primary": "An imagined state or society in which there is great suffering or injustice, typically one that is totalitarian or post-apocalyptic.",
    "secondary": "Coined by John Stuart Mill in an 1868 parliamentary speech (as the opposite of utopia), dystopia serves as a prominent literary genre dissecting state surveillance, technological coercion, and moral decay.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "Speech in the House of Commons",
        "quote": "What is commonly called Utopian is something too good to be practicable; but what they seem to favor is rather a **dystopia**, too bad to be endured."
      },
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "The perpetual nightmare of Oceania revealed how totalitarian bureaucracy could manufacture an inescapable **dystopia**."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "In this conditioned **dystopia**, human liberty was exchanged for synthetic stability and sensory gratification."
      }
    ]
  },
  "Dashboard — top\\dystopian.md": {
    "primary": "Of, relating to, or denoting an imagined society characterized by oppression, misery, or totalitarian control.",
    "secondary": "In literary criticism and cultural studies, dystopian narratives explore prophetic warnings regarding unchecked state apparatuses, ecological collapse, and algorithmic dehumanization.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "When the Sleeper Wakes",
        "quote": "The subterranean labor city embodied a grim **dystopian** vision of unrestrained corporate plutocracy."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Story of Utopias",
        "quote": "Modern mechanistic society threatened to realize the very **dystopian** nightmares earlier visionaries sought to avert."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Scientific Outlook",
        "quote": "A purely technocratic state without ethical constraints would evolve into a terrifyingly efficient **dystopian** machine."
      }
    ]
  },
  "Dashboard — top\\ectopia.md": {
    "primary": "The abnormal displacement or malposition of an organ or other body part, especially present from birth.",
    "secondary": "In clinical teratology and pediatric surgery, ectopia includes conditions like ectopia cordis (heart outside thoracic cavity) and ectopia lentis (dislocation of the ocular crystalline lens, as in Marfan syndrome).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bilateral **ectopia** lentis in an adolescent should immediately raise suspicion of underlying Marfan syndrome."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "Arrested embryological migration of the testis results in cryptorchidism or perineal **ectopia**."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Failure of the ventral body wall to close completely produces the tragic anomaly of thoracic **ectopia**."
      }
    ]
  },
  "Dashboard — top\\ectopic.md": {
    "primary": "In an abnormal place or position; displaced; occurring outside the normal anatomical site.",
    "secondary": "In obstetrics and cardiology, ectopic describes extrauterine pregnancies (most commonly tubal ectopic pregnancy) or cardiac pacemaking impulses originating outside the sinoatrial node.",
    "quotes": [
      {
        "author": "William Hunter",
        "work": "Anatomia Uteri Humani Gravidi",
        "quote": "Dissection of an **ectopic** gestation revealed the blastocyst implanted directly into the ampulla of the fallopian tube."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rupture of an **ectopic** pregnancy constitutes a surgical emergency demanding immediate exploratory laparotomy."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Heart",
        "quote": "An **ectopic** atrial focus fired prematurely, producing an irregular compensatory pause on the rhythm strip."
      }
    ]
  },
  "Dashboard — top\\entopic.md": {
    "primary": "Occurring in the normal or expected anatomical place (contrasted with ectopic).",
    "secondary": "In developmental anatomy and ophthalmology, entopic refers to normal organ position or endogenous visual perceptions (entoptic phenomena) arising within the eyeball itself.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "Following physiological descent, the gonads occupy their normal **entopic** position within the scrotal sac."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Surgical repositioning aimed to restore the herniated abdominal viscera to their true **entopic** relationships."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "The perception of retinal blood vessels under oblique illumination represents a classic **entopic** visual effect."
      }
    ]
  },
  "Dashboard — top\\epitope.md": {
    "primary": "The part of an antigen molecule to which an antibody attaches itself; an antigenic determinant.",
    "secondary": "In molecular immunology, epitopes are categorized as conformational (formed by discontinuous amino acid residues brought together by 3D folding) or linear (contiguous sequence residues).",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The side-chain receptor locks specifically onto the complementary chemical **epitope** of the foreign toxoid."
      },
      {
        "author": "Macfarlane Burnet",
        "work": "The Clonal Selection Theory of Acquired Immunity",
        "quote": "Each pre-existing lymphocyte clone bears surface receptors tailored to recognize a single foreign **epitope**."
      },
      {
        "author": "César Milstein",
        "work": "Nobel Lecture: With Antibody-Producing Cells to the Golden Egg",
        "quote": "Monoclonal antibodies provided an analytical scalpel capable of discriminating between closely related **epitope** variants."
      }
    ]
  },
  "Dashboard — top\\eutopia.md": {
    "primary": "A place of ideal peace and happiness; a good and prosperous society (distinct from utopia as 'nowhere').",
    "secondary": "Coined from Greek *eu* (good, well) and *topos* (place), eutopia emphasizes the tangible, achievable perfection of human institutions, contrasted with utopian impossibility.",
    "quotes": [
      {
        "author": "Thomas More",
        "work": "Utopia",
        "quote": "Wherfore not Utopie, but rather rightely my name is **Eutopie**: a place of felicitie."
      },
      {
        "author": "Patrick Geddes",
        "work": "Cities in Evolution",
        "quote": "Urban planning must strive not for distant impossible dreams, but for the regional realization of an achievable **eutopia**."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Story of Utopias",
        "quote": "While utopia signifies nowhere, **eutopia** summons human ingenuity to cultivate the best possible home on earth."
      }
    ]
  },
  "Dashboard — top\\isotope.md": {
    "primary": "Each of two or more forms of the same chemical element that contain equal numbers of protons but different numbers of neutrons in their nuclei.",
    "secondary": "Coined in 1913 by Margaret Todd and Frederick Soddy from Greek *isos* (equal) and *topos* (place, occupying the same position in the periodic table), isotopes revolutionized radiochemistry and nuclear physics.",
    "quotes": [
      {
        "author": "Frederick Soddy",
        "work": "The Radio-Elements and the Periodic Law",
        "quote": "Chemically identical elements possessing different atomic weights occupy the same periodic locus and were termed an **isotope**."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "The discovery that lead could exist as a stable radiogenic **isotope** settled longstanding puzzles in uranium decay."
      },
      {
        "author": "Francis William Aston",
        "work": "Mass Spectra and Isotopes",
        "quote": "Mass spectrograph analysis demonstrated that neon is a mixture of more than one distinct **isotope**."
      }
    ]
  },
  "Dashboard — top\\isotopic.md": {
    "primary": "Of, relating to, or having the properties of an isotope; having identical chemical properties but differing in atomic mass.",
    "secondary": "In geochronology and biochemistry, isotopic fractionation and isotopic labeling (e.g. carbon-14, deuterium) trace metabolic pathways and determine geologic rock ages.",
    "quotes": [
      {
        "author": "Harold Urey",
        "work": "The Thermodynamic Properties of Isotopic Substances",
        "quote": "Small differences in zero-point vibrational energy allow the chemical separation of **isotopic** molecules like deuterium."
      },
      {
        "author": "Francis William Aston",
        "work": "Isotopes",
        "quote": "The whole number rule revealed that fractional atomic weights result from variable natural **isotopic** abundances."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Mass spectrometry accurately separates positive ions according to their unique **isotopic** mass-to-charge ratios."
      }
    ]
  },
  "Dashboard — top\\nomotopic.md": {
    "primary": "Originating or situated in the normal anatomical position, especially said of cardiac rhythms originating in the sinoatrial node.",
    "secondary": "In clinical cardiology and electrophysiology, nomotopic arrhythmias (such as sinus tachycardia or sinus arrhythmia) represent rhythm variations originating within the normal sinoatrial pacemaker.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The clinician must determine whether the accelerated pulse reflects a **nomotopic** sinus acceleration or an ectopic tachycardia."
      },
      {
        "author": "Willem Einthoven",
        "work": "The Galvanometric Registration of the Human Electrocardiogram",
        "quote": "Normal P waves indicate that the cardiac activation impulse arises from its **nomotopic** pacemaker site."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Heart",
        "quote": "Under exercise stress, the heart maintains a **nomotopic** pacemaker drive while scaling up stroke volume."
      }
    ]
  },
  "Dashboard — top\\polytope.md": {
    "primary": "A geometric figure bounded by flat sides, representing the generalization to any number of dimensions of polygons (two dimensions) and polyhedra (three dimensions).",
    "secondary": "Coined in 1882 by Alicia Boole Stott, polytope theory in higher-dimensional geometry classifies regular 4-polytopes (such as the 24-cell and 120-cell) and supports linear programming (simplex algorithm).",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The four-dimensional hypercube is the simplest regular **polytope** possessing eight cubical boundary cells."
      },
      {
        "author": "Alicia Boole Stott",
        "work": "Geometrical Deduction of Semiregular from Regular Polytopes",
        "quote": "By sectioning four-dimensional space with three-dimensional hyperplanes, each complex **polytope** reveals its inner symmetry."
      },
      {
        "author": "Ludwig Schläfli",
        "work": "Theory of Continuous Manifolds",
        "quote": "Schläfli symbols provide an elegant algebraic notation for classifying every regular multidimensional **polytope**."
      }
    ]
  },
  "Dashboard — top\\toper.md": {
    "primary": "A chronic or habitual drinker of alcoholic liquor, especially one given to heavy intoxication; a drunkard.",
    "secondary": "Frequently appearing in eighteenth- and nineteenth-century English tavern literature, a toper was characterized as a convivial, seasoned imbiber of ale, punch, or port.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The mug was called a God-forgive-me because its immense depth made any seasoned **toper** feel ashamed when he saw the bottom empty."
      },
      {
        "author": "Washington Irving",
        "work": "The Sketch-Book of Geoffrey Crayon",
        "quote": "The retired old **toper** derived kindred pleasure from inhaling the rich aroma of the empty wine cask."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "The History of Henry Esmond",
        "quote": "The jovial country squire was an unrepentant **toper**, spending every evening over bumpers of mulled claret."
      }
    ]
  },
  "Dashboard — top\\topiary.md": {
    "primary": "The art or practice of clipping and training shrubs or trees into decorative ornamental shapes; clipped or shaped foliage.",
    "secondary": "Originating in ancient Roman gardening (*ars topiaria*) and reaching elaborate heights in Renaissance formal gardens, topiary sculpts boxwood, yew, and privet into geometric figures, animals, or labyrinthine hedges.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Of Gardens",
        "quote": "I, for my part, do not like images cut out in juniper or other garden stuff; they be for children; such **topiary** work tires the eye."
      },
      {
        "author": "Alexander Pope",
        "work": "The Guardian: Essay on Verdant Sculpture",
        "quote": "Pope satirized formal **topiary** gardens where yew trees were distorted into dragons, giants, and geometric cones."
      },
      {
        "author": "John Evelyn",
        "work": "Sylva, or A Discourse of Forest-Trees",
        "quote": "The dense evergreen foliage of boxwood renders it the quintessential shrub for architectural **topiary** hedges."
      }
    ]
  },
  "Dashboard — top\\topic.md": {
    "primary": "A matter dealt with in a text, discourse, or conversation; a subject of discussion or study.",
    "secondary": "In classical Aristotelian rhetoric, *topoi* (topics, from Greek *topos* place) were mental 'places' or commonplaces where arguments, proofs, and rhetorical strategies could be located.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Topics",
        "quote": "Our treatise aims to discover a method by which we can reason from accepted opinions on any proposed **topic**."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "In disputation, disputants frequently wander from the main **topic** into fruitless verbal tangles."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "A conversationalist of lively intellect can extract entertaining discourse from the most trivial daily **topic**."
      }
    ]
  },
  "Dashboard — top\\topical.md": {
    "primary": "Of immediate relevance, interest, or importance at the present time; applied directly to a part of the body (medicine).",
    "secondary": "In clinical pharmacology, topical administration delivers dermatological ointments, drops, or creams directly to cutaneous or mucosal tissues to produce localized therapeutic effects.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "For superficial fungal infections, **topical** applications of sulfur and salicylic acid ointment suffice."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Newspaper editors maintain reader engagement by publishing vigorous editorials on **topical** legislative debates."
      },
      {
        "author": "George Orwell",
        "work": "The Lion and the Unicorn",
        "quote": "Satirical cartoonists thrive by seizing upon **topical** political controversies and translating them into visual humor."
      }
    ]
  },
  "Dashboard — top\\topically.md": {
    "primary": "In a manner relating to current events or local subjects; by direct application to a local area or surface of the body.",
    "secondary": "In pharmacology and therapeutics, drugs administered topically avoid systemic first-pass hepatic metabolism, minimizing systemic toxicity.",
    "quotes": [
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Antiseptic dressings applied **topically** to open surgical wounds drastically curtailed the incidence of hospital gangrene."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The soothing lotion was applied **topically** to relieve intense burning along the inflamed cutaneous border."
      },
      {
        "author": "Matthew Arnold",
        "work": "Essays in Criticism",
        "quote": "The poet addressed the political crisis **topically**, infusing temporary events with enduring philosophical reflections."
      }
    ]
  },
  "Dashboard — top\\topographic.md": {
    "primary": "Of or relating to the detailed physical features or map of an area or anatomical region.",
    "secondary": "In surgical anatomy and geodesy, topographic relationships describe three-dimensional spatial coordinates, surface contours, and underlying structural landmarks.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of the Physical Description of the Universe",
        "quote": "A precise **topographic** survey of Andean mountain chains reveals the direct influence of altitude on vegetation belts."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "Knowledge of the **topographic** anatomy of the femoral triangle is indispensable for locating the femoral artery."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "River erosion continually modifies the **topographic** relief of river basins across millennia."
      }
    ]
  },
  "Dashboard — top\\topographical.md": {
    "primary": "Relating to the arrangement of physical features, mapping, or surveying of a geographical or anatomical surface.",
    "secondary": "In military cartography and geomorphology, topographical maps use contour lines to represent elevation, drainage patterns, and human settlements.",
    "quotes": [
      {
        "author": "John Wesley Powell",
        "work": "The Exploration of the Colorado River",
        "quote": "Our expedition completed the first detailed **topographical** map of the Grand Canyon's sheer labyrinthine gorges."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "Careful study of the **topographical** contours convinced the general staff that the ridge could be held against artillery."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Holmes studied the Ordnance Survey sheet, noting every **topographical** pitfall of the treacherous Grimpen Mire."
      }
    ]
  },
  "Dashboard — top\\topographically.md": {
    "primary": "In terms of the topography or physical features of an area or anatomical region.",
    "secondary": "In neuroanatomy, neurons organized topographically (such as the motor homunculus or retinotopic visual maps) maintain spatial neighborhood relationships between sensory surfaces and cortical representations.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Sensory projections from the retina are mapped **topographically** across the primary visual cortex of the occipital lobe."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The isolated volcanic islands of the Galápagos are separated **topographically** by deep marine channels."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Parkinsonian tremors were analyzed **topographically**, progressing from distal phalanges to proximal musculature."
      }
    ]
  },
  "Dashboard — top\\topography.md": {
    "primary": "The arrangement of the natural and artificial physical features of an area; detailed mapping or charting of such features.",
    "secondary": "In surface metrology and corneal ophthalmology, topography measures microscopic elevation profiles and curvature variations across tissues or manufactured surfaces.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of the New Continent",
        "quote": "The unique **topography** of the Orinoco river basin determines its seasonal inundations and ecological boundaries."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "Every river reveals its local **topography** through the gentle meanderings of its alluvial banks."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The natural **topography** of Constantinople, surrounded by sea on three sides, rendered it nearly impregnable."
      }
    ]
  },
  "Dashboard — top\\topology.md": {
    "primary": "The branch of mathematics concerned with properties of space that are preserved under continuous deformations, such as stretching, crumpling, and bending, but not tearing or gluing.",
    "secondary": "Founded conceptually by Leonhard Euler (Seven Bridges of Königsberg) and Henri Poincaré (Analysis Situs), topology underpins modern geometry, differential manifold theory, and network architectures.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "The study of **topology** allows the mathematician to classify manifolds by their fundamental group and connectivity."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "Qualitative spatial relations find their most abstract and rigorous expression in algebraic **topology**."
      },
      {
        "author": "Richard Feynman",
        "work": "The Character of Physical Law",
        "quote": "In condensed matter physics, the **topology** of quantum wave functions dictates quantized conductivity."
      }
    ]
  },
  "Dashboard — top\\toponomastics.md": {
    "primary": "The study of place names, their origins, meanings, use, and typological classification; toponymy.",
    "secondary": "In onomastics and historical linguistics, toponomastics illuminates ancient migration patterns, substrate languages, and topographical perception of early settlers.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Celtic river names surviving across England provide rich evidence for the student of comparative **toponomastics**."
      },
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The field of **toponomastics** proves that names of mountains and streams outlive the conquests of empires."
      },
      {
        "author": "Otto Jespersen",
        "work": "Growth and Structure of the English Language",
        "quote": "Scandinavian place names ending in '-by' and '-thorpe' illustrate how **toponomastics** documents the Danelaw settlements."
      }
    ]
  },
  "Dashboard — top\\toponym.md": {
    "primary": "A place name, especially one derived from a topographical feature.",
    "secondary": "In cultural geography and cartography, a toponym reflects linguistic history, political commemoration, or environmental characteristics of a geographic locality.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Every descriptive **toponym** in an indigenous tongue encapsulates a precise geographic or ecological observation."
      },
      {
        "author": "George R. Stewart",
        "work": "Names on the Land: A Historical Account of Place-Naming in the United States",
        "quote": "The continent was baptized with names; each newly bestowed **toponym** told of discovery, hope, or nostalgia."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "The Savage Mind",
        "quote": "In traditional oral cultures, each mythic **toponym** marks a sacred stop along ancestral wandering routes."
      }
    ]
  },
  "Dashboard — top\\toponymy.md": {
    "primary": "The study of place names (toponyms); the place names of a region or language collectively.",
    "secondary": "In historical geography and philology, toponymy reconstructs dialect boundaries and historical landscape use from linguistic strata embedded in geographical names.",
    "quotes": [
      {
        "author": "Isaac Taylor",
        "work": "Words and Places: Or, Etymological Illustrations of History, Ethnology and Geography",
        "quote": "Local **toponymy** serves as an enduring palimpsest upon which successive waves of invaders have inscribed their history."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The fossilized archaic sounds preserved in regional **toponymy** often escape standard phonological decay."
      },
      {
        "author": "Marc Bloch",
        "work": "French Rural History",
        "quote": "Medieval clearing of forests can be traced through the agrarian **toponymy** of village settlements."
      }
    ]
  },
  "Dashboard — top\\topos.md": {
    "primary": "A traditional theme or motif in literature; a rhetorical commonplace; in mathematics, a generalized category sharing properties with the category of sheaves.",
    "secondary": "In literary scholarship, Ernst Robert Curtius popularized topos (plural *topoi*) as recurring rhetorical conventions (e.g. the locus amoenus); in algebraic geometry, Alexander Grothendieck defined a topos as a generalized geometric space.",
    "quotes": [
      {
        "author": "Ernst Robert Curtius",
        "work": "European Literature and the Latin Middle Ages",
        "quote": "The medieval ideal landscape or locus amoenus is a rhetorical **topos** inherited directly from Roman antiquity."
      },
      {
        "author": "Alexander Grothendieck",
        "work": "Récoltes et Semailles",
        "quote": "The mathematical notion of a **topos** provides a vast synthesis uniting topology, geometry, and arithmetic."
      },
      {
        "author": "Northrop Frye",
        "work": "Anatomy of Criticism",
        "quote": "Archetypal criticism traces how a poetic **topos** migrates through genres while retaining its symbolic vitality."
      }
    ]
  },
  "Dashboard — top\\utopian.md": {
    "primary": "Modeled on or aiming for a state in which everything is desirable or perfect; idealistic and visionary but often impractical.",
    "secondary": "Derived from Sir Thomas More's 1516 satire *Utopia* (coined from Greek *ou* not + *topos* place), utopian political projects attempt radical societal reorganization based on egalitarian or rationalist ideals.",
    "quotes": [
      {
        "author": "Thomas More",
        "work": "Utopia",
        "quote": "In their ideal commonwealth, the citizens designed **utopian** laws that eliminated private property and greed."
      },
      {
        "author": "Karl Marx",
        "work": "The Communist Manifesto",
        "quote": "We must distinguish scientific socialism from the visionary fantasies of early **utopian** socialists like Fourier and Owen."
      },
      {
        "author": "Isaiah Berlin",
        "work": "The Crooked Timber of Humanity",
        "quote": "The pursuit of the ideal society frequently transforms **utopian** dreams into coercive ideological tyrannies."
      }
    ]
  },
  "Dashboard — top\\utopianism.md": {
    "primary": "The belief in or pursuit of an ideal, perfect society; the visionary striving for an unattainable social paradise.",
    "secondary": "In political philosophy and sociology, utopianism can serve as a revolutionary critique of existing social inequities or as an ungrounded ideological blueprint vulnerable to dogmatism.",
    "quotes": [
      {
        "author": "Karl Popper",
        "work": "The Open Society and Its Enemies",
        "quote": "The danger of radical **utopianism** lies in its willingness to sacrifice living generations for a hypothetical perfection."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Story of Utopias",
        "quote": "Genuine **utopianism** is not escapism, but a vital catalyst for projecting imaginative ideals into practical reality."
      },
      {
        "author": "George Orwell",
        "work": "James Burnham and the Managerial Revolution",
        "quote": "Totalitarian fanaticism often masks its will to power behind the lofty rhetoric of radical **utopianism**."
      }
    ]
  },
  "Dashboard — trach\\trachea.md": {
    "primary": "The large membranous and cartilaginous tube conveying air between the larynx and bronchial tubes in vertebrates; the windpipe.",
    "secondary": "In human anatomy, the trachea is supported by sixteen to twenty C-shaped hyaline cartilages, lined by pseudostratified ciliated columnar epithelium that traps and clears inhaled debris.",
    "quotes": [
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The cartilaginous rings of the **trachea** remain incomplete posteriorly to accommodate the expanding esophagus."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "The **trachea** bifurcates at the level of the fifth thoracic vertebra into the right and left main bronchi."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Foreign body aspiration into the **trachea** produces sudden paroxysmal coughing and stridor."
      }
    ]
  },
  "Dashboard — trach\\tracheal.md": {
    "primary": "Of, relating to, or situated near the trachea (windpipe); in insects, relating to the respiratory system of tubes.",
    "secondary": "In entomology, the tracheal system delivers atmospheric oxygen directly to body tissues via branching cuticle-lined tubes branching from external spiracles.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Caterpillar",
        "quote": "Fine silver threads of the insect's **tracheal** network distribute air to every muscle fiber."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Respiratory spiracles open into stout longitudinal **tracheal** trunks traversing the arthropod body."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Aortic aneurysm compression against the left bronchus produces a classic physical sign known as **tracheal** tug."
      }
    ]
  },
  "Dashboard — trach\\tracheid.md": {
    "primary": "An elongated, thick-walled, lignified water-conducting and supporting cell in the xylem of vascular plants, having tapered ends and pitted walls without perforations.",
    "secondary": "In plant anatomy and paleobotany, tracheids are the sole water-conducting conduits in gymnosperms and seedless vascular plants, contrasted with the vessel elements of angiosperms.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Bordered pits along the tapered end walls of each **tracheid** permit lateral water movement while arresting gas embolisms."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The coniferous wood of pine is composed almost exclusively of uniform rows of the fibrous **tracheid**."
      },
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "Scalariform wall thickenings inside each fossilized **tracheid** confirmed the vascular nature of the Rhynie chert plants."
      }
    ]
  },
  "Dashboard — trach\\tracheids.md": {
    "primary": "Plural of tracheid; elongated, lignified, imperforate xylem cells that conduct water and mineral nutrients in vascular plants.",
    "secondary": "In comparative xylem physiology, tracheids provide mechanical support and safer hydraulic transport than open vessels under severe freeze-thaw or drought-induced cavitation stress.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Vascular Differentiation in Plants",
        "quote": "During secondary xylem development, fusiform cambial initials differentiate into elongated **tracheids**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "Water absorbed by root hairs ascends through bundles of lignified **tracheids** toward the transpirational leaves."
      },
      {
        "author": "Arthur George Tansley",
        "work": "Elements of Plant Biology",
        "quote": "In gymnosperm timber, the uniform arrangement of **tracheids** imparts exceptional mechanical strength and resilience."
      }
    ]
  },
  "Dashboard — trach\\tracheitis.md": {
    "primary": "Inflammation of the trachea, typically caused by viral or bacterial infection.",
    "secondary": "In pediatric otolaryngology, bacterial tracheitis (often caused by *Staphylococcus aureus*) is a potentially life-threatening airway emergency requiring urgent airway stabilization and intravenous antibiotics.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **tracheitis** commonly accompanies severe influenza, provoking painful substernal raw cough and hoarseness."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "In winter catarrhs, inflammation descends rapidly into the windpipe, causing acute **tracheitis** and burning pain."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Maintaining warm, humidified room air eases the labored respiration of patients suffering from acute **tracheitis**."
      }
    ]
  },
  "Dashboard — trach\\trachelospermum.md": {
    "primary": "A genus of evergreen woody climbing vines in the dogbane family (Apocynaceae), notably star jasmine (*Trachelospermum jasminoides*), prized for fragrant white flowers.",
    "secondary": "Named from Greek *trachelos* (neck) and *sperma* (seed) in reference to the slender neck of its seeds, *Trachelospermum* produces glossy foliage and indole-scented corollas with twisted lobes.",
    "quotes": [
      {
        "author": "Robert Fortune",
        "work": "A Residence Among the Chinese",
        "quote": "Garden walls in Shanghai were luxuriantly draped with the fragrant white blooms of **Trachelospermum** jasminoides."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "In mild climates, **Trachelospermum** serves as an indispensable ornamental evergreen climber for trellises."
      },
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "Morphological characters of the seeds distinguish the climbing liana **Trachelospermum** from allied apocynaceous genera."
      }
    ]
  },
  "Dashboard — trach\\tracheobronchitis.md": {
    "primary": "Inflammation involving both the trachea and the bronchial airways.",
    "secondary": "In respiratory medicine, acute infectious tracheobronchitis is marked by retrosternal burning discomfort, productive purulent cough, and rhonchi, frequently triggered by respiratory syncytial virus, adenovirus, or *Bordetella*.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In elderly and debilitated patients, acute **tracheobronchitis** may rapidly progress to fatal bronchopneumonia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Autopsies of acute **tracheobronchitis** reveal hyperemic mucosal swelling accompanied by dense neutrophilic exudation."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Body",
        "quote": "Post-operative pulmonary toilet is essential to prevent atelectasis secondary to mucous plugging in **tracheobronchitis**."
      }
    ]
  },
  "Dashboard — trach\\tracheophyta.md": {
    "primary": "The division or subkingdom of plants (vascular plants) characterized by possessing specialized conducting tissues (xylem and phloem).",
    "secondary": "In phylogenetic plant taxonomy, Tracheophyta encompasses lycophytes, monilophytes (ferns), gymnosperms, and angiosperms, defined by sporophyte dominance and lignified vascular elements.",
    "quotes": [
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Evolution of the Land Plants",
        "quote": "The geological conquest of terrestrial continents began with the evolutionary diversification of the **Tracheophyta**."
      },
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "Lignified conducting elements characterize all true members of the **Tracheophyta** discovered in Devonian deposits."
      },
      {
        "author": "Arthur George Tansley",
        "work": "The New Phytologist",
        "quote": "Systematic classification separates the non-vascular bryophytes from the advanced cormophytic **Tracheophyta**."
      }
    ]
  },
  "Dashboard — trach\\tracheophyte.md": {
    "primary": "A vascular plant; any plant belonging to the division Tracheophyta, having lignified tissues for conducting water and minerals.",
    "secondary": "In plant biology, a tracheophyte features a dominant diploid sporophyte generation equipped with true roots, stems, leaves, and vascular cylinder (stele).",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The development of internal xylem vessels permitted the **tracheophyte** to achieve massive upright arborescent size."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The mid-Paleozoic landscape was transformed as each primitive **tracheophyte** evolved complex branching architecture."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Cuticular water-proofing and stomatal control enabled the **tracheophyte** to flourish in arid terrestrial regimes."
      }
    ]
  },
  "Dashboard — trach\\tracheostomy.md": {
    "primary": "A surgical procedure to create an opening through the neck into the trachea, allowing the insertion of a tube to facilitate breathing.",
    "secondary": "In critical care medicine and otolaryngology, tracheostomy secures long-term mechanical ventilation, facilitates pulmonary toilet, and bypasses severe upper airway obstruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In laryngeal diphtheria, emergency **tracheostomy** frequently rescued the asphyxiating child from impending suffocation."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Following extensive posterior fossa surgery, temporary **tracheostomy** prevented dangerous postoperative aspiration."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Body",
        "quote": "For patients requiring prolonged mechanical ventilation, a planned **tracheostomy** offers superior patient comfort and safety."
      }
    ]
  },
  "Dashboard — trach\\tracheotomy.md": {
    "primary": "The surgical incision made directly into the trachea through the anterior neck to relieve airway obstruction.",
    "secondary": "Practiced since ancient times (described by Galen and refined by Armand Trousseau in nineteenth-century Paris), tracheotomy is the surgical incision preceding the placement of a cannula.",
    "quotes": [
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Trousseau championed prompt **tracheotomy** in membranous croup, saving hundreds of lives in Parisian hospitals."
      },
      {
        "author": "William Halsted",
        "work": "Surgical Papers",
        "quote": "The rapid performance of emergency **tracheotomy** demands precise anatomical identification of the cricoid cartilage."
      },
      {
        "author": "Charles Dickens",
        "work": "The Uncommercial Traveller",
        "quote": "The hospital surgeon kept silver cannula tubes polished and ready for urgent **tracheotomy** at a moment's notice."
      }
    ]
  },
  "Dashboard — trach\\trachinotus.md": {
    "primary": "A genus of deep-bodied, silvery marine carangid fishes comprising the pompanos and permits.",
    "secondary": "In marine ichthyology, *Trachinotus* species inhabit warm surf zones and coastal reefs, celebrated as premier game and food fishes prized for delicate flesh.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The Florida pompano, *Trachinotus carolinus*, represents the most delectable table fish belonging to the genus **Trachinotus**."
      },
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The genus **Trachinotus** is recognized by its compressed rhomboidal body, short snout, and spinous dorsal fin."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "Schools of **Trachinotus** migrate along Atlantic sandy beaches feeding upon small bivalves and coquina clams."
      }
    ]
  },
  "Dashboard — trach\\trachipteridae.md": {
    "primary": "A family of elongate, ribbon-like marine lampriform fishes commonly known as ribbonfishes or dealfishes.",
    "secondary": "In deep-sea marine biology, Trachipteridae inhabit mesopelagic depths, featuring laterally compressed silver bodies, elongated dorsal rays, and an absence of anal fins.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Genera of Fishes",
        "quote": "Fishes of the family **Trachipteridae** possess slender ribbon-like bodies of gleaming silver with crimson fins."
      },
      {
        "author": "William Beebe",
        "work": "Half Mile Down",
        "quote": "From the bathysphere window, Beebe observed the undulating rhythmic locomotion of oceanic **Trachipteridae** in deep twilight."
      },
      {
        "author": "Albert Günther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "Fragile bony skeletons and fragile fin rays cause stranded specimens of **Trachipteridae** to fragment easily upon beaches."
      }
    ]
  },
  "Dashboard — trach\\trachipterus.md": {
    "primary": "A genus of marine ribbonfishes in the family Trachipteridae, characterized by highly compressed, elongated bodies.",
    "secondary": "In systematic ichthyology, *Trachipterus* species inhabit offshore pelagic zones worldwide, displaying dramatic metamorphic transformations from larval forms with trailing fin filaments.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "In the genus **Trachipterus**, the tail ends in a fan-shaped caudal fin directed obliquely upward."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The king-of-the-salmon, classified under **Trachipterus**, was revered in indigenous mythology of the Pacific Northwest."
      },
      {
        "author": "Arthur Smith Woodward",
        "work": "Outlines of Vertebrate Paleontology",
        "quote": "Rare fossil impressions indicate that ancestors of **Trachipterus** roamed pelagic seas during the Tertiary period."
      }
    ]
  },
  "Dashboard — trach\\trachodon.md": {
    "primary": "A historical genus of large duck-billed herbivorous dinosaurs (hadrosaurids) from the Late Cretaceous of North America.",
    "secondary": "In vertebrate paleontology, Joseph Leidy erected *Trachodon* in 1856 based on fossil teeth found in Montana; though largely considered a *nomen dubium* today, it historically anchored popular understanding of hadrosaurs.",
    "quotes": [
      {
        "author": "Joseph Leidy",
        "work": "Notice of Remains of Extinct Reptiles and Fishes",
        "quote": "The fossil teeth from the Judith River badlands led Leidy to establish the herbivorous reptilian genus **Trachodon**."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Dinosauria of North America",
        "quote": "Serrated grinding pavements of teeth enabled **Trachodon** to macerate fibrous Cretaceous vegetation with great efficiency."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Skeletal Adaptations of Hadrosaurian Dinosaurs",
        "quote": "Early museum restorations depicted **Trachodon** as a semiaquatic swamp-dwelling browser with webbed front paws."
      }
    ]
  },
  "Dashboard — trach\\trachodont.md": {
    "primary": "Pertaining to or resembling the hadrosaurid dinosaurs historically referred to as Trachodon; a duck-billed dinosaur.",
    "secondary": "In paleontological literature, trachodont dinosaurs featured complex dental batteries comprising hundreds of replacement teeth arranged to grind tough flowering plants.",
    "quotes": [
      {
        "author": "O. C. Marsh",
        "work": "The Dinosaurs of North America",
        "quote": "The broad, flattened edentulous muzzle of the **trachodont** dinosaur formed an effective vegetative duck-bill."
      },
      {
        "author": "William Diller Matthew",
        "work": "Dinosaurs: With Special Reference to the American Museum Collections",
        "quote": "Remarkable mummified skin impressions proved that the **trachodont** body was covered with non-overlapping tubercular scales."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Bipedal locomotion and specialized cranial crests distinguished the flourishing Late Cretaceous **trachodont** radiation."
      }
    ]
  },
  "Dashboard — trach\\trachoma.md": {
    "primary": "A contagious bacterial infection of the eye caused by *Chlamydia trachomatis*, leading to inflammation and scarring of the inner eyelids and potentially blindness.",
    "secondary": "In global public health and ophthalmology, trachoma is the leading infectious cause of blindness worldwide, controlled via the WHO SAFE strategy (Surgery, Antibiotics, Facial cleanliness, Environmental improvement).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic **trachoma** produces follicular conjunctivitis followed by cicatricial entropion and blinding corneal pannus."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Crowded, unventilated barracks fostered widespread outbreaks of Egyptian ophthalmia, now recognized as **trachoma**."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "Mass administration of oral sulfonamides provided the first effective pharmaceutical weapon against endemic **trachoma**."
      }
    ]
  },
  "Dashboard — trach\\trachurus.md": {
    "primary": "A genus of marine carangid fishes known as horse mackerels or jack mackerels.",
    "secondary": "In commercial fisheries biology, *Trachurus* species form immense migratory pelagic schools along continental shelves, characterized by a curved lateral line armed with sharp bony scutes.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "The genus **Trachurus** is recognized by the series of large, keeled bony shields protecting its entire lateral line."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The common horse mackerel, grouped under **Trachurus**, supports extensive commercial trawl fisheries across the eastern Atlantic."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Fisheries of the World",
        "quote": "Enormous shoals of **Trachurus** enter coastal bays in late autumn, pursued by predatory tuna and dolphins."
      }
    ]
  },
  "Dashboard — trag\\extragalactic.md": {
    "primary": "Situated, originating, or existing outside the Milky Way galaxy.",
    "secondary": "In observational astrophysics and cosmology, extragalactic astronomy investigates external galaxies, quasars, galaxy clusters, and the expansion of the cosmic web.",
    "quotes": [
      {
        "author": "Edwin Hubble",
        "work": "The Realm of the Nebulae",
        "quote": "Cepheid variable stars in the Andromeda nebula confirmed beyond doubt its true **extragalactic** nature and vast distance."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Expanding Universe",
        "quote": "Redshift measurements of distant **extragalactic** nebulae provided empirical evidence for cosmic expansion."
      },
      {
        "author": "Subrahmanyan Chandrasekhar",
        "work": "Principles of Stellar Dynamics",
        "quote": "Gravitational interactions between passing galaxies govern the structural evolution of rich **extragalactic** clusters."
      }
    ]
  },
  "Dashboard — trag\\tragacanth.md": {
    "primary": "A natural gum obtained from the dried sap of several species of Middle Eastern legumes of the genus *Astragalus*.",
    "secondary": "In pharmacognosy and food technology, gum tragacanth forms viscous, mucilaginous colloids used as an emulsifier, binder for pharmaceutical lozenges, and textile sizing agent.",
    "quotes": [
      {
        "author": "Theophrastus",
        "work": "Enquiry into Plants",
        "quote": "The thorny shrub exuding **tragacanth** gum grows wild on the stony mountain slopes of Asia Minor."
      },
      {
        "author": "Nicholas Culpeper",
        "work": "The Complete Herbal",
        "quote": "Gum **tragacanth** dissolved in rosewater provides an incomparable demulcent for soothing harsh pulmonary coughs."
      },
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Chemical analysis indicates that gum **tragacanth** consists of bassorin and water-soluble tragacanthin fractions."
      }
    ]
  },
  "Dashboard — trag\\tragedian.md": {
    "primary": "An actor who specializes in tragic roles; a writer of tragedies.",
    "secondary": "In classical theatrical history, the tragedian commanded heightened poetic declamation, cothurni, and masks to evoke the cathartic terror and pity of dramatic fate.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "The arrival of the traveling **tragedian** troupe in Elsinore provided Hamlet the occasion to catch the conscience of the king."
      },
      {
        "author": "Aristotle",
        "work": "Poetics",
        "quote": "Aeschylus was the first **tragedian** to introduce a second actor, reducing the prominence of the tragic chorus."
      },
      {
        "author": "William Hazlitt",
        "work": "Characters of Shakespear's Plays",
        "quote": "Edmund Kean was a sublime **tragedian** whose fiery passion illuminated Shakespeare like flashes of lightning."
      }
    ]
  },
  "Dashboard — trag\\tragedienne.md": {
    "primary": "A female actor who specializes in playing tragic roles in dramatic theater.",
    "secondary": "In theatrical history, celebrated nineteenth-century tragediennes such as Sarah Siddons, Rachel Félix, and Sarah Bernhardt attained international acclaim for portraying monumental heroines like Phèdre, Medea, and Lady Macbeth.",
    "quotes": [
      {
        "author": "Charlotte Brontë",
        "work": "Villette",
        "quote": "Watching the great French **tragedienne** Vashti upon the stage, Lucy Snowe was overwhelmed by demonic passion and tragic terror."
      },
      {
        "author": "Henry James",
        "work": "The Tragic Muse",
        "quote": "Miriam harbored the fierce, singular ambition to establish herself as the supreme dramatic **tragedienne** of her era."
      },
      {
        "author": "George Eliot",
        "work": "Daniel Deronda",
        "quote": "The aging **tragedienne** recounted the glorious triumphs of her theatrical youth in Vienna and St. Petersburg."
      }
    ]
  },
  "Dashboard — trag\\tragedy.md": {
    "primary": "A play, novel, or other literary work dealing with tragic events and having an unhappy ending, especially one concerning the downfall of the main character; an event causing great suffering.",
    "secondary": "In literary philosophy, tragedy derived from Greek *tragoidia* (goat-song), defined by Aristotle as an imitation of a noble action which through pity and fear effects the catharsis of such emotions.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Poetics",
        "quote": "A true **tragedy** achieves through incidents arousing pity and fear the proper purgation or catharsis of these emotions."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "Attic **tragedy** was born from the mystical union of the Dionysian chorus with the Apollonian world of dream and illusion."
      },
      {
        "author": "Arthur Miller",
        "work": "Tragedy and the Common Man",
        "quote": "I believe that the common man is as apt a subject for **tragedy** in its highest sense as kings were in ancient times."
      }
    ]
  },
  "Dashboard — trag\\tragelaphus.md": {
    "primary": "A genus of spiral-horned, medium to large African antelopes including the bongo, sitatunga, bushbuck, nyala, and kudu.",
    "secondary": "Named from Greek *tragos* (he-goat) and *elaphos* (deer), *Tragelaphus* species inhabit diverse habitats from dense rainforests to arid brush, displaying marked sexual dimorphism and elegant twisted horns in males.",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "African Game Trails",
        "quote": "In the dense bamboo thickets of Mount Kenya, we tracked the rare and elusive forest antelope **Tragelaphus**."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Game Animals of Africa",
        "quote": "Magnificent spiral horns and white vertical flank stripes characterize male antelopes of the genus **Tragelaphus**."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Study of Mammals",
        "quote": "Osteological features of the cranium unite the kudu and bushbuck within the bovid genus **Tragelaphus**."
      }
    ]
  },
  "Dashboard — trag\\tragic.md": {
    "primary": "Causing or characterized by extreme distress, sorrow, or ruin; relating to or characteristic of literary tragedy.",
    "secondary": "In philosophical aesthetics, the tragic consciousness reflects human courage confronting inescapable cosmic limitations, fate, and moral dilemmas.",
    "quotes": [
      {
        "author": "A. C. Bradley",
        "work": "Shakespearean Tragedy",
        "quote": "The **tragic** hero falls from high prosperity through an internal flaw that precipitates total ruin."
      },
      {
        "author": "Albert Camus",
        "work": "The Myth of Sisyphus",
        "quote": "Sisyphus is the absurd hero par excellence; his rock is his thing, and his consciousness makes his fate **tragic**."
      },
      {
        "author": "John Keats",
        "work": "Letters of John Keats",
        "quote": "Shakespeare possessed above all men that Negative Capability necessary to grasp the profound **tragic** mystery of human life."
      }
    ]
  },
  "Dashboard — trag\\tragical.md": {
    "primary": "Of, relating to, or having the character of tragedy; sorrowful; calamitous (archaic or formal variant of tragic).",
    "secondary": "Frequently utilized in early modern English drama and Renaissance rhetoric to describe catastrophic historical narratives and fate-driven dramas.",
    "quotes": [
      {
        "author": "Christopher Marlowe",
        "work": "The Tragical History of Doctor Faustus",
        "quote": "Behold the **tragical** history of a scholar who bartered eternal salvation for earthly dominion."
      },
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "The best actors in the world, either for tragedy, comedy, history, pastoral, pastoral-comical, historical-pastoral, **tragical**-historical."
      },
      {
        "author": "Francis Bacon",
        "work": "The History of the Reign of King Henry VII",
        "quote": "The rebellion concluded with the **tragical** execution of the pretender's aristocratic conspirators."
      }
    ]
  },
  "Dashboard — trag\\tragically.md": {
    "primary": "In a tragic manner; with disastrous or sorrowful consequences; in a way that relates to tragedy.",
    "secondary": "In narrative exposition, describing events where potential greatness is cut down prematurely by misfortune, hubris, or malevolent circumstances.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "Misunderstood by society, Tess found her generous young heart **tragically** ensnared in unyielding social hypocrisy."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The promising reign of Emperor Julian ended **tragically** in the desert sands of Mesopotamia."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "The fall of Singapore proved **tragically** decisive in exposing the vulnerability of British imperial defenses."
      }
    ]
  },
  "Dashboard — trag\\tragicomedy.md": {
    "primary": "A play, novel, or other literary work blending elements of both tragedy and comedy.",
    "secondary": "Coined by Plautus in the prologue to *Amphitruo*, developed by Italian Renaissance theorist Giambattista Guarini, and exemplified in Shakespeare's late romances (*The Winter's Tale*, *The Tempest*).",
    "quotes": [
      {
        "author": "John Dryden",
        "work": "An Essay of Dramatic Poesy",
        "quote": "English playwrights invented a lively **tragicomedy** that mirrors real life with its alternating mirth and sorrow."
      },
      {
        "author": "Samuel Johnson",
        "work": "Preface to Shakespeare",
        "quote": "Shakespeare's plays are not in the rigorous sense either tragedies or comedies, but compositions of a distinct kind; an exhibiting of human life as **tragicomedy**."
      },
      {
        "author": "Samuel Beckett",
        "work": "Waiting for Godot",
        "quote": "Beckett famously subtitled his masterpiece of modern existential theatre as a two-act **tragicomedy**."
      }
    ]
  },
  "Dashboard — trag\\tragicomic.md": {
    "primary": "Manifesting, relating to, or combining tragic and comic elements.",
    "secondary": "In literary criticism and character study, describing scenes or individuals that evoke simultaneous amusement and poignant sorrow.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Micawber's perpetual financial crises presented a **tragicomic** spectacle of cheerful optimism dashed by debtor's prison."
      },
      {
        "author": "Anton Chekhov",
        "work": "Letters of Anton Chekhov",
        "quote": "Life in the provinces is a subtle, **tragicomic** affair where absurd trivialities conceal deep spiritual emptiness."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "The countess observed the marital discord with a cynical, **tragicomic** detachment born of worldly experience."
      }
    ]
  },
  "Dashboard — trag\\tragicomical.md": {
    "primary": "Relating to, resembling, or having the qualities of tragicomedy (variant of tragicomic).",
    "secondary": "In eighteenth-century literary criticism, applied to picaresque romances and farcical satires where grave dilemmas resolve through comic absurdity.",
    "quotes": [
      {
        "author": "Laurence Sterne",
        "work": "The Life and Opinions of Tristram Shandy, Gentleman",
        "quote": "My uncle Toby's military miniature campaigns in the garden presented a most lovable and **tragicomical** diversion."
      },
      {
        "author": "Tobias Smollett",
        "work": "The Adventures of Roderick Random",
        "quote": "The hero endured a series of **tragicomical** misadventures aboard the man-of-war before fortune smiled."
      },
      {
        "author": "Oliver Goldsmith",
        "work": "The Vicar of Wakefield",
        "quote": "The sudden loss of our family fortune inaugurated a **tragicomical** migration to a humble country parsonage."
      }
    ]
  },
  "Dashboard — trag\\tragopan.md": {
    "primary": "A genus of brightly colored, horned pheasants (*Tragopan*) native to the dense forests of the Himalayas and East Asia.",
    "secondary": "In ornithology, male tragopans are celebrated for spectacular courtship displays during which they erect colorful fleshy blue horns and expand a brightly patterned throat wattle (lappet).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man, and Selection in Relation to Sex",
        "quote": "During courtship, the male **tragopan** inflates a pair of vibrant horns and spreads a vivid crimson gular lappet."
      },
      {
        "author": "William Beebe",
        "work": "A Monograph of the Pheasants",
        "quote": "High in the rhododendron forests of the Himalayas, the shy Satyr **tragopan** roosts among moss-covered branches."
      },
      {
        "author": "John Gould",
        "work": "The Birds of Asia",
        "quote": "Gould's hand-colored lithographs captured the resplendent plumage and spotted breast of the Western **tragopan**."
      }
    ]
  },
  "Dashboard — trag\\tragopogon.md": {
    "primary": "A genus of biennial or perennial herbaceous plants in the dandelion tribe of the sunflower family (Asteraceae), commonly called goatsbeard or salsify.",
    "secondary": "Named from Greek *tragos* (goat) and *pogon* (beard) in reference to the conspicuous hairy pappus of its fruiting seedhead, *Tragopogon* includes the edible vegetable salsify (*Tragopogon porrifolius*).",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Linnaeus noted that the yellow blossoms of **Tragopogon** pratensis close promptly at midday, naming it Jack-go-to-bed-at-noon."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The large feathery parachute attached to each achene of **Tragopogon** aids wind dispersal across open prairies."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Classic botanical studies by Ownbey proved that allopolyploid speciation occurred spontaneously in North American **Tragopogon**."
      }
    ]
  },
  "Dashboard — trag\\tragulidae.md": {
    "primary": "A family of small, primitive, even-toed ungulates comprising the mouse-deer or chevrotains, native to South/Southeast Asia and Central Africa.",
    "secondary": "In mammalian taxonomy, Tragulidae are the only extant members of the infraorder Tragulina, retaining primitive ruminant characteristics such as four-toed feet, three-chambered stomachs, and tusk-like upper canines in place of horns.",
    "quotes": [
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "The skull of the **Tragulidae** lacks frontal appendages entirely, relying on elongated saber-like upper canines for defense."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "Members of the family **Tragulidae** represent an archaic survivor of early Oligocene artiodactyl radiation."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Fossil chevrotains demonstrate how the **Tragulidae** diverged before the development of true four-chambered stomachs in Pecora."
      }
    ]
  },
  "Dashboard — trag\\tragulus.md": {
    "primary": "A genus of tiny, hornless, forest-dwelling ungulates known as Asian mouse-deer or chevrotains, belonging to the family Tragulidae.",
    "secondary": "In tropical ecology, *Tragulus* species (such as the lesser mouse-deer, *Tragulus kanchil*) are among the smallest living hoofed mammals, weighing under two kilograms and foraging on fallen fruits on rainforest floors.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "While walking through the Sumatran jungle, I encountered the miniature mouse-deer **Tragulus**, no larger than a hare."
      },
      {
        "author": "Thomas Horsfield",
        "work": "Zoological Researches in Java",
        "quote": "Horsfield described the delicate, slender limbs and agile nocturnal habits of **Tragulus** javanicus."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The male **Tragulus** defends its territory with sharp, protruding canine tusks rather than horns or antlers."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Finish Slice 5 - Batch 4] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
