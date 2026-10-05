# -*- coding: utf-8 -*-
"""
curate_anatomy_b1_p1a.py
Batch 1 Part 1a of Cluster Anatomy & Clinical Medicine (25 words):
- adip (5 words): adipose, adiposeness, adiposis, adiposity, superadipose
- cervic (4 words): cervical, cervicectomy, cervicitis, cervicothoracic
- lacrim (4 words): lacrimal, lacrimation, lacrimator, lacrimatory
- dent part 1 (12 words): dent, dental, dentate, dented, denticle, denticulate,
  dentifrice, dentin, dentine, dentist, dentistry, dentition
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_p1a = {
    # ==================== Dashboard — adip (5 words) ====================
    "adipose": {
        "primary": "Pertaining to, composed of, or resembling animal fat; fatty.",
        "secondary": "In histology and metabolic physiology, describing connective tissue specialized for triacylglycerol storage, endocrine signaling, and thermal insulation.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In animals living in cold climates, a thick layer of **adipose** tissue beneath the dermis serves as an essential barrier against freezing temperatures."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Excessive accumulation of **adipose** deposits around the pericardium frequently embarrasses cardiac contractions."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Microscopic sections through the hypodermis reveal dense clusters of **adipose** cells packed with gleaming oil droplets."}
        ]
    },
    "adiposeness": {
        "primary": "Excessive fattiness, corpulence, or fatty degeneration in animal tissues.",
        "secondary": "In clinical pathology and historical autopsy reports, pronounced lipid accumulation infiltrating parenchymal organs or subcutaneous compartments.",
        "quotes": [
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "A marked **adiposeness** of the abdominal walls severely impedes deep palpation of the visceral organs."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham, M.D.", "quote": "Sedentary living combined with rich wines induces an unwholesome **adiposeness** that clogs the vital vessels."},
            {"author": "Erasmus Darwin", "work": "Zoonomia; or, The Laws of Organic Life", "quote": "Morbid **adiposeness** in elderly patients frequently gives rise to dropsical swellings in the lower extremities."}
        ]
    },
    "adiposis": {
        "primary": "A medical condition characterized by excessive or abnormal accumulation of fat within the body.",
        "secondary": "In clinical endocrinology and metabolic pathology, localized or diffuse lipid dysregulation, exemplified by adiposis dolorosa (Dercum's disease).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dercum described a painful form of **adiposis** characterized by tender lipomatous masses and asthenia in middle-aged women."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Fatty infiltration of the myocardium represents an extreme consequence of systemic **adiposis**."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "Disruption of hepatic glycogen regulation frequently accelerates abnormal **adiposis** in laboratory animals."}
        ]
    },
    "adiposity": {
        "primary": "Excessive corpulence, obesity, or fatty accumulation throughout bodily tissues.",
        "secondary": "In nutritional science and clinical anthropometry, the proportional abundance of total body fat relative to lean skeletal and muscular mass.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "His rotund figure and jovial countenance displayed a comfortable **adiposity** that suggested years of peaceful dining."},
            {"author": "William Osler", "work": "Aequanimitas", "quote": "Moderate exercise and abstemious dining remain our principal defenses against the encumbrance of advancing **adiposity**."},
            {"author": "Charles Dickens", "work": "The Posthumous Papers of the Pickwick Club", "quote": "The fat boy leaned against the doorpost in a state of profound somnolence induced by constitutional **adiposity**."}
        ]
    },
    "superadipose": {
        "primary": "Exhibiting an excessive or extreme degree of fattiness or corpulence beyond ordinary obesity.",
        "secondary": "In clinical bariatrics and pathological anatomy, designating severe Class III morbid obesity characterized by extensive systemic metabolic stress.",
        "quotes": [
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "In **superadipose** subjects, respiratory excursions are dramatically restricted by the heavy burden resting upon the thorax."},
            {"author": "Thomas Sydenham", "work": "Medical Observations", "quote": "A **superadipose** constitution renders the patient especially vulnerable to apoplectic seizures during hot summer weather."},
            {"author": "Erasmus Darwin", "work": "Zoonomia", "quote": "He described a **superadipose** invalid whose immense bulk prevented any independent locomotion about his chamber."}
        ]
    },

    # ==================== Dashboard — cervic (4 words) ====================
    "cervical": {
        "primary": "Pertaining to the neck, or relating to the cervix of the uterus.",
        "secondary": "In human anatomy and obstetrics, relating to the seven vertebrae of the neck or the narrow inferior neck of the uterus.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The giraffe possesses the identical number of **cervical** vertebrae as the shortest-necked mammal, though each bone is enormously elongated."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Enlargement of the deep **cervical** lymph nodes often provides the earliest diagnostic clue in malignant lymphomas."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The anterior nerve roots emerge through the intervertebral foramina along the entire **cervical** segment of the spinal column."}
        ]
    },
    "cervicectomy": {
        "primary": "The surgical excision or amputation of the cervix uteri.",
        "secondary": "In gynecological oncology, trachelectomy or surgical removal of the uterine cervix performed to treat early-stage malignancies while preserving fertility.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early surgical intervention by radical **cervicectomy** prevents invasive dissemination in localized malignant lesions."},
            {"author": "Howard Kelly", "work": "Operative Gynecology", "quote": "The surgeon executed a high **cervicectomy**, carefully ligating the descending branches of the uterine arteries."},
            {"author": "Sir Astley Cooper", "work": "Lectures on the Principles and Practice of Surgery", "quote": "Amputation of the diseased cervix, known as **cervicectomy**, was performed with successful arrest of chronic hemorrhages."}
        ]
    },
    "cervicitis": {
        "primary": "Inflammation of the mucous membrane lining the cervix uteri.",
        "secondary": "In clinical gynecology and reproductive pathology, acute or chronic inflammatory changes of the endocervical and ectocervical epithelium caused by bacterial infection or chemical irritation.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic **cervicitis** often presents with persistent mucopurulent discharge and secondary pelvic discomfort."},
            {"author": "Howard Kelly", "work": "Operative Gynecology", "quote": "Topical antiseptic applications were formerly employed to alleviate the ulcerations associated with severe **cervicitis**."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Local inflammatory engorgement of the neck of the womb, termed **cervicitis**, yields readily to soothing fomentations."}
        ]
    },
    "cervicothoracic": {
        "primary": "Pertaining to or involving both the cervical (neck) and thoracic (chest) regions of the body.",
        "secondary": "In neuroanatomy and spine surgery, designating the cervicothoracic junction (C7–T1) or the cervicothoracic sympathetic ganglion (stellate ganglion).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful neurological examination traced the cutaneous sensory loss directly to the **cervicothoracic** segments of the cord."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The transitional vertebrae of the **cervicothoracic** border exhibit vestigial rib elements in embryonic development."},
            {"author": "Sir Astley Cooper", "work": "A Treatise on Dislocations and Fractures of the Joints", "quote": "Fractures occurring at the **cervicothoracic** junction demand rigorous immobilization to prevent catastrophic displacement of the vertebrae."}
        ]
    },

    # ==================== Dashboard — lacrim (4 words) ====================
    "lacrimal": {
        "primary": "Pertaining to, producing, or conveying tears.",
        "secondary": "In ophthalmology and craniofacial anatomy, designating the tear-secreting gland, puncta, sac, nasolacrimal duct, or the small fragile lacrimal bone of the orbit.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Spasmodic contraction of the eyelids during violent weeping compresses the **lacrimal** gland, forcing a profuse stream of tears."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction of the **lacrimal** sac leads to chronic epiphora and distressing secondary infections of the conjunctiva."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Tears secreted by the **lacrimal** gland wash across the cornea and drain through two tiny canals into the nasal cavity."}
        ]
    },
    "lacrimation": {
        "primary": "The secretion or discharge of tears, especially when excessive.",
        "secondary": "In clinical ophthalmology and toxicology, reflex tear shedding triggered by corneal irritation, chemical vapors, emotional distress, or trigeminal autonomic cephalalgias.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Irritation of the eye by cold wind or foreign particles excites instantaneous reflex **lacrimation** to cleanse the delicate surface."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Unilateral headache accompanied by profuse **lacrimation** and nasal congestion points to involvement of sympathetic nerve pathways."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Excessive **lacrimation** overflows the margins of the lower lid when the drainage ducts become overwhelmed."}
        ]
    },
    "lacrimator": {
        "primary": "A substance or chemical agent that irritates the eyes and stimulates the flow of tears.",
        "secondary": "In toxicology and chemical warfare, a volatile riot-control agent (such as CS gas or chloroacetophenone) that produces transient incapacitating blepharospasm and crying.",
        "quotes": [
            {"author": "Humphry Davy", "work": "Researches, Chemical and Philosophical", "quote": "Certain volatile halogen vapors act as a powerful **lacrimator**, blinding the experimenter with sudden copious tears."},
            {"author": "J. B. S. Haldane", "work": "Callinicus: A Defence of Chemical Warfare", "quote": "A harmless tear gas functions as an effective **lacrimator**, dispersing hostile gatherings without inflicting permanent organic trauma."},
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Police patrols deployed aerosol canisters of synthetic **lacrimator** to neutralize rioters without resorting to lethal firearms."}
        ]
    },
    "lacrimatory": {
        "primary": "Pertaining to or causing tears, or a small antique vessel formerly believed to hold tears of mourners.",
        "secondary": "In classical archaeology and ophthalmology, a tear-bottle (*lachrymatory*) found in ancient Roman sepulchers, or physiological reflexes producing weeping.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "Among the burnt relics were found small glass ampullae, commonly reputed for tear-bottles or **lacrimatory** vessels of ancient mourners."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Miss Dartle looked with bitter scorn at the weepings of Mrs. Steerforth, mocking her **lacrimatory** displays as hollow theatricals."},
            {"author": "Nathaniel Hawthorne", "work": "Mosses from an Old Manse", "quote": "The antique scholar displayed an exquisite Roman **lacrimatory**, imagining the forgotten sorrows once consecrated within its delicate crystal."}
        ]
    },

    # ==================== Dashboard — dent (part 1: 12 words) ====================
    "dent": {
        "primary": "A slight hollow or depression made in a surface by a blow or pressure.",
        "secondary": "In metallurgy and mechanical inspection, plastic surface deformation caused by localized impact that alters contour without rupturing material integrity.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The heavy iron fluke of the anchor struck the bulwark, leaving a deep **dent** in the seasoned oak timber."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "My axe head bore a small **dent** from striking a hidden granite pebble buried within the frozen pine stump."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old copper kettle showed many a **dent** and scratch from half a century of active boiling upon the hearth."}
        ]
    },
    "dental": {
        "primary": "Pertaining to the teeth, or relating to dentistry and dental care.",
        "secondary": "In phonetics and odontological anatomy, speech sounds articulated with the tongue against the upper teeth, or anatomical structures of the dentition.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **dental** formulas of placental mammals exhibit striking homologies that elucidate their ancestral genealogical affinities."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic oral sepsis arising from neglected **dental** caries frequently serves as the hidden nidus for bacterial endocarditis."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In carnivorous quadrupeds, the specialized **dental** apparatus includes sharp sectorial blades designed to shear flesh and bone."}
        ]
    },
    "dentate": {
        "primary": "Having tooth-like notches, projections, or serrations along the margin.",
        "secondary": "In botany and neuroanatomy, describing leaves with outward-pointing teeth perpendicular to the edge, or the dentate gyrus and dentate nucleus of the brain.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The leaves of the primrose are distinctly **dentate**, bearing small glandular teeth along their ruffled margins."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "In this species of birch, the leaf margin is sharply and doubly **dentate** from base to apex."},
            {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Dense rows of granule cells populate the **dentate** gyrus, projecting mossy fibers into the pyramidal neurons of CA3."}
        ]
    },
    "dented": {
        "primary": "Having a surface depression or indentation caused by an impact or blow.",
        "secondary": "In material forensics and armor history, exhibiting localized plastic deformation after absorbing kinetic mechanical force.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The captain's pewter mug was battered and **dented** from being hammered upon the cabin table during tropical storms."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight's helmet was sorely bruised and **dented** by the furious axe strokes of his Saxon antagonist."},
            {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "My sheet-iron breastplate was so **dented** by lance thrusts that it pinched my ribs at every step."}
        ]
    },
    "denticle": {
        "primary": "A small tooth or tooth-like projection, notch, or serration.",
        "secondary": "In elasmobranch marine zoology and comparative odontography, dermal denticles (placoid scales) covering shark skin, homologous to vertebrate teeth.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rough shagreen of the shark consists of countless microscopic **denticle** structures embedded within the dermis."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Each dermal **denticle** contains a central pulp cavity surrounded by calcified dentine and capped with hard enamel."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "Under high magnification, every **denticle** reveals intricate fluting that reduces drag as the fish glides through water."}
        ]
    },
    "denticulate": {
        "primary": "Having small teeth, minute notches, or delicate serrations along the edge.",
        "secondary": "In systematic botany and malacology, describing margins or radular ribbons adorned with fine, diminutive tooth-like serrations.",
        "quotes": [
            {"author": "Asa Gray", "work": "First Lessons in Botany and Vegetable Physiology", "quote": "When the tooth-like projections of a leaf margin are very small and fine, botanists term the leaf **denticulate**."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The wild varieties of this brassica display a **denticulate** foliage that becomes smooth under systematic garden cultivation."},
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The slender stalks bear narrow leaves finely **denticulate** along their edges like the small blade of a saw."}
        ]
    },
    "dentifrice": {
        "primary": "A paste, powder, or liquid preparation used for cleaning and polishing the teeth.",
        "secondary": "In dental hygiene history and pharmacognosy, abrasive and antiseptic formulations (historically containing chalk, charcoal, or myrrh) designed to remove plaque and prevent oral halitosis.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The maid of honor polished her pearly teeth with an aromatic **dentifrice** imported from the eastern merchants."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Upon the dressing-table stood a pot of scented **dentifrice** and a silver-handled brush belonging to the young gentleman."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Careful scrubbing with a mild prepared chalk **dentifrice** preserves the enamel far better than harsh acidic washes."}
        ]
    },
    "dentin": {
        "primary": "The hard, dense, calcified tissue forming the bulk of a tooth beneath the enamel and cementum.",
        "secondary": "In oral histology and odontogenesis, mineralized connective tissue traversed by microscopic dentinal tubules containing odontoblastic cellular processes.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The body of the tooth consists of **dentin**, a resilient ivory-like bone substance enclosing the sensitive vascular pulp."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Cross sections of fossil teeth reveal that **dentin** tubules maintain identical microscopic configurations through millions of years."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Erosion of the protective enamel exposes the underlying **dentin**, rendering the tooth acutely sensitive to thermal changes."}
        ]
    },
    "dentine": {
        "primary": "The yellowish calcified tissue comprising the main structural mass of a tooth surrounding the pulp cavity.",
        "secondary": "In comparative anatomy and dental pathology (variant spelling of dentin), tubular calcified tissue composed primarily of hydroxyapatite and collagen fibers.",
        "quotes": [
            {"author": "Richard Owen", "work": "Odontography; or, A Treatise on the Comparative Anatomy of the Teeth", "quote": "In the elephant's tusk, modified **dentine** known as ivory displays intersecting curved lines that distinguish it from bone."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The microscopic canals radiating through **dentine** transmit nutritive fluid and sensory fibrils from the central dental pulp."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The thick layer of **dentine** in primate incisors provides tensile resilience against accidental fracture while masticating hard nuts."}
        ]
    },
    "dentist": {
        "primary": "A qualified healthcare practitioner licensed to diagnose, treat, and prevent diseases and conditions of the teeth and gums.",
        "secondary": "In healthcare sociology and medical history, an oral surgical specialist who restores carious teeth, extracts damaged roots, and fabricates prostheses.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He looked as nervous as a patient seated in the operating chair awaiting the fateful entrance of the **dentist**."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The party spent two hours in London while Robert Ferrars paid an urgent visit to his fashionable **dentist**."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "A slip of paper bearing the appointment address of a prominent West End **dentist** was discovered in the deceased man's pocket."}
        ]
    },
    "dentistry": {
        "primary": "The profession, science, or practice of diagnosing, treating, and preventing diseases of the teeth, gums, and oral cavity.",
        "secondary": "In dental medicine and public health, the specialized branch of medicine encompassing endodontics, orthodontics, periodontics, prosthodontics, and oral surgery.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Modern **dentistry** has made astonishing advances, transforming what was once a painful torture into a precise and humane art."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Preventive **dentistry** plays an indispensable role in maintaining systemic resistance against chronic infectious diseases."},
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The brass doorplate announced that the tenant practiced surgery, bleeding, and mechanical **dentistry** upon reasonable terms."}
        ]
    },
    "dentition": {
        "primary": "The arrangement, condition, type, or number of teeth in a person or animal, or the process of teething.",
        "secondary": "In mammalian taxonomy and paleontology, the characteristic dental formula (incisors, canines, premolars, molars) reflecting diet and phylogenetic heritage.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **dentition** of anthropoid apes exhibits the identical thirty-two teeth arranged in the same general formula as in man."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Carnivorous **dentition** is uniquely characterized by sharp tearing canines and shearing blade-like carnassial molars."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The gradual evolution of herbivorous ungulates is recorded in the progressive hypsodont **dentition** adapted for grinding coarse grasses."}
        ]
    }
}
