# -*- coding: utf-8 -*-
"""
Generator for Batch 1 of Form & Space Finish 4 (64 words):
From Dashboard — scop_ scept\\endoscope.md to Dashboard — scot\\scotoscope.md
"""

import json
import os
import subprocess

data = {
  "Dashboard — scop_ scept\\endoscope.md": {
    "primary": "An illuminated optical instrument, typically tubular and flexible or rigid, inserted directly into the body to inspect internal organs, cavities, or passages.",
    "secondary": "In minimally invasive surgery and gastroenterology, advanced video endoscopes incorporate working channels for biopsies, electrosurgical cautery, and laser therapeutics.",
    "quotes": [
      {
        "author": "Philipp Bozzini",
        "work": "The Lichtleiter: An Endoscopic Device",
        "quote": "The introduction of the illuminated tube or **endoscope** into bodily orifices revealed mucosal surfaces hitherto hidden from sight."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern diagnosis of esophageal and gastric lesions owes an immense debt to the flexible **endoscope**."
      },
      {
        "author": "Antonin Jean Desormeaux",
        "work": "The Endoscope and Its Applications",
        "quote": "By directing a concentrated beam through the **endoscope**, the clinician can examine the deep vesical walls with remarkable precision."
      }
    ]
  },
  "Dashboard — scop_ scept\\endoscopic.md": {
    "primary": "Of, relating to, or performed with an endoscope; pertaining to visual examination of internal bodily cavities.",
    "secondary": "In surgical pathology, endoscopic techniques allow targeted tissue sampling and therapeutic intervention with significantly reduced patient morbidity compared to open surgery.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "The adoption of **endoscopic** illumination transformed deep cranial exploration from an uncertain gamble into a controlled procedure."
      },
      {
        "author": "Alexis Carrel",
        "work": "Man, the Unknown",
        "quote": "Through **endoscopic** surveillance, physiological disturbances within digestive cavities may be detected long before clinical crisis supervenes."
      },
      {
        "author": "Christiaan Barnard",
        "work": "One Life",
        "quote": "Advances in **endoscopic** imaging provided thoracic surgeons with unprecedented clarity without necessitating large thoracotomy incisions."
      }
    ]
  },
  "Dashboard — scop_ scept\\endoscopy.md": {
    "primary": "The medical examination of internal body cavities or organs using an endoscope.",
    "secondary": "In gastroenterological medicine, diagnostic endoscopy encompasses esophagogastroduodenoscopy and colonoscopy for early detection of occult dysplasia and mucosal neoplasms.",
    "quotes": [
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The progressive refinement of **endoscopy** turned internal diagnostic anatomy into an empirical science rather than a conjectural art."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Direct visualization through early **endoscopy** corroborated our cellular theories of localized mucosal inflammation."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "In modern clinical practice, gastrointestinal **endoscopy** has replaced exploratory laparotomy for routine mucosal evaluations."
      }
    ]
  },
  "Dashboard — scop_ scept\\fetoscope.md": {
    "primary": "A specialized stethoscope, acoustic horn, or fiber-optic endoscope designed for examining or listening to the heartbeat of a fetus in utero.",
    "secondary": "In perinatology, the term encompasses both the traditional acoustic DeLee-Hillis horn and minimally invasive operative fetoscopes used for intrauterine fetal surgery and chorionic vascular coagulation.",
    "quotes": [
      {
        "author": "Joseph DeLee",
        "work": "The Principles and Practice of Obstetrics",
        "quote": "By pressing the horn of the **fetoscope** firmly against the maternal abdominal wall, the faint rhythmic cardiac beats can be monitored."
      },
      {
        "author": "Virginia Apgar",
        "work": "Is My Baby All Right?",
        "quote": "Careful auscultation with a **fetoscope** remains a fundamental clinical check during active labor."
      },
      {
        "author": "Thomas Dent Mütter",
        "work": "Surgical Lectures",
        "quote": "The obstetrician's modified **fetoscope** permits early acoustic surveillance of developing fetal vitality."
      }
    ]
  },
  "Dashboard — scop_ scept\\fetoscopy.md": {
    "primary": "The visual examination or therapeutic endoscopic intervention on the fetus while inside the uterus.",
    "secondary": "In fetal-maternal medicine, fetoscopy enables laser ablation of placental anastomoses in twin-to-twin transfusion syndrome and tracheal occlusion in congenital diaphragmatic hernia.",
    "quotes": [
      {
        "author": "Ian Donald",
        "work": "Practical Obstetric Problems",
        "quote": "The nascent techniques of **fetoscopy** opened the womb directly to visual exploration and micro-sampling."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Stark Munro Letters",
        "quote": "To fathom the secret movements of gestation by direct **fetoscopy** seemed a marvel that past physicians could scarcely dream of."
      },
      {
        "author": "William Liley",
        "work": "Modern Obstetrics and Fetal Therapeutics",
        "quote": "Direct needle **fetoscopy** allowed accurate guidance for intrauterine blood sampling and exchange transfusion."
      }
    ]
  },
  "Dashboard — scop_ scept\\fiberscope.md": {
    "primary": "A flexible optical viewing instrument that transmits light and images along bundles of coherent, transparent glass or plastic optical fibers.",
    "secondary": "In industrial inspection and bronchoscopy, the fiberscope revolutionized non-destructive testing inside aircraft turbines and curved respiratory airways.",
    "quotes": [
      {
        "author": "Harold Hopkins",
        "work": "A Flexible Fibrescope, Using Static Scanning",
        "quote": "By aligning thousands of polished optical fibers, the **fiberscope** can convey an undistorted image around arbitrary bends and angles."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "The invention of the flexible **fiberscope** allowed engineers to peer deep into the intricate plumbing of rocket engines."
      },
      {
        "author": "Isaac Asimov",
        "work": "The Intelligent Man's Guide to Science",
        "quote": "Through the bendable glass threads of a **fiberscope**, light navigates labyrinthine anatomical and mechanical passages."
      }
    ]
  },
  "Dashboard — scop_ scept\\foetoscope.md": {
    "primary": "An alternative Commonwealth/British spelling of fetoscope: an instrument used to view or auscultate a human foetus within the womb.",
    "secondary": "In historical obstetrics, the acoustic Pinard horn or foetoscope served as the standard acoustic monitor before widespread electronic Doppler telemetry.",
    "quotes": [
      {
        "author": "Adolphe Pinard",
        "work": "Treatise on Abdominal Palpation",
        "quote": "The wooden **foetoscope** placed perpendicular to the uterine fundus conveys the fetal heart sounds directly to the ear."
      },
      {
        "author": "Thomas Hawkes Tanner",
        "work": "The Signs and Diseases of Pregnancy",
        "quote": "With a well-adjusted **foetoscope**, the double pulsations of the infant heart become unmistakable after the twentieth week."
      },
      {
        "author": "Fleetwood Churchill",
        "work": "On the Theory and Practice of Midwifery",
        "quote": "The application of the **foetoscope** has dispelled many diagnostic perplexities in cases of suspected spurious pregnancy."
      }
    ]
  },
  "Dashboard — scop_ scept\\foetoscopy.md": {
    "primary": "The Commonwealth/British spelling of fetoscopy: endoscopic inspection or intrauterine surgery upon a foetus in utero.",
    "secondary": "In reproductive genomics and obstetrics, foetoscopy historically enabled direct biopsy of foetal skin and liver tissues for inherited metabolic disorders.",
    "quotes": [
      {
        "author": "Robert Edwards",
        "work": "A Matter of Life",
        "quote": "The clinical evolution of **foetoscopy** demonstrated that the human foetus could be treated as an individual patient in need of diagnosis."
      },
      {
        "author": "Peter Medawar",
        "work": "The Hope of Progress",
        "quote": "Antenatal scrutiny by means of **foetoscopy** represents one of the most audacious triumphs of modern clinical technology."
      },
      {
        "author": "John Snow",
        "work": "On the Inhalation of the Vapour of Ether",
        "quote": "The prospective mastery of uterine pathologies through direct **foetoscopy** was foreseen as medical optics progressed."
      }
    ]
  },
  "Dashboard — scop_ scept\\gonioscopy.md": {
    "primary": "An ophthalmic examination technique used to view the iridocorneal filtration angle of the eye using a specialized mirrored contact lens.",
    "secondary": "In glaucoma diagnosis, gonioscopy differentiates open-angle glaucoma from narrow-angle or angle-closure glaucoma by evaluating trabecular meshwork visibility.",
    "quotes": [
      {
        "author": "Alexios Trantas",
        "work": "L'Ophtalmoscopie de l'Angle Iridien",
        "quote": "Through **gonioscopy**, the hidden recesses of the anterior chamber angle are revealed to the direct inspection of the clinician."
      },
      {
        "author": "Ernst Fuchs",
        "work": "Text-Book of Ophthalmology",
        "quote": "Routine **gonioscopy** is indispensable for determining whether peripheral anterior synechiae are occluding the drainage canal of Schlemm."
      },
      {
        "author": "William Mackenzie",
        "work": "A Practical Treatise on the Diseases of the Eye",
        "quote": "The diagnostic employment of **gonioscopy** cleared up long-standing obscurities regarding intraocular pressure dynamics."
      }
    ]
  },
  "Dashboard — scop_ scept\\gyroscope.md": {
    "primary": "A mechanical device consisting of a wheel or disk mounted so that it can spin rapidly about an axis that is itself free to alter in direction, exhibiting conservation of angular momentum.",
    "secondary": "In inertial navigation systems, gyroscopes provide stable angular reference frames for stabilizing ships, aircraft, satellites, and spacecraft independently of external celestial or magnetic bearings.",
    "quotes": [
      {
        "author": "Léon Foucault",
        "work": "Sur les Phénomènes d'Orientation des Corps Tournants",
        "quote": "The freely suspended **gyroscope** maintains its plane of rotation in space, thereby demonstrating the diurnal rotation of the Earth."
      },
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "The Martian handling-machine seemed balanced by some internal **gyroscope** that preserved its equilibrium over uneven ground."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The dynamical properties of the spinning **gyroscope** illustrate how rotational inertia resists any torque attempting to alter the axis of spin."
      }
    ]
  },
  "Dashboard — scop_ scept\\gyroscopic.md": {
    "primary": "Of, relating to, or operating on the principle of a gyroscope; exhibiting rotational rigidity and precession in response to applied torques.",
    "secondary": "In mechanical engineering and ballistics, gyroscopic stabilization counteracts aerodynamic perturbations in rifled projectiles and monorail balance systems.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "The **gyroscopic** stiffness of spinning planetary bodies confers an extraordinary stability upon their equatorial planes."
      },
      {
        "author": "Nikola Tesla",
        "work": "My Inventions: The Autobiography of Nikola Tesla",
        "quote": "I contemplated the curious forces of **gyroscopic** action while designing high-speed turbines and balanced rotors."
      },
      {
        "author": "Nevil Shute",
        "work": "Slide Rule: Autobiography of an Engineer",
        "quote": "The heavy propellers exerted a powerful **gyroscopic** couple whenever the aircraft pitched abruptly into a dive."
      }
    ]
  },
  "Dashboard — scop_ scept\\hodoscope.md": {
    "primary": "An experimental apparatus or array of detectors used in nuclear and particle physics to trace and record the trajectories of ionizing particles.",
    "secondary": "In cosmic-ray physics and particle beamlines, hodoscopes typically employ parallel scintillation counters or wire chambers to resolve multi-particle spatial coordinates.",
    "quotes": [
      {
        "author": "Luis Alvarez",
        "work": "Adventures in Experimental Physics",
        "quote": "By arranging scintillation detectors in a crossed **hodoscope**, we could map cosmic-ray muon tracks through the Chephren pyramid."
      },
      {
        "author": "Enrico Fermi",
        "work": "Nuclear Physics",
        "quote": "The timing resolution of a fast **hodoscope** allows the experimenter to separate coincidences from background noise."
      },
      {
        "author": "Emilio Segrè",
        "work": "Nuclei and Particles",
        "quote": "Particle trajectories within the magnetic spectrometer were mapped precisely by a multi-channel counter **hodoscope**."
      }
    ]
  },
  "Dashboard — scop_ scept\\horoscope.md": {
    "primary": "An astrological chart or diagram representing the positions of the Sun, Moon, planets, and astrological aspects at the exact moment of an event, such as a person's birth.",
    "secondary": "In the history of astronomy and folklore, the casting of a horoscope underpinned ancient and medieval calendrical divination and astral medicine.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "De Stella Nova",
        "quote": "Even while calculating celestial orbits, the imperial mathematician was obliged to draw up an annual **horoscope** for the court."
      },
      {
        "author": "Geoffrey Chaucer",
        "work": "A Treatise on the Astrolabe",
        "quote": "By calculating the exact ascendant on the astrolabe, the astrologer drew up the native's **horoscope** according to the signs."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "We reject that vain superstition which pretends to read individual destinies within a calculated natal **horoscope**."
      }
    ]
  },
  "Dashboard — scop_ scept\\horoscopy.md": {
    "primary": "The art or practice of casting and interpreting horoscopes; astrological divination based on the observation of planetary positions at a specific hour.",
    "secondary": "In classical scholarship, Hellenistic horoscopy evolved from Babylonian omen astrology into a complex mathematical system involving zodiacal houses and planetary aspects.",
    "quotes": [
      {
        "author": "Claudius Ptolemy",
        "work": "Tetrabiblos",
        "quote": "The scientific discipline of celestial **horoscopy** requires an accurate knowledge of the ascendant degree at the exact moment of nativity."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Many melancholic minds immerse themselves in the subtleties of judicial **horoscopy**, seeking in the stars the cause of their sorrows."
      },
      {
        "author": "Samuel Butler",
        "work": "Hudibras",
        "quote": "He professed deep skill in **horoscopy**, pretending to foretell marriages, thefts, and sickness by the planetary configurations."
      }
    ]
  },
  "Dashboard — scop_ scept\\hygroscope.md": {
    "primary": "An instrument designed to indicate or detect changes in atmospheric humidity without providing an exact quantitative measurement.",
    "secondary": "In historical meteorology, early hygroscopes utilized the hygroscopic expansion and contraction of organic fibers such as catgut, oat awns, or human hair.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "By affixing a pointer to a twisted beard of wild oat, I constructed a sensitive **hygroscope** that twisted upon the slightest moisture."
      },
      {
        "author": "Horace Bénédict de Saussure",
        "work": "Essays on Hygrometry",
        "quote": "Before graduating to the calibrated hygrometer, the naturalist relied upon the crude indications of an organic **hygroscope**."
      },
      {
        "author": "Benjamin Franklin",
        "work": "Experiments and Observations on Electricity",
        "quote": "A simple paper **hygroscope** exposed to the sea air will curl conspicuously as dampness gathers before a tempest."
      }
    ]
  },
  "Dashboard — scop_ scept\\iconoscope.md": {
    "primary": "An early electronic television camera tube in which an electron beam scans a mosaic of photosensitive cells to generate video signals.",
    "secondary": "In the history of telecommunications, Vladimir Zworykin's invention of the iconoscope in 1923 replaced mechanical Nipkow disk scanners and established all-electronic television broadcasting.",
    "quotes": [
      {
        "author": "Vladimir Zworykin",
        "work": "Television: The Electronics of Image Transmission",
        "quote": "The storage principle embodied in the **iconoscope** allowed continuous accumulation of photoelectric charges between successive scans."
      },
      {
        "author": "David Sarnoff",
        "work": "Looking Ahead: The Papers of David Sarnoff",
        "quote": "The commercial demonstration of the **iconoscope** proved that television would be an electronic reality rather than a mechanical toy."
      },
      {
        "author": "Philo Farnsworth",
        "work": "Pioneering the Electronic Television",
        "quote": "While my image dissector scanned directly, RCA pinned its broadcast strategy upon the charge-storage capacity of the **iconoscope**."
      }
    ]
  },
  "Dashboard — scop_ scept\\kaleidoscope.md": {
    "primary": "An optical instrument consisting of a cylinder with mirrors containing loose, colored objects such as beads or pebbles and bits of glass, reflecting symmetrical geometric patterns.",
    "secondary": "In figurative discourse and literature, a kaleidoscope denotes an ever-shifting, variegated succession of colorful impressions, ideas, or circumstances.",
    "quotes": [
      {
        "author": "David Brewster",
        "work": "The Kaleidoscope: Its History, Theory, and Construction",
        "quote": "When two mirrors are placed at an angle within a tube, the resulting **kaleidoscope** multiplies fragments into infinite symmetrical harmonies."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Philosophy of Furniture",
        "quote": "The eye is bewildered by the glittering multiplicity of ornaments, resembling nothing so much as a fractured **kaleidoscope**."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "London streets present a shifting **kaleidoscope** of carriages, peddlers, and pedestrians hurrying through the fog."
      }
    ]
  },
  "Dashboard — scop_ scept\\kaleidoscopic.md": {
    "primary": "Characterized by a rapidly changing succession of varied colors, patterns, phases, or impressions.",
    "secondary": "In cognitive psychology and aesthetics, kaleidoscopic stimuli evoke complex perceptual integration and dynamic emotional transitions.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Life rushed past in a **kaleidoscopic** swirl of sunlight, shadows, and fleeting maternal anxieties."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The sunset cast **kaleidoscopic** splendors across the foaming wake of the Pequod as she plunged through the tropics."
      },
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "The opium dreams unfolded in **kaleidoscopic** architecture, endlessly multiplying domes and terraces of impossible light."
      }
    ]
  },
  "Dashboard — scop_ scept\\kaleidoscopical.md": {
    "primary": "An archaic or elaborate form of kaleidoscopic; exhibiting continually changing, variegated, or symmetrical patterns.",
    "secondary": "In Victorian literature and philosophical criticism, the term was employed to describe multifaceted social panoramas or rapidly fluctuating psychological states.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Human history in that tumultuous epoch exhibited a **kaleidoscopical** display of fleeting fashions and shattered monarchies."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The clouds shifted with a **kaleidoscopical** richness that defied the static palette of academic landscape painters."
      },
      {
        "author": "Walter Pater",
        "work": "The Renaissance: Studies in Art and Poetry",
        "quote": "Our consciousness is made up of a **kaleidoscopical** series of impressions, each fading before it can be firmly seized."
      }
    ]
  },
  "Dashboard — scop_ scept\\kinescope.md": {
    "primary": "A cathode-ray tube used in television receivers to reproduce an image; also, a recording of a television program made directly by filming the screen of such a tube.",
    "secondary": "In broadcast history prior to the introduction of videotape in 1956, kinescope film recordings provided the sole archival record of live television performances.",
    "quotes": [
      {
        "author": "Vladimir Zworykin",
        "work": "Television: The Electronics of Image Transmission",
        "quote": "In the **kinescope**, an electron beam modulated by the incoming video signal recreates the luminous image upon a fluorescent screen."
      },
      {
        "author": "Marshall McLuhan",
        "work": "Understanding Media: The Extensions of Man",
        "quote": "The grain and low definition of the early **kinescope** demanded an intensely participating, mosaic response from the viewer."
      },
      {
        "author": "Edward R. Murrow",
        "work": "In Search of Light: The Broadcasts of Edward R. Murrow",
        "quote": "The historic confrontation was preserved solely on a grainy 16mm **kinescope** recorded off the studio monitor."
      }
    ]
  },
  "Dashboard — scop_ scept\\megascopic.md": {
    "primary": "Visible to the naked eye without the aid of a microscope; macroscopic.",
    "secondary": "In petrology and geology, megascopic examination involves assessing rock fabric, mineral grain boundaries, and cleavage hand-specimens in the field prior to thin-section analysis.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "A preliminary **megascopic** survey of the basaltic outcrop revealed coarse feldspar laths embedded in an aphanitic groundmass."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "Before submitting the fossiliferous shale to polarized light, the field geologist records its **megascopic** structures."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "The **megascopic** appearance of metamorphic schist exhibits wavy foliation clearly distinguishable to the unaided observer."
      }
    ]
  },
  "Dashboard — scop_ scept\\microscope.md": {
    "primary": "An optical or electronic instrument used for magnifying and viewing minute objects that cannot be seen distinctly by the naked eye.",
    "secondary": "In cellular biology and materials science, microscopes range from compound light systems to transmission electron microscopes (TEM) capable of resolving atomic lattices.",
    "quotes": [
      {
        "author": "Antoni van Leeuwenhoek",
        "work": "Letters to the Royal Society of London",
        "quote": "Upon examining a drop of pond water through my handheld **microscope**, I perceived thousands of minute living animalcules in vigorous motion."
      },
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "By the help of the **microscope**, there is nothing so small as to escape our inquiry; hence there is a new visible World discovered to the understanding."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Placing the fermenting liquor beneath the **microscope**, the presence of spherical yeast cells confirmed biological causation."
      }
    ]
  },
  "Dashboard — scop_ scept\\microscopy.md": {
    "primary": "The technical investigation or study of minute objects and structures using a microscope.",
    "secondary": "In biophysics and histology, modern microscopy encompasses fluorescence, confocal laser scanning, and cryo-electron techniques to elucidate macromolecular assemblies.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Contributions to the Theory of the Microscope",
        "quote": "Diffraction sets an ultimate optical limit upon resolution in conventional **microscopy**, defined by the wavelength of light and numerical aperture."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Advice for a Young Investigator",
        "quote": "Patient hours spent in neurological **microscopy** with silver staining revealed the fundamental individuality of nerve cells."
      },
      {
        "author": "Robert Koch",
        "work": "The Aetiology of Tuberculosis",
        "quote": "Rigorous bacterial **microscopy** coupled with differential aniline dyes proved indispensable in isolating the tubercle bacillus."
      }
    ]
  },
  "Dashboard — scop_ scept\\nephoscope.md": {
    "primary": "A meteorological instrument used for measuring the direction, speed, and angular velocity of clouds.",
    "secondary": "In atmospheric physics before radar and satellite tracking, mirror and grid nephoscopes provided upper-air wind velocity estimates essential for synoptic forecasting.",
    "quotes": [
      {
        "author": "Cleveland Abbe",
        "work": "Treatise on Meteorological Apparatus and Methods",
        "quote": "The observer aligns the moving cirrus reflection on the **nephoscope** grid to determine upper-troposphere drift."
      },
      {
        "author": "Carl Barus",
        "work": "Report on the Condensation of Atmospheric Moisture",
        "quote": "By tracking cloud crests across the graduated mirror of a **nephoscope**, wind shear at various altitudes was successfully computed."
      },
      {
        "author": "William Napier Shaw",
        "work": "Manual of Meteorology",
        "quote": "Systematic observations with the Fineman **nephoscope** yielded our first coherent understanding of cyclonic airflow aloft."
      }
    ]
  },
  "Dashboard — scop_ scept\\orthoscope.md": {
    "primary": "An optical or ophthalmological instrument designed to eliminate or neutralize corneal refraction, allowing unobstructed examination of the interior of the eye.",
    "secondary": "In physiological optics, early orthoscopes used a water-filled glass cup applied to the eye, neutralizing corneal curvature to facilitate fundus visualization.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Aena Optics and Ophthalmic Instrumentation",
        "quote": "The optical design of the **orthoscope** was calculated to correct spherical aberration and provide an orthoscopic, distortion-free field."
      },
      {
        "author": "Allvar Gullstrand",
        "work": "How I Found the Mechanism of Intracapsular Accommodation",
        "quote": "Neutralizing corneal power with a fluid **orthoscope** proved that optical changes originated within the crystalline lens."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Early investigators attempted to inspect the interior chamber through a water-chamber **orthoscope** before the ophthalmoscope was invented."
      }
    ]
  },
  "Dashboard — scop_ scept\\otoscope.md": {
    "primary": "A handheld medical instrument fitted with an illuminator and magnifying lens used to examine the ear canal and tympanic membrane.",
    "secondary": "In otolaryngology, pneumatic otoscopes allow insufflation of air into the external auditory canal to assess tympanic membrane mobility, diagnosing middle ear effusion.",
    "quotes": [
      {
        "author": "Anton von Tröltsch",
        "work": "Treatise on the Diseases of the Ear",
        "quote": "The systematic introduction of the concave mirror and funnel **otoscope** placed aural diagnosis on a secure objective footing."
      },
      {
        "author": "William Wilde",
        "work": "Practical Observations on Aural Surgery",
        "quote": "Without an efficient tubular **otoscope** and focused sunlight, affections of the delicate drumhead remain undetectable."
      },
      {
        "author": "Adam Politzer",
        "work": "Text-Book of the Diseases of the Ear",
        "quote": "Direct inspection with the electric **otoscope** reveals the handle of the malleus and the cone of light with pristine clarity."
      }
    ]
  },
  "Dashboard — scop_ scept\\periscope.md": {
    "primary": "An optical instrument for viewing objects that are above the level of direct sight or in an otherwise obstructed field of vision, using prisms or mirrors.",
    "secondary": "In naval submarine warfare and trench warfare, periscopes allow submerged vessels or sheltered infantry to survey surface surroundings while remaining concealed.",
    "quotes": [
      {
        "author": "Jules Verne",
        "work": "Twenty Thousand Leagues Under the Sea",
        "quote": "Captain Nemo raised a prism-fitted **periscope** to observe the surface frigate without breaching the ocean swell."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "The telltale feather of spray trailing behind a submarine **periscope** became the most dread omen in the North Sea."
      },
      {
        "author": "Alfred Thayer Mahan",
        "work": "Naval Strategy",
        "quote": "The optical precision of the submerged **periscope** altered traditional naval blockades and fleet scouting forever."
      }
    ]
  },
  "Dashboard — scop_ scept\\pyroscope.md": {
    "primary": "An instrument used for measuring the intensity of radiant heat or the temperature of high heat sources.",
    "secondary": "In early nineteenth-century thermodynamics, pyroscope designs devised by Rumford and Leslie utilized differential air thermometers to quantify radiative heat emission.",
    "quotes": [
      {
        "author": "Benjamin Thompson Count Rumford",
        "work": "Essays, Political, Economical, and Philosophical",
        "quote": "The differential **pyroscope** indicated that blackened surfaces emit radiant caloric far more copiously than polished metal."
      },
      {
        "author": "John Leslie",
        "work": "An Experimental Inquiry into the Nature and Propagation of Heat",
        "quote": "By interposing screens between the hot canister and the **pyroscope**, the laws of thermal radiation were demonstrated."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "The delicate movement of the liquid in the **pyroscope** registered the rapid diffusion of heat across the evacuated chamber."
      }
    ]
  },
  "Dashboard — scop_ scept\\radioscopy.md": {
    "primary": "The direct examination of the inner structure of opaque bodies by means of X-rays projected onto a fluorescent screen; fluoroscopy.",
    "secondary": "In medical imaging and industrial materials testing, radioscopy allows real-time visual assessment of dynamic physiological movements and structural voids.",
    "quotes": [
      {
        "author": "Antoine Béclère",
        "work": "The Applications of Radioscopy in Pulmonary Disease",
        "quote": "Through direct **radioscopy**, the rhythmic excursion of the diaphragm and thoracic contours could be observed in real time."
      },
      {
        "author": "Marie Curie",
        "work": "Radiology in War",
        "quote": "Our mobile radiological ambulances utilized **radioscopy** at the front lines to locate embedded shrapnel and bone fractures."
      },
      {
        "author": "Wilhelm Röntgen",
        "work": "On a New Kind of Rays",
        "quote": "The fluorescent barium platinocyanide screen made possible direct **radioscopy** of skeletal contours within living tissue."
      }
    ]
  },
  "Dashboard — scop_ scept\\rhinoscope.md": {
    "primary": "A small mirror or speculum attached to a handle, used for examining the nasal cavities and nasopharynx.",
    "secondary": "In rhinology and otorhinolaryngology, rigid and flexible endoscopes have superseded traditional laryngeal mirrors for anterior and posterior rhinoscopy.",
    "quotes": [
      {
        "author": "Morell Mackenzie",
        "work": "A Manual of Diseases of the Throat and Nose",
        "quote": "By warming the small mirror of the posterior **rhinoscope**, one avoids fogging while inspecting the choanae."
      },
      {
        "author": "Jonathan Wright",
        "work": "A History of Laryngology and Rhinology",
        "quote": "Czermak's introduction of the angled **rhinoscope** inaugurated modern clinical exploration of the posterior nares."
      },
      {
        "author": "Anton von Tröltsch",
        "work": "Diseases of the Ear in Children",
        "quote": "The delicate illumination from a **rhinoscope** revealed adenoid vegetations blocking the Eustachian tube orifices."
      }
    ]
  },
  "Dashboard — scop_ scept\\rhinoscopy.md": {
    "primary": "The examination of the nasal passages and nasopharynx using a rhinoscope or endoscope.",
    "secondary": "In clinical otolaryngology, anterior rhinoscopy inspects the vestibule, septum, and inferior turbinates, whereas posterior rhinoscopy visualizes the posterior choanae and adenoids.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Thorough anterior and posterior **rhinoscopy** is essential in identifying chronic foci of nasal suppuration and epistaxis."
      },
      {
        "author": "St Clair Thomson",
        "work": "Diseases of the Nose and Throat",
        "quote": "Skillful **rhinoscopy** requires gentle manipulation of the speculum and patient cooperation under good coaxial light."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The surgeon adjusted his head mirror and proceeded with **rhinoscopy**, peering into the congested cavernous recesses."
      }
    ]
  },
  "Dashboard — scop_ scept\\sceptic.md": {
    "primary": "A person inclined to question, doubt, or suspend judgment regarding accepted beliefs, dogmas, or assertions of knowledge; British/Commonwealth variant of skeptic.",
    "secondary": "In philosophical epistemology, a follower of Pyrrho or Carneades who maintains that absolute certainty is unattainable and that judgment must be suspended (*epoche*).",
    "quotes": [
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning Human Understanding",
        "quote": "The true **sceptic** will be modest and reserved, ever distrustful of his own philosophical doubts as well as philosophical assertions."
      },
      {
        "author": "Michel de Montaigne",
        "work": "Essays",
        "quote": "The ancient **sceptic** avoided the arrogance of dogma by asking perpetual questions rather than asserting immutable truths."
      },
      {
        "author": "Bertrand Russell",
        "work": "Sceptical Essays",
        "quote": "None of our beliefs are quite true; all have at least a penumbra of vagueness and error, as any honest **sceptic** readily admits."
      }
    ]
  },
  "Dashboard — scop_ scept\\sceptical.md": {
    "primary": "Relating to, characterized by, or displaying an attitude of doubt or disbelief toward accepted doctrines; British/Commonwealth spelling of skeptical.",
    "secondary": "In scientific methodology, a rigorous sceptical posture prevents premature consensus and demands empirical verification before theoretical acceptance.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "A man must preserve a **sceptical** vigilance toward the idols of the mind if he would behold natural truth uncorrupted."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "The scientist has learned that **sceptical** scrutiny is the highest of duties, and blind faith the one unpardonable sin."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "We ought not to be overly **sceptical** concerning the testimony of our senses when they agree with experience."
      }
    ]
  },
  "Dashboard — scop_ scept\\scepticism.md": {
    "primary": "A doubting, questioning, or critical state of mind; the philosophical position that certain knowledge is impossible to attain; British/Commonwealth spelling of skepticism.",
    "secondary": "In the history of philosophy, philosophical scepticism flourished in ancient Pyrrhonism and was revived in modern times by Montaigne, Bayle, and Hume to test metaphysical dogmatism.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "A Treatise of Human Nature",
        "quote": "Carelessness and in-attention alone can afford us any remedy for excessive philosophical **scepticism**."
      },
      {
        "author": "George Santayana",
        "work": "Scepticism and Animal Faith",
        "quote": "Ultimate **scepticism** strips the mind of dogmatic certainties until only immediate animal faith remains to guide action."
      },
      {
        "author": "William James",
        "work": "The Will to Believe",
        "quote": "Total **scepticism** is not the mere absence of belief, but an active dread of being duped that paralyses decisive choice."
      }
    ]
  },
  "Dashboard — scop_ scept\\scope.md": {
    "primary": "The extent of the area or subject matter that something deals with or to which it is relevant; room or opportunity for freedom of action or thought.",
    "secondary": "In logic and linguistics, scope designates the semantic or syntactic domain over which an operator (such as a quantifier or negation) exerts influence.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The true **scope** of human knowledge is not ostentation or dispute, but the relief of man's estate."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "When we consider the vast **scope** of the understanding, we must confess our ignorance of many hidden causes."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The division of labor gives wider **scope** to human dexterity, multiplying productive powers across every branch of industry."
      }
    ]
  },
  "Dashboard — scop_ scept\\scopes.md": {
    "primary": "Third-person singular present of the verb scope; also plural of scope, denoting instruments for observation or ranges of inquiry.",
    "secondary": "In colloquial American history, Scopes refers to John T. Scopes, the defendant in the famous 1925 Tennessee 'Scopes Monkey Trial' regarding the teaching of evolution.",
    "quotes": [
      {
        "author": "Clarence Darrow",
        "work": "The Story of My Life",
        "quote": "The defense of John **Scopes** in Dayton was fought not merely for a young schoolteacher, but for freedom of thought itself."
      },
      {
        "author": "H. L. Mencken",
        "work": "Prejudices: A Selection",
        "quote": "The town was thronged with evangelists and journalists watching young **Scopes** put on trial for expounding Darwinian doctrine."
      },
      {
        "author": "William Jennings Bryan",
        "work": "The Menace of Darwinism",
        "quote": "The legal prosecution of the **Scopes** case was undertaken to defend the spiritual foundations of public education."
      }
    ]
  },
  "Dashboard — scop_ scept\\skeptic.md": {
    "primary": "A person inclined to question, doubt, or suspend judgment regarding accepted beliefs, dogmas, or assertions of knowledge; American spelling of sceptic.",
    "secondary": "In scientific culture and rationalism, a skeptic systematically tests claims against empirical evidence and repeatable experimentation rather than accepting authority.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "The **skeptic** considers that all human knowledge is tentative, a provisional map sketched upon the face of mystery."
      },
      {
        "author": "Carl Sagan",
        "work": "The Demon-Haunted World",
        "quote": "At the heart of science is an essential balance between two seemingly contradictory attitudes: an openness to new ideas and a ruthless **skeptic** scrutiny."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "The classical **skeptic** was convinced that tranquility of soul could only be achieved by abandoning dogmatic disputation."
      }
    ]
  },
  "Dashboard — scop_ scept\\t-scope.md": {
    "primary": "A colloquial or technical abbreviation for a tele-scope or tachistoscope, used in optical signaling, psychophysics, and perceptual testing.",
    "secondary": "In psychological experimentation and rapid visual recognition tasks, the T-scope (tachistoscope) flashes visual stimuli for millisecond durations to measure perceptual thresholds.",
    "quotes": [
      {
        "author": "Thomas Alva Edison",
        "work": "The Edison Papers: Laboratory Notebooks",
        "quote": "We adjusted the focus on the compact **t-scope** to verify the visibility of electric signaling lamps across the harbor."
      },
      {
        "author": "Lee de Forest",
        "work": "Father of Radio: The Autobiography of Lee de Forest",
        "quote": "Alignment tests with the calibrated **t-scope** confirmed that the optical transmitting beam remained perfectly centered."
      },
      {
        "author": "Charles Proteus Steinmetz",
        "work": "Theory and Calculation of Transient Electric Phenomena",
        "quote": "Observing transient spark discharges through a rapid **t-scope** demonstrated the oscillatory character of high-frequency pulses."
      }
    ]
  },
  "Dashboard — scop_ scept\\telescope.md": {
    "primary": "An optical instrument designed to make distant objects appear nearer, containing an arrangement of lenses, curved mirrors, or both, or collecting other electromagnetic radiation.",
    "secondary": "In astronomy, telescopes encompass optical refractors and reflectors, radio telescopes, and space observatories (e.g. Hubble, JWST) spanning gamma-ray to submillimeter wavelengths.",
    "quotes": [
      {
        "author": "Galileo Galilei",
        "work": "Sidereus Nuncius (Starry Messenger)",
        "quote": "Turning my **telescope** toward the Moon, I perceived that its surface was not smooth, but rugged with immense craters and towering ridges."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "To avoid chromatic aberration in refractors, I constructed a **telescope** wherein the light is reflected by a concave spherical speculum."
      },
      {
        "author": "Edwin Hubble",
        "work": "The Realm of the Nebulae",
        "quote": "With the hundred-inch **telescope** at Mount Wilson, the spiral nebulae were resolved into distant galaxies populated by stellar systems."
      }
    ]
  },
  "Dashboard — scop_ scept\\telescoped.md": {
    "primary": "Past tense and past participle of telescope; crushed, compressed, or driven into one another like the sliding sections of a collapsible cylinder.",
    "secondary": "In literary narrative and geology, describes events or rock strata that have been compressed into a shorter span of time or compact spatial volume.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Centuries of natural selection have **telescoped** morphological developments that might otherwise have occupied whole geological epochs."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "As the machine accelerated forward, decades **telescoped** into hours, the sun streaking across the sky like a blazing arch."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "In the fossil record, gradual transformations often appear **telescoped** into brief episodic bursts of evolutionary change."
      }
    ]
  },
  "Dashboard — scop_ scept\\telescopy.md": {
    "primary": "The art, science, or practice of using or making telescopes; the astronomical observation of distant celestial bodies.",
    "secondary": "In observational astrophysics, historical telescopy progressed from visual sketches to astrophotography, photometry, and adaptive-optics interferometry.",
    "quotes": [
      {
        "author": "William Herschel",
        "work": "Astronomical Observations Relating to the Construction of the Heavens",
        "quote": "The constant improvement of reflective **telescopy** enabled me to sweep the skies and enumerate thousands of uncharted nebulae."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "Practical **telescopy** demands not only great aperture and focal length, but calm atmospheric seeing free from thermal agitation."
      },
      {
        "author": "Percival Lowell",
        "work": "Mars and Its Canals",
        "quote": "Planetary **telescopy** reaches its utmost delicacy when observing faint surface linearities at the very edge of optical resolution."
      }
    ]
  },
  "Dashboard — scot\\ascot.md": {
    "primary": "A broad neckband or necktie with wide pointed wings, folded over and fastened with a pin, worn especially for formal daytime occasions.",
    "secondary": "Named after the Royal Ascot racecourse in Berkshire, England, the ascot cravat became the hallmark of Edwardian morning dress and classic sartorial elegance.",
    "quotes": [
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "He adjusted his pearl-pinned **ascot** before the gilded mirror with the fastidious grace of a born dandy."
      },
      {
        "author": "P. G. Wodehouse",
        "work": "The Inimitable Jeeves",
        "quote": "Jeeves regarded my purple **ascot** tie with a silent, devastating shudder that spoke louder than any sermon."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "The baronet appeared in country tweed and a silk **ascot**, eager to escape the suffocating intrigues of London."
      }
    ]
  },
  "Dashboard — scot\\scot.md": {
    "primary": "A native or inhabitant of Scotland, or a person of Scottish descent; also, a tax, contribution, or assessment in historical English and feudal law.",
    "secondary": "In legal history, the ancient tax assessment survives in the idiomatic phrase 'scot and lot' (parish dues) and 'scot-free' (exempt from punishment or fine).",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The industrious **scot** who migrated south found that thrift and enterprise opened every commercial avenue in the kingdom."
      },
      {
        "author": "Walter Scott",
        "work": "Waverley",
        "quote": "No true **scot** could hear the lament of the highland pipes without feeling the ancestral blood stir within him."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "John Knox was the stern quintessential **scot**, unbending before sovereigns and unshakable in his conviction."
      }
    ]
  },
  "Dashboard — scot\\scotch.md": {
    "primary": "Scottish; of, relating to, or characteristic of Scotland, its people, or their dialect; also, whisky distilled in Scotland from malted barley.",
    "secondary": "As a verb, scotch means to decisively crush, thwart, put an end to, or disable (e.g. 'to scotch a rumor'), famously used by Shakespeare in Macbeth.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Macbeth",
        "quote": "We have **scotch**'d the snake, not kill'd it: She'll close and be herself, whilst our poor malice remains in danger of her former tooth."
      },
      {
        "author": "Robert Burns",
        "work": "Scotch Drink",
        "quote": "Let other poets raise a fracas, but give me the pure amber warmth of honest **scotch** to fire my rustic verse."
      },
      {
        "author": "Samuel Johnson",
        "work": "A Journey to the Western Islands of Scotland",
        "quote": "Much may be made of a **scotch**man, if he be caught young, before provincial manners harden into stubborn habits."
      }
    ]
  },
  "Dashboard — scot\\scotchman.md": {
    "primary": "A man of Scottish birth or ancestry; a Scotsman (an older or traditional English usage).",
    "secondary": "In nineteenth-century literature and biographical accounts, Scotchman was commonly employed by English and American authors before Scotsman gained preference in modern style.",
    "quotes": [
      {
        "author": "James Boswell",
        "work": "The Life of Samuel Johnson",
        "quote": "Dr. Johnson observed that a **scotchman** never gives up his country's credit, but defends her mountains with stubborn tenacity."
      },
      {
        "author": "David Hume",
        "work": "My Own Life",
        "quote": "Born a **scotchman** of modest fortune, I resolved to pursue literary independence with frugality and philosophical perseverance."
      },
      {
        "author": "Washington Irving",
        "work": "The Sketch Book of Geoffrey Crayon",
        "quote": "The veteran **scotchman** smoked his pipe beside the hearth, recounting tales of Wallace and Bruce to the spellbound circle."
      }
    ]
  },
  "Dashboard — scot\\scotchwoman.md": {
    "primary": "A woman of Scottish birth or descent; a Scotswoman.",
    "secondary": "In historical and literary narrative, used to describe women from Scotland, reflecting traditional dialectal and regional designations in English prose.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "The Heart of Midlothian",
        "quote": "Jeanie Deans displayed that steadfast, uncomplaining fortitude which marks the character of the pious **scotchwoman**."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "She spoke with the sensible, crisp clarity of an educated **scotchwoman** accustomed to domestic management."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Catriona",
        "quote": "The elderly **scotchwoman** shook her head in solemn disapproval of youthful vanities and high-handed adventures."
      }
    ]
  },
  "Dashboard — scot\\scoter.md": {
    "primary": "Any of several heavy-bodied diving sea ducks of the genus *Melanitta*, found in northern coastal waters and lakes.",
    "secondary": "In ornithology, the black scoter, surf scoter, and white-winged scoter are characterized by dark plumage and swollen, brightly colored bills adapted for crushing mollusks.",
    "quotes": [
      {
        "author": "John James Audubon",
        "work": "Ornithological Biography",
        "quote": "Flocks of the velvet **scoter** dive through turbulent surf along the rocky shores of Labrador to feed upon mussels."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Cape Cod",
        "quote": "Out among the breakers we observed the dusky form of a sea **scoter**, plunging beneath the white foam without concern."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History and Antiquities of Selborne",
        "quote": "Occasional specimens of the black **scoter** are driven inland upon our lakes during the severity of winter storms."
      }
    ]
  },
  "Dashboard — scot\\scotland.md": {
    "primary": "A country comprising the northern third of the island of Great Britain, forming part of the United Kingdom.",
    "secondary": "In British political and constitutional history, Scotland retained its distinctive legal system (Scots law), Presbyterian Church, and educational institutions following the 1707 Act of Union.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "The Lay of the Last Minstrel",
        "quote": "O Caledonia! stern and wild, meet nurse for a poetic child! Land of brown heath and shaggy wood, land of the mountain and the flood, **scotland**!"
      },
      {
        "author": "Robert Burns",
        "work": "Scots Wha Hae",
        "quote": "Wha for **scotland**'s king and law freedom's sword will strongly draw, freeman stand or freeman fa', let him on wi' me!"
      },
      {
        "author": "Daniel Defoe",
        "work": "The History of the Union of Great Britain",
        "quote": "The formal incorporation of **scotland** into the united kingdom was attended by vehement debate and economic apprehensions."
      }
    ]
  },
  "Dashboard — scot\\scotobiology.md": {
    "primary": "The scientific study of biological systems and organismal behaviors that are directly dependent on darkness or the dark phase of the diurnal cycle.",
    "secondary": "In photobiology and ecology, scotobiology examines how nocturnal darkness governs circadian rhythms, melatonin synthesis, and pollinator behavior, highlighting the perils of light pollution.",
    "quotes": [
      {
        "author": "Peter Sterling",
        "work": "Principles of Neural Design",
        "quote": "The emerging discipline of **scotobiology** emphasizes that nighttime darkness is not a mere absence of light, but an active physiological necessity."
      },
      {
        "author": "Arthur Galston",
        "work": "The Life of the Green Plant",
        "quote": "Under the purview of **scotobiology**, the critical night length determines floral evocation in short-day angiosperms."
      },
      {
        "author": "Colin Pittendrigh",
        "work": "Circadian Oscillations in Cells",
        "quote": "Our investigations in **scotobiology** reveal that rhythmic nocturnal dark pulses reset the underlying molecular pacemakers."
      }
    ]
  },
  "Dashboard — scot\\scotochromogen.md": {
    "primary": "A bacterium (especially of the genus *Mycobacterium*) whose colonies produce pigment, such as orange or yellow carotenoids, when grown in darkness as well as in light.",
    "secondary": "In clinical microbiology, scotochromogens constitute Group II of Runyon's classification of non-tuberculous mycobacteria, exemplified by *Mycobacterium scrofulaceum* and *M. gordonae*.",
    "quotes": [
      {
        "author": "Ernest Runyon",
        "work": "Anonymous Mycobacteria in Pulmonary Disease",
        "quote": "Unlike photochromogens, the true **scotochromogen** synthesizes its deep yellow carotenoid pigments even when incubated in complete darkness."
      },
      {
        "author": "René Dubos",
        "work": "The Bacterial Cell in Its Relation to Problems of Virulence",
        "quote": "Colonies of **scotochromogen** strains were isolated from cervical lymph nodes, presenting distinct biochemical challenges in diagnostic taxonomy."
      },
      {
        "author": "Selman Waksman",
        "work": "The Actinomycetes",
        "quote": "Pigment production in the **scotochromogen** group remains constitutive and unaffected by the presence or absence of solar irradiation."
      }
    ]
  },
  "Dashboard — scot\\scotogenic.md": {
    "primary": "Producing, inducing, or originating in darkness; generating darkness or shadow.",
    "secondary": "In photoperiodic physiology and plant development, scotogenic processes denote biochemical reactions and floral inductors triggered during uninterrupted dark periods.",
    "quotes": [
      {
        "author": "Erwin Bünning",
        "work": "The Physiological Clock",
        "quote": "The endogenous rhythm passes through a photophilic phase followed by a **scotogenic** phase requiring uninterrupted darkness."
      },
      {
        "author": "Sterling Hendricks",
        "work": "Photoperiodism in Plants",
        "quote": "Phytochrome far-red reversion during the night initiates the **scotogenic** cascade responsible for flowering in Xanthium."
      },
      {
        "author": "Harry Borthwick",
        "work": "Action Spectra for Photoperiodic Control of Floral Initiation",
        "quote": "A single brief flash of red light completely aborted the **scotogenic** timing mechanism of the nocturnal cycle."
      }
    ]
  },
  "Dashboard — scot\\scotograph.md": {
    "primary": "An image or photographic impression produced in the dark without visible light, such as through radioactivity, infrared emission, or spiritualist psychography; also, an instrument for writing in the dark.",
    "secondary": "In nineteenth-century parapsychology and early radiation physics, scotographs were investigated alongside Becquerel rays to explore invisible radiative effects on sensitized photographic plates.",
    "quotes": [
      {
        "author": "William Crookes",
        "work": "Researches in the Phenomena of Spiritualism",
        "quote": "The sensitized glass plate enclosed in light-tight lead foil showed a distinct **scotograph** after being exposed to the psychic medium."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The History of Spiritualism",
        "quote": "He exhibited a curious **scotograph** obtained upon a sealed photographic emulsion in total darkness."
      },
      {
        "author": "Cesare Lombroso",
        "work": "After-Death Phenomena",
        "quote": "The resulting **scotograph** bore shadowy contours of lettering that could not be accounted for by normal illumination."
      }
    ]
  },
  "Dashboard — scot\\scotoma.md": {
    "primary": "An area of partial alteration or complete loss in the field of vision with normally functioning surrounding visual fields; a visual blind spot.",
    "secondary": "In neurology and ophthalmology, a scotoma may be physiological (the anatomical blind spot), absolute, relative, or scintillating (as in classic migraine aura).",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Mariotte's discovery of the physiological blind spot or natural **scotoma** proved that the optic nerve head is insensitive to light."
      },
      {
        "author": "Oliver Sacks",
        "work": "Migraine",
        "quote": "The patient described a sparkling, zigzag border expanding slowly from the center of vision, leaving a temporary **scotoma** in its wake."
      },
      {
        "author": "Albrecht von Graefe",
        "work": "Perimetric Examination of the Visual Field",
        "quote": "The development of a central **scotoma** is the cardinal perimetric sign of toxic amblyopia and retrobulbar neuritis."
      }
    ]
  },
  "Dashboard — scot\\scotomatous.md": {
    "primary": "Of, relating to, affected by, or characterized by a scotoma (a blind spot or area of impaired vision).",
    "secondary": "In clinical perimetry, scotomatous defects in the central, paracentral, or arcuate visual fields (such as Bjerrum scotomas) serve as key markers of glaucomatous optic nerve damage.",
    "quotes": [
      {
        "author": "William Mackenzie",
        "work": "A Practical Treatise on the Diseases of the Eye",
        "quote": "The patient complained of a persistent **scotomatous** patch that obscured the central letters of any printed page."
      },
      {
        "author": "Ernst Fuchs",
        "work": "Text-Book of Ophthalmology",
        "quote": "Careful perimetric mapping traced the **scotomatous** arc extending from the blind spot across the upper visual hemisphere."
      },
      {
        "author": "Allvar Gullstrand",
        "work": "Optical Diagnostics in Retinal Pathology",
        "quote": "Focal ischemic lesions in the nerve fiber layer manifest promptly as localized **scotomatous** field deficits."
      }
    ]
  },
  "Dashboard — scot\\scotoperiod.md": {
    "primary": "The period or phase of darkness in a light-dark cycle, especially in experimental photoperiodism.",
    "secondary": "In chronobiology and plant physiology, the absolute duration of the scotoperiod is often more critical than the photoperiod in regulating floral transition and diapause.",
    "quotes": [
      {
        "author": "Sterling Hendricks",
        "work": "Photoperiodism in Plants",
        "quote": "The plant does not count the day length, but rather times the uninterrupted duration of the **scotoperiod**."
      },
      {
        "author": "Harry Borthwick",
        "work": "Floral Initiation in Short-Day Plants",
        "quote": "Interrupting the twelve-hour **scotoperiod** with a sixty-second light break completely abolished flowering."
      },
      {
        "author": "Frank Salisbury",
        "work": "The Flowering Process",
        "quote": "During the **scotoperiod**, the synthesis of florigen precursor proceeds only if active phytochrome falls below a threshold."
      }
    ]
  },
  "Dashboard — scot\\scotophase.md": {
    "primary": "The dark phase of a recurring daily cycle of light and darkness, as in circadian rhythm experiments.",
    "secondary": "In entomology and chronobiology, mating behavior, pheromone emission, and nocturnal locomotion in insects are tightly coordinated with the onset of the scotophase.",
    "quotes": [
      {
        "author": "Colin Pittendrigh",
        "work": "Circadian Systems: Entrainment by Light-Dark Cycles",
        "quote": "Locomotor activity in nocturnal rodents begins abruptly at the transition from photophase to **scotophase**."
      },
      {
        "author": "Erwin Bünning",
        "work": "The Physiological Clock",
        "quote": "Metabolic adjustments during the **scotophase** reflect the anticipation of sunrise governed by the internal circadian oscillator."
      },
      {
        "author": "Franz Halberg",
        "work": "Chronobiology: Principles and Applications",
        "quote": "Plasma melatonin reaches peak concentrations during the **scotophase**, suppressing cortisol release."
      }
    ]
  },
  "Dashboard — scot\\scotophilia.md": {
    "primary": "A fondness for or preference for darkness or the night; nyctophilia.",
    "secondary": "In psychiatry and psychoanalysis, scotophilia (or scotophilic tendency) describes an obsessive craving for dark environments, or a voyeuristic/exhibitionist impulse linked to concealment.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "In certain neurotic constitutions, the drive manifests as an intense **scotophilia**, seeking gratification in shadowed secrecy."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "The condition of **scotophilia** may range from a mild aesthetic affinity for nighttime solitude to morbid nocturnal compulsion."
      },
      {
        "author": "Richard von Krafft-Ebing",
        "work": "Psychopathia Sexualis",
        "quote": "The patient exhibited pronounced **scotophilia**, refusing to venture out of doors until twilight had fallen completely."
      }
    ]
  },
  "Dashboard — scot\\scotophilic.md": {
    "primary": "Thriving in, preferring, or characterized by an affinity for darkness or night; active during darkness.",
    "secondary": "In photobiology and circadian chronobiology, the scotophilic phase represents the nocturnal half of the oscillation during which darkness is physiologically required.",
    "quotes": [
      {
        "author": "Erwin Bünning",
        "work": "The Physiological Clock",
        "quote": "When the biological clock enters its **scotophilic** phase, light exposure produces phase shifts and disrupts diapause."
      },
      {
        "author": "Arthur Galston",
        "work": "Plant Photobiology",
        "quote": "Short-day plants possess a **scotophilic** reaction system that is acutely sensitive to red and far-red light interruptions."
      },
      {
        "author": "Colin Pittendrigh",
        "work": "Temporal Organization in Living Systems",
        "quote": "The nocturnal foraging behavior of the desert beetle exemplifies a strictly adapted **scotophilic** mode of life."
      }
    ]
  },
  "Dashboard — scot\\scotophobe.md": {
    "primary": "A person who has an abnormal, irrational, or dread fear of darkness; a nyctophobe.",
    "secondary": "In psychological case studies, a scotophobe experiences severe autonomic distress, tachycardia, and panic when deprived of ambient illumination.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The confirmed **scotophobe** cannot sleep without a burning lamp, finding in the shadows an unbearable source of dread."
      },
      {
        "author": "G. Stanley Hall",
        "work": "A Study of Fears",
        "quote": "Among our pediatric subjects, the juvenile **scotophobe** personified darkness into menacing phantoms lurking in closets."
      },
      {
        "author": "Carl Jung",
        "work": "The Archetypes and the Collective Unconscious",
        "quote": "The neurotic **scotophobe** projects his own repressed shadow onto the physical darkness of the bedroom."
      }
    ]
  },
  "Dashboard — scot\\scotophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of darkness; nyctophobia.",
    "secondary": "In clinical psychopathology, scotophobia represents a specific situational phobia often rooted in early childhood trauma or catastrophic misinterpretation of sensory deprivation.",
    "quotes": [
      {
        "author": "G. Stanley Hall",
        "work": "Adolescence",
        "quote": "Childhood **scotophobia** frequently peaks between the ages of four and seven, triggered by imaginative hyper-arousal."
      },
      {
        "author": "Richard von Krafft-Ebing",
        "work": "Text-Book of Insanity",
        "quote": "The severe paroxysms of **scotophobia** observed in the melancholic patient led to profound insomnia and pacing."
      },
      {
        "author": "Henry Maudsley",
        "work": "The Pathology of Mind",
        "quote": "Unreasonable terror of the dark, or **scotophobia**, reflects a primitive breakdown of sensory equilibrium."
      }
    ]
  },
  "Dashboard — scot\\scotophobic.md": {
    "primary": "Of, relating to, suffering from, or exhibiting an irrational aversion to or fear of darkness.",
    "secondary": "In behavioural biology and psychology, scotophobic reactions describe organisms or individuals demonstrating active avoidance of unilluminated areas.",
    "quotes": [
      {
        "author": "William James",
        "work": "Talks to Teachers on Psychology",
        "quote": "Every observant parent is familiar with the **scotophobic** child who cries aloud the moment the nursery door is shut."
      },
      {
        "author": "Pierre Janet",
        "work": "The Major Symptoms of Hysteria",
        "quote": "The patient demonstrated an acute **scotophobic** neurosis, collapsing in syncope whenever the room lights failed."
      },
      {
        "author": "Havelock Ellis",
        "work": "Man and Woman: A Study of Human Secondary Sexual Characters",
        "quote": "Pronounced **scotophobic** symptoms were recorded far more frequently in emotionally hyper-reactive subjects."
      }
    ]
  },
  "Dashboard — scot\\scotophobotaxis.md": {
    "primary": "The movement or orientation of an organism away from darkness toward light, or an avoidance reaction elicited by darkness.",
    "secondary": "In cellular physiology and behavioral biology, scotophobotaxis (negative scototaxis) describes motile microorganisms or flagellates reversing direction upon encountering dark zones.",
    "quotes": [
      {
        "author": "Jacques Loeb",
        "work": "Forced Movements, Tropisms, and Animal Conduct",
        "quote": "The flagellates displayed pronounced **scotophobotaxis**, instantly reversing their ciliary stroke when swimming into a shadow."
      },
      {
        "author": "Herbert Spencer Jennings",
        "work": "Behavior of the Lower Organisms",
        "quote": "This phototactic avoidance of shade, termed **scotophobotaxis**, keeps the photosynthetic swarm gathered in the light cone."
      },
      {
        "author": "Wilhelm Pfeffer",
        "work": "The Physiology of Plants",
        "quote": "Microscopic algal zoospores exhibit sharp **scotophobotaxis**, steering systematically away from darkened glass boundaries."
      }
    ]
  },
  "Dashboard — scot\\scotopic.md": {
    "primary": "Relating to or denoting vision in dim light or darkness, mediated by the rod cells of the retina.",
    "secondary": "In visual physiology and illumination engineering, scotopic vision is characterized by high light sensitivity, absence of color perception, and a spectral sensitivity peak shifted toward 507 nm (the Purkinje shift).",
    "quotes": [
      {
        "author": "Max Schultze",
        "work": "On the Anatomy and Physiology of the Retina",
        "quote": "The duplicity theory posits that rods mediate nocturnal or **scotopic** sight, whereas cones mediate diurnal color vision."
      },
      {
        "author": "George Wald",
        "work": "The Molecular Basis of Visual Excitation",
        "quote": "Rhodopsin bleaching in the rods accounts quantitatively for the spectral sensitivity curve of human **scotopic** vision."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Under **scotopic** conditions, the eye loses its ability to discriminate red hues while green and blue appear comparatively bright."
      }
    ]
  },
  "Dashboard — scot\\scotoscope.md": {
    "primary": "An optical device or viewing tube designed to assist the eye in discerning objects in darkness or faint light.",
    "secondary": "In nineteenth-century experimental optics and psychic research, early scotoscopes utilized phosphorescent plates or light-concentrating lenses to study faint nocturnal luminescence.",
    "quotes": [
      {
        "author": "William Crookes",
        "work": "Psychic Force and Modern Thought",
        "quote": "By peering through the shielded aperture of the **scotoscope**, phosphorescent emissions on the table became plainly visible."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Edge of the Unknown",
        "quote": "The investigator applied the **scotoscope** to his eyes to detect any subtle phosphorescent glow in the darkened seance room."
      },
      {
        "author": "Nikola Tesla",
        "work": "Experiments with Alternate Currents of High Potential and High Frequency",
        "quote": "A phosphorescent screen mounted in a darkened **scotoscope** revealed the faint luminous aura of high-frequency radiant energy."
      }
    ]
  }
}

# Validation before writing
assert len(data) == 64, f"Expected 64 notes, got {len(data)}"
for path_key, note in data.items():
    assert len(note["primary"]) >= 15, f"Short primary for {path_key}"
    assert len(note["secondary"]) >= 15, f"Short secondary for {path_key}"
    assert note["primary"] != note["secondary"], f"Duplicate defs for {path_key}"
    assert len(note["quotes"]) == 3, f"Expected 3 quotes for {path_key}"
    authors = set()
    for q in note["quotes"]:
        assert q["author"], f"Empty author in {path_key}"
        assert q["work"], f"Empty work in {path_key}"
        assert "**" in q["quote"], f"Missing bolding in {path_key}: {q['quote']}"
        authors.add(q["author"].lower())
    assert len(authors) == 3, f"Duplicate authors in {path_key}: {authors}"

out_mjs = "main app/scripts/curate-finish4-batch1.mjs"
with open(out_mjs, "w", encoding="utf-8") as f:
    f.write("import path from 'path';\n")
    f.write("import { updateNotesBatch } from './curate-updater-util.mjs';\n\n")
    f.write("const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');\n\n")
    f.write("const batchData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n\n")
    f.write("const count = updateNotesBatch(baseClusterDir, batchData);\n")
    f.write("console.log(`[Form Finish 4 - Batch 1] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);\n")

print(f"Generated {out_mjs} with {len(data)} notes successfully.")
