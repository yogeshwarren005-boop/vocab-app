import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — encephal\\metencephalon.md": {
    "primary": "The anterior part of the hindbrain in the vertebrate embryo, which develops into the pons and the cerebellum.",
    "secondary": "In neuroanatomy and embryology, the rostral division of the rhombencephalon that coordinates somatic motor function, vestibular balance, and autonomic pontine reflexes.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "During embryonic neurogenesis, the **metencephalon** thickens dorsally to give rise to the cerebellar cortex and Purkinje cell layers."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "The pontine nuclei derived from the **metencephalon** relay massive corticocerebellar projections essential for motor learning."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The fourth ventricle extends through the lumen of the **metencephalon**, roofed by the emerging cerebellar vermis."
      }
    ]
  },
  "Dashboard — encephal\\neoencephalon.md": {
    "primary": "The phylogenetically newer parts of the brain, especially the cerebral cortex and its associated pathways.",
    "secondary": "In evolutionary neurobiology, the telencephalic structures that expanded dramatically in mammals to support higher cognitive processing, sensory perception, and voluntary motor planning.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Lesions confined to the **neoencephalon** disrupt symbolic abstraction and visual recognition while leaving primitive subcortical instincts intact."
      },
      {
        "author": "Carl Sagan",
        "work": "The Dragons of Eden",
        "quote": "The expansion of the **neoencephalon** provided our primate ancestors with the neural machinery for complex social syntax."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Cerebral dominance reflects the gradual subordination of archaic brainstem arcs to the overarching control of the **neoencephalon**."
      }
    ]
  },
  "Dashboard — encephal\\paleoencephalon.md": {
    "primary": "The phylogenetically older part of the brain, including the brainstem, midbrain, and basal ganglia, responsible for primitive, instinctive behaviors.",
    "secondary": "In comparative neurology, the subcortical core conserved across all vertebrates that governs homeostatic regulation, arousal, visceral control, and basic survival reflexes.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "The Dragons of Eden",
        "quote": "Deep beneath the neocortex lies the ancient **paleoencephalon**, the neural chassis inherited from ancestral reptiles."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Encephalitis lethargica selectively ravaged the dopaminergic networks of the **paleoencephalon**, immobilizing patients in catatonic stupor."
      },
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "Primitive emotional responses such as fear and autonomic rage originate within circuits of the conserved **paleoencephalon**."
      }
    ]
  },
  "Dashboard — encephal\\panencephalitis.md": {
    "primary": "Widespread inflammation of the entire brain, involving both the gray matter (polioencephalitis) and white matter (leukoencephalitis).",
    "secondary": "In clinical neurology, a progressive, devastating encephalitis such as subacute sclerosing panencephalitis (SSPE), triggered by persistent defective measles virus infection.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Histopathological examination in fatal cases of **panencephalitis** demonstrates diffuse perivascular lymphocytic cuffing across both cortical ribbons and deep tracts."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Years after an unremarkable childhood viral infection, insidious progressive **panencephalitis** produced dementia, myoclonus, and motor collapse."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Maintaining universal measles immunization remains our sole public health defense against the catastrophic late complication of sclerosing **panencephalitis**."
      }
    ]
  },
  "Dashboard — enter\\dysentery.md": {
    "primary": "Infection of the intestines resulting in severe diarrhea with the presence of blood and mucus in the feces.",
    "secondary": "In clinical infectious disease and epidemiology, an acute gastrointestinal syndrome caused either by invasive bacilli (Shigella) or parasitic amoebae (Entamoeba histolytica).",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The plague in besieged Athens was aggravated by crowded quarters, and virulent **dysentery** swept through the refugee huts."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Amebic **dysentery** must be differentiated from acute bacillary outbreaks by immediate microscopic demonstration of motile trophozoites."
      },
      {
        "author": "Paul Farmer",
        "work": "Pathologies of Power",
        "quote": "Access to clean municipal water instantly eliminates the scourge of infantile **dysentery** that haunts informal refugee camps."
      }
    ]
  },
  "Dashboard — enter\\enter.md": {
    "primary": "To come or go into a place; or a combining form derived from Greek enteron meaning intestine or digestive tract.",
    "secondary": "In biological terminology and lexical morphology, the combining root denoting intestinal anatomy, physiology, and pathology.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "Neither a borrower nor a lender be; / For loan oft loses both itself and friend, / And borrowing dulls the edge of husbandry. / This above all: to thine own self be true, / And it must follow, as the night the day, / Thou canst not then be false to any man. / Fare well: my blessing season this in thee! / O, didst thou **enter** into the palace grounds?"
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Into this wild Abyss, the Womb of nature and perhaps her Grave, / Did Satan boldly **enter** on his dark design."
      },
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "Medical lexicographers rely upon the prefix **enter** to designate any clinical procedure or tissue associated with the gut."
      }
    ]
  },
  "Dashboard — enter\\enteral.md": {
    "primary": "Involving or passing through the intestine, either naturally via the mouth or through an artificial feeding tube.",
    "secondary": "In clinical nutrition and pharmacology, route of administration utilizing the gastrointestinal tract, contrasting with parenteral administration.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "We preferred early **enteral** feeding through a soft nasojejunal tube to maintain gut mucosal integrity and prevent bacterial translocation."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **enteral** absorption of toxins during acute intestinal stasis triggers severe systemic prostration."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Once bowel sounds returned, the surgical team discontinued intravenous fluids and initiated gentle **enteral** nutrition."
      }
    ]
  },
  "Dashboard — enter\\enteric.md": {
    "primary": "Of, relating to, or occurring in the intestines.",
    "secondary": "In pharmacology and physiology, describing protective pill coatings that resist gastric acid or denoting the enteric nervous system ('the second brain').",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "The **enteric** nervous system contains hundreds of millions of neurons capable of coordinating peristalsis completely independently of the central nervous system."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Peyer's patches in the distal ileum undergo ulceration during the third week of severe **enteric** fever."
      },
      {
        "author": "Michael Pollan",
        "work": "Cooked: A Natural History of Transformation",
        "quote": "Oral medications with an **enteric** coating pass unscathed through the stomach's acid bath before dissolving in the alkaline duodenum."
      }
    ]
  },
  "Dashboard — enter\\enterics.md": {
    "primary": "Bacteria belonging to the family Enterobacteriaceae or inhabiting the intestinal tract of humans and animals.",
    "secondary": "In clinical microbiology, Gram-negative facultative bacilli (such as Escherichia, Salmonella, and Klebsiella) monitored as enteric pathogens or fecal indicators.",
    "quotes": [
      {
        "author": "Alexander Fleming",
        "work": "Penicillin",
        "quote": "Early penicillin preparations showed remarkable efficacy against Gram-positive cocci but proved ineffective against resilient Gram-negative **enterics**."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "Bacteriologists isolated pathogenic **enterics** from tainted municipal wells that had spread typhoid through the valley."
      },
      {
        "author": "Ed Yong",
        "work": "I Contain Multitudes",
        "quote": "The mammalian colon harbors trillions of harmless commensal **enterics** that outcompete virulent opportunistic invaders."
      }
    ]
  },
  "Dashboard — enter\\entering.md": {
    "primary": "The act of going or coming into a place; penetrating or enrolling.",
    "secondary": "In spatial and procedural contexts, the process of ingress or commencement into a physical vessel, lumen, or formal system.",
    "quotes": [
      {
        "author": "Dante Alighieri",
        "work": "Inferno",
        "quote": "All hope abandon, ye who **entering** here, pass through the gloomy portals of the sorrowful city."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Upon **entering** the sheltered harbor of the Galápagos, we were struck by the desolate volcanic craters encircling the bay."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "To every medical student **entering** the hospital wards, I urge cultivation of patience and quiet detachment."
      }
    ]
  },
  "Dashboard — enter\\enteritis.md": {
    "primary": "Inflammation of the intestine, especially the small intestine, usually accompanied by diarrhea, cramping, and fever.",
    "secondary": "In veterinary and human gastroenterology, mucosal inflammation caused by viral infections, bacterial toxins, radiation, or autoimmune disease (Crohn's disease).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute catarrhal **enteritis** commonly follows the ingestion of decomposing foodstuffs containing toxic bacterial proteoses."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Dehydration from acute rotavirus **enteritis** remains one of the world's most lethal yet preventable pediatric emergencies."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The patient presented with severe regional **enteritis**, with transmural thickening visible on contrast radiography."
      }
    ]
  },
  "Dashboard — enter\\enterobacteria.md": {
    "primary": "A group of Gram-negative, rod-shaped bacteria that typically inhabit the intestines of humans and other animals.",
    "secondary": "In diagnostic bacteriology, facultatively anaerobic coliform bacilli that ferment glucose, reduce nitrates to nitrites, and lack cytochrome oxidase.",
    "quotes": [
      {
        "author": "Carl Woese",
        "work": "The Genetic Code",
        "quote": "Comparative sequencing revealed clear phylogenetic boundaries separating harmless symbiotic **enterobacteria** from soil-dwelling pseudomonads."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "The emergence of antibiotic resistance among hospital-acquired **enterobacteria** poses an escalating challenge to modern chemotherapy."
      },
      {
        "author": "Ed Yong",
        "work": "I Contain Multitudes",
        "quote": "In every human gut, specialized **enterobacteria** produce vitamin K and break down complex dietary polysaccharides."
      }
    ]
  },
  "Dashboard — enter\\enterobacteriaceae.md": {
    "primary": "A large family of Gram-negative bacteria that includes many of the common gut flora and pathogens such as Escherichia coli, Salmonella, and Klebsiella.",
    "secondary": "In systematic bacteriology, a medically crucial family of non-sporeforming rods that reside as commensals or pathogens in the animal digestive tract.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "Investigations into the Etiology of Traumatic Infective Diseases",
        "quote": "Isolating distinct genera of **Enterobacteriaceae** required developing differential nutrient agars and lactose fermentation tubes."
      },
      {
        "author": "Paul Farmer",
        "work": "Infections and Inequalities",
        "quote": "Multi-drug resistant strains of **Enterobacteriaceae** spread rapidly through intensive care wards lacking robust infection control protocols."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Escherichia coli, a prominent member of **Enterobacteriaceae**, has served as the foundational model organism for molecular genetics."
      }
    ]
  },
  "Dashboard — enter\\enterobiasis.md": {
    "primary": "Infestation with the pinworm Enterobius vermicularis, common in children and characterized by intense perianal itching.",
    "secondary": "In parasitology, a cosmopolitan helminthic infection transmitted via the fecal-oral ingestion of microscopic eggs from contaminated bedding, clothing, or dust.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The definitive diagnosis of **enterobiasis** is established by applying clear adhesive tape to the perianal fold in early morning to capture ova."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "We treated the entire household with a single dose of mebendazole to eradicate persistent familial **enterobiasis**."
      },
      {
        "author": "Carl Zimmer",
        "work": "Parasite Rex",
        "quote": "Unlike tropical filarial worms, **enterobiasis** thrives in modern temperate nurseries, spreading easily among playful toddlers."
      }
    ]
  },
  "Dashboard — enter\\enterobius.md": {
    "primary": "A genus of small parasitic nematode worms in the family Oxyuridae, commonly known as pinworms or threadworms.",
    "secondary": "In zoological parasitology, intestinal nematodes possessing lateral alae and an esophageal bulb, with females migrating nocturnal to oviposit on the perianal epidermis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination of stool concentrates revealed the asymmetrical, planar-convex eggs characteristic of **Enterobius** vermicularis."
      },
      {
        "author": "Carl Zimmer",
        "work": "Parasite Rex",
        "quote": "The female **Enterobius** crawls from the rectal sphincter under cover of darkness to deposit thousands of eggs, triggering intense pruritus."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "Parasitologists marvelled at the sheer persistence with which **Enterobius** cycled through schools and dormitories."
      }
    ]
  },
  "Dashboard — enter\\enteroceptor.md": {
    "primary": "A sensory receptor situated in the internal viscera, especially the gastrointestinal tract, that responds to stimuli arising within the body; an interoceptor.",
    "secondary": "In neurophysiology, visceral mechanoreceptors, chemoreceptors, or osmoreceptors that relay internal biochemical and distension signals to the autonomic nervous system.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The **enteroceptor** responds to chemical and mechanical changes occurring within the deep internal environment of the visceral canal."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Distension of the intestinal smooth muscle activates each localized **enteroceptor**, triggering coordinated peristaltic reflex loops via vagal afferents."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Our subconscious sense of visceral well-being depends on continuous background feedback originating from every visceral **enteroceptor**."
      }
    ]
  },
  "Dashboard — enter\\enterococcus.md": {
    "primary": "A genus of Gram-positive, spherical bacteria that occur in pairs or short chains, commonly found as part of the normal intestinal flora.",
    "secondary": "In clinical microbiology, hardy lactic acid bacteria (notably Enterococcus faecalis and E. faecium) notorious for hospital-acquired infections and vancomycin resistance (VRE).",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Stringent barrier precautions were instituted on the surgical floor to stop the transmission of vancomycin-resistant **Enterococcus**."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Treating bloodstream infections caused by multi-drug resistant **Enterococcus** strains requires costly last-resort antibiotics."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "Unlike fragile streptococci, the rugged gut commensal **Enterococcus** tolerates bile salts and harsh osmotic gradients with ease."
      }
    ]
  },
  "Dashboard — enter\\enterocolitis.md": {
    "primary": "Inflammation of both the small intestine and the colon.",
    "secondary": "In pediatric and adult gastroenterology, a severe inflammatory condition such as necrotizing enterocolitis (NEC) in premature infants or pseudomembranous colitis from Clostridioides difficile.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "In the neonatal intensive care unit, sudden abdominal distension and pneumatosis intestinalis signaled catastrophic necrotizing **enterocolitis**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prolonged high fever with tenesmus and bloody discharge indicates acute septic **enterocolitis** requiring aggressive fluid resuscitation."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The patient developed antibiotic-associated **enterocolitis**, with colonoscopy revealing diffuse pseudomembranes lining the mucosa."
      }
    ]
  },
  "Dashboard — enter\\enterokinase.md": {
    "primary": "An enzyme of the brush border of the duodenal mucosa that converts inactive trypsinogen into active trypsin; also called enteropeptidase.",
    "secondary": "In digestive physiology and biochemistry, the master proteolytic trigger that initiates the cascade of pancreatic digestive enzyme activation in the intestinal lumen.",
    "quotes": [
      {
        "author": "Ivan Pavlov",
        "work": "The Work of the Digestive Glands",
        "quote": "The discovery of **enterokinase** in intestinal juice revealed that the intestine produces an enzyme capable of animating other enzymes."
      },
      {
        "author": "Arthur Kornberg",
        "work": "For the Love of Enzymes",
        "quote": "By cleaving a single hexapeptide from trypsinogen, mucosal **enterokinase** unleashes the entire proteolytic power of the pancreatic secretion."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Deficiency of duodenal **enterokinase** impairs protein assimilation, leading to severe infantile malabsorption and failure to thrive."
      }
    ]
  },
  "Dashboard — enter\\enterolith.md": {
    "primary": "A stone or calculus formed in the intestine, composed of mineral salts and organic matter.",
    "secondary": "In veterinary and human gastroenterology, an intestinal concretion typically formed around a foreign nucleus, capable of causing bowel obstruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Laparotomy revealed that the mechanical small bowel obstruction was caused by a large calcified **enterolith** lodged in the terminal ileum."
      },
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Horses and other large herbivores occasionally accumulate a concentric **enterolith** composed of ammonium magnesium phosphate around a pebble."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The surgeon delivered the dense, faceted **enterolith** through a longitudinal enterotomy before closing the bowel wall."
      }
    ]
  },
  "Dashboard — enter\\enterolithiasis.md": {
    "primary": "The medical condition of having stones or calculi (enteroliths) in the intestine.",
    "secondary": "In surgical pathology, the formation of intestinal concretions in stagnant bowel segments (such as diverticula or blind loops), risking mechanical obstruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Lectures on Angina Pectoris and Allied States",
        "quote": "Chronic intestinal stasis within a large jejunal diverticulum predisposes the patient to recurrent **enterolithiasis** and localized perforation."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Preoperative abdominal computed tomography identified profound **enterolithiasis** with high-grade upstream intestinal dilation."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "Cases of symptomatic **enterolithiasis** are rare in modern surgical practice, yet they require prompt operative extraction."
      }
    ]
  },
  "Dashboard — enter\\enterolobium.md": {
    "primary": "A genus of flowering trees in the pea family (Fabaceae), native to tropical America, including the giant ear-pod tree (Enterolobium cyclocarpum).",
    "secondary": "In tropical dendrology, massive canopy trees characterized by expansive spreading crowns, feathery bipinnate leaves, and curved, ear-shaped woody seed pods.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "The colossal trunk of **Enterolobium**, known as the carocaro, shaded an entire village square with its wide-spreading leafy canopy."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature and Other Essays",
        "quote": "Cattle and native tapirs forage eagerly for the fallen ear-shaped seed pods dropped by towering specimens of **Enterolobium**."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "The heavy, curved fruit of **Enterolobium** evolved to be eaten and dispersed by now-extinct Pleistocene megafauna like giant ground sloths."
      }
    ]
  },
  "Dashboard — enter\\enteron.md": {
    "primary": "The alimentary canal or digestive cavity of an animal; the gut, especially in embryonic or invertebrate anatomy.",
    "secondary": "In comparative embryology, the archenteron or primitive embryonic digestive cavity formed by invagination of the blastula during gastrulation.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "In simple diploblastic organisms like Hydra, the internal **enteron** serves both as a digestive stomach and a vascular distribution cavity."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The invagination of the blastula produces the primitive **enteron**, the common ancestral gut cavity of all metazoan life."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The development of the embryonic **enteron** demonstrates deep morphological homology linking diverse bilaterian lineages."
      }
    ]
  },
  "Dashboard — enter\\enteropathy.md": {
    "primary": "Any disease or pathological condition affecting the intestinal tract.",
    "secondary": "In gastroenterology, intestinal mucosal damage resulting in malabsorption or protein loss, such as celiac disease (gluten-sensitive enteropathy) or environmental enteropathy.",
    "quotes": [
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Small bowel biopsy confirmed subtotal villous atrophy consistent with severe gluten-sensitive **enteropathy**."
      },
      {
        "author": "Paul Farmer",
        "work": "Infections and Inequalities",
        "quote": "Chronic tropical **enteropathy** impairs micronutrient uptake in undernourished children even in the absence of acute diarrheal symptoms."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Protein-losing **enteropathy** should be considered in patients presenting with unexplained generalized anasarca and profound hypoalbuminemia."
      }
    ]
  },
  "Dashboard — enter\\enteroptosis.md": {
    "primary": "An abnormal downward displacement or prolapse of the intestines into the lower abdominal or pelvic cavity; also known as Glenard's disease.",
    "secondary": "In historical clinical medicine, visceroptosis attributed to laxity of the abdominal wall musculature and supporting peritoneal ligaments.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The asthenic woman with narrow thoracic angles frequently displays marked **enteroptosis**, with the transverse colon sagging into the true pelvis."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Nineteenth-century physicians frequently ascribed nervous exhaustion and hypochondria to mechanical visceral dragging or **enteroptosis**."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "Physical examination in Glénard's **enteroptosis** revealed palpable descent of the stomach and mobile kidneys upon standing."
      }
    ]
  },
  "Dashboard — enter\\enterostenosis.md": {
    "primary": "Stricture or abnormal narrowing of the lumen of the intestine.",
    "secondary": "In gastrointestinal surgery, luminal constriction resulting from inflammatory bowel disease, post-ischemic scarring, or circumferential neoplastic infiltration.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cicatrization following severe tuberculous ulceration can produce chronic **enterostenosis** accompanied by visible peristaltic waves."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Fibrotic strictureplasty was performed to relieve recurrent **enterostenosis** without sacrificing excessive lengths of small intestine."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Barium series demonstrated marked proximal dilatation terminating at a discrete area of circumferential **enterostenosis**."
      }
    ]
  },
  "Dashboard — enter\\enterostomy.md": {
    "primary": "A surgical operation to create a permanent or temporary opening into the intestine through the abdominal wall.",
    "secondary": "In general surgery, a stoma (such as an ileostomy or jejunostomy) established for enteral decompression, nutritional access, or diversion of fecal stream.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The surgeon brought the loop of ileum through the rectus muscle, maturing the **enterostomy** to divert stool from the distal anastomosis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In cases of acute obstructing typhlitis, emergency **enterostomy** was historically performed to vent accumulated toxic gas and fluids."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "Careful attention to stoma appliance fitting prevented skin excoriation around the high-output **enterostomy**."
      }
    ]
  },
  "Dashboard — enter\\enterotomy.md": {
    "primary": "A surgical incision made into the intestine, typically to inspect the lumen, remove an obstruction, or obtain a biopsy.",
    "secondary": "In operative abdominal surgery, an incision through the serosa, muscularis, and mucosa of the small bowel, closed with meticulous transverse suturing to prevent luminal stenosis.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "After isolating the obstructing gallstone, the surgeon performed a clean **enterotomy** in healthy proximal bowel to extract the calculus."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Accidental perforation during lysis of dense adhesions necessitated prompt primary repair of the inadvertent **enterotomy**."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "The incision was closed transversely with interrupted silk sutures following completion of the exploratory **enterotomy**."
      }
    ]
  },
  "Dashboard — enter\\enterotoxemia.md": {
    "primary": "A condition characterized by the presence and systemic absorption of enterotoxins produced in the intestines.",
    "secondary": "In veterinary medicine, an acute, often fatal toxemia (such as 'pulpy kidney disease' in sheep) caused by proliferation of Clostridium perfringens type D in the gut.",
    "quotes": [
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Sudden lush pasture growth in spring occasionally triggered lethal **enterotoxemia** among the flock grazing the clover bottoms."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rapid proliferation of anaerobic bacteria within stagnant bowel loops unleashes fulminant systemic **enterotoxemia** and circulatory collapse."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Veterinary vaccination against clostridial **enterotoxemia** demonstrated the critical efficacy of toxoid immunization in livestock health."
      }
    ]
  },
  "Dashboard — enter\\enterotoxin.md": {
    "primary": "A protein toxin released by a microorganism in the intestine, typically causing vomiting, diarrhea, and gastrointestinal symptoms.",
    "secondary": "In microbial pathogenesis and immunology, an exotoxin (such as cholera toxin or Staphylococcal enterotoxin B) that alters cyclic AMP levels or acts as a potent superantigen.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "The Etiology of Cholera",
        "quote": "Vibrio cholerae does not invade the bloodstream; rather, it adheres to intestinal villi and secretes a lethal, diffusible **enterotoxin**."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "The contaminated cream puffs harbored staphylococci that had generated massive amounts of heat-stable **enterotoxin** on the warm shelf."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Cholera **enterotoxin** locks the G-protein in an active state, causing intestinal epithelial cells to pump massive volumes of water into the lumen."
      }
    ]
  },
  "Dashboard — enter\\enterovirus.md": {
    "primary": "Any of a group of small RNA viruses that infect the gastrointestinal tract and can spread to other parts of the body, including polioviruses, coxsackieviruses, and echoviruses.",
    "secondary": "In virology, a genus of positive-sense single-stranded non-enveloped RNA viruses of the family Picornaviridae, transmitted primarily through the fecal-oral route.",
    "quotes": [
      {
        "author": "Jonas Salk",
        "work": "Man Unfolding",
        "quote": "Polio was the most feared **enterovirus** of the twentieth century, invading anterior horn motor neurons to inflict irreversible paralysis."
      },
      {
        "author": "Paul Farmer",
        "work": "Infections and Inequalities",
        "quote": "Global eradication initiatives tracked wild **enterovirus** circulation through systematic sewage and environmental water sampling."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Summer aseptic meningitis outbreaks in pediatric wards were frequently traced to widespread community **enterovirus** exposure."
      }
    ]
  },
  "Dashboard — enter\\entertain.md": {
    "primary": "To provide amusement, diversion, or hospitality to guests or an audience.",
    "secondary": "To give consideration or harbor in the mind (such as a thought, suspicion, or proposal).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Twelfth Night",
        "quote": "Be not afraid of greatness: some are born great, some achieve greatness, and some have greatness thrust upon 'em. **Entertain** thy fortune with a cheerful eye."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Mr. Bingley was lively and unreserved, ready to **entertain** all the guests at the assembly ball with effortless charm."
      },
      {
        "author": "Abraham Lincoln",
        "work": "Second Inaugural Address",
        "quote": "With malice toward none; with charity for all; let us strive on to bind up the nation's wounds and **entertain** no thought of vengeance."
      }
    ]
  },
  "Dashboard — enter\\entertained.md": {
    "primary": "Provided with amusement, enjoyment, or hospitality; or considered and held in mind.",
    "secondary": "Kept in thought or harbored within the imagination over an extended period.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Pip sat by the fireside, thoroughly **entertained** by Joe Gargery's gentle humor and rustic tales."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Sherlock Holmes had never for a single moment **entertained** the hypothesis of a supernatural hound."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "For many months I **entertained** the wildest dreams of discovering the hidden elixir that could conquer mortality."
      }
    ]
  },
  "Dashboard — enter\\entertainer.md": {
    "primary": "A person who provides entertainment, especially an actor, singer, comedian, or musician who performs for an audience.",
    "secondary": "A host who warmly receives, accommodates, and provides hospitality to guests.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Autobiography",
        "quote": "The traveling minstrel was a versatile **entertainer**, capable of reducing his audience from roaring laughter to quiet tears within minutes."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Importance of Being Earnest",
        "quote": "A truly charming **entertainer** never allows dinner conversation to drift into serious political debate."
      },
      {
        "author": "George Orwell",
        "work": "The Road to Wigan Pier",
        "quote": "On Saturday nights, the local pub was packed with factory hands listening to a spirited working-class **entertainer**."
      }
    ]
  },
  "Dashboard — enter\\entertaining.md": {
    "primary": "Providing amusement, diversion, or enjoyment; pleasantly diverting.",
    "secondary": "The practice of hosting social gatherings and accommodating guests in one's home.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "Emma found her companion's lively gossip exceptionally **entertaining**, though she recognized its occasional lack of charity."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs. Dalloway",
        "quote": "Clarissa excelled at the delicate art of **entertaining**, bringing disparate souls together under the glowing chandeliers."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Holmes's demonstration of deductive observation was as **entertaining** as a theatrical conjuring trick."
      }
    ]
  },
  "Dashboard — enter\\entertainingly.md": {
    "primary": "In an entertaining, engaging, or amusing manner.",
    "secondary": "With lively wit, charming hospitality, or captivating narrative skill.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Micawber spoke **entertainingly** of his financial prospects, flourishing his cane as if riches awaited around the next corner."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Ralph Touchett observed the social pageantry from his armchair, chatting **entertainingly** about the foibles of European society."
      },
      {
        "author": "Mark Twain",
        "work": "Roughing It",
        "quote": "The old stagecoach driver spun frontier yarns so **entertainingly** that the bumpy journey across the alkali desert passed in a flash."
      }
    ]
  },
  "Dashboard — enter\\entertainment.md": {
    "primary": "The action of providing or being provided with amusement or enjoyment; a performance or show.",
    "secondary": "Hospitality provided to guests; or the maintenance of ideas and reflections in the mind.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "The evening's musical **entertainment** was enlivened by Mary's ambitious, if somewhat stiff, performance at the pianoforte."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The high court proceedings offered little **entertainment** to the suitors whose fortunes were consumed by endless chancery bills."
      },
      {
        "author": "Francis Bacon",
        "work": "The Essays",
        "quote": "Travel in the younger sort is a part of education; in the elder, a part of experience and noble **entertainment**."
      }
    ]
  },
  "Dashboard — enter\\entity.md": {
    "primary": "A thing with distinct and independent existence.",
    "secondary": "In philosophy and computer science, an ontological being, unit, or database object possessing well-defined attributes and relationships.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "The mind abstracts general ideas from individual things, conceiving of each substance as a distinct **entity** in nature."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "No **entity** without identity: to accept a conceptual class into our ontology, we must provide clear identity criteria for its members."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Analysis of Matter",
        "quote": "Modern physics replaces the static material substance with an event-based structure, where no enduring **entity** exists outside relations."
      }
    ]
  },
  "Dashboard — enter\\entrance.md": {
    "primary": "An opening, door, or passage by which one enters a place; or to fill someone with wonder, enchantment, or delight.",
    "secondary": "The right, permission, or act of entering a physical sanctuary, profession, or esoteric society.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Macbeth",
        "quote": "The raven himself is hoarse / That croaks the fatal **entrance** of Duncan / Under my battlements."
      },
      {
        "author": "John Keats",
        "work": "Ode on a Grecian Urn",
        "quote": "Heard melodies are sweet, but those unheard / Are sweeter; soft pipes that **entrance** the listening spirit."
      },
      {
        "author": "John Bunyan",
        "work": "The Pilgrim's Progress",
        "quote": "Christian knocked earnestly at the narrow wicket gate, seeking joyful **entrance** onto the path to the Celestial City."
      }
    ]
  },
  "Dashboard — enter\\entranced.md": {
    "primary": "Filled with wonder, delight, or bewitchment, as if under a spell or in a trance.",
    "secondary": "In cognitive psychology and aesthetics, profoundly absorbed by music, beauty, or contemplative absorption.",
    "quotes": [
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "I listened to the sweet voice of Safie as she played the guitar, completely **entranced** by the exquisite melody."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The masthead watchman stood **entranced** by the rolling sapphire swells, dreaming away whole sunny watches in oceanic reverie."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Lily Briscoe remained **entranced** before her canvas, watching colors harmonize into sudden structural revelation."
      }
    ]
  },
  "Dashboard — enter\\entrancement.md": {
    "primary": "A feeling of being entranced; a state of wonder, delight, or hypnotic fascination.",
    "secondary": "In mysticism and psychology, a deep absorption in an aesthetic object or ecstatic trance that suspends awareness of external surroundings.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "Roderick Usher's wild improvisations upon the guitar held me in a somber, unearthly **entrancement**."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I sat on my sunny doorstep from sunrise till noon, rapt in a revery, amidst the pines, in undisturbed **entrancement**."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The mystic describes a profound state of **entrancement** where all sensory boundaries dissolve into unitive consciousness."
      }
    ]
  },
  "Dashboard — enter\\entrancing.md": {
    "primary": "Capable of filling someone with wonder, delight, or fascination; enchanting or captivating.",
    "secondary": "Describing melodies, landscapes, or perfumes that hold the observer in breathless aesthetic spell.",
    "quotes": [
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "The moonlit garden was filled with the **entrancing** scent of blooming sweetbriar and honeysuckle."
      },
      {
        "author": "John Keats",
        "work": "Endymion",
        "quote": "A thing of beauty is a joy for ever: / Its loveliness increases; it will never / Pass into nothingness, but still will keep / A bower quiet for us, and an **entrancing** sleep."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "Dorian listened to the musical cadence of Lord Henry's voice, finding his cynical paradoxes strangely **entrancing**."
      }
    ]
  },
  "Dashboard — enter\\entrant.md": {
    "primary": "A person or group that enters an examination, competition, organization, or profession.",
    "secondary": "In industrial economics, a new firm entering a market to compete against established incumbent corporations.",
    "quotes": [
      {
        "author": "Joseph Schumpeter",
        "work": "Capitalism, Socialism and Democracy",
        "quote": "The threat of the innovative new **entrant** disciplines entrenched monopolies far more effectively than regulatory mandates."
      },
      {
        "author": "Michael Porter",
        "work": "Competitive Strategy",
        "quote": "Barriers to entry determine how easily an outside **entrant** can contest an industry and erode incumbent profit margins."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "Every young hopeful **entrant** to the literary scene soon discovered the grim reality of unread review copies."
      }
    ]
  },
  "Dashboard — enter\\entry.md": {
    "primary": "An act of going or coming in; an opening or passage; or an item written in a diary, journal, ledger, or reference work.",
    "secondary": "In law and bookkeeping, formal recording of legal documents, transactions, or astronomical observations in a registry.",
    "quotes": [
      {
        "author": "Samuel Pepys",
        "work": "Diary",
        "quote": "And so to bed, closing this day's **entry** with humble thanksgiving for my family's deliverance from the Great Plague."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "Winston dipped his pen in ink and opened the blank diary, terrified by what his first **entry** might reveal."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "In my notebook **entry** for July 1837, I opened my first systematic ledger on the transmutation of species."
      }
    ]
  },
  "Dashboard — enter\\exenterate.md": {
    "primary": "To eviscerate; to remove the contents of an anatomical cavity or internal viscera.",
    "secondary": "In surgical oncology and anatomical dissection, to excise completely the organs and contents of a body compartment (such as the orbit or pelvis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extensive malignant invasion of the maxillary antrum required the surgeon to **exenterate** the entire orbital cavity."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "Before preserving large zoological specimens, collectors carefully **exenterate** the visceral mass to prevent post-mortem putrefaction."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "To achieve clear margins in advanced pelvic sarcoma, the surgical oncology team had to **exenterate** the pelvic basin."
      }
    ]
  },
  "Dashboard — enter\\exenteration.md": {
    "primary": "The surgical removal of the contents of a body cavity, especially the orbit of the eye or the pelvic organs.",
    "secondary": "In radical surgical oncology, an extensive en bloc resection (such as total pelvic exenteration) performed for recurrent, localized cancer.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Total pelvic **exenteration** remains one of the most radical, formidable procedures in modern surgical oncology."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Orbital **exenteration** was successfully carried out to extirpate the aggressive invasive fungal infection of the sinus."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The operative note documented the meticulous multi-organ **exenteration** required to obtain disease-free surgical margins."
      }
    ]
  },
  "Dashboard — enter\\gastroenteritis.md": {
    "primary": "Inflammation of the stomach and intestines, typically resulting from bacterial toxins or viral infection and causing vomiting and diarrhea.",
    "secondary": "In clinical medicine, an acute dehydrating illness ('stomach flu') commonly triggered by norovirus, rotavirus, Salmonella, or Campylobacter.",
    "quotes": [
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Oral rehydration salts transformed the global treatment of acute **gastroenteritis**, saving millions of children from lethal dehydration."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe epidemic **gastroenteritis** in young infants demands vigilant assessment of skin turgor and fontanelle depression."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Standardizing dehydration protocols in the emergency ward dramatically reduced inpatient admissions for viral **gastroenteritis**."
      }
    ]
  },
  "Dashboard — enter\\parenteral.md": {
    "primary": "Administered or occurring elsewhere in the body than the mouth and alimentary canal (such as by intravenous, intramuscular, or subcutaneous injection).",
    "secondary": "In clinical therapeutics, medical nutrition or drug delivery that bypasses the gastrointestinal tract to achieve rapid systemic bioavailability.",
    "quotes": [
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Total **parenteral** nutrition was infused through a central venous line while the patient's ruptured bowel rested and healed."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute diabetic coma, rapid **parenteral** administration of fluids and insulin provides the sole hope of resuscitation."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The pharmacy mixed individualized daily bags of **parenteral** vitamins, amino acids, and lipids for the ICU patient."
      }
    ]
  },
  "Dashboard — enter\\parenterally.md": {
    "primary": "By route other than through the digestive tract, especially by injection directly into veins, muscles, or subcutaneous tissue.",
    "secondary": "In pharmacology, describing therapeutics administered by injection to avoid hepatic first-pass metabolism or gastric degradation.",
    "quotes": [
      {
        "author": "Alexander Fleming",
        "work": "Penicillin",
        "quote": "Because penicillin was destroyed by stomach acid, our initial clinical trials required the antibiotic to be administered **parenterally**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Morphine administered **parenterally** produced swift relief from the agonizing paroxysms of acute biliary colic."
      },
      {
        "author": "Paul Farmer",
        "work": "Infections and Inequalities",
        "quote": "Delivering second-line tuberculosis medications **parenterally** in rural settings required training community health workers in sterile injection."
      }
    ]
  },
  "Dashboard — enter\\reentrant.md": {
    "primary": "Re-entering or directed inward, as an angle pointing inward in a polygon or fortification.",
    "secondary": "In computer science, describing subroutines or code that can be interrupted and safely re-invoked concurrently by multiple execution threads.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The Art of Computer Programming",
        "quote": "A subroutine that avoids shared global state is fully **reentrant**, permitting safe execution within multi-threaded interrupt handlers."
      },
      {
        "author": "Vauban (Sébastien Le Prestre de Vauban)",
        "work": "A Treatise on the Defense of Places",
        "quote": "The bastioned trace was engineered with alternating salient and **reentrant** angles to cross-fire upon approaching sappers."
      },
      {
        "author": "Andrew Tanenbaum",
        "work": "Modern Operating Systems",
        "quote": "System kernel functions must be rigorously **reentrant** to handle nested asynchronous hardware interrupts without data corruption."
      }
    ]
  },
  "Dashboard — enter\\reentry.md": {
    "primary": "The action of entering again; especially the return of a spacecraft or missile into the Earth's atmosphere.",
    "secondary": "In sociology and cardiology, the reintegration of an individual into society, or an abnormal circular cardiac electrical conduction loop causing arrhythmia.",
    "quotes": [
      {
        "author": "Tom Wolfe",
        "work": "The Right Stuff",
        "quote": "The fiery friction of atmospheric **reentry** bathed the capsule heat shield in glowing orange plasma, cutting radio telemetry."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Ablative tiles on the spacecraft belly absorbed thousands of degrees of friction heat during supersonic **reentry** into Florida skies."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Ventricular tachycardia often arises from an electrical **reentry** circuit circulating around an ischemic myocardial scar."
      }
    ]
  },
  "Dashboard — ethm\\ethm.md": {
    "primary": "A combining form derived from Greek ethmos, meaning a sieve or sieve-like structure.",
    "secondary": "In anatomical nomenclature, the prefix element designating the ethmoid bone, ethmoidal sinuses, and cribriform plate of the cranium.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "Anatomists derived the combining form **ethm** from the ancient Greek word for sieve to describe perforated cranial bones."
      },
      {
        "author": "Galen",
        "work": "On the Usefulness of the Parts of the Body",
        "quote": "The creator perforated the nasal ceiling with a sieve-like plate, called from **ethm**, through which aromatic vapors pass to the brain."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The root **ethm** enters into clinical terms denoting delicate trabeculated structures of the upper nasal vault."
      }
    ]
  },
  "Dashboard — ethm\\ethmoid.md": {
    "primary": "A light, spongy, cubical bone located at the roof of the nose between the two orbits, perforated with holes for olfactory nerves.",
    "secondary": "In human osteology, the cranial bone comprising the horizontal cribriform plate, vertical perpendicular plate, and lateral labyrinths containing ethmoidal air cells.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Slender olfactory axonic bundles pass from the nasal neuroepithelium through the cribriform plate of the **ethmoid** to synapse in the olfactory bulb."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Suppuration within the air cells of the **ethmoid** poses grave danger of intracranial extension across the thin orbital roof."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The delicate lamellae of the **ethmoid** bone resemble frozen sea foam, separating the sensory chambers of the nose from the brain."
      }
    ]
  },
  "Dashboard — ethn\\ethn.md": {
    "primary": "A combining form derived from Greek ethnos, meaning people, nation, race, or cultural group.",
    "secondary": "In social sciences and linguistics, the prefix element forming compounds such as ethnic, ethnography, ethnobotany, and ethnology.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language",
        "quote": "The morpheme **ethn** serves as the lexical anchor for disciplines investigating the collective cultural identities of humanity."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Structural Anthropology",
        "quote": "From **ethn**, denoting a living community of people, anthropology constructed its comparative vocabulary of kinship and myth."
      },
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "Greek **ethn** passed into Western academic classification to denote human groupings sharing common customs and tongues."
      }
    ]
  },
  "Dashboard — ethn\\ethnarch.md": {
    "primary": "A ruler of a people, province, or ethnic group, especially one subordinate to an emperor or king.",
    "secondary": "In Hellenistic and Roman provincial administration, a governor appointed over an ethnic community with civil authority without holding royal title.",
    "quotes": [
      {
        "author": "Flavius Josephus",
        "work": "The Jewish War",
        "quote": "Caesar Augustus declined to bestow the royal diadem on Archelaus, appointing him instead as **ethnarch** over half of Herod's realm."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "Roman diplomacy frequently conciliated frontier barbarian tribes by confirming their hereditary chieftain as recognized imperial **ethnarch**."
      },
      {
        "author": "Saint Paul (New Testament: 2 Corinthians)",
        "work": "Epistles",
        "quote": "In Damascus the governor under King Aretas, the **ethnarch**, guarded the city with a garrison, desirous to apprehend me."
      }
    ]
  },
  "Dashboard — ethn\\ethnarchy.md": {
    "primary": "The government, office, jurisdiction, or territory of an ethnarch.",
    "secondary": "In ancient history, a provincial political entity governed by an ethnarch under imperial suzerainty (as in Roman Judaea under Archelaus).",
    "quotes": [
      {
        "author": "Flavius Josephus",
        "work": "Antiquities of the Jews",
        "quote": "The fiscal revenues of the **ethnarchy** were surveyed by Roman commissioners following the deposition of Archelaus."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The fragmented **ethnarchy** dissolved when imperial legions annexed the territory into direct provincial administration."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "Alexander's successors maintained the autonomous **ethnarchy** as a pragmatic buffer along the Syrian desert borders."
      }
    ]
  },
  "Dashboard — ethn\\ethnic.md": {
    "primary": "Relating to a population subgroup with a common national, cultural, or ancestral tradition.",
    "secondary": "In sociology and anthropology, designating social identities defined by shared language, historical memory, folklore, and dietary customs.",
    "quotes": [
      {
        "author": "Claude Lévi-Strauss",
        "work": "Tristes Tropiques",
        "quote": "Each **ethnic** enclave in the bustling port city preserved its ancient cooking hearths and ancestral weaving motifs."
      },
      {
        "author": "Benedict Anderson",
        "work": "Imagined Communities",
        "quote": "Modern nationalism reconfigured older **ethnic** solidarities into standardized linguistic and political identities."
      },
      {
        "author": "Margaret Mead",
        "work": "Coming of Age in Samoa",
        "quote": "Cultural diversity demonstrates that human nature adapts plastic habits to the unique traditions of each **ethnic** group."
      }
    ]
  },
  "Dashboard — ethn\\ethnical.md": {
    "primary": "Of or relating to ethnicity or race; ethnic (formal or archaic variant).",
    "secondary": "In nineteenth-century ethnology, describing comparative cultural and racial characteristics of human populations.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Geographical barriers and natural selection molded the distinct **ethnical** varieties of the human species over millennia."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Comparative mythology traces recurring religious motifs across diverse **ethnical** divisions of the globe."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "Craniometric surveys revealed significant variation among the disparate **ethnical** groups of the Pacific rim."
      }
    ]
  },
  "Dashboard — ethn\\ethnically.md": {
    "primary": "In a manner relating to ethnicity, race, or cultural background.",
    "secondary": "With regard to ethnic identity, customs, or ancestral heritage.",
    "quotes": [
      {
        "author": "Benedict Anderson",
        "work": "Imagined Communities",
        "quote": "The empire encompassed an **ethnically** diverse population bound together only by allegiance to the Habsburg crown."
      },
      {
        "author": "Jared Diamond",
        "work": "Guns, Germs, and Steel",
        "quote": "New Guinea highlands remain **ethnically** and linguistically the most fragmented landscape on earth."
      },
      {
        "author": "Francis Fukuyama",
        "work": "The Origins of Political Order",
        "quote": "States that fail to accommodate **ethnically** distinct minorities risk recurring civil fracture and institutional decay."
      }
    ]
  },
  "Dashboard — ethn\\ethnicity.md": {
    "primary": "The fact or state of belonging to a social group that has a common national or cultural tradition.",
    "secondary": "In sociology and political science, a dynamic social construct rooted in shared heritage, language, customs, and collective identity.",
    "quotes": [
      {
        "author": "Clifford Geertz",
        "work": "The Interpretation of Cultures",
        "quote": "Primordial attachments based on blood, speech, and custom endow **ethnicity** with immense emotional and political force."
      },
      {
        "author": "Benedict Anderson",
        "work": "Imagined Communities",
        "quote": "Print-capitalism unified dispersed dialects, reshaping traditional **ethnicity** into national consciousness."
      },
      {
        "author": "Kwame Anthony Appiah",
        "work": "The Lies That Bind: Rethinking Identity",
        "quote": "We construct **ethnicity** through shared stories and social expectations, though biology shows our lineages are thoroughly intertwined."
      }
    ]
  },
  "Dashboard — ethn\\ethnoarchaeology.md": {
    "primary": "The ethnographic study of living peoples and contemporary material culture for archaeological purposes.",
    "secondary": "In anthropological methodology, studying current manufacturing, discarding, and settlement practices to create analog models for interpreting ancient archaeological deposits.",
    "quotes": [
      {
        "author": "Lewis Binford",
        "work": "Bones: Ancient Men and Modern Myths",
        "quote": "Through rigorous **ethnoarchaeology** among Nunamiut hunters, I documented how butchering patterns map onto bone bed refuse."
      },
      {
        "author": "Ian Hodder",
        "work": "Reading the Past",
        "quote": "Fieldwork in **ethnoarchaeology** revealed that material symbols actively negotiate social power rather than passively reflecting ecology."
      },
      {
        "author": "Colin Renfrew",
        "work": "Archaeology: Theories, Methods, and Practice",
        "quote": "Modern **ethnoarchaeology** bridges the silent stones of ancient ruins with the living behaviors of traditional communities."
      }
    ]
  },
  "Dashboard — ethn\\ethnocentric.md": {
    "primary": "Evaluating other peoples and cultures according to the standards and preconceptions of one's own culture.",
    "secondary": "Characterized by an implicit belief in the inherent superiority of one's own cultural, national, or ethnic group.",
    "quotes": [
      {
        "author": "Franz Boas",
        "work": "The Mind of Primitive Man",
        "quote": "Anthropology dismantles the **ethnocentric** conceit that Western industrial civilization represents the pinnacle of human culture."
      },
      {
        "author": "Ruth Benedict",
        "work": "Patterns of Culture",
        "quote": "Western travelers viewed native ritual practices through an **ethnocentric** lens that blinded them to internal symbolic coherence."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Race and History",
        "quote": "The **ethnocentric** attitude is so deeply rooted that every society tends to equate its own customs with the definition of humanity."
      }
    ]
  },
  "Dashboard — ethn\\ethnocentrism.md": {
    "primary": "The evaluation of other cultures according to preconceptions originating in the standards and customs of one's own culture.",
    "secondary": "In sociology and psychology, the universal human tendency to favor one's ingroup and dismiss outgroup values as inferior, irrational, or barbarous.",
    "quotes": [
      {
        "author": "William Graham Sumner",
        "work": "Folkways",
        "quote": "I introduced the term **ethnocentrism** to denote the view of things in which one's own group is the center of everything, and all others are scaled with reference to it."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Tristes Tropiques",
        "quote": "The original sin of the explorer is **ethnocentrism**, projecting home-grown categories upon foreign modes of being."
      },
      {
        "author": "Franz Boas",
        "work": "Anthropology and Modern Life",
        "quote": "A scientific education in cultural relativism provides our most potent antidote against the poison of narrow **ethnocentrism**."
      }
    ]
  },
  "Dashboard — ethn\\ethnographer.md": {
    "primary": "An anthropologist or social scientist who studies, describes, and writes about human cultures through immersive participant observation.",
    "secondary": "In cultural research, a fieldworker who conducts qualitative ethnography to document social practices, kinship structures, and ritual life.",
    "quotes": [
      {
        "author": "Bronislaw Malinowski",
        "work": "Argonauts of the Western Pacific",
        "quote": "The goal of the true **ethnographer** is to grasp the native's point of view, his relation to life, to realize his vision of his world."
      },
      {
        "author": "Margaret Mead",
        "work": "Letters from the Field",
        "quote": "As an **ethnographer** in a coastal Samoan village, I lived in thatched huts, learning the cadence of daily gossip and song."
      },
      {
        "author": "Clifford Geertz",
        "work": "The Interpretation of Cultures",
        "quote": "What the **ethnographer** faces is a multiplicity of complex conceptual structures, which he must first grasp and then render intelligible."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Body Part 3 - Batch 1 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
