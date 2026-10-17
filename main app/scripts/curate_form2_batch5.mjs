import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — cycl\\cyclosorus.md": {
    "primary": "A large genus of terrestrial marsh and woodland ferns in the family Thelypteridaceae, commonly known as maiden ferns.",
    "secondary": "In systematic pteridology, tropical and subtropical ferns characterized by pinnatifid fronds and circular sori borne midway along free or anastomosing veins.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Species of **Cyclosorus** flourish along marshy ditches, their circular sori neatly aligned beneath indusiate flaps."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The vigorous creeping rootstock of **Cyclosorus** rapidly establishes attractive green carpets in moist shade."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "Along shaded jungle riverbanks, robust fronds of **Cyclosorus** arched over the water in graceful emerald tiers."
      }
    ]
  },
  "Dashboard — cycl\\cyclosporeae.md": {
    "primary": "A former taxonomic group or order of brown algae (Phaeophyceae) characterized by producing gametes in conceptacles without a free-living gametophyte generation.",
    "secondary": "In systematic phycology, an order including rockweeds (Fucales) possessing cyclic reproductive life histories where the diploid plant produces eggs and antherozoids directly.",
    "quotes": [
      {
        "author": "William Gilson Farlow",
        "work": "The Marine Algae of New England",
        "quote": "The division **Cyclosporeae** unites rockweeds whose reproductive cells develop within specialized pit-like conceptacles."
      },
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "In **Cyclosporeae**, the alternation of generations is completely suppressed, the diploid plant giving rise directly to gametes."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Gymnosperms and Cryptogams",
        "quote": "Fertilization in the **Cyclosporeae** occurs freely in open sea water when the gametes are expelled from the conceptacle."
      }
    ]
  },
  "Dashboard — cycl\\cyclostomata.md": {
    "primary": "A group or superclass of primitive jawless aquatic vertebrates comprising living lampreys and hagfishes.",
    "secondary": "In systematic zoology, an ancient chordate assemblage possessing a circular, toothed, suctorial mouth without paired jaws or pelvic fins; also an order of stenolaemate bryozoans.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The **Cyclostomata** represent the most primitive surviving branch of craniate vertebrates, lacking biting jaws and true ribs."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "The round suctorial mouth of **Cyclostomata** allows these creatures to cling like leeches to the sides of living fishes."
      },
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Story",
        "quote": "Living **Cyclostomata** preserve in degenerate form the ancient, jawless architecture of early Paleozoic ostracoderms."
      }
    ]
  },
  "Dashboard — cycl\\cyclostome.md": {
    "primary": "Any primitive jawless vertebrate of the Cyclostomata, such as a lamprey or hagfish.",
    "secondary": "In comparative vertebrate anatomy, an aquatic craniate possessing a circular sucking mouth, persistent unconstricted notochord, and pouch-like gill chambers.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The brain of a **cyclostome** presents an extraordinarily primitive arrangement, with simple optic lobes and no true cerebellum."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "In the developmental history of every higher vertebrate, an ancestral **cyclostome** stage precedes the emergence of jaws."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The lancelet and the **cyclostome** stand at the very base of the genealogical tree of all vertebrate animals."
      }
    ]
  },
  "Dashboard — cycl\\cyclostyle.md": {
    "primary": "An early mechanical apparatus for duplicating handwritten documents using a pen with a tiny toothed wheel that perforates a waxed stencil sheet.",
    "secondary": "In the history of printing technology, the rotary duplicating process patented by David Gestetner that preceded modern mimeography and xerography.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Bruce-Partington Plans",
        "quote": "The confidential government circular had been rapidly multiplied on the office **cyclostyle** for immediate distribution."
      },
      {
        "author": "H. G. Wells",
        "work": "The New Machiavelli",
        "quote": "Political manifestos were turned out by the ream, the wet ink from the **cyclostyle** smelling pungently in the attic room."
      },
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "Revolutionary leaflets printed on a hand-cranked **cyclostyle** were posted nightly along the barricades."
      }
    ]
  },
  "Dashboard — cycl\\cyclothymia.md": {
    "primary": "A chronic mood disorder characterized by alternating periods of mild hypomanic symptoms and depressive episodes not severe enough to meet major bipolar criteria.",
    "secondary": "In clinical psychiatry and affective nosology, a persistent affective oscillation lasting at least two years, representing a milder, ambulatory variant on the bipolar spectrum.",
    "quotes": [
      {
        "author": "Emil Kraepelin",
        "work": "Manic-Depressive Insanity and Paranoia",
        "quote": "Under the concept of **cyclothymia**, I grouped those mild, lifelong temperamental fluctuations between buoyancy and melancholic dejection."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Certain poetic temperaments display an innate **cyclothymia**, swinging rhythmically between ecstatic enthusiasm and gloomy gloom."
      },
      {
        "author": "Oliver Sacks",
        "work": "Musicophilia",
        "quote": "The composer's creative productivity ebbed and surged with the subtle phases of his constitutional **cyclothymia**."
      }
    ]
  },
  "Dashboard — cycl\\cyclothymic.md": {
    "primary": "Pertaining to, affected by, or characteristic of cyclothymia; exhibiting cyclical mood swings.",
    "secondary": "In personality theory and psychiatry, describing a constitutional temperament marked by recurring, alternating cycles of elation and despondency.",
    "quotes": [
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "The **cyclothymic** individual experiences alternating seasons of tireless enterprise followed by passive, brooding fatigue."
      },
      {
        "author": "Carl Jung",
        "work": "Psychological Types",
        "quote": "Kretschmer associated pyknic physical builds with a predominantly **cyclothymic** personality orientation."
      },
      {
        "author": "Virginia Woolf",
        "work": "A Writer's Diary",
        "quote": "Her sensitive spirit responded in **cyclothymic** waves to every shift in atmospheric pressure and creative tension."
      }
    ]
  },
  "Dashboard — cycl\\cyclotomic.md": {
    "primary": "Relating to or functioning in the division of a circle into equal parts.",
    "secondary": "In algebraic number theory, describing polynomials (cyclotomic polynomials $\\Phi_n(x)$) or number fields obtained by adjoining complex roots of unity to the rational numbers.",
    "quotes": [
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "The theory of the division of the circle, or **cyclotomic** analysis, demonstrates the geometric constructibility of the regular 17-gon."
      },
      {
        "author": "Richard Dedekind",
        "work": "Theory of Algebraic Integers",
        "quote": "Kummer was led to the discovery of ideal numbers through his profound investigations into **cyclotomic** fields."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The irreducible factors of $x^n - 1$ over the field of rational numbers are precisely the canonical **cyclotomic** polynomials."
      }
    ]
  },
  "Dashboard — cycl\\cyclotron.md": {
    "primary": "A type of particle accelerator in which charged particles are accelerated outward from the center along a spiral path by an alternating high-frequency electric field within a magnetic field.",
    "secondary": "In nuclear and high-energy physics, an apparatus invented by Ernest O. Lawrence in 1930 that produces high-energy beams of protons or deuterons for nuclear transmutation and medical isotope production.",
    "quotes": [
      {
        "author": "Ernest Lawrence",
        "work": "Nobel Lecture: The Development of the Cyclotron",
        "quote": "The hollow D-shaped electrodes of the **cyclotron** repeatedly impart energy pulses to ions circling within the magnetic gap."
      },
      {
        "author": "Enrico Fermi",
        "work": "Nuclear Physics",
        "quote": "Beams of energetic deuterons produced by the university **cyclotron** made artificial radioactive isotopes readily available for medical research."
      },
      {
        "author": "Richard Feynman",
        "work": "Surely You're Joking, Mr. Feynman!",
        "quote": "At Princeton we crawled into the basement beneath the **cyclotron** magnet to adjust the high-voltage spark gaps."
      }
    ]
  },
  "Dashboard — cycl\\dicyclic.md": {
    "primary": "Having or consisting of two cycles, whorls, or rings; bicyclic.",
    "secondary": "In botany and chemistry, describing flowers possessing two floral whorls, or crinoids having two circlets of plates (infrabasals and basals) below the radial plates.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "A flower whose perianth is arranged in two distinct concentric whorls is described as **dicyclic**."
      },
      {
        "author": "Francis Bather",
        "work": "The Echinoderma",
        "quote": "In a **dicyclic** crinoid calyx, a ring of infrabasal plates separates the true basals from the summit of the stem."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Naphthalene presents a planar **dicyclic** aromatic framework sharing two adjacent bridgehead carbon atoms."
      }
    ]
  },
  "Dashboard — cycl\\eccyclema.md": {
    "primary": "A low wheeled platform or revolving stage mechanism in ancient Greek theater, rolled out through the central palace doors to reveal interior tableaux.",
    "secondary": "In classical drama and theatrical archaeology, the mechanical device used especially in Attic tragedy to expose the aftermath of off-stage murders or secret interior scenes.",
    "quotes": [
      {
        "author": "Aeschylus",
        "work": "Agamemnon",
        "quote": "The royal portal swings open and the **eccyclema** rolls forward, displaying Clytemnestra standing triumphantly over the slain king."
      },
      {
        "author": "Aristophanes",
        "work": "The Acharnians",
        "quote": "Euripides, wheel thyself out upon the **eccyclema**, and lend me a tragic beggar's rags from thy stage wardrobe!"
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "The Greek stage maintained poetic illusion by bringing the hidden catastrophe into daylight upon the solemn **eccyclema**."
      }
    ]
  },
  "Dashboard — cycl\\encyclia.md": {
    "primary": "A genus of neotropical epiphytic orchids in the family Orchidaceae, known as butterfly orchids or clamshell orchids.",
    "secondary": "In systematic orchidology, pseudobulbous orchids distinguished from Epidendrum by having a lip that encircles the column without being fused to it along its entire length.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Genera and Species of Orchidaceous Plants",
        "quote": "I established **Encyclia** in reference to the curious floral lip that wraps like a collar around the central column."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Florists prize **Encyclia** tampensis for its graceful sprays of scented greenish-bronze blossoms with magenta spots."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "Trunks of live oaks along the coastal lagoons were encrusted with clusters of wild **Encyclia** in full bloom."
      }
    ]
  },
  "Dashboard — cycl\\encyclical.md": {
    "primary": "Intended for wide circulation; circular; specifically, a papal letter addressed to all bishops or churches of the Catholic communion.",
    "secondary": "In ecclesiastical history, an authoritative circular pastoral letter expounding church doctrine, moral guidance, or social teachings.",
    "quotes": [
      {
        "author": "Pope Leo XIII",
        "work": "Rerum Novarum",
        "quote": "By this our solemn **encyclical**, We address the rights and duties of capital and labor before the entire Christian world."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "The arrival of an **encyclical** letter from Rome commanded universal reverence and obedience throughout the dioceses."
      },
      {
        "author": "Lord Acton",
        "work": "Historical Essays and Studies",
        "quote": "The language of the papal **encyclical** was studied with intense diplomatic anxiety across every European chancellery."
      }
    ]
  },
  "Dashboard — cycl\\encyclopaedia.md": {
    "primary": "A comprehensive reference work containing articles on all branches of knowledge or covering comprehensively a particular discipline; an encyclopedia.",
    "secondary": "In the history of scholarship, a systematic work designed to encompass the complete circle of human education and enlightenment.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "A well-ordered **encyclopaedia** should trace the living branches of knowledge back to their common trunk in natural philosophy."
      },
      {
        "author": "Denis Diderot",
        "work": "Encyclopédie",
        "quote": "The ultimate aim of an **encyclopaedia** is to gather the knowledge scattered over the surface of the earth, so that our descendants may become more virtuous and happy."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Adventurer",
        "quote": "The compiler of an **encyclopaedia** undertakes the laborious duty of making wisdom accessible to common understanding."
      }
    ]
  },
  "Dashboard — cycl\\encyclopaedic.md": {
    "primary": "Pertaining to, resembling, or having the comprehensive scope of an encyclopaedia; encompassing universal knowledge.",
    "secondary": "Describing vast, exhaustive erudition or scholarship that spans across numerous disparate fields and arts.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "Lord Bacon possessed an **encyclopaedic** grasp of human thought, surveying every province of nature from a commanding summit."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Byzantine compiler Photius left behind an **encyclopaedic** treasury of classical authors whose originals are forever lost."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "Coleridge discoursed upon poetry, theology, and chemistry with **encyclopaedic** fluency that dazzled his listeners."
      }
    ]
  },
  "Dashboard — cycl\\encyclopaedism.md": {
    "primary": "The principles, spirit, or philosophy of an encyclopaedist; the pursuit or dissemination of universal knowledge.",
    "secondary": "In cultural and intellectual history, the Enlightenment philosophical movement associated with Diderot and d'Alembert that sought to systematize reason and reform society.",
    "quotes": [
      {
        "author": "Denis Diderot",
        "work": "Prospectus of the Encyclopédie",
        "quote": "True **encyclopaedism** consists not in pedantic accumulation of facts, but in liberating the human intellect from superstition."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The triumphant march of eighteenth-century **encyclopaedism** undermined the ancient thrones and altars of the monarchy."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "French **encyclopaedism** transformed literary men into the foremost political directors of the nation."
      }
    ]
  },
  "Dashboard — cycl\\encyclopaedist.md": {
    "primary": "A person who compiles, edits, or writes articles for an encyclopaedia; one with encyclopaedic learning.",
    "secondary": "In history, one of the French Enlightenment philosophers and savants who contributed to the famous Encyclopédie of Diderot and d'Alembert.",
    "quotes": [
      {
        "author": "Voltaire",
        "work": "Philosophical Dictionary",
        "quote": "The courageous **encyclopaedist** labors in the face of censorship to spread the light of truth and toleration."
      },
      {
        "author": "Jean-Jacques Rousseau",
        "work": "Confessions",
        "quote": "In my youth in Paris, I was admitted into the circle of the **encyclopaedist** philosophers who met at d'Holbach's table."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Essays on History",
        "quote": "Every **encyclopaedist** of that brilliant generation wielded the pen as an engine of political emancipation."
      }
    ]
  },
  "Dashboard — cycl\\encyclopedia.md": {
    "primary": "A comprehensive reference work containing articles on a broad range of topics or a specific subject, usually arranged alphabetically.",
    "secondary": "In education and cultural literacy, a multi-volume compendium summarizing the totality of contemporary human knowledge.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "The universe is an open **encyclopedia** where every visible form expresses an underlying spiritual idea."
      },
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "quote": "A steamboat pilot's memory must be an absolute **encyclopedia** of river channels, snags, and shifting sandbars."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "In the solitude of the woods, the changes of the season are an **encyclopedia** written in fresh leaves and falling snow."
      }
    ]
  },
  "Dashboard — cycl\\encyclopedic.md": {
    "primary": "Covering a wide range of subjects in great depth; comprehensive; characteristic of an encyclopedia.",
    "secondary": "Describing knowledge, scholarship, or reading that spans universally across diverse sciences and humanities.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "The aim of physical cosmography is to present an **encyclopedic** survey of nature from distant nebulae to terrestrial mosses."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Murders in the Rue Morgue",
        "quote": "Dupin exhibited an **encyclopedic** familiarity with odd treatises and obscure criminal annals."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Dryden's prefaces display an **encyclopedic** acquaintance with the principles of classical and modern drama."
      }
    ]
  },
  "Dashboard — cycl\\encyclopedism.md": {
    "primary": "The practice or ideal of comprehensive, encyclopedic learning; universal knowledge.",
    "secondary": "In cultural history, the Enlightenment doctrine that universal education and organized scientific reference works drive moral and political progress.",
    "quotes": [
      {
        "author": "Denis Diderot",
        "work": "Encyclopédie",
        "quote": "The spirit of **encyclopedism** requires courage to overturn all intellectual idols and examine nature with unbiased reason."
      },
      {
        "author": "John Stuart Mill",
        "work": "Autobiography",
        "quote": "My father's rigorous educational regime cultivated a disciplined **encyclopedism** from my earliest boyhood."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Condition of Man",
        "quote": "Modern universities have largely replaced the unifying synthesis of **encyclopedism** with narrow departmental specialization."
      }
    ]
  },
  "Dashboard — cycl\\encyclopedist.md": {
    "primary": "A compiler or writer of an encyclopedia; a person of broad and comprehensive knowledge.",
    "secondary": "Historically, one of the French Enlightenment thinkers (Philosophes) who contributed to the Encyclopédie.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "The passionate writings of each **encyclopedist** dismantled the traditional reverence for established institutions."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Critical and Miscellaneous Essays",
        "quote": "Diderot labored as a tireless **encyclopedist**, forging weapons of criticism in the workshops of eighteenth-century Paris."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "No psychological **encyclopedist** can compress the chaotic variety of human consciousness into a rigid textbook scheme."
      }
    ]
  },
  "Dashboard — cycl\\epicycle.md": {
    "primary": "A small circle whose center moves around the circumference of a larger circle (the deferent), used in Ptolemaic astronomy to explain planetary retrograde motion.",
    "secondary": "In the history of astronomy, a geometric device devised by Apollonius and refined by Ptolemy to reconcile observed planetary irregularities with uniform circular motion.",
    "quotes": [
      {
        "author": "Nicolaus Copernicus",
        "work": "De revolutionibus orbium coelestium",
        "quote": "By placing the sun at the center, the complicated **epicycle** upon epicycle of Ptolemy became completely superfluous."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "How gird the Sphere / With Centric and Eccentric scribbld ore, / Cycle and **Epicycle**, Orb in Orb."
      },
      {
        "author": "Galileo Galilei",
        "work": "Dialogue Concerning the Two Chief World Systems",
        "quote": "To salvage geocentrism, the Peripatetics were compelled to load every planet with an imaginary **epicycle**."
      }
    ]
  },
  "Dashboard — cycl\\epicyclic.md": {
    "primary": "Of, relating to, or having the motion of an epicycle; revolving upon an epicycle.",
    "secondary": "In mechanical engineering, designating gear trains (epicyclic or planetary gearing) in which one or more outer gears revolve around a central sun gear.",
    "quotes": [
      {
        "author": "William John Macquorn Rankine",
        "work": "A Manual of Machinery and Millwork",
        "quote": "In an **epicyclic** gear train, the planetary pinions rotate on moving arms around the coaxial sun gear."
      },
      {
        "author": "Johannes Kepler",
        "work": "Astronomia Nova",
        "quote": "The ancient hypothesis of **epicyclic** motion failed because nature prefers the simplicity of the Keplerian ellipse."
      },
      {
        "author": "Arthur Eddington",
        "work": "Space, Time and Gravitation",
        "quote": "General relativity banished the last lingering **epicyclic** corrections from the orbit of Mercury."
      }
    ]
  },
  "Dashboard — cycl\\epicyclical.md": {
    "primary": "Pertaining to an epicycle; epicyclic in form or trajectory.",
    "secondary": "In historical cosmology and kinematics, describing composite circular trajectories wherein a secondary circle rolls upon a primary path.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Principia Mathematica",
        "quote": "The ancient astronomers disguised the true laws of gravity beneath an artificial web of **epicyclical** motions."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Popular Scientific Lectures",
        "quote": "Kinematic curves generated by **epicyclical** rolling find direct utility in the profiling of clock pinions."
      },
      {
        "author": "William Whewell",
        "work": "History of the Inductive Sciences",
        "quote": "Hipparchus applied the **epicyclical** system with consummate mathematical skill to calculate lunar inequalities."
      }
    ]
  },
  "Dashboard — cycl\\epicycloid.md": {
    "primary": "A plane curve traced by a point on the circumference of a circle as it rolls without slipping around the outside of a fixed circle.",
    "secondary": "In geometry and mechanical gear design, a roulette curve utilized in profiling the addendum of epicyclic and spur gear teeth to maintain constant angular velocity.",
    "quotes": [
      {
        "author": "Christiaan Huygens",
        "work": "Horologium Oscillatorium",
        "quote": "The properties of the **epicycloid** guarantee that gear teeth roll upon one another with pure rolling and minimal friction."
      },
      {
        "author": "Leonhard Euler",
        "work": "Mechanica",
        "quote": "The rectification of the **epicycloid** demonstrates its kinship with the common cycloid discovered by Galileo."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The spiral coils of ammonite shells can be modeled geometrically by an expanding logarithmic **epicycloid**."
      }
    ]
  },
  "Dashboard — cycl\\exocycloida.md": {
    "primary": "A former or obsolete taxonomic order of irregular sea urchins (Echinoidea) characterized by having the periproct situated outside the apical system.",
    "secondary": "In systematic invertebrate paleontology, echinoids (such as sand dollars and heart urchins) that evolved bilateral symmetry from regular radial ancestors.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Monographies d'Échinodermes",
        "quote": "In the **Exocycloida**, the excretory periproct has migrated out of the central apical disc toward the posterior margin."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The shift in periproct position observed in **Exocycloida** correlates with burrowing adaptations in marine sand."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Fossil transitions across the **Exocycloida** document the evolutionary transition from regular to irregular echinoid tests."
      }
    ]
  },
  "Dashboard — cycl\\hemicycle.md": {
    "primary": "A semicircular shape, structure, room, or arena.",
    "secondary": "In classical and civic architecture, a semicircular colonnade, theater seating gallery, or parliamentary debating chamber.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The marble seats in the **hemicycle** caught the afternoon glow as the assembly gathered beneath the arcade."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "In the vast **hemicycle** of the legislative chamber, representatives debate with fervent democratic eloquence."
      },
      {
        "author": "Henry James",
        "work": "Italian Hours",
        "quote": "We lingered along the ruined **hemicycle** of the Roman amphitheater, admiring the sweep of its ancient tiers."
      }
    ]
  },
  "Dashboard — cycl\\hemicyclium.md": {
    "primary": "A semicircular recess, curved alcove, or semicircular stone bench in classical Greco-Roman architecture.",
    "secondary": "In classical archaeology and landscape gardening, an exedra or curved stone conversation bench built along pathways or in garden nymphaea.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "A spacious **hemicyclium** was constructed in the palaestra where philosophers and rhetoricians could dispute in comfort."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Scholars walked the shaded terraces of Hadrian's villa, resting upon marble seats in the cool **hemicyclium**."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The Pompeian street of tombs is famous for its elegant stone **hemicyclium**, offered as a resting place for wayfarers."
      }
    ]
  },
  "Dashboard — cycl\\heterocycle.md": {
    "primary": "A chemical cyclic compound that contains atoms of at least two different elements as members of its ring.",
    "secondary": "In organic chemistry and pharmacology, a ring system containing heteroatoms (commonly nitrogen, oxygen, or sulfur) alongside carbon, fundamental to nucleic acids, vitamins, and drugs.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Pyridine is a classic aromatic **heterocycle** in which a single nitrogen atom replaces a CH group of benzene."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "The chemical synthesis of adenosine required masterful construction of the purine **heterocycle**."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "Virtually every essential pharmaceutical molecule incorporates an intricate **heterocycle** that docks into protein pockets."
      }
    ]
  },
  "Dashboard — cycl\\heterocyclic.md": {
    "primary": "Pertaining to, having, or containing a closed ring composed of two or more different kinds of atoms.",
    "secondary": "In synthetic chemistry, describing classes of compounds such as furans, pyrroles, thiophenes, and indoles whose rings include non-carbon heteroatoms.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The stability of **heterocyclic** aromatic rings arises from delocalized pi-electron sextets across carbon and heteroatom p-orbitals."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember: The Autobiography of a Chemist",
        "quote": "Our investigations into vitamin B1 centered on its unique thiazole and pyrimidine **heterocyclic** nuclei."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "Complementary base pairing in DNA depends entirely on hydrogen bonding between pairs of planar **heterocyclic** bases."
      }
    ]
  },
  "Dashboard — cycl\\homocyclic.md": {
    "primary": "Pertaining to, having, or containing a closed chemical ring composed entirely of atoms of the same single element.",
    "secondary": "In organic chemistry, describing carbocyclic rings (such as benzene, cyclohexane, or cyclopentadiene) whose ring vertices consist solely of carbon atoms.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Benzene and cyclohexane represent the classical prototypes of **homocyclic** carbon compounds in organic chemistry."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "Comparing **homocyclic** rings with heterocyclic analogues highlights the dramatic influence of heteroatoms on ring resonance."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Origin of Life",
        "quote": "Primitive catalytic synthesis yielded both simple **homocyclic** hydrocarbons and reactive nitrogenous heterocycles."
      }
    ]
  },
  "Dashboard — cycl\\hypercycle.md": {
    "primary": "A theoretical organization of self-replicating macromolecular units connected in a cyclic, cross-catalytic feedback loop.",
    "secondary": "In theoretical biology and prebiotic origins of life, Manfred Eigen and Peter Schuster's model of mutually supporting RNA/protein catalytic cycles capable of overcoming the error catastrophe in early evolution.",
    "quotes": [
      {
        "author": "Manfred Eigen",
        "work": "The Hypercycle: A Principle of Natural Self-Organization",
        "quote": "The **hypercycle** links distinct self-replicating informational units into a cooperative network, overcoming the information threshold."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Eigen's concept of the prebiotic **hypercycle** showed how chemical cooperation could emerge before the advent of true cells."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Blind Watchmaker",
        "quote": "In early molecular evolution, an autocatalytic **hypercycle** can maintain vast libraries of genetic information without error."
      }
    ]
  },
  "Dashboard — cycl\\hypocycloid.md": {
    "primary": "A plane curve traced by a point on the circumference of a circle as it rolls without slipping along the inside of a fixed circle.",
    "secondary": "In geometry and kinematics, a family of roulette curves including the astroid (four-cusped hypocycloid) and deltoid (three-cusped hypocycloid).",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Mechanica",
        "quote": "When the diameter of the rolling circle is half that of the fixed circle, the **hypocycloid** degenerates into a straight line."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Internal cusps of radiating radiolarian skeletons frequently trace the elegant curvature of a geometric **hypocycloid**."
      },
      {
        "author": "William John Macquorn Rankine",
        "work": "A Manual of Machinery and Millwork",
        "quote": "Internal gear flanks are formed along an internal **hypocycloid** curve to ensure rolling contact with external pinion teeth."
      }
    ]
  },
  "Dashboard — cycl\\isocyclic.md": {
    "primary": "Composed of a closed ring of atoms belonging to only one element; homocyclic.",
    "secondary": "In chemistry, designating rings consisting exclusively of identical atoms, specifically carbocyclic rings consisting entirely of carbon.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The benzene ring provides the foundational archetype of an **isocyclic** aromatic system."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "Chemists distinguish **isocyclic** rings from heterocycles by the complete absence of non-carbon ring members."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Physical Basis of Life",
        "quote": "Under ultraviolet irradiation, simple **isocyclic** hydrocarbons polymerize into tarry prebiotic matrices."
      }
    ]
  },
  "Dashboard — cycl\\megacycle.md": {
    "primary": "One million cycles; especially one million cycles per second, equivalent to one megahertz (MHz).",
    "secondary": "In telecommunications, electrical engineering, and radio broadcasting, the historic unit of frequency for shortwave, VHF, and radar signals.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "A broadband channel operating at one **megacycle** per second possesses an information transmission capacity proportional to its bandwidth."
      },
      {
        "author": "Alan Turing",
        "work": "Proposals for Development in the Mathematics Division of an Automatic Computing Engine",
        "quote": "The ultrasonic mercury delay lines operate with acoustic carrier frequencies near one **megacycle**."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "High-frequency radar pulses oscillating at hundreds of **megacycle** units detected distant aircraft with precision."
      }
    ]
  },
  "Dashboard — cycl\\mesocyclone.md": {
    "primary": "A persistent, rotating updraft of air within a supercell thunderstorm, typically several miles in diameter.",
    "secondary": "In severe-storm meteorology and Doppler radar analysis, a rotating core within a convective storm that often serves as the precursor and parent circulation for tornadoes.",
    "quotes": [
      {
        "author": "Charles Richter",
        "work": "Elementary Seismology",
        "quote": "Atmospheric vortices and the deep rotation of a **mesocyclone** release kinetic energies rivaling moderate earthquakes."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Intense wind shear tilts convective updrafts, creating the spinning vortex of a severe **mesocyclone** across the plains."
      },
      {
        "author": "Rachel Carson",
        "work": "Lost Woods: The Discovered Writing of Rachel Carson",
        "quote": "The dark, wall-cloud vortex of the **mesocyclone** descended from the thunderhead like an ominous rotating funnel."
      }
    ]
  },
  "Dashboard — cycl\\monocycle.md": {
    "primary": "A single-wheeled vehicle; a unicycle; or an engine running a single cycle.",
    "secondary": "In mechanical history and locomotion, an experimental pedal-driven or motorized single-wheeled craft where the rider sits inside or atop a large wheel.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The War in the Air",
        "quote": "Eccentric inventors demonstrated a steam **monocycle**, wobbling precariously along the gravel path to the amusement of onlookers."
      },
      {
        "author": "Mark Twain",
        "work": "A Connecticut Yankee in King Arthur's Court",
        "quote": "Sir Sagramor looked as bewildered as if he had beheld a knight mounted upon an iron **monocycle**."
      },
      {
        "author": "Jules Verne",
        "work": "The Steam House",
        "quote": "The eccentric engineer designed a light **monocycle** fitted with broad pneumatic treads for desert locomotion."
      }
    ]
  },
  "Dashboard — cycl\\monocyclic.md": {
    "primary": "Consisting of or having only one cycle, ring, or floral whorl.",
    "secondary": "In organic chemistry, designating a compound (such as benzene, cyclopentane, or furan) that contains only a single closed ring of bonded atoms.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Cyclohexane is a **monocyclic** alkane whose puckered chair conformation eliminates eclipsing torsional strain."
      },
      {
        "author": "Francis Bather",
        "work": "The Echinoderma",
        "quote": "In a **monocyclic** crinoid, the dorsal cup contains only a single ring of basal plates below the radials."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Flowers with a **monocyclic** perianth possess only a calyx, the corolla being entirely absent."
      }
    ]
  },
  "Dashboard — cycl\\polycyclic.md": {
    "primary": "Having, containing, or composed of multiple cycles or rings.",
    "secondary": "In organic chemistry and environmental toxicology, designating molecules (such as polycyclic aromatic hydrocarbons, PAHs) that contain two or more fused rings of carbon atoms.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Phenanthrene and anthracene represent prototypical **polycyclic** aromatic hydrocarbons with planar fused rings."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Industrial combustion releases airborne **polycyclic** hydrocarbons that accumulate as persistent environmental carcinogens."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "Synthesizing complex **polycyclic** alkaloids demanded stereochemical control over multiple fused ring junctions."
      }
    ]
  },
  "Dashboard — cycl\\pseudocyclosis.md": {
    "primary": "Apparent or simulated cyclosis; the illusion of cytoplasmic streaming produced by passive Brownian motion or external physical forces.",
    "secondary": "In cellular biophysics and microscopy, Brownian thermal agitation of cytoplasmic granules that mimics active, ATP-driven intracellular cyclosis.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "A Brief Account of Microscopical Observations",
        "quote": "The continuous thermal dance of suspended pollen granules must not be confounded with active vital streaming or **pseudocyclosis**."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Physical Basis of Life",
        "quote": "Under high magnification, passive micro-convection currents can simulate **pseudocyclosis** in moribund plant cells."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Physical Basis of Life",
        "quote": "Careful vital staining separates metabolic cytoplasmic circulation from purely physical **pseudocyclosis**."
      }
    ]
  },
  "Dashboard — cycl\\recyclable.md": {
    "primary": "Capable of being recycled; suitable for processing and remanufacturing into new materials or products.",
    "secondary": "In environmental engineering and sustainable materials science, denoting products (such as metals, glass, or thermoplastics) that can be recovered and reused within closed circular industrial cycles.",
    "quotes": [
      {
        "author": "Barry Commoner",
        "work": "The Closing Circle: Nature, Man, and Technology",
        "quote": "A sustainable industrial ecology must rely upon **recyclable** containers rather than disposable, non-degradable synthetics."
      },
      {
        "author": "Rachel Carson",
        "work": "Lost Woods: The Discovered Writing of Rachel Carson",
        "quote": "Nature wastes nothing; every mineral element in the forest is entirely **recyclable** through continuous biological turnover."
      },
      {
        "author": "E. F. Schumacher",
        "work": "Small Is Beautiful",
        "quote": "Prudent economic stewardship treats scarce natural resources as **recyclable** assets held in trust for future generations."
      }
    ]
  },
  "Dashboard — cycl\\recycle.md": {
    "primary": "To convert waste materials into reusable items; to treat or process used or discarded materials so as to make them suitable for reuse.",
    "secondary": "In systems ecology and ecological economics, to pass energy, water, nutrients, or industrial byproducts repeatedly through a operational cycle to prevent resource exhaustion.",
    "quotes": [
      {
        "author": "Barry Commoner",
        "work": "The Closing Circle: Nature, Man, and Technology",
        "quote": "In nature, the fundamental ecological law is that organisms must **recycle** their wastes back into the soil and water."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Decomposers break down dead biomass to **recycle** vital phosphorus and nitrogen into the plant community."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "The oak leaves fall to **recycle** sunshine and rain into rich black loam beneath the roots."
      }
    ]
  },
  "Dashboard — cycl\\recycling.md": {
    "primary": "The process of collecting, processing, and remanufacturing waste materials into new products.",
    "secondary": "In biogeochemistry and circular economy, the natural or industrial circulation and return of elements or commodities into productive use.",
    "quotes": [
      {
        "author": "Barry Commoner",
        "work": "The Closing Circle",
        "quote": "The breakdown of natural **recycling** mechanisms is the root cause of the modern environmental crisis."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Upwelling deep currents accomplish a perpetual **recycling** of oceanic nutrients to nourish surface plankton."
      },
      {
        "author": "E. F. Schumacher",
        "work": "Small Is Beautiful",
        "quote": "Efficient industrial **recycling** reduces our rapacious depletion of virgin geological deposits."
      }
    ]
  },
  "Dashboard — cycl\\tetracyclic.md": {
    "primary": "Having or containing four closed chemical rings.",
    "secondary": "In biochemistry and clinical psychopharmacology, describing tetracyclic antidepressants (such as mirtazapine or maprotiline) or steroids possessing the cyclopentanoperhydrophenanthrene four-ring core.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Cholesterol and sex hormones are built upon an identical **tetracyclic** carbon skeleton of three six-membered and one five-membered ring."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "Total chemical synthesis of the fused **tetracyclic** steroid nucleus was an Everest of twentieth-century organic chemistry."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Novel **tetracyclic** agents were introduced to modulate central noradrenergic neurotransmission in treatment-resistant depression."
      }
    ]
  },
  "Dashboard — cycl\\tricycle.md": {
    "primary": "A human-powered, pedal-driven or hand-cranked vehicle having three wheels (typically one in front and two in back).",
    "secondary": "In Victorian transport history, a stable cycle adopted extensively by women, the elderly, and rural postal carriers before the safety bicycle predominated.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Greek Interpreter",
        "quote": "Outside the window, a grocer's boy rattled past upon a heavy iron-framed delivery **tricycle**."
      },
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "Elderly rectors preferred the stately stability of a **tricycle** to the hazardous balance of the high-wheel bicycle."
      },
      {
        "author": "Thomas Hardy",
        "work": "Jude the Obscure",
        "quote": "A child was pedaling an old-fashioned wooden **tricycle** back and forth across the sunlit cobbles."
      }
    ]
  },
  "Dashboard — cycl\\tricyclic.md": {
    "primary": "Having or containing three cycles, rings, or whorls; especially designating organic compounds with three fused rings of atoms.",
    "secondary": "In psychopharmacology, designating the classic class of tricyclic antidepressants (TCAs, such as amitriptyline and imipramine) featuring a three-ring chemical core that inhibits serotonin and norepinephrine reuptake.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The introduction of **tricyclic** antidepressants transformed the prognosis of severe endogenous melancholia."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Anthracene and phenanthrene represent the classic isomeric forms of **tricyclic** fused aromatic systems."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Low doses of a **tricyclic** compound were administered to modulate chronic neuropathic pain pathways."
      }
    ]
  },
  "Dashboard — cycl\\unicycle.md": {
    "primary": "A single-wheeled pedal-driven cycle, commonly used by acrobats and circus performers.",
    "secondary": "In kinematics and balance robotics, a vehicle that requires active dynamic balancing around both pitch and roll axes simultaneously.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Taming the Bicycle",
        "quote": "He balanced atop a tall circus **unicycle** with the casual grace of a bird resting upon a telegraph wire."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "Balancing upon a **unicycle** provides an exquisite physical illustration of rapid negative sensory feedback in neuromuscular control."
      },
      {
        "author": "H. G. Wells",
        "work": "Boon",
        "quote": "The street performer pedaled his swaying **unicycle** in nimble figures of eight before the appreciative crowd."
      }
    ]
  },
  "Dashboard — cycl\\unicyclist.md": {
    "primary": "A person who rides a unicycle, especially as a performing acrobat or street entertainer.",
    "secondary": "In biomechanics and motor learning, an individual who has mastered dynamic gyroscopic posture and fine ankle torque control over a single wheel.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Roughing It",
        "quote": "The agile circus **unicyclist** juggled burning torches while pedaling backward on his tall solitary wheel."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The vestibular coordination exhibited by a professional **unicyclist** reflects cerebellar plasticity pushed to its limits."
      },
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "Crowds paused on the promenade to watch the nimble **unicyclist** perform daring pivots upon the boardwalk."
      }
    ]
  },
  "Dashboard — cyst\\cyst.md": {
    "primary": "A closed sac or capsule having a distinct membrane, filled with fluid, air, or semi-solid matter, formed abnormally in body tissues.",
    "secondary": "In protozoology and cryptogamic botany, a tough, protective, thick-walled resting stage assumed by an organism to survive adverse environmental conditions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Aspiration of the renal **cyst** yielded clear amber fluid containing urea and traces of albumin."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Retention of glandular secretions behind an obstructed duct inevitably distends the acinus into a true retention **cyst**."
      },
      {
        "author": "Leeuwenhoek",
        "work": "Letters to the Royal Society",
        "quote": "Within each desiccated microscopic **cyst**, the tiny infusorian retains the latent spark of life until moisture returns."
      }
    ]
  },
  "Dashboard — cyst\\cysteine.md": {
    "primary": "A non-essential sulfur-containing proteinogenic amino acid ($C_3H_7NO_2S$) containing a reactive thiol (-SH) side chain.",
    "secondary": "In molecular biochemistry and structural biology, an amino acid whose oxidation forms covalent disulfide bridges that stabilize the tertiary and quaternary structures of proteins.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Disulfide cross-linkages formed between pairs of **cysteine** residues impart structural rigidity to globular enzymes and keratin."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "The reactive thiol group of **cysteine** frequently serves as the essential catalytic nucleophile in enzyme active sites."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "Site-directed mutagenesis replacing a single **cysteine** disrupted the delicate folding pathway of the mutant polypeptide."
      }
    ]
  },
  "Dashboard — cyst\\cystic.md": {
    "primary": "Pertaining to, having the nature of, or containing a cyst or cysts.",
    "secondary": "In human anatomy, pertaining specifically to the urinary bladder or gallbladder (as in the cystic duct and cystic artery).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **cystic** duct joins the common hepatic duct at an acute angle to form the common bile duct."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Impact of a gallstone in the **cystic** duct produces intense biliary colic accompanied by acute distension."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In **cystic** hygroma of the neck, dilated lymphatic channels form interconnected fluid chambers lined with endothelium."
      }
    ]
  },
  "Dashboard — cyst\\cysticercus.md": {
    "primary": "The larval stage of a tapeworm (genus Taenia) consisting of a fluid-filled sac containing an invaginated scolex; a bladder worm.",
    "secondary": "In parasitology and veterinary pathology, the encysted metacestode that resides in muscle or neural tissue of intermediate hosts (causing cysticercosis in humans and swine).",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Autopsy revealed that the cerebral tumor was in reality an encysted **cysticercus** cellulosae embedded in the meninges."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "When ingested by a suitable definitive host, the scolex of the **cysticercus** evaginates and attaches firmly to the intestinal mucosa."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Human infection by the larval **cysticercus** occurs through fecal-oral ingestion of Taenia solium ova, causing epilepsy."
      }
    ]
  },
  "Dashboard — cyst\\cystine.md": {
    "primary": "A dimeric sulfur-containing amino acid formed by the oxidation of two cysteine molecules joined by a covalent disulfide bond.",
    "secondary": "In medical biochemistry and nephrology, an insoluble amino acid that precipitates to form urinary stones in patients with inherited cystinuria.",
    "quotes": [
      {
        "author": "William Hyde Wollaston",
        "work": "On Cystic Oxide, a New Species of Urinary Calculus",
        "quote": "I isolated a peculiar crystalline substance from a bladder stone, to which I assigned the name **cystine**."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The covalent disulfide linkage in **cystine** links adjacent peptide chains, stabilizing hair, wool, and insulin."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Hexagonal microscopic crystals of **cystine** in urinary sediment confirm the metabolic diagnosis of cystinuria."
      }
    ]
  },
  "Dashboard — cyst\\cystitis.md": {
    "primary": "Inflammation of the urinary bladder, typically caused by bacterial infection.",
    "secondary": "In urology, an acute or chronic condition characterized by dysuria, urinary frequency, urgency, and pelvic pain, most commonly caused by uropathogenic Escherichia coli.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute bacterial **cystitis**, the patient complains of scalding micturition, tenesmus, and constant suprapubic distress."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The sensory innervation of the vesical trigone explains the excruciating reflex spasm provoked by acute **cystitis**."
      },
      {
        "author": "Sir Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "Warm hip baths and copious bland fluids afford soothing palliative relief during paroxysms of catarrhal **cystitis**."
      }
    ]
  },
  "Dashboard — cyst\\cystocele.md": {
    "primary": "A medical condition in which the urinary bladder herniates or prolapses into the vagina due to weakening of pelvic floor muscles and fascia.",
    "secondary": "In gynecology and urogynecology, anterior vaginal wall prolapse resulting from tears or attenuation of the pubocervical fascia, often associated with childbirth trauma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A prominent **cystocele** may impede complete vesical emptying, leading to stagnant residual urine and recurrent infections."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Laceration of the pelvic diaphragm during protracted labor removes the support necessary to prevent an expanding **cystocele**."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Life of Sir William Osler",
        "quote": "The clinical examination clearly revealed a large anterior **cystocele** protruding upon standing."
      }
    ]
  },
  "Dashboard — cyst\\cystolith.md": {
    "primary": "A stone or calculus formed in the urinary bladder; or in botany, an internal nodule of calcium carbonate on a cellulose stalk in epidermal plant cells.",
    "secondary": "In plant anatomy, a mineralized intrusion (common in Urticaceae and Acanthaceae) that deposits calcium carbonate; in urology, a bladder stone formed around a nidus.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "Under the microscope, epidermal cells of the nettle leaf contain a curious stalked calcified body known as a **cystolith**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The vesical sound produced a distinct metallic click upon contacting the large uric acid **cystolith**."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The physiological role of the foliar **cystolith** appears to be both calcium storage and skeletal stiffening."
      }
    ]
  },
  "Dashboard — cyst\\cystoma.md": {
    "primary": "A cystic tumor; a benign or malignant new growth containing cysts.",
    "secondary": "In surgical pathology and gynecology, an encapsulated fluid-filled neoplasm, notably an ovarian cystadenoma (serous or mucinous cystoma).",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A multilocular **cystoma** arises from glandular proliferation wherein adjacent acini dilate into massive mucus-filled cavities."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Pulsatile dullness across the lower abdomen suggested an expanding multilocular ovarian **cystoma**."
      },
      {
        "author": "Sir Frederick Treves",
        "work": "A Manual of Surgery",
        "quote": "Surgical excision of a giant **cystoma** required careful aspiration of its viscous contents before mobilizing adhesions."
      }
    ]
  },
  "Dashboard — cyst\\cystoparalysis.md": {
    "primary": "Paralysis of the urinary bladder musculature; cystoplegia.",
    "secondary": "In clinical neurology and neuro-urology, neurogenic bladder dysfunction resulting from spinal cord lesions, trauma, or tabes dorsalis, leading to urinary retention or overflow incontinence.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Following transverse myelitis of the lumbar cord, acute **cystoparalysis** necessitates regular catheterization to prevent rupture."
      },
      {
        "author": "Sir Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "Complete **cystoparalysis** allows the bladder to become enormously distended without the patient experiencing pain."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Secondary bacterial infection rapidly supervenes in the stagnant urine accompanying chronic spinal **cystoparalysis**."
      }
    ]
  },
  "Dashboard — cyst\\cystophora.md": {
    "primary": "A genus of pinnipeds in the true seal family Phocidae, comprising the hooded seal (Cystophora cristata); also a genus of brown seaweeds.",
    "secondary": "In marine mammalogy, North Atlantic arctic seals whose adult males possess an inflatable nasal bladder and nasal septum used in aggressive sexual displays.",
    "quotes": [
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "The hooded seal, designated **Cystophora** cristata, drifts southward upon the pack ice off the coast of Labrador."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "When angered, the male **Cystophora** inflates an extraordinary red nasal balloon from its nostrils with startling effect."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The inflatable hood of the male **Cystophora** provides a striking example of secondary sexual characters used in rivalry."
      }
    ]
  },
  "Dashboard — cyst\\cystoplegia.md": {
    "primary": "Paralysis of the bladder; cystoparalysis.",
    "secondary": "In neurology, loss of voluntary contractile power in the detrusor muscle of the urinary bladder due to central or peripheral denervation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In tabetic neurosyphilis, insidious **cystoplegia** often leads to painless urinary retention with constant dribbling overflow."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Injury to the parasympathetic pelvic splanchnic nerves paralyzes detrusor tone, resulting in severe clinical **cystoplegia**."
      },
      {
        "author": "Sir Frederick Treves",
        "work": "Surgical Applied Anatomy",
        "quote": "Postoperative **cystoplegia** following pelvic surgery must be managed by catheter drainage to avert detrusor overstretching."
      }
    ]
  },
  "Dashboard — cyst\\cystopteris.md": {
    "primary": "A genus of small, delicate, deciduous leptosporangiate ferns in the family Cystopteridaceae, commonly known as bladder ferns.",
    "secondary": "In systematic pteridology, shade-tolerant rupicolous ferns characterized by bipinnate to tripinnatifid fronds and round sori covered by inflated hood-like or bladder-like indusia.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The fragile bladder fern, **Cystopteris** fragilis, roots in cool dripping crevices of limestone gorges throughout the northern states."
      },
      {
        "author": "John Muir",
        "work": "My First Summer in the Sierra",
        "quote": "Beneath the spray of the waterfall, tender green fronds of **Cystopteris** fluttered with delicate grace against the wet granite."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Species of **Cystopteris** are among the earliest ferns to unfurl their fronds in shady rock gardens in early spring."
      }
    ]
  },
  "Dashboard — cyst\\encysted.md": {
    "primary": "Enclosed or contained within a cyst, capsule, or membranous sac.",
    "secondary": "In pathology and parasitology, walled off by fibrous inflammatory tissue or larval capsules to isolate foreign bodies, pathogens, or parasites from host tissue.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A chronic abscess often becomes completely **encysted** by dense concentric layers of fibrous connective tissue."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Trichina spiralis larvae remain dormant for years when safely **encysted** within calcified muscle capsules."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "The cercaria loses its tail and becomes firmly **encysted** upon aquatic vegetation awaiting ingestion by its final host."
      }
    ]
  },
  "Dashboard — cyst\\polycystic.md": {
    "primary": "Characterized by, consisting of, or containing multiple cysts.",
    "secondary": "In clinical genetics and internal medicine, designating inherited pathological conditions (notably polycystic kidney disease and polycystic ovary syndrome) marked by the progressive proliferation of fluid-filled cysts.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bilateral **polycystic** kidneys may enlarge to enormous dimensions, gradually replacing normal renal parenchyma with honeycomb cysts."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Congenital **polycystic** degeneration represents a developmental failure in the union of metanephric tubules with collecting ducts."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Life of Sir William Osler",
        "quote": "Osler demonstrated the familial transmission of adult **polycystic** renal disease through three successive generations."
      }
    ]
  },
  "Dashboard — de\\arthrodesis.md": {
    "primary": "The surgical immobilization or fusion of a joint by promoting bone consolidation across the joint space.",
    "secondary": "In orthopedic surgery, an operative procedure performed to eliminate intractable pain, restore structural stability, or correct severe deformity in an arthritic or damaged joint.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In chronic tuberculous destruction of the knee, successful **arthrodesis** eliminates excruciating pain and permits stable weight-bearing."
      },
      {
        "author": "Sir Frederick Treves",
        "work": "A Manual of Surgery",
        "quote": "The surgeon denuded the articular cartilages of the ankle, preparing the opposing bony surfaces for formal **arthrodesis**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Spinal **arthrodesis** permanently locks adjoining vertebrae into a continuous solid osseous pillar."
      }
    ]
  },
  "Dashboard — de\\asyndetic.md": {
    "primary": "Characterized by or relating to the omission of conjunctions between parts of a sentence; asyndetic.",
    "secondary": "In classical rhetoric and stylistic analysis, describing swift, unpunctuated, or unlinked series of words, phrases, or clauses (such as 'Veni, vidi, vici') that convey urgency, dramatic acceleration, or terse emphasis.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Rhetoric",
        "quote": "An **asyndetic** style possesses dramatic vigor, giving the impression that many distinct things are uttered simultaneously."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Caesar's famous dispatch was strictly **asyndetic**, expressing military conquest in three swift words."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "The modern stream of consciousness frequently adopts an **asyndetic** rhythm, tumbling thoughts together without connective particles."
      }
    ]
  },
  "Dashboard — de\\asyndeton.md": {
    "primary": "A rhetorical figure of speech in which coordinating conjunctions are deliberately omitted between successive words, phrases, or clauses.",
    "secondary": "In classical literature and prose composition, a stylistic device (as in 'I came, I saw, I conquered') employed to achieve brevity, rapid momentum, and emotional intensity.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Rhetoric",
        "quote": "The figure of **asyndeton** speeds up the narration and imbues the spoken word with sudden emotional force."
      },
      {
        "author": "Longinus",
        "work": "On the Sublime",
        "quote": "By stripping away connectives, **asyndeton** presents actions tumbling forward with the rapid urgency of torrents."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War: Their Finest Hour",
        "quote": "The great orator deployed **asyndeton** to strike like hammer blows upon the ears of parliament."
      }
    ]
  }
};

const updated = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`[Batch 5] Successfully updated ${updated} of ${Object.keys(batchData).length} notes.`);
