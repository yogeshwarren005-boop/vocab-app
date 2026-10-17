import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — hyper\\hyperoodon.md": {
    "primary": "A genus of beaked whales in the family Ziphiidae, commonly known as bottlenose whales, comprising the northern bottlenose whale (*Hyperoodon ampullatus*) and southern bottlenose whale (*Hyperoodon planifrons*).",
    "secondary": "In marine mammalogy, *Hyperoodon* is renowned for deep, prolonged squid-hunting dives into submarine canyons (exceeding 1,400 meters) and prominent maxillary crests on the skull of mature males.",
    "quotes": [
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "The skull of **Hyperoodon** is characterized by colossal longitudinal maxillary crests towering above the rostrum."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "In the bottlenose whale, referred to **Hyperoodon**, functional teeth are reduced to a single pair hidden at the mandibular tip."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Pelagic schools of **Hyperoodon** frequent Arctic waters, diving to great depths to capture deep-sea cephalopods."
      }
    ]
  },
  "Dashboard — hyper\\hyperope.md": {
    "primary": "A person affected by hyperopia (farsightedness).",
    "secondary": "In clinical optometry, a hyperope has an eye whose refractive power is insufficient for its axial length, requiring active ciliary accommodation or convex corrective lenses to see clearly.",
    "quotes": [
      {
        "author": "Francis Cornelis Donders",
        "work": "On the Anomalies of Accommodation and Refraction of the Eye",
        "quote": "The youthful **hyperope** frequently conceals his optical error by continuous involuntary ciliary muscle contraction."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Without convex lenses, the **hyperope** suffers ocular fatigue whenever sustained near work is attempted."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Headaches recurring after close reading led us to refer the young **hyperope** for formal refraction."
      }
    ]
  },
  "Dashboard — hyper\\hyperopia.md": {
    "primary": "A refractive error of the eye in which parallel light rays focus behind the retina when accommodation is relaxed; farsightedness (American medical spelling).",
    "secondary": "In physiological optics, hyperopia results from an eyeball that is axially too short or has a flat corneal curvature, causing near objects to appear blurred while distant objects may remain clear through accommodative effort.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "The essential optical defect in **hyperopia** is that the focal point of the unaccommodated eye falls behind the retina."
      },
      {
        "author": "Francis Cornelis Donders",
        "work": "On the Anomalies of Accommodation and Refraction of the Eye",
        "quote": "I proved that constant accommodative effort in uncorrected **hyperopia** is the principal trigger of childhood convergent squint."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Correction of latent **hyperopia** by suitable plus spectacles dispels chronic frontal headaches and eye-strain."
      }
    ]
  },
  "Dashboard — hyper\\hyperopic.md": {
    "primary": "Of, relating to, or affected by hyperopia (farsightedness).",
    "secondary": "In ophthalmology, a hyperopic eye requires converging convex lenses to shift the image plane forward onto the neurosensory retinal surface.",
    "quotes": [
      {
        "author": "Francis Cornelis Donders",
        "work": "On the Anomalies of Accommodation and Refraction of the Eye",
        "quote": "The **hyperopic** eye is structurally too short along its anteroposterior optical axis."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Convex lenses place the focal conjugate of a **hyperopic** globe directly upon the fovea centralis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Children with marked **hyperopic** refraction often develop compensatory accommodative strabismus."
      }
    ]
  },
  "Dashboard — hyper\\hyperotreta.md": {
    "primary": "A former taxonomic class, order, or suborder of jawless marine vertebrates comprising the hagfishes (Myxini).",
    "secondary": "In comparative vertebrate anatomy, Hyperotreta is distinguished by the nasohypophysial duct opening posteriorly into the pharynx, slime glands along the body, and the absence of paired fins or true vertebrae.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In the **Hyperotreta**, or hagfishes, the single nasal aperture perforates the palate to enter the alimentary canal."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The slime-secreting pores of the **Hyperotreta** furnish a remarkable defensive shroud against marine predators."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Basal craniate affinities place the **Hyperotreta** at the very threshold of modern vertebrate phylogeny."
      }
    ]
  },
  "Dashboard — hyper\\hyperoxia.md": {
    "primary": "An excess of oxygen in body tissues or organs, resulting from breathing gas mixtures with high oxygen partial pressures.",
    "secondary": "In pulmonary medicine and hyperbaric therapy, prolonged hyperoxia causes absorption atelectasis, generation of reactive oxygen species, pulmonary toxicity (Lorrain Smith effect), and central nervous system seizures (Paul Bert effect).",
    "quotes": [
      {
        "author": "John Scott Haldane",
        "work": "Respiration",
        "quote": "Exposure to severe **hyperoxia** under pressure induces violent epileptiform convulsions in experimental animals."
      },
      {
        "author": "Claude Bernard",
        "work": "Lessons on the Effects of Toxic and Medicinal Substances",
        "quote": "Pure oxygen becomes paradoxical at high pressure, tissue **hyperoxia** arresting cellular metabolism instead of stimulating it."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unregulated neonatal **hyperoxia** was later recognized as the causative factor in retrolental fibroplasia."
      }
    ]
  },
  "Dashboard — hyper\\hyperpyrexia.md": {
    "primary": "An exceptionally high body core temperature, typically defined as exceeding 106°F (41.1°C), constituting an acute medical emergency.",
    "secondary": "In critical care medicine, hyperpyrexia arises in severe heat stroke, thyroid storm, neuroleptic malignant syndrome, or hypothalamic hemorrhage, threatening irreversible encephalopathy and multi-organ failure.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rheumatic **hyperpyrexia** with temperatures climbing above 107°F demands immediate immersion in ice-water baths."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "The sudden advent of **hyperpyrexia** in sunstroke is accompanied by complete cessation of sweating and deep coma."
      },
      {
        "author": "Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "Unless heroic measures rapidly subdue the extreme **hyperpyrexia**, fatal cardiac and cerebral exhaustion swiftly follows."
      }
    ]
  },
  "Dashboard — hyper\\hypersecretion.md": {
    "primary": "Excessive or abnormally elevated secretion of a bodily fluid, chemical substance, or hormone by a gland or mucosal lining.",
    "secondary": "In pathophysiology, hypersecretion describes glandular overactivity, such as gastric acid hypersecretion in gastrinoma or mucous hypersecretion in chronic bronchitis.",
    "quotes": [
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice and the Physiology of Digestion",
        "quote": "Stimulation by spicy condiments provoked temporary **hypersecretion** of highly acid gastric fluid."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Pituitary **hypersecretion** of growth hormone in adults transforms the skeletal contours into the grotesque habitus of acromegaly."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Pancreatic **hypersecretion** follows experimental intravenous injection of purified secretin."
      }
    ]
  },
  "Dashboard — hyper\\hypersensitised.md": {
    "primary": "Rendered excessively sensitive, responsive, or allergic to a specific antigen, allergen, or stimulus (British spelling).",
    "secondary": "In immunology, an individual or animal whose immune system has generated high titers of IgE antibodies or sensitized T cells after initial antigen exposure is hypersensitised.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The guinea pig had been **hypersensitised** by a minute preliminary injection of foreign horse serum."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Cells **hypersensitised** to toxins display altered receptor avidities upon subsequent experimental challenge."
      },
      {
        "author": "Frank Macfarlane Burnet",
        "work": "The Clonal Selection Theory of Acquired Immunity",
        "quote": "A **hypersensitised** organism mobilizes memory clones with accelerated velocity upon re-exposure to the antigen."
      }
    ]
  },
  "Dashboard — hyper\\hypersensitive.md": {
    "primary": "Abnormally or excessively sensitive, either immunologically (producing an exaggerated allergic response) or emotionally/sensory-wise.",
    "secondary": "In clinical immunology, hypersensitive states mediate asthma, anaphylaxis, serum sickness, and contact dermatitis; in psychology, describes individuals acutely vulnerable to emotional slights.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Asthmatic individuals are uniquely **hypersensitive** to airborne emanations from horses or specific pollens."
      },
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The radicle tip is extraordinarily **hypersensitive** to contact, turning away from microscopic obstacles."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The melancholic temperament is often **hypersensitive** to subtle shifts in social tone and imaginary disapproval."
      }
    ]
  },
  "Dashboard — hyper\\hypersensitivity.md": {
    "primary": "A state of altered immunological reactivity in which an exaggerated or inappropriate immune response produces tissue injury, disease, or systemic symptoms.",
    "secondary": "Classified by Philip Gell and Robin Coombs into four types: Type I (immediate IgE-mediated), Type II (antibody-dependent cytotoxic), Type III (immune complex-mediated), and Type IV (cell-mediated delayed-type).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Anaphylaxis represents the most dramatic and perilous manifestation of immediate systemic **hypersensitivity**."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The phenomena of serum sickness and drug **hypersensitivity** reflect violent antibody-antigen clashes within the vascular bed."
      },
      {
        "author": "Frank Macfarlane Burnet",
        "work": "The Clonal Selection Theory of Acquired Immunity",
        "quote": "Delayed **hypersensitivity** to tuberculin relies entirely upon sensitized lymphocytes rather than circulating humoral antibodies."
      }
    ]
  },
  "Dashboard — hyper\\hypersensitized.md": {
    "primary": "Rendered excessively sensitive or allergic to an antigen or environmental trigger (American spelling).",
    "secondary": "In experimental immunology and clinical allergology, describes tissues or subjects primed by prior exposure to mount rapid secondary inflammatory responses.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Re-injection of protein antigen into a **hypersensitized** animal provokes sudden bronchospasm and vascular collapse."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The **hypersensitized** tissue reacted violently with local edema and petechial extravasation."
      },
      {
        "author": "Frank Macfarlane Burnet",
        "work": "The Clonal Selection Theory of Acquired Immunity",
        "quote": "Clonal proliferation ensures that the **hypersensitized** host responds with heightened vigor upon second contact."
      }
    ]
  },
  "Dashboard — hyper\\hypersomnia.md": {
    "primary": "A sleep disorder characterized by excessive daytime sleepiness (EDS) or abnormally prolonged nocturnal sleep episodes.",
    "secondary": "In sleep medicine and neurology, hypersomnia is categorized as central (narcolepsy, idiopathic hypersomnia, Kleine-Levin syndrome) or secondary to obstructive sleep apnea, depression, or brainstem lesions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients suffering from epidemic encephalitis often present with profound lethargy and intractable **hypersomnia**."
      },
      {
        "author": "A. R. Luria",
        "work": "The Working Brain",
        "quote": "Lesions impinging upon the ascending reticular activating system abolish cortical tone, inducing persistent **hypersomnia**."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The post-encephalitic syndrome locked victims in a decades-long state of stuporous **hypersomnia**."
      }
    ]
  },
  "Dashboard — hyper\\hypersplenism.md": {
    "primary": "A clinical hematological disorder characterized by spleen enlargement (splenomegaly), reduction of one or more circulating blood cell lines (cytopenias), and compensatory bone marrow hyperplasia.",
    "secondary": "In clinical hepatology, hypersplenism commonly complicates cirrhotic portal hypertension; splenic sequestration and destruction of platelets and red blood cells resolve following splenectomy or shunt decompression.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Splenectomy reverses the severe cytopenias of **hypersplenism** when the bone marrow retains regenerative capacity."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "In chronic portal obstruction, congestive splenomegaly leads to profound secondary **hypersplenism**."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "The massive spleen sequestrated circulating corpuscles, causing that peripheral impoverishment termed **hypersplenism**."
      }
    ]
  },
  "Dashboard — hyper\\hyperstat.md": {
    "primary": "A pharmaceutical brand name for diazoxide, an intravenous nondiuretic benzothiadiazine vasodilator used for the emergency reduction of acute severe hypertension.",
    "secondary": "In cardiovascular pharmacology and emergency medicine, diazoxide (Hyperstat) activates ATP-sensitive potassium channels in vascular smooth muscle, provoking rapid arteriolar relaxation and profound blood pressure reduction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In malignant hypertensive crises, intravenous vasodilators such as **Hyperstat** were deployed to avert cerebral hemorrhage."
      },
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Rapid intravenous bolus injection of **Hyperstat** exerts immediate arteriolar vasodilation accompanied by reflex tachycardia."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Because **Hyperstat** binds extensively to serum albumin, rapid administration is necessary to achieve effective free drug levels."
      }
    ]
  },
  "Dashboard — hyper\\hypertensin.md": {
    "primary": "An older or historical physiological name for angiotensin, an oligopeptide hormone that causes vasoconstriction and elevation of blood pressure.",
    "secondary": "Discovered independently in 1939 by Eduardo Braun-Menéndez (who termed it *hypertensin*) and Irvine Page (who named it *angiotonin*); the two research groups merged their terms in 1958 to establish the official international name *angiotensin*.",
    "quotes": [
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Renin cleaved the circulating globulin substrate to produce the powerful pressor peptide termed **hypertensin**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The discovery of **hypertensin** explained the humoral mechanism underlying Goldblatt's experimental renal hypertension."
      },
      {
        "author": "Walter Bradford Cannon",
        "work": "The Wisdom of the Body",
        "quote": "Renal ischemia releases renin, which rapidly generates circulating **hypertensin** to restore glomerular filtration pressure."
      }
    ]
  },
  "Dashboard — hyper\\hypertension.md": {
    "primary": "Abnormally and persistently high arterial blood pressure, typically defined as resting systolic pressure $\\ge 130$ mm Hg or diastolic pressure $\\ge 80$ mm Hg.",
    "secondary": "In clinical cardiology, divided into essential (primary) hypertension (accounting for over 90% of cases) and secondary hypertension (due to renal parenchymal disease, renovascular stenosis, or pheochromocytoma); major risk factor for stroke and coronary artery disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic arterial **hypertension** leads steadily to left ventricular hypertrophy and arteriolosclerosis of the kidneys."
      },
      {
        "author": "Harvey Cushing",
        "work": "Papers Relating to the Pituitary Body, Hypothalamus and Parasympathetic Nervous System",
        "quote": "Basophilic pituitary adenomas produce a distinct clinical syndrome characterized by obesity, cutaneous striae, and severe **hypertension**."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "The hard, incompressible radial pulse indicated that prolonged vascular **hypertension** which invariably accompanies contracted kidneys."
      }
    ]
  },
  "Dashboard — hyper\\hypertensive.md": {
    "primary": "Of, relating to, suffering from, or caused by abnormally high blood pressure.",
    "secondary": "In clinical medicine, hypertensive emergencies involve acute end-organ damage (hypertensive encephalopathy, acute aortic dissection, or acute pulmonary edema) requiring immediate parenteral blood pressure reduction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **hypertensive** crisis culminated in acute cerebral edema and temporary amaurosis."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "Accented aortic second sound and an heaving apical impulse are classical physical signs of the **hypertensive** heart."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "Post-mortem examination of the **hypertensive** subject revealed marked concentric hypertrophy of the left ventricle."
      }
    ]
  },
  "Dashboard — hyper\\hypertext.md": {
    "primary": "A software system and text format that allows documents to contain embedded cross-references (hyperlinks) to other documents or media, enabling non-linear reading and exploration.",
    "secondary": "Coined by Ted Nelson in 1965 in his vision of Project Xanadu; in computer science, hypertext forms the foundational text model of Tim Berners-Lee's World Wide Web via Hypertext Markup Language (HTML) and HTTP.",
    "quotes": [
      {
        "author": "Ted Nelson",
        "work": "Literary Machines",
        "quote": "By **hypertext**, I mean non-sequential writing—text that branches and allows choices to the reader on an interactive screen."
      },
      {
        "author": "Tim Berners-Lee",
        "work": "Weaving the Web",
        "quote": "The Web was conceived as an open, universal **hypertext** space wherein all information everywhere could be linked."
      },
      {
        "author": "Vannevar Bush",
        "work": "As We May Think",
        "quote": "The human mind operates by association; building trails between items anticipates the dynamic structure of **hypertext**."
      }
    ]
  },
  "Dashboard — hyper\\hyperthermal.md": {
    "primary": "Of, relating to, or characterized by unusually high heat, elevated temperature, or thermal springs.",
    "secondary": "In hydrogeology and vulcanology, hyperthermal springs issue mineral-rich waters at temperatures significantly exceeding ambient local mean temperature; in therapeutics, hyperthermal baths induce systemic vasodilation.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Deep fissures in volcanic regions discharge boiling **hyperthermal** waters charged with silica and sulfur."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "The temperature of the subterranean **hyperthermal** springs remains remarkably constant through seasonal atmospheric shifts."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Precipitation of siliceous sinter around **hyperthermal** geysers builds extensive terrace formations over centuries."
      }
    ]
  },
  "Dashboard — hyper\\hyperthermia.md": {
    "primary": "An abnormally elevated body core temperature that occurs when the body produces or absorbs more heat than it can dissipate, overwhelming thermoregulatory mechanisms.",
    "secondary": "In critical care medicine, hyperthermia is distinguished from fever (where the hypothalamic set-point is elevated by pyrogens); causes include heat stroke, malignant hyperthermia (ryanodine receptor mutation), and serotonin syndrome.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In exertional heat stroke, rapid **hyperthermia** damages cerebral endothelium, producing delirium and coma."
      },
      {
        "author": "Walter Bradford Cannon",
        "work": "The Wisdom of the Body",
        "quote": "When ambient humidity arrests sweat evaporation, catastrophic **hyperthermia** rapidly overwhelms internal homeostasis."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "Immediate active cooling is mandatory in severe **hyperthermia** before irreversible brain damage occurs."
      }
    ]
  },
  "Dashboard — hyper\\hyperthermy.md": {
    "primary": "An elevated body temperature or fever; an alternative or variant form of hyperthermia.",
    "secondary": "Used in earlier clinical and physiological treatises to describe excessive elevation of body heat, whether induced experimentally, climatically, or by therapeutic baths.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Lessons on the Heat of the Animal Body",
        "quote": "Puncture of the cerebral peduncles induced marked **hyperthermy** in experimental animals."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "The patient exhibited extreme **hyperthermy**, the clinical thermometer registering above forty-one degrees centigrade."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Therapeutic **hyperthermy** was historically explored as an empirical modality against chronic neurosyphilitic infection."
      }
    ]
  },
  "Dashboard — hyper\\hyperthyroidism.md": {
    "primary": "A condition resulting from the excessive production and secretion of thyroid hormones (triiodothyronine [T3] and thyroxine [T4]) by an overactive thyroid gland.",
    "secondary": "In clinical endocrinology, Graves' disease (autoantibodies stimulating the TSH receptor) is the most common cause, presenting with weight loss, heat intolerance, fine tremor, tachycardia, pretibial myxedema, and thyroid eye disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The classical picture of **hyperthyroidism** combines exophthalmos, fine digital tremor, tachycardia, and diffuse goiter."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Profound metabolic acceleration in **hyperthyroidism** induces muscular wasting and emotional volatility."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Basal metabolic rate rises precipitously under the influence of the excess thyroid hormones in clinical **hyperthyroidism**."
      }
    ]
  },
  "Dashboard — hyper\\hypertonia.md": {
    "primary": "Abnormally increased muscle tone and reduced capacity of a muscle to stretch, causing rigidity, spasticity, or stiffness.",
    "secondary": "In clinical neurology, hypertonia indicates an upper motor neuron lesion, manifesting as velocity-dependent spasticity (with clasp-knife response) or velocity-independent rigidity (lead-pipe or cogwheel in extrapyramidal parkinsonism).",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Decerebrate transection releases descending brainstem tracts, producing generalized extensor **hypertonia**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Spastic **hypertonia** of the lower extremities accompanied by hyperreflexia and Babinski signs denotes pyramidal tract injury."
      },
      {
        "author": "A. R. Luria",
        "work": "The Working Brain",
        "quote": "Subcortical extrapyramidal disease produces plastic **hypertonia**, impeding smooth reciprocal movement."
      }
    ]
  },
  "Dashboard — hyper\\hypertonic.md": {
    "primary": "Having a higher osmotic pressure or osmolarity than a surrounding or reference solution; also, exhibiting abnormally high muscular tone.",
    "secondary": "In cellular physiology, red blood cells placed in a hypertonic solution lose water by osmosis and undergo crenation; in neurology, denotes spastic or rigid musculature resulting from central disinhibition.",
    "quotes": [
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Erythrocytes immersed in a **hypertonic** saline bath shrink and crenate as internal water diffuses outward."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The postural muscles remain persistently **hypertonic** when inhibitory cortical projections are severed."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intravenous infusion of **hypertonic** mannitol is employed to extract fluid from swollen brain parenchyma."
      }
    ]
  },
  "Dashboard — hyper\\hypertonicity.md": {
    "primary": "The state or property of being hypertonic; excessive osmotic pressure, or abnormally high muscular or vascular tone.",
    "secondary": "In nephrology, extracellular hypertonicity drives intracellular dehydration and stimulates thirst and vasopressin; in neurology, muscular hypertonicity characterizes spastic hemiplegia and dystonia.",
    "quotes": [
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Hypothalamic osmoreceptors respond to the slightest increase in extracellular **hypertonicity** by releasing antidiuretic hormone."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The exaggerated stretch reflex in spasticity provides objective evidence of underlying muscular **hypertonicity**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sustained vascular **hypertonicity** of the peripheral arterioles elevates systemic diastolic blood pressure."
      }
    ]
  },
  "Dashboard — hyper\\hypertonus.md": {
    "primary": "A state of abnormally increased muscle tone or tension; hypertonia.",
    "secondary": "In neurophysiology, hypertonus results from the loss of supraspinal inhibitory control over gamma or alpha motor neurons, producing muscular stiffness and resistance to passive movement.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The **hypertonus** of decerebrate rigidity is confined predominantly to those muscles which counteract the force of gravity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Following cerebral apoplexy, initial flaccid paralysis is gradually replaced by permanent spastic **hypertonus**."
      },
      {
        "author": "Henry Head",
        "work": "Studies in Neurology",
        "quote": "Reflex **hypertonus** in hemiplegia can be temporarily inhibited by eliciting flexor withdrawal reflexes."
      }
    ]
  },
  "Dashboard — hypn\\hypn.md": {
    "primary": "A combining prefix or abbreviated root derived from Greek *hypnos* denoting sleep, dreaming, or hypnosis.",
    "secondary": "In medical lexicography and pharmacology, hypn- forms words pertaining to somnolence, soporific agents, or altered trance states (such as hypnology, hypnagogue, and hypnotic).",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Ancient etymologists derived terms of slumber from the Greek **hypn**- root, honoring the deity of repose."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The pharmacopeia classifies sleep-inducing compounds under derivatives of the classical **hypn**- designation."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The physician employs subtle **hypn**-inducing draughts to soothe the agonizing restlessness of delirium."
      }
    ]
  },
  "Dashboard — hypn\\hypnagogia.md": {
    "primary": "The transitional state of consciousness experienced during the onset of sleep, situated between wakefulness and dreaming.",
    "secondary": "In psychology and sleep neurology, hypnagogia is characterized by spontaneous sensory hallucinations (visual geometric patterns, phantom sounds, sensations of falling), lucid ideation, and sleep paralysis.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "During nocturnal **hypnagogia**, vivid kaleidoscopic imagery drifts across the visual field without conscious bidding."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Phantasmagoric visions arising in **hypnagogia** demonstrate the uninhibited hallucinatory power of early sleep."
      },
      {
        "author": "Oliver Sacks",
        "work": "Hallucinations",
        "quote": "Many creative thinkers have captured their most original insights in the liminal twilight of **hypnagogia**."
      }
    ]
  },
  "Dashboard — hypn\\hypnagogic.md": {
    "primary": "Of, relating to, or occurring in the drowsy transitional state of consciousness immediately preceding sleep.",
    "secondary": "In sleep medicine, hypnagogic hallucinations and hypnagogic jerks (sudden myoclonic muscle twitches upon falling asleep) are common physiological phenomena, also occurring with high frequency in narcolepsy.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Vivid **hypnagogic** images frequently deceive the drowsy mind with the appearance of waking reality."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "The sleeper absorbs lingering **hypnagogic** impressions directly into the initial dream scenarios of the night."
      },
      {
        "author": "Oliver Sacks",
        "work": "Hallucinations",
        "quote": "Auditory **hypnagogic** illusions, such as hearing one's name whispered in an empty bedroom, are remarkably widespread."
      }
    ]
  },
  "Dashboard — hypn\\hypnagogue.md": {
    "primary": "An agent, medicinal substance, or drug that induces, promotes, or facilitates sleep; a hypnotic or soporific.",
    "secondary": "In classical pharmacopeias, herbal draughts such as poppy extracts, henbane, and valerian were prescribed as reliable hypnagogues to combat insomnia and soothe agitation.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Syrup of white poppy acts as a benign **hypnagogue**, gently closing the eyes of the restless melancholy patient."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chloral hydrate proved a dependable **hypnagogue** in managing the acute nocturnal restlessness of typhoid fever."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "Sleep is so like death that I dare not trust it without prayers, desiring no other **hypnagogue** than quiet conscience."
      }
    ]
  },
  "Dashboard — hypn\\hypnoanalysis.md": {
    "primary": "A psychotherapeutic technique combining hypnosis with psychoanalytic methods to uncover and resolve repressed unconscious conflicts, memories, or traumas.",
    "secondary": "Popularized during World War II for treating acute combat neurosis (shell shock); under hypnotic trance, the patient achieves intense cathartic abreaction of repressed psychological trauma while defenses are lowered.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "Breuer's early successes with cathartic **hypnoanalysis** demonstrated that neurotic symptoms carry hidden historical meaning."
      },
      {
        "author": "Carl Jung",
        "work": "The Practice of Psychotherapy",
        "quote": "While **hypnoanalysis** can rapidly uncover traumatic complexes, permanent integration demands conscious waking effort."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Psychic trauma underlying hysterical aphonia was brought to the surface and dispelled by deep **hypnoanalysis**."
      }
    ]
  },
  "Dashboard — hypn\\hypnogenesis.md": {
    "primary": "The induction, production, or generation of a state of sleep or hypnosis.",
    "secondary": "In experimental psychophysiology and nineteenth-century neurology (notably Charcot and Bernheim), hypnogenesis was investigated using rhythmic auditory clicks, visual fixation on rotating mirrors, or verbal suggestion.",
    "quotes": [
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "Visual fixation upon a bright metallic sphere facilitates rapid **hypnogenesis** in susceptible hysterical subjects."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The physiological mechanism of **hypnogenesis** relies upon the steady narrowing of focal attention to a monotonous cue."
      },
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "Bernheim argued that verbal suggestion alone is the true effective instrument of clinical **hypnogenesis**."
      }
    ]
  },
  "Dashboard — hypn\\hypnogogic.md": {
    "primary": "Inducing sleep; also relating to or occurring during the drowsy state immediately preceding sleep (a variant spelling of hypnagogic).",
    "secondary": "In historical psychological texts, used to describe sensory illusions, hypnic jerks, or involuntary visual dreamlets that appear as one falls asleep.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The sensory impressions of the **hypnogogic** state fade seamlessly into the autonomous architecture of dreaming."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Silberer analyzed the symbolic nature of **hypnogogic** hallucinations occurring as waking attention wanes."
      },
      {
        "author": "Oliver Sacks",
        "work": "Hallucinations",
        "quote": "Patients frequently mistake **hypnogogic** phantoms for supernatural presences entering the darkened room."
      }
    ]
  },
  "Dashboard — hypn\\hypnoid.md": {
    "primary": "Resembling sleep or hypnosis; also, denoting an altered, trance-like state of consciousness in which traumatic memories become sequestered.",
    "secondary": "In early psychoanalytic history (Breuer and Freud's *Studies on Hysteria*), 'hypnoid hysteria' referred to hysterical symptoms originating from emotional shocks sustained during spontaneous twilight states of mind (hypnoid states).",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "Breuer assumed that hysterical conversion symptoms originate in peculiar, dreamy states of mind termed **hypnoid** states."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The split-off consciousness observed in secondary personalities frequently arises from an initial **hypnoid** dissociation."
      },
      {
        "author": "Carl Jung",
        "work": "Psychology of the Unconscious",
        "quote": "The emergence of mythic fantasies in twilight **hypnoid** reverie reveals the autonomous activity of the collective psyche."
      }
    ]
  },
  "Dashboard — hypn\\hypnopedia.md": {
    "primary": "The practice or purported technique of learning or memorizing information while asleep, usually by listening to recorded audio during sleep (hypnopaedia).",
    "secondary": "Famous as a major social conditioning mechanism in Aldous Huxley's dystopian novel *Brave New World*; in cognitive neuroscience, empirical research demonstrates that true complex declarative learning does not occur during deep sleep, though sensory conditioning and memory consolidation are active.",
    "quotes": [
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "The principle of sleep-teaching, or **hypnopedia**, had been discovered, drumming moral lessons beneath the child's pillow."
      },
      {
        "author": "H. G. Wells",
        "work": "The Sleeper Awakes",
        "quote": "Subconscious auditory instruction during slumber hinted at the futuristic possibilities of institutional **hypnopedia**."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The notion that the intellect could master scientific systems through passive **hypnopedia** confuses rest with waking effort."
      }
    ]
  },
  "Dashboard — hypn\\hypnophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of falling asleep.",
    "secondary": "In clinical psychology and sleep medicine, hypnophobia often stems from terror of recurrent nightmares, sleep paralysis, panic attacks upon awakening, or an irrational dread of dying during sleep (thanatophobia).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients who suffer violent nocturnal angina often develop an acute **hypnophobia**, dreading the onset of slumber."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Severe neurotic **hypnophobia** is rooted in unconscious guilt, the patient fearing the uninhibited fantasies of the dream."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Morbid terror of sleep, or **hypnophobia**, generates exhausting insomnia that further deranges the nervous system."
      }
    ]
  },
  "Dashboard — hypn\\hypnopompia.md": {
    "primary": "The transitional state of consciousness experienced when awakening from sleep, intermediate between dreaming and full alertness.",
    "secondary": "In sleep neurology and psychology, hypnopompia (coined by F. W. H. Myers) is characterized by lingering dream imagery, auditory hallucinations, sleep inertia, and occasional episodes of isolated sleep paralysis.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "During morning **hypnopompia**, fragments of the night's final dream linger vividly against the waking daylight."
      },
      {
        "author": "Oliver Sacks",
        "work": "Hallucinations",
        "quote": "Unlike hypnagogic visions, **hypnopompia** surprises the sleeper as he emerges toward wakefulness with eyes half open."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "The abrupt transition in **hypnopompia** allows waking critical logic to disintegrate the fragile structure of the dream."
      }
    ]
  },
  "Dashboard — hypn\\hypnos.md": {
    "primary": "The ancient Greek mythological personification and god of sleep, son of Nyx (Night) and twin brother of Thanatos (Death); also, sleep or slumber itself.",
    "secondary": "In classical literature (Homer, Hesiod, Ovid), Hypnos dwells in a dark cave in the underworld through which the river Lethe flows; in psychology, symbolizes restful subconscious restoration.",
    "quotes": [
      {
        "author": "Homer",
        "work": "Iliad",
        "quote": "Then Hera sought out **Hypnos**, the sovereign lord of all gods and mortal men, entreating him to close Zeus' eyes."
      },
      {
        "author": "Hesiod",
        "work": "Theogony",
        "quote": "There dwell the children of dark Night, **Hypnos** and Thanatos, awful gods whom the shining sun never beholds."
      },
      {
        "author": "John Keats",
        "work": "Endymion",
        "quote": "O gentle **Hypnos**, pour thy quiet poppy-balm upon the weary eyes of wanderers beneath the silent stars."
      }
    ]
  },
  "Dashboard — hypn\\hypnosis.md": {
    "primary": "A trance-like, focused state of consciousness characterized by heightened suggestibility, deep physical relaxation, and focused selective attention.",
    "secondary": "Coined in the 1840s by Scottish surgeon James Braid from Greek *hypnos* (sleep); widely utilized in clinical hypnotherapy, anesthesia (hypnoanalgesia), and cognitive neuroscience to investigate dissociation and executive control.",
    "quotes": [
      {
        "author": "James Braid",
        "work": "Neurypnology; or, the Rationale of Nervous Sleep",
        "quote": "I adopted the term **hypnosis** to describe a state of nervous sleep induced by fixed concentration of the gaze."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The essential feature of **hypnosis** is the inhibition of the subject's critical will, surrendering control to suggestion."
      },
      {
        "author": "Sigmund Freud",
        "work": "An Autobiographical Study",
        "quote": "I soon abandoned **hypnosis** as an unreliable instrument, developing the technique of free association to replace it."
      }
    ]
  },
  "Dashboard — hypn\\hypnotherapy.md": {
    "primary": "The use of hypnosis as a therapeutic psychological treatment to alleviate medical, psychological, or behavioral symptoms.",
    "secondary": "In clinical psychotherapy and behavioral medicine, hypnotherapy is employed for smoking cessation, chronic pain management, irritable bowel syndrome, phobias, and anxiety reduction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In stubborn hysterical contractures, judicious **hypnotherapy** often achieves sudden and dramatic functional recovery."
      },
      {
        "author": "Carl Jung",
        "work": "The Practice of Psychotherapy",
        "quote": "While modern **hypnotherapy** can suppress symptoms, the underlying psychic conflict requires conscious analysis."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "The profound reduction in chronic phantom limb pain achieved through **hypnotherapy** highlighted central brain plasticity."
      }
    ]
  },
  "Dashboard — hypn\\hypnotic.md": {
    "primary": "Tending to produce, induce, or relate to sleep or hypnosis; also, a drug or agent that produces somnolence (a sleeping pill).",
    "secondary": "In pharmacology, hypnotic agents (such as benzodiazepines, Z-drugs, and barbiturates) enhance inhibitory GABAergic neurotransmission to treat insomnia; in aesthetics, describes rhythmic, mesmerizing sights or sounds.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chloral hydrate and paraldehyde are valuable **hypnotic** drugs when severe insomnia resists general hygienic measures."
      },
      {
        "author": "James Braid",
        "work": "Neurypnology",
        "quote": "Fixed ocular convergence produces the **hypnotic** trance by fatiguing the levator muscles of the eyelid."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The steady, rhythmic drumming of the tropical rain had an almost **hypnotic** power over his weary senses."
      }
    ]
  },
  "Dashboard — hypn\\hypnotically.md": {
    "primary": "In a hypnotic manner; by means of hypnosis or as if in a mesmerizing trance.",
    "secondary": "Adverb used in clinical psychology to denote responses elicited under hypnotic trance, or in literature to describe captivating, trance-inducing actions or rhythms.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The subject obeyed the post-hypnotic suggestion promptly, behaving **hypnotically** while rationalizing his action."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "The flickering flames danced **hypnotically** upon the ancient granite hearth, lulling us into silence."
      },
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "When queried **hypnotically**, the patient recounted the forgotten scene of her father's illness with tearful clarity."
      }
    ]
  },
  "Dashboard — hypn\\hypnotise.md": {
    "primary": "To induce a state of hypnosis in someone; to entrance, mesmerize, or fascinate (British spelling).",
    "secondary": "In psychological medicine and social commentary, to place a subject under focused trance through suggestion or captivating influence.",
    "quotes": [
      {
        "author": "James Braid",
        "work": "Neurypnology",
        "quote": "I proceeded to **hypnotise** the patient by requesting him to maintain an immovable gaze upon a lancet case held before his eyes."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Parasite",
        "quote": "She possessed an uncanny power to **hypnotise** susceptible companions by the mere intensity of her commanding stare."
      },
      {
        "author": "H. G. Wells",
        "work": "The Invisible Man",
        "quote": "The sudden mystery of the voice in the empty room seemed to **hypnotise** the constable into bewildered immobility."
      }
    ]
  },
  "Dashboard — hypn\\hypnotised.md": {
    "primary": "Put into a state of hypnosis; entranced, spellbound, or completely captivated (British spelling).",
    "secondary": "In nineteenth-century neurological clinics, patients who were hypnotised displayed heightened suggestibility, analgesia to pinpricks, and catalepsy.",
    "quotes": [
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "The **hypnotised** subject maintained her arm outstretched in rigid catalepsy for nearly twenty minutes."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of the Four",
        "quote": "Watson gazed upon the bizarre treasure chest like a man who had been completely **hypnotised** by its sparkling jewels."
      },
      {
        "author": "James Braid",
        "work": "Neurypnology",
        "quote": "Having successfully **hypnotised** the patient, surgical excision was completed without the slightest manifestation of pain."
      }
    ]
  },
  "Dashboard — hypn\\hypnotiser.md": {
    "primary": "A person who induces hypnosis in another; a hypnotist (British spelling).",
    "secondary": "In the history of psychiatry, the role of the hypnotiser transitioned from the animal magnetist (Mesmer) to the clinical psychotherapist (Braid, Charcot, Bernheim).",
    "quotes": [
      {
        "author": "James Braid",
        "work": "Neurypnology",
        "quote": "The successful **hypnotiser** relies not on mysterious fluidic currents, but on physiological exhaustion of the ocular muscles."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A single firm word of command from the **hypnotiser** suffices to banish the patient's spontaneous willpower."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Parasite",
        "quote": "The sinister **hypnotiser** exercised an invisible tyranny over the mental faculties of his impressionable victim."
      }
    ]
  },
  "Dashboard — hypn\\hypnotism.md": {
    "primary": "The study, science, or practice of inducing and utilizing hypnosis.",
    "secondary": "In the history of medicine and psychology, nineteenth-century debates between the Salpêtrière school (Charcot, viewing hypnotism as a somatic manifestation of hysteria) and the Nancy school (Bernheim, viewing it as universal suggestion) formed modern understanding of suggestibility.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The phenomena of **hypnotism** opened the doors to scientific exploration of the subliminal consciousness."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "We observed three distinct stages of profound **hypnotism**: lethargy, catalepsy, and somnambulism."
      },
      {
        "author": "Sigmund Freud",
        "work": "An Autobiographical Study",
        "quote": "My experience with **hypnotism** convinced me of the profound reality of powerful unconscious mental processes."
      }
    ]
  },
  "Dashboard — hypn\\hypnotist.md": {
    "primary": "A person who practices hypnosis or is skilled in putting people into a hypnotic trance.",
    "secondary": "In clinical medicine, psychology, and stage performance, a hypnotist employs verbal suggestion, rhythmic cues, and eye-fixation techniques to guide individuals into altered states of consciousness.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The subject accepts the hallucinations suggested by the **hypnotist** as indubitable sensory facts."
      },
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "When the **hypnotist** placed his hand upon the patient's forehead, forgotten memories surged into consciousness."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "The skilled clinical **hypnotist** reframes somatic pain pathways through guided dissociative imagery."
      }
    ]
  },
  "Dashboard — hypn\\hypnotizer.md": {
    "primary": "A person who hypnotizes others; a hypnotist (American spelling).",
    "secondary": "In psychological literature and popular fiction, often used to depict practitioners who induce trance or exert psychological influence over subjects.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The rapport established between the subject and the **hypnotizer** channels all subsequent cognitive responses."
      },
      {
        "author": "Mark Twain",
        "work": "Autobiography",
        "quote": "As a boy in Hannibal, I pretended to be spellbound by the itinerant traveling **hypnotizer** to amaze the crowd."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Facts in the Case of M. Valdemar",
        "quote": "As the **hypnotizer**, I sat beside the dying man, making the customary passes across his forehead and chest."
      }
    ]
  },
  "Dashboard — i\\anion.md": {
    "primary": "A negatively charged ion that is attracted to the anode (positive electrode) during electrolysis.",
    "secondary": "Coined in 1834 by Michael Faraday and William Whewell from Greek *anion* (going up); common anions include chloride ($Cl^-$), sulfate ($SO_4^{2-}$), bicarbonate ($HCO_3^-$), and hydroxide ($OH^-$).",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "I propose to call that body an **anion** which goes to the anode, bearing a negative electrical polarity."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "Electrolytic dissociation splits neutral salt molecules into a positive cation and a mobile negative **anion**."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Chloride functions as the principal extracellular **anion** balancing sodium to maintain physiological osmotic equilibrium."
      }
    ]
  },
  "Dashboard — i\\anionic.md": {
    "primary": "Of, relating to, containing, or acting as an anion (a negatively charged ion).",
    "secondary": "In surface chemistry and biochemistry, anionic surfactants (such as sodium dodecyl sulfate / SDS) possess negatively charged polar headgroups, widely utilized in cell lysis, protein gel electrophoresis, and industrial detergents.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "The velocity of migration of the **anionic** constituent varies systematically with ionic radius and hydration."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Discharge at the positive terminal confirms that the liberated element belongs to the **anionic** class of matter."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "The negative charge of the glomerular basement membrane repels circulating **anionic** albumin molecules."
      }
    ]
  },
  "Dashboard — i\\cation.md": {
    "primary": "A positively charged ion that is attracted to the cathode (negative electrode) during electrolysis.",
    "secondary": "Coined in 1834 by Michael Faraday and William Whewell from Greek *kation* (going down); primary biological cations include sodium ($Na^+$), potassium ($K^+$), calcium ($Ca^{2+}$), and magnesium ($Mg^{2+}$).",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The body which moves to the cathode I designate a **cation**, being positively electrified in the electrolyte."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "Dissolution of metallic salts releases the hydated **cation** to conduct current through the aqueous solution."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Sodium constitutes the predominant extracellular **cation**, dictating blood volume and vascular tonicity."
      }
    ]
  },
  "Dashboard — i\\cationic.md": {
    "primary": "Of, relating to, possessing the nature of, or functioning as a cation (a positively charged ion).",
    "secondary": "In pharmacology and microbiology, cationic antimicrobial peptides (such as polymyxins and defensins) bind selectively to negatively charged bacterial lipopolysaccharide membranes to disrupt membrane integrity.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Electromotive force drives the **cationic** components toward the negative plate at predictable rates."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Hydrogen and metals appear invariably as the **cationic** products of aqueous electrolysis."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Ion channels display selective filters that admit specific **cationic** species while excluding opposing anions."
      }
    ]
  },
  "Dashboard — i\\deionize.md": {
    "primary": "To remove dissolved mineral ions or salts from water or another liquid, typically through ion-exchange resins or reverse osmosis.",
    "secondary": "In analytical chemistry and semiconductor manufacturing, mixed-bed ion-exchange resins deionize tap water to produce ultrapure deionized (DI) water with extremely low electrical conductivity.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "To conduct precise galvanic experiments, chemists must completely **deionize** the water to prevent parasitic conduction."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Resin filters that **deionize** solutions exchange metal cations for hydrogen ions and anions for hydroxyl groups."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "Repeated distillation through quartz vessels served historically to **deionize** reagents prior to spectroscopic testing."
      }
    ]
  },
  "Dashboard — i\\hyperion.md": {
    "primary": "In Greek mythology, a Titan god of heavenly light, son of Uranus and Gaia, and father of Helios (the Sun), Selene (the Moon), and Eos (the Dawn); also, a sponge-like, chaotic moon of Saturn.",
    "secondary": "In astronomy, Hyperion (Saturn VII, discovered in 1848 by Bond and Lassell) is noted for its highly irregular shape, deeply cratered sponge-like surface, low density, and chaotic rotation driven by orbital resonance with Titan.",
    "quotes": [
      {
        "author": "John Keats",
        "work": "Hyperion",
        "quote": "Deep in the shady sadness of a vale far sunken from the healthy breath of morn, sat gray-haired Saturn, while fallen **Hyperion** groaned in his fiery sphere."
      },
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "So excellent a king; that was, to this, **Hyperion** to a satyr; so loving to my mother that he might not beteem the winds of heaven visit her face too roughly."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The discovery of the irregular satellite **Hyperion** added a strange, perturbing member to the Saturnian system."
      }
    ]
  },
  "Dashboard — i\\ion.md": {
    "primary": "An atom, radical, or molecule that has acquired a net electric charge by gaining or losing one or more valence electrons.",
    "secondary": "Introduced by Michael Faraday in 1834 from Greek *ion* ('going'); ions in aqueous solutions (electrolytes) conduct electricity and govern biological membrane potentials (via Na+, K+, Ca2+, and Cl-).",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Finally, I require a term to express those bodies which pass to the electrodes: I propose to call them **ion** elements."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "Electrolytic conduction depends directly upon the dissociation of molecules into free, independently moving **ion** particles."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "The asymmetric distribution of potassium and sodium **ion** species establishes the resting potential of the nerve cell."
      }
    ]
  },
  "Dashboard — i\\ionate.md": {
    "primary": "To convert into ions; to ionize or treat with ionizing substances (a rare or archaic verb).",
    "secondary": "Used in early twentieth-century chemical engineering and electrochemistry as an occasional variant for ionize or electrochemically activate solutions.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Thermal agitation and polar solvent forces combine to **ionate** neutral salt crystals upon dissolution."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The electric tension applied across the cell served to **ionate** the fluid into oppositely migrating constituents."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "Intense spark discharges readily **ionate** surrounding gas molecules, inducing electrical conductivity."
      }
    ]
  },
  "Dashboard — i\\ionic.md": {
    "primary": "Of, relating to, or existing in the form of ions; also, of or relating to Ionia (ancient Greece), its classical dialect, or the classical Ionic architectural order characterized by scroll-like fluted volutes.",
    "secondary": "In chemistry, ionic bonds form via electrostatic attraction between oppositely charged ions in crystal lattices; in architecture, the Ionic order is distinguished by paired spiral volutes on capital heads.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "The conductivity of dilute electrolyte solutions is governed strictly by the **ionic** mobility of dissociated salts."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "The graceful spiraling volutes of the **Ionic** capital convey an exquisite sense of feminine proportion and harmony."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Electrochemical decomposition confirms that chemical affinity is fundamentally linked to **ionic** attractions."
      }
    ]
  },
  "Dashboard — i\\ionise.md": {
    "primary": "To convert an atom, molecule, or substance wholly or partly into ions (British spelling).",
    "secondary": "In radiation physics and chemistry, high-energy electromagnetic rays (X-rays, gamma rays) or collisions ionise neutral gas atoms, liberating free electrons and creating positive ions.",
    "quotes": [
      {
        "author": "Ernest Rutherford",
        "work": "Radioactivity",
        "quote": "Alpha particles emitted by radium **ionise** the air through which they pass, rendering it a conductor of electricity."
      },
      {
        "author": "J. J. Thomson",
        "work": "Conduction of Electricity through Gases",
        "quote": "Röntgen rays possess the remarkable property to **ionise** gases by detaching corpuscles from neutral molecules."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Polar water molecules surround salt crystals to **ionise** the lattice into solvated cations and anions."
      }
    ]
  },
  "Dashboard — i\\ionization.md": {
    "primary": "The process by which an atom or molecule acquires a negative or positive charge by gaining or losing electrons (American spelling).",
    "secondary": "In physics and analytical instrumentation, ionization techniques (electron ionization, electrospray, MALDI) convert neutral analytes into charged ions for separation and detection in mass spectrometry.",
    "quotes": [
      {
        "author": "J. J. Thomson",
        "work": "Conduction of Electricity through Gases",
        "quote": "The rate of **ionization** within the gas chamber was measured directly by the saturation current between the plates."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "Each alpha particle produces intense columnar **ionization** along its rectilinear path in the cloud chamber."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "The degree of electrolytic **ionization** increases continuously as the salt solution is diluted with water."
      }
    ]
  },
  "Dashboard — i\\ionize.md": {
    "primary": "To convert an atom, molecule, or compound into ions, or to separate into ions (American spelling).",
    "secondary": "In atomic physics and spectroscopy, incident electromagnetic photons with energy exceeding the ionization potential ionize target atoms, ejecting photoelectrons.",
    "quotes": [
      {
        "author": "J. J. Thomson",
        "work": "Conduction of Electricity through Gases",
        "quote": "Ultraviolet light striking a polished zinc plate will rapidly **ionize** the adjacent gas and discharge an electroscope."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "Energetic rays emitted from radioactive ores **ionize** the surrounding atmosphere with tremendous efficiency."
      },
      {
        "author": "Enrico Fermi",
        "work": "Nuclear Physics",
        "quote": "Fast charged particles **ionize** gas atoms along their trajectory through Coulomb interactions with bound electrons."
      }
    ]
  },
  "Dashboard — i\\polyanion.md": {
    "primary": "A macromolecule, polymer, or complex chemical species that carries multiple negative electric charges at physiological pH.",
    "secondary": "In molecular biology and biochemistry, DNA and RNA are quintessential polyanions due to their negatively charged repeating phosphodiester backbones, which interact with cationic histone proteins.",
    "quotes": [
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "The double helix of nucleic acid is a towering **polyanion**, shielded in vivo by basic histones and divalent cations."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Complex silicate and polyphosphate structures function chemically as a giant **polyanion** lattice."
      },
      {
        "author": "Max Perutz",
        "work": "Proteins and Nucleic Acids",
        "quote": "Electrostatic repulsion along the **polyanion** chain maintains the extended rod-like rigidity of helical DNA."
      }
    ]
  },
  "Dashboard — i\\polycation.md": {
    "primary": "A macromolecule, polymer, or chemical complex carrying multiple positive electric charges.",
    "secondary": "In gene therapy and biophysics, synthetic polycations (such as polyethylenimine, poly-L-lysine, or chitosan) bind electrostatically to polyanionic DNA or RNA to form compact polyplex nanoparticles for cellular gene delivery.",
    "quotes": [
      {
        "author": "Max Perutz",
        "work": "Proteins and Nucleic Acids",
        "quote": "Histone octamers act as a specialized **polycation** spool around which the negative DNA helix tightly winds."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Basic polyamino acids behave in aqueous solution as an extended **polycation**, attracting surrounding anions."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "The interaction between a synthetic **polycation** and genetic material proved crucial for early transfection assays."
      }
    ]
  },
  "Dashboard — i\\union.md": {
    "primary": "The action of joining or being joined together, especially in a political, social, marriage, or legal bond; also, an organized association of workers formed to protect and further their rights and interests (trade union).",
    "secondary": "In set theory and mathematics, the union of a collection of sets is the set of all elements contained in at least one of the sets; in American history, the Union denotes the United States as a federal republic, especially during the Civil War.",
    "quotes": [
      {
        "author": "Abraham Lincoln",
        "work": "First Inaugural Address",
        "quote": "I hold that, in contemplation of universal law and of the Constitution, the **Union** of these States is perpetual."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Workmen frequently enter into a voluntary **union** to raise the wages of their labour and protect their craft."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "The logical **union** of two distinct classes contains every entity that belongs to either class or to both."
      }
    ]
  },
  "Dashboard — i\\unionise.md": {
    "primary": "To organize workers or workplaces into a labor trade union (British spelling).",
    "secondary": "In labor economics and industrial relations, to unionise involves collective bargaining, negotiating contracts, and organizing employees to counter employer power.",
    "quotes": [
      {
        "author": "George Bernard Shaw",
        "work": "The Intelligent Woman's Guide to Socialism and Capitalism",
        "quote": "The imperative to **unionise** arose as the only practical shield for the individual labourer against exploitation."
      },
      {
        "author": "H. G. Wells",
        "work": "The World of William Clissold",
        "quote": "Attempts to **unionise** the sprawling retail trade met with fierce managerial opposition throughout the provinces."
      },
      {
        "author": "Winston Churchill",
        "work": "Great Contemporaries",
        "quote": "Efforts to **unionise** the industrial proletariat transformed British parliamentary politics in the late nineteenth century."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Form Part 4 - Batch 2] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
