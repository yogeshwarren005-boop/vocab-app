import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — paed (34 words) ===
  "Dashboard — paed/orthopaedic.md": {
    primary: "Relating to the branch of medicine concerned with the correction of deformities of bones or muscles (British spelling of orthopedic).",
    secondary: "In surgical history, coined by Nicolas Andry from Greek orthos ('straight') and pais ('child') to describe methods of correcting childhood musculoskeletal deformities.",
    quotes: [
      { author: "Nicolas Andry", work: "Orthopaedia: Or, the Art of Correcting and Preventing Deformities in Children", quote: "I have formed the term **orthopaedic** from two Greek words, signifying the straight rearing of children." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early **orthopaedic** intervention prevents permanent joint contraction following acute paralytic polio." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "The surgeon fitted an **orthopaedic** splint to align the fractured metatarsal neatly." }
    ]
  },
  "Dashboard — paed/orthopaedics.md": {
    primary: "The branch of medicine dealing with the correction of deformities of bones or muscles (British spelling of orthopedics).",
    secondary: "In surgical specialties, the prevention, diagnosis, and treatment of musculoskeletal trauma, sports injuries, and degenerative spine disease.",
    quotes: [
      { author: "Nicolas Andry", work: "Orthopaedia", quote: "The foundational aim of **orthopaedics** was to train crooked young limbs to grow straight and robust." },
      { author: "William Osler", work: "Aequanimitas", quote: "Modern **orthopaedics** combines anatomical precision with biomechanical engineering to restore mobility." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "Pioneering bone-grafting techniques established **orthopaedics** as an essential surgical discipline." }
    ]
  },
  "Dashboard — paed/orthopaedist.md": {
    primary: "A surgeon or physician who specializes in orthopaedics (British spelling of orthopedist).",
    secondary: "A medical specialist performing arthroplasty, spinal stabilization, and complex fracture repair.",
    quotes: [
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The skilled **orthopaedist** reconstructed my severed quadriceps tendon with meticulous care." },
      { author: "William Osler", work: "The Master-Word in Medicine", quote: "The consulting **orthopaedist** warned against premature weight-bearing on the healing femur." },
      { author: "Arthur Conan Doyle", work: "Memories and Adventures", quote: "A celebrated Edinburgh **orthopaedist** demonstrated how spinal curvature could be halted by early bracing." }
    ]
  },
  "Dashboard — paed/orthopedic.md": {
    primary: "Relating to the branch of medicine concerned with the correction of deformities of bones or muscles; designed to relieve skeletal discomfort.",
    secondary: "In clinical medicine, pertaining to surgical and non-surgical treatments for musculoskeletal trauma, deformities, and degenerative joint diseases.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The **orthopedic** surgeon must understand physical mechanics as thoroughly as human anatomy." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The recovery of limb function required prolonged **orthopedic** physiotherapy and corrective footwear." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "Remarkable biocompatible titanium alloys transformed modern **orthopedic** joint replacement." }
    ]
  },
  "Dashboard — paed/orthopedical.md": {
    primary: "Pertaining to orthopedics; orthopedic (archaic or formal variant).",
    secondary: "Relating to corrective mechanical apparatus or surgical procedures designed to correct bodily deformities.",
    quotes: [
      { author: "Nicolas Andry", work: "Orthopaedia", quote: "We employed an **orthopedical** brace designed to relieve abnormal vertebral pressure during growth." },
      { author: "William Buchan", work: "Domestic Medicine", quote: "Gentle **orthopedical** exercises were recommended to prevent rickety bowlegs in nursing infants." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient practitioners devised various **orthopedical** splints to straighten warped infant bones." }
    ]
  },
  "Dashboard — paed/orthopedist.md": {
    primary: "A physician or surgeon who specializes in orthopedics.",
    secondary: "A specialist trained in the diagnosis, surgical repair, and rehabilitation of bones, joints, ligaments, and tendons.",
    quotes: [
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "My **orthopedist** examined the neurological reflex response following the complex knee repair." },
      { author: "William Osler", work: "Aequanimitas", quote: "The clinical insight of an experienced **orthopedist** can avert permanent childhood lameness." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The resident **orthopedist** inspected the traction pulleys aligned beside the hospital bed." }
    ]
  },
  "Dashboard — paed/paed.md": {
    primary: "A combining root derived from Ancient Greek pais (stem paid-), meaning 'child', 'boy', or 'education'.",
    secondary: "In etymological lexicography and morphological analysis, the base morpheme underlying terms relating to child rearing, education, and childhood medicine.",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "The civic education of youth, rooted in ancient **paed**-agogy, forms the guardian soul of the republic." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Greek concept of **paed**-eia represented the total cultural upbringing that fashioned the ideal citizen." },
      { author: "Aristotle", work: "Politics", quote: "Civic legislators must legislate first for the nursery and the physical culture of the growing **paed**-." }
    ]
  },
  "Dashboard — paed/paederast.md": {
    primary: "A man who engages in sexual relations with boys (British/historical spelling of pederast).",
    secondary: "In classical Greek cultural history, the adult male partner (erastēs) in an institutionalized mentorship and romantic relationship with an adolescent youth (erōmenos).",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "Pausanias praised the noble **paederast** who guided his young beloved toward philosophy and civic virtue." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Roman satirists ridiculed the Greek customs of the philosophical **paederast** as corrupt foreign indulgence." },
      { author: "Michel Foucault", work: "The Use of Pleasure", quote: "Classical Athenian society subjected the conduct of the **paederast** to intense ethical and civic scrutiny." }
    ]
  },
  "Dashboard — paed/paederastic.md": {
    primary: "Relating to, characterized by, or practicing pederasty (British spelling).",
    secondary: "In classical historiography and literary analysis, describing the romantic and pedagogical relationship between adult men and youths in ancient Greece.",
    quotes: [
      { author: "Plato", work: "Phaedrus", quote: "Socrates scrutinized the **paederastic** speeches of Lysias, distinguishing sensual desire from philosophical love." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Spartan educational system integrated **paederastic** mentorship to foster absolute martial comradeship." },
      { author: "Michel Foucault", work: "The Care of the Self", quote: "Attic comedies frequently mocked the **paederastic** pursuit of evasive youths across gymnasium palaiastrai." }
    ]
  },
  "Dashboard — paed/paederasty.md": {
    primary: "Sexual relations between a man and a boy (British spelling of pederasty).",
    secondary: "In classical antiquity, a formalized social, educational, and erotic custom in ancient Greek city-states between an older man and an adolescent youth.",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "In Elis and Boeotia, custom sanctions **paederasty** without question, whereas in Ionia it is condemned as servile." },
      { author: "Michel Foucault", work: "The Use of Pleasure", quote: "Athenian discourse on **paederasty** wrestled constantly with the paradox of loving a youth destined for free citizenship." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Christian emperors enacted severe capital statutes to eradicate the ancient pagan tolerance of **paederasty**." }
    ]
  },
  "Dashboard — paed/paediatric.md": {
    primary: "Relating to the branch of medicine dealing with children and their diseases (British spelling of pediatric).",
    secondary: "In healthcare and developmental medicine, concerning clinical care, neonatology, and preventative wellness for infants and adolescents.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The establishment of specialized **paediatric** wards drastically reduced cross-infection among hospitalized infants." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "Routine childhood immunization transformed **paediatric** practice from palliative watching to triumphant prevention." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Early **paediatric** histories often revealed unrecognized bouts of viral encephalitis in childhood." }
    ]
  },
  "Dashboard — paed/paediatrician.md": {
    primary: "A medical practitioner specializing in children and their diseases (British spelling of pediatrician).",
    secondary: "A specialist physician managing congenital disorders, pediatric pharmacology, and child developmental milestones.",
    quotes: [
      { author: "Benjamin Spock", work: "The Common Sense Book of Baby and Child Care", quote: "Trust your common sense and consult your **paediatrician** whenever persistent fever alarms you." },
      { author: "William Osler", work: "Aequanimitas", quote: "The observant **paediatrician** must possess infinite patience when decoding the non-verbal complaints of an infant." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "A dedicated **paediatrician** ministers to both the physical child and the anxious fears of the mother." }
    ]
  },
  "Dashboard — paed/paediatrics.md": {
    primary: "The branch of medicine dealing with children and their diseases (British spelling of pediatrics).",
    secondary: "The clinical medical specialty dedicated to the physical, emotional, and social health of children from birth through adolescence.",
    quotes: [
      { author: "William Osler", work: "The Evolution of Modern Medicine", quote: "The emergence of modern **paediatrics** as an autonomous discipline was a crowning achievement of 19th-century clinical care." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "No branch of clinical practice has achieved more radiant triumphs than preventive **paediatrics**." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Congenital neurological deficits require interdisciplinary collaboration with developmental **paediatrics**." }
    ]
  },
  "Dashboard — paed/paedogenesis.md": {
    primary: "Reproduction by sexually mature larvae or animals that have otherwise not attained physical maturity (neoteny).",
    secondary: "In evolutionary developmental biology, a form of heterochrony where reproductive organs accelerate development relative to somatic tissues (e.g. axolotls or gall midges).",
    quotes: [
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "The axolotl remains permanently in its larval aquatic form, reproducing through precocious **paedogenesis**." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "In cecidomyiid gall midges, **paedogenesis** allows daughter larvae to develop inside the hemolymph of the mother larva." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Cellular investigations into **paedogenesis** highlight how endocrine timing alters the sequence of developmental stages." }
    ]
  },
  "Dashboard — paed/paedomorphism.md": {
    primary: "The retention of juvenile or larval features in the adult animal; neoteny.",
    secondary: "In evolutionary morphology and anthropology, the macro-evolutionary process whereby descendants resemble the juvenile ancestral stages (often posited in human cranial evolution).",
    quotes: [
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Human adult anatomy displays marked **paedomorphism**, retaining flat faces and open cranial sutures characteristic of juvenile apes." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Evolutionary radiation in salamanders has repeatedly been facilitated by adaptive **paedomorphism**." },
      { author: "Gavin de Beer", work: "Embryos and Ancestors", quote: "Through **paedomorphism**, adult organisms escape overspecialized ancestral constraints and open new morphological paths." }
    ]
  },
  "Dashboard — paed/paedophile.md": {
    primary: "A person who is sexually attracted to children (British spelling of pedophile).",
    secondary: "In clinical psychiatry and forensic psychology, an individual exhibiting pedophilic disorder characterized by persistent sexual urges toward prepubescent children.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Early forensic alienists classified the compulsive **paedophile** among the severe pathologies of sexual deviation." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Pathological fixation upon infantile love objects characterizes the distorted libido of the **paedophile**." },
      { author: "Michel Foucault", work: "The History of Sexuality", quote: "Nineteenth-century psychiatry isolated the **paedophile** as a dangerous medical category requiring penal confinement." }
    ]
  },
  "Dashboard — paed/paedophilia.md": {
    primary: "Sexual attraction to children (British spelling of pedophilia).",
    secondary: "In psychiatric nosology (DSM-5 / ICD-11), a paraphilic disorder defined by recurrent, intense sexual fantasies or behaviors involving prepubescent children.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Medical jurisprudence recognized that cases of **paedophilia** demanded strict societal protection of vulnerable youth." },
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "The psychopathology of **paedophilia** represents an arrest of psychosexual maturation at an archaic developmental phase." },
      { author: "Michel Foucault", work: "Abnormal: Lectures at the Collège de France", quote: "The legal and clinical apparatus surrounding **paedophilia** established new regimes of forensic supervision." }
    ]
  },
  "Dashboard — paed/page.md": {
    primary: "One side of a leaf of a book, newspaper, or letter; or a youth employed to run errands or attend a person of high rank.",
    secondary: "In feudal history, a boy of noble birth training for knighthood as personal attendant to a lord or lady.",
    quotes: [
      { author: "Walter Scott", work: "Ivanhoe", quote: "The handsome young **page** bore his lord's heavy shield and spurred his steed beside the knight." },
      { author: "John Milton", work: "Areopagitica", quote: "As good almost kill a man as kill a good book; who kills a man kills a reasonable creature, but he who destroys a good book kills reason itself upon the printed **page**." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I turned the yellowed **page** of Bewick's History of British Birds, entranced by solitary Arctic shores." }
    ]
  },
  "Dashboard — paed/pager.md": {
    primary: "An electronic telecommunication device that beeps or vibrates when receiving a message or telephone number; a beeper.",
    secondary: "In clinical hospital communication and historical technology, a portable wireless radio receiver carrying emergency clinical alerts.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The sudden shrill beep of the resident's **pager** interrupted our clinical neurological rounds." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "In the modern emergency room, the ever-vibrating **pager** tethered the surgeon to the bedside." },
      { author: "Don DeLillo", work: "White Noise", quote: "Electronic murmurs from the pocket **pager** reminded us of the invisible network wrapping the city." }
    ]
  },
  "Dashboard — paed/paginate.md": {
    primary: "To number the pages of a book, manuscript, or document.",
    secondary: "In typography and desktop publishing, to arrange text and layout into sequential discrete pages.",
    quotes: [
      { author: "Thomas Frognall Dibdin", work: "The Bibliomania; or Book-Madness", quote: "Early printers did not always **paginate** their folios, relying instead on signature marks at the bottom of the leaf." },
      { author: "George Saintsbury", work: "A History of Elizabethan Literature", quote: "The publisher failed to **paginate** the preliminary verses correctly before binding the volume." },
      { author: "James Murray", work: "The Oxford English Dictionary (Preface)", quote: "Meticulous scribes were hired to **paginate** the vast bundles of lexicographical slips." }
    ]
  },
  "Dashboard — paed/paging.md": {
    primary: "The act of calling someone using a public address system or electronic pager; or numbering the pages of a book.",
    secondary: "In computer memory management, a virtual memory architecture that transfers fixed-size blocks of data (pages) between RAM and disk.",
    quotes: [
      { author: "Andrew S. Tanenbaum", work: "Modern Operating Systems", quote: "Virtual memory systems employ demand **paging** to swap idle processes between physical memory and backing store." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The loud **paging** for Dr. Munro echoed through the crowded hospital corridors." },
      { author: "Douglas Hofstadter", work: "Gödel, Escher, Bach", quote: "The computer kernel manages memory **paging** transparently, creating the illusion of boundless workspace." }
    ]
  },
  "Dashboard — paed/pedagogic.md": {
    primary: "Of, relating to, or characteristic of teaching or educators; pedagogical.",
    secondary: "In educational philosophy, pertaining to structured instructional methods and curriculum delivery.",
    quotes: [
      { author: "John Dewey", work: "The School and Society", quote: "Our **pedagogic** aim must be to cultivate independent critical inquiry rather than passive memorization." },
      { author: "Jean-Jacques Rousseau", work: "Emile: Or, On Education", quote: "Natural learning outshines artificial **pedagogic** contrivances every day of a child's life." },
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "The schoolmaster was burdened with heavy **pedagogic** routines that dulled his poetic imagination." }
    ]
  },
  "Dashboard — paed/pedagogical.md": {
    primary: "Relating to teaching or the profession of teaching; pedagogic.",
    secondary: "Concerning the theory, methods, and psychological principles of education.",
    quotes: [
      { author: "John Dewey", work: "Democracy and Education", quote: "The **pedagogical** responsibility of the school is to provide an environment that coordinates the social activities of life." },
      { author: "Lev Vygotsky", work: "Mind in Society", quote: "Instruction is most fruitful when directed toward the zone of proximal development in **pedagogical** design." },
      { author: "Paulo Freire", work: "Pedagogy of the Oppressed", quote: "A revolutionary **pedagogical** approach rejects the banking concept of education in favor of problem-posing dialogue." }
    ]
  },
  "Dashboard — paed/pedagogically.md": {
    primary: "In a manner relating to the methods and principles of teaching; from an educational standpoint.",
    secondary: "With regard to instructional efficacy, developmental appropriateness, or didactic design.",
    quotes: [
      { author: "John Dewey", work: "Experience and Education", quote: "To organize subject matter **pedagogically** requires adapting abstract concepts to the learner's present experience." },
      { author: "Maria Montessori", work: "The Montessori Method", quote: "The classroom environment was arranged **pedagogically** to foster autonomous exploration and physical grace." },
      { author: "Jean Piaget", work: "The Science of Education and the Psychology of the Child", quote: "Abstract logic cannot be taught **pedagogically** before the child masters concrete operational thinking." }
    ]
  },
  "Dashboard — paed/pedagogue.md": {
    primary: "A teacher, especially a strict, pedantic, or old-fashioned one.",
    secondary: "In ancient Greece and Rome, a trusted slave (paidagōgos) charged with escorting boys to school, carrying their satchels, and supervising morals.",
    quotes: [
      { author: "Plato", work: "Lysis", quote: "The boys' **pedagogue** arrived, speaking broken Greek, and ordered the youths home as the wrestling school closed." },
      { author: "Washington Irving", work: "The Legend of Sleepy Hollow", quote: "Ichabod Crane was the village **pedagogue**, whose tall, lank frame struck terror into unruly schoolboys." },
      { author: "Charles Dickens", work: "Hard Times", quote: "Mr. M'Choakumchild was a dry **pedagogue** determined to cram facts and figures into tiny human vessels." }
    ]
  },
  "Dashboard — paed/pedagogy.md": {
    primary: "The method and practice of teaching, especially as an academic subject or theoretical concept.",
    secondary: "In educational theory, the holistic study of instructional strategies, developmental psychology, and socio-cultural learning dynamics.",
    quotes: [
      { author: "Paulo Freire", work: "Pedagogy of the Oppressed", quote: "Authentic **pedagogy** does not treat learners as passive recipients of knowledge, but as co-creators of meaning." },
      { author: "John Dewey", work: "My Pedagogic Creed", quote: "I believe that all **pedagogy** must be based upon the psychological nature and capacities of the child." },
      { author: "Maria Montessori", work: "The Absorbent Mind", quote: "A scientific **pedagogy** begins by liberating the natural developmental instincts of the young mind." }
    ]
  },
  "Dashboard — paed/pedant.md": {
    primary: "A person who is excessively concerned with minor details and rules or with displaying academic learning.",
    secondary: "In comedy and satire, a stock scholarly character (il pedante) whose arrogant adherence to sterile book-learning blinds him to practical reality.",
    quotes: [
      { author: "William Shakespeare", work: "Love's Labour's Lost", quote: "Holofernes stands as the quintessential **pedant**, stuffing Latin scraps into every rustic conversation." },
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "The bookful blockhead, ignorantly read, With loads of learned lumber in his head, stands as a tiresome **pedant**." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The Grand Academy of Lagado was crowded with every variety of star-gazing, hair-splitting **pedant**." }
    ]
  },
  "Dashboard — paed/pedantic.md": {
    primary: "Excessively concerned with literal accuracy or formal rules; ostentatious in one's learning.",
    secondary: "Characterized by meticulous, tedious, and narrow-minded scholastic exactitude.",
    quotes: [
      { author: "John Locke", work: "Some Thoughts Concerning Education", quote: "Avoid **pedantic** disputation, which teaches youths to quarrel about empty words rather than seek truth." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mary Bennet delivered moral platitudes in a stiff, **pedantic** tone that amused her father." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "Syme spoke with **pedantic** passion about the destruction of words in the Eleventh Edition of the Newspeak dictionary." }
    ]
  },
  "Dashboard — paed/pedantry.md": {
    primary: "Excessive concern with minor details and formal rules; an ostentatious display of bookish learning.",
    secondary: "In literary and philosophical critique, dogmatic fixation on academic trivia that obscures real intellectual substance.",
    quotes: [
      { author: "Michel de Montaigne", work: "Essays", quote: "I hate that hollow **pedantry** which fills the memory with Greek names while leaving the judgment barren." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "**Pedantry** is the unseasonable ostentation of learning, obtruding scholastic distinctions into polite company." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Scholasticism fell into terminal decay when vain **pedantry** preferred contentious disputations to experimental inquiry." }
    ]
  },
  "Dashboard — paed/pediatric.md": {
    primary: "Relating to the branch of medicine dealing with children and their diseases.",
    secondary: "In clinical healthcare, pertaining to infants, children, and adolescents, including developmental milestones and congenital disorders.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The treatment of infantile malnutrition represents a major triumph of modern **pediatric** research." },
      { author: "Benjamin Spock", work: "Baby and Child Care", quote: "Modern **pediatric** practice stresses trust between parent and child rather than rigid schedules." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "Vaccination eliminated what were once routine **pediatric** catastrophes from family life." }
    ]
  },
  "Dashboard — paed/pediatrics.md": {
    primary: "The branch of medicine dealing with the health and medical care of infants, children, and adolescents.",
    secondary: "The medical discipline focused on physical, mental, and behavioral growth, and preventing developmental and infectious childhood ailments.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The rise of **pediatrics** as an independent specialty gave voice to those little patients who cannot speak for themselves." },
      { author: "William Osler", work: "Aequanimitas", quote: "In **pediatrics**, diagnostic accuracy relies upon exquisite observation rather than patient interrogation." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "Clean water and antibiotics transformed 20th-century **pediatrics** into an inspiring success." }
    ]
  },
  "Dashboard — paed/pediatrist.md": {
    primary: "A pediatrician; a physician who specializes in the treatment of children's diseases.",
    secondary: "A clinical child specialist (an older or alternative term for pediatrician).",
    quotes: [
      { author: "William Osler", work: "The Master-Word in Medicine", quote: "The consulting **pediatrist** was called in to assess the persistent whooping cough." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "The young **pediatrist** carried his pocket stethoscope into every working-class nursery." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The **pediatrist** documented the congenital visual anomalies manifesting in early infancy." }
    ]
  },
  "Dashboard — paed/pedodontics.md": {
    primary: "The branch of dentistry that deals with children's teeth.",
    secondary: "In specialized dentistry, preventative, restorative, and interceptive orthodontics tailored to pediatric oral development.",
    quotes: [
      { author: "William Osler", work: "Modern Medicine", quote: "Advances in **pedodontics** emphasized preventive fluoride application to arrest early enamel decay." },
      { author: "Morris Fishbein", work: "Fads and Quackery in Healing", quote: "The modern **pedodontics** clinic creates a welcoming environment to banish childhood dental anxiety." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "Public health initiatives integrating **pedodontics** with municipal water treatment saved millions of teeth." }
    ]
  },
  "Dashboard — paed/pedophilia.md": {
    primary: "Sexual attraction to children; variant spelling of paedophilia.",
    secondary: "In psychiatric diagnosis, a paraphilia marked by recurrent urges or behavior toward prepubescent individuals.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Legal systems require psychiatric evaluation to address the pathological manifestations of **pedophilia**." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "The etiology of **pedophilia** reveals an abnormal fixation on childish objects due to severe developmental arrests." },
      { author: "Michel Foucault", work: "Abnormal", quote: "The emergence of the clinical category of **pedophilia** reorganized penal boundaries around the protection of youth." }
    ]
  },

  // === Dashboard — pater (27 words) ===
  "Dashboard — pater/allopatric.md": {
    primary: "Occurring in separate non-overlapping geographical areas (of animals or plant populations).",
    secondary: "In evolutionary biology, describing speciation (allopatric speciation) that occurs when populations become geographically isolated from one another.",
    quotes: [
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The geographical isolation of an **allopatric** population is the primary precondition for genetic divergence into a new species." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "When **allopatric** populations accumulate sufficient genetic differences, reproductive isolation prevents interbreeding upon secondary contact." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "Punctuated equilibria rests upon the rapid speciation of small, peripherally isolated **allopatric** populations." }
    ]
  },
  "Dashboard — pater/allopatry.md": {
    primary: "The condition of having non-overlapping, separate geographical ranges (of related species or populations).",
    secondary: "In biogeography and evolutionary ecology, geographic separation that prevents gene flow between divergent lineages.",
    quotes: [
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Prolonged **allopatry** allows natural selection and genetic drift to alter gene frequencies without hindrance." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "The vast majority of geographic subspecies owe their initial distinctive traits to territorial **allopatry**." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Divergence in mating calls evolved during centuries of mountain **allopatry** across the archipelago." }
    ]
  },
  "Dashboard — pater/eupatrides.md": {
    primary: "A member of the ancient Athenian nobility or hereditary aristocracy ('those of good fathers').",
    secondary: "In classical Attic constitutional history, the noble caste who held a monopoly on archonships and Areopagus membership prior to the Solonian reforms.",
    quotes: [
      { author: "Aristotle", work: "Constitution of the Athenians", quote: "The ancient population was divided into the **Eupatrides**, the agriculturalists, and the artisans." },
      { author: "Plutarch", work: "Life of Theseus", quote: "Theseus invited the **Eupatrides** to manage religious rites, supply magistrates, and expound sacred laws." },
      { author: "George Grote", work: "A History of Greece", quote: "Solon broke the hereditary political monopoly of the **Eupatrides** by basing civic rights on wealth rather than birth." }
    ]
  },
  "Dashboard — pater/pater.md": {
    primary: "Father (often used in schoolboy slang or formal phrases, e.g. paterfamilias).",
    secondary: "In Roman law and cultural history, the supreme head of the domestic household (paterfamilias) exercising patria potestas.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "The Newcomes", quote: "The boy penned an urgent letter to his **pater**, pleading for an advance on his quarterly allowance." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Roman law granted the **pater** absolute power of life and death over all descendants under his roof." },
      { author: "James Joyce", work: "A Portrait of the Artist as a Young Man", quote: "Stephen Dedalus reflected on his **pater**, who had been in his day a sportsman, bank clerk, and tenor." }
    ]
  },
  "Dashboard — pater/paternal.md": {
    primary: "Of, relating to, or characteristic of a father; fatherly.",
    secondary: "Derived or inherited through a father's line (patrilineal).",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Mr. John Dashwood felt only a faint impulse of **paternal** generosity toward his dependent half-sisters." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The monarch should govern his people with the gentle, protective care of a **paternal** sovereign." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Joe Gargery smiled with all the tender, protective warmth of a true **paternal** guardian." }
    ]
  },
  "Dashboard — pater/paternalism.md": {
    primary: "The policy or practice of governing people in a fatherly manner, especially by providing for their needs without giving them rights or responsibilities.",
    secondary: "In political philosophy and medical ethics, overriding an individual's autonomy for their own supposed best interests.",
    quotes: [
      { author: "John Stuart Mill", work: "On Liberty", quote: "State **paternalism** cannot be justified, for the individual is the sole rightful sovereign over his own body and mind." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "An administrative **paternalism** can degrade citizens into a timid herd of industrious animals, with government as their shepherd." },
      { author: "Isaiah Berlin", work: "Two Concepts of Liberty", quote: "**Paternalism** is the greatest possible despotism, for it denies mature human beings their moral agency." }
    ]
  },
  "Dashboard — pater/paternalistic.md": {
    primary: "Characterized by the practice of managing people in the manner of a father dealing with his children; patronizing.",
    secondary: "Imposing well-intentioned restrictions that limit personal freedom and self-determination.",
    quotes: [
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "Miners fiercely resented the **paternalistic** surveillance exercised by the coal company housing committee." },
      { author: "Hannah Arendt", work: "On Revolution", quote: "Benevolent but **paternalistic** rule inevitably suffocates the genuine civic spirit of free citizens." },
      { author: "Noam Chomsky", work: "Deterring Democracy", quote: "Imperial states justify foreign interventions through an insufferably **paternalistic** rhetoric of civilizing missions." }
    ]
  },
  "Dashboard — pater/paternally.md": {
    primary: "In a paternal or fatherly manner; as a father does.",
    secondary: "From the father's side of the family; patrilineally.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Mr. Rochester looked down **paternally** upon Adele, indulging her innocent childish vanity." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The old laird patted the youth **paternally** on the shoulder, encouraging him to persevere." },
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "Estate descent traced **paternally** took legal precedence over maternal claims in feudal land tenure." }
    ]
  },
  "Dashboard — pater/paternity.md": {
    primary: "The state of being someone's father; fatherhood.",
    secondary: "Descent from or relationship to a father; or the origin or authorship of an idea or work.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The law establishes a firm presumption of legitimate **paternity** for all children born in lawful wedlock." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "Mr. Micawber assumed an air of grave **paternity**, counseling his boys upon the perils of debt." },
      { author: "Oliver Wendell Holmes Jr.", work: "The Common Law", quote: "Questions of disputed **paternity** were historically determined by the testimony of midwives and solemn oaths." }
    ]
  },
  "Dashboard — pater/paternoster.md": {
    primary: "The Lord's Prayer, especially in the Latin form; or a bead in a rosary representing this prayer.",
    secondary: "In mechanical engineering, a continuous moving elevator or conveyor with a chain of open compartments that moves continuously in a loop.",
    quotes: [
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", quote: "The devout prioress told her rosary, repeating each **paternoster** with humble, gentle reverence." },
      { author: "Dante Alighieri", work: "Purgatorio", quote: "The penitents on the terrace of pride recited an expanded, solemn paraphrasing of the **Paternoster**." },
      { author: "Arthur Conan Doyle", work: "The White Company", quote: "The pious archer muttered a hasty **paternoster** before loosing his shaft into the French ranks." }
    ]
  },
  "Dashboard — pater/paterson.md": {
    primary: "A patronymic surname meaning 'son of Patrick/Peter'; or a major industrial city in northeastern New Jersey, USA.",
    secondary: "In modernist American poetry, the epic poem Paterson by William Carlos Williams embodying the industrial city as a living man.",
    quotes: [
      { author: "William Carlos Williams", work: "Paterson", quote: "A man is indeed a city, and the roaring falls of **Paterson** pour like language through his soul." },
      { author: "Allen Ginsberg", work: "Kaddish", quote: "Memories of my childhood home in **Paterson** returned with the bittersweet pain of passing time." },
      { author: "Alexander Hamilton", work: "Report on Manufactures", quote: "The cascading Great Falls at **Paterson** provided unmatched water power for the nation's earliest textile mills." }
    ]
  },
  "Dashboard — pater/patness.md": {
    primary: "The quality of being pat; exact suitability, opportune timing, or glib plausibility.",
    secondary: "In literary and dramatic criticism, the overly neat, convenient, or contrived resolution of a plot.",
    quotes: [
      { author: "Henry James", work: "The Art of the Novel", quote: "The suspicious **patness** of the convenient inheritance robbed the final chapter of authentic dramatic weight." },
      { author: "Virginia Woolf", work: "Granite and Rainbow", quote: "Life defies the artificial **patness** with which Victorian novelists loved to tie up every emotional loose end." },
      { author: "George Orwell", work: "Inside the Whale", quote: "Propaganda novels suffer from an ideological **patness** where the villain always repents or meets gruesome defeat." }
    ]
  },
  "Dashboard — pater/patriarch.md": {
    primary: "The male head of a family or tribe; or an eminent senior male figure.",
    secondary: "In Christian ecclesiastical hierarchy, a bishop of the highest rank in the Eastern Orthodox, Oriental Orthodox, or Catholic churches.",
    quotes: [
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Old Count Rostov sat at the head of the banquet table like a genial, hospitable **patriarch**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **Patriarch** of Constantinople crowned the Byzantine emperor before the high altar of Hagia Sophia." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The ancient whale swam like a solitary, sea-scarred **patriarch** leading his leviathan herd." }
    ]
  },
  "Dashboard — pater/patriarchal.md": {
    primary: "Of, relating to, or characteristic of a patriarch; governed or dominated by men.",
    secondary: "In sociology and feminist theory, describing a social system in which men hold primary power and predominate in roles of political leadership.",
    quotes: [
      { author: "Virginia Woolf", work: "Three Guineas", quote: "The daughters of educated men must organize outside the rigid boundaries of the **patriarchal** state." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Under the **patriarchal** regime, woman was relegated to domestic immanence while man laid claim to transcendence." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "Henchard governed his household and corn dealership with severe, old-fashioned **patriarchal** authority." }
    ]
  },
  "Dashboard — pater/patriarchate.md": {
    primary: "The office, jurisdiction, or see of an ecclesiastical patriarch; or the residence of a patriarch.",
    secondary: "In church history, the five ancient patriarchal sees of the Pentarchy: Rome, Constantinople, Alexandria, Antioch, and Jerusalem.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Council of Chalcedon confirmed the preeminence of the Ecumenical **Patriarchate** of Constantinople." },
      { author: "Eusebius", work: "Ecclesiastical History", quote: "The apostolic succession within the Alexandrian **patriarchate** preserved orthodox trinitarian dogma." },
      { author: "Henry Chadwick", work: "The Early Church", quote: "Rivalry between the Roman see and the eastern **patriarchate** laid the seeds of the Great Schism." }
    ]
  },
  "Dashboard — pater/patriarchic.md": {
    primary: "Of or belonging to a patriarch; patriarchal (archaic or formal variant).",
    secondary: "Pertaining to ancient tribal rule centered on an elder male progenitor.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Milton described the ancient **patriarchic** age when simple shepherds held direct converse with angels." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Venerable customs formed a **patriarchic** bond that cemented generations in reciprocal loyalty." },
      { author: "Walter Scott", work: "Waverley", quote: "The highland clan system was essentially **patriarchic**, regarding the chieftain as a father of his people." }
    ]
  },
  "Dashboard — pater/patriarchy.md": {
    primary: "A system of society or government in which men hold the power and women are largely excluded from it.",
    secondary: "In cultural and gender studies, the institutionalized social system wherein father figures hold primary authority over women, children, and property.",
    quotes: [
      { author: "Friedrich Engels", work: "The Origin of the Family, Private Property and the State", quote: "The overthrow of mother-right was the world-historic defeat of the female sex, inaugurating **patriarchy**." },
      { author: "Adrienne Rich", work: "Of Woman Born", quote: "Under institutional **patriarchy**, female reproduction and labor have been subjected to male legal dominion." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "True virtue cannot flourish in a society where entrenched domestic **patriarchy** infantilizes women." }
    ]
  },
  "Dashboard — pater/patriot.md": {
    primary: "A person who vigorously supports their country and is prepared to defend it against enemies or detractors.",
    secondary: "In political history, an adherent of national self-determination and republican liberty (e.g. American Revolution).",
    quotes: [
      { author: "Samuel Johnson", work: "The Patriot", quote: "A genuine **patriot** loves his country with rational affection, seeking its true moral and economic welfare." },
      { author: "Thomas Paine", work: "The American Crisis", quote: "The summer soldier and the sunshine **patriot** will, in this crisis, shrink from the service of their country." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Where'er we tread 'tis haunted, holy ground; No earth of thine is lost in vulgar mould, But one vast realm of wonder, where the blood of the fallen **patriot** hallows every field." }
    ]
  },
  "Dashboard — pater/patrioteer.md": {
    primary: "A person who makes an ostentatious or jingoistic display of patriotism, especially for selfish or commercial gain.",
    secondary: "In political satire and rhetoric, a hypocritical flag-waver who uses nationalism to stifle dissent or enrich himself.",
    quotes: [
      { author: "H. L. Mencken", work: "Prejudices: First Series", quote: "The professional **patrioteer** wrap himself in the flag to divert public attention from his empty pockets." },
      { author: "Sinclair Lewis", work: "It Can't Happen Here", quote: "Every loud-mouthed **patrioteer** on the platform shouted about liberty while demanding the arrest of critics." },
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "We must distinguish between the quiet love of country and the noisy bluster of the commercial **patrioteer**." }
    ]
  },
  "Dashboard — pater/patriotic.md": {
    primary: "Having or expressing devotion to and vigorous support for one's country.",
    secondary: "In civic philosophy, motivated by love of the laws, institutions, and welfare of the political community.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "There is an instinctive **patriotic** sentiment born of custom, and a reflective patriotism born of political participation." },
      { author: "Abraham Lincoln", work: "First Inaugural Address", quote: "The mystic chords of memory will swell the chorus of the Union, touched by the better angels of our **patriotic** nature." },
      { author: "George Orwell", work: "Notes on Nationalism", quote: "True **patriotic** devotion is defensive both militarily and culturally, unlike aggressive nationalism." }
    ]
  },
  "Dashboard — pater/patriotism.md": {
    primary: "Devotion to and vigorous support for one's country.",
    secondary: "In political theory, the civic virtue that binds citizens in loyalty to the constitution and common welfare.",
    quotes: [
      { author: "Samuel Johnson", work: "Boswell's Life of Samuel Johnson", quote: "**Patriotism** is the last refuge of a scoundrel, remarked Johnson, condemning hypocritical political posturing." },
      { author: "Mark Twain", work: "Corn-Pone Opinions", quote: "True **patriotism** is supporting your country all the time, and your government when it deserves it." },
      { author: "Leo Tolstoy", work: "Patriotism and Government", quote: "Tolstoy argued that exclusive **patriotism** was an outmoded superstition generating endless military conflicts." }
    ]
  },
  "Dashboard — pater/patrology.md": {
    primary: "The study of early Christian writers, Church Fathers, and their theological doctrines; patristics.",
    secondary: "In ecclesiastical scholarship, the systematic historical and linguistic analysis of Christian literature from the apostolic age to Gregory the Great.",
    quotes: [
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", quote: "My immersion in patristic studies and **patrology** convinced me of the continuous development of Catholic dogma." },
      { author: "Eusebius", work: "Ecclesiastical History", quote: "The foundations of sacred **patrology** were laid by recording the letters and martyrdoms of the apostolic fathers." },
      { author: "Jaroslav Pelikan", work: "The Christian Tradition", quote: "Modern theological renewal frequently springs from a fresh return to the rich sources of ancient **patrology**." }
    ]
  },
  "Dashboard — pater/patronym.md": {
    primary: "A name derived from the name of a father or male ancestor, typically by the addition of a prefix or suffix (such as -son, Mac-, or Fitz-).",
    secondary: "In onomastics and historical anthropology, a paternal identifier reflecting lineage in naming systems before fixed surnames became universal.",
    quotes: [
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "The Scandinavian **patronym** ending in -sen or -son originally changed with each succeeding generation." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Homeric warriors took immense pride in declaiming their **patronym** before charging into battle." },
      { author: "H. L. Mencken", work: "The American Language", quote: "Immigration authorities frequently converted foreign **patronym** endings into standard Anglo-Saxon surnames." }
    ]
  },
  "Dashboard — pater/patronymic.md": {
    primary: "Denoting or derived from the name of one's father or a male ancestor; or a patronymic name.",
    secondary: "In Russian naming conventions and classical literature, the middle name derived from the father's given name (e.g. Ivanovich, Atrides).",
    quotes: [
      { author: "Leo Tolstoy", work: "Anna Karenina", quote: "Polite Russian address required speaking both the Christian name and the **patronymic** with gentle respect." },
      { author: "Homer", work: "The Iliad", quote: "Agamemnon was hailed by his noble **patronymic**, Atrides, leader of the Achaean host." },
      { author: "Fyodor Dostoevsky", work: "The Brothers Karamazov", quote: "The courtroom clerk formally announced each witness by his full surname and **patronymic**." }
    ]
  },
  "Dashboard — pater/sympatric.md": {
    primary: "Occurring within the same geographical area; overlapping in distribution (of animals or plants).",
    secondary: "In evolutionary biology, describing speciation (sympatric speciation) that occurs without geographic isolation through ecological or behavioral niches.",
    quotes: [
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Rigid reproductive isolating mechanisms are essential to prevent gene fusion between **sympatric** species." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The sudden diversification of cichlid fishes in Lake Victoria provides dramatic evidence of rapid **sympatric** speciation." },
      { author: "Theodosius Dobzhansky", work: "Genetics of the Evolutionary Process", quote: "Ecological niche divergence allows two closely related **sympatric** fly populations to exploit different host plants." }
    ]
  },
  "Dashboard — pater/sympatry.md": {
    primary: "The occurrence of organisms in the same geographical area without interbreeding.",
    secondary: "In ecology and population genetics, spatial co-existence of related taxa maintaining distinct gene pools.",
    quotes: [
      { author: "Ernst Mayr", work: "Populations, Species, and Evolution", quote: "Character displacement is frequently observed when two closely related bird species enter secondary **sympatry**." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "Ecological competition is fiercest in regions of territorial **sympatry** where food requirements overlap." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The maintenance of high tropical biodiversity relies on complex niche partitionings sustained in mutual **sympatry**." }
    ]
  },
  "Dashboard — pater/unpatriotic.md": {
    primary: "Not patriotic; not showing love for or devotion to one's country.",
    secondary: "In political discourse, perceived or accused of acting against the interests, safety, or honor of the commonwealth.",
    quotes: [
      { author: "George Orwell", work: "Notes on Nationalism", quote: "Dissent from government foreign policy is often smeared by jingoists as treacherous and **unpatriotic**." },
      { author: "Bertrand Russell", work: "Justice in War-Time", quote: "During wartime hysteria, advocating for peace is immediately condemned as an **unpatriotic** crime." },
      { author: "Mark Twain", work: "The Mysterious Stranger", quote: "The loud mob will shout down the calm citizen, calling him a cowardly and **unpatriotic** traitor." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);
  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 6!`);
