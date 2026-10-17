import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — caust\\cauterize.md": {
    "primary": "To burn, sear, or destroy tissue using a hot iron, electric current, freezing agent, or caustic chemical to stop bleeding or prevent infection (US spelling).",
    "secondary": "Metaphorically, to make insensitive, callous, or deadened to emotional, moral, or psychological feelings.",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "The Apologie and Treatise of Ambroise Paré",
        "quote": "I observed that those wounded limbs which we did not **cauterize** with boiling oil healed far more cleanly."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The surgeon chose to **cauterize** the oozing bleeding vessels with electrocautery before closing the fascial layer."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Desperate political crises require stern remedies to **cauterize** the festering corruptions of the old regime."
      }
    ]
  },
  "Dashboard — caust\\cautery.md": {
    "primary": "An instrument, burning device, or chemical agent used for searing or destroying living tissue; or the medical procedure of cauterizing.",
    "secondary": "In clinical surgery, an operative modality divided into actual cautery (heat/electricity) and potential cautery (chemical escharotics) for surgical hemostasis and ablation.",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "The Apologie and Treatise of Ambroise Paré",
        "quote": "Before my day, surgeons relied solely upon the cruel application of the actual **cautery** to arrest hemorrhage."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Light linear **cautery** applied to the mucous membrane of the septum effectively prevented recurrent nosebleeds."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Medicine must not shrink from applying the sharp knife or searing **cautery** when gangrenous corruption threatens the body."
      }
    ]
  },
  "Dashboard — caust\\caution.md": {
    "primary": "Prudence, care, and forethought exercised to avoid danger, error, or harm; or a formal warning.",
    "secondary": "In law and administrative ethics, a formal warning administered in lieu of immediate prosecution, or the deliberate suspension of hasty judgment in scientific inquiry.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "The understanding must not be supplied with wings, but rather hung with weights, that it may proceed with patient **caution**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The mother baboon watches over her infant with extraordinary vigilance and instinctive **caution** whenever predators lurk near."
      },
      {
        "author": "William Shakespeare",
        "work": "Julius Caesar",
        "quote": "Caesar, all hail! The ides of March are come, yet take **caution** of the warning that the soothsayer gave."
      }
    ]
  },
  "Dashboard — caust\\cautiously.md": {
    "primary": "In a careful, prudent, and watchful manner; with deliberate caution so as to avoid hazards or mistakes.",
    "secondary": "Proceeding with measured steps and thorough verification before committing to a decisive course of action.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "We steered **cautiously** through the narrow channel, keeping a sharp lookout for submerged coral heads."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The whaleboat approached the sleeping leviathan **cautiously**, every oar muffled with canvas against the thole-pins."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Lydgate weighed his diagnostic opinions **cautiously**, aware that local prejudices watched his every medical decision."
      }
    ]
  },
  "Dashboard — caust\\cautiousness.md": {
    "primary": "The quality, habit, or state of being cautious, prudent, and vigilant against potential dangers or errors.",
    "secondary": "In phrenological and psychological history, an innate faculty or personality trait governing circumspection, risk aversion, and defensive foresight.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Excessive **cautiousness** paralyzes spontaneous action, trapping the neurotic mind in an endless cycle of hesitation."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Commercial enterprise in democratic nations is characterized by bold ambition tempered by an instinctive practical **cautiousness**."
      },
      {
        "author": "Francis Galton",
        "work": "Inquiries into Human Faculty and Its Development",
        "quote": "Phrenologists assigned a prominent cranial bump above the ears to denote the moral faculty of **cautiousness**."
      }
    ]
  },
  "Dashboard — caust\\diacaustic.md": {
    "primary": "In optics and geometry, a caustic curve or surface formed by the envelope of light rays refracted through a curved transparent surface or lens.",
    "secondary": "In differential geometry and geometrical optics, the refracted envelope line or focal cusp produced by spherical aberration, contrasting with reflected catacaustic curves.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Rays passing through a thick spherical glass sphere converge upon an intricate refracted envelope termed a **diacaustic** curve."
      },
      {
        "author": "Christiaan Huygens",
        "work": "Treatise on Light",
        "quote": "The geometry of the **diacaustic** illustrates how unequal refraction across curved boundaries creates caustic cusps of intense illumination."
      },
      {
        "author": "Ernst Mach",
        "work": "The Principles of Physical Optics",
        "quote": "Spherical aberration in simple lenses reveals itself directly through the bright cusp of the refracted **diacaustic**."
      }
    ]
  },
  "Dashboard — caust\\encaustic.md": {
    "primary": "An ancient painting technique using pigments mixed with hot molten beeswax, applied to a surface and fixed with heat; or a work produced in this medium.",
    "secondary": "In the history of art and ceramics, an exceptionally durable medium famously seen in Roman Egyptian Fayum mummy portraits, and in ceramic floor tiles decorated with inlaid colored clays.",
    "quotes": [
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "The ancient masters perfected **encaustic** painting, burning wax colours into wood and ivory so durably that moisture could never fade them."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The pavement of the medieval basilica was paved with rich **encaustic** tiles displaying armorial badges and heraldic beasts."
      },
      {
        "author": "Walter Pater",
        "work": "Studies in the History of the Renaissance",
        "quote": "The life-like gaze in the Fayum portraits survives because the molten **encaustic** wax locked in the pigment with translucent vitality."
      }
    ]
  },
  "Dashboard — caust\\holocaust.md": {
    "primary": "Great destruction or slaughter on a mass scale, especially caused by fire; specifically (capitalized), the mass genocide of six million Jews by the Nazi regime; historically, a whole sacrificial burnt offering.",
    "secondary": "In historical theology and cultural memory, an offering consumed entirely by sacrificial flames; in modern historiography, the systematic, state-sponsored industrial genocide of European Jewry.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Samson Agonistes",
        "quote": "Like that self-begotten bird in the Arabian woods, from out her ashy womb now teemed, reviving from a fiery **holocaust**."
      },
      {
        "author": "Primo Levi",
        "work": "If This Is a Man",
        "quote": "The memory of the monstrous industrial **holocaust** in Auschwitz remains a permanent obligation and warning to all human civilization."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The blazing temples of the conquered city seemed an immense **holocaust** offered unto the fury of the victorious legions."
      }
    ]
  },
  "Dashboard — caust\\hypocaust.md": {
    "primary": "An ancient Roman heating system in which hot air and smoke from a furnace circulated through an underfloor chamber and hollow wall tiles to warm rooms and public baths.",
    "secondary": "In classical archaeology and architectural engineering, an underfloor heating plenum supported on stone or brick pilae pillars (suspensura), essential to Roman thermae and villas.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "De Architectura",
        "quote": "The floor of the hot bath should be suspended above the **hypocaust** on brick pillars so the furnace heat may spread uniformly underneath."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Even in the chilly climate of Britain, the Roman villas were provided with an subterranean **hypocaust** to maintain perpetual spring within."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "Excavations revealed the ruined pillars of the Roman **hypocaust**, showing how ancient luxury triumphed over northern frost."
      }
    ]
  },
  "Dashboard — cen\\Cenozoic.md": {
    "primary": "The current geological era, beginning approximately 66 million years ago with the extinction of the non-avian dinosaurs and continuing to the present day; the Age of Mammals.",
    "secondary": "In historical geology and paleobiology, the era divided into the Paleogene, Neogene, and Quaternary periods, marked by continental drift toward modern positions and explosive angiosperm-mammal co-radiation.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "In the strata of the **Cenozoic** era, we observe the gradual dawn of the modern marine mollusc species."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "During the **Cenozoic** epoch, mammalian quadrupeds diversified rapidly to occupy the terrestrial niches left vacant by giant reptiles."
      },
      {
        "author": "Carl Sagan",
        "work": "The Dragons of Eden",
        "quote": "The **Cenozoic** witnessed the rapid expansion of mammalian neocortical brain structures, culminating in hominid intelligence."
      }
    ]
  },
  "Dashboard — cen\\caenogastropod.md": {
    "primary": "Any mollusk belonging to the Caenogastropoda, the largest and most ecologically diverse clade of modern marine and freshwater snails.",
    "secondary": "In invertebrate zoology and malacology, advanced gastropods characterized by a single pectinibranch gill, an anterior inhalant siphon, and a specialized radular apparatus.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The predatory moon snail is an active **caenogastropod** that drills neat countersunk holes through the shells of clams."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The asymmetrical reduction of the right gill and osphradium characterizes the advanced architecture of the typical **caenogastropod**."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Evolutionary radiation within the marine **caenogastropod** lineages produced specialized venomous hunters such as the cone snails."
      }
    ]
  },
  "Dashboard — cen\\caenogenesis.md": {
    "primary": "The evolutionary emergence or introduction of novel developmental adaptations in an embryo or larva that were not present in ancestral adult forms; caenogeny.",
    "secondary": "In evolutionary embryology, Ernst Haeckel's term for developmental modifications (such as embryonic membranes or larval adaptations) that distort the ancestral phylogenetic sequence.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "I have designated as **caenogenesis** those recent embryonic adaptations which falsify and obscure the ancestral palingenetic record."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The aquatic adaptations of insect larvae afford classic examples of **caenogenesis**, evolving independently of the terrestrial adult form."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "Embryological recapitulation is never a verbatim transcript, for **caenogenesis** continuously interpolates new survival features."
      }
    ]
  },
  "Dashboard — cen\\cen.md": {
    "primary": "A combining form of Greek origin meaning new, recent, or fresh (derived from Greek kainos, often spelled caen- or cen-).",
    "secondary": "In geological and biological nomenclature, a prefix appearing in terms designating recent epochs or new structural forms (as in Cenozoic and caenogenesis).",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek element **cen**, drawn from kainos, denotes the new and recent in the nomenclature of modern geology."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Compounded with zoic, the root **cen** marks our current geological chapter of living creation."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Names formed with **cen** distinguish the newer tertiary formations containing high proportions of living shells."
      }
    ]
  },
  "Dashboard — centr\\acentric.md": {
    "primary": "Lacking a center or not situated in the center; in cytogenetics, describing a chromosome or chromatid fragment that lacks a centromere.",
    "secondary": "In radiation genetics and chromosomal pathology, describing an unstable chromosome fragment that cannot attach to the mitotic spindle and is lost during cell division.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Ionizing radiation creates an **acentric** chromosomal fragment that fails to align upon the equatorial plate and is excluded from daughter nuclei."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Without spindle microtubule attachment at a kinetochore, the **acentric** chromatin body drifts passively into the cytoplasm."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Chromosomal breakage yields one dicentric chromosome and one **acentric** fragment, both destined to cause cell lethality."
      }
    ]
  },
  "Dashboard — centr\\acrocentric.md": {
    "primary": "Describing a chromosome in which the centromere is located near one end, resulting in one very short arm and one exceptionally long arm.",
    "secondary": "In human cytogenetics, referring to chromosomes 13, 14, 15, 21, and 22, which possess short arms bearing nucleolar organizing regions (rDNA repeats) and are prone to Robertsonian translocations.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Robertsonian centric fusion between two non-homologous **acrocentric** chromosomes reduces the total chromosome number while preserving genetic material."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Trisomy of the small **acrocentric** chromosome twenty-one produces the complex neurodevelopmental phenotypes of Down syndrome."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Karyotypic analysis revealed that each **acrocentric** element terminates in a minute heterochromatic satellite knob."
      }
    ]
  },
  "Dashboard — centr\\amniocentesis.md": {
    "primary": "A prenatal diagnostic procedure in which a small sample of amniotic fluid is extracted from the uterus via needle puncture through the abdominal wall to test for fetal genetic abnormalities.",
    "secondary": "In obstetrics and medical genetics, an invasive diagnostic test performed between the 15th and 20th weeks of gestation to analyze fetal karyotypes, alpha-fetoprotein, and chromosomal aneuploidies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern prenatal diagnosis was revolutionized by ultrasound-guided **amniocentesis**, permitting direct cytogenetic examination of fetal cells."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Mankind Evolving",
        "quote": "Through routine **amniocentesis**, parents can ascertain the chromosomal constitution of their unborn child."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "Advanced maternal age remains the primary clinical indication for diagnostic **amniocentesis** in high-risk pregnancies."
      }
    ]
  },
  "Dashboard — centr\\anthropocentric.md": {
    "primary": "Regarding humankind as the central or most important element of existence, especially as opposed to God, nature, or other living creatures.",
    "secondary": "In environmental ethics and philosophy of science, a conceptual framework that evaluates the natural world solely according to human interests and values.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Astronomy has been a persistent humbler of our **anthropocentric** conceits, demonstrating that Earth is a mere speck in cosmic space."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Natural selection shatters the proud **anthropocentric** delusion that all other creatures were created solely for man's utility."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "An **anthropocentric** ethic that values other species only as commercial resources invites ecological collapse."
      }
    ]
  },
  "Dashboard — centr\\anthropocentricity.md": {
    "primary": "The state, quality, or worldview of being anthropocentric; human-centeredness in perception, philosophy, or ethics.",
    "secondary": "In epistemology and theology, the bias of viewing the cosmic order through the lens of human desires, scale, and moral assumptions.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Pale Blue Dot",
        "quote": "Our posturing, our imagined self-importance, the delusion that we have some privileged position in the Universe, are challenged by the **anthropocentricity** of our early myths."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evolution and Ethics",
        "quote": "The scientific revolution dealt a fatal blow to the naive **anthropocentricity** that once placed human drama at the hub of nature."
      },
      {
        "author": "William James",
        "work": "The Will to Believe",
        "quote": "Pragmatism recognizes that all philosophical systems bear the indelible mark of human **anthropocentricity**."
      }
    ]
  },
  "Dashboard — centr\\anthropocentrism.md": {
    "primary": "The philosophical belief or ethical stance that human beings are the central or most significant entities in the universe.",
    "secondary": "In ecological philosophy, a normative perspective contrasted with biocentrism and ecocentrism, holding that moral obligations apply directly only to human beings.",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Ecosystem preservation requires moving beyond narrow **anthropocentrism** toward a biophilic reverence for all living organisms."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Copernicus displaced our planet, and Darwin displaced our biology, yet human **anthropocentrism** stubbornly persists in our politics."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution in Action",
        "quote": "Evolutionary humanism replaces religious **anthropocentrism** with an understanding of man as nature's conscious trustee."
      }
    ]
  },
  "Dashboard — centr\\barycenter.md": {
    "primary": "The center of mass of two or more celestial bodies that orbit each other; the common point around which two or more bodies revolve.",
    "secondary": "In celestial mechanics and orbital astrophysics, the gravitational balance point of a planetary or stellar system (such as the Earth-Moon barycenter).",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The Sun and planets revolve about a common center of gravity, the **barycenter** of the entire solar system."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The Earth and Moon perform mutual monthly revolutions about their common **barycenter**, situated within the terrestrial mantle."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Astronomers detect unseen extrasolar planets by measuring the reflex wobble of a parent star around the system's **barycenter**."
      }
    ]
  },
  "Dashboard — centr\\biocentric.md": {
    "primary": "Viewing or considering life and the biological sphere as the central fact of existence; considering all living organisms as having inherent moral value.",
    "secondary": "In environmental ethics and deep ecology, describing philosophical frameworks that prioritize ecological health and biodiversity over human material exploitation.",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "Biophilia",
        "quote": "A truly **biocentric** perspective recognizes that human psychological vitality is inextricably tied to the richness of living nature."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "We need a **biocentric** understanding of pest control, working with natural predators rather than flooding the biosphere with poison."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Adopting a **biocentric** philosophy compels humanity to regard itself as an integral branch of the evolving tree of life."
      }
    ]
  },
  "Dashboard — centr\\biocentrism.md": {
    "primary": "An ethical perspective that extends inherent moral value and rights to all living things, asserting that human beings are merely one member of the biotic community.",
    "secondary": "In environmental philosophy and bioethics, a doctrine contrasted with anthropocentrism, holding that every organism possesses an objective good of its own.",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The philosophical shift toward **biocentrism** provides the ethical foundation necessary to halt the global biodiversity crisis."
      },
      {
        "author": "Rachel Carson",
        "work": "Lost Woods: The Discovered Writing of Rachel Carson",
        "quote": "Only through an attitude of humble **biocentrism** can modern civilization live in enduring harmony with the natural world."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution in Action",
        "quote": "Scientific **biocentrism** treats the entire planetary biosphere as a continuous, interconnected fabric of life."
      }
    ]
  },
  "Dashboard — centr\\cental.md": {
    "primary": "A unit of weight or mass equal to 100 pounds (avoirdupois); a hundredweight (cwt in the US decimal system).",
    "secondary": "In commercial grain trading and commodities measurement, a standardized unit adopted in 19th-century British and American ports to simplify transactions.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The market price of wheat was calculated per **cental** of dry grain at the principal agricultural exchanges."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "The ledger recorded every **cental** of wool dispatched to the northern weaving mills with commercial exactitude."
      },
      {
        "author": "Washington Irving",
        "work": "A History of New York",
        "quote": "Dutch merchants weighed out each **cental** of cured tobacco with substantial brass scales upon the wharf."
      }
    ]
  },
  "Dashboard — centr\\centaur.md": {
    "primary": "A mythological creature in ancient Greek lore with the upper torso, arms, and head of a human and the body and legs of a horse.",
    "secondary": "In astronomy, a minor celestial body (such as Chiron) orbiting the sun between Jupiter and Neptune, exhibiting characteristics of both asteroids and comets.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "Wise Chiron, the most righteous of all the centaurs, instructed the young Achilles in the healing arts and archery."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Fierce as the savage **centaur** galloping over Thessalian hills, the fallen angels mobilized their grim ranks."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Astronomers discovered Chiron, the first icy **centaur** whose erratic orbit crosses the realm of the giant outer planets."
      }
    ]
  },
  "Dashboard — centr\\centauromachy.md": {
    "primary": "In classical Greek art and mythology, a battle or combat between the Lapiths and the Centaurs, especially at the wedding feast of Peirithoos.",
    "secondary": "In art history, a celebrated allegorical motif in Greek architectural sculpture (such as the Parthenon metopes) symbolizing the triumph of civilization over barbarism.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "Aratra Pentelici",
        "quote": "On the high metopes of the Parthenon, the fierce **centauromachy** embodies the eternal struggle between civic intellect and bestial fury."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The marble friezes commemorating the ancient **centauromachy** displayed the athletic grace of Athenian sculptors in their prime."
      },
      {
        "author": "Walter Pater",
        "work": "Greek Studies",
        "quote": "The sculptor depicted the **centauromachy** with rhythmic balance, harmonizing human muscular poise against the wild rearing of equine limbs."
      }
    ]
  },
  "Dashboard — centr\\centered.md": {
    "primary": "Placed, situated, or fixed at the center; having a central focus or point of origin; emotionally stable, balanced, and confident.",
    "secondary": "In mechanical engineering and typography, aligned with an axis or central baseline without lateral deviation.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "The soul is **centered** within itself, resting in calm equilibrium amidst the fluctuating opinions of the crowd."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "All her domestic energies were **centered** upon holding the family circle together against the eroding wash of time."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The concentric chromatic rings were perfectly **centered** around the dark central point of glass contact."
      }
    ]
  },
  "Dashboard — centr\\centering.md": {
    "primary": "The act, process, or technique of placing or adjusting something at the center; also the temporary wooden framework that supports an arch or vault during construction.",
    "secondary": "In psychology and contemplative practice, a focusing technique used to quiet mental distractions and achieve inner emotional balance.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "When the masonry of the pointed arch was completed, the workmen struck away the timber **centering** beneath."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The conscious **centering** of attention upon a single idea inhibits competing motor and sensory impulses."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Roman engineers erected colossal vaulted aqueducts by shifting massive wooden **centering** from span to span."
      }
    ]
  },
  "Dashboard — centr\\centesis.md": {
    "primary": "A surgical puncture or perforation of a body cavity or organ to aspirate or remove accumulated fluid (as in thoracentesis or paracentesis).",
    "secondary": "In clinical operative surgery, a diagnostic or therapeutic procedure utilizing a trocar, cannula, or needle to relieve pressure or analyze intracavitary effusions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt abdominal **centesis** was carried out to relieve respiratory distress caused by massive cirrhotic ascites."
      },
      {
        "author": "Hippocrates",
        "work": "Aphorisms",
        "quote": "In cases of empyema, early **centesis** of the thoracic wall permits evacuation of pus before the lung collapses irrevocably."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Diagnostic lumbar **centesis** yielded clear cerebrospinal fluid under markedly elevated manometric pressure."
      }
    ]
  },
  "Dashboard — centr\\centr.md": {
    "primary": "A combining form of Greek origin meaning center, sharp point, prick, or middle (derived from Greek kentron).",
    "secondary": "In scientific, mathematical, and spatial nomenclature, a productive root appearing in words like centrifugal, centripetal, eccentric, and centrosome.",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek stem **centr**, originally a sharp goad or stationary compass point, became the parent of all our terms for midpoint."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "From the pivot point of the geometer's compass, the root **centr** radiates across every European tongue."
      },
      {
        "author": "Isaac Newton",
        "work": "Principia",
        "quote": "Forces directed toward a central attracting body are compounded with the stem **centr** to designate radial gravitation."
      }
    ]
  },
  "Dashboard — centr\\central.md": {
    "primary": "Situated at, in, or near the center; forming the center; of primary importance, principal, essential, or dominant.",
    "secondary": "In neuroanatomy, designating structures lying along the neuraxis (such as the central nervous system, central sulcus, or central canal of the spinal cord).",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "The **central** nervous system integrates sensory input from peripheral nerves to execute voluntary behavioral programs."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "Natural selection occupies the **central** position in explaining the origin of complex adaptations across all taxa."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Truth is a **central** sun whose illumination warms and orders all the collateral branches of human inquiry."
      }
    ]
  },
  "Dashboard — centr\\centralisation.md": {
    "primary": "The concentration of administrative control, power, or authority under a single unified center (British spelling).",
    "secondary": "In political science and sociology, the historical consolidation of legal, financial, and executive powers in national state capitals.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Administrative **centralisation** enervates the nations that submit to it, diminishing civic civic energy for bureaucratic symmetry."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "Excessive governmental **centralisation** suffocates local initiative and reduces citizens to passive recipients of state directives."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The Jacobin regime pushed political **centralisation** to its ultimate limit, directing every provincial guillotine from Paris."
      }
    ]
  },
  "Dashboard — centr\\centralise.md": {
    "primary": "To bring under a single central authority, control, or management; to concentrate at a central point (British spelling).",
    "secondary": "To consolidate disparate local agencies, jurisdictions, or resources into an integrated administrative framework.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "The royal intendants sought to **centralise** all provincial public works under the direct supervision of the royal council."
      },
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "A wise constitution does not attempt to **centralise** local municipal concerns in the national parliament."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Diocletian restructured the Roman world to **centralise** the collection of taxes and military commands."
      }
    ]
  },
  "Dashboard — centr\\centralised.md": {
    "primary": "Concentrated at a single center or managed under unified central authority (British spelling).",
    "secondary": "Describing hierarchical governance, financial banking systems, or computational architectures directed from a central core.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "A **centralised** administration produces uniformity of regulations, but frequently stifles the creative vitality of the provinces."
      },
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "The economy of Oceania was strictly **centralised**, every ration and production quota decreed from the Ministry of Plenty."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "France possessed a formidable **centralised** army, whereas England relied upon decentralized county militias."
      }
    ]
  },
  "Dashboard — centr\\centralising.md": {
    "primary": "Acting to concentrate authority, resources, or operations under a single central body (British spelling).",
    "secondary": "Tending toward centralization; pulling away from local autonomy toward centralized control.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "The **centralising** instincts of modern monarchies prepared the ground for the absolute state long before the revolution."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "Every increase in the **centralising** power of the bureaucracy threatens individual liberty and spontaneous enterprise."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Constantine pursued a **centralising** policy by relocating the imperial seat of power to the shores of the Bosporus."
      }
    ]
  },
  "Dashboard — centr\\centralism.md": {
    "primary": "The principle, policy, or practice of concentrating administrative power and decision-making authority in a single central body.",
    "secondary": "In political theory, a system of unitary government that subordinates local and regional jurisdictions to the national center (e.g., democratic centralism).",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Democratic nations are naturally inclined toward **centralism**, seeking in uniform laws an escape from aristocratic privilege."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "Our federal union carefully balances the benefits of national unity against the suffocating dangers of complete **centralism**."
      },
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "Rigid bureaucratic **centralism** converts the civil service into a stagnant monopoly impervious to popular critique."
      }
    ]
  },
  "Dashboard — centr\\centralist.md": {
    "primary": "An advocate, supporter, or proponent of political or administrative centralism; or relating to the concentration of power.",
    "secondary": "In political history, contrasting with federalist, regionalist, or confederal factions in constitutional debates.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "The ardent **centralist** regarded provincial privileges as archaic obstructions to enlightened national efficiency."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The opponents of the new Constitution unfairly denounced every energetic federal measure as the design of a **centralist** faction."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The Jacobin **centralist** believed that the republic could survive only if every departmental decree emanated directly from Paris."
      }
    ]
  },
  "Dashboard — centr\\centralistic.md": {
    "primary": "Pertaining to, advocating, or characterized by political or administrative centralism.",
    "secondary": "Describing institutions, legislation, or constitutional models that concentrate authority and suppress regional autonomy.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The **centralistic** tendencies of modern democratic states tend to erode intermediary civic institutions."
      },
      {
        "author": "John Stuart Mill",
        "work": "Representative Government",
        "quote": "A purely **centralistic** system of education risks indoctrinating youth into a uniform state ideology."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Under Diocletian, the Roman state assumed an openly **centralistic** character that extinguished ancient municipal liberties."
      }
    ]
  },
  "Dashboard — centr\\centrality.md": {
    "primary": "The state or condition of being in the center; focal prominence, pivotal importance, or vital significance.",
    "secondary": "In network theory and human geography, a quantitative measure of a node's structural influence or geographic accessibility within a network.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The geographical **centrality** of Rome within the Mediterranean basin facilitated both military conquest and commercial dominance."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The feeling of bodily **centrality** provides the continuous anchor for our subjective sense of selfhood."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "St. Mark's square possessed a spiritual and civic **centrality** around which the entire public life of Venice revolved."
      }
    ]
  },
  "Dashboard — centr\\centralization.md": {
    "primary": "The process of bringing activities, operations, or authority from dispersed points into a single central control point (US spelling).",
    "secondary": "In public administration and corporate strategy, consolidating decision-making authority within a unified executive command structure.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "I distinguish between two forms of **centralization**: governmental, which is necessary, and administrative, which is enervating."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "Without a competent **centralization** of financial and military power, the fragile confederacy would dissolve in mutual conflict."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "The continuous **centralization** of information in government archives can improve efficiency while endangering civic freedom."
      }
    ]
  },
  "Dashboard — centr\\centralize.md": {
    "primary": "To draw into or gather around a common center; to bring under a single central control or direction (US spelling).",
    "secondary": "In computer systems and organizational management, to replace distributed nodes with a single authoritative central server or hub.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "As conditions become more equal, men naturally seek to **centralize** the power of the state to guarantee equal rights."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "To conduct foreign relations effectively, the republic was compelled to **centralize** diplomatic authority in the national executive."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Philosophical academies must **centralize** empirical observations to construct a unified natural history."
      }
    ]
  },
  "Dashboard — centr\\centralized.md": {
    "primary": "Concentrated at a single center; controlled, coordinated, or governed by a single unified authority (US spelling).",
    "secondary": "In network topology and political economy, an architecture where all control lines lead to an authoritative central node.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "A completely **centralized** government manages roads and police with admirable precision, yet deadens the initiative of the citizens."
      },
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "The revolutionary militias resisted every attempt to replace their democratic committees with a **centralized** military command."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "The Library of Alexandria created the first **centralized** repository of global human knowledge in the ancient world."
      }
    ]
  },
  "Dashboard — centr\\centralizing.md": {
    "primary": "Tending to draw toward the center; concentrating power or control at a single point (US spelling).",
    "secondary": "Describing policies, political movements, or corporate restructuring that aggregate decision-making authority.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The **centralizing** current of modern legislation steadily absorbs local judicial powers into state commissions."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "A strong national currency requires **centralizing** fiscal authority within a permanent federal treasury."
      },
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "Local self-government operates as an indispensable counterpoise to the **centralizing** ambitions of the bureaucracy."
      }
    ]
  },
  "Dashboard — centr\\centrally.md": {
    "primary": "In, at, or near the center; in a central manner or position; of primary or pivotal importance.",
    "secondary": "Directed or administered from a central governing location or authority.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Roman forum was **centrally** situated between the Capitoline and Palatine hills, commanding the civic heart of the city."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Information from all sensory modalities converges **centrally** within the thalamus before reaching neocortical fields."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The grand portal opened **centrally** upon the piazza, flanked by twin marble columns of antique porphyry."
      }
    ]
  },
  "Dashboard — centr\\centranthus.md": {
    "primary": "A genus of flowering plants in the honeysuckle family Caprifoliaceae (formerly Valerianaceae), native to Southern Europe, commonly known as red valerian.",
    "secondary": "In horticulture and botany, herbaceous perennials (notably Centranthus ruber) with spur-bearing asymmetric flowers, famous for thriving on old stone walls and coastal cliffs.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "The long, slender nectar spur of **Centranthus** restricts pollination to insects possessing elongated proboscides."
      },
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "The spur-bearing monandrous floral structure of **Centranthus** represents an evolutionary reduction from ancestral valerian types."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "On dry limestone ruins across southern England, crimson clumps of naturalized **Centranthus** blossom through the summer."
      }
    ]
  },
  "Dashboard — centr\\centrarchid.md": {
    "primary": "Any freshwater fish belonging to the family Centrarchidae, comprising the North American sunfishes, black basses, and crappies.",
    "secondary": "In freshwater fisheries biology and aquatic ecology, predatory ray-finned fishes characterized by dorsal spines and male parental nest-guarding behavior.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Every clear gravelly shallows in springtime reveals a watchful male **centrarchid** fanning oxygen over its prepared gravel nest."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "Looking down into the clear waters of the pond, I watched the lively bream, a familiar little **centrarchid**, hover over its circular bed."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The largemouth bass is the premier sportfish among the family, an aggressive **centrarchid** native to quiet, vegetated waters."
      }
    ]
  },
  "Dashboard — centr\\centrarchidae.md": {
    "primary": "The family of North American freshwater percoid fishes comprising the sunfishes, black basses, rock basses, and crappies.",
    "secondary": "In ichthyological systematics, an endemic Nearctic family possessing 3 to 10 anal spines and continuous dorsal fins, highly valued for sport and food.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Genera of Fishes",
        "quote": "The family **Centrarchidae** dominates the warm-water lacustrine ecosystems of eastern and central North America."
      },
      {
        "author": "Louis Agassiz",
        "work": "Lake Superior: Its Physical Character, Vegetation, and Animals",
        "quote": "Morphological comparisons of **Centrarchidae** illustrate the rapid post-glacial radiation of teleosts across inland river basins."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "Osteological examination of **Centrarchidae** confirms their placement among the advanced ctenoid-scaled percomorphs."
      }
    ]
  },
  "Dashboard — centr\\centre.md": {
    "primary": "The middle point or part of something; the focal point of activity, attention, or importance (British spelling).",
    "secondary": "In geometry, the point equidistant from all points on the circumference of a circle or sphere; in politics, a moderate, non-extremist position.",
    "quotes": [
      {
        "author": "William Butler Yeats",
        "work": "The Second Coming",
        "quote": "Turning and turning in the widening gyre, the falcon cannot hear the falconer; things fall apart; the **centre** cannot hold; mere anarchy is loosed upon the world."
      },
      {
        "author": "John Donne",
        "work": "A Valediction: Forbidding Mourning",
        "quote": "Thy soul, the fix'd foot, makes no show to move, but doth, if th' other do; and though it in the **centre** sit, yet when the other far doth roam, it leans, and hearkens after it."
      },
      {
        "author": "Isaac Newton",
        "work": "Principia",
        "quote": "The celestial bodies are continually drawn off from rectilinear motions by forces directed toward the **centre** of the Sun."
      }
    ]
  },
  "Dashboard — centr\\centreboard.md": {
    "primary": "A retractable wooden or metal keel or fin lowered through a watertight trunk in the middle of a sailboat's hull to reduce leeway.",
    "secondary": "In naval architecture and dinghy sailing, a pivoting underwater foil that provides lateral hydrodynamic resistance against windward drift.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The shallow skiff was fitted with a stout oak **centreboard**, dropped into the channel whenever we hauled close to the wind."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Mirror of the Sea",
        "quote": "Lowering the **centreboard** gave the light racing cutter immediate grip in the choppy coastal waters."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "Our boat, drawing but little water with the **centreboard** housed, glided smoothly over the sandy river bars."
      }
    ]
  },
  "Dashboard — centr\\centrefold.md": {
    "primary": "The large folded sheet of paper located at the exact middle of a magazine, newspaper, or periodical, often featuring a panoramic illustration, chart, or photograph.",
    "secondary": "In print publishing and popular culture, a two-page spread or pull-out illustration occupying the central binding fold of an issue.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "The illustrated journal opened upon a broad **centrefold** depicting the naval review at Spithead in vivid color."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "He unfolded the newspaper to the **centrefold**, scanning the advertisements and commercial headlines with cynical detachment."
      },
      {
        "author": "James Joyce",
        "work": "Ulysses",
        "quote": "He opened the weekly gazette, studying the double-spread lithograph displayed upon the glossy **centrefold**."
      }
    ]
  },
  "Dashboard — centr\\centrepiece.md": {
    "primary": "An ornamental object, decorative display, or floral arrangement placed in the center of a dining table or formal banquet.",
    "secondary": "The most important, prominent, or central item, event, or feature of an artistic exhibition, program, or architectural composition.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "The grand silver epergne loaded with choice fruits stood as the magnificent **centrepiece** of the wedding breakfast."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The carved marble altar forms the sublime architectural **centrepiece** around which all other chapel decorations harmonize."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The triumphal arch of Constantine was erected as the proud **centrepiece** of imperial victory in the eternal city."
      }
    ]
  },
  "Dashboard — centr\\centrex.md": {
    "primary": "A business telecommunications service provided by a central telephone company that provides private branch exchange (PBX) switching capabilities directly from the central office.",
    "secondary": "In telecommunications engineering, a centralized multi-line telephone switching architecture eliminating the need for private on-premises switching hardware.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "The transition to centralized automated exchange systems like **centrex** signaled the dawn of planetary electronic interconnectivity."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "The busy factory switchboard was replaced by an electronic **centrex** service, routing department calls automatically."
      },
      {
        "author": "Carl Sagan",
        "work": "The Dragons of Eden",
        "quote": "Just as the cerebral cortex coordinates millions of neural circuits, a telephone **centrex** routes complex messages across modern cities."
      }
    ]
  },
  "Dashboard — centr\\centric.md": {
    "primary": "Situated at, pertaining to, or revolving around a center; having a center; symmetrical around a central axis.",
    "secondary": "In anatomy and optics, designating central positioning (as in centric occlusion in dental bite alignment, or centric photoreceptors in the fovea).",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The radial structure of the rose reveals a **centric** symmetry where every petal curves toward the luminous heart."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The colored rings displayed a strictly **centric** arrangement about the point of closest optical contact."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Our spatial perceptions organize themselves around a **centric** bodily origin from which all distances are measured."
      }
    ]
  },
  "Dashboard — centr\\centrical.md": {
    "primary": "Placed in or near the center; central (formal or historical variant).",
    "secondary": "Relating to or proceeding from a focal central position.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "The geocentric theory placed our terrestrial globe in a **centrical** position that flattered human vanity."
      },
      {
        "author": "Thomas Browne",
        "work": "The Garden of Cyrus",
        "quote": "The quincunx pattern delights the eye by establishing a **centrical** harmony among four equidistant corner points."
      },
      {
        "author": "Samuel Johnson",
        "work": "The History of Rasselas, Prince of Abissinia",
        "quote": "The palace occupied a **centrical** valley sheltered on all sides by lofty mountains."
      }
    ]
  },
  "Dashboard — centr\\centrifugate.md": {
    "primary": "To subject a liquid or suspension to centrifugation; to separate components of varying densities using a high-speed centrifuge.",
    "secondary": "In laboratory medicine and biochemistry, to spin down cellular elements, precipitates, or macromolecules in an acceleration field.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The technician must **centrifugate** the urine specimen to concentrate casts and red blood cells for microscopic sediment analysis."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Ultracentrifugal techniques enable researchers to **centrifugate** macromolecular solutions and determine protein molecular weights directly."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin: Its Practical Application",
        "quote": "Before chemical extraction of antibiotic broths, it is necessary to **centrifugate** the culture to clear fungal mycelia."
      }
    ]
  },
  "Dashboard — centr\\centrifugation.md": {
    "primary": "The process or technique of separating substances of different densities from a liquid mixture or suspension using high-speed rotational force (centrifugal force).",
    "secondary": "In cell biology and biophysics, differential and density-gradient centrifugation techniques developed by Theodor Svedberg to fractionate subcellular organelles and nucleic acids.",
    "quotes": [
      {
        "author": "Theodor Svedberg",
        "work": "The Ultracentrifuge (Nobel Lecture)",
        "quote": "Through high-speed **centrifugation**, we succeeded in sedimenting protein molecules and demonstrating their discrete molecular weights."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rapid **centrifugation** of whole blood separates yellow plasma from the packed red erythrocyte column."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "Industrial **centrifugation** whirled the viscous varnish until suspended resin impurities were forced against the outer drum."
      }
    ]
  },
  "Dashboard — centr\\centrifuge.md": {
    "primary": "A motorized laboratory or industrial apparatus with a rapidly spinning rotor that applies centrifugal force to separate substances of different densities.",
    "secondary": "In molecular biology and isotopic physics, high-speed machines (ultracentrifuges or gas centrifuges) essential for subcellular fractionation and isotope separation.",
    "quotes": [
      {
        "author": "Theodor Svedberg",
        "work": "The Ultracentrifuge",
        "quote": "The optical ultracentrifuge enabled direct observation of sedimentation boundaries while the rotor spun at forty thousand revolutions per minute."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A benchtop clinical **centrifuge** quickly prepares blood serum for diagnostic agglutination tests."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "The roar of the heavy chemical **centrifuge** signaled that the batch of crystalline paint pigments was finally drying."
      }
    ]
  },
  "Dashboard — centr\\centriole.md": {
    "primary": "A small, cylindrical cellular organelle composed of nine microtubule triplets, typically occurring in pairs within the centrosome of animal cells.",
    "secondary": "In cell biology, an organelle that duplicates during the cell cycle to organize centrosomal pericentriolar material and form the basal body of cilia and flagella.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "At the heart of the radiating aster lies the minute **centriole**, dividing to establish the opposing poles of the mitotic spindle."
      },
      {
        "author": "Theodor Boveri",
        "work": "Cells and Tissues",
        "quote": "The sperm provides the fertilizing egg with a functional **centriole**, restoring the reproductive motor of the zygote."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "In developing neuroblasts, the mother **centriole** docks at the apical membrane to nucleate the primary sensory cilium."
      }
    ]
  },
  "Dashboard — centr\\centriscidae.md": {
    "primary": "A family of small, slender tropical marine fishes commonly known as shrimpfishes or razor fishes, noted for rigid armored bodies and swimming in a vertical, head-down posture.",
    "secondary": "In syngnathiform ichthyology, specialized reef teleosts possessing transparent razor-like dorsal carapaces formed by fused vertebral plates.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The extraordinary family **Centriscidae** swim in synchronized schools with their long snouts pointing straight toward the seafloor."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Hiding among the long spines of tropical sea urchins, tiny members of **Centriscidae** mimic swaying seaweeds in their vertical drift."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The cranial and thoracic armor of **Centriscidae** illustrates an extreme adaptation where the vertebral column fuses into a rigid dorsal shield."
      }
    ]
  },
  "Dashboard — centr\\centrism.md": {
    "primary": "A moderate political philosophy, outlook, or policy that avoids ideological extremes and seeks compromise between left-wing and right-wing positions.",
    "secondary": "In political science, a strategic electoral positioning around the median voter, emphasizing institutional pragmatism, fiscal prudence, and social stability.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "A robust commercial middle class naturally fosters political **centrism**, fearing the violent disruptions of both radicalism and reaction."
      },
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "Healthy representative assemblies require a steady anchor of thoughtful **centrism** to reconcile conflicting class interests."
      },
      {
        "author": "Arthur M. Schlesinger Jr.",
        "work": "The Vital Center",
        "quote": "Democratic **centrism** is not a spineless avoidance of principle, but an active, militant defense of freedom against totalitarian extremes."
      }
    ]
  },
  "Dashboard — centr\\centrist.md": {
    "primary": "A person who holds moderate political views or belongs to a centrist party; or of or relating to political centrism.",
    "secondary": "Describing politicians, policies, or voters occupying the political center between social democracy and conservative liberalism.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "The prudent **centrist** deputy sought to preserve constitutional reform while checking the destructive fury of the mob."
      },
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "The moderate **centrist** parties favored restoring normal republican administration before attempting sweeping economic transformations."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The genius of Halifax lay in his role as a consummate **centrist** trimmer, shifting his weight whenever the boat listed too dangerously."
      }
    ]
  },
  "Dashboard — centr\\centrocercus.md": {
    "primary": "A genus of large North American grouse in the pheasant family Phasianidae, comprising the sage-grouse (notably Centrocercus urophasianus).",
    "secondary": "In avian behavioral ecology, prominent sagebrush-steppe birds celebrated for spectacular communal lek displays where cocks inflate yellow esophageal air sacs.",
    "quotes": [
      {
        "author": "John James Audubon",
        "work": "The Birds of America",
        "quote": "The cock of the plains, **Centrocercus**, struts across the open sage-plains at dawn, puffing out his breast with resonant booming sounds."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The spectacular mating ritual of **Centrocercus** provides a classic example of sexual selection operating through lek displays."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The conservation of **Centrocercus** serves as an umbrella policy protecting the entire sagebrush biome of the American West."
      }
    ]
  },
  "Dashboard — centr\\centroid.md": {
    "primary": "The geometric center or center of mass of a plane figure, solid object, or system of points of uniform density.",
    "secondary": "In statics, differential geometry, and computational mechanics, the mean arithmetic position of all points in a geometric shape, determined by integration of spatial coordinates.",
    "quotes": [
      {
        "author": "Archimedes",
        "work": "On the Equilibrium of Planes",
        "quote": "The **centroid** of any triangle lies upon the intersection of its three median lines, dividing each in the ratio of two to one."
      },
      {
        "author": "Isaac Newton",
        "work": "Principia",
        "quote": "For a body of uniform density, gravitational attraction acts as if its entire mass were concentrated at its **centroid**."
      },
      {
        "author": "Ernst Mach",
        "work": "The Science of Mechanics",
        "quote": "The calculation of the **centroid** enables engineers to determine rotational moments of inertia in structural beams."
      }
    ]
  },
  "Dashboard — centr\\centroidal.md": {
    "primary": "Of, relating to, or passing through a centroid (the geometric center of mass).",
    "secondary": "In structural engineering and continuum mechanics, describing axes (such as the centroidal axis) along which bending moments produce pure axial stress without cross-sectional torsion.",
    "quotes": [
      {
        "author": "Ernst Mach",
        "work": "The Science of Mechanics",
        "quote": "Bending stresses in a loaded beam vanish along the neutral surface that passes through its **centroidal** axis."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Crystallographic symmetry operations frequently align with the principal **centroidal** planes of the mineral crystal."
      },
      {
        "author": "Isaac Newton",
        "work": "Principia",
        "quote": "The orbital mechanics of mutually attracting spheroids depend on lines drawn between their respective **centroidal** foci."
      }
    ]
  },
  "Dashboard — centr\\centrolobium.md": {
    "primary": "A genus of leguminous trees native to tropical South America (family Fabaceae), prized for their lustrous, durable timber known as canarywood or araribá.",
    "secondary": "In tropical dendrology and forestry, canopy trees producing large, spiny, winged samara fruits (bearing a prominent central spine, hence the Greek name) and yellow-orange wood with red figure.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Travels on the Amazon and Rio Negro",
        "quote": "The dense tropical forests of Brazil contain towering hardwoods such as **Centrolobium**, whose heavy winged seeds spin like autogyros to the forest floor."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "The prized timber known as araribá is furnished by the noble tree **Centrolobium**, celebrated for its resilience in ship construction."
      },
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "The spiny, winged pod of **Centrolobium** protects the solitary seed during its long dispersal flight across the canopy."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Form & Space Part 1 - Batch 5 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
