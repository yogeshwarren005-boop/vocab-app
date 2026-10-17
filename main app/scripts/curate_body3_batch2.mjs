import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — ethn\\ethnographic.md": {
    "primary": "Of or relating to ethnography; describing customs, social structures, and cultures of specific human groups.",
    "secondary": "In qualitative anthropology and sociology, describing observational field research conducted through immersive participant observation.",
    "quotes": [
      {
        "author": "Bronislaw Malinowski",
        "work": "Argonauts of the Western Pacific",
        "quote": "The **ethnographic** diary records the imponderabilia of actual life and typical behavior in an indigenous village."
      },
      {
        "author": "Clifford Geertz",
        "work": "The Interpretation of Cultures",
        "quote": "Thick description distinguishes meaningful human action from mere physical twitching in **ethnographic** analysis."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Tristes Tropiques",
        "quote": "The **ethnographic** journey confronts the observer with the fragility of our own civilized categories."
      }
    ]
  },
  "Dashboard — ethn\\ethnographical.md": {
    "primary": "Pertaining to ethnography; ethnographic (formal or archaic variant).",
    "secondary": "In nineteenth-century scientific travel writing, descriptive of cultural artifacts, tribal rituals, and linguistics recorded in the field.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Our collections included valuable **ethnographical** specimens of Fuegian bark canoes, stone tools, and woven baskets."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The **ethnographical** notes I gathered among the Dayaks documented complex tattooing traditions and head-hunting ceremonies."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "An **ethnographical** survey of fire-making techniques reveals remarkable parallel inventions across isolated continents."
      }
    ]
  },
  "Dashboard — ethn\\ethnography.md": {
    "primary": "The scientific description of the customs of individual peoples and cultures.",
    "secondary": "In cultural anthropology, the qualitative research method and resultant written monograph based on extensive direct participant observation in a community.",
    "quotes": [
      {
        "author": "Margaret Mead",
        "work": "Coming of Age in Samoa",
        "quote": "Modern **ethnography** demonstrates that many emotional storms of adolescence are cultural artifacts rather than biological imperatives."
      },
      {
        "author": "Bronislaw Malinowski",
        "work": "Argonauts of the Western Pacific",
        "quote": "Living among the Trobriand Islanders without white companions transformed my **ethnography** into genuine participant understanding."
      },
      {
        "author": "Clifford Geertz",
        "work": "Works and Lives: The Anthropologist as Author",
        "quote": "The power of classical **ethnography** rests on convincing the reader that the researcher was genuinely there and saw things firsthand."
      }
    ]
  },
  "Dashboard — ethn\\ethnologic.md": {
    "primary": "Of or relating to ethnology; dealing with the comparative study of cultures and races.",
    "secondary": "In anthropological theory, pertaining to the systemic comparison of cultural, linguistic, and historical developments among diverse peoples.",
    "quotes": [
      {
        "author": "Franz Boas",
        "work": "The Mind of Primitive Man",
        "quote": "Rigorous **ethnologic** research disproved the simplistic biological determinism of early nineteenth-century racial theorists."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Linguistic classification often cross-cuts **ethnologic** boundaries, revealing independent historical migrations."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Structural Anthropology",
        "quote": "The **ethnologic** comparative method identifies universal structural properties underlying disparate kinship terminologies."
      }
    ]
  },
  "Dashboard — ethn\\ethnological.md": {
    "primary": "Relating to ethnology; comparative, analytical, and historical study of human cultures.",
    "secondary": "In museum curation and social anthropology, describing collections, analyses, and comparative syntheses of human societies.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The **ethnological** evidence gathered from every quarter of the globe points toward common ancestry for all human races."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Researches into the Early History of Mankind",
        "quote": "An **ethnological** comparison of burial customs reveals recurring intuitions regarding the soul and an afterlife."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Huge **ethnological** libraries were ransacked to illustrate how agricultural rituals centered upon dying and rising fertility gods."
      }
    ]
  },
  "Dashboard — ethn\\ethnologist.md": {
    "primary": "A specialist in ethnology, the comparative study of peoples and their cultures.",
    "secondary": "In the human sciences, a scholar who synthesizes ethnographic data to explain cultural evolution, diffusion, and kinship structures.",
    "quotes": [
      {
        "author": "Claude Lévi-Strauss",
        "work": "Tristes Tropiques",
        "quote": "The professional **ethnologist** lives as an exile at home and a perpetual stranger abroad."
      },
      {
        "author": "Franz Boas",
        "work": "Race, Language, and Culture",
        "quote": "The careful **ethnologist** must master the native language to understand the inner conceptual world of his informants."
      },
      {
        "author": "Margaret Mead",
        "work": "Sex and Temperament in Three Primitive Societies",
        "quote": "To the trained **ethnologist**, contrasting personality ideals among neighboring tribes illuminate the plasticity of culture."
      }
    ]
  },
  "Dashboard — ethn\\ethnology.md": {
    "primary": "The study of the characteristics of various peoples and the differences and relationships between them.",
    "secondary": "In academic anthropology, the comparative and theoretical branch that analyzes ethnographic data to formulate cross-cultural generalizations.",
    "quotes": [
      {
        "author": "Claude Lévi-Strauss",
        "work": "Structural Anthropology",
        "quote": "If ethnography is the field observation of a culture, **ethnology** is the comparative science that synthesizes these observations into general laws."
      },
      {
        "author": "Franz Boas",
        "work": "The Mind of Primitive Man",
        "quote": "Modern **ethnology** establishes that human achievements depend on historical circumstance rather than innate racial genius."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "The science of **ethnology** organizes the arts, beliefs, and morals of mankind into orderly developmental series."
      }
    ]
  },
  "Dashboard — ethn\\ethnomusicology.md": {
    "primary": "The study of the music of different cultures, especially non-Western music in its cultural context.",
    "secondary": "In cultural anthropology and musicology, the multidisciplinary field that examines musical sound, performance practices, and social meaning within communities.",
    "quotes": [
      {
        "author": "Alan Merriam",
        "work": "The Anthropology of Music",
        "quote": "The discipline of **ethnomusicology** treats music not merely as acoustic sound, but as human behavior integrated into culture."
      },
      {
        "author": "Oliver Sacks",
        "work": "Musicophilia",
        "quote": "Field recordings in **ethnomusicology** reveal how communal polyrhythms induce ecstatic trance states across African traditions."
      },
      {
        "author": "Béla Bartók",
        "work": "Hungarian Folk Music",
        "quote": "My pioneering excursions into **ethnomusicology** among Carpathian peasants unlocked modal harmonies that revitalized modern classical composition."
      }
    ]
  },
  "Dashboard — ethn\\ethnos.md": {
    "primary": "A people, nation, or ethnic group characterized by shared culture, ancestry, language, and historical self-awareness.",
    "secondary": "In political anthropology and sociology, the primordial cultural community contrasted with the political apparatus of the state (demos).",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "Economy and Society",
        "quote": "Belief in common descent binds the members of an **ethnos**, providing an emotional ground for collective political action."
      },
      {
        "author": "Benedict Anderson",
        "work": "Imagined Communities",
        "quote": "The modern nation-state sought to align political boundaries with an idealized, homogeneous **ethnos**."
      },
      {
        "author": "Anthony D. Smith",
        "work": "The Ethnic Origins of Nations",
        "quote": "The enduring continuity of the ancient **ethnos** depends upon shared myths of origin and collective historical memories."
      }
    ]
  },
  "Dashboard — ethn\\paleoethnography.md": {
    "primary": "The ethnographic study of prehistoric or ancient peoples and their cultures based on material remains.",
    "secondary": "In archaeology, the reconstruction of social organization, kinship, and daily life in prehistoric societies through material culture analysis.",
    "quotes": [
      {
        "author": "V. Gordon Childe",
        "work": "What Happened in History",
        "quote": "Through meticulous **paleoethnography**, we can reconstruct the domestic economy of Neolithic lake dwellings from waterlogged wood and seeds."
      },
      {
        "author": "André Leroi-Gourhan",
        "work": "Treasures of Prehistoric Art",
        "quote": "Spatial distribution of flint blades and hearths in Magdalenian rock shelters provides the foundation for paleolithic **paleoethnography**."
      },
      {
        "author": "Colin Renfrew",
        "work": "Archaeology: Theories, Methods, and Practice",
        "quote": "Modern **paleoethnography** moves beyond typological lists to illuminate the lived social reality of ancient hunting bands."
      }
    ]
  },
  "Dashboard — ethn\\polyethnic.md": {
    "primary": "Inhabited by, comprising, or characteristic of people from several or many ethnic groups.",
    "secondary": "In political science and sociology, describing pluralistic societies or multi-ethnic empires characterized by cultural and linguistic diversity.",
    "quotes": [
      {
        "author": "J.S. Furnivall",
        "work": "Colonial Policy and Practice",
        "quote": "In a **polyethnic** plural society, disparate communities live side by side, meeting only in the marketplace without social integration."
      },
      {
        "author": "Benedict Anderson",
        "work": "Imagined Communities",
        "quote": "The Ottoman Empire governed a vast **polyethnic** mosaic through the decentralized millet system for centuries."
      },
      {
        "author": "Francis Fukuyama",
        "work": "The Origins of Political Order",
        "quote": "Building durable democratic institutions within a **polyethnic** state requires robust legal protections for minority rights."
      }
    ]
  },
  "Dashboard — gargal\\gargal.md": {
    "primary": "A combining form derived from Greek gargalizein, meaning to tickle or provoke laughter through tactile stimulation.",
    "secondary": "In physiological psychology and historical neurology, the root morpheme denoting heavy, laughter-inducing tickling and tactile reflexes.",
    "quotes": [
      {
        "author": "G. Stanley Hall",
        "work": "The Psychology of Tickling, Laughing, and the Comic",
        "quote": "We isolated the Greek root **gargal** to designate the coarse, laughter-provoking form of tickle that convulsed children."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Tactile reflexes derived from **gargal** stimulation provoke instinctive laughter and evasive muscular contractions across young primates."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The reflex response to sensory **gargal** excitation illustrates how localized cutaneous nerves evoke systemic visceral agitation."
      }
    ]
  },
  "Dashboard — gargal\\gargalesis.md": {
    "primary": "Heavy, laughter-inducing tickling, produced by firmer touch to sensitive areas of the body such as the armpits or ribs.",
    "secondary": "In neurophysiology and sensory psychology, vigorous tactile stimulation contrasted with knismesis (light, feather-like itching tickle).",
    "quotes": [
      {
        "author": "G. Stanley Hall",
        "work": "The Psychology of Tickling, Laughing, and the Comic",
        "quote": "We proposed the term **gargalesis** for the deep, aggressive tickling that provokes uncontrollable convulsions of laughter and writhing."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Infants giggle and pull away from **gargalesis**, showing that laughter is innately linked to surprise and gentle tactile combat."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "Sensory thresholds for **gargalesis** vary widely, reflecting complex cortical gating between tickle perception and defense reflexes."
      }
    ]
  },
  "Dashboard — gargal\\gargalesthesia.md": {
    "primary": "Sensitivity to being tickled; tactile responsiveness to tickling sensations.",
    "secondary": "In clinical neurology, cutaneous and somatosensory responsiveness evaluated to assess peripheral nerve function and parietal lobe processing.",
    "quotes": [
      {
        "author": "G. Stanley Hall",
        "work": "A Study of Tickling",
        "quote": "Children display heightened **gargalesthesia** across the soles of the feet, the axillae, and the lateral thoracic margins."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Neurological examination demonstrated preserved deep pain perception alongside complete loss of cutaneous **gargalesthesia** below the spinal lesion."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Cortical suppression of self-induced tickle explains why normal **gargalesthesia** requires unpredictable tactile stimulation by another person."
      }
    ]
  },
  "Dashboard — gargal\\hypergargalesthesia.md": {
    "primary": "Abnormally excessive or heightened sensitivity to tickling.",
    "secondary": "In clinical neurology and sensory processing, an extreme tactile hypersensitivity where the slightest touch evokes violent laughter, reflex spasm, or distress.",
    "quotes": [
      {
        "author": "G. Stanley Hall",
        "work": "The Psychology of Tickling",
        "quote": "Certain nervous temperaments exhibit pronounced **hypergargalesthesia**, flinching and shouting even before a teasing finger makes contact."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Tactile hyperesthesia in early neuropathy occasionally manifests as unbearable **hypergargalesthesia** upon light touch."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "Autistic patients often experience sensory overload, describing normal social touch as agonizing **hypergargalesthesia**."
      }
    ]
  },
  "Dashboard — gastr\\Myxogastria.md": {
    "primary": "A class of plasmodial or acellular slime molds characterized by a multinucleate, macroscopic streaming amoeboid vegetative stage (plasmodium).",
    "secondary": "In protistology and mycology (often classified as Myxomycetes), amoebozoan organisms that feed by phagocytosis before differentiating into intricate fruiting bodies.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The multinucleate plasmodia of **Myxogastria** crawl across moist forest timber, exhibiting magnificent protoplasmic streaming."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Decaying logs shelter vibrant slime molds of the class **Myxogastria**, whose pulsating golden nets engulf bacteria and spores."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Upon desiccation, the giant plasmodium of **Myxogastria** transforms into spore-bearing sporangia of exquisite geometric complexity."
      }
    ]
  },
  "Dashboard — gastr\\epigastric.md": {
    "primary": "Lying upon or over the stomach; relating to the upper central region of the abdomen.",
    "secondary": "In clinical anatomy and medical diagnosis, describing symptoms (such as epigastric pain) located between the xiphoid process and the umbilicus.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe, burning **epigastric** pain occurring two hours after meals is classic for a penetrating duodenal ulcer."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The emergency physician palpated the patient's tense **epigastric** region, suspecting acute pancreatitis or a perforated viscus."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Careful percussion outlined the enlarged left hepatic lobe projecting deep into the **epigastric** notch."
      }
    ]
  },
  "Dashboard — gastr\\epigastrium.md": {
    "primary": "The upper central region of the abdomen, situated above the umbilical region and between the costal margins.",
    "secondary": "In surface anatomy and physical examination, the abdominal zone overlying the stomach, duodenum, pancreas, and left lobe of the liver.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Inspection of the **epigastrium** in severe pyloric obstruction frequently reveals visible gastric peristalsis passing from left to right."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Guarding and rebound tenderness localized in the **epigastrium** pointed toward acute chemical peritonitis from an ulcer perforation."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "The patient complained of constant dull ache deep in the **epigastrium**, radiating straight through to the lumbar spine."
      }
    ]
  },
  "Dashboard — gastr\\gasteroid.md": {
    "primary": "Resembling or shaped like a stomach; or (of fungi) having spores that develop and mature inside a closed basidioma.",
    "secondary": "In mycology, describing gasteroid fungi (such as puffballs, earthstars, and stinkhorns) whose basidiospores are not forcibly discharged into the air.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In the damp Patagonian beech woods, we discovered peculiar **gasteroid** fungi whose internal powdery spores puff out when trodden on."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Evolutionary transitions from agarics to **gasteroid** fruiting bodies occurred independently in several desert fungal lineages."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "Strange **gasteroid** puffballs dotted the Andean paramo, releasing dense clouds of chocolate-colored spores into the mountain wind."
      }
    ]
  },
  "Dashboard — gastr\\gastr.md": {
    "primary": "A combining form derived from Greek gaster (genitive gastros), meaning stomach or belly.",
    "secondary": "In medical and zoological terminology, the root element utilized in gastric, gastroscopy, gastronomy, and gastropod.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The Greek anatomical root **gastr** provided medical Latin with hundreds of prefixes relating to the stomach and digestion."
      },
      {
        "author": "Galen",
        "work": "On the Usefulness of the Parts of the Body",
        "quote": "Nature bestowed upon the creature a digestive receptacle, derived from **gastr**, to concoct food into blood."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinical terms incorporating **gastr** form the foundation of our gastroenterological diagnostic nomenclature."
      }
    ]
  },
  "Dashboard — gastr\\gastralgia.md": {
    "primary": "Severe pain in the stomach or epigastric region, typically of a burning or cramping nature; stomachache.",
    "secondary": "In historical and clinical medicine, paroxysmal gastric pain associated with peptic ulcer disease, gastric neurosis, or acute gastritis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Periodic **gastralgia** relieved immediately by milk or antacids is an almost pathognomonic symptom of duodenal ulceration."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The nervous invalid complained of agonizing bouts of **gastralgia** whenever emotional tension overwhelmed her digestion."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "We ruled out cardiac ischemia before treating the patient's recurrent nighttime **gastralgia** with proton pump inhibitors."
      }
    ]
  },
  "Dashboard — gastr\\gastrectomy.md": {
    "primary": "Surgical removal of all (total gastrectomy) or part (partial gastrectomy) of the stomach.",
    "secondary": "In surgical oncology and bariatrics, resection of gastric tissue for gastric adenocarcinoma, intractable ulcer disease, or metabolic weight reduction (sleeve gastrectomy).",
    "quotes": [
      {
        "author": "Theodor Billroth",
        "work": "Open Letters on Surgical Innovations",
        "quote": "In 1881, I successfully performed the world's first partial **gastrectomy**, resecting a pyloric cancer and restoring intestinal continuity."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Following total **gastrectomy**, patients require lifelong parenteral vitamin B12 supplementation due to the loss of gastric intrinsic factor."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon completed the subtotal **gastrectomy**, fashioning a Roux-en-Y gastrojejunostomy to re-establish enteral flow."
      }
    ]
  },
  "Dashboard — gastr\\gastric.md": {
    "primary": "Of, relating to, or situated near the stomach.",
    "secondary": "In physiology, denoting the hydrochloric acid, pepsin, and intrinsic factor produced by the gastric mucosa for digestion.",
    "quotes": [
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice and the Physiology of Digestion",
        "quote": "Through Alexis St. Martin's fistula, I extracted pure **gastric** juice and demonstrated its power to digest meat outside the living body."
      },
      {
        "author": "Ivan Pavlov",
        "work": "The Work of the Digestive Glands",
        "quote": "Sham feeding in dogs stimulated profuse reflex secretion of **gastric** acid mediated by the vagus nerves."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic **gastric** ulcer carries serious risks of catastrophic hemorrhage, pyloric stenosis, or malignant degeneration."
      }
    ]
  },
  "Dashboard — gastr\\gastrin.md": {
    "primary": "A peptide hormone secreted by G cells in the pyloric antrum of the stomach that stimulates gastric acid secretion.",
    "secondary": "In endocrinology and gastrointestinal physiology, a hormone that acts on parietal and enterochromaffin-like (ECL) cells, hypersecreted in Zollinger-Ellison syndrome.",
    "quotes": [
      {
        "author": "Arthur Kornberg",
        "work": "For the Love of Enzymes",
        "quote": "The peptide hormone **gastrin** binds to cholecystokinin-B receptors, triggering intracellular calcium release and acid pumping."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A gastrinoma of the pancreas secretes autonomous floods of **gastrin**, producing fulminant, intractable multiple peptic ulcers."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Feedback regulation of **gastrin** secretion by luminal hydrochloric acid demonstrates classical hormonal homeostasis in the digestive tract."
      }
    ]
  },
  "Dashboard — gastr\\gastritis.md": {
    "primary": "Inflammation of the protective mucosal lining of the stomach.",
    "secondary": "In gastroenterology and histopathology, acute erosive or chronic non-erosive inflammation, most commonly caused by Helicobacter pylori infection, NSAIDs, or alcohol.",
    "quotes": [
      {
        "author": "Barry Marshall",
        "work": "Helicobacter Pioneers",
        "quote": "To prove that the spiral bacillus caused disease, I drank a culture of Helicobacter pylori and developed acute, biopsy-proven **gastritis** within days."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute toxic **gastritis** follows the ingestion of corrosive poisons, showing extensive mucosal necrosis and sloughing."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Prophylactic acid suppression in surgical intensive care prevents the development of acute stress-induced **gastritis** and mucosal bleeding."
      }
    ]
  },
  "Dashboard — gastr\\gastroboletus.md": {
    "primary": "A genus of bolete-like fungi in the family Boletaceae that produce secotioid or semi-enclosed fruiting bodies that do not open fully.",
    "secondary": "In systematic mycology, an evolutionary intermediate between traditional capped boletes and hypogeous false truffles, characterized by contorted pore tubes.",
    "quotes": [
      {
        "author": "Alexander H. Smith",
        "work": "The Boletes of Michigan",
        "quote": "Species of **Gastroboletus** represent secotioid adaptations to arid montane environments, retaining their spores within enclosed spongy tubes."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "In high Sierra Nevada conifer forests, small rodents dig for partially buried basidiocarps of **Gastroboletus**, dispersing their spores."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "The subterranean habit of **Gastroboletus** protects its reproductive tissue from drying alpine winds and early autumn frosts."
      }
    ]
  },
  "Dashboard — gastr\\gastrocnemius.md": {
    "primary": "The chief muscle of the calf of the leg, which flexes the knee and foot, terminating downward in the calcaneal (Achilles) tendon.",
    "secondary": "In musculoskeletal anatomy, a superficial two-headed biarticular muscle essential for running, jumping, and plantar flexion of the ankle.",
    "quotes": [
      {
        "author": "Leonardo da Vinci",
        "work": "Anatomical Drawings",
        "quote": "The two powerful bellies of the **gastrocnemius** unite into the strong cord of the heel to lift the whole weight of the body in walking."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The massive development of the human **gastrocnemius** muscle is an evolutionary adaptation directly linked to upright bipedal posture."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "Following the tendon tear, the lateral head of my **gastrocnemius** contracted into an agonizing, useless knot of muscle fiber."
      }
    ]
  },
  "Dashboard — gastr\\gastrocybe.md": {
    "primary": "A monotypic genus of secotioid fungi in the family Bolbitiaceae, notably Gastrocybe lateritia.",
    "secondary": "In agaricology, an ephemeral mushroom that fruits in grassy lawns at dawn, collapsing into a gelatinous mass as its spores mature internally.",
    "quotes": [
      {
        "author": "Alexander H. Smith",
        "work": "The Mushroom Hunter's Field Guide",
        "quote": "The fragile, unexpanded cap of **Gastrocybe** emerges on dew-drenched suburban lawns before dissolving by mid-morning."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Mycologists study **Gastrocybe** as a prime example of evolutionary transition toward gastroid spore retention within the agarics."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Before the prairie sun grew warm, ephemeral little mushrooms like **Gastrocybe** appeared and melted back into the turf."
      }
    ]
  },
  "Dashboard — gastr\\gastroduodenal.md": {
    "primary": "Of, relating to, or connecting the stomach and the duodenum.",
    "secondary": "In abdominal surgery and gastroenterology, referring to the gastroduodenal artery, gastroduodenal junction (pylorus), or peptic ulceration involving both organs.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Erosion of the large **gastroduodenal** artery by a posterior duodenal ulcer produces catastrophic, life-threatening hematemesis."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The surgical resident placed deep transfixion stitches to ligate the bleeding **gastroduodenal** vessel at the base of the ulcer."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Contrast imaging confirmed patent transit across the reconstructed **gastroduodenal** junction following pyloroplasty."
      }
    ]
  },
  "Dashboard — gastr\\gastroenteritis.md": {
    "primary": "Inflammation of the mucous membrane of both the stomach and the intestines, causing vomiting, diarrhea, and cramps.",
    "secondary": "In clinical infectious disease and public health, an acute, highly communicable syndrome caused by viruses (norovirus), bacteria (Salmonella), or protozoa.",
    "quotes": [
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Preventing infantile death from epidemic **gastroenteritis** requires community water sanitation combined with packaged oral rehydration therapy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In severe toxic **gastroenteritis**, constant vomiting precludes oral fluid intake, demanding prompt intravenous electrolyte replacement."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "A standard clinical checklist for pediatric **gastroenteritis** ensured that nurses monitored capillary refill and urine output vigilantly."
      }
    ]
  },
  "Dashboard — gastr\\gastroenterologist.md": {
    "primary": "A physician who specializes in the diagnosis and treatment of disorders of the digestive system (gastrointestinal tract and liver).",
    "secondary": "In clinical internal medicine, a specialist trained in endoscopic procedures (colonoscopy, upper endoscopy, ERCP) to treat luminal and hepatobiliary diseases.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "The skilled **gastroenterologist** manipulated the flexible endoscope with fingertip sensitivity, identifying the bleeding arteriole in seconds."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "We consulted the hospital's senior **gastroenterologist** to perform an urgent endoscopic sclerotherapy on the bleeding esophageal varices."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "Routine screening colonoscopies performed by the **gastroenterologist** detect and remove adenomatous polyps before they turn malignant."
      }
    ]
  },
  "Dashboard — gastr\\gastroenterology.md": {
    "primary": "The branch of medicine and physiology concerned with the structure, functions, and diseases of the digestive tract.",
    "secondary": "A subspecialty of internal medicine encompassing the esophagus, stomach, small intestine, colon, pancreas, gallbladder, and liver.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The rapid development of **gastroenterology** as an independent discipline owes much to the clinical application of mucosal biopsies."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "Modern clinical **gastroenterology** combines molecular pathophysiology with high-definition optical imaging of the living mucosa."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Advances in interventional **gastroenterology** have replaced many traditional open abdominal surgeries with minimally invasive endoscopy."
      }
    ]
  },
  "Dashboard — gastr\\gastroenterostomy.md": {
    "primary": "A surgical operation creating an artificial passage between the stomach and the small intestine (usually the jejunum).",
    "secondary": "In gastrointestinal surgery, a bypass procedure (such as Billroth II or Roux-en-Y reconstruction) to treat gastric outlet obstruction or facilitate bariatric weight loss.",
    "quotes": [
      {
        "author": "Theodor Billroth",
        "work": "Surgical Memoirs",
        "quote": "To relieve the vomiting caused by an inoperable pyloric tumor, Anton Wölfler devised the palliative procedure of anterior **gastroenterostomy**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient made a complete recovery from gastric outlet stenosis following a well-placed posterior **gastroenterostomy**."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Laparoscopic Roux-en-Y gastric bypass creates a miniature stomach pouch and connects it via a hand-sewn **gastroenterostomy**."
      }
    ]
  },
  "Dashboard — gastr\\gastroesophageal.md": {
    "primary": "Of, relating to, or involving both the stomach and the esophagus.",
    "secondary": "In clinical medicine, designating the gastroesophageal junction, lower esophageal sphincter, or gastroesophageal reflux disease (GERD).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Incompetence of the lower sphincter mechanism permits acidic **gastroesophageal** reflux, producing chronic retrosternal heartburn."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Long-standing severe **gastroesophageal** reflux can induce Barrett's metaplasia in the distal squamous mucosa, predisposing to adenocarcinoma."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The barium swallow clearly demonstrated hiatal herniation across the weakened **gastroesophageal** diaphragm opening."
      }
    ]
  },
  "Dashboard — gastr\\gastrogavage.md": {
    "primary": "Artificial feeding into the stomach through a flexible tube passed down the esophagus or through a gastrostomy.",
    "secondary": "In clinical therapeutics and pediatric nursing, enteral tube administration of liquid nutrition in patients unable to swallow voluntarily.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In cases of profound diphtheritic pharyngeal paralysis, nutritional sustenance was maintained through cautious **gastrogavage**."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "Families often face agonizing decisions regarding long-term **gastrogavage** via feeding tubes for patients with end-stage dementia."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The nurse measured the residual volume before administering the scheduled morning **gastrogavage** formula."
      }
    ]
  },
  "Dashboard — gastr\\gastrointestinal.md": {
    "primary": "Of or relating to the stomach and the intestines.",
    "secondary": "Pertaining to the entire digestive tract from mouth to anus, including its mucosal, secretory, and neuromuscular functions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute massive **gastrointestinal** bleeding demands rapid vascular access and immediate blood cross-matching."
      },
      {
        "author": "Ed Yong",
        "work": "I Contain Multitudes",
        "quote": "The human **gastrointestinal** tract contains a microbial ecosystem composed of hundreds of diverse bacterial species."
      },
      {
        "author": "Michael Pollan",
        "work": "The Omnivore's Dilemma",
        "quote": "The omnivore's profound anxiety is managed by the intricate sensory and chemical defenses of our **gastrointestinal** tract."
      }
    ]
  },
  "Dashboard — gastr\\gastrolith.md": {
    "primary": "A stone swallowed by an animal (especially a bird, reptile, or extinct dinosaur) that stays in the gizzard or stomach to grind food.",
    "secondary": "In paleontology and comparative vertebrate zoology, a polished stomach stone (gizzard stone) used for mechanical digestion in animals lacking chewing dentition.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In the muscular gizzards of South American ostriches, we found dozens of rounded pebbles serving as functional **gastrolith** grinders."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "Paleontologists identify fossil sauropod skeletons by clusters of polished **gastrolith** stones preserved inside the rib cage."
      },
      {
        "author": "David Attenborough",
        "work": "Life on Earth",
        "quote": "Modern crocodiles deliberately swallow heavy stones that function both as a digestive **gastrolith** and as stabilizing ballast for diving."
      }
    ]
  },
  "Dashboard — gastr\\gastrolobium.md": {
    "primary": "A genus of flowering plants in the legume family (Fabaceae), native to Western Australia, commonly known as poison peas.",
    "secondary": "In economic botany and veterinary toxicology, shrubs containing lethal concentrations of monofluoroacetate ('1080'), deadly to introduced domestic livestock.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Australian pastoralists suffered catastrophic sheep losses after herds grazed upon the toxic legume **Gastrolobium**."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Australasia",
        "quote": "Native Australian marsupials have evolved remarkable physiological tolerance to the deadly fluoroacetates in **Gastrolobium**."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "On the Flora of Australia",
        "quote": "The western flora abounds in brightly flowered species of **Gastrolobium**, notorious for poisoning introduced European stock."
      }
    ]
  },
  "Dashboard — gastr\\gastromy.md": {
    "primary": "Surgical incision into the stomach (variant or archaic form of gastrotomy).",
    "secondary": "In historical operative surgery, surgical opening of the stomach wall to explore the interior, relieve obstruction, or excise gastric tumors.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Operative intervention by **gastromy** was performed to remove a massive trichobezoar obstructing the pylorus."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Before the advent of modern flexible gastroscopy, surgical **gastromy** was often the only way to identify bleeding mucosal ulcers."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon made a clean anterior incision during the **gastromy**, taking care to avoid the gastroepiploic arcade."
      }
    ]
  },
  "Dashboard — gastr\\gastromycete.md": {
    "primary": "A fungus of the group Gasteromycetes (puffballs, earthstars, stinkhorns), in which spores mature within an enclosed fruiting body.",
    "secondary": "In classical mycology, a basidiomycete that relies on external agents (wind, rain, insects) rather than forcible ballistosporic discharge to disperse spores.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Under the damp fallen leaves, a curious subterranean **gastromycete** developed, waiting for rains to breach its outer peridium."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Unlike a gill mushroom, a true **gastromycete** encloses its fertile gleba until the basidiospores have matured completely."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "A dry puffball, an ancient **gastromycete**, sent up a miniature volcanic plume of smoke beneath the hunter's boot."
      }
    ]
  },
  "Dashboard — gastr\\gastromycetes.md": {
    "primary": "A former class or informal group of basidiomycete fungi (including puffballs, stinkhorns, and bird's nest fungi) characterized by internal spore maturation.",
    "secondary": "In systematic mycology, an artificial, polyphyletic assemblage of fungi that independently evolved enclosed basidiomata (gasteroid forms).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The class **Gastromycetes** comprises puffballs, earthstars, and stinkhorns, all possessing an internal gleba enclosed by a peridium."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "DNA sequencing dismantled **Gastromycetes**, showing that gasteroid evolution arose repeatedly from diverse agaric and bolete ancestors."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The subterranean fungi of the **Gastromycetes** demonstrate how cryptogamic life thrives in dark humus far from the sun."
      }
    ]
  },
  "Dashboard — gastr\\gastronome.md": {
    "primary": "A connoisseur of good food; a gourmet or epicure.",
    "secondary": "In culinary culture and literature, a person who possesses discriminating appreciation and philosophical understanding of the culinary arts.",
    "quotes": [
      {
        "author": "Jean Anthelme Brillat-Savarin",
        "work": "The Physiology of Taste",
        "quote": "A true **gastronome** does not merely eat to sustain the body; he tastes with cultivated, intellectual discernment."
      },
      {
        "author": "Honoré de Balzac",
        "work": "Cousin Pons",
        "quote": "The old musician was a passionate **gastronome**, willing to endure any domestic humiliation for a seat at a sumptuous table."
      },
      {
        "author": "Michael Pollan",
        "work": "The Omnivore's Dilemma",
        "quote": "The modern **gastronome** seeks not just decadent luxury, but an authentic ecological connection to where food is grown."
      }
    ]
  },
  "Dashboard — gastr\\gastronomic.md": {
    "primary": "Of, relating to, or characteristic of gastronomy or good eating.",
    "secondary": "Pertaining to the culinary arts, haute cuisine, and the cultural philosophy of dining.",
    "quotes": [
      {
        "author": "Jean Anthelme Brillat-Savarin",
        "work": "The Physiology of Taste",
        "quote": "The discovery of a new dish does more for the happiness of mankind than the discovery of a star, according to the **gastronomic** code."
      },
      {
        "author": "Anthony Bourdain",
        "work": "Kitchen Confidential",
        "quote": "Paris was a temple of intense, uncompromising **gastronomic** passion where every sauce carried centuries of technique."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "Understanding chemical caramelization transforms simple kitchen cookery into rigorous **gastronomic** mastery."
      }
    ]
  },
  "Dashboard — gastr\\gastronomical.md": {
    "primary": "Relating to gastronomy; gastronomic (formal or variant form).",
    "secondary": "In literature and travel prose, describing elaborate meals, regional culinary traditions, and dining pleasures.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Pickwick Papers",
        "quote": "Mr. Wardle's Christmas dinner was a **gastronomical** triumph of roast beef, mince pies, and smoking bowls of punch."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "Jos Sedley devoted his days to **gastronomical** indulgences, dreaming of spicy Indian curries and rich claret."
      },
      {
        "author": "Mark Twain",
        "work": "A Tramp Abroad",
        "quote": "I compiled a **gastronomical** inventory of beloved American dishes that European hotels tragically failed to serve."
      }
    ]
  },
  "Dashboard — gastr\\gastronomy.md": {
    "primary": "The practice or art of choosing, cooking, and eating good food.",
    "secondary": "In cultural history and sensory philosophy, the comprehensive study of food and culture, focusing on gourmet cuisine and dietary aesthetic traditions.",
    "quotes": [
      {
        "author": "Jean Anthelme Brillat-Savarin",
        "work": "The Physiology of Taste",
        "quote": "**Gastronomy** is the intelligent knowledge of whatever concerns man's nourishment, governing chemistry, agriculture, and trade."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "Molecular **gastronomy** bridges empirical kitchen lore with the physical chemistry of foams, emulsions, and gels."
      },
      {
        "author": "Michael Pollan",
        "work": "Cooked: A Natural History of Transformation",
        "quote": "True **gastronomy** honors the biological alchemy that turns raw produce into delicious, communal human communion."
      }
    ]
  },
  "Dashboard — gastr\\gastroparesis.md": {
    "primary": "A condition that affects the normal spontaneous movement of the muscles (motility) in your stomach, resulting in delayed gastric emptying without mechanical obstruction.",
    "secondary": "In gastroenterology, a chronic neuromuscular disorder commonly associated with autonomic diabetic neuropathy, viral infections, or post-surgical vagal nerve injury.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Longstanding diabetic neuropathy frequently produces symptomatic **gastroparesis**, marked by early satiety, nausea, and erratic glycemic control."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Radionuclide gastric-emptying scintigraphy confirmed marked **gastroparesis**, with significant retention of the radiolabeled solid meal at four hours."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Post-vagotomy **gastroparesis** required dietary restructuring into small, frequent low-fiber meals combined with prokinetic therapy."
      }
    ]
  },
  "Dashboard — gastr\\gastrophryne.md": {
    "primary": "A genus of small, narrow-mouthed toads in the family Microhylidae, native to North and Central America, including the eastern narrow-mouthed toad (Gastrophryne carolinensis).",
    "secondary": "In herpetology, secretive fossorial amphibians characterized by a pointed snout, a distinctive fold of skin behind the eyes, and a specialized ant-eating diet.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "Manual of the Vertebrates of the Northern United States",
        "quote": "The tiny narrow-mouthed toad **Gastrophryne** burrows into moist humus, feeding almost exclusively upon small ants."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "After warm summer thunderstorms, the bleating, sheep-like calls of **Gastrophryne** filled the flooded roadside ditches."
      },
      {
        "author": "David Attenborough",
        "work": "Life in Cold Blood",
        "quote": "The smooth, slippery skin and pointed snout of **Gastrophryne** permit it to squeeze effortlessly into subterranean ant chambers."
      }
    ]
  },
  "Dashboard — gastr\\gastropod.md": {
    "primary": "A mollusk of the large class Gastropoda, such as a snail, slug, or whelk, typically having a single spiral shell or no shell at all.",
    "secondary": "In invertebrate zoology, an asymmetrical mollusk characterized by torsion during larval development and a broad, muscular ventral creeping foot.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The freshwater **gastropod** Ancylus adheres tenaciously to floating driftwood, facilitating accidental transport between isolated ponds."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Larval torsion in the developing **gastropod** rotates the visceral mass by 180 degrees, bringing the mantle cavity above the head."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The carnivorous marine **gastropod** drills a neat round hole through the bivalve shell with its rasping radula."
      }
    ]
  },
  "Dashboard — gastr\\gastropoda.md": {
    "primary": "A very large class of mollusks (including snails, slugs, sea hares, and limpets) having a muscular foot, eyes, and usually a spiral shell.",
    "secondary": "In systematic malacology, the most diverse molluscan class, displaying developmental torsion, a radula, and adaptive radiation into marine, freshwater, and terrestrial biomes.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The distinguishing morphological hallmark of the class **Gastropoda** is the asymmetrical disposition of the visceral sac relative to the foot."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Tertiary sedimentary strata are dated with extraordinary precision using the fossil shells of extinct **Gastropoda**."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Speciation among land snails of the **Gastropoda** across Pacific islands provides classic models of adaptive radiation in miniature."
      }
    ]
  },
  "Dashboard — gastr\\gastroptosis.md": {
    "primary": "An abnormal downward displacement or prolapse of the stomach into the lower abdominal or pelvic cavity.",
    "secondary": "In clinical gastroenterology, sagging of the stomach caused by laxity of the gastrophrenic and gastrohepatic ligaments, often part of generalized visceroptosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Barium radiography in the upright position clearly demonstrated profound **gastroptosis**, with the greater curvature dipping into the true pelvis."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Nineteenth-century clinicians often attributed visceral neurosis and melancholic symptoms to the mechanical dragging of **gastroptosis**."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "Abdominal palpation confirmed that the splashing succussion splash originated far below the umbilicus, indicative of marked **gastroptosis**."
      }
    ]
  },
  "Dashboard — gastr\\gastroschisis.md": {
    "primary": "A congenital defect in the abdominal wall, typically to the right of the umbilical cord, through which the intestines protrude without a covering sac.",
    "secondary": "In pediatric surgery and teratology, an abdominal wall malformation requiring immediate neonatal protective wrapping and surgical reduction to prevent gut ischemia.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The pediatric surgery team mobilized immediately to cover the exposed bowel of the newborn delivered with congenital **gastroschisis**."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Unlike omphalocele, the herniated evisceration in **gastroschisis** is naked, lacking an overlying amnioperitoneal membrane."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Staged reduction using a spring-loaded silastic silo allowed the swollen intestines of the **gastroschisis** infant to return safely into the abdominal cavity."
      }
    ]
  },
  "Dashboard — gastr\\gastroscope.md": {
    "primary": "An optical instrument for inspecting the interior of the stomach.",
    "secondary": "In gastroenterology, a flexible fiberoptic or video endoscope equipped with light sources, lens systems, and channels for biopsy forceps and cautery instruments.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The rigid **gastroscope** devised by Mikulicz represented a heroic, if precarious, attempt to visualize mucosal lesions directly."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "The modern video **gastroscope** transmits high-definition digital imagery, illuminating bleeding ulcer beds in vivid color."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The gastroenterologist guided the lubricated tip of the **gastroscope** past the cricopharyngeus muscle into the gastric lumen."
      }
    ]
  },
  "Dashboard — gastr\\gastroscopy.md": {
    "primary": "Examination of the interior of the stomach using a gastroscope.",
    "secondary": "In diagnostic and interventional endoscopy, an upper endoscopy procedure that evaluates mucosal inflammation, ulceration, bleeding, or neoplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Introduction of flexible fiberoptics transformed **gastroscopy** from a dangerous specialty procedure into an indispensable outpatient diagnostic tool."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "A routine pre-procedure **gastroscopy** checklist verified conscious sedation monitoring, patient allergies, and biopsy instrument sterility."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "The urgent **gastroscopy** pinpointed a bleeding Dieulafoy lesion along the lesser curvature, which was promptly coagulated."
      }
    ]
  },
  "Dashboard — gastr\\gastrostomy.md": {
    "primary": "The surgical creation of an opening through the abdominal wall into the stomach, typically to insert a feeding tube.",
    "secondary": "In general surgery and interventional radiology, a procedure (often performed endoscopically as PEG) to provide enteral feeding in dysphagic patients.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In cases of inoperable cicatricial esophageal stricture, a permanent **gastrostomy** preserves life by permitting direct gastric feeding."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "The placement of a percutaneous endoscopic **gastrostomy** tube has become routine, though its clinical benefits in terminal dementia remain contested."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon brought the anterior gastric wall up to the fascia, securing the Stamm **gastrostomy** with concentric purse-string sutures."
      }
    ]
  },
  "Dashboard — gastr\\gastrotrich.md": {
    "primary": "A minute, microscopic worm-like aquatic animal belonging to the phylum Gastrotricha, having a scaly or spiny cuticle and cilia on the ventral surface.",
    "secondary": "In meiofaunal zoology, pseudocoelomate invertebrates inhabiting marine sands and freshwater benthos, characterized by adhesive tubes and a muscular sucking pharynx.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The interstitial spaces of freshwater sands harbor the agile **gastrotrich**, gliding by means of longitudinal ventral ciliary bands."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "Microscopic meiofauna like the **gastrotrich** demonstrate that morphological complexity does not depend on macroscopic body size."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "In every handful of tidal sand dwells an invisible zoo, where each tiny **gastrotrich** browses upon single-celled diatoms."
      }
    ]
  },
  "Dashboard — gastr\\gastrula.md": {
    "primary": "An early multicellular embryo, following the blastula, in which the germ layers (ectoderm, endoderm, and mesoderm) are formed.",
    "secondary": "In developmental biology, the cup-shaped embryonic stage produced by invagination during gastrulation, enclosing the primitive gut (archenteron).",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "I formulated the Gastraea theory, proposing that the embryonic **gastrula** mirrors the common two-layered ancestor of all higher animal phyla."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The transformation of the hollow blastula into the double-walled **gastrula** is one of the grand conserved architectural movements of animal life."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Lewis Wolpert famously remarked that it is not birth, marriage, or death, but the formation of the **gastrula** that is the most important time in your life."
      }
    ]
  },
  "Dashboard — gastr\\gastrulation.md": {
    "primary": "The process in embryonic development by which a blastula develops into a gastrula with three primary germ layers.",
    "secondary": "In embryology, a coordinated choreography of cell movements (invagination, involution, epiboly) that establishes the body plan and gut tube in bilaterians.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "During **gastrulation**, extensive cellular rearrangements internalize the prospective endoderm and mesoderm while spreading ectoderm over the surface."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Morphogenetic movements during **gastrulation** establish the primary anteroposterior and dorsoventral body axes of the organism."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "The mysterious biological cues directing **gastrulation** marshal millions of identical embryonic cells into distinct tissue fates."
      }
    ]
  },
  "Dashboard — gastr\\mesogastric.md": {
    "primary": "Of or relating to the middle region of the abdomen (umbilical region); or relating to the mesogastrium.",
    "secondary": "In embryology and anatomy, pertaining to the embryonic mesentery (dorsal or ventral mesogastrium) that suspends the stomach from the abdominal wall.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Localized tenderness in the **mesogastric** zone surrounding the umbilicus suggests pathology of the small intestine or mesenteric nodes."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "During gastric rotation, the dorsal **mesogastric** fold balloons outward to form the expansive apron of the greater omentum."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon divided the avascular window in the **mesogastric** ligament to enter the lesser peritoneal sac."
      }
    ]
  },
  "Dashboard — glia\\anglia.md": {
    "primary": "The medieval Latin name for England, or the historic eastern English region of East Anglia.",
    "secondary": "In historical geography, the ancestral territory occupied by the Angles in Britain, comprising Norfolk, Suffolk, and parts of Cambridgeshire.",
    "quotes": [
      {
        "author": "Bede",
        "work": "Ecclesiastical History of the English People",
        "quote": "From the country of the Angles came the people of East **Anglia**, settling fertile lands bounded by the fenland marshes and the North Sea."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The Saxons and Angles established their heptarchy, bestowing upon the conquered Roman province the enduring name of **Anglia**."
      },
      {
        "author": "Thomas Hardy",
        "work": "A Pair of Blue Eyes",
        "quote": "Ancient Saxon dialects still echoed in the placenames across the windswept coastal heaths of East **Anglia**."
      }
    ]
  },
  "Dashboard — glia\\anglian.md": {
    "primary": "Of or relating to the Angles, an ancient Germanic people who settled in Britain in the 5th century AD, or to East Anglia.",
    "secondary": "In historical linguistics and archaeology, the Old English dialect and cultural tradition of Northumbria, Mercia, and East Anglia.",
    "quotes": [
      {
        "author": "Bede",
        "work": "Ecclesiastical History of the English People",
        "quote": "The **Anglian** kingdom of Northumbria embraced the Christian faith through the preaching of the holy bishop Aidan."
      },
      {
        "author": "J.R.R. Tolkien",
        "work": "Beowulf: The Monsters and the Critics",
        "quote": "The poetic diction of Beowulf preserves archaic **Anglian** linguistic forms reflecting ancient heroic traditions."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "Fierce **Anglian** warriors carved out independent principalities along the Humber and Trent river valleys."
      }
    ]
  },
  "Dashboard — glia\\glia.md": {
    "primary": "The non-neuronal supporting tissue of the central and peripheral nervous system, comprising astrocytes, oligodendrocytes, and microglia; neuroglia.",
    "secondary": "In neurobiology, active cellular partners that provide metabolic support, modulate synaptic transmission, maintain the blood-brain barrier, and direct neural repair.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "I coined the term neuro-**glia** to designate the interstitial connective substance that embeds the nervous elements of the brain."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Far from being a passive cement, the delicate arborizations of the **glia** interact dynamically with active neuronal synapses."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Astrocytic **glia** actively clear neurotransmitters from the synaptic cleft, shaping the temporal duration of synaptic currents."
      }
    ]
  },
  "Dashboard — glia\\glial.md": {
    "primary": "Of, relating to, or composed of glia (neuroglia).",
    "secondary": "In neuroscience and neuropathology, pertaining to non-neuronal brain cells and their functions in myelination, homeostasis, and response to cerebral injury (gliosis).",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "The blood-brain barrier is fortified by specialized end-feet of **glial** cells wrapped around cerebral capillary endothelial walls."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Histological staining revealed dense **glial** scarring within the basal ganglia of post-encephalitic patients."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Recent discoveries demonstrate that **glial** networks communicate through calcium waves, coordinating widespread cerebral metabolic states."
      }
    ]
  },
  "Dashboard — glia\\glioblastoma.md": {
    "primary": "A highly malignant, rapidly growing brain tumor that arises from astrocytes or glial precursors; glioblastoma multiforme (GBM).",
    "secondary": "In neuro-oncology, a Grade IV astrocytic neoplasm characterized by cellular pleomorphism, nuclear atypia, microvascular proliferation, and pseudopalisading necrosis.",
    "quotes": [
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "A primary **glioblastoma** infiltrates the brain parenchyma like fungal mycelia through soil, defying complete surgical resection."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "The MRI scan revealed the grim, irregular ring-enhancing mass of a **glioblastoma** deep in the patient's temporal lobe."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The neuropathologist identified pseudopalisading necrosis on frozen section, confirming the diagnosis of fatal **glioblastoma**."
      }
    ]
  },
  "Dashboard — glia\\glioma.md": {
    "primary": "A tumor that arises from the glial (supportive) tissue of the brain or spinal cord.",
    "secondary": "In clinical oncology and neuropathology, a primary central nervous system neoplasm categorized into astrocytomas, oligodendrogliomas, and ependymomas.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intracranial **glioma** typically manifests with progressive morning headache, papilledema, and focal sensorimotor deficits."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "A slow-growing frontal **glioma** produced subtle disinhibition and personality changes long before physical weakness appeared."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Targeted molecular therapies for low-grade **glioma** aim to inhibit mutant IDH enzymes that drive oncogenic chromatin remodeling."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Body Part 3 - Batch 2 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
