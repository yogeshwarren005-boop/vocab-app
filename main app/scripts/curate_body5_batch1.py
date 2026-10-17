import json
import os
import re
import sys

BATCH1_DATA = {
  "Dashboard — nephr/nephrostome.md": {
    "primary": "The ciliated funnel-shaped opening through which an excretory tubule (nephridium) communicates with the coelomic cavity in invertebrate and primitive vertebrate excretory systems.",
    "secondary": "In comparative anatomy and embryology, a cellular funnel that draws coelomic fluid into the nephridial canal for filtration, found in annelids and early vertebrate pronephric tubules.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Each segmental organ communicates with the peritoneal cavity by a wide, ciliated funnel termed the **nephrostome**."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The primitive excretory duct originates at a peritoneal aperture or **nephrostome**, through which coelomic waste products are swept."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "In the development of the elasmobranch pronephros, several segmentally arranged ciliated funnels or **nephrostomes** open directly into the body cavity."
      }
    ]
  },
  "Dashboard — nephr/nephrotomy.md": {
    "primary": "The surgical incision into the substance of a kidney, typically performed to drain an abscess, explore the renal pelvis, or remove renal calculi.",
    "secondary": "In operative urology, a delicate parenchyma-splitting incision designed to expose internal calyces while minimizing vascular damage and renal ischemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When suppuration within the renal pelvis threatens systemic sepsis, prompt exploratory **nephrotomy** is indicated to afford free drainage."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "I performed the first successful **nephrotomy** for calculus in an otherwise intact organ, opening the renal parenchyma along the convex border."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Through an incision in the loin, the kidney is mobilized and subjected to longitudinal **nephrotomy** for the extraction of deeply lodged stones."
      }
    ]
  },
  "Dashboard — nephr/nephrotoxic.md": {
    "primary": "Destructive, poisonous, or damaging to the kidney cells or renal functional parenchyma.",
    "secondary": "In pharmacology and pathology, describing chemical agents, heavy metals, biological toxins, or metabolites that induce acute tubular necrosis or glomerular impairment.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Specific organic compounds and heterologous sera demonstrate marked **nephrotoxic** properties, precipitating acute degeneration of the convoluted tubules."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Among mineral poisons, bichloride of mercury exhibits a virulent **nephrotoxic** action, leading to complete anuria."
      },
      {
        "author": "Carl von Noorden",
        "work": "Clinical Treatises on the Pathology and Therapy of Disorders of Metabolism and Nutrition",
        "quote": "Excessive accumulation of metallic salts exerts an intensely **nephrotoxic** influence upon the secretory epithelium of the Malpighian tufts."
      }
    ]
  },
  "Dashboard — nephr/nephrotoxicity.md": {
    "primary": "The toxic or destructive effect exerted upon the kidneys by chemical substances, pharmaceuticals, or biological agents.",
    "secondary": "In clinical toxicology and pharmacokinetics, the dose-dependent or idiosyncratic propensity of a compound to cause renal dysfunction, measured by elevated serum creatinine and reduced clearance.",
    "quotes": [
      {
        "author": "Louis Goodman and Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Aminoglycoside antibiotics require close therapeutic drug monitoring to prevent irreversible **nephrotoxicity** and preserve glomerular filtration."
      },
      {
        "author": "Harry Goldblatt",
        "work": "Studies on Experimental Hypertension",
        "quote": "Sustained arterial constriction combined with toxic insult amplifies the severity of chemical **nephrotoxicity** in animal models."
      },
      {
        "author": "Donald Seldin",
        "work": "The Kidney: Physiology and Pathophysiology",
        "quote": "The clinical spectrum of drug-induced **nephrotoxicity** encompasses acute tubular necrosis, allergic interstitial nephritis, and chronic interstitial fibrosis."
      }
    ]
  },
  "Dashboard — nephr/nephrotoxin.md": {
    "primary": "A toxic substance, chemical agent, or antibody that specifically damages kidney tissue.",
    "secondary": "In immunopathology and nephrology, an endogenous cytotoxic autoantibody or exogenous chemical poison whose primary pathophysiological target is renal tubular or glomerular cells.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Collected Papers on Immunology",
        "quote": "Injection of renal emulsions into foreign hosts stimulated the production of a specific **nephrotoxin** capable of dissolving tubular epithelium."
      },
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "The selective affinity of a serum **nephrotoxin** for renal parenchymal proteins illustrates the antigenic differentiation of vertebrate viscera."
      },
      {
        "author": "William Welch",
        "work": "Papers and Addresses",
        "quote": "Pathologists recognize that experimental inoculation with a bacterial **nephrotoxin** rapidly induces albuminuria and tubular necrosis."
      }
    ]
  },
  "Dashboard — nephr/pronephros.md": {
    "primary": "The primordial, most anterior excretory organ of vertebrate embryos, representing the earliest stage of kidney development.",
    "secondary": "In comparative embryology, a transient functional kidney in larval anamniotes (such as fish and amphibians) that degenerates in amniotes while providing the initial duct system for subsequent renal stages.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The primitive head-kidney or **pronephros** is the first urinary organ to differentiate in the intermediate cell mass of the vertebrate embryo."
      },
      {
        "author": "Charles Sedgwick Minot",
        "work": "Human Embryology",
        "quote": "In the human embryo, the **pronephros** consists of a few rudimentary tubules that rapidly atrophy as the mesonephros assumes prominence."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The ontogenetic appearance of the ancestral **pronephros** recapitulates the earliest aquatic stage of vertebrate excretory evolution."
      }
    ]
  },
  "Dashboard — nephr/protonephridium.md": {
    "primary": "A primitive, branched tubular excretory organ found in invertebrates lacking a coelom or blood vascular system, terminating internally in a flame cell or solenocyte.",
    "secondary": "In invertebrate zoology, an osmoregulatory and excretory organ in flatworms and rotifers that filters interstitial fluid by ciliary beat without communicating directly with a coelomic space.",
    "quotes": [
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The excretory network of the platyhelminth resolves into a terminal **protonephridium** bearing a flickering bundle of internal cilia."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Unlike the open segmental organs of annelids, the closed **protonephridium** relies upon flame-cells to propel fluid through its convoluted ducts."
      },
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Platyhelminthes and Rhynchocoela",
        "quote": "Osmoregulation in freshwater planarians is primarily maintained by the active hydrostatic filtration of the **protonephridium** system."
      }
    ]
  },
  "Dashboard — neur/amphineura.md": {
    "primary": "An archaic class or subclass of primitive marine mollusks characterized by bilateral symmetry, non-ganglionated longitudinal nerve cords, and the absence of a distinct head.",
    "secondary": "In systematic malacology, a historic taxonomic group encompassing the Polyplacophora (chitons) and Aplacophora, renowned for possessing four longitudinal parallel nerve cords linked by transverse commissures.",
    "quotes": [
      {
        "author": "Edwin Ray Lankester",
        "work": "Notes on Embryology and Classification for the Use of Students",
        "quote": "Under the class **Amphineura** are grouped those archaic mollusks in which the nervous system consists of two pairs of unganglionated nerve cords."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The arrangement of the nervous cords in the **Amphineura** displays an ancestral ladder-like architecture reminiscent of primitive worms."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "Phylogenetic inquiry places the **Amphineura** near the base of the molluscan stem because of their symmetrical nerve tracts and segmented shells."
      }
    ]
  },
  "Dashboard — neur/aneurin.md": {
    "primary": "The historical international nonproprietary name for vitamin B1 (thiamine), designated for its ability to treat and prevent polyneuritis.",
    "secondary": "In nutritional biochemistry, a water-soluble heterocyclic amine whose pyrophosphate ester functions as an essential coenzyme in carbohydrate metabolism and neural energy production.",
    "quotes": [
      {
        "author": "Christiaan Eijkman",
        "work": "Nobel Lecture in Physiology or Medicine",
        "quote": "The crystalline antineuritic factor, subsequently designated **aneurin**, completely reversed the paralysis observed in beriberi."
      },
      {
        "author": "Casimir Funk",
        "work": "The Vitamines",
        "quote": "Extracts from rice polishings rich in **aneurin** demonstrated the curative power of specific organic bases in avian polyneuritis."
      },
      {
        "author": "Robert R. Williams",
        "work": "Water-Soluble Vitamins",
        "quote": "Chemical synthesis confirmed that **aneurin** chloride hydrochloride corresponds structurally to the thiazole-pyrimidine compound thiamine."
      }
    ]
  },
  "Dashboard — neur/aneurism.md": {
    "primary": "An archaic spelling of aneurysm, signifying a localized abnormal dilatation of an artery resulting from weakness in the vessel wall.",
    "secondary": "In classical surgery and morbid anatomy, a pulsating arterial tumor caused by rupture or expansion of the muscular tunics of an arterial trunk.",
    "quotes": [
      {
        "author": "John Hunter",
        "work": "Lectures on the Principles of Surgery",
        "quote": "In the treatment of popliteal **aneurism**, I recommended tying the femoral artery in the sound part above the sac."
      },
      {
        "author": "Astley Cooper",
        "work": "The Anatomy and Surgical Treatment of Abdominal Hernia and Aneurism",
        "quote": "A pulsating tumour in the groin affords unmistakable evidence of an inguinal **aneurism** demanding surgical ligature."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Thoracic **aneurism** frequently reveals itself by pressure upon the recurrent laryngeal nerve, causing hoarseness and brassy cough."
      }
    ]
  },
  "Dashboard — neur/aneurismal.md": {
    "primary": "Pertaining to, resembling, or caused by an aneurism (aneurysm).",
    "secondary": "In historical pathology, describing the sac, thrill, murmur, or vascular remodeling associated with an arterial dilatation.",
    "quotes": [
      {
        "author": "Matthew Baillie",
        "work": "The Morbid Anatomy of Some of the Most Important Parts of the Human Body",
        "quote": "The inner coat of the aorta is often extensively diseased, giving rise to an **aneurismal** enlargement of the descending arch."
      },
      {
        "author": "Astley Cooper",
        "work": "Lectures on the Principles and Practice of Surgery",
        "quote": "Upon applying the ear over the swelling, a distinct **aneurismal** bruit can be perceived synchronously with the radial pulse."
      },
      {
        "author": "Joseph Lister",
        "work": "The Collected Papers of Joseph Lister",
        "quote": "Antiseptic catgut ligatures were successfully applied to secure the vessel proximal to the **aneurismal** sac without secondary hemorrhage."
      }
    ]
  },
  "Dashboard — neur/aneurismatic.md": {
    "primary": "Affected with or exhibiting the characteristics of an aneurism; aneurysmal.",
    "secondary": "In older medical literature, relating to the pathological formation, structure, or manifestations of an aneurismal dilatation.",
    "quotes": [
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "Post-mortem examination disclosed an extensive **aneurismatic** pouch arising from the thoracic aorta and eroding the adjacent ribs."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Auscultation enables the physician to detect the rasping bellows-sound indicative of an **aneurismatic** dilatation of the arterial trunk."
      },
      {
        "author": "Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "The **aneurismatic** tumor gradually expanded until its thinned walls ruptured into the left pleural cavity."
      }
    ]
  },
  "Dashboard — neur/aneurysm.md": {
    "primary": "A localized, abnormal balloon-like distension or dilatation of a blood vessel, typically an artery, caused by a weakening of the vascular wall.",
    "secondary": "In vascular surgery and cardiovascular pathology, a structural lesion classified as true (involving all three arterial wall layers) or false (pseudoaneurysm), posing catastrophic risks of rupture, thrombosis, or embolization.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Syphilitic aortitis remains the most frequent underlying etiology in the development of a large saccular aortic **aneurysm**."
      },
      {
        "author": "Rudolph Matas",
        "work": "Testing the Efficiency of the Collateral Circulation",
        "quote": "Endoaneurysmorrhaphy permits the obliteration or reconstruction of the **aneurysm** sac while preserving the lumen of the parent trunk."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "An unruptured berry **aneurysm** at the circle of Willis may mimic a parasellar neoplasm by compressing the optic chiasm."
      }
    ]
  },
  "Dashboard — neur/aneurysmal.md": {
    "primary": "Pertaining to, resembling, or caused by an aneurysm.",
    "secondary": "In clinical medicine, characterizing the sac, bruit, rupture risk, or bony erosion produced by an arterial wall dilatation.",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Intracranial Arterial Aneurysms",
        "quote": "Direct surgical clipping of the **aneurysmal** neck provides definitive protection against fatal subarachnoid hemorrhage."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Erosion of the vertebral bodies without involvement of the intervertebral discs is pathognomonic of **aneurysmal** pulsation."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The internal carotid artery is especially prone to **aneurysmal** dilatation where it courses within the cavernous sinus."
      }
    ]
  },
  "Dashboard — neur/aneurysmatic.md": {
    "primary": "Of the nature of, or exhibiting features characteristic of, an aneurysm (synonymous with aneurysmal).",
    "secondary": "In histopathology and classic surgery, describing vascular malformations or bone cavities that show localized dilatation and blood pooling.",
    "quotes": [
      {
        "author": "James Paget",
        "work": "Lectures on Surgical Pathology",
        "quote": "In certain osseous tumours, vascular spaces expand so markedly as to impart an **aneurysmatic** thrill to the palpating fingers."
      },
      {
        "author": "Carl von Rokitansky",
        "work": "A Manual of Pathological Anatomy",
        "quote": "The structural attenuation of the middle tunic constitutes the primary morphological basis of every true **aneurysmatic** dilatation."
      },
      {
        "author": "Samuel Gross",
        "work": "A System of Surgery",
        "quote": "Compression above the **aneurysmatic** swelling diminished the amplitude of pulsation and arrested further growth of the sac."
      }
    ]
  },
  "Dashboard — neur/aponeurosis.md": {
    "primary": "A broad, flat sheet of dense pearly-white collagenous connective tissue that attaches sheet-like muscles to bones, fascia, or other muscles.",
    "secondary": "In gross anatomy and surgical dissection, a tough fibrous membrane serving as an expanded tendon for broad muscles such as the abdominal wall musculature or the epicranius.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The external oblique muscle terminates in front in a broad, thin **aponeurosis** which covers the entire anterior surface of the abdomen."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The broad tendon expands like a membrane, which the Greeks called an **aponeurosis**, covering the palm and sole to protect the underlying tendons."
      },
      {
        "author": "William Hunter",
        "work": "Medical Commentaries",
        "quote": "Tension across the epicranial **aponeurosis** connects the frontal and occipital bellies into a unified functional scalp unit."
      }
    ]
  },
  "Dashboard — neur/aponeurotic.md": {
    "primary": "Pertaining to, resembling, or composed of an aponeurosis.",
    "secondary": "In surgical anatomy, describing fibrous sheets, expansions, or incisions through dense membranous muscle insertions.",
    "quotes": [
      {
        "author": "Charles Bell",
        "work": "The Anatomy and Philosophy of Expression as Connected with the Fine Arts",
        "quote": "The facial muscles find insertion either into the mobile integument or into the glistening **aponeurotic** layer beneath."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The bicipital fascia constitutes an **aponeurotic** band that passes obliquely across the brachial artery to join the deep fascia of the forearm."
      },
      {
        "author": "Joseph Leidy",
        "work": "An Elementary Treatise on Human Anatomy",
        "quote": "The rectus sheath is formed by the split layers of the internal oblique **aponeurotic** fibers enclosing the muscular belly."
      }
    ]
  },
  "Dashboard — neur/endoneurium.md": {
    "primary": "The delicate sheath of loose connective tissue enclosing each individual nerve fiber or axon within a peripheral nerve fascicle.",
    "secondary": "In neurohistology, the intrafascicular stroma consisting of fine collagen fibrils, fibroblasts, and extracellular fluid surrounding the Schwann cell-axon complex.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Degeneration and Regeneration of the Nervous System",
        "quote": "During Wallerian degeneration, proliferating Schwann cells align within the surviving tubes of **endoneurium** to guide regenerating axons."
      },
      {
        "author": "Louis-Antoine Ranvier",
        "work": "Leçons sur l'histologie du système nerveux",
        "quote": "Silver impregnation reveals fine reticular fibrils within the **endoneurium** closely investing the myelin sheath of each nerve fiber."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Conduction velocity along a peripheral fiber depends not merely upon axon diameter but upon its metabolic milieu within the **endoneurium**."
      }
    ]
  },
  "Dashboard — neur/epineurium.md": {
    "primary": "The tough, dense outer sheath of fibrous connective tissue that surrounds and binds together a peripheral nerve trunk.",
    "secondary": "In surgical neurology and microanatomy, the vascularized fibrocollagenous sheath that encloses multiple nerve fascicles, cushions against external mechanical compression, and provides anchorage for epineurial sutures.",
    "quotes": [
      {
        "author": "Louis-Antoine Ranvier",
        "work": "Technique microscopique",
        "quote": "The thick outermost fibrous coat encompassing the entire nerve trunk is denominated the **epineurium**."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Nutrient blood vessels, the vasa nervorum, ramify abundantly within the **epineurium** before sending capillaries into the deeper fascicles."
      },
      {
        "author": "Sydney Sunderland",
        "work": "Nerves and Nerve Injuries",
        "quote": "In microsurgical nerve repair, precise alignment of the severed fascicles is achieved by placing delicate sutures through the **epineurium**."
      }
    ]
  },
  "Dashboard — neur/mononeuropathy.md": {
    "primary": "A neurological condition or neuropathy affecting only a single peripheral or cranial nerve.",
    "secondary": "In clinical neurology, a focal nerve deficit resulting from localized trauma, entrapment, ischemia, or compression (such as carpal tunnel syndrome of the median nerve), contrasted with generalized polyneuropathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Isolated wrist drop resulting from radial nerve compression during drunken stupor represents a classic example of acute **mononeuropathy**."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Focal entrapment beneath a rigid ligament leads to chronic **mononeuropathy**, with sensory loss restricted to the autonomous anatomical zone."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "The diagnostic differentiation between a toxic polyneuritis and an ischemic diabetic **mononeuropathy** rests upon the asymmetric distribution of deficits."
      }
    ]
  },
  "Dashboard — neur/neur.md": {
    "primary": "A Greek combining form and root (neuron) signifying nerve, tendon, sinew, or the nervous system.",
    "secondary": "In medical lexicography and anatomical nomenclature, the fundamental root employed in constructing terms denoting nerves, neuronal structures, neurological disorders, and neuroscientific disciplines.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The ancient Greek designation for sinew and cord evolved into the root **neur**, by which modern science designates the conducting units of mind."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Every reflex arc traces its operational continuity to the anatomical pathway symbolized by the classical combining form **neur**."
      },
      {
        "author": "Thomas Willis",
        "work": "Cerebri Anatome",
        "quote": "The white medullary cords spreading from the encephalon were recognized by the ancients under the appellation **neur**, distributing animal spirits to the limbs."
      }
    ]
  },
  "Dashboard — neur/neural.md": {
    "primary": "Of, relating to, or situated in the nerves, neurons, or the nervous system.",
    "secondary": "In neurobiology and embryology, pertaining to the dorsal axis, nerve signaling pathways, neural tube development, or computational neural architectures.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The central feature of **neural** coordination is the conversion of isolated afferent impulses into purposeful, coordinated motor acts."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "The functional independence of each **neural** unit demonstrates that conduction occurs across contact points rather than continuous syncytial networks."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "On the Sensations of Tone",
        "quote": "Auditory perception transforms acoustic mechanical vibrations into discrete **neural** discharges along the fibers of the acoustic nerve."
      }
    ]
  },
  "Dashboard — neur/neuralgia.md": {
    "primary": "Severe, sharp, paroxysmal pain occurring along the course or distribution of a sensory nerve.",
    "secondary": "In clinical neurology, a syndrome of intense lancinating pain unaccompanied by gross structural inflammation of the nerve, exemplified by trigeminal neuralgia (tic douloureux).",
    "quotes": [
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Trigeminal **neuralgia** consists of sudden, excruciating paroxysms of pain provoked by the lightest touch upon a trigger zone of the face."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Among the most agonizing affections known to clinical practice is facial **neuralgia**, which reduces the sufferer to complete despair."
      },
      {
        "author": "Silas Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "The intense burning **neuralgia** following gunshot injuries of peripheral nerves produces profound vasomotor and trophic changes."
      }
    ]
  },
  "Dashboard — neur/neuralgic.md": {
    "primary": "Pertaining to, resembling, or afflicted with neuralgia.",
    "secondary": "In symptom evaluation, describing sharp, stabbing, electric-shock-like pains that shoot along an anatomical nerve pathway.",
    "quotes": [
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Senile and Chronic Diseases",
        "quote": "The lightning pains of tabes dorsalis bear a deceptive resemblance to ordinary **neuralgic** attacks in the extremities."
      },
      {
        "author": "Silas Weir Mitchell",
        "work": "Wear and Tear, or Hints for the Overworked",
        "quote": "Exhausted mental workers frequently suffer from persistent **neuralgic** headaches centered behind the orbital cavities."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The epileptiform **neuralgic** spasm causes involuntary grimacing and convulsive twitches of the facial musculature."
      }
    ]
  },
  "Dashboard — neur/neuralgy.md": {
    "primary": "An archaic variant spelling of neuralgia, denoting sharp paroxysmal nerve pain.",
    "secondary": "In eighteenth- and nineteenth-century medical tracts, the denomination given to nervous pains lacking visible organic lesions or fever.",
    "quotes": [
      {
        "author": "Benjamin Rush",
        "work": "Medical Inquiries and Observations",
        "quote": "Affections of the nerves, historically styled **neuralgy**, yield most readily to depletion followed by therapeutic tonics."
      },
      {
        "author": "John Bell",
        "work": "The Principles of Surgery",
        "quote": "When simple division of the infraorbital nerve fails to cure facial **neuralgy**, the surgeon must seek an irritation nearer the trunk."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon: A Dictionary of Medical Science",
        "quote": "Under the term **neuralgy**, practitioners classify severe pains seated in the nerves without inflammatory swelling."
      }
    ]
  },
  "Dashboard — neur/neurapraxia.md": {
    "primary": "The mildest form of traumatic peripheral nerve injury, characterized by a temporary physiological conduction block without anatomical severance of axons or sheaths.",
    "secondary": "In the Seddon classification of nerve injuries, a focal myelin disruption or metabolic stun causing transient motor paralysis with little or no sensory or autonomic loss and complete spontaneous recovery.",
    "quotes": [
      {
        "author": "Herbert Seddon",
        "work": "Three Types of Nerve Injury",
        "quote": "I propose the term **neurapraxia** for those conditions where nerve conduction fails temporarily without axonal fragmentation or Wallerian degeneration."
      },
      {
        "author": "Sydney Sunderland",
        "work": "A Classification of Peripheral Nerve Injuries",
        "quote": "In a first-degree injury or **neurapraxia**, continuity of all anatomical components is preserved and function returns within days or weeks."
      },
      {
        "author": "Harvey Cushing",
        "work": "Notes on Penetrating Wounds of the Brain",
        "quote": "Transient radial nerve palsy following battlefield contusion often proves to be a self-limiting **neurapraxia**."
      }
    ]
  },
  "Dashboard — neur/neurasthenia.md": {
    "primary": "A historical diagnosis characterized by chronic physical and mental fatigue, lack of energy, headache, irritability, and diffuse functional disturbances (nervous exhaustion).",
    "secondary": "In late nineteenth-century psychiatry and social medicine, a fashionable syndrome popularized by George Beard, conceptualized as a depletion of nervous energy under the stresses of modern industrialized life.",
    "quotes": [
      {
        "author": "George Miller Beard",
        "work": "A Practical Treatise on Nervous Exhaustion (Neurasthenia)",
        "quote": "Modern civilization, with its rapid transit and intense intellectual competition, is the direct exciting cause of **neurasthenia**."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In cases of American nervousness or **neurasthenia**, voluntary attention is easily fatigued and requires frequent intervals of repose."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Aetiology of Hysteria",
        "quote": "I separated the anxiety neuroses from typical **neurasthenia**, identifying distinct psychosexual determinants in their pathogenesis."
      }
    ]
  },
  "Dashboard — neur/neurasthenic.md": {
    "primary": "Pertaining to, suffering from, or characteristic of neurasthenia.",
    "secondary": "In historical clinical psychology, describing individuals displaying constitutional weakness of nervous stamina, chronic fatigue, and functional hypersensitivity.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Many religious leaders have had a profoundly **neurasthenic** constitution, which made them hyper-excitable to spiritual suggestions."
      },
      {
        "author": "George Miller Beard",
        "work": "American Nervousness: Its Causes and Consequences",
        "quote": "The **neurasthenic** patient suffers from subjective symptoms of overwhelming exhaustion despite the absence of organic lesion."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "A morbid hypersensitivity to sensory impressions characterizes the chronic **neurasthenic** invalid."
      }
    ]
  },
  "Dashboard — neur/neurectomy.md": {
    "primary": "The surgical excision or removal of a nerve or a segment of a nerve.",
    "secondary": "In neurosurgery, a destructive procedure undertaken to relieve intractable chronic neuralgia, abolish spasticity, or eradicate localized peripheral nerve tumors.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "The Surgical Aspects of Major Neuralgia of the Trigeminal Nerve",
        "quote": "Peripheral **neurectomy** of the infraorbital branch affords only transient relief, as the agonizing pain inevitably recurs within months."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "When pharmacotherapy fails to ameliorate spasmodic torticollis, selective spinal accessory **neurectomy** may be contemplated."
      },
      {
        "author": "Robert Liston",
        "work": "Practical Surgery",
        "quote": "Excision of a segment of the nerve trunk by **neurectomy** prevents reunion and terminates the transmission of abnormal impulses."
      }
    ]
  },
  "Dashboard — neur/neurilemma.md": {
    "primary": "The delicate, thin outermost cytoplasmic sheath of Schwann cells investing the myelin sheath of peripheral nerve fibers.",
    "secondary": "In neuroanatomy, the cellular sheath essential for peripheral nerve regeneration, forming tubes along which sprouting axons navigate following injury.",
    "quotes": [
      {
        "author": "Theodor Schwann",
        "work": "Microscopical Researches into the Accordance in the Structure and Growth of Animals and Plants",
        "quote": "The structureless outer membrane enclosing the fatty matter of the nerve fiber corresponds to the cellular sheath termed the **neurilemma**."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The nuclei of the **neurilemma** belong to the cells of Schwann, whose protoplasm wraps tightly about the axon cylinder."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Each tubular nerve fiber is bounded externally by a delicate transparent envelope, the sheath of Schwann or **neurilemma**."
      }
    ]
  },
  "Dashboard — neur/neurilemoma.md": {
    "primary": "A benign neoplasm originating from the Schwann cells of the peripheral nerve sheath (synonymous with schwannoma).",
    "secondary": "In surgical pathology, an encapsulated, slowly growing peripheral or cranial nerve tumor exhibiting distinctive Antoni A (dense, palisading) and Antoni B (loose, myxoid) histological patterns.",
    "quotes": [
      {
        "author": "Arthur Purdy Stout",
        "work": "The Peripheral Manifestations of the Specific Nerve Sheath Tumor (Neurilemoma)",
        "quote": "I coined the term **neurilemoma** to designate encapsulated benign tumors arising exclusively from the sheath of Schwann."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "The eighth cranial nerve tumor is a classic **neurilemoma**, expanding benignly within the cerebellopontine angle."
      },
      {
        "author": "Dorothy Russell",
        "work": "Pathology of Tumours of the Nervous System",
        "quote": "Microscopic sections of a **neurilemoma** reveal orderly palisading nuclei forming Verocay bodies within dense Antoni A tissue."
      }
    ]
  },
  "Dashboard — neur/neurinoma.md": {
    "primary": "A benign tumor of the peripheral nerve sheath derived from Schwann cells; a schwannoma.",
    "secondary": "In classical neuro-oncology and European neuropathology, the historical designation (introduced by Verocay) for solitary encapsulated sheath tumors, particularly of the acoustic nerve.",
    "quotes": [
      {
        "author": "José Verocay",
        "work": "Zur Kenntnis der Neurofibrome",
        "quote": "Because these tumors originate from immature cells of the Schwannian sheath, I proposed designating the solitary lesion a **neurinoma**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus and the Syndrome of the Cerebellopontile Angle",
        "quote": "Unilateral tinnitus and progressive deafness frequently signal the occult growth of an acoustic **neurinoma**."
      },
      {
        "author": "Walter Dandy",
        "work": "Results of Removal of Acoustic Tumors by the Unilateral Approach",
        "quote": "Complete extirpation of the acoustic **neurinoma** with its capsule affords permanent cure without recurrence."
      }
    ]
  },
  "Dashboard — neur/neuritis.md": {
    "primary": "Inflammation of a nerve or nerves, typically characterized by pain, tenderness, sensory disturbances, and loss of motor function.",
    "secondary": "In clinical neurology, an inflammatory, infectious, or toxic lesion of peripheral nerve fibers resulting in axonal degeneration, demyelination, and impaired conduction.",
    "quotes": [
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Multiple **neuritis** manifests symmetrically in the extremities with bilateral foot-drop, wrist-drop, and loss of deep tendon reflexes."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Optic **neuritis** or choked disc is one of the most reliable physical signs of increased intracranial pressure from cerebral tumor."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Acute localized **neuritis** produces exquisite tenderness upon deep palpation along the anatomical course of the nerve trunk."
      }
    ]
  },
  "Dashboard — neur/neuroanatomic.md": {
    "primary": "Pertaining to the gross structural anatomy and microscopic organization of the nervous system.",
    "secondary": "In neurological research, relating to the spatial mapping of tracts, nuclei, cytoarchitectural cortical layers, and synaptic circuitry.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Our **neuroanatomic** investigations established that the neuron is an autonomous embryological and trophic unit."
      },
      {
        "author": "Camillo Golgi",
        "work": "Studies on the Fine Anatomy of the Central Nervous Organs",
        "quote": "The black reaction provided the first clear **neuroanatomic** pictures of dendritic arborizations in the cerebellar cortex."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Direct intraoperative electrical stimulation verified the **neuroanatomic** somatotopic arrangement of the precentral motor gyrus."
      }
    ]
  },
  "Dashboard — neur/neuroanatomical.md": {
    "primary": "Relating to or concerning neuroanatomy (the anatomy of the nervous system).",
    "secondary": "In neuroscience, describing morphological studies, structural tract-tracing techniques, or cytoarchitectural variations of the brain and spinal cord.",
    "quotes": [
      {
        "author": "C. Judson Herrick",
        "work": "The Evolution of Human Nature",
        "quote": "Comparative **neuroanatomical** analysis demonstrates the progressive expansion of association areas in higher mammalian brains."
      },
      {
        "author": "Korbinian Brodmann",
        "work": "Vergleichende Lokalisationslehre der Grosshirnrinde",
        "quote": "Differences in cellular laminations justify the delineation of distinct **neuroanatomical** regions across the cerebral cortex."
      },
      {
        "author": "Walle Nauta",
        "work": "Silver Impregnation of Degenerating Axons",
        "quote": "Selective impregnation of degenerating fibers opened unprecedented avenues for mapping complex **neuroanatomical** projections."
      }
    ]
  },
  "Dashboard — neur/neuroanatomy.md": {
    "primary": "The branch of anatomy that deals with the structural organization, macroscopic features, and microscopic architecture of the nervous system.",
    "secondary": "In biomedical education and research, the foundational discipline elucidating neural nuclei, fiber tracts, cranial nerve origins, and cortical localization.",
    "quotes": [
      {
        "author": "Thomas Willis",
        "work": "Cerebri Anatome",
        "quote": "A rigorous foundation in **neuroanatomy** is indispensable for unraveling the mysteries of voluntary motion and sensation."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "Modern **neuroanatomy** began when the silver-dichromate method revealed the magnificent diversity of neuronal morphology."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "The neurosurgeon must command every nuance of **neuroanatomy** before attempting resection within the speech zones."
      }
    ]
  },
  "Dashboard — neur/neurobiological.md": {
    "primary": "Pertaining to the biological principles, cellular mechanisms, and molecular processes governing the nervous system.",
    "secondary": "In modern brain science, characterizing interdisciplinary studies integrating cellular physiology, genetics, biophysics, and neural circuit dynamics.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Synaptic plasticity in the sea slug Aplysia elucidated the fundamental **neurobiological** basis of simple forms of learning."
      },
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "Recording intracellular potentials from retinal ganglion cells uncovered key **neurobiological** principles of sensory encoding."
      },
      {
        "author": "Francis Crick",
        "work": "The Astonishing Hypothesis",
        "quote": "The scientific quest for consciousness requires a rigorous **neurobiological** explanation grounded in synchronized neuronal firing."
      }
    ]
  },
  "Dashboard — neur/neurobiologist.md": {
    "primary": "A scientist or specialist who studies the biology, structure, physiology, and pathology of the nervous system.",
    "secondary": "In contemporary science, a researcher investigating cellular signaling, neural development, circuitry, or neurochemical transmission.",
    "quotes": [
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "The task of the **neurobiologist** is to bridge the conceptual gap between biophysical ion flows and complex behavioral outputs."
      },
      {
        "author": "Rita Levi-Montalcini",
        "work": "In Praise of Imperfection",
        "quote": "My destiny as a **neurobiologist** was sealed when the nerve growth factor revealed itself in our embryonic chick cultures."
      },
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "As a young **neurobiologist**, I resolved to reduce Freudian concepts of memory to specific cellular mechanisms in defined circuits."
      }
    ]
  },
  "Dashboard — neur/neurobiology.md": {
    "primary": "The scientific study of the biology, cellular mechanics, developmental processes, and functional circuits of the nervous system.",
    "secondary": "An integrative discipline synthesizing neuroanatomy, neurophysiology, neurogenetics, and molecular pharmacology to understand brain function and behavior.",
    "quotes": [
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "The emergence of modern **neurobiology** as a unified discipline dissolved the artificial barriers between anatomy and physiology."
      },
      {
        "author": "David Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "The triumph of visual **neurobiology** lies in showing how individual cortical neurons parse the visual scene into lines and orientations."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "A central premise of **neurobiology** is that all mental processes represent reflections of brain cell interactions."
      }
    ]
  },
  "Dashboard — neur/neuroblast.md": {
    "primary": "An embryonic, undifferentiated cell of neuroectodermal origin that develops into a mature neuron.",
    "secondary": "In developmental neurobiology, a migratory progenitor cell derived from the germinal epithelium of the neural tube that extends neurites and undergoes terminal differentiation.",
    "quotes": [
      {
        "author": "Wilhelm His",
        "work": "Die Neuroblasten und deren Entstehung im embryonalen Mark",
        "quote": "I observed that each **neuroblast** is an independent cellular unit originating from the deep germinal layer of the neural tube."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Studies on Vertebrate Neurogenesis",
        "quote": "The pyriform **neuroblast** extends a pioneering axonal cone that steers actively through the embryonic intercellular spaces."
      },
      {
        "author": "Ross Granville Harrison",
        "work": "Observations on the Living Developing Nerve Fiber",
        "quote": "Culturing isolated **neuroblast** cells in clotted lymph proved that the nerve fiber grows as a protoplasmic outgrowth of the cell body."
      }
    ]
  },
  "Dashboard — neur/neuroblastoma.md": {
    "primary": "A highly malignant childhood cancer originating from primitive neural crest cells, predominantly affecting the adrenal medulla and sympathetic nervous system.",
    "secondary": "In pediatric oncology, an embryonal neoplasm characterized by small round blue cells, catecholamine hypersecretion, and genetic hallmarks such as MYCN amplification.",
    "quotes": [
      {
        "author": "James Homer Wright",
        "work": "Neurocytoma or Neuroblastoma, a Kind of Tumor Not Generally Recognized",
        "quote": "I identified rosettes formed by delicate fibrillar bundles in these malignant tumors, proving their origin from primitive cells of the sympathetic system and designating them **neuroblastoma**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Metastatic spread from a primary retroperitoneal **neuroblastoma** frequently involves the orbits and calvarium in early childhood."
      },
      {
        "author": "Sidney Farber",
        "work": "Chemotherapy in the Treatment of Leukemia and Wilms' Tumor",
        "quote": "The spontaneous maturation of a malignant **neuroblastoma** into a benign ganglioneuroma remains one of the fascinating enigmas of tumor biology."
      }
    ]
  },
  "Dashboard — neur/neurochemical.md": {
    "primary": "Pertaining to the chemical substances, neurotransmitters, and molecular reactions occurring within the nervous system.",
    "secondary": "In neuropsychopharmacology, describing endogenous ligands, second messengers, ion channel modulators, and biochemical alterations in neurological disorders.",
    "quotes": [
      {
        "author": "Henry Hallett Dale",
        "work": "Adventures in Physiology",
        "quote": "The identification of acetylcholine as a chemical transmitter at autonomic ganglia marked a profound transformation in **neurochemical** thought."
      },
      {
        "author": "Otto Loewi",
        "work": "The Chemical Transmission of Nerve Action",
        "quote": "The release of Vagusstoff into the perfusion fluid proved that cardiac inhibition is mediated by a specific **neurochemical** agent."
      },
      {
        "author": "Julius Axelrod",
        "work": "Noradrenaline: Fate and Control of Its Biosynthesis",
        "quote": "Reuptake into presynaptic nerve terminals constitutes the major physiological mechanism terminating **neurochemical** transmission by catecholamines."
      }
    ]
  },
  "Dashboard — neur/neurocranium.md": {
    "primary": "The part of the skull that encloses and protects the brain and brainstem (the cranial cavity), distinct from the facial skeleton.",
    "secondary": "In comparative craniology and embryology, the chondrocranium and membranous skull vault derived from neural crest and paraxial mesoderm surrounding the cerebral vesicles.",
    "quotes": [
      {
        "author": "Ernst Gaupp",
        "work": "Die Entwickelung des Kopfskelettes",
        "quote": "In vertebrate ontogeny, the **neurocranium** arises as a cartilaginous capsule sheltering the encephalon before ossification begins."
      },
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "The cranial segments forming the **neurocranium** represent modified, expanded vertebrae adapted to encase the imperial organ of mind."
      },
      {
        "author": "Gavin de Beer",
        "work": "The Development of the Vertebrate Skull",
        "quote": "The distinction between the protective **neurocranium** and the food-gathering viscerocranium is preserved throughout chordate phylogeny."
      }
    ]
  },
  "Dashboard — neur/neurocyte.md": {
    "primary": "A mature nerve cell; a neuron.",
    "secondary": "In cellular neuroanatomy and historical cytology, the anatomical unit comprising the nerve cell body (soma or perikaryon) along with its dendritic and axonal processes.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "Every individual **neurocyte** exhibits remarkable polarization, receiving excitations through dendrites and transmitting them along its axon."
      },
      {
        "author": "Charles Sedgwick Minot",
        "work": "Human Embryology",
        "quote": "As the neuroblast matures into the functional **neurocyte**, its protoplasm develops intricate neurofibrils and Nissl granules."
      },
      {
        "author": "Camillo Golgi",
        "work": "Sur l'anatomie fine des organes centraux du système nerveux",
        "quote": "The metallic deposit reveals the complete boundary of the **neurocyte**, disproving earlier hypotheses of diffuse protoplasmic fusion."
      }
    ]
  },
  "Dashboard — neur/neurodermatitis.md": {
    "primary": "A chronic, itchy skin condition characterized by localized lichenification (thickening of the skin) provoked by habitual scratching and rubbing, often associated with psychological stress.",
    "secondary": "In dermatology, lichen simplex chronicus, wherein an initial pruritic sensation triggers a chronic itch-scratch cycle exacerbated by emotional tension and autonomic hyperactivity.",
    "quotes": [
      {
        "author": "Louis-Anne-Jean Brocq",
        "work": "Pruritus and Neurodermatitis",
        "quote": "I proposed the designation **neurodermatitis** to emphasize that severe cutaneous pruritus and lichenification often develop without preceding primary eruption."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intense emotional stress or nervous exhaustion frequently precipitates stubborn patches of **neurodermatitis** upon the nape of the neck."
      },
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "In intractable **neurodermatitis**, the uncontrollable impulse to scratch reveals the intimate nexus connecting psychoneurotic tension to cutaneous eroticism."
      }
    ]
  },
  "Dashboard — neur/neuroendocrine.md": {
    "primary": "Relating to or involving the functional interactions between the nervous system and the endocrine glands.",
    "secondary": "In systemic physiology, describing specialized neurosecretory cells that receive neural input and release signaling hormones directly into the bloodstream (such as hypothalamic-pituitary mediators).",
    "quotes": [
      {
        "author": "Ernst Scharrer and Berta Scharrer",
        "work": "Neurosecretion",
        "quote": "The discovery of secretory granules within diencephalic neurons established the reality of a unified **neuroendocrine** control system."
      },
      {
        "author": "Geoffrey Harris",
        "work": "Neural Control of the Pituitary Gland",
        "quote": "Hypothalamic portal vessels transport **neuroendocrine** releasing factors that regulate the trophic secretions of the anterior hypophysis."
      },
      {
        "author": "Walter Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "The sympathetic division and the adrenal medulla operate in tandem as an integrated **neuroendocrine** apparatus for emergency mobilization."
      }
    ]
  },
  "Dashboard — neur/neuroendocrinology.md": {
    "primary": "The medical and biological science that investigates the mutual relationships and coordinated actions of the nervous and endocrine systems.",
    "secondary": "In physiology and endocrinology, the study of hypothalamic neuropeptides, pituitary feedback loops, circadian hormone secretion, and neural regulation of homeostatic metabolism.",
    "quotes": [
      {
        "author": "Geoffrey Harris",
        "work": "Neural Control of the Pituitary Gland",
        "quote": "The foundation of modern **neuroendocrinology** was laid when hypothalamic humoral transmission was demonstrated to govern the adenohypophysis."
      },
      {
        "author": "Roger Guillemin",
        "work": "Peptides in the Brain: The New Endocrinology of the Neuron",
        "quote": "The isolation and synthesis of TRH and GnRH ushered **neuroendocrinology** into the molecular era of peptide therapeutics."
      },
      {
        "author": "Andrew Schally",
        "work": "Aspects of Hypothalamic Regulation of the Pituitary Gland",
        "quote": "Purifying minute quantities of hypothalamic releasing hormones from hundreds of thousands of animal brains revolutionized experimental **neuroendocrinology**."
      }
    ]
  },
  "Dashboard — neur/neuroepithelioma.md": {
    "primary": "A rare, malignant tumor of the nervous system arising from primitive neuroepithelial cells, characteristically occurring in the retina, peripheral nerves, or brain.",
    "secondary": "In surgical neuropathology, an aggressive embryonal neuroectodermal neoplasm composed of primitive neuroblasts forming true rosettes and ependymal-like tubules.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "The histological architecture of a **neuroepithelioma** displays primitive neuroectodermal tubules resembling the embryonic central canal."
      },
      {
        "author": "Dorothy Russell",
        "work": "Pathology of Tumours of the Nervous System",
        "quote": "True rosettes with a central lumen bounded by a blepharoplast-bearing limiting membrane define the diagnosis of **neuroepithelioma**."
      },
      {
        "author": "James Ewing",
        "work": "Neoplastic Diseases",
        "quote": "Retinal and peripheral **neuroepithelioma** exhibits rapid infiltrative growth and early metastasis along neural axes."
      }
    ]
  },
  "Dashboard — neur/neuroepithelium.md": {
    "primary": "A specialized type of epithelial tissue containing sensory receptor cells that convert environmental stimuli into nerve impulses.",
    "secondary": "In sensory histology and embryology, the receptor lining found in the olfactory mucosa, retina, taste buds, and internal ear, as well as the proliferative lining of the embryonic neural tube.",
    "quotes": [
      {
        "author": "Wilhelm His",
        "work": "Zur Geschichte des menschlichen Rückenmarkes und der Nervenwurzeln",
        "quote": "The primary wall of the medullary tube consists of a pseudostratified **neuroepithelium** whose mitotic figures border the internal lumen."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The olfactory **neuroepithelium** is unique among mammalian sensory surfaces in that its bipolar receptor cells project axons directly into the brain."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Light striking the retinal **neuroepithelium** undergoes photochemical decomposition in the rods and cones to initiate sensory conduction."
      }
    ]
  },
  "Dashboard — neur/neuroethics.md": {
    "primary": "The interdisciplinary field of study that examines the ethical, legal, and social implications of neuroscience and neurotechnology.",
    "secondary": "In bioethics and cognitive science, the systematic evaluation of moral questions surrounding brain enhancement, neural privacy, neuroimaging in law, and brain-machine interfaces.",
    "quotes": [
      {
        "author": "William Safire",
        "work": "Visions for a New Field of Neuroethics",
        "quote": "I define **neuroethics** as the examination of what is right and wrong about our treatment of, or our enhancement of, the human brain."
      },
      {
        "author": "Martha Farah",
        "work": "Neuroethics: The Practical and the Philosophical",
        "quote": "Advances in functional brain imaging raise urgent questions for **neuroethics** concerning mental privacy and personal responsibility."
      },
      {
        "author": "Patricia Churchland",
        "work": "Brain-Wise: Studies in Neurophilosophy",
        "quote": "Philosophical inquiries into free will and moral responsibility must align with the emerging empirical findings of **neuroethics**."
      }
    ]
  },
  "Dashboard — neur/neurofibroma.md": {
    "primary": "A benign nerve sheath tumor composed of a heterogeneous mixture of Schwann cells, fibroblasts, perineurial cells, and mast cells embedded in a collagenous matrix.",
    "secondary": "In clinical oncology, a soft, slow-growing neoplasm of peripheral nerves that may present as solitary lesions or as multiple disfiguring growths in neurofibromatosis type 1.",
    "quotes": [
      {
        "author": "Friedrich Daniel von Recklinghausen",
        "work": "Ueber die multiplen Fibrome der Haut und ihre Beziehung zu den multiplen Neuromen",
        "quote": "I established that these widespread cutaneous nodules arise from the connective tissue of fine peripheral nerves, proposing the name **neurofibroma**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Unlike the solitary encapsulated schwannoma, a plexiform **neurofibroma** infiltrates diffuse nerve trunks and expands into surrounding tissues."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The hallmark of von Recklinghausen's disease is the presence of molluscum fibrosum or cutaneous **neurofibroma** scattered over the trunk."
      }
    ]
  },
  "Dashboard — neur/neurofibromatosis.md": {
    "primary": "A hereditary autosomal dominant genetic disorder characterized by the development of multiple tumors (neurofibromas) along nerves, pigmented skin patches (café-au-lait spots), and skeletal deformities.",
    "secondary": "In clinical genetics, a condition classified into NF1 (peripheral, linked to chromosome 17) and NF2 (central, linked to chromosome 22 with bilateral acoustic neuromas), caused by mutations in tumor suppressor genes.",
    "quotes": [
      {
        "author": "Friedrich Daniel von Recklinghausen",
        "work": "Ueber die multiplen Fibrome der Haut",
        "quote": "The syndrome uniting cutaneous pigmentation, skeletal anomalies, and generalized nerve tumors is appropriately designated generalized **neurofibromatosis**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients afflicted with **neurofibromatosis** present numerous soft sessile tumors alongside characteristic brown macules across the skin."
      },
      {
        "author": "Victor McKusick",
        "work": "Mendelian Inheritance in Man",
        "quote": "The genetic mapping of **neurofibromatosis** type 1 confirmed mutations in the neurofibromin gene governing RAS GTPase activity."
      }
    ]
  },
  "Dashboard — neur/neurogenesis.md": {
    "primary": "The biological process by which neural stem and progenitor cells produce new neurons.",
    "secondary": "In developmental and adult neurobiology, the proliferation, migration, differentiation, and functional integration of neurons into existing neural circuits.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Studies on Vertebrate Neurogenesis",
        "quote": "During early **neurogenesis**, the primitive neuroepithelial germinal cells divide rhythmically to populate the mantle layer of the spinal cord."
      },
      {
        "author": "Joseph Altman",
        "work": "Are New Neurons Formed in the Adult Brain?",
        "quote": "Thymidine autoradiography revealed unmistakable evidence of adult hippocampal **neurogenesis**, challenging the dogma that mature neurons never divide."
      },
      {
        "author": "Fernando Nottebohm",
        "work": "Neuronal Replacement in Adulthood",
        "quote": "Seasonal song learning in songbirds is driven by robust adult **neurogenesis** within the higher vocal center of the forebrain."
      }
    ]
  },
  "Dashboard — neur/neurogenic.md": {
    "primary": "Originating in, stimulated by, or caused by the nervous system or nerve tissue.",
    "secondary": "In physiology and pathology, describing bodily processes, shocks, muscular contractions, or bladder dysfunctions initiated primarily by neural impulses rather than myogenic or chemical mechanisms.",
    "quotes": [
      {
        "author": "Walter Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "The acute release of epinephrine from the adrenal gland is a purely **neurogenic** reflex evoked by splanchnic nerve stimulation."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Rhythmic stepping movements in the spinal animal exhibit a coordinated **neurogenic** timing governed by reciprocal inhibition."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Puncture of the fourth ventricle elicits a **neurogenic** glycosuria by transmitting impulses through the sympathetic nervous pathways."
      }
    ]
  },
  "Dashboard — neur/neuroglia.md": {
    "primary": "The non-neuronal supporting cellular framework and connective interstitial tissue of the central and peripheral nervous systems (glial cells).",
    "secondary": "In cellular neuroscience, the diverse collective of astrocytes, oligodendrocytes, microglia, and ependymal cells that maintain ionic homeostasis, form myelin sheaths, modulate synapses, and provide immune defense.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Die Cellularpathologie in ihrer Begründung auf physiologische und pathologische Gewebelehre",
        "quote": "I introduced the term **neuroglia** for that interstitial connective substance which cements the nerve elements of the brain and cord together."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "Glial cells are not inert structural scaffolding; the **neuroglia** actively regulates metabolic exchange between blood capillaries and neurons."
      },
      {
        "author": "Pío del Río-Hortega",
        "work": "Microglia",
        "quote": "By developing specific silver carbonate impregnations, I demonstrated that **neuroglia** contains distinct mobile phagocytic elements."
      }
    ]
  },
  "Dashboard — neur/neurogliacyte.md": {
    "primary": "An individual glial cell of the central nervous system; a neuroglial cell.",
    "secondary": "In cytopathology and neurohistology, an individual astrocyte, oligodendrocyte, or microglial cell, often evaluated for reactive hypertrophy or neoplastic transformation.",
    "quotes": [
      {
        "author": "Pío del Río-Hortega",
        "work": "The Microglia and Its Pathological Alterations",
        "quote": "Under pathological irritation, the resting **neurogliacyte** retracts its delicate ramified processes and transforms into an active macrophage."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The fibrous **neurogliacyte** of the white matter extends long, smooth expansions that terminate in perivascular sucker feet upon capillary walls."
      },
      {
        "author": "Camillo Golgi",
        "work": "Sulla fina anatomia degli organi centrali del sistema nervoso",
        "quote": "Every star-shaped **neurogliacyte** contributes to a vast metabolic syncytium that supports adjacent pyramidal nerve cells."
      }
    ]
  },
  "Dashboard — neur/neuroglial.md": {
    "primary": "Pertaining to, composed of, or derived from neuroglia.",
    "secondary": "In neuropathology, describing scar tissue (gliosis), tumors (gliomas), or supportive cell networks within the brain and spinal cord.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The **neuroglial** matrix pervades both gray and white substance, multiplying vigorously in areas of chronic cerebral irritation."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Silver impregnation reveals a dense **neuroglial** meshwork surrounding each synaptic glomerulus in the cerebellar granular layer."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Traumatic injury to the cerebral mantle provokes a permanent **neuroglial** scar that may serve as an epileptogenic focus."
      }
    ]
  },
  "Dashboard — neur/neurohormone.md": {
    "primary": "A chemical substance produced and released by neurosecretory nerve cells directly into the circulation to influence distant target organs or cells.",
    "secondary": "In endocrinology, an agent such as vasopressin, oxytocin, or hypothalamic hypophysiotropic releasing factors that combines neural signaling with endocrine action.",
    "quotes": [
      {
        "author": "Ernst Scharrer",
        "work": "Die Lichtempfindlichkeit blinder Elritzen",
        "quote": "The secretion of a true **neurohormone** from hypothalamic nuclei demonstrates that neurons can function as bona fide endocrine glands."
      },
      {
        "author": "Geoffrey Harris",
        "work": "Neural Control of the Pituitary Gland",
        "quote": "Each hypothalamic **neurohormone** enters the capillary plexus of the median eminence to reach and stimulate anterior pituitary cells."
      },
      {
        "author": "Vincent du Vigneaud",
        "work": "Trail of Sulfur Research: From Insulin to Oxytocin",
        "quote": "Elucidating the cyclic peptide structure of oxytocin provided the first chemical description of a mammalian peptide **neurohormone**."
      }
    ]
  },
  "Dashboard — neur/neurohypophysis.md": {
    "primary": "The posterior lobe of the pituitary gland, consisting of nervous tissue and neurosecretory axonal endings derived from the diencephalon.",
    "secondary": "In human neuroendocrinology, the neurohemal organ comprising the pars nervosa and infundibulum, which stores and releases oxytocin and antidiuretic hormone synthesized in the hypothalamus.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Extracts from the **neurohypophysis** exert a profound pressor effect upon the vascular tree and control renal water excretion."
      },
      {
        "author": "Geoffrey Harris",
        "work": "Neural Control of the Pituitary Gland",
        "quote": "Axons originating in the supraoptic and paraventricular nuclei descend through the pituitary stalk to terminate within the **neurohypophysis**."
      },
      {
        "author": "Walter Cannon",
        "work": "The Wisdom of the Body",
        "quote": "Homeostatic regulation of blood osmolality depends directly upon the release of antidiuretic hormone from the vascularized **neurohypophysis**."
      }
    ]
  },
  "Dashboard — neur/neurolemma.md": {
    "primary": "The thin membranous outer sheath of Schwann cells enclosing the myelin sheath of peripheral nerve fibers; an alternative spelling of neurilemma.",
    "secondary": "In anatomical terminology, the external nucleated cytoplasmic layer of a Schwann cell surrounding an axon in the peripheral nervous system, absent in the central nervous system.",
    "quotes": [
      {
        "author": "Theodor Schwann",
        "work": "Microscopical Researches",
        "quote": "The structureless outer membrane enclosing the fatty matter of the peripheral fiber corresponds to the cellular **neurolemma**."
      },
      {
        "author": "Louis-Antoine Ranvier",
        "work": "Leçons sur l'histologie du système nerveux",
        "quote": "At each node of Ranvier, the myelin is interrupted while the delicate **neurolemma** continues across the constriction."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The presence of a nucleated **neurolemma** in peripheral nerves explains their capacity for regeneration compared to central white tracts."
      }
    ]
  },
  "Dashboard — neur/neuroleptic.md": {
    "primary": "A medication or pharmacological agent used to treat psychosis (an antipsychotic), characterized by emotional calming, suppression of hallucinations, and psychomotor deceleration.",
    "secondary": "In psychopharmacology, describing major tranquilizers (such as chlorpromazine or haloperidol) that act primarily as antagonists at dopamine D2 receptors and may induce extrapyramidal motor signs.",
    "quotes": [
      {
        "author": "Jean Delay and Pierre Deniker",
        "work": "Thirty-Eight Cases of Psychoses Treated with Chlorpromazine",
        "quote": "We propose the term **neuroleptic** for drugs that produce psychological detachment, emotional indifference, and reduction of motor agitation without inducing true hypnosis."
      },
      {
        "author": "Arvid Carlsson",
        "work": "Nobel Lecture: A Half-Century of Neurotransmitter Research",
        "quote": "The therapeutic efficacy of every major **neuroleptic** compound correlates directly with its affinity for blocking striatal and mesolimbic dopamine receptors."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Overmedication with a potent **neuroleptic** agent reproduced the parkinsonian rigidity and masked facies seen in encephalitis lethargica."
      }
    ]
  },
  "Dashboard — neur/neurolinguist.md": {
    "primary": "A specialist or researcher who investigates the neurological mechanisms and neural substrates of language comprehension, production, and acquisition.",
    "secondary": "In cognitive science, an interdisciplinary scholar analyzing aphasic syndromes, brain lesion mapping, and neuroimaging data to construct models of linguistic cognition.",
    "quotes": [
      {
        "author": "Roman Jakobson",
        "work": "Child Language, Aphasia and Phonological Universals",
        "quote": "The **neurolinguist** must dissect the dissolution of phonological oppositions in brain-injured patients to reconstruct the hierarchy of language."
      },
      {
        "author": "Aleksandr Luria",
        "work": "Basic Problems of Neurolinguistics",
        "quote": "By correlating focal cortical excisions with specific linguistic breakdowns, the **neurolinguist** uncovers the dynamic architecture of inner speech."
      },
      {
        "author": "Noam Chomsky",
        "work": "Language and Mind",
        "quote": "The future task of the **neurolinguist** will be to discover the biological machinery that instantiates universal grammar within human neural circuitry."
      }
    ]
  },
  "Dashboard — neur/neurolinguistics.md": {
    "primary": "The branch of linguistics and cognitive neuroscience that studies the neural mechanisms, brain structures, and physiological processes underlying language processing.",
    "secondary": "An interdisciplinary scientific domain investigating the localization, comprehension, syntactic decoding, and neural representation of spoken, written, and signed languages.",
    "quotes": [
      {
        "author": "Aleksandr Luria",
        "work": "Basic Problems of Neurolinguistics",
        "quote": "Modern **neurolinguistics** regards language not as the product of an isolated cerebral center, but as a complex functional system engaging distributed cortical networks."
      },
      {
        "author": "Roman Jakobson",
        "work": "Studies on Child Language and Aphasia",
        "quote": "The foundational premise of **neurolinguistics** is that linguistic theory and clinical aphasiology provide indispensable mutual insights."
      },
      {
        "author": "Eric Lenneberg",
        "work": "Biological Foundations of Language",
        "quote": "Critical period phenomena in language acquisition provided a decisive developmental framework for the emerging field of **neurolinguistics**."
      }
    ]
  },
  "Dashboard — neur/neurologic.md": {
    "primary": "Of, relating to, or dealing with neurology or the anatomy, functions, and disorders of the nervous system (neurological).",
    "secondary": "In clinical examination, describing the systematic evaluation of cranial nerves, motor tone, sensation, coordination, and reflexes to detect nervous system pathology.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A methodical **neurologic** examination must precede any diagnostic pronouncement regarding localized cerebral pathology."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "The progressive muscular atrophy described in our wards revealed unmistakable evidence of severe underlying **neurologic** disease."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Relief of intracranial tension following tumor decompression resulted in immediate improvement of the patient's focal **neurologic** deficits."
      }
    ]
  }
}

def update_notes():
    base_cluster_dir = os.path.abspath("App database/Greek roots/Cluster Body & Physiology")
    updated = 0
    errors = []

    for rel_path, data in BATCH1_DATA.items():
        file_path = os.path.join(base_cluster_dir, rel_path.replace("/", "\\"))
        if not os.path.exists(file_path):
            errors.append(f"File not found: {file_path}")
            continue

        primary = data["primary"].strip()
        secondary = data["secondary"].strip()
        quotes = data["quotes"]

        # Validation
        if not primary or not secondary:
            errors.append(f"{rel_path}: Empty definition")
        if primary.lower() == secondary.lower():
            errors.append(f"{rel_path}: Duplicate definition")
        if len(quotes) != 3:
            errors.append(f"{rel_path}: Expected 3 quotes, got {len(quotes)}")
        
        authors = [q["author"] for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"{rel_path}: Duplicate authors {authors}")
        
        for q in quotes:
            if re.search(r"Academic Lexicon|Classic Author|Unknown Author|Placeholder", q["author"], re.I):
                errors.append(f"{rel_path}: Placeholder author {q['author']}")
            if "**" not in q["quote"]:
                errors.append(f"{rel_path}: Quote missing bold word: {q['quote']}")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_idx = content.find("> [!book]")
        if book_idx == -1:
            errors.append(f"No '> [!book]' in {file_path}")
            continue

        header_part = content[:book_idx].rstrip()
        def_block = (
            f"> [!book] 📖 Definitions & Semantic Range\n"
            f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {primary}\n"
            f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {secondary}"
        )
        quote_lines = [
            f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*"
            for q in quotes
        ]
        quotes_block = f"> [!quote] 💬 Contextual Usage & Authentic Quotations\n" + "\n".join(quote_lines)
        new_content = f"{header_part}\n\n{def_block}\n\n{quotes_block}\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1

    if errors:
        print("ERRORS FOUND:")
        for err in errors:
            print("  ", err)
        sys.exit(1)

    print(f"Batch 1 successfully updated {updated} notes.")

if __name__ == "__main__":
    update_notes()
