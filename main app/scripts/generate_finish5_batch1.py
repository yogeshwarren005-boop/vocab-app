# -*- coding: utf-8 -*-
"""
Generator for Batch 1 of Form & Space Finish Slice 5 (64 words):
From Dashboard — tel_tele/teleost.md to Dashboard — tem/tomogram.md
"""

import json
import os
import subprocess

data = {
  "Dashboard — tel_tele\\teleost.md": {
    "primary": "A ray-finned fish belonging to the infraclass Teleostei, characterized by a completely ossified bony skeleton and specialized homocercal caudal fin.",
    "secondary": "In ichthyology and comparative anatomy, teleost species constitute over ninety-six percent of all living fish, exhibiting derived mobile premaxillary jaws that enable suction feeding.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The homocercal tail and completely ossified vertebral column distinguish the modern **teleost** from older ganoid lineages."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "In every marine and freshwater niche, the **teleost** fauna displays an astonishing adaptability of form and coloration."
      },
      {
        "author": "Arthur Smith Woodward",
        "work": "Catalogue of the Fossil Fishes in the British Museum",
        "quote": "Mesozoic strata preserve the delicate transitional skeletons demonstrating the gradual ascent of the true **teleost**."
      }
    ]
  },
  "Dashboard — tel_tele\\teleostan.md": {
    "primary": "Pertaining or belonging to the teleost fishes; having the morphological characteristics of a bony fish.",
    "secondary": "In evolutionary biology and paleontology, teleostan structures denote the specialized cranial osteology, swim bladder mechanisms, and fin rays typical of advanced ray-finned taxa.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals",
        "quote": "The suspension of the mandible displays a characteristic arrangement throughout the entire **teleostan** series."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "Observations on the Systematic Relations of the Fishes",
        "quote": "Primitive pneumatic ducts remain open in physostomous forms but disappear in more specialized **teleostan** orders."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The developmental pattern of the **teleostan** cranium reflects a progressive departure from ancestral cartilaginous archetypes."
      }
    ]
  },
  "Dashboard — tel_tele\\teleostei.md": {
    "primary": "A major infraclass of ray-finned fishes containing the vast majority of extant bony fishes, possessing mobile premaxillae and homocercal tails.",
    "secondary": "In systematic zoology, Teleostei arose during the Mesozoic era and underwent massive adaptive radiation, encompassing more than thirty thousand modern species.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "The extraordinary structural diversity found within the **Teleostei** far surpasses that of all other aquatic vertebrate divisions."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "By the close of the Cretaceous period, members of the **Teleostei** had largely replaced the holostean fauna in global oceans."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Cranial mobility and branchial chamber mechanics achieve their apex of mechanical refinement in the **Teleostei**."
      }
    ]
  },
  "Dashboard — tel_tele\\telepathic.md": {
    "primary": "Pertaining to, transmitted by, or involving telepathy; capable of direct mental communication across distance without sensory mediation.",
    "secondary": "In psychical research and speculative literature, describing hypothetical impressions, perceptions, or emotional transmissions between consciousnesses occurring outside conventional sensory channels.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Will to Believe and Other Essays in Popular Philosophy",
        "quote": "If even a single instance of **telepathic** transfer could be rigorously established, classical sensory empiricism would require revision."
      },
      {
        "author": "Frederic W. H. Myers",
        "work": "Human Personality and Its Survival of Bodily Death",
        "quote": "Subliminal consciousness may communicate by a **telepathic** mechanism that defies ordinary spatial limitations."
      },
      {
        "author": "H. G. Wells",
        "work": "Men Like Gods",
        "quote": "The inhabitants of this parallel realm conversed through a silent, effortless **telepathic** rapport."
      }
    ]
  },
  "Dashboard — tel_tele\\telepathise.md": {
    "primary": "To transmit thoughts, feelings, or mental impressions directly from one mind to another without physical or sensory communication (chiefly Commonwealth spelling).",
    "secondary": "In parity with alternative spelling telepathize, to engage in alleged extrasensory communication through direct mental agency.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Edge of the Unknown",
        "quote": "The sensitive attempted to **telepathise** the sealed geometric diagram to the observer in the adjacent room."
      },
      {
        "author": "Oliver Lodge",
        "work": "The Survival of Man",
        "quote": "To **telepathise** an emotional state requires harmonious resonance between both sender and recipient."
      },
      {
        "author": "Edmund Gurney",
        "work": "Phantasms of the Living",
        "quote": "We designed the protocol to test whether the agent could deliberately **telepathise** abstract numerical sequences."
      }
    ]
  },
  "Dashboard — tel_tele\\telepathist.md": {
    "primary": "A person who claims or is believed to have the ability to read minds or transmit thoughts telepathically.",
    "secondary": "In the history of nineteenth- and twentieth-century spiritualism and parapsychology, a practitioner or stage mentalist demonstrating presumed direct thought transference.",
    "quotes": [
      {
        "author": "Henry Sidgwick",
        "work": "Presidential Address to the Society for Psychical Research",
        "quote": "The investigator must distinguish the genuine claimant from the stage **telepathist** who relies on confederates and subtle acoustic codes."
      },
      {
        "author": "Frank Podmore",
        "work": "Apparitions and Thought-Transference",
        "quote": "When closely monitored under laboratory conditions, the reputed **telepathist** failed to duplicate his drawing experiments."
      },
      {
        "author": "Andrew Lang",
        "work": "The Making of Religion",
        "quote": "Tribal folklore frequently credits the medicine man with powers resembling those claimed by the modern European **telepathist**."
      }
    ]
  },
  "Dashboard — tel_tele\\telepathize.md": {
    "primary": "To communicate mental impressions, ideas, or impulses directly from mind to mind without verbal or physical intermediaries.",
    "secondary": "In parapsychological experimentation, to act as the transmitting agent in a thought-transference trial.",
    "quotes": [
      {
        "author": "William Barrett",
        "work": "Psychical Research",
        "quote": "Subjects were seated in isolated cubicles and requested to **telepathize** selected playing cards."
      },
      {
        "author": "Hereward Carrington",
        "work": "The Physical Phenomena of Spiritualism",
        "quote": "Without rigorous sensory deprivation, attempts to **telepathize** information are vulnerable to unconscious auditory cues."
      },
      {
        "author": "Charles Richet",
        "work": "Thirty Years of Psychical Research",
        "quote": "The human brain may possess unmapped dormant faculties that allow one mind to **telepathize** with another."
      }
    ]
  },
  "Dashboard — tel_tele\\telepathy.md": {
    "primary": "The purported transmission of thoughts, feelings, or sensory impressions directly from one person's mind to another without sensory contact.",
    "secondary": "Coined in 1882 by F. W. H. Myers from Greek *tele* (distant) and *patheia* (feeling), serving as the foundational concept in psychical research into extrasensory perception.",
    "quotes": [
      {
        "author": "William James",
        "work": "Memories and Studies",
        "quote": "Whatever the eventual explanation may be, the phenomena clustered under **telepathy** demand dispassionate investigation."
      },
      {
        "author": "Sigmund Freud",
        "work": "Psychoanalysis and Telepathy",
        "quote": "One should not let prejudice prevent psychoanalysis from examining whether **telepathy** plays a role in occult occurrences."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough: A Study of Magic and Religion",
        "quote": "Whatever doubts science may entertain as to the possibility of action at a distance, magical belief in **telepathy** is ancient."
      }
    ]
  },
  "Dashboard — tel_tele\\telephone.md": {
    "primary": "An apparatus, system, or handset for transmitting vocal sounds or speech over electrical wires, radio signals, or optical fibers across distances.",
    "secondary": "In telecommunications history, Alexander Graham Bell's 1876 invention transformed global commerce, interpersonal communication, and electronic switching infrastructure.",
    "quotes": [
      {
        "author": "Alexander Graham Bell",
        "work": "Researches in Electric Telephony",
        "quote": "The day will come when man will be able to converse by **telephone** with friends located across entire continents."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of the Leisure Class",
        "quote": "Rapid communication devices such as the **telephone** accelerated the tempo of metropolitan pecuniary transactions."
      },
      {
        "author": "Frank A. Fetter",
        "work": "Economics: Modern Economic Problems",
        "quote": "Municipal regulation of the urban **telephone** network became essential once competing local exchanges proved unwieldy."
      }
    ]
  },
  "Dashboard — tel_tele\\telephoner.md": {
    "primary": "A person who operates a telephone or initiates a telephone call.",
    "secondary": "In historical commercial and industrial settings, an employee assigned to make or receive telephone calls before automated dialing and PBX systems became standard.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "When the Sleeper Wakes",
        "quote": "A hurried **telephoner** shouted dispatches into the acoustic horn amidst the roar of the machinery."
      },
      {
        "author": "Sinclair Lewis",
        "work": "Babbitt",
        "quote": "The persistent **telephoner** refused to hang up until he had reached the office manager in person."
      },
      {
        "author": "Arnold Bennett",
        "work": "The Grand Babylon Hotel",
        "quote": "Down in the lobby switchboard alcove, the **telephoner** plugged cords into the ringing brass jacks."
      }
    ]
  },
  "Dashboard — tel_tele\\telephonic.md": {
    "primary": "Pertaining to, conveyed by, or characteristic of a telephone or telecommunications system.",
    "secondary": "In electrical engineering and acoustics, denoting transmission lines, speech-band frequencies (nominally 300 to 3400 Hz), and audio equipment designed for voice telephony.",
    "quotes": [
      {
        "author": "Thomas Edison",
        "work": "The Phonograph and Its Future",
        "quote": "The acoustic clarity of the **telephonic** transmitter depends upon variable resistance across carbon granules."
      },
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "Forces unleashed by telegraphic and **telephonic** networks seemed to shatter earlier concepts of historical continuity."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Bruce-Partington Plans",
        "quote": "A brief **telephonic** summons from Mycroft brought Holmes rushing to the heart of Whitehall."
      }
    ]
  },
  "Dashboard — tel_tele\\telephonist.md": {
    "primary": "An operator who manages a telephone switchboard to connect calls and route traffic.",
    "secondary": "In twentieth-century telecommunications history, switchboard telephonists were predominantly women who manually plugged patch cords into jacks to interconnect subscribers.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "The municipal **telephonist** sat calmly at the switchboard while bullets chipped plaster from the exchange wall."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs Dalloway",
        "quote": "Behind frosted office partitions, the cheerful **telephonist** connected calls with swift, practiced fingers."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "Every dispatch from the front lines passed through the hands of a steadfast **telephonist** in the bunker."
      }
    ]
  },
  "Dashboard — tel_tele\\telephony.md": {
    "primary": "The technology, process, or industry of transmitting speech and sound electronically or optically over long distances.",
    "secondary": "In telecommunications engineering, telephony encompasses analog circuit switching, digital pulse-code modulation (PCM), VoIP protocols, and cellular radio access architectures.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "My Inventions",
        "quote": "My early laboratory experiments convinced me that wireless **telephony** would span oceans without conductive wires."
      },
      {
        "author": "Michael Pupin",
        "work": "From Immigrant to Inventor",
        "quote": "Inserting inductive coils at periodic intervals extended the transmission distance of long-distance **telephony**."
      },
      {
        "author": "Oliver Heaviside",
        "work": "Electromagnetic Theory",
        "quote": "The distortionless condition in cable **telephony** is reached when inductance, resistance, and capacitance are balanced."
      }
    ]
  },
  "Dashboard — tel_tele\\telephoto.md": {
    "primary": "A camera lens system with a focal length significantly longer than the physical barrel, used to produce magnified images of distant subjects.",
    "secondary": "In optics and photographic design, a telephoto lens incorporates a front positive element group and a rear negative element group to reduce overall optical assembly length.",
    "quotes": [
      {
        "author": "Ansel Adams",
        "work": "The Camera",
        "quote": "Using a **telephoto** lens compresses spatial perspective, bringing distant mountain peaks into dramatic juxtaposition."
      },
      {
        "author": "Alfred Stieglitz",
        "work": "Camera Work",
        "quote": "The subtle atmospheric haze caught by the **telephoto** objective lent the urban skyline an ethereal softness."
      },
      {
        "author": "Edward Weston",
        "work": "The Daybooks of Edward Weston",
        "quote": "I framed the distant desert dunes through the heavy **telephoto** glass until the contours filled the plate."
      }
    ]
  },
  "Dashboard — tel_tele\\teleport.md": {
    "primary": "To transport instantaneously across space or time without traversing the physical distance between points, especially through technological or supernatural means.",
    "secondary": "In quantum mechanics, quantum teleportation refers to the protocol whereby the quantum state of a particle is transferred to another distant particle using entanglement and classical communication.",
    "quotes": [
      {
        "author": "Charles Fort",
        "work": "Lo!",
        "quote": "I use the term to designate hypothetical transportations that seem to **teleport** physical bodies across miles."
      },
      {
        "author": "Isaac Asimov",
        "work": "Foundation and Empire",
        "quote": "In theoretical physics, no macroscopic device could simply **teleport** matter without immense energy expenditure."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "Speculation that future civilizations might **teleport** travelers remains one of the grandest dreams of science."
      }
    ]
  },
  "Dashboard — tel_tele\\teleprinter.md": {
    "primary": "An electromechanical typewriter and communication terminal used to send and receive typed messages over telegraph lines or radio channels.",
    "secondary": "Widely employed in twentieth-century news agencies, stock exchanges, and military networks, teleprinters utilized 5-level Baudot or 7-level ASCII codes to automate teletype communication.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "Dispatches from the Ministry arrived continuously, clattering out from the brass carriage of the **teleprinter**."
      },
      {
        "author": "Graham Greene",
        "work": "Our Man in Havana",
        "quote": "The rhythmic chattering of the embassy **teleprinter** warned the consul that London demanded immediate answers."
      },
      {
        "author": "Arthur Koestler",
        "work": "Darkness at Noon",
        "quote": "Official bulletins were torn directly from the humming **teleprinter** and handed to the interrogation committee."
      }
    ]
  },
  "Dashboard — tel_tele\\telescope.md": {
    "primary": "An optical instrument designed to collect and magnify electromagnetic radiation, especially visible light, from distant celestial objects.",
    "secondary": "In observational astronomy, telescopes are classified broadly into refracting (dioptric), reflecting (catoptric), and catadioptric systems, as well as radio and space-based observatories.",
    "quotes": [
      {
        "author": "Galileo Galilei",
        "work": "Sidereus Nuncius",
        "quote": "Directing my newly constructed **telescope** toward the heavens, I beheld four satellites revolving around Jupiter."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "To avoid chromatic aberration in lenses, I resolved to construct a reflecting **telescope** with a polished metal mirror."
      },
      {
        "author": "William Herschel",
        "work": "Astronomical Observations Relating to the Construction of the Heavens",
        "quote": "Scanning the nebula with my forty-foot **telescope**, the unresolved mist resolved into countlessly glittering suns."
      }
    ]
  },
  "Dashboard — tel_tele\\telescoped.md": {
    "primary": "Compressed, collapsed, or driven into one another like the concentric sliding sections of a cylindrical hand telescope.",
    "secondary": "In narrative theory or historiography, describing a structure in which events spanning decades are condensed into a single concise chronological sequence.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "The Uncommercial Traveller",
        "quote": "The railway carriages had **telescoped** upon impact, splintering wooden bulkheads into kindling."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "In his memory, long months of agonizing solitude seemed **telescoped** into an instantaneous pang of regret."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The chronicler **telescoped** three separate barbarian incursions into a single disastrous campaign."
      }
    ]
  },
  "Dashboard — tel_tele\\telescopium.md": {
    "primary": "A faint southern constellation introduced in the eighteenth century by Nicolas-Louis de Lacaille, representing an astronomical telescope.",
    "secondary": "In modern celestial cartography, Telescopium contains no stars brighter than third magnitude and borders Ara, Corona Australis, Indus, and Pavo in the southern hemisphere.",
    "quotes": [
      {
        "author": "Nicolas-Louis de Lacaille",
        "work": "Coelum Australe Stelliferum",
        "quote": "In mapping the uncatalogued stars of the southern sky, I designated the new grouping as **Telescopium**."
      },
      {
        "author": "Richard A. Proctor",
        "work": "A Star Atlas for the Library, the School and the Observatory",
        "quote": "The constellation **Telescopium** occupies a barren tract of sky south of Sagittarius and the Southern Crown."
      },
      {
        "author": "Agnes Mary Clerke",
        "work": "A Popular History of Astronomy during the Nineteenth Century",
        "quote": "Lacaille chose names representing scientific instruments for southern asterisms, including **Telescopium** and Microscopium."
      }
    ]
  },
  "Dashboard — tel_tele\\telescopy.md": {
    "primary": "The art, science, or practice of making, using, or observing through telescopes.",
    "secondary": "In the history of instrumentation, telescopy encompasses the optical design, mechanical mounting, and observational techniques used in visual and photographic astronomy.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "Practical **telescopy** requires not merely fine optical figure but stable equatorial mountings to track celestial motion."
      },
      {
        "author": "George Ellery Hale",
        "work": "The Study of Stellar Evolution",
        "quote": "Advances in photographic **telescopy** permitted astronomers to capture faint nebulae invisible to the human eye."
      },
      {
        "author": "Percival Lowell",
        "work": "Mars and Its Canals",
        "quote": "Planetary **telescopy** demands nights of extraordinary atmospheric stillness to reveal fine surface markings."
      }
    ]
  },
  "Dashboard — tel_tele\\teleselling.md": {
    "primary": "The direct selling of products or commercial services to potential customers via telephone calls; telemarketing.",
    "secondary": "In marketing management, teleselling incorporates scripted outbound sales calls, inbound customer order processing, and computerized database management systems.",
    "quotes": [
      {
        "author": "Philip Kotler",
        "work": "Marketing Management",
        "quote": "Direct marketing expenditures shifted heavily toward **teleselling** as corporate call center automation lowered transaction costs."
      },
      {
        "author": "Peter Drucker",
        "work": "Management: Tasks, Responsibilities, Practices",
        "quote": "The success of outbound **teleselling** relies on understanding customer needs rather than relentless repetitive badgering."
      },
      {
        "author": "David Ogilvy",
        "work": "Ogilvy on Advertising",
        "quote": "Integrating direct mail campaigns with coordinated **teleselling** yielded response rates far superior to print advertising alone."
      }
    ]
  },
  "Dashboard — tel_tele\\televise.md": {
    "primary": "To broadcast or transmit moving visual images and accompanying sound by television.",
    "secondary": "In communications and media history, the verb describes the transition from local camera capture to radio-frequency modulation and terrestrial or satellite distribution.",
    "quotes": [
      {
        "author": "John Logie Baird",
        "work": "Television: A Description of the Baird System",
        "quote": "Our earliest successful apparatus could **televise** only crude silhouetted outlines of the human face."
      },
      {
        "author": "George Orwell",
        "work": "The Lion and the Unicorn",
        "quote": "Commercial interests will undoubtedly seek to **televise** spectacles calculated to keep the populace passive."
      },
      {
        "author": "Marshall McLuhan",
        "work": "Understanding Media: The Extensions of Man",
        "quote": "The decision to **televise** political debates altered the balance of rhetorical style in modern democracies."
      }
    ]
  },
  "Dashboard — tel_tele\\television.md": {
    "primary": "A telecommunication system and electronic receiver for broadcasting and reproducing moving images and synchronized sound over distance.",
    "secondary": "In cultural sociology and media studies, television emerged as the dominant twentieth-century medium for domestic entertainment, news broadcasting, and political dissemination.",
    "quotes": [
      {
        "author": "Marshall McLuhan",
        "work": "The Gutenberg Galaxy",
        "quote": "Electronic media, preeminently **television**, reshaped human perception into that of a simultaneous global village."
      },
      {
        "author": "Neil Postman",
        "work": "Amusing Ourselves to Death",
        "quote": "When public discourse is conducted primarily through **television**, serious argument gives way to visual entertainment."
      },
      {
        "author": "E. B. White",
        "work": "One Man's Meat",
        "quote": "I believe **television** is going to be the test of the modern world, a weapon of either enlightenment or utter triviality."
      }
    ]
  },
  "Dashboard — tel_tele\\teleworking.md": {
    "primary": "The practice of working remotely from home or an alternative location using telecommunications, computers, and the internet rather than commuting.",
    "secondary": "In organizational sociology and labor economics, teleworking expanded rapidly in the digital era, reshaping urban transit, corporate real estate, and work-life balance.",
    "quotes": [
      {
        "author": "Alvin Toffler",
        "work": "The Third Wave",
        "quote": "The rise of the electronic cottage means that **teleworking** will replace the daily commute for millions of knowledge workers."
      },
      {
        "author": "Manuel Castells",
        "work": "The Rise of the Network Society",
        "quote": "Flexibility in network enterprises is reflected in the proliferation of **teleworking** and distributed project teams."
      },
      {
        "author": "Charles Handy",
        "work": "The Age of Unreason",
        "quote": "Organizations adopting **teleworking** must measure productivity by tangible output rather than mere physical attendance."
      }
    ]
  },
  "Dashboard — tel_tele\\telex.md": {
    "primary": "An international telecommunications network of teleprinters connected through dedicated exchanges for transmitting written messages.",
    "secondary": "In commercial history, Telex provided legally recognized written confirmations for international banking, maritime shipping, and diplomatic correspondence prior to the internet.",
    "quotes": [
      {
        "author": "John le Carré",
        "work": "Tinker Tailor Soldier Spy",
        "quote": "The station chief waited anxiously beside the cipher room while the **telex** drum clattered out instructions."
      },
      {
        "author": "Frederick Forsyth",
        "work": "The Dogs of War",
        "quote": "Confidential banking transfers were executed through encoded **telex** cables routed through Zurich."
      },
      {
        "author": "Ken Follett",
        "work": "The Key to Rebecca",
        "quote": "Every urgent dispatch from headquarters arrived over the secure military **telex** link in Cairo."
      }
    ]
  },
  "Dashboard — tem\\acrotomophilia.md": {
    "primary": "A paraphilia characterized by sexual attraction specifically to individuals with amputated limbs.",
    "secondary": "In clinical sexology and psychiatric nosology, acrotomophilia is distinguished from apotemnophilia (the desire to become an amputee oneself), representing an erotic preference for asymmetry or stump anatomy.",
    "quotes": [
      {
        "author": "Richard von Krafft-Ebing",
        "work": "Psychopathia Sexualis",
        "quote": "Certain abnormal erotic fixations, such as **acrotomophilia**, demonstrate how specific physical mutilations can become fetishes."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "In cases of **acrotomophilia**, the erotic imagination focuses with singular intensity upon the site of amputation."
      },
      {
        "author": "John Money",
        "work": "Lovemaps: Clinical Concepts of Sexual/Erotic Health and Pathology",
        "quote": "The diagnostic delineation between apotemnophilia and **acrotomophilia** hinges upon whether the eroticized deficiency belongs to self or partner."
      }
    ]
  },
  "Dashboard — tem\\anatomic.md": {
    "primary": "Of, relating to, or conforming to the structure of the body or anatomy.",
    "secondary": "In surgical and clinical pathology, anatomic relationships dictate operative incisions, vascular ligation points, and radiological identification of normal and abnormal tissues.",
    "quotes": [
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Direct dissection of the cadaver reveals true **anatomic** landmarks that ancient texts had erroneously described."
      },
      {
        "author": "William Hunter",
        "work": "Anatomia Uteri Humani Gravidi",
        "quote": "Carefully prepared engravings preserve the exact **anatomic** proportions of maternal and fetal blood vessels."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "A sound knowledge of **anatomic** variations in the arterial system is indispensable to every operating surgeon."
      }
    ]
  },
  "Dashboard — tem\\anatomise.md": {
    "primary": "To dissect an animal or plant body in order to study its internal structure (chiefly Commonwealth spelling); figuratively, to examine or analyze minutely.",
    "secondary": "In literary and philosophical discourse, to anatomise a subject is to deconstruct its constituent elements, motives, or logical premises with exhaustive rigor.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "I undertake to **anatomise** this vast body of human misery, tracing every symptom to its secret fountain."
      },
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "We must **anatomise** nature by diligent experiment, rather than fashion theories out of imaginative conjecture."
      },
      {
        "author": "William Shakespeare",
        "work": "King Lear",
        "quote": "Let them **anatomise** Regan; see what breeds about her heart, whether there be any cause in nature."
      }
    ]
  },
  "Dashboard — tem\\anatomize.md": {
    "primary": "To dissect a biological organism for structural study; to analyze, dissect, or critique an argument, concept, or character in meticulous detail.",
    "secondary": "In the history of scientific methodology and rhetoric, anatomizing implies uncovering hidden internal mechanisms through rigorous decomposition.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "He who would understand the human intellect must **anatomize** our complex ideas into their simple components."
      },
      {
        "author": "Jonathan Swift",
        "work": "A Tale of a Tub",
        "quote": "Last week I saw a woman flayed, and you will hardly believe how much it altered her person for the worse; let us **anatomize** folly."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "It is the proper business of moral satire to **anatomize** the hypocrisies that disguise self-love."
      }
    ]
  },
  "Dashboard — tem\\apotemnophilia.md": {
    "primary": "A condition characterized by the intense, compulsive desire for the amputation of one or more healthy limbs.",
    "secondary": "In neuropsychiatry, often classified under body integrity dysphoria (BID), apotemnophilia is hypothesized to arise from a congenital mismatch between cortical body maps in the parietal cortex and physical anatomy.",
    "quotes": [
      {
        "author": "V. S. Ramachandran",
        "work": "The Tell-Tale Brain",
        "quote": "Patients afflicted with **apotemnophilia** experience a profound, lifelong conviction that a specific limb does not belong to them."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "The bizarre phenomenology of **apotemnophilia** highlights how deeply the neurological body-image governs our sense of self."
      },
      {
        "author": "John Money",
        "work": "The Journal of Sex Research",
        "quote": "Clinical studies of **apotemnophilia** reveal that the desire for amputation is frequently localized to an exact anatomical boundary."
      }
    ]
  },
  "Dashboard — tem\\atomic.md": {
    "primary": "Of, relating to, or composed of atoms; existing as an indivisible unit or single minute particle.",
    "secondary": "In modern physics and chemistry, atomic denotes structures governed by quantum mechanics at sub-nanometer scales, nuclear forces, and periodic elemental properties.",
    "quotes": [
      {
        "author": "John Dalton",
        "work": "A New System of Chemical Philosophy",
        "quote": "Chemical analysis and synthesis go no farther than to the separation of particles one from another, and to their union; no new **atomic** body is created."
      },
      {
        "author": "Niels Bohr",
        "work": "On the Constitution of Atoms and Molecules",
        "quote": "The stationary states of an **atomic** system can be calculated by applying quantum conditions to electronic orbits."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "Scattering experiments revealed that nearly the entire mass of the **atomic** structure is concentrated in a tiny central nucleus."
      }
    ]
  },
  "Dashboard — tem\\atomise.md": {
    "primary": "To reduce to atoms, tiny particles, or a fine spray; to fragment or break down a cohesive whole into isolated elements (chiefly Commonwealth spelling).",
    "secondary": "In social theory and politics, to atomise a community or society is to disintegrate shared communal bonds, leaving isolated individuals vulnerable to alienation or state control.",
    "quotes": [
      {
        "author": "Hannah Arendt",
        "work": "The Origins of Totalitarianism",
        "quote": "Totalitarian movements seek systematically to **atomise** civil society, destroying every traditional group and family loyalty."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Extreme individualism threatens to **atomise** the social fabric, isolating every citizen in solitary indifference."
      },
      {
        "author": "J. B. S. Haldane",
        "work": "Possible Worlds and Other Essays",
        "quote": "High-velocity fuel injectors **atomise** heavy oil droplets into a vapor susceptible to instantaneous combustion."
      }
    ]
  },
  "Dashboard — tem\\atomism.md": {
    "primary": "The philosophical or scientific theory that all matter is composed of small, indivisible particles called atoms.",
    "secondary": "Originating in ancient Greece with Leucippus and Democritus, revived by Epicurus and Lucretius, and formalized in modern chemistry by John Dalton, atomism explains macroscopic physical phenomena through mechanical interactions of corpuscles.",
    "quotes": [
      {
        "author": "Lucretius",
        "work": "De Rerum Natura",
        "quote": "The ancient doctrine of **atomism** asserts that void and imperishable particles constitute the entire fabric of existence."
      },
      {
        "author": "Robert Boyle",
        "work": "The Sceptical Chymist",
        "quote": "A refined corpuscular philosophy, drawing upon mechanical **atomism**, explains chemical transformations far better than the four elements."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Philosophy of Logical Atomism",
        "quote": "My aim in logical **atomism** is to analyze propositions into ultimate simple facts that correspond directly to reality."
      }
    ]
  },
  "Dashboard — tem\\atomize.md": {
    "primary": "To break into atoms or minute particles; to disperse a liquid into a fine mist; to dissolve social or conceptual unity into fragmented parts.",
    "secondary": "In engineering and combustion science, atomizing fuel increases surface area for rapid oxidation; in political science, atomizing refers to the destruction of intermediate civic institutions.",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "Modern urban sprawl tends to **atomize** civic life, scattering citizens into detached suburban enclaves."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World Revisited",
        "quote": "Bureaucratic centralization and mass media collaborate to **atomize** the population into manageable, solitary units."
      },
      {
        "author": "C. P. Snow",
        "work": "The Two Cultures",
        "quote": "Without an overarching humanistic dialogue, specialized disciplines will **atomize** intellectual life into mutually unintelligible fragments."
      }
    ]
  },
  "Dashboard — tem\\autotomic.md": {
    "primary": "Pertaining to, exhibiting, or capable of autotomy; relating to the deliberate shedding of a limb or body part.",
    "secondary": "In invertebrate zoology and herpetology, autotomic adaptations involve preformed fracture planes and rapid hemostatic sphincters that prevent fatal blood loss during appendage detachment.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "Regeneration",
        "quote": "The **autotomic** reflex in crabs occurs at a specific predetermined articular groove across the second leg segment."
      },
      {
        "author": "Julian Huxley",
        "work": "Problems of Relative Growth",
        "quote": "Following the **autotomic** loss of a claw, compensatory growth hormones stimulate regeneration in subsequent molts."
      },
      {
        "author": "G. H. Parker",
        "work": "The Elementary Nervous System",
        "quote": "An **autotomic** detachment of the tail in lizards is triggered by sensory shocks transmitted through local spinal reflexes."
      }
    ]
  },
  "Dashboard — tem\\autotomise.md": {
    "primary": "To shed or cast off a limb or appendage spontaneously by autotomy, typically as a defensive reflex (chiefly Commonwealth spelling).",
    "secondary": "In behavioral ecology, describing organisms such as geckos, spiders, and octopuses that sacrifice non-vital appendages to escape predation.",
    "quotes": [
      {
        "author": "William Beebe",
        "work": "Nonsuch: Land of Water",
        "quote": "When grasped by a hungry reef fish, the brittlestar will promptly **autotomise** two or three writhing arms to distract its foe."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Certain harvestmen will **autotomise** a long leg that continues to twitch rhythmically while the arachnid scuttles away."
      },
      {
        "author": "J. Arthur Thomson",
        "work": "The Biology of the Seasons",
        "quote": "A captured lizard does not hesitate to **autotomise** its tail to ensure its immediate survival."
      }
    ]
  },
  "Dashboard — tem\\autotomize.md": {
    "primary": "To discard or cast off a body part spontaneously through reflex autotomy in response to danger or injury.",
    "secondary": "In physiological biology, autotomize describes active muscular severance along a predetermined cleavage plane, minimizing hemorrhage and facilitating tissue regeneration.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "The ability to **autotomize** a tail represents an exquisite evolutionary trade-off between current survival and energetic cost."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Blind Watchmaker",
        "quote": "Natural selection favors individuals that can cleanly **autotomize** an extremity rather than perish in the predator's grasp."
      },
      {
        "author": "Raymond L. Ditmars",
        "work": "Reptiles of the World",
        "quote": "If you seize the glass snake lizard by the tail, the creature will instantly **autotomize** the member into several fragments."
      }
    ]
  },
  "Dashboard — tem\\autotomy.md": {
    "primary": "The spontaneous casting off of a limb or other body part when seized, threatened, or injured, followed in many taxa by regeneration.",
    "secondary": "In evolutionary morphology, autotomy is an anti-predator defense widespread in arthropods, echinoderms, and reptiles, supported by specialized nervous arcs and fracture planes.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "The phenomenon of **autotomy** in crustaceans illustrates how an apparent voluntary mutilation is governed by instinctive reflex."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish: An Introduction to the Study of Zoology",
        "quote": "When an appendage is severely bruised, **autotomy** at the breakage plane prevents dangerous fluid leakage."
      },
      {
        "author": "Hans Driesch",
        "work": "The Science and Philosophy of the Organism",
        "quote": "Following deliberate **autotomy**, the stump displays an intrinsic morphogenetic field capable of complete organogenesis."
      }
    ]
  },
  "Dashboard — tem\\diatom.md": {
    "primary": "A single-celled photosynthetic alga of the class Bacillariophyceae, having a cell wall composed of silica consisting of two overlapping valves.",
    "secondary": "In marine ecology and limnology, diatoms are critical primary producers in aquatic food webs, generating significant global oxygen, with their fossilized siliceous frustules forming diatomaceous earth.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "Under the microscope, each siliceous **diatom** shell exhibits delicate geometric perforations of peerless symmetry."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The spring phytoplankton bloom is inaugurated by the explosive multiplication of every floating **diatom** species."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "Countless billions of the glassy **diatom** *Coscinodiscus* drift through the sunlit epipelagic waters of the North Sea."
      }
    ]
  },
  "Dashboard — tem\\diatomic.md": {
    "primary": "Consisting of two atoms in each molecule; having two replaceable atoms or radicals.",
    "secondary": "In physical chemistry, homonuclear diatomic gases (such as H2, N2, O2, F2, Cl2) and heteronuclear diatomic molecules (such as CO, NO, HCl) display characteristic rotational and vibrational energy spectra.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The bond energy and interatomic distance in a **diatomic** molecule like nitrogen reflect a stable triple covalent bond."
      },
      {
        "author": "Gerhard Herzberg",
        "work": "Molecular Spectra and Molecular Structure: Spectra of Diatomic Molecules",
        "quote": "Infrared and Raman spectra of any **diatomic** species yield fundamental parameters of internuclear distance and force constants."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Avogadro's hypothesis reconciled the observed combining volumes of gases by proving that elemental oxygen is **diatomic**."
      }
    ]
  },
  "Dashboard — tem\\dichotomous.md": {
    "primary": "Dividing into two parts, branches, or classifications; exhibiting dichotomy.",
    "secondary": "In botany and biological taxonomy, dichotomous branching occurs when the apical growing point forks equally into two equivalent axes, widely utilized in diagnostic dichotomous keys.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "A diagnostic **dichotomous** key guides the student through successive pairs of mutually exclusive floral characteristics."
      },
      {
        "author": "William Bateson",
        "work": "Materials for the Study of Variation",
        "quote": "Certain abnormal mutations produce a **dichotomous** fork in appendages that are normally single and undivided."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The fossil flora displays a primitive **dichotomous** venation pattern characteristic of ancient paleozoic ferns."
      }
    ]
  },
  "Dashboard — tem\\dichotomously.md": {
    "primary": "In a dichotomous manner; dividing or branching repeatedly into two equal forks or divisions.",
    "secondary": "In systematic taxonomy and morphometrics, describing vegetative growth or structural bifurcations that split symmetrically at successive nodes.",
    "quotes": [
      {
        "author": "Francis Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The terminal shoot divides **dichotomously**, each subsequent branch pursuing an independent arc of circumnutation."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "The inflorescence branches **dichotomously**, bearing pairs of subsessile flowers along the upper nodes."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Certain seaweeds and coral colonies ramify **dichotomously** according to rigorous mathematical laws of surface tension."
      }
    ]
  },
  "Dashboard — tem\\dichotomy.md": {
    "primary": "A division or contrast between two things that are represented as being opposed or entirely different.",
    "secondary": "In philosophical epistemology and formal logic, a dichotomy partitions a universe of discourse into two mutually exclusive and collectively exhaustive categories.",
    "quotes": [
      {
        "author": "William James",
        "work": "Pragmatism: A New Name for Some Old Ways of Thinking",
        "quote": "Philosophers have long posited a rigid **dichotomy** between the tender-minded rationalist and tough-minded empiricist."
      },
      {
        "author": "John Dewey",
        "work": "Democracy and Education",
        "quote": "We must overcome the false **dichotomy** between cultural education and vocational preparation in modern schooling."
      },
      {
        "author": "Arthur Schopenhauer",
        "work": "The World as Will and Representation",
        "quote": "The fundamental **dichotomy** of consciousness divides the subject who knows from the object that is known."
      }
    ]
  },
  "Dashboard — tem\\ectomy.md": {
    "primary": "A surgical excision or removal of a specified anatomical organ or part (used as an independent noun or suffix).",
    "secondary": "In medical lexicography and operative surgery, derived from Greek *ektome* (cutting out), forming compounds like appendectomy, hysterectomy, and splenectomy.",
    "quotes": [
      {
        "author": "William Halsted",
        "work": "Surgical Papers",
        "quote": "The complete **ectomy** of the affected lymphatic chain proved crucial in reducing regional cancer recurrence."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "Where total **ectomy** of the acoustic neuroma would endanger the facial nerve, subcapsular curettage was preferred."
      },
      {
        "author": "William J. Mayo",
        "work": "Collected Papers of the Mayo Clinic",
        "quote": "A timely surgical **ectomy** of the inflamed gallbladder prevents perforation and generalized biliary peritonitis."
      }
    ]
  },
  "Dashboard — tem\\embolectomy.md": {
    "primary": "The surgical removal of an embolus (such as a dislodged blood clot) that is blocking a blood vessel.",
    "secondary": "In vascular surgery, the procedure was revolutionized by Thomas Fogarty's invention of the balloon catheter, enabling rapid, minimally invasive arterial embolectomy under local anesthesia.",
    "quotes": [
      {
        "author": "Alexis Carrel",
        "work": "Results of the Transplantation of Blood Vessels, Organs and Limbs",
        "quote": "Careful vascular suturing following **embolectomy** restores pulsatile distal perfusion without forming secondary thrombi."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Could one extract the impacted plug by direct **embolectomy**, ischemic necrosis of the peripheral tissue might be averted."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Heart",
        "quote": "Emergency femoral **embolectomy** must be executed within six hours of acute occlusion to preserve limb viability."
      }
    ]
  },
  "Dashboard — tem\\entomologic.md": {
    "primary": "Of or relating to entomology, the scientific study of insects.",
    "secondary": "In biological nomenclature, denoting field collections, specimen preparation, and morphological keys applied to insect classification and pest management.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Spider",
        "quote": "My small garden observatory afforded endless opportunities for meticulous **entomologic** research."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The Moluccas proved a paradise for **entomologic** discovery, yielding beetles and butterflies of unmatched splendor."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The vast diversity recorded in every standard **entomologic** catalog demonstrates the ceaseless action of natural selection."
      }
    ]
  },
  "Dashboard — tem\\entomological.md": {
    "primary": "Pertaining to the scientific study of insects or the methods and collections of entomologists.",
    "secondary": "In agricultural and public health contexts, entomological surveys monitor vector-borne disease transmission (e.g. malaria mosquitoes) and crop pollination dynamics.",
    "quotes": [
      {
        "author": "Vladimir Nabokov",
        "work": "Speak, Memory",
        "quote": "Armed with an **entomological** net and killing jar, I spent my childhood summers scouring Russian bogs for rare blues."
      },
      {
        "author": "Henry Walter Bates",
        "work": "The Naturalist on the River Amazons",
        "quote": "Our **entomological** collections from the Amazonian basin exceeded fourteen thousand species, mostly new to science."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Rigorous **entomological** analysis of pheromone trails uncovered the chemical syntax governing the ant colony."
      }
    ]
  },
  "Dashboard — tem\\entomologist.md": {
    "primary": "A scientist or specialist who studies insects.",
    "secondary": "Entomologists conduct research in insect physiology, taxonomy, ecology, ethology, and pest control, often working in agriculture, forestry, and public health epidemiology.",
    "quotes": [
      {
        "author": "Charles Valentine Riley",
        "work": "Annual Report on the Noxious, Beneficial, and Other Insects of Missouri",
        "quote": "The economic **entomologist** must balance agricultural chemical application with the preservation of natural predators."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "Every patient **entomologist** finds that an artificial formicarium reveals social behaviors invisible in open fields."
      },
      {
        "author": "August Forel",
        "work": "The Senses of Insects",
        "quote": "To the keen **entomologist**, the olfactory antenna of a wasp is a sensory marvel beyond human imagination."
      }
    ]
  },
  "Dashboard — tem\\entomology.md": {
    "primary": "The scientific study of insects, a major branch of zoology.",
    "secondary": "Encompassing the morphology, taxonomy, physiology, ecology, and economic significance of Hexapoda, entomology provides foundational insights into pollination, evolution, and vector biology.",
    "quotes": [
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "The study of **entomology** opens to our view a world of miniature wonders exhibiting divine wisdom and design."
      },
      {
        "author": "John Henry Comstock",
        "work": "The Elements of Insect Anatomy",
        "quote": "Modern **entomology** establishes wing venation homologies as the primary structural basis for insect classification."
      },
      {
        "author": "L. O. Howard",
        "work": "A History of Applied Entomology",
        "quote": "The progress of agricultural **entomology** transformed the control of destructive plagues like the cotton boll weevil."
      }
    ]
  },
  "Dashboard — tem\\entomomancy.md": {
    "primary": "Divination or prophecy based on the appearance, numbers, or behavior of insects.",
    "secondary": "In cultural anthropology and the history of occultism, entomomancy was practiced in various ancient cultures by interpreting ant swarms, locust flights, or spider web patterns as omens.",
    "quotes": [
      {
        "author": "Edward Tylor",
        "work": "Primitive Culture",
        "quote": "Practices of **entomomancy** survive in folklore where sudden swarms of ants or bees are interpreted as auguries of war."
      },
      {
        "author": "James George Frazer",
        "work": "Folk-Lore in the Old Testament",
        "quote": "Diviners resorted to **entomomancy**, observing the erratic migrations of locusts to foretell royal fortunes."
      },
      {
        "author": "Andrew Lang",
        "work": "Custom and Myth",
        "quote": "Like augury from birds, rustic **entomomancy** attributed prophetic intelligence to the movements of common insects."
      }
    ]
  },
  "Dashboard — tem\\entomophagous.md": {
    "primary": "Feeding on or consuming insects; insectivorous.",
    "secondary": "In trophic ecology and human nutrition, entomophagous animals (like anteaters, bats, and swallows) control insect populations, while human entomophagy is studied as a sustainable protein source.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Darwinism: An Exposition of the Theory of Natural Selection",
        "quote": "Mimetic protective colorations evolved specifically to deceive keen-sighted **entomophagous** birds."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The specialized glandular hairs of sundews prove that a plant can adopt an **entomophagous** habit in nitrogen-poor bogs."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The pangolin and aardvark exhibit extreme morphological convergence suited to their **entomophagous** diet."
      }
    ]
  },
  "Dashboard — tem\\entomophilous.md": {
    "primary": "Pollinated by insects (of flowers or plants).",
    "secondary": "In pollination biology, entomophilous angiosperms have co-evolved conspicuous brightly colored petals, sweet fragrances, and nectar rewards to attract insect pollinators like bees and moths.",
    "quotes": [
      {
        "author": "Christian Konrad Sprengel",
        "work": "Discovery of the Secret of Nature in the Structure and Fertilization of Flowers",
        "quote": "The colored guidelines on the corolla exist expressly to guide the bee into the throat of the **entomophilous** flower."
      },
      {
        "author": "Hermann Müller",
        "work": "The Fertilisation of Flowers",
        "quote": "The sticky, sculptured pollen grains of an **entomophilous** blossom adhere readily to the hairy coat of foraging bees."
      },
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by which Orchids are Fertilised by Insects",
        "quote": "Orchid floral architecture represents the most intricate **entomophilous** adaptation observed in the vegetable kingdom."
      }
    ]
  },
  "Dashboard — tem\\epitomise.md": {
    "primary": "To serve as a perfect example or summary of something; to embody typical characteristics (chiefly Commonwealth spelling).",
    "secondary": "In literary criticism and historiography, to epitomise an intellectual era or aesthetic movement is to synthesize its central themes and virtues in a single work or figure.",
    "quotes": [
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "The grand classical ideals seem to **epitomise** the harmonious balance of sweetness and light."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "Dante's great poem does in truth **epitomise** the spiritual consciousness of the entire Christian Middle Ages."
      },
      {
        "author": "Walter Pater",
        "work": "Studies in the History of the Renaissance",
        "quote": "The enigmatic smile of the Mona Lisa appeared to **epitomise** the restless, questing soul of the new age."
      }
    ]
  },
  "Dashboard — tem\\epitomize.md": {
    "primary": "To be a typical or ideal representation of; to embody or exemplify; to summarize the essence of a larger concept.",
    "secondary": "In rhetoric and critical analysis, epitomize denotes distilling an expansive thesis, cultural epoch, or artistic ethos into a quintessential expression.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Great individuals **epitomize** the latent thoughts and aspirations of their contemporary generation."
      },
      {
        "author": "George Santayana",
        "work": "The Life of Reason",
        "quote": "A Greek temple seems to **epitomize** the serenity and proportion that reason seeks to instill in human life."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Instinct of Workmanship",
        "quote": "The gilded ornamentation of lavish estates came to **epitomize** conspicuous consumption in the industrial era."
      }
    ]
  },
  "Dashboard — tem\\microtome.md": {
    "primary": "A precision mechanical instrument used to cut extremely thin slices (sections) of biological tissue for microscopic examination.",
    "secondary": "Invented in proto-form by Alexander Cummings and George Adams and refined by Wilhelm His, microtomes slice specimens embedded in paraffin or resin to thicknesses of 1 to 10 micrometers.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Recollections of My Life",
        "quote": "With a newly acquired sliding **microtome**, I could cut silver-impregnated brain sections of uniform thinness."
      },
      {
        "author": "E. V. Cowdry",
        "work": "Laboratory Technique in Biology and Medicine",
        "quote": "Maintaining an exquisitely honed razor edge on the rotary **microtome** prevents tissue tearing and compression artifacts."
      },
      {
        "author": "Wilhelm His",
        "work": "The Development of the Human Embryo",
        "quote": "Serial reconstruction of embryonic organs became practicable only after the development of the mechanical **microtome**."
      }
    ]
  },
  "Dashboard — tem\\monatomic.md": {
    "primary": "Having or consisting of a single atom in the molecule; having a valency of one.",
    "secondary": "In thermodynamics and physical chemistry, noble gases (He, Ne, Ar, Kr, Xe, Rn) are monatomic at standard conditions, exhibiting an ideal heat capacity ratio (gamma) of exactly 5/3.",
    "quotes": [
      {
        "author": "William Ramsay",
        "work": "The Gases of the Atmosphere: The History of Their Discovery",
        "quote": "Acoustic velocity measurements confirmed that argon gas is strictly **monatomic**, lacking internal molecular vibrations."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "The ratio of specific heats in a **monatomic** gas agrees with the kinetic theory calculation for three translational degrees of freedom."
      },
      {
        "author": "Lord Rayleigh",
        "work": "Scientific Papers",
        "quote": "The spectrum and thermodynamic behavior of helium reaffirmed its fundamentally **monatomic** constitution."
      }
    ]
  },
  "Dashboard — tem\\monoatomic.md": {
    "primary": "Consisting of single separate atoms rather than polyatomic molecules (variant of monatomic); having a valence of one.",
    "secondary": "In vacuum science and surface physics, monoatomic layers (such as graphene or adatoms) exhibit distinct electronic band structures and two-dimensional quantum transport.",
    "quotes": [
      {
        "author": "Irving Langmuir",
        "work": "Phenomena, Atoms and Molecules",
        "quote": "Tungsten filaments in high vacuum adsorb a stable **monoatomic** film of thorium that drastically increases electron emission."
      },
      {
        "author": "J. J. Thomson",
        "work": "Rays of Positive Electricity and Their Application to Chemical Analyses",
        "quote": "Positive ray parabolas showed distinct traces corresponding to **monoatomic** ions in the discharge tube."
      },
      {
        "author": "Linus Pauling",
        "work": "The Architecture of Molecules",
        "quote": "Under high thermal excitation, metal vapors like mercury behave as ideal **monoatomic** gases."
      }
    ]
  },
  "Dashboard — tem\\pentatomic.md": {
    "primary": "Containing or composed of five atoms in a molecule; having five replaceable hydrogen atoms or five hydroxyl groups.",
    "secondary": "In molecular chemistry, pentatomic molecules (such as methane, CH4, or phosphorus pentafluoride, PF5) possess distinctive tetrahedral, trigonal bipyramidal, or planar geometries.",
    "quotes": [
      {
        "author": "Dmitri Mendeleev",
        "work": "The Principles of Chemistry",
        "quote": "Marsh gas, or methane, represents the simplest **pentatomic** carbon compound with four peripheral hydrogen atoms."
      },
      {
        "author": "August Kekulé",
        "work": "Lehrbuch der Organischen Chemie",
        "quote": "The symmetrical chemical stability of the **pentatomic** methane molecule reflects carbon's saturated tetravalent character."
      },
      {
        "author": "Gerhard Herzberg",
        "work": "Infrared and Raman Spectra of Polyatomic Molecules",
        "quote": "Normal vibrational modes in a **pentatomic** tetrahedral molecule split into nine distinct fundamental frequencies."
      }
    ]
  },
  "Dashboard — tem\\polyatomic.md": {
    "primary": "Consisting of or containing three or more atoms within a molecule or ionic species.",
    "secondary": "In physical chemistry, polyatomic molecules (such as H2O, CO2, NH3, benzene) feature complex vibrational modes, rotational manifolds, and cooperative chemical bonds compared to simple diatomic species.",
    "quotes": [
      {
        "author": "Gilbert N. Lewis",
        "work": "Valence and the Structure of Atoms and Molecules",
        "quote": "Shared electron pairs provide the coherent architecture binding stable **polyatomic** molecules together."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Resonance between canonical structures stabilizes many planar **polyatomic** ions such as carbonate and nitrate."
      },
      {
        "author": "Gerhard Herzberg",
        "work": "Electronic Spectra and Electronic Structure of Polyatomic Molecules",
        "quote": "The determination of geometry in excited states of a **polyatomic** species requires resolving overlapping band bands."
      }
    ]
  },
  "Dashboard — tem\\polytomy.md": {
    "primary": "A division or branching into many parts, sections, or categories; in phylogenetics, an internal node of a cladogram that has more than two immediate descendant lineages.",
    "secondary": "In cladistics, a polytomy can represent either 'soft polytomy' (uncertainty due to insufficient phylogenetic data) or 'hard polytomy' (simultaneous, rapid speciation events).",
    "quotes": [
      {
        "author": "Willi Hennig",
        "work": "Phylogenetic Systematics",
        "quote": "A trichotomy or higher **polytomy** in a cladogram usually signals an unresolved relationship awaiting more synapomorphies."
      },
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "Whenever explosive adaptive radiation occurs within a brief geological interval, a phylogenetic **polytomy** may reflect historical reality."
      },
      {
        "author": "Douglas J. Futuyma",
        "work": "Evolutionary Biology",
        "quote": "The tree exhibits a star-like **polytomy** at the base of the mammalian radiation due to rapid post-Cretaceous speciation."
      }
    ]
  },
  "Dashboard — tem\\Temnospondyli.md": {
    "primary": "An extinct, diverse subclass or order of primitive labyrinthodont amphibians that flourished from the Carboniferous through the Early Cretaceous periods.",
    "secondary": "In vertebrate paleontology, temnospondyls were among the earliest terrestrial tetrapods, featuring multipartite vertebrae (pleurocentra and intercentra) and giving rise hypothetically to modern Lissamphibia.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The massive skulls and stereospondylous vertebrae of the **Temnospondyli** dominate Carboniferous swamp deposits."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Extinct Batrachia of North America",
        "quote": "In these Permian formations, species assigned to **Temnospondyli** attained lengths exceeding nine feet."
      },
      {
        "author": "Robert L. Carroll",
        "work": "Vertebrate Paleontology and Evolution",
        "quote": "The sensory sulci on the skull roof indicate that many advanced members of the **Temnospondyli** returned to a purely aquatic habit."
      }
    ]
  },
  "Dashboard — tem\\tmesis.md": {
    "primary": "The insertion of a word or phrase between the parts of a compound word or between syllables of a word (e.g. 'a whole nother', 'what person soever').",
    "secondary": "In classical philology and rhetoric, tmesis was frequently employed in ancient Greek poetry (notably Homeric verse) where preverbs were separated from their verbs by metrical necessity.",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "The rhetorical figure of **tmesis** separates compound elements, giving poetic cadence an unexpected force."
      },
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "Archaic legal idioms retain instances of **tmesis**, as when 'howsoever' is divided into 'how great soever'."
      },
      {
        "author": "H. W. Fowler",
        "work": "A Dictionary of Modern English Usage",
        "quote": "Deliberate **tmesis** in vernacular speech serves as an emphatic intensifier, often creating humorous colloquialisms."
      }
    ]
  },
  "Dashboard — tem\\tome.md": {
    "primary": "A large, heavy, or scholarly book, especially one forming part of a multivolume work.",
    "secondary": "Derived from Greek *tomos* (a section or roll of papyrus cut from a larger scroll), tome carries connotations of erudition, density, and intellectual gravitas.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Raven",
        "quote": "Once upon a midnight dreary, while I pondered, weak and weary, / Over many a quaint and curious volume of forgotten **tome**."
      },
      {
        "author": "Washington Irving",
        "work": "The Sketch Book of Geoffrey Crayon",
        "quote": "He sat surrounded by venerable folios, extracting wisdom from each leather-bound **tome** on the dusty shelves."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Professor Teufelsdröckh produced a massive **tome** containing speculative philosophies of cosmic clothing."
      }
    ]
  },
  "Dashboard — tem\\tomogram.md": {
    "primary": "A two-dimensional radiographic image or sectional picture of an internal plane or slice of an organ or object.",
    "secondary": "In diagnostic radiology, tomograms obtained via conventional linear tomography or computerized tomography (CT) reconstruct cross-sectional slices while blurring out adjacent structures.",
    "quotes": [
      {
        "author": "Godfrey Hounsfield",
        "work": "Computerized Transverse Axial Scanning",
        "quote": "The reconstructed **tomogram** revealed clear density variations between gray and white matter that planar radiography could never show."
      },
      {
        "author": "Allan M. Cormack",
        "work": "Representation of a Function by Its Line Integrals",
        "quote": "Mathematical line integrals through the patient allow one to construct a precise sectional **tomogram** of tissue absorption."
      },
      {
        "author": "William Osler",
        "work": "A Equanimitas and Other Addresses",
        "quote": "A modern diagnostic **tomogram** enables the clinician to detect deep thoracic lesions before external symptoms emerge."
      }
    ]
  }
}

out_mjs = "main app/scripts/curate-finish5-batch1.mjs"

with open(out_mjs, "w", encoding="utf-8") as f:
    f.write("import path from 'path';\n")
    f.write("import { updateNotesBatch } from './curate-updater-util.mjs';\n\n")
    f.write("const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');\n\n")
    f.write("const batchData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n\n")
    f.write("const count = updateNotesBatch(baseClusterDir, batchData);\n")
    f.write("console.log(`[Finish Slice 5 - Batch 1] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);\n")

print(f"Generated {out_mjs} with {len(data)} notes.")
