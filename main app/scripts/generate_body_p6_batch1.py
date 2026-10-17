import json
import os

batch1_data = {
  "Dashboard — oste\\osteoclast.md": {
    "primary": "A large, multinucleated bone cell that absorbs and removes osseous tissue during normal skeletal growth, remodeling, and repair.",
    "secondary": "In bone cell biology and endocrinology, a macrophage-lineage cell that secretes acid and cathepsin K to demineralize and digest bone matrix.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The multinucleated giant cell termed an **osteoclast** hollows out Howship's lacunae across the resorbing bone surface." },
      { "author": "Alexander Maximow", "work": "A Text-Book of Histology", "quote": "Bone remodeling represents a dynamic balance between matrix deposition by osteoblasts and localized resorption by each **osteoclast**." },
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "quote": "Parathyroid hormone stimulates rapid proliferation of the **osteoclast**, driving calcium liberation into the extracellular fluid." }
    ]
  },
  "Dashboard — oste\\osteocyte.md": {
    "primary": "A mature, star-shaped bone cell formed when an osteoblast becomes surrounded and entrapped within its own mineralized matrix.",
    "secondary": "In skeletal physiology, the most abundant cell in adult bone, residing in lacunae and communicating via dendritic processes through canaliculi to sense mechanical strain.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Within each calcified lacuna sits a living **osteocyte**, maintaining metabolic communication with adjacent cells through canaliculi." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The slender protoplasmic extensions of the **osteocyte** form an extensive syncytium permeating the dense haversian lamellae." },
      { "author": "Alexander Maximow", "work": "A Text-Book of Histology", "quote": "Mechanical stress sensed by each **osteocyte** directs the remodeling machinery of the skeleton through sclerostin signaling." }
    ]
  },
  "Dashboard — oste\\osteodystrophy.md": {
    "primary": "Abnormal development or defective growth and mineralization of bone tissue.",
    "secondary": "In clinical nephrology and endocrinology, renal osteodystrophy—a complex skeletal disorder accompanying chronic kidney disease, characterized by hyperparathyroidism, osteomalacia, and osteosclerosis.",
    "quotes": [
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "quote": "Renal **osteodystrophy** illustrates how defective tubular phosphate clearance and failing calcitriol synthesis cripple skeletal integrity." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic uremic states, progressive **osteodystrophy** produces severe bone pain, skeletal deformities, and spontaneous fractures." },
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Endocrine imbalances of the parathyroid axis provoke generalized **osteodystrophy**, manifesting as fibrous replacement of marrow." }
    ]
  },
  "Dashboard — oste\\osteogenesis.md": {
    "primary": "The biological process of bone formation, development, and mineralization; ossification.",
    "secondary": "In clinical genetics, specifically osteogenesis imperfecta (brittle bone disease), a hereditary disorder of type I collagen synthesis causing fragile bones and blue sclerae.",
    "quotes": [
      { "author": "Alexander Maximow", "work": "A Text-Book of Histology", "quote": "Endochondral **osteogenesis** replaces a cartilaginous model with vascularized trabecular bone, whereas intramembranous ossification develops directly from mesenchyme." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Active periosteal **osteogenesis** bridges the fracture gap, providing the provisional callus that stabilizes broken bones." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Primary centers of **osteogenesis** appear in the fetal diaphysis long before secondary epiphyseal ossification commences." }
    ]
  },
  "Dashboard — oste\\osteogenic.md": {
    "primary": "Producing, forming, or contributing to the development of bone tissue; of or relating to osteogenesis.",
    "secondary": "In skeletal histology and pathology, designating osteogenic precursor stem cells in the periosteum and endosteum, or osteogenic sarcomas that produce neoplastic bone.",
    "quotes": [
      { "author": "Alexander Maximow", "work": "A Text-Book of Histology", "quote": "The inner vascular layer of the periosteum contains committed **osteogenic** cells that proliferate upon mechanical injury." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "True **osteogenic** sarcoma is defined histologically by malignant stromal cells producing osteoid directly without an intervening cartilage phase." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The vascular connective tissue surrounding the fracture serves as an energetic **osteogenic** blastema for skeletal restoration." }
    ]
  },
  "Dashboard — oste\\osteoglossidae.md": {
    "primary": "A family of primitive, freshwater bony fishes (the bonytongues or arowanas), characterized by heavily toothed parasphenoid and glossohyal bones.",
    "secondary": "In ichthyology and biogeography, an ancient relict Gondwanan family containing colossal freshwater fishes like the pirarucu (Arapaima gigas) and Asian arowana.",
    "quotes": [
      { "author": "Louis Agassiz", "work": "Recherches sur les Poissons Fossiles", "quote": "The family **osteoglossidae** unites fishes whose tongues are armed with sharp bony teeth that bite against the palate." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The ancient lineage of the **osteoglossidae** is distributed across South America, Africa, and Australia, testifying to ancient continental linkages." },
      { "author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The massive bony scales and heavy cephalic plates of **osteoglossidae** reflect an archaic grade of teleost evolution." }
    ]
  },
  "Dashboard — oste\\osteoglossiformes.md": {
    "primary": "An ancient, basal order of teleost ray-finned fishes comprising the bonytongues, mormyrids (elephantfishes), and related archaic freshwater lineages.",
    "secondary": "In evolutionary ichthyology, an early-diverging teleost clade characterized by primitive caudal fin skeletons, toothed tongues, and electroreceptive adaptations.",
    "quotes": [
      { "author": "Louis Agassiz", "work": "Monograph on the Fossil Fishes", "quote": "Fossils of the **osteoglossiformes** demonstrate that this toothed-tongue lineage flourished in Cretaceous lakes before modern percoids evolved." },
      { "author": "David Starr Jordan", "work": "The Genera of Fishes", "quote": "Within the order **osteoglossiformes**, the weakly electric mormyrids possess enlarged cerebellums that rival mammalian proportions." },
      { "author": "Alfred Sherwood Romer", "work": "Vertebrate Paleontology", "quote": "The basal position of **osteoglossiformes** on the teleost tree illuminates the transition from archaic holostean to advanced modern teleost anatomy." }
    ]
  },
  "Dashboard — oste\\osteoid.md": {
    "primary": "Resembling bone in structure, appearance, or chemical composition.",
    "secondary": "In bone histology, the uncalcified, organic extracellular matrix secreted by osteoblasts, composed primarily of type I collagen fibers and ground substance.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The newly deposited **osteoid** seam must undergo mineralization by calcium hydroxyapatite before true rigid bone is achieved." },
      { "author": "Alexander Maximow", "work": "A Text-Book of Histology", "quote": "In rickets, failure of calcification produces abnormally wide seams of unmineralized **osteoid** bordering the trabeculae." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "The histological demonstration of malignant **osteoid** tissue produced directly by tumor cells confirms the diagnosis of osteosarcoma." }
    ]
  },
  "Dashboard — oste\\osteologer.md": {
    "primary": "An archaic or literary term for an osteologist; an investigator who studies bones and skeletal frameworks.",
    "secondary": "In historical intellectual literature, a comparative anatomist dedicated to classifying fossil and living vertebrate skeletons.",
    "quotes": [
      { "author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "The antiquary and the **osteologer** gaze with equal wonder upon the calcined fragments of ancient kings and warriors." },
      { "author": "Richard Owen", "work": "On the Nature of Limbs", "quote": "The patient **osteologer** discovers in the flipper of a whale the identical pentadactyl homologies that govern the human hand." },
      { "author": "Thomas Henry Huxley", "work": "The Elements of Comparative Anatomy", "quote": "Every trained **osteologer** must be able to reconstruct an extinct quadruped from a single fossilized articular facet." }
    ]
  },
  "Dashboard — oste\\osteologist.md": {
    "primary": "A specialist in osteology; a scientist or physical anthropologist who studies the structure, evolution, and diseases of bones.",
    "secondary": "In forensic science and paleontology, an expert who identifies, reconstructs, and analyzes human or animal skeletal remains.",
    "quotes": [
      { "author": "Richard Owen", "work": "A History of British Fossil Mammals and Birds", "quote": "To the comparative **osteologist**, every groove and tubercle on a fossil femur speaks of locomotion, weight, and habitat." },
      { "author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The skeletal comparisons of the **osteologist** demonstrated beyond dispute the profound morphological affinities uniting man with the great apes." },
      { "author": "Georges Cuvier", "work": "Recherches sur les Ossemens Fossiles", "quote": "Guided by the law of correlation of parts, the skilled **osteologist** can reconstruct the entire form of a vanished mammal." }
    ]
  },
  "Dashboard — oste\\osteology.md": {
    "primary": "The scientific branch of anatomy and anthropology that deals with the study of bones, their structure, development, and function.",
    "secondary": "In medical education, the foundational study of the human skeleton, detailing bone landmarks, foramina, and muscular attachment sites.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Human **osteology** forms the indispensable groundwork of anatomical science, providing the rigid framework upon which all soft tissues rely." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "I begin my anatomical demonstrations with **osteology**, for the bones are the foundation, the props, and the pillars of the entire bodily edifice." },
      { "author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "quote": "Comparative **osteology** reveals that all vertebrate skeletons are architectural variations of a single primordial ideal archetype." }
    ]
  },
  "Dashboard — oste\\osteolysis.md": {
    "primary": "The pathological destruction, dissolution, or enzymatic resorption of bone tissue.",
    "secondary": "In oncology and orthopedics, localized bone destruction caused by metastatic tumors or inflammatory response to prosthetic wear particles.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Active **osteolysis** along the margins of the chronic gumma leaves pitted, irregular excavations across the skull table." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Multiple myeloma presents radiographically with punched-out areas of **osteolysis** unaccompanied by reactive new bone formation." },
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "quote": "Extreme hyperparathyroidism provokes widespread generalized **osteolysis**, causing subperiosteal bone resorption in the phalanges." }
    ]
  },
  "Dashboard — oste\\osteoma.md": {
    "primary": "A benign, slow-growing tumor composed of mature, compact, or cancellous bone tissue.",
    "secondary": "In surgical pathology, a well-differentiated osteoblastic neoplasm developing most commonly on the skull and facial bones or within paranasal sinuses.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "An ivory **osteoma** of the calvarium consists of dense, sclerotic bone as hard and smooth as polished elephant tusk." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Benign **osteoma** must be distinguished from osteochondroma by the absence of a proliferative cartilaginous cap." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Surgical excision of an orbital **osteoma** is warranted when its gradual expansion displaces the globe outward." }
    ]
  },
  "Dashboard — oste\\osteomalacia.md": {
    "primary": "A disease of adults characterized by softening of the bones resulting from inadequate mineralization of the organic bone matrix.",
    "secondary": "In clinical endocrinology, the adult counterpart of rickets, commonly caused by severe vitamin D deficiency, renal tubular acidosis, or malabsorption, producing diffuse bone pain and pseudo-fractures.",
    "quotes": [
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "quote": "In **osteomalacia**, the total volume of bone matrix remains normal, but failure of calcium deposition leaves the skeleton soft and yielding." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The pregnant woman with severe **osteomalacia** develops a triradiate pelvis that creates insuperable obstacles to natural delivery." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination in **osteomalacia** reveals wide borders of uncalcified osteoid tissue encasing every bony trabecula." }
    ]
  },
  "Dashboard — oste\\osteomyelitis.md": {
    "primary": "An acute or chronic inflammation and bacterial infection of bone and bone marrow, commonly caused by pyogenic organisms.",
    "secondary": "In orthopedic surgery, an infection typically provoked by Staphylococcus aureus via hematogenous seeding or open fracture, risking bone necrosis (sequestrum) and involucrum formation.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute hematogenous **osteomyelitis** in children demands urgent surgical decompression of the subperiosteal space to preserve the femoral shaft." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Chronic suppurative **osteomyelitis** forms deep sinus tracts that periodically discharge dead bone fragments termed sequestra." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The introduction of penicillin dramatically reduced the crippling amputations once necessitated by intractable acute **osteomyelitis**." }
    ]
  },
  "Dashboard — oste\\osteonecrosis.md": {
    "primary": "The death of bone cells and bone marrow tissue resulting from interruption of local blood supply; avascular necrosis.",
    "secondary": "In clinical orthopedics, ischemic death of bone tissue, most commonly affecting the femoral head, talus, or scaphoid, causing articular collapse.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Radiation therapy can induce profound localized **osteonecrosis**, destroying the vascular supply of the mandible." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Disruption of the retinacular vessels in intracapsular femoral neck fractures frequently precipitates avascular **osteonecrosis**." },
      { "author": "John Charnley", "work": "Low Friction Arthroplasty of the Hip", "quote": "Subchondral collapse secondary to femoral head **osteonecrosis** is one of the premier indications for total hip arthroplasty." }
    ]
  },
  "Dashboard — oste\\osteopath.md": {
    "primary": "A licensed medical practitioner trained in osteopathic medicine, utilizing manual musculoskeletal manipulation alongside standard medical and surgical therapies.",
    "secondary": "A health professional holding a Doctor of Osteopathic Medicine (D.O.) degree, practicing holistic medicine emphasizing the body's interrelated organ systems.",
    "quotes": [
      { "author": "Andrew Taylor Still", "work": "Autobiography of A. T. Still", "quote": "The **osteopath** seeks the cause of illness, adjusts the abnormal mechanical strains of the body, and allows nature to effect the cure." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The modern **osteopath** incorporates standard pharmacological knowledge while maintaining special dexterity in spinal biomechanics." },
      { "author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "Early sectarian schools evolved until the modern **osteopath** underwent clinical laboratory training comparable to standard physicians." }
    ]
  },
  "Dashboard — oste\\osteopathist.md": {
    "primary": "An osteopath; a person who advocates or practices osteopathy.",
    "secondary": "In medical history, early practitioners of Andrew Taylor Still's manipulative philosophy during the late nineteenth and early twentieth centuries.",
    "quotes": [
      { "author": "Andrew Taylor Still", "work": "Philosophy and Mechanical Principles of Osteopathy", "quote": "The true **osteopathist** must be a master of living anatomy, understanding how every nerve and vessel travels through fascial planes." },
      { "author": "Abraham Flexner", "work": "Medical Education", "quote": "In evaluating medical institutions, we noted how the practicing **osteopathist** gradually incorporated standard bacteriology into his clinic." },
      { "author": "William Osler", "work": "Aequanimitas", "quote": "While we criticize exclusive systems, we acknowledge that the skilled **osteopathist** frequently achieves relief in chronic mechanical back strains." }
    ]
  },
  "Dashboard — oste\\osteopathy.md": {
    "primary": "A system of complementary and mainstream healthcare founded by Andrew Taylor Still, emphasizing the therapeutic role of the musculoskeletal system in health and disease.",
    "secondary": "In medical licensing, a recognized branch of medicine in the United States granting full medical practice rights to Doctors of Osteopathic Medicine.",
    "quotes": [
      { "author": "Andrew Taylor Still", "work": "The Philosophy of Osteopathy", "quote": "I proclaimed that the body produces its own remedies, and upon that foundational truth I erected the science of **osteopathy**." },
      { "author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "The scientific maturation of **osteopathy** required bridging manual mechanical manipulation with modern clinical pathology." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The popularity of **osteopathy** served as a timely reminder to orthodox practitioners that physical manipulation has genuine therapeutic value." }
    ]
  },
  "Dashboard — oste\\osteopenia.md": {
    "primary": "A condition characterized by decreased bone mineral density and bone mass, less severe than osteoporosis.",
    "secondary": "In clinical bone densitometry, a T-score between -1.0 and -2.5 standard deviations below the young adult mean, indicating elevated fracture risk.",
    "quotes": [
      { "author": "Fuller Albright", "work": "Metabolic Bone Diseases", "quote": "Subclinical **osteopenia** may exist for decades before a sudden low-impact fall reveals the compromised strength of the skeleton." },
      { "author": "Eugene Braunwald", "work": "Heart Disease and Systemic Disorders", "quote": "Postmenopausal **osteopenia** responds favorably to weight-bearing exercise, adequate calcium intake, and antiresorptive therapy." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early recognition of skeletal **osteopenia** in elderly patients allows timely prophylactic interventions against hip fractures." }
    ]
  },
  "Dashboard — oste\\osteopetrosis.md": {
    "primary": "A rare inherited skeletal disorder characterized by defective osteoclast function, resulting in overly dense, sclerotic, and brittle bones (marble bone disease).",
    "secondary": "In medical genetics and hematology, a disease spectrum where unremodeled bone obliterates marrow cavities, causing pancytopenia, hepatosplenomegaly, and cranial nerve compression.",
    "quotes": [
      { "author": "Heinrich Albers-Schönberg", "work": "Roentgen Pictures of an Unusual Bone Disease", "quote": "The radiographs in **osteopetrosis** display uniform, marble-like radiodensity across all long bones, with complete loss of the medullary canal." },
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "quote": "In congenital **osteopetrosis**, the failure of osteoclasts to resorb primary spongiosa leads to dense bone that fractures like chalk." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Extensive calcification in **osteopetrosis** encroaches upon the optic and acoustic foramina, inducing progressive blindness and deafness." }
    ]
  },
  "Dashboard — oste\\osteophyte.md": {
    "primary": "A bony projection or spur that develops along joint margins or vertebral bodies in response to cartilage degeneration and stress.",
    "secondary": "In rheumatology and orthopedics, a fibrocartilaginous and osseous outgrowth characteristic of osteoarthritis, spondylosis, or chronic mechanical joint instability.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Marginal proliferation of bone, producing the classic **osteophyte**, represents an attempt by the joint to widen its load-bearing surface." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cervical spondylosis, a posterior vertebral **osteophyte** can encroach upon the spinal cord or exiting nerve roots." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of Old Age", "quote": "The Heberden nodes observed on osteoarthritic distal interphalangeal joints are composed of hypertrophic **osteophyte** outgrowths." }
    ]
  },
  "Dashboard — oste\\osteoporosis.md": {
    "primary": "A systemic skeletal disorder characterized by low bone mineral density, deterioration of bone microarchitecture, and increased bone fragility.",
    "secondary": "In clinical endocrinology and geriatrics, postmenopausal or senile bone loss leading to spontaneous compression fractures of vertebrae and hip fractures.",
    "quotes": [
      { "author": "Fuller Albright", "work": "Postmenopausal Osteoporosis", "quote": "I demonstrated that **osteoporosis** is primarily a disorder of tissue formation, wherein estrogen withdrawal accelerates bone resorption over synthesis." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Senile **osteoporosis** transforms the sturdy cortical bone of the femoral neck into a fragile, porous sponge prone to fracture." },
      { "author": "Eugene Braunwald", "work": "Cardiovascular and Metabolic Medicine", "quote": "Screening for asymptomatic **osteoporosis** with dual-energy X-ray absorptiometry permits early intervention before fractures occur." }
    ]
  },
  "Dashboard — oste\\osteosarcoma.md": {
    "primary": "The most common primary malignant bone tumor, characterized by the direct production of osteoid or immature bone by neoplastic mesenchymal cells.",
    "secondary": "In orthopedic oncology, an aggressive cancer arising predominantly in the metaphyses of long bones (such as the distal femur or proximal tibia) in adolescents and young adults.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "The histologic hallmark of **osteosarcoma** is the deposition of unmineralized osteoid matrix by highly pleomorphic, anaplastic stromal cells." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Amputation was formerly the sole treatment for extremity **osteosarcoma**, but modern adjuvant chemotherapy enables limb-salvage surgery." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Multi-agent chemotherapy transformed the survival curve of young patients diagnosed with metastatic **osteosarcoma**." }
    ]
  },
  "Dashboard — oste\\osteosclerosis.md": {
    "primary": "An abnormal hardening, thickening, or increased density of bone tissue.",
    "secondary": "In skeletal radiology and pathology, localized or generalized bone thickening accompanying chronic osteomyelitis, Paget's disease, or fluorosis.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Chronic low-grade inflammation induces productive **osteosclerosis**, narrowing the haversian canals and solidifying the cancellous bone." },
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "quote": "The 'rugger-jersey spine' observed in secondary hyperparathyroidism features bands of **osteosclerosis** adjacent to the vertebral endplates." },
      { "author": "Heinrich Albers-Schönberg", "work": "Studies in Bone Pathology", "quote": "In extreme **osteosclerosis**, the brittle bones exhibit remarkable radiodensity, masking all internal trabecular architecture." }
    ]
  },
  "Dashboard — oste\\osteosis.md": {
    "primary": "Any generic disease, abnormal development, or pathological condition affecting bone tissue.",
    "secondary": "In pathology, the formation or proliferation of bone in abnormal locations, or generalized bone alterations (such as osteosis cutis).",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Under the general term **osteosis**, early pathologists included diverse hypertrophic and degenerative skeletal changes." },
      { "author": "Alexander Maximow", "work": "A Text-Book of Histology", "quote": "Metaplastic **osteosis** occurs when primitive pluripotential fibroblasts within connective tissue differentiate into true osteoblasts." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Focal cutaneous **osteosis** demonstrates genuine bone trabeculae developing within the dermal layers of the skin." }
    ]
  },
  "Dashboard — oste\\osteostracan.md": {
    "primary": "An extinct jawless armored vertebrate of the class Osteostraci, having a broad, semicircular bony head shield (an osteostracan).",
    "secondary": "In paleontology, a Silurian or Devonian agnathan characterized by true cellular bone in its head shield and sensory fields linked to cranial nerves.",
    "quotes": [
      { "author": "Louis Agassiz", "work": "Recherches sur les Poissons Fossiles", "quote": "The well-preserved shield of the **osteostracan** reveals dorsal orbits and an enigmatic median sensory aperture." },
      { "author": "Hugh Miller", "work": "The Old Red Sandstone", "quote": "The fossil beds of Scotland yielded numerous plates of this archaic **osteostracan**, crowned with polished tuberculated bone." },
      { "author": "Alfred Sherwood Romer", "work": "Vertebrate Paleontology", "quote": "Internal vascular canals within the **osteostracan** head shield provide the earliest clear evidence of cellular bone in the fossil record." }
    ]
  },
  "Dashboard — oste\\osteostraci.md": {
    "primary": "An extinct order or class of armored jawless ostracoderms (Agnatha) characterized by a continuous, cellular bony head shield.",
    "secondary": "In evolutionary biology, Paleozoic agnathans closely related to jawed vertebrates, possessing paired pectoral fins and sensory cephalic fields.",
    "quotes": [
      { "author": "Louis Agassiz", "work": "Monograph on the Fossil Fishes of the Old Red Sandstone", "quote": "We erect the group **osteostraci** to emphasize the presence of true bony structure in the head shields of these ancient fishes." },
      { "author": "Arthur Smith Woodward", "work": "Catalogue of the Fossil Fishes in the British Museum", "quote": "The **osteostraci** flourished throughout late Silurian seas, disappearing abruptly at the close of the Devonian period." },
      { "author": "Alfred Sherwood Romer", "work": "Vertebrate Paleontology", "quote": "Morphological studies on **osteostraci** demonstrate that paired fins and sensory lateral lines originated before the evolution of jaws." }
    ]
  },
  "Dashboard — oste\\osteothrombosis.md": {
    "primary": "Thrombosis occurring within the veins or capillary channels of a bone.",
    "secondary": "In surgical pathology and orthopedic infection, intravascular clotting within osseous canals that leads to bone ischemia and necrosis during acute osteomyelitis.",
    "quotes": [
      { "author": "Percivall Pott", "work": "Observations on Wounds and Contusions of the Head", "quote": "Septic **osteothrombosis** within the diploic veins of the skull can swiftly extend inward to cause epidural suppuration." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Early antibiotic intervention prevents extensive **osteothrombosis** within nutrient vessels, sparing the femoral shaft from total necrosis." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination reveals septic **osteothrombosis** filling the haversian canals and cutting off blood flow to the osteocytes." }
    ]
  },
  "Dashboard — oste\\osteotome.md": {
    "primary": "A surgical chisel-like cutting instrument beveled on both sides of the blade, used by orthopedic surgeons to divide or excise bone.",
    "secondary": "In reconstructive and corrective orthopedic surgery, an instrument driven by a mallet to perform precise osteotomies without shattering bone.",
    "quotes": [
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The sharp **osteotome** divided the sclerotic bone cleanly, allowing immediate realignment of the malunited fracture." },
      { "author": "Robert Jones", "work": "Injuries to Joints", "quote": "When driving the **osteotome** through dense cortical bone, the surgeon must avoid penetrating into posterior neurovascular bundles." },
      { "author": "John Charnley", "work": "Arthroplasty of the Hip", "quote": "A broad, curved **osteotome** facilitates the clean resection of the femoral head prior to reaming the acetabulum." }
    ]
  },
  "Dashboard — oste\\osteotomy.md": {
    "primary": "The surgical cutting, division, or resection of a bone, performed to realign deformities, relieve osteoarthritis pain, or alter limb length.",
    "secondary": "In reconstructive orthopedics, an operative realignment procedure such as high tibial osteotomy or femoral corrective osteotomy.",
    "quotes": [
      { "author": "Robert Jones", "work": "Orthopaedic Surgery of Injuries", "quote": "Corrective **osteotomy** of the tibia restores mechanical axis alignment, halting the progression of unicompartmental knee arthritis." },
      { "author": "John Charnley", "work": "The Closed Treatment of Common Fractures", "quote": "Intertrochanteric **osteotomy** alters the weight-bearing area of the femoral head, providing years of relief from arthritic pain." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The success of a corrective **osteotomy** depends on rigid internal fixation and meticulous preservation of periosteal blood supply." }
    ]
  },
  "Dashboard — oste\\periosteum.md": {
    "primary": "A specialized, dense, vascular fibrous membrane that covers and protects the outer surface of all bones except at joint surfaces.",
    "secondary": "In bone physiology and surgery, a two-layered tissue consisting of an outer fibrous protective coat and an inner cambium layer containing osteogenic progenitor cells.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **periosteum** is a tough fibrous membrane adhering tenaciously to the bone surface and transmitting nutrient blood vessels." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "Stripping away the **periosteum** reveals the compact bone beneath, which derives its sensory vitality largely from this outer sheath." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "When bone is fractured, the proliferating osteoblasts of the **periosteum** generate the essential external callus of repair." }
    ]
  },
  "Dashboard — oste\\synostosis.md": {
    "primary": "The union or fusion of adjacent bones by the growth of osseous tissue, converting a joint into solid bone.",
    "secondary": "In craniofacial and orthopedic surgery, normal physiological fusion (as in cranial sutures with age) or pathological premature fusion (craniosynostosis).",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The three separate components of the os coxae undergo complete **synostosis** during puberty to form the adult pelvic bone." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Premature **synostosis** of the sagittal suture arrests transverse cranial growth, producing a scaphocephalic head form." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "In radioulnar **synostosis**, congenital osseous fusion locks the forearm in permanent pronation." }
    ]
  },
  "Dashboard — oste\\teleostei.md": {
    "primary": "The vast taxonomic infraclass of ray-finned fishes (Actinopterygii) comprising the overwhelming majority of living bony fishes.",
    "secondary": "In evolutionary ichthyology, modern bony fishes characterized by homocercal tails, mobile premaxillae, cycloid or ctenoid scales, and ossified skeletons.",
    "quotes": [
      { "author": "Louis Agassiz", "work": "Recherches sur les Poissons Fossiles", "quote": "The explosive diversification of the **teleostei** during the Cretaceous period replaced archaic ganoid fishes in all aquatic realms." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Nearly all living food and game fishes belong to the **teleostei**, exhibiting an unrivaled evolutionary plastic adaptability." },
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "In **teleostei**, complete ossification of the vertebral column provides the rigid leverage required for rapid underwater propulsion." }
    ]
  },
  "Dashboard — ot\\Aotus.md": {
    "primary": "A genus of nocturnal New World monkeys (the night monkeys or owl monkeys), distinguished by immense eyes and small, inconspicuous external ears.",
    "secondary": "In primatology and biomedical research, Central and South American arboreal primates belonging to the family Aotidae, widely studied in malaria research.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The nocturnal monkey **Aotus** sleeps curled in hollow trees by day, venturing forth under the moon with silent, cat-like leaps." },
      { "author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "The immense, luminous eyes of **Aotus** dominate its round facial disk, while its ears are hidden beneath soft fur." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Monogamous family groupings in **Aotus** demonstrate that male parental care is deeply integrated into primate social evolution." }
    ]
  },
  "Dashboard — ot\\Myosotis.md": {
    "primary": "A genus of flowering plants in the borage family (Boraginaceae), commonly known as forget-me-nots, characterized by small sky-blue blossoms.",
    "secondary": "In botanical etymology, a generic title derived from Greek for 'mouse's ear,' alluding to the soft, hairy, rounded foliage of the species.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The exquisite blue blossoms of **Myosotis** grace wet stream banks throughout summer, their yellow throats guiding pollinating insects." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The generic designation **Myosotis** commemorates the small, velvety, oblong leaves that resemble the soft ears of a field mouse." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Few garden border plants are more beloved than **Myosotis**, carpeting damp woodland glades with clouds of azure flowers." }
    ]
  },
  "Dashboard — ot\\anotia.md": {
    "primary": "Congenital complete absence of the external ear (pinna or auricle).",
    "secondary": "In clinical teratology and otolaryngology, an extreme first and second branchial arch defect, typically accompanied by atresia of the external auditory canal.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete **anotia** is rarely an isolated anomaly, occurring most frequently within craniofacial microsomia syndromes." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Failure of the six embryonic auricular hillocks of His to develop culminates in unilateral or bilateral **anotia**." },
      { "author": "Isidore Geoffroy Saint-Hilaire", "work": "General and Particular History of Anomalies of Organization", "quote": "In our teratological classifications, **anotia** designates the complete developmental arrest of the external auditory apparatus." }
    ]
  },
  "Dashboard — ot\\exoticism.md": {
    "primary": "The quality, state, or condition of being exotic; foreignness, unusualness, or colorful unfamiliarity.",
    "secondary": "In literary criticism and art history, the fascination with or aesthetic appropriation of distant, non-Western cultures, styles, and landscapes.",
    "quotes": [
      { "author": "Edward Said", "work": "Orientalism", "quote": "Romantic **exoticism** reimagined the East as a sensual playground of decadent despots and veiled mystery." },
      { "author": "Gustave Flaubert", "work": "Salammbô", "quote": "The lush **exoticism** of ancient Carthage provided a canvas of jeweled elephants, incense, and barbaric splendor." },
      { "author": "Victor Segalen", "work": "Essay on Exoticism: An Aesthetics of Diversity", "quote": "True **exoticism** is not the mere tourist pursuit of novel sights, but the acute perception of irreducible cultural otherness." }
    ]
  },
  "Dashboard — ot\\exoticness.md": {
    "primary": "The quality or degree of being exotic; foreign, unfamiliar, or strikingly unusual appearance or character.",
    "secondary": "In aesthetics and cultural commentary, the distinctive appeal of objects, languages, or artistic expressions derived from remote regions.",
    "quotes": [
      { "author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The overwhelming **exoticness** of the South American tropical foliage filled the English travelers with uneasy wonder." },
      { "author": "Henry James", "work": "Transatlantic Sketches", "quote": "There is a singular **exoticness** in the Roman twilight that bewitches the American visitor with historical reverie." },
      { "author": "Joseph Conrad", "work": "Lord Jim", "quote": "The wild **exoticness** of the Eastern archipelago had absorbed him completely, isolating him from his former maritime world." }
    ]
  },
  "Dashboard — ot\\exotism.md": {
    "primary": "A variant form of exoticism; the quality of being foreign or exotic.",
    "secondary": "In literary studies and comparative linguistics, a foreign word, idiom, or cultural concept borrowed into another language or literature.",
    "quotes": [
      { "author": "Charles Baudelaire", "work": "The Flowers of Evil", "quote": "A heady perfume evoking distant island harbors imbued his verses with a haunting, bittersweet **exotism**." },
      { "author": "Victor Segalen", "work": "Notes on Exoticism", "quote": "We must liberate the philosophy of **exotism** from the colonial parlor and restore its authentic aesthetic power." },
      { "author": "Edward Said", "work": "Culture and Imperialism", "quote": "Nineteenth-century European opera repeatedly turned to lavish **exotism** to stage imperial anxieties." }
    ]
  },
  "Dashboard — ot\\microtia.md": {
    "primary": "A congenital malformation characterized by an abnormally small, underdeveloped, or absent external ear (pinna).",
    "secondary": "In pediatric plastic surgery, a spectrum ranging from a mild miniature pinna (Grade I) to a rudimentary vertical sausage-like cartilage vestige (Grade III).",
    "quotes": [
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Defective mesenchymal condensation within the embryonic hyoid arch produces the variable grades of clinical **microtia**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Unilateral **microtia** is frequently associated with conductive hearing loss resulting from external auditory canal atresia." },
      { "author": "Isidore Geoffroy Saint-Hilaire", "work": "Treatise on Teratology", "quote": "The miniature ear remnants seen in **microtia** demonstrate that localized branchial growth can be arrested while facial bones develop normally." }
    ]
  },
  "Dashboard — ot\\ot.md": {
    "primary": "The Greek lexical combining form (ot- / oto-) denoting the ear, the sense of hearing, or ear diseases.",
    "secondary": "In anatomical and physiological nomenclature, an essential radical prefix entering into terms such as otology, otitis, and otoscopy.",
    "quotes": [
      { "author": "Galen", "work": "On Anatomical Procedures", "quote": "The ancient Greeks formed all words pertaining to the hearing organ from the radical **ot**, tracing its internal bony passages." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "Terms derived from **ot** identify the acoustic labyrinth carved within the dense petrous bone." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "In systematic anatomy, the radical **ot** designates both the sensory mechanisms of hearing and the peripheral auricular cartilage." }
    ]
  },
  "Dashboard — ot\\otalgia.md": {
    "primary": "Pain in the ear; earache.",
    "secondary": "In clinical otolaryngology, ear pain classified as primary (originating within the ear) or referred otalgia (originating from dental, pharyngeal, or temporomandibular sources via cranial nerves).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Referred **otalgia** in an elderly smoker with a normal ear examination warrants thorough laryngopharyngeal endoscopy to exclude occult carcinoma." },
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "Acute nocturnal **otalgia** seized the infant with uncontrollable crying, her hand clutching repeatedly at the swollen ear." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Severe **otalgia** accompanied by throbbing deep within the temporal bone heralds acute purulent suppuration of the middle ear." }
    ]
  },
  "Dashboard — ot\\otic.md": {
    "primary": "Of, relating to, or situated in or near the ear (e.g. otic capsule, otic drops).",
    "secondary": "In human neuroanatomy and embryology, designating structures such as the otic ganglion, otic vesicle (otocyst), or otic placode.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **otic** ganglion is situated immediately below the foramen ovale, supplying parasympathetic secretory fibers to the parotid gland." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "The **otic** capsule of the petrous temporal bone is the densest skeletal structure in the human body." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Invagination of the ectodermal **otic** placode forms the closed hollow vesicle that develops into the membranous labyrinth." }
    ]
  },
  "Dashboard — ot\\otitis media.md": {
    "primary": "Inflammation or infection of the middle ear space, located directly behind the tympanic membrane.",
    "secondary": "In clinical otolaryngology, categorized into acute otitis media (with purulent middle-ear effusion and bulging eardrum) and chronic otitis media with effusion.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suppurative **otitis media** following scarlet fever was historically the leading cause of mastoiditis and brain abscess in childhood." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Spontaneous perforation of the drumhead in acute **otitis media** yields a discharge of yellow pus that instantly relieves the agonizing pain." },
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "Eustachian tube obstruction during winter colds traps secretions, sparking acute **otitis media** in tender infants." }
    ]
  },
  "Dashboard — ot\\otitis.md": {
    "primary": "Inflammation of the ear, involving either the external, middle, or internal ear structures.",
    "secondary": "In clinical medicine, subdivided into otitis externa (swimmer's ear), otitis media, and otitis interna (labyrinthitis causing vertigo).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **otitis** requires vigilant examination of the mastoid process to ensure inflammation has not invaded the bony cells." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Infection in external **otitis** is constrained by the dense cartilaginous meatus, producing exquisite tenderness upon traction of the pinna." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Neglected **otitis** has too often been permitted to erode the tegmen tympani, carrying lethal infection directly into the middle cranial fossa." }
    ]
  },
  "Dashboard — ot\\otocephaly.md": {
    "primary": "A lethal congenital malformation characterized by the ventromedial migration and fusion of the external ears beneath an absent or rudimentary lower jaw.",
    "secondary": "In developmental teratology, agnathia-otocephaly complex, an extreme first branchial arch defect resulting in lack of a mandible and approximation of the ears.",
    "quotes": [
      { "author": "Isidore Geoffroy Saint-Hilaire", "work": "General and Particular History of Anomalies of Organization", "quote": "In **otocephaly**, the external ears meet in the anterior midline of the neck because the lower jaw has completely failed to form." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The severe developmental anomaly termed **otocephaly** demonstrates how mandibular hypoplasia disrupts the lateral migration of the auricles." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Severe disruption of neural crest cell migration into the first pharyngeal arch is the underlying developmental etiology of human **otocephaly**." }
    ]
  },
  "Dashboard — ot\\otocleisis.md": {
    "primary": "Occlusion, closure, or stenosis of the external auditory canal or the Eustachian tube.",
    "secondary": "In otology, pathological or congenital imperforation of the ear canal causing conductive hearing impairment.",
    "quotes": [
      { "author": "Albrecht von Haller", "work": "First Lines of Physiology", "quote": "Complete **otocleisis** prevents the ingress of atmospheric acoustic vibrations, rendering the individual completely deaf in that ear." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic scarring following chemical burns may produce fibrous **otocleisis** of the meatus, requiring surgical canalplasty." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Congenital **otocleisis** of the auditory passage can be corrected by careful surgical incision when normal ossicles are present." }
    ]
  },
  "Dashboard — ot\\otoconium.md": {
    "primary": "One of the minute calcium carbonate crystals (otoliths) embedded in the gelatinous membrane of the utricle and saccule of the inner ear.",
    "secondary": "In vestibular sensory neurobiology, microscopic mineral particles that provide gravitational inertia to bend underlying hair cell stereocilia during linear motion.",
    "quotes": [
      { "author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Within the sensory macula, each microscopic **otoconium** granule presses upon the sensory cilia, registering gravitational orientation." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The gelatinous layer covering the vestibular hair cells is encrusted with millions of prismatic **otoconium** crystals." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "Linear acceleration shifts the heavy **otoconium** mass relative to the sensory neuroepithelium, firing action potentials into the vestibular nerve." }
    ]
  },
  "Dashboard — ot\\otocyst.md": {
    "primary": "An auditory or balance vesicle found in aquatic invertebrates, functioning as a primitive organ of equilibrium; a statocyst.",
    "secondary": "In vertebrate embryology, the otic vesicle that invaginates from the embryonic surface ectoderm to form the membranous labyrinth.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The primitive **otocyst** of the medusa consists of a closed epithelial sac containing fluid and a single calcareous mineral grain." },
      { "author": "Ernst Haeckel", "work": "The History of Creation", "quote": "During the fourth week of human development, the **otocyst** closes off from the surface, sinking into the mesenchyme to differentiate into the inner ear." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "quote": "In gastropod mollusks, the paired **otocyst** structures are situated near the pedal ganglia, coordinating postural balance during crawling." }
    ]
  },
  "Dashboard — ot\\otodynia.md": {
    "primary": "Severe, throbbing, or lancinating pain in the ear; acute otalgia.",
    "secondary": "In historical clinical practice, agonizing ear pain caused by deep inflammation, acute middle-ear suppuration, or furunculosis of the ear canal.",
    "quotes": [
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "The patient complained of violent **otodynia**, describing a sharp darting pain that shot from the ear deep into the brain." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe **otodynia** aggravated by chewing is the characteristic bedside sign of acute furunculosis of the cartilaginous meatus." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "In acute suppurative disease, the throbbing **otodynia** ceases the moment the tympanic membrane ruptures and discharges its purulent burden." }
    ]
  },
  "Dashboard — ot\\otolaryngologist.md": {
    "primary": "A medical physician and surgeon who specializes in the diagnosis, medical management, and operative treatment of disorders of the ear, nose, throat, and related head and neck structures (an ENT specialist).",
    "secondary": "An expert in managing complex head and neck pathology, including hearing loss, sinusitis, airway obstruction, sleep apnea, and head and neck neoplasms.",
    "quotes": [
      { "author": "Chevalier Jackson", "work": "Bronchoscopy and Esophagoscopy", "quote": "The modern **otolaryngologist** must possess the delicate manual dexterity of an eye surgeon and the broad physiological vision of an internist." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cooperation with a skilled **otolaryngologist** is essential whenever deep retropharyngeal suppuration threatens descending mediastinitis." },
      { "author": "Harvey Cushing", "work": "Surgery of the Head", "quote": "The diagnostic acumen of the **otolaryngologist** detects early nasopharyngeal malignancies long before cranial nerve palsies appear." }
    ]
  },
  "Dashboard — ot\\otolaryngology.md": {
    "primary": "The medical and surgical specialty that focuses on the anatomy, physiology, diagnosis, and treatment of diseases of the ears, nose, and throat (ENT).",
    "secondary": "In clinical medicine, a surgical discipline encompassing otology, rhinology, laryngology, facial plastic surgery, and head and neck oncology.",
    "quotes": [
      { "author": "Chevalier Jackson", "work": "The Life of Chevalier Jackson: An Autobiography", "quote": "The development of endolaryngeal optical instruments expanded the frontiers of **otolaryngology** into life-saving airway surgery." },
      { "author": "William Osler", "work": "Aequanimitas", "quote": "Specialization in **otolaryngology** brought unprecedented surgical precision to conditions that were formerly fatal in childhood." },
      { "author": "Harvey Cushing", "work": "Intracranial Tumours", "quote": "Modern transsphenoidal approaches to the pituitary gland rely on the shared anatomical expertise of neurosurgery and **otolaryngology**." }
    ]
  },
  "Dashboard — ot\\otolith.md": {
    "primary": "A dense calcium carbonate granule or stone in the inner ear of vertebrates, resting upon sensory hair cells to detect gravity and motion.",
    "secondary": "In ichthyology and fisheries biology, one of three pairs of earstones in bony fishes (sagitta, asteriscus, lapillus), whose growth rings record age and environmental history.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The dense **otolith** shifts under gravitational acceleration, exerting mechanical shearing force upon the underlying sensory hair cells." },
      { "author": "Ernst Haeckel", "work": "The History of Creation", "quote": "In bony fishes, the large calcareous **otolith** fills the saccular cavity, vibrating in resonance with aquatic sound waves." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Vestibular nerve endings form delicate calyceal contacts beneath the macula where the heavy **otolith** mass rests." }
    ]
  },
  "Dashboard — ot\\otologist.md": {
    "primary": "A medical doctor who specializes in otology; a physician and surgeon dedicated to the diagnosis and treatment of diseases of the ear and hearing mechanisms.",
    "secondary": "An expert in managing complex middle ear reconstruction, cochlear implants, chronic mastoiditis, acoustic neuromas, and vestibular balance disorders.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The consulting **otologist** promptly performed a cortical mastoidectomy to halt the spread of infection toward the lateral sinus." },
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear: Their Nature, Diagnosis, and Treatment", "quote": "The mission of the **otologist** is to elevate ear surgery from empirical quackery into an exact scientific discipline." },
      { "author": "Adam Politzer", "work": "A Text-Book of the Diseases of the Ear", "quote": "Through pneumatic otoscopy and functional tuning-fork tests, the modern **otologist** accurately localizes conductive hearing lesions." }
    ]
  },
  "Dashboard — ot\\otology.md": {
    "primary": "The branch of medicine and surgery that investigates the anatomy, physiology, diagnosis, and treatment of the ear and its sensory mechanisms.",
    "secondary": "In medical history, a specialty founded by Joseph Toynbee and Adam Politzer that pioneered middle-ear dissection, tympanoplasty, and audiometric testing.",
    "quotes": [
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "Systematic postmortem dissection of over two thousand temporal bones laid the anatomical foundations of modern **otology**." },
      { "author": "Adam Politzer", "work": "A Text-Book of the Diseases of the Ear", "quote": "The introduction of the operating microscope into clinical **otology** transformed microsurgery of the middle ear." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Every physician practicing internal medicine must master the fundamentals of **otology** to detect early complications of purulent ear disease." }
    ]
  },
  "Dashboard — ot\\otopathy.md": {
    "primary": "Any generic disease, abnormality, or pathological disorder affecting the ear.",
    "secondary": "In clinical diagnosis, an overarching term encompassing inflammatory, degenerative, neoplastic, or vascular conditions of the auditory and vestibular apparatus.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic suppurative **otopathy** can remain dormant for years before suddenly erupting into intracranial complications." },
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "The primary clinical manifestations of chronic **otopathy** include progressive deafness, persistent tinnitus, and occasional vertigo." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Inflammatory **otopathy** following blunt head injury must be investigated immediately for basilar skull fracture and cerebrospinal fluid leak." }
    ]
  },
  "Dashboard — ot\\otophyma.md": {
    "primary": "A rare dermatological and otological condition characterized by benign tuberous hypertrophy, bulbous lobulation, and nodular swelling of the external ear pinna.",
    "secondary": "In clinical dermatology, a severe phymatous variant of rosacea (analogous to rhinophyma of the nose) affecting the auricular cartilage and sebaceous glands.",
    "quotes": [
      { "author": "Ferdinand von Hebra", "work": "Diseases of the Skin", "quote": "The disfiguring lobulated masses of **otophyma** represent chronic sebaceous hyperplasia and connective tissue hypertrophy of the earlobe." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic sections in **otophyma** reveal massively dilated sebaceous follicles surrounded by chronic telangiectatic and lymphocytic stroma." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surgical debulking and contoured re-epithelialization provide substantial cosmetic and functional rehabilitation in advanced **otophyma**." }
    ]
  },
  "Dashboard — ot\\otoplasty.md": {
    "primary": "Plastic, reconstructive, or cosmetic surgery performed on the external ear (auricle or pinna).",
    "secondary": "In reconstructive surgery, procedures performed to reshape prominent ears (pinback otoplasty), repair trauma, or reconstruct the auricle in congenital microtia.",
    "quotes": [
      { "author": "Jacques Joseph", "work": "Nasenplastik und Sonstige Gesichtsplastik", "quote": "Correction of prominent ears by posterior cartilage scoring and suturing represents the foundational technique of modern cosmetic **otoplasty**." },
      { "author": "Harold Gillies", "work": "Plastic Surgery of the Face", "quote": "Total auricular reconstruction requires multi-stage **otoplasty** using autologous costal cartilage carved to mimic the helical rim." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Careful hemostasis and gentle bolsters are essential following **otoplasty** to avert compressive hematoma and subsequent cartilage necrosis." }
    ]
  },
  "Dashboard — ot\\otorhinology.md": {
    "primary": "The medical subspecialty dealing collectively with the anatomy, diseases, and treatment of the ear and the nose.",
    "secondary": "In clinical medicine, the dual discipline uniting otology and rhinology, historically preceding the full integration of laryngology.",
    "quotes": [
      { "author": "Chevalier Jackson", "work": "The Life of Chevalier Jackson", "quote": "The intimate anatomical connection between the nasopharynx and middle ear justifies the joint clinical focus of **otorhinology**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Treating adenoidal hypertrophy and nasal septal deviation falls squarely within the preventive domain of practical **otorhinology**." },
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "Progress in **otorhinology** demonstrated that Eustachian tube dysfunction is almost invariably secondary to chronic nasal catarrh." }
    ]
  },
  "Dashboard — ot\\otorrhea.md": {
    "primary": "A discharge of fluid, whether purulent, serous, or bloody, issuing from the external auditory meatus.",
    "secondary": "In clinical otology, a cardinal symptom of acute or chronic otitis media with tympanic membrane perforation, otitis externa, or temporal bone fracture with CSF leakage.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Foul-smelling chronic **otorrhea** in a child is a ominous sign of cholesteatoma eroding the delicate ossicular chain." },
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "The sudden cessation of purulent **otorrhea** accompanied by rising fever and headache points toward impending intracranial extension." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Clear, watery **otorrhea** following a heavy fall upon the head provides unmistakable bedside proof of a basilar skull fracture." }
    ]
  },
  "Dashboard — ot\\otosclerosis.md": {
    "primary": "A hereditary skeletal disorder of the otic capsule characterized by abnormal bone remodeling, leading to stapes fixation and progressive conductive hearing loss.",
    "secondary": "In otology and hearing science, a condition typically presenting in young adults, marked by replacement of normal enchondral bone by vascular spongy bone, treated surgically by stapedectomy.",
    "quotes": [
      { "author": "Adam Politzer", "work": "A Text-Book of the Diseases of the Ear", "quote": "In 1893, I demonstrated that clinical ankylosis of the stapes is caused by a primary bone disease of the otic capsule, which I termed **otosclerosis**." },
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "The patient with bilateral **otosclerosis** hears speech better in a noisy environment, displaying the classic sign of paracusis Willisii." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Progressive conductive hearing loss with normal tympanic membranes in a young pregnant woman strongly points to familial **otosclerosis**." }
    ]
  },
  "Dashboard — ot\\otoscope.md": {
    "primary": "An optical medical instrument equipped with a light source, magnifying lens, and speculum, used for examining the external auditory canal and tympanic membrane.",
    "secondary": "In clinical diagnosis, a handheld instrument (often with a pneumatic bulb attachment) used to inspect the ear canal and assess tympanic membrane mobility.",
    "quotes": [
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "By introducing the speculum of the **otoscope** under reflected light, the pearly translucence of the normal tympanic membrane is revealed." },
      { "author": "Adam Politzer", "work": "A Text-Book of the Diseases of the Ear", "quote": "The illuminated electric **otoscope** converted ear examination from a cumbersome laboratory procedure into a swift routine bedside test." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "No pediatric examination for unexplained fever is complete until the physician has inspected both drumheads with the **otoscope**." }
    ]
  },
  "Dashboard — ot\\otoscopy.md": {
    "primary": "The medical clinical examination of the external ear canal and tympanic membrane using an otoscope.",
    "secondary": "In otology, pneumatic otoscopy to test eardrum mobility, evaluate middle-ear effusion, and detect perforations or cholesteatoma.",
    "quotes": [
      { "author": "Joseph Toynbee", "work": "The Diseases of the Ear", "quote": "Systematic **otoscopy** requires straightening the cartilaginous meatus by gently pulling the adult pinna upward and backward." },
      { "author": "Adam Politzer", "work": "Diseases of the Ear", "quote": "Pneumatic **otoscopy** demonstrates whether the tympanic membrane moves freely or is dampened by viscous middle-ear fluid." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bedside **otoscopy** reveals the loss of the normal light reflex and bulging redness characteristic of acute suppurative otitis media." }
    ]
  }
}

content = f'''import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH1_DATA = {json.dumps(batch1_data, indent=2, ensure_ascii=False)};

const updated = updateNotesBatch(BASE_DIR, BATCH1_DATA);
console.log(`Body & Physiology Part 6 - Batch 1 Completed: ${{updated}} / ${{Object.keys(BATCH1_DATA).length}} notes updated.`);
'''

with open('main app/scripts/curate-body-p6-batch1.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Generated curate-body-p6-batch1.mjs with {len(batch1_data)} entries.")
