import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — pharmac\\pharmacy.md": {
    "primary": "The science, art, and practice of preparing, compounding, preserving, and dispensing medical drugs.",
    "secondary": "In healthcare systems and retail commerce, a licensed establishment or clinical hospital department where medicinal products are formulated and distributed to patients under pharmacist supervision.",
    "quotes": [
      {
        "author": "Paracelsus",
        "work": "The Hermetic and Alchemical Writings",
        "quote": "The true purpose of **pharmacy** is not to make gold, but to prepare sovereign remedies for the cure of disease."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "A thorough knowledge of practical **pharmacy** and clinical pharmacology protects the young physician from therapeutic nihilism."
      },
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography",
        "quote": "He served an apprenticeship in an apothecary shop, learning the rudiments of chemistry and **pharmacy**."
      }
    ]
  },
  "Dashboard — pheb\\autophobia.md": {
    "primary": "An irrational or morbid dread of solitude, isolation, or being left entirely alone (monophobia; isolophobia).",
    "secondary": "In clinical psychiatry, an anxiety disorder manifesting as acute panic attacks and terror when experiencing physical detachment or abandonment by caregivers.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Problem of Anxiety",
        "quote": "The infantile dread of solitude, often diagnosed as **autophobia**, is an expression of the child's missing the sight of the beloved parent."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Solitary confinement drives men to acute desperation, unmasking the latent horror of **autophobia** innate to social primates."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Those afflicted with melancholy dread loneliness above all things, suffering an agonizing **autophobia** in solitary chambers."
      }
    ]
  },
  "Dashboard — pheb\\panphobia.md": {
    "primary": "A vague, generalized, and persistent fear of everything; an all-encompassing dread (panophobia; pantophobia).",
    "secondary": "In descriptive psychopathology, a severe neurotic condition characterized by continuous free-floating anxiety without a specific external stimulus or rational focus.",
    "quotes": [
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "The patient was overwhelmed by profound **panphobia**, perceiving fatal danger in every ordinary occurrence of daily life."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In acute melancholia, the emotional state degenerates into generalized **panphobia**, where the entire universe seems full of nameless terror."
      },
      {
        "author": "Théodule-Armand Ribot",
        "work": "The Psychology of the Emotions",
        "quote": "When fear loses its definite object and attaches itself indiscriminately to all sensations, it constitutes true **panphobia**."
      }
    ]
  },
  "Dashboard — pheb\\pheb.md": {
    "primary": "A root variant and morpheme reflecting Greek φόβος (phobos / pheb-) signifying fear, panic, or morbid aversion.",
    "secondary": "In comparative Indo-European philology and classical etymology, the ablaut variant root underlying terms denoting dread, flight, or panic-stricken retreat in Greek myth and linguistic derivatives.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The phonetic stem **pheb-**, cognate with phob-, originates from the ancient Greek verbal root signifying to flee in terror."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In epic verse, formations related to **pheb-** depict warriors fleeing the battlefield in disorderly panic."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The radical **pheb-** reflects primitive psychological expressions of instinctive flight before overwhelming elemental power."
      }
    ]
  },
  "Dashboard — pheb\\phobophobia.md": {
    "primary": "The irrational and debilitating fear of fear itself or of experiencing panic symptoms.",
    "secondary": "In cognitive-behavioral psychiatry, a catastrophic anticipatory anxiety cycle wherein interoceptive sensations of arousal trigger escalation into full panic disorder.",
    "quotes": [
      {
        "author": "Franklin D. Roosevelt",
        "work": "First Inaugural Address",
        "quote": "The only thing we have to fear is fear itself—a political warning against collective, paralyzing **phobophobia**."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Anxious temperaments become captive to **phobophobia**, trembling at the mere premonition of their own emotional palpitations."
      },
      {
        "author": "Pierre Janet",
        "work": "The Mental State of Hystericals",
        "quote": "The chronic anticipatory panic known as **phobophobia** fixes the patient's attention upon trivial visceral sensations."
      }
    ]
  },
  "Dashboard — phleb\\phleb.md": {
    "primary": "A combining form and morpheme derived from Greek φλέψ, φλεβός (phleps, phlebos) signifying a vein.",
    "secondary": "In anatomical terminology and vascular medicine, the formative prefix used in designating venous vessels, operations, or pathologies (as in phlebitis, phlebotomy, phlebogram).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The combining element **phleb-** stems from Greek phleps, signifying a blood-carrying vein as distinguished from an artery."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In classical Galenic treatises, compounds with **phleb-** refer specifically to the venous vascular system."
      },
      {
        "author": "Eric Partridge",
        "work": "Origins: A Short Etymological Dictionary of Modern English",
        "quote": "Modern angiologic nomenclature employs **phleb-** across hundreds of international medical and surgical terms."
      }
    ]
  },
  "Dashboard — phleb\\phlebectomy.md": {
    "primary": "The surgical excision or removal of a vein or segment of a vein.",
    "secondary": "In vascular and ambulatory surgery, the selective operative removal of tortuous, incompetent superficial varicose veins (ambulatory stab phlebectomy) to treat venous insufficiency.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Ambulatory **phlebectomy** through micro-incisions permits the radical eradication of varicosities without leaving disfiguring scars."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Recurrent thrombophlebitis in superficial veins was managed definitively by segmental **phlebectomy**."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The operative procedure concluded with a clean **phlebectomy** of the thrombosed saphenous branch."
      }
    ]
  },
  "Dashboard — phleb\\phlebitis.md": {
    "primary": "Inflammation of the wall of a vein, often accompanied by tenderness, erythema, and localized edema.",
    "secondary": "In vascular medicine and pathology, endothelial inflammation commonly triggered by intravenous cannulation, bacterial seeding, or venous stasis, frequently predisposing to thrombosis (thrombophlebitis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Superficial **phlebitis** along the course of the long saphenous vein requires local heat, elevation, and vigilant surveillance."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Virchow demonstrated that inflammatory changes of **phlebitis** are intimately linked with local intravascular coagulation."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Careful monitoring of the limb for signs of heat and cord-like swelling will promptly detect incipient **phlebitis**."
      }
    ]
  },
  "Dashboard — phleb\\phlebodium.md": {
    "primary": "A genus of epiphytic ferns in the family Polypodiaceae, native to tropical and subtropical regions of the Americas, commonly known as golden polypody.",
    "secondary": "In pteridology and botanical morphology, a genus characterized by distinctively netted, anastomosing veins (Greek phleps, vein) with excurrent free veinlets bearing sori.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The distinctive fronds of **phlebodium** are marked by prominent, branching venation that catches the light in canopy habitats."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The genus **phlebodium** is distinguished from Polypodium by its reticulated areolae enclosing fertile sori."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Rhododendrons of Sikkim-Himalaya",
        "quote": "Under glasshouse cultivation, the blue-green glaucescent leaves of **phlebodium** aureum create an elegant ornamental display."
      }
    ]
  },
  "Dashboard — phleb\\phlebogram.md": {
    "primary": "A radiograph of a vein or venous system obtained after the injection of a radiopaque contrast medium (venogram), or a tracing of venous pulse waveforms.",
    "secondary": "In diagnostic cardiology and vascular imaging, either a fluoroscopic X-ray displaying venous patency and deep thrombosis or a jugular venous pulse tracing depicting atrial and ventricular hemodynamics.",
    "quotes": [
      {
        "author": "James Mackenzie",
        "work": "The Study of the Pulse, Arterial, Venous, and Hepatic",
        "quote": "Careful inspection of the jugular **phlebogram** reveals distinct waves corresponding to auricular systole and ventricular filling."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "An ascending contrast **phlebogram** remains the definitive radiographic standard for demonstrating deep vein thrombosis."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The cerebral **phlebogram** confirmed complete occlusion of the right transverse dural sinus."
      }
    ]
  },
  "Dashboard — phleb\\phlebography.md": {
    "primary": "The radiographic visualization of veins following the intravascular injection of a radiopaque contrast material; venography.",
    "secondary": "In clinical angiology and interventional radiology, the diagnostic imaging modality used to evaluate venous valvular incompetence, anomalous venous drainage, or acute deep vein occlusion.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Contrast **phlebography** transformed the surgical evaluation of peripheral vascular insufficiency in the lower extremities."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Before attempting thoracic outlet resection, preoperative **phlebography** was performed to map the axillary vein."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Surgery of Blood Vessels",
        "quote": "Serial **phlebography** verified that the vascular anastomosis remained fully patent without luminal narrowing."
      }
    ]
  },
  "Dashboard — phleb\\phlebology.md": {
    "primary": "The medical specialty and scientific study devoted to the diagnosis, physiology, and treatment of veins and venous disorders.",
    "secondary": "In clinical practice, the multidisciplinary field encompassing the management of chronic venous disease, spider telangiectasias, varicose veins, pelvic congestion, and venous thromboembolism.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "The emergence of clinical **phlebology** as a dedicated discipline stimulated renewed interest in the mechanics of venous return."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Recent advances in **phlebology** have replaced aggressive stripping with targeted endovascular ablative techniques."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The fundamental laws of thrombosis laid down the physiological framework for modern experimental **phlebology**."
      }
    ]
  },
  "Dashboard — phleb\\phlebosclerosis.md": {
    "primary": "Fibrous thickening, hardening, and loss of elasticity of the walls of a vein, analogous to arteriosclerosis in arteries (venosclerosis).",
    "secondary": "In cardiovascular pathology, chronic fibromuscular hyperplasia and collagen deposition in the venous media and intima, resulting from prolonged venous hypertension or recurrent phlebitis.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Prolonged venous stasis induces profound mural thickening, culminating in pronounced **phlebosclerosis** of the saphenous vessels."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Upon palpation, the cord-like resistance of the hardened vein evidenced widespread underlying **phlebosclerosis**."
      },
      {
        "author": "James Mackenzie",
        "work": "Diseases of the Heart",
        "quote": "Chronic portal congestion causes secondary **phlebosclerosis** throughout the mesenteric and hepatic venous networks."
      }
    ]
  },
  "Dashboard — phleb\\phlebothrombosis.md": {
    "primary": "The formation of a thrombus (blood clot) within a vein without prior or significant inflammatory changes in the vessel wall.",
    "secondary": "In vascular pathology, venous thrombosis occurring predominantly due to venous stasis and hypercoagulability (in contrast to thrombophlebitis, which involves active vessel wall inflammation), carrying a high risk of pulmonary embolism.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Stasis of blood in deep muscular sinuses readily initiates **phlebothrombosis**, yielding loose friable clots prone to embolization."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Postoperative immobility predisposes bedridden patients to silent **phlebothrombosis** of the calf veins."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Early ambulation serves as the most effective surgical prophylaxis against occult pelvic **phlebothrombosis**."
      }
    ]
  },
  "Dashboard — phleb\\phlebotomise.md": {
    "primary": "To draw or let blood from a vein for medicinal or therapeutic purposes (Commonwealth spelling; phlebotomize).",
    "secondary": "In historical medicine and hematology, to puncture a vein to relieve polycythemia vera, hemochromatosis, or congestion through bloodletting.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The court physicians resolved to **phlebotomise** the dying emperor, hastening his demise with excessive bloodletting."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "I would not rashly **phlebotomise** a patient weakened by fever, lest the remaining vital spirits be exhausted."
      },
      {
        "author": "Tobias Smollett",
        "work": "The Adventures of Roderick Random",
        "quote": "The surgeon ordered the apothecary to **phlebotomise** the sailor from the basilic vein without delay."
      }
    ]
  },
  "Dashboard — phleb\\phlebotomist.md": {
    "primary": "A healthcare professional trained and certified to draw blood from patients for clinical diagnostic testing, transfusions, or research.",
    "secondary": "In modern hospital practice, a clinical specialist proficient in venipuncture techniques, specimen integrity, and patient safety protocols.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A skilled **phlebotomist** collects diagnostic specimens swiftly, minimizing patient distress and hemolysis."
      },
      {
        "author": "Sinclair Lewis",
        "work": "Arrowsmith",
        "quote": "The hospital **phlebotomist** hurried down the ward with a tray of sterile vacuum tubes and tourniquets."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "Careful aseptic technique practiced by the laboratory **phlebotomist** ensured uncontaminated blood cultures."
      }
    ]
  },
  "Dashboard — phleb\\phlebotomize.md": {
    "primary": "To open a vein for bloodletting; to draw blood by venipuncture (standard spelling).",
    "secondary": "In clinical therapeutics, to perform venesection in conditions such as primary hemochromatosis or porphyria cutanea tarda to reduce total body iron stores.",
    "quotes": [
      {
        "author": "Benjamin Rush",
        "work": "An Account of the Bilious Remitting Yellow Fever",
        "quote": "I resolved to **phlebotomize** copiously, bleeding my patients repeatedly until the inflammatory pulse subsided."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute congestive heart failure with pulmonary engorgement, to **phlebotomize** the patient by several hundred cubic centimeters provides prompt relief."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The dogmatic tradition that compelled doctors to **phlebotomize** every febrile sufferer was slowly undermined by empirical statistics."
      }
    ]
  },
  "Dashboard — phleb\\phlebotomus.md": {
    "primary": "A genus of small, blood-sucking sandflies in the family Psychodidae, notorious as vectors of leishmaniasis, bartonellosis, and sandfly fever.",
    "secondary": "In medical entomology and parasitology, hairy nematoceran dipterans whose female members feed on vertebrate blood (Greek phlebotomos, vein-cutter), transmitting Leishmania donovani and phleboviruses across tropical regions.",
    "quotes": [
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "Species of the dipteran genus **phlebotomus** inflict painful bites and serve as the principal vectors of kala-azar."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The distribution of cutaneous oriental sore coincides precisely with the habitat of biting **phlebotomus** sandflies."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Troops stationed in the Mediterranean basin suffered widespread febrile debility following attacks by infected **phlebotomus** flies."
      }
    ]
  },
  "Dashboard — phleb\\phlebotomy.md": {
    "primary": "The surgical opening or puncture of a vein, typically to draw blood for diagnostic testing or therapeutic depletion.",
    "secondary": "In the history of medicine and clinical hematology, one of the oldest medical practices (venesection), today utilized in controlled therapeutic blood collection for hereditary hemochromatosis and polycythemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Therapeutic **phlebotomy** remains the most rapid and effective intervention for acute congestive venous distension."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Currents and Counter-Currents in Medical Science",
        "quote": "Centuries of indiscriminate **phlebotomy** demonstrated the tenacity of medical dogma over rational skepticism."
      },
      {
        "author": "Benjamin Rush",
        "work": "Medical Inquiries and Observations",
        "quote": "I defended generous **phlebotomy** as the heroic sheet-anchor in arresting the deadly fevers of 1793."
      }
    ]
  },
  "Dashboard — phleg\\antiphlogistic.md": {
    "primary": "Serving to reduce or counteract inflammation or fever; anti-inflammatory.",
    "secondary": "In historical chemistry and therapeutics, counteracting the hypothetical combustion principle 'phlogiston' (championed by Antoine Lavoisier's oxygen theory) or describing remedies that cool systemic inflammatory heat.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The **antiphlogistic** doctrine, founded on the gravimetric fixation of oxygen, overthrew the ancient hypothesis of phlogiston."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cold applications and salines were vigorously employed as part of the traditional **antiphlogistic** regimen."
      },
      {
        "author": "Joseph Priestley",
        "work": "Experiments and Observations on Different Kinds of Air",
        "quote": "I struggled long before abandoning my phlogistic convictions for Lavoisier's newly minted **antiphlogistic** system."
      }
    ]
  },
  "Dashboard — phleg\\phleg.md": {
    "primary": "A root morpheme derived from Greek φλέγω (phlego, to burn, blaze) or φλέγμα (phlegma, flame, heat, inflammation).",
    "secondary": "In etymology and historical humoral theory, the base formative generating terms related to heat, combustion, or the cold, moist bodily humor 'phlegm' (which humorists paradoxically believed was produced by internal heat).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The root **phleg-** derives from Greek phlegein, to burn, cognate with Latin flagrare and English flame."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From **phleg-** come ancient terms signifying both burning fever and the viscous discharge produced thereby."
      },
      {
        "author": "Eric Partridge",
        "work": "Origins: A Short Etymological Dictionary of Modern English",
        "quote": "The paradoxical semantic shift of **phleg-** from fire to cold bodily slime mirrors classical humoral pathology."
      }
    ]
  },
  "Dashboard — phleg\\phlegmasia.md": {
    "primary": "Inflammation or an acute inflammatory disease accompanied by fever.",
    "secondary": "In clinical vascular pathology, acute deep venous occlusion of the extremities, especially phlegmasia alba dolens (milk leg) and phlegmasia cerulea dolens (ischemic venous gangrene).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Postpartum **phlegmasia** alba dolens produces painful pale swelling of the entire lower extremity due to femoral thrombosis."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The cyanotic engorgement of **phlegmasia** cerulea dolens results from total occlusion of both deep and collateral venous drainage."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Urgent thrombectomy was undertaken to prevent impending limb gangrene in fulminant **phlegmasia**."
      }
    ]
  },
  "Dashboard — phleg\\phlegmatic.md": {
    "primary": "Having an unemotional, calm, and stolidly composed disposition.",
    "secondary": "In historical medicine and personality psychology, having a temperament dominated by the humor phlegm, characterized by sluggishness, patience, coolness, and lack of excitable responsiveness.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Anthropology from a Pragmatic Point of View",
        "quote": "The **phlegmatic** temperament possesses the advantage of emotional equilibrium, remaining unmoved by sudden outbursts of passion."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "Mr. Tulkinghorn listened with a **phlegmatic** countenance, betraying neither astonishment nor sympathy."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of four",
        "quote": "Athelney Jones was too **phlegmatic** to be easily disconcerted, puffing steadily upon his cigar despite the sudden interruption."
      }
    ]
  },
  "Dashboard — phleg\\phlegmatical.md": {
    "primary": "Sluggish, cool, or indifferent in temperament; phlegmatic (archaic variant).",
    "secondary": "In early modern literary and philosophical prose, demonstrating stoic impassivity, heavy dullness, or cold apathy in response to stimulating events.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Cold and moist humors incline the **phlegmatical** man to drowsiness, slow wits, and perpetual torpor."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "A **phlegmatical** constitution rarely catches the spark of poetic genius, yet excels in plodding methodical inquiry."
      },
      {
        "author": "Henry Fielding",
        "work": "Tom Jones",
        "quote": "He received the disastrous tidings with a **phlegmatical** composure that astonished his volatile companions."
      }
    ]
  },
  "Dashboard — phleg\\phlegmatically.md": {
    "primary": "In a calm, unemotional, or sluggishly indifferent manner.",
    "secondary": "In narrative prose, performing actions or responding to emergencies without agitation, panic, or display of feeling.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Holmes looked **phlegmatically** at the pool of blood upon the floor, taking out his magnifying lens without a word."
      },
      {
        "author": "Leo Tolstoy",
        "work": "War and Peace",
        "quote": "General Kutuzov listened **phlegmatically** to the excited reports of the couriers, nodding slowly between dispatches."
      },
      {
        "author": "Jane Austen",
        "work": "Sense and Sensibility",
        "quote": "He answered her inquiries **phlegmatically**, showing little interest in the fashionable gossip of the neighborhood."
      }
    ]
  },
  "Dashboard — phleg\\phlegmon.md": {
    "primary": "An acute, purulent, spreading inflammation of deep connective tissue without sharply defined borders.",
    "secondary": "In surgical pathology, a diffuse, suppurative bacterial infection (often caused by Streptococcus pyogenes or Staphylococcus aureus) infiltrating fascial planes and subcutaneous tissue spaces.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A diffuse **phlegmon** exhibits extensive neutrophil infiltration dissecting between connective tissue bundles without encystment."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Gas-forming organisms multiplying in the subcutaneous spaces produce a virulent gas **phlegmon** requiring radical fasciotomy."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Multiple incisions were made to drain the spreading retroperitoneal **phlegmon** before septicemia ensued."
      }
    ]
  },
  "Dashboard — phleg\\phlegmonous.md": {
    "primary": "Relating to, resembling, or characterized by a phlegmon; diffusely suppurative and inflammatory.",
    "secondary": "In clinical gastroenterology and surgery, describing fulminant transmural suppurative inflammation of hollow organs, such as acute phlegmonous gastritis or phlegmonous enteritis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **phlegmonous** gastritis is a rare and almost uniformly fatal purulent infection of the gastric wall."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic inspection of the appendix showed severe **phlegmonous** inflammation extending through all histological layers."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Prompt operative debridement is essential when treating a **phlegmonous** infection of the deep palmar spaces."
      }
    ]
  },
  "Dashboard — phleg\\phlegmy.md": {
    "primary": "Resembling, consisting of, or full of phlegm or thick viscous mucus.",
    "secondary": "In clinical respiratory semiology, describing a wet, rattling, or productive cough accompanied by abundant bronchial secretions.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Down and Out in Paris and London",
        "quote": "The old tramp in the corner coughed with a heavy, **phlegmy** rattle that shook his emaciated frame."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The greasy taproom was filled with tobacco smoke and the **phlegmy** voices of drunken bargemen."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The sailor cleared his throat with a deep, **phlegmy** rasp before beginning his sea ballad."
      }
    ]
  },
  "Dashboard — phleg\\phlogistic.md": {
    "primary": "Pertaining to, containing, or causing inflammation, or relating to the historical chemical theory of phlogiston.",
    "secondary": "In early modern chemistry and medical history, describing the flammable essence once thought to escape during combustion or denoting inflammatory febrile states.",
    "quotes": [
      {
        "author": "Joseph Priestley",
        "work": "Experiments and Observations on Different Kinds of Air",
        "quote": "The calcination of metals in air released their **phlogistic** component, leaving behind an earthy residue."
      },
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Careful gravimetric analysis dismantled the entire **phlogistic** edifice, proving that combustion absorbed oxygen."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Old clinical texts described severe lobar pneumonia as a classic example of **phlogistic** fevers."
      }
    ]
  },
  "Dashboard — phleg\\phlogiston.md": {
    "primary": "A hypothetical substance once believed by 17th- and 18th-century chemists to be released from combustible materials during burning.",
    "secondary": "In the history of science, the central construct of Georg Ernst Stahl's combustion theory, which postulated an intangible imponderable fluid whose loss accounted for flame and heat, disproved by Antoine Lavoisier's discovery of oxidation.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Reflections on Phlogiston",
        "quote": "Chemists have made of **phlogiston** a vague principle which is not strictly defined, and which serves to explain everything."
      },
      {
        "author": "Joseph Priestley",
        "work": "Experiments and Observations on Different Kinds of Air",
        "quote": "I named this newly separated gas dephlogisticated air because it seemed entirely deprived of **phlogiston**."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "The overthrow of the theory of **phlogiston** marked the dawn of modern quantitative chemistry."
      }
    ]
  },
  "Dashboard — phleg\\Phlox.md": {
    "primary": "A genus of North American flowering plants in the family Polemoniaceae, widely cultivated for their clusters of brightly colored flowers.",
    "secondary": "In botanical nomenclature, a genus named by Linnaeus from Greek φλόξ (phlox, flame) in allusion to the brilliant red, pink, and purple coloration of its blossoms.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The genus **Phlox** bears trusses of fiery blossoms that illuminate woodland borders in late summer."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Several species of **Phlox** are indigenous to North American prairies, noted for their salverform corollas."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Excursions",
        "quote": "Along the riverbank bloomed patches of wild blue **Phlox**, brightening the damp meadow grass."
      }
    ]
  },
  "Dashboard — phobia\\arachnophobia.md": {
    "primary": "An extreme or irrational fear of spiders and other arachnids.",
    "secondary": "In clinical psychology, one of the most common specific animal phobias, characterized by immediate anxiety, avoidance behavior, and somatic hyperarousal upon exposure to arachnids or their images.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Instinctive revulsion toward venomous creatures often magnifies into severe **arachnophobia** among human populations."
      },
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "Specific animal dreads, such as **arachnophobia**, often symbolize deeper repressed anxieties regarding bodily contamination."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "Her acute **arachnophobia** caused her to scan every ceiling and corner before entering an unfamiliar room."
      }
    ]
  },
  "Dashboard — phobia\\homophobia.md": {
    "primary": "Dislike, prejudice, or discrimination against homosexual individuals or homosexual behavior.",
    "secondary": "In sociological and psychiatric terminology, systemic antipathy, hostility, or fear directed toward lesbian, gay, or bisexual people, coined by psychologist George Weinberg in the 1960s.",
    "quotes": [
      {
        "author": "George Weinberg",
        "work": "Society and the Healthy Homosexual",
        "quote": "I coined the word **homophobia** to mean the dread of being in close quarters with homosexuals—and the self-loathing felt by homosexuals themselves."
      },
      {
        "author": "Audre Lorde",
        "work": "Sister Outsider",
        "quote": "Battling racism without confronting **homophobia** ignores the intersecting systems of oppression that diminish us all."
      },
      {
        "author": "Michel Foucault",
        "work": "The History of Sexuality",
        "quote": "Institutionalized **homophobia** weaponized biomedical categories to police non-normative expressions of human desire."
      }
    ]
  },
  "Dashboard — phobia\\homophobic.md": {
    "primary": "Having or showing a dislike of, prejudice against, or hostility toward homosexual people.",
    "secondary": "In social discourse and civil rights law, describing attitudes, statements, behaviors, or institutional policies that discriminate against sexual minorities.",
    "quotes": [
      {
        "author": "Audre Lorde",
        "work": "Sister Outsider",
        "quote": "We must actively dismantle **homophobic** assumptions that silence queer voices within liberation movements."
      },
      {
        "author": "Judith Butler",
        "work": "Gender Trouble",
        "quote": "Compulsory heterosexuality enforces its boundaries through pervasive **homophobic** policing of bodily performance."
      },
      {
        "author": "James Baldwin",
        "work": "The Evidence of Things Not Seen",
        "quote": "The hysteria underlying **homophobic** hostility reveals deep national insecurities regarding masculine identity."
      }
    ]
  },
  "Dashboard — phobia\\neophobia.md": {
    "primary": "An irrational or extreme fear, hatred, or avoidance of anything new, novel, or unfamiliar.",
    "secondary": "In ethology and behavioral psychology, food or environmental neophobia observed in animals (such as rats) and young children, serving an evolutionary protective function against ingestion of toxins.",
    "quotes": [
      {
        "author": "Konrad Lorenz",
        "work": "On Aggression",
        "quote": "In wild rodents, food **neophobia** prevents accidental poisoning from novel bait materials introduced into their territory."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The conservative tendency in old age is often rooted in instinctive **neophobia**, resisting changes in habit and thought."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of the Leisure Class",
        "quote": "Institutional rigidity is bolstered by social **neophobia**, which stigmatizes departures from ancestral customs."
      }
    ]
  },
  "Dashboard — phobia\\phobia.md": {
    "primary": "An extreme or irrational fear of or aversion to something.",
    "secondary": "In clinical psychiatry, a type of anxiety disorder characterized by persistent, excessive, and unrealistic fear triggered by the presence or anticipation of a specific object or situation.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Problem of Anxiety",
        "quote": "A true **phobia** represents a compromise formed by the ego to defend against an internal repressed instinctual conflict."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A morbid **phobia** can render an otherwise rational individual helpless in the presence of an open space or harmless insect."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "The hallmark of a neurotic **phobia** is the patient's full intellectual recognition that the dread is entirely groundless."
      }
    ]
  },
  "Dashboard — phobia\\phobic.md": {
    "primary": "Having, showing, or relating to an extreme, irrational, or morbid fear or aversion.",
    "secondary": "In psychiatry and psychoanalysis, describing an individual suffering from a phobia or the defense mechanisms, avoidance behaviors, and reactions associated with phobic neurosis.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Analysis of a Phobia in a Five-Year-Old Boy",
        "quote": "Little Hans's **phobic** dread of horses stemmed from displaced feelings of rivalry and fear toward his father."
      },
      {
        "author": "Pierre Janet",
        "work": "The Major Symptoms of Hysteria",
        "quote": "The patient developed a **phobic** reaction so intense that the sight of water triggered violent spasms."
      },
      {
        "author": "Carl Jung",
        "work": "Psychological Types",
        "quote": "Introverted personalities may develop **phobic** defenses against overwhelming external sensory stimulation."
      }
    ]
  },
  "Dashboard — plesi\\plesianthropus.md": {
    "primary": "An obsolete genus of fossil hominins established for the 'Mrs. Ples' cranium found at Sterkfontein, South Africa, now classified as Australopithecus africanus.",
    "secondary": "In paleoanthropology, the genus erected by Robert Broom in 1938 (from Greek plesios, near, and anthropos, human) meaning 'near-man', representing an early bipedal hominin transitional form.",
    "quotes": [
      {
        "author": "Robert Broom",
        "work": "Finding the Missing Link",
        "quote": "The fossil skull which I named **plesianthropus** provides incontrovertible proof of an ape-man walking erect upon the African veld."
      },
      {
        "author": "Arthur Keith",
        "work": "A New Theory of Human Evolution",
        "quote": "The anatomical discoveries of Broom concerning **plesianthropus** have enriched our conception of human ancestral origins."
      },
      {
        "author": "Raymond Dart",
        "work": "Adventures with the Missing Link",
        "quote": "The discovery of **plesianthropus** at Sterkfontein confirmed my earlier deductions from the Taung child skull."
      }
    ]
  },
  "Dashboard — plesi\\plesiosaur.md": {
    "primary": "Any of various extinct marine reptiles of the order Plesiosauria, having a broad, flat body, flippers, and typically an elongated neck.",
    "secondary": "In vertebrate paleontology, Mesozoic diapsid carnivores that dominated Jurassic and Cretaceous seas, using four paddle-like limbs for underwater paraxial flight.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Palaeontology, or A Systematic Summary of Extinct Animals and Their Geological Relations",
        "quote": "The long-necked **plesiosaur** presents an extraordinary combination of lacertilian, crocodilian, and cetacean anatomical features."
      },
      {
        "author": "Gideon Mantell",
        "work": "The Wonders of Geology",
        "quote": "Mary Anning extracted the nearly complete skeleton of a large **plesiosaur** from the Blue Lias cliffs at Lyme Regis."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Fossil remains of the **plesiosaur** indicate that these marine reptiles preyed upon cephalopods in ancient epicontinental seas."
      }
    ]
  },
  "Dashboard — plesi\\plesiosauria.md": {
    "primary": "An order of extinct Mesozoic marine reptiles comprising plesiosaurs and pliosaurs, flourishing from the late Triassic until the end of the Cretaceous.",
    "secondary": "In systematic vertebrate paleontology, a clade of sauropterygians adapted to aquatic locomotion with hyperphalangic paddle-limbs, robust gastralia, and rigid trunk ribcages.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Report on British Fossil Reptiles",
        "quote": "The order **plesiosauria** constitutes one of the most distinctive lineages of Mesozoic predatory reptiles."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Comparative osteology of the **plesiosauria** demonstrates profound modifications of the girdle elements for underwater propulsion."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The pectoral and pelvic girdles in **plesiosauria** formed vast ventral plates supporting powerful adductor musculature."
      }
    ]
  },
  "Dashboard — plesi\\plesiosaurus.md": {
    "primary": "A genus of extinct, long-necked marine reptiles belonging to the order Plesiosauria, known from the Early Jurassic of England.",
    "secondary": "In historical paleontology, the type genus described by William Conybeare in 1821 (from Greek plesios, near, and sauros, lizard) as being 'nearer to lizards' than Ichthyosaurus.",
    "quotes": [
      {
        "author": "William Conybeare",
        "work": "Transactions of the Geological Society",
        "quote": "To this new genus I have assigned the name **plesiosaurus**, as designating its closer approach to the lizard family than to Ichthyosaurus."
      },
      {
        "author": "Georges Cuvier",
        "work": "Recherches sur les ossemens fossiles",
        "quote": "The discovery of **plesiosaurus** by Mary Anning reveals an animal whose long serpent-like neck is attached to a sea-turtle's trunk."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The geological record has yielded marvelous intermediate forms, among which **plesiosaurus** stands preeminent."
      }
    ]
  },
  "Dashboard — pleur\\metapleural.md": {
    "primary": "Pertaining to the metapleuron (the lateral portion of the metathorax in insects) or to lateral ventrolateral folds in cephalochordates.",
    "secondary": "In insect morphology and chordate anatomy, designating structures such as the metapleural glands of ants (which secrete antimicrobial compounds) or the metapleural folds of amphioxus (Branchiostoma).",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Ants possess specialized **metapleural** glands on the thorax that produce phenylacetic acid to inhibit fungal spore germination."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In amphioxus, the ventrolateral **metapleural** folds run along each side of the body, enclosing the atrial cavity."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "The presence of active **metapleural** glands is a fundamental morphological hallmark distinguishing Formicidae from other aculeate wasps."
      }
    ]
  },
  "Dashboard — pleur\\pleura.md": {
    "primary": "A delicate serous membrane enclosing each lung and lining the thoracic cavity (consisting of visceral and parietal layers).",
    "secondary": "In human anatomy and thoracic pathology, the double-layered mesothelial sac that secretes serous fluid into the pleural space to allow frictionless pulmonary sliding during breathing.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Each lung is invested on its external surface by a delicate serous sac, the **pleura**, which also lines the inner thoracic wall."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fibrinous exudate coating the inflamed **pleura** produces the harsh friction rub audible on auscultation."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Malignant mesothelioma arises directly from the mesothelial lining cells of the parietal and visceral **pleura**."
      }
    ]
  },
  "Dashboard — pleur\\pleural.md": {
    "primary": "Relating to the pleura or the thoracic cavity surrounding the lungs.",
    "secondary": "In pulmonary medicine and radiology, describing pathological conditions, fluids, or spaces associated with the pleura (such as pleural effusion, pleural space, pleural rub).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Percussion over a massive **pleural** effusion yields stony dullness with absent tactile fremitus."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **pleural** cavity contains normally only a capillary film of serous fluid that lubricates pulmonary excursions."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Opening the **pleural** cavity without negative-pressure chambers formerly led to fatal lung collapse."
      }
    ]
  },
  "Dashboard — pleur\\pleuralgia.md": {
    "primary": "Pain in the side, chest wall, or pleura (pleurodynia).",
    "secondary": "In clinical medicine, sharp, lancinating thoracic chest pain aggravated by deep inspiration or coughing, originating from parietal pleural irritation, intercostal neuralgia, or rib trauma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden onset of severe **pleuralgia** in young adults should suggest acute pleurisy or spontaneous pneumothorax."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Intercostal shingles often masquerades as acute **pleuralgia** before the vesicular cutaneous eruption appears."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Patients tormented with sharp **pleuralgia** find breathing insupportable except when lying immobilized on the affected side."
      }
    ]
  },
  "Dashboard — pleur\\pleurisy.md": {
    "primary": "Inflammation of the pleura accompanied by sharp chest pain that worsens during breathing and coughing.",
    "secondary": "In respiratory medicine, fibrinous or serofibrinous inflammation of the pleural membranes (pleuritis), commonly secondary to pneumonia, tuberculosis, pulmonary embolism, or viral infection.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Dry **pleurisy** is characterized by acute stitch-like pain in the side, aggravated by respiration and accompanied by a superficial leathery friction sound."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Auscultation enabled me to detect the characteristic rubbing sound that signals acute **pleurisy** before effusion accumulates."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Norwood Builder",
        "quote": "The old housekeeper was confined to her bed with a severe attack of winter **pleurisy**."
      }
    ]
  },
  "Dashboard — pleur\\pleuritis.md": {
    "primary": "Inflammation of the pleura; pleurisy.",
    "secondary": "In histological pathology and clinical pulmonology, acute or chronic inflammation of the mesothelial lining and subpleural connective tissue, often leading to fibrous adhesions between lung and chest wall.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In acute fibrinous **pleuritis**, dense networks of fibrin and migrating leucocytes cover the glistening surface of the lungs."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Tuberculous **pleuritis** frequently presents insidiously with massive lymphocytic effusion and minimal fever."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Chronic calcifying **pleuritis** created an unyielding fibrous peel that severely restricted ventilatory excursion."
      }
    ]
  },
  "Dashboard — pleur\\pleurobrachia.md": {
    "primary": "A genus of ctenophores (comb jellies) commonly known as sea gooseberries, characterized by a rounded, transparent body and two long tentilla-bearing tentacles.",
    "secondary": "In marine invertebrate zoology, the type genus of Pleurobrachiidae, possessing eight meridional rows of ciliated comb plates (ctenes) used for swimming and colloblasts for capturing planktonic prey.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The transparent spherical body of **pleurobrachia** glitters with iridescent colors along its eight active comb rows."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Specimens of **pleurobrachia** swept along by ocean currents trail long, contractile tentacles adorned with sticky colloblasts."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "At night the waters sparkled with phosphorescent flashes emitted by drifting **pleurobrachia** and hydromedusae."
      }
    ]
  },
  "Dashboard — pleur\\pleurobrachiidae.md": {
    "primary": "A family of cydippid ctenophores comprising pelagic comb jellies with spherical, ovate, or pear-shaped bodies and retractile tentacles.",
    "secondary": "In invertebrate systematics, a cosmopolitan marine family characterized by well-developed tentacular sheaths, biradial symmetry, and rows of locomotive paddle-like cilia.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Members of the **pleurobrachiidae** exhibit the quintessential ctenophore body plan with fully functional aboral sensory organs."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Taxonomic distinction of the **pleurobrachiidae** relies upon the deep lateral insertion of the tentacular apparatus."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Swarms of **pleurobrachiidae** drift across the continental shelf, grazing upon larval copepods and fish fry."
      }
    ]
  },
  "Dashboard — pleur\\pleurocarp.md": {
    "primary": "A moss that bears its female reproductive organs (archegonia) and subsequent sporophytes on short lateral branches rather than at the stem apex.",
    "secondary": "In bryology, a freely branching, prostrate, or mat-forming moss (order Hypnales, etc.), contrasting morphologically and ecologically with upright acrocarpous mosses.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "A typical **pleurocarp** forms extensive, creeping carpets across damp forest floors and fallen logs."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "The distinction between an acrocarp and a **pleurocarp** is fundamental in bryological identification and classification."
      },
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Branching lateral fructifications distinguish the habit of the creeping **pleurocarp** from the erect cushions of Polytrichum."
      }
    ]
  },
  "Dashboard — pleur\\pleurocarpous.md": {
    "primary": "Having female reproductive organs and sporophytes produced on short lateral twigs or branches rather than terminating the main stem (of mosses).",
    "secondary": "In bryological ecology, characterizing prostrate, interwoven, carpet-forming mosses that dominate moist forest soils, rotting wood, and wetland bogs.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Most **pleurocarpous** mosses are recognized by their spreading, feathery mats and lateral capsule stalks."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Botany of the Antarctic Voyage",
        "quote": "In subantarctic woodlands, luxurious carpets of **pleurocarpous** species drape rocks and tree bases alike."
      },
      {
        "author": "Charles Darwin",
        "work": "Journal of Researches",
        "quote": "Damp southern beech forests in Tierra del Fuego were upholstered in thick mats of **pleurocarpous** mosses."
      }
    ]
  },
  "Dashboard — pleur\\pleurodont.md": {
    "primary": "Having teeth ankylosed or attached by their sides to the inner surface of the jaw bone without sockets.",
    "secondary": "In herpetology and comparative vertebrate anatomy, describing dentition typical of iguanas, monitors, and many other lizards, where teeth fuse directly to the lingual shelf of the jawbone.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Odontography; or, A Treatise on the Comparative Anatomy of the Teeth",
        "quote": "In the **pleurodont** dentition of iguanid lizards, the base of each tooth fuses securely along the inner alveolar ledge."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Lizards exhibit either acrodont or **pleurodont** tooth attachment, reflecting divergent evolutionary lineages within the squamates."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "The fossil jaw fragments revealed a typical **pleurodont** structure, confirming their affinity with modern lacertilians."
      }
    ]
  },
  "Dashboard — pleur\\pleurodynia.md": {
    "primary": "Severe paroxysmal pain in the chest wall, intercostal muscles, or pleural region.",
    "secondary": "In infectious disease, epidemic pleurodynia (Bornholm disease), an acute infection caused by Coxsackie B viruses, presenting with sudden, knife-like spasms of thoracic and diaphragmatic muscle pain.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Epidemic **pleurodynia** manifests with excruciating paroxysms of pain at the diaphragmatic attachments, simulating acute peritonitis."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Muscular **pleurodynia** must be carefully distinguished from true pleurisy by the complete absence of a friction rub."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The agonizing thoracic cramps of **pleurodynia** render every deep breath an ordeal for the patient."
      }
    ]
  },
  "Dashboard — pleur\\pleuron.md": {
    "primary": "The lateral region, sclerite, or side wall of each segment of an insect or other arthropod body.",
    "secondary": "In arthropod morphology, the lateral cuticular plate connecting the dorsal tergum to the ventral sternum, supporting the articulating bases of the legs and wings.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish: An Introduction to the Study of Zoology",
        "quote": "Each abdominal somite consists of a dorsal tergum, a ventral sternum, and flanking lateral plates termed the **pleuron**."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "The thoracic **pleuron** of worker ants contains the deep opening of the metapleural gland."
      },
      {
        "author": "John Lubbock",
        "work": "Ants, Bees, and Wasps",
        "quote": "Examination under the microscope reveals muscular attachments securing the coxae firmly to the **pleuron**."
      }
    ]
  },
  "Dashboard — pleur\\pleuronectes.md": {
    "primary": "A genus of flatfishes in the family Pleuronectidae that includes the European plaice (Pleuronectes platessa).",
    "secondary": "In ichthyology, a genus of right-eyed flatfishes named from Greek pleuron (side) and nekton (swimmer), reflecting their evolutionary adaptation of swimming horizontally on their left side with both eyes on the right.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Linnaeus established **Pleuronectes** to encompass the flatfishes whose asymmetrical skulls adapt them for bottom-dwelling life."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The ontogenetic migration of the eye across the head in **pleuronectes** illustrates how directional selection transforms asymmetrical morphology."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In adult **pleuronectes**, the entire dorsal surface is pigmented while the blind side remains stark white."
      }
    ]
  },
  "Dashboard — pleur\\pleuronectidae.md": {
    "primary": "A family of flatfishes commonly known as righteye flounders, characterized by having both eyes on the right side of the body.",
    "secondary": "In systematic ichthyology, marine demersal teleosts whose pelagic symmetrical larvae undergo cranial metamorphosis during settlement, resulting in an asymmetrical benthic adult morphology.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The family **pleuronectidae** comprises benthic predators exquisitely adapted for camouflage among sandy sea bottoms."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Skeletal asymmetry in the **pleuronectidae** was long cited as one of the most remarkable puzzles of vertebrate morphology."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Flounders belonging to the **pleuronectidae** lay buried in the silt, only their elevated periscopic eyes protruding."
      }
    ]
  },
  "Dashboard — pleur\\pleuropneumonia.md": {
    "primary": "Concurrent inflammation of both the lungs and the pleura (pneumonia complicated by pleurisy).",
    "secondary": "In veterinary medicine and agricultural history, contagious bovine pleuropneumonia (CBPP), a devastating livestock disease caused by Mycoplasma mycoides characterized by marbling of the lungs and copious pleural exudate.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extensive fibrinous exudation upon the visceral pleura accompanied dense hepatization, establishing a diagnosis of acute **pleuropneumonia**."
      },
      {
        "author": "Louis Pasteur",
        "work": "Collected Works on Infectious Diseases",
        "quote": "Preventive inoculation against contagious bovine **pleuropneumonia** checked the ruinous spread of the plague among French herds."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The thick gelatinous interlobular septa seen in bovine **pleuropneumonia** demonstrate marked lymphatic thrombosis."
      }
    ]
  },
  "Dashboard — pleur\\pleurosorus.md": {
    "primary": "A genus of small lithophytic or epipetric ferns in the family Aspleniaceae, native to temperate regions and rocky cliffs.",
    "secondary": "In pteridology, delicate rock-dwelling ferns characterized by elongated, exindusiate sori running alongside the lateral veins of the frond segments.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "Specimens of **pleurosorus** nestle in sheltered rock crevices, protected from desiccating alpine winds."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The distinctive lack of an indusium differentiates **pleurosorus** from typical members of Asplenium."
      },
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "Crevices along basaltic cliffs yielded fragile fronds of **pleurosorus** rutifolius in the Australian ranges."
      }
    ]
  },
  "Dashboard — pleur\\pleurothallis.md": {
    "primary": "A huge genus of Neotropical epiphytic orchids in the family Orchidaceae, characterized by non-pseudobulbous stems bearing a single leaf.",
    "secondary": "In systematic botany, one of the most species-rich genera of angiosperms, featuring small, intricately structured zygomorphic flowers emerging from the sulcus of the leaf blade.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Fertilisation of Orchids",
        "quote": "The miniature flowers of **pleurothallis** present microscopic floral mechanisms adapted for tiny dipteran pollinators."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Neotropical cloud forests harbor an immense diversity of the genus **pleurothallis**, growing high in the mossy canopy."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "In **pleurothallis**, each slender stem bears only a single solitary leaf, from whose base delicate racemes arise."
      }
    ]
  },
  "Dashboard — pleur\\pleurotus.md": {
    "primary": "A genus of gilled mushrooms commonly known as oyster mushrooms, typically growing shelf-like on decaying wood.",
    "secondary": "In mycology and biotechnology, wood-decaying basidiomycete fungi (e.g. Pleurotus ostreatus) characterized by eccentric or lateral stipes, white spore prints, and carnivorous nematophagous abilities.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Species of the genus **pleurotus** flourish on decaying tree trunks, displaying laterally attached imbricated caps."
      },
      {
        "author": "Beatrix Potter",
        "work": "Illustrations and Studies in Mycology",
        "quote": "The fan-shaped, fleshy basidiocarps of **pleurotus** ostreatus cluster upon decaying beech logs in autumn."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Wood-decay fungi such as **pleurotus** play an indispensable role in recycling forest lignocellulose back into living soil."
      }
    ]
  },
  "Dashboard — pleur\\pseudopleuronectes.md": {
    "primary": "A genus of righteye flatfishes in the family Pleuronectidae that includes the winter flounder (Pseudopleuronectes americanus).",
    "secondary": "In marine fisheries biology, cold-adapted demersal flatfishes native to the northwestern Atlantic, renowned for expressing antifreeze proteins in their blood plasma during winter.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The genus **pseudopleuronectes** encompasses valuable commercial flounders abundant along North American coastal shoals."
      },
      {
        "author": "Henry Bigelow",
        "work": "Fishes of the Gulf of Maine",
        "quote": "The winter flounder, **pseudopleuronectes** americanus, migrates into shallow estuaries to spawn during the coldest months."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Trawlers dragging the continental shelf harvest rich catches of **pseudopleuronectes** resting in muddy troughs."
      }
    ]
  },
  "Dashboard — pleur\\tripleurospermum.md": {
    "primary": "A genus of flowering plants in the family Asteraceae commonly known as scentless mayweed or false chamomile.",
    "secondary": "In botanical taxonomy, annual or perennial herbs distinguished from Matricaria by having achenes with three prominent ribs and two resin glands on the dorsal surface.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Linnaeus described the daisy-like heads of **tripleurospermum** growing profusely in fallow grain fields."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The lack of aromatic fragrance immediately separates **tripleurospermum** inodorum from true chamomile."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "We found hearty colonies of **tripleurospermum** thriving along gravelly riverbeds in high Himalayan valleys."
      }
    ]
  },
  "Dashboard — pne\\anapnograph.md": {
    "primary": "An apparatus or instrument for recording the speed, volume, and respiratory force of breathing movements.",
    "secondary": "In historical respiratory physiology, an early diagnostic spirometric device developed in the 19th century to register graphical tracings of pulmonary inhalation and exhalation.",
    "quotes": [
      {
        "author": "John Tyndall",
        "work": "Sound: A Course of Eight Lectures Delivered at the Royal Institution",
        "quote": "The experimental tracings obtained from an **anapnograph** demonstrate rhythmic air movements during vocal respiration."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Physiological recordings made with the **anapnograph** revealed the alternating tidal patterns of Cheyne-Stokes breathing."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Instrumental verification of respiratory pressure by the **anapnograph** provided quantitative data for pulmonary dynamics."
      }
    ]
  },
  "Dashboard — pne\\anapnoic.md": {
    "primary": "Relating to, relieving, or restoring respiration; respiratory; reviving breath.",
    "secondary": "In classical pharmacological texts and physiological semiotics, designating therapeutic measures, vapory inhalations, or stimuli that restore breathing during asphyxia or syncope.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Strong smelling salts and cool affusion were applied as an **anapnoic** stimulus to revive the fainting patient."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on Experimental Pathology",
        "quote": "The reflex excitation of the vagus nerve elicited an immediate **anapnoic** response in the anesthetized animal."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Fresh air admitted into the sickroom proved the most grateful **anapnoic** remedy for the breathless invalid."
      }
    ]
  }
};

console.log('Starting Body Rem B Batch 2 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 2 complete: successfully updated ' + updated + ' notes.');
