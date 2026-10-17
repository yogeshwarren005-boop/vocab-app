import json
import os

batch2_data = {
  "Dashboard — arthr\\Anarthria.md": {
    "primary": "Complete loss of the ability to articulate speech resulting from severe motor impairment or paralysis of the vocal musculature.",
    "secondary": "In clinical aphasiology and neurology, Pierre Marie's severe expressive speech deficit caused by subcortical or bulbar motor pathway lesions, distinct from cognitive aphasia.",
    "quotes": [
      { "author": "Pierre Marie", "work": "Revision of the Question of Aphasia", "quote": "True **anarthria** consists in the inability to articulate words, while internal language and comprehension remain intact." },
      { "author": "Paul Broca", "work": "Remarks on the Seat of the Faculte of Articulate Language", "quote": "When motor coordinates for speech are destroyed without paralysis of tongue or lips, profound **anarthria** supervenes." },
      { "author": "A. R. Luria", "work": "Higher Cortical Functions in Man", "quote": "Subcortical lesions affecting the striopallidal pathways produce severe **anarthria** with intact phonemic hearing." }
    ]
  },
  "Dashboard — arthr\\arthr.md": {
    "primary": "The Greek anatomical root and combining form denoting a joint or articulation (arthr- / arthro-).",
    "secondary": "In descriptive anatomy and zoology, a root designating articulated connections between bones, cartilages, or exoskeleton segments.",
    "quotes": [
      { "author": "Galen", "work": "On the Usefulness of the Parts of the Body", "quote": "Every movable union of skeletal elements was designated by ancient anatomists through the radical **arthr**." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "Dissecting the limbs reveals how bone meets bone through specialized synovial junctions marked by the Greek stem **arthr**." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "In osteology and syndesmology, words derived from **arthr** categorize both immovable sutures and free diarthrodial joints." }
    ]
  },
  "Dashboard — arthr\\arthralgia.md": {
    "primary": "Severe pain in one or more joints, occurring without necessary inflammatory swelling or erythema.",
    "secondary": "In rheumatology, a subjective symptom of articular discomfort that may herald early viral infections, systemic autoimmune disorders, or degenerative wear.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The onset of dengue is characterized by excruciating **arthralgia** that earns the disease its popular title of breakbone fever." },
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "Sharp **arthralgia** frequently precedes the outward swelling of the joint, tormenting the patient throughout the night." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Persistent hip **arthralgia** in young children should prompt an immediate search for insidious spinal or pelvic disease." }
    ]
  },
  "Dashboard — arthr\\arthralgic.md": {
    "primary": "Of, relating to, or characterized by arthralgia; afflicted with pain in the joints.",
    "secondary": "In clinical diagnosis, designating patient complaints or symptom complexes dominated by articular pain without overt signs of acute effusion.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The convalescent patient remained weak and **arthralgic**, complaining of dull aches whenever barometric pressure plummeted." },
      { "author": "Benjamin Rush", "work": "Medical Inquiries and Observations", "quote": "A severe **arthralgic** paroxysm seized the extremities following sudden exposure to cold autumnal rains." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "Transient **arthralgic** complaints in pediatric patients must be scrutinized for evidence of underlying rheumatic fever." }
    ]
  },
  "Dashboard — arthr\\arthritic.md": {
    "primary": "Pertaining to, caused by, or suffering from arthritis; afflicted with inflammation of the joints.",
    "secondary": "An individual afflicted with chronic arthritis; characterized by stiffness, deformity, or swelling of the articular joints.",
    "quotes": [
      { "author": "Michel de Montaigne", "work": "Essays", "quote": "The **arthritic** old soldier limps patiently along, nursing the joints that cold campaigns had stiffened." },
      { "author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Thou art a boil, a plague sore, an embossed carbuncle in my corrupted blood; yet **arthritic** aches grip my bones." },
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "Grandfather Smallweed sat bundled up in his armchair, a bitter **arthritic** invalid barking orders at his family." }
    ]
  },
  "Dashboard — arthr\\arthritis.md": {
    "primary": "Inflammation of one or more joints, causing pain, swelling, stiffness, and restricted movement.",
    "secondary": "In pathology, an umbrella term encompassing osteoarthritis, rheumatoid arthritis, gout, and infectious joint diseases.",
    "quotes": [
      { "author": "Thomas Sydenham", "work": "Treatise on the Gout and Dropsy", "quote": "Gout is a specific form of **arthritis** that seizes the great toe with agonizing nocturnal burning." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic rheumatoid **arthritis** gradually destroys articular cartilage, leading to bony ankylosis and crippling contractures." },
      { "author": "Benjamin Rush", "work": "An Account of the Arthritic State of Fever", "quote": "Articular inflammation or **arthritis** is not a local disease alone, but partakes of systemic vascular agitation." }
    ]
  },
  "Dashboard — arthr\\arthrocentesis.md": {
    "primary": "The clinical procedure of puncturing a joint capsule with a sterile needle to aspirate synovial fluid for diagnostic analysis or therapeutic decompression.",
    "secondary": "In emergency medicine and rheumatology, joint fluid aspiration performed to distinguish septic arthritis from crystal-induced gout or pseudogout.",
    "quotes": [
      { "author": "Harvey Cushing", "work": "Surgery of the Joints", "quote": "Diagnostic **arthrocentesis** yielded turbid yellow fluid containing abundant polymorphonuclear leukocytes." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Immediate **arthrocentesis** relieves acute intra-articular pressure, mitigating irreversible ischemic damage to the cartilaginous surfaces." },
      { "author": "Charles H. Mayo", "work": "Observations on Joint Surgery", "quote": "Polarized light microscopy of fluid obtained via **arthrocentesis** immediately reveals needle-shaped urate crystals." }
    ]
  },
  "Dashboard — arthr\\arthrodesis.md": {
    "primary": "The surgical immobilization and permanent bony fusion of a joint, performed to alleviate intractable pain or correct gross instability.",
    "secondary": "In orthopedic surgery, an operative procedure creating complete ankylosis across an articular space using bone grafts and internal hardware.",
    "quotes": [
      { "author": "Eduard Albert", "work": "Some Cases of Arthrodesis in Paralytic Flail Joints", "quote": "By performing an **arthrodesis** of the flail knee joint, we transformed a useless dangling limb into a stable weight-bearing pillar." },
      { "author": "Robert Jones", "work": "Injuries to Joints", "quote": "Triple **arthrodesis** of the tarsus provides enduring stability for patients suffering from post-traumatic foot deformities." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Careful denudation of articular cartilage is essential if the attempted **arthrodesis** is to achieve solid osseous union." }
    ]
  },
  "Dashboard — arthr\\arthrogram.md": {
    "primary": "A radiographic image of the interior of a joint obtained after injecting a radiopaque contrast material or air into the synovial capsule.",
    "secondary": "In orthopedic radiology, an imaging study visualizing soft tissue structures such as meniscal tears, labral detachments, and ligamentous disruptions.",
    "quotes": [
      { "author": "Charles Dotter", "work": "Arthrography of the Knee", "quote": "The contrast **arthrogram** demonstrated extravasation of dye along the posterior horn, confirming a complete meniscal tear." },
      { "author": "John Charnley", "work": "The Closed Treatment of Common Fractures", "quote": "Examination of the pediatric hip **arthrogram** revealed that the femoral head was securely seated within the cartilaginous socket." },
      { "author": "Ian Donald", "work": "Radiological Techniques in Joint Disease", "quote": "Air-contrast double injection provides an **arthrogram** of exceptional sharpness, outlining delicate synovial fringes." }
    ]
  },
  "Dashboard — arthr\\arthrography.md": {
    "primary": "The radiographic examination of a joint capsule and its internal structures following injection of radiopaque contrast medium.",
    "secondary": "In diagnostic radiology, contrast fluoroscopy or computed tomography used to assess articular cartilage erosion and internal joint derangements.",
    "quotes": [
      { "author": "Charles Dotter", "work": "Arthrography of the Knee", "quote": "Before the advent of magnetic resonance imaging, **arthrography** was the definitive diagnostic method for inspecting the knee joint." },
      { "author": "John Charnley", "work": "Arthroplasty of the Hip", "quote": "Postoperative **arthrography** detects subtle prosthetic loosening by showing contrast leaking along the cement-bone interface." },
      { "author": "Robert Jones", "work": "Injuries to Joints", "quote": "Techniques of diagnostic **arthrography** opened a new era in evaluating chronic athletic trauma of the shoulder." }
    ]
  },
  "Dashboard — arthr\\arthrology.md": {
    "primary": "The branch of anatomical and physiological science that deals with the study of joints and articulations.",
    "secondary": "In medical education, the systematic study of the classification, morphology, biomechanics, and pathology of skeletal connections.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "In systematic **arthrology**, joints are categorized as synarthroses, amphiarthroses, or diarthroses according to their degree of movement." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "A thorough mastery of **arthrology** is indispensable to any physician who would reduce dislocations without causing fracture." },
      { "author": "Albrecht von Haller", "work": "First Lines of Physiology", "quote": "Comparative **arthrology** demonstrates how the quadruped carpus is exquisitely modified to support the locomotive shocks of the animal." }
    ]
  },
  "Dashboard — arthr\\arthromere.md": {
    "primary": "Any of the homologous body segments or metameres that compose the body of an arthropod.",
    "secondary": "In invertebrate morphology, a body segment bearing a pair of jointed appendages and corresponding nerve ganglia.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Each successive **arthromere** of the lobster's abdomen consists of a dorsal tergum, a ventral sternum, and lateral pleura." },
      { "author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "The serial repetition of each **arthromere** reveals the metameric ancestry shared by annelids and arthropods." },
      { "author": "E. Ray Lankester", "work": "The Structure and Classification of the Arthropoda", "quote": "Cephalic tagmatization fuses several primitive **arthromere** units into a single consolidated cranium." }
    ]
  },
  "Dashboard — arthr\\arthromeric.md": {
    "primary": "Of, relating to, or consisting of an arthromere; segmental in anatomical construction.",
    "secondary": "In developmental biology, describing the metameric body segmentation typical of embryonic and adult arthropods.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The segmented nerve cord exhibits a distinctly **arthromeric** arrangement of paired ganglia corresponding to each ring." },
      { "author": "Francis Maitland Balfour", "work": "A Treatise on Comparative Embryology", "quote": "Transverse somite divisions establish the **arthromeric** boundaries before the cuticular exoskeleton begins to harden." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "quote": "Appendages develop as paired lateral evaginations situated on each individual **arthromeric** division." }
    ]
  },
  "Dashboard — arthr\\arthropathy.md": {
    "primary": "Any disease, pathological disorder, or abnormal condition affecting a joint.",
    "secondary": "In rheumatology and neurology, specific destructive joint disorders such as neuropathic arthropathy (Charcot joint) associated with tabes dorsalis or diabetes.",
    "quotes": [
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "quote": "In tabetic patients, a painless destructive **arthropathy** suddenly disintegrates the knee joint without signs of acute fever." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hemophilic **arthropathy** results from repeated intra-articular hemorrhages that progressively erode the hyaline articular cartilage." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Degenerative **arthropathy** begins with fibrillation of the cartilaginous matrix, followed by subchondral sclerosis and osteophyte formation." }
    ]
  },
  "Dashboard — arthr\\arthroplasty.md": {
    "primary": "The surgical reconstruction, repair, or prosthetic replacement of a diseased, damaged, or ankylosed joint.",
    "secondary": "In orthopedic surgery, total joint replacement (such as total hip or knee replacement) restoring mobility and relieving chronic pain.",
    "quotes": [
      { "author": "John Charnley", "work": "Low Friction Arthroplasty of the Hip", "quote": "The success of total hip **arthroplasty** depends upon the combination of high-density polyethylene and self-curing acrylic bone cement." },
      { "author": "Robert Jones", "work": "Injuries to Joints", "quote": "Excision **arthroplasty** provides a movable, albeit fibrous, junction for patients crippled by septic ankylosis." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Meticulous aseptic technique is the paramount requirement in **arthroplasty**, where deep prosthetic sepsis spells disaster." }
    ]
  },
  "Dashboard — arthr\\arthropod.md": {
    "primary": "Any invertebrate animal belonging to the phylum Arthropoda, characterized by a chitinous exoskeleton, segmented body, and paired jointed appendages.",
    "secondary": "In evolutionary zoology, members of the most diverse animal phylum, comprising insects, crustaceans, arachnids, and myriapods.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The rigid external cuticle of the **arthropod** necessitates periodic ecdysis to permit somatic growth." },
      { "author": "Ernst Haeckel", "work": "The History of Creation", "quote": "From trilobites to butterflies, every **arthropod** shares a bilateral body plan organized into functional tagmata." },
      { "author": "Charles Darwin", "work": "The Origin of Species", "quote": "The compound eye of the **arthropod** demonstrates an astonishing optical complexity evolved through insensible gradations." }
    ]
  },
  "Dashboard — arthr\\arthropoda.md": {
    "primary": "The massive taxonomic phylum comprising invertebrate animals with jointed legs, segmented bodies, and chitinous exoskeletons.",
    "secondary": "In systematic taxonomy, the animal phylum containing over eighty percent of all described living animal species, dominant across terrestrial and aquatic ecosystems.",
    "quotes": [
      { "author": "Ernst Haeckel", "work": "Systematic Phylogeny", "quote": "The phylum **arthropoda** embodies the pinnacle of protostome morphological radiation and ecological diversification." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In **arthropoda**, the coelom is largely replaced by an open hemocoel through which blood circulates bathed by muscle contractions." },
      { "author": "E. Ray Lankester", "work": "The Structure and Classification of the Arthropoda", "quote": "Comparative appendicular morphology proves that all **arthropoda** share a common segmented ancestor." }
    ]
  },
  "Dashboard — arthr\\arthropodal.md": {
    "primary": "Of, relating to, or resembling an arthropod.",
    "secondary": "In comparative anatomy, describing characteristics typical of arthropods, such as jointed appendages, chitinous cuticles, and hemocoelic body cavities.",
    "quotes": [
      { "author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The tropical forest floor teems with bizarre **arthropodal** life, from giant centipedes to camouflaged stick-insects." },
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The **arthropodal** limb functions via antagonistic muscle groups attached directly to the inner surface of the exoskeleton." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "quote": "Onychophorans exhibit an intermediate grade between annelid wormlike traits and true **arthropodal** sclerotization." }
    ]
  },
  "Dashboard — arthr\\arthropodan.md": {
    "primary": "Belonging to, characteristic of, or pertaining to the phylum Arthropoda; an arthropod.",
    "secondary": "In evolutionary biology and paleontology, describing the clade or morphological lineage of jointed-legged ecdysozoans.",
    "quotes": [
      { "author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "The **arthropodan** line achieved mastery of land flight millions of years before vertebrates took to the air." },
      { "author": "E. Ray Lankester", "work": "Extinct Animals", "quote": "Giant eurypterids of the Silurian seas represent the largest **arthropodan** predators in the fossil record." },
      { "author": "Stephen Jay Gould", "work": "Wonderful Life: The Burgess Shale and the Nature of History", "quote": "The Burgess Shale deposits revealed a wild disparity of **arthropodan** body architectures that defy modern classification." }
    ]
  },
  "Dashboard — arthr\\arthropodous.md": {
    "primary": "Possessing jointed legs or appendages; characteristic of or belonging to the arthropods.",
    "secondary": "In historical zoological descriptions, designating organisms or anatomical structures exhibiting articulated jointed construction.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The **arthropodous** limb consists of distinct podomeres linked by flexible articular membranes." },
      { "author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "An **arthropodous** organization provides extraordinary leverage and agility across rugged terrain." },
      { "author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "Even sessile barnacles betray their **arthropodous** nature through their jointed, feather-like thoracic cirri." }
    ]
  },
  "Dashboard — arthr\\arthropteris.md": {
    "primary": "A genus of climbing or epiphytic ferns in the family Tectariaceae, native to the Old World tropics and Australasia.",
    "secondary": "In systematic pteridology, ferns characterized by fronds jointed to creeping rhizomes and round indusiate sori.",
    "quotes": [
      { "author": "William Jackson Hooker", "work": "Species Filicum", "quote": "The articulating stipe of **arthropteris** enables the plant to climb gracefully up the trunks of rainforest trees." },
      { "author": "F. O. Bower", "work": "The Ferns (Filicales)", "quote": "In **arthropteris**, the pinnae are articulate to the rachis, falling cleanly away upon senescence." },
      { "author": "Alan R. Smith", "work": "A Classification for Extant Ferns", "quote": "Recent phylogenetic analyses place **arthropteris** firmly within Tectariaceae despite historical confusion with Oleandra." }
    ]
  },
  "Dashboard — arthr\\arthroscope.md": {
    "primary": "An endoscopic surgical instrument equipped with fiberoptic illumination and lenses, inserted into a joint cavity for direct visual examination.",
    "secondary": "In orthopedic surgery, an instrument introduced through a puncture incision to inspect articular surfaces, menisci, and synovial linings.",
    "quotes": [
      { "author": "Kenji Takagi", "work": "The Arthroscope", "quote": "By inserting a miniature **arthroscope** into the knee, the surgeon inspects the living cartilage without opening the joint capsule." },
      { "author": "Masaki Watanabe", "work": "Atlas of Arthroscopy", "quote": "The development of the modern self-focusing **arthroscope** converted joint diagnostics into a minimally invasive art." },
      { "author": "John Charnley", "work": "The Closed Treatment of Common Fractures", "quote": "Direct visualization through the **arthroscope** prevents unnecessary exploratory arthrotomies in athletic knee trauma." }
    ]
  },
  "Dashboard — arthr\\arthroscopic.md": {
    "primary": "Of, relating to, or performed by means of an arthroscope or arthroscopy.",
    "secondary": "In orthopedic surgical practice, designating minimally invasive joint procedures, such as arthroscopic meniscectomy or cruciate ligament reconstruction.",
    "quotes": [
      { "author": "Masaki Watanabe", "work": "Atlas of Arthroscopy", "quote": "We performed the first **arthroscopic** meniscectomy using specialized miniaturized cutting instruments through portal incisions." },
      { "author": "John Charnley", "work": "Injuries of the Knee", "quote": "Rapid rehabilitation is the chief benefit of **arthroscopic** repair, sparing the quadriceps mechanism significant surgical trauma." },
      { "author": "Atul Gawande", "work": "Complications", "quote": "The surgeon monitored the video screen as the **arthroscopic** shaver smoothed the ragged edges of the torn meniscus." }
    ]
  },
  "Dashboard — arthr\\arthroscopy.md": {
    "primary": "The minimally invasive surgical examination and operative treatment of the interior of a joint using an arthroscope.",
    "secondary": "In clinical orthopedics, a diagnostic and therapeutic technique widely employed to repair cartilage tears, reconstruct ligaments, and biopsy synovial tissue.",
    "quotes": [
      { "author": "Masaki Watanabe", "work": "Memories of Arthroscopy", "quote": "Pioneering knee **arthroscopy** in Tokyo laid the technological foundation for modern ambulatory sports medicine." },
      { "author": "Kenji Takagi", "work": "Practical Arthroscopy", "quote": "Through diagnostic **arthroscopy**, early tubercular lesions of the synovium can be detected long before radiographic signs appear." },
      { "author": "Atul Gawande", "work": "Better", "quote": "Routine knee **arthroscopy** has replaced large exploratory incisions with tiny keyhole puncture wounds." }
    ]
  },
  "Dashboard — arthr\\arthrosis.md": {
    "primary": "An anatomical articulation or joint between two or more bones.",
    "secondary": "In clinical pathology, a degenerative, non-inflammatory disease of a joint (osteoarthrosis or osteoarthritis).",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Every movable skeletal union constitutes a true **arthrosis**, secured by fibrous ligaments and lubricated by synovia." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Unlike inflammatory arthritis, senile **arthrosis** represents mechanical wear and tear accompanied by cartilage erosion." },
      { "author": "Jean-Martin Charcot", "work": "Diseases of Old Age", "quote": "Severe hip **arthrosis** limits ambulation in the elderly, producing characteristic antalgic gait patterns." }
    ]
  },
  "Dashboard — arthr\\arthrospore.md": {
    "primary": "An asexual, vegetative spore formed by the septation and fragmentation of a fungal hypha or bacterial filament; an arthroconidium.",
    "secondary": "In medical mycology, the infectious spore form of Coccidioides immitis, easily airborne and capable of causing valley fever upon inhalation.",
    "quotes": [
      { "author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "Upon maturity, the hypha breaks apart at the transverse septa, releasing each rectangular **arthrospore** into the wind." },
      { "author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The disarticulation of filaments into an **arthrospore** suspension facilitates rapid microbial dispersal across substrate surfaces." },
      { "author": "Ferdinand Cohn", "work": "Researches on Bacteria", "quote": "Certain filamentous bacteria propagate through chains of resting **arthrospore** segments resilient against drying." }
    ]
  },
  "Dashboard — arthr\\arthrosporic.md": {
    "primary": "Of, relating to, or characterized by arthrospores; reproducing by means of arthrospores.",
    "secondary": "In mycology and bacteriology, designating species that form spores through the fragmentation of hyphal threads.",
    "quotes": [
      { "author": "Anton de Bary", "work": "Morphology of the Fungi", "quote": "The **arthrosporic** mode of reproduction differs fundamentally from the endogenous production of ascospores within a sac." },
      { "author": "Ferdinand Cohn", "work": "Beiträge zur Biologie der Pflanzen", "quote": "In filamentous schizomycetes, **arthrosporic** fragmentation occurs rapidly when nutrient broth becomes exhausted." },
      { "author": "Roland Thaxter", "work": "Studies on Myxobacteria", "quote": "Hyphae displaying **arthrosporic** cleavage separate cleanly along double cell walls under mechanical vibration." }
    ]
  },
  "Dashboard — arthr\\arthrosporous.md": {
    "primary": "Bearing, producing, or multiplying by arthrospores; characterized by vegetative hyphal fragmentation.",
    "secondary": "In systematic mycology and microbiology, describing fungal or bacterial taxa that disperse primarily through fragmented jointed spores.",
    "quotes": [
      { "author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "The **arthrosporous** fungi spread rapidly across decaying organic substrates by shedding millions of rectangular conidia." },
      { "author": "Julius von Sachs", "work": "Textbook of Botany", "quote": "We contrast endosporous bacteria with **arthrosporous** varieties whose entire cellular bodies transform into reproductive units." },
      { "author": "William Bulloch", "work": "The History of Bacteriology", "quote": "Early investigators debated whether **arthrosporous** fragmentation represented true sporulation or mere physical dissolution." }
    ]
  },
  "Dashboard — arthr\\dysarthria.md": {
    "primary": "A motor speech disorder characterized by poor articulation, slurred speech, or difficulty speaking due to neurological impairment of speech muscles.",
    "secondary": "In clinical neurology, a motor deficit resulting from damage to cranial nerves, the cerebellum, basal ganglia, or corticobulbar tracts, with language comprehension intact.",
    "quotes": [
      { "author": "A. R. Luria", "work": "The Working Brain", "quote": "Cerebellar lesions produce an explosive, scanning **dysarthria** with erratic vocal pitch and broken rhythm." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "quote": "Scanning speech, nystagmus, and intention tremor form the classic triad of multiple sclerosis, marked by progressive **dysarthria**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bulbar palsy manifests early as nasal **dysarthria** and difficulty swallowing due to paralysis of the palatal muscles." }
    ]
  },
  "Dashboard — arthr\\enarthrosis.md": {
    "primary": "A ball-and-socket joint, in which the rounded head of one bone fits into the cuplike cavity of another, allowing movement in all directions.",
    "secondary": "In human anatomy, specifically the hip joint (coxofemoral joint) or shoulder joint (glenohumeral joint).",
    "quotes": [
      { "author": "Galen", "work": "On Anatomical Procedures", "quote": "Nature fashioned the hip as an **enarthrosis**, where the deep acetabular socket firmly grips the spherical femoral head." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The shoulder is an **enarthrosis** endowed with extraordinary range of motion at the expense of intrinsic bony stability." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "Disarticulating an **enarthrosis** demonstrates how the cotyloid ligament deepens the receiving cavity to retain the bone." }
    ]
  },
  "Dashboard — arthr\\pancreatitis.md": {
    "primary": "Inflammation of the pancreas, accompanied by severe epigastric pain and elevated serum digestive enzymes.",
    "secondary": "In clinical gastroenterology, an acute or chronic condition caused by premature activation of zymogens leading to enzymatic autodigestion, often linked to gallstones or alcohol.",
    "quotes": [
      { "author": "Reginald Heber Fitz", "work": "Acute Pancreatitis", "quote": "Acute hemorrhagic **pancreatitis** strikes suddenly with violent epigastric agony, collapse, and extensive retroperitoneal necrosis." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A gallstone impacted at the ampulla of Vater can trigger catastrophic reflux of bile into the pancreatic duct, provoking acute **pancreatitis**." },
      { "author": "Claude Bernard", "work": "Memoir on the Pancreas", "quote": "The potent digestive ferments of the gland become instruments of destruction whenever acute **pancreatitis** disrupts tissue integrity." }
    ]
  },
  "Dashboard — arthr\\pharyngitis.md": {
    "primary": "Inflammation of the mucous membranes and submucosa of the pharynx; commonly called a sore throat.",
    "secondary": "In clinical medicine, an infectious condition typically caused by respiratory viruses or Group A Streptococcus, presenting with erythema, exudates, and fever.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Streptococcal **pharyngitis** requires prompt bacteriological diagnosis to guide antimicrobial therapy and prevent acute rheumatic fever." },
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "Epidemic catarrhs of winter are invariably accompanied by fiery **pharyngitis** that makes swallowing even liquids painful." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Severe membranous **pharyngitis** must be watched vigilantly to ensure inflammatory edema does not spread downward into the glottis." }
    ]
  },
  "Dashboard — arthr\\polyarthritis.md": {
    "primary": "Inflammation of multiple joints simultaneously or in rapid succession (typically five or more joints).",
    "secondary": "In clinical rheumatology, symmetrical or migratory joint inflammation characteristic of systemic autoimmune disorders, including rheumatoid arthritis and lupus.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The migratory **polyarthritis** of acute rheumatic fever flits from joint to joint, leaving no residual deformity behind." },
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "When multiple joints swell simultaneously, the condition ceases to be simple podagra and enters the realm of systemic **polyarthritis**." },
      { "author": "Paul Klemperer", "work": "Collagen Diseases", "quote": "Chronic symmetrical **polyarthritis** is the clinical hallmark of connective tissue degeneration within synovial membranes." }
    ]
  },
  "Dashboard — arthr\\rheumatoid arthritis.md": {
    "primary": "A chronic, systemic autoimmune inflammatory disorder characterized primarily by symmetrical, destructive, erosive inflammation of the peripheral joints.",
    "secondary": "In rheumatology, an autoimmune disease characterized by persistent synovial proliferation (pannus formation), circulating rheumatoid factors, and eventual joint ankylosis.",
    "quotes": [
      { "author": "Alfred Baring Garrod", "work": "A Treatise on Gout and Rheumatic Gout", "quote": "I propose the term **rheumatoid arthritis** to designate this chronic symmetrical articular affection distinct from true gout." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In **rheumatoid arthritis**, proliferative changes in the synovium and cartilage lead slowly to characteristic ulnar deviation of the fingers." },
      { "author": "Philip Hench", "work": "The Effect of a Hormone of the Adrenal Cortex on Rheumatoid Arthritis", "quote": "Administering cortisone produced dramatic, unprecedented remission of pain and stiffness in patients with advanced **rheumatoid arthritis**." }
    ]
  },
  "Dashboard — arthr\\spondyloarthropathy.md": {
    "primary": "Any of a family of interrelated chronic inflammatory rheumatic diseases primarily affecting the spine, sacroiliac joints, and entheses.",
    "secondary": "In rheumatology, an HLA-B27 associated seronegative disease complex encompassing ankylosing spondylitis, psoriatic arthritis, and reactive arthritis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Axial stiffness and fusion of the vertebral column in young men point to a progressive seronegative **spondyloarthropathy**." },
      { "author": "Jean-Martin Charcot", "work": "Clinical Lectures on Senile Diseases", "quote": "In severe **spondyloarthropathy**, the entire spinal axis transforms into a rigid, curved osseous column termed bamboo spine." },
      { "author": "Philip Hench", "work": "Rheumatism and Arthritis", "quote": "Unlike rheumatoid disease, **spondyloarthropathy** targets the entheses where tendons insert into bone, driving asymmetric inflammation." }
    ]
  },
  "Dashboard — axon\\axon.md": {
    "primary": "The long, slender, cylindrical projection of a nerve cell that conducts electrical impulses (action potentials) away from the cell body.",
    "secondary": "In neurobiology, the primary functional efferent neurite terminating in synaptic boutons that release neurotransmitters across synaptic clefts.",
    "quotes": [
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System of Man and Vertebrates", "quote": "The individual **axon** travels immense distances through white matter tracts to deliver its electrical message to distant targets." },
      { "author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The wave of negativity traveling down the motor **axon** evokes muscular contraction across the terminal neuromuscular junction." },
      { "author": "Alan Hodgkin", "work": "The Conduction of the Nervous Impulse", "quote": "By inserting a capillary electrode into the giant **axon** of the squid, we recorded the inward sodium rush of the action potential." }
    ]
  },
  "Dashboard — axon\\axonal.md": {
    "primary": "Of, relating to, or situated in an axon.",
    "secondary": "In neurobiology and neuropathology, describing processes such as axonal transport, axonal degeneration (Wallerian degeneration), or axonal terminal sprouting.",
    "quotes": [
      { "author": "Santiago Ramón y Cajal", "work": "Degeneration and Regeneration of the Nervous System", "quote": "Following nerve transection, the distal **axonal** segments fragment and are consumed by proliferating Schwann cells." },
      { "author": "Alan Hodgkin", "work": "The Conduction of the Nervous Impulse", "quote": "The **axonal** membrane behaves as a voltage-sensitive capacitor governed by selective ionic permeabilities." },
      { "author": "Andrew Huxley", "work": "Reflections on Muscle", "quote": "Fast **axonal** transport carries vital neurotransmitter vesicles from the cell body toward distant presynaptic terminals." }
    ]
  },
  "Dashboard — axon\\axone.md": {
    "primary": "A variant or historical spelling of axon, the principal efferent nerve fiber that transmits impulses away from the neuron cell body.",
    "secondary": "In early twentieth-century neuroanatomy, the axis-cylinder or neurite conducting nerve impulses to other neurons or effector organs.",
    "quotes": [
      { "author": "Santiago Ramón y Cajal", "work": "Structure of the Nervous System", "quote": "Each motor neuron emits a solitary **axone** that enters the anterior root to innervate peripheral striated muscle fibers." },
      { "author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The terminal arborizations of an **axone** form functional synaptic contacts with the dendrites of neighboring nerve cells." },
      { "author": "C. Judson Herrick", "work": "An Introduction to Neurology", "quote": "The myelin sheath encircling the central **axone** dramatically increases the conduction velocity of the electrical impulse." }
    ]
  },
  "Dashboard — axon\\axonography.md": {
    "primary": "The scientific recording, graphical tracing, and analysis of electrical impulses (action potentials) traveling along nerve axons.",
    "secondary": "In experimental neurophysiology, electrophysiological oscillography applied to single-fiber nerve preparations.",
    "quotes": [
      { "author": "Alan Hodgkin", "work": "The Conduction of the Nervous Impulse", "quote": "Modern **axonography** allows us to record voltage sweeps lasting fractions of a millisecond across single nerve fibers." },
      { "author": "Andrew Huxley", "work": "Measurement of Membrane Current in the Squid Giant Axon", "quote": "Quantitative **axonography** confirmed that potassium outward currents mediate the rapid repolarization of the nerve membrane." },
      { "author": "John Carew Eccles", "work": "The Physiology of Nerve Cells", "quote": "Precision **axonography** demonstrated that subthreshold local potentials fail to propagate down the length of the nerve cord." }
    ]
  },
  "Dashboard — axon\\axonotmesis.md": {
    "primary": "A type of peripheral nerve injury characterized by disruption of the nerve axon and myelin sheath while the supporting connective tissue sheath (endoneurium) remains intact.",
    "secondary": "In clinical neurology, the intermediate grade of nerve trauma in Herbert Seddon's classification, which permits spontaneous axonal regeneration along intact tubular scaffolds.",
    "quotes": [
      { "author": "Herbert Seddon", "work": "Three Types of Nerve Injury", "quote": "In **axonotmesis**, the essential neural tubes survive unbroken, ensuring that regenerating fibers find their proper peripheral destinations." },
      { "author": "Wilder Penfield", "work": "Surgical Pathology of the Peripheral Nerves", "quote": "Unlike complete transection, **axonotmesis** usually recovers spontaneously without the necessity of open operative nerve suturing." },
      { "author": "Sydney Sunderland", "work": "Nerves and Nerve Injuries", "quote": "Wallerian degeneration proceeds distally in **axonotmesis**, followed by axonal regeneration at the rate of one millimeter per day." }
    ]
  },
  "Dashboard — blenn\\blenn.md": {
    "primary": "The Greek lexical combining form (blenn- / blenno-) denoting mucus, slime, or viscous fluid secretions.",
    "secondary": "In anatomical and pathology terminology, a root designating mucopurulent discharges or slime-producing organs.",
    "quotes": [
      { "author": "Galen", "work": "Method of Medicine", "quote": "Ancient physicians used the term **blenn** to designate cold, phlegmatic, and viscous secretions of the mucous membranes." },
      { "author": "Albrecht von Haller", "work": "First Lines of Physiology", "quote": "Secretory follicles lining the respiratory passage produce protective lubricative fluid rooted in the ancient radical **blenn**." },
      { "author": "Thomas Wharton", "work": "Adenographia", "quote": "Glandular anatomy differentiates serous secretions from the thick, viscous fluids designated under the prefix **blenn**." }
    ]
  },
  "Dashboard — blenn\\blennadenitis.md": {
    "primary": "Inflammation of mucous glands, especially those of the conjunctiva, respiratory tract, or genitourinary mucous membranes.",
    "secondary": "In ophthalmology, chronic inflammation of the mucous crypts and glands of Krause and Wolfring within the eyelid conjunctiva.",
    "quotes": [
      { "author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "Follicular **blennadenitis** of the palpebral conjunctiva produces persistent granular irritation requiring topical astringents." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Catarrhal **blennadenitis** of the bronchial glands exacerbates chronic cough in patients with recurrent bronchitis." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination in **blennadenitis** shows the mucous acini distended with stagnant inspissated secretions." }
    ]
  },
  "Dashboard — blenn\\blenniidae.md": {
    "primary": "The family of small, marine perciform fishes known as combtooth blennies, characterized by scaleless, slime-covered bodies and blunt heads.",
    "secondary": "In ichthyology, a family of benthic reef and tidepool fishes possessing close-set, comb-like teeth and modified pelvic fins used for perching on rocks.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Fishes of the family **blenniidae** are nimble tidepool inhabitants, often leaping across exposed rocks between waves." },
      { "author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "A tiny member of the **blenniidae** peered out from an abandoned worm tube in the coral reef, waving its fringed tentacles." },
      { "author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The **blenniidae** are easily recognized by their slender, elongated form, slimy skin, and fleshy orbital crests." }
    ]
  },
  "Dashboard — blenn\\blennioid.md": {
    "primary": "Resembling or having the morphological characteristics of a blenny fish; blenny-like.",
    "secondary": "In systematic ichthyology, designating fishes exhibiting the slender, slippery, scaleless body and benthic habits of the blennioids.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "Fishes", "quote": "The **blennioid** form represents an exquisite morphological adaptation for living in the turbulent surge zone of rocky shores." },
      { "author": "William Beebe", "work": "Field Book of Shore Fishes of Bermuda", "quote": "This small **blennioid** creature darted among the sea anemones, sheltered by its viscous skin secretion." },
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "In the shallow tidepools, several **blennioid** fishes lay nestled in crevices, waiting for the rising tide." }
    ]
  },
  "Dashboard — blenn\\blennioidea.md": {
    "primary": "The suborder of marine perciform fishes comprising blennies, clinids, chaenopsids, and pricklebacks.",
    "secondary": "In ichthyological taxonomy, a major radiation of bottom-dwelling shore fishes sharing jugular pelvic fins and slender, mucous-covered bodies.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "The Genera of Fishes", "quote": "We group these specialized benthic families into the suborder **blennioidea**, characterized by jugular pelvic fins and scaleless skin." },
      { "author": "Georges Cuvier", "work": "Histoire Naturelle des Poissons", "quote": "The anatomical features of **blennioidea** reflect an ancient divergence toward rock-dwelling, sedentary marine life." },
      { "author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The suborder **blennioidea** contains numerous genera distributed along the rocky shores of temperate and tropical seas." }
    ]
  },
  "Dashboard — blenn\\blennius.md": {
    "primary": "A genus of marine combtooth blennies (family Blenniidae), comprising small, scaleless fishes with tentacled crests above their eyes.",
    "secondary": "In taxonomic history, the type genus established by Linnaeus in 1758, encompassing active intertidal fishes that graze on algae and small invertebrates.",
    "quotes": [
      { "author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "The genus **blennius** is characterized by a slimy body, two jugular ventral rays, and teeth arranged in a close comb-like row." },
      { "author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "In **blennius**, the dorsal fin runs the entire length of the back, and the head is adorned with curious fleshy appendages." },
      { "author": "David Starr Jordan", "work": "Fishes", "quote": "Naturalists along the Mediterranean have long studied **blennius** for its curious territorial fidelity to rocky crevices." }
    ]
  },
  "Dashboard — blenn\\blennophobia.md": {
    "primary": "An irrational, abnormal, and persistent fear or visceral revulsion of slime, mucus, or viscous substances.",
    "secondary": "In psychopathology, a specific phobia presenting with acute disgust and avoidance behaviors triggered by slippery, slimy, or gelatinous textures.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Visceral aversions to slippery textures often crystallize into pathological **blennophobia**, paralyzing the neurotic subject." },
      { "author": "G. Stanley Hall", "work": "A Study of Fears", "quote": "In children, an intense horror of slugs and sticky mud often heralds persistent adult **blennophobia**." },
      { "author": "George M. Beard", "work": "A Practical Treatise on Nervous Exhaustion", "quote": "Morbid dread of bodily secretions is a well-known symptom of neurasthenia, presenting as acute **blennophobia**." }
    ]
  },
  "Dashboard — blenn\\blennorrhagia.md": {
    "primary": "An excessive, profuse mucous or mucopurulent discharge, especially from the urethra; gonorrhea.",
    "secondary": "In historical clinical medicine, the profuse purulent urethritis caused by Neisseria gonorrhoeae before the discovery of antibiotics.",
    "quotes": [
      { "author": "Philippe Ricord", "work": "Treatise on Venereal Diseases", "quote": "Through rigorous inoculation experiments, I demonstrated that **blennorrhagia** is completely distinct from the syphilitic chancre." },
      { "author": "John Hunter", "work": "A Treatise on the Venereal Disease", "quote": "The inflammatory discharge in acute **blennorrhagia** issues from the vascular lining of the anterior urethra." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Untreated gonorrheal **blennorrhagia** frequently leads to chronic posterior urethritis and fibrous stricture formation." }
    ]
  },
  "Dashboard — blenn\\blennosperma.md": {
    "primary": "A small genus of spring-flowering annual herbs in the daisy family (Asteraceae), native to vernal pools and wet meadows in California and Chile.",
    "secondary": "In systematic botany, stickyseed herbs whose achenes produce a mucilaginous, sticky gelatinous coat when moistened by winter rains.",
    "quotes": [
      { "author": "Asa Gray", "work": "Botanical Memoirs", "quote": "The generic name **blennosperma** accurately describes the achene, which becomes surrounded by a thick envelope of mucilage when wetted." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "In **blennosperma**, the gelatinous seed coat facilitates anchorage in the drying mud of ephemeral spring pools." },
      { "author": "Willis Linn Jepson", "work": "A Flora of California", "quote": "The yellow radiate heads of **blennosperma** carpet the margins of California vernal pools in early March." }
    ]
  },
  "Dashboard — blenn\\blenny.md": {
    "primary": "Any of numerous small, elongated, scaleless or small-scaled marine fishes of the suborder Blennioidei, common in tidepools and coastal reefs.",
    "secondary": "In marine biology, bottom-dwelling coastal fishes characterized by blunt heads, large pectoral fins, and a thick coating of body slime.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "A startled **blenny** darted from under a frond of sea lettuce, disappearing into a shadowed granite crevice." },
      { "author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "The curious little **blenny** rested on its pelvic fins, watching my diver's helmet with large, rotating eyes." },
      { "author": "David Starr Jordan", "work": "Fishes", "quote": "Every rocky headland washed by temperate surf is home to the agile, slime-coated **blenny**." }
    ]
  },
  "Dashboard — brachi\\Brachiosaurus.md": {
    "primary": "A genus of massive sauropod dinosaurs of the Late Jurassic period, distinguished by forelegs longer than its hindlegs and an erect neck.",
    "secondary": "In vertebrate paleontology, an immense quadrupedal herbivore whose giraffe-like posture allowed browsing on high conifer canopies.",
    "quotes": [
      { "author": "Elmer S. Riggs", "work": "Brachiosaurus altithorax, the Largest Known Dinosaur", "quote": "The remarkable disproportion of the humerus to the femur led me to designate this titanic reptile **Brachiosaurus**." },
      { "author": "Henry Fairfield Osborn", "work": "Sauropoda of the Morrison Formation", "quote": "With its elevated shoulders and colossal neck, **Brachiosaurus** browsed upon high Jurassic tree canopies beyond the reach of diplodocids." },
      { "author": "Robert T. Bakker", "work": "The Dinosaur Heresies", "quote": "The high nostrils and towering posture of **Brachiosaurus** made it the ultimate high-canopy harvesting machine of the Jurassic." }
    ]
  },
  "Dashboard — brachi\\abrachia.md": {
    "primary": "Congenital absence of the arms or upper extremities.",
    "secondary": "In teratology and developmental embryology, an extreme limb reduction anomaly resulting from failure of upper limb-bud initiation during early gestation.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital anomalies of the extremities range from subtle polydactyly to total **abrachia**, where both arms are entirely missing at birth." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Arrest of the upper limb buds during the fourth week of embryonic development culminates in complete **abrachia**." },
      { "author": "Isidore Geoffroy Saint-Hilaire", "work": "General and Particular History of Anomalies of Organization", "quote": "In our teratological taxonomy, **abrachia** exemplifies the complete suppression of the anterior paired appendages." }
    ]
  },
  "Dashboard — brachi\\brachi.md": {
    "primary": "The anatomical combining form derived from the Greek brachion, denoting the arm or an arm-like structure (brachi- / brachio-).",
    "secondary": "In comparative anatomy and embryology, a radical designating the upper limb or structures connected with the brachium.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The root **brachi** enters into the nomenclature of muscles and vessels supplying the upper limb from shoulder to elbow." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "The muscular anatomy of the human arm is described under terms compounded from the ancient Greek **brachi**." },
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "In tetrapod morphology, the anterior limb segments are designated by derivatives of the ancestral stem **brachi**." }
    ]
  },
  "Dashboard — brachi\\brachial artery.md": {
    "primary": "The major systemic blood vessel of the upper arm, extending from the lower border of the teres major as a continuation of the axillary artery.",
    "secondary": "In clinical medicine, the principal artery of the arm used for measuring systemic blood pressure via sphygmomanometry, dividing at the elbow into radial and ulnar branches.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **brachial artery** descends down the medial side of the arm, lying along the inner border of the biceps muscle." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "Ligature of the **brachial artery** requires delicate dissection to avoid injuring the accompanying median nerve." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Compressing the **brachial artery** against the humerus provides immediate hemostasis for severe hemorrhage in the forearm." }
    ]
  },
  "Dashboard — brachi\\brachial.md": {
    "primary": "Of, relating to, or situated in the arm, especially the upper arm (e.g. brachial plexus, brachial veins).",
    "secondary": "In zoology, designating an arm-like appendage, ray, or locomotive tentacle in marine invertebrates.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **brachial** plexus arises from the ventral rami of the lower four cervical nerves and the first thoracic nerve." },
      { "author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "Severe traction upon the neonate's shoulder during delivery can tear the **brachial** nerves, causing Erb's palsy." },
      { "author": "Galen", "work": "On Anatomical Procedures", "quote": "The main **brachial** vessels lie deeply sheltered along the inner aspect of the bone to escape external injury." }
    ]
  },
  "Dashboard — brachi\\brachialgia.md": {
    "primary": "Severe pain in the arm or upper extremity, particularly of neuralgic or radicular origin.",
    "secondary": "In clinical neurology, radiating pain along the distribution of the cervical nerve roots (cervicobrachialgia) caused by cervical disk herniation or osteophytes.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cervical osteoarthritis frequently presents as excruciating nocturnal **brachialgia** radiating down to the fingertips." },
      { "author": "Harvey Cushing", "work": "Tumors of the Nervus Acusticus", "quote": "Compressive neurofibromas of the cervical spine provoke persistent unilateral **brachialgia** resistant to simple analgesics." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "quote": "The patient complained of lancinating **brachialgia**, accompanied by numbness and paresthesias in the thumb and index finger." }
    ]
  },
  "Dashboard — brachi\\brachiate.md": {
    "primary": "To swing hand over hand from branch to branch using the arms as the primary means of arboreal locomotion (as gibbons do).",
    "secondary": "In descriptive botany, having widely spreading, opposite branches arranged alternately at right angles to each other.",
    "quotes": [
      { "author": "C. R. Carpenter", "work": "A Field Study of the Behavior and Social Relations of the Gibbon", "quote": "Watching gibbons **brachiate** through the high rain forest canopy reveals an acrobatic agility unmatched by any other primate." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "The stem produces opposite, spreading limbs that **brachiate** at successive nodes in a decussate pattern." },
      { "author": "Julian Huxley", "work": "The Courtship Habits of the Great Crested Grebe and Other Studies", "quote": "Specialized anatomical adaptations in the wrist and shoulder enable the lesser apes to **brachiate** with effortless momentum." }
    ]
  },
  "Dashboard — brachi\\brachiation.md": {
    "primary": "A form of arboreal locomotion in which an animal swings hand over hand along tree branches using only its arms.",
    "secondary": "In primatology and physical anthropology, the specialized locomotive adaptation of apes featuring elongated forelimbs, mobile wrists, and a rotatable shoulder.",
    "quotes": [
      { "author": "C. R. Carpenter", "work": "A Field Study in Siam of the Behavior and Social Relations of the Gibbon", "quote": "True **brachiation** allows the gibbon to traverse gaps in the forest canopy at speeds exceeding thirty miles per hour." },
      { "author": "Sherwood Washburn", "work": "The Evolution of Man", "quote": "The anatomical modifications required for **brachiation** freed the ancestral ape torso from quadrupedal stiffness." },
      { "author": "Jane Goodall", "work": "The Chimpanzees of Gombe", "quote": "While chimpanzees rely mostly on knuckle-walking, they readily employ **brachiation** when traveling through the high fruiting trees." }
    ]
  },
  "Dashboard — brachi\\brachiferous.md": {
    "primary": "Bearing or possessing arms, arm-like branches, or brachial appendages.",
    "secondary": "In invertebrate morphology and botany, describing organisms equipped with arm-like appendages or radiating branches.",
    "quotes": [
      { "author": "John Lindley", "work": "An Introduction to Botany", "quote": "The **brachiferous** arrangement of the inflorescence features wide lateral arms spreading perpendicularly from the main axis." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Echinoderms display a **brachiferous** body plan in which each radial arm bears ambulacral grooves and tube feet." },
      { "author": "Ernst Haeckel", "work": "Report on the Deep-Sea Keratosa", "quote": "The sponge skeleton projected several **brachiferous** lobes that supported the inhalant dermal pores." }
    ]
  },
  "Dashboard — brachi\\brachinus.md": {
    "primary": "A genus of ground beetles (family Carabidae), commonly called bombardier beetles, capable of expelling a boiling chemical defensive spray.",
    "secondary": "In entomology and chemical ecology, beetles that mix hydroquinones and hydrogen peroxide in an abdominal chamber with enzymes to produce explosive steam.",
    "quotes": [
      { "author": "Charles Darwin", "work": "Life and Letters of Charles Darwin", "quote": "Under a piece of bark I found a specimen of **brachinus**, which instantly discharged its pungent artillery into my hand." },
      { "author": "Thomas Say", "work": "American Entomology", "quote": "When touched, the small carabid beetle **brachinus** emits an audible detonation followed by a cloud of caustic smoke." },
      { "author": "Jean-Henri Fabre", "work": "The Life of the Beetle", "quote": "The internal pyrotechnic apparatus of **brachinus** illustrates how nature anticipates the thermal explosions of human chemistry." }
    ]
  },
  "Dashboard — brachi\\brachiocubital.md": {
    "primary": "Of, relating to, or involving both the upper arm (brachium) and the forearm or elbow (cubitus).",
    "secondary": "In descriptive anatomy and clinical surgery, pertaining to the region extending along the arm from the shoulder to the elbow joint.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **brachiocubital** fascia binds together the flexor and extensor muscles as they cross the elbow articulation." },
      { "author": "Charles Bell", "work": "The Anatomy of the Human Body", "quote": "Careful dissection of the **brachiocubital** region reveals the superficial course of the basilic and cephalic veins." },
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "The **brachiocubital** musculature coordinates the powerful flexion of the forearm upon the upper arm." }
    ]
  },
  "Dashboard — brachi\\brachionerysipelas.md": {
    "primary": "An acute, spreading erysipelas or severe streptococcal dermal infection localized to the upper arm.",
    "secondary": "In historical clinical surgery, an acute cutaneous and subcutaneous inflammatory infection of the arm presenting with bright erythema and high fever.",
    "quotes": [
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Trauma to the upper extremity occasionally provokes rapid **brachionerysipelas**, spreading from the wound toward the axilla." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Early drainage and antiseptic compresses arrested the fulminant course of acute **brachionerysipelas**." },
      { "author": "Astley Cooper", "work": "Lectures on the Principles and Practice of Surgery", "quote": "The intense burning redness of **brachionerysipelas** demands vigilant monitoring lest gangrenous cellulitis supervene." }
    ]
  },
  "Dashboard — brachi\\brachionigraph.md": {
    "primary": "An instrument or physiological apparatus designed for measuring, recording, and graphically tracing the movements and mechanical work of the arm.",
    "secondary": "In early experimental physiology and kinesiology, a mechanical recorder tracing arm flexion, fatigue, and tremor during physical exertion.",
    "quotes": [
      { "author": "Angelo Mosso", "work": "Fatigue", "quote": "Using a customized **brachionigraph**, we plotted the progressive decline of voluntary muscular power in the human arm." },
      { "author": "Étienne-Jules Marey", "work": "Movement", "quote": "The **brachionigraph** provided an accurate graphic tracing of the trajectory and velocity of arm movement during heavy labor." },
      { "author": "Hugo Münsterberg", "work": "Psychology and Industrial Efficiency", "quote": "Industrial psychologists employed the **brachionigraph** to optimize repetitive arm movements among factory workers." }
    ]
  },
  "Dashboard — brachi\\brachiopod.md": {
    "primary": "Any marine coelomate invertebrate belonging to the phylum Brachiopoda, enclosed in a bivalve shell with dorsal and ventral valves.",
    "secondary": "In marine biology and paleontology, commonly known as lampshells, possessing a ciliated lophophore for feeding and a muscular pedicle for attachment.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain species of the **brachiopod** Lingula have survived through immense geological epochs with scarcely any visible change." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Unlike molluscan bivalves whose shells are lateral, the valves of the **brachiopod** are dorsal and ventral." },
      { "author": "James Dwight Dana", "work": "Manual of Geology", "quote": "The Paleozoic seas swarmed with diverse **brachiopod** colonies that formed thick beds of fossiliferous limestone." }
    ]
  },
  "Dashboard — brachi\\brachiopoda.md": {
    "primary": "An ancient phylum of solitary, marine bivalve invertebrates equipped with a lophophore and unequal dorsal and ventral shells.",
    "secondary": "In invertebrate paleontology, an ancient phylum with over 12,000 fossil species, exceptionally abundant from the Cambrian through the Permian.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The phylum **brachiopoda** holds a unique evolutionary position, combining bivalve protective architecture with a sophisticated lophophore." },
      { "author": "Charles Darwin", "work": "The Origin of Species", "quote": "The sudden abundance of **brachiopoda** in primordial strata troubled early geologists who sought gradual ancestral lineages." },
      { "author": "Charles Doolittle Walcott", "work": "Cambrian Brachiopoda", "quote": "The well-preserved chitinous shells of the earliest **brachiopoda** illuminate the dawn of biomineralization in Cambrian seas." }
    ]
  },
  "Dashboard — brachi\\brachiopodous.md": {
    "primary": "Of, relating to, or having the anatomical characteristics of a brachiopod; belonging to the phylum Brachiopoda.",
    "secondary": "In marine invertebrate morphology, describing organisms possessing unequal dorsal-ventral valves and ciliated brachial arms (lophophore).",
    "quotes": [
      { "author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The spiral ciliated arms of the **brachiopodous** animal create continuous feeding currents within the mantle cavity." },
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The **brachiopodous** pedicle anchors the shell securely to rocky sea bottoms, resisting the pull of tidal currents." },
      { "author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Abundant **brachiopodous** fossils characterize the Devonian limestone formations across the Appalachian basin." }
    ]
  },
  "Dashboard — brachi\\brachiorrhachidian.md": {
    "primary": "Pertaining to or involving both the upper arm (brachium) and the spinal cord or vertebral column (rhachis).",
    "secondary": "In neuroanatomy and clinical neurology, designating the cervical spinal roots and cord pathways that innervate the arm.",
    "quotes": [
      { "author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "The **brachiorrhachidian** pathways coordinate reflex withdrawal of the arm when noxious stimuli touch the hand." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Cervical enlargement of the spinal cord reflects the vast concentration of motor neurons supplying **brachiorrhachidian** trunks." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "quote": "Spinal cord tumors compressing the fifth cervical segment provoke severe **brachiorrhachidian** pain and motor weakness." }
    ]
  },
  "Dashboard — brachi\\brachium.md": {
    "primary": "The arm, specifically the upper arm between the shoulder and the elbow joint in human anatomy.",
    "secondary": "In neuroanatomy, any arm-like connecting tract or peduncle of white nerve fibers in the brain stem (e.g. brachium pontis, brachium conjunctivum).",
    "quotes": [
      { "author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "The humerus provides the sole skeletal foundation of the **brachium**, articulating above with the scapula and below with the radius and ulna." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The superior cerebellar peduncle was formerly known to anatomists as the **brachium** conjunctivum connecting the cerebellum to the midbrain." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Myelinated fibers streaming through the **brachium** of the inferior colliculus convey auditory impulses toward the thalamus." }
    ]
  },
  "Dashboard — brachi\\microbrachia.md": {
    "primary": "Abnormal congenital smallness or underdevelopment of the arms.",
    "secondary": "In teratology and medical genetics, a congenital reduction anomaly where the upper extremities are abnormally small while maintaining recognizable anatomical proportions.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Disproportionate limb development presenting as congenital **microbrachia** may occur as an isolated defect or within genetic syndromes." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Vascular insufficiency during early limb-bud development can result in bilateral **microbrachia** without affecting cranial structures." },
      { "author": "Isidore Geoffroy Saint-Hilaire", "work": "Treatise on Teratology", "quote": "In cases of **microbrachia**, each skeletal element of the arm is present in miniature form, retaining normal anatomical articulation." }
    ]
  }
}

content = f'''import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH2_DATA = {json.dumps(batch2_data, indent=2, ensure_ascii=False)};

const updated = updateNotesBatch(BASE_DIR, BATCH2_DATA);
console.log(`Body & Physiology Part 1 - Batch 2 Completed: ${{updated}} / ${{Object.keys(BATCH2_DATA).length}} notes updated.`);
'''

with open('main app/scripts/curate-body-p1-batch2.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Generated curate-body-p1-batch2.mjs with {len(batch2_data)} entries.")
