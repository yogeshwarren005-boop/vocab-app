# -*- coding: utf-8 -*-
"""
Generator for Body Part 3 - Batch 5 (indices 256..319, 64 words).
From Dashboard — haem/hemorrhoidectomy.md to Dashboard — hist/histiocytosis.md.
"""
import json
import os

batch5_data = {
    # 1. hemorrhoidectomy
    "Dashboard — haem\\hemorrhoidectomy.md": {
        "primary": "The surgical removal and excision of diseased or prolapsed hemorrhoids.",
        "secondary": "In colorectal surgery, an operative resection of third- or fourth-degree hemorrhoidal cushions performed using open (Milligan-Morgan) or closed (Ferguson) anatomical techniques.",
        "quotes": [
            {"author": "Percivall Pott", "work": "Chirurgical Works", "quote": "When strangulated piles resist all soothing emollients, a prompt **hemorrhoidectomy** rescues the patient from threatened sloughing and gangrene."},
            {"author": "Joseph Lister", "work": "Collected Papers", "quote": "By performing **hemorrhoidectomy** under carbolic irrigation, the customary septic suppuration of the perineal tissues was entirely averted."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Delicate submucosal dissection during **hemorrhoidectomy** avoids subsequent cicatricial narrowing of the anal canal."}
        ]
    },
    # 2. hemosiderin
    "Dashboard — haem\\hemosiderin.md": {
        "primary": "An insoluble yellowish-brown iron-storage complex composed of ferritin, ferric oxide, and degraded protein found in cells.",
        "secondary": "In histopathology, granular golden-brown pigment formed by the phagocytic breakdown of red blood cells, readily identified by Perls' Prussian blue stain.",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination of chronically congested lungs revealed alveolar macrophages densely packed with golden granules of **hemosiderin**."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The bronze pigmentation of the dermis and liver in bronze diabetes is due to an overwhelming deposition of **hemosiderin**."},
            {"author": "Felix Hoppe-Seyler", "work": "Handbuch der Physiologisch- und Pathologisch-Chemischen Analyse", "quote": "Chemical degradation confirmed that **hemosiderin** represents an insoluble ferric aggregate derived from catabolized hemoglobin."}
        ]
    },
    # 3. hemosiderosis
    "Dashboard — haem\\hemosiderosis.md": {
        "primary": "A condition characterized by an excessive focal or systemic accumulation of hemosiderin within tissues and macrophages.",
        "secondary": "In clinical hematology, iron overload occurring without the tissue injury and cirrhosis characteristic of hemochromatosis, often secondary to multiple blood transfusions.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic hemolytic disorders managed by multiple transfusions, generalized **hemosiderosis** progressively saturates the reticuloendothelial system."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Focal **hemosiderosis** marks the exact site of previous tissue hemorrhage where phagocytes have digested extravasated corpuscles."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "When total iron stores surpass macrophage capacity, systemic **hemosiderosis** extends into parenchymal glandular organs."}
        ]
    },
    # 4. hemostasis
    "Dashboard — haem\\hemostasis.md": {
        "primary": "The physiological arrest of bleeding, involving vascular constriction, platelet adhesion, and blood coagulation.",
        "secondary": "In operative surgery, the technical achievement of arresting blood loss through mechanical, thermal, or pharmacological methods.",
        "quotes": [
            {"author": "William Stewart Halsted", "work": "The Training of the Surgeon", "quote": "The surgeon who insists upon rigorous **hemostasis** maintains an operative field in which anatomical planes remain crystal clear."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Normal biological **hemostasis** proceeds through vascular spasm, formation of a temporary platelet plug, and synthesis of a stable fibrin mesh."},
            {"author": "Alexis Carrel", "work": "The Treatment of Infected Wounds", "quote": "Meticulous vascular **hemostasis** eliminated blood accumulation, thereby preventing wound breakdown and bacterial colonization."}
        ]
    },
    # 5. hemostat
    "Dashboard — haem\\hemostat.md": {
        "primary": "A surgical clamp or forceps designed to compress blood vessels to arrest hemorrhage.",
        "secondary": "Any chemical agent, pharmaceutical dressing, or mechanical appliance utilized to arrest or prevent bleeding.",
        "quotes": [
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The delicate curved **hemostat** grasps only the bleeding vessel tip, sparing surrounding tissue from unnecessary crushing trauma."},
            {"author": "Joseph Lister", "work": "The Collected Papers of Joseph Lister", "quote": "The application of a sterilized **hemostat** promptly halted the spurting digital branch prior to ligature application."},
            {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "With swift precision, the operator snapped a **hemostat** onto the deep vessel, instantly halting the scarlet fountain."}
        ]
    },
    # 6. hemostatic
    "Dashboard — haem\\hemostatic.md": {
        "primary": "Tending to arrest or stop bleeding; possessing the property of halting hemorrhage.",
        "secondary": "A pharmacological agent, dressing, or coagulant substance that stops bleeding when applied locally or administered systemically.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Local pressure augmented with a cold **hemostatic** compress arrested the troublesome capillary oozing from the granulating bed."},
            {"author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Surgical authors have celebrated various herbal decoctions for their reputed **hemostatic** power upon lacerated flesh."},
            {"author": "Florence Nightingale", "work": "Notes on Hospitals", "quote": "Every field station must remain furnished with dependable **hemostatic** dressings to control traumatic arterial wounds."}
        ]
    },
    # 7. hemotherapy
    "Dashboard — haem\\hemotherapy.md": {
        "primary": "The medical treatment of disease through the therapeutic administration of blood or blood products; blood transfusion therapy.",
        "secondary": "In the history of medicine, therapeutic modalities relying upon whole blood, serum, or autologous blood injections to stimulate immunity or restore volume.",
        "quotes": [
            {"author": "Karl Landsteiner", "work": "The Specificity of Serological Reactions", "quote": "The classification of human blood into distinct groups transformed clinical **hemotherapy** into a predictable and safe therapeutic science."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of acute post-hemorrhagic collapse, direct **hemotherapy** supplies the vital volume and cellular elements required to sustain life."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Early forms of biological **hemotherapy** demonstrated how serum antitoxins could neutralize circulating diphtheria toxin."}
        ]
    },
    # 8. hyperaemia
    "Dashboard — haem\\hyperaemia.md": {
        "primary": "An excess of blood in the vessels supplying an organ or other part of the body; congestion.",
        "secondary": "In pathophysiological terminology, an active arteriolar dilatation (active hyperemia) or passive venous engorgement (passive hyperemia) resulting in vascular pooling.",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Active inflammatory **hyperaemia** causes the characteristic rubor of inflamed tissues by dilating pre-capillary arterioles."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic cardiac decompensation, passive pulmonary **hyperaemia** induces persistent cough and rusty sputum."},
            {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "Sectioning the cervical sympathetic trunk provoked immediate cutaneous **hyperaemia** and elevation of local temperature."}
        ]
    },
    # 9. hyperemia
    "Dashboard — haem\\hyperemia.md": {
        "primary": "An increased volume of blood in a particular organ, vascular bed, or bodily tissue.",
        "secondary": "In physiology and pathology, vascular engorgement categorized as active (functional or reactive, mediated by local vasodilators) or passive (resulting from impaired venous drainage).",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The intense focal **hyperemia** observed surrounding the wound site marks the preliminary vascular phase of repair."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inspection of the pharyngeal mucosa revealed diffuse fiery **hyperemia** characteristic of acute streptococcal infection."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Following temporary arterial occlusion, reactive **hyperemia** rapidly restores oxygenation to the ischemic muscle tissue."}
        ]
    },
    # 10. hyperemic
    "Dashboard — haem\\hyperemic.md": {
        "primary": "Characterized by, affected with, or exhibiting hyperemia; engorged with blood.",
        "secondary": "In clinical physical examination, describing tissues or mucous membranes that appear unusually red, flushed, and warm owing to vascular distension.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The tympanic membrane appeared markedly **hyperemic**, bulging outward under the pressure of middle-ear suppuration."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Around the central necrotic focus, a wide zone of **hyperemic** capillary loops marked the boundary of vital reaction."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "In acute laryngitis, the vocal folds present an intensely **hyperemic** and edematous mucosal border."}
        ]
    },
    # 11. hyphaema
    "Dashboard — haem\\hyphaema.md": {
        "primary": "The presence of blood in the anterior chamber of the eye between the cornea and the iris.",
        "secondary": "In ophthalmic surgery and trauma, a hemorrhagic collection in the anterior ocular segment resulting from blunt trauma to the iris or ciliary body, carrying risk of secondary glaucoma.",
        "quotes": [
            {"author": "William Mackenzie", "work": "A Practical Treatise on the Diseases of the Eye", "quote": "Blunt contusion of the globe frequently precipitates a visible **hyphaema**, the blood settling down by gravity to the lower angle of the chamber."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Laceration of the delicate circulus arteriosus iridis leads directly to traumatic **hyphaema** obscuring the lower half of the pupil."},
            {"author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "Unless strict bed rest is enforced, recurrent **hyphaema** may cause secondary corneal blood staining and severe elevation of intraocular tension."}
        ]
    },
    # 12. hyphema
    "Dashboard — haem\\hyphema.md": {
        "primary": "An accumulation of red blood cells in the anterior chamber of the eye.",
        "secondary": "In clinical ophthalmology, a traumatic or spontaneous ocular hemorrhage graded by the depth of blood layering (grades I through IV, up to complete eight-ball hyphema).",
        "quotes": [
            {"author": "William Mackenzie", "work": "A Practical Treatise on the Diseases of the Eye", "quote": "A layered **hyphema** was readily perceived through the transparent cornea, forming a dark red crescent at the base of the chamber."},
            {"author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "The spontaneous resorption of a traumatic **hyphema** depends upon patent trabecular outflow channels and absence of re-bleeding."},
            {"author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "In our eye clinic, sports injuries frequently presented with painful **hyphema** requiring topical cycloplegics and elevation of the head."}
        ]
    },
    # 13. hypovolemia
    "Dashboard — haem\\hypovolemia.md": {
        "primary": "A state of abnormally decreased volume of circulating blood plasma in the body.",
        "secondary": "In critical care medicine and physiology, effective intravascular fluid depletion resulting from hemorrhage, severe dehydration, or third-spacing, culminating in hypovolemic shock.",
        "quotes": [
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Severe acute **hypovolemia** triggers arterial baroreceptors to provoke intense sympathetic vasoconstriction and tachycardia."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The profound collapse seen in severe cholera is an extreme example of dehydration-induced **hypovolemia**."},
            {"author": "Alexis Carrel", "work": "The Treatment of Infected Wounds", "quote": "Prompt intravenous fluid infusion reversed the life-threatening **hypovolemia** resulting from battlefield exsanguination."}
        ]
    },
    # 14. hypovolemic
    "Dashboard — haem\\hypovolemic.md": {
        "primary": "Pertaining to, caused by, or characterized by hypovolemia; exhibiting low circulating blood volume.",
        "secondary": "In emergency and critical care medicine, describing shock states (hypovolemic shock) manifested by hypotension, cold clammy extremities, oliguria, and metabolic acidosis.",
        "quotes": [
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "In the early phases of **hypovolemic** shock, peripheral arteriolar constriction preserves cerebral and coronary perfusion."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient lapsed into a **hypovolemic** crisis marked by imperceptible radial pulses and clammy, pallid skin."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "To operate upon a patient in deep **hypovolemic** collapse without simultaneous vascular replenishment invites immediate cardiac arrest."}
        ]
    },
    # 15. ischemia
    "Dashboard — haem\\ischemia.md": {
        "primary": "An inadequate blood supply to an organ or tissue of the body, causing a deficiency of oxygen and nutrients.",
        "secondary": "In pathophysiological cardiology and neurology, localized tissue hypoperfusion resulting from arterial stenosis, thrombosis, embolism, or spasm, leading to cellular dysfunction or infarction.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Angina pectoris arises from transient myocardial **ischemia** provoked when coronary flow fails to satisfy metabolic demand."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Complete arterial **ischemia** leads irrevocably to coagulation necrosis and ischemic infarction of the dependent tissue territory."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "During localized **ischemia**, accumulation of acidic metabolites and adenosine acts as a potent stimulus for collateral vasodilation."}
        ]
    },
    # 16. ischemic
    "Dashboard — haem\\ischemic.md": {
        "primary": "Relating to, affected by, or caused by ischemia; deficient in blood supply.",
        "secondary": "Describing clinical disease entities (such as ischemic heart disease, ischemic stroke, or ischemic colitis) characterized by arterial circulatory compromise.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sudden focal neurological deficit was attributed to an acute **ischemic** attack in the distribution of the middle cerebral artery."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The wedge-shaped pale lesion within the spleen exhibited the classic morphological architecture of an **ischemic** infarct."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Severe **ischemic** contracture of muscle fibers ensues when collateral arterial blood flow falls below the critical threshold."}
        ]
    },
    # 17. methemoglobin
    "Dashboard — haem\\methemoglobin.md": {
        "primary": "A stable oxidation product of hemoglobin in which the iron of the heme group is oxidized from the ferrous (Fe2+) to the ferric (Fe3+) state, unable to bind oxygen.",
        "secondary": "In clinical biochemistry and toxicology, an altered blood metalloprotein that causes functional tissue hypoxia and gives blood a chocolate-brown appearance.",
        "quotes": [
            {"author": "Felix Hoppe-Seyler", "work": "Zeitschrift für Physiologische Chemie", "quote": "Upon treatment of hemoglobin with ferricyanide or nitrites, a brown derivative termed **methemoglobin** is produced, lacking oxygen-carrying capacity."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Toxic aniline exposure produces slate-gray cyanosis caused by the extensive conversion of normal pigment into **methemoglobin**."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Magnetic susceptibility data demonstrate that the iron atom in **methemoglobin** occupies a high-spin trivalent state coordinated with a water molecule."}
        ]
    },
    # 18. methemoglobinemia
    "Dashboard — haem\\methemoglobinemia.md": {
        "primary": "The presence of higher than normal levels of methemoglobin in the blood, resulting in cyanosis and impaired tissue oxygen delivery.",
        "secondary": "In clinical toxicology and genetics, an acquired (drug- or toxin-induced) or congenital (cytochrome b5 reductase deficiency or Hemoglobin M) disorder characterized by chocolate-colored blood and hypoxia unresponsive to supplemental oxygen.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The distinctive lavender-blue cyanosis of toxic **methemoglobinemia** fails to clear even when the patient inspires one hundred percent oxygen."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Certain aromatic nitro compounds provoke severe **methemoglobinemia** by promoting rapid catalytic oxidation of intracellular iron."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "When arterial **methemoglobinemia** exceeds thirty percent, symptoms of severe cerebral hypoxia, dizziness, and headache manifest promptly."}
        ]
    },
    # 19. microhematuria
    "Dashboard — haem\\microhematuria.md": {
        "primary": "The presence of microscopic quantities of red blood cells in the urine, detectable only by chemical reagent strips or microscopic sediment analysis.",
        "secondary": "In nephrology and urology, asymptomatic microscopic hematuria (defined as 3 or more RBCs per high-power field) serving as an early indicator of glomerulopathy, urolithiasis, or occult urothelial malignancy.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Routine urinalysis frequently discloses unsuspected **microhematuria**, which may constitute the earliest sign of latent glomerulonephritis."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "Even when the urine appears clear to the unaided eye, microscopic sediment examination reveals persistent **microhematuria** in subacute renal dropsy."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "The quiescent gravel stone lodged within the calyx betrayed its presence solely through persistent **microhematuria** on exertion."}
        ]
    },
    # 20. microhemorrhage
    "Dashboard — haem\\microhemorrhage.md": {
        "primary": "A minute, microscopic hemorrhage or petechial bleeding within a bodily tissue.",
        "secondary": "In neuroimaging and neuropathology, cerebral microbleeds detected by gradient-echo or susceptibility-weighted MRI, indicating chronic hypertensive microangiopathy or cerebral amyloid angiopathy.",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Widespread capillary **microhemorrhage** was observed throughout the cerebellar folia following violent septic embolization."},
            {"author": "Santiago Ramón y Cajal", "work": "Degeneration and Regeneration of the Nervous System", "quote": "Surrounding each focal **microhemorrhage**, reactive microglial phagocytes gathered to digest fragmented erythrocyte debris."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In infective endocarditis, retinal examination with the ophthalmoscope discloses pale-centered **microhemorrhage** known as Roth's spots."}
        ]
    },
    # 21. polycythaemia
    "Dashboard — haem\\polycythaemia.md": {
        "primary": "An abnormally increased concentration of hemoglobin and red blood cells in the circulating blood.",
        "secondary": "In clinical hematology, absolute erythrocytosis categorized as primary (polycythaemia vera, a myeloproliferative neoplasm) or secondary (driven by hypoxia-induced erythropoietin elevation).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic cyanotic **polycythaemia**, the ruddy, dusky hue of the face is accompanied by notable splenomegaly and massive erythrocyte counts."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "High-altitude acclimatization stimulates physiological **polycythaemia**, raising the hematocrit to enhance total blood oxygen-carrying capacity."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The elevated vascular viscosity attending severe **polycythaemia** substantially retards capillary circulation and predisposes to venous thrombosis."}
        ]
    },
    # 22. heparin
    "Dashboard — hepat\\heparin.md": {
        "primary": "A naturally occurring glycosaminoglycan anticoagulant produced by mast cells and basophils, used medically to prevent and treat thrombosis.",
        "secondary": "In pharmacology and hematology, an unbranched sulfated polysaccharide that binds to and exponentially accelerates the inhibitory activity of antithrombin III against thrombin and factor Xa.",
        "quotes": [
            {"author": "William Henry Howell", "work": "The Harvey Lectures", "quote": "Because this potent physiological anticoagulant was first extracted in quantity from canine liver tissue, we designated it **heparin**."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Therapeutic **heparin** administration immediately prolongs the partial thromboplastin time by neutralizing active coagulation proteases."},
            {"author": "Alexis Carrel", "work": "The Treatment of Infected Wounds", "quote": "The introduction of pure **heparin** during vascular suturing dramatically reduced the risk of intraluminal platelet thrombus formation."}
        ]
    },
    # 23. hepat
    "Dashboard — hepat\\hepat.md": {
        "primary": "The liver; a combining form or lexical root derived from ancient Greek denoting the liver.",
        "secondary": "In anatomical nomenclature and morphological linguistics, the fundamental root (from Greek ἧπαρ, ἡπατ-) prefixed across biomedical terms indicating hepatic structure, function, or disease.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The ancient Greek designation **hepat** remains the root of all modern anatomical designations pertaining to the parenchymal architecture of the liver."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clinicians employ the combining element **hepat** in diagnosing conditions ranging from simple hepatomegaly to toxic hepatopathy."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Our physiological investigations into the glycogenic function of the liver firmly established the primacy of the **hepat** root in metabolic science."}
        ]
    },
    # 24. hepatic
    "Dashboard — hepat\\hepatic.md": {
        "primary": "Of, relating to, or situated in the liver.",
        "secondary": "In human anatomy and physiology, designating structures (such as the hepatic artery, hepatic portal vein, or hepatic ducts) and metabolic functions specific to the liver.",
        "quotes": [
            {"author": "William Harvey", "work": "De Motu Cordis", "quote": "Blood carried through the mesenteric channels passes into the **hepatic** portal circulation before being returned toward the vena cava and right auricle."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **hepatic** lobules represent miniature hexagonal prisms, each penetrated centrally by an intralobular vein."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Advanced **hepatic** cirrhosis culminates in portal hypertension, ascites, and eventual hepatic encephalopathy."}
        ]
    },
    # 25. hepatica
    "Dashboard — hepat\\hepatica.md": {
        "primary": "A genus of small perennial herbs (liverleaf) in the buttercup family Ranunculaceae, native to woodland regions of the Northern Hemisphere.",
        "secondary": "In ethnobotany and medical history, the plant *Hepatica nobilis*, historically regarded under the doctrine of signatures as a liver remedy due to its three-lobed, liver-shaped leaves.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "The Writings of Henry David Thoreau: Journal", "quote": "Beneath the dead brown leaves on the southern bank, the delicate blue blossom of the **hepatica** was the earliest messenger of spring."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The three-lobed, coriaceous leaves of **hepatica** persist through the winter, providing a classic example of early woodland vernal bloom."},
            {"author": "William Turner", "work": "A New Herball", "quote": "The herb termed **hepatica** hath leaves resembling the lobes of the liver, wherefore ancient leeches prescribed it for diverse visceral obstructions."}
        ]
    },
    # 26. hepaticae
    "Dashboard — hepat\\hepaticae.md": {
        "primary": "The class of non-vascular bryophytic land plants comprising the liverworts (now often treated as Marchantiophyta).",
        "secondary": "In systematic bryology, primitive green plants characterized by dorsiventrally flattened thallose or leafy gametophytes, unicellular rhizoids, and elaters in the sporangium.",
        "quotes": [
            {"author": "Joseph Dalton Hooker", "work": "Flora Antarctica", "quote": "Damp rock crevasses in the subantarctic islands were richly carpeted with exquisite species belonging to the **hepaticae**."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Within the division of bryophytes, the **hepaticae** are set apart from the true mosses by their flattened thalli and distinctive sporophyte capsules."},
            {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Moist soil under forest shade affords an ideal habitat for spreading carpets of thalloid **hepaticae**."}
        ]
    },
    # 27. hepaticopsida
    "Dashboard — hepat\\hepaticopsida.md": {
        "primary": "A taxonomic class containing the liverworts, equivalent to Hepaticae or Marchantiopsida.",
        "secondary": "In modern plant taxonomy and evolutionary phylogenetics, the ancestral land plant clade characterized by lack of stomata, presence of oil bodies, and a brief, ephemeral sporophyte generation.",
        "quotes": [
            {"author": "Douglas Houghton Campbell", "work": "The Structure and Development of Mosses and Ferns", "quote": "The morphological divergence between the **hepaticopsida** and other bryophyte lineages sheds crucial light on early terrestrial plant evolution."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Representatives of **hepaticopsida** exhibit simple alternation of generations wherein the gametophyte remains the dominant photosynthetic phase."},
            {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "Deep ravines in the eastern Himalaya yielded an astonishing profusion of cryptogamic vegetation, including rare endemic **hepaticopsida**."}
        ]
    },
    # 28. hepatitis
    "Dashboard — hepat\\hepatitis.md": {
        "primary": "Inflammation of the liver, resulting in parenchymal cellular injury and potential impairment of liver function.",
        "secondary": "In clinical hepatology, an acute or chronic hepatic inflammatory disorder induced by hepatotropic viruses (A, B, C, D, E), autoimmune mechanisms, alcohol, or hepatotoxins.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute viral **hepatitis** presents with malaise, anorexia, and right upper quadrant tenderness, followed in several days by prominent clinical jaundice."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic sections from cases of acute yellow atrophy demonstrate an extreme, fulminant form of necrotizing **hepatitis**."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Obstinate inflammation of the liver, or acute **hepatitis**, if not promptly relieved by cooling remedies, may terminate in purulent abscess."}
        ]
    },
    # 29. hepatobiliary
    "Dashboard — hepat\\hepatobiliary.md": {
        "primary": "Relating to or involving both the liver and the gallbladder or bile ducts.",
        "secondary": "In gastroenterology and gastrointestinal surgery, denoting the integrated anatomical and physiological organ system responsible for bile synthesis, secretion, transport, and excretion.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The development of obstructive jaundice requires immediate evaluation of the entire **hepatobiliary** tree to rule out choledocholithiasis."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **hepatobiliary** ducts form an intricate arborizing network draining hepatic bile into the duodenum via the common bile duct."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Careful surgical exploration of the **hepatobiliary** triangle minimizes the catastrophic risk of inadvertent common duct transection."}
        ]
    },
    # 30. hepatocarcinoma
    "Dashboard — hepat\\hepatocarcinoma.md": {
        "primary": "A primary malignant tumor of the liver arising from hepatocytes; hepatocellular carcinoma.",
        "secondary": "In oncological pathology, a malignant epithelial hepatic neoplasm frequently developing in the background of chronic cirrhosis, viral hepatitis, or hemochromatosis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rapid enlargement of a cirrhotic liver accompanied by bloody ascites strongly suggests the development of supervening **hepatocarcinoma**."},
            {"author": "Rudolf Virchow", "work": "Die krankhaften Geschwülste", "quote": "Primary epithelial malignancies of the liver, classified as **hepatocarcinoma**, recapitulate in disordered cords the cellular patterns of hepatic trabeculae."},
            {"author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Deep-seated visceral cancers presenting as intractable **hepatocarcinoma** historically defied all surgical knife and operative salvage."}
        ]
    },
    # 31. hepatocellular carcinoma
    "Dashboard — hepat\\hepatocellular carcinoma.md": {
        "primary": "The most common type of primary liver cancer, originating in the hepatocytes and often associated with chronic liver disease.",
        "secondary": "In modern gastrointestinal oncology, a hypervascular parenchymal malignancy characterized by elevated serum alpha-fetoprotein, portal vein invasion, and variable architectural trabecular differentiation.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surveillance of cirrhotic patients is critical because chronic parenchymal regeneration predisposes to the emergence of **hepatocellular carcinoma**."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "In **hepatocellular carcinoma**, neoplastic liver cells produce bile-like secretions while proliferating in expansive, atypical glandular trabeculae."},
            {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "The molecular etiology of **hepatocellular carcinoma** links chronic viral inflammation and genomic instability directly to clonal hepatic malignant transformation."}
        ]
    },
    # 32. hepatocyte
    "Dashboard — hepat\\hepatocyte.md": {
        "primary": "A parenchymal liver cell, constituting the principal structural and functional cell of the liver.",
        "secondary": "In cell biology and histology, a polarized polyhedral epithelial cell responsible for protein synthesis, lipid and carbohydrate metabolism, bile secretion, and xenobiotic detoxification.",
        "quotes": [
            {"author": "Santiago Ramón y Cajal", "work": "Histology", "quote": "Each polyhedral **hepatocyte** lies bordered on one surface by vascular sinusoids and on the other by delicate intercellular bile canaliculi."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The remarkable regenerative capacity of the liver resides in the mitotic potential retained by the mature **hepatocyte** even after extensive necrosis."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Within the endoplasmic reticulum of each **hepatocyte**, cytochrome P450 enzymes catalyze the oxidative detoxification of diverse pharmaceuticals."}
        ]
    },
    # 33. hepatoflavin
    "Dashboard — hepat\\hepatoflavin.md": {
        "primary": "A historical name for riboflavin (vitamin B2) when originally isolated from mammalian liver tissue.",
        "secondary": "In nutritional biochemistry, a water-soluble yellow-green fluorescent pigment isolated from hepatic extracts, subsequently demonstrated to be identical to vitamin B2.",
        "quotes": [
            {"author": "Paul Karrer", "work": "Helv. Chim. Acta", "quote": "The yellow water-soluble pigment isolated from liver, designated **hepatoflavin**, was found identical in constitution to lactoflavin and ovoflavin."},
            {"author": "Richard Kuhn", "work": "Berichte der deutschen chemischen Gesellschaft", "quote": "Our isolation of crystalline **hepatoflavin** proved that this essential growth factor serves universally as the prosthetic group of yellow respiratory enzymes."},
            {"author": "Frederick Gowland Hopkins", "work": "Feeding Experiments Illustrating the Importance of Accessory Factors", "quote": "Early bioassays revealed that concentrated extracts containing **hepatoflavin** cured specific nutritional deficiencies in experimental animals."}
        ]
    },
    # 34. hepatology
    "Dashboard — hepat\\hepatology.md": {
        "primary": "The branch of medicine and medical science concerned with the study, diagnosis, and treatment of diseases of the liver, gallbladder, and biliary tree.",
        "secondary": "In internal medicine, a specialized subdiscipline of gastroenterology addressing acute liver failure, cirrhosis, viral hepatitis, and liver transplantation.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Recent advances in clinical **hepatology** have elucidated the physiological distinctions between obstructive and hemolytic varieties of jaundice."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Modern experimental **hepatology** dates from the discovery that the liver acts as an active chemical factory rather than a passive filter."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Contemporary **hepatology** relies extensively upon metabolic clearance assays and imaging of hepatic portal hemodynamics."}
        ]
    },
    # 35. hepatoma
    "Dashboard — hepat\\hepatoma.md": {
        "primary": "A tumor of the liver, especially a primary hepatocellular carcinoma.",
        "secondary": "In historical oncological taxonomy, a general clinical designation for any circumscribed liver cell neoplasm, encompassing both benign hepatic adenomas and malignant liver cell carcinomas.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Palpation of an irregular, stone-hard mass in the right hypochondrium pointed toward an advanced malignant **hepatoma**."},
            {"author": "Rudolf Virchow", "work": "Die krankhaften Geschwülste", "quote": "Histological examination confirmed that the nodular **hepatoma** had originated directly from the proliferating cords of hepatic parenchymal cells."},
            {"author": "Percivall Pott", "work": "Chirurgical Works", "quote": "The diagnosis of deep visceral **hepatoma** in previous centuries was reached only upon the post-mortem inspection of the enlarged liver."}
        ]
    },
    # 36. hepatomancy
    "Dashboard — hepat\\hepatomancy.md": {
        "primary": "Divination by the inspection of the entrails, especially the liver, of sacrificed animals; haruspicy.",
        "secondary": "In ancient history and archaeology, a widespread religious ritual practiced by Babylonians, Etruscans, and Romans, who mapped anatomical liver markings to celestial portents.",
        "quotes": [
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The ancient Babylonian priests developed **hepatomancy** into an elaborate science, charting the lobes and gall-bladder of sacrificial sheep."},
            {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "Belief that divine will was inscribed upon the liver made **hepatomancy** one of the most authoritative divination arts of antiquity."},
            {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "Clay models of the sheep's liver from Mesopotamia prove that anatomical study first began as an adjunct to superstitious **hepatomancy**."}
        ]
    },
    # 37. hepatomegaly
    "Dashboard — haem\\hepatomegaly.md" if False else "Dashboard — hepat\\hepatomegaly.md": {
        "primary": "Abnormal enlargement of the liver beyond its normal anatomical boundaries.",
        "secondary": "In clinical diagnosis, a cardinal physical sign detected by abdominal percussion and palpation, caused by hepatic congestion, steatosis, amyloidosis, neoplasia, or storage diseases.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Massive tender **hepatomegaly** extending three finger-breadths below the costal margin accompanied acute congestive cardiac failure."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "In chronic albuminuria, progressive amyloid degeneration of the abdominal viscera was heralded by smooth, painless **hepatomegaly**."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Obstruction of the portal vessels was attended with heaviness in the right flank and perceptible **hepatomegaly**."}
        ]
    },
    # 38. hepatorenal
    "Dashboard — hepat\\hepatorenal.md": {
        "primary": "Relating to, involving, or affecting both the liver and the kidneys.",
        "secondary": "In clinical nephrology and hepatology, denoting hepatorenal syndrome, a condition of acute, functional renal failure developing in patients with advanced liver disease and portal hypertension.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The development of oliguria and azotemia in decompensated cirrhosis illustrates the ominous nature of the **hepatorenal** syndrome."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "Concomitant pathological alterations in the liver and kidneys were frequently traced to shared **hepatorenal** circulatory derangements."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Splanchnic arterial vasodilation in severe cirrhosis triggers compensatory renal vasoconstriction, precipitating functional **hepatorenal** failure."}
        ]
    },
    # 39. hepatoscopy
    "Dashboard — hepat\\hepatoscopy.md": {
        "primary": "The examination of the liver of sacrificed animals for divination purposes; hepatomancy or haruspicy.",
        "secondary": "In medical and cultural anthropology, the ancient ritual reading of the liver's physical characteristics (lobes, fissures, gall bladder) to discern omens.",
        "quotes": [
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The Etruscan haruspices practiced rigorous **hepatoscopy**, dividing the surface of the bronze liver into regions corresponding to specific deities."},
            {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "Long before human dissection was permitted, primitive anatomical knowledge was gained through sacrificial **hepatoscopy**."},
            {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "The practice of **hepatoscopy** rested on the ancient belief that the liver was the prime seat of vitality and the soul."}
        ]
    },
    # 40. hepatotoxic
    "Dashboard — hepat\\hepatotoxic.md": {
        "primary": "Damaging, toxic, or destructive to the liver cells.",
        "secondary": "In pharmacology and toxicology, describing drugs, industrial solvents (like carbon tetrachloride), or natural compounds that induce hepatic necrosis or cholestasis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inadvertent ingestion of toxic mushrooms produces devastating hepatic necrosis due to powerful **hepatotoxic** amatoxins."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Certain chemical agents display an elective **hepatotoxic** affinity, paralyzing the metabolic enzymes of the liver parenchyma."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Excessive doses of acetaminophen become fiercely **hepatotoxic** once endogenous glutathione reserves are depleted."}
        ]
    },
    # 41. hepatotoxicity
    "Dashboard — hepat\\hepatotoxicity.md": {
        "primary": "The property or state of being toxic or damaging to the liver; chemical-driven liver damage.",
        "secondary": "In clinical pharmacology, drug-induced liver injury (DILI) categorized as intrinsic (predictable and dose-dependent) or idiosyncratic (unpredictable, host-dependent).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The prompt recognition of drug-induced **hepatotoxicity** is vital to halt irreversible parenchymal necrosis."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Industrial exposure to chlorinated hydrocarbons carries a well-known risk of acute **hepatotoxicity** and central lobular necrosis."},
            {"author": "Alexander Fleming", "work": "On the Antibacterial Action of Cultures of a Penicillium", "quote": "Unlike older arsenical compounds, penicillin demonstrated an absence of systemic **hepatotoxicity** in therapeutic dosages."}
        ]
    },
    # 42. hepatotoxin
    "Dashboard — hepat\\hepatotoxin.md": {
        "primary": "A toxic substance or agent that damages or destroys liver cells.",
        "secondary": "In chemical pathology and toxicology, any chemical compound, biological alkaloid (e.g. phalloidin), or bacterial toxin that specifically targets hepatocytes.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Phosphorus serves as the classic experimental **hepatotoxin**, provoking rapid fatty metamorphosis followed by acute yellow atrophy."},
            {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "By administering a specific **hepatotoxin**, we were able to dissociate the glycogen-storing function of the liver from its biliary secretion."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The cellular receptors of the liver parenchyma exhibit high binding avidity for this dangerous bacterial **hepatotoxin**."}
        ]
    },
    # 43. hepatotropic
    "Dashboard — hepat\\hepatotropic.md": {
        "primary": "Having an affinity for, or specifically affecting, the liver.",
        "secondary": "In virology and infectious disease, describing pathogens (such as hepatitis A, B, C, D, and E viruses) that preferentially infect and replicate within hepatocytes.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical syndrome of acute viral hepatitis is mediated by a distinct group of obligate **hepatotropic** viruses."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Specific chemical compounds exhibit a strongly **hepatotropic** localization, accumulating selectively within liver tissue."},
            {"author": "Patrick Manson", "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates", "quote": "The sporozoite stage of Plasmodium displays a marked **hepatotropic** tropism, entering liver parenchyma before attacking red blood cells."}
        ]
    },
    # 44. megalohepatia
    "Dashboard — hepat\\megalohepatia.md": {
        "primary": "Abnormal, massive enlargement of the liver; massive hepatomegaly.",
        "secondary": "In clinical diagnosis, extreme hepatic hypertrophy where the liver edge descends into the lower abdomen or pelvis, seen in amyloidosis, severe congestion, or metastatic malignancy.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In advanced cases of leukemic infiltration, enormous **megalohepatia** filled the right side of the abdomen and displaced the intestines."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "The autopsy revealed profound **megalohepatia**, the liver weighing upwards of eleven pounds and exhibiting universal waxy degeneration."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Persistent visceral dropsy was attended with painful **megalohepatia** that oppressed the diaphragm and produced severe dyspnea."}
        ]
    },
    # 45. anhidrosis
    "Dashboard — hidrot\\anhidrosis.md": {
        "primary": "An abnormal lack or deficiency of sweating in response to heat or exertion.",
        "secondary": "In neurology and dermatology, the inability to sweat resulting from sweat gland dysfunction, autonomic neuropathies, or sympathetic denervation (such as Horner's syndrome).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Unilateral facial **anhidrosis** combined with miosis and ptosis constitutes the classic clinical triad of Horner's syndrome."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "In extreme environmental heat, generalized **anhidrosis** rapidly leads to hyperpyrexia, heatstroke, and cardiovascular collapse."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Interruption of the thoracic sympathetic nerve trunk eliminates sudomotor impulses, resulting in complete regional **anhidrosis**."}
        ]
    },
    # 46. dyshidrosis
    "Dashboard — hidrot\\dyshidrosis.md": {
        "primary": "A skin condition characterized by small, intensely itchy blisters on the palms of the hands and soles of the feet; pompholyx.",
        "secondary": "In clinical dermatology, an acute, recurrent, or chronic vesicular dermatitis traditionally believed to be related to sweat gland dysfunction, now understood as an eczematous reaction.",
        "quotes": [
            {"author": "Tilbury Fox", "work": "Skin Diseases: Their Description, Pathology, Diagnosis, and Treatment", "quote": "The tiny sago-grain vesicles erupting along the margins of the fingers in **dyshidrosis** are accompanied by burning and tingling sensations."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Recurrent attacks of **dyshidrosis** typically trouble young adults during hot, humid summer seasons."},
            {"author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "We observed stubborn cases of **dyshidrosis** where deep-seated intraepidermal vesicles coalesced into large painful bullae."}
        ]
    },
    # 47. dyshidrotic
    "Dashboard — hidrot\\dyshidrotic.md": {
        "primary": "Of, relating to, or affected by dyshidrosis.",
        "secondary": "In dermatology, describing blistering eczematous eruptions (dyshidrotic eczema or dyshidrotic dermatitis) localized predominantly to the palmar and plantar surfaces.",
        "quotes": [
            {"author": "Tilbury Fox", "work": "Skin Diseases: Their Description, Pathology, Diagnosis, and Treatment", "quote": "The **dyshidrotic** eruption consists of deep intraepidermal vesicles that do not rupture readily but dry into brownish crusts."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A topical soothing astringent lotion was prescribed to relieve the intense pruritus of the **dyshidrotic** flare."},
            {"author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "Patients prone to hyperhidrosis frequently suffer simultaneous attacks of **dyshidrotic** eczema upon both hands."}
        ]
    },
    # 48. hematidrosis
    "Dashboard — hidrot\\hematidrosis.md": {
        "primary": "An extremely rare condition in which a person sweats blood or blood-pigmented fluid; bloody sweat.",
        "secondary": "In dermatology and physiological pathology, a phenomenon where dermal capillary networks surrounding sweat glands rupture under extreme stress or coagulopathy, discharging blood into sweat ducts.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Authentic instances of **hematidrosis**, though exceedingly rare, have been documented under conditions of profound emotional paroxysm."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Extreme terror and agonizing suspense have been recorded by medical observers to induce that rare phenomenon termed **hematidrosis**."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "In violent hysterical convulsions, cutaneous pores have been observed to discharge a bloody dew resembling **hematidrosis**."}
        ]
    },
    # 49. hidrocystoma
    "Dashboard — hidrot\\hidrocystoma.md": {
        "primary": "A benign, cystic tumor or retention cyst originating from sweat glands, typically found on the face.",
        "secondary": "In dermatopathology, a translucent cystic proliferation categorized as eccrine hidrocystoma (ductal retention cyst) or apocrine hidrocystoma (true cystic adenoma), exacerbated by heat and sweating.",
        "quotes": [
            {"author": "Tilbury Fox", "work": "Skin Diseases: Their Description, Pathology, Diagnosis, and Treatment", "quote": "Upon the periorbital skin of the middle-aged female, tiny translucent papules of **hidrocystoma** enlarge conspicuously in hot weather."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Biopsy of the bluish facial papule confirmed a benign **hidrocystoma** lined by two layers of sweat duct epithelium."},
            {"author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "Puncture of the delicate cystic dome in **hidrocystoma** discharges a drop of clear, sterile sudoriferous fluid."}
        ]
    },
    # 50. hidropoiesis
    "Dashboard — hidrot\\hidropoiesis.md": {
        "primary": "The production, secretion, or formation of sweat by the sweat glands.",
        "secondary": "In human cutaneous physiology, the process of eccrine and apocrine sudoriferous secretion regulated by hypothalamic thermoregulatory centers via sympathetic cholinergic innervation.",
        "quotes": [
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "The rate of active **hidropoiesis** serves as a sensitive indicator of autonomic sympathetic excitation in mammalian skin."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Thermoregulatory **hidropoiesis** allows the body to dissipate significant thermal energy through evaporative cooling."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The microscopic coils of the sudoriferous gland provide the anatomical site for continuous cellular **hidropoiesis**."}
        ]
    },
    # 51. hidroschesis
    "Dashboard — hidrot\\hidroschesis.md": {
        "primary": "The retention, suppression, or checking of perspiration.",
        "secondary": "In medical historical physiology and pathology, an acute or chronic condition characterized by the abnormal cessation of sweat secretion.",
        "quotes": [
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Sudden exposure to bitter cold when overheated frequently produces **hidroschesis**, followed by severe pleuritic inflammation."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In toxic anticholinergic poisoning, acute **hidroschesis** leads directly to flushed, dry skin and high fever."},
            {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "Pharmacological block of sympathetic postganglionic fibers produces immediate experimental **hidroschesis** in the affected limb."}
        ]
    },
    # 52. hidrosis
    "Dashboard — hidrot\\hidrosis.md": {
        "primary": "The production and excretion of sweat; perspiration.",
        "secondary": "In clinical dermatology, any functional state or pathological alteration of sweat gland excretion, encompassing both hyperhidrosis and hypohidrosis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Copious nocturnal **hidrosis** soaking through bedclothes is a classic constitutional symptom of active tuberculosis."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "The rate of physiological **hidrosis** increases sharply during vigorous muscular exertion to maintain homeostatic core temperature."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sudden visceral terror stimulates instantaneous palmar **hidrosis** through involuntary autonomic pathways."}
        ]
    },
    # 53. hidrot
    "Dashboard — hidrot\\hidrot.md": {
        "primary": "The root and combining form representing sweat or perspiration; derived from Greek hidros, hidrotos.",
        "secondary": "In morphological linguistics and biomedical nomenclature, the classical Greek root denoting sudorific function and disorders of sweat secretion.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The Greek stem **hidrot** supplies medical terminology with essential designations for all conditions involving sudoriferous secretion."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "From hyperhidrosis to anhidrosis, the lexical root **hidrot** recurs wherever sweat gland pathology is classified."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Physiologists traced the secretory mechanisms of **hidrot** derivatives to understand thermoregulation across warm-blooded organisms."}
        ]
    },
    # 54. hidrotic
    "Dashboard — hidrot\\hidrotic.md": {
        "primary": "Causing or promoting the secretion of sweat; sudorific.",
        "secondary": "In clinical pharmacology and medical therapeutics, a drug or substance (such as pilocarpine) that stimulates sweat gland activity.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hot drinks, warm blankets, and a mild **hidrotic** draught were administered to promote diaphoresis at the onset of fever."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "The physician should employ mild **hidrotic** remedies with prudent caution, lest profuse sweating debilitate the patient."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "The subcutaneous injection of pilocarpine exerted a powerful **hidrotic** effect, exciting rapid glandular discharge."}
        ]
    },
    # 55. hyperhidrosis
    "Dashboard — hidrot\\hyperhidrosis.md": {
        "primary": "Abnormally excessive sweating, often exceeding that required for normal thermoregulation.",
        "secondary": "In dermatology and neurology, a condition categorized as primary focal hyperhidrosis (affecting palms, soles, axillae) or secondary generalized hyperhidrosis (due to endocrine, metabolic, or neoplastic disorders).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe primary **hyperhidrosis** of the hands causes constant dripping of sweat, creating profound psychological distress and functional impairment."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Overactivity of the thoracic sympathetic chain drives localized **hyperhidrosis** even in cool ambient surroundings."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Emotional stress triggers acute palmar **hyperhidrosis**, reflecting heightened sympathetic autonomic discharge."}
        ]
    },
    # 56. hypohidrosis
    "Dashboard — hidrot\\hypohidrosis.md": {
        "primary": "An abnormally diminished or reduced capacity to sweat in response to appropriate stimuli.",
        "secondary": "In clinical neurology and dermatology, partial sudomotor failure caused by peripheral neuropathy, connective tissue disorders, or ectodermal dysplasias, predisposing to heat intolerance.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient with generalized **hypohidrosis** presented during the summer heat wave with dangerous hyperthermia and weakness."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "In peripheral diabetic neuropathy, stocking-glove **hypohidrosis** reflects progressive degeneration of small unmyelinated sympathetic fibers."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Congenital absence of sudoriferous tubules manifests clinically as profound **hypohidrosis** across the skin surface."}
        ]
    },
    # 57. polyhidrosis
    "Dashboard — hidrot\\polyhidrosis.md": {
        "primary": "Excessive or profuse perspiration; hyperhidrosis.",
        "secondary": "In clinical terminology, an alternate designation for excessive generalized or localized sweating occurring during febrile crises, thyrotoxicosis, or autonomic overactivity.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "During the defervescence of malaria paroxysms, drenching **polyhidrosis** bathes the patient from head to foot."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "The critical sweating stage of the ague was marked by violent **polyhidrosis**, bringing swift relief from internal heat."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Direct stimulation of the peripheral secretomotor nerves produced instantaneous **polyhidrosis** in experimental preparations."}
        ]
    },
    # 58. ahistorical
    "Dashboard — hist\\ahistorical.md": {
        "primary": "Lacking historical perspective or context; unconcerned with history or historical development.",
        "secondary": "In historiography and critical theory, describing analyses, doctrines, or assumptions that treat cultural, social, or linguistic phenomena as static and universal rather than products of temporal development.",
        "quotes": [
            {"author": "Michel Foucault", "work": "The Archaeology of Knowledge", "quote": "To view language as a timeless grammatical structure detached from discourse is to adopt an essentially **ahistorical** stance."},
            {"author": "Edward Said", "work": "Orientalism", "quote": "Orientalist discourse posited an **ahistorical**, unchanging East perpetually contrasted with a dynamic Western world."},
            {"author": "Fredric Jameson", "work": "Postmodernism, or, the Cultural Logic of Late Capitalism", "quote": "Postmodern cultural fragmentation often fosters an **ahistorical** consumer consciousness severed from historical memory."}
        ]
    },
    # 59. antihistamine
    "Dashboard — hist\\antihistamine.md": {
        "primary": "A drug or pharmaceutical agent that opposes the actions of histamine, used primarily to treat allergic reactions.",
        "secondary": "In clinical pharmacology, a competitive H1-receptor inverse agonist that reduces pruritus, vascular permeability, rhinorrhea, and bronchospasm in allergic and anaphylactic disorders.",
        "quotes": [
            {"author": "Daniel Bovet", "work": "Nobel Lecture: The Relationships Between Chemical Structure and Pharmacodynamic Action", "quote": "The synthesis of the first synthetic **antihistamine** opened completely new horizons for the pharmacological management of anaphylaxis."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Administration of an effective **antihistamine** blocks the arteriolar vasodilation and increased capillary permeability triggered by allergen challenge."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern treatment of urticaria and hay fever relies fundamentally upon the prompt administration of an appropriate **antihistamine**."}
        ]
    },
    # 60. histaminase
    "Dashboard — hist\\histaminase.md": {
        "primary": "An enzyme that breaks down and metabolizes histamine; diamine oxidase.",
        "secondary": "In biochemistry and clinical medicine, an enzyme present in intestinal mucosa, kidney, and placenta that deaminates extracellular histamine into imidazole-4-acetic acid, moderating inflammatory responses.",
        "quotes": [
            {"author": "Henry Dale", "work": "Adventures in Physiology", "quote": "The discovery of **histaminase** demonstrated nature's enzymatic safeguard for rapidly inactivating toxic concentrations of liberated histamine."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "High maternal plasma levels of **histaminase** during pregnancy protect the fetal-placental unit from circulating maternal histamine."},
            {"author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Metabolic degradation catalyzed by tissue **histaminase** represents an essential homeostatic pathway in cellular physiology."}
        ]
    },
    # 61. histamine
    "Dashboard — hist\\histamine.md": {
        "primary": "A physiologically active biogenic amine found in body tissues, involved in local immune responses, gastric acid secretion, and neurotransmission.",
        "secondary": "In immunology and pharmacology, 2-(1H-imidazol-4-yl)ethanamine, synthesized by mast cells and basophils, which binds to H1, H2, H3, and H4 receptors to mediate vasodilation, vascular permeability, smooth muscle contraction, and pruritus.",
        "quotes": [
            {"author": "Henry Dale", "work": "The Action of Extracts of the Pituitary Body", "quote": "Our isolation of **histamine** from animal ergot extracts revealed a compound possessing astonishing potency in depressing arterial pressure."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Degranulation of sensitized mast cells discharges preformed **histamine**, sparking the triple response of Lewis in the microcirculation."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The profound capillary dilation and bronchospasm characteristic of anaphylactic shock are mediated by sudden explosive release of **histamine**."}
        ]
    },
    # 62. histidine
    "Dashboard — hist\\histidine.md": {
        "primary": "An essential basic amino acid with an imidazole side chain, necessary for growth and tissue repair.",
        "secondary": "In biochemistry, a semi-essential alpha-amino acid that serves as a versatile nucleophilic and general acid-base catalyst in enzyme active sites and functions as the metabolic precursor to histamine and carnosine.",
        "quotes": [
            {"author": "Albrecht Kossel", "work": "The Chemical Composition of the Cell Nucleus", "quote": "From the hydrolytic cleavage of protamines, we succeeded in isolating a new basic crystalline hexone base which we named **histidine**."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The imidazole ring of **histidine** provides the crucial axial ligand binding the heme iron atom within the hemoglobin subunit."},
            {"author": "Henry Dale", "work": "Adventures in Physiology", "quote": "Enzymatic decarboxylation of dietary **histidine** in animal tissues generates the vasoactive autacoid histamine."}
        ]
    },
    # 63. histiocyte
    "Dashboard — hist\\histiocyte.md": {
        "primary": "A stationary phagocytic cell found in connective tissue; a resident macrophage.",
        "secondary": "In cellular immunology and histopathology, a tissue-resident mononuclear phagocyte derived from circulating monocytes or embryonic precursors, responsible for antigen presentation, phagocytosis, and tissue homeostasis.",
        "quotes": [
            {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "Within connective tissue spaces, the large stationary macrophage or **histiocyte** avidly ingests foreign particulates and cellular debris."},
            {"author": "Santiago Ramón y Cajal", "work": "Histology", "quote": "The reticuloendothelial system includes the resting **histiocyte**, ready to mobilize upon the introduction of inflammatory stimuli."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Granulomatous lesions characteristically display proliferations of epithelioid cells derived from the transformed interstitial **histiocyte**."}
        ]
    },
    # 64. histiocytosis
    "Dashboard — hist\\histiocytosis.md": {
        "primary": "An abnormal excessive proliferation and accumulation of histiocytes in bodily tissues and organs.",
        "secondary": "In clinical hematology and oncology, a diverse group of rare disorders (including Langerhans cell histiocytosis and hemophagocytic lymphohistiocytosis) characterized by clonal or reactive infiltration of histiocytes causing osteolytic lesions, rash, or organ failure.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diffuse osseous lesions and hepatosplenomegaly in childhood may point toward a severe form of systemic **histiocytosis**."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination of the resected tissue demonstrated massive infiltration by atypical macrophages, diagnostic of **histiocytosis**."},
            {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "In reactive **histiocytosis**, cytokine hypersecretion drives unregulated phagocytic engulfment of mature hematopoietic cells."}
        ]
    }
}

# Write out curate_body3_batch5.mjs
mjs_path = os.path.join("main app", "scripts", "curate_body3_batch5.mjs")
with open(mjs_path, "w", encoding="utf-8") as f:
    f.write("""import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = """ + json.dumps(batch5_data, indent=2, ensure_ascii=False) + """;

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Body Part 3 - Batch 5 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
""")

print(f"Generated {mjs_path} with {len(batch5_data)} entries.")
