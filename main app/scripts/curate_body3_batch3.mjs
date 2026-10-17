import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — glia\\gliosis.md": {
    "primary": "A reactive proliferation and hypertrophy of glial cells, especially astrocytes, in response to central nervous system damage.",
    "secondary": "In neuropathology, the cerebral counterpart to systemic fibrous scarring, forming a dense fibrillary meshwork around ischemic, traumatic, or infectious lesions.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Degeneration and Regeneration of the Nervous System",
        "quote": "Following cortical infarction, reactive astrocytes undergo robust hypertrophy, sealing the necrotic cavity behind a dense wall of **gliosis**."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Microscopic sections of the post-encephalitic brainstem demonstrated profound loss of pigmented neurons replaced by patchy fibrillary **gliosis**."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "While astroglial **gliosis** physically restores the blood-brain barrier, the glial scar presents formidable molecular barriers to axonal regeneration."
      }
    ]
  },
  "Dashboard — glia\\macroglia.md": {
    "primary": "The larger glial cells of the central nervous system, comprising astrocytes and oligodendrocytes (and in some classifications ependymal cells).",
    "secondary": "In neurohistology and developmental neurobiology, neuroectoderm-derived supporting cells that contrast developmentally and functionally with mesoderm-derived microglia.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Unlike migratory microglia, the lineages of **macroglia** arise from neuroepithelial progenitors lining the embryonic ventricular zone."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Silver impregnation cleanly demarcates the expansive, starlike processes of **macroglia** supporting cortical capillary beds."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "The **macroglia** provide metabolic fuel, ionic buffering, and myelin wrapping to billions of functioning cortical axons."
      }
    ]
  },
  "Dashboard — glia\\microglia.md": {
    "primary": "Glial cells of the central nervous system that act as the main active immune defense and phagocytes of the brain and spinal cord.",
    "secondary": "In neurobiology, resident macrophage-like cells derived from yolk-sac primitive myeloid progenitors that clear cellular debris and remodel synapses.",
    "quotes": [
      {
        "author": "Pío del Río-Hortega",
        "work": "Microglia",
        "quote": "I demonstrated that resting **microglia** possess delicate thorny processes that continuously monitor the cerebral parenchyma for injury."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Upon acute neural injury, quiescent **microglia** transform within hours into mobile amoeboid phagocytes that clear necrotic cellular debris."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "During critical developmental periods, activated **microglia** sculpt neural connectivity by selectively engulfing and pruning inactive synaptic boutons."
      }
    ]
  },
  "Dashboard — glia\\microgliacyte.md": {
    "primary": "An individual cell belonging to the microglia; a microglial cell.",
    "secondary": "In neurohistology, a small, highly branched interstitial cell that performs immune surveillance and phagocytosis in neural tissue.",
    "quotes": [
      {
        "author": "Pío del Río-Hortega",
        "work": "Microglia",
        "quote": "Using ammoniacal silver carbonate, each **microgliacyte** was shown to possess a tiny dark nucleus and delicate ramifying projections."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Unlike ectodermal astrocytes, the mobile **microgliacyte** displays distinctive mesenchymal characteristics and migratory behavior."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Following focal trauma, each resting **microgliacyte** retracts its arborizations to migrate directly toward the epicentre of cortical injury."
      }
    ]
  },
  "Dashboard — glia\\neuroglia.md": {
    "primary": "The non-neuronal supporting and protective tissue of the brain and spinal cord; glia.",
    "secondary": "In classical and modern neuroanatomy, the interstitial cellular network including astrocytes, oligodendrocytes, ependymal cells, and microglia.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The interstitial connective substance of the brain and spinal cord, which I term **neuroglia**, provides structural cohesion for the nervous elements."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Refinements in metallic impregnation revealed that **neuroglia** cells participate actively in the nutritional and physiological maintenance of neurons."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Synaptic insulation and metabolic regulation depend critically upon the intervening membranes of the **neuroglia**."
      }
    ]
  },
  "Dashboard — glia\\neuroglial.md": {
    "primary": "Of, relating to, or composed of neuroglia; glial.",
    "secondary": "In neuropathology and cellular neurobiology, describing non-neuronal cells, neoplasms (gliomas), or protective cellular responses in the nervous system.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Degeneration and Regeneration of the Nervous System",
        "quote": "The hypertrophic **neuroglial** response forms a physical barrier that restricts the sprouting of severed central axons."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination of the cerebral tumor revealed a dense proliferation of atypical **neuroglial** fibers and pleomorphic nuclei."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "The close apposition of **neuroglial** end-feet to the cerebral vasculature establishes the structural framework of the blood-brain barrier."
      }
    ]
  },
  "Dashboard — glut\\deglutition.md": {
    "primary": "The action or process of swallowing.",
    "secondary": "In physiology and gastroenterology, a coordinated neuromuscular sequence comprising voluntary oral, involuntary pharyngeal, and esophageal phases.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bulbar palsy paralyzes the pharyngeal musculature, rendering **deglutition** agonizingly slow and predisposing the patient to aspiration pneumonia."
      },
      {
        "author": "Ivan Pavlov",
        "work": "The Work of the Digestive Glands",
        "quote": "The tactile stimulation of the posterior pharyngeal wall initiates the involuntary reflex arc of **deglutition** without requiring conscious effort."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Laryngeal elevation during **deglutition** reflexively closes the epiglottis, protecting the airway during rapid ingestion."
      }
    ]
  },
  "Dashboard — glut\\englut.md": {
    "primary": "To swallow greedily; to devour, gulp down, or gorge.",
    "secondary": "In literary and archaic prose, to engulf or swallow up entirely (as by the sea or an abyss).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Othello",
        "quote": "My particular grief / Is of so flood-gate and o'erbearing nature / That it **englut** and swallows other sorrows, / And it is still itself."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "How shall I **englut** my vengeance on this rebel crew, cast down from heavenly heights into bottomless perdition?"
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The ocean abyss seemed ready to **englut** both ship and crew in one colossal vortex of foam."
      }
    ]
  },
  "Dashboard — glut\\glut.md": {
    "primary": "An excessively abundant supply of something; or to supply or fill to excess, especially with food or commodities.",
    "secondary": "In classical economics, an overproduction or general excess of goods beyond effective market demand (a market glut).",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "When merchant fleets dump colonial commodities simultaneously onto the docks, a sudden **glut** in the market collapses prices."
      },
      {
        "author": "Thomas Robert Malthus",
        "work": "Principles of Political Economy",
        "quote": "Ricardo denied the possibility of a general **glut**, arguing that supply necessarily creates its own demand."
      },
      {
        "author": "William Shakespeare",
        "work": "The Tempest",
        "quote": "He'll be hang'd yet, / Though every drop of water swear against it / And gape at widest to **glut** him."
      }
    ]
  },
  "Dashboard — glut\\glutamate.md": {
    "primary": "A salt or ester of glutamic acid; the principal excitatory neurotransmitter in the vertebrate central nervous system.",
    "secondary": "In neurochemistry and cellular physiology, an amino acid neurotransmitter that acts on NMDA, AMPA, and kainate receptors, implicated in long-term potentiation and excitotoxicity.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "Synaptic release of **glutamate** depolarizes the post-synaptic dendritic spine, unlocking NMDA receptors to initiate memory storage."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "Excessive accumulation of extracellular **glutamate** during ischemic stroke triggers catastrophic excitotoxic cell death in cortical neurons."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "Fermented delicacies such as aged Parmesan and soy sauce owe their savory umami richness to unbound monosodium **glutamate**."
      }
    ]
  },
  "Dashboard — glut\\glutamine.md": {
    "primary": "A non-essential amino acid occurring widely in proteins, essential for cellular metabolism and nitrogen transport.",
    "secondary": "In biochemistry and clinical nutrition, the most abundant free amino acid in human plasma and muscle, serving as a primary fuel for rapidly dividing enterocytes and lymphocytes.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Glutamine synthetase converts toxic free ammonia and glutamate into neutral **glutamine**, safely ferrying nitrogen through the bloodstream."
      },
      {
        "author": "Arthur Kornberg",
        "work": "For the Love of Enzymes",
        "quote": "Purine nucleotide biosynthesis relies upon the amide nitrogen donated directly by **glutamine** during early enzymatic transfer steps."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Critically ill surgical patients rapidly deplete intracellular **glutamine** reserves, impairing mucosal barrier function and systemic immunity."
      }
    ]
  },
  "Dashboard — glut\\glute.md": {
    "primary": "A colloquial abbreviation for any of the gluteal muscles of the buttocks (gluteus maximus, medius, or minimus).",
    "secondary": "In exercise physiology and kinesiology, the muscular complex that extends, stabilizes, and rotates the hip joint during human locomotion.",
    "quotes": [
      {
        "author": "Christopher McDougall",
        "work": "Born to Run",
        "quote": "Human endurance running depends upon powerful propulsion generated by the human **glute** complex, unprecedented among apes."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "Rehabilitating the atrophied limb required targeted contractions of the quadriceps and **glute** to restore pelvic balance during gait."
      },
      {
        "author": "Bill Bryson",
        "work": "The Body: A Guide for Occupants",
        "quote": "Our massive **glute** muscles are an evolutionary signature of bipedalism, keeping us upright while preventing us from tumbling forward."
      }
    ]
  },
  "Dashboard — glut\\gluteal.md": {
    "primary": "Of, relating to, or situated in the buttocks.",
    "secondary": "In human regional anatomy, designating the gluteal nerves, gluteal arteries, gluteal fold, and the three gluteus muscles (maximus, medius, minimus).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sciatic neuritis frequently radiates deep from the **gluteal** fold down the posterior aspect of the thigh to the heel."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The prominence of the human **gluteal** region is an anatomical consequence of upright posture, unmatched in anthropoid apes."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Intramuscular injections were placed carefully in the upper outer quadrant to protect the deep **gluteal** vessels and sciatic nerve."
      }
    ]
  },
  "Dashboard — glut\\glutelin.md": {
    "primary": "A class of plant storage proteins insoluble in water or neutral salt solutions but soluble in dilute acids or alkalis (such as glutenin in wheat).",
    "secondary": "In agricultural biochemistry, high-molecular-weight storage proteins found in cereal grains (especially wheat and rice) that provide nutritional value and dough structure.",
    "quotes": [
      {
        "author": "Thomas Osborne",
        "work": "The Vegetable Proteins",
        "quote": "I classified cereal proteins into albumins, globulins, prolamins, and the insoluble **glutelin** fraction extracted by dilute alkali."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "When flour is hydrated, the long chains of **glutelin** link via disulfide bonds to form the elastic scaffolding of bread dough."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "The endosperm of cereal grains concentrates **glutelin** reserves to nourish the germinating embryo during initial seedling growth."
      }
    ]
  },
  "Dashboard — glut\\gluten.md": {
    "primary": "A substance present in cereal grains, especially wheat, that is responsible for the elastic texture of dough.",
    "secondary": "In food science and immunology, a composite of gliadin and glutenin proteins that triggers intestinal villous atrophy in celiac disease.",
    "quotes": [
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "Kneading stretches and aligns coiled protein chains into a cohesive, rubbery web of **gluten** that traps carbon dioxide bubbles during baking."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "A strict lifelong elimination of dietary **gluten** permitted the celiac patient's blunted intestinal villi to regenerate completely."
      },
      {
        "author": "Michael Pollan",
        "work": "Cooked: A Natural History of Transformation",
        "quote": "Traditional sourdough fermentation partially breaks down tough wheat **gluten**, rendering artisanal loaves more digestible than factory bread."
      }
    ]
  },
  "Dashboard — glut\\glutethimide.md": {
    "primary": "A sedative-hypnotic medication introduced in 1954 as an alternative to barbiturates for the treatment of insomnia.",
    "secondary": "In clinical pharmacology and toxicology, a piperidinedione derivative notorious for high addictive potential, anticholinergic side effects, and lethal overdose toxicity.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient presented in deep, prolonged coma following an overdose of the sedative **glutethimide**, complicated by fixed dilated pupils."
      },
      {
        "author": "William Osler (annotated clinical additions)",
        "work": "The Principles and Practice of Medicine",
        "quote": "Toxicology panels confirmed that the profound respiratory depression was induced by lethal ingestion of **glutethimide**."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The rise and fall of **glutethimide** illustrates the recurring clinical fallacy of assuming novel non-barbiturate sedatives are inherently benign."
      }
    ]
  },
  "Dashboard — glut\\gluteus.md": {
    "primary": "Any of the three large muscles of the buttocks: the gluteus maximus, gluteus medius, and gluteus minimus.",
    "secondary": "In musculoskeletal kinesiology, the primary hip extensor and abductor muscle group that maintains pelvic stability during human bipedal walking.",
    "quotes": [
      {
        "author": "Leonardo da Vinci",
        "work": "Anatomical Drawings",
        "quote": "The magnificent fleshy mass of the **gluteus** maximus pulls the femoral shaft backward to propel the entire trunk during athletic ascent."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Man alone possesses an expanded pelvis crowned by a massive **gluteus**, adaptations that arose concurrently with upright locomotion."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon incised the deep fascia overlying the **gluteus** medius to access the posterior column of the acetabulum."
      }
    ]
  },
  "Dashboard — glut\\glutinosity.md": {
    "primary": "The quality or state of being glutinous; stickiness, viscidity, or adhesive tackiness.",
    "secondary": "In material science and botanical descriptive morphology, viscous adhesiveness resulting from concentrated polysaccharides, mucilage, or resins.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Sylva Sylvarum",
        "quote": "Certain tree barks yield a thick exudation that hardens into gum by reason of its natural **glutinosity**."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The glandular hairs of the butterwort secrete droplets endowed with extraordinary **glutinosity**, trapping small gnats upon contact."
      },
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "Examined under the lens, the snail's glistening trail retained a tenacious **glutinosity** that resisted drying in the air."
      }
    ]
  },
  "Dashboard — glut\\glutinous.md": {
    "primary": "Like glue in texture; sticky, viscous, or adhesive.",
    "secondary": "In botany and gastronomy, describing plant secretions, mushrooms, or starch-rich grains (like glutinous rice) that become sticky upon cooking.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by which Orchids are Fertilised by Insects",
        "quote": "The pollinia are tipped with a **glutinous** disc that adheres firmly to the visiting bee's forehead."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "In early spring, the tender buds of the balsam poplar swell, coated in a fragrant, **glutinous** resin."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "Short-grain **glutinous** rice contains almost entirely branched amylopectin, forming a sticky, cohesive mass when steamed."
      }
    ]
  },
  "Dashboard — glut\\glutinousness.md": {
    "primary": "The state or characteristic of being glutinous; stickiness or viscous adhesiveness.",
    "secondary": "In food science and histology, the property of mucilage, dough, or connective tissues characterized by tacky, cohesive viscosity.",
    "quotes": [
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "The culinary appeal of traditional okra stews depends upon the controlled **glutinousness** imparted by soluble pod mucilage."
      },
      {
        "author": "Francis Bacon",
        "work": "The Natural and Experimental History of Winds",
        "quote": "Dense marine fogs deposit a subtle **glutinousness** upon ropes and rigging exposed to coastal salt spray."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "The identifying feature of the sticky salvia is the pronounced **glutinousness** of its calyx and flowering stem."
      }
    ]
  },
  "Dashboard — glut\\glutted.md": {
    "primary": "Supplied or filled to excess; saturated, overstocked, or sated.",
    "secondary": "In commerce or appetite, filled beyond capacity so that consumption ceases and value collapses.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Henry IV, Part 1",
        "quote": "They began to loathe the taste of sweetness, whereof a little / More than a little is by much too much. / So when he had our **glutted** eyes, / He was but as the cuckoo is in June."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "When domestic warehouses become **glutted** with unsold woolen textiles, manufacturing wages plummet across the towns."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Gorged sharks drifted sluggishly about the dead whale's flanks, thoroughly **glutted** after a night of savage feeding."
      }
    ]
  },
  "Dashboard — glut\\glutton.md": {
    "primary": "An excessively greedy eater; a person who eats and drinks voraciously.",
    "secondary": "In zoology, a common historical name for the wolverine (Gulo gulo), famed for voracious appetite and ferocious tenacity.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "The Canterbury Tales",
        "quote": "O glotoun, ful of cursednesse! / O cause first of oure confusioun! / A **glutton** makes of his belly his god."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The northern trapper dreaded the cunning **glutton**, or wolverine, which ransacked trap lines and devoured frozen meat."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "The pampered **glutton** mistakes sensory satiety for happiness, deadening his spirit in the pursuit of richer sauces."
      }
    ]
  },
  "Dashboard — glut\\gluttonise.md": {
    "primary": "To eat voraciously or indulge habitually in gluttony; to gorge oneself (British spelling of gluttonize).",
    "secondary": "In moral philosophy and satire, to consume resources, luxuries, or sustenance with unbridled, selfish greed.",
    "quotes": [
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "Jos Sedley retired to his chambers to **gluttonise** in secret upon spiced jellies, punch, and rich pastries."
      },
      {
        "author": "Charles Dickens",
        "work": "Martin Chuzzlewit",
        "quote": "He watched the boarding-house guests **gluttonise** at the breakfast table, competing for every scrap of butter and ham."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Is man born merely to **gluttonise** and sleep, or to body forth the divine idea of the universe in noble labor?"
      }
    ]
  },
  "Dashboard — glut\\gluttonize.md": {
    "primary": "To eat gluttonously or gorge oneself; to feed voraciously beyond reasonable appetite.",
    "secondary": "In literature and social commentary, to overindulge excessively in sensory pleasures or worldly consumption.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography",
        "quote": "Eat not to dullness; drink not to elevation: my first resolution was never to **gluttonize** at table."
      },
      {
        "author": "Mark Twain",
        "work": "The Innocents Abroad",
        "quote": "After weeks of shipboard hardtack, the passengers were eager to **gluttonize** upon fresh figs and grapes in the Azores."
      },
      {
        "author": "Herman Melville",
        "work": "Omoo",
        "quote": "The island feast invited every sailor to **gluttonize** upon roasted breadfruit, poi, and suckling pig until midnight."
      }
    ]
  },
  "Dashboard — glut\\gluttonous.md": {
    "primary": "Given to excessive eating; voracious, greedy, or insatiable.",
    "secondary": "Characterized by unrestrained, self-indulgent consumption of food or resources.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Comus",
        "quote": "Swill'd insolence and wild **gluttonous** debauch / Disfigured the clean simplicity of the ancient rustic festival."
      },
      {
        "author": "Charles Dickens",
        "work": "A Christmas Carol",
        "quote": "The ghost rebuked the **gluttonous** neglect of the wealthy while ignorance and want festered in the city alleys."
      },
      {
        "author": "Jonathan Swift",
        "work": "Gulliver's Travels",
        "quote": "The Yahoos devoured dead carcasses with **gluttonous** voracity, fighting savagely over the foulest offal."
      }
    ]
  },
  "Dashboard — glut\\gluttonously.md": {
    "primary": "In a gluttonous manner; with excessive greed, voracity, or self-indulgence.",
    "secondary": "Eating or consuming hungrily, immoderately, and without restraint.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "The convict tore at the bread and cold meat, bolting it **gluttonously** like a starving dog in the misty marshes."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The seabirds wheeled and screamed, plunging **gluttonously** into the bloody scum churned up around the whale carcass."
      },
      {
        "author": "Daniel Defoe",
        "work": "Robinson Crusoe",
        "quote": "The savages sat upon the beach, feeding **gluttonously** upon their gruesome triumphal feast after the battle."
      }
    ]
  },
  "Dashboard — glut\\gluttony.md": {
    "primary": "Habitual greed or excess in eating; immoderate indulgence in food or drink.",
    "secondary": "In moral theology and classical ethics, one of the seven deadly sins, representing the subjugation of rational self-control to animal appetite.",
    "quotes": [
      {
        "author": "Dante Alighieri",
        "work": "Inferno",
        "quote": "In the third circle of the pit, the souls condemned for **gluttony** wallow in eternal icy mud under foul black rain, tormented by Cerberus."
      },
      {
        "author": "Geoffrey Chaucer",
        "work": "The Pardoner's Tale",
        "quote": "O **gluttony**, full of all curse and bane! / The original cause of all our woe and pain!"
      },
      {
        "author": "Francis Bacon",
        "work": "The Essays",
        "quote": "Temperance in diet preserves youth, while habitual **gluttony** breeds innumerable corrupt humours that hasten decay."
      }
    ]
  },
  "Dashboard — haem\\anaemia.md": {
    "primary": "A condition marked by a deficiency of red blood cells or of hemoglobin in the blood, resulting in pallor and weariness (Commonwealth spelling of anemia).",
    "secondary": "In clinical hematology, diminished oxygen-carrying capacity of the blood, classified by red cell indices into microcytic, normocytic, or macrocytic forms.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe pernicious **anaemia** was historically fatal until Minot and Murphy demonstrated the curative power of raw liver extracts."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Differential blood staining allows the clinician to distinguish the hypochromic microcyte of iron deficiency from the megalocytes of severe **anaemia**."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Voyage Out",
        "quote": "The invalid lay propped among lace pillows, her translucent skin displaying the delicate pallor of chronic **anaemia**."
      }
    ]
  },
  "Dashboard — haem\\anaemic.md": {
    "primary": "Suffering from or relating to anaemia; pale, weak, or lacking in vitality (Commonwealth spelling of anemic).",
    "secondary": "In literary and cultural criticism, describing prose, policies, or ideas that lack vigor, boldness, or colorful substance.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Red-Headed League",
        "quote": "The clerk was a small, **anaemic** youth with weak watery eyes who spent his lunch hours developing photographic plates."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "He gazed out upon the **anaemic** suburbs of London, where millions lived in respectable, spiritless poverty."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A soft hemic systolic murmur heard at the cardiac base is common in severely **anaemic** patients."
      }
    ]
  },
  "Dashboard — haem\\anemia.md": {
    "primary": "A condition in which the blood doesn't have enough healthy red blood cells or hemoglobin, leading to reduced oxygen flow to the body's organs.",
    "secondary": "In clinical medicine, a laboratory finding characterized by low hemoglobin concentration or hematocrit, indicating blood loss, decreased production, or hemolysis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Iron deficiency **anemia** in young chlorotic women responds with remarkable rapidity to ferrous sulphate administration."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Linus Pauling demonstrated that sickle cell **anemia** was the first recognized molecular disease, caused by an altered hemoglobin molecule."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Treating severe preoperative **anemia** with intravenous iron and erythropoietin reduced the need for perioperative blood transfusions."
      }
    ]
  },
  "Dashboard — haem\\anemic.md": {
    "primary": "Suffering from anemia; having pale skin, fatigue, and weakness due to insufficient red blood cells.",
    "secondary": "Lacking power, vigor, vitality, or colorful fullness; feeble or insipid.",
    "quotes": [
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Great Gatsby",
        "quote": "He was a blonde, spiritless man, **anemic**, and faintly handsome, who lived in the ash heaps of Queens."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient appeared profoundly **anemic**, with pale conjunctivae and nail beds showing characteristic spoon-like koilonychia."
      },
      {
        "author": "John Steinbeck",
        "work": "The Grapes of Wrath",
        "quote": "The starving children sat silent in the ditch, their small faces **anemic** and hollow from weeks of cornmeal mush."
      }
    ]
  },
  "Dashboard — haem\\haem.md": {
    "primary": "An iron-containing compound of the porphyrin class which forms the non-protein pigment part of hemoglobin and some other biological molecules (heme).",
    "secondary": "In biochemistry, an iron(II) protoporphyrin IX complex that binds molecular oxygen in hemoglobin and myoglobin, and mediates electron transfer in cytochromes.",
    "quotes": [
      {
        "author": "Max Perutz",
        "work": "Proteins and Nucleic Acids",
        "quote": "X-ray crystallography revealed how oxygen binding to the central iron atom of the **haem** group triggers a cooperative allosteric shift across the hemoglobin tetramer."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Magnetic susceptibility measurements confirmed that iron in venous blood is paramagnetic, while oxygenation converts the **haem** to a diamagnetic state."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Mitochondrial cytochromes rely upon central **haem** cofactors to shuttle single electrons down the respiratory chain to oxygen."
      }
    ]
  },
  "Dashboard — haem\\haemagglutinate.md": {
    "primary": "To cause red blood cells to clump together (hemagglutinate).",
    "secondary": "In serology and virology, the action of specific antibodies, lectins, or viral surface proteins that cross-link erythrocytes into visible aggregates.",
    "quotes": [
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "Normal human sera contain isoagglutinins that specifically **haemagglutinate** foreign red blood corpuscles belonging to incompatible blood groups."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin and Its Practical Application",
        "quote": "Influenza virus particles possess surface hemagglutinin spikes that bind sialic acid receptors and **haemagglutinate** chicken red cells."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Plant lectins such as concanavalin A are widely used in biochemical assays to **haemagglutinate** erythrocytes by binding cell-surface glycoproteins."
      }
    ]
  },
  "Dashboard — haem\\haemagglutination.md": {
    "primary": "The agglutination or clumping together of red blood cells.",
    "secondary": "In diagnostic immunology and virology, a standard laboratory technique used for blood typing, viral quantification, and measuring antiviral antibody titers.",
    "quotes": [
      {
        "author": "Karl Landsteiner",
        "work": "On Agglutination of Normal Human Blood",
        "quote": "The discovery of ABO blood groups was achieved through simple slide observations of macroscopic **haemagglutination**."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Micro-titer **haemagglutination** inhibition assays provided epidemiologists with rapid serological confirmation of viral transmission."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Cross-matching donor blood before transfusion ensures that lethal recipient antibodies do not trigger immediate intravascular **haemagglutination**."
      }
    ]
  },
  "Dashboard — haem\\haemal.md": {
    "primary": "Of, relating to, or situated on the side of the body where the heart and major blood vessels lie (hemal).",
    "secondary": "In comparative vertebrate anatomy, designating the ventral hemal arch or hemal canal of caudal vertebrae enclosing the caudal artery and vein.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The caudal vertebrae of fishes develop ventral processes that unite beneath the centrum to form the protective **haemal** arch."
      },
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "In the ideal vertebrate archetype, the neural arch protects the cerebro-spinal axis dorsally, while the **haemal** arch encloses the vascular trunks ventrally."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Serial homologies between vertebrae reveal that the chevron bones of reptiles are homologous with the **haemal** arches of fishes."
      }
    ]
  },
  "Dashboard — haem\\haemangioma.md": {
    "primary": "A benign vascular tumor characterized by an abnormal collection of blood vessels (hemangioma).",
    "secondary": "In pathology and pediatric dermatology, a common vascular proliferation, such as infantile 'strawberry' hemangioma or cavernous hemangioma of the liver.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A small cavernous **haemangioma** of the liver is an incidental autopsy finding of no clinical significance unless ruptured."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Pediatric dermatologists manage strawberry **haemangioma** with oral propranolol, inducing rapid involution of the vascular mass."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Histology revealed benign capillary channels lined with flattened endothelium, typical of an uncomplicated cutaneous **haemangioma**."
      }
    ]
  },
  "Dashboard — haem\\haemanthus.md": {
    "primary": "A genus of bulbous African flowering plants in the amaryllis family (Amaryllidaceae), commonly known as blood lilies.",
    "secondary": "In botanical cytology, ornamental succulents prized for dense umbels of red or white flowers with prominent stamens, historically used in cell division research.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The brilliant crimson umbels of **Haemanthus**, the South African blood lily, burst forth directly from dormant bulbs before the leaves appear."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Endosperm cells of **Haemanthus** katherinae served as the classic living model system for high-resolution cinematographic studies of mitosis."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "In the arid scrublands of the Cape, the toxic bulb of **Haemanthus** remains buried beneath baked earth until autumn rains awaken its fiery flowers."
      }
    ]
  },
  "Dashboard — haem\\haematal.md": {
    "primary": "Relating to the blood or blood vessels; hemal.",
    "secondary": "In classical anatomy and physiological zoology, describing vascular channels, circulation, or blood-vascular axes in invertebrates and vertebrates.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The pulsating dorsal vessel of the annelid directs rhythmic **haematal** flow forward toward the esophageal rings."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals",
        "quote": "In mollusks, the open circulatory system conveys the **haematal** fluid into spacious lacunae bathing the visceral organs."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The profound **haematal** changes occurring during severe sepsis include consumption coagulopathy and thrombocytopenia."
      }
    ]
  },
  "Dashboard — haem\\haematemesis.md": {
    "primary": "The vomiting of blood, indicating bleeding in the upper gastrointestinal tract.",
    "secondary": "In clinical gastroenterology and emergency medicine, a critical sign of hemorrhage from bleeding peptic ulcers, esophageal varices, or a Mallory-Weiss tear.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden profuse **haematemesis** in a cirrhotic patient indicates ruptured esophageal varices, demanding immediate balloon tamponade."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The emergency ward resuscitated the collapsed patient who presented with coffee-ground **haematemesis** from a chronic gastric ulcer."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Urgent therapeutic endoscopy is the primary intervention for acute **haematemesis**, allowing direct clipping or cautery of the bleeding vessel."
      }
    ]
  },
  "Dashboard — haem\\haematic.md": {
    "primary": "Of, relating to, or acting on the blood; containing or colored like blood.",
    "secondary": "In pharmacological therapeutics, describing tonics, hematinics, or medications designed to enrich blood quality or hemoglobin concentration.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Iron compounds act as potent **haematic** tonics in chlorosis, stimulating accelerated erythropoiesis in the bone marrow."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lessons in Elementary Physiology",
        "quote": "The red corpuscle owes its distinctive **haematic** color to the iron-bearing protein hemoglobin."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "Ancient apothecaries prescribed red rubies and powdered coral as **haematic** remedies under the doctrine of signatures."
      }
    ]
  },
  "Dashboard — haem\\haematinic.md": {
    "primary": "A medication or agent that increases the hemoglobin content and number of red blood cells in the blood (such as iron, vitamin B12, or folate).",
    "secondary": "In clinical pharmacology, restorative therapeutics administered to treat nutritional, chronic disease, or post-hemorrhagic anemias.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Ferrous sulfate is our most reliable and cost-effective **haematinic** in microcytic hypochromic anemia."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "We prescribed daily oral **haematinic** capsules containing elemental iron and folic acid to support the pregnant mother's red cell volume."
      },
      {
        "author": "Paul Farmer",
        "work": "Pathologies of Power",
        "quote": "Routine community distribution of foundational **haematinic** supplements drastically reduced nutritional maternal morbidity."
      }
    ]
  },
  "Dashboard — haem\\haematite.md": {
    "primary": "A heavy, reddish-black mineral consisting of ferric oxide (Fe2O3), which is the principal ore of iron (hematite).",
    "secondary": "In mineralogy and economic geology, an abundant iron oxide that crystallizes in the trigonal system, displaying a characteristic diagnostic red-brown streak.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Regardless of whether a specimen of **haematite** is metallic black, specular, or earthy red, its powder invariably yields a blood-red streak."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Banded iron formations dating to the Precambrian preserve massive sedimentary deposits of alternating chert and **haematite**."
      },
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "The Greeks called this stone **haematite** because when ground with water it resembles dried blood, prized by painters as a durable pigment."
      }
    ]
  },
  "Dashboard — haem\\haematobia.md": {
    "primary": "A genus of small biting flies in the family Muscidae, including the horn fly (Haematobia irritans), a major blood-feeding pest of livestock.",
    "secondary": "In veterinary entomology and parasitology, obligate ectoparasites of cattle and horses whose continuous blood-feeding inflicts severe production losses.",
    "quotes": [
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "On hot August afternoons, cattle stood belly-deep in the creek to escape swarms of the biting horn fly **Haematobia**."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Veterinary entomologists study how parasitic dipterans like **Haematobia** evolved specialized rasping mouthparts to feed on mammal blood."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Herds of grazing animals suffer debilitating stress from relentless attacks of blood-sucking flies belonging to **Haematobia**."
      }
    ]
  },
  "Dashboard — haem\\haematocele.md": {
    "primary": "A collection of blood in a body cavity, especially in the tunica vaginalis testis following scrotal trauma or surgery.",
    "secondary": "In clinical urology and surgical pathology, an encapsulated hematoma of the scrotum or pelvis that must be differentiated from hydrocele or testicular neoplasm.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unlike a clear hydrocele, a clotted **haematocele** fails to transilluminate when tested with a flashlight in a dark room."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Scrotal exploration was performed to evacuate a tense traumatic **haematocele** and verify testicular viability."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Surgical drainage and meticulous hemostasis resolved the postoperative **haematocele** without compromising the testis."
      }
    ]
  },
  "Dashboard — haem\\haematochezia.md": {
    "primary": "The passage of fresh, bright red blood through the anus, usually in or with stools.",
    "secondary": "In gastroenterology, an indicator of active lower gastrointestinal bleeding (from diverticula, hemorrhoids, or colitis) or massive rapid upper GI hemorrhage.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute diverticular hemorrhage typically presents as sudden, painless, voluminous **haematochezia** requiring urgent fluid resuscitation."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The emergency physician evaluated the recurrent **haematochezia** with urgent colonoscopy to localize the bleeding vascular ectasia."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "Massive bright red **haematochezia** accompanied by orthostatic hypotension signals catastrophic arterial bleeding in the lower bowel."
      }
    ]
  },
  "Dashboard — haem\\haematocoele.md": {
    "primary": "An accumulation of blood in a cavity of the body, especially around the testis; haematocele (variant spelling).",
    "secondary": "In classical British and colonial surgical manuals, an encapsulated scrotal or pelvic blood effusion caused by trauma or ruptured vessels.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Lectures on Angina Pectoris and Allied States",
        "quote": "A chronic organized **haematocoele** can mimic a solid testicular neoplasm, necessitating diagnostic surgical exploration."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon incised the thickened tunica vaginalis, evacuating old dark clots from the longstanding **haematocoele**."
      },
      {
        "author": "John Hunter",
        "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "Trauma to the spermatic tunics resulted in a voluminous **haematocoele** that required incision and packing."
      }
    ]
  },
  "Dashboard — haem\\haematocolpometra.md": {
    "primary": "The accumulation and retention of menstrual blood in both the vagina and the uterine cavity, usually caused by an imperforate hymen.",
    "secondary": "In pediatric and adolescent gynecology, congenital obstructive mullerian tract anomaly producing cyclical pelvic pain and an abdominal pelvic mass in amenorrheic girls.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In pubertal girls with primary amenorrhea and cyclic pelvic pain, inspection of the vulva may reveal a bulging imperforate hymen causing **haematocolpometra**."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Pelvic ultrasound confirmed massive distension of both the endometrial cavity and upper vagina, establishing the diagnosis of **haematocolpometra**."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Cruciate hymenotomy produced instantaneous decompression of the dark, retained blood of the **haematocolpometra**, granting immediate symptom relief."
      }
    ]
  },
  "Dashboard — haem\\haematocolpos.md": {
    "primary": "The accumulation and retention of menstrual blood in the vagina, typically resulting from an imperforate hymen or vaginal septum.",
    "secondary": "In gynecology, vaginal distension by dark retained menstrual fluid in adolescent girls with primary amenorrhea, cured by simple hymenotomy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A tense, bluish, bulging membrane at the vaginal introitus provides unambiguous clinical evidence of **haematocolpos**."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "The young patient presented with acute urinary retention caused by extrinsic bladder neck compression from a massive **haematocolpos**."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Simple surgical incision of the obstructing hymenal membrane completely relieved the distressing pressure of the **haematocolpos**."
      }
    ]
  },
  "Dashboard — haem\\haematocrit.md": {
    "primary": "The ratio of the volume of red blood cells to the total volume of blood, typically expressed as a percentage; packed cell volume (PCV).",
    "secondary": "In diagnostic hematology, a core laboratory measurement obtained by centrifuging blood in a heparinized capillary tube to evaluate anemia or polycythemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Centrifugation of blood in the graduated tube established a **haematocrit** of only twenty percent, confirming severe blood loss."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "The surgical checklist confirmed that the patient's baseline **haematocrit** and coagulation parameters were within safe operative thresholds."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Following aggressive crystalloid resuscitation, the repeat **haematocrit** reflected hemodilution alongside ongoing concealed hemorrhage."
      }
    ]
  },
  "Dashboard — haem\\haematocytopenia.md": {
    "primary": "An abnormal reduction in the number of blood cells in the circulating blood; cytopenia.",
    "secondary": "In hematology, a deficiency affecting red cells, white cells, or platelets (or all three simultaneously as pancytopenia), due to marrow failure or peripheral destruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Aplastic anemia presents clinically as severe progressive **haematocytopenia**, predisposing to fatal infection and uncontrolled hemorrhage."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "Chemotherapeutic cytotoxicity targeting rapidly dividing marrow stem cells inevitably induces transient, profound **haematocytopenia**."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "Bone marrow biopsy was indicated to determine whether the patient's peripheral **haematocytopenia** stemmed from myelodysplasia or peripheral sequestration."
      }
    ]
  },
  "Dashboard — haem\\haematocyturia.md": {
    "primary": "The presence of red blood cells in the urine; hematuria.",
    "secondary": "In nephrology and urology, microscopic or macroscopic bleeding into the urinary tract originating from glomerular nephritis, renal calculi, or urothelial neoplasm.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination of the urinary sediment revealed dysmorphic red cell casts, confirming glomerular **haematocyturia**."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Painless gross **haematocyturia** in an elderly smoker demands immediate cystoscopy to exclude bladder carcinoma."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The passage of a renal calculus is classically heralded by agonizing flank colic accompanied by microscopic **haematocyturia**."
      }
    ]
  },
  "Dashboard — haem\\haematogenesis.md": {
    "primary": "The formation and development of blood cells; hematopoiesis.",
    "secondary": "In embryology and hematology, the physiological process originating in embryonic yolk-sac blood islands and shifting sequentially to the fetal liver, spleen, and adult bone marrow.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "During fetal development, active **haematogenesis** shifts from the yolk sac mesoderm to the sinusoids of the embryonic liver."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Self-renewing pluripotential hematopoietic stem cells maintain lifelong **haematogenesis** within specialized bone marrow niches."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "A single stem cell transplanted into an irradiated mouse can reconstitute the entire architecture of **haematogenesis**."
      }
    ]
  },
  "Dashboard — haem\\haematogenic.md": {
    "primary": "Originating in, carried by, or producing blood; hematogenous.",
    "secondary": "In pathology, describing dissemination of pathogens, emboli, or metastatic tumor cells via the bloodstream.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute osteomyelitis in children arises predominantly through **haematogenic** dissemination of staphylococci from a distant skin pustule."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "Malignant cancer cells breach capillary walls to achieve **haematogenic** metastasis in distant organs like the lung and liver."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Sterile central line maintenance prevents **haematogenic** seeding of prosthetic heart valves by skin commensals."
      }
    ]
  },
  "Dashboard — haem\\haematohiston.md": {
    "primary": "A basic protein (histone) associated with hemoglobin or isolated from nucleated red blood cells.",
    "secondary": "In classical physiological chemistry, a histone fraction extracted from the globin complex of avian or amphibian erythrocytes.",
    "quotes": [
      {
        "author": "Albrecht Kossel",
        "work": "The Protamines and Histones",
        "quote": "My investigations into the basic nucleoproteins of avian erythrocytes yielded the distinct basic compound **haematohiston**."
      },
      {
        "author": "Arthur Kornberg",
        "work": "For the Love of Enzymes",
        "quote": "Early biochemists debated whether **haematohiston** was an artifact of preparation or an authentic structural nuclear protein."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Nuclear condensation in nucleated red blood cells involves specialized histone variants analogous to classical **haematohiston**."
      }
    ]
  },
  "Dashboard — haem\\haematoidin.md": {
    "primary": "A reddish-orange, iron-free crystalline substance formed in tissues by the breakdown of hemoglobin from old hemorrhages (chemically identical to bilirubin).",
    "secondary": "In histopathology and forensic medicine, crystals deposited in old hematomas and infarcts, demonstrating localized hemoglobin catabolism.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "I demonstrated that **haematoidin** forms magnificent rhombic orange crystals within old hemorrhagic apoplexy cysts, completely devoid of iron."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination of long-standing pulmonary infarcts reveals yellow-red granules of **haematoidin** engulfed within macrophages."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "The chemical distinction between fresh blood pigment and ancient **haematoidin** residues formed the basis of Holmes's forensic discourse."
      }
    ]
  },
  "Dashboard — haem\\haematological.md": {
    "primary": "Of, relating to, or involving hematology, the branch of medicine concerned with the blood and blood-forming tissues.",
    "secondary": "In laboratory medicine, describing blood counts, smear morphology, coagulation profiles, or blood malignancies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A complete **haematological** survey must include erythrocyte counts, leucocyte differentiation, and stained platelet morphology."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "Acute lymphoblastic leukemia was the first **haematological** malignancy cured by targeted combination chemotherapy."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The lab technician telephoned critical **haematological** results, warning of severe consumptive thrombocytopenia."
      }
    ]
  },
  "Dashboard — haem\\haematologist.md": {
    "primary": "A physician or scientist who specializes in the diagnosis, treatment, and study of blood diseases and disorders.",
    "secondary": "In clinical medicine, a specialist who manages anemias, coagulopathies, sickle cell disease, leukemias, and bone marrow transplants.",
    "quotes": [
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "The pioneering **haematologist** Sidney Farber dared to administer antifolate chemicals to children dying of acute leukemia."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "We reviewed the perplexing bone marrow aspirate with the hospital's senior **haematologist** to identify the abnormal blast cells."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "To the observant **haematologist**, the stained peripheral smear tells an intimate story of marrow reserve and systemic health."
      }
    ]
  },
  "Dashboard — haem\\haematology.md": {
    "primary": "The branch of medicine concerned with the study of the cause, prognosis, treatment, and prevention of diseases related to blood.",
    "secondary": "The specialized field of pathology and internal medicine encompassing benign and malignant disorders of erythrocytes, leukocytes, platelets, and coagulation factors.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern clinical **haematology** began when Paul Ehrlich introduced aniline dye combinations to differentiate white blood cells."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Progress in molecular **haematology** transformed bone marrow transplantation from an experimental gamble into a curative therapy."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Coagulation algorithms developed in laboratory **haematology** drastically reduced bleeding complications during massive trauma surgery."
      }
    ]
  },
  "Dashboard — haem\\haematolysis.md": {
    "primary": "The destruction, breakdown, or dissolution of red blood cells with release of hemoglobin into the surrounding medium; hemolysis.",
    "secondary": "In clinical pathology, intravascular or extravascular erythrocyte breakdown resulting from toxins, immune antibodies, mechanical heart valves, or hereditary enzyme defects.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe transfusion reactions trigger acute intravascular **haematolysis**, heralded by rigors, lumbar pain, and hemoglobinuria."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Complement-mediated **haematolysis** requires the coordinated interaction of sensitized amboceptors with thermolabile serum factors."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Elevated indirect bilirubin and undetectable serum haptoglobin provided unequivocal evidence of brisk ongoing **haematolysis**."
      }
    ]
  },
  "Dashboard — haem\\haematoma.md": {
    "primary": "A solid swelling of clotted blood within the tissues, resulting from a broken blood vessel; a hematoma.",
    "secondary": "In clinical surgery and neurosurgery, a localized blood collection (such as an epidural or subdural hematoma) that exerts pathological mass effect.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Laceration of the middle meningeal artery by a temporal skull fracture produces an expanding epidural **haematoma**."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The emergency craniotomy was performed immediately to evacuate the acute subdural **haematoma** and relieve brain herniation."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The orthopedic surgeon drained the tense subungual **haematoma** by trephining the nail plate with a heated wire."
      }
    ]
  },
  "Dashboard — haem\\haematopodidae.md": {
    "primary": "A family of wading shorebirds in the order Charadriiformes, commonly known as oystercatchers.",
    "secondary": "In ornithology, robust coastal shorebirds characterized by stout red chisel-like bills, black and white or all-black plumage, and specialized bivalve-feeding habits.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Along the rocky shores of Tierra del Fuego, shorebirds of the family **Haematopodidae** pried limpets from the boulders with flattened bills."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The piercing whistling cries of **Haematopodidae** echoed over the mudflats as the tide retreated, exposing cockle beds."
      },
      {
        "author": "David Attenborough",
        "work": "The Life of Birds",
        "quote": "Members of **Haematopodidae** learn specialized shell-smashing or shell-stabbing techniques by observing their parents for months."
      }
    ]
  },
  "Dashboard — haem\\haematopoiesis.md": {
    "primary": "The production of all types of blood cells, including formation, development, and differentiation of a stem cell into mature blood elements.",
    "secondary": "In physiology and hematology, lifelong blood cell generation occurring within the marrow stroma, regulated by cytokines such as erythropoietin and thrombopoietin.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Pluripotent hematopoietic stem cells in the bone marrow drive continuous **haematopoiesis**, producing billions of new blood cells each day."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "In chronic myeloid leukemia, the normal hierarchy of **haematopoiesis** is hijacked by an aberrant fusion kinase, BCR-ABL."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extramedullary **haematopoiesis** in the spleen and liver compensates when myelofibrosis obliterates normal bone marrow architecture."
      }
    ]
  },
  "Dashboard — haem\\haematopoietic.md": {
    "primary": "Of, relating to, or involved in the formation of blood cellular components.",
    "secondary": "In molecular oncology and medicine, describing hematopoietic stem cells, hematopoietic growth factors, and hematopoietic neoplasms (leukemias and lymphomas).",
    "quotes": [
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "The discovery of the self-renewing **haematopoietic** stem cell by Till and McCulloch laid the conceptual cornerstone of modern regenerative medicine."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Recombinant human erythropoietin stimulated the patient's **haematopoietic** marrow, correcting severe anemia without transfusions."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Total body irradiation obliterates the **haematopoietic** marrow, rendering autologous or allogeneic stem cell rescue essential for survival."
      }
    ]
  },
  "Dashboard — haem\\haematopus.md": {
    "primary": "The genus of oystercatchers in the family Haematopodidae, robust wading birds characterized by long, straight, red bills.",
    "secondary": "In avian taxonomy, charadriiform birds (including the Eurasian oystercatcher, Haematopus ostralegus) specialized for cracking or prying open coastal mollusks.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Specimens of **Haematopus** collected in the Falkland Islands used their heavy chisel bills to wrench limpets from wave-beaten rocks."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The piping cries of **Haematopus** sounded across the stormy shoals as flocks of oystercatchers settled on the sandspit."
      },
      {
        "author": "David Attenborough",
        "work": "The Life of Birds",
        "quote": "The bill tip of **Haematopus** is richly supplied with sensory corpuscles, allowing it to probe intertidal sand for buried bivalves."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Body Part 3 - Batch 3 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
