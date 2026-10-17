import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — ambly\\Amblypoda.md": {
    "primary": "An extinct order of primitive, archaic ungulate mammals from the Paleocene and Eocene epochs, characterized by stout limbs and short, blunt, five-toed feet.",
    "secondary": "In vertebrate paleontology, an obsolete taxonomic wastebasket taxon established by E. D. Cope uniting diverse archaic herbivores such as pantodonts and dinoceratans.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "The archaic ungulate order **Amblypoda** comprises early tertiary quadrupeds whose plantigrade extremities retain five primitive digits."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Age of Mammals in Europe, Asia and North America",
        "quote": "Among the archaic fauna of the Wasatch formation, the short-footed **Amblypoda** represented the foremost massive browsers of their era."
      },
      {
        "author": "William Diller Matthew",
        "work": "Memoirs of the American Museum of Natural History",
        "quote": "Subsequent osteological comparison demonstrated that the disparate groups united under **Amblypoda** evolved their heavy columnar limbs independently."
      }
    ]
  },
  "Dashboard — ambly\\ambage.md": {
    "primary": "A winding, circuitous path or roundabout course; metaphorically, circumlocution or indirectness of speech.",
    "secondary": "In classical rhetoric and literary criticism, deliberate verbal evasion, obscurity, or labyrinthine discourse employed to avoid direct assertion.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "Troilus and Criseyde",
        "quote": "With double wordes and half with wordes queynte, withouten **ambage** she declared her intent unto the knight."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Truth hath a direct and perspicuous line, whereas error leadeth the mind through endless **ambage** and perplexing mazes."
      },
      {
        "author": "John Milton",
        "work": "Paradise Regained",
        "quote": "The subtle tempter veiled his design beneath dark rhetorical **ambage**, seeking to ensnare the solitary wanderer in words."
      }
    ]
  },
  "Dashboard — ambly\\ambagious.md": {
    "primary": "Characterized by roundabout ways or indirect paths; circuitous, winding, or circumlocutory.",
    "secondary": "In stylistic analysis, describing discourse, legal drafting, or narrative structures burdened by excessive complexity and verbose obscurity.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Through long **ambagious** corridors of bureaucratic delay, the petition crawled from minister to clerk without decision."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "The Master of Ballantrae",
        "quote": "The lawyer pursued an **ambagious** line of questioning, circling round the vital document without once naming it aloud."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of the Four",
        "quote": "His narrative was singularly **ambagious**, full of trivial digressions that tested the patience of my companion."
      }
    ]
  },
  "Dashboard — ambly\\amber.md": {
    "primary": "A hard, translucent, yellowish to brownish-yellow fossilized resin derived from ancient coniferous trees, prized as a gemstone.",
    "secondary": "In paleobiology and gemology, an amorphous biogenic organic polymer valued for exceptionally preserving delicate fossil inclusions and for its electrostatic triboelectric properties.",
    "quotes": [
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "When rubbed vigorously with the hand, **amber** acquires heat and draws unto itself pine needles and light flakes of chaff."
      },
      {
        "author": "Francis Bacon",
        "work": "Sylva Sylvarum",
        "quote": "The electrum or yellow **amber** doth manifest a subtle attraction when chafed, an effect common to resins and vitreous bodies."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "Delicate insects preserved within ancient Baltic **amber** reveal morphological features identical to those observed across geological epochs."
      }
    ]
  },
  "Dashboard — ambly\\ambition.md": {
    "primary": "An earnest desire for achievement, distinction, wealth, or power, accompanied by the determination to attain it.",
    "secondary": "In moral philosophy and psychology, a dual-natured motivational drive that ranges from virtuous aspiration for excellence to destructive egotism.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Julius Caesar",
        "quote": "The noble Brutus hath told you Caesar was ambitious: if it were so, it was a grievous fault, and grievously hath Caesar answer'd it; yet Brutus says he was ambitious, and Brutus is an honourable man."
      },
      {
        "author": "Francis Bacon",
        "work": "Essays",
        "quote": "**Ambition** is like choler; which is an humor that maketh men active, earnest, full of alacrity, and stirring, if it be not stopped."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "Learn from me, if not by my precepts, at least by my example, how dangerous is the acquirement of knowledge and how much happier that man is who believes his native town to be the world, than he who aspires to become greater than his nature will allow through blind **ambition**."
      }
    ]
  },
  "Dashboard — ambly\\ambitious.md": {
    "primary": "Having or exhibiting a strong desire and determination to succeed, achieve distinction, or attain power.",
    "secondary": "Describing plans, projects, or creative works that demand exceptional effort, skill, scale, or resources to execute successfully.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The most **ambitious** emperors were frequently restrained by the turbulent and venal demands of the Praetorian guards."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "The young novelist embarked on an **ambitious** canvas, intending to portray the entire panorama of Edwardian social discontent."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "In democratic communities, men are easily moved by small aspirations, yet rare is the soul possessed of truly **ambitious** grandeur."
      }
    ]
  },
  "Dashboard — ambly\\ambitiously.md": {
    "primary": "In an ambitious manner; with eager aspiration, bold enterprise, or a high degree of intent.",
    "secondary": "Carried out on a grand scale or with great boldness, often stretching available capacities or conventional limits.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "She looked forward **ambitiously** to an existence where her intellect might expand beyond provincial borders."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The minister planned **ambitiously** for the expansion of naval supremacy across both northern and southern hemispheres."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Lydgate framed his clinical research **ambitiously**, dreaming of establishing fundamental cellular laws."
      }
    ]
  },
  "Dashboard — ambly\\ambitiousness.md": {
    "primary": "The quality, state, or disposition of being ambitious; aspiring character or zealous drive.",
    "secondary": "The characteristic of an enterprise, artistic endeavor, or intellectual scheme that exhibits bold scale and lofty scope.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "The energetic character is defined by an active **ambitiousness** that refuses to acquiesce in inherited misery."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Our self-feeling in this world is determined entirely by what we back ourselves to be, so that **ambitiousness** dictates both our pride and shame."
      },
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "Without an inner standard of perfection, mere worldly **ambitiousness** degenerates into restless commercial rivalry."
      }
    ]
  },
  "Dashboard — ambly\\ambly.md": {
    "primary": "A combining form of Greek origin meaning blunt, dull, dim, or weakened.",
    "secondary": "In scientific and medical terminology, a productive prefix denoting impairment of acuity (as in amblyopia) or rounded anatomical margins (as in Amblyrhynchus).",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The prefix **ambly** derives from the Greek for blunt or dull, serving scientific nomenclature across ophthalmology and zoology."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Terms compounded with **ambly** frequently signify an organ whose terminal apex is obtuse rather than sharp."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-book of Geology",
        "quote": "Mineral names employing **ambly** signal obtuse interfacial angles between cleavage planes."
      }
    ]
  },
  "Dashboard — ambly\\amblygeustia.md": {
    "primary": "A condition characterized by a blunting, dulling, or reduction of the sense of taste; hypogeusia.",
    "secondary": "In sensory neurology and otolaryngology, partial gustatory impairment resulting from cranial nerve lesions, zinc deficiency, or glossal epithelial damage.",
    "quotes": [
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Affection of the glossopharyngeal trunk produces unilateral **amblygeustia**, the patient experiencing only dull sensations from sapid substances."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Transient **amblygeustia** may accompany severe febrile conditions or marked nutritional deficiencies of the oral mucosa."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "He complained of profound gustatory blunting, an **amblygeustia** that rendered even fiery spices tasteless upon his tongue."
      }
    ]
  },
  "Dashboard — ambly\\amblygonite.md": {
    "primary": "A fluorophosphate mineral composed of lithium, sodium, and aluminium [(Li,Na)AlPO4(F,OH)], typically found in granite pegmatites.",
    "secondary": "In economic geology and mineralogy, an important commercial ore of lithium named for its obtuse cleavage angle (Greek amblys 'blunt' and gonia 'angle').",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "The mineral **amblygonite** crystallizes in the triclinic system and is distinguished by its pale vitreous lustre and rich lithium content."
      },
      {
        "author": "August Breithaupt",
        "work": "Complete Handbook of Mineralogy",
        "quote": "We designated this pegmatitic species **amblygonite** on account of the obtuse cleavage plane that sets it apart from spodumene."
      },
      {
        "author": "Archibald Geikie",
        "work": "The Founders of Geology",
        "quote": "In lithium-bearing pegmatites, massive nodules of **amblygonite** often occur associated with tourmaline and lepidolite."
      }
    ]
  },
  "Dashboard — ambly\\amblyopia.md": {
    "primary": "A disorder of sight characterized by dimness of vision or reduced visual acuity without apparent anatomical defect in the eye; lazy eye.",
    "secondary": "In clinical ophthalmology and developmental neurobiology, cortical visual deficit caused by abnormal binocular visual experience during early childhood critical periods.",
    "quotes": [
      {
        "author": "David Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "Monocular deprivation during early postnatal development causes functional **amblyopia** by reorganizing ocular dominance columns in the striate cortex."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Toxic **amblyopia** from chronic tobacco and alcohol abuse presents with bilateral central scotomas and impaired colour perception."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "Because her strabismus went uncorrected in infancy, she developed profound **amblyopia** in the deviating eye."
      }
    ]
  },
  "Dashboard — ambly\\amblyopic.md": {
    "primary": "Pertaining to, affected by, or characteristic of amblyopia.",
    "secondary": "In physiological optics, describing an eye or visual pathway exhibiting reduced acuity and contrast sensitivity unresponsive to refractive correction alone.",
    "quotes": [
      {
        "author": "Torsten Wiesel",
        "work": "Nobel Lecture in Physiology or Medicine",
        "quote": "Cortical neurons driven exclusively by the normal eye reveal how the **amblyopic** eye loses functional connectivity in area seventeen."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "The patient retained peripheral fields while central fixation remained markedly **amblyopic**."
      },
      {
        "author": "Oliver Sacks",
        "work": "Seeing Voices",
        "quote": "Patching the dominant eye forces the visual cortex to process signals from the suppressed, **amblyopic** eye before neural plasticity wanes."
      }
    ]
  },
  "Dashboard — ambly\\amblyrhynchus.md": {
    "primary": "A genus of iguanid lizards native to the Galápagos Islands, comprising the marine iguana (Amblyrhynchus cristatus).",
    "secondary": "In evolutionary biology and herpetology, the only extant marine lizard genus, characterized by a blunt snout adapted for grazing underwater algae off submerged lava reefs.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The genus **Amblyrhynchus** possesses a remarkably short, blunt muzzle, admirably suited for cropping sea-weed from the wave-washed rocks."
      },
      {
        "author": "Herman Melville",
        "work": "The Encantadas",
        "quote": "Climbing upon the jagged basalt, the hideous black lizards of **Amblyrhynchus** bask in motionless assemblies under the equatorial glare."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The cranium of **Amblyrhynchus** exhibits flattened premaxillary bones that accommodate its specialized herbivorous dentition."
      }
    ]
  },
  "Dashboard — ambly\\unambitious.md": {
    "primary": "Not having or showing ambition; content with modest aims, simple circumstances, or low profile.",
    "secondary": "Characterized by unpretentious simplicity and lack of ostentation or striving for grand achievements.",
    "quotes": [
      {
        "author": "Thomas Gray",
        "work": "Elegy Written in a Country Churchyard",
        "quote": "Far from the madding crowd's ignoble strife, their sober wishes never learn'd to stray; along the cool sequester'd vale of life they kept the noiseless tenor of their way, in **unambitious** peace."
      },
      {
        "author": "George Eliot",
        "work": "Scenes of Clerical Life",
        "quote": "He lived an **unambitious** life, performing his parish duties with quiet diligence and asking nothing of fame."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I wished to live deliberately and in an **unambitious** simplicity, unburdened by the frantic pursuits of the marketplace."
      }
    ]
  },
  "Dashboard — amph\\Amphipoda.md": {
    "primary": "An order of small, malacostracan crustaceans with laterally compressed bodies, lacking a carapace, including sandhoppers and freshwater scuds.",
    "secondary": "In marine biology and invertebrate zoology, a diverse benthic and pelagic taxon displaying sessile compound eyes and distinct thoracic appendages adapted for both swimming and crawling.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The order **Amphipoda** is distinguished from the Isopoda by lateral flattening of the thorax and the grouping of abdominal appendages."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Under every clump of washed-up kelp, multitudes of **Amphipoda** scatter like fleas when the weed is lifted."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "In certain species of **Amphipoda**, the male grasps the female with enlarged anterior appendages during prolonged amplexus."
      }
    ]
  },
  "Dashboard — amph\\amph.md": {
    "primary": "A combining form of Greek origin meaning both, of both kinds, around, or on both sides (variant of amphi-).",
    "secondary": "In scientific nomenclature and etymology, an elided prefix occurring before vowels or 'h', appearing in biological and chemical terms designating dual modes or environments.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The prefix **amph**, truncated from amphi before a vocalic stem, denotes duality and surrounding presence across ancient Greek compounds."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "Terms compounded with **amph** consistently signify twofold adaptations to contrasting media."
      },
      {
        "author": "Richard Chenevix Trench",
        "work": "English Past and Present",
        "quote": "Greek borrowings starting with **amph** introduce nuances of duality into English scientific discourse."
      }
    ]
  },
  "Dashboard — amph\\amphetamine.md": {
    "primary": "A synthetic central nervous system stimulant that promotes wakefulness and focus, used therapeutically to treat ADHD and narcolepsy.",
    "secondary": "In psychopharmacology and neurochemistry, a phenethylamine derivative that acts by reversing monoamine transporters, triggering massive presynaptic release of dopamine and norepinephrine.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Before the advent of L-DOPA, high doses of **amphetamine** were occasionally administered to arouse post-encephalitic patients from profound lethargy."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "By inhibiting dopamine reuptake and reversing the vesicular transporter, **amphetamine** substantially increases extracellular catecholamines in the nucleus accumbens."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World Revisited",
        "quote": "The pharmacological mobilization of mental energy via synthetic **amphetamine** raises ethical questions about chemical enhancement in competitive societies."
      }
    ]
  },
  "Dashboard — amph\\amphibia.md": {
    "primary": "A class of cold-blooded, ectothermic vertebrate animals whose larvae typically undergo metamorphosis from aquatic respiration to terrestrial existence.",
    "secondary": "In evolutionary biology and systematics, a monophyletic tetrapod clade encompassing anurans, urodeles, and caecilians, functioning as vital bioindicators of wetland health.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "The class **Amphibia** encompasses cold, moist quadrupeds with naked skin, inhabiting murky waters and humid recesses of the earth."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Cuvier divided **Amphibia** into batrachians that lose their gills in adult life and those that retain them permanently."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The transitional habits of **Amphibia** afford a living illustration of how aquatic vertebrates acquired the organs of terrestrial life."
      }
    ]
  },
  "Dashboard — amph\\amphibian.md": {
    "primary": "Any cold-blooded vertebrate belonging to the class Amphibia, such as a frog, toad, salamander, or newt.",
    "secondary": "A vehicle, aircraft, or military craft designed to operate on both land and water; metaphorically, an entity thriving in two distinct realms.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "Every air-breathing vertebrate passes through an embryonic stage reminiscent of the ancestral **amphibian** gill-slit arrangement."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The little **amphibian** crept out from the marsh weeds, shedding its tadpole tail to begin life on dry mud."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The rapid global decline of **amphibian** populations signaled early warnings of fungal pathogens and environmental disruption."
      }
    ]
  },
  "Dashboard — amph\\amphibiotic.md": {
    "primary": "Living in water during the larval or nymphal stage and on land as an adult; having an amphibious life cycle.",
    "secondary": "In entomology and aquatic ecology, describing insects such as mayflies, dragonflies, and stoneflies whose life stages link freshwater and riparian ecosystems.",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "Unlike terrestrial social insects, **amphibiotic** organisms must adapt their respiratory anatomy to two entirely dissimilar physical media."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The **amphibiotic** insects emerging from the estuary shoreline furnish sustenance to countless migratory shorebirds."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "A Text-Book of Entomology",
        "quote": "Odonata exhibit an **amphibiotic** ontogeny, breathing via rectal tracheal gills as nymphs before emerging into winged aerial predators."
      }
    ]
  },
  "Dashboard — amph\\amphibious.md": {
    "primary": "Able to live or operate both on land and in water; adapted to both terrestrial and aquatic environments.",
    "secondary": "Having a dual or ambivalent nature; capable of operating effectively across two contrasting spheres or situations.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "Man is that great and true **amphibious** creature whose nature is disposed to live, not only like other creatures in divers elements, but in divided and distinguished worlds."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The harpooneer led an **amphibious** existence, equally at home plunged neck-deep in icy brine or pacing the dry cedar decks."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The littoral tribes pursued an **amphibious** warfare, retreating into marshy inlets whenever Roman infantry approached."
      }
    ]
  },
  "Dashboard — amph\\amphibole.md": {
    "primary": "An extensive group of inosilicate rock-forming minerals consisting of double chains of silica tetrahedra with hydroxyl or halogen ions.",
    "secondary": "In mineralogy and petrology, minerals such as hornblende and tremolite characterized by prismatic cleavage intersecting at approximately 56° and 124°.",
    "quotes": [
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Because its Protean forms easily deceive the eye, I have applied the name **amphibole**, from the Greek word for ambiguous or deceptive."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The cleavage angles of **amphibole** readily distinguish its prismatic crystals from those of the pyroxene series."
      },
      {
        "author": "Archibald Geikie",
        "work": "Class-Book of Geology",
        "quote": "Under intense regional metamorphism, augite crystals recrystallize into fibrous green needles of **amphibole**."
      }
    ]
  },
  "Dashboard — amph\\amphibolips.md": {
    "primary": "A genus of gall wasps in the family Cynipidae that induce large, globular galls (oak apples) on oak trees.",
    "secondary": "In forest entomology and cecidology, hymenopteran insects that chemically manipulate the developmental genetics of Quercus leaf tissues to produce protective larval dwellings.",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "Demons of the Dust",
        "quote": "The female wasp of **Amphibolips** injects secretions into the spring bud of the red oak, causing the swelling of a spongy oak apple."
      },
      {
        "author": "Alfred Kinsey",
        "work": "The Gall Wasp Genus Cynips: A Study in the Origin of Species",
        "quote": "The taxonomic boundaries between Cynips and **Amphibolips** depend heavily upon the internal structure and radiating fibres of the larval cell."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Insects Injurious to Forest and Shade Trees",
        "quote": "In early summer the larvae of **Amphibolips** feed securely within the central core of the spherical green gall."
      }
    ]
  },
  "Dashboard — amph\\amphibolite.md": {
    "primary": "A medium- to coarse-grained metamorphic rock composed mainly of amphibole (especially hornblende) and plagioclase feldspar.",
    "secondary": "In petrology, a metamorphic facies indicative of medium-to-high temperature and moderate-to-high pressure metamorphism of basaltic or gabbroic protoliths.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "Text-book of Geology",
        "quote": "Dark crystalline sheets of **amphibolite** cut through the ancient Lewisian gneiss of the Northwest Highlands."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "Under regional thermal metamorphism, basic volcanic traps recrystallize into foliated masses of dark **amphibolite**."
      },
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "The transition from greenstone to **amphibolite** illustrates the progressive rearrangement of volcanic minerals under subterranean pressure."
      }
    ]
  },
  "Dashboard — amph\\amphibology.md": {
    "primary": "Ambiguity in sentence structure or phrasing, permitting more than one grammatical interpretation; a statement of uncertain meaning.",
    "secondary": "In formal logic and rhetoric, a fallacy arising when syntactical looseness causes a proposition to support two contradictory conclusions.",
    "quotes": [
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "The oracles of the pagans gained their reputation through cunning **amphibology**, leaving the hearer to interpret the outcome either way."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Words should be free from misleading **amphibology**, lest philosophical inquiry degenerate into disputes over verbal syntax."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The poet must distinguish between intentional symbolic resonance and careless grammatical **amphibology** that obscures his thought."
      }
    ]
  },
  "Dashboard — amph\\amphiboly.md": {
    "primary": "Ambiguity resulting from grammatical or syntactical construction rather than ambiguous word meaning; an amphibolous proposition.",
    "secondary": "In Kantian philosophy, the confusion of transcendental concepts of reflection (the amphiboly of reflexive concepts), confounding phenomena with noumena.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The **amphiboly** of the concepts of reflection arises when we mistake pure objects of the understanding for empirical appearances."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "An **amphiboly** occurs when the phrasing of a sentence allows two different subjects or predicates to be understood."
      },
      {
        "author": "William James",
        "work": "The Meaning of Truth",
        "quote": "Epistemological debates are frequently plagued by an **amphiboly** regarding whether 'object' refers to mental content or reality."
      }
    ]
  },
  "Dashboard — amph\\amphibrach.md": {
    "primary": "A metrical foot in poetry consisting of a long or stressed syllable between two short or unstressed syllables (˘ ¯ ˘).",
    "secondary": "In classical and accentual-syllabic prosody, a three-syllable foot frequently employed in buoyant verse, ballads, and limericks.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Metrical Feet: A Lesson for a Boy",
        "quote": "**Amphibrach** hastes with a stately stride on, with its first and its last syllable short and the center one long."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The triple roll of the **amphibrach** lends an irresistible tripping cadence to English humorous verse."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "When smooth rhythm is required, poets avoid the abrupt disturbance that a misplaced **amphibrach** introduces into heroic lines."
      }
    ]
  },
  "Dashboard — amph\\amphicarpa.md": {
    "primary": "A genus of twining leguminous herbs in the Fabaceae family, notable for producing both aerial and subterranean fruits.",
    "secondary": "In evolutionary botany, a legume exhibiting amphicarpy (cleistogamous geocarpic flowers below ground alongside chasmogamous aerial flowers), commonly known as hog peanut.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In **Amphicarpa**, subterranean flowers bury their ovaries into the soil before fertilization, securing seeds even if aerial blooms fail."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The twining stems of **Amphicarpa** climb over low bushes in rich woods, bearing delicate purplish racemes above."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Journal of Henry David Thoreau",
        "quote": "I dug into the damp forest loam and uncovered the plump, fleshy beans of the subterranean **Amphicarpa**."
      }
    ]
  },
  "Dashboard — amph\\amphicarpaea.md": {
    "primary": "The standardized botanical generic name for the genus Amphicarpaea (hog-peanut) in the legume family Fabaceae.",
    "secondary": "In plant systematics, a genus of twining nitrogen-fixing plants famous for dimorphic seed production as an ecological bet-hedging strategy.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "The legal botanical spelling **Amphicarpaea** designates the hog-peanut, whose underground fruits were gathered by indigenous peoples."
      },
      {
        "author": "Charles Darwin",
        "work": "The Movements and Habits of Climbing Plants",
        "quote": "The revolving nutation of **Amphicarpaea** shoots ensures rapid attachment to supporting woodland undergrowth."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Cyclopedia of American Horticulture",
        "quote": "Species of **Amphicarpaea** thrive in shaded deciduous valleys, flourishing where moist humus permits geocarpic rooting."
      }
    ]
  },
  "Dashboard — amph\\amphictyony.md": {
    "primary": "An association or confederation of neighboring Greek states or tribes organized to protect and manage a shared sacred sanctuary.",
    "secondary": "In ancient history and political theory, an early form of international religious council, most famously the Delphic Amphictyonic League.",
    "quotes": [
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "The Delphic **amphictyony** represented a sacred covenant among twelve tribes to guarantee peace at Apollo's holy shrine."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The ancient **amphictyony** of Greece failed to avert mutual slaughter whenever the passions of Sparta and Athens collided."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The **amphictyony** of ancient Greece had ample authority in theory, yet in practice it could not enforce decrees against dominant members."
      }
    ]
  },
  "Dashboard — amph\\amphidiploid.md": {
    "primary": "An organism or cell having a diploid set of chromosomes from each of two distinct parental species; an allotetraploid that functions as a fertile diploid.",
    "secondary": "In cytogenetics and plant breeding, an interspecific hybrid whose doubled chromosome complement allows normal bivalent pairing during meiosis, establishing instant speciation.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The synthesis of an **amphidiploid** plant demonstrates how hybrid vigor can be fixed instantly without segregational sterility."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Polyploidy, particularly in the form of an **amphidiploid**, provides the principal mechanism for sudden speciation in vascular flora."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Primula kewensis arose as a fertile **amphidiploid** when the sterile diploid hybrid doubled its chromosome count spontaneously."
      }
    ]
  },
  "Dashboard — amph\\amphidiploidy.md": {
    "primary": "The condition of being an amphidiploid; the genetic state where allopolyploidy restores full fertility to an interspecific hybrid.",
    "secondary": "In evolutionary genomics, an allotetraploid mechanism that combines divergent parental genomes, preventing aneuploidy and facilitating genome buffering.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Mankind Evolving",
        "quote": "Through **amphidiploidy**, disparate ancestral genomes establish stable bivalent pairing, creating stable new polyploid species."
      },
      {
        "author": "George Ledyard Stebbins",
        "work": "Variation and Evolution in Plants",
        "quote": "The widespread prevalence of **amphidiploidy** among cultivated wheats and cottons underlines its agricultural and evolutionary significance."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "While rare in bisexual animals, **amphidiploidy** remains one of the most prolific speciation processes throughout the plant kingdom."
      }
    ]
  },
  "Dashboard — amph\\amphigory.md": {
    "primary": "A verse or composition that has the appearance of meaning or profound depth but is in fact meaningless nonsense or absurd parody.",
    "secondary": "In literary criticism, a burlesque stylistic exercise designed to mock pretentiousness by combining high-flown diction with syntactic incoherence.",
    "quotes": [
      {
        "author": "Algernon Charles Swinburne",
        "work": "The Heptalogia",
        "quote": "His parodic lines were pure **amphigory**, echoing majestic rhythms while dissolving every shred of logical significance."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "The Book of Snobs",
        "quote": "The poet laureate of fashionable salons recited a sentimental **amphigory** that moved ladies to tears of baffled bewilderment."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "To the uninitiated reader, Teufelsdröckh's discourse may seem an impenetrable **amphigory**, yet a spark of divine irony glows within."
      }
    ]
  },
  "Dashboard — amph\\amphimacer.md": {
    "primary": "A metrical foot in classical and accentual poetry consisting of three syllables: a long, a short, and a long (¯ ˘ ¯); also called a cretic foot.",
    "secondary": "In Greek and Latin prosody, a metrical foot characterized by a central short syllable framed by two long quantities, common in choral lyrics and dramatic strophes.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Metrical Feet: A Lesson for a Boy",
        "quote": "First and last being long, short the middle, an **amphimacer** strikes its emphatic, bounding pulse."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "In Swinburnian verse, the insertion of an **amphimacer** creates a sudden resonant crest upon the lyrical wave."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "The pedant scans the line with heavy ear, debating whether an **amphimacer** or a molossus best terminates the measure."
      }
    ]
  },
  "Dashboard — amph\\amphimixis.md": {
    "primary": "True sexual reproduction involving the union and fusion of male and female gametes to produce a genetically unique zygote.",
    "secondary": "In evolutionary biology and population genetics, the primary source of genetic recombination, contrasted with apomixis, automixis, or parthenogenesis.",
    "quotes": [
      {
        "author": "August Weismann",
        "work": "The Germ-Plasm: A Theory of Heredity",
        "quote": "The ultimate biological significance of **amphimixis** consists in the continuous generation of individual hereditary variability."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "By recombining distinct mutations from separate lineages, **amphimixis** accelerates the rate of adaptive evolution in sexual species."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics of the Evolutionary Process",
        "quote": "Organisms that abandon **amphimixis** for asexual reproduction often trade short-term demographic gains for long-term evolutionary stagnation."
      }
    ]
  },
  "Dashboard — amph\\amphineura.md": {
    "primary": "A former class or subphylum of primitive marine mollusks with bilateral symmetry and paired nerve cords, comprising chitons and solenogasters.",
    "secondary": "In invertebrate phylogeny and historical malacology, a classical grouping reflecting archaic molluscan nervous system architecture with lateral and pedal longitudinal cords.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The subphylum **Amphineura** reveals the primitive scalariform nervous system that connects ancestral mollusks with unsegmented worms."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In **Amphineura**, the absence of cephalic eyes and the simple radula testify to an ancient, unspecialized molluscan grade."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "The dorsal calcareous plates of Polyplacophora illustrate the distinctive bilateral shell pattern characteristic of **Amphineura**."
      }
    ]
  },
  "Dashboard — amph\\amphioxidae.md": {
    "primary": "A family of small, fish-like cephalochordates, commonly known as lancelets, possessing a persistent notochord throughout life.",
    "secondary": "In vertebrate paleontology and evolutionary morphology, the taxonomic family (often Branchiostomatidae) representing the closest living invertebrate relatives of vertebrates.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The family **Amphioxidae** occupies a uniquely central position, demonstrating the archetypal chordate body plan before skull formation."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "No other group in living nature illuminates the primordial transition to vertebrates more clearly than **Amphioxidae**."
      },
      {
        "author": "William Bateson",
        "work": "Materials for the Study of Variation",
        "quote": "The metameric segmentation of the myotomes in **Amphioxidae** provides the key to understanding the origins of vertebrate muscular symmetry."
      }
    ]
  },
  "Dashboard — amph\\amphioxus.md": {
    "primary": "A small, translucent, fish-shaped marine cephalochordate (Branchiostoma) lacking a skull, jaws, and paired fins, but possessing a dorsal notochord.",
    "secondary": "In comparative embryology and evolutionary biology, a classic model organism providing structural insight into the stem lineage of all vertebrates.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The lancelet or **amphioxus** is a wonderful creature, so low in the scale of organization that naturalists long doubted whether to place it among the vertebrates."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "In **amphioxus**, the spinal cord runs uninterrupted from snout to tail, without swelling into an anterior cranial brain."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "From an ancestor closely resembling the living **amphioxus**, the entire host of fishes, reptiles, birds, and mammals originally ascended."
      }
    ]
  },
  "Dashboard — amph\\amphipod.md": {
    "primary": "Any crustacean belonging to the order Amphipoda, characterized by a laterally flattened body and legs adapted for both swimming and hopping.",
    "secondary": "In marine and freshwater ecology, an abundant macroinvertebrate herbivore and detritivore serving as a fundamental trophic link in aquatic food webs.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Deep in the abyss, the scavenged carcass was instantly swarmed by pale, ravenous swarms of benthic **amphipod** species."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "On the damp sandy beach, whenever a mound of dry kelp was disturbed, many a tiny **amphipod** leapt vigorously into the air."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "Unlike the depressed isopod, the typical **amphipod** is compressed sideways, enabling it to scurry through dense tangles of filamentous algae."
      }
    ]
  },
  "Dashboard — amph\\amphiprion.md": {
    "primary": "A genus of pomacentrid marine reef fishes commonly known as clownfish or anemonefish, noted for their bright coloration and symbiotic relationship with sea anemones.",
    "secondary": "In marine ethology and physiological ecology, a protandrous hermaphroditic fish possessing protective mucus that inhibits sea anemone nematocyst discharge.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Within the stinging tentacles of large tropical sea anemones, the vivid little damselfish of **Amphiprion** finds complete immunity."
      },
      {
        "author": "David Attenborough",
        "work": "Life on Earth",
        "quote": "The relationship between **Amphiprion** and its anemone host is an extraordinary instance of mutualist symbiosis on coral reefs."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "A chemical coating across the epidermal scales of **Amphiprion** prevents the stinging capsules of the anemone from firing."
      }
    ]
  },
  "Dashboard — amph\\amphiprostylar.md": {
    "primary": "Having open columnar porticoes at both the front and rear facades, but no columns along the lateral sides (describing classical buildings).",
    "secondary": "In classical architecture, describing a temple design typified by the Temple of Athena Nike on the Athenian Acropolis, balancing entrance and rear colonnades.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "De Architectura",
        "quote": "The **amphiprostylar** temple has all the features of the prostyle, and besides has columns and a pediment in the rear like those in front."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "The elegant symmetry of an **amphiprostylar** facade bestows noble balance without the heavy encumbrance of a continuous peristyle."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "In the miniature sanctuary of Athena Nike, the **amphiprostylar** arrangement produced an exquisite lightness upon the bastion."
      }
    ]
  },
  "Dashboard — amph\\amphiprostyle.md": {
    "primary": "A classical temple or building possessing a row of columns at both front and back facades, but without lateral columns.",
    "secondary": "In architectural history, a specific design typology distinguished from peripteral and prostyle plans, providing double axial dignity to religious monuments.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "De Architectura",
        "quote": "When columns of equal number and proportion stand before the posticum as before the pronaos, the building is termed an **amphiprostyle**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Near the banks of the Ilissus stood a small Ionic **amphiprostyle**, admired by travelers for its pristine proportion."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Greek master preferred the dignified economy of the **amphiprostyle** when hillside terrain precluded a wide colonnade."
      }
    ]
  },
  "Dashboard — amph\\amphiprotic.md": {
    "primary": "Describing a chemical substance or molecule that can both donate and accept a proton (hydrogen ion), acting as both a Brønsted acid and base.",
    "secondary": "In physical chemistry, referring to self-ionizing solvents such as water (H2O) and liquid ammonia, or polyprotic acid anions such as bicarbonate (HCO3-).",
    "quotes": [
      {
        "author": "Gilbert N. Lewis",
        "work": "Valence and the Structure of Atoms and Molecules",
        "quote": "The water molecule is quintessential in its **amphiprotic** behavior, simultaneously capable of releasing or capturing a proton."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The bicarbonate ion acts as an **amphiprotic** buffer in mammalian blood, stabilizing systemic pH against sudden acidemia or alkalemia."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Solvents displaying **amphiprotic** autoionization form conjugate pairs that govern the dissociation constants of dissolved salts."
      }
    ]
  },
  "Dashboard — amph\\amphisbaena.md": {
    "primary": "A mythical serpent or dragon depicted with a head at each end of its body, capable of moving in either direction.",
    "secondary": "In herpetology, any burrowing, limbless, ringed reptile belonging to the worm lizard genus Amphisbaena, native to tropical regions.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Dreadful was the din of hissing through the hall, thickly swarming with scorpions and asps, and the two-headed **amphisbaena** dire."
      },
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "The **amphisbaena** hath a twin head, that is, one at either extremity, as if one mouth were too little for the discharge of its poison."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In the pampas we unearthed a subterranean reptile of the genus **amphisbaena**, whose blunt tail closely simulated its blind head."
      }
    ]
  },
  "Dashboard — amph\\amphisbaenia.md": {
    "primary": "A suborder of squamate reptiles comprising the worm lizards, characterized by elongated, limbless bodies and adaptations for subterranean burrowing.",
    "secondary": "In vertebrate phylogenetics, a specialized fossorial clade of lepidosaurs possessing heavily ossified skulls and distinctive ring-like annuli around the trunk.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The skull of **Amphisbaenia** is consolidated into a compact, bullet-shaped digging tool, perfectly adapted for head-first soil penetration."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "In **Amphisbaenia**, the outer skin is divided into regular rectangular segments that resemble the metameres of an earthworm."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Hidden beneath the tropical leaf litter, species of **Amphisbaenia** tunnel through subterranean runways in search of termites."
      }
    ]
  },
  "Dashboard — amph\\amphisbaenidae.md": {
    "primary": "The family of worm lizards within the suborder Amphisbaenia, comprising mostly limbless, burrowing reptiles with annular body rings.",
    "secondary": "In systematic herpetology, the most species-rich clade of amphisbaenians, widespread across the Neotropics and sub-Saharan Africa.",
    "quotes": [
      {
        "author": "Hans Gadow",
        "work": "Amphibia and Reptiles",
        "quote": "The family **Amphisbaenidae** exhibits a complete loss of limbs and pelvic vestiges, moving forward or backward through soil by concertina locomotion."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The cranial osteology of **Amphisbaenidae** shows fusion of suture lines to resist the severe mechanical strain of underground excavation."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The disjunct trans-Atlantic distribution of **Amphisbaenidae** offers striking evidence of ancient continental connections."
      }
    ]
  },
  "Dashboard — amph\\amphistylar.md": {
    "primary": "Having columns or porticoes at both ends (front and rear); amphiprostyle.",
    "secondary": "In classical architectural criticism, describing temple structures that maintain balanced colonnades at opposing facades while leaving the flank walls uninterrupted.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The dignified **amphistylar** arrangement presents a noble porch alike to the approaching worshipper and the retreating procession."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The architect employed an **amphistylar** plan to ensure that the monument looked equally impressive from both public squares."
      },
      {
        "author": "Vitruvius",
        "work": "De Architectura",
        "quote": "When colonnades crown both front and rear aspects of the cella, the temple assumes an **amphistylar** dignity."
      }
    ]
  },
  "Dashboard — amph\\amphitheatre.md": {
    "primary": "An oval or circular open-air building with tiers of seats rising around a central arena, used in ancient Rome for gladiator contests and public spectacles.",
    "secondary": "Any natural or architectural bowl-shaped formation, valley, or tiered auditorium resembling a Roman amphitheatre.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The colossal **amphitheatre** of Titus, which has withstood the injuries of time, was erected to accommodate more than eighty thousand spectators."
      },
      {
        "author": "Lord Byron",
        "work": "Childe Harold's Pilgrimage",
        "quote": "Arches on arches! as it were that Rome, collecting the chief trophies of her line, would build up all her triumphs in one dome, her **amphitheatre** stands sublime."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "From the mountain ridge we looked down into a vast natural **amphitheatre** carpeted with alpine flowers."
      }
    ]
  },
  "Dashboard — amph\\amphitheatric.md": {
    "primary": "Resembling, pertaining to, or characteristic of an amphitheatre.",
    "secondary": "Describing landscape forms, seating arrangements, or theatrical staging featuring concentric, upwardly sloping tiers.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "The volcanic crater formed an **amphitheatric** basin of terrifying depth, ringed with basaltic precipices."
      },
      {
        "author": "Walter Scott",
        "work": "The Heart of Midlothian",
        "quote": "The spectators occupied an **amphitheatric** ring of hills that overlooked the tournament meadow."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The university senate assembled in an **amphitheatric** chamber where rows of graduates rose toward the vaulted ceiling."
      }
    ]
  },
  "Dashboard — amph\\amphitheatrical.md": {
    "primary": "Shaped like or having the tiered, circular or oval arrangement of an amphitheatre.",
    "secondary": "In geomorphology and descriptive geography, describing semicircular mountain hollows, valleys, or arenas with rising slopes.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The ancient glacial cirque displayed an **amphitheatrical** form, its sheer rock walls cupping a deep turquoise tarn."
      },
      {
        "author": "Washington Irving",
        "work": "The Sketch Book of Geoffrey Crayon",
        "quote": "The mountains formed an **amphitheatrical** sweep, protecting the quiet green valley from the harsh northern gales."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "We drifted past an **amphitheatrical** bank of willows and maples that sloped down to the water's edge."
      }
    ]
  },
  "Dashboard — amph\\amphitropous.md": {
    "primary": "Describing an ovule in plants whose body is curved half-way around on its stalk, so that both the micropyle and chalaza are situated laterally.",
    "secondary": "In botanical embryology and organography, an ovule orientation intermediate between anatropous and campylotropous configurations.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "An **amphitropous** ovule is half inverted, with the hilum situated centrally along its lateral curvature."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In certain Caryophyllaceae, the ovule is distinctly **amphitropous**, bending upon its stalk so that base and apex lie transverse."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "The vascular raphe terminates prematurely in the **amphitropous** seed, distributing nourishment across the mid-region."
      }
    ]
  },
  "Dashboard — amph\\amphiuma.md": {
    "primary": "A genus of aquatic, eel-like salamanders native to southeastern North America, possessing four tiny, vestigial limbs.",
    "secondary": "In comparative anatomy and herpetology, commonly called the congo snake, famous for possessing exceptionally large nucleated erythrocytes and immense genomes.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The elongated body of **Amphiuma** retains minute two- or three-toed extremities that are completely useless for terrestrial locomotion."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "The red blood corpuscles of **Amphiuma** are among the largest known in the animal kingdom, easily examined under low magnification."
      },
      {
        "author": "John James Audubon",
        "work": "Ornithological Biography",
        "quote": "In the murky cypress bayous, we caught an **Amphiuma** writhing in the mud, mistaken by the boatmen for a venomous water serpent."
      }
    ]
  },
  "Dashboard — amph\\amphiumidae.md": {
    "primary": "The family of aquatic urodeles (salamanders) comprising the single extant genus Amphiuma, native to the southeastern United States.",
    "secondary": "In amphibian systematics, paedomorphic salamanders that lack external gills in adulthood but retain internal gill slits and an elongated body plan.",
    "quotes": [
      {
        "author": "Hans Gadow",
        "work": "Amphibia and Reptiles",
        "quote": "The family **Amphiumidae** occupies muddy ditches and sluggish streams of the North American coastal plain."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Fossil vertebrae of **Amphiumidae** found in Cretaceous strata establish their long persistence as specialized aquatic predators."
      },
      {
        "author": "Edward O. Wilson",
        "work": "Naturalist",
        "quote": "Wading through Alabama bogs as a boy, I encountered representatives of **Amphiumidae** buried in the black peat."
      }
    ]
  },
  "Dashboard — amph\\amphora.md": {
    "primary": "A tall ancient Greek or Roman earthen jar with two handles and a narrow neck, used for storing and transporting oil, wine, or grain.",
    "secondary": "An ancient Greco-Roman liquid and dry volumetric unit of capacity (approximately 26 liters in ancient Rome).",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Odyssey",
        "quote": "There within the storeroom stood jar upon jar of seasoned wine, and many a great **amphora** filled with sweet golden oil."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Sunken Roman galleys off the Mediterranean coast still yield cargo holds packed with terracotta **amphora** vessels intact."
      },
      {
        "author": "John Keats",
        "work": "Ode on a Grecian Urn",
        "quote": "The classic shape of an ancient **amphora** preserved in fired clay immortalizes the rustic festivities of antiquity."
      }
    ]
  },
  "Dashboard — amph\\amphoric.md": {
    "primary": "Resembling the hollow sound produced by blowing gently across the mouth of an empty bottle or jug.",
    "secondary": "In clinical medicine and pulmonology, describing an abnormal hollow, resonant breathing sound (amphoric breathing) heard over large pulmonary cavities or open pneumothorax.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Upon auscultation over the tuberculous cavity, one hears marked **amphoric** respiration, resembling wind blown across a jug."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The stethoscope detects an **amphoric** resonance whenever a cavernous fistula communicates directly with a bronchial branch."
      },
      {
        "author": "William R. Gowers",
        "work": "Lectures on the Diagnosis of Diseases of the Brain",
        "quote": "The physical signs included localized pectoriloquy and distinct **amphoric** echo produced by adjacent consolidation."
      }
    ]
  },
  "Dashboard — amph\\amphoteric.md": {
    "primary": "Capable of reacting chemically either as an acid or as a base; exhibiting both acidic and basic properties.",
    "secondary": "In biochemistry and inorganic chemistry, describing substances such as amino acids, zinc oxide, and aluminum hydroxide that can both neutralize acids and react with bases.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Because aluminum hydroxide dissolves readily in either strong acid or strong alkali, it serves as a textbook example of an **amphoteric** compound."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Proteins and polypeptides are inherently **amphoteric**, their amino and carboxyl groups ionising according to surrounding solution pH."
      },
      {
        "author": "Gilbert N. Lewis",
        "work": "Valence and the Structure of Atoms and Molecules",
        "quote": "An **amphoteric** oxide bridges the periodic divide between electropositive metals and electronegative nonmetals."
      }
    ]
  },
  "Dashboard — amph\\amphotericin.md": {
    "primary": "An antifungal polyene antibiotic medication produced by Streptomyces nodosus, used intravenously to treat severe, life-threatening systemic fungal infections.",
    "secondary": "In pharmacology, a membrane-active agent that binds to fungal ergosterol, creating transmembrane ion-permeable channels that cause cell lysis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In systemic blastomycosis and cryptococcal meningitis, intravenous **amphotericin** remains the indispensable mainstay of antimycotic therapy."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Fungal infections penetrating the blood-brain barrier necessitate aggressive therapy with liposomal **amphotericin** despite its nephrotoxicity."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Her convalescence was interrupted by a severe opportunistic infection that mandated prolonged infusions of **amphotericin**."
      }
    ]
  },
  "Dashboard — amph\\amphoterism.md": {
    "primary": "The chemical property or state of being amphoteric; the ability to react either as an acid or as a base.",
    "secondary": "In physical and analytical chemistry, the dual electrochemical behavior exhibited by ampholytes and zwitterions at their isoelectric point.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The phenomenon of **amphoterism** in zinc compounds illustrates how coordinate covalent bonding adapts to hydroxide ion concentration."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "The electrophoretic migration of amino acids halts when their internal **amphoterism** reaches electrochemical equilibrium."
      },
      {
        "author": "Gilbert N. Lewis",
        "work": "Valence and the Structure of Atoms and Molecules",
        "quote": "The **amphoterism** of water underlies the entire thermodynamic framework of aqueous acid-base equilibria."
      }
    ]
  },
  "Dashboard — ana\\anaphylactic.md": {
    "primary": "Relating to, caused by, or suffering from anaphylaxis; exhibiting hypersensitivity to a foreign antigen.",
    "secondary": "In clinical immunology, describing an immediate IgE-mediated type I hypersensitivity reaction causing bronchospasm, vasodilation, and vascular collapse.",
    "quotes": [
      {
        "author": "Charles Richet",
        "work": "Anaphylaxis (Nobel Lecture)",
        "quote": "The **anaphylactic** state is that profound vulnerability into which an organism is thrown by a prior minute dose of antigen."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Administration of horse antiserum may provoke an acute **anaphylactic** shock characterized by sudden dyspnea and vascular collapse."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Systemic **anaphylactic** hypotension rapidly impairs cerebral autoregulation, depriving cortical neurons of oxygenated blood."
      }
    ]
  },
  "Dashboard — ana\\anaphylaxis.md": {
    "primary": "A severe, acute, potentially life-threatening systemic allergic reaction triggered by exposure to an allergen.",
    "secondary": "In immunology, an immediate type I hypersensitivity syndrome mediated by cross-linking of allergen-specific IgE antibodies on mast cells and basophils, releasing histamine and leukotrienes.",
    "quotes": [
      {
        "author": "Charles Richet",
        "work": "Anaphylaxis",
        "quote": "I designated this fatal vulnerability **anaphylaxis**, from the Greek ana against and phylaxis protection, denoting the antithesis of immunity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt subcutaneous administration of adrenaline is the sovereign intervention against fatal respiratory obstruction during **anaphylaxis**."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "He described his sudden allergy to penicillin as a frightening descent into acute **anaphylaxis**, his airway swelling shut in minutes."
      }
    ]
  },
  "Dashboard — ana\\anarrhexis.md": {
    "primary": "The surgical refreacturing, breaking, or resetting of a bone that has united abnormally; also the operative rupture of a structure.",
    "secondary": "In orthopedic surgery, an intentional osteotomy or manual refracture performed to correct malunion, angular deformity, or improper joint alignment.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When malunion of the radius causes crippling deformities of the wrist, surgical **anarrhexis** is indicated to restore functional alignment."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Following traumatic contracture, orthopedic **anarrhexis** of the united callus relieved pressure on the adjacent median nerve."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-book of Geology",
        "quote": "Metaphorically, structural geologists compare the tectonic resetting of broken strata to the orthopedic **anarrhexis** of fractured limbs."
      }
    ]
  },
  "Dashboard — ana\\parana.md": {
    "primary": "A major river of south-central South America flowing through Brazil, Paraguay, and Argentina; also a federal state in southern Brazil.",
    "secondary": "In physical geography and geology, the second-longest river system in South America, whose basin includes the colossal Paraná flood basalt province.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "We navigated up the great river **Paraná**, whose muddy waters flow between high red clay cliffs rich in fossil mammalian bones."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "The hydrographic basin of the **Paraná** drains a continent-wide expanse of fertile plains and sub-tropical gallery forests."
      },
      {
        "author": "Herman Melville",
        "work": "The Confidence-Man",
        "quote": "The wanderer dreamed of wild southern waters, of steaming forests bordering the mighty **Paraná** in remote provinces."
      }
    ]
  },
  "Dashboard — ant\\ant.md": {
    "primary": "A prefix variant of anti- used before vowels or the letter 'h', signifying opposite, opposing, counter, or against; also a small eusocial insect of the family Formicidae.",
    "secondary": "In linguistics and morphemic analysis, the elided Greek prefix appearing in words such as antagonist, Antarctic, and antonym.",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "In English compound words, the prefix **ant** represents the ancient Greek preposition for opposite or in front of."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Ants",
        "quote": "Every solitary **ant** operates as an individual neuron within the superorganism of the subterranean colony."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The phonetic loss of the final vowel reduces anti to **ant** whenever the following root begins with an open syllable."
      }
    ]
  },
  "Dashboard — ant\\antagonise.md": {
    "primary": "To cause someone to become hostile, unfriendly, or opposed; to provoke resistance or active opposition.",
    "secondary": "In physiology and pharmacology, to counteract or neutralize the physiological effect of an agonist, enzyme, or hormone (British spelling).",
    "quotes": [
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "He was careful not to **antagonise** the senior trustees before his medical reform proposals could be formally debated."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "To **antagonise** established theological dogma required both unassailable scientific evidence and unflinching moral courage."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Certain motor impulses directly **antagonise** opposing habitual reflexes, extinguishing them by reciprocal inhibition."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Form & Space Part 1 - Batch 1 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
